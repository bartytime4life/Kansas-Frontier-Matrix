#!/usr/bin/env bash
set -euo pipefail

GATE="${1:-}"
if [[ ! "$GATE" =~ ^[A-G]$ ]]; then
  echo "usage: $0 <A|B|C|D|E|F|G>" >&2
  exit 2
fi

CONTRACT="${PROMOTION_CONTRACT:-promotion-contract.json}"
OUT_DIR="${PROMOTION_WORK_DIR:-.promotion}"
OUT="$OUT_DIR/gate_${GATE}.json"
POLICY="$(python - <<'PY' "$CONTRACT" "$GATE"
import json, sys
contract = json.load(open(sys.argv[1], encoding="utf-8"))
print(contract["gates"][sys.argv[2]]["policy"])
PY
)"

mkdir -p "$OUT_DIR"
python tools/validators/build_gate_input.py --gate "$GATE" --contract "$CONTRACT" --out "$OUT"
conftest test "$OUT" --policy "$POLICY"

case "$GATE" in
  A)
    python tools/validators/check_spec_hash.py artifacts/EvidenceBundle.json artifacts/spec_hash.txt --receipt-out "$OUT_DIR/spec_hash_check.json"
    ;;
  G)
    python tools/validators/verify_release_manifest_hashes.py artifacts/release_manifest.json
    ;;
esac
