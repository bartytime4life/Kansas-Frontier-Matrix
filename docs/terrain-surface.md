# Surface color and cell samples

Scene Studio adds two independent surface lenses to [Terrain drawing](terrain-drawing.md): **Slope** and **Facing direction**. Both start **Off**. They color a local patch of the already-loaded display DEM; selecting a lens does not enable Terrain 3D, acquire a DEM, or admit a new data source.

## Use

1. Open **Scene**, choose **Terrain 3D**, then zoom to at least **8.5** over Kansas or choose a close **Kansas landscapes** viewpoint.
2. Under **Surface color**, select **Slope** or **Facing direction**. Contours and the surface grid remain independent choices; either lens works with line drawing **Off**.
3. Read the fixed legend. **Color strength** adjusts opacity from 20–75% (default 55%) so map labels and imagery remain visible. Scene light does not change a surface color's meaning.
4. Point at or tap a colored cell, or activate **Sample view center** by keyboard or touch. The same cached cell supplies approximate slope to one decimal degree, downhill compass direction, and the rounded unexaggerated center elevation in meters. A pale outline marks the sampled cell.

The floating Scene panel stays open for map taps while surface sampling is active. It shares the Explorer shell's stacking context with the Evidence Drawer and paints above it while open, so tapping a valid provider polygon can select its record without covering the surface sample. Compact evidence autofocus waits while surface inspection is active; dismissing Scene preserves Escape focus return and restores the drawer's keyboard behavior. Other outside clicks and Escape still close Scene. This exception consumes no map input: existing evidence selection and gestures continue normally. Measurement tools pause the surface probe; completing a measurement does not promote a cell to evidence. Hover/click fallback selection explicitly excludes `scene-*` display sources while retaining provider and basemap feature handling.

## Meaning and limits

Slope uses fixed degree bands: **<2°**, **2–5°**, **5–10°**, **10–20°**, **≥20°**. These are degrees, not percent grade. Facing direction is downhill azimuth clockwise from north, grouped as N, NE, E, SE, S, SW, W and NW. **Flat** includes slopes below **0.5°**, where direction is treated as unstable. It does not describe sunlight, exposure duration, drainage routing or site suitability.

The implementation in `app/terrain-surface.ts` uses Horn 3×3 neighborhood derivatives, requiring all nine finite samples. It uses separate latitude-adjusted east-west and north-south ground distances, then computes slope as `atan(hypot(gEast, gNorth))` and downhill aspect as `atan2(-gEast, -gNorth)`. This is a browser implementation over a sampled display grid, not a GDAL invocation; the [GDAL slope/aspect documentation](https://gdal.org/en/stable/programs/gdaldem.html) describes the reference algorithm and angle conventions.

Each valid cell is centered on its actual elevation sample and extends half a grid interval in each direction. Missing neighborhoods remain uncolored, and the outer unsampled rim is not extrapolated. **Valid surface cells** reports valid neighborhoods divided by possible interior cells; **Valid samples** reports the separate fraction of usable DEM readings. The percentages can differ substantially near gaps. Grid spacing is sampling density, not provider resolution or accuracy. Changing display exaggeration does not change these readings.

Existing provider limitations remain visible in **Sampling & source limits**: Mapzen is a display DEM with the existing zoom-11 source cap; USGS 3DEP is a mosaic with varying dates and resolutions. A visible tile does not establish a work-unit date, vertical datum or certified accuracy. These cell estimates are not survey measurements or report evidence.

## Rendering and lifecycle

The existing controller samples once for lines and cells, bounded to the Kansas focus box and a centered patch at most approximately 24 km across. Grids remain 33×33 in Battery saver, 49×49 normally, and at most 65×65 with Finer drawing. The maximum is 3,969 interior cells. Sampling yields every 128 points and geometry yields every four rows. No added DEM source, request path, worker, shader, persistent storage or continuous render loop is involved.

Cells use a native [MapLibre fill layer](https://maplibre.org/maplibre-style-spec/layers/#fill), sharing `scene-terrain-drawing` GeoJSON with the existing line features. Explicit roles separate polygons, grid and contours. Fill stays below line casings, provider evidence, selections and labels. Opacity, surface mode, line mode and lighting changes reuse the cache and update paint. Fixed surface palette values are exported from the same model used by the legend.

Completed geometry remains through a pure bearing/pitch orbit. Sampling cancels during motion; pan/zoom, changed terrain identity, style replacement, leaving regional Terrain 3D, or both channels Off clear obsolete geometry. The probe clears on motion, leaving the map/cell, lens changes, measurement activation, replacement of the sampled cache, source/style changes, Off and teardown. It reads cached cell data rather than arbitrary rendered features. A same-lens button press preserves the current reading; switching lenses allows a fresh center sample immediately.

Opening or closing an overlaid drawer schedules two layout checks. While a surface lens is enabled, those checks skip `map.resize()` only when the public canvas CSS width/height exactly match the container dimensions. This avoids MapLibre's synthetic movement events for an unchanged layout clearing the first tapped sample. A real dimension change still resizes and invalidates the reading; runtime motion/source/style/lens clearing remains intact. Existing cutaway resize protection and ordinary map behavior are retained.

## Validation and rollback

`tests/scene-surface-integration.test.mjs` executes actual page/component callbacks for channel independence, same-lens reselect and center sampling, opacity bounds, regional-terrain guards, disposed-map callbacks, measurement priority, both generic feature fallbacks, fixed model legends, distinct coverage readings, disabled/flat states, tap/outside/Escape behavior, shared panel stacking, compact evidence focus and both deferred drawer resize callbacks. Its eleven checks pass together with the ten existing Scene Studio and landscape integration checks. The resize regression exercises unchanged dimensions, actual dimensions changing before either callback, active/Off lens scope, fresh deferred configuration, and the renderer's actual movement callback. Pure math and renderer lifecycle coverage is separate in `tests/terrain-surface.test.mjs` and the terrain-drawing tests. Full build, combined-suite and independent desktop/phone review are recorded by the integration agent after source freeze; this document does not assert those outcomes or extended GPU endurance.

Choose **Surface color → Off** to hide the lens and clear its reading. Set line drawing Off as well to remove generated geometry and stop its controller work. To remove the addition from source, restore only the surface-related changes from saved Site v201 and remove the new surface model, integration tests and this document, preserving unrelated newer edits. No stored-data or preference-schema migration is required.
