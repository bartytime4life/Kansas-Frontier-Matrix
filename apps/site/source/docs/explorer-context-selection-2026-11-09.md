# Context transport, export integrity and repository recovery

This bounded correction starts from main
`91e743e940eb1b5f4db2e07473af460f274a2b1b`, the independently merged PR #5791.
It improves existing public display and reviewed-export paths without admitting
sources, releasing data or changing hosted state.

## Confirmed problems and corrections

| Surface | Reproduced problem | Resulting behaviour |
|---|---|---|
| NOAA hydrology transport | Successful readers held locks; an oversized response waited forever for uncooperative cancellation; a stalled body outlived the timeout | Bound binary collection with the existing helper, retain the complete-read deadline, release reader locks and cancel rejected bodies without awaiting cancellation |
| USGS streamflow transport | The same lock/cancellation failures affected response and shared network budgets | Preserve per-chunk accounting across concurrent reads and existing aggregate limits while adding abort handling, nonblocking cancellation and unconditional reader cleanup |
| GBIF flora/fauna tiles | Empty HTTP200 or206, including HTML, became a transparent tile labelled no-records | Treat only the source's explicit204 as the existing empty-tile case; require a nonempty200 of the existing image MIME for normal imagery |
| Reviewed water/weather exports | HTTP failures with otherwise matching JSON could still create a verified download | Reject failed HTTP responses before parsing evidence or exporting; preserve release, expiry, station, package and selection-generation checks |
| Repository briefing | A stalled response left Checking current main and a disabled Refresh indefinitely | Apply a fifteen-second header/body deadline, keep Restart available while pending, expose Retry on failure, and ignore late results after close/restart/timeout |

The modal also keeps its status, tabs and Close control reachable on phones and
short screens through one vertical scroll container.

GBIF documents its density endpoint's200 response as a map tile and204 as an empty
map tile in its [official Maps API specification](https://techdocs.gbif.org/openapi/v2-maps.json).
The existing country/year/taxon/coarse-bin queries remain unchanged. An empty
occurrence-map tile establishes neither ecological absence nor source completeness;
these layers remain external display context. Satellite date confirmation and its
separate no-substitution rule remain intact.

NOAA keeps its original replacement UTF-8 decode and structured error codes. USGS
keeps fatal decoding and its shared per-chunk network budget, rather than reserving
a full response allocation for each concurrent request. The change adds no browser
request-signal forwarding to those routes. Read deadlines do not establish provider
completeness or scientific/operational accuracy.

Repository observations keep the existing one-minute, observation-time expiry,
fixed public repository identity, pinned historical Site snapshot and separate
source histories. Retry does not synchronize code, inspect CI, activate data or
write to GitHub. Existing modal focus trapping and Escape behaviour are retained.

## Validation

- Final production build and containment checks pass. TypeScript passes. All 1,622
  Site tests pass, including the complete repeat after the browser-discovered CSS
  correction. Lint reports zero errors and the same 77 inherited warnings.
- Water-conformance passes 371 tests, including 70 mirror regressions. Strict
  inventory covers 923 files with no unexpected difference; all 262 withheld paths
  remain absent and predecessor bytes/dependency inputs are unchanged.
- Disposable backend smoke passes 110 checks across 79 routes; 14 provider-only
  routes remain outside the offline check. The later CSS-only correction changes
  no backend source.
- Independent source/test review passes for transport, data/export, repository
  lifecycle and modal scrolling. Native Response fixtures exercise cap/timeout,
  uncooperative cancellation, concurrent byte accounting, failed HTTP exports,
  explicit empty tiles, late reads, restart/close and observation-based expiry.
- The actual final built app shows a finite timeout after a deliberately stalled
  body and recovers through keyboard Retry using labelled synthetic metadata.
  At 390×844, native wheel scrolling reaches the status card and all seven tabs;
  Functions opens its content, Close stays visible, Enter preserves the recovery
  control's focus, and Escape returns focus to More. Document width is 390 pixels.
  Short-desktop 1280×720 scrolling also reaches the status card and tabs.

The first phone check exposed a 1047-pixel snapshot in an 844-pixel overflow-hidden
modal, making lower controls unreachable by wheel. Only repository selectors in
globals.css changed: one vertical scroller, sticky opaque heading/Close, expanding
content and three-column phone tabs. The final browser rerun confirms recovery.
Before/after screenshots were saved and inspected. A transient capture immediately
after reflow was excluded; the accepted phone captures show the settled layout.

The before-capture used the real built application through a labelled loopback
proxy that stalled only repository-status after headers and a JSON prefix. The
old screen stayed pending with Refresh disabled. The proxy blocks application
writes and can release a clearly synthetic metadata observation through an
explicit fixture control. Synthetic response behaviour is distinct from live
GitHub availability, private authentication, evidence stores and production
acceptance. The actual local map and source-status entry were also inspected.

## Inventory and rollback

The append-only `site-v268-context-selection-overlay-20261109.json` successor binds
seventeen Site source/test/style/note changes to the unchanged previous receipt. Three
new Site files extend the inventory; all 262 withheld carriers remain absent.
Authority remains CONTENT_PARITY_ONLY, status REVIEW_ONLY, source/overlay review
pending, and human acceptance/hosted equivalence false. Historical Site identity
is an inherited declaration, not a fresh hosted-source readback.

The original owner checkout is preserved. No dependency, operational store,
schema, access, admission, release, deployment or publication changes. Undo with
a focused inverse commit or reviewed forward correction. Revert successor and
selector together; preserve every predecessor receipt and withheld path.
