/** Camera math for a bounded landscape window. Source elevations never change. */
// Shared with the actual MapLibre constructor: detail actions must be reachable.
export const TERRAIN_DETAIL_MAX_ZOOM = 20;
export type TerrainFootprint = readonly [number, number, number, number];
export type TerrainViewport = Readonly<{center: readonly [number, number]; zoom: number; width: number; height: number}>;
const DEG = Math.PI / 180;
const EARTH = 6371008.8; // MapLibre's altitude-to-Mercator conversion radius.
const mercatorY = (latitude: number) => (1 - Math.log(Math.tan(Math.PI / 4 + latitude * DEG / 2)) / Math.PI) / 2;
const latitudeAt = (y: number) => Math.atan(Math.sinh(Math.PI * (1 - 2 * y))) / DEG;

/**
 * getBounds() includes the distant horizon in an oblique camera. Sample a local
 * map-scale window instead: a fixed 82% of the unpitched viewport, independent
 * of bearing/pitch. The 96² provider grid therefore keeps useful local detail
 * while rotating a scene does not create a different acquisition job.
 */
export function terrainViewFootprint(view: TerrainViewport, visible: TerrainFootprint): TerrainFootprint {
  const {center: [longitude, latitude], zoom, width, height} = view;
  if (![longitude, latitude, zoom, width, height, ...visible].every(Number.isFinite)
    || width < 1 || height < 1 || Math.abs(latitude) >= 85
    || longitude < visible[0] || longitude > visible[2] || latitude < visible[1] || latitude > visible[3]) return visible;
  const world = 512 * 2 ** zoom, halfX = width * .82 / (2 * world), halfY = height * .82 / (2 * world), y = mercatorY(latitude);
  return [longitude - halfX * 360, latitudeAt(y + halfY), longitude + halfX * 360, latitudeAt(y - halfY)];
}

/** Query ownership excludes orientation, but includes size, pan and zoom. */
export function sameTerrainFootprint(a: TerrainFootprint, b: TerrainFootprint): boolean {
  return a.every((value, index) => Math.abs(value - b[index]) <= 1e-7);
}

export type TerrainViewLease = Readonly<{bounds:TerrainFootprint;zoom:number;width:number;height:number;sourceZoom?:number}>;
/** Keep the acquired window fixed through small cumulative pans. Only its
 * central 65% is a navigation lease; it does not claim the new viewport is
 * covered. Zoom, resize and crossing that core always acquire a new window. */
export function terrainLeaseContains(lease:TerrainViewLease,view:TerrainViewport):boolean {
  if(![...lease.bounds,lease.zoom,lease.width,lease.height,...view.center,view.zoom,view.width,view.height].every(Number.isFinite)
    || Math.abs(lease.zoom-view.zoom)>1e-7 || lease.width!==view.width || lease.height!==view.height) return false;
  const [west,south,east,north]=lease.bounds,inset=.175;
  return west<east&&south<north&&view.center[0]>=west+(east-west)*inset&&view.center[0]<=east-(east-west)*inset
    &&view.center[1]>=south+(north-south)*inset&&view.center[1]<=north-(north-south)*inset;
}

/** Translate a display-scale acquisition window for a pan. In particular, a
 * fitted camera must not silently turn a detailed study into a coarse grid.
 * This defines a NEW request; old values are never moved or stretched. Zoom or
 * resize deliberately returns to viewport-based acquisition. */
export function terrainPanFootprint(lease:TerrainViewLease,view:TerrainViewport):TerrainFootprint|null {
  if(![...lease.bounds,lease.zoom,lease.width,lease.height,...view.center,view.zoom,view.width,view.height].every(Number.isFinite)
    || Math.abs(lease.zoom-view.zoom)>1e-7 || lease.width!==view.width || lease.height!==view.height || Math.abs(view.center[1])>=85) return null;
  const [west,south,east,north]=lease.bounds;
  if(west>=east||south>=north)return null;
  const halfX=(east-west)/2,halfY=(mercatorY(south)-mercatorY(north))/2,y=mercatorY(view.center[1]);
  return [view.center[0]-halfX,latitudeAt(y+halfY),view.center[0]+halfX,latitudeAt(y-halfY)];
}

export type TerrainInspection = Readonly<{
  corners: readonly (readonly [number, number])[]; heights: readonly number[]; scale: number;
  width: number; height: number; bearing: number; fieldOfView: number; centerElevation: number;
}>;
/**
 * Solve perspective inequalities for all eight corners of the height prism.
 * cameraForBounds uses the map's current pitch and can frame a distant horizon
 * when the requested inspection pitch differs. This fit uses the target pitch
 * explicitly and constrains the camera to remain above the scaled data tops.
 */
export function terrainInspectionCamera(input: TerrainInspection) {
  const {corners, heights, scale, width, height, bearing, fieldOfView} = input;
  if (corners.length < 4 || !heights.length || ![width, height, scale, bearing, fieldOfView, ...corners.flat()].every(Number.isFinite)
    || width < 160 || height < 160 || scale <= 0 || fieldOfView <= 0 || fieldOfView >= 90) throw Error('Map viewport unavailable');
  const west = Math.min(...corners.map(p => p[0])), east = Math.max(...corners.map(p => p[0]));
  const northY = Math.min(...corners.map(p => mercatorY(p[1]))), southY = Math.max(...corners.map(p => mercatorY(p[1])));
  const center: [number, number] = [(west + east) / 2, latitudeAt((northY + southY) / 2)];
  const metresPerWorld = 2 * Math.PI * EARTH * Math.cos(center[1] * DEG);
  const origin = Number.isFinite(input.centerElevation) ? input.centerElevation : 0;
  const pitch = 52, sine = Math.sin(pitch * DEG), cosine = Math.cos(pitch * DEG), angle = bearing * DEG;
  const focal = height / (2 * Math.tan(fieldOfView * DEG / 2));
  const availableX = width * .76 / 2 / focal, availableY = height * .70 / 2 / focal;
  let low=Infinity,high=-Infinity;
  for(const z of heights){if(!Number.isFinite(z))throw Error('Unsupported source height');low=Math.min(low,z*scale);high=Math.max(high,z*scale);}
  let distance = Math.max(100, high - origin + 80) / (metresPerWorld * cosine);
  for (const [longitude, latitude] of corners) {
    const eastOffset = (longitude - center[0]) / 360;
    const northOffset = (mercatorY(center[1]) - mercatorY(latitude));
    const x = eastOffset * Math.cos(angle) + northOffset * Math.sin(angle);
    const y = -eastOffset * Math.sin(angle) + northOffset * Math.cos(angle);
    for (const z of [low, high]) {
      const dz = (z - origin) / metresPerWorld;
      const depthOffset = y * sine - dz * cosine;
      const up = y * cosine + dz * sine;
      distance = Math.max(distance, Math.abs(x) / availableX - depthOffset, Math.abs(up) / availableY - depthOffset);
    }
  }
  const zoom = Math.min(18, Math.log2(focal / (512 * distance * 1.06)));
  if (!Number.isFinite(zoom)) throw Error('Footprint could not be framed');
  return {center, zoom, bearing, pitch};
}
