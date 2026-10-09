# Scene Studio

Scene Studio gives the existing MapLibre map a compact light-and-camera workspace. Open **Scene** on the map in any view. The atlas remains the main surface; the toolbar and data workflows are unchanged.

## Presentation recipes

- **Daylight:** clear sky, crisp cyan curtain and outline, light from 210°.
- **Golden hour:** dusk sky, copper curtain and outline, warm horizon, light from 265°.
- **Blue hour:** night sky, cool blue curtain and outline, light from 225°.
- **Survey:** legacy restrained relief/sky, light from 315°, with curtain and outline glow off.

These names describe presentation light, not capture time or observed weather. Recipes update the existing atmosphere, azimuth and cinematic settings; they do not add a separately saved theme. Manual lighting changes display **Custom**; real-sun following displays **Following the sun** instead of falsely selecting a manual recipe. Recipes preserve the current basemap, camera, DEM provider/exaggeration, 2D-relief choice, provider layers, columns/buildings switches and dates. They never request new DEMs. Optional curtains/glow previously switched off stay off; use **Effects & rendering** to enable them explicitly.

The current basemap continues to determine the terrain relief treatment. Survey does not switch to a new topographic provider. Provider building palettes follow the existing lighting pipeline. Provider-value and hazard colors remain unchanged. The Kansas outline is the existing simplified display boundary.

## Camera composition

Tilt and orientation use the current MapLibre camera. The lens slider controls the actual vertical field of view through [Map.setVerticalFieldOfView](https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/#setverticalfieldofview), not a CSS zoom. Controls read the actual camera after movement, lens updates and restored views. Tilt respects the existing maximum: 60° for flat/tilted maps, 72° for Terrain 3D; globe tilt is fixed. Lens bounds are 20–60°.

Manual camera controls stop flyover/orbit. Sliders update immediately. Reset uses a 300 ms ease unless reduced motion is enabled, and preserves location, zoom and active data:

| View | Tilt | Bearing | Vertical field of view |
| --- | ---: | ---: | ---: |
| 2D map | 0° | 0° | 36° |
| Tilted map | 56° | 0° | 36° |
| Terrain 3D | 48° | 0° | 44° |
| Globe | 0° | 0° | 42° |

The existing flyover and Cinematic/Natural/Plain modes remain available. Cinematic and Natural explicitly enable 2D relief as before; their descriptions disclose this, unlike the new presentation recipes that preserve the current DEM choice. Plain restores the original appearance, including the original offline outline palette.

## Rendering and limits

The existing [MapLibre CustomLayerInterface](https://maplibre.org/maplibre-gl-js/docs/API/interfaces/CustomLayerInterface/) draws the Kansas curtain with its existing vertex buffer, program and projection variants. Effective scene lighting selects static palette objects; the render callback updates uniforms. Palette changes allocate no new GPU resources and introduce no animation or repaint loop. Decorative outline/beacon colors update in place only when changed. Existing Battery saver, hidden-tab and reduced-motion gates remain in force. There is no added terrain, shadow geometry, simulated weather, observation or elevation value.

## Verification

- Combined studio, cinematic, overlay, terrain performance/provenance/relief and effects-containment suite: 49 tests passed.
- New studio behavior tests plus overlay suite: 12 tests passed, covering real component callbacks, unique control IDs, manual/custom/sun matching, camera clamps and reset preserving location/zoom, reduced motion, effective renderer-to-GPU palette updates, stable resources, unchanged repaint work, paused shimmer, and offline palette restoration.
- TypeScript: passed. Changed-file ESLint: zero errors; 25 warnings in existing `page.tsx` code.
- Final production build and complete Site suite: 815 tests passed.
- Independent browser review passed at desktop, tablet and 375 px phone widths: recipes, manual/solar lighting, keyboard lens adjustment, Escape/focus return, scroll access to Plain, and live flyover-to-manual-camera handoff. Screenshots confirm the rendered studio and tilted map. A temporary renderer degradation during hot reload/viewport changes recovered after a fresh reload; sustained device/GPU and full provider acceptance remain separate.

## Rollback

At runtime, choose **Effects & rendering → Plain** and use **Reset composition** for the current view. To remove this feature from source, restore only `app/scene-effects-controls.tsx`, `app/scene-effects.css`, `app/page.tsx`, `app/scene-effects.ts`, `app/scene-overlays.ts`, `app/aurora-curtain-layer.ts`, `app/map-runtime.ts`, `tests/scene-overlays.test.mjs` and `docs/cinematic-scene-effects.md` from the verified pre-change Site source; remove this document, `app/scene-studio.ts` and `tests/scene-studio.test.mjs`. No data, bindings, provider setup or stored user assets require migration. The existing scene-effect preference key remains unchanged.
