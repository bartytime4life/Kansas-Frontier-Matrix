#!/bin/sh
set -eu

if [ "$#" -ne 1 ]; then
  echo "usage: $0 <source_name>" >&2
  exit 2
fi

source_name="$1"
out_dir="data/work/sample_ingest"
receipt_dir="data/receipts"

mkdir -p "$out_dir" "$receipt_dir"

ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
run_id="sample-${source_name}-$(date -u +%Y%m%dT%H%M%SZ)"
out_file="${out_dir}/${run_id}.json"
receipt_file="${receipt_dir}/${run_id}.json"

cat > "$out_file" <<JSON
{
  "run_id": "${run_id}",
  "source_name": "${source_name}",
  "ingested_at": "${ts}",
  "status": "work"
}
JSON

cat > "$receipt_file" <<JSON
{
  "run_id": "${run_id}",
  "artifact": "${out_file}",
  "recorded_at": "${ts}",
  "type": "sample_ingest_receipt"
}
JSON

echo "wrote ${out_file}"
echo "wrote ${receipt_file}"
