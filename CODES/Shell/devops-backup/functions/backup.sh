#!/usr/bin/env bash

check_prerequisites() {
    local source_dir="$1"
    local nfs_mount="$2"
    local required_cmds=("tar" "gzip" "findmnt" "who" "awk" "cp" "sha256sum")

    log_message "INFO" "Running prerequisite checks..."

    # 1. Verify required commands are installed using a loop
    for cmd in "${required_cmds[@]}"; do
        if ! command -v "$cmd" >/dev/null 2>&1; then
            log_message "ERROR" "Required command '$cmd' is not installed."
            return 1
        fi
    done
    log_message "SUCCESS" "All required commands are available."

    # 2. Verify source directory exists and is readable
    if [[ ! -d "$source_dir" || ! -r "$source_dir" ]]; then
        log_message "ERROR" "Source directory '$source_dir' does not exist or is not readable."
        return 1
    fi
    log_message "SUCCESS" "Source directory '$source_dir' exists and is readable."

    # 3. Verify NFS destination is mounted and writable
    if ! findmnt -rn -M "$nfs_mount" >/dev/null 2>&1; then
        log_message "ERROR" "NFS destination '$nfs_mount' is not currently mounted."
        return 1
    fi

       local test_file="$nfs_mount/.write_test_$$"
    if ! touch "$test_file" 2>/dev/null; then
        log_message "WARNING" "NFS mount '$nfs_mount' is mounted, but current user lacks write permission."
        log_message "ERROR" "Cannot write to NFS destination '$nfs_mount'."
        return 1
    fi
    rm -f "$test_file"


    log_message "SUCCESS" "NFS destination '$nfs_mount' is mounted and writable."
    return 0
}

create_backup_filename() {
    local target_dir="$1"
    local current_user
    local current_host
    local current_date
    local normalized_path

    current_user="$(whoami)"
    current_host="$(hostname -s)"
    current_date="$(date '+%Y-%m-%d')"

    # Convert path such as /var/log into var-log
    normalized_path="${target_dir#/}"
    normalized_path="${normalized_path%/}"
    normalized_path="${normalized_path//\//-}"

    echo "${current_user}-on-${current_host}-${current_date}-${normalized_path}-backup.tar.gz"
}

create_archive() {
    local source_dir="$1"
    local staging_path="$2"

    log_message "INFO" "Creating compressed archive '$staging_path' from '$source_dir'..."

    # Some files inside /var/log (such as active journals) may rotate during archiving;
    # exit code 0 = clean, exit code 1 = warning/changed files, >=2 = real error.
    set +e
    tar -czf "$staging_path" -C / "${source_dir#/}" 2>/tmp/tar_backup.err
    local tar_exit=$?
    set -e

    if [[ "$tar_exit" -eq 0 ]]; then
        log_message "SUCCESS" "Archive created cleanly at '$staging_path'."
        rm -f /tmp/tar_backup.err
        return 0
    elif [[ "$tar_exit" -eq 1 ]]; then
        log_message "WARNING" "Archive created with minor file warnings: $(tr '\n' ' ' < /tmp/tar_backup.err)"
        rm -f /tmp/tar_backup.err
        return 0
    else
        log_message "ERROR" "Archive creation failed (exit code $tar_exit): $(tr '\n' ' ' < /tmp/tar_backup.err)"
        rm -f /tmp/tar_backup.err
        return 1
    fi
}

transfer_backup() {
    local source_file="$1"
    local dest_dir="$2"
    local dest_file="$dest_dir/$(basename "$source_file")"

    log_message "INFO" "Transferring '$source_file' to NFS share '$dest_file'..."

    if ! cp -p "$source_file" "$dest_file"; then
        log_message "ERROR" "Failed to copy backup archive to '$dest_file'."
        return 1
    fi

    if [[ ! -f "$dest_file" || ! -s "$dest_file" ]]; then
        log_message "ERROR" "Destination file '$dest_file' is missing or empty after transfer."
        return 1
    fi

    local src_sum dst_sum
    src_sum="$(sha256sum "$source_file" | awk '{print $1}')"
    dst_sum="$(sha256sum "$dest_file" | awk '{print $1}')"

    if [[ "$src_sum" != "$dst_sum" ]]; then
        log_message "ERROR" "Checksum mismatch between local archive and NFS copy."
        return 1
    fi

    log_message "SUCCESS" "Backup verified and transferred to '$dest_file' (SHA256 matched)."
    return 0
}
