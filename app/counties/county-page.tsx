import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { PUBLIC_SITE_ORIGIN } from "../crawler-discovery";
import {
  COUNTY_FACTS_SOURCES, COUNTY_PAGES, comparedWith, count, countyBridgesHref, countyMapHref,
  countyObservatoryHref, countyPage, countyPath, dollars, number, percent, populationChange, years,
} from "../county-pages";
import { LANDING_GUIDES } from "../landing-guides";
import explore from "../explore/explore.module.css";
import styles from "./counties.module.css";

const description = (name: string, period: string) =>
  `${name}, Kansas at a glance: population, household income, age, home values, rent, education and poverty from the Census Bureau (${period} survey), its bridges in the KDOT inventory, and a map of the county.`;

export function countyMetadata(slug: string): Metadata {
  const county = countyPage(slug);
  if (!county) return {};
  const url = `${PUBLIC_SITE_ORIGIN}${countyPath(county)}`, title = `${county.name}, Kansas`;
  const text = description(county.name, county.latest.period);
  return {
    title: `${title} · Kansas Frontier Matrix`, description: text, alternates: { canonical: url },
    openGraph: { title, description: text, url, type: "website", images: [{ url: `${PUBLIC_SITE_ORIGIN}/og-guided.png`, width: 1731, height: 909, alt: "Kansas Frontier Matrix map" }] },
    twitter: { card: "summary_large_image", title, description: text, images: [`${PUBLIC_SITE_ORIGIN}/og-guided.png`] },
  };
}

export function CountyPage({ slug }: { slug: string }) {
  const county = countyPage(slug);
  if (!county) notFound();
  const { latest, earlier, population, bridges } = county, href = countyMapHref(county);
  const [relation, share] = populationChange(population);
  const position = COUNTY_PAGES.indexOf(county);
  const before = COUNTY_PAGES[(position + COUNTY_PAGES.length - 1) % COUNTY_PAGES.length], after = COUNTY_PAGES[(position + 1) % COUNTY_PAGES.length];
  return <main className={explore.page}>
    <header className={explore.header}><Link href="/">← Kansas map</Link><Link href="/counties">All 105 counties</Link></header>
    <article className={explore.article}>
      <p className={explore.kicker}>Kansas county · FIPS {county.fips}</p>
      <h1>{county.name}, Kansas</h1>
      <p>The Census Bureau estimates that <strong>{number(population.value)}</strong> people lived in {county.name} on July 1, {population.year}. That is {relation} its estimate of {number(population.baseValue)} for July 1, {population.baseYear}{share && ` (${share})`}.</p>
      <p><a className={explore.cta} href={href}>Open the map on {county.name} →</a></p>
      <h2>At a glance, {latest.period}</h2>
      <p>The ± value shows the 90% margin of error for American Community Survey estimates.</p>
      <ul className={styles.facts}>
        <li><span>Median household income</span><strong>{dollars(latest.medianIncome)}</strong><em>in {latest.period.slice(-4)} dollars</em></li>
        <li><span>Median age</span><strong>{years(latest.medianAge)}</strong><em>{earlier.period} estimate {years(earlier.medianAge)}<br />{comparedWith(latest.medianAge, earlier.medianAge, latest.period)}</em></li>
        <li><span>Median home value</span><strong>{dollars(latest.medianHomeValue)}</strong><em>owner-occupied homes</em></li>
        <li><span>Median rent</span><strong>{dollars(latest.medianRent)}</strong><em>per month, with utilities</em></li>
        <li><span>Adults 25 and over with a bachelor&rsquo;s degree or higher</span><strong>{percent(latest.educationPct)}</strong><em>{earlier.period} estimate {percent(earlier.educationPct)}<br />{comparedWith(latest.educationPct, earlier.educationPct, latest.period)}</em></li>
        <li><span>People below the poverty line</span><strong>{percent(latest.povertyPct)}</strong><em>{earlier.period} estimate {percent(earlier.povertyPct)}<br />{comparedWith(latest.povertyPct, earlier.povertyPct, latest.period)}</em></li>
        <li><span>Homes lived in by their owner</span><strong>{percent(latest.ownerOccupiedPct)}</strong><em>of occupied homes</em></li>
        <li><span>Housing units</span><strong>{count(latest.housingUnits)}</strong><em>{earlier.period} estimate {count(earlier.housingUnits)}</em></li>
      </ul>
      <h2>Bridges</h2>
      <p>The Kansas Department of Transportation&rsquo;s bridge inventory lists <strong>{number(bridges.records)}</strong> bridge records in {county.name}: {number(bridges.state)} on state highways and {number(bridges.local)} on local roads.{bridges.oldestYear !== null && <> The oldest recorded built year is {bridges.oldestYear}.</>}{bridges.longestFt !== null && <> The longest structure is {number(bridges.longestFt)} feet.</>}</p>
      <p>{bridges.closed === 0 ? "None is recorded as closed to traffic." : `${number(bridges.closed)} ${bridges.closed === 1 ? "is" : "are"} recorded as closed to traffic.`}{bridges.register > 0 && ` ${number(bridges.register)} local-road ${bridges.register === 1 ? "bridge is" : "bridges are"} marked as on the National Register of Historic Places.`}</p>
      <p><a href={countyBridgesHref(county)}>Open the map on {county.name}&rsquo;s bridges →</a> · <Link href="/explore/kansas-bridges">About the bridge layers</Link></p>
      <p className={styles.source}>Inventory as of {COUNTY_FACTS_SOURCES.bridges.inventoryAsOf}. These are inventory records, which are not always one physical bridge each. A recorded status is the inventory&rsquo;s own attribute, not a current safety assessment or permission to enter a structure.</p>
      <h2>On the map</h2>
      <p>The map opens centred on {county.name} with county outlines on. Switch on any layer from the Layers panel to see it for this county. These guides explain the main ones:</p>
      <ul>{LANDING_GUIDES.map(guide => <li key={guide.slug}><Link href={`/explore/${guide.slug}`}>{guide.title}</Link></li>)}</ul>
      <p><Link href={countyObservatoryHref(county)}>Compare {county.name} in the County Observatory →</Link></p>
      <h2>About these numbers</h2>
      <p className={styles.source}>The U.S. Census Bureau publishes July 1 population estimates for {population.baseYear} and {population.year}. A later release can revise earlier years, and the page gives the two estimates without saying why they differ.</p>
      <p className={styles.source}>The U.S. Census Bureau&rsquo;s American Community Survey 5-year estimates summarize {earlier.period} and {latest.period}. Dollar amounts use each period&rsquo;s final year and appear for {latest.period} only.</p>
      <p className={styles.source}>The <a href="https://www2.census.gov/programs-surveys/acs/tech_docs/statistical_testing/2025_Instructions_for_Stat_Testing_ACS.pdf">Census Bureau comparison method</a> uses both periods&rsquo; margins of error. “Difference uncertain” means the survey does not establish a change at the 90% confidence level. The education and poverty figures use margins of error derived from Census estimates.</p>
      <p className={explore.caution}>Census estimates and the KDOT inventory are public context from their providers, not Kansas Frontier Matrix evidence.</p>
    </article>
    <nav className={explore.related} aria-label="Other counties"><h2>More counties</h2>
      <ul className={styles.neighbors}>
        <li><Link href={countyPath(before)}>← {before.name}</Link></li>
        <li><Link href="/counties">All 105 counties</Link></li>
        <li><Link href={countyPath(after)}>{after.name} →</Link></li>
      </ul>
    </nav>
  </main>;
}
