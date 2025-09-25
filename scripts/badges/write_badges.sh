#!/usr/bin/env bash
# Kansas-Frontier-Matrix — Badge Writer
# Generates shields.io endpoint JSONs in web/badges/
# ✔ green = no errors/warnings
# ⚠ orange = warnings only
# ❌ red = errors or unmapped

set -euo pipefail

SRC_DIR="data/sources"
BADGE_DIR="web/badges"
REPORT="build/stac_report.json"
MAP="scripts/badges/source_map.json"

mkdir -p "$BADGE_DIR"

# Collect sources
mapfile -t SOURCES < <(jq -r '.id // empty' "$SRC_DIR"/*.json | sort -u)

write_badge () {
  local id="$1" label="$2" msg="$3" color="$4"
  cat > "$BADGE_DIR/${id}.json" <<EOF
{ "schemaVersion": 1, "label": "${label}", "message": "${msg}", "color": "${color}" }
EOF
}

# Default all ❌ until proven otherwise
for id in "${SOURCES[@]}"; do
  write_badge "$id" "$id" "❌" "red"
done

# Skip if no report
[ -s "$REPORT" ] || exit 0

REPORT_DATA="$(cat "$REPORT")"

for id in "${SOURCES[@]}"; do
  ITEMS=$(jq -r --arg sid "$id" '.[$sid][]?' "$MAP" 2>/dev/null || echo "")
  [ -z "$ITEMS" ] && continue

  ERR=0; WARN=0; COUNT=0
  while IFS= read -r key; do
    row=$(jq -c --arg k "$key" '.[] | select((.stac_item==$k) or (.id==$k))' <<<"$REPORT_DATA")
    if [ -n "$row" ]; then
      e=$(jq -r '.errors // 0' <<<"$row")
      w=$(jq -r '.warnings // 0' <<<"$row")
      ERR=$((ERR+e)); WARN=$((WARN+w)); COUNT=$((COUNT+1))
    fi
  done <<< "$ITEMS"

  if [ $COUNT -eq 0 ]; then
    write_badge "$id" "$id" "❌" "red"
  elif [ $ERR -gt 0 ]; then
    write_badge "$id" "$id" "❌" "red"
  elif [ $WARN -gt 0 ]; then
    write_badge "$id" "$id" "⚠" "orange"
  else
    write_badge "$id" "$id" "✔" "brightgreen"
  fi
done
