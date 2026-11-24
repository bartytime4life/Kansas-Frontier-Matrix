# Kansas LiDAR layers in Terrain & elevation

From the welcome **Terrain & elevation** card, choose **Open Kansas terrain & layers**
(the card itself opens the map). The Terrain controls stay visible after entry.
Its first controls are **Ground**, **Surface**,
**Canopy height** and an independent **LiDAR points** toggle. Ground keeps the
selected continuous elevation source. The other layers request the current map
view; choosing one does not jump to a fixed example or change source values.
There is no paid API, subscription or visitor provider account.

Pan or zoom to another area to refresh an enabled native layer. The old result
is removed as the map moves. Each source can report processing, partial coverage,
no coverage, detail required or unavailable. For derived surface/canopy, zoom
into an extent small enough for complete native support. A processing response
is polled at two-second intervals for at most two minutes, then remains an
honest processing state with **Refresh this view**. Ground does not require a
native-point processing request.

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
obsolete work. The GPU budget is at most100,000 display points,64² grid cells
and4,194,304 offscreen pixels per native-layer frame (at most two frames).

The preserved NEON example at `/terrain` and Terrain Science at `/labs/terrain`
remain secondary examples in source details and the Science library; they are not
welcome-card actions and neither represents generic Kansas-wide coverage.
The generic models retain complete grid provenance for later science adapters;
a link alone does not claim that arbitrary tools ingest them automatically.

Focused schema, geometry, lifecycle and simulated GL tests do not establish
actual GPU appearance or native-provider delivery. The existing CI browser suite
contains explicitly synthetic desktop/mobile shader/pick/cleanup cases. Actual
Chrome/owner rendering and live source/transport qualification remain separate.
