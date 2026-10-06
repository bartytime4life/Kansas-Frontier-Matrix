#!/bin/bash
set -euo pipefail

service_label="com.kansasfrontiermatrix.local-qwen"
script_dir="$(cd "$(dirname "$0")" && pwd -P)"
user_home="${HOME:?HOME is required}"
agent_dir="$user_home/Library/LaunchAgents"
support_root="$user_home/Library/Application Support/Kansas Frontier Matrix/qwen-bridge-v1"
log_dir="$user_home/Library/Logs/Kansas Frontier Matrix"
plist_path="$agent_dir/$service_label.plist"
remove_logs=false

usage() {
  printf '%s\n' \
    "Usage: scripts/uninstall-local-qwen-macos.sh [--remove-logs]" \
    "" \
    "Stops and removes only the governed local Qwen bridge LaunchAgent." \
    "Ollama and its model are retained. Logs are retained unless requested."
}

for argument in "$@"; do
  case "$argument" in
    --remove-logs) remove_logs=true ;;
    --help|-h) usage; exit 0 ;;
    *) printf 'Unknown option: %s\n' "$argument" >&2; usage >&2; exit 2 ;;
  esac
done

if [[ "$(uname -s)" != "Darwin" ]]; then
  printf 'This uninstaller supports macOS only.\n' >&2
  exit 1
fi

if [[ "$UID" -eq 0 ]]; then
  printf 'Run this uninstaller as the signed-in macOS user, not with sudo.\n' >&2
  exit 1
fi

expected_support="$user_home/Library/Application Support/Kansas Frontier Matrix/qwen-bridge-v1"
if [[ "$support_root" != "$expected_support" || "$support_root" == "$user_home" || "$support_root" == "/" ]]; then
  printf 'Refusing to remove an unexpected support path.\n' >&2
  exit 1
fi

contract_path="$script_dir/qwen-local-contract.mjs"
node_bin="$(command -v node || true)"
if [[ -z "$node_bin" || ! -x "$node_bin" ]] && [[ -x "$support_root/bin/node" ]]; then
  node_bin="$support_root/bin/node"
fi
lsof_bin="$(command -v lsof || true)"
if [[ ! -f "$contract_path" || -z "$node_bin" || ! -x "$node_bin" || -z "$lsof_bin" || ! -x "$lsof_bin" ]]; then
  printf 'The governed bridge contract or macOS listener inspector is unavailable; no files were removed.\n' >&2
  exit 1
fi
bridge_port="$("$node_bin" --input-type=module -e '
  import { pathToFileURL } from "node:url";
  const contract = await import(pathToFileURL(process.argv[1]).href);
  const port = contract.QWEN_LOCAL_BRIDGE_PORT;
  if (!Number.isInteger(port) || port < 1 || port > 65535) process.exit(1);
  process.stdout.write(String(port));
' "$contract_path")"
if [[ ! "$bridge_port" =~ ^[0-9]+$ ]]; then
  printf 'The governed bridge port is invalid; no files were removed.\n' >&2
  exit 1
fi

if launchctl print "gui/$UID/$service_label" >/dev/null 2>&1; then
  if ! launchctl bootout "gui/$UID/$service_label" >/dev/null 2>&1; then
    printf 'The local Qwen companion could not be unloaded; no files were removed.\n' >&2
    exit 1
  fi
fi

unloaded=false
for _attempt in 1 2 3 4 5 6 7 8 9 10; do
  if ! launchctl print "gui/$UID/$service_label" >/dev/null 2>&1; then
    unloaded=true
    break
  fi
  sleep 0.25
done
if [[ "$unloaded" != true ]]; then
  printf 'The local Qwen companion is still registered; no files were removed.\n' >&2
  exit 1
fi

if pgrep -f "$support_root/scripts/local-qwen-bridge.mjs" >/dev/null 2>&1; then
  printf 'A local Qwen companion process is still running; no files were removed.\n' >&2
  exit 1
fi

listener_details="$("$lsof_bin" -nP -iTCP:"$bridge_port" -sTCP:LISTEN 2>/dev/null || true)"
if [[ -n "$listener_details" ]]; then
  printf 'A process is still listening on the governed local Qwen port; no files were removed:\n%s\n' "$listener_details" >&2
  exit 1
fi

rm -f "$plist_path"
rm -f \
  "$support_root/bin/node" \
  "$support_root/scripts/local-qwen-bridge.mjs" \
  "$support_root/scripts/qwen-local-contract.mjs" \
  "$support_root/app/qwen-context-safety.mjs"
rmdir "$support_root/bin" "$support_root/scripts" "$support_root/app" "$support_root" 2>/dev/null || true

if [[ "$remove_logs" == true ]]; then
  rm -f "$log_dir/qwen-bridge.log" "$log_dir/qwen-bridge.error.log"
  rmdir "$log_dir" 2>/dev/null || true
fi

printf 'Local Qwen bridge removed. Ollama and its model were left unchanged.\n'
