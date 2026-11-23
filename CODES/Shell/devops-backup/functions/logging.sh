#!/usr/bin/env bash
set -euo pipefail

log_message() {
    local level="$1"
    local message="$2"
    local log_file="${LOG_FILE:-/var/log/devops-backup/backup.log}"
    local timestamp
    timestamp="$(date '+%Y-%m-%d %H:%M:%S')"

    local formatted_entry="[$timestamp] [$level] $message"

    mkdir -p "$(dirname "$log_file")"
    echo "$formatted_entry" | tee -a "$log_file"
}

list_logged_in_users() {
    log_message "INFO" "Checking currently logged-in users..."

    local active_users
    #Best of Both Worlds (Portable Approach)
    if command -v loginctl >/dev/null 2>&1 && [[ -d /run/systemd/system ]]; then
        active_users="$(loginctl list-sessions --no-legend | awk '{print $3 " (" $5 ", " $4 ")"}' | sort -u)"
    else
        active_users="$(who | awk '{print $1 " (" $2 ", " $5 ")"}' | sort -u)"
    fi
    #END

    if [[ -z "$active_users" ]]; then
        active_users="$(whoami) (current shell)"
    fi

    echo "Currently logged-in users:"
    while IFS= read -r session_info; do
        [[ -n "$session_info" ]] || continue
        echo "  - $session_info"
        log_message "INFO" "Active user session: $session_info"
    done <<< "$active_users" # Here string
    # The <<< operator feeds the multi-line text inside $active_users directly into the while loop 
    # as standard input—just like feeding a file into a loop, without needing to create a temporary file. (This is also a Bash-specific feature).
}
