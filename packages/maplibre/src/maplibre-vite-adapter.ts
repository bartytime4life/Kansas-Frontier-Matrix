import "maplibre-gl/dist/maplibre-gl.css";

import workerUrl from "maplibre-gl/dist/maplibre-gl-worker.mjs?worker&url";
import { setWorkerUrl } from "maplibre-gl";

import {
  createMapLibreAdapter,
  type MapLibreAdapterOptions,
} from "./maplibre-adapter";
import type { InlineGeoJsonMapRuntimePort } from "./map-runtime-port";

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
): InlineGeoJsonMapRuntimePort {
  configureMapLibreViteWorker();
  return createMapLibreAdapter(options);
}
