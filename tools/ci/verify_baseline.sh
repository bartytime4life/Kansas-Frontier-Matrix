#!/bin/sh
set -eu

report_path="baseline-report.txt"
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
    *)
      report_path="$1"
      shift
      ;;
  esac
done

cd "${repo_root}"

[ -f "README.md" ]
[ ! -f "readme.md" ]
[ -f ".github/CODEOWNERS" ]

for path in \
  ".github/workflows/README.md" \
  "apps/governed-api/README.md" \
  "apps/web/README.md" \
  "ui/README.md" \
  "data/registry/README.md" \
  "data/proofs/README.md" \
  "data/receipts/README.md" \
  "data/published/README.md" \
  "release/README.md"
do
  [ -f "$path" ]
done

workflow_yml_count="$(
  git ls-files '.github/workflows/*.yml' '.github/workflows/*.yaml' \
    | wc -l \
    | tr -d '[:space:]'
)"

{
  echo "README.md: yes"
  echo "readme.md: no"
  echo "CODEOWNERS: yes"
  echo "workflow_yml_count: ${workflow_yml_count}"
} | tee "${report_path}"
