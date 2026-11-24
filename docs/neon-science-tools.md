# NEON samples across KFM

The Terrain & vegetation lab at `/labs/terrain` is a descriptive science view of
the same validated historical Konza pilot used by the main map and acquisition
workspace. It uses the existing `/api/neon/preview` route and the existing signed
relay to dev’s 14 TB drive. It adds no provider credential, subscription, paid
API, external tile service or new dev worker route.

## Direct landscape view

Open `/terrain` (or **Konza 3D** in the welcome Terrain & elevation card,
Research Atlas navigation or Terrain Science navigation). The welcome toolbar
keeps its primary map action and Options without a duplicate sample link. The explicit legacy
review URL `/?neon-review=3` temporarily redirects to `/terrain`; ordinary root
visits remain unchanged. The focused route automatically requests the same
bounded, validated pilot once per live attempt. It starts on Ground at a
clearly labelled 3× relative-height scale, fits the actual tile and pitches the
camera to 60 degrees. Surface and independent Canopy, 1×–5× scale, fit/tilt,
overhead samples, rotation, deterministic actual-sample story stops and original
cell readings are visible on the page. No drawer or second loading action is
required.

The route uses the existing renderer acquisition seam and a local explicitly
Mercator style with no external basemap, DEM, sprite or font dependency. A
completed source request is not a rendering-success signal: ready requires an
owned rendered sample feature in the framed viewport. Style/import and overlay
startup have bounded deadlines. Errors or lost WebGL contexts remove the failed
map; Retry recreates both the renderer and receipt attempt. Disposed attempts
abort their request and ignore late callbacks. Reduced motion suppresses camera
transitions. WebGL2-unavailable browsers receive a plain explanation and a link
to the existing 2D Science inspector, not a fabricated 3D fallback.

The neutral background and column illumination are display settings, not new
observations. The native 83.41 m canopy outlier is retained as a review warning,
not assigned to a preview location. Full source identity, all three hashes and
source-linked JSON remain available under source details. The direct route adds
no provider credential, cost, service or source-admission change. HTTP and
controller tests do not establish actual GPU or visual acceptance; Chrome must
render the deployed route for that separate evidence lane.

## Terrain card entry

The existing welcome **Terrain & elevation / Relief model** card is also the
home for the historical **NEON · Konza pilot** source row. **Konza 3D** opens
`/terrain` directly; **Terrain Science** opens `/labs/terrain`. The same small
navigation entry is visible in the terrain Chosen map and full-screen preview
panels, outside source-note disclosures. These are ordinary links: showing the
card or a terrain preview starts no NEON request and creates no duplicate
viewer/controller.

The card body still opens the existing relief map; its arrow still opens that
relief preview, and its plus still adds/removes Terrain in a combined map. The
sample entry preserves the continuous category and the separate aerial context.
The Terrain category explicitly uses the continuous USGS 3DEP mixed-date
ground mosaic for mesh, color relief and hillshade. Other category provider
defaults remain unchanged. Photo-real context can add the separately dated
2024 aerial imagery to the selected ground model.
Neither is the historical NEON ground/surface/independent-canopy sample tile.
The Konza row labels September 2024 as a catalog month and retains sampled
preview/review-pending scope. The accepted direct viewer, source mathematics,
startup scheduler, cache/relay and Science/export contracts are unchanged.

## Continuous Kansas ground and provider discovery

Terrain & elevation is the continuous Kansas experience. Its card body opens
USGS 3DEP ground, its arrow previews that same provider, and its plus keeps the
existing combined-topic behavior. Ground color, hillshade and mesh share the
selected DEM provider. Separate tile managers preserve renderer isolation;
provider changes retain original layer paint and ordering. Other category
presets keep their existing provider defaults. Returning from aerial imagery
restores Terrain's USGS selection instead of silently replacing it with Mapzen.

Terrain starts at the existing close Konza / Flint Hills camera so local relief
is visible without changing source heights or display exaggeration. It is a
window into a continuous Kansas ground model, not the NEON sample tile. The
terrain dock exposes source/readiness, 1× true vertical scale and Whole Kansas,
with Konza and Red Hills shortcuts visible and remaining landscapes under More. The
existing 0.5×–3× slider remains presentation-only; readings and source units are
unchanged. The explicit Mapzen choice remains available as coarse display
context. An unavailable selected DEM stays labelled unavailable and can be
retried; an explicit category selection is not silently described as USGS while
showing another source.

USGS 3DEP is a mixed-resolution, mixed-date bare-earth mosaic. Deeper renderer
tiles improve display sampling where the provider supports them; they do not
prove statewide native 1 m LiDAR, a common acquisition date, datum or field
accuracy. This is a continuous ground model, not a vegetation surface or raw
point cloud. The accepted historical Konza viewer and its independent CHM remain
separate sample tools; neither is fabricated from the statewide DTM.

A compact shared LiDAR source catalog is available in the terrain instrument,
Terrain Science and acquisition workspace (`/acquisition#lidar-sources`). It
separates connected continuous terrain and prepared sample science from provider
discovery and unqualified access. Native DASC/USGS assets, survey indexes, orbital
profiles and KDOT derived assets keep their distinct readiness and geometry.
Showing the catalog starts no download or acquisition. Mirrors of the same
survey are not independent measurements; quantitative comparison requires
product, reference/epoch/datum, date, support, quality and co-registration checks.
No service, account payment or subscription is added by these controls.

## Shared data contract

`app/neon-lidar-science.ts` exports `createNeonScienceDataset(input)` and
`neonScienceDatasetJSON(dataset)`. The adapter accepts only a complete validated
`kfm-neon-relay-pilot-v1` receipt with the expected site, month, run, release and
tile. A raw local or synthetic grid cannot be promoted into this provider
science view. Existing local imports remain available for explicitly labelled
raster inspection.

The adapter returns `kfm-neon-science-v1`, containing the parsed receipt and a
record bundle that the existing RecordLab/science models can use. Every preview
cell has a stable identity, one-based row/column, native sample-center easting
and northing, DTM, DSM, independent provider CHM, DSM minus DTM, and difference
QA. It retains original numeric values, nulls, valid zero and negative source
differences. An overflowing source difference is null with nonfinite QA rather
than an invented number. Coordinates and indices are inspection fields, not
default scientific measures.

There is no invented longitude/latitude, per-sample observation date, annual
series or county assignment. The catalog month is not an exact acquisition
date. Original file retrieval timestamps are unknown in this receipt; preview
preparation and relay-cache times remain separately named. The three original
filenames, products, byte lengths and SHA-256 values accompany the bundle.

Other KFM components can use the same adapter after the shared bounded client
loader returns a receipt. They must preserve its review/cache labels and use the
same receipt revision for all linked views. This is a reusable data contract,
not automatic compatibility with every notebook/import format. No static Labs
snapshot manifest, SQL dataset allowlist or governed admission gate is widened.

## Descriptive tools and exports

RecordLab’s distribution, filtering, source inspection, quartiles, sample
standard deviation, complete-pair Pearson/Spearman association, ranking and CSV
operate on these exact sample rows. Quartiles use type-7 interpolation at
`(n - 1)p`; sample standard deviation uses `n - 1`. Missing values do not become
zero and incomplete pairs do not enter a relationship calculation. These
existing mathematics are unchanged by the adapter.

The record and group-summary CSVs retain all three raw-file hashes. Their
optional `analysis_context` JSON column carries compact source identity,
sampling, reference/time distinctions, pending-review flags and native-outlier
statistics. It avoids repeating verbose CRS and review prose in every row.
The source-linked dataset JSON retains the full receipt, recorded CRS, review
notes and regenerated derived rows. Presentation precision never rounds the
stored source values. Existing CSV shapes are unchanged for datasets without
analysis context.

The preview contains regularly spaced nearest native samples; it is not a
random sample or a complete native raster population. Summary statistics and
relationships describe this selected preview only. Adjacent samples are
spatially dependent, and DSM minus DTM is arithmetically coupled to both inputs.
No correlation, fitted line or count establishes causation, independent sample
size, vegetation area, species, biomass, carbon, growth, change or field accuracy.

## Relative 3D display

In Appearance, **Explore in 3D** loads the Konza pilot if needed, enables the
column representation, fits its tile and tilts the camera in one action. It uses
the currently loaded preview when one is already present. The first 3D entry
uses a labelled 3× scale; the control remains adjustable from 1× to 5×. Return to
Flat samples for an overhead view. The separate statewide Terrain 3D preset uses
an external elevation source and does not display these local NEON samples.

The map displays a bounded column representation of the sample grid. Its shared
local height baseline and any vertical exaggeration are visualization settings. Source readings and science exports remain unscaled.
Ground/surface columns represent sampled elevations relative to that baseline;
canopy columns use valid DTM as their base and the independent provider CHM as
their height. Missing ground cannot support a placed canopy column. The
rectangular display footprints are not measured vegetation volumes or surveyed
terrain meshes. The flat overlay remains available.

Actual sampled low/high ground, highest canopy and largest DSM minus DTM can
provide deterministic story stops. A preview maximum is labelled as sampled;
it cannot stand in for the retained native canopy maximum of 83.41 m. These
outliers still need review. Globe/active external-terrain alignment is not
invented, and invalid/extreme rendered geometry is omitted rather than changing
source measurements.

## Verification and release boundary

The earlier live release’s dev-backed API, grid and map-cell reads were verified
before this usability/science/3D follow-up. That acceptance does not establish
this new interface or the new GPU rendering. The follow-up needs its own adapter,
science, component, rendering-math, type/build/CI and live/browser verification.
No dev service, data migration, credential rotation or subscription is required.
Revert the follow-up application source and redeploy to return to the previously
verified flat pilot; keep the current dev relay and original data intact.
