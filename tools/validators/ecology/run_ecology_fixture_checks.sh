#!/usr/bin/env bash
# KFM Ecology Fixture Validation Runner
#
# Runs validator across valid and invalid fixture sets.
# - Valid fixtures MUST pass
# - Invalid fixtures MUST fail
#
# Exit code:
#   0 → success (all expectations met)
#   1 → failure (any mismatch or execution error)

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
VALIDATOR="$ROOT_DIR/tools/validators/ecology/validate_ecology_bundle.py"

VALID_DIR="$ROOT_DIR/tests/fixtures/ecology/valid"
INVALID_DIR="$ROOT_DIR/tests/fixtures/ecology/invalid"

echo "=== KFM Ecology Fixture Checks ==="
echo "ROOT_DIR: $ROOT_DIR"
echo

if [[ ! -f "$VALIDATOR" ]]; then
  echo "ERROR: validator not found at $VALIDATOR"
  exit 1
fi

# Ensure directories exist (NEEDS_VERIFICATION if not present)
if [[ ! -d "$VALID_DIR" ]]; then
  echo "ERROR: valid fixture directory missing: $VALID_DIR"
  exit 1
fi

if [[ ! -d "$INVALID_DIR" ]]; then
  echo "ERROR: invalid fixture directory missing: $INVALID_DIR"
  exit 1
fi

echo "→ Running VALID fixtures (expect: pass)"
python "$VALIDATOR" \
  --bundle "$VALID_DIR"/*.json \
  --expect pass

echo
echo "→ Running INVALID fixtures (expect: fail)"
python "$VALIDATOR" \
  --bundle "$INVALID_DIR"/*.json \
  --expect fail

echo
echo "✓ All ecology fixture checks passed"
