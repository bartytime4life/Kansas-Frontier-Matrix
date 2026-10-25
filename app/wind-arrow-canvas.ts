import type { Map as MapLibreMap } from "./maplibre-seam";
import type { WindArrowFrame, WindArrowSample } from "./wind-arrow-data";
import { globeOverviewSizeScale, onVisibleGlobeHemisphere } from "./globe-context";
import { LIGHT_CATEGORY_BASEMAPS } from "./category-basemap-keys";

/** Meteorological directions describe where wind comes from. Flow moves toward
 * where it blows; screen motion is an illustrative cue, not a trajectory. */
export const windToHeading = (windFromDegrees: number): number => (windFromDegrees + 180) % 360;

export const windToCompass = (heading: number): string =>
  ["N", "NE", "E", "SE", "S", "SW", "W", "NW"][Math.round(((heading % 360) + 360) % 360 / 45) % 8];

/** Flow lines are spread between forecast grid points. Only report a nearby
 * model sample; visual positions between samples are not measurements. */
export function nearestWindFlowSample(map: MapLibreMap, frame: WindArrowFrame, x: number, y: number, radius = 90): WindArrowSample | null {
  const globe = map.getProjection?.()?.type === "globe";
  const scale = globe ? globeOverviewSizeScale(map.getZoom()) : 1;
  if (scale < 0.06) return null;
  const center = globe ? map.getCenter() : null;
  let nearest: WindArrowSample | null = null;
  let distanceSquared = (radius * scale) ** 2;
  for (const sample of frame.samples) {
    if (sample.speedMetersPerSecond < CALM_METERS_PER_SECOND) continue; // No flow is drawn for calm samples.
    if (center && !onVisibleGlobeHemisphere(center, [sample.longitude, sample.latitude])) continue;
    const point = map.project([sample.longitude, sample.latitude]);
    const candidateDistance = (point.x - x) ** 2 + (point.y - y) ** 2;
    if (candidateDistance < distanceSquared) {
      distanceSquared = candidateDistance;
      nearest = sample;
    }
  }
  return nearest;
}

/*
 * Geographic streamlines
 * ----------------------
 * Particles live in Web Mercator coordinates on the ground and are advected by
 * a smooth field built from the frame's GFS 10 m samples (bilinear between a
 * regular sample grid, otherwise inverse-distance weighting). Trails are traced
 * back along the same field, so every point of a line is a ground position and
 * is projected to the screen each frame: lines rotate with the bearing,
 * foreshorten and converge with pitch, and follow the globe.
 *
 * Display rate (illustrative, not a trajectory): a particle moves
 * WIND_FLOW_DISPLAY_RATE screen pixels per second for each m/s of modelled wind
 * at the map's nominal top-down scale at the view centre. Ground distance is
 * therefore compressed by one uniform time factor across the view (about an
 * hour of real 10 m wind per displayed second at zoom 7), so direction and
 * relative speed are the model's, and the nearer ground in a pitched view moves
 * faster on screen exactly as real flow would. Positions between grid points
 * are interpolated for display only and are never reported as readings.
 */
export const WIND_FLOW_DISPLAY_RATE = 8;
const CALM_METERS_PER_SECOND = 0.4;
// Trail persistence shortens as wind strengthens so light air still reads as a
// line and strong wind does not smear across the view. Head motion stays linear.
const TRAIL_SECONDS = 5;
const trailSeconds = (speed: number) => TRAIL_SECONDS / (1 + speed / 10);
const FIELD_RESOLUTION = 24;
const FRAME_BUDGET_MS = 3.5;
const ALPHA_LEVELS = 8;
const SPEED_EDGES = [3, 6, 9, 13] as const; // m/s colour-bucket edges
// Pale cyan for light air through white to amber for strong wind; every core
// sits on a dark translucent under-stroke so it reads on any basemap.
/** Line palette per basemap tone: deep teal on light maps, pale cyan glow on
 * dark and imagery maps. Amber marks only strong wind (≥ 13 m/s). */
export type WindFlowTone = "light" | "dark";
const PALETTES = {
  light: {
    speed: ["16, 104, 130", "14, 95, 120", "12, 82, 106", "10, 61, 82", "176, 104, 14"],
    halo: "255, 255, 255", haloAlpha: 0.42, head: "0, 140, 172", glowAlpha: 0,
  },
  dark: {
    speed: ["120, 196, 228", "143, 214, 238", "192, 236, 248", "238, 250, 252", "255, 210, 136"],
    halo: "4, 20, 28", haloAlpha: 0.22, head: "240, 252, 255", glowAlpha: 0.16,
  },
} as const;
const SPEED_BUCKETS = 5;
const LIGHT_BASEMAPS = new Set<string>(["standard", ...LIGHT_CATEGORY_BASEMAPS, "prairie", "streets", "topo"]);
/** Light vector basemaps get dark lines; midnight and imagery get light ones. */
export const windFlowToneForBasemap = (basemap: string): WindFlowTone => LIGHT_BASEMAPS.has(basemap) ? "light" : "dark";

type WindField = {
  x0: number; y0: number; x1: number; y1: number; nx: number; ny: number;
  gxScale: number; gyScale: number;
  /** Mercator velocity per m/s, already divided by cos(latitude). */
  fx: Float32Array; fy: Float32Array; speed: Float32Array;
};

type FlowState = {
  capacity: number;
  x: Float64Array; y: Float64Array; age: Float32Array; life: Float32Array; trail: Float32Array; alive: Uint8Array;
  lastTime: number | null;
  /** Shrinks the particle count when per-point projection runs over budget. */
  load: number;
  seedZoom: number;
  random: () => number;
  coverageKey: string; coverage: number;
  stats: WindFlowStats;
};

export type WindFlowStats = Readonly<{ mode: "homography" | "per-point" | "none"; particles: number; active: number; segments: number; cpuMs: number }>;

const mercatorX = (longitude: number) => (longitude + 180) / 360;
const mercatorY = (latitude: number) => (180 - (180 / Math.PI) * Math.log(Math.tan(Math.PI / 4 + latitude * Math.PI / 360))) / 360;
const longitudeOf = (x: number) => x * 360 - 180;
const latitudeOf = (y: number) => (360 / Math.PI) * Math.atan(Math.exp((180 - y * 360) * Math.PI / 180)) - 90;
const smoothstep = (edge0: number, edge1: number, value: number) => {
  const t = Math.max(0, Math.min(1, (value - edge0) / (edge1 - edge0)));
  return t * t * (3 - 2 * t);
};

function seededRandom(seed: number): () => number {
  let state = seed >>> 0;
  return () => {
    state = (state + 0x6d2b79f5) >>> 0;
    let t = state;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

type RegularGrid = { rows: number; cols: number; latitudes: number[]; longitudes: number[] };

/** Detect the row-major south→north, west→east grid the wind route requests. */
function regularGrid(samples: readonly WindArrowSample[]): RegularGrid | null {
  const count = samples.length;
  const columnOptions: number[] = [];
  for (let cols = 2; cols <= count / 2; cols += 1) if (count % cols === 0) columnOptions.push(cols);
  columnOptions.sort((a, b) => Math.abs(a - Math.sqrt(count)) - Math.abs(b - Math.sqrt(count)));
  for (const cols of columnOptions) {
    const rows = count / cols;
    const latitudes = Array.from({ length: rows }, (_, row) => samples.slice(row * cols, row * cols + cols).reduce((sum, sample) => sum + sample.latitude, 0) / cols);
    const longitudes = Array.from({ length: cols }, (_, col) => {
      let sum = 0;
      for (let row = 0; row < rows; row += 1) sum += samples[row * cols + col].longitude;
      return sum / rows;
    });
    let minimumSpacing = Infinity;
    for (let index = 1; index < rows; index += 1) minimumSpacing = Math.min(minimumSpacing, latitudes[index] - latitudes[index - 1]);
    for (let index = 1; index < cols; index += 1) minimumSpacing = Math.min(minimumSpacing, longitudes[index] - longitudes[index - 1]);
    if (!(minimumSpacing > 1e-3)) continue;
    const tolerance = minimumSpacing * 0.3;
    if (samples.every((sample, index) => Math.abs(sample.latitude - latitudes[Math.floor(index / cols)]) <= tolerance
      && Math.abs(sample.longitude - longitudes[index % cols]) <= tolerance)) return { rows, cols, latitudes, longitudes };
  }
  return null;
}

const bracket = (values: readonly number[], value: number): [number, number] => {
  if (value <= values[0]) return [0, 0];
  const last = values.length - 1;
  if (value >= values[last]) return [last - 1, 1];
  let index = 0;
  while (index < last - 1 && value > values[index + 1]) index += 1;
  return [index, (value - values[index]) / (values[index + 1] - values[index])];
};

const fieldCache = new WeakMap<WindArrowFrame, WindField | null>();

function windField(frame: WindArrowFrame): WindField | null {
  if (fieldCache.has(frame)) return fieldCache.get(frame)!;
  const samples = frame.samples.filter((sample) => [sample.latitude, sample.longitude, sample.speedMetersPerSecond, sample.windFromDegrees].every(Number.isFinite));
  if (!samples.length) { fieldCache.set(frame, null); return null; }
  // Vector components of where the wind blows TO (east u, north v).
  const east = samples.map((sample) => sample.speedMetersPerSecond * Math.sin(windToHeading(sample.windFromDegrees) * Math.PI / 180));
  const north = samples.map((sample) => sample.speedMetersPerSecond * Math.cos(windToHeading(sample.windFromDegrees) * Math.PI / 180));
  const grid = samples.length >= 4 ? regularGrid(samples) : null;
  let west: number, eastEdge: number, south: number, northEdge: number;
  if (grid) {
    const halfRow = (grid.latitudes[grid.rows - 1] - grid.latitudes[0]) / (grid.rows - 1) / 2;
    const halfColumn = (grid.longitudes[grid.cols - 1] - grid.longitudes[0]) / (grid.cols - 1) / 2;
    south = grid.latitudes[0] - halfRow; northEdge = grid.latitudes[grid.rows - 1] + halfRow;
    west = grid.longitudes[0] - halfColumn; eastEdge = grid.longitudes[grid.cols - 1] + halfColumn;
  } else {
    const latitudes = samples.map((sample) => sample.latitude), longitudes = samples.map((sample) => sample.longitude);
    const divisions = Math.max(1, Math.sqrt(samples.length) - 1);
    const latitudeMargin = Math.max(0.08, (Math.max(...latitudes) - Math.min(...latitudes)) / divisions / 2);
    const longitudeMargin = Math.max(0.08, (Math.max(...longitudes) - Math.min(...longitudes)) / divisions / 2);
    south = Math.min(...latitudes) - latitudeMargin; northEdge = Math.max(...latitudes) + latitudeMargin;
    west = Math.min(...longitudes) - longitudeMargin; eastEdge = Math.max(...longitudes) + longitudeMargin;
  }
  const nx = FIELD_RESOLUTION, ny = FIELD_RESOLUTION;
  const field: WindField = {
    x0: mercatorX(west), x1: mercatorX(eastEdge), y0: mercatorY(northEdge), y1: mercatorY(south), nx, ny,
    gxScale: 0, gyScale: 0,
    fx: new Float32Array(nx * ny), fy: new Float32Array(nx * ny), speed: new Float32Array(nx * ny),
  };
  field.gxScale = (nx - 1) / (field.x1 - field.x0);
  field.gyScale = (ny - 1) / (field.y1 - field.y0);
  for (let j = 0; j < ny; j += 1) {
    const latitude = latitudeOf(field.y0 + (field.y1 - field.y0) * j / (ny - 1));
    const cosine = Math.cos(latitude * Math.PI / 180);
    for (let i = 0; i < nx; i += 1) {
      const longitude = longitudeOf(field.x0 + (field.x1 - field.x0) * i / (nx - 1));
      let u = 0, v = 0;
      if (grid) {
        const [row, ty] = bracket(grid.latitudes, latitude);
        const [col, tx] = bracket(grid.longitudes, longitude);
        const a = row * grid.cols + col, b = a + 1, c = a + grid.cols, d = c + 1;
        u = (east[a] * (1 - tx) + east[b] * tx) * (1 - ty) + (east[c] * (1 - tx) + east[d] * tx) * ty;
        v = (north[a] * (1 - tx) + north[b] * tx) * (1 - ty) + (north[c] * (1 - tx) + north[d] * tx) * ty;
      } else {
        let weightSum = 0;
        for (let index = 0; index < samples.length; index += 1) {
          const dLat = samples[index].latitude - latitude, dLng = (samples[index].longitude - longitude) * cosine;
          const weight = 1 / (dLat * dLat + dLng * dLng + 1e-6);
          weightSum += weight; u += east[index] * weight; v += north[index] * weight;
        }
        u /= weightSum; v /= weightSum;
      }
      const k = j * nx + i;
      field.fx[k] = u / cosine;
      field.fy[k] = -v / cosine;
      field.speed[k] = Math.hypot(u, v);
    }
  }
  fieldCache.set(frame, field);
  return field;
}

/** Bilinear lookup into the display field. Writes [fx, fy, m/s] or returns false outside it. */
function sampleField(field: WindField, x: number, y: number, out: Float64Array): boolean {
  const gx = (x - field.x0) * field.gxScale, gy = (y - field.y0) * field.gyScale;
  if (!(gx >= 0 && gy >= 0 && gx <= field.nx - 1 && gy <= field.ny - 1)) return false;
  const i = Math.min(field.nx - 2, gx | 0), j = Math.min(field.ny - 2, gy | 0);
  const tx = gx - i, ty = gy - j;
  const a = j * field.nx + i, b = a + 1, c = a + field.nx, d = c + 1;
  const wa = (1 - tx) * (1 - ty), wb = tx * (1 - ty), wc = (1 - tx) * ty, wd = tx * ty;
  out[0] = field.fx[a] * wa + field.fx[b] * wb + field.fx[c] * wc + field.fx[d] * wd;
  out[1] = field.fy[a] * wa + field.fy[b] * wb + field.fy[c] * wc + field.fy[d] * wd;
  out[2] = field.speed[a] * wa + field.speed[b] * wb + field.speed[c] * wc + field.speed[d] * wd;
  return true;
}

/** Solve the 3×3 projective transform (h33 = 1) mapping four source points to four screen points. */
function solveHomography(source: readonly number[], target: readonly number[]): Float64Array | null {
  const rows: number[][] = [];
  for (let index = 0; index < 4; index += 1) {
    const X = source[index * 2], Y = source[index * 2 + 1], u = target[index * 2], v = target[index * 2 + 1];
    rows.push([X, Y, 1, 0, 0, 0, -u * X, -u * Y, u], [0, 0, 0, X, Y, 1, -v * X, -v * Y, v]);
  }
  for (let column = 0; column < 8; column += 1) {
    let pivot = column;
    for (let row = column + 1; row < 8; row += 1) if (Math.abs(rows[row][column]) > Math.abs(rows[pivot][column])) pivot = row;
    if (Math.abs(rows[pivot][column]) < 1e-12) return null;
    [rows[column], rows[pivot]] = [rows[pivot], rows[column]];
    for (let row = 0; row < 8; row += 1) {
      if (row === column) continue;
      const factor = rows[row][column] / rows[column][column];
      if (factor) for (let k = column; k < 9; k += 1) rows[row][k] -= factor * rows[column][k];
    }
  }
  const h = new Float64Array(9);
  for (let index = 0; index < 8; index += 1) h[index] = rows[index][8] / rows[index][index];
  h[8] = 1;
  return h.every(Number.isFinite) ? h : null;
}

function invert3(m: Float64Array): Float64Array | null {
  const [a, b, c, d, e, f, g, h, i] = m;
  const A = e * i - f * h, B = -(d * i - f * g), C = d * h - e * g;
  const det = a * A + b * B + c * C;
  if (!Number.isFinite(det) || Math.abs(det) < 1e-18) return null;
  return new Float64Array([A / det, -(b * i - c * h) / det, (b * f - c * e) / det, B / det, (a * i - c * g) / det, -(a * f - c * d) / det, C / det, -(a * h - b * g) / det, (a * e - b * d) / det]);
}

type View = {
  map: MapLibreMap;
  width: number; height: number;
  /** Mercator → screen through a homography (flat map, no terrain) or per-point map.project. */
  perPoint: boolean;
  globeCenter: { lng: number; lat: number } | null;
  cx: number; cy: number; worldSize: number;
  h: Float64Array | null; inverse: Float64Array | null;
};

function buildView(map: MapLibreMap, width: number, height: number, globe: boolean): View {
  const zoom = map.getZoom();
  const center = map.getCenter?.() ?? null;
  const view: View = {
    map, width, height, perPoint: true, globeCenter: globe ? center : null,
    cx: center ? mercatorX(center.lng) : 0, cy: center ? mercatorY(center.lat) : 0, worldSize: 512 * 2 ** zoom,
    h: null, inverse: null,
  };
  if (globe || !center) return view;
  // A flat pitched/rotated Mercator map is a perspective view of a plane, so
  // ground → screen is exactly projective. Fit it from four projected points
  // near the centre (always in front of the camera) and verify a fifth.
  const reach = 128;
  const source = [-reach, -reach, reach, -reach, reach, reach, -reach, reach];
  const projectLocal = (X: number, Y: number) => map.project([longitudeOf(view.cx + X / view.worldSize), latitudeOf(view.cy + Y / view.worldSize)]);
  const target: number[] = [];
  for (let index = 0; index < 4; index += 1) {
    const point = projectLocal(source[index * 2], source[index * 2 + 1]);
    target.push(point.x, point.y);
  }
  const h = solveHomography(source, target);
  const inverse = h && invert3(h);
  if (!h || !inverse) return view;
  const check = projectLocal(reach * 0.7, -reach * 0.4);
  const X = reach * 0.7, Y = -reach * 0.4, w = h[6] * X + h[7] * Y + 1;
  const error = Math.hypot((h[0] * X + h[1] * Y + h[2]) / w - check.x, (h[3] * X + h[4] * Y + h[5]) / w - check.y);
  if (!(error < 0.75)) return view;
  view.h = h;
  view.inverse = inverse;
  // Terrain lifts ground points off the plane, so project each one; the
  // homography still drives seeding and distance haze.
  view.perPoint = Boolean(map.getTerrain?.());
  return view;
}

/** Project a Mercator point. Writes [x, y, relative scale] or returns false when culled. */
function projectPoint(view: View, x: number, y: number, out: Float64Array): boolean {
  const h = view.h;
  let scale = 1;
  if (h) {
    const X = (x - view.cx) * view.worldSize, Y = (y - view.cy) * view.worldSize;
    const w = h[6] * X + h[7] * Y + 1;
    if (w < 0.02) return false; // behind the camera or past the horizon
    scale = 1 / w;
    if (!view.perPoint) {
      out[0] = (h[0] * X + h[1] * Y + h[2]) * scale;
      out[1] = (h[3] * X + h[4] * Y + h[5]) * scale;
      out[2] = scale;
      return true;
    }
  }
  const point = view.map.project([longitudeOf(x), latitudeOf(y)]);
  if (!Number.isFinite(point.x) || !Number.isFinite(point.y)) return false;
  out[0] = point.x; out[1] = point.y; out[2] = scale;
  return true;
}

/** Stationary travel arrows are anchored only at actual model samples. Their
 * screen heading is projected geographically, so bearing and pitch apply. */
export function windDirectionGlyphs(map: MapLibreMap, frame: WindArrowFrame): readonly {
  x: number; y: number; dx: number; dy: number; length: number;
}[] {
  const globe = map.getProjection?.()?.type === "globe";
  const scale = globe ? globeOverviewSizeScale(map.getZoom()) : 1;
  if (scale < 0.06) return [];
  const center = globe ? map.getCenter() : null;
  const canvas = map.getCanvas();
  const glyphs: { x: number; y: number; dx: number; dy: number; length: number }[] = [];
  for (const sample of frame.samples) {
    if (![sample.latitude, sample.longitude, sample.windFromDegrees, sample.speedMetersPerSecond].every(Number.isFinite)
      || sample.speedMetersPerSecond < CALM_METERS_PER_SECOND) continue;
    if (center && !onVisibleGlobeHemisphere(center, [sample.longitude, sample.latitude])) continue;
    const point = map.project([sample.longitude, sample.latitude]);
    const heading = windToHeading(sample.windFromDegrees) * Math.PI / 180;
    const next = map.project([
      sample.longitude + Math.sin(heading) * 0.01 / Math.cos(sample.latitude * Math.PI / 180),
      sample.latitude + Math.cos(heading) * 0.01,
    ]);
    const dx = next.x - point.x, dy = next.y - point.y, magnitude = Math.hypot(dx, dy);
    if (![point.x, point.y, magnitude].every(Number.isFinite) || magnitude < 0.001
      || point.x < 0 || point.y < 0 || point.x > canvas.clientWidth || point.y > canvas.clientHeight
      || glyphs.some(other => Math.hypot(other.x - point.x, other.y - point.y) < 24)) continue;
    glyphs.push({ x: point.x, y: point.y, dx: dx / magnitude, dy: dy / magnitude, length: 18 * Math.min(1, scale * 2.2) });
  }
  return glyphs;
}

/** Screen → ground on the flat map plane; false above the horizon. */
function unprojectScreen(view: View, sx: number, sy: number, out: Float64Array): boolean {
  const m = view.inverse!, h = view.h!;
  const W = m[6] * sx + m[7] * sy + m[8];
  if (Math.abs(W) < 1e-12) return false;
  const X = (m[0] * sx + m[1] * sy + m[2]) / W, Y = (m[3] * sx + m[4] * sy + m[5]) / W;
  const w = h[6] * X + h[7] * Y + 1;
  if (w < 0.02) return false;
  out[0] = view.cx + X / view.worldSize; out[1] = view.cy + Y / view.worldSize; out[2] = 1 / w;
  return true;
}

const insideField = (field: WindField, x: number, y: number) => x >= field.x0 && x <= field.x1 && y >= field.y0 && y <= field.y1;

function estimateCoverage(view: View, field: WindField, scratch: Float64Array): number {
  if (view.inverse) {
    let hits = 0, total = 0;
    for (let row = 0; row < 9; row += 1) for (let col = 0; col < 12; col += 1) {
      total += 1;
      if (unprojectScreen(view, (col + 0.5) / 12 * view.width, (row + 0.5) / 9 * view.height, scratch)
        && scratch[2] > 0.12 && insideField(field, scratch[0], scratch[1])) hits += 1;
    }
    return hits / total;
  }
  // Globe: screen area of the field's projected footprint.
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  for (let row = 0; row <= 4; row += 1) for (let col = 0; col <= 4; col += 1) {
    const x = field.x0 + (field.x1 - field.x0) * col / 4, y = field.y0 + (field.y1 - field.y0) * row / 4;
    if (view.globeCenter && !onVisibleGlobeHemisphere(view.globeCenter, [longitudeOf(x), latitudeOf(y)])) continue;
    if (!projectPoint(view, x, y, scratch)) continue;
    minX = Math.min(minX, scratch[0]); maxX = Math.max(maxX, scratch[0]);
    minY = Math.min(minY, scratch[1]); maxY = Math.max(maxY, scratch[1]);
  }
  if (!(maxX > minX && maxY > minY)) return 0;
  const width = Math.max(0, Math.min(view.width, maxX) - Math.max(0, minX));
  const height = Math.max(0, Math.min(view.height, maxY) - Math.max(0, minY));
  return Math.min(1, width * height / (view.width * view.height));
}

const states = new WeakMap<HTMLCanvasElement, FlowState>();

function flowState(canvas: HTMLCanvasElement, capacity: number): FlowState {
  let state = states.get(canvas);
  if (!state || state.capacity < capacity) {
    state = {
      capacity: Math.max(capacity, state?.capacity ?? 0),
      x: new Float64Array(capacity), y: new Float64Array(capacity), age: new Float32Array(capacity), life: new Float32Array(capacity), trail: new Float32Array(capacity), alive: new Uint8Array(capacity),
      lastTime: null, load: 1, seedZoom: NaN, random: seededRandom(0x5eed), coverageKey: "", coverage: 0,
      stats: { mode: "none", particles: 0, active: 0, segments: 0, cpuMs: 0 },
    };
    states.set(canvas, state);
  }
  return state;
}

/** Drop a canvas's particles (layer hidden or unmounted). */
export function resetWindFlowCanvas(canvas: HTMLCanvasElement): void {
  states.delete(canvas);
}

/** Last frame's draw statistics, for QA and tests. */
export function windFlowCanvasStats(canvas: HTMLCanvasElement): WindFlowStats | null {
  return states.get(canvas)?.stats ?? null;
}

type Bucket = { data: number[]; length: number; penX: number; penY: number };
const newBucket = (): Bucket => ({ data: [], length: 0, penX: NaN, penY: NaN });
// Buckets: speed colour × alpha level, plus one head bucket per alpha level.
const buckets: Bucket[] = Array.from({ length: SPEED_BUCKETS * ALPHA_LEVELS + ALPHA_LEVELS }, newBucket);

function pushSegment(bucket: Bucket, x0: number, y0: number, x1: number, y1: number) {
  const data = bucket.data;
  if (bucket.penX !== x0 || bucket.penY !== y0) {
    data[bucket.length++] = 0; data[bucket.length++] = x0; data[bucket.length++] = y0;
  }
  data[bucket.length++] = 1; data[bucket.length++] = x1; data[bucket.length++] = y1;
  bucket.penX = x1; bucket.penY = y1;
}

type PathTarget = { moveTo(x: number, y: number): void; lineTo(x: number, y: number): void };
function tracePath(target: PathTarget, bucket: Bucket) {
  const data = bucket.data;
  for (let index = 0; index < bucket.length; index += 3) {
    if (data[index] === 0) target.moveTo(data[index + 1], data[index + 2]);
    else target.lineTo(data[index + 1], data[index + 2]);
  }
}

/** Draw GFS 10 m wind as softly glowing ground streamlines. Direction and
 * relative pace come from the model; positions between grid points, particle
 * placement and the time compression are visual and never imply a measured
 * path. With `animate` false the same lines are drawn as a still frame. */
export function drawWindFlowCanvas(canvas: HTMLCanvasElement, map: MapLibreMap, frame: WindArrowFrame, elapsedMs: number, animate: boolean, tone: WindFlowTone = "dark"): void {
  const palette = PALETTES[tone];
  const started = typeof performance !== "undefined" ? performance.now() : 0;
  const mapCanvas = map.getCanvas();
  const width = mapCanvas.clientWidth;
  const height = mapCanvas.clientHeight;
  if (!width || !height) return;
  const pixelRatio = Math.min(1.5, window.devicePixelRatio || 1);
  const targetWidth = Math.round(width * pixelRatio);
  const targetHeight = Math.round(height * pixelRatio);
  if (canvas.width !== targetWidth || canvas.height !== targetHeight) {
    canvas.width = targetWidth;
    canvas.height = targetHeight;
  }
  const context = canvas.getContext("2d");
  if (!context) return;
  context.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
  context.clearRect(0, 0, width, height);
  const globe = map.getProjection?.()?.type === "globe";
  const zoom = map.getZoom();
  const visualScale = globe ? globeOverviewSizeScale(zoom) : 1;
  if (visualScale < 0.06) return;
  const field = windField(frame);
  if (!field) return;

  const view = buildView(map, width, height, globe);
  const area = width * height;
  // Particle density per covered screen area, capped by projection cost.
  const capacity = view.perPoint ? 320 : 1500;
  const pixelsPerParticle = view.perPoint ? 1400 : 1800;
  const steps = view.perPoint ? 10 : 24;
  const state = flowState(canvas, capacity);
  const scratch = new Float64Array(3), sample = new Float64Array(3), point = new Float64Array(3);

  // Time: advance by real elapsed time, clamped after hidden tabs or stalls.
  // A clock that runs backwards (a recorder restarting) restarts the particles.
  let dt = 0;
  if (animate) {
    if (state.lastTime !== null && elapsedMs < state.lastTime) {
      state.alive.fill(0);
      state.random = seededRandom(0x5eed);
    } else if (state.lastTime !== null) dt = Math.min(0.1, (elapsedMs - state.lastTime) / 1000);
    state.lastTime = elapsedMs;
  }
  // A large zoom change leaves particles clustered; let them fade and reseed.
  if (!(Math.abs(zoom - state.seedZoom) <= 0.4)) {
    if (!animate || !Number.isFinite(state.seedZoom)) state.alive.fill(0);
    else for (let index = 0; index < state.capacity; index += 1) state.life[index] = Math.min(state.life[index], state.age[index] + 0.2 + state.random() * 1.1);
    state.seedZoom = zoom;
  }

  const coverageKey = `${width}x${height}|${view.cx.toFixed(7)},${view.cy.toFixed(7)}|${zoom.toFixed(3)}|${map.getBearing?.() ?? 0}|${map.getPitch?.() ?? 0}|${globe}|${field.x0},${field.y0}`;
  const cameraChanged = coverageKey !== state.coverageKey;
  if (cameraChanged) {
    state.coverageKey = coverageKey;
    state.coverage = estimateCoverage(view, field, scratch);
  }
  // A still frame only reseeds when the camera changes, so it never flickers.
  const canSpawn = animate || cameraChanged;
  const active = Math.min(capacity, Math.round(state.coverage * area / pixelsPerParticle * state.load));

  const centerCosine = Math.cos(latitudeOf(view.cy) * Math.PI / 180);
  // Mercator displacement per field unit for one displayed second.
  // The globe overview shrinks cues with Kansas; motion shrinks more gently.
  const rate = WIND_FLOW_DISPLAY_RATE * centerCosine * Math.sqrt(visualScale) / view.worldSize;
  const headStep = rate * dt;
  const margin = 60;

  // Globe seeding draws from the part of the field inside the visible bounds.
  let seedX0 = field.x0, seedX1 = field.x1, seedY0 = field.y0, seedY1 = field.y1;
  if (!view.inverse) {
    const bounds = map.getBounds?.();
    if (bounds) {
      seedX0 = Math.max(seedX0, mercatorX(bounds.getWest())); seedX1 = Math.min(seedX1, mercatorX(bounds.getEast()));
      seedY0 = Math.max(seedY0, mercatorY(bounds.getNorth())); seedY1 = Math.min(seedY1, mercatorY(bounds.getSouth()));
      if (!(seedX1 > seedX0 && seedY1 > seedY0)) { seedX0 = field.x0; seedX1 = field.x1; seedY0 = field.y0; seedY1 = field.y1; }
    }
  }
  const spawn = (index: number): boolean => {
    if (!canSpawn) return false;
    for (let attempt = 0, attempts = animate ? (view.perPoint ? 6 : 4) : 12; attempt < attempts; attempt += 1) {
      let x: number, y: number, depth = 1;
      if (view.inverse) {
        if (!unprojectScreen(view, -20 + state.random() * (width + 40), -20 + state.random() * (height + 40), scratch)) continue;
        x = scratch[0]; y = scratch[1]; depth = scratch[2];
      } else {
        x = seedX0 + state.random() * (seedX1 - seedX0);
        y = seedY0 + state.random() * (seedY1 - seedY0);
        if (view.globeCenter && !onVisibleGlobeHemisphere(view.globeCenter, [longitudeOf(x), latitudeOf(y)])) continue;
        if (!projectPoint(view, x, y, point) || point[0] < -margin || point[1] < -margin || point[0] > width + margin || point[1] > height + margin) continue;
      }
      if (!sampleField(field, x, y, sample) || sample[2] < CALM_METERS_PER_SECOND) continue;
      // Denser and brighter where the model wind is stronger; sparse toward the haze.
      if (state.random() > (0.3 + 0.7 * Math.min(1, sample[2] / 7)) * smoothstep(0.06, 0.3, depth)) continue;
      state.x[index] = x; state.y[index] = y;
      state.age[index] = animate ? 0 : state.random() * 4;
      state.life[index] = 2.5 + state.random() * 4;
      // Per-line length variation keeps neighbouring trails from aligning in rows.
      state.trail[index] = 0.6 + state.random() * 0.8;
      state.alive[index] = 1;
      return true;
    }
    return false;
  };

  for (const bucket of buckets) { bucket.length = 0; bucket.penX = NaN; bucket.penY = NaN; }
  let drawn = 0, segments = 0;
  // Hard per-frame budget: per-point projection (globe, terrain while DEM
  // tiles load) can be far slower than the homography; never exceed ~4 ms.
  const now = () => (typeof performance !== "undefined" ? performance.now() : 0);
  let overBudget = false;
  for (let index = 0; index < state.capacity; index += 1) {
    if (view.perPoint && now() - started > FRAME_BUDGET_MS) { overBudget = true; break; }
    if (index >= active) { state.alive[index] = 0; continue; }
    if ((!state.alive[index] || (animate && state.age[index] >= state.life[index])) && !spawn(index)) { state.alive[index] = 0; continue; }
    let x = state.x[index], y = state.y[index];
    if (!sampleField(field, x, y, sample) || sample[2] < CALM_METERS_PER_SECOND) { state.alive[index] = 0; continue; }
    if (headStep > 0) {
      x += sample[0] * headStep; y += sample[1] * headStep;
      state.x[index] = x; state.y[index] = y;
      state.age[index] += dt;
      if (!sampleField(field, x, y, sample) || sample[2] < CALM_METERS_PER_SECOND) { state.alive[index] = 0; continue; }
    }
    if (view.globeCenter && !onVisibleGlobeHemisphere(view.globeCenter, [longitudeOf(x), latitudeOf(y)])) { state.alive[index] = 0; continue; }
    if (!projectPoint(view, x, y, point) || point[0] < -margin || point[1] < -margin || point[0] > width + margin || point[1] > height + margin) { state.alive[index] = 0; continue; }
    const speed = sample[2];
    const age = state.age[index], life = state.life[index];
    const lifeFade = animate ? Math.max(0, Math.min(1, age / 0.6, (life - age) / 0.8)) : 1;
    // Soft edge where the model field ends (Kansas border or request extent).
    const edge = Math.min(x - field.x0, field.x1 - x) * field.gxScale / 1.5, edgeY = Math.min(y - field.y0, field.y1 - y) * field.gyScale / 1.5;
    const strength = (0.7 + 0.3 * Math.min(1, speed / 9)) * lifeFade * Math.min(1, edge, edgeY);
    if (strength <= 0.02) continue;
    const color = speed < SPEED_EDGES[0] ? 0 : speed < SPEED_EDGES[1] ? 1 : speed < SPEED_EDGES[2] ? 2 : speed < SPEED_EDGES[3] ? 3 : 4;
    let previousX = point[0], previousY = point[1], previousScale = point[2];
    const trailStep = rate * trailSeconds(speed) * state.trail[index] / steps;
    drawn += 1;
    for (let step = 0; step < steps; step += 1) {
      if (step > 0 && (!sampleField(field, x, y, sample) || sample[2] < CALM_METERS_PER_SECOND)) break;
      x -= sample[0] * trailStep; y -= sample[1] * trailStep;
      if (!projectPoint(view, x, y, point)) break;
      // Bright head fading toward the tail (as in the Weather scene), hazed
      // toward the horizon in pitched views.
      const tail = 1 - (step + 0.5) / steps;
      const alpha = strength * tail ** 2 * smoothstep(0.06, 0.3, Math.min(previousScale, point[2]));
      const level = Math.min(ALPHA_LEVELS - 1, Math.floor(alpha * ALPHA_LEVELS + 0.35) - 1);
      if (level >= 0) {
        pushSegment(buckets[color * ALPHA_LEVELS + level], previousX, previousY, point[0], point[1]);
        if (step === 0) pushSegment(buckets[SPEED_BUCKETS * ALPHA_LEVELS + level], previousX, previousY, point[0], point[1]);
        segments += 1;
      }
      previousX = point[0]; previousY = point[1]; previousScale = point[2];
    }
  }

  // Line weight: hairline when zoomed out, slightly bolder close in; thinner
  // with pitch so far lines do not clot; globe overview keeps Kansas-sized cues.
  const pitch = map.getPitch?.() ?? 0;
  const lineWidth = Math.max(0.6, (1 + 0.4 * smoothstep(4.5, 10, zoom)) * (1 - 0.15 * Math.min(1, pitch / 60)) * Math.min(1, visualScale * 2.2));
  const halo = Math.min(2.5, lineWidth + 1.1);
  // Butt caps: neighbouring alpha steps of one trail meet without beading.
  context.lineCap = "butt";
  context.lineJoin = "round";
  const canUsePath2D = typeof Path2D === "function";
  const paths: (Path2D | null)[] = buckets.map((bucket) => {
    if (!bucket.length || !canUsePath2D) return null;
    const path = new Path2D();
    tracePath(path, bucket);
    return path;
  });
  const strokeBucket = (index: number, style: string, widthPx: number) => {
    const bucket = buckets[index];
    if (!bucket.length) return;
    context.strokeStyle = style;
    context.lineWidth = widthPx;
    const path = paths[index];
    if (path) context.stroke(path);
    else { context.beginPath(); tracePath(context, bucket); context.stroke(); }
  };
  const levelAlpha = (level: number) => (level + 1) / ALPHA_LEVELS;
  const colorBuckets = SPEED_BUCKETS * ALPHA_LEVELS;
  const speedColor = (index: number) => palette.speed[Math.floor(index / ALPHA_LEVELS)];
  // 1. Subtle separation halo: white on light maps, dark on dark/imagery maps.
  for (let index = 0; index < colorBuckets; index += 1) strokeBucket(index, `rgba(${palette.halo}, ${(levelAlpha(index % ALPHA_LEVELS) * palette.haloAlpha).toFixed(3)})`, halo);
  // 2. Soft coloured glow on dark and imagery maps only.
  if (palette.glowAlpha) for (let index = 0; index < colorBuckets; index += 1) strokeBucket(index, `rgba(${speedColor(index)}, ${(levelAlpha(index % ALPHA_LEVELS) * palette.glowAlpha).toFixed(3)})`, Math.min(2.5, lineWidth * 2.2));
  // 3. Thin core coloured by model speed, fading to transparent toward the tail.
  for (let index = 0; index < colorBuckets; index += 1) strokeBucket(index, `rgba(${speedColor(index)}, ${levelAlpha(index % ALPHA_LEVELS).toFixed(3)})`, lineWidth);
  // 4. Small bright head.
  context.lineCap = "round";
  for (let level = 0; level < ALPHA_LEVELS; level += 1) strokeBucket(colorBuckets + level, `rgba(${palette.head}, ${levelAlpha(level).toFixed(3)})`, lineWidth * 1.3);

  // Still trails alone cannot communicate travel direction reliably. With
  // reduced/disabled motion, add a small arrow at each visible model point.
  if (!animate) for (const glyph of windDirectionGlyphs(map, frame)) {
    const { x, y, dx, dy, length } = glyph;
    const tipX = x + dx * length / 2, tipY = y + dy * length / 2;
    context.beginPath();
    context.moveTo(x - dx * length / 2, y - dy * length / 2);
    context.lineTo(tipX, tipY);
    context.moveTo(tipX - dx * length * 0.35 - dy * length * 0.25, tipY - dy * length * 0.35 + dx * length * 0.25);
    context.lineTo(tipX, tipY);
    context.lineTo(tipX - dx * length * 0.35 + dy * length * 0.25, tipY - dy * length * 0.35 - dx * length * 0.25);
    context.strokeStyle = `rgba(${palette.halo}, 0.9)`;
    context.lineWidth = lineWidth + 2;
    context.stroke();
    context.strokeStyle = `rgba(${palette.speed[2]}, 1)`;
    context.lineWidth = lineWidth * 1.5;
    context.stroke();
  }

  const cpuMs = now() - started;
  if (overBudget || cpuMs > FRAME_BUDGET_MS) state.load = Math.max(0.05, state.load * 0.6);
  else if (cpuMs < FRAME_BUDGET_MS / 2) state.load = Math.min(1, state.load * 1.1);
  state.stats = {
    mode: view.perPoint ? "per-point" : "homography",
    particles: drawn,
    active,
    segments,
    cpuMs,
  };
}
