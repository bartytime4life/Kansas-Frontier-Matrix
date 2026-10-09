# Terrain drawing and Kansas viewpoints

The Scene Studio now draws local contours and a surface grid from elevations the current MapLibre map has already loaded. It also offers six direct landscape viewpoints and an interruptible 90° orbit. This extends [Scene Studio](scene-studio.md) without changing the toolbar, basemap, provider records or persisted data.

Independent [Surface color lenses](terrain-surface.md) add slope, downhill facing direction and a dedicated cell sample to the same loaded grid. Surface colors have fixed legends; line colors continue to follow scene light.

## Use

1. Open **Scene**, choose **Terrain 3D**, and zoom to at least **8.5** over Kansas. The **Kansas landscapes** disclosure offers five close landscape views plus a statewide overview. The overview deliberately remains below drawing zoom and gives a zoom-in message.
2. Under **Terrain drawing**, choose **Contours**, **Surface grid**, or **Both**. The default is **Off**. Choosing a drawing mode alone never enables terrain or requests a DEM.
3. Read the actual contour interval, sample spacing and valid-sample percentage below the controls. Grid-only mode omits the unused contour interval while retaining spacing and valid-sample coverage. Missing elevations remain gaps. Drawing covers a centered local patch at most approximately 24 km across, rather than claiming statewide coverage.
4. **Sampling & source limits** contains the finer-sampling option and metadata for the selected provider. Battery saver selects fewer samples. Spacing describes sampling density, not source accuracy.
5. **Orbit this view** makes one 90° turn over 12 seconds. Stop it with the button, map pointer/touch/wheel/key input, a direct camera or landscape action, or a representation change. It also stops when the tab is hidden or reduced motion becomes active.

The drawing uses normal terrain-draped GeoJSON lines. Stronger index contours occur every fifth interval. The grid joins only adjacent loaded samples. Colors follow the effective presentation light, including the existing real-sun option. No contour elevation, source observation date, terrain height or provider-value color is invented or changed.

## Viewpoint behavior

The six shortcuts reuse the existing `KANSAS_FLYOVER` targets, excluding its return leg: Kansas overview, Arikaree Breaks, Smoky Hill chalk country, Red Hills, Flint Hills, and Kansas River valley. They switch to regional Terrain 3D and change the camera center, zoom, pitch and bearing. They preserve the chosen basemap, DEM provider, exaggeration, light, lens, selected feature, source dates, active layers and topographic-height preference. Entering Terrain 3D uses its normal existing tile loader; the terrain drawing itself introduces no request path or additional DEM source.

Shortcuts use a 900 ms camera transition, or an immediate transition under reduced motion. Orbit and the existing flyover are mutually exclusive; direct composition and shortcuts stop either first. Orbit uses MapLibre's existing camera ease and a bounded completion timer, with no second animation loop. The full flyover retains its previous tour behavior.

## Data and resource boundaries

Sampling is limited to the Kansas focus box where the existing elevation helper treats unavailable zero readings as missing. It reads the active terrain through `unexaggeratedTerrainElevation`; changing display exaggeration does not change contour elevations. The bounded sampling grids are 33×33 in Battery saver, 49×49 normally and at most 65×65 for finer drawing. Sampling yields between batches of 128 points; geometry work yields between groups of four rows. Levels and segments are capped.

Mapzen's display DEM is capped at zoom 11 to avoid known high-zoom discontinuities; closer camera views overzoom that DEM. USGS 3DEP is a mixed-resolution/date mosaic. A displayed tile does not establish a particular work unit, acquisition date, vertical datum or certified accuracy. These limits and the existing provider source link remain available directly in the panel.

The page creates one drawing controller for the current map and updates its configuration across all three Scene Studio instances. The controller owns source/camera listeners and scheduled work. It cancels incomplete sampling during motion and clears old geography after pan/zoom, source/provider/style changes, Off, or leaving regional terrain. Finished lines may remain during a pure bearing/pitch orbit because the sampled geographic patch is unchanged. Map teardown destroys the controller before removing the map. Palette-only updates do not resample.

## Validation

`tests/scene-landscape-integration.test.mjs` executes the actual page/component callbacks and covers:

- All six shortcuts preserving existing presentation/data choices, with normal and reduced-motion transitions.
- Orbit mutual exclusion, every direct-input interruption, hidden-tab cancellation, natural completion and listener/timer cleanup.
- Reduced-motion/globe guards and representation-change cancellation.
- Configuration reaching one existing controller, enabled only for style-ready regional terrain, with synchronous Off updates.
- All four drawing mode buttons, six viewpoint buttons, real readings, provider limits and Battery saver/reduced-motion controls.

These five tests pass. The prior Scene Studio/cinematic behavior tests pass, and TypeScript passes. The renderer has separate pure geometry and lifecycle tests in `tests/terrain-drawing*.test.mjs`. Production build, full-suite results and desktop/phone browser evaluation are recorded by the integration agent after the final combined source is stable. This document does not claim survey accuracy, publication or extended GPU endurance.

## Rollback

Choose **Terrain drawing → Off** to hide the generated lines. If a Surface color lens is active, turn it Off as well to remove the shared geometry and stop its work; stop an active orbit or flyover before another camera action. To remove this addition from source, restore only its UI integration changes in `app/page.tsx`, `app/scene-effects-controls.tsx` and `app/scene-effects.css` from saved Site v200, then remove `app/terrain-drawing.ts`, `app/terrain-drawing-runtime.ts`, the terrain-drawing tests, `tests/scene-landscape-integration.test.mjs` and this document. Preserve unrelated newer edits and account for the surface lens's shared-controller dependency. No stored-data or preference-schema migration is involved.
