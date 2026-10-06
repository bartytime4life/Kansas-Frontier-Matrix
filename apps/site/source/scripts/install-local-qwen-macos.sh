#!/bin/bash
set -euo pipefail

service_label="com.kansasfrontiermatrix.local-qwen"
script_dir="$(cd "$(dirname "$0")" && pwd -P)"
source_root="$(cd "$script_dir/.." && pwd -P)"
user_home="${HOME:?HOME is required}"
agent_dir="$user_home/Library/LaunchAgents"
support_root="$user_home/Library/Application Support/Kansas Frontier Matrix/qwen-bridge-v1"
installed_node="$support_root/bin/node"
log_dir="$user_home/Library/Logs/Kansas Frontier Matrix"
plist_path="$agent_dir/$service_label.plist"
pull_model=false

usage() {
  printf '%s\n' \
    "Usage: scripts/install-local-qwen-macos.sh [--pull-model]" \
    "" \
    "Installs the governed local Qwen bridge as a user LaunchAgent." \
    "--pull-model explicitly authorizes downloading the pinned model."
}

for argument in "$@"; do
  case "$argument" in
    --pull-model) pull_model=true ;;
    --help|-h) usage; exit 0 ;;
    *) printf 'Unknown option: %s\n' "$argument" >&2; usage >&2; exit 2 ;;
  esac
done

if [[ "$(uname -s)" != "Darwin" ]]; then
  printf 'This installer supports macOS only.\n' >&2
  exit 1
fi

if [[ "$UID" -eq 0 ]]; then
  printf 'Run this installer as the signed-in macOS user, not with sudo.\n' >&2
  exit 1
fi

node_bin="$(command -v node || true)"
if [[ -z "$node_bin" || ! -x "$node_bin" ]]; then
  printf 'Node.js is required before installing the local Qwen bridge.\n' >&2
  exit 1
fi
if ! "$node_bin" -e '
  const [major, minor] = process.versions.node.split(".").map(Number);
  process.exit(major > 22 || (major === 22 && minor >= 13) ? 0 : 1);
'; then
  printf 'Node.js 22.13.0 or newer is required for the local Qwen bridge.\n' >&2
  exit 1
fi

contract_path="$source_root/scripts/qwen-local-contract.mjs"
if [[ ! -f "$contract_path" ]]; then
  printf 'Required bridge contract is missing: %s\n' "$contract_path" >&2
  exit 1
fi
contract_values="$("$node_bin" --input-type=module -e '
  import { pathToFileURL } from "node:url";
  const contract = await import(pathToFileURL(process.argv[1]).href);
  const values = [
    contract.QWEN_LOCAL_MODEL,
    contract.QWEN_LOCAL_MODEL_DIGEST,
    contract.QWEN_LOCAL_OLLAMA_VERSION,
    contract.QWEN_LOCAL_OLLAMA_ORIGIN,
    contract.QWEN_LOCAL_BRIDGE_ORIGIN,
    contract.QWEN_LOCAL_SITE_ORIGIN,
  ];
  if (values.some((value) => typeof value !== "string" || !value || value.includes("\t"))) process.exit(1);
  process.stdout.write(values.join("\t"));
' "$contract_path")"
IFS=$'\t' read -r model_name model_digest ollama_version ollama_origin bridge_origin site_origin <<< "$contract_values"
if [[ -z "$model_name" || -z "$model_digest" || -z "$ollama_version" \
  || -z "$ollama_origin" || -z "$bridge_origin" || -z "$site_origin" ]]; then
  printf 'The local Qwen contract is incomplete. The bridge was not installed.\n' >&2
  exit 1
fi

ollama_bin="$(command -v ollama || true)"
if [[ -z "$ollama_bin" && -x /Applications/Ollama.app/Contents/Resources/ollama ]]; then
  ollama_bin="/Applications/Ollama.app/Contents/Resources/ollama"
fi
if [[ -z "$ollama_bin" || ! -x "$ollama_bin" ]]; then
  printf 'Ollama is not installed. Install and start Ollama, then run this installer again.\n' >&2
  exit 1
fi

ollama_cli() {
  env OLLAMA_HOST="$ollama_origin" "$ollama_bin" "$@"
}

if ! ollama_cli list >/dev/null 2>&1; then
  printf 'Ollama is installed but not running. Start Ollama, then run this installer again.\n' >&2
  exit 1
fi

ollama_port="${ollama_origin##*:}"
lsof_bin="$(command -v lsof || true)"
if [[ ! "$ollama_port" =~ ^[0-9]+$ || -z "$lsof_bin" || ! -x "$lsof_bin" ]]; then
  printf 'The Ollama port or macOS listener inspector is unavailable. The bridge was not installed.\n' >&2
  exit 1
fi
ollama_listeners="$("$lsof_bin" -nP -iTCP:"$ollama_port" -sTCP:LISTEN -Fpucn 2>/dev/null || true)"
if ! printf '%s\n' "$ollama_listeners" | "$node_bin" -e '
  const fs = require("node:fs");
  const [expectedUid, expectedPort] = process.argv.slice(1);
  const records = [];
  let current = null;
  for (const line of fs.readFileSync(0, "utf8").split(/\r?\n/)) {
    if (line.startsWith("p")) {
      current = { pid: line.slice(1), uid: "", names: [] };
      records.push(current);
    } else if (current && line.startsWith("u")) current.uid = line.slice(1);
    else if (current && line.startsWith("n")) current.names.push(line.slice(1).replace(/\s+\(LISTEN\)$/, ""));
  }
  const loopbackNames = new Set([`127.0.0.1:${expectedPort}`, `[::1]:${expectedPort}`, `::1:${expectedPort}`]);
  const safe = records.length > 0 && records.every((record) =>
    /^\d+$/.test(record.pid) && record.uid === expectedUid && record.names.length > 0
      && record.names.every((name) => loopbackNames.has(name))
  );
  process.exit(safe ? 0 : 1);
' "$UID" "$ollama_port"; then
  printf 'Ollama must have only current-user loopback listeners on port %s. Stop any wildcard, external, or foreign-user listener before installing.\n' "$ollama_port" >&2
  exit 1
fi

version_json="$(curl -sS --max-time 3 "$ollama_origin/api/version")"
if ! printf '%s' "$version_json" | "$node_bin" -e '
  const fs = require("node:fs");
  const expected = process.argv[1];
  const payload = JSON.parse(fs.readFileSync(0, "utf8"));
  process.exit(payload?.version === expected ? 0 : 1);
' "$ollama_version"; then
  printf 'Running Ollama does not match the test-pinned version %s. The bridge was not installed.\n' "$ollama_version" >&2
  exit 1
fi
if ! ollama_cli list | awk 'NR > 1 { print $1 }' | grep -Fxq "$model_name"; then
  if [[ "$pull_model" == true ]]; then
    ollama_cli pull "$model_name"
  else
    printf 'Pinned model %s is missing. Run `ollama pull %s`, or rerun with --pull-model.\n' "$model_name" "$model_name" >&2
    exit 1
  fi
fi

tags_json="$(curl -sS --max-time 3 "$ollama_origin/api/tags")"
if ! printf '%s' "$tags_json" | "$node_bin" -e '
  const fs = require("node:fs");
  const [name, expected] = process.argv.slice(1);
  const payload = JSON.parse(fs.readFileSync(0, "utf8"));
  const model = Array.isArray(payload.models) ? payload.models.find((item) => item?.name === name || item?.model === name) : null;
  const observed = typeof model?.digest === "string" ? (model.digest.startsWith("sha256:") ? model.digest : `sha256:${model.digest}`).toLowerCase() : "";
  process.exit(observed === expected ? 0 : 1);
' "$model_name" "$model_digest"; then
  printf 'Installed %s does not match the test-pinned digest %s. The bridge was not installed.\n' "$model_name" "$model_digest" >&2
  exit 1
fi

for required_file in \
  "$source_root/scripts/local-qwen-bridge.mjs" \
  "$source_root/scripts/qwen-local-contract.mjs" \
  "$source_root/app/qwen-context-safety.mjs"; do
  if [[ ! -f "$required_file" ]]; then
    printf 'Required bridge file is missing: %s\n' "$required_file" >&2
    exit 1
  fi
done

bridge_port="${bridge_origin##*:}"
if [[ ! "$bridge_port" =~ ^[0-9]+$ || -z "$lsof_bin" || ! -x "$lsof_bin" ]]; then
  printf 'The bridge port or macOS listener inspector is unavailable. The bridge was not installed.\n' >&2
  exit 1
fi

backup_dir="$(mktemp -d "${TMPDIR:-/tmp}/kfm-qwen-install.XXXXXX")"
preserve_backup=false
cleanup_backup() {
  if [[ "$preserve_backup" != true ]]; then rm -rf -- "$backup_dir"; fi
}
trap cleanup_backup EXIT
had_support=false
had_plist=false
previous_loaded=false
previous_disabled=false
if [[ -d "$support_root" ]]; then
  had_support=true
  mkdir -p "$backup_dir/support"
  cp -pR "$support_root/." "$backup_dir/support/"
fi
if [[ -f "$plist_path" ]]; then
  had_plist=true
  cp -p "$plist_path" "$backup_dir/previous.plist"
fi
if launchctl print "gui/$UID/$service_label" >/dev/null 2>&1; then previous_loaded=true; fi
if launchctl print-disabled "gui/$UID" 2>/dev/null | grep -Fq '"'"$service_label"'" => true'; then
  previous_disabled=true
fi

new_plist="$backup_dir/new.plist"
escape_plist_text() {
  "$node_bin" -e '
    process.stdout.write(process.argv[1]
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;"));
  ' "$1"
}
plist_node="$(escape_plist_text "$installed_node")"
plist_bridge="$(escape_plist_text "$support_root/scripts/local-qwen-bridge.mjs")"
plist_stdout="$(escape_plist_text "$log_dir/qwen-bridge.log")"
plist_stderr="$(escape_plist_text "$log_dir/qwen-bridge.error.log")"
cat > "$new_plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>$service_label</string>
  <key>ProgramArguments</key>
  <array>
    <string>$plist_node</string>
    <string>$plist_bridge</string>
  </array>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>ThrottleInterval</key><integer>10</integer>
  <key>StandardOutPath</key><string>$plist_stdout</string>
  <key>StandardErrorPath</key><string>$plist_stderr</string>
</dict>
</plist>
PLIST
chmod 0600 "$new_plist"
plutil -lint "$new_plist" >/dev/null

mutation_started=false
restore_previous_installation() {
  failure_status=$?
  if [[ "$failure_status" -eq 0 ]]; then failure_status=1; fi
  trap - ERR
  set +e
  if [[ "$mutation_started" != true ]]; then exit "$failure_status"; fi
  rollback_incomplete() {
    preserve_backup=true
    printf '%s Backup preserved at %s\n' "$1" "$backup_dir" >&2
  }
  rollback_unloaded=true
  if launchctl print "gui/$UID/$service_label" >/dev/null 2>&1; then
    rollback_unloaded=false
    if launchctl bootout "gui/$UID/$service_label" >/dev/null 2>&1; then
      for _rollback_stop_attempt in 1 2 3 4 5 6 7 8 9 10; do
        if ! launchctl print "gui/$UID/$service_label" >/dev/null 2>&1; then
          rollback_unloaded=true
          break
        fi
        sleep 0.25
      done
    fi
  fi
  if [[ "$rollback_unloaded" != true ]]; then
    rollback_incomplete 'Rollback is incomplete because the failed companion could not be unloaded; installed files were not overwritten again.'
    exit "$failure_status"
  fi
  if ! rm -f \
    "$support_root/bin/node" \
    "$support_root/scripts/local-qwen-bridge.mjs" \
    "$support_root/scripts/qwen-local-contract.mjs" \
    "$support_root/app/qwen-context-safety.mjs"; then
    rollback_incomplete 'Rollback is incomplete because refreshed runtime files could not be cleared.'
    exit "$failure_status"
  fi
  if [[ "$had_support" == true ]]; then
    if ! mkdir -p "$support_root" || ! cp -pR "$backup_dir/support/." "$support_root/"; then
      rollback_incomplete 'Rollback is incomplete because the prior runtime files could not be copied back.'
      exit "$failure_status"
    fi
  else
    rmdir "$support_root/bin" "$support_root/scripts" "$support_root/app" "$support_root" 2>/dev/null || true
    if [[ -e "$support_root" ]]; then
      rollback_incomplete 'Rollback is incomplete because the failed new runtime directory is not empty.'
      exit "$failure_status"
    fi
  fi
  if [[ "$had_plist" == true ]]; then
    if ! install -m 0600 "$backup_dir/previous.plist" "$plist_path" \
      || ! cmp -s "$backup_dir/previous.plist" "$plist_path"; then
      rollback_incomplete 'Rollback is incomplete because the prior LaunchAgent plist was not restored byte-for-byte.'
      exit "$failure_status"
    fi
  else
    if ! rm -f "$plist_path" || [[ -e "$plist_path" ]]; then
      rollback_incomplete 'Rollback is incomplete because the failed new LaunchAgent plist remains.'
      exit "$failure_status"
    fi
  fi
  if [[ "$had_support" == true ]] && ! diff -qr "$backup_dir/support" "$support_root" >/dev/null 2>&1; then
    rollback_incomplete 'Rollback is incomplete because the restored runtime differs from the preserved prior runtime.'
    exit "$failure_status"
  fi
  if [[ "$previous_disabled" == true && "$previous_loaded" != true ]] \
    && ! launchctl disable "gui/$UID/$service_label" >/dev/null 2>&1; then
    rollback_incomplete 'Rollback restored the prior files but could not restore the disabled LaunchAgent override.'
    exit "$failure_status"
  fi
  if [[ "$previous_loaded" == true && "$had_plist" == true ]]; then
    if ! launchctl enable "gui/$UID/$service_label" >/dev/null 2>&1; then
      rollback_incomplete 'Rollback restored the prior files but could not temporarily enable the prior LaunchAgent.'
      exit "$failure_status"
    fi
    rollback_loaded=false
    for _restore_attempt in 1 2 3 4 5 6 7 8 9 10; do
      if launchctl bootstrap "gui/$UID" "$plist_path" >/dev/null 2>&1; then
        rollback_loaded=true
        break
      fi
      sleep 0.5
    done
    if [[ "$rollback_loaded" != true ]]; then
      rollback_incomplete 'Previous companion files were restored, but macOS did not reload the prior LaunchAgent.'
      exit "$failure_status"
    fi
    rollback_ready=false
    rollback_health="$backup_dir/rollback-health.json"
    for _rollback_health_attempt in 1 2 3 4 5 6 7 8 9 10; do
      rollback_description="$(launchctl print "gui/$UID/$service_label" 2>/dev/null || true)"
      rollback_pid="$(printf '%s\n' "$rollback_description" | awk '/^[[:space:]]*pid = [0-9]+/ { print $3; exit }')"
      rollback_status="$(curl -sS --max-time 2 -o "$rollback_health" -w '%{http_code}' -H "Origin: $site_origin" "$bridge_origin/health" 2>/dev/null || true)"
      if [[ "$rollback_pid" =~ ^[0-9]+$ && "$rollback_status" == "200" ]] \
        && "$lsof_bin" -nP -a -p "$rollback_pid" -iTCP:"$bridge_port" -sTCP:LISTEN 2>/dev/null | grep -Fq "127.0.0.1:$bridge_port" \
        && "$node_bin" --input-type=module -e '
          import { readFileSync } from "node:fs";
          import { pathToFileURL } from "node:url";
          const contract = await import(pathToFileURL(process.argv[1]).href);
          const payload = JSON.parse(readFileSync(process.argv[2], "utf8"));
          process.exit(contract.localQwenHealthStatus(payload) === "ready" ? 0 : 1);
        ' "$support_root/scripts/qwen-local-contract.mjs" "$rollback_health"; then
        rollback_ready=true
        break
      fi
      sleep 0.5
    done
    if [[ "$rollback_ready" != true ]]; then
      rollback_incomplete 'Previous companion files and registration were restored, but governed health did not recover.'
      exit "$failure_status"
    fi
    if [[ "$previous_disabled" == true ]] \
      && ! launchctl disable "gui/$UID/$service_label" >/dev/null 2>&1; then
      rollback_incomplete 'The prior companion recovered, but its disabled-on-next-launch override could not be restored.'
      exit "$failure_status"
    fi
    printf 'The previous local Qwen companion was restored and passed governed health checks.\n' >&2
    exit "$failure_status"
  fi
  if [[ "$previous_loaded" == true ]]; then
    rollback_incomplete 'Previous companion files were restored, but its LaunchAgent plist was unavailable.'
  elif [[ "$had_support" == true || "$had_plist" == true ]]; then
    printf 'The previous local Qwen installation files were restored and remain unloaded.\n' >&2
  else
    printf 'The failed new local Qwen installation was removed; no previous installation existed.\n' >&2
  fi
  exit "$failure_status"
}
trap restore_previous_installation ERR

if [[ "$previous_loaded" == true ]]; then
  if ! launchctl bootout "gui/$UID/$service_label" >/dev/null 2>&1; then
    printf 'The existing local Qwen companion could not be unloaded; no files were replaced.\n' >&2
    false
  fi
  unloaded=false
  for _attempt in 1 2 3 4 5 6 7 8 9 10; do
    if ! launchctl print "gui/$UID/$service_label" >/dev/null 2>&1; then unloaded=true; break; fi
    sleep 0.25
  done
  if [[ "$unloaded" != true ]]; then
    printf 'The existing local Qwen companion did not stop; no refresh was retained.\n' >&2
    false
  fi
else
  launchctl bootout "gui/$UID/$service_label" >/dev/null 2>&1 || true
fi

mutation_started=true
mkdir -p "$agent_dir" "$support_root/bin" "$support_root/scripts" "$support_root/app" "$log_dir"
install -m 0755 "$node_bin" "$installed_node"
install -m 0644 "$source_root/scripts/local-qwen-bridge.mjs" "$support_root/scripts/local-qwen-bridge.mjs"
install -m 0644 "$source_root/scripts/qwen-local-contract.mjs" "$support_root/scripts/qwen-local-contract.mjs"
install -m 0644 "$source_root/app/qwen-context-safety.mjs" "$support_root/app/qwen-context-safety.mjs"
install -m 0600 "$new_plist" "$plist_path"
plutil -lint "$plist_path" >/dev/null
if ! "$installed_node" -e '
  const [major, minor] = process.versions.node.split(".").map(Number);
  process.exit(major > 22 || (major === 22 && minor >= 13) ? 0 : 1);
'; then
  printf 'The copied Node runtime failed its version check.\n' >&2
  false
fi

launchctl enable "gui/$UID/$service_label"
loaded=false
for _attempt in 1 2 3 4 5 6 7 8 9 10; do
  if launchctl bootstrap "gui/$UID" "$plist_path" >/dev/null 2>&1; then
    loaded=true
    break
  fi
  sleep 0.5
done
if [[ "$loaded" != true ]]; then
  printf 'macOS did not load the refreshed LaunchAgent.\n' >&2
  false
fi

ready=false
health_path="$backup_dir/health.json"
for _attempt in 1 2 3 4 5 6 7 8 9 10; do
  service_description="$(launchctl print "gui/$UID/$service_label" 2>/dev/null || true)"
  service_pid="$(printf '%s\n' "$service_description" | awk '/^[[:space:]]*pid = [0-9]+/ { print $3; exit }')"
  http_status="$(curl -sS --max-time 2 -o "$health_path" -w '%{http_code}' -H "Origin: $site_origin" "$bridge_origin/health" 2>/dev/null || true)"
  if [[ "$service_pid" =~ ^[0-9]+$ && "$http_status" == "200" ]] \
    && "$lsof_bin" -nP -a -p "$service_pid" -iTCP:"$bridge_port" -sTCP:LISTEN 2>/dev/null | grep -Fq "127.0.0.1:$bridge_port" \
    && "$installed_node" --input-type=module -e '
      import { readFileSync } from "node:fs";
      import { pathToFileURL } from "node:url";
      const contract = await import(pathToFileURL(process.argv[1]).href);
      const payload = JSON.parse(readFileSync(process.argv[2], "utf8"));
      process.exit(contract.localQwenHealthStatus(payload) === "ready" ? 0 : 1);
    ' "$support_root/scripts/qwen-local-contract.mjs" "$health_path"; then
    ready=true
    break
  fi
  sleep 0.5
done

if [[ "$ready" != true ]]; then
  printf 'The refreshed LaunchAgent failed its exact process and governed-health checks. Review %s.\n' "$log_dir/qwen-bridge.error.log" >&2
  false
fi

trap - ERR
printf 'Local Qwen bridge installed and ready on %s with %s.\n' "$bridge_origin" "$model_name"
