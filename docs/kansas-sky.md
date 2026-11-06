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
History expires with the page; toggling the layer off stops drawing/polling.

Trails use at most 20,000 retained display points; visual detail is thinned before
current aircraft are removed. The live feed still caps 3,000 aircraft and reports
omitted/truncated records. The custom layer uses persistent bounded GPU buffers.
Equal-time identity churn also obeys the history cap, preserving the latest
accepted feed snapshot before retiring historical one-point tracks.
The aircraft list supplies keyboard selection, including globe views where
precise elevated click picking is unavailable. Manual map movement releases
Follow/Orbit; reduced motion disables automatic camera movement.

## Prepared dated flights and rights

Two November 3, 2026 Kansas crossings are served from
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

The converter bounds compressed/decompressed bytes and sample counts, clips the
region, and chooses the longest continuous segment. Raw stale/new-leg flags,
method changes, ground transitions and gaps split segments; original quality
fields are retained when present, not carried forward as new measurements.
`tests/fixtures/kansas-sky/` contains original member bytes solely for offline
byte-for-byte reproduction. It is not an application endpoint.

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

Review exact-head CI and its screenshots before merging. A merge, Preview
deployment, public publication and governed data activation are separate actions.
Publication remains on hold. Rollback targets the relevant source commit;
no database rollback is necessary. Volumetric historical weather is deferred.
