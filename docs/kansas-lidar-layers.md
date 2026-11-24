# Kansas LiDAR layers in Terrain & elevation

From the welcome **Terrain & elevation** card, choose **Open Kansas terrain & layers**
(the card itself opens the map). The Terrain controls stay visible after entry.
Its primary controls are **Ground**, **Surface**, and **Canopy height**. Each draws
solid geographic cells with shaded sidewalls, height color, and linked numerical
readings. Ground requests a separate free USGS3DEP raster for the current Kansas
view. Surface and canopy request complete native survey analysis for a close-up
area; missing support remains a hole. Raw **LiDAR points** are secondary controls.
There is no paid API, subscription or visitor provider account, and no fixed
Konza location is selected.

**View map** closes the controls while retaining the enabled layers. **Tilt3D**
uses the current center, zoom and bearing. The source/readout badge appears when
controls close. **Zoom to detail here** is an explicit close-up action at the
current location, available when safe terrain camera context is ready. A close
view can still exceed source budgets or lack classification. These controls do
not change source heights or infer data.

Pan or zoom to another area to refresh an enabled native layer. The old result
is removed as the map moves. Each source can report processing, partial coverage,
no coverage, detail required or unavailable. For derived surface/canopy, zoom
into an extent small enough for complete native support. A processing response
is polled at two-second intervals for at most two minutes, then remains an
honest processing state with **Refresh this view**. Ground uses a distinct raster job, and does not request native points.

Surface and canopy are exclusive analysis layers; points can accompany either.
Opacity and point color/size change display only. Click an actually drawn point
or cell for its linked reading, or choose its source record/cell by keyboard.
Empty pixels and missing cell support have no height reading. Display scale is
shown separately from original numerical metres. Very close cameras may clip
heights outside their physical view; zoom out to see more of the cloud.

## Scientific meaning

- The continuous DEM is broad map context with varying native source resolution,
  acquisition and accuracy. It is not uniform statewide one-metre LiDAR.
- Display points are a bounded source-linked EPT hierarchy/LOD selection, not the
  complete survey density. Synthetic/withheld flags and noise classes7/18 are
  retained for inspection but omitted from default rendering and color domains.
- Every point keeps original EPSG:3857 XYZ, attributes and `(native asset, record)`
  identity. Each asset retains its acquisition, encoding, vertical reference and
  GPS time type. Raw GPS numbers are not converted to calendar dates. Encoding
  describes coordinate storage, not field accuracy.
- Analysis grids require complete bounded hierarchy support from one identified
  survey, separately from sparse display points. Cells retain counts and ground
  model residuals. Residuals describe model fit, not independent accuracy.
- Surface can include buildings and wires. Canopy requires real vegetation
  classes3/4/5 and supported same-survey ground. Its rendered top is ground plus
  canopy height; the numeric canopy reading remains height above that ground.
  Missing classifications/support stay null. No fixed NEON canopy substitution
  or sparse-LOD surface is used.
- Native point/cell colors and IDs share the same own-depth rasterization,
  composited above map context. Registration to the displayed DEM is unverified;
  this is not terrain occlusion or a point-minus-DEM accuracy measurement.

Review stays pending; these layers do not admit or release data as KFM evidence.
Source/method/hash/cache details remain inspectable. Artifact hashes refer to
source files checked upstream, not browser hashes of HTTP cache envelopes.

## Implementation and verification

`app/kansas-lidar-view.ts` exports validated view/grid models and cell readings;
`app/native-lidar.ts` supports fixed v1 examples and multi-survey viewport v2.
The reusable client binds the echoed query and native/grid identities to its
canonical SHA256 key, clips requests to the Kansas context window, bounds each
reply to one megabyte and total native transport to16MiB, and reads at most two
native chunks concurrently. New selection, movement, unmount or clear cancels
obsolete work. The GPU budget is at most100,000 display points,96² provider Ground cells or64² native analysis cells,300,000 packed grid vertices and4,194,304 offscreen pixels per layer frame (at most two frames). The point cap is unchanged.

The preserved NEON example at `/terrain` and Terrain Science at `/labs/terrain`
remain secondary examples in source details and the Science library; they are not
welcome-card actions and neither represents generic Kansas-wide coverage.
The generic models retain complete grid provenance for later science adapters;
a link alone does not claim that arbitrary tools ingest them automatically.

Focused schema, geometry, lifecycle and simulated GL tests do not establish
actual GPU appearance or native-provider delivery. The existing CI browser suite
contains explicitly synthetic desktop/mobile shader/pick/cleanup cases. Actual
Chrome/owner rendering and live source/transport qualification remain separate.

## Solid Ground geometry and scientific reuse

`GET /api/terrain/ground?bbox=west,south,east,north&size=96` returns a separate
`kfm-ground-view-v1` processing or complete receipt with a
`kfm-3dep-ground-grid-v1` grid. `app/kansas-ground.ts` and
`app/kansas-ground-client.ts` export validated geometry, cell inspection and
bounded loading for other KFM tools. This is a usable shared data contract;
individual science tools must still choose their own method and adapter.

The dev actor retains the original floating-point GeoTIFF and provider catalog
response with SHA256 and retrieval metadata on the14TB drive. All96² values are
exact decoded Float32 values, with provider masks and implausible/nonfinite
values left null. Explicit nearest-neighbor resampling preserves provider pixel
values; output spacing varies with the view and is not native source resolution.
A statewide view is coarse, and zooming requests a finer output grid. The
provider mosaic includes multiple DEM resolutions; it is not uniformly1m LiDAR.

Cell corners come from the verified GeoTIFF EPSG3857 affine, with rows north to
south and columns west to east. Inverse Mercator maps those corners onto the
map; projected cell distance must not be confused with ground distance.
Ground/surface cells retain absolute source top elevations. A shared closure
base below the supported minimum closes the visible block; it is display-only,
not a subsurface measurement. Canopy uses supported same-survey ground plus
classified vegetation height; negative heights remain source readings for
review rather than raised vegetation columns. Display scale affects geometry,
never the numeric reading. Sidewall shading describes shape, not another
measured variable. The color legend states unscaled source metres.

Catalog entries are intersecting candidates, not identified per-cell lineage.
A bounded catalog can be incomplete, and source date/resolution attributes have
heterogeneous encoding/units. Retrieval, processing, transport-cache time and
survey acquisition must remain separate. No ground-source minus native-source
height comparison is an accuracy claim without datum/registration verification.

Primary references: [USGS3DEP dynamic service](https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer),
[USGS3DEP products](https://www.usgs.gov/3d-elevation-program/about-3dep-products-services),
and [Esri exportImage parameters](https://developers.arcgis.com/rest/services-reference/enterprise/export-image/).

## Reveal landforms and reproducible study

The Ground grid supports **Height**, **Slope** and **Local relief** colors on the
same absolute-elevation cell geometry. Slope is a Horn3×3 derivative of unscaled
source elevations with separate local WGS84 east/north distance factors for
EPSG3857. Local relief is elevation minus the complete7×7 box-neighborhood mean,
in metres. The fixed output grid/window defines the analysis scale; neither
method reveals subpixel features or gains accuracy through visual exaggeration.
Edges and incomplete neighborhoods have no derived value and stay distinguishable
from real zero. The study JSON exports the validated public Ground receipt,
source digest and exact analytic recipe for reuse; it contains no private token.

These methods adapt terrain-inspection and reproducibility ideas from the
OpenAI to Z Challenge. Kansas use cases and source-backed future comparisons are
in [Terrain discovery concepts](terrain-discovery-concepts.md). Terrain shape
alone is not evidence of an archaeological date, cultural attribution or a
calibrated discovery probability.

## Solid Ground / Surface / Canopy height

The primary Terrain layer choices now draw solid stepped cells, rather than
requiring a dot cloud to explain a landscape. Opening the current Terrain map
requests Ground for that current view. Rendering a welcome card does not fetch
it. Ground uses the independent `/api/terrain/ground?bbox=...&size=96` provider
DEM path, with no EPT/point request. The96×96 output is a nearest-neighbor,
provider-resampled F32 DEM, not uniform native1m LiDAR. Footprints follow the
returned EPSG:3857 bounds, north-to-south rows; click coordinates refer to actual
pixel centers. Projected spacing is separate from approximate local physical
spacing. Catalog candidates retain raw heterogeneous date/resolution fields and
are not per-cell lineage or verified flight dates.

Surface and Canopy height retain the complete native same-survey analysis
contract and its close-view/budget/coverage limits. Missing support stays absent.
Canopy tops are that cell's ground plus vegetation height; a neutral same-cell
ground pedestal supports the colored canopy segment. Negative unsupported canopy
values remain inspectable but are omitted from solid rendering. Surface is not
labelled vegetation. Optional raw points are in a secondary disclosure.

Top elevations remain absolute source elevations under the existing display
scale. The shared closure base is below the supported same-grid minimum; closure
walls are a visual aid, not surveyed cliff faces, subsurface geometry or a height
rebase. Ground96² needs at most276,480 vertices; native64² canopy with separate
pedestal/vegetation walls needs at most221,184. Grid upload has a300,000-vertex
ceiling, independent of the100,000 point-row/vertex ceiling. The own-depth color/ID
render and registration limits remain. Reading and source values never scale.

View in3D explicitly tilts the current center/zoom/bearing to60degrees; View map
closes only controls. Zoom to detail here is an explicit conditional shortcut for
native detail-required views: current center/bearing, at least zoom17.5,pitch55,
only with actual terrain and a finite public center-elevation value. It never
sets/rebases elevation and does not guarantee coverage or analysis-budget success.
Reduced/disabled motion uses zero duration. Whole-state relief at true scale can
be subtle; no artificial terrain-height/density claim is made.

## Reveal landforms and reproducible studies

Ground color can show source Height, Horn3×3 Slope in degrees, or Local relief
(center elevation minus the full 7×7 unweighted mean) in metres. Geometry stays at
the original Ground elevation. Slope accounts for separate local WGS84 east/north
lengths per EPSG:3857 projected metre at the row latitude. All nine/49 samples
must exist; edges or missing neighborhoods remain NoData and use neutral color.
These are local derivatives of the resampled output grid; large output footprints
and row-local metric approximation limit interpretation. They are not native
survey detail, calibrated field accuracy, a classifier or archaeological evidence.

Download terrain study JSON includes the validated public Ground receipt, exact
source artifact SHA, original unscaled samples/mask, fixed analysis recipe and
derived arrays. Cache/retrieval timestamps remain distinct from acquisition.
No credentials or private source paths are exported. Regenerate the recipes from
those retained inputs; display exaggeration is never an analytical input.

Local-relief colors and the legend share a symmetric[-maxAbs,+maxAbs] domain.
Zero is the neutral center; below/above the local mean are blue/yellow. A flat
zero result uses neutral color with a[0,0] legend, without inventing a spread.
