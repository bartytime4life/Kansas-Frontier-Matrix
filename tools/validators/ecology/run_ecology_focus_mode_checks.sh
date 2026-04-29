#!/usr/bin/env bash
# KFM Ecology Focus Mode Validation Runner
#
# Validates governed Focus Mode fixtures and runtime outcomes.
#
# Expectations:
# - request fixtures must pass schema validation
# - valid_request.json must return ANSWER
# - deny_sensitive_request.json must return DENY
# - abstain_missing_evidence.json must return ABSTAIN
#
# Exit code:
#   0 → success
#   1 → failure

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

if [[ ! -d "$REQUEST_DIR" ]]; then
  echo "ERROR: Focus Mode fixture directory missing: $REQUEST_DIR"
  exit 1
fi

require_fixture() {
  local file="$1"

  if [[ ! -f "$REQUEST_DIR/$file" ]]; then
    echo "ERROR: required Focus Mode fixture missing: $REQUEST_DIR/$file"
    exit 1
  fi
}

run_runtime_expect_outcome() {
  local fixture="$1"
  local expected="$2"
  local output_file

  output_file="$(mktemp)"

  echo "→ Executing Focus Mode fixture: $fixture"
  echo "  expected_outcome=$expected"

  python "$RUNTIME" "$REQUEST_DIR/$fixture" > "$output_file"

  if ! grep -Eq "\"outcome\"[[:space:]]*:[[:space:]]*\"$expected\"|\"visible_outcome\"[[:space:]]*:[[:space:]]*\"$expected\"" "$output_file"; then
    echo "ERROR: Focus Mode outcome mismatch for $fixture"
    echo "Expected: $expected"
    echo "Actual output:"
    cat "$output_file"
    rm -f "$output_file"
    exit 1
  fi

  cat "$output_file"
  rm -f "$output_file"
  echo
}

require_fixture "valid_request.json"
require_fixture "deny_sensitive_request.json"
require_fixture "abstain_missing_evidence.json"

echo "→ Validating Focus Mode request fixtures"
python "$VALIDATOR" \
  --bundle "$REQUEST_DIR"/*.json \
  --expect pass

echo
run_runtime_expect_outcome "valid_request.json" "ANSWER"
run_runtime_expect_outcome "deny_sensitive_request.json" "DENY"
run_runtime_expect_outcome "abstain_missing_evidence.json" "ABSTAIN"

echo "✓ Ecology Focus Mode checks completed"
