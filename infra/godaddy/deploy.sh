#!/usr/bin/env bash
# Mirror the built public-site bundle to GoDaddy (cPanel) web hosting.
#
# Uses lftp over SFTP (preferred) or explicit FTPS. Credentials come only from
# the environment; nothing is written to the repository. The remote document
# root keeps cPanel-owned paths (AutoSSL validation, cgi-bin, .user.ini).
#
# Required environment:
#   GODADDY_HOST          SFTP/FTP host name (for example the cPanel server name)
#   GODADDY_USER          cPanel / FTP account user name
#   one of:
#     GODADDY_SSH_KEY       private key text (SFTP only; preferred)
#     GODADDY_PASSWORD      account or FTP password
# Required for SFTP:
#   GODADDY_KNOWN_HOSTS   output of `ssh-keyscan -p PORT HOST` (host key pin)
# Optional:
#   GODADDY_PROTOCOL      sftp (default) | ftps
#   GODADDY_PORT          default 22 for sftp, 21 for ftps
#   GODADDY_REMOTE_DIR    default public_html
#   GODADDY_DELETE        true to remove remote files absent from the bundle (default false)
#   DRY_RUN               true to list changes without transferring (default false)
#   SITE_DIR              bundle directory (default apps/public-site/dist)

set -euo pipefail

die() { echo "deploy: $*" >&2; exit 1; }

SITE_DIR="${SITE_DIR:-apps/public-site/dist}"
PROTOCOL="${GODADDY_PROTOCOL:-sftp}"
REMOTE_DIR="${GODADDY_REMOTE_DIR:-public_html}"
DELETE="${GODADDY_DELETE:-false}"
DRY_RUN="${DRY_RUN:-false}"

[[ -n "${GODADDY_HOST:-}" ]] || die "GODADDY_HOST is not set"
[[ -n "${GODADDY_USER:-}" ]] || die "GODADDY_USER is not set"
[[ -f "$SITE_DIR/index.html" && -f "$SITE_DIR/.htaccess" ]] || die "no built bundle in $SITE_DIR"
[[ "$GODADDY_HOST" =~ ^[A-Za-z0-9.-]+$ ]] || die "GODADDY_HOST must be a bare host name"
[[ "$REMOTE_DIR" =~ ^[A-Za-z0-9._/-]+$ && "$REMOTE_DIR" != *..* ]] || die "GODADDY_REMOTE_DIR has unsafe characters"
command -v lftp >/dev/null || die "lftp is not installed"

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
chmod 700 "$work"

settings="set cmd:fail-exit true; set net:max-retries 3; set net:timeout 30;"
case "$PROTOCOL" in
  sftp)
    PORT="${GODADDY_PORT:-22}"
    [[ -n "${GODADDY_KNOWN_HOSTS:-}" ]] || die "GODADDY_KNOWN_HOSTS is required for sftp (run: ssh-keyscan -p $PORT $GODADDY_HOST)"
    printf '%s\n' "$GODADDY_KNOWN_HOSTS" > "$work/known_hosts"
    ssh_cmd="ssh -a -x -o BatchMode=yes -o StrictHostKeyChecking=yes -o UserKnownHostsFile=$work/known_hosts"
    if [[ -n "${GODADDY_SSH_KEY:-}" ]]; then
      printf '%s\n' "$GODADDY_SSH_KEY" > "$work/id_key"
      chmod 600 "$work/id_key"
      ssh_cmd="$ssh_cmd -o IdentitiesOnly=yes -i $work/id_key"
      export LFTP_PASSWORD="unused"
    else
      [[ -n "${GODADDY_PASSWORD:-}" ]] || die "set GODADDY_SSH_KEY or GODADDY_PASSWORD"
      ssh_cmd="${ssh_cmd/BatchMode=yes/BatchMode=no}"
      export LFTP_PASSWORD="$GODADDY_PASSWORD"
    fi
    settings="$settings set sftp:auto-confirm no; set sftp:connect-program \"$ssh_cmd\";"
    url="sftp://$GODADDY_HOST:$PORT"
    ;;
  ftps)
    PORT="${GODADDY_PORT:-21}"
    [[ -n "${GODADDY_PASSWORD:-}" ]] || die "GODADDY_PASSWORD is required for ftps"
    export LFTP_PASSWORD="$GODADDY_PASSWORD"
    settings="$settings set ftp:ssl-force true; set ftp:ssl-protect-data true; set ftp:ssl-protect-list true; set ssl:verify-certificate true; set ftp:passive-mode true;"
    url="ftp://$GODADDY_HOST:$PORT"
    ;;
  *) die "GODADDY_PROTOCOL must be sftp or ftps" ;;
esac

mirror="mirror --reverse --verbose --parallel=4 --no-perms"
mirror="$mirror --exclude-glob .well-known/acme-challenge/ --exclude-glob .well-known/pki-validation/"
mirror="$mirror --exclude-glob cgi-bin/ --exclude-glob .user.ini --exclude-glob .htpasswd"
[[ "$DELETE" == "true" ]] && mirror="$mirror --delete"
[[ "$DRY_RUN" == "true" ]] && mirror="$mirror --dry-run"

echo "deploy: $PROTOCOL to $GODADDY_HOST:$PORT/$REMOTE_DIR (delete=$DELETE, dry_run=$DRY_RUN)"
lftp --env-password -u "$GODADDY_USER" "$url" -e "$settings $mirror \"$SITE_DIR/\" \"$REMOTE_DIR/\"; bye"
echo "deploy: done"
