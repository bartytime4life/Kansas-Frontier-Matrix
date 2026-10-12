# Reviewed soil moisture (NOAA USCRN)

This documents the owner-private Site's reviewed-soil layer (ADR-0046). It
follows the reviewed-water and reviewed-weather boundaries
(`docs/governed-water.md`, `docs/governed-weather.md`) and never shares a table,
object prefix, route or decision with them. A Site deployment alone does not
establish that a real soil package is active.

`app/governed-soil.ts` verifies the bounded soil snapshot carrier
(`kfm.soil-snapshot/v1`: the two Kansas USCRN stations, daily soil moisture and
soil temperature at 5, 10, 20, 50 and 100 cm, a 30-day local-standard-time
window, at most 600 observations, one evidence bundle per station and depth)
and projects the same bootstrap/layers/evidence responses as the monorepo
Python API. It re-applies the Python candidate validator's rules: the closed
record schema, NOAA's daily01 token form, values re-derived from their tokens,
complete station-days, record order and capture-time freshness. Withheld values
(missing or physically impossible) stay `null` and are never shown as zero. The
soil gate accepts only `kfm.soil-release-decision/v1` decisions and the
admitted USCRN license; water and weather decisions are refused with
`RELEASE_BINDING_MISMATCH`.

The Python release code generates the Site fixtures in
`tests/fixtures/governed-soil/`, and `tests/governed-soil.test.mjs` requires
identical responses. `tools/fixtures/soil_site_fixtures.py` in the repository
checks that the committed fixtures still match (`--write` regenerates them after
an intended change).

## Routes

- `GET /api/governed/soil/v1/{bootstrap,layers,evidence}`, optionally with one
  `?station_id=` (`53974` or `03067`). Reads the active soil package from R2
  (`governed-soil/v1/objects/`) and D1 (`soil_active`, `soil_packages`), then
  evaluates the gate after the storage read. The evidence view returns the
  station's five depth bundles.
- `POST /api/governed/soil-admin/stage` (staging token): validates and stores a
  soil package as `STAGED`; never activates; refuses water and weather packages.
- `GET /api/governed/soil-admin/status` (owner or staging token): active and
  previous soil package ids, revision and the decision's `expires_at`.
- `POST /api/governed/soil-admin/activate` and `.../withdraw` (signed-in owner,
  same origin): compare-and-swap activation, rollback and withdrawal, each
  recorded in `soil_activation_events`.

The soil routes use the Site's existing release owner list
(`KFM_WATER_OWNER_IDS` / `KFM_WATER_OWNER_EMAILS`) and staging token
(`KFM_WATER_WORKER_TOKEN`); no new setting is needed. Additive migration
`0007_governed_soil.sql` creates the soil metadata tables only and activates
nothing.

## Map control and release page

"Reviewed soil moisture" in the layer catalog shows the two stations; a station
whose soil moisture stopped before the window ended is drawn hollow. For the
selected station it shows the latest day's soil moisture and temperature at
each depth, says the values describe one station point and may be revised, and
lists retrieval, review and release times with the NOAA NCEI source and each
depth's evidence reference. Evidence must be the selected station's five depth
bundles from the same release, and a fresh single-station export is withheld if
the selection changes while it is in flight. The owner releases packages at
`/governed/soil-release`.

Local conformance: `node --test tests/governed-soil*.test.mjs`.

Rollback before activation is to leave the soil tables empty; the layer then
answers `NO_APPROVED_SNAPSHOT`. After activation, roll back to the previous
package or withdraw the active one from the release page.
