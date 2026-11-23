// County landing pages: one plain page per Kansas county, built from the Census county table the County
// Conditions lab already ships. app/county-facts.generated.json is written by scripts/prepare-county-pages.mjs.
import facts from "./county-facts.generated.json";

/** An estimate and its published or derived 90% margin of error. */
export type Estimate = [value: number, margin: number];
export type CountyPage = {
  fips: string; name: string; slug: string; center: [number, number];
  latest: { period: string; medianIncome: Estimate; medianAge: Estimate; medianHomeValue: Estimate; medianRent: Estimate; educationPct: Estimate; povertyPct: Estimate; ownerOccupiedPct: Estimate; housingUnits: Estimate };
  earlier: { period: string; medianAge: Estimate; educationPct: Estimate; povertyPct: Estimate; housingUnits: Estimate };
};

export const COUNTY_PAGES = facts.counties as unknown as readonly CountyPage[];
export const COUNTY_FACTS_SOURCE = facts.source;
const BY_SLUG = new Map(COUNTY_PAGES.map(county => [county.slug, county]));
export const countyPage = (slug: string): CountyPage | undefined => BY_SLUG.get(slug);
export const countyPath = (county: Pick<CountyPage, "slug">) => `/counties/${county.slug}`;
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
