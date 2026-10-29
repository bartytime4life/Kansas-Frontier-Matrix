import type { ExpressionSpecification } from "./maplibre-seam";

// Categorical district identity only; colors never encode a party or result.
export const CIVIC_COLORS = Object.freeze([[1, "#397f7a"], [2, "#a77530"], [3, "#7762a5"], [4, "#bf7161"], [5, "#617b43"], [6, "#44638c"], [7, "#98638c"], [8, "#78664f"], [0, "#4b5666"]] as const);
export const civicDistrictColor = (): ExpressionSpecification => ["match", ["get", "district"], ...CIVIC_COLORS.flat(), "#777777"] as unknown as ExpressionSpecification;

/**
 * Map keys: how the starter data layers encode their values, defined once so
 * the layer styles and the keys shown beside the map cannot drift apart.
 */

/**
 * NWS alert severity (CAP), as one ordinal palette for every alert drawing,
 * live or reviewed: pale yellow for Minor to magenta for Extreme (the Storm
 * Prediction Center's colour for its highest risk), each step more salient on
 * the dark storm base as on the light ones. An alert without a recognised
 * severity is neutral grey, so it never reads as part of the scale.
 */
export const NWS_SEVERITY_COLORS = Object.freeze([["Extreme", "#c2188f"], ["Severe", "#e4572e"], ["Moderate", "#f29e4c"], ["Minor", "#f2d27a"]] as const);
export const NWS_SEVERITY_UNKNOWN_COLOR = "#9aa5ad";
export const nwsSeverityColor = (): ExpressionSpecification =>
  ["match", ["get", "severity"], ...NWS_SEVERITY_COLORS.flat(), NWS_SEVERITY_UNKNOWN_COLOR] as unknown as ExpressionSpecification;

/** USGS earthquake magnitude: colour stops, and circle radius stops at zoom 4 and 10. */
export const EARTHQUAKE_MAGNITUDE_COLORS = Object.freeze([[0, "#ffd7a8"], [2, "#f2a65a"], [4, "#ef6b45"], [6, "#d9364f"]] as const);
export const EARTHQUAKE_RADIUS_Z4 = Object.freeze([[0, 3], [3, 7], [6, 12]] as const);
export const EARTHQUAKE_RADIUS_Z10 = Object.freeze([[0, 5], [3, 11], [6, 18]] as const);
const magnitude: ExpressionSpecification = ["coalesce", ["get", "magnitude"], 0];
export const earthquakeColor = (): ExpressionSpecification =>
  ["interpolate", ["linear"], magnitude, ...EARTHQUAKE_MAGNITUDE_COLORS.flat()] as unknown as ExpressionSpecification;
export const earthquakeRadius = (): ExpressionSpecification =>
  ["interpolate", ["linear"], ["zoom"], 4, ["interpolate", ["linear"], magnitude, ...EARTHQUAKE_RADIUS_Z4.flat()], 10, ["interpolate", ["linear"], magnitude, ...EARTHQUAKE_RADIUS_Z10.flat()]] as unknown as ExpressionSpecification;

/**
 * KDOT reference lines, drawn by KDOT's own service with these symbols
 * (esriSLS, 1.5 px). Mid-luminance colours, at least 3:1 against both the
 * light category bases (network, civic, parchment) and the dark ones, so
 * each line reads on its own map. Two datasets never share a colour.
 */
export const KDOT_LINE_SYMBOLS = Object.freeze({
  "kdot-roads": Object.freeze({ color: "#b8730c", dashed: false, label: "Public roads" }),
  "kdot-rail-active": Object.freeze({ color: "#0f8a80", dashed: false, label: "Active railroads" }),
  "kdot-roads-1918": Object.freeze({ color: "#b5432c", dashed: false, label: "1918 state highways" }),
  "kdot-rail-abandoned": Object.freeze({ color: "#7d68b0", dashed: true, label: "Abandoned railroads" }),
} as const);
export type KdotLineId = keyof typeof KDOT_LINE_SYMBOLS;
/** An ArcGIS RGBA colour for a #rrggbb hex. */
export const esriColor = (hex: string): number[] => [1, 3, 5].map(i => parseInt(hex.slice(i, i + 2), 16)).concat(255);

/** VIIRS detection confidence (provider classes), and NIFC incident types. */
export const FIRE_CONFIDENCE_COLORS = Object.freeze({ high: "#ff3757", nominal: "#ff713b", low: "#ffc46c" } as const);
export const FIRE_REPORT_COLORS = Object.freeze([["Wildfire", "#ff4e67"], ["Prescribed fire", "#ffcb6a"], ["Incident complex", "#b9a4ff"]] as const);
export const FIRE_REPORT_OTHER_COLOR = "#ff4e67";

/**
 * Reviewed USGS discharge snapshots: circle radius (px) stops over the square
 * root of discharge (ft³/s), so area grows with discharge from a 3 px floor
 * (radius = 3 + 0.06·√Q) and stops growing at 62,500 ft³/s. The ring says
 * whether the value is provisional or approved.
 */
export const DISCHARGE_RADIUS_STOPS = Object.freeze([[0, 3], [100, 9], [250, 18]] as const);
export const GAUGE_FILL_COLOR = "#3fd0c9";
export const GAUGE_PROVISIONAL_RING = "#f2b84b";
export const GAUGE_APPROVED_RING = "#f4fbfb";
export const dischargeRadius = (): ExpressionSpecification =>
  ["interpolate", ["linear"], ["sqrt", ["max", 0, ["to-number", ["get", "value"], 0]]], ...DISCHARGE_RADIUS_STOPS.flat()] as unknown as ExpressionSpecification;

/** Linear interpolation through [x, y] stops, clamped at the ends, as MapLibre's "interpolate" does. */
const along = (stops: readonly (readonly [number, number])[], x: number): number => {
  if (x <= stops[0][0]) return stops[0][1];
  for (let i = 1; i < stops.length; i++) {
    const [x1, y1] = stops[i], [x0, y0] = stops[i - 1];
    if (x <= x1) return y0 + (y1 - y0) * (x - x0) / (x1 - x0);
  }
  return stops[stops.length - 1][1];
};

export type MapKeyItem = Readonly<{ label: string; color: string; shape: "dot" | "area" | "line" | "ring"; size?: number; dashed?: boolean; stroke?: string }>;
/** A colour ramp drawn as a bar: its CSS gradient and tick labels placed along it (0–100 %). */
export type MapKeyRamp = Readonly<{ css: string; ticks: readonly Readonly<{ label: string; at: number }>[] }>;
/** Keys that share a group are shown as one, under the group's title and note. */
export type MapKey = Readonly<{ id: string; title: string; items: readonly MapKeyItem[]; note: string; group?: Readonly<{ id: string; title: string; note: string }>; ramp?: MapKeyRamp }>;

const KDOT_NETWORK = Object.freeze({ id: "kdot-network", title: "KDOT roads and rail",
  note: "Drawn by KDOT's service: roads from zoom 9, railroads from zoom 8. One line weight for every road; it is not road class or width." });
const HISTORIC_LINES = Object.freeze({ id: "kdot-historic", title: "1918 roads and former rail",
  note: "The 1918 State Highway Commission map as KDOT digitized it, and lines KDOT designates abandoned. Today's railroads are the inked lines with ties." });

/** Keys for the starter layers whose symbols encode a value, by source id. */
/** Only validated constituencies for the selected term receive a historical key. */
export function withCivicKey(keys: readonly MapKey[], districts: readonly number[], congress: number | null): readonly MapKey[] {
  return keys.flatMap(key => key.id !== "census-congress-119" ? [key] : !districts.length || congress === null ? [] : [{ ...key,
    title: `Kansas U.S. House · Congress ${congress}`,
    items: CIVIC_COLORS.filter(([district]) => districts.includes(district)).map(([district, color]) => ({ label: district === 0 ? "Statewide at-large" : `District ${district}`, color, shape: district === 0 ? "line" as const : "area" as const, dashed: district === 0 })),
  }]);
}

export const MAP_KEYS: Readonly<Record<string, MapKey>> = Object.freeze({
  "usgs-earthquakes": Object.freeze({
    id: "usgs-earthquakes", title: "Earthquake magnitude",
    // Drawn at the zoom-4 size, the statewide view's.
    items: Object.freeze(EARTHQUAKE_MAGNITUDE_COLORS.map(([m, color], i) => Object.freeze({
      label: i === EARTHQUAKE_MAGNITUDE_COLORS.length - 1 ? `M ${m}+` : `M ${m}`, color, shape: "dot" as const,
      size: Math.round(2 * along(EARTHQUAKE_RADIUS_Z4, m)),
    }))),
    note: "USGS magnitude: colour and circle size both rise with it. Circles grow as you zoom in.",
  }),
  "census-congress-119": Object.freeze({
    id: "census-congress-119", title: "Kansas U.S. House · districts through time",
    items: Object.freeze(CIVIC_COLORS.slice(0, 4).map(([district, color]) => Object.freeze({ label: district === 0 ? "At-large · dashed outline" : `District ${district}`, color, shape: "area" as const }))),
    note: "Colors identify district numbers, not parties or persistent territory. Only the selected Congress is shown; at-large constituencies may overlap numbered districts.",
  }),
  "deflock-alpr": Object.freeze({
    id: "deflock-alpr", title: "DeFlock · reported ALPR areas",
    items: Object.freeze([{ label: "0.05° report cell", color: "#9b72cf", shape: "area" as const }]),
    note: "Numbers count community reports, not verified devices. Cells are generalized areas, not camera coverage; blank does not mean camera-free.",
  }),
  "nws-alerts": Object.freeze({
    id: "nws-alerts", title: "NWS alert severity",
    items: Object.freeze([...NWS_SEVERITY_COLORS.map(([label, color]) => Object.freeze({ label, color, shape: "area" as const })),
      Object.freeze({ label: "Unknown", color: NWS_SEVERITY_UNKNOWN_COLOR, shape: "area" as const })]),
    note: "Each area takes its alert's CAP severity; select one for its event, urgency and expiry.",
  }),
  "nasa-gibs-fire-points": Object.freeze({
    id: "nasa-gibs-fire-points", title: "Satellite fire detections (VIIRS)",
    items: Object.freeze((["high", "nominal", "low"] as const).map(level => Object.freeze({ label: `${level[0].toUpperCase()}${level.slice(1)} confidence`, color: FIRE_CONFIDENCE_COLORS[level], shape: "dot" as const, size: 10 }))),
    note: "Each dot is a 375 m detection pixel's centre; zoom in for the dashed scan × track pixel. A heat source, not a perimeter or a confirmed wildfire.",
  }),
  "nifc-fire-reports": Object.freeze({
    id: "nifc-fire-reports", title: "Reported fire incidents (NIFC)",
    items: Object.freeze(FIRE_REPORT_COLORS.map(([label, color]) => Object.freeze({ label, color, shape: "ring" as const }))),
    note: "The incident's reported location, not its extent; size, containment and cause are in the record.",
  }),
  ...Object.fromEntries((Object.keys(KDOT_LINE_SYMBOLS) as KdotLineId[]).map(id => {
    const { color, dashed, label } = KDOT_LINE_SYMBOLS[id];
    const historic = id === "kdot-roads-1918" || id === "kdot-rail-abandoned";
    return [id, Object.freeze({ id, title: label, items: Object.freeze([Object.freeze({ label, color, dashed, shape: "line" as const })]), note: "",
      group: historic ? HISTORIC_LINES : KDOT_NETWORK })];
  })),
});

/** The key for reviewed discharge snapshots, drawn at the sizes the gauges take. */
export const REVIEWED_DISCHARGE_KEY: MapKey = Object.freeze({
  id: "reviewed-discharge", title: "Reviewed discharge (USGS, ft³/s)",
  items: Object.freeze([
    ...([100, 1_000, 10_000, 62_500] as const).map((flow, i, all) => Object.freeze({
      label: `${flow.toLocaleString("en-US")}${i === all.length - 1 ? "+" : ""}`, color: GAUGE_FILL_COLOR, shape: "dot" as const,
      size: Math.round(2 * along(DISCHARGE_RADIUS_STOPS, Math.sqrt(flow))), stroke: GAUGE_APPROVED_RING })),
    Object.freeze({ label: "Provisional", color: GAUGE_FILL_COLOR, shape: "dot" as const, size: 12, stroke: GAUGE_PROVISIONAL_RING }),
    Object.freeze({ label: "Approved", color: GAUGE_FILL_COLOR, shape: "dot" as const, size: 12, stroke: GAUGE_APPROVED_RING }),
  ]),
  note: "Circle area grows with discharge from a 3 px floor; flows above 62,500 ft³/s draw at the largest size. Amber ring: provisional USGS value; white: approved.",
});
/** Released earthquakes: the live catalog's magnitude colours, with the review ring the gauges use. */
export const REVIEWED_EARTHQUAKE_KEY: MapKey = Object.freeze({
  id: "reviewed-earthquakes", title: "Reviewed earthquakes (USGS)",
  items: Object.freeze([
    ...EARTHQUAKE_MAGNITUDE_COLORS.map(([m, color], i) => Object.freeze({ label: i === EARTHQUAKE_MAGNITUDE_COLORS.length - 1 ? `M ${m}+` : `M ${m}`, color, shape: "dot" as const })),
    Object.freeze({ label: "Automatic solution", color: EARTHQUAKE_MAGNITUDE_COLORS[1][1], shape: "dot" as const, size: 12, stroke: GAUGE_PROVISIONAL_RING }),
    Object.freeze({ label: "Reviewed by USGS", color: EARTHQUAKE_MAGNITUDE_COLORS[1][1], shape: "dot" as const, size: 12, stroke: GAUGE_APPROVED_RING }),
  ]),
  note: "A stored hourly capture of the USGS catalog for the Kansas window, past 30 days. Amber ring: automatic solution that USGS may still revise; white: reviewed by an analyst.",
});

/** The keys for the starter layers a map shows, in the map's own order; keys of one group are merged. */
export const mapKeysFor = (starters: readonly string[], visible: (id: string) => boolean): readonly MapKey[] => {
  const keys: MapKey[] = [];
  for (const id of starters) {
    const key = MAP_KEYS[id];
    if (!key || !visible(id)) continue;
    const group = key.group;
    const shared = group ? keys.findIndex(k => k.id === group.id) : -1;
    if (group && shared >= 0) keys[shared] = { ...keys[shared], items: [...keys[shared].items, ...key.items] };
    else keys.push(group ? { id: group.id, title: group.title, note: group.note, items: key.items } : key);
  }
  return keys;
};

/** A map's keys with the key for a drawn reviewed snapshot added, once (alerts share the live key). */
export const withReviewedKey = (keys: readonly MapKey[], reviewedSourceId: string | null): readonly MapKey[] => {
  const key = reviewedSourceId === "usgs-streamflow" ? REVIEWED_DISCHARGE_KEY : reviewedSourceId === "nws-alerts" ? MAP_KEYS["nws-alerts"]
    : reviewedSourceId === "usgs-earthquakes" ? REVIEWED_EARTHQUAKE_KEY : reviewedSourceId === "newberry-county-history" ? { id: "newberry-county-history", title: "Historical source areas", items: [{ label: "County and predecessor outlines", color: "#927347", shape: "area" as const }], note: "Newberry reconstruction for one exact day. Names and source labels do not establish legal or sovereignty authority." } : null;
  return key && !keys.some(k => k.id === key.id) ? [...keys, key] : keys;
};

// ---------------------------------------------------------------------------
// Elevation keys for the basemaps that colour the ground by height. The ramps
// stay with the styles (category-basemaps.ts); these draw them as a bar.
// ---------------------------------------------------------------------------

export const FEET_PER_METRE = 3.28084;
type Stops = readonly (readonly [number, string])[];
const percent = (value: number, min: number, max: number) => Math.round((value - min) / (max - min) * 1000) / 10;
/** A CSS gradient over [min, max]: interpolated like MapLibre's "interpolate", or hard bands from each stop to the next. */
export const rampGradient = (stops: Stops, min: number, max: number, stepped: boolean): string => {
  const parts = stepped
    ? stops.map(([value, color], i) => `${color} ${percent(value, min, max)}% ${percent(stops[i + 1]?.[0] ?? max + (max - min), min, max)}%`)
    : stops.map(([value, color]) => `${color} ${percent(value, min, max)}%`);
  return `linear-gradient(to right, ${parts.join(", ")})`;
};
const ticks = (values: readonly number[], min: number, max: number) =>
  Object.freeze(values.map(value => Object.freeze({ label: value.toLocaleString("en-US"), at: percent(value, min, max) })));

/** Kansas spans 207 m (679 ft) where the Verdigris River leaves the state to 1,231 m (4,039 ft) at Mount Sunflower. */
export const KANSAS_ELEVATION_M = Object.freeze({ low: 207, high: 1231 });

/** The relief basemap's continuous elevation ramp, in metres. */
export const reliefElevationKey = (ramp: Stops): MapKey => Object.freeze({
  id: "elevation-relief", title: "Elevation (m above sea level)", items: Object.freeze([]),
  ramp: Object.freeze({ css: rampGradient(ramp, 200, 1300, false), ticks: ticks([300, 600, 900, 1200], 200, 1300) }),
  note: `Colour is height alone; shading is the scene's sun. Kansas spans ${KANSAS_ELEVATION_M.low} m, where the Verdigris River leaves the state, to ${KANSAS_ELEVATION_M.high.toLocaleString("en-US")} m at Mount Sunflower.`,
});

/** The aviation chart's 1,000 ft terrain bands, in feet as sectional charts give them. */
export const chartElevationKey = (bands: Stops): MapKey => {
  const feet: Stops = bands.map(([metres, color]) => [Math.round(metres * FEET_PER_METRE / 10) * 10, color] as const);
  return Object.freeze({
    id: "elevation-chart", title: "Terrain elevation (ft)", items: Object.freeze([]),
    ramp: Object.freeze({ css: rampGradient(feet, 500, 4500, true), ticks: ticks([1000, 2000, 3000, 4000], 500, 4500) }),
    note: `Tinted in 1,000 ft bands, as sectional charts tint terrain. Kansas spans about ${Math.round(KANSAS_ELEVATION_M.low * FEET_PER_METRE / 10) * 10} to ${(Math.round(KANSAS_ELEVATION_M.high * FEET_PER_METRE / 10) * 10).toLocaleString("en-US")} ft.`,
  });
};

/** A map's keys with its basemap's elevation key first, when the basemap colours the ground by height. */
export const withElevationKey = (keys: readonly MapKey[], key: MapKey | null): readonly MapKey[] => key ? [key, ...keys] : keys;

/** NWS flood categories as NOAA NWPS reports them at a gauge, in the NWS colours (major purple … no flooding green). */
export type FloodStatus = "major" | "moderate" | "minor" | "action" | "none" | "not_defined" | "low_water" | "not_current" | "out_of_service" | "unknown";
export const FLOOD_STATUS: Readonly<Record<FloodStatus, Readonly<{ label: string; color: string }>>> = Object.freeze({
  major: { label: "Major flooding", color: "#cc33ff" },
  moderate: { label: "Moderate flooding", color: "#ff0000" },
  minor: { label: "Minor flooding", color: "#ff9900" },
  action: { label: "Near flood stage (action)", color: "#ffff00" },
  none: { label: "No flooding", color: "#00ff00" },
  not_defined: { label: "Flood category not defined", color: "#72afe9" },
  low_water: { label: "At or below low-water threshold", color: "#906320" },
  not_current: { label: "Data not current", color: "#bdc2bb" },
  out_of_service: { label: "Out of service", color: "#6b6b6b" },
  unknown: { label: "No category given", color: "#8fb5c2" },
});
