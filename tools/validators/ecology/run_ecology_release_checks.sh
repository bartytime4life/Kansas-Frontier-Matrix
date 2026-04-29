#!/usr/bin/env bash
# KFM Ecology Release Validation Runner
#
# Validates governed ecology output artifacts:
# - EvidenceBundle objects
# - DecisionEnvelope objects
# - EcologicalClaim triplets
# - ReleaseManifest objects
#
# Expectations:
# - processed → pass validation; policy_decision may be allow, hold, or generalize
# - triplets → pass validation
# - published → pass validation and policy_decision=allow only
#
# Exit code:
#   0 → success
#   1 → failure

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

validate_dir() {
  local label="$1"
  local dir="$2"
  local required="$3"
  local expect_policy="${4:-}"

  if [[ ! -d "$dir" ]]; then
    if [[ "$required" == "required" ]]; then
      echo "ERROR: $label directory missing: $dir"
      exit 1
    fi

    echo "SKIP: $label directory not present: $dir"
    return 0
  fi

  shopt -s nullglob
  local files=("$dir"/*.json)
  shopt -u nullglob

  if [[ "${#files[@]}" -eq 0 ]]; then
    if [[ "$required" == "required" ]]; then
      echo "ERROR: $label contains no JSON files: $dir"
      exit 1
    fi

    echo "SKIP: $label has no JSON files: $dir"
    return 0
  fi

  echo "→ Validating $label"
  echo "  files=${#files[@]}"
  echo "  expect=pass"

  if [[ -n "$expect_policy" ]]; then
    echo "  expect_policy=$expect_policy"
    python "$VALIDATOR" \
      --bundle "$dir"/*.json \
      --expect pass \
      --expect-policy "$expect_policy"
  else
    python "$VALIDATOR" \
      --bundle "$dir"/*.json \
      --expect pass
  fi

  echo
}

validate_dir "processed ecology outputs" "$PROCESSED_DIR" "optional"
validate_dir "ecology triplets" "$TRIPLETS_DIR" "optional"
validate_dir "published ecology releases" "$PUBLISHED_DIR" "required" "allow"

echo "✓ All ecology release checks passed"
