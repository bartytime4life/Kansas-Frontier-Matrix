import type { FeatureCollection, Point } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import type { MapKey } from "./map-keys";
import type { MetarObservation } from "./aviation-weather";

/**
 * Surface observations as a meteorologist plots them: the station model for
 * each Kansas-area METAR, read from the Aviation Weather Center through the
 * site's own METAR route (the last observation per station, under 90 minutes
 * old). Sky cover fills the station circle, the wind barb points into the wind
 * in knots, temperature is upper left and dew point lower left in °F.
 */

export const SURFACE_OBS_API_PATH = "/api/aviation/metar";
export const SURFACE_OBS_REFRESH_MS = 5 * 60 * 1000;
export const SURFACE_OBS_SOURCE = "https://aviationweather.gov/data/metar/";

type Row = Record<string, unknown>;
const isRow = (value: unknown): value is Row => Boolean(value) && typeof value === "object" && !Array.isArray(value);

/** The METAR route's envelope, with records that carry a station, a place and a time. */
export function validSurfaceEnvelope(value: unknown): value is { retrievedAt: string; records: MetarObservation[] } {
  return isRow(value) && typeof value.retrievedAt === "string" && Array.isArray(value.records)
    && value.records.every(r => isRow(r) && typeof r.station === "string" && typeof r.lon === "number" && typeof r.lat === "number" && typeof r.observedAt === "string");
}

export const toF = (c: number) => c * 9 / 5 + 32;
const KT_TO_MPH = 1.150779;
/** Saturation vapour pressure over water, hPa (Magnus form, Alduchov and Eskridge 1996). */
const saturation = (c: number) => 6.1094 * Math.exp(17.625 * c / (c + 243.04));
/** Relative humidity, percent, from temperature and dew point. */
export const relativeHumidity = (tempC: number, dewC: number) => Math.min(100, 100 * saturation(dewC) / saturation(tempC));

/** The NWS heat index, °F (Rothfusz regression with its adjustments), from 80 °F; null below. */
export function heatIndexF(tempF: number, rh: number): number | null {
  if (tempF < 80) return null;
  const simple = 0.5 * (tempF + 61 + (tempF - 68) * 1.2 + rh * 0.094);
  if ((simple + tempF) / 2 < 80) return simple;
  const T = tempF, R = rh;
  let hi = -42.379 + 2.04901523 * T + 10.14333127 * R - 0.22475541 * T * R - 0.00683783 * T * T - 0.05481717 * R * R
    + 0.00122874 * T * T * R + 0.00085282 * T * R * R - 0.00000199 * T * T * R * R;
  if (R < 13 && T >= 80 && T <= 112) hi -= (13 - R) / 4 * Math.sqrt((17 - Math.abs(T - 95)) / 17);
  else if (R > 85 && T >= 80 && T <= 87) hi += (R - 85) / 10 * (87 - T) / 5;
  return hi;
}
/** The NWS (2001) wind chill, °F, at 50 °F or colder with wind over 3 mph; null otherwise. */
export function windChillF(tempF: number, windKt: number): number | null {
  const v = windKt * KT_TO_MPH;
  if (tempF > 50 || v <= 3) return null;
  return 35.74 + 0.6215 * tempF - 35.75 * v ** 0.16 + 0.4275 * tempF * v ** 0.16;
}

export type SkyCover = "clear" | "few" | "scattered" | "broken" | "overcast" | "obscured" | "missing";
const COVER_ORDER: readonly SkyCover[] = ["clear", "few", "scattered", "broken", "overcast", "obscured"];
/** The greatest sky cover reported, in the station circle's terms; vertical visibility (an obscured sky) counts as obscured. */
export function skyCover(record: Pick<MetarObservation, "clouds" | "ceilingCover">): SkyCover {
  const covers = record.clouds.map(layer => ({ CLR: "clear", SKC: "clear", NCD: "clear", NSC: "clear", CAVOK: "clear", FEW: "few", SCT: "scattered", BKN: "broken", OVC: "overcast", OVX: "obscured", VV: "obscured" } as Record<string, SkyCover>)[layer.cover.toUpperCase()])
    .filter((cover): cover is SkyCover => Boolean(cover));
  if (record.ceilingCover === "VV") covers.push("obscured");
  return covers.length ? covers.reduce((a, b) => COVER_ORDER.indexOf(b) > COVER_ORDER.indexOf(a) ? b : a) : "missing";
}

/** Wind speed rounded to the 5 kt the barb can show; under 2.5 kt is calm. */
export const barbKnots = (kt: number) => Math.round(kt / 5) * 5;

/**
 * The icon frame, in image pixels (drawn at pixel ratio 2, so 56 CSS px across).
 * The station sits at its centre, where the map rotates it; the frame leaves
 * room past the staff's tip for the outermost feather and its stroke.
 */
export const ICON_SIZE = 112;
export const ICON_STROKE = 3;
const C = ICON_SIZE / 2, RING = 7, STAFF = 40, FEATHER = 16, SPACING = 6.2, ANGLE = 65 * Math.PI / 180;
export type Shapes = Readonly<{ lines: readonly (readonly [number, number, number, number])[]; triangles: readonly (readonly [number, number, number, number, number, number])[] }>;

/**
 * A wind barb for a north wind (the staff points up, towards where the wind
 * comes from); the map rotates it to the wind's direction. Feathers are on the
 * staff's clockwise side, toward lower pressure in the Northern Hemisphere:
 * pennants of 50 kt from the tip, then full barbs of 10, then a half barb of 5
 * (set in from the tip when it stands alone).
 */
export function barbShapes(knots: number): Shapes {
  const lines: [number, number, number, number][] = [];
  const triangles: [number, number, number, number, number, number][] = [];
  const tip = C - RING - STAFF;
  lines.push([C, C - RING, C, tip]);
  const dx = Math.sin(ANGLE) * FEATHER, dy = -Math.cos(ANGLE) * FEATHER;
  let rest = barbKnots(knots), y = tip;
  while (rest >= 50) { triangles.push([C, y, C + dx, y + dy + SPACING, C, y + SPACING * 1.6]); y += SPACING * 1.6 + 1; rest -= 50; }
  while (rest >= 10) { lines.push([C, y, C + dx, y + dy]); y += SPACING; rest -= 10; }
  if (rest >= 5) {
    if (y === tip) y += SPACING;
    lines.push([C, y, C + dx / 2, y + dy / 2]);
  }
  return { lines, triangles };
}

/** The few canvas calls the icons need; a CanvasRenderingContext2D, or a recorder in tests. */
export type PaintContext = {
  clearRect(x: number, y: number, w: number, h: number): void; beginPath(): void; moveTo(x: number, y: number): void; lineTo(x: number, y: number): void;
  closePath(): void; arc(x: number, y: number, r: number, start: number, end: number): void; stroke(): void; fill(): void;
  lineWidth: number; strokeStyle: string; fillStyle: string; lineCap: string;
};
const INK = "#eef3f6";
/** Paints a barb or a sky-cover circle into the icon frame. */
export function paintStationIcon(ctx: PaintContext, icon: Readonly<{ kind: "barb"; knots: number } | { kind: "sky"; cover: SkyCover }>): void {
  ctx.clearRect(0, 0, ICON_SIZE, ICON_SIZE);
  ctx.strokeStyle = INK; ctx.fillStyle = INK; ctx.lineWidth = ICON_STROKE; ctx.lineCap = "round";
  if (icon.kind === "barb") {
    const shapes = barbShapes(icon.knots);
    for (const [x1, y1, x2, y2] of shapes.lines) { ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke(); }
    for (const [x1, y1, x2, y2, x3, y3] of shapes.triangles) { ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.lineTo(x3, y3); ctx.closePath(); ctx.fill(); }
    return;
  }
  const r = RING - 0.6;
  ctx.beginPath(); ctx.arc(C, C, r, 0, Math.PI * 2); ctx.stroke();
  const fraction = { clear: 0, few: 0.25, scattered: 0.5, broken: 0.75, overcast: 1, obscured: 0, missing: 0 }[icon.cover];
  if (fraction) {
    ctx.beginPath(); ctx.moveTo(C, C); ctx.arc(C, C, r, -Math.PI / 2, -Math.PI / 2 + fraction * Math.PI * 2); ctx.closePath(); ctx.fill();
  }
  if (icon.cover === "obscured" || icon.cover === "missing") {
    // An X for a sky obscured; an M (two strokes and a peak) for a missing report.
    const k = r * 0.6;
    ctx.lineWidth = 2; ctx.beginPath();
    if (icon.cover === "obscured") { ctx.moveTo(C - k, C - k); ctx.lineTo(C + k, C + k); ctx.moveTo(C + k, C - k); ctx.lineTo(C - k, C + k); }
    else { ctx.moveTo(C - k, C + k); ctx.lineTo(C - k, C - k); ctx.lineTo(C, C); ctx.lineTo(C + k, C - k); ctx.lineTo(C + k, C + k); }
    ctx.stroke();
  }
}
export const SKY_ICONS: readonly SkyCover[] = [...COVER_ORDER, "missing"];
/** Barb icons from 5 to 150 kt, in 5 kt steps. */
export const BARB_ICONS: readonly number[] = Array.from({ length: 30 }, (_, i) => (i + 1) * 5);
export const skyIconId = (cover: SkyCover) => `kfm-sfc-sky-${cover}`;
export const barbIconId = (knots: number) => `kfm-sfc-barb-${knots}`;

const round = (value: number) => Math.round(value);
const shortWeather = (wx: string | null) => wx ? wx.split(/\s+/)[0] : "";

/** One point per station with what its plot needs: cover, barb and direction, °F temperature and dew point, weather. */
export function surfaceCollection(records: readonly MetarObservation[]): FeatureCollection<Point> {
  return { type: "FeatureCollection", features: records.map(r => {
    const kt = r.windKt === null ? null : barbKnots(Math.min(r.windKt, 150));
    const barb = kt === null || kt === 0 || r.windVariable || r.windDirDeg === null ? "" : barbIconId(kt);
    return { type: "Feature", id: r.station, geometry: { type: "Point", coordinates: [r.lon, r.lat] }, properties: {
      station: r.station, sky: skyIconId(skyCover(r)), barb, dir: r.windDirDeg ?? 0,
      calm: r.windKt === 0 || (kt === 0 && !r.windVariable), variable: r.windVariable && (r.windKt ?? 0) > 0,
      t: r.tempC === null ? "" : String(round(toF(r.tempC))), td: r.dewpointC === null ? "" : String(round(toF(r.dewpointC))), wx: shortWeather(r.weather),
    } };
  }) };
}

const TIME = new Intl.DateTimeFormat("en-US", { timeZone: "America/Chicago", hour: "numeric", minute: "2-digit", timeZoneName: "short" });
export const centralTime = (iso: string) => TIME.format(Date.parse(iso));
const COMPASS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"];
const compass = (deg: number) => COMPASS[Math.round(deg / 22.5) % 16];
const place = (r: MetarObservation) => r.name ? `${r.station} ${r.name.replace(/,.*$/, "")}` : r.station;
const wind = (r: MetarObservation) => r.windKt === null ? "wind missing" : r.windKt === 0 ? "calm"
  : `${r.windVariable || r.windDirDeg === null ? "variable" : `${compass(r.windDirDeg)} (${r.windDirDeg}°)`} ${r.windKt} kt${r.gustKt ? `, gusts ${r.gustKt}` : ""}`;

/** The statewide line: how many stations and when they observed, the warmest and coolest, and the strongest wind. */
export function surfaceReading(records: readonly MetarObservation[]): string {
  if (!records.length) return "No Kansas-area METARs under 90 minutes old; no conditions are inferred.";
  const times = records.map(r => r.observedAt).sort();
  const withT = records.filter(r => r.tempC !== null);
  const warm = withT.reduce<MetarObservation | null>((a, r) => !a || r.tempC! > a.tempC! ? r : a, null);
  const cool = withT.reduce<MetarObservation | null>((a, r) => !a || r.tempC! < a.tempC! ? r : a, null);
  const windy = records.reduce<MetarObservation | null>((a, r) => Math.max(r.gustKt ?? 0, r.windKt ?? 0) > Math.max(a?.gustKt ?? 0, a?.windKt ?? 0) ? r : a, null);
  const first = centralTime(times[0]), last = centralTime(times[times.length - 1]);
  return `${records.length} station${records.length === 1 ? "" : "s"}, observed ${first === last ? first : `${first}–${last}`}`
    + (warm && cool ? warm === cool ? ` · ${place(warm)} ${round(toF(warm.tempC!))}°F` : ` · warmest ${place(warm)} ${round(toF(warm.tempC!))}°F, coolest ${place(cool)} ${round(toF(cool.tempC!))}°F` : "")
    + (windy && (windy.windKt || windy.gustKt) ? ` · strongest wind ${place(windy)}, ${wind(windy)}` : "");
}

/** One station's observation decoded: temperatures with humidity and the felt temperature, wind, visibility, pressure, sky and weather. */
export function stationDetail(r: MetarObservation): string {
  const parts = [`${place(r)} · ${centralTime(r.observedAt)}`];
  if (r.tempC !== null) {
    const t = toF(r.tempC);
    let line = `${round(t)}°F (${r.tempC.toFixed(0)}°C)`;
    if (r.dewpointC !== null) {
      const rh = relativeHumidity(r.tempC, r.dewpointC);
      line += `, dew point ${round(toF(r.dewpointC))}°F, humidity ${round(rh)}%`;
      const hi = heatIndexF(t, rh);
      if (hi !== null && round(hi) > round(t)) line += `, heat index ${round(hi)}°F`;
    }
    const wc = r.windKt === null ? null : windChillF(t, r.windKt);
    if (wc !== null && round(wc) < round(t)) line += `, wind chill ${round(wc)}°F`;
    parts.push(line);
  }
  parts.push(wind(r));
  if (r.visibilitySm !== null) parts.push(`visibility ${r.visibilityAtLeast ? "at least " : ""}${r.visibilitySm} mi`);
  if (r.altimeterInHg !== null) parts.push(`altimeter ${r.altimeterInHg.toFixed(2)} inHg`);
  const cover = skyCover(r);
  parts.push(r.ceilingFtAgl !== null ? `ceiling ${r.ceilingCover ?? ""} ${r.ceilingFtAgl.toLocaleString("en-US")} ft`.replace("  ", " ") : `sky ${cover === "missing" ? "not reported" : cover}`);
  if (r.weather) parts.push(r.weather);
  return parts.join(" · ");
}

export function surfaceList(records: readonly MetarObservation[]): { id: string; label: string }[] {
  return records.map(r => ({ id: r.station, label: `${place(r)} · ${r.tempC === null ? "–" : round(toF(r.tempC))}/${r.dewpointC === null ? "–" : round(toF(r.dewpointC))}°F · ${wind(r)}` }))
    .sort((a, b) => a.label.localeCompare(b.label));
}

export function surfaceKey(): MapKey {
  return Object.freeze({
    id: "surface-obs",
    title: "Surface observations · METAR station model",
    items: Object.freeze([
      Object.freeze({ label: "Temperature °F (upper left)", color: "#ff7a66", shape: "dot" as const }),
      Object.freeze({ label: "Dew point °F (lower left)", color: "#6fdc84", shape: "dot" as const }),
      Object.freeze({ label: "Sky cover: open clear, quarter few, half scattered, three-quarter broken, filled overcast", color: INK, shape: "ring" as const }),
      Object.freeze({ label: "Wind barb into the wind: half 5 kt, full 10 kt, pennant 50 kt", color: INK, shape: "line" as const }),
    ]),
    note: "Airport observations (METAR), the latest per station and under 90 minutes old. A station describes its own airfield; conditions between stations are not interpolated.",
  });
}

export const SURFACE_OBS_SOURCE_ID = "kfm-surface-obs";
export const SURFACE_SKY_LAYER_ID = "kfm-surface-obs-sky";
export const SURFACE_BARB_LAYER_ID = "kfm-surface-obs-barb";
export const SURFACE_TEXT_LAYER_ID = "kfm-surface-obs-text";
export const SURFACE_SELECTED_LAYER_ID = "kfm-surface-obs-selected";
const LAYERS = [SURFACE_SELECTED_LAYER_ID, SURFACE_TEXT_LAYER_ID, SURFACE_BARB_LAYER_ID, SURFACE_SKY_LAYER_ID];
const shown = new WeakMap<MapLibreMap, FeatureCollection>();

/** Paints one station-model icon into image data; in the browser, on a canvas. */
export type IconPainter = (paint: (ctx: PaintContext) => void) => ImageData | { width: number; height: number; data: Uint8Array | Uint8ClampedArray } | null;
const canvasPainter: IconPainter = paint => {
  if (typeof document === "undefined") return null;
  const canvas = document.createElement("canvas");
  canvas.width = ICON_SIZE; canvas.height = ICON_SIZE;
  const ctx = canvas.getContext("2d");
  if (!ctx) return null;
  paint(ctx as unknown as PaintContext);
  return ctx.getImageData(0, 0, ICON_SIZE, ICON_SIZE);
};

/** The station plots (or nothing, for null) above the radar and alerts, with the picked station ringed. */
export function syncSurfaceObs(map: MapLibreMap, collection: FeatureCollection | null, selected: string | null = null, painter: IconPainter = canvasPainter): void {
  if (!collection) {
    for (const id of LAYERS) if (map.getLayer(id)) map.removeLayer(id);
    if (map.getSource(SURFACE_OBS_SOURCE_ID)) map.removeSource(SURFACE_OBS_SOURCE_ID);
    shown.delete(map);
    return;
  }
  const icons = [...SKY_ICONS.map(cover => [skyIconId(cover), { kind: "sky" as const, cover }] as const), ...BARB_ICONS.map(knots => [barbIconId(knots), { kind: "barb" as const, knots }] as const)];
  for (const [id, icon] of icons) {
    if (map.hasImage(id)) continue;
    const image = painter(ctx => paintStationIcon(ctx, icon));
    if (image) map.addImage(id, image as never, { pixelRatio: 2 });
  }
  const source = map.getSource(SURFACE_OBS_SOURCE_ID) as GeoJSONSource | undefined;
  if (!source) map.addSource(SURFACE_OBS_SOURCE_ID, { type: "geojson", data: collection });
  else if (shown.get(map) !== collection) source.setData(collection);
  shown.set(map, collection);
  if (!map.getLayer(SURFACE_SKY_LAYER_ID)) map.addLayer({ id: SURFACE_SKY_LAYER_ID, type: "symbol", source: SURFACE_OBS_SOURCE_ID,
    layout: { "icon-image": ["get", "sky"] as never, "icon-allow-overlap": true, "icon-ignore-placement": true } });
  if (!map.getLayer(SURFACE_BARB_LAYER_ID)) map.addLayer({ id: SURFACE_BARB_LAYER_ID, type: "symbol", source: SURFACE_OBS_SOURCE_ID, filter: ["!=", ["get", "barb"], ""] as never,
    layout: { "icon-image": ["get", "barb"] as never, "icon-rotate": ["get", "dir"] as never, "icon-rotation-alignment": "map", "icon-allow-overlap": true, "icon-ignore-placement": true } });
  if (!map.getLayer(SURFACE_TEXT_LAYER_ID)) map.addLayer({ id: SURFACE_TEXT_LAYER_ID, type: "symbol", source: SURFACE_OBS_SOURCE_ID,
    layout: {
      "text-field": ["format",
        ["get", "t"], { "text-color": "#ff7a66" }, "\n", {},
        ["case", ["get", "variable"], "VRB ", ["get", "calm"], "CALM ", ""], { "text-color": "#cfe2ea", "font-scale": 0.75 }, ["get", "wx"], { "text-color": "#f2d16b", "font-scale": 0.8 }, "\n", {},
        ["get", "td"], { "text-color": "#6fdc84" }] as never,
      "text-font": ["Noto Sans Bold"], "text-size": 11, "text-anchor": "right", "text-justify": "right", "text-offset": [-1.1, 0] as never, "text-line-height": 1.05,
      "text-allow-overlap": true, "text-ignore-placement": true,
    },
    paint: { "text-halo-color": "#0d1217", "text-halo-width": 1.2 } });
  if (!map.getLayer(SURFACE_SELECTED_LAYER_ID)) map.addLayer({ id: SURFACE_SELECTED_LAYER_ID, type: "circle", source: SURFACE_OBS_SOURCE_ID,
    paint: { "circle-color": "rgba(0,0,0,0)", "circle-radius": 14, "circle-stroke-color": "#f2d16b", "circle-stroke-width": 2 } });
  map.setFilter(SURFACE_SELECTED_LAYER_ID, ["==", ["get", "station"], selected ?? ""] as never);
}
