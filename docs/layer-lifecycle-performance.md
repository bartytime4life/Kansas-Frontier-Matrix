# Layer lifecycle and performance — October 11, 2026

## Public KFM investigation — November 6, 2026

Read-only checks at 06:08–06:24 UTC inspected the public Explorer, welcome-to-map
handoff, weather map, zoom interaction, data-library search, a 20-record FAA
airport page, civic sources/counties, knowledge and topic navigation.
These are bounded workstation observations, not a load test or
whole-product reliability certification. The public `/api/build` reported app
`urdng3v1vk`, commit `b7866a4086121d24f26ba6b1c168adc890892589`, digest
`sha256:41dda2f3be3cef4873be48ec76e3d4142a9352da06c8d3591fd5c530734a38d2`.
The repository branch and local candidate are newer; their evidence cannot be
attributed to that deployed build.

| Check | Observed result | Interpretation |
| --- | --- | --- |
| Cache-disabled Explorer reload | TTFB 374 ms; first contentful paint 528 ms; load 782 ms | This run's initial document was responsive. External map readiness occurs later. |
| Initial page module | 1,636,384 decoded bytes; 427,855 compressed body bytes | The eager Explorer module remains a sizable startup cost. Compression is working. |
| Welcome settled | Two full-sized MapLibre canvases, plus two small overlay canvases; 6,301 DOM elements | Explorer starts underneath the welcome's separate map. |
| Welcome idle sample | 0.201 s main-thread task time in 14.124 s | No sustained main-thread saturation established in that interval. |
| Weather activation profile | About 6.8 s non-idle samples in 27.7 s; several approximately 1 s graphics/shader/cleanup calls | Graphics handoff is an investigation priority. Sampling does not identify the driver, GPU process, or app as the sole cause. |
| Subsequent zoom profile | About 0.23 s non-idle in 30.18 s | The earlier stall is not a constant JavaScript busy loop. |
| Later welcome-to-aviation attempt | Browser command deadlines exceeded; affected tab closed | Retained as a failed run, not discarded or repaired with longer waits. |
| Data library | Document load 532 ms; filter selected one airport collection; actual 20-record read 729 ms, HTTP 200 | This path worked in the measured run. |
| Civic atlas | Document load 508 ms; source filter returned four Census matches; 105 counties loaded in 881 ms, HTTP 200 | County choices and source filtering worked. |
| Released knowledge | Search API HTTP 503 in 119 ms; visible unavailable-store message | A separate service-availability failure; no unreleased records substituted. |
| Topic navigation | Civic → Knowledge → Topics completed; subject headings rendered | Navigation works despite the held knowledge service; not proof every topic's data is available. |
| Governed water and weather | Both HTTP 503, `RELEASE_STORE_UNAVAILABLE`, in 131–141 ms during independent HTTP checks | A release-store availability/configuration failure, not a slow successful read. No fallback or policy bypass applied. |
| Public alerts and radar manifest | HTTP 200 in 317 ms and 163 ms during independent checks | Healthy responses for these requests only. |

Resource Timing omits cross-origin byte sizes when the provider does not expose
them. The network-event buffer reported truncation, so its 5.88 MB observed sum
is a lower bound, not complete transfer size. Competing tabs, current provider
responses, the embedded browser and graphics stack remain uncontrolled variables.
The failed live transition and successful local evaluation use different builds
and browser sessions; they are not an identical-input before/after comparison.

A later 06:51 UTC HTTP recheck was blocked by the client (HTTP 403 from the local
request path and `net::ERR_BLOCKED_BY_CLIENT` in the browser). It does not
establish a new origin failure or prove the earlier 503 responses persisted.

The bounded source correction delays the Explorer bootstrap until the welcome
is dismissed or a map is requested. The welcome keeps its own preview. A one-way
request latch preserves the already-created Explorer when the guide is reopened,
including its camera, selected layers and existing cleanup/error handling. Startup
uses the already-pending category camera and source/style refs. This removes a
confirmed redundant initial allocation; it does **not** establish the cause of
the graphics stall or the prior intermittent Sky disappearance.

Three actual-effect regression checks cover no hidden bootstrap, startup on
request and guide reopening without renderer disposal. The old page fails two
of these checks. Existing runtime, category, focus, terrain and weather checks
remain independent. No source refresh, timeout, assertion, release gate or
production data was weakened. Existing `app/`, `tests/` and `docs/` roots own
this lifecycle change under Directory Rules / ADR-0029; revert the startup latch
to restore eager initialization without changing retained data.

Retain the dated HTTP receipts, full Resource Timing entries, both CPU profiles,
failed-transition notes and baseline/candidate test logs outside deployment
assets. Recheck the exact candidate on the target host after authorized release;
then repeat cold/warm transitions, device and long-session tests. Host metrics,
all 189 archive collections, every map combination, physical phones, concurrent
load and the configured private archive job remain **NEEDS VERIFICATION**.

## Cached terrain-raster toggles — October 13, 2026

The GoDaddy composition at `d9b456a87b0b0bf1482d121f2f808748c4b569dc`
preserved opacity across repeated toggles, but its hillshade status stayed at
Loading after hiding and showing already cached tiles. Visibility reset the
tile-status tracker even though MapLibre retained the same raster source and
did not need to emit another tile completion.

Ordinary hillshade/slope visibility changes now keep the exact renderer's tile
results and immediately evaluate them against the current bounds, zoom and
source readiness. Partial failures remain disclosed. Completion while hidden
can establish a cached tile for that same source; it does not display a hidden
layer or acquire new data. Replacing/removing the renderer source, changing the
basemap, or explicitly retrying invalidates the previous coverage. A settled
source alone still cannot establish coverage, and cached tiles from a disjoint
viewport or coarse zoom cannot attest the current view.

Actual callback regressions cover repeated warm toggles, hidden completion,
partial coverage, bounds/zoom changes, unsettled sources and renderer
replacement. This is a display-status repair in existing `app/`, `tests/` and
`docs/` responsibility roots under Directory Rules v2 and accepted ADR-0029.
Provider requests, cache budgets, payloads, dates, opacity, water rendering,
free reports, publication policy and the private Sites project are unchanged.
Reverting this patch restores prior status handling without changing stored
data. Hosted acceptance and owner approval of this new revision remain separate
from local regression/build verification.

Changed-area validation passed: production build, TypeScript, 53 scoped
callback/lifecycle/navigation/water tests, two report-privacy tests and six
local production-server HTTP checks. ESLint has zero errors and the same 42
warning messages as the exact base; these inherited warnings are not a clean
lint claim. The old page fails three new callback regressions.

In the candidate browser, eight warm 2D hide/show cycles immediately restored
Displayed with 46% opacity; four Terrain 3D cycles retained Displayed with
partial response. Actual free JSON/HTML exports worked and retained evidence
limitations; JSON also retained the terrain context. An isolated 2D
interrupted-pan sample reached 59.9 FPS,
p95 17.6 ms, max 19.2 ms and zero intervals over 25 ms, with ten selected layers,
2,311 flowing reaches and unchanged data signature. This measures one RTX 5080
workload at zoom 10.5, not every device or provider condition.

Terrain 3D pacing remains variable: candidate samples were 49.4–58.4 FPS and a
later unchanged-live-revision control was 43.3 FPS under the current conditions.
Earlier live samples were 59.1–59.5 FPS. These are separate live provider
snapshots and are not a controlled before/after claim or proof of sustained
3D 60 FPS. All samples, including slower and competing-tab runs, are retained
in the delivery receipt. This status repair does not modify water/terrain
rendering or claim to resolve that performance limit.

## Authority and scope

Started from the same-Site source of owner-private Explorer v232,
`2e35af50b61655cf2775f8db33b13b8055cc5779`. Native Sites readback confirmed a
successful deployment and owner-only custom access revision 1, with DB/BUCKET
bindings. The source was opened in a new isolated checkout. The original KFM
worktree at `e53b94caa7f3bca00d61ab2e10c5373a054caa2c` was clean and preserved.

Before delivery, native readback identified concurrent v233 source
`2e8650133d2a1a0ecb44db8bab00bd9f6dc7b0b9`. Its search-to-layer routing,
guide focus return, and map keyboard focus/CSS fixes were preserved by applying
this patch onto a fresh v233 checkout. Typecheck, build and all tests were rerun
on the reconciled source. The security scan reviews the frozen layer patch
against v232; the concurrent changes are identified separately, not claimed
as part of that diff scan.

[GitHub #5035](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5035)
and [#5036](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5036)
identify separate weather integration and provenance work; they do not establish
standalone Site parity. [Drive Chronicle](https://docs.google.com/document/d/1fBOUDqrcsHaPJiEfM5HmtJL7fBMKFr-rgoN2ge_uVrI/edit)
was checked; its v230 checkpoint is historical relative to native v232.
The [Notion performance roadmap](https://app.notion.com/p/3d8a92021bf68190a68ef071b378162e)
requires exact source times, explicit limits, cold/warm measurements and device
acceptance. Its October 8 edition is planning context, not current deployment authority.

## Lifecycle trace

| Stage | Owner and behavior |
| --- | --- |
| Selection | `page.tsx` holds requested visibility, opacity, saved exploration context and source-specific dates. Selection survives Browse/On map/topic filtering. |
| Eligibility | `live-context.ts` applies supported atlas frames, regional Mercator restrictions and source zoom limits. Requested and actually displayed remain distinct. |
| Retrieval | Current JSON feeds use `refreshOfficialContext`; explicitly dated reads use `loadOfficialArchiveDay`. River Pulse, NOAA gauges, radar/GeoColor, groundwater and soil controls retain separate adapters and source-time contracts. MapLibre schedules visible tiles. |
| Scheduling | `LayerJsonReads` allows three selected/explicit JSON reads at once; queued reads canceled before starting never fetch. Exact URL plus byte budget identifies a shared acquisition. Cancellation belongs to each consumer; the final consumer cancels the stream. |
| Validation | Bounded JSON reads include the body deadline, feed identity, response state, feature count and retrieval time. NASA source day must match; other adapters' optional source-day claims must match when supplied. An absent day claim is not invented. |
| Cache | Only dated generic context responses use a five-minute, four-entry page-memory LRU. Each response is at most 8 MiB serialized input (32 MiB aggregate input ceiling; not a heap-memory guarantee). Original retrieval/observation times remain intact. Current and explicit Retry reads bypass it. Existing opt-in browser file caches and provider tile caches retain their own limits. |
| Rendering | `applyOfficialContextState` shares unchanged GeoJSON feature references, applies effective visibility, balances related raster opacity, and composes rasters/areas/lines/points/selection. Registry filters, zoom limits and ordering now skip unchanged writes and invalidate on renderer identity changes. |
| Interaction | One sampled rendered hit stack supplies hover/click, local previews and basemap fallback. The top eligible visible provider/registry feature receives input. Zero requested opacity cannot take provider/registry input. Local preview ownership and display-only/evidence separation remain intact. |
| Removal | Hiding generic JSON layers aborts pending/queued reads, clears pending ownership and returns the control to its confirmed or idle state. Confirmed snapshots stay available within this page. Leaving Present cancels obsolete current generic reads. Unmount cancels remaining requests and disposes map/renderer work. |
| Failure/retry | Current refresh failures clear older mapped generic geometry; dated selections clear incompatible old geometry before loading. Empty is a checked empty response, never an inferred zero or all-clear. Partial stays partial. Retry bypasses the new memory cache. |

Radar's exact-frame staging buffers, SMAP/Crop-CASMA controls, HMS progressive
playback, river direction previews, groundwater bounds/record caps, evidence
selection coherence, saved camera context, keyboard alternatives, reduced motion
and battery saver remain separate existing mechanisms. This patch adds no source,
data import, governed activation, storage migration, policy change or mirror waiver.

## Reproducible measurements

Run from this Site checkout with installed locked dependencies:

```sh
# Preserve the immutable baseline in a separate directory before editing:
git show 2e35af50b61655cf2775f8db33b13b8055cc5779:app/page.tsx > /tmp/kfm-layer-baseline/page.tsx
git show 2e35af50b61655cf2775f8db33b13b8055cc5779:app/map-runtime.ts > /tmp/kfm-layer-baseline/map-runtime.ts
node scripts/measure-layer-lifecycle.mjs /tmp/kfm-layer-baseline
node --test tests/layer-lifecycle.test.mjs
```

Create `/tmp/kfm-layer-baseline` first. This controlled benchmark uses the actual
production date callback and registry functions with synthetic empty earthquake
responses, an 80 ms adapter delay, and 24 synthetic registry layers / 48 renderers.
Fixtures are never installed or served by the application. It does not measure
provider speed, map GPU frames, browser INP, or device performance. The deployed
v232 legacy registry is empty; its mutation result is scalability regression
coverage, not an observed improvement in today's provider-layer frame rate.

Observed on Linux / AMD Ryzen 9 9950X / Node v22.13.1:

| Scenario | Before | After |
| --- | --- | --- |
| Six alternating dated reads, two unique days | 6 requests, 501.095 ms | 2 requests, 169.033 ms |
| Four repeat date reads | 80.470–80.715 ms each | 0.031–0.071 ms each |
| First two date reads | 91.162 / 80.641 ms | 81.659 / 80.612 ms |
| 100 opacity updates in the synthetic registry | 24,000 map mutations | 200 map mutations |
| Registry loop CPU time (single run; noisy) | 6.232 ms | 3.642 ms |
| Sampled hover/click hit queries | Multiple queries (up to 4, plus local preview query) | 1 shared query |

The request reduction, mutation counts and correctness assertions are stable
comparisons; single-run submillisecond timings are illustrative. Cold provider
work is still required. A different UTC day can be checked while the previous day is loading; the prior request is canceled.
Progress distinguishes waiting for a slot from receiving
data and explains that hiding cancels acquisition.

## Acceptance evidence and limits

Deterministic tests cover shared consumers, queued cancellation, replacement after
abort, bounded LRU expiry/eviction, current/forced bypass, partial/empty/failure,
wrong-day rejection, topmost overlap, actual date callbacks completing out of
order, failure clearing old geometry and explicit retry. Existing transport tests
exercise stalled headers/body, body cancellation and byte bounds. Existing real
callback tests retain measurement, local preview, scene/evidence fallback and
HMS transition ownership. Full production build, TypeScript and Site tests are
recorded by delivery separately from deployment.

Local Chrome smoke exercised ten show/hide actions on NIFC context with five
selected layers; final selection count, counties and River Pulse displays remained
coherent. The automation took 29.231 s for ten actions, dominated by automation
round trips; this is not an input latency measurement or a rapid-toggle benchmark.
Actual rapid timing is covered by controlled callback tests.

Local Chrome also exercised a new date while the previous archive request was
loading, then hid the layer. Selection counts returned coherently and acquisition
stopped. A mobile viewport smoke opened the layer dialog, toggled the earthquake
checkbox using Space, and closed with Escape; focus returned to the map. This
is a narrow keyboard/responsive smoke, not comprehensive accessibility acceptance.
The final cancellation copy distinguishes an uncompleted day from a checked
empty response. Reduced-motion safeguards remain covered by existing tests;
browser reduced-motion emulation was not available in this session.

Real GPU FPS/long tasks/INP, throttled browser network conditions, a full physical
device matrix, long-session resource retention and comprehensive visual and
accessibility acceptance remain unverified. No synthetic benchmark or successful
publication closes those gates. Source-provider failures and missing coverage
remain explicit rather than replaced with invented data.

### Independent browser matrix evidence — November 6

Review run 42183198971 reached the final Explorer cases but exhausted the
existing combined job's 30-minute allocation. The complete
`tests/explorer-startup.browser.mjs` invocation now runs in its own
`explorer-browser` job, on the same pinned source, Node and locked dependencies.
The original HTTP/database/specialist-browser checks remain in
`verify-core-delivery`. Every Explorer case, assertion and per-test deadline is
retained; the overall allocation is not increased. Runtime logs and screenshots
are uploaded independently so an unrelated check cannot hide this matrix's
evidence. This is CI scheduling, not an application performance improvement or
a substitute for correcting the documented source and fixture defects.
