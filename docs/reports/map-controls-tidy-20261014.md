# Tidy live-map controls — 2026-10-14

The Explore tab and its large navigation pane are removed. Appearance and Measure remain. Underground is an Appearance choice, while navigation stays on the live canvas and secondary navigation uses its small inline menu. The header no longer repeats Underground, 2D, Terrain, Globe, Compare or basemap controls. Their functions remain reachable from Appearance, the Map menu or advanced tools.

## Source and placement

This interface-only batch starts at repository `5ff78dacc4f035e92959625155994979a2640c17` and authoritative native Site v267 `8b4c03a5ba2c803d1f323460a23778adc8e4c76b`. Native v268 is saved from `358280aee889e2e2cf832bd598155ca21653c8de` without deployment. Its audience and DB/BUCKET declarations are unchanged. The application mirror stays in `apps/site/source`, checks in existing test responsibilities, and this report and append-only receipt in their existing documentation/evidence roots, following Directory Rules as adopted by ADR-0029.

The PC application deliberately uses a separate compatibility patch at `a438b2dd3dad0206b1b8e86245a7c3bf6ed74ee2` on its existing v259 `441c3e29581ffb0293d8e643e5c37eed50319032`. It is not described as full-source-equivalent to native v268. All 273 public asset files remain identical to that local base. The 995 tracked source files and 428 prepared build files match the installed patch; 42 older immutable assets remain for existing tabs. The prior install and v109 persisted store remain retained. Only the existing Explorer service was restarted, preserving its original store and local imagery configuration. Other services and working copies were untouched.

## Executed verification

- Native: production build, TypeScript, 1,336/1,336 tests; 32 focused controls, Underground, phone and focus checks.
- Local compatibility: production build, TypeScript, 1,156/1,156 tests.
- Composed repository: production build, TypeScript, 1,347/1,347 tests; changed-area lint zero errors and 44 warnings. Warning inheritance was not separately established.
- Mirror guards: 38/38 tests; recorded content parity passes, with eight existing overlays and 258 historical withheld paths retained. Content parity does not approve review, release or hosted equivalence.
- Isolated local browser: two primary tabs, four Appearance view cards; Underground enters the existing workspace and transfers focus. High Plains keeps 50 records and 28 columns, one aquifer overlap and complete 2048×1718 surface, with partial coverage and unbounded-class limitations intact.
- Phone viewport at 390 pixels: choosing Line closes the pane and returns focus to the live map; real two-point drawing, finish and clear work without horizontal document overflow. Viewport override restored.
- Installed port 4173: compact header and Appearance/Underground entry verified. Escape closes Appearance and restores Map-menu focus; Underground closes to the live map. The user's existing 1833 time filter remains selected and correctly withholds incompatible records, without changing aquifer time support. Existing 2048 surface completes. HTTP returns 200.

One captured React 418 hydration error at 15:01:28 UTC did not recur after subsequent installed reload. Its cause remains unattributed; this report does not call historical captured logs empty. The browser-geometry script has updated selectors but was not executed. These are bounded observations, not full device, accessibility, long-session, performance or hosted acceptance. Native v268 is saved only; this batch did not change the hosted application or GoDaddy application, activate data, change access or install acquisition jobs.

## Recovery and review

Restore the retained v259 alias and restart only the existing Explorer service to recover the prior UI, leaving its store intact. Revert the repository UI changes and receipt selector together, retaining both immutable receipts and safety overlays. Native publication and repository merge require their separate owner disposition. New receipt `data/receipts/generated/site-v268-tidy-map-controls-20261014.json` remains REVIEW_ONLY, with human acceptance and source/overlay review pending. Exact-head CI is reported separately on the pull request.
