# Underground Explorer

This addition starts from owner-private Site v155, source `d8f2db1ee6e0fedd495ed538a85ad23b3302e2ae`. It preserves the existing Map Library, place dossiers, Evidence Drawer, reports, Earth Engine controls, DB/R2 bindings, and Site audience. GitHub PR #4899 merged during implementation; the feature review starts from `8c955317117e53fa93ece5d0af4455d86fad17b3`, retaining its separate CodeQL test correction. The dirty owner maintenance checkout is not used as an import source.

## Behavior

Open **Underground** in the map representation strip. The surface map remains above a resizable panel. Hover for nearby recorded columns; click to pin. The fixed surface crosshair, directional buttons, and **Inspect here · map center** provide keyboard/touch navigation. A pin survives map movement. The probe is a search location, not a claim that the nearest borehole describes that precise location.

County navigation and an on-demand statewide ID/county locator cover 314,844 mapped WWC5 records and 6,598 core locations. Well/core chips change the underground query only. Results cover up to eight spatial tiles around a 25 km probe/section corridor, return up to 50 records, and show up to 20 columns. Long sections, missing tiles, invalid records, and truncation are explicitly reported. Empty results mean none in the available data. Provider point markers and the selected interval remain linked without replacing existing map sources.

**Draw a section** uses the existing distance drawing interaction. Finish that line, then choose **Use drawn section**. Distances along the route and offsets use spherical segment projection with endpoint clamping. The chart shows each record's own reference depth, not a common elevation section. Enable the existing surface DEM and sample it separately to see a surface profile; missing DEM samples remain gaps. The DEM is not used to invent sea-level alignment for boreholes.

Original log descriptions remain separate from KGS standardized interpretation codes. Invalid depths are excluded and accounted for by the preparer; valid gaps and overlaps remain. Core start/end values describe inventory envelopes, not recovered material throughout the range. Available photographs open the original KGS per-well pages; the display does not invent photographic coverage. Selecting a source interval opens its original description, unit, depth reference, source time, location method, limitations, source link, and photo link in the existing Evidence Drawer.

**3D log** is an optional dynamically loaded Three.js recorded-depth diagram. It supports orbit/zoom, depth clipping, description isolation, visible exaggeration, and True scale. The nominal 5 m column width is explicitly illustrative. It is not a georeferenced well trajectory or continuous geological cutaway. No imported record supplies the required surveyed trajectory and shared elevation reference. Clipping animates over 180 ms, stops between interactions, and respects reduced motion. WebGL failure offers retry and the 2D view remains available. Pixel ratio is bounded and the 3D diagram draws at most 500 intervals.

**Geophysical surveys** distinguishes electrical, electromagnetic, GPR, and seismic methods. Four qualified KGS electrical collections provide 21 measured conductivity profiles and 25,479 original samples, shown in mS/m against depth below local land surface. The trace is decimated to at most approximately 600 display points without changing the retained source values. Approximate Google Earth positions do not establish a surveyed horizontal or elevation datum. Duplicate-series and invalid-location profiles remain held. GPR/tTEM entries remain reference links; no radar time is converted to depth without a qualified velocity model, and conductivity is never relabeled as lithology.

**Soil horizons** queries the existing public USDA Soil Data Access service through a bounded, read-only Site route. It retains separate soil-map components, proportions, centimetre depth units, retrieval time, and the 100-horizon response limit. These alternatives do not establish the exact soil beneath the pointer. Browser-location privacy suppresses this external coordinate lookup.

## Persistence and exports

The optional validated `SubsurfaceContext` extends existing workspaces/reports without changing storage keys or the database. Workspaces retain settings, source hashes/editions, and record IDs, then reload eligible current assets. Missing records and changed source versions are labelled; captured rows never masquerade as a fresh response. Old workspaces/reports remain readable and quota/storage errors follow existing handling.

Reports capture bounded KGS source rows and source editions with a capture timestamp. Provider context remains separate from included evidence and does not create EvidenceRefs or an EvidenceBundle. Reports provide a source-labelled interval CSV and a self-contained SVG column diagram with explicit depth/reference/spacing limits. CSV formula prefixes and SVG metacharacters are escaped. The image is a recorded-column diagram, not a geological reconstruction. Current geophysical, live soil, and display-DEM views are separately labelled and are not included in this first KGS column snapshot.

Browser-location redaction removes the entire underground context from saved/exported state, including coordinates, transects, record IDs, and section images. It also suppresses direct interval/image downloads. The underground privacy flag remains sticky during an investigation. No screenshot of the unrestricted canvas is used as a redaction shortcut.

Source archive editions, observation/record dates, interpretation editions, and retrieval times remain distinct. In historical map frames, WWC5/core records with later or unknown record dates are held; the archive is still a current source edition, not a reconstructed historical inventory. Soil and geophysical views explicitly retain their own source editions.

## Data and path ownership

See [subsurface-data.md](subsurface-data.md) and [subsurface-geophysics.md](subsurface-geophysics.md) for receipts, rights, transformations, exclusions, and reproducibility. Compressed KGS assets total 22.9 MB and are spatially partitioned, hashed, and fetched in a worker with request cancellation and a bounded tile cache. The statewide locator is loaded only for a search. Asset hashes provide immutable edition identity even though the display URLs remain stable across Site deployments.

Placement follows the adopted Directory Rules and accepted ADR-0029: application behavior, display assets, source preparation, regression tests, and behavior documentation remain in this standalone application's existing `app/`, `public/`, `scripts/`, `tests/`, and `docs/` responsibilities. The GitHub mirror remains under `apps/site/source`. These are provider display derivatives, not a new registry, evidence store, governed processed-data root, or database migration. No source admission, promotion, or independent evidence acceptance is implied.

## Delivery and remaining qualification

Review is separated into source assets/contracts, linked sections/persistence, and qualified pilot field profiles/optional 3D presentation. The full Kansas River sediment-model cutaway is **blocked**: native numerical model geometry and redistribution qualification remain unavailable. Published pictures are not numeric depth surfaces. GPR/tTEM raw numerical assets remain unverified. These holds do not prevent the statewide recorded-column viewer from working.

Validation covers full asset integrity and field exclusions, original workbook sample bounds, coordinate/depth/radar handling, gaps/overlaps, duplicate identity, section offsets, historical holds, canceled responses, unavailable/corrupt sources, legacy storage, quota failure, source-labelled exports, redaction, and bounded soil requests. Type check, production build, and full Site regressions run before packaging. Browser access still fails the admin policy security check; visual, keyboard-flow, mobile, and WebGL acceptance are pending and must not be inferred from unit/build success. Runtime UI controls and CSS have been implemented, but no browser performance or smoothness acceptance is claimed.

Rollback retains saved v155 (`appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_769352625ae8819192b37861a2d0bc12`) and its source. No DB migration or binding change is required. The inherited repository `MIRROR_REVIEW_REQUIRED` receipt gate remains separate; feature checks cannot waive it.
