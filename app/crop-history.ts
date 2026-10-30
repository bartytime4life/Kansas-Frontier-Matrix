import { CDL_FIRST_YEAR, CDL_LATEST_YEAR, CDL_MAIN_CLASSES, type CdlValue } from "./cropland";
import type { MapKey } from "./map-keys";

/**
 * A field's crop history: what the USDA Cropland Data Layer recorded at one 30 m
 * cell each year since 2008, grouped into crop families and read for a pattern.
 * The pattern describes what was recorded. It is not agronomic advice, and the
 * CDL's classification is less certain for minor crops and in small fields.
 */

export const CROP_HISTORY_API_PATH = (lon: number, lat: number) => `/api/cropland/history?lon=${lon.toFixed(5)}&lat=${lat.toFixed(5)}`;
/** Fewer classified years than this and no pattern is read. */
export const MIN_YEARS_FOR_PATTERN = 5;

export type CropFamily = "corn" | "sorghum" | "soybeans" | "sunflower" | "wheat" | "double-crop" | "hay" | "fallow" | "grass" | "other";
/** Each family with its label and its colour: the CDL's own class colour where the class is a main crop on the map. */
export const CROP_FAMILIES: Readonly<Record<CropFamily, Readonly<{ label: string; color: string }>>> = Object.freeze({
  corn: { label: "corn", color: "#ffd300" },
  sorghum: { label: "sorghum", color: "#ff9e0b" },
  soybeans: { label: "soybeans", color: "#267000" },
  sunflower: { label: "sunflower", color: "#ffff00" },
  wheat: { label: "winter wheat", color: "#a87000" },
  "double-crop": { label: "double-crop wheat and soybeans", color: "#707000" },
  hay: { label: "alfalfa or hay", color: "#ffa5e2" },
  fallow: { label: "fallow", color: "#bfbf77" },
  grass: { label: "grassland or pasture", color: "#e8ffbf" },
  other: { label: "other classes", color: "#8a8a8a" },
});
const CODE_FAMILY: Readonly<Record<number, CropFamily>> = Object.freeze({ 1: "corn", 4: "sorghum", 5: "soybeans", 6: "sunflower", 24: "wheat", 26: "double-crop", 36: "hay", 61: "fallow", 176: "grass" });
/** A crop family for a CDL class code. Codes not named here are other classes (forest, water, development and the rest). */
export const familyOf = (code: number): CropFamily => CODE_FAMILY[code] ?? "other";
// The families' colours must agree with the map's own legend where they overlap.
for (const entry of CDL_MAIN_CLASSES) {
  const family = familyOf(entry.value);
  if (family !== "other" && CROP_FAMILIES[family].color !== entry.color) throw new Error(`Crop family colour for ${entry.name} differs from the map.`);
}

export type CropHistoryYear = Readonly<{ year: number; state: "ready" | "none" | "failed"; crop: CdlValue | null }>;
export type CropHistory = Readonly<{ lon: number; lat: number; retrievedAt: string; years: readonly CropHistoryYear[] }>;

export function validCropHistory(value: unknown, lon: number, lat: number): value is CropHistory {
  if (!value || typeof value !== "object") return false;
  const v = value as { lon?: unknown; lat?: unknown; years?: unknown };
  return v.lon === lon && v.lat === lat && Array.isArray(v.years) && v.years.every(y => y && typeof y === "object"
    && typeof (y as CropHistoryYear).year === "number" && ["ready", "none", "failed"].includes((y as CropHistoryYear).state));
}

export type RotationPattern = Readonly<{
  label: string;
  detail: string;
  /** Years with a classified crop, the basis of the pattern. */
  classified: number;
  /** Years CropScape did not answer for. */
  failed: number;
  counts: Readonly<Partial<Record<CropFamily, number>>>;
  changes: number;
}>;

const pct = (n: number, d: number) => `${Math.round(n / d * 100)}%`;
const FAMILY_NAMES = Object.keys(CROP_FAMILIES) as CropFamily[];

/**
 * The pattern of a field's classified years, in four readings:
 * - continuous corn, when corn is at least 80% of the years;
 * - grassland or pasture, when grass is at least 80%;
 * - corn–soybean rotation, when both appear at least 25% of the time and at least 60% of their back-to-back years alternate;
 * - otherwise the dominant family, when it is at least 60%, or mixed cropping.
 */
export function rotationPattern(years: readonly CropHistoryYear[]): RotationPattern {
  const classifiedYears = years.filter(y => y.crop !== null).sort((a, b) => a.year - b.year);
  const failed = years.filter(y => y.state === "failed").length;
  const families = classifiedYears.map(y => familyOf(y.crop!.value));
  const counts: Partial<Record<CropFamily, number>> = {};
  for (const f of families) counts[f] = (counts[f] ?? 0) + 1;
  const n = families.length;
  const countOf = (f: CropFamily) => counts[f] ?? 0;
  // Changes of crop between consecutive classified years, and how many of the corn/soybean pairs alternate.
  let changes = 0, cornSoyPairs = 0, cornSoyAlternating = 0;
  for (let i = 1; i < n; i++) {
    const a = families[i - 1], b = families[i];
    if (a !== b) changes++;
    if ((a === "corn" || a === "soybeans") && (b === "corn" || b === "soybeans")) {
      cornSoyPairs++;
      if (a !== b) cornSoyAlternating++;
    }
  }
  const summary = FAMILY_NAMES.filter(f => countOf(f) > 0).map(f => `${CROP_FAMILIES[f].label} ${countOf(f)}`).join(", ");
  const base = `${n} years read${failed ? `, ${failed} unanswered` : ""} · ${summary} · ${changes} change${changes === 1 ? "" : "s"} of crop`;
  const common = { classified: n, failed, counts, changes };
  if (n < MIN_YEARS_FOR_PATTERN) return { ...common, label: "Too few years to read a pattern", detail: base };
  const dominant = FAMILY_NAMES.reduce((a, b) => countOf(b) > countOf(a) ? b : a, "other" as CropFamily);
  if (countOf("corn") / n >= 0.8) return { ...common, label: "Continuous corn", detail: `Corn in ${pct(countOf("corn"), n)} of years · ${base}` };
  if (countOf("grass") / n >= 0.8) return { ...common, label: "Grassland or pasture", detail: `Grass in ${pct(countOf("grass"), n)} of years · ${base}` };
  if (countOf("corn") / n >= 0.25 && countOf("soybeans") / n >= 0.25 && cornSoyPairs >= 3 && cornSoyAlternating / cornSoyPairs >= 0.6)
    return { ...common, label: "Corn–soybean rotation", detail: `${cornSoyAlternating} of ${cornSoyPairs} corn and soybean years alternate · ${base}` };
  if (countOf(dominant) / n >= 0.6) return { ...common, label: `Mostly ${CROP_FAMILIES[dominant].label}`, detail: `${CROP_FAMILIES[dominant].label} in ${pct(countOf(dominant), n)} of years · ${base}` };
  return { ...common, label: "Mixed cropping", detail: base };
}

/** The timeline's bars: one per year since the first CDL year, a family where classified, and the state where not. */
export function historyBars(history: CropHistory): readonly Readonly<{ year: number; family: CropFamily | null; state: CropHistoryYear["state"]; label: string }>[] {
  return history.years.map(y => {
    const family = y.crop ? familyOf(y.crop.value) : null;
    const label = y.state === "failed" ? "not answered" : y.state === "none" || !y.crop ? "no class here" : `${CROP_FAMILIES[family!].label} (${y.crop.value})`;
    return { year: y.year, family, state: y.state, label };
  });
}

/** The point's line: where it is and the pattern read from its years. */
export function cropHistoryReading(history: CropHistory, pattern: RotationPattern): string {
  const coordinate = `${Math.abs(history.lat).toFixed(3)}°${history.lat >= 0 ? "N" : "S"}, ${Math.abs(history.lon).toFixed(3)}°${history.lon >= 0 ? "E" : "W"}`;
  return `${pattern.label} at ${coordinate} · ${CDL_FIRST_YEAR}–${CDL_LATEST_YEAR} · ${pattern.detail}`;
}

export function cropHistoryKey(): MapKey {
  return Object.freeze({
    id: "crop-history",
    title: `Crop history at a point · ${CDL_FIRST_YEAR}–${CDL_LATEST_YEAR}`,
    items: Object.freeze(FAMILY_NAMES.filter(f => f !== "other").map(f => Object.freeze({ label: CROP_FAMILIES[f].label, color: CROP_FAMILIES[f].color, shape: "area" as const }))),
    note: "USDA NASS Cropland Data Layer classes for the 30 m cell at one point, each year. A pattern describes what was recorded, not what should be planted; the classification is less certain for minor crops and small fields.",
  });
}
