export type BasemapKey = "midnight" | "prairie";

export type BasemapDescriptor = Readonly<{
  title: string;
  note: string;
}>;

export const BASEMAPS: Readonly<Record<BasemapKey, BasemapDescriptor>> = Object.freeze({
  midnight: Object.freeze({
    title: "Midnight navy",
    note: "Renderer-neutral high-contrast preference descriptor",
  }),
  prairie: Object.freeze({
    title: "Prairie dusk",
    note: "Renderer-neutral low-glare preference descriptor",
  }),
});

export type TileCoordinate = Readonly<{ z: number; x: number; y: number; label: string }>;

const radians = (degrees: number) => degrees * (Math.PI / 180);

export const lngLatToTile = (longitude: number, latitude: number, zoom: number): TileCoordinate => {
  const z = Math.max(0, Math.min(22, Math.floor(Number.isFinite(zoom) ? zoom : 0)));
  const lng = Math.max(-180, Math.min(180, Number.isFinite(longitude) ? longitude : 0));
  const lat = Math.max(-85.051129, Math.min(85.051129, Number.isFinite(latitude) ? latitude : 0));
  const tileCount = 2 ** z;
  const x = Math.max(0, Math.min(tileCount - 1, Math.floor(((lng + 180) / 360) * tileCount)));
  const latitudeRadians = radians(lat);
  const y = Math.max(0, Math.min(tileCount - 1, Math.floor(
    ((1 - Math.log(Math.tan(latitudeRadians) + (1 / Math.cos(latitudeRadians))) / Math.PI) / 2) * tileCount,
  )));
  return Object.freeze({ z, x, y, label: `${z}/${x}/${y}` });
};
