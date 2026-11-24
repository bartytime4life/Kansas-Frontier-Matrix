# KFM live-site audit · 24 November 2026

Scope: the public GoDaddy site at https://kansasfrontiermatrix.com, application `urdng3v1vk`, published source `8859a1d29466ec3dae4180077a6aaa6ec920e894`. Read-only public route checks and actual browser journeys were followed by bounded source fixes. The separate dirty monorepo checkout and original Sites composition were preserved.

## Observed journeys

| Step | Journey | Result and evidence |
|---|---|---|
| 1 | Open welcome and choose Terrain & elevation | Welcome renders and opens the working map. An existing terrain session had an internal `MAP_SOURCE_FAILED` warning. Captures 01–02. |
| 2 | Close landscape → Whole Kansas; inspect source status | The close view can become ready. The long statewide transition produced busy DEM replies and an unavailable state. Controls remained available. Capture 03 and the saved network event window. |
| 3 | Find Sedgwick County and open its record | Search returned the correct county. Keyboard activation opened the 2020 Census record with population, geometry edition, source link and limitations. Capture 04. |
| 4 | Data Library → railroads → Atack Railroads → first page | Filter returned two collections. The chosen collection returned 20 records with retained fields, pagination, download and retrieval time. Capture 05. |
| 5 | Research atlas → Signal Studio → year-to-year differences | Real source snapshots loaded. The selected annual-pair count changed from 76 to 75 and statistics recalculated. The result retained units and the association/causation boundary. Captures 06–08. |
| 6 | Phone welcome → map → layer sheet → river filter | At 390 × 844, welcome, map controls and sheet fit the viewport. Filtering exposed three river layers. Selecting River Pulse changed its state to Displayed. Captures 09–11. |
| 7 | Candidate phone science table → inspect annual pair | The changed row action is 44 × 44 CSS pixels and still selects the correct source pair. No horizontal page overflow was observed; the wide data table scrolls inside its container. Capture 12. |

A separate bounded HTTP sweep read all 43 static page routes declared by the current application. All returned HTTP 200 without a server error/recovery page. This checks route delivery, not every interactive control or every parameterized record route.

## Fixes in this change

1. **Reduce unnecessary live elevation exports during terrain shortcuts.** With USGS 3DEP selected, Whole Kansas and named landscape navigation now move directly to the target camera. Previously the 1.4–1.8 second zoom animation requested intermediate DEM levels; abandoned work could occupy the host's 16-request pool before the destination loaded. The final camera, source, units and vertical scale are preserved. Coarse Mapzen context retains its existing animation. Ordinary user navigation and provider failure behavior are unchanged. This reduces one known source of avoidable requests; it does not guarantee that the provider or a large final viewport can never be busy.
2. **Retain actionable terrain recovery instructions.** The initial terrain failure message was later overwritten by an internal runtime-proof code. The load and idle paths now retain the specific recovery message: retry the selected DEM or choose coarse display context. The finite diagnostic, readiness requirements and degraded state remain intact. No missing height is inferred.
3. **Honor original elevation-cache expiry.** A nearly expired 3DEP tile could still advertise 900 seconds of browser freshness. Memory and edge replies now cap `max-age` at the original copy's remaining lifetime, and recompute `s-maxage` on edge reads. Retrieval time and pixels are unchanged. The regression checks five seconds remaining, less than one second remaining, exact expiry, and a new upstream read after expiry.
4. **Enlarge phone source-row actions.** Signal Studio's annual-pair selection buttons were 25 pixels tall. At narrow widths or with a coarse pointer they are now at least 44 × 44 pixels, without changing the scientific calculations, selected pair or desktop table density.

## Validation

- Production build, TypeScript and changed-file lint pass.
- Application Node suite: **3,570 passed, zero failed, 25 explicit skips**.
- Thirty focused terrain/cache/category checks pass.
- All three isolated terrain-browser journeys pass: desktop and phone automatic fallback, plus successful USGS loading and manual provider recovery. They use synthetic DEM transport with real installed MapLibre/WebGL; they do not certify current USGS availability. The manual-outage case checks the recovery wording and that an internal code does not replace it.
- The candidate phone science row was measured and activated in the in-app browser using real public source snapshots. Its 44 × 44 target selected the correct row.
- Remote CI and public publication are recorded separately in the handoff. A source build or merge alone is not a live deployment.

## Remaining priorities

- Reusable geographic Ground/Surface/Canopy tiles and a coverage manifest remain the largest planned terrain optimization. Keep heavy source processing on dev, compact reusable outputs on GoDaddy and bounded active-view work in browsers, as specified in `resource-placement.md`.
- The pinned Node framework creates route Requests without tying their signal to a disconnected socket. Browser cancellation therefore does not establish upstream cancellation on GoDaddy. A future transport-lifecycle change needs an actual HTTP disconnect regression and must retain concurrency slots until the underlying read settles.
- Broad final views can still need many legitimate elevation tiles. A bounded priority queue, persistent prepared tiles and per-view coverage states deserve measured follow-up; increasing limits or concealing gaps would not fix source latency.
- Signal Studio's introductory section uses much of a phone's first screen. A compact returning-user introduction could expose the controls sooner. This is a design opportunity, not a failed scientific workflow.
- The browser snapshot exposed repeated decorative disclosure arrows from filtered content. The hidden rows had `display:none`; an assistive-technology check is needed before attributing this to a screen-reader bug rather than capture behavior.
- This is a representative combined functional/UX audit. No full WCAG certification, screen-reader acceptance, sustained-load benchmark, universal device-speed claim, new source admission, or survey-accuracy certification is made. No private files were uploaded and no paid service was added.
