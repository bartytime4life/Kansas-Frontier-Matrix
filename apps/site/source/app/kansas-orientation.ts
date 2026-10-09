import type { FeatureCollection, LineString, Polygon } from "geojson";
import type { LayerSpecification, SourceSpecification } from "maplibre-gl";

/**
 * Offline orientation for the local basemaps. When the standard vector
 * basemap is unreachable, the Site falls back to a local style; without this
 * the map is an empty colour. These shapes are hand-simplified display
 * geometry (a few dozen vertices) bundled with the application. They orient
 * the reader and carry no evidence, measurement, legal boundary or source
 * authority. Layer ids deliberately avoid the `kfm-` prefix so registry and
 * overlay placement logic keeps treating them as basemap.
 */
export const ORIENTATION_SOURCE_ID = "orientation-kansas";

const KANSAS_OUTLINE: [number, number][] = [
  [-102.0517, 40.0], [-95.308, 40.0], [-95.2, 39.93], [-95.08, 39.87], [-94.99, 39.78],
  [-95.01, 39.68], [-95.1, 39.57], [-95.04, 39.47], [-94.96, 39.37], [-94.9, 39.3],
  [-94.8, 39.2], [-94.62, 39.115], [-94.608, 39.05], [-94.6178, 37.0], [-102.0418, 36.993],
  [-102.0517, 40.0],
];

// Simplified courses of major Kansas rivers (display only).
const RIVERS: { name: string; coordinates: [number, number][] }[] = [
  { name: "Arkansas River", coordinates: [[-102.05, 38.05], [-101.4, 38.0], [-101.0, 37.97], [-100.5, 37.85], [-100.0, 37.75], [-99.6, 37.85], [-99.3, 37.95], [-99.0, 38.2], [-98.77, 38.36], [-98.45, 38.3], [-98.2, 38.2], [-97.9, 38.06], [-97.6, 37.9], [-97.33, 37.69], [-97.2, 37.4], [-97.04, 37.0]] },
  { name: "Smoky Hill and Kansas rivers", coordinates: [[-102.05, 38.9], [-101.5, 38.88], [-101.0, 38.85], [-100.3, 38.83], [-99.5, 38.85], [-98.9, 38.78], [-98.6, 38.75], [-98.1, 38.78], [-97.61, 38.84], [-97.2, 38.95], [-96.83, 39.03], [-96.57, 39.18], [-96.2, 39.12], [-95.68, 39.05], [-95.23, 38.97], [-94.9, 39.07], [-94.62, 39.11]] },
  { name: "Republican River", coordinates: [[-98.0, 40.0], [-97.75, 39.8], [-97.6, 39.6], [-97.4, 39.45], [-97.2, 39.3], [-97.0, 39.15], [-96.83, 39.03]] },
  { name: "Neosho River", coordinates: [[-96.9, 38.9], [-96.5, 38.6], [-96.18, 38.4], [-95.8, 38.1], [-95.5, 37.85], [-95.3, 37.6], [-95.0, 37.25], [-94.85, 37.0]] },
  { name: "Solomon River", coordinates: [[-100.5, 39.45], [-99.8, 39.45], [-99.0, 39.4], [-98.3, 39.3], [-97.8, 39.1], [-97.61, 38.84]] },
];

function graticule(): { coordinates: [number, number][] }[] {
  const lines: { coordinates: [number, number][] }[] = [];
  for (let lon = -106; lon <= -90; lon += 1) lines.push({ coordinates: [[lon, 34], [lon, 43]] });
  for (let lat = 34; lat <= 43; lat += 1) lines.push({ coordinates: [[-106, lat], [-90, lat]] });
  return lines;
}

export const KANSAS_ORIENTATION: FeatureCollection<Polygon | LineString, { role: string; name?: string }> = Object.freeze({
  type: "FeatureCollection",
  features: [
    { type: "Feature", properties: { role: "outline", name: "Kansas (simplified)" }, geometry: { type: "Polygon", coordinates: [KANSAS_OUTLINE] } },
    ...RIVERS.map((river) => ({ type: "Feature" as const, properties: { role: "river", name: river.name }, geometry: { type: "LineString" as const, coordinates: river.coordinates } })),
    ...graticule().map((line) => ({ type: "Feature" as const, properties: { role: "graticule" }, geometry: { type: "LineString" as const, coordinates: line.coordinates } })),
  ],
}) as FeatureCollection<Polygon | LineString, { role: string; name?: string }>;

export type OrientationPalette = Readonly<{ land: string; outline: string; river: string; graticule: string }>;

export function orientationSource(): SourceSpecification {
  return { type: "geojson", data: KANSAS_ORIENTATION, attribution: "KFM simplified orientation outline · display only" };
}

export function orientationLayers(palette: OrientationPalette): LayerSpecification[] {
  return [
    { id: "orientation-graticule", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "graticule"], paint: { "line-color": palette.graticule, "line-width": 0.6, "line-opacity": 0.55 } },
    { id: "orientation-kansas-land", type: "fill", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "outline"], paint: { "fill-color": palette.land, "fill-opacity": 0.9 } },
    { id: "orientation-rivers", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "river"], layout: { "line-cap": "round", "line-join": "round" }, paint: { "line-color": palette.river, "line-width": ["interpolate", ["linear"], ["zoom"], 4, 1, 9, 2.6], "line-opacity": 0.85 } },
    { id: "orientation-kansas-outline", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "outline"], layout: { "line-join": "round" }, paint: { "line-color": palette.outline, "line-width": ["interpolate", ["linear"], ["zoom"], 4, 1.2, 9, 2.4], "line-opacity": 0.9 } },
  ];
}
