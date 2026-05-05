#!/usr/bin/env bash
# KFM Ecology Fixture Validation Runner
#
# Runs validator across fixture sets.
#
# Expectations:
# - valid fixtures MUST pass validation
# - invalid fixtures MUST fail validation
# - hold fixtures MUST pass validation and produce policy_decision=hold
# - generalize fixtures MUST pass validation and produce policy_decision=generalize
# - allow fixtures MUST pass validation and produce policy_decision=allow
#
# Exit code:
#   0 → success
#   1 → failure

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
VALIDATOR="$ROOT_DIR/tools/validators/ecology/validate_ecology_bundle.py"

VALID_DIR="$ROOT_DIR/tests/fixtures/ecology/valid"
INVALID_DIR="$ROOT_DIR/tests/fixtures/ecology/invalid"
HOLD_DIR="$ROOT_DIR/tests/fixtures/ecology/hold"
GENERALIZE_DIR="$ROOT_DIR/tests/fixtures/ecology/generalize"
ALLOW_DIR="$ROOT_DIR/tests/fixtures/ecology/allow"

echo "=== KFM Ecology Fixture Checks ==="
echo "ROOT_DIR: $ROOT_DIR"
echo

if [[ ! -f "$VALIDATOR" ]]; then
  echo "ERROR: validator not found at $VALIDATOR"
  exit 1
fi

require_json_dir() {
  local label="$1"
  local dir="$2"

  if [[ ! -d "$dir" ]]; then
    echo "ERROR: $label fixture directory missing: $dir"
    exit 1
  fi

  shopt -s nullglob
  local files=("$dir"/*.json)
  shopt -u nullglob

  if [[ "${#files[@]}" -eq 0 ]]; then
    echo "ERROR: $label fixture directory contains no JSON files: $dir"
    exit 1
  fi
}

run_required_set() {
  local label="$1"
  local dir="$2"
  local expect="$3"
  local expect_policy="${4:-}"

  require_json_dir "$label" "$dir"

  shopt -s nullglob
  local files=("$dir"/*.json)
  shopt -u nullglob

  echo "→ Running $label fixtures"
  echo "  files=${#files[@]}"
  echo "  expect=$expect"

  if [[ -n "$expect_policy" ]]; then
    echo "  expect_policy=$expect_policy"
    python "$VALIDATOR" \
      --bundle "$dir"/*.json \
      --expect "$expect" \
      --expect-policy "$expect_policy"
  else
    python "$VALIDATOR" \
      --bundle "$dir"/*.json \
      --expect "$expect"
  fi

  echo
}

run_required_set "VALID" "$VALID_DIR" "pass"
run_required_set "INVALID" "$INVALID_DIR" "fail"
run_required_set "HOLD" "$HOLD_DIR" "pass" "hold"
run_required_set "GENERALIZE" "$GENERALIZE_DIR" "pass" "generalize"
run_required_set "ALLOW" "$ALLOW_DIR" "pass" "allow"

echo "✓ All ecology fixture checks passed"
