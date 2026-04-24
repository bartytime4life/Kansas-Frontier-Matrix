#!/bin/sh
set -eu

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
checker="${script_dir}/check_readme_paths.sh"

"${checker}" --root . >/dev/null

# unknown option should fail
if "${checker}" --unknown >/dev/null 2>&1; then
  echo "expected checker to fail on unknown option"
  exit 1
fi

echo "check_readme_paths tests passed"
