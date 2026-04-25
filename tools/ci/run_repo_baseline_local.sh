#!/bin/sh
set -eu

# Mirrors the current `verification-baseline / repo-baseline` workflow job.

sh -n ./tools/ci/verify_baseline.sh \
  ./tools/ci/test_verify_baseline.sh \
  ./tools/ci/check_readme_paths.sh \
  ./tools/ci/test_check_readme_paths.sh \
  ./tools/ci/check_python_syntax.sh \
  ./tools/ci/test_check_python_syntax.sh \
  ./scripts/bootstrap.sh \
  ./scripts/dev_up.sh \
  ./scripts/sample_ingest.sh

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

python3 -m pytest -q tests/ci

echo "run_repo_baseline_local: completed"
