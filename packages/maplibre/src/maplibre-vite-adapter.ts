import workerUrl from "maplibre-gl/dist/maplibre-gl-worker.mjs?worker&url";
import { setWorkerUrl } from "maplibre-gl";

import {
  createMapLibreAdapter,
  type MapLibreAdapter,
  type MapLibreAdapterOptions,
} from "./maplibre-adapter";
import type {
  Synthetic3DFixtureLabController,
  Synthetic3DFixtureLabOptions,
} from "./synthetic-3d-fixture-contract";

export {
  SYNTHETIC_3D_FIXTURE_EXTRUSION_LAYER_ID,
  SYNTHETIC_3D_FIXTURE_FEATURES,
  SYNTHETIC_3D_FIXTURE_LAB_PROFILE,
  SYNTHETIC_3D_FIXTURE_SOURCE_ID,
  Synthetic3DFixtureLabError,
} from "./synthetic-3d-fixture-contract";
export type {
  Synthetic3DFixtureCamera,
  Synthetic3DFixtureFeature,
  Synthetic3DFixtureLabController,
  Synthetic3DFixtureLabOptions,
  Synthetic3DFixtureLabReasonCode,
  Synthetic3DFixtureLabSnapshot,
  Synthetic3DFixtureLabState,
  Synthetic3DFixtureProjection,
  Synthetic3DFixtureSelection,
} from "./synthetic-3d-fixture-contract";

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
 * Create the branch-only synthetic 3D fixture lab through the same package-owned
 * Vite worker seam. The renderer implementation is loaded only when an app
 * explicitly opts into the fixture lab.
 */
export async function createViteSynthetic3DFixtureLab(
  options: Synthetic3DFixtureLabOptions,
): Promise<Synthetic3DFixtureLabController> {
  configureMapLibreViteWorker();
  const { createSynthetic3DFixtureLab } = await import(
    "./synthetic-3d-fixture-lab"
  );
  return createSynthetic3DFixtureLab(options);
}
