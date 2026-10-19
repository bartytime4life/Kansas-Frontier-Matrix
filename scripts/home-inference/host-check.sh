#!/usr/bin/env bash
# KFM home inference host check. READ-ONLY. Run after installation and after
# every reboot, Ollama update or configuration change:
#
#   sudo bash /opt/kfm-inference/host-check.sh
#
# sudo is only needed to read the firewall ruleset and the gateway self-check.
# Exit status is non-zero when any FAIL is reported.
set -u
export LC_ALL=C
failures=0
pass() { printf 'PASS  %s\n' "$1"; }
warn() { printf 'WARN  %s\n' "$1"; }
fail() { printf 'FAIL  %s\n' "$1"; failures=$((failures + 1)); }
have() { command -v "$1" >/dev/null 2>&1; }

listeners() { ss -Hltn "sport = :$1" 2>/dev/null | awk '{print $4}'; }
loopback_only() {
  local port=$1 name=$2 found
  found=$(listeners "$port")
  if [ -z "$found" ]; then fail "$name is not listening on port $port"; return; fi
  if echo "$found" | grep -Evq '^(127\.[0-9.]+|\[::1\]):'"$port"'$'; then
    fail "$name listens beyond loopback: $(echo "$found" | tr '\n' ' ')"
  else pass "$name listens on loopback only ($(echo "$found" | tr '\n' ' '))"; fi
}

have ss || { echo "ss (iproute2) is required"; exit 2; }

loopback_only 11434 "Ollama"
loopback_only 8787 "KFM gateway"

if have systemctl; then
  for unit in ollama kfm-inference-gateway; do
    [ "$(systemctl is-enabled "$unit" 2>/dev/null)" = enabled ] && pass "$unit starts at boot" || fail "$unit is not enabled at boot"
    [ "$(systemctl is-active "$unit" 2>/dev/null)" = active ] && pass "$unit is running" || fail "$unit is not running"
  done
  env=$(systemctl show ollama -p Environment 2>/dev/null)
  echo "$env" | grep -q 'OLLAMA_NO_CLOUD=1' && pass "Ollama local-only mode (OLLAMA_NO_CLOUD=1)" || fail "OLLAMA_NO_CLOUD=1 is not set for the Ollama service"
  echo "$env" | grep -q 'OLLAMA_HOST=127.0.0.1:11434' && pass "Ollama bound by configuration to 127.0.0.1:11434" || fail "OLLAMA_HOST is not pinned to 127.0.0.1:11434"
  for target in sleep.target suspend.target hibernate.target hybrid-sleep.target; do
    [ "$(systemctl is-enabled "$target" 2>/dev/null)" = masked ] || { warn "$target is not masked; the PC may suspend (sudo systemctl mask $target)"; break; }
  done
  if have timedatectl; then
    [ "$(timedatectl show -p NTPSynchronized --value 2>/dev/null)" = yes ] && pass "clock is NTP-synchronised" || fail "clock is not NTP-synchronised; signed requests will be refused"
  fi
fi

# Unsigned requests must be refused even from this machine.
if have curl; then
  code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 5 http://127.0.0.1:8787/v1/health)
  [ "$code" = 401 ] && pass "gateway refuses unsigned requests" || fail "unsigned gateway request returned HTTP $code (expected 401)"
  code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 5 http://127.0.0.1:8787/api/tags)
  [ "$code" = 401 ] && pass "gateway does not expose Ollama routes" || fail "gateway /api/tags returned HTTP $code (expected 401)"
fi

if [ "$(id -u)" -eq 0 ] && [ -f /opt/kfm-inference/gateway.mjs ]; then
  if KFM_GATEWAY_PROFILES=/etc/kfm-inference/profiles.json KFM_GATEWAY_KEYS=/etc/kfm-inference/gateway-keys.json \
     node /opt/kfm-inference/gateway.mjs --check >/tmp/kfm-gateway-check.$$ 2>&1; then
    pass "approved profile installed with the pinned digest"
  else fail "gateway self-check: $(tr -d '\n' </tmp/kfm-gateway-check.$$ | cut -c1-300)"; fi
  rm -f /tmp/kfm-gateway-check.$$
  perms=$(stat -c '%a %U' /etc/kfm-inference/gateway-keys.json 2>/dev/null)
  case "$perms" in 600\ root|400\ root) pass "gateway key file is root-only ($perms)";; *) fail "gateway key file permissions are '$perms' (expected 600 root)";; esac
  if have nft; then
    nft list ruleset 2>/dev/null | grep -Eq 'hook input .*policy drop' && pass "firewall drops unsolicited inbound traffic" || warn "no nftables input chain with policy drop found (ufw users: check 'ufw status verbose')"
  fi
else
  warn "run with sudo for the gateway self-check, key-file and firewall checks"
fi

if have nvidia-smi; then
  nvidia-smi --query-gpu=temperature.gpu,memory.used,memory.total --format=csv,noheader 2>/dev/null | sed 's/^/INFO  GPU temp, memory used, total: /'
fi

echo
[ "$failures" -eq 0 ] && echo "Host check passed." || echo "Host check: $failures failure(s)."
exit $((failures > 0))
