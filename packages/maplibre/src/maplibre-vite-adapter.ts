import workerUrl from "maplibre-gl/dist/maplibre-gl-worker.mjs?worker&url";
import { setWorkerUrl } from "maplibre-gl";

import {
  createMapLibreAdapter,
  type MapLibreAdapter,
  type MapLibreAdapterOptions,
} from "./maplibre-adapter";
import {
  createSynthetic3dFixtureLab,
  type Synthetic3dFixtureFeature,
  type Synthetic3dFixtureLabController,
  type Synthetic3dFixtureLabOptions,
  type Synthetic3dFixtureProjection,
  type Synthetic3dFixtureSelection,
  type Synthetic3dFixtureSkyPreset,
  type Synthetic3dFixtureSnapshot,
  type Synthetic3dFixtureStatus,
} from "./synthetic-3d-fixture-lab";

export {
  SYNTHETIC_3D_EXTRUSION_LAYER_ID,
  SYNTHETIC_3D_FIXTURE_FEATURES,
  SYNTHETIC_3D_FIXTURE_PROFILE,
  SYNTHETIC_3D_FIXTURE_SOURCE_ID,
  SYNTHETIC_3D_POINT_LAYER_ID,
  Synthetic3dFixtureLabError,
} from "./synthetic-3d-fixture-lab";
export type {
  Synthetic3dFixtureFeature,
  Synthetic3dFixtureLabController,
  Synthetic3dFixtureLabOptions,
  Synthetic3dFixtureProjection,
  Synthetic3dFixtureSelection,
  Synthetic3dFixtureSkyPreset,
  Synthetic3dFixtureSnapshot,
  Synthetic3dFixtureStatus,
};

let workerConfigured = false;

/**
 * Configure MapLibre's v6 worker for a Vite consumer exactly once.
 *
 * Vite's worker pipeline emits a self-contained, same-origin worker asset.
 * Keeping this setup in the package-owned adapter seam prevents an app from
 * acquiring MapLibre directly or depending on its worker distribution layout.
 */
function configureMapLibreViteWorker(): void {
  if (workerConfigured) return;
  setWorkerUrl(workerUrl);
  workerConfigured = true;
}

/** Create the admitted adapter with MapLibre's Vite worker configured first. */
export function createViteMapLibreAdapter(
  options: MapLibreAdapterOptions,
): MapLibreAdapter {
  configureMapLibreViteWorker();
  return createMapLibreAdapter(options);
}

/**
 * Create the isolated synthetic 3D fixture lab with the same package-owned
 * Vite worker boundary. The lab is inline-only and does not admit external
 * styles, tiles, APIs, DEMs, PMTiles, glyphs, sprites, or live sources.
 */
export function createViteSynthetic3dFixtureLab(
  options: Synthetic3dFixtureLabOptions,
): Promise<Synthetic3dFixtureLabController> {
  configureMapLibreViteWorker();
  return createSynthetic3dFixtureLab(options);
}
