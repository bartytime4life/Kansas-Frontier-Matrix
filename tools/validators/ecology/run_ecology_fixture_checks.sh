#!/usr/bin/env bash
# KFM Ecology Fixture Validation Runner
#
# Runs validator across fixture sets.
# - Valid fixtures MUST pass validation
# - Invalid fixtures MUST fail validation
# - Hold fixtures MUST pass validation and produce policy_decision=hold
# - Generalize fixtures MUST pass validation and produce policy_decision=generalize
# - Publishable fixtures MUST pass validation and produce policy_decision=allow
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

run_if_json_exists() {
  local label="$1"
  local dir="$2"
  local expect="$3"
  local expect_policy="${4:-}"

  if [[ ! -d "$dir" ]]; then
    echo "SKIP: $label directory not present: $dir"
    return 0
  fi

  shopt -s nullglob
  local files=("$dir"/*.json)
  shopt -u nullglob

  if [[ "${#files[@]}" -eq 0 ]]; then
    echo "SKIP: $label has no JSON fixtures: $dir"
    return 0
  fi

  echo "→ Running $label fixtures"
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

require_json_dir "valid" "$VALID_DIR"
require_json_dir "invalid" "$INVALID_DIR"

run_if_json_exists "VALID" "$VALID_DIR" "pass"
run_if_json_exists "INVALID" "$INVALID_DIR" "fail"
run_if_json_exists "HOLD" "$HOLD_DIR" "pass" "hold"
run_if_json_exists "GENERALIZE" "$GENERALIZE_DIR" "pass" "generalize"
run_if_json_exists "ALLOW" "$ALLOW_DIR" "pass" "allow"

echo "✓ All ecology fixture checks passed"
