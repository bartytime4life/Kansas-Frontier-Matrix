#!/usr/bin/env bash
# Launch the built Site with serve-local.sh and check that its storage-backed
# routes answer from a migrated local D1 schema. Needs no provider network, and
# no answer here is evidence of hosted behaviour, data admission, or release.
set -euo pipefail

site_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
port="${SITE_PORT:-4173}"
base="http://127.0.0.1:${port}"
log="$(mktemp)"
# A throwaway D1/R2 state keeps the empty-store assertions independent of any
# records in the developer's persistent .wrangler/local-state.
state="$(mktemp -d)"

SITE_HOST=127.0.0.1 SITE_PORT="$port" SITE_STATE_DIR="$state" \
  setsid "$site_root/serve-local.sh" >"$log" 2>&1 &
server=$!
cleanup() {
  kill -TERM -- "-$server" 2>/dev/null || true
  wait "$server" 2>/dev/null || true
  rm -rf "$log" "$state"
}
trap cleanup EXIT

for _ in $(seq 1 120); do
  if curl -fs -o /dev/null "$base/"; then break; fi
  if ! kill -0 "$server" 2>/dev/null; then
    cat "$log" >&2
    printf 'serve-local.sh exited before the Site answered.\n' >&2
    exit 1
  fi
  sleep 1
done

failures=0
# expect PATH STATUS [JSON-FIELD EXPECTED-VALUE]
expect() {
  local path="$1" status="$2" field="${3:-}" want="${4:-}" body code got
  body="$(mktemp)"
  code="$(curl -sS -m 30 -o "$body" -w '%{http_code}' "$base$path" || true)"
  got=""
  if [[ -n "$field" ]]; then
    got="$(node -e '
      let value;
      try { value = JSON.parse(require("fs").readFileSync(process.argv[1], "utf8")); } catch { process.exit(0); }
      for (const key of process.argv[2].split(".")) value = value?.[key];
      process.stdout.write(String(value ?? ""));' "$body" "$field")"
  fi
  if [[ "$code" == "$status" && "$got" == "$want" ]]; then
    printf 'ok   %s %s %s\n' "$code" "$path" "$got"
  else
    printf 'FAIL %s %s (wanted %s %s=%s, got %s=%s)\n' "$code" "$path" "$status" "$field" "$want" "$field" "$got" >&2
    head -c 400 "$body" >&2; printf '\n' >&2
    failures=$((failures + 1))
  fi
  rm -f "$body"
}

expect / 200
expect /api/governed/v1/bootstrap 200 envelope.reason_code NO_APPROVED_SNAPSHOT
expect /api/governed/v1/layers 200 envelope.reason_code NO_APPROVED_SNAPSHOT
expect /api/governed/v1/evidence 200 envelope.reason_code NO_APPROVED_SNAPSHOT
expect /api/governed/v1/unknown-view 404 envelope.reason_code ROUTE_NOT_FOUND
expect /api/governed/v1/knowledge 200 envelope.reason_code NO_APPROVED_KNOWLEDGE
expect /api/crop-casma/availability 200 code NO_APPROVED_SOIL_PACKAGE
expect /api/data-submissions 401

if (( failures > 0 )); then
  printf '%d local Site backend check(s) failed.\n' "$failures" >&2
  exit 1
fi
printf 'Local Site backend checks passed.\n'
