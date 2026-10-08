# Cutaway surface detail — 2026-10-08

## Behavior

The 3D cutaway renders the selected basemap and copied display layers in a
separate MapLibre canvas. It requests detail for the visible portion of the
accepted geographic slice after camera movement settles (200 ms). The default
maximum dimension is 4096 pixels; the High option uses 2048. The renderer uses
one disposable context, a 96-tile cache, and actual provider tiles. During loading,
available detail appears at most once per second as an explicitly partial preview;
a slow optional overlay cannot hold back the basemap until global map load. Crisp image
sampling and full surface opacity are the defaults. The selector screenshot
is no longer the detail source as the user zooms in.

Surface map mode offers an independent interactive map within the same fixed
slice. Its camera remains separate from the left selector and 3D camera.
Changing source records, source frames or opacity requires Refresh surface
while the selector still represents that slice; moving the selector cannot
silently replace the accepted area. Unsupported custom/canvas display layers
remain explicitly omitted. Reports retain original recorded values.

## Basemap choice and source limits

The cutaway exposes vector streets/buildings, Esri imagery, USGS topographic
context, and **Kansas NG911 aerial imagery — 2024 — approximately 1 foot**.
Kansas imagery is an opt-in browser display carrier from DASC/KGS; it is not
an admitted KFM data source, a new backend API, or a downloadable evidence set.
The existing external carrier inventory discloses the endpoint and role.

- Provider account: [DASC FY2025 report](https://storymaps.arcgis.com/stories/426fc98cba994ff99d0c9f21c96eef08), documenting the February–April 2024 leaf-off acquisition and approximately 1-foot imagery.
- [Published image service](https://dascservices.kansasgis.org/arcgis/rest/services/IMAGERY_STATEWIDE/NG911_2024_1ft_Natural_Color/ImageServer).
- Service metadata checked 2026-10-08: Web Mercator grid spacing 0.3048006096 m; public Image capability; the service folder lists 2024 as its newest NG911 natural-color edition.

The exact local flight date is unresolved. This is a dated acquisition, not
live imagery. Esri dates and resolution vary geographically; current service
publication does not establish recent acquisition. Vector detail also depends
on provider coverage. Zooming beyond source resolution cannot reveal additional
measurements. No upscaling or generated detail is represented as source data.

Unavailable tiles remain coverage gaps; no older imagery is substituted.
Basemap tile errors leave navigation and records usable. Slow initial/detail
requests have explicit status and retry controls. NASA raster date uncertainty,
checked detection day/per-point times and independent Earth Engine years retain
their existing meanings. Earth Engine activation, source admission, report
records, DB/R2 bindings and owner-private audience are unchanged.

## Validation and mirror boundary

Implementation base: same-Site v180, `ec04779d27e0601b183d3709f71722134cc50c44`.
GitHub main pinned at `12c90d93afcd415ad298a9594e70746e6ea52818`; focused follow-up
on PR #4930 base head `4f03e82e410851355eb1a8e2a7f00081badbbe2e`.
Existing Site resource-panel/CSS differences and newer mirror runtime,
soil-moisture and radar changes are retained. Existing files were patched.
The error-handler test supplies both bases' dependency seams.

Standalone and mirror have separate production builds, TypeScript and focused
lint checks. Regression tests cover footprint clipping, increased detail on
zoom, 2048/4096 limits, source-time/value retention, debouncing, disposal,
pre-load tile failure, timeout, view switching, zoom reversal and controls.
The full suites contain 633 standalone tests and 637 mirror tests.

Bounded local browser checks confirmed the 4096-pixel Kansas aerial surface,
map detail zoom 13.0 to 14.9 while retaining the selected slice, basemap
switching, keyboard layer access, and 390-pixel responsive layout with no page
overflow. Mobile Surface map zoom advanced 9.4 to 10.4 with unchanged bounds.
Provider availability is independent of these checks. Full accessibility,
physical-device and long-session acceptance remain separate.

Inherited `MIRROR_REVIEW_REQUIRED` remains pending. Build/test success does not
approve historical receipts or merge the PR. Deployment source/version/access
readbacks belong in the PR delivery record.
