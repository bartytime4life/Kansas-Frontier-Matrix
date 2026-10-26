/**
 * Keys of the category basemaps in app/category-basemaps.ts. Kept free of
 * imports so allow-lists (saved views, wind-arrow contrast, report
 * attribution) can share them without pulling in style code.
 */
export const CATEGORY_BASEMAP_KEYS = Object.freeze(["aviation-chart", "civic", "hydro", "relief", "storm", "network", "historic"] as const);
export type CategoryBasemapKey = (typeof CATEGORY_BASEMAP_KEYS)[number];

/** Light-ground category basemaps; overlays drawn on them need dark strokes. */
export const LIGHT_CATEGORY_BASEMAPS: readonly CategoryBasemapKey[] = Object.freeze(["aviation-chart", "civic", "relief", "network", "historic"]);

export const isCategoryBasemapKey = (value: unknown): value is CategoryBasemapKey =>
  typeof value === "string" && (CATEGORY_BASEMAP_KEYS as readonly string[]).includes(value);
