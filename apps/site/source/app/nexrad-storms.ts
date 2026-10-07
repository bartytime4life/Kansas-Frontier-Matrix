import type { Feature, FeatureCollection, LineString, Point } from "geojson";

/**
 * NOAA NEXRAD Level III storm products for the Event Observatory.
 *
 * NCEI's NEXRAD product page directs public users to the NOAA Open Data
 * Dissemination copy of the archive. Only two small text-bearing products are
 * read here: NST (storm tracking, product 58) and NMD (mesocyclone detection,
 * product 141). Each file is roughly 0.1-15 KB. Nothing is stored server-side;
 * results are cached in memory only. Detections are radar algorithm output,
 * never confirmed tornadoes, hail, damage or warnings.
 */
export const NEXRAD_SOURCE_PAGE = "https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar";
export const NEXRAD_L3_BUCKET = "https://unidata-nexrad-level3.s3.amazonaws.com";
export const NEXRAD_EARLIEST_DAY = "2020-01-01";
export const STORM_PRODUCT_BYTES = 256 * 1024;
export const STORM_LIST_BYTES = 2 * 1024 * 1024;
export const STORM_LOOKBACK_MS = 12 * 60_000;
export const STORM_LIMITATION = "Radar algorithm detections from NOAA NEXRAD Level III storm-tracking and mesocyclone products. They are not confirmed tornadoes, hail, damage or warnings. A storm can be missed far from a radar or when the beam is blocked.";

export type StormRadarId = "ICT" | "DDC" | "GLD" | "TWX";
export type StormProduct = "NST" | "NMD";
export type RotationClass = "tornado_signature" | "strong_low" | "strong_aloft" | "weak";
export type StormRadar = Readonly<{ id: StormRadarId; site: string; name: string; lat: number; lon: number; heightFt: number }>;

// Positions reported by each site's own product description block.
export const STORM_RADARS: readonly StormRadar[] = Object.freeze([
  { id: "ICT", site: "KICT", name: "Wichita", lat: 37.654, lon: -97.443, heightFt: 1400 },
  { id: "DDC", site: "KDDC", name: "Dodge City", lat: 37.761, lon: -99.969, heightFt: 2671 },
  { id: "GLD", site: "KGLD", name: "Goodland", lat: 39.367, lon: -101.7, heightFt: 3717 },
  { id: "TWX", site: "KTWX", name: "Topeka", lat: 38.997, lon: -96.232, heightFt: 1415 },
]);
const RADAR_BY_ID = new Map(STORM_RADARS.map((radar) => [radar.id, radar]));
const PRODUCT_CODES: Record<StormProduct, number> = { NST: 58, NMD: 141 };

export const ROTATION_LABELS: Record<RotationClass, string> = {
  tornado_signature: "Tornado vortex signature",
  strong_low: "Strong rotation near the ground",
  strong_aloft: "Strong rotation aloft",
  weak: "Weak rotation",
};
export const ROTATION_COLORS: Record<RotationClass | "none", string> = {
  tornado_signature: "#ff3fa4",
  strong_low: "#ff5a4f",
  strong_aloft: "#ffa53d",
  weak: "#ffe27a",
  none: "#e9f3f6",
};
const ROTATION_ORDER: readonly (RotationClass | "none")[] = ["none", "weak", "strong_aloft", "strong_low", "tornado_signature"];

export type StormMotion = Readonly<{ towardDeg: number; toward: string; speedKt: number; speedMph: number }>;
export type StormCell = Readonly<{
  kind: "cell"; radar: StormRadarId; stormId: string; volumeTime: string;
  position: readonly [number, number]; past: readonly (readonly [number, number])[]; forecast: readonly (readonly [number, number])[];
  rangeKm: number; motion: StormMotion | null; newCell: boolean;
}>;
export type StormRotation = Readonly<{
  kind: "rotation"; radar: StormRadarId; stormId: string | null; volumeTime: string; position: readonly [number, number];
  rangeKm: number; strengthRank: number; lowLevel: boolean; tvs: boolean; rotationClass: RotationClass; baseKft: string; depthKft: string;
}>;
export type StormProductResult = Readonly<{ radar: StormRadarId; product: StormProduct; volumeTime: string; cells: readonly StormCell[]; rotations: readonly StormRotation[] }>;
export type StormListingRow = Readonly<{ key: string; bytes: number; time: string }>;
export type StormRadarStatus = Readonly<{ id: StormRadarId; site: string; name: string; status: "ok" | "no-scan" | "unavailable"; volumeTime: string | null; message: string }>;
export type StormFrame = Readonly<{
  format: "kfm-nexrad-storms-v1"; time: string; retrievedAt: string; radars: readonly StormRadarStatus[];
  data: FeatureCollection; counts: Readonly<{ cells: number; rotations: number; tornadoSignatures: number }>;
  source: string; limitation: string; evidenceRole: "EXTERNAL_CONTEXT_ONLY";
}>;
export type StormAvailability = Readonly<{ format: "kfm-nexrad-storm-availability-v1"; start: string; end: string; radars: readonly Readonly<{ id: StormRadarId; times: readonly string[]; status: "ok" | "unavailable" }>[] }>;

const KEY = /^(ICT|DDC|GLD|TWX)_(NST|NMD)_(\d{4})_(\d{2})_(\d{2})_(\d{2})_(\d{2})_(\d{2})$/;
const COMPASS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"];
export const compass16 = (degrees: number) => COMPASS[Math.round(((degrees % 360) + 360) % 360 / 22.5) % 16];

export function stormRadar(id: string): StormRadar | null { return RADAR_BY_ID.get(id as StormRadarId) ?? null; }

/** Exact UTC volume time encoded by an allowed object key, or null. */
export function stormKeyTime(key: string): string | null {
  const match = KEY.exec(key);
  if (!match) return null;
  const [, , , y, mo, d, h, mi, s] = match;
  const iso = `${y}-${mo}-${d}T${h}:${mi}:${s}.000Z`;
  const ms = Date.parse(iso);
  return Number.isFinite(ms) && new Date(ms).toISOString() === iso ? iso : null;
}

export function stormObjectUrl(key: string): string {
  if (!stormKeyTime(key)) throw new Error("Storm product key is not allowed.");
  return `${NEXRAD_L3_BUCKET}/${key}`;
}

export function stormListUrl(radar: StormRadarId, product: StormProduct, day: string): string {
  if (!RADAR_BY_ID.has(radar) || !(product in PRODUCT_CODES) || !/^\d{4}-\d{2}-\d{2}$/.test(day)) throw new Error("Storm listing scope is not allowed.");
  const query = new URLSearchParams({ "list-type": "2", prefix: `${radar}_${product}_${day.replaceAll("-", "_")}_`, "max-keys": "1000" });
  return `${NEXRAD_L3_BUCKET}/?${query}`;
}

/** Parse one complete S3 listing page; every key must belong to the request. */
export function parseStormListing(xml: string, radar: StormRadarId, product: StormProduct, day: string): StormListingRow[] {
  if (/<!DOCTYPE|<!ENTITY/i.test(xml) || !xml.includes("<ListBucketResult")) throw new Error("Unrecognized radar archive listing.");
  if (!/<IsTruncated>false<\/IsTruncated>/.test(xml)) throw new Error("Radar archive listing was incomplete.");
  const rows: StormListingRow[] = [];
  for (const block of xml.matchAll(/<Contents>([\s\S]*?)<\/Contents>/g)) {
    const key = block[1].match(/<Key>([^<]{1,64})<\/Key>/)?.[1] ?? "";
    const bytes = Number(block[1].match(/<Size>(\d{1,9})<\/Size>/)?.[1] ?? NaN);
    const time = stormKeyTime(key);
    if (!time || !key.startsWith(`${radar}_${product}_`) || time.slice(0, 10) !== day) throw new Error("Radar archive listing contained an unexpected key.");
    if (!Number.isInteger(bytes) || bytes < 1 || bytes > STORM_PRODUCT_BYTES) throw new Error("Radar product exceeded its size budget.");
    rows.push({ key, bytes, time });
  }
  if (rows.length > 1000) throw new Error("Radar archive listing exceeded its budget.");
  return rows.sort((a, b) => a.time.localeCompare(b.time));
}

/** Latest volume at or before the cursor and no older than the lookback. */
export function latestStormVolume(rows: readonly StormListingRow[], cursor: string, lookbackMs = STORM_LOOKBACK_MS): StormListingRow | null {
  const at = Date.parse(cursor);
  let best: StormListingRow | null = null;
  for (const row of rows) {
    const time = Date.parse(row.time);
    if (time <= at && at - time <= lookbackMs && (!best || time > Date.parse(best.time))) best = row;
  }
  return best;
}

const EARTH_KM = 6371.0088;
export function destination(lat: number, lon: number, azimuthDeg: number, distanceKm: number): [number, number] {
  const rad = Math.PI / 180, phi = lat * rad, lam = lon * rad, theta = azimuthDeg * rad, delta = distanceKm / EARTH_KM;
  const phi2 = Math.asin(Math.sin(phi) * Math.cos(delta) + Math.cos(phi) * Math.sin(delta) * Math.cos(theta));
  const lam2 = lam + Math.atan2(Math.sin(theta) * Math.sin(delta) * Math.cos(phi), Math.cos(delta) - Math.sin(phi) * Math.sin(phi2));
  return [Math.round(lam2 / rad * 1000) / 1000, Math.round(phi2 / rad * 1000) / 1000];
}
export function distanceKm(a: readonly [number, number], b: readonly [number, number]): number {
  const rad = Math.PI / 180, dLat = (b[1] - a[1]) * rad, dLon = (b[0] - a[0]) * rad;
  const h = Math.sin(dLat / 2) ** 2 + Math.cos(a[1] * rad) * Math.cos(b[1] * rad) * Math.sin(dLon / 2) ** 2;
  return 2 * EARTH_KM * Math.asin(Math.min(1, Math.sqrt(h)));
}
const ijPoint = (radar: StormRadar, i: number, j: number) => {
  const east = i / 4, north = j / 4;
  return destination(radar.lat, radar.lon, (Math.atan2(east, north) * 180 / Math.PI + 360) % 360, Math.hypot(east, north));
};
const motion = (fromDeg: number, knots: number): StormMotion => {
  const towardDeg = (fromDeg + 180) % 360;
  return { towardDeg, toward: compass16(towardDeg), speedKt: knots, speedMph: Math.round(knots * 1.15078) };
};
export function rotationClass(rank: number, lowLevel: boolean, tvs: boolean): RotationClass {
  if (tvs) return "tornado_signature";
  if (rank >= 5) return lowLevel ? "strong_low" : "strong_aloft";
  return "weak";
}

function tabularLines(view: DataView, bytes: Uint8Array, offsetHalfwords: number): string[] {
  const start = offsetHalfwords * 2;
  if (start <= 0 || start + 132 > bytes.length || view.getInt16(start) !== -1 || view.getInt16(start + 2) !== 3) throw new Error("Storm product text block is invalid.");
  const end = start + view.getInt32(start + 4);
  if (end > bytes.length || end < start + 132) throw new Error("Storm product text block is invalid.");
  let position = start + 128;
  if (view.getInt16(position) !== -1) throw new Error("Storm product text block is invalid.");
  const pages = view.getInt16(position + 2);
  if (pages < 0 || pages > 64) throw new Error("Storm product text block is invalid.");
  position += 4;
  const lines: string[] = [], decoder = new TextDecoder("ascii");
  for (let page = 0; page < pages; page++) {
    for (;;) {
      if (position + 2 > end) throw new Error("Storm product text block is invalid.");
      const size = view.getInt16(position); position += 2;
      if (size === -1) break;
      if (size < 0 || size > 80 || position + size > end) throw new Error("Storm product text block is invalid.");
      lines.push(decoder.decode(bytes.subarray(position, position + size))); position += size;
    }
  }
  return lines;
}

const PACKETS = new Set([1, 2, 3, 4, 6, 8, 11, 12, 15, 19, 20, 23, 24, 25, 26]);
type Shape = { current: [number, number]; past: [number, number][]; forecast: [number, number][] };
function stormGeometry(view: DataView, bytes: Uint8Array, offsetHalfwords: number, radar: StormRadar): Map<string, Shape> {
  const start = offsetHalfwords * 2;
  if (start <= 0 || start + 10 > bytes.length || view.getInt16(start) !== -1 || view.getInt16(start + 2) !== 1) throw new Error("Storm product graphic block is invalid.");
  const end = start + view.getInt32(start + 4), layers = view.getInt16(start + 8);
  if (end > bytes.length || layers < 0 || layers > 18) throw new Error("Storm product graphic block is invalid.");
  const storms = new Map<string, Shape>();
  let current: Shape | null = null, position = start + 10;
  const nestedPoints = (from: number, to: number) => {
    const points: [number, number][] = [];
    for (let at = from; at < to;) {
      const code = view.getInt16(at), length = view.getInt16(at + 2);
      if (!PACKETS.has(code) || code === 23 || code === 24 || length < 0 || at + 4 + length > to) throw new Error("Storm product graphic block is invalid.");
      if (code === 2 && length >= 4) points.push(ijPoint(radar, view.getInt16(at + 4), view.getInt16(at + 6)));
      at += 4 + length;
    }
    return points;
  };
  for (let layer = 0; layer < layers; layer++) {
    if (position + 6 > end || view.getInt16(position) !== -1) throw new Error("Storm product graphic block is invalid.");
    const layerEnd = position + 6 + view.getInt32(position + 2);
    if (layerEnd > end) throw new Error("Storm product graphic block is invalid.");
    for (let at = position + 6; at < layerEnd;) {
      if (at + 4 > layerEnd) throw new Error("Storm product graphic block is invalid.");
      const code = view.getInt16(at), length = view.getInt16(at + 2);
      if (!PACKETS.has(code) || length < 0 || at + 4 + length > layerEnd) throw new Error("Storm product graphic block is invalid.");
      if (code === 15) {
        if (length !== 6) throw new Error("Storm product graphic block is invalid.");
        const id = String.fromCharCode(bytes[at + 8], bytes[at + 9]);
        if (!/^[A-Z][0-9]$/.test(id)) throw new Error("Storm identifier is invalid.");
        current = storms.get(id) ?? { current: ijPoint(radar, view.getInt16(at + 4), view.getInt16(at + 6)), past: [], forecast: [] };
        storms.set(id, current);
      } else if ((code === 23 || code === 24) && current) {
        current[code === 23 ? "past" : "forecast"].push(...nestedPoints(at + 4, at + 4 + length));
      }
      at += 4 + length;
    }
    position = layerEnd;
  }
  return storms;
}

const STORM_ROW = /^\s+([A-Z][0-9])\s+(\d{1,3})\/\s*(\d{1,3})\s+(?:(\d{1,3})\/\s*(\d{1,3})|NEW)\s+.*?\d+\.\d\/\s*\d+\.\d\s*$/;
const MESO_ROW = /^\s*(\d{1,4})\s+(\d{1,3})\/\s*(\d{1,3})\s+(\d{1,2})(L?)\s+(?:([A-Z][0-9])\s+)?\d{1,3}\s+\d{1,3}\s+([<>]?\s*\d{1,2})\s+([<>]?\s*\d{1,2})\s+\d{1,3}\s+\d{1,2}\s+\d{1,3}\s+([YN])\s+(?:(\d{1,3})\/\s*(\d{1,3})\s+)?\d{1,6}\s*$/;
const NM_KM = 1.852;

/** Decode one exact NST or NMD file. Identity, size, length and time must agree. */
export function parseStormProduct(raw: Uint8Array, key: string): StormProductResult {
  const time = stormKeyTime(key), match = KEY.exec(key);
  if (!time || !match) throw new Error("Storm product key is not allowed.");
  const radar = RADAR_BY_ID.get(match[1] as StormRadarId)!, product = match[2] as StormProduct;
  if (raw.length < 1 || raw.length > STORM_PRODUCT_BYTES) throw new Error("Storm product exceeded its size budget.");
  const head = new TextDecoder("latin1").decode(raw.subarray(0, 64));
  const envelope = /^SDUS\d{2} K[A-Z]{3} \d{6}\r\r\n([A-Z0-9]{6})\r\r\n/.exec(head);
  if (!envelope || envelope[1] !== product + radar.id) throw new Error("Storm product envelope does not match its key.");
  const bytes = raw.subarray(envelope[0].length);
  if (bytes.length < 120) throw new Error("Storm product header is incomplete.");
  const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  const code = view.getInt16(0), length = view.getInt32(8), blocks = view.getInt16(16);
  if (code !== PRODUCT_CODES[product] || view.getInt16(30) !== code || length !== bytes.length || view.getInt16(18) !== -1 || blocks < 2 || blocks > 5) throw new Error("Storm product header is invalid.");
  if (Math.abs(view.getInt32(20) / 1000 - radar.lat) > 0.01 || Math.abs(view.getInt32(24) / 1000 - radar.lon) > 0.01 || Math.abs(view.getInt16(28) - radar.heightFt) > 50) throw new Error("Storm product radar location does not match its key.");
  const volumeDays = view.getInt16(40), volumeSeconds = view.getInt32(42);
  if (volumeDays < 1 || volumeSeconds < 0 || volumeSeconds >= 86_400) throw new Error("Storm product time is invalid.");
  const volumeTime = new Date((volumeDays - 1) * 86_400_000 + volumeSeconds * 1000).toISOString();
  if (volumeTime !== time) throw new Error("Storm product time does not match its key.");
  const symbology = view.getInt32(108), tabular = view.getInt32(116);
  const lines = tabular ? tabularLines(view, bytes, tabular) : [];
  const cells: StormCell[] = [], rotations: StormRotation[] = [];
  if (product === "NST") {
    const shapes = symbology ? stormGeometry(view, bytes, symbology, radar) : new Map<string, Shape>();
    const rows = new Map<string, RegExpExecArray>();
    for (const line of lines) { const row = STORM_ROW.exec(line); if (row && !rows.has(row[1])) rows.set(row[1], row); }
    const declared = /NUMBER OF STORM CELLS\s+(\d+)/.exec(lines.join("\n"));
    const ids = [...new Set([...shapes.keys(), ...rows.keys()])].sort();
    if (declared && Number(declared[1]) !== ids.length) throw new Error("Storm table is incomplete.");
    for (const stormId of ids) {
      const row = rows.get(stormId), shape = shapes.get(stormId);
      const position = shape?.current ?? destination(radar.lat, radar.lon, Number(row![2]), Number(row![3]) * NM_KM);
      cells.push({ kind: "cell", radar: radar.id, stormId, volumeTime, position, past: shape?.past ?? [], forecast: shape?.forecast ?? [],
        rangeKm: distanceKm([radar.lon, radar.lat], position), motion: row?.[4] ? motion(Number(row[4]), Number(row[5])) : null, newCell: Boolean(row) && !row![4] });
    }
  } else {
    const candidates = lines.filter((line) => /^\s*\d{1,4}\s+\d{1,3}\//.test(line));
    for (const line of candidates) {
      const row = MESO_ROW.exec(line);
      if (!row) throw new Error("Rotation table row is not recognized.");
      const rank = Number(row[4]), lowLevel = row[5] === "L", tvs = row[9] === "Y";
      const position = destination(radar.lat, radar.lon, Number(row[2]), Number(row[3]) * NM_KM);
      rotations.push({ kind: "rotation", radar: radar.id, stormId: row[6] ?? null, volumeTime, position, rangeKm: Number(row[3]) * NM_KM,
        strengthRank: rank, lowLevel, tvs, rotationClass: rotationClass(rank, lowLevel, tvs), baseKft: row[7].replace(/\s/g, ""), depthKft: row[8].replace(/\s/g, "") });
    }
  }
  return { radar: radar.id, product, volumeTime, cells, rotations };
}

const worst = (a: RotationClass | "none", b: RotationClass | "none") => ROTATION_ORDER.indexOf(b) > ROTATION_ORDER.indexOf(a) ? b : a;

/**
 * Build one display frame. Neighboring radars often track the same storm;
 * the detection closest to its radar (best beam resolution) is kept and the
 * others are listed as "also seen by" rather than drawn twice.
 */
export function stormFeatures(products: readonly StormProductResult[], cursor: string): FeatureCollection {
  const cursorMs = Date.parse(cursor);
  const cells = products.flatMap((product) => product.cells).sort((a, b) => a.rangeKm - b.rangeKm);
  const rotations = products.flatMap((product) => product.rotations).sort((a, b) => a.rangeKm - b.rangeKm);
  const rotationByStorm = new Map<string, RotationClass | "none">();
  for (const rotation of rotations) if (rotation.stormId) {
    const key = `${rotation.radar}:${rotation.stormId}`;
    rotationByStorm.set(key, worst(rotationByStorm.get(key) ?? "none", rotation.rotationClass));
  }
  const keptCells: { cell: StormCell; alsoSeenBy: Set<string>; rotation: RotationClass | "none" }[] = [];
  for (const cell of cells) {
    const twin = keptCells.find((kept) => kept.cell.radar !== cell.radar && distanceKm(kept.cell.position, cell.position) < 10);
    const rotation = rotationByStorm.get(`${cell.radar}:${cell.stormId}`) ?? "none";
    if (twin) { twin.alsoSeenBy.add(stormRadar(cell.radar)!.name); twin.rotation = worst(twin.rotation, rotation); continue; }
    keptCells.push({ cell, alsoSeenBy: new Set(), rotation });
  }
  const keptRotations: StormRotation[] = [];
  for (const rotation of rotations) if (!keptRotations.some((kept) => kept.radar !== rotation.radar && distanceKm(kept.position, rotation.position) < 6)) keptRotations.push(rotation);
  const features: Feature[] = [];
  const ageMinutes = (volumeTime: string) => Math.max(0, Math.round((cursorMs - Date.parse(volumeTime)) / 60_000));
  for (const { cell, alsoSeenBy, rotation } of keptCells) {
    const radar = stormRadar(cell.radar)!;
    const base = { radar: radar.site, radarName: radar.name, stormId: cell.stormId, volumeTime: cell.volumeTime };
    if (cell.past.length) features.push({ type: "Feature", geometry: { type: "LineString", coordinates: [cell.position, ...cell.past].map((p) => [...p]) } as LineString, properties: { ...base, kind: "past" } });
    if (cell.forecast.length) features.push({ type: "Feature", geometry: { type: "LineString", coordinates: [cell.position, ...cell.forecast].map((p) => [...p]) } as LineString, properties: { ...base, kind: "forecast" } });
    features.push({ type: "Feature", geometry: { type: "Point", coordinates: [...cell.position] } as Point, properties: {
      ...base, kind: "cell", ageMinutes: ageMinutes(cell.volumeTime), rotation, rotationColor: ROTATION_COLORS[rotation],
      rotationLabel: rotation === "none" ? "No rotation detected" : ROTATION_LABELS[rotation],
      toward: cell.motion?.toward ?? null, towardDeg: cell.motion?.towardDeg ?? null, speedMph: cell.motion?.speedMph ?? null,
      newCell: cell.newCell, alsoSeenBy: [...alsoSeenBy].join(", "), distanceFromRadarMiles: Math.round(cell.rangeKm / 1.609),
    } });
  }
  for (const rotation of keptRotations) {
    const radar = stormRadar(rotation.radar)!;
    features.push({ type: "Feature", geometry: { type: "Point", coordinates: [...rotation.position] } as Point, properties: {
      kind: "rotation", radar: radar.site, radarName: radar.name, stormId: rotation.stormId, volumeTime: rotation.volumeTime,
      ageMinutes: ageMinutes(rotation.volumeTime), rotation: rotation.rotationClass, rotationColor: ROTATION_COLORS[rotation.rotationClass],
      rotationLabel: ROTATION_LABELS[rotation.rotationClass], strengthRank: rotation.strengthRank, tvs: rotation.tvs,
      baseKft: rotation.baseKft, depthKft: rotation.depthKft, distanceFromRadarMiles: Math.round(rotation.rangeKm / 1.609),
    } });
  }
  return { type: "FeatureCollection", features };
}

export function stormRadarSites(): FeatureCollection {
  return { type: "FeatureCollection", features: STORM_RADARS.map((radar) => ({ type: "Feature", geometry: { type: "Point", coordinates: [radar.lon, radar.lat] }, properties: { kind: "radar", radar: radar.site, radarName: radar.name } })) };
}

/** One plain-language sentence for a selected storm cell or rotation. */
export function describeStormFeature(properties: Record<string, unknown>): string {
  const radarName = String(properties.radarName ?? "a Kansas"), age = Number(properties.ageMinutes ?? 0);
  const seen = `Seen by the ${radarName} radar${age > 0 ? ` ${age} min before the clock` : " at the clock time"}`;
  const caveat = properties.rotation === "tornado_signature" ? " This is a radar algorithm flag, not a confirmed tornado." : "";
  if (properties.kind === "rotation") return `${String(properties.rotationLabel)} in storm ${properties.stormId ?? "(unassigned)"}. ${seen}. Strength rank ${properties.strengthRank} of 25; base ${properties.baseKft} kft.${caveat}`;
  const motionText = properties.speedMph != null && properties.toward ? `moving ${properties.toward} at about ${properties.speedMph} mph` : properties.newCell ? "newly identified, motion not yet known" : "motion not reported";
  return `Storm ${properties.stormId}, ${motionText}. ${String(properties.rotationLabel ?? "No rotation detected")}. ${seen}${properties.alsoSeenBy ? `; also tracked by ${properties.alsoSeenBy}` : ""}.${caveat}`;
}
