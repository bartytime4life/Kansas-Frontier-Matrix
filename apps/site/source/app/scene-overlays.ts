import type { Feature, FeatureCollection, Polygon } from "geojson";
import type { GeoJSONSource, LayerSpecification, Map as MapLibreMap } from "./maplibre-seam";
import { KANSAS_OUTLINE, ORIENTATION_SOURCE_ID } from "./kansas-orientation";
import { uploadedGeoJSON } from "./map-performance";
import { createNightSkyLayer, nightSkyShouldShow, SKY_DARKNESS, type NightSkyCatalog } from "./night-sky";
import { CURTAIN_MIN_PITCH, effectiveSceneLight, sceneEffectsFor, type SceneLightPreset } from "./scene-effects";
import type { TerrainSourceRecord } from "./terrain-sources";

/**
 * Scene overlays that carry the cinematic look into every view: a Kansas glow
 * and orbit beacon on any basemap, optional 2D shaded relief, 3D columns for
 * provider point values, and light-matched provider buildings.
 *
 * All are display derivatives. Columns are drawn from the same features the
 * official layers already show and encode only a provider value; missing
 * values draw no column. Nothing here is queryable, reported or exported.
 */

type MapProjection = string | undefined;
const projectionOf = (map: MapLibreMap): MapProjection => {
  const type = map.getProjection()?.type;
  return typeof type === "string" ? type : undefined;
};

/** Below data overlays and labels, above the basemap. */
const firstOverlayId = (map: MapLibreMap): string | undefined => map.getStyle().layers?.find((layer) => layer.type === "symbol"
  || (layer.id.startsWith("kfm-") && layer.id !== "kfm-background") || layer.id.startsWith("external-"))?.id;

const removeLayers = (map: MapLibreMap, layerIds: readonly string[], sourceId?: string) => {
  for (const id of layerIds) if (map.getLayer(id)) map.removeLayer(id);
  if (sourceId && map.getSource(sourceId)) map.removeSource(sourceId);
};

const setVisibility = (map: MapLibreMap, id: string, visible: boolean) => {
  if (!map.getLayer(id)) return;
  const value = visible ? "visible" : "none";
  if (map.getLayoutProperty(id, "visibility") !== value) map.setLayoutProperty(id, "visibility", value);
};

// ---------------------------------------------------------------------------
// Kansas glow and orbit beacon
// ---------------------------------------------------------------------------

export const KANSAS_GLOW_SOURCE_ID = "scene-kansas-glow";
export const KANSAS_GLOW_LAYER_IDS = ["scene-kansas-glow-halo", "scene-kansas-glow-edge", "scene-kansas-beacon"] as const;
const KANSAS_CENTER: [number, number] = [-98.38, 38.48];
export const KANSAS_GLOW_PALETTES: Record<SceneLightPreset, readonly [string, string, string]> = {
  night: ["#508bd8", "#a2d9ff", "#85bbf5"],
  dusk: ["#d68c49", "#ffe0a1", "#f3b56a"],
  clear: ["#42b7c8", "#baf3f2", "#7edee8"],
};
// The offline outline keeps its source, widths and geometry. Plain restores
// its original palette, including after a style switch (layer identity key).
const offlineOutlineColors = new WeakMap<object, unknown>();
function syncOfflineOutlineColor(map: MapLibreMap, enabled: boolean, colors: readonly string[]) {
  ["orientation-kansas-glow", "orientation-kansas-outline"].forEach((id, index) => {
    const layer = map.getLayer(id);
    if (!layer) return;
    if (!enabled) {
      if (offlineOutlineColors.has(layer)) {
        map.setPaintProperty(id, "line-color", offlineOutlineColors.get(layer) as never);
        offlineOutlineColors.delete(layer);
      }
      return;
    }
    if (!offlineOutlineColors.has(layer)) offlineOutlineColors.set(layer, map.getPaintProperty(id, "line-color"));
    if (map.getPaintProperty(id, "line-color") !== colors[index]) map.setPaintProperty(id, "line-color", colors[index]);
  });
}

export const kansasGlowData = (): FeatureCollection => ({
  type: "FeatureCollection",
  features: [
    { type: "Feature", properties: { role: "outline" }, geometry: { type: "Polygon", coordinates: [[...KANSAS_OUTLINE]] } },
    { type: "Feature", properties: { role: "beacon" }, geometry: { type: "Point", coordinates: KANSAS_CENTER } },
  ],
});

export function kansasGlowLayers(): LayerSpecification[] {
  return [
    { id: KANSAS_GLOW_LAYER_IDS[0], type: "line", source: KANSAS_GLOW_SOURCE_ID, filter: ["==", ["get", "role"], "outline"], layout: { "line-join": "round" }, paint: {
      "line-color": "#f2c55c",
      "line-width": ["interpolate", ["linear"], ["zoom"], 0, 3, 4, 10, 9, 22],
      "line-blur": ["interpolate", ["linear"], ["zoom"], 0, 3, 4, 8, 9, 16],
      "line-opacity": 0.34,
    } },
    { id: KANSAS_GLOW_LAYER_IDS[1], type: "line", source: KANSAS_GLOW_SOURCE_ID, filter: ["==", ["get", "role"], "outline"], layout: { "line-join": "round" }, paint: {
      "line-color": "#ffe2a0",
      "line-width": ["interpolate", ["linear"], ["zoom"], 0, 0.6, 4, 1.2, 9, 2.2],
      "line-opacity": 0.7,
    } },
    // A soft point of light marks Kansas from orbit and fades as it grows on screen.
    { id: KANSAS_GLOW_LAYER_IDS[2], type: "circle", source: KANSAS_GLOW_SOURCE_ID, maxzoom: 5, filter: ["==", ["get", "role"], "beacon"], paint: {
      "circle-color": "#ffd77f",
      "circle-radius": ["interpolate", ["linear"], ["zoom"], 0, 16, 2.5, 26, 4.8, 8],
      "circle-blur": 1,
      "circle-opacity": ["interpolate", ["linear"], ["zoom"], 0, 0.9, 3, 0.6, 4.8, 0],
    } },
  ] as LayerSpecification[];
}

export function syncKansasGlow(map: MapLibreMap, light: SceneLightPreset = "night", azimuth = 210): void {
  if (!sceneEffectsFor(map).kansasGlow) {
    syncOfflineOutlineColor(map, false, []);
    removeLayers(map, KANSAS_GLOW_LAYER_IDS, KANSAS_GLOW_SOURCE_ID);
    return;
  }
  const colors = KANSAS_GLOW_PALETTES[effectiveSceneLight(map, light, azimuth).preset];
  syncOfflineOutlineColor(map, true, colors);
  if (!map.getSource(KANSAS_GLOW_SOURCE_ID)) map.addSource(KANSAS_GLOW_SOURCE_ID, { type: "geojson", data: kansasGlowData(), attribution: "KFM simplified Kansas outline · display only" });
  if (!map.getLayer(KANSAS_GLOW_LAYER_IDS[0])) {
    const beforeId = firstOverlayId(map);
    for (const layer of kansasGlowLayers()) map.addLayer(layer, beforeId);
  }
  KANSAS_GLOW_LAYER_IDS.forEach((id, index) => {
    const property = index === 2 ? "circle-color" : "line-color";
    if (map.getPaintProperty(id, property) !== colors[index]) map.setPaintProperty(id, property, colors[index]);
  });
  // The offline styles already draw their own outline glow; keep only the beacon there.
  const offlineStyle = Boolean(map.getSource(ORIENTATION_SOURCE_ID));
  setVisibility(map, KANSAS_GLOW_LAYER_IDS[0], !offlineStyle);
  setVisibility(map, KANSAS_GLOW_LAYER_IDS[1], !offlineStyle);
  setVisibility(map, KANSAS_GLOW_LAYER_IDS[2], true);
}

// ---------------------------------------------------------------------------
// 2D shaded relief
// ---------------------------------------------------------------------------

export const RELIEF_2D_SOURCE_ID = "scene-relief-dem";
export const RELIEF_2D_LAYER_ID = "scene-relief-2d";

const RELIEF_2D_PALETTES: Record<SceneLightPreset, Readonly<{ highlight: string; shadow: string; accent: string }>> = {
  night: { highlight: "rgba(188, 216, 238, 0.32)", shadow: "rgba(2, 8, 24, 0.62)", accent: "rgba(44, 74, 110, 0.3)" },
  dusk: { highlight: "rgba(255, 214, 160, 0.34)", shadow: "rgba(8, 10, 34, 0.58)", accent: "rgba(63, 95, 138, 0.28)" },
  clear: { highlight: "rgba(255, 248, 228, 0.36)", shadow: "rgba(14, 34, 54, 0.5)", accent: "rgba(88, 125, 148, 0.26)" },
};

export function relief2dPaint(preset: SceneLightPreset, azimuth: number) {
  const palette = RELIEF_2D_PALETTES[preset];
  return {
    "hillshade-method": "standard" as const,
    "hillshade-illumination-anchor": "map" as const,
    "hillshade-illumination-direction": ((azimuth % 360) + 360) % 360,
    "hillshade-exaggeration": 0.74,
    "hillshade-highlight-color": palette.highlight,
    "hillshade-shadow-color": palette.shadow,
    "hillshade-accent-color": palette.accent,
  };
}

/** 2D relief is shown only on flat (Mercator, no terrain) maps; Terrain 3D has its own relief. */
export const relief2dShouldShow = (relief2d: boolean, terrainOn: boolean, projection: MapProjection): boolean =>
  relief2d && !terrainOn && projection !== "globe";

export function syncRelief2d(map: MapLibreMap, dem: TerrainSourceRecord, light: SceneLightPreset, azimuth: number): void {
  const show = relief2dShouldShow(sceneEffectsFor(map).relief2d, Boolean(map.getTerrain()), projectionOf(map));
  // Removing the source (not just hiding it) stops DEM requests when off.
  if (!show || !dem.tileTemplate) { removeLayers(map, [RELIEF_2D_LAYER_ID], RELIEF_2D_SOURCE_ID); return; }
  if (!map.getSource(RELIEF_2D_SOURCE_ID)) {
    map.addSource(RELIEF_2D_SOURCE_ID, {
      type: "raster-dem",
      tiles: [dem.tileTemplate],
      tileSize: dem.tileSize ?? 256,
      ...(dem.minZoom === undefined ? {} : { minzoom: dem.minZoom }),
      maxzoom: dem.maxZoom ?? 11,
      ...(dem.bounds === undefined ? {} : { bounds: [...dem.bounds] as [number, number, number, number] }),
      encoding: dem.encoding,
      attribution: dem.attribution,
    });
  }
  const scene = effectiveSceneLight(map, light, azimuth);
  const paint = relief2dPaint(scene.preset, scene.azimuth);
  if (!map.getLayer(RELIEF_2D_LAYER_ID)) {
    // Beneath the glow, data overlays and labels.
    const beforeId = map.getLayer(KANSAS_GLOW_LAYER_IDS[0]) ? KANSAS_GLOW_LAYER_IDS[0] : firstOverlayId(map);
    map.addLayer({ id: RELIEF_2D_LAYER_ID, type: "hillshade", source: RELIEF_2D_SOURCE_ID, paint } as LayerSpecification, beforeId);
    return;
  }
  for (const [key, value] of Object.entries(paint)) {
    const property = key as Parameters<MapLibreMap["setPaintProperty"]>[1];
    if (JSON.stringify(map.getPaintProperty(RELIEF_2D_LAYER_ID, property)) !== JSON.stringify(value)) map.setPaintProperty(RELIEF_2D_LAYER_ID, property, value);
  }
}

// ---------------------------------------------------------------------------
// 3D value columns
// ---------------------------------------------------------------------------

export const COLUMNS_SOURCE_ID = "scene-value-columns";
export const COLUMNS_LAYER_ID = "scene-value-columns";
export const MAX_COLUMNS = 2000;

export type ColumnFeed = Readonly<{
  kind: "earthquake" | "streamflow";
  sourceId: string;
  /** The official point layer; columns follow its visibility. */
  pointLayerId: string;
}>;

type ColumnProperties = Readonly<{ kind: ColumnFeed["kind"]; h: number; color: string; id: string }>;

const hexToRgb = (hex: string) => [1, 3, 5].map((offset) => parseInt(hex.slice(offset, offset + 2), 16));
const mixHex = (a: string, b: string, t: number) => {
  const [ar, ag, ab] = hexToRgb(a), [br, bg, bb] = hexToRgb(b);
  const channel = (x: number, y: number) => Math.round(x + (y - x) * t).toString(16).padStart(2, "0");
  return `#${channel(ar, br)}${channel(ag, bg)}${channel(ab, bb)}`;
};
/** Same colour ramp as the earthquake points: 0 → 2 → 4 → 6 magnitude. */
export function earthquakeColumnColor(magnitude: number): string {
  const stops: [number, string][] = [[0, "#ffd7a8"], [2, "#f2a65a"], [4, "#ef6b45"], [6, "#d9364f"]];
  if (magnitude <= stops[0][0]) return stops[0][1];
  for (let index = 1; index < stops.length; index += 1) {
    const [m1, c1] = stops[index];
    if (magnitude <= m1) { const [m0, c0] = stops[index - 1]; return mixHex(c0, c1, (magnitude - m0) / (m1 - m0)); }
  }
  return stops[stops.length - 1][1];
}
const STREAMFLOW_TREND_COLORS: Record<string, string> = { rising: "#55e6ff", falling: "#a5b4ff", steady: "#73cfa8" };

/** Column height as a 0–1 share of the zoom-scaled maximum, or null for no column. */
export function columnValue(kind: ColumnFeed["kind"], properties: Record<string, unknown> | null | undefined): { h: number; color: string } | null {
  if (!properties) return null;
  if (kind === "earthquake") {
    const magnitude = Number(properties.magnitude);
    if (properties.magnitude === null || properties.magnitude === undefined || !Number.isFinite(magnitude) || magnitude < 0) return null;
    return { h: Math.max(0.04, Math.min(1, magnitude / 6)), color: earthquakeColumnColor(magnitude) };
  }
  const value = Number(properties.value);
  const visual = Number(properties.visualMagnitude);
  if (properties.missing === true || !(value > 0) || !Number.isFinite(visual)) return null;
  return { h: Math.max(0.04, Math.min(1, visual / 5)), color: STREAMFLOW_TREND_COLORS[String(properties.trend)] ?? "#67e8f9" };
}

/** A small hexagon footprint (metres) around a point. */
export function hexagon(center: readonly [number, number], radiusMeters: number): Polygon {
  const [lng, lat] = center;
  const dLat = radiusMeters / 111_320;
  const dLng = radiusMeters / (111_320 * Math.cos((lat * Math.PI) / 180));
  const ring: [number, number][] = Array.from({ length: 6 }, (_, index) => {
    const angle = (Math.PI / 3) * index + Math.PI / 6;
    return [lng + Math.cos(angle) * dLng, lat + Math.sin(angle) * dLat];
  });
  ring.push(ring[0]);
  return { type: "Polygon", coordinates: [ring] };
}

export function buildValueColumns(inputs: readonly Readonly<{ kind: ColumnFeed["kind"]; data: FeatureCollection | undefined }>[], radiusMeters = 3200): FeatureCollection<Polygon, ColumnProperties> {
  const features: Feature<Polygon, ColumnProperties>[] = [];
  for (const { kind, data } of inputs) {
    for (const [index, feature] of (data?.features ?? []).entries()) {
      if (features.length >= MAX_COLUMNS) break;
      if (feature.geometry?.type !== "Point") continue;
      const [lng, lat] = feature.geometry.coordinates;
      if (!Number.isFinite(lng) || !Number.isFinite(lat) || Math.abs(lat) > 85) continue;
      const value = columnValue(kind, feature.properties as Record<string, unknown> | null);
      if (!value) continue;
      features.push({ type: "Feature", properties: { kind, h: Number(value.h.toFixed(4)), color: value.color, id: String(feature.properties?.featureId ?? `${kind}-${index}`) }, geometry: hexagon([lng, lat], radiusMeters) });
    }
  }
  return { type: "FeatureCollection", features };
}

export const COLUMN_HEIGHT = ["interpolate", ["linear"], ["zoom"],
  4, ["*", ["get", "h"], 140000], 7, ["*", ["get", "h"], 52000], 10, ["*", ["get", "h"], 9000], 13, ["*", ["get", "h"], 1800]] as const;

export const columnsShouldShow = (columns: boolean, pitch: number, efficient: boolean): boolean =>
  columns && !efficient && Number.isFinite(pitch) && pitch >= CURTAIN_MIN_PITCH;

const layerVisible = (map: MapLibreMap, id: string) => Boolean(map.getLayer(id)) && map.getLayoutProperty(id, "visibility") !== "none";

/** Rebuilds columns from what the official point layers currently show. */
export function syncValueColumns(map: MapLibreMap, feeds: readonly ColumnFeed[], efficient: boolean): void {
  const settings = sceneEffectsFor(map);
  if (!settings.columns) { removeLayers(map, [COLUMNS_LAYER_ID], COLUMNS_SOURCE_ID); return; }
  const inputs = feeds.filter((feed) => layerVisible(map, feed.pointLayerId))
    .map((feed) => ({ kind: feed.kind, data: uploadedGeoJSON(map.getSource(feed.sourceId) as GeoJSONSource | undefined) }));
  const data = buildValueColumns(inputs);
  const source = map.getSource(COLUMNS_SOURCE_ID) as GeoJSONSource | undefined;
  if (!source) map.addSource(COLUMNS_SOURCE_ID, { type: "geojson", data, attribution: "Column heights encode provider values · display only" });
  else source.setData(data);
  if (!map.getLayer(COLUMNS_LAYER_ID)) {
    // Under the official point symbols so each point stays visible on its column.
    const beforeId = feeds.map((feed) => feed.pointLayerId).find((id) => map.getLayer(id)) ?? firstOverlayId(map);
    map.addLayer({ id: COLUMNS_LAYER_ID, type: "fill-extrusion", source: COLUMNS_SOURCE_ID, layout: { visibility: "none" }, paint: {
      "fill-extrusion-color": ["get", "color"],
      "fill-extrusion-height": COLUMN_HEIGHT as unknown as number,
      "fill-extrusion-base": 0,
      "fill-extrusion-opacity": 0.92,
      // A flat side tone keeps column colour close to the matching point colour.
      "fill-extrusion-vertical-gradient": false,
    } } as LayerSpecification, beforeId);
  }
  syncValueColumnsVisibility(map, efficient);
}

export function syncValueColumnsVisibility(map: MapLibreMap, efficient: boolean): void {
  setVisibility(map, COLUMNS_LAYER_ID, columnsShouldShow(sceneEffectsFor(map).columns, map.getPitch(), efficient));
}

// ---------------------------------------------------------------------------
// Lit provider buildings
// ---------------------------------------------------------------------------

export const BUILDINGS_LAYER_ID = "building-3d";
const BUILDING_PROPERTIES = ["fill-extrusion-color", "fill-extrusion-opacity", "fill-extrusion-vertical-gradient"] as const;
type BuildingProperty = (typeof BUILDING_PROPERTIES)[number];

const BUILDING_RAMPS: Record<SceneLightPreset, readonly [string, string, string, string]> = {
  clear: ["#e6d9c2", "#d3c3a8", "#b9c4d0", "#9cb7d8"],
  dusk: ["#f2c99c", "#dcab84", "#ab9dba", "#7f8fba"],
  night: ["#33465f", "#3f5674", "#55719a", "#86abdc"],
};

/** Height-shaded colour from the provider's own render_height; missing heights stay at the base colour. */
export function buildingPaint(preset: SceneLightPreset): Record<BuildingProperty, unknown> {
  const [c0, c1, c2, c3] = BUILDING_RAMPS[preset];
  return {
    "fill-extrusion-color": ["interpolate", ["linear"], ["coalesce", ["get", "render_height"], 0], 0, c0, 25, c1, 80, c2, 200, c3],
    "fill-extrusion-opacity": 0.94,
    "fill-extrusion-vertical-gradient": true,
  };
}

const buildingOriginals = new WeakMap<object, Map<BuildingProperty, unknown>>();

/** Applies or restores the provider style's building paint. Heights are never changed. */
export function syncBuildingStyle(map: MapLibreMap, light: SceneLightPreset, azimuth: number): void {
  const layer = map.getLayer(BUILDINGS_LAYER_ID);
  if (!layer || layer.type !== "fill-extrusion") return;
  let originals = buildingOriginals.get(layer);
  const settings = sceneEffectsFor(map);
  if (!settings.buildings || !settings.cinematic) {
    if (!originals) return;
    for (const [property, value] of originals) map.setPaintProperty(BUILDINGS_LAYER_ID, property, value as never);
    buildingOriginals.delete(layer);
    return;
  }
  if (!originals) {
    originals = new Map(BUILDING_PROPERTIES.map((property) => [property, map.getPaintProperty(BUILDINGS_LAYER_ID, property)]));
    buildingOriginals.set(layer, originals);
  }
  const paint = buildingPaint(effectiveSceneLight(map, light, azimuth).preset);
  for (const property of BUILDING_PROPERTIES) {
    if (JSON.stringify(map.getPaintProperty(BUILDINGS_LAYER_ID, property)) !== JSON.stringify(paint[property])) {
      map.setPaintProperty(BUILDINGS_LAYER_ID, property, paint[property] as never);
    }
  }
}

// ---------------------------------------------------------------------------
// Real night sky
// ---------------------------------------------------------------------------

export const NIGHT_SKY_LAYER_ID = "scene-night-sky";

// The catalog is a separate chunk, fetched the first time the sky is shown.
let catalog: NightSkyCatalog | null = null;
let catalogRequest: Promise<NightSkyCatalog | null> | null = null;
let loadNightSkyCatalog = (): Promise<NightSkyCatalog> => import("./night-sky-catalog.json").then((module) => module.default as NightSkyCatalog);
/** Test seam: replaces the catalog loader and forgets any loaded catalog. */
export const setNightSkyCatalogLoader = (loader: () => Promise<NightSkyCatalog>): void => { loadNightSkyCatalog = loader; catalog = null; catalogRequest = null; };
const requestCatalog = (map: MapLibreMap) => {
  catalogRequest ??= loadNightSkyCatalog().then((loaded) => { catalog = loaded; return loaded; }, () => { catalogRequest = null; return null; });
  void catalogRequest.then((loaded) => { if (loaded) { try { map.triggerRepaint(); } catch { /* map removed */ } } });
};

// One twinkle clock for the page; null holds the stars still (reduced
// motion, ambient motion off, Battery saver or a hidden tab).
let twinkleStartedAt: number | null = null;
export const setNightSkyTwinkle = (active: boolean): void => {
  twinkleStartedAt = active ? (twinkleStartedAt ?? performance.now()) : null;
};
const twinkleClock = (): number | null => twinkleStartedAt === null ? null : (performance.now() - twinkleStartedAt) / 1000;

const skyDarkness = new WeakMap<object, number>();

/**
 * Adds (or removes) the night sky beneath every other layer, records how
 * dark this view's sky is, and sets visibility for the current camera.
 * Safe to call on every style load and light change.
 */
export function syncNightSky(map: MapLibreMap, light: SceneLightPreset, azimuth: number, efficient: boolean): boolean {
  if (!sceneEffectsFor(map).stars) {
    if (map.getLayer(NIGHT_SKY_LAYER_ID)) map.removeLayer(NIGHT_SKY_LAYER_ID);
    return true;
  }
  skyDarkness.set(map, SKY_DARKNESS[effectiveSceneLight(map, light, azimuth).preset]);
  // Decorative: a GPU or shader failure removes the sky and never degrades the map.
  try {
    if (!map.getLayer(NIGHT_SKY_LAYER_ID)) {
      const order = typeof map.getLayersOrder === "function" ? map.getLayersOrder() : (map.getStyle().layers ?? []).map((layer) => layer.id);
      map.addLayer(createNightSkyLayer({
        id: NIGHT_SKY_LAYER_ID,
        catalog: () => catalog,
        darkness: () => skyDarkness.get(map) ?? 0,
        clock: twinkleClock,
      }), order.find((id) => id !== NIGHT_SKY_LAYER_ID));
      map.setLayoutProperty(NIGHT_SKY_LAYER_ID, "visibility", "none");
    }
    syncNightSkyVisibility(map, efficient);
    return true;
  } catch {
    try { if (map.getLayer(NIGHT_SKY_LAYER_ID)) map.removeLayer(NIGHT_SKY_LAYER_ID); } catch { /* already gone */ }
    return false;
  }
}

export function syncNightSkyVisibility(map: MapLibreMap, efficient: boolean): void {
  if (!map.getLayer(NIGHT_SKY_LAYER_ID)) return;
  const visible = nightSkyShouldShow(sceneEffectsFor(map).stars, efficient, projectionOf(map), map.getPitch(), skyDarkness.get(map) ?? 0);
  if (visible && !catalog) requestCatalog(map);
  setVisibility(map, NIGHT_SKY_LAYER_ID, visible);
}

export const nightSkyIsVisible = (map: MapLibreMap): boolean =>
  Boolean(map.getLayer(NIGHT_SKY_LAYER_ID)) && map.getLayoutProperty(NIGHT_SKY_LAYER_ID, "visibility") === "visible";

/** Stars twinkle only through air: on a tilted map, not from orbit. */
export const nightSkyIsTwinkling = (map: MapLibreMap): boolean => nightSkyIsVisible(map) && projectionOf(map) !== "globe";

/** IDs of every overlay this module may add, for tests and composition. */
export const SCENE_OVERLAY_LAYER_IDS: readonly string[] = [...KANSAS_GLOW_LAYER_IDS, RELIEF_2D_LAYER_ID, COLUMNS_LAYER_ID, NIGHT_SKY_LAYER_ID];
