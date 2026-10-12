import type { Map as MapLibreMap } from "./maplibre-seam";
import type { StreamflowFrame } from "./streamflow";
import type { DownstreamPath, WaterReadingCue } from "./water-flow-context";
import { globeOverviewSizeScale, onVisibleGlobeHemisphere } from "./globe-context";

type ScreenPoint = Readonly<{ x: number; y: number }>;

/** Precomputed distances keep long river trails from rescanning every vertex. */
function pointAlong(points: readonly ScreenPoint[], cumulative: readonly number[], distance: number): Readonly<{ x: number; y: number; angle: number }> | null {
  if (distance < 0 || distance > cumulative.at(-1)!) return null;
  let low = 1, high = points.length - 1;
  while (low < high) { const middle = (low + high) >>> 1; if (cumulative[middle] < distance) low = middle + 1; else high = middle; }
  while (low < points.length - 1 && cumulative[low] - cumulative[low - 1] < 0.1) low++;
  const from = points[low - 1], to = points[low], length = cumulative[low] - cumulative[low - 1];
  if (length < 0.1) return null;
  const fraction = Math.max(0, Math.min(1, (distance - cumulative[low - 1]) / length));
  return { x: from.x + (to.x - from.x) * fraction, y: from.y + (to.y - from.y) * fraction, angle: Math.atan2(to.y - from.y, to.x - from.x) };
}

/** A screen-space streak stays on the provider's mapped line. Its length is illustrative. */
function strokeMappedTrail(context: CanvasRenderingContext2D, points: readonly ScreenPoint[], cumulative: readonly number[], head: number, reach: number, width: number, opacity: number): void {
  const start = Math.max(0, head - reach);
  const tail = pointAlong(points, cumulative, start);
  const tip = pointAlong(points, cumulative, head);
  if (!tail || !tip || head - start < 2) return;
  context.beginPath();
  context.moveTo(tail.x, tail.y);
  // Retain every provider bend between the clipped endpoints. Fixed-distance
  // sampling drew chords across short bends and could leave the river line.
  let low = 1, high = cumulative.length;
  while (low < high) { const middle = (low + high) >>> 1; if (cumulative[middle] <= start) low = middle + 1; else high = middle; }
  for (let index = low; index < points.length && cumulative[index] < head; index++) {
    context.lineTo(points[index].x, points[index].y);
  }
  context.lineTo(tip.x, tip.y);
  context.lineWidth = width;
  context.strokeStyle = `rgba(231, 255, 249, ${opacity})`;
  context.shadowColor = "rgba(19, 67, 101, .9)";
  context.shadowBlur = width * 2;
  context.stroke();
}

type ProjectedPath = { path: DownstreamPath; points: ScreenPoint[]; cumulative: number[]; length: number; visible: [number, number][] };
const projectedPathCache = new WeakMap<MapLibreMap, { paths: readonly DownstreamPath[]; camera: string; result: ProjectedPath[] }>();
function projectPaths(map: MapLibreMap, paths: readonly DownstreamPath[], width: number, height: number): ProjectedPath[] {
  const center = map.getCenter();
  const camera = [center.lng, center.lat, map.getZoom(), map.getBearing?.() ?? 0, map.getPitch?.() ?? 0, width, height, map.getProjection()?.type].join(":");
  const cached = projectedPathCache.get(map);
  if (cached?.paths === paths && cached.camera === camera) return cached.result;
  const result = paths.flatMap(path => {
    const points = path.coordinates.map(coordinate => map.project(coordinate as [number, number]));
    if (points.some(point => !Number.isFinite(point.x) || !Number.isFinite(point.y))) return [];
    const cumulative = [0];
    for (let i = 1; i < points.length; i++) cumulative.push(cumulative[i - 1] + Math.hypot(points[i].x - points[i - 1].x, points[i].y - points[i - 1].y));
    // Clip possible head positions to a viewport padded by the maximum tail.
    // Distance intervals avoid iterating miles of off-screen particles at high zoom.
    const visible: [number, number][] = [];
    for (let i = 1; i < points.length; i++) {
      let low = 0, high = 1;
      const from = points[i - 1], to = points[i];
      for (const [start, delta, minimum, maximum] of [[from.x, to.x - from.x, -260, width + 260], [from.y, to.y - from.y, -260, height + 260]]) {
        if (delta === 0) { if (start < minimum || start > maximum) high = -1; continue; }
        const a = (minimum - start) / delta, b = (maximum - start) / delta;
        low = Math.max(low, Math.min(a, b)); high = Math.min(high, Math.max(a, b));
      }
      if (high < low) continue;
      const distance = cumulative[i] - cumulative[i - 1];
      const start = cumulative[i - 1] + low * distance, end = cumulative[i - 1] + high * distance;
      const previous = visible.at(-1);
      if (previous && start <= previous[1] + .01) previous[1] = end;
      else visible.push([start, end]);
    }
    return [{ path, points, cumulative, length: cumulative.at(-1)!, visible }];
  });
  projectedPathCache.set(map, { paths, camera, result });
  return result;
}

/** Layered short bands create a tapered tail along bends, not across them. */
function luminousTrail(context: CanvasRenderingContext2D, points: readonly ScreenPoint[], cumulative: readonly number[], head: number, scale: number) {
  const reach = 240 * scale;
  strokeMappedTrail(context, points, cumulative, head, reach, 11 * scale, .10);
  const start = Math.max(0, head - reach), length = head - start;
  for (let band = 0; band < 10; band++) {
    const fraction = (band + 1) / 10;
    const tip = start + length * fraction;
    strokeMappedTrail(context, points, cumulative, tip, length / 10 + 1, (1 + fraction * 3.5) * scale, fraction * fraction * .88);
  }
  strokeMappedTrail(context, points, cumulative, head, 25 * scale, 2 * scale, .98);
}

/** The particle pace is constant screen motion, never a measured water velocity. */
export function drawWaterMotionCanvas(
  canvas: HTMLCanvasElement,
  map: MapLibreMap,
  frame: StreamflowFrame,
  selectedStationId: string | null,
  paths: readonly DownstreamPath[],
  selectedCue: WaterReadingCue | null,
  elapsedMs: number,
  animateReadings: boolean,
  animateDirection: boolean,
): void {
  const width = map.getCanvas().clientWidth;
  const height = map.getCanvas().clientHeight;
  if (!width || !height) return;
  const ratio = Math.min(1.5, window.devicePixelRatio || 1);
  if (canvas.width !== Math.round(width * ratio) || canvas.height !== Math.round(height * ratio)) {
    canvas.width = Math.round(width * ratio);
    canvas.height = Math.round(height * ratio);
  }
  const context = canvas.getContext("2d");
  if (!context) return;
  context.setTransform(ratio, 0, 0, ratio, 0, 0);
  context.clearRect(0, 0, width, height);
  const globe = map.getProjection()?.type === "globe";
  const visualScale = globe ? globeOverviewSizeScale(map.getZoom()) : 1;
  if (visualScale < 0.06) return;
  const center = globe ? map.getCenter() : null;
  const onVisibleHemisphere = (coordinate: readonly number[]) => !center || onVisibleGlobeHemisphere(center, coordinate);

  // Rings report change at each gauge. They do not spread water over the map.
  for (const feature of frame.features) {
    if (feature.geometry.type !== "Point") continue;
    if (!onVisibleHemisphere(feature.geometry.coordinates)) continue;
    const point = map.project(feature.geometry.coordinates as [number, number]);
    if (point.x < -24 || point.y < -24 || point.x > width + 24 || point.y > height + 24) continue;
    const selected = feature.properties.stationId === selectedStationId;
    const unavailable = feature.properties.missing || feature.properties.value === null;
    const trend = unavailable ? "missing" : feature.properties.value === 0 ? "zero" : feature.properties.trend;
    if (unavailable || trend === "zero") {
      const radius = (selected ? 11 : 7) * visualScale;
      context.save();
      context.strokeStyle = unavailable ? "rgba(199, 212, 221, .9)" : "rgba(255, 184, 105, .98)";
      context.lineWidth = (selected ? 2.3 : 1.8) * visualScale;
      context.setLineDash(unavailable ? [2 * visualScale, 3 * visualScale] : []);
      context.beginPath(); context.arc(point.x, point.y, radius, 0, Math.PI * 2); context.stroke();
      context.setLineDash([]);
      context.beginPath();
      const mark = 3 * visualScale;
      context.moveTo(point.x - mark, point.y - (unavailable ? mark : 0));
      context.lineTo(point.x + mark, point.y + (unavailable ? mark : 0));
      if (unavailable) { context.moveTo(point.x - mark, point.y + mark); context.lineTo(point.x + mark, point.y - mark); }
      context.stroke(); context.restore();
      continue;
    }
    const color = trend === "rising" ? "102, 233, 239" : trend === "falling" ? "165, 180, 255" : trend === "steady" ? "162, 218, 190" : "204, 216, 220";
    const pulsing = animateReadings && (trend === "rising" || trend === "falling");
    if (selected) {
      context.save();
      context.strokeStyle = "rgba(192, 255, 240, .85)";
      context.lineWidth = 1.8 * visualScale;
      const rotation = animateDirection || animateReadings ? elapsedMs / 9000 : 0;
      for (let segment = 0; segment < 4; segment++) {
        const angle = rotation + segment * Math.PI / 2;
        context.beginPath(); context.arc(point.x, point.y, 21 * visualScale, angle, angle + .38); context.stroke();
      }
      context.restore();
    }
    const seed = [...feature.properties.stationId].reduce((sum, character) => (sum * 31 + character.charCodeAt(0)) % 997, 0) / 997;
    const phase = pulsing ? (elapsedMs / (selected ? 1800 : 2600) + seed) % 1 : 0.45;
    const eased = phase * phase * (3 - 2 * phase);
    const travel = trend === "falling" ? 1 - eased : eased;
    const radius = (selected ? 10 + travel * 14 : 6 + travel * 8) * visualScale;
    context.beginPath();
    context.arc(point.x, point.y, radius, 0, Math.PI * 2);
    const opacity = pulsing ? Math.sin(Math.PI * phase) : 0.46;
    context.strokeStyle = `rgba(${color}, ${(selected ? 0.62 : 0.35) * opacity})`;
    context.lineWidth = (selected ? 2.5 : 1.5) * visualScale;
    context.stroke();

  }

  if (!selectedStationId || !selectedCue || paths.length === 0) return;
  const moving = selectedCue.value !== null && selectedCue.value > 0;
  for (const { path, points, cumulative, length, visible } of projectPaths(map, paths, width, height)) {
    if (path.coordinates.some(coordinate => !onVisibleHemisphere(coordinate))) continue;
    if (length < 12) continue;
    context.save();
    context.lineJoin = "round";
    context.lineCap = "round";
    context.beginPath();
    points.forEach((point, index) => index === 0 ? context.moveTo(point.x, point.y) : context.lineTo(point.x, point.y));
    context.strokeStyle = moving ? "rgba(8, 40, 53, .74)" : "rgba(8, 40, 53, .62)";
    context.lineWidth = 6 * visualScale;
    context.stroke();
    context.strokeStyle = moving ? "rgba(112, 235, 241, .76)" : selectedCue.value === 0 ? "rgba(255, 184, 105, .62)" : "rgba(180, 195, 207, .48)";
    context.lineWidth = 2.3 * visualScale;
    context.setLineDash(moving && !path.hasConnectors ? [] : [4, 5]);
    context.stroke();
    context.setLineDash([]);
    if (!moving) { context.restore(); continue; }
    // Keep at least one moving marker on short mapped segments. Longer gaps
    // between heads make the luminous trail legible without suggesting speed.
    const spacing = length >= 320 ? 280 : Math.max(12, length - 6);
    const offset = moving && animateDirection && length >= 30 ? (elapsedMs * 0.055) % spacing : 0;
    const firstArrow = length < 30 ? length / 2 : moving && animateDirection ? 3 + offset : 16;
    for (const [start, end] of visible) for (let distance = firstArrow + Math.max(0, Math.ceil((start - firstArrow) / spacing)) * spacing; distance < Math.min(length - 3, end + .001); distance += spacing) {
      const position = pointAlong(points, cumulative, distance);
      if (!position) continue;
      // A trail is at most 240 screen pixels long. Skip only heads farther
      // than that from the viewport, retaining tails that can still be seen.
      const margin = 240 * visualScale + 20;
      if (position.x < -margin || position.y < -margin || position.x > width + margin || position.y > height + margin) continue;
      if (moving && animateDirection) {
        luminousTrail(context, points, cumulative, distance, visualScale);
      }
      // The tail may still be visible after its head leaves the viewport.
      if (position.x < -20 || position.y < -20 || position.x > width + 20 || position.y > height + 20) continue;
      context.translate(position.x, position.y);
      context.rotate(position.angle);
      context.beginPath();
      context.moveTo(5 * visualScale, 0);
      context.lineTo(-4 * visualScale, -3.5 * visualScale);
      context.lineTo(-4 * visualScale, 3.5 * visualScale);
      context.closePath();
      context.fillStyle = moving ? "rgba(230, 255, 248, .95)" : "rgba(211, 231, 224, .75)";
      context.shadowColor = moving ? "rgba(59, 224, 239, .95)" : "transparent";
      context.shadowBlur = moving ? 8 * visualScale : 0;
      context.fill();
      context.setTransform(ratio, 0, 0, ratio, 0, 0);
    }
    context.restore();
  }
}
