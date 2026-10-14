# River Pulse startup request ownership — 2026-10-14

Baseline: owner-private Explorer v262, source
`10c9a0a2f2a3833a08869ddb28e7dd037e83a054`, same Site
`appgprj_6aa0b1c41bc08191bfd86003920f1631`.

The automatic River Pulse cadence called its immediate refresh before the
deferred URL/same-tab history restore selected the actual station, day,
visibility and map year. An archive startup therefore issued a default
statewide request, then the intended station-day request. A hidden River Pulse
could also acquire default data before its visibility was restored.

The immediate/cadence refresh now requires the existing
`explorerRestoredRef.current` readiness marker. The restoration callback still
starts the validated selected query. Explicit refresh, station/day selection,
retry, coalescing, cancellation, generation protection and the five-minute
current refresh are retained. No requests, source payloads, timestamps, units,
data eligibility, private candidate assets, source admission, DB/R2 bindings,
audience or provider budgets were replaced or relaxed.

## Reproducible browser experiment

Build the unchanged base, then the patched source with the same locked
dependencies. Use Vite production preview on 4199, and the task-owned QA proxy
on 4217 with `QA_PHASE=before` or `after`. Both phases use normal transport;
there is no synthetic provider replay or artificial throttle. The proxy injects
local PerformanceObserver instrumentation only; neither it nor measurement
code is included in the Site source/deployment. Raw exports, proxy events,
before/after regression logs and context-failure comparison live outside the
application in the task's `.layer-system-work/startup-request-evidence/`.

Historical URL: `/?ctx=usgs-streamflow,census-counties,usgs-3dhp-hydrography,nasa-gibs-fire-points,nifc-fire-reports&hydroStation=USGS-06864500&hydroDay=2024-09-02&hydroTime=2024-09-02T23%3A45%3A00Z&t=2026&c=-98.38,38.48&z=5.45`.
Open it, inspect River Pulse, export QA metrics, reload twice and export each
result after data arrives. Preserve the same station/day/frame and map context.
Hidden control: `/?ctx=census-counties&t=2026&c=-98.38,38.48&z=5.45`.
Current control: `/?ctx=usgs-streamflow,census-counties&hydroRange=24h&t=2026&c=-98.38,38.48&z=5.45`.
The after Current control additionally restored Ellsworth; its network endpoint
is identical, and the selected station remained coherent.

Browser: Codex in-app Chromium, Chrome/155 Linux user agent. The first two
baseline exports were 1280 × 720 CSS pixels; the third resized to 1761 × 1292
with the visible app window. All after runs were explicitly fixed at
1280 × 720. Counts are exact for each run. Timings below are descriptive and
are not a statistically controlled speedup claim: caches, provider acquisition,
window size and normal workstation scheduling can vary.

| Measurement | Before | After |
|---|---|---|
| Historical startup River Pulse requests, 3 runs | 2 / 2 / 2 | 1 / 1 / 1 |
| Obsolete statewide requests in those runs | 1 / 1 / 1 | 0 / 0 / 0 |
| Selected historical station requests | 1 / 1 / 1 | 1 / 1 / 1 |
| Browser historical resource duration, ms | 644.6 / 530.4 / 549.1 | 673.1 / 455.3 / 502.1 |
| Historical resource median, ms | 549.1 | 502.1 |
| Historical accepted response body | 25,644 bytes | 25,644 bytes |
| Selected station/day/frame | Ellsworth / 2024-09-02 / 96 of 96 | Same |
| Hidden-layer startup River Pulse requests | 1 | 0 |
| Current startup control River Pulse requests | 1 | 1 |

The baseline proxy canceled two obsolete requests after 16.6 and 9.6 ms. In
the third, it finished sending a 730,598-byte cached response in 11.4 ms even
though the browser's ResourceTiming record reported a canceled/zero-body read.
These are different observations: proxy bytes sent are not proof that the
browser accepted, decoded or displayed those observations. The hidden baseline
did accept an unnecessary 730,598-byte network body. After the fix neither
archived nor hidden startup issued that request. No GPU FPS, INP or rendering
speed improvement is inferred from these request measurements.

## Validation and boundaries

Four tests execute the actual production effect: pending restoration cannot
start default work; archive ownership suppresses current cadence; restored
Current retains immediate/five-minute refresh and hidden/in-flight checks;
deselected/non-present stops playback without registering a cadence. The first
two fail on unchanged v262; all four pass after the guard. Browser Current
loaded 17,373 observations with exact source frames; historical runs retained
96 observations ending at 2024-09-02 23:45 UTC.

TypeScript and production build passed. Full suite: 1,231 pass / 7 fail out of
1,238. All seven failed names and reasons reproduce in an immutable v262 copy:
missing monorepo policy/weather files, sibling Desk/serve-local files and
subsurface temporary paths rejected under the standalone directory layout.
No tests, storage-denial controls or governed data were weakened to obtain a
green result. Full-suite/monorepo validation remains unresolved.

Local `/api/governed/v1/layers` reports `RELEASE_STORE_UNAVAILABLE`; that remains
a separate governed-data limit. Request elimination, local/browser checks,
private Site deployment, mirror review, source admission and owner acceptance
are distinct claims. The final native deployment and hosted browser readback
are recorded in the task receipt after publication.
