# Aquifers and groundwater

Added to the existing official map context in the Aquifers & groundwater group.
All layers start off and have independent opacity. They do not enter KFM evidence,
review, or persisted datasets.

Seven live KGS WWC5 aquifer image layers: Alluvial (4), Dakota (5), Glacial Drift
(6), High Plains (7), Ozark (8), Osage (10), Flint Hills (11). Explicit layer IDs
exclude the WWC5 well-owner layers. Extent vintage is not supplied. Provider
polygons are drawn with distinct translucent colors and outlines. Bounds are
Kansas, display zoom 5+, and regional rasters retain the flat-map restriction.

Four pinned snapshots were retrieved from the official KGS High Plains Atlas's
linked ArcGIS map on 2026-10-04. Source URLs, counts, fields, retrieval timestamps,
provider class labels/colors, and generalization are in
`public/data/groundwater/manifest.json`. Source feature counts were checked
against complete query responses; no transfer-limit flag was accepted.

- Water-table elevation: 25 polygon records, 2022–2024.
- Saturated thickness: 8 polygon records, 2022–2024.
- Depth to water: 10 polygon records, 2022–2024.
- Monitoring locations: 1,384 points, 2026 network edition.

Class codes remain codes, never used as numeric measured elevations. Null or
unclassified records remain in downloads but are hidden on the map. Provider
ranges and colors are preserved. The three polygon snapshots use outSR=4326,
maxAllowableOffset=0.0005 degrees and five-decimal coordinate precision. Regional
estimates are not parcel measurements. Snapshot metadata is distinct from the
2026 operational-present carrier and does not auto-refresh.

KGS's source section-property description explains that water levels represent
winter conditions and average 2022–2024 values. Depth to water subtracts that
interpolated water table from a land DEM; saturated thickness subtracts estimated
bedrock elevation from the water table. These classified displays do not provide
a precise head grid, a resolved elevation datum for analysis, or hydraulic
properties for calculating groundwater direction/speed. Surface-water animation
and terrain profiles remain separate.

Monitoring point selection exposes its local well and USGS identifiers plus an
allowlisted HTTPS KGS WIZARD record link. No measured water level is attached to
the point snapshot. Opening the provider record is required for dated observations.

Validation: snapshot completeness/class matching/link safety; map harness for
lazy loading, opacity, visibility, and temporal holds; live nonempty KGS High
Plains export image. Browser/WebGL acceptance was not available in this session.
