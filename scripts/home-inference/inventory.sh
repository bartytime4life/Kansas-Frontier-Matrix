#!/usr/bin/env bash
# KFM home inference PC inventory (phase 0). READ-ONLY: it installs, changes,
# downloads and opens nothing. Run as your normal user on the second Linux PC:
#
#   bash inventory.sh > ~/kfm-inventory-$(date +%F).txt
#
# MAC addresses, serial numbers, UUIDs and non-loopback IP addresses are
# redacted, but read the file before you share it.
set -u
export LC_ALL=C

have() { command -v "$1" >/dev/null 2>&1; }
redact() {
  # Handle IPv6 before MAC/IPv4 so mixed addresses and two-digit hextets cannot
  # be split into partially redacted fragments. Keep listener brackets/ports.
  sed -E \
    -e 's/[0-9a-fA-F:]*::[0-9a-fA-F:]*([0-9]{1,3}\.){3}[0-9]{1,3}/<ip6>/g' \
    -e 's/([0-9a-fA-F]{1,4}:){6}([0-9]{1,3}\.){3}[0-9]{1,3}/<ip6>/g' \
    -e 's/\[::1\]/@LOSIX@/g' -e 's/\[::\]/@ANYSIX@/g' -e 's/(^|[^0-9a-fA-F:])::1([^0-9a-fA-F:]|$)/\1@LOSIX@\2/g' \
    -e 's/([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}/<ip6>/g' \
    -e 's/[0-9a-fA-F:]*::[0-9a-fA-F:]*/<ip6>/g' \
    -e 's/([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}/<mac>/g' \
    -e 's/\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b/<uuid>/g' \
    -e 's/(Serial( Number)?|UUID|serial)[[:space:]]*[:=][[:space:]]*.*/\1: <redacted>/' \
    -e 's/\b0\.0\.0\.0\b/@ANY@/g' -e 's/\b127(\.[0-9]{1,3}){3}\b/@LO&@/g' \
    -e 's/\b([0-9]{1,3}\.){3}[0-9]{1,3}\b/<ip>/g' \
    -e 's/@ANY@/0.0.0.0/g' -e 's/@LO([0-9.]+)@/\1/g' -e 's/@LOSIX@/[::1]/g' -e 's/@ANYSIX@/[::]/g' \
    -e 's/((KEY|TOKEN|SECRET|PASSWORD)[A-Z_]*=)[^[:space:]]+/\1<redacted>/g'
}
section() { printf '\n== %s\n' "$1"; }
run() {
  # Bounded: a hung driver tool cannot stall the inventory.
  if have "$1"; then timeout 20 "$@" 2>&1 | redact; else echo "(not installed: $1)"; fi
}

echo "KFM home inference inventory — read-only — $(date -u +%FT%TZ)"
echo "Review before sharing. Nothing on this machine was changed."

section "Operating system"
uname -srm
grep -E '^(PRETTY_NAME|VERSION_ID|ID)=' /etc/os-release 2>/dev/null
have systemctl && echo "init: systemd $(systemctl --version | head -1 | awk '{print $2}')"
uptime -p 2>/dev/null

section "CPU"
if have lscpu; then
  lscpu | grep -E '^(Architecture|Model name|Socket\(s\)|Core\(s\) per socket|Thread\(s\) per core|CPU\(s\)|CPU max MHz|L3 cache)'
  # AVX2/AVX-512 decide CPU-only speed; report presence only, not the full flag list.
  for flag in avx2 avx512f avx512_bf16 amx_tile; do
    grep -qw "$flag" /proc/cpuinfo 2>/dev/null && echo "cpu flag: $flag"
  done
fi

section "Memory"
free -h
grep -E '^(MemTotal|SwapTotal)' /proc/meminfo
have swapon && swapon --show 2>/dev/null

section "Disk (models need room: plan 2-3x the largest model download)"
df -h / /var/lib /usr/share 2>/dev/null | awk '!seen[$0]++'
for dir in /usr/share/ollama/.ollama/models /var/lib/ollama "$HOME/.ollama/models"; do
  [ -d "$dir" ] && echo "ollama model store: $dir $(du -sh "$dir" 2>/dev/null | cut -f1)"
done
have lsblk && lsblk -d -o NAME,SIZE,ROTA,TRAN,MODEL 2>/dev/null | redact

section "GPU"
if have lspci; then lspci | grep -Ei 'vga|3d|display'; else echo "(lspci not installed: pciutils)"; fi
if have nvidia-smi; then
  run nvidia-smi --query-gpu=name,memory.total,driver_version,compute_cap,power.limit,temperature.gpu --format=csv
else echo "(nvidia-smi not installed)"; fi
if have rocm-smi; then run rocm-smi --showproductname --showmeminfo vram --showdriverversion; fi
ls /dev/dri 2>/dev/null | sed 's/^/dri: /'

section "Ollama"
if have ollama; then
  run ollama --version
  echo "-- installed models"; run ollama list
  echo "-- loaded models"; run ollama ps
else echo "(ollama not installed)"; fi
if have systemctl; then
  echo "service enabled: $(systemctl is-enabled ollama 2>/dev/null || echo no)  active: $(systemctl is-active ollama 2>/dev/null || echo no)"
  systemctl show ollama -p Environment 2>/dev/null | tr ' ' '\n' | grep -E 'OLLAMA_' | redact
fi

section "Listening sockets (expect nothing on 11434 or 8787 except 127.0.0.1 / ::1)"
if have ss; then ss -Hltn 2>/dev/null | awk '{print $4}' | sort -u | redact; fi

section "Network link (wired is preferred)"
for dev in /sys/class/net/*; do
  name=$(basename "$dev"); [ "$name" = lo ] && continue
  kind=ethernet; [ -d "$dev/wireless" ] && kind=wifi
  echo "$name: $kind state=$(cat "$dev/operstate" 2>/dev/null) speed=$(cat "$dev/speed" 2>/dev/null || echo ?)Mb/s"
done
have resolvectl && resolvectl status 2>/dev/null | grep -E 'DNS Servers|Current DNS' | redact

section "Clock (request signatures require time within 60 seconds)"
if have timedatectl; then timedatectl show -p NTPSynchronized -p Timezone 2>/dev/null; fi

section "Power and sleep (an inference server must not suspend)"
for target in sleep.target suspend.target hibernate.target hybrid-sleep.target; do
  have systemctl && echo "$target: $(systemctl is-enabled "$target" 2>/dev/null || echo unknown)"
done
for supply in /sys/class/power_supply/*; do
  [ -e "$supply/type" ] && echo "power supply: $(basename "$supply") type=$(cat "$supply/type")"
done
have sensors && sensors 2>/dev/null | grep -Ei 'package|tctl|edge|composite' | head -6

section "Firewall"
if have ufw; then ufw status 2>/dev/null | head -3 || echo "(ufw status needs sudo)"; fi
if have nft; then nft list tables 2>/dev/null || echo "(nft list needs sudo)"; fi
if have firewall-cmd; then firewall-cmd --state 2>/dev/null; fi

section "Runtimes"
have node && echo "node $(node --version)" || echo "(node not installed; the gateway needs Node.js 22 or newer)"
have cloudflared && run cloudflared --version

echo
echo "== End of inventory. Next: measure upload/latency over a few days and record power draw under load."
