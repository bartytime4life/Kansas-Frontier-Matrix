#!/bin/sh
set -eu

# Mirrors the current `verification-baseline / repo-baseline` workflow job.

sh -n ./tools/ci/verify_baseline.sh \
  ./tools/ci/test_verify_baseline.sh \
  ./tools/ci/check_readme_paths.sh \
  ./tools/ci/test_check_readme_paths.sh \
  ./tools/ci/check_python_syntax.sh \
  ./tools/ci/test_check_python_syntax.sh \
  ./tools/ci/install_boundary_test_deps.sh \
  ./scripts/bootstrap.sh \
  ./scripts/dev_up.sh \
  ./scripts/sample_ingest.sh

# Optional proposed HUC12/admin crosswalk pipeline files.
# Keep these guarded so baseline remains green before the lane is fully merged.
if [ -f ./pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/runner.py ]; then
  python3 -m py_compile ./pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/runner.py
fi

if [ -f ./tools/validators/crosswalk/validate_crosswalk_sql.sql ]; then
  test -s ./tools/validators/crosswalk/validate_crosswalk_sql.sql
fi

if [ -f ./schemas/contracts/v1/crosswalk/crosswalk_pair.schema.json ]; then
  python3 -m json.tool ./schemas/contracts/v1/crosswalk/crosswalk_pair.schema.json >/dev/null
fi

if [ -f ./policy/crosswalk/crosswalk.rego ]; then
  test -s ./policy/crosswalk/crosswalk.rego
fi

if [ -f ./data/registry/crosswalk/sources.yaml ]; then
  test -s ./data/registry/crosswalk/sources.yaml
fi

sh ./tools/ci/test_verify_baseline.sh
sh ./tools/ci/test_check_readme_paths.sh
sh ./tools/ci/test_check_python_syntax.sh
sh ./tools/ci/check_readme_paths.sh --manifest ./tools/ci/readme_required_paths.txt
sh ./tools/ci/verify_baseline.sh baseline-report.txt
sh ./tools/ci/check_python_syntax.sh

./scripts/bootstrap.sh
python3 ./scripts/validate_schemas.py
python3 ./scripts/catalog_validate.py
python3 ./tools/ci/validate_policy_runtime_fixtures.py --root .
python3 ./tools/ci/validate_renderer_fixtures.py --root .
python3 ./tools/ci/report_placeholder_markers.py --root . --top 5
python3 ./tools/ci/check_markdown_authority_thresholds.py --root .
python3 ./tools/ci/check_governed_api_path_policy.py --root .
python3 ./tools/ci/generate_markdown_debt_backlog.py --root . --top 10 --output artifacts/observability/markdown_debt_backlog.md
python3 ./tools/ci/build_governed_artifacts.py --root . --out-dir artifacts/governed

if [ "${KFM_INSTALL_BOUNDARY_DEPS:-0}" = "1" ]; then
  sh ./tools/ci/install_boundary_test_deps.sh
fi

python3 -m pytest -q tests/ci
python3 -m pytest -q apps/governed-api/ecology/tests apps/ui/ecology/tests

if [ -d ./tests/crosswalk ]; then
  python3 -m pytest -q tests/crosswalk
fi

echo "run_repo_baseline_local: completed"
