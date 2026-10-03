# Local imagery recovery, transport context and HMS playback

These changes belong to the standalone Site's existing app, scripts, tests and
behavior documentation. Directory Rules v2 §10.1 and ADR-0029 assign interface
behavior to the application; this adds no canonical source, schema or proof root.
Hosted access, data admission and publication remain separate from local preview.

## Earth Engine

The local preview previously returned HTTP 401 from its imagery catalog. Its
local R2 bucket also had no installed imagery objects. The saved reviewed set
`ks-2024-853d5dd49991dd281119` retains five approved visual-context products.
Its manifest SHA-256 is
`1e0dd252204fc525b8aabb8935cf869b922e0fc2666161d04c3c500211a550d1`.

A loopback-only operator may opt into read-only installed imagery with the local
Worker binding `KFM_LOCAL_REVIEWED_IMAGERY_ORIGIN=http://127.0.0.1:4173`.
This setting is absent from committed and hosted configuration. It permits only
GET catalog/active/tile paths on that exact origin; cross-site requests fail.
It depends on binding the local server to 127.0.0.1, not a LAN/public listener.
It does not authenticate an owner or permit installer, stage or activation writes.
All reads still require an installed active pointer and valid manifest/index/tile
hashes. Hosted reads still require the owner. Remove the local binding to revoke
this local operator read capability.

With the local Explorer stopped, `scripts/earth-engine/restore-local-display.mjs`
verifies the explicit reviewed package before copying immutable objects into
its existing local R2 store. It refuses conflicting objects or a different active
pointer. `--package PATH --reviewed-set SET_ID` validates only; adding
`--persist-to PATH/.wrangler/local-state/v3/r2` restores a previously reviewed
2024 pointer after object readback. No remote data or credentials are accessed.
Retain the prior state backup; this command is not a new imagery review.

Only 2024 is present in that package. Earlier year options remain preparation
choices, never reused 2024 pixels. Refresh also clears a transient tile-failure
hold. Crop imagery uses nearest-neighbor display so categorical colors do not
blend into invented classes. Live Earth Engine execution remains separate.

## Transport layers

Map layers → Roads, rail & bridges adds independent visibility and opacity for:
state bridges, local bridges, local bridges recorded NRHP listed/eligible,
local bridges built before 1950, local bridges explicitly recorded closed, and
KDOT's digitized 1918 roads. Each has a provider link, scale guidance and limits.
The service renders original geometry in Web Mercator; point symbols are not
bridge decks, surveyed footprints or navigation/safety guidance.

Live field checks found that KDOT uses text values, not NBI numeric codes:
`HISTSIGN IN ('Br eligible for NRHP','Br on Natl Reg Hist Place')` and
`OPPOSTCL='Closed to all traffic'`. Unknown/possible historic significance and
load postings are not included in these two specific filters. Pre-1950 means
`YEARBUILT >= 1800 AND YEARBUILT < 1950`, not a heritage or closure finding.

KDOT's [1918 roads service](https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation/Historical_Roads/MapServer)
uses a georeferenced historical map cross-referenced with period AAA maps;
named routes may conflict. Legacy route identifiers in other KDOT services
are not abandoned roads. A complete closed-road or demolished-bridge history
is still unverified; differences between maps are not treated as closures.

The supplied local raw folders contain 596 PDFs: bridges 105, statewide roads
55, county roadways 105, historic county/township maps 100, prior county maps
191 and urban roadways 40. One file per collection was inspected structurally.
The Allen bridge map was visually inspected and dated 31 March 2023. Its
numbered bridge locators are useful corroboration, but have no embedded
georeferencing. Sampled historical sheets also lack it. Sampled county and
urban roadway PDFs contain geospatial viewports, requiring coordinate and
alignment validation before overlay preparation. Originals remain untouched;
no automatic tracing or bulk promotion of these PDFs occurred.

### Bridge record inspection

In each bridge layer's **Options**, enable that layer and choose **Inspect map
center**. The search uses a selected 100 m, 500 m or 1 km radius and exactly the
same provider filter as the overlay. Individual results expose the official
identifier and record link, crossing, source-recorded status, construction and
reconstruction years, historic designation and separate inspection fields.
**Center map on bridge** retains the chosen basemap and respects reduced motion.
Distances are approximate great-circle distances from the recorded search center.

State and non-state services have different schemas: state `BUILT_DATE` and
`STR_NAME` are not substituted for the local service's `YEARBUILT` and `BRKEY`.
The state service does not supply the local inspection/historic fields. Missing,
sentinel and future dates remain unknown. `INSPDATE`, `LASTINSP`, any provider
modification string and KFM retrieval time remain separately labeled; none
establishes when a closure occurred. Current service access is not live status.

`GET /api/bridge-records` is a bounded external-context read, not the governed
released-evidence API or a statewide acquisition pipeline. It allows only the
five fixed bridge layer IDs, Kansas map centers and the three radii. Unknown
parameters, URLs and SQL are rejected. It uses fixed provider field lists and
does not follow redirects or accept ArcGIS error bodies even with HTTP 200.

The inspector first asks KDOT for a count with the same fixed filter and search
circle, then reads `OBJECTID`-ordered pages of 50, up to five pages/250 provider
records. The entire search has a 12-second server deadline, a 4 KiB count limit
and a 128 KiB limit per page; the browser has its own 15-second deadline and a
512 KiB response limit. Page overlap, unordered IDs, malformed pages and count
excess fail closed. A count beyond the cap, a short page, or omitted invalid or
out-of-scope records yields an explicitly partial result. The provider count is
shown alongside the inspected count, but the provider does not offer an immutable
snapshot across requests, so its inventory can change during paging. The list
is sorted by distance only after the bounded read and does not claim to contain
the nearest 250 when capped. Empty results do not establish absence.

Moving the map, changing radius, disabling the layer, cancelling or unmounting
cancels outstanding work. A failed/replaced query cannot relabel earlier results;
their search center, radius and retrieval time remain visible. No inventory
record enters saved evidence, reports, canonical storage or releases. Tests cover
provider errors, redirects, byte bounds, cancellation, count/page agreement,
ordered paging and the cap, filter parity, duplicate identity, geographic bounds
and distinct date/status meanings. A live KDOT check on 2026-10-03 returned three
matching non-state records within a 1 km Wichita sample; that check does not
establish statewide completeness or current road access.

### Local archive reconciliation — 2 October 2026

A fresh SHA-256 audit of all 596 local PDFs matched every one of the 541 prior
screening records without changed or missing bytes. There are 55 additional
paths in Past Published County Maps. All 55 opened for structural inspection;
none declared a geospatial viewport or legacy geospatial dictionary. The reader
recovered a cross-reference warning in `doniphan1999.pdf`; that file needs
source-integrity review before preparation. They need
independent control and alignment work, rather than stretching scans to an
outline. The previous 185 embedded-control candidates retain identical bytes;
their old classification is still screening, not alignment acceptance.

Two files have identical bytes despite conflicting names:
`KFM Past Published County Maps/1972 Kansas.pdf` and
`KFM Past Published County Maps/Crawford1936.pdf`, SHA-256
`8bb99b3713851861779d924d7eafd5fced020138dc49ba346c9ead7d2313285a`.
Preserve both and hold filename-derived date/location claims pending source
review. The separate statewide `Kansas Road Maps/1972 Kansas.pdf` has a different
hash and is not replaced. The reconciliation and structural-screening receipts
are outside the Site tree with local delivery evidence; the canonical prior
screening, raw PDFs, permissions and release states remain untouched.

## HMS playback

HMS Options offers 7 days, 30 days, Full archive → latest, exact UTC dates,
date scrubbing, Play/Pause, Next day, speed, repeat and smooth fade. The connected
KML archive starts 2005-08-05. This is not a completeness claim or the start of
all HMS products. Daily footprints retain original geometry, density and source
validity intervals. A daily frame shows footprints overlapping that UTC day,
not a single simultaneous snapshot or measured plume motion. Early NOAA records
can have identical Start/End times: these retain timestamp-only support, with no
invented duration. They appear in their daily frame and at the exact timestamp
in the existing Observatory; reversed intervals still fail validation.

Only one day and a next-day preload are requested, with a three-frame cache,
30-second request deadlines, 4-MiB response bounds, and existing upstream
2-MiB publication bounds. Missing requested publications stop playback, retain
the last checked map/date and require retry or explicit Next day. Verified empty
days clear footprints but never assert clean air. Prior-day overlap failures
remain partial. Daily history does not claim smooth physical motion: fade-through
changes opacity only, waits for the GeoJSON upload, and uses no invented geometry.
Layer holds, reduced motion, tab hiding and component teardown cancel playback.
Follow latest publication returns to the existing rolling source refresh.
It also clears the archive-status wording and resets the requested-day cursor;
the displayed source retrieval remains distinct from a successful refresh.

Playback interruption repair (2026-10-03): the 30-second request deadline and
caller cancellation now include decoding a stalled response body. A publication
that calls the same day both available and missing is rejected and not cached.
Map updates are serialized through a latest-request queue: an interrupted upload
must restore the previously confirmed payload before the next update reads its
starting frame. Superseded queued frames never run. Restoration has the existing
10-second geometry-upload bound; this is not an unbounded animation queue.

A frame is accepted only while the same map and GeoJSON source remain attached,
after its upload and optional fade complete. Missing/replaced renderers cannot
advance the displayed date. Cancelled styles release their opacity multiplier so
the next style cannot inherit an invisible smoke layer. Publication-fetch errors
and map-update errors now have separate messages; a failed map update does not
claim NOAA has a missing publication. These changes retain exact provider
geometry, daily time support, opacity preferences, manual steps and all existing
range/speed controls. They do not infer plume motion or fill archive gaps.

`tests/hms-smoke-transition.test.mjs` exercises stalled bodies, deadlines,
contradictory coverage, missing/replaced sources, superseded uploads, queued
cancellation and date commitment after rendering work. Its controlled renderer
tests execute the production callback but do not establish real WebGL acceptance.

[NOAA HMS guidance](https://www.ospo.noaa.gov/products/land/hms.html) describes
near-real-time forward production, gaps and observing limitations. The archive
is not retrospectively gap-filled. Sensors, clouds and analysis change coverage;
long-term comparisons need those caveats.

## Verification and recovery

Run TypeScript, the production build and Site tests. Tests exercise archive bounds,
missing-publication rejection, cache bounds, cancellation, local read origin/write
denials, activated digest checks, and independent layer controls. Provider image
checks verify nonempty imagery and CORS separately from browser rendering.
Keep source/build/local-state backups outside the app. Restoring the previous
build revokes this feature path; restore only the imagery prefix or the preserved
local state with the service stopped if undoing the copied imagery. Do not reset
unrelated D1/R2 data or replace newer source edits. Browser visual acceptance
remains separate and must not be inferred from HTTP or unit tests.
