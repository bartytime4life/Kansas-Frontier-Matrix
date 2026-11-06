# Kansas Sky aircraft and replay

Kansas Sky lives inside the working Aviation layer. It is not a separate demo:
Layers, Find, airspace and ordinary map controls remain available. The welcome
Aviation glimpse remains zones-only. Water-animation defaults are unchanged.
Clicking a map aircraft opens Layers → On map and focuses its instruments;
the aircraft list provides the same selection without requiring a pointer.

## Observation and time contract

The existing Kansas center/250 NM request and regional bounds are retained.
Live polling remains every 20 seconds while shown. The existing in-process
15-second traffic cache coalesces concurrent requests; it now bounds cached
bodies to 8 MiB and eight route keys. This is per-process, not global admission.
The fixed provider requests, timeouts and response read limits remain in force.
Failures are not cached as observations.

The response extends existing aircraft records additively with UTC observation
time, provider-vs-retrieval timestamp basis, position method, reported roll,
optional IAS/Mach, vertical-rate reference and bounded observation quality.
`seen_pos` is required: last-message age alone does not prove position freshness.
Old/future-dated snapshots are refused. Cached age is never clamped to make an
old observation fresh. Live samples stop at their last observed position and
expire after 60 seconds; they are not extrapolated between polls.

[readsb's specification](https://github.com/wiedehopf/readsb/blob/dev/README-json.md)
defines geometric altitude relative to the WGS84 ellipsoid. The UI distinguishes
it from pressure altitude. Rendered vertical placement is approximate, not an
MSL conversion or confirmed airspace occupancy. Missing instruments remain
unavailable; only reported roll tilts the schematic silhouette. No owner,
mission or accident-cause inference is made.

Live mode displays current eligible observations. Session and recorded modes
are always labelled REPLAY and share one cursor for aircraft, instruments,
trails and timeline. A noninteractive map status keeps REPLAY and UTC time visible
when Layers is closed; live status labels the receiver-check time separately.
Only samples bracketed by two recorded observations are
interpolated. Gaps over 60 seconds, provider or position-method changes, ground
transitions and explicit breaks disconnect tracks. No positions appear before
the first or after the last observation. Replay airspace/weather elsewhere on
the map remains current context, explicitly not reconstructed historical context.

## Memory and rendering bounds

The browser retains ten minutes regionally and up to one hour for the selected
aircraft, limited to 100,000 regional points plus 10,000 selected points. The
actual retained interval is displayed. Selecting a different aircraft does not
recover history already pruned. Nothing is written to SQL or browser persistence.
Session history expires with the page; toggling the layer off stops drawing/polling.
The separately prepared daily archive described below is not browser persistence.

Trails use at most 20,000 retained display points; visual detail is thinned before
current aircraft are removed. The live feed still caps 3,000 aircraft and reports
omitted/truncated records. The custom layer uses persistent bounded GPU buffers.
Equal-time identity churn also obeys the history cap, preserving the latest
accepted feed snapshot before retiring historical one-point tracks.
The aircraft list supplies keyboard selection, including globe views where
precise elevated click picking is unavailable. Manual map movement releases
Follow/Orbit; reduced motion disables automatic camera movement.

## Prepared dated flights and rights

The two legacy November 3, 2026 retained segments are preserved in
`public/data/aviation/replays/`: AC2FEA (23:14:49.100–23:43:54.470 UTC, 261 samples)
and AAE1EA (14:34:20.010–15:12:21.030 UTC, 151 samples).
The catalog binds each JSON SHA256; each file binds its original compressed
archive member, UTC sample times, license and transformation. The client checks
size, catalog identity, digest, time bounds and record shape before rendering.
It never requests entire global archives or internal stores.

On 2026-11-04 the official [API](https://www.adsb.lol/docs/open-data/api) and
[historical-data documentation](https://www.adsb.lol/docs/open-data/historical)
state ODbL 1.0. Attribution: adsb.lol and receiver contributors. These derived
replay records retain ODbL 1.0, with original source members and deterministic
transformation available for inspection. Public availability is not itself a
security defect. The existing adsb.fi fallback remains separately subject to
its personal/non-commercial terms; this change grants no commercial license.

Preparation is offline:

```sh
python3 scripts/prepare-kansas-sky-replay.py TRACE.json.gz SOURCE_URL MEMBER OUTPUT.json
node --test tests/kansas-sky.test.mjs tests/aviation-route-cache.test.mjs tests/aviation-layer.test.mjs
node scripts/benchmark-kansas-sky.mjs
```

The legacy converter mode bounds compressed/decompressed bytes and sample counts,
clips the region, and chooses the longest continuous segment. Daily preparation
uses its explicit all-segments mode described below. Raw stale/new-leg flags,
method changes, ground transitions and gaps split segments; original quality
fields are retained when present, not carried forward as new measurements.
`tests/fixtures/kansas-sky/` contains original member bytes solely for offline
byte-for-byte reproduction. It is not an application endpoint.

## View aircraft in the existing map — 2026-11-05

Choose an observed aircraft or a dated recorded flight, then **View aircraft in
3D**. The map frames that aircraft at the same approximate display height used
by the renderer. A larger faceted aircraft symbol makes heading and reported
roll visible; it is deliberately enlarged, not a real-size or aircraft-specific
model. Other aircraft and the 2D chart keep their compact symbols.

The map overlay keeps Play/Pause, Orbit/Follow, and the recorded-flight timeline
available with Layers closed. Source-backed times, missing observations and the
REPLAY label remain visible. Playback uses the existing chosen speed; the overlay
does not start playback automatically. A panel resize does not release the
camera. Manual map input or another camera navigation does; disabling the layer,
hiding the tab or unmounting also releases its elevation/ground-clamping settings.
Reduced motion permits a static framed view and explicit playback, without
Follow or Orbit. No new source, collector, service or application is introduced.

Tests exercise the camera's altitude target, camera ownership/release, panel
resize versus navigation, and bounded selected-symbol geometry. Baseline failure
and candidate success establish these specific changes, not a root cause for
all historical layer-disappearance reports. Real map browser inspection remains
separate from synthetic and source-level tests; neither establishes production
reliability or physical-device performance. The new view changes presentation
only and keeps the existing replay validation, provenance and error reporting.

## Whole journeys, aircraft briefs and daily preparation — 2026-11-06

The selected recorded aircraft can be viewed along its entire retained regional
path. The altitude profile and timeline select the same recorded time; separate
legs and observation gaps stay separate. Elapsed and ahead-of-cursor recorded
paths use distinct colors: the latter is known recorded history, never a live
prediction. Bounded vertical guides connect observed flight height to available
terrain context. Missing terrain omits a guide; it does not invent ground height.
The aircraft brief summarizes reported identity, selected-time measurements and
retained coverage. Expanded details expose available quality and instrument
fields; absent values remain unavailable. Neither callsign nor transponder
identity establishes ownership, purpose, destination or a complete lifetime.

Long aircraft-days are split into bounded files. The controls identify the loaded
part, available versus expected parts, and its observed time interval. Previous
and Next load only the adjacent part for the same aircraft, UTC day and provider,
using the same digest and byte validation. Playback pauses at a part boundary;
there is no automatic cross-file continuation. **This part** replaces **Whole
path** for split recordings. One file is loaded at a time, and unavailable parts
or failed loads cannot be presented as complete history. The two prepared
recordings currently each fit in one file.

Whole-path framing measures the flight dock and reserves its space once.
Flight-camera ownership temporarily releases the regional navigation bounds and
minimum zoom so the retained route can fit beside the controls. Ordinary
projection refreshes respect that ownership; closing, hiding or leaving flight
view restores navigation limits. This is a camera presentation change only:
provider requests, archive bounds, geographic eligibility and release checks
remain unchanged. With terrain active, MapLibre retains a requested camera
transform. Its minimum-zoom setter can copy old regional bounds back into the
live transform after those bounds were cleared. A bounded local runtime trace
confirmed this exact sequence. The correction completes the public camera
transaction before setting bounds, without editing private renderer state.
Regressions use the installed MapLibre setter bodies, terrain camera state and
projection changes; browser captures separately check the actual route and dock
layout. This cause applies to route framing, not the earlier intermittent layer
disappearance or the public graphics stall.

Replay motion runs independently of the slower instrument/list updates. Optional
**Smooth live · 30 s delay** uses one delayed clock and only positions bracketed
by actual retained reports for aircraft still eligible in the current feed. It
never extrapolates beyond an observation or bridges a gap. Receiver-check and
displayed times remain distinct; warmup, missing positions and reduced-motion
behavior are explicit. Rendering budgets may thin old geometry or reduce redraw
frequency while preserving retained observations. CPU fixture measurements are
not browser FPS, GPU capacity, physical-device or production reliability proof.

The original two source members have now also been prepared without discarding
shorter regional segments. The dated directory contains 964 AC2FEA observations
in four segments and 151 AAE1EA observations in one segment: 1,115 total. These
are **selected recordings**, not all aircraft on November 3. The legacy 412-point
catalog remains compatible. Each derivative is reproducible from the same
hash-bound original members. The day index advertises collection as unconfigured.

The owner selected Kansas and nearby airspace and the existing hosted KFM
service as the intended archive destination. The fixed regional bounds remain
west -103.2, east -93.6, south 36.2, north 40.9; this includes border context and
is not an exact state-boundary census. Every eligible regional observation and
every disconnected segment in the selected provider's source member is retained.
Original compressed members remain private provenance; UI files are derivatives.

The official [historical archive](https://www.adsb.lol/docs/open-data/historical)
publishes daily readsb production archives under ODbL 1.0. Freshly inspected
November 4 release metadata describes two SHA-256-bound assets totaling
3,618,676,224 bytes. This global transfer belongs in a scheduled preparation job,
not a browser or ordinary web request. The adsb.fi fallback is not mixed into
these shareable daily derivatives.

`scripts/prepare-kansas-sky-day.py` defaults to a metadata-only plan. Explicit
`--download` verifies all ordered production archive parts, streams tar members
without extracting their paths, retains regional originals and creates bounded
per-aircraft chunks plus a receipt. It preserves all eligible segments instead
of choosing only the longest one. One-point observations remain observations,
not an invented route. Files carry at most 2,500 original points and 4 MiB; no
observations are deleted merely to fit the browser. A one-day catalog is bounded
to 10,000 entries and 4 MiB. Exceeding a bound holds the preparation visibly.
The download cap is 6 GiB, candidate cap 2 GiB, and retained capacity defaults to
the existing 80 GB ceiling. No automatic deletion or overwrite is implemented.
Interrupted work remains explicitly incomplete; a complete candidate day is
renamed into place atomically. Repeated days verify existing hashes. A local
`--tar` diagnostic can only claim partial-input coverage.

`scripts/import-kansas-sky-day.mjs` is the Node operator bridge to the existing
private MySQL ingestion store, not a public upload API. Its default is verify/plan.
An explicit apply requires the existing configured published-role, TLS, capacity,
activation and paused-state gates. Artifacts remain WORK/QUARANTINE, unreleased,
with pending rights/sensitivity review. The day manifest is stored only after its
artifacts; interrupted imports resume by deterministic identities. No new database,
parallel storage authority, public read bypass, SQL migration or browser timer
is introduced. The prepared files are not automatically copied into public/.

Hosted activation remains **NEEDS VERIFICATION**. The November 6 dashboard
required a fresh owner sign-in. The available hosting connection does not expose
job-runner or storage configuration. A job runtime with Python 3 for preparation
and Node 22 for import must be confirmed; do not assume the web runtime includes
Python or a persistent writable disk. Confirm durable job output, verified MySQL
configuration, existing schema/capacity, the first complete stored provider day,
a subsequent scheduled day, recovery from a missing release, and a reviewed
public read/release path before claiming daily user-visible history is active.
An external scheduler can trigger preparation independently of visitors, but CI
artifacts alone are not durable hosted storage. No schedule, production store,
release state, deployment or publication is changed by this source candidate.

The preparation command accepts an explicit private output directory outside the
application checkout. Review its plan before running the multi-gigabyte transfer:

```sh
python3 scripts/prepare-kansas-sky-day.py --day yesterday
python3 scripts/prepare-kansas-sky-day.py --day YYYY-MM-DD --output /verified/private/job-output --download
node scripts/import-kansas-sky-day.mjs /verified/private/job-output/YYYY-MM-DD
```

The first command is plan-only; the latter two are preparation and import-plan
examples, not executed hosted collection. Actual apply and scheduled activation
require the verified target configuration. Files in app/, scripts/, server/,
tests/, docs/ and deliberately prepared public/data/aviation/replays/ continue
their existing Directory Rules / ADR-0029 responsibilities. This section is the
placement and migration note: existing private capture tables are reused; no
schema migration or new release authority is created. Rollback the source change
without deleting retained originals, candidate receipts or stored captures.

## Ownership, validation and rollout

Existing application `app/`, offline tooling `scripts/`, bounded public artifacts
`public/data/aviation/`, and validation `tests/` own this change. This follows
Directory Rules responsibility/lifecycle boundaries and creates no new schema,
registry, database, collector or release authority. Native Staging, the monorepo
mirror, installed PC composition and AI/data stores are not modified.

Ordinary tests exercise ordering, duplicates, missing measurements, timestamps,
gaps, providers, bounded history, cache coalescing and real archive reproduction.
The synthetic 3,000-aircraft benchmark measures Node CPU work only, not physical
GPU/FPS, production multi-user capacity or provider performance. The isolated
browser CI journey uses explicitly synthetic responses, production-built UI,
desktop and narrow/reduced-motion layouts. It is not live-provider acceptance.

### Style loading and browser acceptance — 2026-11-05

If initial attachment or a replacement style is still loading its sources,
the aircraft renderer retains a temporary frame listener and installs once
the style is ready. It releases that listener after installation or disposal.
Observations received while waiting remain available for the first draw and
aircraft picking. Recovery does not require a second `style.load` event, and
disposing a pending renderer cannot reinstall it later.

The page also refreshes its style-readiness signal on a ready frame when its
health probe found a pending style. A map that continuously repaints can be
fully loaded without emitting `idle`; waiting only for that event can otherwise
leave all dependent controls marked Not ready. This temporary check releases
its listener after refresh or page disposal. Full map-health and source-error
reporting still run independently. The browser regression keeps the real map
repainting and proves aircraft drawing and style recovery before any idle event.

Terminal tile failures can finish style loading without scheduling another
frame. Pending renderer and page-readiness checks therefore also recheck on
map error events, and remove both subscriptions after success or disposal.
They still require a loaded style and retain the owning source's failure
report. Delayed external-tile failures are covered in both browser layouts;
the expected degraded-map notice must coexist with working aircraft rendering.

The style-reload check observes the requested `style.load` event, then requires
the replacement style's marker, a loaded style, the aircraft layer and a fresh
GPU draw after that event. A cached vertex count from before the transition
cannot establish recovery. Screenshot metadata is collected after this proof;
the ordinary bounded wait and failure behavior remain in force.

County search preloads independently of aircraft inspection. Its Sky fixture
now returns an explicitly synthetic empty inventory, so the production reader's
one- and two-second retries of an injected 503 cannot be mistaken for reads
caused by an aircraft click. The test requires exactly one preload and still
rejects any additional county request during inspection. Census recovery and
aircraft click ownership retain their separate source-level coverage.

Fault controls block post-reload drawing or inject an additional county read
to check that those failures remain detectable. Request recovery, timeouts and
protocol-error handling are unchanged. This correction stays in the existing
`app/`, `tests/` and `docs/` roots under the accepted Directory Rules / ADR-0029
responsibility boundaries. Revert the correction to restore its preceding
renderer and acceptance behavior; no data or storage operation is required.
Exact-head results and known limits belong to the delivery record.

### Daily catalog and compact selection acceptance — 2026-11-06

The first journey CI run retained two distinct failures. Desktop replay reached
the real dated catalog because its synthetic fixture intercepted only the older
root catalog. The fixture now owns archive discovery, an empty legacy fallback,
the selected day catalog and its declared recording; unexpected archive paths
fail explicitly. Request and digest assertions prove the complete chain, including
rejection of altered bytes. This does not alter production data or loaders.

On the compact layer panel, newly added flight controls pushed the selected
identity heading below the visible area. The existing heading now sits directly
after the aircraft selector. All controls and the original simultaneous selector
and heading visibility assertion remain. These causes are distinct from style
readiness and the original intermittent layer disappearance. The failed CI run,
source regression and final exact-head acceptance must all remain retained.

A later hosted run passed five of six Sky scenarios but retained a desktop
continuous-repaint failure when manual dragging should release Follow. Source
reproduction established a separate lifecycle defect: the control can mount
before its stable map ref contains a map, so an effect depending only on that
ref and enabled state never attaches input handlers. Map readiness now refreshes
that subscription. The regression fails on the preceding source and passes after
the dependency correction. Browser drag coordinates, release assertion and
ordinary waits remain unchanged; bounded input/event diagnostics distinguish
canvas delivery, camera state and listener presence. This source defect does not
by itself prove the cause of that particular hosted failure or the older layer
investigation; retain and compare exact-head browser evidence separately.

Review exact-head CI and its screenshots before merging. A merge, Preview
deployment, public publication and governed data activation are separate actions.
Publication remains on hold. Rollback targets the relevant source commit;
no database rollback is necessary. Volumetric historical weather is deferred.
