#!/usr/bin/env bash
# KFM Ecology Release Validation Runner
#
# Validates governed ecology output artifacts:
# - EvidenceBundle objects
# - DecisionEnvelope objects
# - EcologicalClaim triplets
# - ReleaseManifest objects

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
VALIDATOR="$ROOT_DIR/tools/validators/ecology/validate_ecology_bundle.py"

PROCESSED_DIR="$ROOT_DIR/data/processed/ecology"
TRIPLETS_DIR="$ROOT_DIR/data/triplets/ecology"
PUBLISHED_DIR="$ROOT_DIR/data/published/ecology"

echo "=== KFM Ecology Release Checks ==="
echo "ROOT_DIR: $ROOT_DIR"
echo

if [[ ! -f "$VALIDATOR" ]]; then
  echo "ERROR: validator not found at $VALIDATOR"
  exit 1
fi

echo "→ Validating processed ecology outputs"
python "$VALIDATOR" \
  --bundle "$PROCESSED_DIR"/*.json \
  --expect pass

echo
echo "→ Validating ecology triplets"
python "$VALIDATOR" \
  --bundle "$TRIPLETS_DIR"/*.json \
  --expect pass

echo
echo "→ Validating published ecology releases"
python "$VALIDATOR" \
  --bundle "$PUBLISHED_DIR"/*.json \
  --expect pass

echo
echo "✓ All ecology release checks passed"
