#!/usr/bin/env bash
# KFM Ecology UI payload validation runner
#
# Validates UI-facing payload fixtures:
# - EcologyEvidenceDrawerPayload
#
# Expectations:
# - All UI fixtures must pass schema validation
# - No governance-layer failures (UI objects are exempt from policy gating)
#
# Exit code:
#   0 → success
#   1 → failure

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
VALIDATOR="$ROOT_DIR/tools/validators/ecology/validate_ecology_bundle.py"
UI_DIR="$ROOT_DIR/tests/fixtures/ecology/ui"

echo "=== KFM Ecology UI Checks ==="
echo "ROOT_DIR: $ROOT_DIR"
echo

if [[ ! -f "$VALIDATOR" ]]; then
  echo "ERROR: validator not found at $VALIDATOR"
  exit 1
fi

if [[ ! -d "$UI_DIR" ]]; then
  echo "SKIP: UI fixture directory not present: $UI_DIR"
  exit 0
fi

shopt -s nullglob
UI_FILES=("$UI_DIR"/*.json)
shopt -u nullglob

if [[ "${#UI_FILES[@]}" -eq 0 ]]; then
  echo "SKIP: no UI fixture files found in $UI_DIR"
  exit 0
fi

echo "→ Validating UI payload fixtures"
echo "  files=${#UI_FILES[@]}"

python "$VALIDATOR" \
  --bundle "$UI_DIR"/*.json \
  --expect pass

echo
echo "✓ Ecology UI checks passed"
