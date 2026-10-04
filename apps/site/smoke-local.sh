#!/usr/bin/env bash
# Launch the built Site with serve-local.sh and check that every API route that
# can answer without a provider is mounted and gives its deliberate offline
# answer: storage-backed reads from a migrated empty local D1 schema, and
# validation, sign-in, same-origin or not-configured refusals elsewhere. Needs
# no provider network, and no answer here is evidence of hosted behaviour,
# data admission, or release.
set -euo pipefail

site_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
api_root="$site_root/source/app/api"

# Every app/api route must appear in exactly one list, so a new route cannot
# go unchecked by accident. Routes in smoke_routes are exercised below.
smoke_routes=(
  3dep-dem-tile airflow-tile blm-plss-records bridge-records
  crop-casma/availability crop-casma/tile
  data-submissions "data-submissions/[id]"
  "earth-engine-context/[setId]/[layerId]/[...tile]" earth-engine-context/activate
  earth-engine-context/active earth-engine-context/catalog earth-engine-context/stage
  event-atlas/counties event-atlas/geology-legend event-atlas/manifest
  event-atlas/resources event-atlas/weather
  "governed/v1/[view]" governed/v1/knowledge
  historical-topo historical-topo/activate historical-topo/overlay historical-topo/queue
  historical-topo/review "historical-topo/review/tiles/[scan]/[package]/[z]/[x]/[y]"
  historical-topo/stage "historical-topo/tiles/[scan]/[package]/[z]/[x]/[y]"
  hydrology/coverage hydrology/direction hydrology/noaa hydrology/streamflow
  lightning/archive lightning/flashes live-context qwen
  soil-moisture/availability soil-moisture/tile source-download
  terrain-tile wind-arrows
)
# These have no request they refuse with a distinct status before contacting
# their provider: they take no input, fetch a provider manifest first, or report
# invalid input and provider failure alike as 502. An offline check cannot tell
# a healthy route from a broken one.
network_routes=(
  event-atlas/radar-frame event-atlas/tile
  lightning/frames lightning/legend lightning/preview
  "lightning/tiles/[frame]/[z]/[x]/[y]" noaa-radar/frames noaa-satellite/frames
  repository-status
)
inventory_drift="$(diff \
  <(cd "$api_root" && find . -name route.ts | sed 's|^\./||; s|/route\.ts$||' | LC_ALL=C sort) \
  <(printf '%s\n' "${smoke_routes[@]}" "${network_routes[@]}" | LC_ALL=C sort) || true)"
if [[ -n "$inventory_drift" ]]; then
  printf 'API route inventory drift (< route files, > listed here):\n%s\n' "$inventory_drift" >&2
  printf 'Add each route to smoke_routes with a check below, or to network_routes.\n' >&2
  exit 1
fi

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
checks=0
# expect METHOD PATH STATUS [JSON-FIELD EXPECTED-VALUE [JSON-BODY]]
expect() {
  local method="$1" path="$2" status="$3" field="${4:-}" want="${5:-}" json="${6:-}" body code got
  body="$(mktemp)"
  local -a request=(-sS -m 30 -X "$method" -o "$body" -w '%{http_code}')
  [[ -z "$json" ]] || request+=(-H 'content-type: application/json' --data "$json")
  code="$(curl "${request[@]}" "$base$path" || true)"
  got=""
  if [[ -n "$field" ]]; then
    got="$(node -e '
      let value;
      try { value = JSON.parse(require("fs").readFileSync(process.argv[1], "utf8")); } catch { process.exit(0); }
      for (const key of process.argv[2].split(".")) value = value?.[key];
      process.stdout.write(String(value ?? ""));' "$body" "$field")"
  fi
  checks=$((checks + 1))
  if [[ "$code" == "$status" && "$got" == "$want" ]]; then
    printf 'ok   %s %-6s %s %s\n' "$code" "$method" "$path" "$got"
  else
    printf 'FAIL %s %-6s %s (wanted %s %s=%s, got %s=%s)\n' "$code" "$method" "$path" "$status" "$field" "$want" "$field" "$got" >&2
    head -c 400 "$body" >&2; printf '\n' >&2
    failures=$((failures + 1))
  fi
  rm -f "$body"
}

expect GET / 200

# Storage-backed reads answer from the empty migrated D1 schema.
expect GET /api/governed/v1/bootstrap 200 envelope.reason_code NO_APPROVED_SNAPSHOT
expect GET /api/governed/v1/layers 200 envelope.reason_code NO_APPROVED_SNAPSHOT
expect GET /api/governed/v1/evidence 200 envelope.reason_code NO_APPROVED_SNAPSHOT
expect GET /api/governed/v1/unknown-view 404 envelope.reason_code ROUTE_NOT_FOUND
expect GET /api/governed/v1/knowledge 200 envelope.reason_code NO_APPROVED_KNOWLEDGE
expect GET /api/crop-casma/availability 200 code NO_APPROVED_SOIL_PACKAGE

# Missing or invalid parameters are refused before any upstream call.
expect GET /api/3dep-dem-tile 400
expect GET /api/airflow-tile 400
expect GET /api/blm-plss-records 400 state error
expect GET /api/bridge-records 400 state error
expect GET /api/crop-casma/tile 400 code INVALID_TILE_REQUEST
expect GET '/api/event-atlas/counties?edition=1999' 400
expect GET '/api/event-atlas/geology-legend?unsupported=1' 400
expect GET /api/event-atlas/manifest 400
expect GET '/api/event-atlas/resources?edition=1900' 400
expect GET /api/event-atlas/weather 400
expect GET /api/historical-topo 400 state error
expect GET /api/hydrology/coverage 400
expect GET /api/hydrology/direction 400
expect GET '/api/hydrology/noaa?mode=unsupported' 400 error.code INVALID_MODE
expect GET /api/hydrology/streamflow 400 code USGS_STREAMFLOW_INVALID_QUERY
expect GET /api/lightning/archive 400
expect GET '/api/lightning/flashes?minutes=7' 400 state error
expect GET /api/live-context 400
expect GET '/api/soil-moisture/availability?retry=2' 400 code INVALID_REQUEST
expect GET /api/soil-moisture/tile 400 code INVALID_TILE_REQUEST
expect GET /api/source-download 400
expect GET /api/terrain-tile 400
expect GET /api/wind-arrows 400

# Signed-out readers and owner routes are refused.
expect GET /api/data-submissions 401
expect GET /api/data-submissions/unknown 401
expect GET /api/earth-engine-context/catalog 401
expect GET /api/earth-engine-context/active 401
expect GET /api/earth-engine-context/set/layer/0/0/0.png 401
expect POST /api/earth-engine-context/activate 401
expect PUT /api/earth-engine-context/stage 401
expect GET /api/historical-topo/overlay 401
expect GET /api/historical-topo/review 401
expect GET /api/historical-topo/review/tiles/1/package/0/0/0.png 401
expect GET /api/historical-topo/tiles/1/package/0/0/0.png 401

# Writes without this Site's origin are refused before authentication.
expect POST /api/data-submissions 403
expect PATCH /api/data-submissions/unknown 403
expect POST /api/historical-topo/overlay 403
expect POST /api/historical-topo/activate 403

# Features whose secret or endpoint is unset stay closed.
expect GET /api/historical-topo/queue 503
expect PUT /api/historical-topo/stage 503
expect POST /api/qwen 503 status not_configured '{"question":"Where is Topeka?","context":{}}'

if (( failures > 0 )); then
  printf '%d of %d local Site backend checks failed.\n' "$failures" "$checks" >&2
  exit 1
fi
printf 'Local Site backend checks passed: %d checks across %d routes; %d provider-only routes listed.\n' \
  "$checks" "${#smoke_routes[@]}" "${#network_routes[@]}"
