#!/bin/sh
set -eu

# Tests for tools/ci/check_crosswalk_static.sh

ROOT="${1:-.}"
CHECK_SCRIPT="$ROOT/tools/ci/check_crosswalk_static.sh"

fail() {
  echo "test_check_crosswalk_static: FAIL: $*" >&2
  exit 1
}

pass() {
  echo "test_check_crosswalk_static: PASS: $*"
}

# Ensure the check script exists and is executable
test -f "$CHECK_SCRIPT" || fail "missing $CHECK_SCRIPT"
test -x "$CHECK_SCRIPT" || chmod +x "$CHECK_SCRIPT"

# -------------------------------------------------------------------
# Test 1: happy path (should pass if lane files exist and are valid)
# -------------------------------------------------------------------
if sh "$CHECK_SCRIPT" "$ROOT" >/dev/null 2>&1; then
  pass "happy path"
else
  echo "---- stdout/stderr from check_crosswalk_static ----"
  sh "$CHECK_SCRIPT" "$ROOT" || true
  fail "happy path failed"
fi

# -------------------------------------------------------------------
# Test 2: missing file detection (should fail)
# -------------------------------------------------------------------
TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT

# Copy minimal tree
mkdir -p "$TMPDIR/tools/ci"
cp "$CHECK_SCRIPT" "$TMPDIR/tools/ci/check_crosswalk_static.sh"

# Intentionally omit required files
if sh "$TMPDIR/tools/ci/check_crosswalk_static.sh" "$TMPDIR" >/dev/null 2>&1; then
  fail "missing file test did not fail as expected"
else
  pass "missing file detection"
fi

# -------------------------------------------------------------------
# Test 3: invalid JSON detection
# -------------------------------------------------------------------
mkdir -p "$TMPDIR/schemas/contracts/v1/crosswalk"
echo '{ invalid json' > "$TMPDIR/schemas/contracts/v1/crosswalk/crosswalk_pair.schema.json"

# Create required placeholders so failure is specifically JSON
mkdir -p "$TMPDIR/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/sql"
mkdir -p "$TMPDIR/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/fixtures"
mkdir -p "$TMPDIR/data/registry/crosswalk"
mkdir -p "$TMPDIR/policy/crosswalk"
mkdir -p "$TMPDIR/tools/validators/crosswalk"
mkdir -p "$TMPDIR/tests/crosswalk"

touch "$TMPDIR/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/README.md"
touch "$TMPDIR/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/runner.py"
touch "$TMPDIR/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/ingest_wbd.py"
touch "$TMPDIR/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/ingest_tiger_admin.py"
touch "$TMPDIR/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/sql/001_schema.sql"
touch "$TMPDIR/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/sql/010_build_crosswalk.sql"
touch "$TMPDIR/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/fixtures/create_fixture.sql"
touch "$TMPDIR/policy/crosswalk/crosswalk.rego"
touch "$TMPDIR/data/registry/crosswalk/sources.yaml"
touch "$TMPDIR/tools/validators/crosswalk/validate_crosswalk_sql.sql"
touch "$TMPDIR/tests/crosswalk/test_crosswalk_fixture.py"

if sh "$TMPDIR/tools/ci/check_crosswalk_static.sh" "$TMPDIR" >/dev/null 2>&1; then
  fail "invalid JSON test did not fail"
else
  pass "invalid JSON detection"
fi

# -------------------------------------------------------------------
# Test 4: python syntax error detection
# -------------------------------------------------------------------
echo 'def broken(' > "$TMPDIR/pipelines/watchers/hydrology_huc12_admin_crosswalk_watch/runner.py"

if sh "$TMPDIR/tools/ci/check_crosswalk_static.sh" "$TMPDIR" >/dev/null 2>&1; then
  fail "python syntax error test did not fail"
else
  pass "python syntax error detection"
fi

echo "test_check_crosswalk_static: completed"
