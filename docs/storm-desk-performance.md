# Storm Desk measurement follow-up — 2026-10-28

The available environment verifies controls, source responses and a GOES polling
regression. It does **not** establish real radar tile savings, native mobile
performance or GPU-presented FPS. No publication or provider-source change is
part of this follow-up.

## Revisions and environment

Before the hosted journey, `https://kansasfrontiermatrix.com/api/build` reported:

- Application `urdng3v1vk`, profile `kfm.godaddy-application-inputs/v1`.
- Clean commit `bd562032da270cab2ffc7dfc70ec30a730b7214e`.
- Application-input digest `sha256:ab019850d5928e30a5181abfba7d420a6de271ef8022a8a6ed0ecd0baae28eb4`, 1,070 files.
- GitHub's comparison identifies this commit as six commits ahead of PR #5522's
  merge `70e1cb1956075047dd5b6c4f55b04088499fa678`; the intervening files concern
  welcome behavior, rather than replacing Storm Desk.

The implementation checkout starts from the newer branch revision
`138e71ca6991bead114bb9ee4a8bd770836c5121`, whose clean application-input digest
was `sha256:b5d6bc6caed1442b02b9dc14640aab40e215364cc860fc649198c627f351e3af`.
It also contains merged #5529's separate terrain changes. The hosted and local
revisions are distinct; the hosted journey does not validate this candidate.

The cloud Chrome browser visibly reports WebGL2 unavailable. Opening a second
tab still leaves the first document `visible` with `document.hidden === false`.
Consequently it cannot establish either native rendering performance or actual
hidden-tab behavior. Its connection to the local candidate's loopback port is
refused. The execution host has no installed Chrome/Chromium executable or
native GPU device. The normal Node suite's recording map performs no provider
network I/O.

## Hosted visitor observations

The journey followed welcome → Weather → Open the storm desk. Active NWS alerts
and latest NOAA radar were selected, radar playback was paused, and Add related
context began collapsed. Expanding it exposed all five unselected options.
Enabling GOES, forecast wind, lightning, smoke and gauges changed their selection
state. Gauges and lightning exposed their separate observation controls.

The radar manifest loaded, but the desk displayed **No observation selected**
and kept radar playback disabled because no WebGL map could confirm a scan.
No radar tile traffic, rendered alert geometry, animation responsiveness or FPS
can be inferred. The source status announced 11 alert features. Empty HMS smoke
was explicitly described as zero mapped features, **not an all-clear**.
Forecast wind remained in a loading state in this unsupported browser; wind
rendering/failure settlement is not verified here.

Switching to Government's Civic map removed Storm Desk's controls and selected
its one-layer starter. Returning through welcome → Weather restored the two
Storm Desk starters and collapsed optional group. A real inactivity/return
comparison and starting/pausing actual rendered radar remain blocked.

## Actual HTTP response measurements

These are single actual GETs from the execution host to the public application's
adapters, taken concurrently in groups of at most three at approximately
10:27 AM America/Chicago (15:27 UTC). They are not browser tile acquisitions,
server-to-provider egress, latency distributions, mobile measurements, or a
before/after benchmark. Connection/proxy overhead is included. Byte counts are
HTTP response-body bytes reported by curl, excluding headers/TLS overhead.

| Adapter | HTTP | Body bytes | First byte, s | Total, s | Source result |
| --- | ---: | ---: | ---: | ---: | --- |
| `/api/build` | 200 | 391 | 3.670885 | 3.715308 | Same hosted revision/digest |
| `/api/noaa-radar/frames` | 200 | 3,426 | 3.694618 | 3.694749 | 95 exact scans; newest 15:20:12 UTC; age 415 s; current; interpolation false |
| `/api/live-context?feed=nws-alerts` | 200 | 26,812 | 3.975193 | 3.975378 | 11 features; ready |
| `/api/noaa-satellite/frames` | 200 | 17,211 | 3.793122 | 3.793345 | 140 dated frames; newest starts 15:00 UTC, valid through 15:09 UTC; provider freshness current |
| `/api/lightning/frames` | 200 | 647 | 4.558020 | 4.558236 | Newest 15:15 UTC; separate 15-minute clock |
| `/api/live-context?feed=noaa-hms-smoke` | 200 | 832 | 3.463235 | 3.463391 | Empty, zero features |

The one-hour radar control's 16-frame selection is a subset of the manifest's
rolling history; it is not a conflicting provider count. These responses prove
that the hosted adapters were reachable at capture time. They do not prove that
the browser can fetch their image tiles or that every selected layer draws.

## Verified fixes and simulated evidence

GOES's polling effect previously depended on the entire layer-visibility object.
An unrelated layer toggle therefore restarted its effect and requested the
manifest again. Its five-minute timer also called the manifest reader while the
document was hidden. The candidate depends on GOES's own selected/present state,
aborts on hide/deselection/cleanup, refreshes on visible return, and refuses a
response that finishes after abort. The callback also guards direct hidden or
deselected refresh attempts.

The actual page effect was executed with controlled timers and visibility. This
is **simulated invocation counting, with no network I/O or GPU**:

| Scenario | Baseline callback calls | Candidate callback calls |
| --- | ---: | ---: |
| Initial selected GOES entry | 1 | 1 |
| One unrelated layer toggle | 1 | 0 |
| Two timer ticks while hidden | 2 | 0 |
| Return to visible | 0 | 1 |

The cancellation tests also check that an aborted delayed response cannot select
an image. This establishes the scheduling/cancellation correction, not actual
byte savings or an FPS improvement. Radar's existing exact timestamp membership,
freshness refusal, inactive-buffer layout hiding and unchanged-scan behavior are
preserved and retain their deterministic tests.

The optional lightning note previously called the fixed
`ldn_lightning_strike_density` source satellite optical density. It now says
ground-network density and still disclaims individual strike locations. This
aligns with the existing source registry and NOAA's
[product description](https://ocean.weather.gov/lightning/lightning_pdd.php),
which identifies ground-based Vaisala detections and an aggregated 8 km product.
The optional layer, endpoint, observations, timestamps, defaults and visual design
are unchanged.

## Reproducible native capture

`scripts/measure-storm-desk.mjs` launches a separate, fresh Chrome profile with
normal caching. It never installs fixtures, intercepts provider responses or
substitutes data. Before launch it checks `/api/build` against an explicitly
supplied expected application-input digest. Pass a locally installed browser
using `--chrome` or `KFM_TEST_CHROME`. The default run is headful and does not
force SwiftShader, disable the GPU or disable the browser sandbox.

In one terminal, build and start the candidate:

```sh
npm ci
npm run build
PORT=5182 npm start
```

In another terminal, obtain the expected digest from the intended checkout with
`node scripts/build-identity.mjs --print`, verify it against `/api/build`, then run:

```sh
node scripts/measure-storm-desk.mjs \
  --origin http://127.0.0.1:5182 \
  --expected-digest sha256:REPLACE_WITH_VERIFIED_DIGEST \
  --chrome /path/to/google-chrome \
  --output /tmp/storm-desktop.json
```

The journey covers welcome, Weather, paused entry, requested playback, pause,
GOES, an unrelated switch, playback before a real hidden tab, visible return,
all remaining optional switches, another category, and Storm Desk return.
The default hidden period is 330 seconds, spanning radar's 240-second and GOES's
300-second intervals. The capture waits for actual document visibility rather
than dispatching a synthetic visibility event. If playback is disabled or the
hidden condition cannot be established, the receipt remains incomplete and
records the blocker. Do not report its absent tile traffic as a reduction.

Separate runs can use:

- `--slow-network`: CDP network emulation at 300 ms latency, 200,000 download
  bytes/s and 100,000 upload bytes/s; this is not a real mobile radio connection.
- `--width 390 --height 844`: phone-sized viewport, not native mobile GPU proof.
- `--soak-seconds 1800`: an additional 30-minute playback phase, with heap,
  document/listener counts and source/layer snapshots for resource comparison.
- `--seconds 60`: longer visible phases. `--headless` is explicit and recorded;
  it must not be silently presented as a normal foreground device run.

The collector observes CDP Network events in the page and attached descendant
workers. It records exact radar observation timestamps, response and completion
latencies, encoded bytes, failures, cache responses, repeated URL hashes and
concurrent duplicates. Raw bodies, headers, credentials and camera coordinates
are not exported. Counts are attributed to request-start phases and also retain
completion phases, so a late completion is not mistaken for a newly initiated
hidden-tab request. Failed transfers have partial-byte lower bounds. Repeated
URLs include legitimate replay and cache hits; they are investigation signals,
not automatic proof of wasted bandwidth. Capture is capped at 20,000 weather
requests and explicitly marked incomplete if the cap is exceeded.

The `?stormPerf=1` candidate probe records at most 2,048 exact-frame readiness
events, source/layer counts, context losses and MapLibre render callbacks. It
adds no timer, network transmission or listener without the opt-in and removes
its listeners on map teardown. The driver also records rAF intervals, long
tasks, JS heap and DOM counters. Staged-to-confirmed latency means the existing
MapLibre source-loaded condition, not a guarantee that every pixel is useful
weather coverage. MapLibre render callbacks and page rAF cadence are separate
metrics; `gpuPresentedFps` remains null. A native GPU trace/presentation tool is
still needed for an actual presented-FPS claim. Review recorded GPU metadata
for software rendering before interpreting results.

Run identical viewports, normal/slow network settings and phase durations on
the intended baseline and candidate before drawing comparative conclusions.
Native mobile, actual tile bandwidth, slow-network frame settlement, real GPU
presentation and extended-session acceptance remain unverified until those
receipts exist.

## Validation and delivery

Production build and the subsequent full Node suite pass: **1,966 passed,
0 failed, 21 skipped (1,987 total)**. TypeScript passes. Changed-file ESLint
has zero errors and 42 existing page warnings. The focused radar, Storm Desk and
instrumentation suite passes all 16 checks. `git diff --check` passes.
The candidate application-input digest is
`sha256:80e713f3103e3e56720f9824396fef2a1ca57c750564b08f92b7daed18798498`
(1,073 files). Its identity is distinct from the hosted baseline above.

The native-driver startup check first verified the locally running production
application identity, then produced an incomplete receipt with
`spawn google-chrome ENOENT`. No browser phase ran. The full native journey has
not been executed end to end in this environment; syntax, collector accounting,
bounded probe lifecycle and missing-browser handling have been checked. These
are not native provider/GPU acceptance results. The earlier broad run overlapped
a build and source edits, so its two build-identity/emitted-asset failures were
discarded and the build/suite were rerun sequentially.
All browser-state observations above concern the hosted baseline; they are
reported separately from controlled Node checks and candidate source review.

Rollback is a revert of this bounded code/documentation change. No data, database,
hosting, DNS, audience, credential, deployment or publication mutation is needed.
