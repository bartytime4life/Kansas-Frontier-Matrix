import type { FeatureCollection, LineString, Polygon } from "geojson";
import type { LayerSpecification, SourceSpecification } from "./maplibre-seam";

/**
 * Offline orientation for the local basemaps. When the standard vector
 * basemap is unreachable, the Site falls back to a local style; without this
 * the map is an empty colour. The state line is the real Census cartographic
 * boundary, simplified for state-scale display and bundled with the
 * application; no rivers or county lines are drawn, so nothing competes with
 * the layers a visitor chooses. They orient the reader and carry no evidence,
 * measurement, legal boundary or source authority. Layer ids deliberately
 * avoid the `kfm-` prefix so registry and overlay placement logic keeps
 * treating them as basemap.
 */
export const ORIENTATION_SOURCE_ID = "orientation-kansas";

/**
 * The Kansas state boundary from the U.S. Census Bureau's cartographic boundary
 * files (2017 edition), as distributed in us-atlas 3.0.1 (states-10m, simplified
 * for 1:10,000,000 display). The Missouri River edge follows the river; vertex
 * accuracy is a few hundred metres, so it is display context at state scale, not
 * a legal boundary.
 */
export const KANSAS_OUTLINE: readonly [number, number][] = [
  [-102.0529, 40.0029], [-101.1304, 40.002], [-100.7572, 40.002], [-99.8132, 40.0012], [-98.8333, 40.002],
  [-98.2482, 40.002], [-97.2468, 40.0012], [-96.3028, 40.0003], [-95.786, 40.0003], [-95.3086, 40.0003],
  [-95.2512, 39.9488], [-95.2045, 39.9393], [-95.2009, 39.9024], [-95.1543, 39.9075], [-95.1363, 39.8766],
  [-95.043, 39.8646], [-95.0143, 39.8998], [-94.9281, 39.8886], [-94.9425, 39.8646], [-94.9174, 39.8362],
  [-94.8779, 39.8268], [-94.8923, 39.7907], [-94.9246, 39.7898], [-94.9138, 39.7589], [-94.8707, 39.7727],
  [-94.8743, 39.7306], [-94.9102, 39.7254], [-94.9569, 39.746], [-94.9748, 39.6816], [-95.0286, 39.6653],
  [-95.0538, 39.6301], [-95.0466, 39.5948], [-95.1076, 39.5742], [-95.104, 39.533], [-95.0502, 39.4978],
  [-95.0466, 39.4729], [-94.9892, 39.4462], [-94.9461, 39.3938], [-94.8958, 39.3938], [-94.8779, 39.3758],
  [-94.9102, 39.3543], [-94.8887, 39.2864], [-94.8241, 39.2418], [-94.8348, 39.2177], [-94.781, 39.2065],
  [-94.763, 39.1799], [-94.7128, 39.1705], [-94.6805, 39.1842], [-94.6625, 39.1576], [-94.5908, 39.155],
  [-94.6087, 39.1198], [-94.6087, 38.7384], [-94.6123, 38.6353], [-94.6123, 38.0374], [-94.6159, 37.9927],
  [-94.6159, 37.3235], [-94.6195, 37.2402], [-94.6195, 36.9988], [-95.5132, 36.9996], [-96.2167, 36.9988],
  [-96.8233, 36.9988], [-97.6058, 36.9988], [-98.3523, 36.9979], [-99.2784, 36.9996], [-99.6481, 36.9996],
  [-100.2008, 37.0022], [-100.7356, 36.9988], [-101.4858, 36.9953], [-102.0421, 36.9928], [-102.0421, 37.9283],
  [-102.0457, 38.046], [-102.0457, 39.137], [-102.0493, 39.3028], [-102.0493, 39.6756], [-102.0529, 40.0029],
];

function graticule(): { coordinates: [number, number][] }[] {
  const lines: { coordinates: [number, number][] }[] = [];
  for (let lon = -106; lon <= -90; lon += 1) lines.push({ coordinates: [[lon, 34], [lon, 43]] });
  for (let lat = 34; lat <= 43; lat += 1) lines.push({ coordinates: [[-106, lat], [-90, lat]] });
  return lines;
}

// A coarse 15° world graticule so the globe reads as a sphere offline.
function worldGraticule(): { coordinates: [number, number][] }[] {
  const lines: { coordinates: [number, number][] }[] = [];
  const span = (from: number, to: number, step: number) => Array.from({ length: Math.round((to - from) / step) + 1 }, (_, index) => from + index * step);
  for (const lon of span(-180, 165, 15)) lines.push({ coordinates: span(-80, 80, 5).map((lat) => [lon, lat] as [number, number]) });
  for (const lat of span(-75, 75, 15)) lines.push({ coordinates: span(-180, 180, 5).map((lon) => [lon, lat] as [number, number]) });
  return lines;
}

export const KANSAS_ORIENTATION: FeatureCollection<Polygon | LineString, { role: string; name?: string }> = Object.freeze({
  type: "FeatureCollection",
  features: [
    { type: "Feature", properties: { role: "outline", name: "Kansas" }, geometry: { type: "Polygon", coordinates: [[...KANSAS_OUTLINE]] } },
    ...graticule().map((line) => ({ type: "Feature" as const, properties: { role: "graticule" }, geometry: { type: "LineString" as const, coordinates: line.coordinates } })),
    ...worldGraticule().map((line) => ({ type: "Feature" as const, properties: { role: "world-graticule" }, geometry: { type: "LineString" as const, coordinates: line.coordinates } })),
  ],
}) as FeatureCollection<Polygon | LineString, { role: string; name?: string }>;

export type OrientationPalette = Readonly<{ land: string; outline: string; muted: string; graticule: string }>;

export function orientationSource(): SourceSpecification {
  return { type: "geojson", data: KANSAS_ORIENTATION, attribution: "U.S. Census Bureau cartographic boundaries (2017, simplified) · display only" };
}

export function orientationLayers(palette: OrientationPalette): LayerSpecification[] {
  return [
    { id: "orientation-world-graticule", type: "line", source: ORIENTATION_SOURCE_ID, maxzoom: 5, filter: ["==", ["get", "role"], "world-graticule"], paint: { "line-color": palette.muted, "line-width": 0.8, "line-opacity": ["interpolate", ["linear"], ["zoom"], 0, 0.42, 3, 0.26, 4.6, 0] } },
    { id: "orientation-graticule", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "graticule"], paint: { "line-color": palette.graticule, "line-width": 0.6, "line-opacity": 0.55 } },
    { id: "orientation-kansas-land", type: "fill", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "outline"], paint: { "fill-color": palette.land, "fill-opacity": 0.9 } },
    // A soft blurred under-stroke gives the offline style depth. Presentation only.
    { id: "orientation-kansas-glow", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "outline"], layout: { "line-join": "round" }, paint: { "line-color": palette.outline, "line-width": ["interpolate", ["linear"], ["zoom"], 4, 9, 9, 18], "line-blur": ["interpolate", ["linear"], ["zoom"], 4, 7, 9, 14], "line-opacity": 0.32 } },
    { id: "orientation-kansas-outline", type: "line", source: ORIENTATION_SOURCE_ID, filter: ["==", ["get", "role"], "outline"], layout: { "line-join": "round" }, paint: { "line-color": palette.outline, "line-width": ["interpolate", ["linear"], ["zoom"], 4, 1.2, 9, 2.4], "line-opacity": 0.9 } },
  ];
}
