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
# - processed → pass (any policy decision allowed except deny)
# - triplets → pass (claims + envelopes valid)
# - published → pass + policy_decision=allow ONLY

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

run_dir_if_present() {
  local label="$1"
  local dir="$2"
  local expect_policy="${3:-}"

  if [[ ! -d "$dir" ]]; then
    echo "SKIP: $label directory not present: $dir"
    return 0
  fi

  shopt -s nullglob
  local files=("$dir"/*.json)
  shopt -u nullglob

  if [[ "${#files[@]}" -eq 0 ]]; then
    echo "SKIP: $label has no JSON files: $dir"
    return 0
  fi

  echo "→ Validating $label"
  echo "  files=${#files[@]}"

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

# --------------------------------------------------
# Processed outputs (allow | hold | generalize OK)
# --------------------------------------------------
run_dir_if_present "processed ecology outputs" "$PROCESSED_DIR"

# --------------------------------------------------
# Triplets (claims + envelopes)
# --------------------------------------------------
run_dir_if_present "ecology triplets" "$TRIPLETS_DIR"

# --------------------------------------------------
# Published releases (STRICT: allow only)
# --------------------------------------------------
run_dir_if_present "published ecology releases" "$PUBLISHED_DIR" "allow"

echo "✓ All ecology release checks passed"
