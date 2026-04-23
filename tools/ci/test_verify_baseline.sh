#!/bin/sh
set -eu

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
verifier="${script_dir}/verify_baseline.sh"

tmpdir="$(mktemp -d)"
trap 'rm -rf "${tmpdir}"' EXIT

seed_repo() {
  root="$1"
  mkdir -p \
    "${root}/.github/workflows" \
    "${root}/apps/governed-api" \
    "${root}/apps/web" \
    "${root}/ui" \
    "${root}/data/registry" \
    "${root}/data/proofs" \
    "${root}/data/receipts" \
    "${root}/data/published" \
    "${root}/release"

  touch \
    "${root}/README.md" \
    "${root}/.github/CODEOWNERS" \
    "${root}/.github/workflows/README.md" \
    "${root}/apps/governed-api/README.md" \
    "${root}/apps/web/README.md" \
    "${root}/ui/README.md" \
    "${root}/data/registry/README.md" \
    "${root}/data/proofs/README.md" \
    "${root}/data/receipts/README.md" \
    "${root}/data/published/README.md" \
    "${root}/release/README.md" \
    "${root}/.github/workflows/verification-baseline.yml"

  (
    cd "${root}"
    git init -q
    git add .
  )
}

# PASS case
pass_root="${tmpdir}/pass"
mkdir -p "${pass_root}"
seed_repo "${pass_root}"
"${verifier}" report.txt --root "${pass_root}"
[ -f "${pass_root}/report.txt" ]
grep -q "workflow_yml_count: 1" "${pass_root}/report.txt"

# FAIL case: lowercase readme should fail verification
fail_root="${tmpdir}/fail"
mkdir -p "${fail_root}"
seed_repo "${fail_root}"
touch "${fail_root}/readme.md"
if "${verifier}" --root "${fail_root}" >/dev/null 2>&1; then
  echo "expected verifier to fail when readme.md is present"
  exit 1
fi

# FAIL case: unknown option should fail with usage error
if "${verifier}" --unknown >/dev/null 2>&1; then
  echo "expected verifier to fail on unknown option"
  exit 1
fi

# FAIL case: multiple positional args should fail
if "${verifier}" report-a.txt report-b.txt --root "${pass_root}" >/dev/null 2>&1; then
  echo "expected verifier to fail on multiple report paths"
  exit 1
fi


echo "verify_baseline tests passed"
