#!/usr/bin/env bash
# Local mirror of .github/workflows/public-core-repair.yml (jobs verify-core-delivery and
# welcome-performance, run one after the other on a single build). Keep the steps below in
# step with that workflow. Unlike CI it runs every step after a failure, so one run reports
# all breakages, and it cleans up the servers it starts. Screenshots and measurements that
# CI uploads as artifacts stay in the log directory.
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

serve_build() {
  NODE_ENV=production PORT=5182 node server/start.mjs > "${RUNNER_TEMP}/$1" 2>&1 &
  site_pid=$!
  trap 'kill "${site_pid}" 2>/dev/null || true' EXIT
  for attempt in $(seq 1 30); do
    if curl --fail --silent http://127.0.0.1:5182/ > /dev/null; then break; fi
    sleep 1
  done
}

fire_renderer() {
  set -euo pipefail
  serve_build fire-runtime.log
  local baseline=1000a5c4521bb3055e3863110754e924cdda801e
  git cat-file -e "${baseline}^{commit}" 2>/dev/null || git fetch --no-tags --depth=1 origin "${baseline}"
  git show "${baseline}:app/fire-detection-style.ts" > "${RUNNER_TEMP}/fire-before.ts"
  KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5182 KFM_FIRE_BASELINE_FILE="${RUNNER_TEMP}/fire-before.ts" \
    KFM_FIRE_SCREENSHOTS="${RUNNER_TEMP}/fire-screenshots" node --test tests/fire-display.browser.mjs
}

http_boundary() {
  set -euo pipefail
  serve_build node-runtime.log
  for suite in godaddy-node-runtime.test.mjs pipeline-http.test.mjs river-pulse.browser.mjs \
    county-search.browser.mjs aviation-layout.browser.mjs; do
    KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5182 node --test "tests/${suite}"
  done
  KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5182 KFM_WORKSPACE_SCREENSHOTS="${RUNNER_TEMP}/workspace-screenshots" \
    node --test tests/explorer-startup.browser.mjs
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

# Separate job in CI; here it reuses the build above.
welcome_performance() {
  set -euo pipefail
  serve_build welcome-runtime.log
  KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5182 KFM_WELCOME_PERFORMANCE=1 KFM_WELCOME_PERFORMANCE_ARTIFACTS="${RUNNER_TEMP}/welcome-performance" \
    KFM_PERFORMANCE_SOURCE="$(git rev-parse HEAD)" node --test --test-name-pattern='welcome performance' tests/explorer-startup.browser.mjs
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
step 06-fire-renderer      fire_renderer
step 07-http-boundary      http_boundary
step 08-preview-port       preview_port
step 09-welcome-performance welcome_performance
echo "overall: $([[ ${overall} -eq 0 ]] && echo PASS || echo FAIL)" | tee -a "${summary}"
exit "${overall}"
