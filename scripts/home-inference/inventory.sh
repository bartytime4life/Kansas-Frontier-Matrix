#!/usr/bin/env bash
# Read-only inventory of the KFM inference PC (Phase 0 in docs/home-inference.md).
# It installs, changes and uploads nothing. Output includes hardware identifiers:
# save it privately and share only the lines a reviewer needs.
#   bash inventory.sh > ~/kfm-inference-inventory-$(date +%F).txt
set -u
section(){ printf '\n== %s ==\n' "$1"; }
have(){ command -v "$1" >/dev/null 2>&1; }

section "Recorded at"; date -u +%FT%TZ
section "Kernel and distribution"; uname -r; grep -E '^(PRETTY_NAME|VERSION_ID)=' /etc/os-release
section "CPU"; lscpu | grep -E '^(Model name|Architecture|CPU\(s\)|Thread|Core|Socket|Flags)' | sed -E 's/^(Flags:).*/\1 (avx2: '"$(grep -qw avx2 /proc/cpuinfo && echo yes || echo no)"', avx512f: '"$(grep -qw avx512f /proc/cpuinfo && echo yes || echo no)"')/'
section "Memory"; free -h
section "Disk (root and Ollama model store)"; df -h / ; [ -d /usr/share/ollama ] && df -h /usr/share/ollama
section "GPU"; (lspci 2>/dev/null | grep -Ei 'vga|3d|display') || echo "lspci unavailable"
if have nvidia-smi; then nvidia-smi --query-gpu=name,driver_version,memory.total,temperature.gpu,power.limit --format=csv; fi
if have rocm-smi; then rocm-smi --showproductname --showmeminfo vram 2>/dev/null; fi
section "Ollama"
if have ollama; then
  ollama --version; ollama list; ollama ps
  echo "service enabled: $(systemctl is-enabled ollama 2>/dev/null) active: $(systemctl is-active ollama 2>/dev/null)"
  systemctl show ollama -p Environment 2>/dev/null | tr ' ' '\n' | grep -E '^(Environment=)?OLLAMA_' || echo "no OLLAMA_* overrides set"
else echo "ollama not installed"; fi
section "Listeners on Ollama (11434) and gateway (8787)"
ss -ltnH 2>/dev/null | awk '$4 ~ /:(11434|8787)$/ {print $4}' | while read -r addr; do
  case "$addr" in 127.0.0.1:*|\[::1\]:*) echo "OK loopback $addr";; *) echo "WARNING not loopback-only: $addr";; esac
done
section "Gateway and tunnel services"
for unit in kfm-inference-gateway cloudflared; do echo "$unit enabled: $(systemctl is-enabled "$unit" 2>/dev/null || echo absent) active: $(systemctl is-active "$unit" 2>/dev/null)"; done
have node && echo "node $(node --version)" || echo "node not installed (gateway needs Node.js 22+)"
section "Power, sleep and uptime"
uptime -p; echo "last boot: $(uptime -s)"
for t in sleep.target suspend.target hibernate.target hybrid-sleep.target; do echo "$t: $(systemctl is-enabled "$t" 2>/dev/null)"; done
have sensors && sensors 2>/dev/null | grep -Ei 'package|tctl|edge|composite' | head -5
section "Network link type (no addresses printed)"
for dev in /sys/class/net/*; do n=${dev##*/}; [ "$n" = lo ] && continue
  kind=$([ -d "$dev/wireless" ] && echo wireless || echo wired/virtual); echo "$n $kind state=$(cat "$dev/operstate")"; done
section "Firewall"
if have ufw; then ufw status 2>/dev/null | head -3 || echo "ufw: run with sudo to read"; elif have firewall-cmd; then firewall-cmd --state 2>/dev/null; else echo "no ufw/firewalld found"; fi
printf '\nNot measured here: sustained upload/latency, power draw (kWh/day), thermals under load and recovery after power loss. See docs/home-inference.md.\n'
