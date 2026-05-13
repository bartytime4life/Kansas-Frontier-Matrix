#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$repo_root"

python tools/validators/source/validate_doctrine_artifact_preflight_summary.py --fixtures
shadow_summary="$(mktemp)"
python scripts/maintenance/run_doctrine_artifact_preflight.py --stable-filenames --emit-normalized-only > "$shadow_summary"
python tools/validators/source/validate_doctrine_preflight_summary_consistency.py --require-normalized-only "$shadow_summary"
rm -f "$shadow_summary"
pytest \
  tests/policy/test_doctrine_artifact_required.py \
  tests/policy/test_doctrine_artifact_registry_validation.py \
  tests/policy/test_doctrine_artifact_registry_status_alignment.py \
  tests/policy/test_doctrine_artifact_presence_input.py \
  tests/policy/test_doctrine_artifact_provenance.py \
  tests/policy/test_doctrine_registry_alignment.py \
  tests/policy/test_sync_doctrine_artifact_provenance_status.py \
  tests/policy/test_doctrine_artifact_provenance_snapshots.py \
  tests/policy/test_run_doctrine_artifact_preflight.py \
  tests/policy/test_preflight_summary_schema_contract.py \
  tests/policy/test_sync_doctrine_artifact_registry_status.py \
  tests/source/test_doctrine_artifact_preflight_summary_schema.py \
  tests/policy/test_preflight_summary_consistency.py -q
