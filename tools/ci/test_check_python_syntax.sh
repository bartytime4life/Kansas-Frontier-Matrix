#!/bin/sh
set -eu

tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT

ok_file="$tmpdir/ok.py"
bad_file="$tmpdir/bad.py"
manifest_ok="$tmpdir/manifest_ok.txt"
manifest_bad="$tmpdir/manifest_bad.txt"
manifest_missing="$tmpdir/manifest_missing.txt"

cat > "$ok_file" <<'PY'
value = 1
PY

cat > "$bad_file" <<'PY'
def broken(:
    pass
PY

printf '%s\n' "$ok_file" > "$manifest_ok"
printf '%s\n' "$ok_file" "$bad_file" > "$manifest_bad"
printf '%s\n' "$ok_file" "$tmpdir/not-found.py" > "$manifest_missing"

./tools/ci/check_python_syntax.sh --manifest "$manifest_ok" >/dev/null

if ./tools/ci/check_python_syntax.sh --manifest "$manifest_bad" >/dev/null 2>&1; then
  echo "expected syntax check to fail for invalid python file" >&2
  exit 1
fi

if ./tools/ci/check_python_syntax.sh --manifest "$manifest_missing" >/dev/null 2>&1; then
  echo "expected syntax check to fail for missing file" >&2
  exit 1
fi

echo "check_python_syntax tests passed"
