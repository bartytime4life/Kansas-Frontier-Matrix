export type AnalysisRecipe = Readonly<{
  id: string;
  eyebrow: string;
  title: string;
  summary: string;
  year: number;
  layerIds: readonly string[];
  center: readonly [number, number];
  zoom: number;
  basemap: "midnight" | "prairie";
  scope: "VIEWPORT" | "VISIBLE_LAYERS";
  detail: "EXECUTIVE" | "STANDARD" | "TECHNICAL";
}>;

export const ANALYSIS_RECIPES: readonly AnalysisRecipe[] = Object.freeze([
  Object.freeze({
    id: "statewide-brief",
    eyebrow: "STATEWIDE",
    title: "Kansas context brief",
    summary: "A balanced statewide view of county locators, water, ecology, atmosphere, communities, and movement context.",
    year: 2026,
    layerIds: Object.freeze(["kansas-extent", "county-starter-points", "watershed-context", "water-context", "prairie-context", "atmosphere-observations", "communities", "transport-context"]),
    center: Object.freeze([-98.38, 38.48]) as readonly [number, number],
    zoom: 5.45,
    basemap: "midnight",
    scope: "VISIBLE_LAYERS",
    detail: "STANDARD",
  }),
  Object.freeze({
    id: "central-kansas",
    eyebrow: "REGIONAL",
    title: "Central Kansas context",
    summary: "Center on the Ellsworth–Salina region and combine county locators, water, agriculture, communities, and movement fixtures.",
    year: 2026,
    layerIds: Object.freeze(["kansas-extent", "county-starter-points", "watershed-context", "water-context", "agriculture-context", "communities", "transport-context"]),
    center: Object.freeze([-98.23, 38.73]) as readonly [number, number],
    zoom: 7.15,
    basemap: "prairie",
    scope: "VIEWPORT",
    detail: "STANDARD",
  }),
  Object.freeze({
    id: "water-communities",
    eyebrow: "HYDROLOGY",
    title: "Watershed systems brief",
    summary: "Inspect synthetic basin envelopes and directional water styling beside community points and visible evidence-state differences.",
    year: 2026,
    layerIds: Object.freeze(["kansas-extent", "county-starter-points", "watershed-context", "water-context", "communities"]),
    center: Object.freeze([-98.25, 38.55]) as readonly [number, number],
    zoom: 6.05,
    basemap: "midnight",
    scope: "VISIBLE_LAYERS",
    detail: "STANDARD",
  }),
  Object.freeze({
    id: "smoke-context",
    eyebrow: "ATMOSPHERE",
    title: "Smoke context timeline",
    summary: "Review synthetic 2026 smoke context beside atmosphere, watershed, and community fixtures without current-condition or health claims.",
    year: 2026,
    layerIds: Object.freeze(["kansas-extent", "county-starter-points", "watershed-context", "smoke-context", "atmosphere-observations", "communities"]),
    center: Object.freeze([-97.05, 38.65]) as readonly [number, number],
    zoom: 6.0,
    basemap: "midnight",
    scope: "VISIBLE_LAYERS",
    detail: "TECHNICAL",
  }),
  Object.freeze({
    id: "elevation-concept",
    eyebrow: "3D CONCEPT",
    title: "Elevation display brief",
    summary: "Pair invented relative-height bands with watershed and water context while keeping the DEM and terrain hold explicit.",
    year: 2026,
    layerIds: Object.freeze(["kansas-extent", "county-starter-points", "watershed-context", "water-context", "elevation-concept", "communities"]),
    center: Object.freeze([-98.38, 38.48]) as readonly [number, number],
    zoom: 5.8,
    basemap: "prairie",
    scope: "VISIBLE_LAYERS",
    detail: "TECHNICAL",
  }),
  Object.freeze({
    id: "agriculture-context",
    eyebrow: "CROSS-DOMAIN",
    title: "Agriculture context report",
    summary: "Compare coarse agriculture regions with hydrology, habitat, community, and transport context.",
    year: 2026,
    layerIds: Object.freeze(["kansas-extent", "county-starter-points", "agriculture-context", "watershed-context", "water-context", "prairie-context", "communities", "transport-context"]),
    center: Object.freeze([-98.45, 38.35]) as readonly [number, number],
    zoom: 5.8,
    basemap: "prairie",
    scope: "VISIBLE_LAYERS",
    detail: "TECHNICAL",
  }),
  Object.freeze({
    id: "historical-vintage",
    eyebrow: "TIME",
    title: "1910 historical-vintage review",
    summary: "Reveal the 1910 study line beside movement and community context without treating the line as a historical claim.",
    year: 1910,
    layerIds: Object.freeze(["kansas-extent", "county-starter-points", "historical-context", "transport-context", "communities"]),
    center: Object.freeze([-98.7, 37.85]) as readonly [number, number],
    zoom: 6.1,
    basemap: "prairie",
    scope: "VISIBLE_LAYERS",
    detail: "STANDARD",
  }),
  Object.freeze({
    id: "evidence-audit",
    eyebrow: "TRUST",
    title: "Evidence-state audit",
    summary: "Bring supported, corrected, missing, stale, restricted, denied, generalized, and error fixtures into one review surface.",
    year: 2026,
    layerIds: Object.freeze(["county-starter-points", "water-context", "agriculture-context", "atmosphere-observations", "public-safe-planning", "review-diagnostics"]),
    center: Object.freeze([-97.65, 38.55]) as readonly [number, number],
    zoom: 5.75,
    basemap: "midnight",
    scope: "VISIBLE_LAYERS",
    detail: "TECHNICAL",
  }),
]);
