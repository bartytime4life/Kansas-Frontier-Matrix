import type { Feature, Geometry } from "geojson";

export type FireNeighbor = Readonly<{ name: string; distanceKm: number; eventTime: string | null }>;

const point = (feature: Feature<Geometry> | null | undefined): [number, number] | null => {
  if (feature?.geometry?.type !== "Point") return null;
  const [longitude, latitude] = feature.geometry.coordinates;
  return Number.isFinite(longitude) && Number.isFinite(latitude) ? [longitude, latitude] : null;
};

const distanceKm = (left: [number, number], right: [number, number]) => {
  const rad = Math.PI / 180;
  const deltaLat = (right[1] - left[1]) * rad;
  const deltaLng = (right[0] - left[0]) * rad;
  const a = Math.sin(deltaLat / 2) ** 2 + Math.cos(left[1] * rad) * Math.cos(right[1] * rad) * Math.sin(deltaLng / 2) ** 2;
  return 6371 * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
};

/** Spatial comparison only. A nearby point cannot establish event identity. */
export const nearbyFireContext = (selected: Feature<Geometry> | null | undefined, candidates: readonly Feature<Geometry>[], timeKey: "acquiredAt" | "discoveryAt", radiusKm = 10): readonly FireNeighbor[] => {
  const origin = point(selected);
  if (!origin) return [];
  return candidates.flatMap((candidate) => {
    const coordinates = point(candidate);
    if (!coordinates) return [];
    const distance = distanceKm(origin, coordinates);
    if (distance > radiusKm) return [];
    const properties = candidate.properties ?? {};
    const time = properties[timeKey];
    return [{
      name: typeof properties.name === "string" ? properties.name.slice(0, 120) : "Unnamed record",
      distanceKm: distance,
      eventTime: typeof time === "string" && Number.isFinite(Date.parse(time)) ? time : null,
    }];
  }).sort((left, right) => left.distanceKm - right.distanceKm).slice(0, 3);
};
