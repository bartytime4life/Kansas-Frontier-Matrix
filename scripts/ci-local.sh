#!/usr/bin/env bash
# Local mirror of .github/workflows/public-core-repair.yml (job verify-core-delivery).
# Keep the steps below in step with that workflow. Unlike CI it runs every step after
# a failure, so one run reports all breakages, and it cleans up the servers it starts.
# Usage: bash scripts/ci-local.sh [LOG_DIR]
set -uo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
logs="${1:-${project_root}/.sites-runtime/ci-local/$(date -u +%Y%m%dT%H%M%SZ)}"
mkdir -p "${logs}"
logs="$(cd "${logs}" && pwd)"
cd "${project_root}"

# The pipeline PC has no system npm; use the pinned copy beside the checkouts.
if ! command -v npm >/dev/null && [[ -x "${project_root}/../development-tools/bin/npm" ]]; then
  export PATH="$(cd "${project_root}/../development-tools/bin" && pwd):${PATH}"
fi
for tool in npm flock setsid curl; do
  command -v "${tool}" >/dev/null || { echo "ci-local.sh requires ${tool}." >&2; exit 69; }
done

# One run at a time: runs share node_modules, dist/ and ports 5182/5183.
mkdir -p .sites-runtime
exec 8>.sites-runtime/ci-local.lock
flock -n 8 || { echo "Another ci-local.sh run holds .sites-runtime/ci-local.lock." >&2; exit 75; }
for port in 5182 5183; do
  if (exec 3<>"/dev/tcp/127.0.0.1/${port}") 2>/dev/null; then echo "Port ${port} is in use; stop that server first." >&2; exit 75; fi
done

export RUNNER_TEMP="${logs}"
summary="${logs}/summary.txt"; : > "${summary}"
overall=0
step() {
  local name=$1 start=$SECONDS rc; shift
  echo "[ci-local] ${name}"
  ( "$@" ) > "${logs}/${name}.log" 2>&1; rc=$?
  local status=PASS; [[ ${rc} -eq 0 ]] || { status="FAIL(${rc})"; overall=1; }
  printf '%-22s %-9s %4ss\n' "${name}" "${status}" "$((SECONDS - start))" | tee -a "${summary}"
}

http_boundary() {
  set -euo pipefail
  NODE_ENV=production PORT=5182 node server/start.mjs > "${RUNNER_TEMP}/node-runtime.log" 2>&1 &
  site_pid=$!
  trap 'kill "${site_pid}" 2>/dev/null || true' EXIT
  for attempt in $(seq 1 30); do
    if curl --fail --silent http://127.0.0.1:5182/ > /dev/null; then break; fi
    sleep 1
  done
  for suite in godaddy-node-runtime.test.mjs pipeline-http.test.mjs county-search.browser.mjs \
    aviation-layout.browser.mjs explorer-startup.browser.mjs; do
    KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5182 node --test "tests/${suite}"
  done
  node --input-type=module - "${RUNNER_TEMP}/node-runtime.log" <<'NODE'
import { readFileSync } from 'node:fs';
import assert from 'node:assert/strict';
const line = readFileSync(process.argv[2], 'utf8').split('\n').find(line => line.startsWith('KFM_NODE_STARTUP '));
assert.ok(line, 'the real startup process must report its HTTP check');
const report = JSON.parse(line.slice('KFM_NODE_STARTUP '.length));
assert.equal(report.production, true);
assert.equal(report.listenPort, 5182);
assert.equal(report.outcome, 'LOOPBACK_BUILD_READY');
assert.equal(report.httpStatus, 200);
NODE
}

preview_port() {
  set -euo pipefail
  # npm run dev starts the server as a grandchild; its own session lets EXIT stop all of it.
  PORT=5183 setsid npm run dev > "${RUNNER_TEMP}/node-preview.log" 2>&1 &
  preview_pid=$!
  trap 'kill -TERM -- "-${preview_pid}" 2>/dev/null || true' EXIT
  for attempt in $(seq 1 120); do
    if curl --fail --silent http://127.0.0.1:5183/api/ai/status > /dev/null; then break; fi
    if ! kill -0 "${preview_pid}" 2>/dev/null; then cat "${RUNNER_TEMP}/node-preview.log"; exit 1; fi
    sleep 1
  done
  KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5183 node --test --test-name-pattern='anonymous map|hosted AI endpoint' tests/godaddy-node-runtime.test.mjs
}

echo "node $(node --version) | npm $(npm --version) | $(git rev-parse --short HEAD) | $(git status --porcelain | wc -l) uncommitted | logs ${logs}" | tee -a "${summary}"
step 01-npm-ci       npm ci
step 02-build        npm run build
step 03-typecheck    npx tsc --noEmit
step 04-node-suite   node --test --test-concurrency=4 tests/*.test.mjs
# CI supplies a disposable mysql:8.4.13 service on 127.0.0.1:13317; never point this at DB_* settings.
if (exec 3<>/dev/tcp/127.0.0.1/13317) 2>/dev/null; then
  step 05-mysql        env KFM_PIPELINE_MYSQL_TEST=1 KFM_MYSQL_TEST=1 node --test tests/pipeline-mysql.test.mjs tests/hosted-ingestion-mysql.test.mjs
else
  printf '%-22s %-9s %s\n' 05-mysql SKIPPED "no disposable MySQL on 127.0.0.1:13317" | tee -a "${summary}"
fi
step 06-http-boundary http_boundary
step 07-preview-port  preview_port
echo "overall: $([[ ${overall} -eq 0 ]] && echo PASS || echo FAIL)" | tee -a "${summary}"
exit "${overall}"
