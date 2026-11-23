#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FUNCTIONS_DIR="$SCRIPT_DIR/functions"

# Source required function libraries
# shellcheck source=functions/logging.sh
source "$FUNCTIONS_DIR/logging.sh"
# shellcheck source=functions/backup.sh
source "$FUNCTIONS_DIR/backup.sh"

SOURCE_DIR="${1:-/var/log}"
NFS_MOUNT="${2:-/mnt/nfs_shared}"
STAGING_DIR="/tmp/devops-backup-staging"
export LOG_FILE="/var/log/devops-backup/backup.log"

cleanup() {
    rm -rf "$STAGING_DIR"
}
trap cleanup EXIT

main() {
    mkdir -p "$STAGING_DIR"

    log_message "INFO" "=== Starting NFS Backup Automation Job ==="
    list_logged_in_users

    if ! check_prerequisites "$SOURCE_DIR" "$NFS_MOUNT"; then
        log_message "ERROR" "Prerequisite check failed. Aborting backup job."
        exit 1
    fi

    local archive_name
    archive_name="$(create_backup_filename "$SOURCE_DIR")"
    local staged_archive="$STAGING_DIR/$archive_name"

    log_message "INFO" "Generated dynamic backup filename: $archive_name"

    if ! create_archive "$SOURCE_DIR" "$staged_archive"; then
        log_message "ERROR" "Backup archiving failed. Aborting transfer."
        exit 1
    fi

    if ! transfer_backup "$staged_archive" "$NFS_MOUNT"; then
        log_message "ERROR" "Transfer to NFS share failed."
        exit 1
    fi

    log_message "SUCCESS" "=== Backup and NFS transfer completed successfully ==="
}

main "$@"
