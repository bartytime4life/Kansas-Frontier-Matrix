# Basemap warning lifecycle and first-event capture

This source-only correction follows production issue #5779. The original
approximately 2026-11-09 02:08 UTC trigger remains **UNKNOWN**. Do not close the
issue or claim a production repair from these source tests.

## Established source defects

The published `6366792b9ffb8d2e7a1b433a38e791850fc8aef8` handler assigned
basemap tile errors to the shared `degradedReason` closure. Neither successful
style synchronization nor successful basemap tile completion retired that
message. Idle could display the same warning again without a new error.
The category-basemap membership test also labeled a local orientation GeoJSON
error as unavailable tiles.

`basemap-health.ts` separates basemap health from terrain/renderer failures.
It retires an abandoned style's active failure scope **before** `setStyle`,
and retires a current failed tile only after a positively loaded matching
tile from the same source instance and source specification. Style load,
idle and `isSourceLoaded` alone do not recover it: MapLibre v6.9.0 can consider
terminal errored tiles settled. Unknown/tileless source failures remain
explicit until the style is replaced. Tracking overflow remains explicitly
unknown. Genuine tile and independent renderer errors stay visible.

Only a positive request/decoder-specification mismatch establishes a stale
source event. Missing event provenance remains unknown. Identical source IDs
and specifications cannot prove an event's original style generation. The
synthetic stale-event tests establish the handler guard, not actual stale
event delivery during the production incident. Source cleanup may detach old
event parents before they can deliver an event.

An explicit `AbortError` does not create an outage or clear prior failures.
Other network cancellations must be correlated with their originating map
event; no free-text exception matching is used to infer provider failures.

Aviation chart and Midnight navy both use `basemap-relief-dem` from the
registered AWS Mapzen Terrarium provider. Switching between them does not
independently test that provider. Console silence is also insufficient:
MapLibre routes handled source errors to listeners rather than necessarily
printing them to the console. The later governed catalog 503 stays separate.

## Opt-in browser-local trace

On a build that includes this change, for local or read-only inspection, add
`basemapTrace=1` to the existing URL **before** opening the map. The query
enables no source, upload, data admission, model, archive or publication.
The trace is available locally as:

```js
window.__kfmBasemapTrace.snapshot()
```

The trace attaches immediately after the Map constructor and before KFM's
controls and event handlers. It records source/style/error/idle/resize,
camera start/end, visibility and navigation events. It retains 512 recent
events plus the first map failure across style changes; dropped events,
uncorrelated tile tokens and collector failures are explicit. The first
failure may be unrelated to the basemap; inspect its finite source label.

Only known display-basemap source IDs, per-capture source-instance/tile
tokens, specification relation, finite HTTP status, dimensions, generation
and timestamps are exported. Raw tile coordinates, source URLs, query
tokens, error messages/stacks, source payloads and camera coordinates are
omitted. The trace adds no requests or persistent storage. Removing the
opt-in or unmounting the map removes its listeners and exposed handle.

This map trace cannot capture events emitted synchronously inside the
constructor or network activity before navigation. For causal acceptance,
enable browser Network/console/page/navigation recording before the first
navigation as well. Capture worker targets separately when needed; page
traffic does not prove complete worker or server-to-provider traffic.
Correlate `startedAtEpochMs` plus relative `at` with browser network clocks.

## Verification and remaining gates

The regression executes the page's actual error/source/idle/style-replacement
callbacks with controlled events and an explicitly successful renderer stub.
It also checks preservation of current failures, stale/missing provenance,
abort behavior, metadata errors, source identity and overflow. The obsolete
source-regex test for category failure was replaced by executed handler
behavior. No assertion is weakened to hide a failure.

```sh
node --test tests/basemap-warning-lifecycle.test.mjs tests/basemap-diagnostics.test.mjs tests/cutaway-basemap-failure.test.mjs tests/category-basemaps.test.mjs tests/runtime-resilience.test.mjs

# Run the identical page-callback tests against an untouched published file.
# Expected RED for the recovery/classification defects, not a passing gate.
KFM_BASEMAP_BASELINE=/absolute/path/to/published-page.tsx node --test tests/basemap-warning-lifecycle.test.mjs

# Built loopback server only. Synthetic fixtures block provider traffic.
KFM_TEST_CHROME=chromium KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5182 node --test tests/kansas-sky.browser.mjs
```

The browser case observes deliberately blocked real MapLibre relief requests
on Midnight navy, verifies that changing to a successfully loaded isolated
style retires that warning, then verifies that new relief failures stay
visible through 375-to-1440 resizing. Its network listener starts before
initial navigation, exports finite provider/catalog lanes, and the map trace
retains the first failure. These are **synthetic loopback** results, not live
provider, real-flight, installed-machine or physical-GPU acceptance.

The healthy cross-origin style fixture includes its required CORS permission.
Native replay dragging waits for the actual unobstructed canvas before input;
its two endpoint assertions and native-gesture Follow-release assertion stay
unchanged. This uses the existing bounded wait, not a longer deadline or skip.

To resolve #5779, capture the unchanged release from the beginning on a
WebGL2-capable browser. Attempt Aviation chart / globe / AAL1179 / Follow /
Orbit / manual zoom / the recorded resizing / Midnight navy. If AAL1179 is
absent, record that limitation; another live aircraft is a different scenario.
The original viewport heights and exact action ordering are incomplete.
Use at most two bounded sequences or ten minutes, preserve the first failure
before retry, and mark any truncated capture incomplete. Distinguish an HTTP
provider failure from a 200 response with decode failure, a local source or
renderer error, a positively stale event and a retained warning. A later
clean screenshot or passing synthetic suite is not causal proof.

Repository placement uses the existing Node composition's `app/`, `tests/`
and `docs/` responsibilities. Merge, installation and deployment require
separate owner authorization. No geographic dataset, provider endpoint,
dependency, DNS, runtime setting or source-activation change is included.
