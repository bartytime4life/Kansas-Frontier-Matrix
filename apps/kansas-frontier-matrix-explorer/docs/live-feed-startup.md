<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/explorer/live-feed-startup
title: Live-feed runtime diagnostics and starter-data selection
type: note
version: v0.1.0
status: proposed; branch-only; hosted-integration-held
owners: ["@bartytime4life"]
created: 2026-09-23
updated: 2026-09-23
policy_label: public; synthetic-fixture; no-source-admission; no-release
responsibility: Explain the repository Worker API-boundary repair, bounded connection probe, synthetic baseline, and held active-Site integration.
owning_root: apps/
current_path: apps/kansas-frontier-matrix-explorer/docs/live-feed-startup.md
truth_posture: CONFIRMED local implementation and tests; NEEDS VERIFICATION current Site connections and integration
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_commit: 21eee8dab4637da4771267078fe963f6525b045f
[/KFM_META_BLOCK_V2] -->

# Live-feed runtime diagnostics and starter-data selection

**REPOSITORY WORKER REPAIR + RUNNABLE DIAGNOSTIC / STARTER SELECTOR NOT MOUNTED IN THE SITE.**

This change does not claim that the user's deployed Explorer has been repaired.
The active Site editor and authenticated application were not accessible in the
execution session. No latest provider observations or historical payloads were
retrieved or certified. The supplied baseline is invented demo geometry, not
latest real data relabeled as synthetic.

## Confirmed problem and repair

At the pinned base, [`worker/index.ts`](../worker/index.ts) serves static assets
and sends an extensionless missing GET to `index.html`. This includes missing
`/api/...` routes. The app [README](../README.md) describes a renderer-neutral
repository shell, not the separately hosted standalone Site's feed adapters.
Returning an HTML shell is not a functioning feed API, even when HTTP is 200.

The Worker now rejects the unimplemented API namespace before static-asset
fallback, returning HTTP 503, JSON `KFM_API_NOT_CONFIGURED`, `no-store`, and
`nosniff`. HEAD has no body; error responses never echo query values. Ordinary
page fallback, real assets and non-GET page behavior remain unchanged. Invalid
path escapes receive a finite HTTP 400 response. No live API route is added.

The [source-alignment record](sites-source-alignment.md) explicitly separates the
standalone Site from this monorepo app. Its version-45 checkpoint is historical,
not a fresh Site readback. The standalone mirror inspected here is
`c4e5ebe54cba9d7ca9bbee108b442bdf68763f58` (v40 lineage), not asserted current.
That mirror's `app/live-context.ts` contains present-frame gating and a 3DEP
client display range of zoom 7 through 12. These explain possible intentional
withholding; they do not prove the cause of the current screenshot.

The merged [USGS decoder candidate](usgs-earthquake-response-candidate.md) is
still documented without a live caller. Merged implementation is not hosted
wiring, and successful radar metadata is not successful radar-image rendering.

## Connection inventory and executable probe

[`probe-context-connections.mjs`](../scripts/probe-context-connections.mjs) has
15 logical entries derived from the historical mirror's `app/site-connections.ts`,
`app/live-context.ts`, and `app/terrain-tiles.ts`. This diagnostic allowlist is
not a new SourceDescriptor registry, source admission, or currentness assertion.

| Logical connection | Bounded diagnostic | Remaining proof |
|---|---|---|
| Census counties | Same-origin JSON route | Edition, schema, geometry, render |
| USGS streamflow | Same-origin JSON adapter | Qualified observations, gaps, selected-station history |
| NOAA NWPS gauges | Same-origin JSON adapter | Observation/forecast/model role and valid time |
| USGS 3DHP | Not requested by probe | External raster, browser policy, actual render |
| USGS WBD | Not requested by probe | External raster, vintage, actual render |
| NOAA NWM analysis | Not requested by probe | Model role, image time and render |
| NOAA NWM short-range | Not requested by probe | Forecast role, image time and render |
| USGS earthquakes | Same-origin JSON route | Full event validation, current query coverage, valid empty |
| NOAA HMS smoke | Same-origin JSON route | Publication gaps versus scoped absence, schema and render |
| NASA FIRMS | Not requested by probe | External raster, observation coverage and render |
| Raspberry Shake stations | Same-origin JSON route | Station metadata only; no waveform operation |
| USGS 3DEP hillshade | One fixed Kansas PNG tile | Full image decode, map source, zoom, opacity and render |
| USGS 3DEP slope | One fixed Kansas PNG tile | Full image decode, map source, zoom, opacity and render |
| NWS alerts | Same-origin JSON route | Scope, zone expansion, current alert validation |
| NOAA radar | Same-origin frame-manifest route | Advertised time, chosen frame image and actual render |

There are ten GET probes, at most two concurrent, an eight-second request/body
deadline and a four-MiB response cap. The two terrain requests use a fixed Kansas
tile, not the operator's location. There is no retry loop, scheduler, provider URL
argument, arbitrary proxy, credential argument, or response-body export. Importing
the module performs no requests. Execution requires an explicit existing-Site or
loopback origin. Redirects are not followed. No source or private data is logged.

From the repository root, for an already running local preview:

```bash
node apps/kansas-frontier-matrix-explorer/scripts/probe-context-connections.mjs \
  --origin http://127.0.0.1:5173
```

An authorized operator can explicitly target the existing Site origin:

```bash
node apps/kansas-frontier-matrix-explorer/scripts/probe-context-connections.mjs \
  --origin https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site
```

**Node does not inherit the browser's sign-in session.** A sign-in redirect,
401/403, HTML response, or network failure is not proof that a public provider is
down. Do not paste browser cookies or tokens into this command. Authenticated
browser tracing is a separate acceptance action. The native Sites editor was
not available in this run; the Site URL fetch did not yield application content.

The report distinguishes `API_NOT_CONFIGURED`, `ROUTE_MISSING`, `AUTH_REQUIRED`,
redirects, rate limits, timeout, invalid media/JSON, and bounded-body failure.
`JSON_RECEIVED_SCHEMA_UNVERIFIED` is not payload correctness or freshness.
`PNG_HEADER_ONLY_RENDER_UNPROVED` is not a decoded or displayed image.
An app-level HTTP 204 is unvalidated: the USGS-only 204 decoder must not be
applied to every provider. All report rows retain false validation, freshness,
and rendering proof flags. The five external raster entries remain not probed.

## Starter-data selection

[`resolveFeedStartup`](../app/feed-startup.ts) is a pure, no-I/O presentation
selector. The [bundled demo](../fixtures/feed-startup.synthetic.json) contains one
invented point and one invented polygon. It has fixed identity, a fixed synthetic
scenario timestamp, no retrieval date, and no hazard or measurement values.
It is not terrain elevation, a fire/smoke perimeter, an earthquake or streamflow.

For **Auto** with no explicit user direction: a valid current response takes
precedence, otherwise use an eligible same-scope snapshot, otherwise the separate
synthetic demonstration. A stale snapshot stays `STALE_SNAPSHOT`; never reset its
source timestamp to retrieval time. Explicit Live or History requests do not
silently become a different date, source, snapshot, or demo. A successful valid
empty result wins over populated fallback data and is not an all-clear. Partial
responses remain partial. Held/restricted/denied, off, unsupported-time and
unsupported-zoom states never gain data through fallback.

Snapshot metadata is bounded to 32 entries, source/product/AOI/time scope keys,
finite counts, canonical UTC timestamps, original role and digest shape. The
caller must actually validate the bytes, recompute and verify the digest, verify
public display permission and rights, and bind the canonical scope. The supplied
`validation` and `displayAllowed` fields are caller attestations, not independent
proof from this selector. Do not deserialize an upstream object directly into
this interface or use this function as a publication or security authority.

`freshnessAnchor` is source-specific: an observation time, model/forecast issue
time, reference-edition update, or validated query-coverage time as appropriate.
For sparse or empty earthquake results it is not simply the most recent event's
time. Forecast valid time can be future; its forecast role must remain visible.
`validUntil` must be established by the reviewed source policy, not a universal
TTL. Preserve coverage intervals and per-feature observation times in the payload.

`liveAvailable` means an eligible, fresh, complete current result, including valid
empty. `renderedLive` additionally requires a nonempty result and matching artifact
and scope renderer evidence plus an explicit rendered state. A later renderer
error or context loss cannot be masked by a retained artifact ID. An enabled toggle, response, snapshot or demo does
not increment that rendered-live count. The original finite connection failure
and loading phase remain visible while Auto shows fallback data.

## Integration still required

The Worker repair is in an existing runtime entrypoint. The CLI is executable.
**The starter selector and demo are not imported into `app/page.tsx` or deployed
Site code in this change.** Their cross-layer consumer is the new test suite.

Before mounting them in the user's existing Explorer:

1. Read back the exact active Site source and environment; reconcile its complete
   standalone mirror without merging its root layout over the monorepo. Preserve
   the current project, slug, audience and saved predecessor.
2. Bind each real loader's validated artifact to its canonical request generation,
   source/product/AOI/time scope and explicit user direction. Abort superseded
   requests and ignore late results. This synchronous selector does not implement
   asynchronous generation control, provider validation or persistent caching.
3. Render the demo in a separate conspicuously labeled synthetic layer and legend,
   never in official hazard layers. Keep the connection failure visible, preserve
   camera and user-selected history, and allow dismissal. Do not store demo bytes
   in a real-data cache or mix them into evidence, exports or operational totals.
4. Admit eligible real snapshot bytes only after their separate rights, validation,
   sensitivity and provenance checks. No real snapshot has been supplied here.
5. Bind map source/tile/image events to the same artifact/frame and selection key.
   Verify each toggle-to-request-to-payload-to-render path, selection/Evidence
   Drawer, timeline, no-data/error behavior, actual WebGL and same-Site recovery.

## Local evidence and delivery limits

Local execution on Node 22.16.0: **94 tests pass, zero skipped**. Tests exercise
startup selection, timeout including stalled body cancellation, bounded reads,
auth/media failures, concurrency, real Worker-to-probe responses and the
Worker-to-probe-to-starter negative integration with synthetic provenance intact.
The initial 13-test Worker suite against the exact original Worker had ten
failures and three passes; the corrected boundary and integration now pass.

Reproduce without installing dependencies:

```bash
node --test \
  apps/kansas-frontier-matrix-explorer/tests/feed-startup.test.mjs \
  apps/kansas-frontier-matrix-explorer/tests/probe-context-connections.test.mjs \
  apps/kansas-frontier-matrix-explorer/tests/worker-api-boundary.test.mjs
```

Node's built-in stripping executes the two TypeScript modules; it is not itself
a type check. A separate focused strict check passed with locally available
TypeScript 5.8.3, ES2022/DOM, ESNext and bundler resolution. This is **not** the
repository's pinned TypeScript 6.0.2 toolchain or a complete app build. The existing
`tests/*.test.mjs` package glob includes these tests after its build prerequisite.
Full pinned-toolchain build, repository validators, hosted CI, independent review,
provider calls, authenticated Site browser acceptance and deployment are NOT_RUN.

Delivery remains branch-only while the implicated delivery path's #4024
containment is unproved. No PR, ready transition, merge, rule change, topology or
baseline rewrite, source admission, release, publication, or Site save/deployment
is authorized by this note. #4228 Stage 1A accepted / Stage 1B HOLD / Stage 2
unauthorized boundaries remain separate. Discard the unaccepted branch to abandon
this candidate; any later integrated rollback is a separately reviewed inverse.
