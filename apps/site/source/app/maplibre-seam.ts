// The Site's single MapLibre acquisition seam (ADR-0006, separately built Site exception).
// Every other Site module takes renderer types and the runtime from here, never from
// maplibre-gl directly; tools/validators/maplibre/assess_acquisition_inventory.py enforces it.
export type * from "maplibre-gl";

export type MapLibreModule = typeof import("maplibre-gl");

// Loaded on demand so the renderer stays out of the initial bundle.
let cacheProtocolInstalled = false;
export const loadMapLibre = async (): Promise<MapLibreModule> => {
  const runtime = await import("maplibre-gl");
  const { basemapCacheProtocol } = await import("./basemap-cache");
  if (!cacheProtocolInstalled) {
    installMapProtocol(runtime, "kfm-basemap", basemapCacheProtocol);
    cacheProtocolInstalled = true;
  }
  return runtime;
};

// Keep renderer protocol registration at the same acquisition seam as the
// module import. Callers provide only the bounded tile loader and own teardown.
export function installMapProtocol(runtime: MapLibreModule, name: string,
  load: Parameters<MapLibreModule["addProtocol"]>[1]): void {
  runtime.addProtocol(name, load);
}
