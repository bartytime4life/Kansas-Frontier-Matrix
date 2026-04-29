#!/usr/bin/env bash
# KFM Ecology Focus Mode Validation Runner

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
VALIDATOR="$ROOT_DIR/tools/validators/ecology/validate_ecology_bundle.py"
RUNTIME="$ROOT_DIR/apps/governed_api/ecology/focus_mode.py"
REQUEST_DIR="$ROOT_DIR/tests/fixtures/ecology/focus_mode"

echo "=== KFM Ecology Focus Mode Checks ==="
echo "ROOT_DIR: $ROOT_DIR"
echo

if [[ ! -f "$VALIDATOR" ]]; then
  echo "ERROR: validator not found at $VALIDATOR"
  exit 1
fi

if [[ ! -f "$RUNTIME" ]]; then
  echo "ERROR: Focus Mode runtime not found at $RUNTIME"
  exit 1
fi

echo "→ Validating Focus Mode request fixtures"
python "$VALIDATOR" \
  --bundle "$REQUEST_DIR"/*.json \
  --expect pass

echo
echo "→ Executing Focus Mode valid request"
python "$RUNTIME" "$REQUEST_DIR/valid_request.json"

echo
echo "→ Executing Focus Mode deny-sensitive request"
python "$RUNTIME" "$REQUEST_DIR/deny_sensitive_request.json"

echo
echo "→ Executing Focus Mode abstain-missing-evidence request"
python "$RUNTIME" "$REQUEST_DIR/abstain_missing_evidence.json"

echo
echo "✓ Ecology Focus Mode checks completed"
