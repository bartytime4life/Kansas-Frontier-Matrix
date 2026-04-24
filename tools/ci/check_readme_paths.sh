#!/bin/sh
set -eu

repo_root="."

while [ "$#" -gt 0 ]; do
  case "$1" in
    --root)
      if [ "$#" -lt 2 ]; then
        echo "missing value for --root" >&2
        exit 2
      fi
      repo_root="$2"
      shift 2
      ;;
    --help|-h)
      echo "usage: $0 [--root <repo_root>]"
      exit 0
      ;;
    --*)
      echo "unknown option: $1" >&2
      exit 2
      ;;
    *)
      echo "unexpected argument: $1" >&2
      exit 2
      ;;
  esac
done

cd "$repo_root"

required_paths='
scripts/README.md
scripts/bootstrap.sh
scripts/dev_up.sh
scripts/sample_ingest.sh
scripts/validate_schemas.py
scripts/catalog_validate.py
tools/ci/README.md
tools/ci/verify_baseline.sh
tools/ci/test_verify_baseline.sh
tools/ci/render_promotion_summary.py
tools/ci/render_promotion_bundle_summary.py
tools/ci/render_diff_summary.py
tools/ci/render_bundle_diff_policy_summary.py
tools/ci/render_promotion_review_handoff.py
tests/ci/README.md
tests/ci/test_render_diff_summary.py
tests/ci/test_render_bundle_diff_policy_summary.py
tests/ci/test_render_promotion_review_handoff.py
'

missing_count=0
for path in $required_paths; do
  if [ ! -f "$path" ]; then
    echo "missing: $path" >&2
    missing_count=$((missing_count + 1))
  fi
done

if [ "$missing_count" -ne 0 ]; then
  echo "check_readme_paths: failed ($missing_count missing path(s))" >&2
  exit 1
fi

echo "check_readme_paths: ok"
