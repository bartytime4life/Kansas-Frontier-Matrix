#!/bin/sh
set -eu

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
checker="${script_dir}/check_readme_paths.sh"
manifest="${script_dir}/readme_required_paths.txt"

"${checker}" --root . --manifest "${manifest}" >/dev/null

# unknown option should fail
if "${checker}" --unknown >/dev/null 2>&1; then
  echo "expected checker to fail on unknown option"
  exit 1
fi

# incomplete root should fail
tmpdir="$(mktemp -d)"
trap 'rm -rf "${tmpdir}"' EXIT
if "${checker}" --root "${tmpdir}" --manifest "${manifest}" >/dev/null 2>&1; then
  echo "expected checker to fail on incomplete root"
  exit 1
fi

# missing manifest should fail
if "${checker}" --manifest "${script_dir}/does-not-exist.txt" >/dev/null 2>&1; then
  echo "expected checker to fail on missing manifest"
  exit 1
fi

# empty/comment-only manifest should fail
empty_manifest="${tmpdir}/empty-manifest.txt"
printf '# comment only\n\n' > "${empty_manifest}"
if "${checker}" --manifest "${empty_manifest}" >/dev/null 2>&1; then
  echo "expected checker to fail on empty manifest"
  exit 1
fi

echo "check_readme_paths tests passed"
