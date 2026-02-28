#!/usr/bin/env bash
set -euo pipefail

test -f README.md
test -f kfm.example.yaml
test -f evidence/run-receipt.json
test -f evidence/checksums.json
echo "Verification passed for sample_dataset"
