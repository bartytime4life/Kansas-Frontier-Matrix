# Reviewed daily weather (NOAA GHCN-Daily)

This documents the owner-private Site's reviewed-weather layer (ADR-0045). It
follows the reviewed-water boundary (`docs/governed-water.md`) and never shares
a table, object prefix, route or decision with it. A Site deployment alone does
not establish that a real weather package is active.

`app/governed-weather.ts` verifies the bounded weather snapshot carrier
(`kfm.weather-snapshot/v1`: four fixed first-order stations, PRCP/TMAX/TMIN, a
30-day station-local window, at most 360 observations) and projects the same
bootstrap/layers/evidence responses as the monorepo Python API. Withheld values
(missing or quality-flagged) stay `null` and are never shown as zero. The weather
gate accepts only `kfm.weather-release-decision/v1` decisions and the admitted
NOAA license; a water decision is refused with `RELEASE_BINDING_MISMATCH`.

The Python release code generates the Site fixtures in
`tests/fixtures/governed-weather/`, and `tests/governed-weather.test.mjs` requires
identical responses. `tools/fixtures/weather_site_fixtures.py` in the repository
checks that the committed fixtures still match (`--write` regenerates them after
an intended change).

## Routes

- `GET /api/governed/weather/v1/{bootstrap,layers,evidence}`, optionally with one
  `?station_id=` from the four stations. Reads the active weather package from
  R2 (`governed-weather/v1/objects/`) and D1 (`weather_active`,
  `weather_packages`), then evaluates the gate after the storage read.
- `POST /api/governed/weather-admin/stage` (staging token): validates and stores a
  weather package as `STAGED`; never activates; refuses water packages.
- `GET /api/governed/weather-admin/status` (owner or staging token): active and
  previous weather package ids, revision and the decision's `expires_at`.
- `POST /api/governed/weather-admin/activate` and `.../withdraw` (signed-in owner,
  same origin): compare-and-swap activation, rollback and withdrawal, each
  recorded in `weather_activation_events`.

The weather routes use the Site's existing release owner list
(`KFM_WATER_OWNER_IDS` / `KFM_WATER_OWNER_EMAILS`) and staging token
(`KFM_WATER_WORKER_TOKEN`); no new setting is needed. Additive migration
`0006_governed_weather.sql` creates the weather metadata tables only and
activates nothing.

## Map control and release page

"Reviewed daily weather" in Weather & hazards shows the four stations; a station
that stopped reporting before the window ended is drawn hollow. For the selected
station it shows the latest station-local day's precipitation, high and low,
marks the data preliminary, and lists retrieval, review and release times with
the NOAA NCEI source. Evidence must belong to the selected station and the same
release, and a fresh single-station export is withheld if the selection changes
while it is in flight. The owner releases packages at `/governed/weather-release`.

Local conformance: `node --test tests/governed-weather*.test.mjs`.

Rollback before activation is to leave the weather tables empty; the layer then
answers `NO_APPROVED_SNAPSHOT`. After activation, roll back to the previous
package or withdraw the active one from the release page.
