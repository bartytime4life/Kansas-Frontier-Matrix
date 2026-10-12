import type { Map as MapLibreMap } from "./maplibre-seam";
import type { WindArrowFrame, WindArrowSample } from "./wind-arrow-data";
import { globeOverviewSizeScale, onVisibleGlobeHemisphere } from "./globe-context";

/** Meteorological directions describe where wind comes from. Flow moves toward
 * where it blows; screen motion is an illustrative cue, not a trajectory. */
export const windToHeading = (windFromDegrees: number): number => (windFromDegrees + 180) % 360;

export const windToCompass = (heading: number): string =>
  ["N", "NE", "E", "SE", "S", "SW", "W", "NW"][Math.round(((heading % 360) + 360) % 360 / 45) % 8];

/** Flow wisps are spread around forecast grid points. Only report a nearby
 * model sample; visual positions between samples are not measurements. */
export function nearestWindFlowSample(map: MapLibreMap, frame: WindArrowFrame, x: number, y: number, radius = 90): WindArrowSample | null {
  const globe = map.getProjection?.()?.type === "globe";
  const scale = globe ? globeOverviewSizeScale(map.getZoom()) : 1;
  if (scale < 0.06) return null;
  const center = globe ? map.getCenter() : null;
  let nearest: WindArrowSample | null = null;
  let distanceSquared = (radius * scale) ** 2;
  for (const sample of frame.samples) {
    if (sample.speedMetersPerSecond < 0.4) continue; // No arrow is drawn for calm samples.
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

function directionOnScreen(map: MapLibreMap, sample: WindArrowSample): [number, number] {
  const heading = windToHeading(sample.windFromDegrees) * Math.PI / 180;
  const from = map.project([sample.longitude, sample.latitude]);
  const latitudeDelta = Math.cos(heading) * 0.04;
  const longitudeDelta = Math.sin(heading) * 0.04 / Math.max(0.2, Math.cos(sample.latitude * Math.PI / 180));
  const to = map.project([sample.longitude + longitudeDelta, sample.latitude + latitudeDelta]);
  const length = Math.hypot(to.x - from.x, to.y - from.y);
  return length > 0.1 ? [(to.x - from.x) / length, (to.y - from.y) / length] : [0, -1];
}

const unitHash = (value: number): number => {
  const noise = Math.sin(value * 127.1 + 78.233) * 43758.5453;
  return noise - Math.floor(noise);
};

/** Draw short, translucent streamers near each model point. Their direction
 * and relative pace come from GFS; curl and particle placement are purely
 * visual and never imply a measured path between forecast grid points. */
export function drawWindFlowCanvas(canvas: HTMLCanvasElement, map: MapLibreMap, frame: WindArrowFrame, elapsedMs: number, animate: boolean): void {
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
  const visualScale = globe ? globeOverviewSizeScale(map.getZoom()) : 1;
  if (visualScale < 0.06) return;
  const center = globe ? map.getCenter() : null;
  frame.samples.forEach((sample, index) => {
    if (sample.speedMetersPerSecond < 0.4) return;
    if (center && !onVisibleGlobeHemisphere(center, [sample.longitude, sample.latitude])) return;
    const origin = map.project([sample.longitude, sample.latitude]);
    if (origin.x < -170 || origin.y < -170 || origin.x > width + 170 || origin.y > height + 170) return;
    const [dx, dy] = directionOnScreen(map, sample);
    const crossX = -dy;
    const crossY = dx;
    const pace = Math.max(2000, 5400 - sample.speedMetersPerSecond * 340);
    const lanes = globe && map.getZoom() < 4 ? 1 : map.getZoom() < 5 ? 4 : 7;
    for (let lane = 0; lane < lanes; lane += 1) {
      const seed = index * 13 + lane * 7 + 1;
      const phase = animate ? (elapsedMs / (pace * (0.82 + unitHash(seed + 2) * 0.36)) + unitHash(seed)) % 1 : unitHash(seed);
      const lateral = (unitHash(seed + 3) - 0.5) * 100 * visualScale;
      const along = ((unitHash(seed + 4) - 0.5) * 55 + (phase - 0.5) * 145) * visualScale;
      const curl = Math.sin(phase * Math.PI * 2 + seed) * (2 + unitHash(seed + 5) * 3) * visualScale;
      const length = (25 + Math.min(35, sample.speedMetersPerSecond * 3.4) + unitHash(seed + 6) * 16) * visualScale;
      const headX = origin.x + dx * along + crossX * (lateral + curl);
      const headY = origin.y + dy * along + crossY * (lateral + curl);
      const tailX = headX - dx * length + crossX * 2.5 * visualScale;
      const tailY = headY - dy * length + crossY * 2.5 * visualScale;
      const middleX = (tailX + headX) / 2 - crossX * (3 + unitHash(seed + 7) * 4) * visualScale;
      const middleY = (tailY + headY) / 2 - crossY * (3 + unitHash(seed + 7) * 4) * visualScale;
      const fade = Math.min(1, phase * 8, (1 - phase) * 8);
      const opacity = (0.48 + Math.min(0.25, sample.speedMetersPerSecond * 0.025)) * fade;
      const gradient = context.createLinearGradient(tailX, tailY, headX, headY);
      gradient.addColorStop(0, "rgba(2, 63, 78, 0)");
      gradient.addColorStop(0.45, `rgba(5, 113, 134, ${opacity * 0.55})`);
      gradient.addColorStop(1, `rgba(194, 250, 245, ${opacity})`);
      context.save();
      context.lineCap = "round";
      context.shadowColor = `rgba(15, 172, 191, ${opacity * 0.7})`;
      context.shadowBlur = 10 * visualScale;
      context.strokeStyle = gradient;
      context.lineWidth = 3.2 * visualScale;
      context.beginPath();
      context.moveTo(tailX, tailY);
      context.quadraticCurveTo(middleX, middleY, headX, headY);
      context.stroke();
      context.shadowBlur = 0;
      context.strokeStyle = `rgba(3, 59, 74, ${opacity * 0.42})`;
      context.lineWidth = 0.8 * visualScale;
      context.stroke();
      context.restore();
    }
  });
}
