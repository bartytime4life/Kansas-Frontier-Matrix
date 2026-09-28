// The Site's single MapLibre acquisition seam (ADR-0006, separately built Site exception).
// Every other Site module takes renderer types and the runtime from here, never from
// maplibre-gl directly; tools/validators/maplibre/assess_acquisition_inventory.py enforces it.
export type * from "maplibre-gl";

export type MapLibreModule = typeof import("maplibre-gl");

// Loaded on demand so the renderer stays out of the initial bundle.
export const loadMapLibre = (): Promise<MapLibreModule> => import("maplibre-gl");
