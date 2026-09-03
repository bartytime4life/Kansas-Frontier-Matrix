#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ "${SITES_ENV_READY:-}" != "1" ]]; then
  exec bash "${script_dir}/sites-env.sh" -- "$0" "$@"
fi

command -v timeout || {
  echo "build-verified.sh requires GNU timeout." >&2
  exit 69
}

vinext="$(command -v vinext || true)"
if [[ "${vinext}" != */node_modules/.bin/vinext || ! -x "${vinext}" ]]; then
  vinext="${SITES_PROJECT_ROOT}/node_modules/.bin/vinext"
fi
if [[ ! -x "${vinext}" ]]; then
  echo "vinext is unavailable from the npm script PATH and app-local node_modules. Run npm run install:ci and wait for it to finish before building." >&2
  exit 69
fi

echo "Running bounded vinext build from ${vinext}..."
timeout \
  --signal=TERM \
  --kill-after="${SITES_BUILD_KILL_AFTER:-10s}" \
  "${SITES_BUILD_TIMEOUT:-3m}" \
  "${vinext}" build
