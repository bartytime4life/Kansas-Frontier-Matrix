#!/usr/bin/env bash
# gen_sha256.sh — Kansas-Frontier-Matrix
# ------------------------------------------------------------
# Cross-platform SHA-256 generator & verifier (GNU/BSD/macOS).
# Writes "<file>.sha256" next to each input file by default.
#
# Usage:
#   bash scripts/gen_sha256.sh <file> [more files...]
#   bash scripts/gen_sha256.sh --verify <file.sha256> [more .sha256 files...]
#   bash scripts/gen_sha256.sh --json <file> [more files...]        # also print JSON lines
#   find data/cogs -type f -name '*.tif' -print0 | \
#     xargs -0 -n1 bash scripts/gen_sha256.sh
#
# Notes:
#   - Auto-detects: sha256sum | gsha256sum | shasum -a 256
#   - On success writes: "<hex>  <basename>" (GNU-compatible format)
#   - Verification accepts either explicit *.sha256 files or infers "<file>.sha256"
#   - Safe with spaces in filenames
# ------------------------------------------------------------

set -euo pipefail

# ---------- args ----------
JSON=0
VERIFY=0

print_help() {
  sed -n '1,40p' "$0" | sed 's/^# \{0,1\}//'
}

args=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help) print_help; exit 0;;
    --json) JSON=1; shift;;
    -c|--check|--verify) VERIFY=1; shift;;
    --) shift; break;;
    -*) echo "Unknown option: $1" >&2; exit 2;;
    *) args+=("$1"); shift;;
  esac
done
# append any remaining (post --)
if [[ $# -gt 0 ]]; then
  args+=("$@")
fi

if [[ ${#args[@]} -eq 0 ]]; then
  echo "No files provided. Try --help." >&2
  exit 2
fi

# ---------- tool detection ----------
SHA_BIN=""
if command -v sha256sum >/dev/null 2>&1; then
  SHA_BIN="sha256sum"
elif command -v gsha256sum >/dev/null 2>&1; then
  SHA_BIN="gsha256sum"
elif command -v shasum >/dev/null 2>&1; then
  SHA_BIN="shasum -a 256"
else
  echo "ERROR: need sha256sum/gsha256sum or shasum." >&2
  exit 1
fi

# ---------- helpers ----------
# Compute SHA256 hex for a single path, print "<hex>  <basename>"
sha_compute_line() {
  local f="$1"
  if [[ "$SHA_BIN" == "shasum -a 256" ]]; then
    # shasum prints: "HEX  PATH"
    (cd "$(dirname -- "$f")" && shasum -a 256 "$(basename -- "$f")")
  else
    # sha256sum/gsha256sum
    "$SHA_BIN" "$f"
  fi
}

# Verify one .sha256 file (GNU or BSD shasum can read -c format)
sha_verify_file() {
  local sf="$1"
  if [[ ! -f "$sf" ]]; then
    echo "Missing .sha256: $sf" >&2
    return 1
  fi
  local dir base
  dir="$(cd "$(dirname -- "$sf")" && pwd)"
  base="$(basename -- "$sf")"
  if [[ "$SHA_BIN" == "shasum -a 256" ]]; then
    # BSD shasum verification must run in the directory for -c to work reliably with spaces
    (cd "$dir" && shasum -a 256 -c "$base")
  else
    (cd "$dir" && sha256sum -c "$base")
  fi
}

write_sha_file() {
  local f="$1"
  local out="${f}.sha256"
  local line
  line="$(sha_compute_line "$f")"
  printf '%s\n' "$line" > "$out"
  # Normalize to GNU two-space format (shasum already OK)
  # Many tools accept single or double spaces; we standardize on two.
  # shellcheck disable=SC2016
  sed -i'' -e 's/ \{1,\}/  /1' "$out" 2>/dev/null || true
  echo "$out"
}

print_json() {
  # path, sha, size
  python3 - "$1" <<'PY'
import hashlib, sys, os, json
p=sys.argv[1]
h=hashlib.sha256()
with open(p,'rb') as f:
    for chunk in iter(lambda:f.read(1024*1024), b''):
        h.update(chunk)
print(json.dumps({"path": p, "sha256": h.hexdigest(), "size": os.path.getsize(p)}))
PY
}

# ---------- main ----------
status=0

if [[ $VERIFY -eq 1 ]]; then
  for x in "${args[@]}"; do
    if [[ -f "$x" && "$x" == *.sha256 ]]; then
      sha_verify_file "$x" || status=$?
    elif [[ -f "$x" ]]; then
      # infer "<file>.sha256"
      sf="${x}.sha256"
      sha_verify_file "$sf" || status=$?
    else
      echo "Not found: $x" >&2
      status=1
    fi
  done
  exit "$status"
fi

# Generate checksums
for f in "${args[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "Skip (not a file): $f" >&2
    status=1
    continue
  fi
  out="$(write_sha_file "$f")" || status=$?
  echo "• wrote $out"
  if [[ $JSON -eq 1 ]]; then
    print_json "$f"
  fi
done

exit "$status"

