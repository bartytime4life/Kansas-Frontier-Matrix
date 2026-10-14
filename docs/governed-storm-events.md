# Reviewed storm event reports (NOAA Storm Events)

This documents the owner-private Site's reviewed storm events layer (ADR-0047).
It follows the reviewed water, weather and soil boundaries
(`docs/governed-water.md`, `docs/governed-weather.md`, `docs/governed-soil.md`)
and never shares a table, object prefix, route or decision with them. A Site
deployment alone does not establish that a real storm events package is
active.

Records are historical National Weather Service event reports from the NOAA
NCEI Storm Events Database: what an office reported, by county or forecast
zone, over a local-time window. They are not warnings, measurements, damage
footprints or declarations, and the layer says so wherever it shows them.
Narratives are never carried.

`app/governed-storm-events.ts` verifies the bounded storm events snapshot
carrier (`kfm.storm-events-snapshot/v1`). A package covers one calendar data
year of Kansas (`STATE_FIPS` 20) rows, at most 5000 events, with one evidence
bundle per month that has events, split into numbered parts of 127 records. It
projects the same bootstrap/layers/evidence responses as the monorepo Python
API. It re-applies the Python candidate validator's rules:
- the closed record schema and captured record and candidate digests;
- event identities, order, local and UTC times;
- damage re-parsed exactly from NCEI's strings, with blank kept unreported,
  never zero;
- review flags, withheld-row counts, the file vintage and freshness;
- the exact validation receipt.

It also rebuilds the catalog and refuses a package whose catalog differs, so
the year summary it serves cannot be misreported. The gate accepts only
`kfm.storm-events-release-decision/v1` decisions and the admitted Storm Events
license. Other families' decisions are refused with `RELEASE_BINDING_MISMATCH`.

The Python release code generates the Site fixtures in
`tests/fixtures/governed-storm-events/`, and
`tests/governed-storm-events.test.mjs` requires identical responses.
`tools/fixtures/storm_events_site_fixtures.py` in the repository checks that the
committed fixtures still match (`--write` regenerates them after an intended
change).

## Routes

- **Read routes:** `GET /api/governed/storm-events/v1/{bootstrap,layers,evidence}`,
  optionally with one `?month=` (exactly `1` to `12`; no leading zeros).
  - Reads the active package from R2 (`governed-storm-events/v1/objects/`) and
    D1 (`storm_events_active`, `storm_events_packages`), then evaluates the gate
    after the storage read.
  - Bootstrap lists the months with events.
  - Layers returns that month's events, with a `selection` summary of exactly
    those records beside the year-level `dataset` summary.
  - Evidence returns every part of the month.
  - A month without events answers `EVIDENCE_NOT_FOUND`.
- **Staging:** `POST /api/governed/storm-events-admin/stage` (staging token)
  validates and stores a storm events package as `STAGED`. It never activates
  and refuses other families' packages.
- **Status:** `GET /api/governed/storm-events-admin/status` (owner or staging
  token) returns the active and previous package ids, the revision and the
  decision's `expires_at`.
- **Activation:** `POST /api/governed/storm-events-admin/activate` and
  `.../withdraw` (signed-in owner, same origin) handle compare-and-swap
  activation, rollback and withdrawal, each recorded in
  `storm_events_activation_events`.

The routes use the Site's existing release owner list (`KFM_WATER_OWNER_IDS` /
`KFM_WATER_OWNER_EMAILS`) and staging token (`KFM_WATER_WORKER_TOKEN`). No new
setting is needed. Additive migration `0008_governed_storm_events.sql` creates
the storm events metadata tables only and activates nothing.

## Map control and release page

"Reviewed storm event reports" in the layer catalog reads one month at a time.
- **Map:** events with a reported begin point are drawn there and colored by
  type. Zone-only events are listed but not drawn. A dot marks where a report
  began, never a path or area.
- **Lists:** the control shows the month's event-type counts and its first 25
  events with county or zone, magnitude and property damage. Unreported damage
  shows as "Not reported".
- **Release details:** it lists the NCEI source file and vintage, the
  retrieval, review and release times, the NCEI source and each part's evidence
  reference.
- **Evidence:** evidence must be every part of the selected month from the
  same release.
- **Export:** a fresh one-month export is withheld if the month changes while
  it is in flight.

The owner releases packages at `/governed/storm-events-release`.

Local conformance: `node --test tests/governed-storm-events*.test.mjs`.

Rollback before activation is to leave the storm events tables empty; the layer
then answers `NO_APPROVED_SNAPSHOT`. After activation, roll back to the
previous package or withdraw the active one from the release page.
