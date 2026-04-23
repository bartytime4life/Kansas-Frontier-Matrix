#!/usr/bin/env bash
set -euo pipefail

report_path="baseline-report.txt"
repo_root="."

while [[ $# -gt 0 ]]; do
  case "$1" in
    --root)
      repo_root="${2:?missing value for --root}"
      shift 2
      ;;
    *)
      report_path="$1"
      shift
      ;;
  esac
done

cd "${repo_root}"

test -f "README.md"
test ! -f "readme.md"
test -f ".github/CODEOWNERS"

required_paths=(
  ".github/workflows/README.md"
  "apps/governed-api/README.md"
  "apps/web/README.md"
  "ui/README.md"
  "data/registry/README.md"
  "data/proofs/README.md"
  "data/receipts/README.md"
  "data/published/README.md"
  "release/README.md"
)

for path in "${required_paths[@]}"; do
  test -f "$path"
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
