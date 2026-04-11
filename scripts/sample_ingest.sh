#!/usr/bin/env bash
set -euo pipefail

SOURCE_NAME="${1:-example_fixture}"
OUT_DIR="data/work/sample_ingest"
mkdir -p "$OUT_DIR"

cp schemas/tests/fixtures/contracts/v1/valid/correction_notice.supersession.valid.json "$OUT_DIR/${SOURCE_NAME}.json"
cat > "$OUT_DIR/${SOURCE_NAME}.receipt.json" <<JSON
{
  "source": "$SOURCE_NAME",
  "copied_from": "schemas/tests/fixtures/contracts/v1/valid/correction_notice.supersession.valid.json",
  "timestamp_utc": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "note": "Sample ingest scaffold for local validation only."
}
JSON

echo "sample-ingest: wrote $OUT_DIR/${SOURCE_NAME}.json"
echo "sample-ingest: wrote $OUT_DIR/${SOURCE_NAME}.receipt.json"
