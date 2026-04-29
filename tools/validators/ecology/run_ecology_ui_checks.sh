#!/usr/bin/env bash
# KFM Ecology UI payload validation runner

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
VALIDATOR="$ROOT_DIR/tools/validators/ecology/validate_ecology_bundle.py"

echo "=== KFM Ecology UI Checks ==="
echo "ROOT_DIR: $ROOT_DIR"
echo

if [[ ! -f "$VALIDATOR" ]]; then
  echo "ERROR: validator not found at $VALIDATOR"
  exit 1
fi

python "$VALIDATOR"   --bundle "$ROOT_DIR/tests/fixtures/ecology/ui"/*.json   --expect pass

echo
echo "✓ Ecology UI checks passed"
