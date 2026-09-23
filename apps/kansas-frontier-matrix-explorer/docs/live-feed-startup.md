<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/explorer/live-feed-startup
title: Live-feed runtime diagnostics and starter-data selection
type: note
version: v0.2.0
status: proposed; validated-branch-only; hosted-integration-held
owners: ["@bartytime4life"]
created: 2026-09-23
updated: 2026-09-23
policy_label: public; synthetic-fixture; no-source-admission; no-release
responsibility: Document the repository startup inspector, bounded connection diagnostics, cancellation, synthetic provenance, and held hosted integration.
owning_root: apps/
current_path: apps/kansas-frontier-matrix-explorer/docs/live-feed-startup.md
truth_posture: CONFIRMED bounded repository code and fixtures; NEEDS VERIFICATION full React and hosted acceptance
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_commit: 9dcdaec2cacbbf9880bd613b546a7314a2673ac5
[/KFM_META_BLOCK_V2] -->

# Live-feed runtime diagnostics and starter-data selection

**PHASE 2 IMPLEMENTED ON A PRESERVED BRANCH / NO SUCCESSOR PR / SITE UNCHANGED.**

This version replaces repeated currentness prose with one active implementation
boundary. The complete [v0.1.0 checkpoint](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/2ac6f209ea269e6df18331c9d53daf18039b8abf/apps/kansas-frontier-matrix-explorer/docs/live-feed-startup.md)
is retained as immutable lineage, including its 15-source inventory and original
94-test scope. Nothing here admits a source or changes the active hosted Site.

## Delivery currentness

[PR #4675](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4675)
was created as a draft at `2ac6f209ea269e6df18331c9d53daf18039b8abf`.
During phase-2 authoring it advanced through a separately initiated test-only
autofix to `4e33d1a0bee88ba2a2bddca4e9d7b7d65c744889` and merged at
2026-09-23T03:55:05Z as `9dcdaec2cacbbf9880bd613b546a7314a2673ac5`.
This session issued neither ready nor merge. The
[final-head authorization job](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/35816100035/job/107037829152)
failed with `EXPECTED_READINESS_HOLD / TRANSITION_AUTHORIZATION_MISSING`.
The initiating client is not identified by owner-account attribution.

The successor is based on that merged main and preserves the autofix exactly.
It remains `VALIDATED_BRANCH_ONLY` under #4024 rather than opening another
same-path PR through the unproved delivery mechanism. No automatic revert,
retroactive authorization, ruleset change or bypass occurred. The existing
#4228 Stage 1A accepted / Stage 1B HOLD / Stage 2 unauthorized boundaries remain.

## Repository is not hosted Site parity

The repository [Worker](../worker/index.ts) has no live-feed API router. PR #4675
makes that explicit: unimplemented `/api/...` requests return HTTP 503 JSON
`KFM_API_NOT_CONFIGURED`, not an HTML SPA shell. That is a diagnostic repair,
not a new live adapter.

The [source-alignment record](sites-source-alignment.md) separates this
renderer-neutral repository app from the standalone hosted Explorer. Its v45
checkpoint is historical. The v40 mirror
`c4e5ebe54cba9d7ca9bbee108b442bdf68763f58` is also historical; it supplies this
probe's reference inventory, not current Site configuration. Its present-frame
and 3DEP zoom 7–12 gates are possible withholding explanations, not a verified
cause of the user's current display problems. Native Sites editing was not
available in this session. No real latest-data or historical snapshot was acquired.

## Phase 2: mounted inspector

[`main.tsx`](../main.tsx) composes
[`FeedStartupPanel`](../app/feed-startup-panel.tsx) beside the existing Explorer.
Its effect adds **Data startup · preview** to the existing report ribbon and
removes that isolated child on cleanup. About does not mount the inspector.
The existing `app/page.tsx` is unchanged, avoiding the parallel seismic
Import-utility work. No map recreation, history patch, layer/time/camera change,
Evidence Drawer selection, geolocation or persistent storage is introduced.

The [DOM surface](../app/feed-startup-surface.mjs) provides an explicitly opened
native dialog, close/Escape handling and focus return, a connection selector,
Auto/Live/History/Demo policy preview, separate synthetic geometry descriptions,
and a 15-row diagnostic table. These are **inspector controls**, not replacements
for the main map's live-feed controls or totals. Live and History never silently
become a different mode. History and Demo do not initiate present-day probes.

The [demo loader](../app/feed-startup-demo.mjs) hashes the exact shipped UTF-8
fixture before use, with a fixed expected digest rather than a digest supplied
by an untrusted payload. Wrong bytes, including whitespace drift, are refused.
The immutable result contains one invented point and one invented polygon, no
observed hazard or measurement values, a fixed scenario time and no retrieval
time. Its source remains `synthetic:starter`; it is never official feed data.

## Request and snapshot currentness

The [request session](../app/feed-startup-session.mjs) adds generation binding,
AbortController cancellation, finite overall deadlines, immutable captured scope,
late-result rejection, disposal and clearing of renderer proof on refresh. A
reader queued before a change to denied is never invoked. An A→B→A selection
cannot accept the first A's late response merely because its scope matches again.
Non-cooperating readers still settle on cancellation/deadline. Disposal removes
retained display artifacts. No automatic polling or persistent cache is added.

The [selector](../app/feed-startup.ts) prefers a valid current result, then an
eligible same-source/product/AOI/time snapshot, then the separate demo in Auto.
Valid empty and partial results remain intact; empty is not an all-clear. Stale
snapshots retain original times and stale labels. Off, held, restricted, denied,
unsupported-time and unsupported-zoom states cannot be bypassed by fallback.

Snapshot metadata is bounded to 32 entries, opaque scope keys, finite counts,
canonical UTC timestamps, original role and digest shape. The caller must
validate actual bytes, recompute and verify their digest, bind their scope, and
verify rights, sensitivity and display permission. `validation` and
`displayAllowed` are caller attestations, not independent proof from this helper.
Do not deserialize upstream data directly into the interface. It is not a source
parser, security boundary or publication authority.

Freshness anchors are source-specific: observations, forecast/model issue time,
reference updates or verified query-coverage time. Sparse/empty earthquake
results do not use the latest event time as a universal freshness clock. Future
observation/reference times after retrieval are refused; future forecast valid
times retain their forecast role. `validUntil` belongs to reviewed source policy.

`liveAvailable` means an eligible fresh complete result, including valid empty.
`renderedLive` additionally requires nonempty data and the exact current artifact,
scope and rendered state. A toggle, HTTP 200, snapshot or synthetic preview does
not prove a rendered live layer. The mounted inspector accepts no real Artifact
from transport-only diagnostics, so those diagnostics cannot increase these counts.

## Connection diagnostics

The [browser-safe probe](../app/context-connection-probe.mjs) is shared with the
[Node CLI](../scripts/probe-context-connections.mjs). Its historical inventory is:
Census counties, USGS streamflow, NOAA NWPS, USGS 3DHP, USGS WBD, NOAA NWM
analysis and short-range guidance, USGS earthquakes, NOAA HMS smoke, NASA FIRMS,
Raspberry Shake station metadata, USGS 3DEP hillshade and slope, NWS alerts, and
NOAA radar frames. The five external raster entries remain `NOT_PROBED_RENDERER`.
The radar request checks frame metadata, not the actual displayed radar image.

There are at most ten GETs, two concurrent, with an eight-second request/body
deadline and four-MiB response cap. Terrain uses one fixed Kansas tile per kind,
not user coordinates. Cancellation stops the remaining queue. Import/mount does
not fetch. The browser supplies its own origin; the module permits the existing
HTTPS Site, loopback previews, or the browser's own HTTPS preview origin. Node
cannot use that browser-only allowance. Arbitrary remote origins, credentials,
paths, queries and fragments in origin arguments are refused. Redirects are not
followed; response bodies and credentials are never exported.

Transport outcomes remain distinct from scientific/source correctness:
`API_NOT_CONFIGURED`, `ROUTE_MISSING`, `AUTH_REQUIRED`, timeout, rate limiting,
wrong media, malformed JSON/UTF-8 and body limits. A JSON response remains
`JSON_RECEIVED_SCHEMA_UNVERIFIED`; a PNG header remains
`PNG_HEADER_ONLY_RENDER_UNPROVED`. HTTP 204 is unvalidated; do not apply the
USGS-only no-data decoder to every source. The inspector projects unqualified
transport as `PAYLOAD_UNVERIFIED`, unprobed imagery as `RENDER_UNVERIFIED`, and
retains the original failure alongside a separately labeled demo.

From a complete checkout, target an already running local preview explicitly:

```bash
node apps/kansas-frontier-matrix-explorer/scripts/probe-context-connections.mjs \
  --origin http://127.0.0.1:5173
```

The existing Site origin can be supplied instead. Node does not inherit the
browser's login session; do not paste cookies/tokens into the command. A sign-in
redirect is not evidence that USGS or NOAA is down.

## Validation and limits

- **PASS: 135 focused offline Node tests**, zero failures/skips: original 94 plus
  41 cancellation, generation, integrity, input and source-composition tests.
  Replayed with the merged test-only autofix preserved byte-for-byte.
- **PASS: 14 offline DOM fixture checks** in Chromium 144.0.7559.96: in-memory
  Worker→probe→session→DOM, explicit modes, late results, Escape/focus, corrupt
  fixture, disposal/remount, 320px layout and 200% text. A narrow-screen header
  overflow at 200% text was corrected and the fixtures rerun.
- **PASS: focused strict TypeScript 5.8.3** for selector/Worker and JavaScript
  syntax checks. This is not the repository-pinned complete React/TypeScript build.
- **BLOCKED_ENVIRONMENT:** local HTTP browser navigation returned
  `ERR_BLOCKED_BY_ADMINISTRATOR`. No browser-policy setting changed. DOM checks
  used an offline document, fixed test-origin seam, in-memory Worker response
  and Python-backed SHA-256 seam. They prove neither actual HTTP nor browser
  WebCrypto availability, full React mounting, authenticated Site behavior,
  WebGL, deployment or recovery.

```bash
node --test \
  apps/kansas-frontier-matrix-explorer/tests/feed-startup.test.mjs \
  apps/kansas-frontier-matrix-explorer/tests/feed-startup-session.test.mjs \
  apps/kansas-frontier-matrix-explorer/tests/probe-context-connections.test.mjs \
  apps/kansas-frontier-matrix-explorer/tests/worker-api-boundary.test.mjs
```

Node type stripping executes the selector in tests; it is not type checking.
Local validation used a byte-verified partial source tree because GitHub DNS/clone
access failed. No complete checkout or pinned dependency install is claimed locally.
The existing native Explorer workflow includes `*.test.mjs` and has no PR
base-branch filter, but it does not automatically run on this ordinary branch.
Success for either prior #4675 head is not successor-head CI proof. Full pinned
build, repository validators and independent/hosted acceptance remain NOT_RUN
for this branch unless a later exact-head record establishes them.

## Placement, remaining integration and rollback

Root ownership is `apps/`: app-local presentation, diagnostics, tests and
behavior-linked documentation under adopted ADR-0029 and the existing Explorer
lane. This is not a parallel source registry, contract, policy, schema, release,
proof or lifecycle-data authority. Original v0.1.0 detail remains in the immutable
link above rather than being repeated as current status.

Next proof is exact active-Site source/mirror reconciliation, a proven eligible
delivery path, source-specific validated and rights-cleared real snapshots,
genuine loader/render currentness, full app/browser testing and same-Site
recovery. Preserve the existing Site identity, audience and saved predecessor.
No real data, live source, model, release or deployment was activated here.

Abandon this branch to decline the candidate. A later integrated rollback uses a
reviewed inverse removing its main composition/new modules and restoring the
prior CLI/helper, preserving PR #4675's independent Worker repair, test autofix,
and evidence history. No same-path successor PR, automatic revert, retroactive
transition authorization, release, publication or Site deployment is performed.
