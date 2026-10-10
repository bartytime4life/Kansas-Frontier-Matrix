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
  acquisition acquisition/terrain
  3dep-dem-tile airflow-tile blm-plss-records bridge-records
  crop-casma/availability crop-casma/preview crop-casma/tile
  daily-archive data-submissions "data-submissions/[id]"
  "earth-engine-context/[setId]/[layerId]/[...tile]" earth-engine-context/activate
  earth-engine-context/active earth-engine-context/catalog earth-engine-context/stage
  event-atlas/counties event-atlas/geology-legend event-atlas/manifest
  event-atlas/resources event-atlas/storms event-atlas/weather
  "governed/v1/[view]" governed/v1/knowledge
  governed/water-admin/activate governed/water-admin/stage governed/water-admin/status governed/water-admin/withdraw
  historical-topo historical-topo/activate historical-topo/overlay historical-topo/queue
  historical-topo/review "historical-topo/review/tiles/[scan]/[package]/[z]/[x]/[y]"
  historical-topo/stage "historical-topo/tiles/[scan]/[package]/[z]/[x]/[y]"
  hydrology/coverage hydrology/direction hydrology/flowlines hydrology/noaa hydrology/streamflow
  lightning/archive lightning/flashes live-context public-maps/preview qwen
  soil-moisture/availability soil-moisture/tile source-download subsurface/soil subsurface/resources
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
# Refuse a busy port before starting migrations or issuing any HTTP request.
# Otherwise an existing operator Site can satisfy the first readiness probe.
node --input-type=module - "$port" <<'NODE'
import { createServer } from "node:net";
const raw = process.argv[2];
const port = Number(raw);
if (!/^[1-9][0-9]{3,4}$/.test(raw) || port < 1024 || port > 65535) {
  console.error("SITE_PORT must be an integer from 1024 through 65535.");
  process.exit(1);
}
const probe = createServer();
probe.once("error", (error) => {
  console.error(error.code === "EADDRINUSE"
    ? `Local smoke port ${port} is already in use; select an unused SITE_PORT.`
    : `Local smoke port cannot be reserved: ${error.code ?? "UNKNOWN"}`);
  process.exitCode = 1;
});
probe.listen({ host: "127.0.0.1", port, exclusive: true }, () => probe.close());
NODE
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

ready=0
for _ in $(seq 1 120); do
  if ! kill -0 "$server" 2>/dev/null; then
    cat "$log" >&2
    printf 'serve-local.sh exited before the Site answered.\n' >&2
    exit 1
  fi
  if curl -fs --connect-timeout 1 --max-time 2 -o /dev/null "$base/" && kill -0 "$server" 2>/dev/null; then
    ready=1
    break
  fi
  sleep 1
done
if (( ready == 0 )); then
  cat "$log" >&2
  printf 'Local smoke server did not become ready; no route assertions were run.\n' >&2
  exit 1
fi

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
expect GET /daily-archive 200
expect GET /api/daily-archive 200 storage.used 0
expect POST /api/daily-archive 403

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
expect GET '/api/crop-casma/preview?unsupported=1' 400 code INVALID_REQUEST
expect GET /api/crop-casma/tile 400 code INVALID_TILE_REQUEST
expect GET '/api/event-atlas/counties?edition=1999' 400
expect GET '/api/event-atlas/geology-legend?unsupported=1' 400
expect GET /api/event-atlas/manifest 400
expect GET '/api/event-atlas/resources?edition=1900' 400
expect GET /api/event-atlas/weather 400
expect GET /api/event-atlas/storms 400
expect GET '/api/event-atlas/storms?time=1999-01-01T00%3A00%3A00Z' 400
expect GET /api/historical-topo 400 state error
expect GET /api/hydrology/coverage 400
expect GET /api/hydrology/direction 400
expect GET /api/hydrology/flowlines 400
expect GET '/api/hydrology/flowlines?cell=-97.10,38.00' 400
expect GET '/api/hydrology/noaa?mode=unsupported' 400 error.code INVALID_MODE
expect GET /api/hydrology/streamflow 400 code USGS_STREAMFLOW_INVALID_QUERY
expect GET /api/lightning/archive 400
expect GET '/api/lightning/flashes?minutes=7' 400 state error
expect GET /api/live-context 400
expect GET /api/public-maps/preview 400
expect GET '/api/soil-moisture/availability?retry=2' 400 code INVALID_REQUEST
expect GET /api/soil-moisture/tile 400 code INVALID_TILE_REQUEST
expect GET /api/source-download 400
expect GET /api/subsurface/soil 400 error "A Kansas coordinate is required."
expect GET /api/subsurface/resources 400 error "Choose a local Kansas area and resource type."
expect GET /api/terrain-tile 400
expect GET /api/wind-arrows 400

# Signed-out readers and owner routes are refused.
expect GET /api/acquisition 401
expect POST /api/acquisition 401
expect GET /api/acquisition/terrain 401
expect POST /api/acquisition/terrain 401
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
expect GET /api/governed/water-admin/status 401 reason_code SIGN_IN_REQUIRED

# Writes without this Site's origin are refused before authentication.
expect POST /api/data-submissions 403
expect PATCH /api/data-submissions/unknown 403
expect POST /api/historical-topo/overlay 403
expect POST /api/historical-topo/activate 403
expect POST /api/governed/water-admin/activate 403 reason_code SAME_ORIGIN_REQUIRED
expect POST /api/governed/water-admin/withdraw 403 reason_code SAME_ORIGIN_REQUIRED

# Features whose secret or endpoint is unset stay closed.
expect GET /api/historical-topo/queue 503
expect PUT /api/historical-topo/stage 503
expect POST /api/governed/water-admin/stage 503 reason_code WATER_STAGING_NOT_CONFIGURED
expect POST /api/qwen 503 status disabled '{"question":"Where is Topeka?","context":{}}'

if (( failures > 0 )); then
  printf '%d of %d local Site backend checks failed.\n' "$failures" "$checks" >&2
  exit 1
fi
printf 'Local Site backend checks passed: %d checks across %d routes; %d provider-only routes listed.\n' \
  "$checks" "${#smoke_routes[@]}" "${#network_routes[@]}"
