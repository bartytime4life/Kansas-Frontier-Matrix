// County landing pages: one plain page per Kansas county, built from three bundles the labs already ship
// (Census survey estimates, Census population estimates, the KDOT bridge inventory).
// app/county-facts.generated.json is written by scripts/prepare-county-pages.mjs.
import facts from "./county-facts.generated.json";

/** An estimate and its published or derived 90% margin of error. */
export type Estimate = [value: number, margin: number];
export type CountyPage = {
  fips: string; name: string; slug: string; center: [number, number];
  /** July 1 Census population estimates for the newest year and the first year of the same vintage. */
  population: { year: number; value: number; baseYear: number; baseValue: number };
  /** Counts of KDOT inventory records, which are not always one physical bridge each. */
  bridges: { records: number; state: number; local: number; closed: number; register: number; oldestYear: number | null; longestFt: number | null };
  latest: { period: string; medianIncome: Estimate; medianAge: Estimate; medianHomeValue: Estimate; medianRent: Estimate; educationPct: Estimate; povertyPct: Estimate; ownerOccupiedPct: Estimate; housingUnits: Estimate };
  earlier: { period: string; medianAge: Estimate; educationPct: Estimate; povertyPct: Estimate; housingUnits: Estimate };
};

export const COUNTY_PAGES = facts.counties as unknown as readonly CountyPage[];
export const COUNTY_FACTS_SOURCE = facts.source;
export const COUNTY_FACTS_SOURCES = facts.sources;
const BY_SLUG = new Map(COUNTY_PAGES.map(county => [county.slug, county]));
export const countyPage = (slug: string): CountyPage | undefined => BY_SLUG.get(slug);
export const countyPath = (county: Pick<CountyPage, "slug">) => `/counties/${county.slug}`;
/** The map centred on the county with the county outlines and both KDOT bridge layers switched on. */
export const countyBridgesHref = (county: Pick<CountyPage, "center">) => `/?ctx=census-counties,kdot-bridges-state,kdot-bridges-local&c=${county.center[0]},${county.center[1]}&z=9.5`;
/** The map centred on the county with the county outlines switched on. */
export const countyMapHref = (county: Pick<CountyPage, "center">) => `/?ctx=census-counties&c=${county.center[0]},${county.center[1]}&z=8.5`;
export const countyObservatoryHref = (county: Pick<CountyPage, "fips">) => `/labs/observatory?county=${county.fips}`;

const whole = new Intl.NumberFormat("en-US", { maximumFractionDigits: 0 });
export const dollars = ([value, margin]: Estimate) => `$${whole.format(value)} (±$${whole.format(margin)})`;
export const percent = ([value, margin]: Estimate) => `${value.toFixed(1)}% (±${margin.toFixed(1)})`;
export const count = ([value, margin]: Estimate) => `${whole.format(value)} (±${whole.format(margin)})`;
export const years = ([value, margin]: Estimate) => `${value.toFixed(1)} years (±${margin.toFixed(1)})`;

/** ACS comparison for nonoverlapping periods, using both estimates' 90% margins. */
export function comparedWith([value, margin]: Estimate, [earlierValue, earlierMargin]: Estimate, period: string): string {
  const difference = value - earlierValue;
  if (Math.abs(difference) <= Math.hypot(margin, earlierMargin)) return "Difference uncertain";
  return `${difference > 0 ? "Higher" : "Lower"} in ${period}`;
}

export const number = (value: number) => whole.format(value);
/** ["13,602 more than", "up 2.6%"] / ["231 fewer than", "down 1.8%"] / ["the same as", null]: the two estimates side by side, with no claim about why. */
export function populationChange({ value, baseValue }: CountyPage["population"]): [relation: string, share: string | null] {
  const difference = value - baseValue;
  if (difference === 0) return ["the same as", null];
  const share = Math.abs(difference) / baseValue * 100;
  return [`${whole.format(Math.abs(difference))} ${difference > 0 ? "more" : "fewer"} than`, `${difference > 0 ? "up" : "down"} ${share < 0.05 ? "less than 0.1" : share.toFixed(1)}%`];
}
