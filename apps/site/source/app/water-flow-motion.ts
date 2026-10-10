/**
 * Flowing water: data rules and geometry for animating river motion.
 *
 * - Direction comes only from USGS 3DHP reaches that carry the provider's
 *   explicit downstream flag (flowdirection = 1, flow follows digitized
 *   order). Reaches without it never move.
 * - Motion speed is one constant display rate everywhere. It is a direction
 *   cue, not water velocity, and is never scaled by discharge.
 * - Measurements change the look only on the reach a USGS gauge sits on,
 *   fading out a few kilometres either side of the gauge. A measured zero
 *   stills the water there; missing or stale readings add nothing. Values
 *   are never painted onto ungauged reaches.
 */

export const FLOWLINE_SERVICE = "https://3dhp.nationalmap.gov/arcgis/rest/services/usgs_3dhp_all/MapServer/50/query";
export const FLOWLINE_LIMITATION = "USGS 3DHP flowlines that carry the provider's downstream flag (flowdirection = 1). Motion shows mapped channel direction at one display speed; it is not water velocity, wet-channel extent, depth or flood level, and gauge readings are not extended beyond the gauged reach.";
export const FLOWLINE_CELL_DEGREES = 0.25;
/** Grid cells covering Kansas (south-west corners). */
export const FLOWLINE_EXTENT = Object.freeze({ west: -102.25, south: 36.75, east: -94.5, north: 40.25 });
/** Flowlines are fetched and drawn only at and above this zoom. */
export const FLOW_MIN_ZOOM = 10;
export const MAX_FLOW_CELLS = 9;
/** Gauge readings fade out this far along their reach. */
export const GAUGE_REACH_WINDOW_M = 2500;
/** A gauge must sit this close to a mapped reach to style it. */
export const GAUGE_SNAP_M = 250;

export type Coordinate = readonly [number, number];
export type FlowReach = Readonly<{
  id: string;
  sequence: number | null;
  downstream: number | null;
  levelpath: number | null;
  name: string | null;
  featureType: number;
  coordinates: readonly Coordinate[];
}>;
export type FlowlineCellPayload = Readonly<{
  format: "kfm-3dhp-flowlines-v1";
  cell: readonly [number, number];
  state: "ready" | "empty";
  truncated: boolean;
  reaches: readonly FlowReach[];
  source: string;
  retrievedAt: string;
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
  limitation: string;
}>;

const onGrid = (value: number) => Math.abs(value / FLOWLINE_CELL_DEGREES - Math.round(value / FLOWLINE_CELL_DEGREES)) < 1e-9;

/** "west,south" on the 0.25° grid inside Kansas, or null. */
export function parseFlowlineCell(raw: string | null): [number, number] | null {
  if (!raw || !/^-?\d{1,3}(\.\d{1,2})?,-?\d{1,2}(\.\d{1,2})?$/.test(raw)) return null;
  const [west, south] = raw.split(",").map(Number);
  if (!onGrid(west) || !onGrid(south)
    || west < FLOWLINE_EXTENT.west || west + FLOWLINE_CELL_DEGREES > FLOWLINE_EXTENT.east
    || south < FLOWLINE_EXTENT.south || south + FLOWLINE_CELL_DEGREES > FLOWLINE_EXTENT.north) return null;
  return [west, south];
}

export const flowlineCellKey = (cell: readonly [number, number]): string => `${cell[0].toFixed(2)},${cell[1].toFixed(2)}`;

/** Cells near the view centre, nearest first. Nothing below the minimum zoom. */
export function flowCellsForView(
  bounds: Readonly<{ west: number; south: number; east: number; north: number }>,
  center: Coordinate, zoom: number,
): [number, number][] {
  if (!(zoom >= FLOW_MIN_ZOOM) || !center.every(Number.isFinite)) return [];
  // Tilted views reach the horizon; keep to the foreground around the centre.
  const west = Math.max(bounds.west, center[0] - 0.4, FLOWLINE_EXTENT.west);
  const east = Math.min(bounds.east, center[0] + 0.4, FLOWLINE_EXTENT.east);
  const south = Math.max(bounds.south, center[1] - 0.3, FLOWLINE_EXTENT.south);
  const north = Math.min(bounds.north, center[1] + 0.3, FLOWLINE_EXTENT.north);
  if (!(east > west && north > south)) return [];
  const cells: [number, number][] = [];
  const step = FLOWLINE_CELL_DEGREES;
  for (let x = Math.floor(west / step) * step; x < east; x += step) {
    for (let y = Math.floor(south / step) * step; y < north; y += step) {
      const cell: [number, number] = [Math.round(x * 100) / 100, Math.round(y * 100) / 100];
      if (parseFlowlineCell(flowlineCellKey(cell))) cells.push(cell);
    }
  }
  const distance = ([x, y]: [number, number]) => Math.hypot(x + step / 2 - center[0], y + step / 2 - center[1]);
  return cells.sort((a, b) => distance(a) - distance(b)).slice(0, MAX_FLOW_CELLS);
}

const finiteInRange = (value: unknown, minimum: number, maximum: number): value is number =>
  typeof value === "number" && Number.isFinite(value) && value >= minimum && value <= maximum;
const sequenceOrNull = (value: unknown) => value === null || (typeof value === "number" && Number.isSafeInteger(value) && value > 0);

/** Strict client-side check of one cell payload. */
export function parseFlowlinePayload(value: unknown): FlowlineCellPayload {
  if (!value || typeof value !== "object") throw new Error("Flowline cell is invalid.");
  const payload = value as Partial<FlowlineCellPayload>;
  if (payload.format !== "kfm-3dhp-flowlines-v1" || !Array.isArray(payload.cell) || payload.cell.length !== 2
    || !parseFlowlineCell(flowlineCellKey(payload.cell as [number, number]))
    || !["ready", "empty"].includes(String(payload.state)) || typeof payload.truncated !== "boolean"
    || !Array.isArray(payload.reaches) || payload.reaches.length > 400 || (payload.state === "ready") !== (payload.reaches.length > 0)
    || payload.source !== FLOWLINE_SERVICE || typeof payload.retrievedAt !== "string" || !Number.isFinite(Date.parse(payload.retrievedAt))
    || payload.evidenceRole !== "EXTERNAL_CONTEXT_ONLY" || typeof payload.limitation !== "string") throw new Error("Flowline cell is invalid.");
  let vertices = 0;
  for (const reach of payload.reaches) {
    if (!reach || typeof reach.id !== "string" || !/^[A-Za-z0-9]{1,16}$/.test(reach.id)
      || !sequenceOrNull(reach.sequence) || !sequenceOrNull(reach.downstream) || !sequenceOrNull(reach.levelpath)
      || !(reach.name === null || (typeof reach.name === "string" && reach.name.length <= 160))
      || ![1, 4, 5, 6].includes(reach.featureType)
      || !Array.isArray(reach.coordinates) || reach.coordinates.length < 2 || reach.coordinates.length > 10000
      || !reach.coordinates.every((point: unknown) => Array.isArray(point) && point.length === 2
        && finiteInRange(point[0], -102.2, -94.4) && finiteInRange(point[1], 36.8, 40.2))) throw new Error("Flowline cell contains an invalid reach.");
    vertices += reach.coordinates.length;
    if (vertices > 80000) throw new Error("Flowline cell geometry limit exceeded.");
  }
  return payload as FlowlineCellPayload;
}

// ---------------------------------------------------------------------------
// Gauge readings
// ---------------------------------------------------------------------------

export type FlowTint = "direction" | "rising" | "steady" | "falling" | "unknown";
export const FLOW_TINT_INDEX: Readonly<Record<FlowTint, number>> = Object.freeze({ direction: 0, rising: 1, steady: 2, falling: 3, unknown: 4 });

export type GaugeCue = Readonly<{
  coordinate: Coordinate;
  /** 0–1 emphasis; follows the same visual magnitude the 3D columns use. */
  intensity: number;
  /** False only for a measured zero: still water on this reach. */
  moving: boolean;
  tint: Exclude<FlowTint, "direction">;
}>;

/** A cue only for a current measured or zero reading; missing and stale add nothing. */
export function gaugeCue(properties: Record<string, unknown> | null | undefined, coordinate: unknown): GaugeCue | null {
  if (!properties || !Array.isArray(coordinate) || coordinate.length < 2) return null;
  const [lng, lat] = coordinate;
  if (!finiteInRange(lng, -102.2, -94.4) || !finiteInRange(lat, 36.8, 40.2)) return null;
  const value = Number(properties.value);
  if (properties.missing === true || properties.value === null || properties.value === undefined || !Number.isFinite(value) || value < 0) return null;
  if (properties.readingState === "zero" || value === 0) return { coordinate: [lng, lat], intensity: 0.5, moving: false, tint: "unknown" };
  if (properties.readingState !== undefined && properties.readingState !== "measured") return null;
  const visual = Number(properties.visualMagnitude);
  const trend = String(properties.trend);
  return {
    coordinate: [lng, lat],
    intensity: Number.isFinite(visual) ? Math.max(0.35, Math.min(1, visual / 5)) : 0.5,
    moving: true,
    tint: trend === "rising" || trend === "falling" || trend === "steady" ? trend : "unknown",
  };
}

// ---------------------------------------------------------------------------
// Geometry
// ---------------------------------------------------------------------------

const RADIANS = Math.PI / 180;
export function distanceMeters(a: Coordinate, b: Coordinate): number {
  const h = Math.sin((b[1] - a[1]) * RADIANS / 2) ** 2 + Math.cos(a[1] * RADIANS) * Math.cos(b[1] * RADIANS) * Math.sin((b[0] - a[0]) * RADIANS / 2) ** 2;
  return 6371008.8 * 2 * Math.asin(Math.sqrt(Math.min(1, h)));
}
export const mercatorX = (lng: number): number => (180 + lng) / 360;
export const mercatorY = (lat: number): number => (180 - (180 / Math.PI) * Math.log(Math.tan(Math.PI / 4 + (lat * RADIANS) / 2))) / 360;

/** Per segment: A (x, y, z), B (x, y, z), distance at A and B, intensity, motion, tint, phase. */
export const FLOW_SEGMENT_FLOATS = 12;
export const MAX_FLOW_SEGMENTS = 60000;

export type FlowGeometry = Readonly<{
  /** Instance data; z (metres) is filled in later from the rendered terrain. */
  segments: Float32Array;
  count: number;
  /** Unique vertices for terrain sampling, with the segment slots they feed. */
  vertices: readonly Readonly<{ lng: number; lat: number; slots: readonly number[] }>[];
  reaches: number;
  gauged: number;
}>;

/** Snap a gauge to the nearest reach segment within the snap distance. */
export function snapGauge(reaches: readonly FlowReach[], gauge: Coordinate): { reach: number; alongM: number; offsetM: number } | null {
  let best: { reach: number; alongM: number; offsetM: number } | null = null;
  const scale = Math.cos(gauge[1] * RADIANS);
  reaches.forEach((reach, reachIndex) => {
    let along = 0;
    for (let i = 1; i < reach.coordinates.length; i += 1) {
      const a = reach.coordinates[i - 1], b = reach.coordinates[i];
      const length = distanceMeters(a, b);
      const dx = (b[0] - a[0]) * scale, dy = b[1] - a[1];
      const denominator = dx * dx + dy * dy;
      if (denominator > 0) {
        const t = Math.max(0, Math.min(1, ((gauge[0] - a[0]) * scale * dx + (gauge[1] - a[1]) * dy) / denominator));
        const point: Coordinate = [a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])];
        const offsetM = distanceMeters(point, gauge);
        if (offsetM <= GAUGE_SNAP_M && (!best || offsetM < best.offsetM)) best = { reach: reachIndex, alongM: along + t * length, offsetM };
      }
      along += length;
    }
  });
  return best;
}

/** Smooth fade from full at the gauge to nothing at the window edge. */
export const gaugeFalloff = (distanceM: number): number => {
  const x = Math.abs(distanceM) / GAUGE_REACH_WINDOW_M;
  return x >= 1 || !Number.isFinite(x) ? 0 : Math.cos(x * Math.PI / 2) ** 2;
};

/**
 * Builds segment instances in downstream order. Distance along each reach
 * grows downstream, so a pattern moving toward larger distance moves with
 * the provider's mapped flow.
 */
export function buildFlowGeometry(reaches: readonly FlowReach[], gauges: readonly GaugeCue[]): FlowGeometry {
  const unique = [...new Map(reaches.map((reach) => [reach.id, reach])).values()];
  const snapped = new Map<number, { alongM: number; cue: GaugeCue }[]>();
  for (const cue of gauges) {
    const hit = snapGauge(unique, cue.coordinate);
    if (hit) snapped.set(hit.reach, [...(snapped.get(hit.reach) ?? []), { alongM: hit.alongM, cue }]);
  }
  const total = Math.min(MAX_FLOW_SEGMENTS, unique.reduce((sum, reach) => sum + reach.coordinates.length - 1, 0));
  const segments = new Float32Array(total * FLOW_SEGMENT_FLOATS);
  const vertices: { lng: number; lat: number; slots: number[] }[] = [];
  let count = 0;
  for (let reachIndex = 0; reachIndex < unique.length && count < total; reachIndex += 1) {
    const reach = unique[reachIndex];
    const marks = snapped.get(reachIndex) ?? [];
    // A stable per-reach phase keeps neighbouring streams from pulsing in step.
    const phase = [...reach.id].reduce((sum, character) => (sum * 31 + character.charCodeAt(0)) % 1000, 7) / 1000;
    let along = 0;
    let previousVertex = -1;
    for (let i = 0; i < reach.coordinates.length; i += 1) {
      const [lng, lat] = reach.coordinates[i];
      const vertex = vertices.push({ lng, lat, slots: [] }) - 1;
      if (i === 0) { previousVertex = vertex; continue; }
      if (count >= total) break;
      const a = reach.coordinates[i - 1];
      const length = distanceMeters(a, [lng, lat]);
      const middle = along + length / 2;
      let intensity = 0, moving = 1, tint: FlowTint = "direction", strongest = 0;
      for (const mark of marks) {
        const weight = gaugeFalloff(middle - mark.alongM) * mark.cue.intensity;
        if (weight > strongest) {
          strongest = weight; intensity = weight; tint = mark.cue.tint;
          moving = mark.cue.moving ? 1 : 1 - gaugeFalloff(middle - mark.alongM);
        }
      }
      const offset = count * FLOW_SEGMENT_FLOATS;
      segments.set([mercatorX(a[0]), mercatorY(a[1]), 0, mercatorX(lng), mercatorY(lat), 0, along, along + length, intensity, moving, FLOW_TINT_INDEX[tint], phase], offset);
      vertices[previousVertex].slots.push(offset + 2);
      vertices[vertex].slots.push(offset + 5);
      along += length;
      previousVertex = vertex;
      count += 1;
    }
  }
  return { segments, count, vertices, reaches: unique.length, gauged: snapped.size };
}
