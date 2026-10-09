# Cinematic MapLibre scene effects — 2026-10-09

This repository change gives the Explorer's 3D views a finished, cinematic look using MapLibre GL JS 6.9 features the Site already ships: tuned relief shading, sky and distance haze, a custom WebGL layer, globe atmosphere and camera animation. Every effect is **presentation only** — no source, layer, evidence state, reported elevation, time, report or API changes — and each can be switched off. It is **repository source only**: it has not been saved or deployed as a Site version, and the existing `MIRROR_REVIEW_REQUIRED` hold is unchanged.

<p align="center">
  <img src="images/cinematic-terrain-before-after-2026-10-09.jpg" alt="Terrain 3D over the Red Hills before and after. Before: dark, low-contrast relief and no visible sky. After: crisp warm-lit relief, an indigo-to-amber dusk sky with horizon haze, and a glowing gold-to-teal light curtain standing on the Kansas–Oklahoma line." width="100%" />
</p>

<sub>Same Red Hills area in Terrain 3D (Midnight basemap, dusk). The before view is limited to the old 60° tilt; Terrain 3D now allows 72°, which brings the sky into view.</sub>

## What changed

| Effect | What you see | How it works | Files |
|---|---|---|---|
| Relief lighting | Slopes and drainage networks read clearly from statewide to local zoom, with a warm key highlight and deep indigo shadow | Retuned the existing DEM hillshade (standard method, full exaggeration, per-light-preset palettes). The palette was picked by rendering the same DEM side by side: MapLibre's `multidirectional` method averages its lights and washed Kansas relief out, so it is not used. | `app/scene-effects.ts`, `app/terrain-relief-style.ts` |
| Sky and haze | Indigo→amber dusk, teal night horizon, blue day sky, and ground fog that adds depth | Richer `sky` presets (zenith, horizon, fog and blend values); the clear-day fog is softened so it does not grey dark basemaps | `app/scene-effects.ts`, `app/map-runtime.ts` |
| Wider tilt in Terrain 3D | Horizon and sky come into view | `maxPitch` is 72° in Terrain 3D (60° elsewhere, unchanged) | `app/page.tsx` |
| Kansas light curtain | A glowing wall of light along the state border in tilted views: bright gold foot, rays, fading to teal | A MapLibre **custom WebGL2 layer** with additive blending. The bundled outline is densified to ~2.5 km steps; wall feet follow the rendered terrain, and hills in front of the wall hide it through the depth test. Hidden in globe view, below 12° tilt, and in Battery saver. A slow shimmer repaints at ~15 fps only while the curtain is on screen, ambient motion is on, reduced motion is off and the tab is visible. | `app/aurora-curtain-layer.ts`, `app/scene-effects.ts` |
| Follow the real sun | Light direction and sky follow the sun over the map center; after sunset a cool fill light lights the scene from the opposite side, labelled as night fill | Uses the Site's existing NREL SPA solar position (`solarPositionAt`), refreshed each minute | `app/scene-effects.ts` |
| Fly over Kansas | A tour of six landscapes (Arikaree Breaks, Smoky Hill chalk country, Red Hills, Flint Hills, Kansas River valley) in Terrain 3D with a caption | `flyTo` then a slow bearing drift per stop. Dragging, scrolling, pressing a key, choosing another map mode or **Stop** hands the camera back at once. Not offered with reduced motion. Camera moves are not added to camera history. Stop centers are approximate viewpoints, not surveyed locations. | `app/scene-effects.ts`, `app/page.tsx` |
| Globe in space | A starfield and blue glow behind the globe instead of a flat olive fill; a faint 15° world graticule so the offline globe reads as a sphere | CSS backdrop behind the transparent globe canvas; globe `atmosphere-blend` eases out as the camera nears Kansas | `app/scene-effects.css`, `app/kansas-orientation.ts` |
| Selection emphasis | A soft glow under a selected line or area, a halo under a selected point, and a short two-ring ping | Three system layers on the existing selection source; the ping stops by itself so the map returns to idle, and is skipped with reduced motion or ambient motion off | `app/map-runtime.ts`, `app/map-layer-composition.ts` |
| Offline basemap glow | Soft glow under the Kansas outline and rivers in the Midnight/Prairie styles | Blurred under-strokes on the bundled orientation geometry | `app/kansas-orientation.ts` |
| Lens vignette | Gentle edge darkening in Terrain 3D only | CSS overlay, no pointer events; 2D evidence views are untouched | `app/scene-effects.css` |

<p align="center">
  <img src="images/cinematic-statewide-curtain-2026-10-09.jpg" alt="Statewide Terrain 3D view: Kansas as a lit relief diorama ringed by a glowing light curtain, with a Fly over Kansas button at the top right." width="78%" />
  <img src="images/cinematic-phone-flyover-2026-10-09.jpg" alt="Flyover on a 390 px phone: caption reading Flyover 2 of 7, Arikaree Breaks, Cheyenne County, north-west Kansas, with a Stop button." width="20%" />
</p>

<p align="center">
  <img src="images/cinematic-globe-before-after-2026-10-09.jpg" alt="Globe before and after: before, a blank sphere on an olive background; after, a sphere with a faint graticule in a starfield." width="64%" />
  <img src="images/cinematic-pitched-2d-2026-10-09.jpg" alt="A tilted 2D view of the offline Kansas outline with the light curtain around it." width="34%" />
</p>

## Controls

<img src="images/cinematic-controls-2026-10-09.jpg" alt="Layers panel, Terrain and 3D appearance section, showing the Cinematic 3D switches: Kansas light curtain, Follow the real sun (reading: sun below the horizon, cool night fill), and a gold Fly over Kansas button." width="60%" align="right" />

- **Layers → Tune this view → Terrain & 3D appearance → Scene effects**, and the Scene Lab: *Cinematic relief & sky*, *Kansas light curtain*, *Follow the real sun*, *Fly over Kansas*.
- A **Fly over Kansas** button appears on the map whenever Terrain 3D is on (top-centre on phones).
- Defaults: cinematic relief and curtain on, sun-following off. Choices are a device-local preference (`kfm-scene-effects-v1`); blocked storage just keeps the defaults. Shared URLs and saved workspaces are unchanged.
- Battery saver pauses the curtain; reduced motion holds the shimmer still, skips the ping and disables the flyover.

<br clear="right" />

## Boundaries

- The curtain stands on the bundled simplified outline. It is not a legal boundary, is not queryable, and does not appear in reports or exports.
- Lighting and haze change colour only. Hover elevations, profiles and locked report readings still divide out the display exaggeration and read the DEM unchanged.
- Following the sun changes the scene light only. It does not change the atlas time, the daylight layer or any provider's observation time.

## Validation

| Check | Result |
|---|---|
| Production build | PASS |
| TypeScript (`tsc --noEmit`) | PASS |
| Node test suite (`npm test`) | 737 tests: 735 pass, 0 fail, 2 skipped (Qwen installer tests intentionally refuse root execution) |
| New `tests/cinematic-scene-effects.test.mjs` | 12/12 pass: preference parsing, sun-light mapping, manual vs. sun light, relief paint switching and change-only writes, curtain visibility rules, curtain failure isolation, densified ring, selection ping, flyover bounds, layer registration, stylesheet order |
| Updated harness stubs | `tests/area-underlay.test.mjs` runs the real `activateMapRepresentation` body in a sandbox and now also stubs `stopFlyover` (a mode change cancels a running flyover). `tests/snapshot-map-state.test.mjs` stubs the new `./scene-effects` import. No assertions were removed or relaxed. |
| ESLint on changed files | 0 errors; new files 0 warnings; `page.tsx` keeps its 25 existing warnings, none on changed lines |
| `tools/validators/maplibre/assess_acquisition_inventory.py` | Same result and finding counts as the base commit (pre-existing `FAIL`); no new renderer acquisition. New modules take MapLibre types only through `app/maplibre-seam.ts`. |
| Rendered checks (headless Chromium, SwiftShader WebGL, live Mapzen DEM) | Desktop 1440 × 900 and phone 390 × 844: 2D, tilted 2D, Terrain 3D at statewide and local zoom, globe, controls panel, sun-following toggle, flyover start/advance/stop by click. No page errors. Terrain views reach the runtime *ready* state and go idle when the shimmer is off. |

A curtain that cannot be created (for example a shader that fails to compile) is removed quietly; it never marks the map style or runtime as failed. Snapshot maps follow the same scene-effect preference.

During development, the curtain's first version re-sampled terrain under the whole border on every source update, which kept a high-zoom Terrain 3D view from settling. It now samples only near the view, and only when the camera settles or the terrain DEM loads. The rendered check above confirms the fix.

## Not covered

- Selection glow and ping were not seen rendered: the sandbox could not reach the provider feeds that supply selectable features, and the bundled local registry is empty. Their logic and layer wiring are unit-tested.
- The standard OpenFreeMap and imagery basemaps were unreachable from the sandbox, so effects were viewed over the offline Midnight style only.
- Real GPU performance on phones and low-end laptops, touch gestures during a flyover, screen readers and physical hardware.
- Saving, deploying or mirroring this source to the Site project.

## Rollback

Switch the effects off in **Scene effects** to restore the previous relief palette, sky and border. To remove the change entirely, revert the commit. No stored data, database schema, API, URL or saved-workspace format is affected; the only new storage is the device-local `kfm-scene-effects-v1` preference, which is ignored once the code is reverted.
