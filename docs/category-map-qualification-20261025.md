# Category-map aviation reconciliation

This repair continues the category-map design merged in #5469 and the additional
basemaps and drawer work merged in #5471. Base:
`a0-hosted-ai-web-20261017@3de7c3f9c85d270f24896df866924edce9c4d075`.
The source snapshot was verified against all 1,582 Git blob hashes before edits.
No existing Site, data binding or provider configuration was replaced.

## Reconciliation

The hosted aviation control had been ported before #5468. Its applicable changes
from qualified head `c8abd1bd252e27647684b83ff31f8c7ab4ed3268` are now reconciled:

- mutually exclusive point/profile tools, map-center placement and capture-phase
  Escape cancellation before the compact navigation panel closes;
- selection ownership in the page click callback, both immediate and deferred
  hover sampling, and delayed Evidence Drawer previews;
- scrollable, focusable 760-pixel cross-section, numbered bands and corresponding
  ordered source list, invalid-path feedback and explicit selector labels;
- render-frame readiness and reduced-motion camera behavior;
- preview-cycle, incomplete-source, listed/future TFR and altitude-reference
  qualifications, including the absence of any clearance claim from blank areas.

The hosted component name, category `showRequest`, pinned bytes, provider routes,
shared upstream caches, Near-here dossier and held aviation-candidate component
are retained. A category show request never arms a picking tool.

## Sun direction

#5469's merged `syncRelief2d` correction already updates the category hillshade
from the effective scene azimuth. The repair adds regression coverage using the
actual aviation-chart and civic style builders, relief enabled/disabled, flat
Mercator, terrain and globe configurations, and normalized negative/wrapped
azimuths. No duplicate relief layer is installed.

## Verification and limits

Local production build and TypeScript pass. The full Node suite before the final
category-show assertion reported 1,854 passing tests, 19 explicit skips and no
failures. The focused reconciliation suite reported 103 passing tests. A fresh
exact-head hosted workflow and independent review remain merge requirements;
local checks are not their substitutes.

The final aviation suite, including category show-after-hide, passed all 45
tests. The actual Node HTTP boundary passed 22 tests. Isolated native-browser
startup/county-search and aviation-layout suites passed 58 and 6 tests,
respectively, including unavailable external services and mobile layouts.

Native Chrome on the local production build confirmed category navigation,
aviation preview labeling, map-dock 2D/3D controls and the sun slider, accessible
altitude slices, compact Escape cancellation without closing Layers, invalid
same-point feedback, map-center A/B placement and keyboard profile scrolling.
The chart remained 760 pixels wide in a 299-pixel panel; ArrowRight moved its
scroll position to 26.67 pixels. At the 390×844 phone viewport, the document
remained 390 pixels wide, the profile was 760 pixels in a 333-pixel scroll
region, map-center point inspection worked, and Escape at point B cancelled
drawing while preserving the open Layers sheet. Aviation 3D exaggeration,
government's illustrative welcome, civic navigation and globe/2D controls were
also exercised. The phone inspector qualified the loaded DEM reference and
did not infer clearance from missing surface restrictions.

Phone hit testing found another category-dock defect: the existing bottom
navigation covered both action buttons. The dock now reserves space above
that rail through its actual 760-pixel breakpoint and scrolls on short screens.
A native geometry fixture renders the actual stateless dock component with
production CSS for both categories and all three modes; it checks viewport
bounds, horizontal overflow and elementFromPoint for every button. It failed
at all four phone/tablet layouts before the fix, and passes at 320×568,
390×844, 568×320, 760×700 and 1440×900 afterward. This geometry fixture does
not claim live-tile rendering or hydrated callback acceptance; those are
separately covered by native UI review and the component regressions.

Some live aviation services returned context during local review; METAR returned
unavailable, and some basemap tiles failed. The viewer displayed the explicit
unavailable-observation and partial-map-degradation messages, retained controls,
and labeled NASR 2026-10-29 as a preview. A successful response is not completeness,
source admission, rights approval, flight clearance or public deployment proof.
Provider attribution and differing provider rights remain visible. Commercial
eligibility of the existing adsb.fi fallback is not qualified by this repair.

## Release boundary and rollback

This is application interaction and regression qualification only. It changes
no aviation source bytes, provider selection, refresh budget, admission status,
storage or deployment settings. No public publication or source activation is
authorized or performed by this repair. Missing tiles, incomplete FAA coverage,
facility-ground approximations, pressure-reference approximations and provider
rights remain explicit limitations. Revert this focused patch to roll back;
there is no data migration.
