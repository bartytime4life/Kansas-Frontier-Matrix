# Layer browser validation — 2026-10-11

## Source identity and preservation

Measured baseline: deployed Site v234, `ab5bb6be71782f410ed182a11c57d891803ce292`, project `appgprj_6aa0b1c41bc08191bfd86003920f1631`.
Changes start from the same Site's newer v237, `a01910bd3fda88271107d971ac16be98e3efcf67`. v235–v237's concurrent source-search, closed-disclosure focus, and Underground close-focus fixes are retained. The v234 Shift+Tab failure was repaired concurrently by v236, rather than attributed to this patch.

Owner-private access revision 1, zero external visitors, existing DB/BUCKET bindings, archive schedule, provider provenance and data-admission boundaries are retained. No GitHub mirror receipt, reviewed data, Earth Engine activation, or governed release was changed. The original workspace remains preserved; QA, source checkouts and evidence are isolated. The local QA proxy and instrumentation are excluded from application source and deployment output.

## Browser and reproducible conditions

Native Chrome 154 on the user's Linux workstation; browser input through CUA, real MapLibre 6.9.0 production builds and actual provider responses. No fixture substituted for provider data. Browser PerformanceObserver recorded paints, resources, EventTiming and main-thread long tasks; a local, test-only script sampled rAF for five seconds. DOM observations measured control bounds, names, focus and computed colors. Existing unrelated user tabs were left open.

Production previews: baseline upstream 4190 / instrumented proxy 4191; changes upstream 4192 / proxy 4193. `npx vite preview --host 127.0.0.1 --port <upstream>` serves the already built source. The independent proxy harness supplies normal/slow/fail and export controls. Raw artifacts and both harness files are preserved in the task workspace's `.layer-system-work/browser-qa-evidence/`; its README gives the full reproduction protocol and timestamp caveats.

Slow mode adds 3,000 ms **after upstream response headers**, then streams 16,384 bytes/sec in 4 KiB chunks, for `/api/live-context` and `/api/hydrology/streamflow|noaa` only. Real upstream/provider latency remains included. External tiles, static assets and other APIs are unchanged. This is controlled API response throttling, not whole-browser 3G emulation. Fail mode injects explicitly labelled HTTP 503 after 500 ms. Neither fault mode exists in the published Site.

## Measured results

| Measurement | v234 baseline | Final v237 + fixes |
|---|---:|---:|
| Repeat-navigation FCP | 136 ms | 116 ms |
| Repeat-navigation LCP | 720 ms | 400 ms |
| Main-thread long tasks during five-second zoom/opacity sample | 0 | 0 |
| rAF interval p50 / p95 / max | 33.4 / 66.7 / 66.8 ms | 33.4 / 66.7 / 66.8 ms |
| EventTiming duration p95 in that sample | 80 ms | 112 ms |
| River Pulse response body, normal repeat | 4,418,336 bytes / 202.6 ms | 4,422,366 bytes / 374.4 ms |
| Two subsequent checks of an already loaded exact day | 0 additional API requests | 0 additional API requests |
| Mobile search input height | 20 px | 44 px |
| Mobile opacity slider target height | 24 px | 44 px |
| Search clear / Change time height | 36 / 36 px | 44 / 44 px |
| Browse / On map / Imagery height | 42 px | 44 px |
| Details disclosure / source-quality action height | 38 / 28 px | 44 / 44 px |
| Page width at 320 / 390 CSS px | 320 not measured / 390 px | 320 / 390 px |
| Back/reload context | Returned to 5 defaults; archive day lost | 6 selections, 2024-09-02 UTC and 91% opacity restored |

These paints are repeat navigation measurements with warmed and variable browser/server/provider caches, not evidence of a causal loading speedup. An earlier first visit to v234 observed FCP 144 ms, LCP 1,080 ms and River Pulse 3,427.2 ms; the first corrected build observed FCP 176 ms, LCP 728 ms and River Pulse 4,238.8 ms. The varying payload and upstream processing prevent a like-for-like provider speed claim. The final normal sample is `browser-1791754276830.json`; baseline `browser-1791753060640.json`.

rAF measures callback cadence, not GPU/map FPS. The callbacks still show 33–67 ms cadence on this shared workstation; no rendering-speed improvement is established. EventTiming p95 increased in the short normal sample (80 → 112 ms); this is recorded as unresolved variability, not labelled an INP regression or silently omitted. It counts event entries rather than deduplicated full interactions. `nextAnimationFrameMs` measures the next callback, not complete map presentation. Samples are short single-session observations, not a device or Core Web Vitals certification.

## Journeys and fixes

- **Rapid selection:** Five off/on pairs under slow delivery settle on one selected earthquake layer, without duplicates or lost other selections. Obsolete requests deliver zero bytes. The initial corrected run canceled four earlier requests in 51.6–69.8 ms; its surviving request finished in 3,320.1 ms. v234 canceled earlier requests in 41.4–130.2 ms and finished its surviving request in 3,627.5 ms. These are local/browser/network-condition observations, not provider benchmarks.
- **Rapid exact dates:** Checks for 2024-07-01, 2024-07-02 and 2024-08-02 are started before delivery. v234's first two requests canceled in 160.7 and 109.8 ms, zero bytes; latest finished in 3,733.8 ms. The corrected run canceled them in 153.3 and 98.8 ms, zero bytes; latest finished in 3,522.5 ms. The final displayed day is exact and empty: zero returned records, zero event frames, no earlier day substituted. Two repeated checks produce no new requests.
- **Partial failure and recovery:** Failure of a selected earthquake request leaves the other map context intact. Added a per-layer alert and direct **Retry layer** action. Current and exact-day retries reuse the source's existing owner and exact selected day; dated retries force a fresh scheduler read. Keyboard focus moves to the stable layer toggle before the transient button disappears. A failed 2024-09-02 request took 502.6 ms; slow retry took 3,813.2 ms and correctly returned an explicit empty result for that same day. River Pulse also recovered through the inline retry: a 502.6 ms injected refresh failure, then a 47.4 ms warm 4,410,249-byte response. Its retained observations are described separately from a fresh response. The generic retry message does not falsely claim retained operational observations were deleted.
- **Overlapping layers:** At the actual NASA pixel above the Census county, pointer input selects the NASA record (0.71 MW, nominal confidence, 2026-10-11T07:56:00Z; scan/track pixel 0.4/0.44 km). At zero detection opacity, the same position selects Shawnee county and its dated 2020 Census population 178,909. Provider identity, limitations and units remain intact. Hiding a layer removes its map halo while its captured record remains available for inspection under the existing hidden-layer warning. This patch does not erase that intentional review context.
- **Mobile and keyboard:** 390×844 and 320×844 CSS viewports have no horizontal page overflow. Enlarged search, clear, topic, date, tab, opacity, disclosure and quality actions to at least 44 px high. Native toggles/close controls were already 44×44. The search name remains exactly “Search map layers” when Clear appears. Shift+Tab wraps Close → Other map tools; Tab wraps back to Close; Escape returns to Map. Retry measures 44 px high, 93.5 px wide, with a visible 2 px focus outline. 44 px is a usability target, not an assertion that every smaller baseline control violated WCAG AA.
- **Accurate accessible status:** Replaced “0 layers visible” (which counted only released local layers while external layers were displayed) with the actual selected-map-layer count and an instruction to consult source/visibility status. Held, empty or unavailable layers are not announced as successfully rendered.
- **Navigation:** Added bounded per-history-entry restoration of the existing camera/layer/opacity/time parameters and validated archive days. Normal browser history is preserved, URL unchanged, embedded host history untouched. Unsupported feed IDs, impossible/future days, precoverage dates and prototype keys are rejected. Changed archive owners are aborted/cleared before reloading. Hidden archive selections retain their day without fetching. Two archive/Back journeys and a full reload retain six selections, the checked day and opacity. New requests revalidate the exact day after a new page mount; this feature preserves context, not provider payloads or source acceptance. A new visit without a prior history entry still uses defaults.

Computed contrast on actual selected card background `#1b303a`: title 12.30:1, metadata 8.10:1, recovery message 8.93:1. Retry text/background 12.31:1; focus outline/card 9.85:1. These sampled colors exceed relevant text/non-text contrast thresholds; they are not an exhaustive contrast audit.

## Validation boundaries and remaining work

TypeScript, production build and all **1,065 tests** pass. Three new tests cover history-state roundtrip, router-state and URL preservation, Current/date clearing, invalid dates/feed identities, blocked/embedded history and fallback to explicit URL. Existing stale-response, scheduler, governed-data and privacy tests remain passing.

Local browser journeys passed as described. Deployment is recorded separately in the task delivery receipt, followed by a hosted browser smoke check. Real fault injection measurements are local; they are not hosted provider outage measurements. Previous Codex Security review of the v232 layer patch is not a scan of this new history/UI patch. This patch was manually reviewed for bounded input, source identity, cancellation and embedded/privacy guards; no security control is waived.

Remaining limits: River Pulse's roughly 4.4 MB bounded response remains expensive on very slow links; a throttled refresh reached the existing ~60 s response timeout and required recovery. No claim of progressive full-window hydrology delivery or a GPU speedup. Local governed release-store 503 and Earth Engine catalog 401 remained fail-closed; no admission was inferred. Full browser/OS network profiles, physical mobile touch devices, GPU traces, screen-reader speech with NVDA/VoiceOver, and runtime OS reduced-motion emulation are not available through this browser surface. Existing reduced-motion guards and tests are retained, but OS preference acceptance is pending. Navigation restoration covers the four existing generic dated adapters; selected external feature snapshots and station-specific archive playback are not claimed as fully replayed across page mounts. Full hosted/accessibility acceptance remains separate from these concrete checks.

## Final source repeat

With the history restoration included, the ten rapid off/on actions canceled five obsolete/current-start requests in 43.1–102.0 ms, all zero body bytes; only the final selected request completed (3,237.7 ms, 2,689 bytes). The rapid-day repeat canceled July 1 and July 2 in 148.8 and 95.6 ms (zero bytes), and August 2 completed in 3,496.9 ms, 745 bytes. Two subsequent checks again made zero extra requests. This final rapid sample had no main-thread long tasks; rAF p50/p95/max was 33.4/66.7/66.7 ms and EventTiming p95 was 160 ms (v234 rapid sample 120 ms). These short-sample event durations remain an unresolved measured difference. Final raw session export: `browser-1791754472517.json`.
