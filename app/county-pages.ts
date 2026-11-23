// County landing pages: one plain page per Kansas county, built from the Census county table the County
// Conditions lab already ships. app/county-facts.generated.json is written by scripts/prepare-county-pages.mjs.
import facts from "./county-facts.generated.json";

/** An estimate and its 90% margin of error, as the Census publishes or derives it. */
export type Estimate = [value: number, margin: number];
export type CountyPage = {
  fips: string; name: string; slug: string; center: [number, number];
  latest: { period: string; medianIncome: Estimate; medianAge: Estimate; medianHomeValue: Estimate; medianRent: Estimate; educationPct: Estimate; povertyPct: Estimate; ownerOccupiedPct: Estimate; housingUnits: Estimate };
  earlier: { period: string; medianAge: number; educationPct: number; povertyPct: number; housingUnits: number };
};

export const COUNTY_PAGES = facts.counties as unknown as readonly CountyPage[];
export const COUNTY_FACTS_SOURCE = facts.source;
const BY_SLUG = new Map(COUNTY_PAGES.map(county => [county.slug, county]));
export const countyPage = (slug: string): CountyPage | undefined => BY_SLUG.get(slug);
export const countyPath = (county: Pick<CountyPage, "slug">) => `/counties/${county.slug}`;
/** The map centred on the county with the county outlines switched on. */
export const countyMapHref = (county: Pick<CountyPage, "center">) => `/?ctx=census-counties&c=${county.center[0]},${county.center[1]}&z=8.5`;

const whole = new Intl.NumberFormat("en-US", { maximumFractionDigits: 0 });
export const dollars = ([value, margin]: Estimate) => `$${whole.format(value)} (±$${whole.format(margin)})`;
export const percent = ([value, margin]: Estimate) => `${value.toFixed(1)}% (±${margin.toFixed(1)})`;
export const count = ([value, margin]: Estimate) => `${whole.format(value)} (±${whole.format(margin)})`;
export const years = ([value, margin]: Estimate) => `${value.toFixed(1)} years (±${margin.toFixed(1)})`;

/**
 * "up from 16.1%" / "down from 18.0%" / "about the same as" for a later and an earlier percentage. The earlier
 * estimate has its own margin of error, so a difference inside the later margin is not called a change.
 */
export function comparedWith([value, margin]: Estimate, earlier: number, unit: "%" | " years"): string {
  const was = `${earlier.toFixed(1)}${unit}`;
  if (Math.abs(value - earlier) <= margin) return `about the same as ${was}`;
  return `${value > earlier ? "up" : "down"} from ${was}`;
}
