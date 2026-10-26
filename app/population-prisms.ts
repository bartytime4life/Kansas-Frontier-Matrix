import type { ExpressionSpecification, LayerSpecification, Map as MapLibreMap } from "./maplibre-seam";

/**
 * Kansas population density peer groups, as the Kansas Department of Health
 * and Environment classifies counties: people per square mile of land area.
 * Lower bounds are inclusive.
 */
export const KANSAS_DENSITY_GROUPS = Object.freeze([
  Object.freeze({ id: "frontier", label: "Frontier", min: 0, range: "under 6", color: "#ddd3ec" }),
  Object.freeze({ id: "rural", label: "Rural", min: 6, range: "6–19.9", color: "#b9a6da" }),
  Object.freeze({ id: "densely-settled-rural", label: "Densely-settled rural", min: 20, range: "20–39.9", color: "#9378c2" }),
  Object.freeze({ id: "semi-urban", label: "Semi-urban", min: 40, range: "40–149.9", color: "#6b4ca3" }),
  Object.freeze({ id: "urban", label: "Urban", min: 150, range: "150 and over", color: "#3f2470" }),
] as const);
export type KansasDensityGroup = (typeof KANSAS_DENSITY_GROUPS)[number];

/** Prism height: 100 m for every person per square mile of land, on a linear scale. */
export const PRISM_METRES_PER_PERSON_PER_SQUARE_MILE = 100;
export const POPULATION_PRISM_LAYER_ID = "external-census-counties-population-prisms";

/** People per square mile of land, or null when either count is missing. */
export function peoplePerSquareMile(population: unknown, landSquareMiles: unknown): number | null {
  return typeof population === "number" && Number.isFinite(population) && population >= 0
    && typeof landSquareMiles === "number" && Number.isFinite(landSquareMiles) && landSquareMiles > 0
    ? population / landSquareMiles : null;
}

export function kansasDensityGroup(density: number): KansasDensityGroup {
  return [...KANSAS_DENSITY_GROUPS].reverse().find(group => density >= group.min) ?? KANSAS_DENSITY_GROUPS[0];
}

/** How many counties fall in each group, and the state's own density, from the county payload. */
export function densityGroupCounts(features: readonly { properties?: Record<string, unknown> | null }[]): Readonly<{
  groups: readonly (KansasDensityGroup & { count: number })[]; counties: number; statewide: number | null;
}> {
  const counts = new Map<string, number>();
  let people = 0, land = 0, counties = 0;
  for (const feature of features) {
    const density = peoplePerSquareMile(feature.properties?.population, feature.properties?.landSquareMiles);
    if (density === null) continue;
    counties++;
    people += feature.properties!.population as number;
    land += feature.properties!.landSquareMiles as number;
    const group = kansasDensityGroup(density);
    counts.set(group.id, (counts.get(group.id) ?? 0) + 1);
  }
  return { groups: KANSAS_DENSITY_GROUPS.map(group => ({ ...group, count: counts.get(group.id) ?? 0 })), counties, statewide: land > 0 ? people / land : null };
}

const density: ExpressionSpecification = ["/", ["to-number", ["get", "population"]], ["to-number", ["get", "landSquareMiles"]]];
const groupColor: ExpressionSpecification = ["step", density, KANSAS_DENSITY_GROUPS[0].color,
  ...KANSAS_DENSITY_GROUPS.slice(1).flatMap(group => [group.min, group.color])] as unknown as ExpressionSpecification;

/** One prism per county: height proportional to density, colour by density group. */
export const populationPrismLayer = (sourceId: string): LayerSpecification => ({
  id: POPULATION_PRISM_LAYER_ID,
  type: "fill-extrusion",
  source: sourceId,
  filter: ["all", ["==", ["typeof", ["get", "population"]], "number"], ["==", ["typeof", ["get", "landSquareMiles"]], "number"], [">", ["get", "landSquareMiles"], 0]],
  paint: {
    "fill-extrusion-color": groupColor,
    "fill-extrusion-height": ["*", density, PRISM_METRES_PER_PERSON_PER_SQUARE_MILE],
    "fill-extrusion-base": 0,
    "fill-extrusion-opacity": 0.9,
    "fill-extrusion-vertical-gradient": true,
  },
});

const prismsOn = new WeakMap<MapLibreMap, boolean>();
/** Whether this map draws the county prisms; the context renderer reads it on each pass. */
export const setPopulationPrisms = (map: MapLibreMap, on: boolean): void => { prismsOn.set(map, on); };
export const populationPrismsOn = (map: MapLibreMap): boolean => prismsOn.get(map) === true;
