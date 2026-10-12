# Reviewed earthquakes (USGS ComCat)

This documents the owner-private Site's reviewed earthquake layer (ADR-0049).
It follows the reviewed water, weather, soil and storm events boundaries
(`docs/governed-water.md`, `docs/governed-weather.md`, `docs/governed-soil.md`,
`docs/governed-storm-events.md`) and never shares a table, object prefix, route
or decision with them. A Site deployment alone does not establish that a real
earthquake package is active.

Records are USGS ANSS Comprehensive Catalog (ComCat) earthquake solutions whose
epicenter lies in the Kansas context envelope (-102.1 to -94.5 longitude, 36.9
to 40.1 latitude): origin time, epicenter, depth and magnitude as ComCat
published them at retrieval. They are not shaking estimates, damage or felt
reports, alerts or attributions of cause, and the layer says so wherever it
shows them. The envelope is not the state boundary; records outside a coarse
Kansas rectangle carry `CONTEXT_MARGIN` and are drawn hollow.

`app/governed-earthquakes.ts` verifies the bounded earthquake snapshot carrier
(`kfm.earthquake-snapshot/v1`). A package covers one calendar data year, at most
6000 events, with one evidence bundle per UTC origin month that has events,
split into numbered parts of 127 records. It projects the same
bootstrap/layers/evidence responses as the monorepo Python API. It re-applies
the Python candidate validator's rules:
- the closed record schema and captured record and candidate digests;
- event identities, alias uniqueness, order and UTC times;
- the number form: coordinates, depth and magnitude at four decimal places,
  written as integers when whole, judged on the captured token so `5.0` for `5`
  is refused as Python refuses it;
- review flags (including `CONTEXT_MARGIN`), the month summary, withheld
  counts and the year state;
- the exact validation receipt.

It also rebuilds the catalog and refuses a package whose catalog differs, so
the year summary it serves cannot be misreported. The gate accepts only
`kfm.earthquake-release-decision/v1` decisions and the admitted ComCat license.
Other families' decisions are refused with `RELEASE_BINDING_MISMATCH`.

The Python release code generates the Site fixtures in
`tests/fixtures/governed-earthquakes/`, and `tests/governed-earthquakes.test.mjs`
requires identical responses. `tools/fixtures/earthquake_site_fixtures.py` in
the repository checks that the committed fixtures still match (`--write`
regenerates them after an intended change).

## Routes

- **Read routes:** `GET /api/governed/earthquakes/v1/{bootstrap,layers,evidence}`,
  optionally with one `?month=` (exactly `1` to `12`; no leading zeros; UTC
  origin month).
  - Reads the active package from R2 (`governed-earthquakes/v1/objects/`) and
    D1 (`earthquakes_active`, `earthquakes_packages`), then evaluates the gate
    after the storage read.
  - Bootstrap lists the months with events.
  - Layers returns that month's earthquakes, with a `selection` summary of
    exactly those records beside the year-level `dataset` summary.
  - Evidence returns every part of the month.
  - A month without events answers `EVIDENCE_NOT_FOUND`.
- **Staging:** `POST /api/governed/earthquakes-admin/stage` (staging token)
  validates and stores an earthquake package as `STAGED`. It never activates
  and refuses other families' packages.
- **Status:** `GET /api/governed/earthquakes-admin/status` (owner or staging
  token) returns the active and previous package ids, the revision and the
  decision's `expires_at`.
- **Activation:** `POST /api/governed/earthquakes-admin/activate` and
  `.../withdraw` (signed-in owner, same origin) handle compare-and-swap
  activation, rollback and withdrawal, each recorded in
  `earthquakes_activation_events`.

The routes use the Site's existing release owner list (`KFM_WATER_OWNER_IDS` /
`KFM_WATER_OWNER_EMAILS`) and staging token (`KFM_WATER_WORKER_TOKEN`). No new
setting is needed. Additive migration `0009_governed_earthquakes.sql` creates
the earthquake metadata tables only and activates nothing.

## Map control and release page

"Reviewed earthquakes" in the layer catalog reads one month at a time.
- **Map:** every epicenter is drawn as a point sized by magnitude (an event
  without a magnitude draws smallest). Automatic solutions are lighter;
  points outside the Kansas rectangle are hollow. A dot marks where a rupture
  began, never a shaking or damage area.
- **Lists:** the control shows the month's count, how many lie outside the
  Kansas rectangle, the magnitude range, review-status counts and the 25
  strongest earthquakes with origin time, magnitude and type, depth, USGS place
  text and status. A missing magnitude or depth shows as "Not reported".
- **Release details:** it lists the data year and whether it is closed, the
  retrieval, review and release times, the month's ComCat query and each
  part's evidence reference.
- **Evidence:** evidence must be every part of the selected month from the
  same release.
- **Export:** a fresh one-month export is withheld if the month changes while
  it is in flight.

The owner releases packages at `/governed/earthquakes-release`.

Local conformance: `node --test tests/governed-earthquakes*.test.mjs`.

Rollback before activation is to leave the earthquake tables empty; the layer
then answers `NO_APPROVED_SNAPSHOT`. After activation, roll back to the
previous package or withdraw the active one from the release page.
