import type { Map as MapLibreMap } from "./maplibre-seam";
import type { StreamflowFrame } from "./streamflow";
import type { DownstreamPath, WaterReadingCue } from "./water-flow-context";
import { globeOverviewSizeScale, onVisibleGlobeHemisphere } from "./globe-context";

type ScreenPoint = Readonly<{ x: number; y: number }>;

function pointAlong(points: readonly ScreenPoint[], distance: number): Readonly<{ x: number; y: number; angle: number }> | null {
  let remaining = distance;
  for (let index = 1; index < points.length; index += 1) {
    const from = points[index - 1];
    const to = points[index];
    const length = Math.hypot(to.x - from.x, to.y - from.y);
    if (length < 0.1) continue;
    if (remaining <= length) {
      const fraction = remaining / length;
      return { x: from.x + (to.x - from.x) * fraction, y: from.y + (to.y - from.y) * fraction, angle: Math.atan2(to.y - from.y, to.x - from.x) };
    }
    remaining -= length;
  }
  return null;
}

/** A screen-space streak stays on the provider's mapped line. Its length is illustrative. */
function strokeMappedTrail(context: CanvasRenderingContext2D, points: readonly ScreenPoint[], head: number, reach: number, width: number, opacity: number): void {
  const start = Math.max(0, head - reach);
  const tail = pointAlong(points, start);
  const tip = pointAlong(points, head);
  if (!tail || !tip || head - start < 2) return;
  context.beginPath();
  context.moveTo(tail.x, tail.y);
  for (let distance = start + 7; distance < head; distance += 7) {
    const point = pointAlong(points, distance);
    if (point) context.lineTo(point.x, point.y);
  }
  context.lineTo(tip.x, tip.y);
  context.lineWidth = width;
  context.strokeStyle = `rgba(231, 255, 249, ${opacity})`;
  context.shadowColor = "rgba(19, 67, 101, .9)";
  context.shadowBlur = width * 2;
  context.stroke();
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
    if (feature.geometry.type !== "Point" || feature.properties.missing || feature.properties.value === null) continue;
    if (!onVisibleHemisphere(feature.geometry.coordinates)) continue;
    const point = map.project(feature.geometry.coordinates as [number, number]);
    if (point.x < -24 || point.y < -24 || point.x > width + 24 || point.y > height + 24) continue;
    const selected = feature.properties.stationId === selectedStationId;
    const trend = feature.properties.value === 0 ? "zero" : feature.properties.trend;
    const color = trend === "rising" ? "102, 233, 239" : trend === "falling" || trend === "zero" ? "255, 184, 135" : trend === "steady" ? "162, 218, 190" : "204, 216, 220";
    const pulsing = animateReadings && (trend === "rising" || trend === "falling");
    const phase = pulsing ? (elapsedMs / (selected ? 1400 : 2200)) % 1 : 0.45;
    const travel = trend === "falling" ? 1 - phase : phase;
    const radius = (selected ? 10 + travel * 14 : 6 + travel * 8) * visualScale;
    context.beginPath();
    context.arc(point.x, point.y, radius, 0, Math.PI * 2);
    const opacity = pulsing ? (trend === "falling" ? phase : 1 - phase) : 0.46;
    context.strokeStyle = `rgba(${color}, ${(selected ? 0.62 : 0.35) * opacity})`;
    context.lineWidth = (selected ? 2.5 : 1.5) * visualScale;
    context.stroke();
    if (trend === "zero" && selected) {
      context.beginPath();
      context.moveTo(point.x - 4 * visualScale, point.y + 4 * visualScale);
      context.lineTo(point.x + 4 * visualScale, point.y - 4 * visualScale);
      context.strokeStyle = "rgba(255, 184, 135, .85)";
      context.lineWidth = 2 * visualScale;
      context.stroke();
    }
  }

  if (!selectedStationId || !selectedCue || paths.length === 0) return;
  const moving = selectedCue.value !== null && selectedCue.value > 0;
  for (const path of paths) {
    if (path.coordinates.some((coordinate) => !onVisibleHemisphere(coordinate))) continue;
    const points = path.coordinates.map((coordinate) => map.project(coordinate as [number, number]));
    const length = points.slice(1).reduce((sum, point, index) => sum + Math.hypot(point.x - points[index].x, point.y - points[index].y), 0);
    if (length < 12) continue;
    context.save();
    context.lineJoin = "round";
    context.lineCap = "round";
    context.beginPath();
    points.forEach((point, index) => index === 0 ? context.moveTo(point.x, point.y) : context.lineTo(point.x, point.y));
    context.strokeStyle = moving ? "rgba(8, 40, 53, .74)" : "rgba(8, 40, 53, .62)";
    context.lineWidth = 6 * visualScale;
    context.stroke();
    context.strokeStyle = moving ? "rgba(112, 235, 241, .76)" : "rgba(180, 220, 220, .48)";
    context.lineWidth = 2.3 * visualScale;
    context.setLineDash(moving ? [] : [4, 5]);
    context.stroke();
    context.setLineDash([]);
    // Keep at least one moving marker on short mapped segments. Longer gaps
    // between heads make the luminous trail legible without suggesting speed.
    const spacing = length >= 180 ? 150 : Math.max(12, length - 6);
    const offset = moving && animateDirection && length >= 30 ? (elapsedMs * 0.055) % spacing : 0;
    const firstArrow = length < 30 ? length / 2 : moving && animateDirection ? 3 + offset : 16;
    for (let distance = firstArrow; distance < length - 3; distance += spacing) {
      const position = pointAlong(points, distance);
      if (!position || position.x < -20 || position.y < -20 || position.x > width + 20 || position.y > height + 20) continue;
      if (moving && animateDirection) {
        strokeMappedTrail(context, points, distance, 136 * visualScale, 8 * visualScale, 0.35);
        strokeMappedTrail(context, points, distance, 96 * visualScale, 4.5 * visualScale, 0.62);
        strokeMappedTrail(context, points, distance, 52 * visualScale, 2.4 * visualScale, 0.95);
      }
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
