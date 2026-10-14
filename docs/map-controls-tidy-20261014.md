# Map controls: one live-map workflow

The Explore tab and its large navigation panel are retired. Appearance and
Measure remain the two everyday control sections. Existing advanced tools,
source status, map layers, saved places, reports and exports remain available.

- The top toolbar keeps search, Time, Layers, Places and the Map menu. Duplicate
  direct Underground/2D/Terrain/Globe/Compare buttons and the wide basemap/control
  controls are removed. The Map menu keeps representation shortcuts and named
  Appearance/Measure entries at every width.
- Zoom and Fit Kansas stay on the live map. A small on-map navigation menu keeps
  view history, north reset, fullscreen, location and copying the center.
- Appearance adds Underground beside the three existing surface representations,
  using the existing transition, location privacy and workspace focus behavior.
- Coordinates, camera readouts, gestures, Shift-drag and area-of-interest tools
  move into Measure. Old `navigate` links and saved fallback views open Appearance;
  the saved value remains readable without reinstating the Explore panel.
- On phones, choosing Point/Line/Polygon closes the controls and focuses the live
  map. Measurement values and their approximate/browser-local boundaries remain
  unchanged. Desktop users can keep the pane beside the map.

## Source and preservation

The current-source candidate starts at native Site v267,
`8b4c03a5ba2c803d1f323460a23778adc8e4c76b`. Existing native publication holds,
owner-only access, DB/BUCKET bindings and public source bytes are unchanged.
The installed PC copy starts at v259,
`441c3e29581ffb0293d8e643e5c37eed50319032`. The same interface change is applied
as a separate local compatibility patch, preserving its existing 273 public
asset files, well/core projection, dependency lock and external persisted store.
These two copies are not represented as full-source equivalents. No data is
imported, regenerated, activated, promoted or exposed to a new audience.

Placement reuses standalone `app/`, `scripts/`, `tests/` and `docs/`; the repository
mirror remains `apps/site/source`. This follows the responsibility-based
Directory Rules adopted by ADR-0029. No parallel authority root is introduced.

## Verification

Both production builds and TypeScript checks pass. The current-source suite
passes all 1,336 tests; the local compatibility suite passes all 1,156 tests,
with the declared monorepo parity dependency supplied. Thirty-two focused
navigation, Underground, phone and focus checks pass. Tests retain the original
source-family expectations for each base; they do not assert newer data exists
in the older local copy. The browser-geometry entry point's selectors were
updated, but that CDP script was not executed in this session.

In the isolated local browser, Appearance has two tabs and four representation
choices; its Underground action opens and focuses the existing workspace.
High Plains still loads 50 records, plots 28 columns and completes the
2048 by 1718 surface with partial coverage and unbounded-class disclosure.
At 390 pixels, Measure hands drawing back to the map; a real two-point line
reports an approximate result, finishes and clears without document overflow.
The temporary viewport is restored after the check. These are bounded browser
observations, not broad physical-device, assistive-technology or performance
acceptance. Final installation readback is recorded separately.

Rollback restores the prior local alias/application build and restarts only the
existing Explorer service, keeping its original persisted-store path. The prior
installation and immutable client assets are retained for recovery/existing
tabs. Native publication and repository merge remain separate from local checks
and installation; neither data approval nor hosted equivalence is implied.
