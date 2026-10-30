/**
 * The SSURGO soil-map unit at a clicked point, as the Field view shows it beside the crop history. Components are
 * alternatives within the mapped area, with their share of it; they do not identify the soil at the point itself.
 */

export const SOIL_API_PATH = (lon: number, lat: number) => `/api/cropland/soil?lon=${lon.toFixed(5)}&lat=${lat.toFixed(5)}`;

export type SoilComponent = Readonly<{
  name: string;
  percent: number | null;
  major: boolean;
  drainage: string | null;
  hydrologicGroup: string | null;
  capability: number | null;
}>;
export type SoilReading = Readonly<{
  lon: number;
  lat: number;
  retrievedAt: string;
  state: "ready" | "none";
  mapUnit: Readonly<{ key: string; name: string; waterStorageCm: number | null }> | null;
  components: readonly SoilComponent[];
}>;

const text = (value: unknown) => value === null || typeof value === "string";
const number = (value: unknown) => value === null || typeof value === "number";

export function validSoil(value: unknown, lon: number, lat: number): value is SoilReading {
  if (!value || typeof value !== "object") return false;
  const v = value as Partial<SoilReading>;
  const unit = v.mapUnit;
  return v.lon === lon && v.lat === lat && (v.state === "ready" || v.state === "none") && Array.isArray(v.components)
    && (unit === null || (typeof unit === "object" && typeof unit.key === "string" && typeof unit.name === "string" && number(unit.waterStorageCm)))
    && v.components.every(c => c && typeof c === "object" && typeof c.name === "string" && number(c.percent) && typeof c.major === "boolean"
      && text(c.drainage) && text(c.hydrologicGroup) && number(c.capability));
}

/** The non-irrigated capability class: 1 has the fewest limitations, 8 the most. */
const capability = (value: number) => `class ${value} of 8`;

/** The map unit's water storage to 150 cm: a weighted average over its components, shown once for the unit. */
export function soilWater(mapUnit: Readonly<{ waterStorageCm: number | null }> | null): string | null {
  return mapUnit?.waterStorageCm == null ? null : `${mapUnit.waterStorageCm.toFixed(1)} cm of water to 150 cm, averaged over the map unit`;
}

/** A component as one line for the dock: its share, drainage, hydrologic group and capability. */
export function soilLine(component: SoilComponent): string {
  const parts = [
    component.percent === null ? null : `${Math.round(component.percent)}% of the map unit`,
    component.drainage ? `${component.drainage.toLowerCase()} drainage` : null,
    component.hydrologicGroup ? `hydrologic group ${component.hydrologicGroup}` : null,
    component.capability === null ? null : `non-irrigated capability ${capability(component.capability)}`,
  ].filter(Boolean);
  return parts.join(" · ");
}
