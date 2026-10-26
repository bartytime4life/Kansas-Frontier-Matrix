/**
 * Real Kansas landscapes for the photo-real 3D view: the 2024 one-foot aerial
 * draped on the USGS 3DEP bare-earth DEM at true vertical scale. Each caption
 * says what the ground is, in terms a geologist or ecologist would accept;
 * the camera frames the landform itself.
 */
export type PhotorealLandscape = Readonly<{
  id: string;
  name: string;
  caption: string;
  camera: Readonly<{ center: readonly [number, number]; zoom: number; pitch: number; bearing: number }>;
}>;

const place = (id: string, name: string, caption: string, center: readonly [number, number], zoom: number, pitch: number, bearing: number): PhotorealLandscape =>
  Object.freeze({ id, name, caption, camera: Object.freeze({ center, zoom, pitch, bearing }) });

export const PHOTOREAL_LANDSCAPES: readonly PhotorealLandscape[] = Object.freeze([
  place("red-hills", "Red Hills · Barber County", "Permian red beds capped by gypsum, eroded into buttes and mesas west of Medicine Lodge.", [-98.73, 37.21], 13.4, 70, 30),
  place("monument-rocks", "Monument Rocks · Gove County", "Pillars of Late Cretaceous Niobrara Chalk, laid down on the floor of an inland sea, standing above the plains.", [-100.763, 38.793], 15.6, 72, -20),
  place("little-jerusalem", "Little Jerusalem Badlands · Logan County", "Niobrara Chalk eroded into spires and ravines; a Kansas state park since 2019.", [-100.945, 38.79], 14.6, 70, 15),
  place("konza", "Konza Prairie · Flint Hills", "Permian limestone and chert (flint) beds under unplowed tallgrass prairie; a long-term ecological research site.", [-96.585, 39.09], 13.2, 68, -35),
  place("arikaree", "Arikaree Breaks · Cheyenne County", "Canyons eroded into thick wind-blown loess near the Colorado and Nebraska lines.", [-101.86, 39.93], 13, 70, 10),
  place("wichita", "Downtown Wichita · Arkansas River", "Buildings at their OpenStreetMap heights beside the Arkansas River, on the 2024 Kansas flight.", [-97.338, 37.687], 15.6, 68, -30),
]);
