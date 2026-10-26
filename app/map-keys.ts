import type { ExpressionSpecification } from "./maplibre-seam";

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

/** Linear interpolation through [x, y] stops, clamped at the ends, as MapLibre's "interpolate" does. */
const along = (stops: readonly (readonly [number, number])[], x: number): number => {
  if (x <= stops[0][0]) return stops[0][1];
  for (let i = 1; i < stops.length; i++) {
    const [x1, y1] = stops[i], [x0, y0] = stops[i - 1];
    if (x <= x1) return y0 + (y1 - y0) * (x - x0) / (x1 - x0);
  }
  return stops[stops.length - 1][1];
};

export type MapKeyItem = Readonly<{ label: string; color: string; shape: "dot" | "area" | "line"; size?: number; dashed?: boolean }>;
/** Keys that share a group are shown as one, under the group's title and note. */
export type MapKey = Readonly<{ id: string; title: string; items: readonly MapKeyItem[]; note: string; group?: Readonly<{ id: string; title: string; note: string }> }>;

const KDOT_NETWORK = Object.freeze({ id: "kdot-network", title: "KDOT roads and rail",
  note: "Drawn by KDOT's service: roads from zoom 9, railroads from zoom 8. One line weight for every road; it is not road class or width." });
const HISTORIC_LINES = Object.freeze({ id: "kdot-historic", title: "1918 roads and former rail",
  note: "The 1918 State Highway Commission map as KDOT digitized it, and lines KDOT designates abandoned. Today's railroads are the inked lines with ties." });

/** Keys for the starter layers whose symbols encode a value, by source id. */
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
  "nws-alerts": Object.freeze({
    id: "nws-alerts", title: "NWS alert severity",
    items: Object.freeze([...NWS_SEVERITY_COLORS.map(([label, color]) => Object.freeze({ label, color, shape: "area" as const })),
      Object.freeze({ label: "Unknown", color: NWS_SEVERITY_UNKNOWN_COLOR, shape: "area" as const })]),
    note: "Each area takes its alert's CAP severity; select one for its event, urgency and expiry.",
  }),
  ...Object.fromEntries((Object.keys(KDOT_LINE_SYMBOLS) as KdotLineId[]).map(id => {
    const { color, dashed, label } = KDOT_LINE_SYMBOLS[id];
    const historic = id === "kdot-roads-1918" || id === "kdot-rail-abandoned";
    return [id, Object.freeze({ id, title: label, items: Object.freeze([Object.freeze({ label, color, dashed, shape: "line" as const })]), note: "",
      group: historic ? HISTORIC_LINES : KDOT_NETWORK })];
  })),
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
