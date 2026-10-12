# Layer lifecycle and performance — October 11, 2026

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
