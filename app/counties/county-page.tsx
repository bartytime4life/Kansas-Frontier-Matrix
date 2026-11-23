import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { PUBLIC_SITE_ORIGIN } from "../crawler-discovery";
import { COUNTY_PAGES, comparedWith, count, countyMapHref, countyPage, countyPath, dollars, percent, years } from "../county-pages";
import { LANDING_GUIDES } from "../landing-guides";
import explore from "../explore/explore.module.css";
import styles from "./counties.module.css";

const description = (name: string, period: string) =>
  `${name}, Kansas at a glance: household income, age, home values, rent, education and poverty from the Census Bureau's ${period} survey, and a map of the county.`;

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
  const { latest, earlier } = county, href = countyMapHref(county);
  const position = COUNTY_PAGES.indexOf(county);
  const before = COUNTY_PAGES[(position + COUNTY_PAGES.length - 1) % COUNTY_PAGES.length], after = COUNTY_PAGES[(position + 1) % COUNTY_PAGES.length];
  return <main className={explore.page}>
    <header className={explore.header}><Link href="/">← Kansas map</Link><Link href="/counties">All 105 counties</Link></header>
    <article className={explore.article}>
      <p className={explore.kicker}>Kansas county · FIPS {county.fips}</p>
      <h1>{county.name}, Kansas</h1>
      <p>These are the Census Bureau&rsquo;s {latest.period} American Community Survey estimates for {county.name}. Each figure is followed by its margin of error: the survey asks a sample of households, so the true value is likely within that range.</p>
      <p><a className={explore.cta} href={href}>Open the map on {county.name} →</a></p>
      <h2>At a glance, {latest.period}</h2>
      <ul className={styles.facts}>
        <li><span>Median household income</span><strong>{dollars(latest.medianIncome)}</strong><em>in {latest.period.slice(-4)} dollars</em></li>
        <li><span>Median age</span><strong>{years(latest.medianAge)}</strong><em>{comparedWith(latest.medianAge, earlier.medianAge, " years")} in {earlier.period}</em></li>
        <li><span>Median home value</span><strong>{dollars(latest.medianHomeValue)}</strong><em>owner-occupied homes</em></li>
        <li><span>Median rent</span><strong>{dollars(latest.medianRent)}</strong><em>per month, with utilities</em></li>
        <li><span>Adults 25 and over with a bachelor&rsquo;s degree or higher</span><strong>{percent(latest.educationPct)}</strong><em>{comparedWith(latest.educationPct, earlier.educationPct, "%")} in {earlier.period}</em></li>
        <li><span>People below the poverty line</span><strong>{percent(latest.povertyPct)}</strong><em>{comparedWith(latest.povertyPct, earlier.povertyPct, "%")} in {earlier.period}</em></li>
        <li><span>Homes lived in by their owner</span><strong>{percent(latest.ownerOccupiedPct)}</strong><em>of occupied homes</em></li>
        <li><span>Housing units</span><strong>{count(latest.housingUnits)}</strong><em>{new Intl.NumberFormat("en-US").format(earlier.housingUnits)} in {earlier.period}</em></li>
      </ul>
      <h2>On the map</h2>
      <p>The map opens centred on {county.name} with county outlines on. Switch on any layer from the Layers panel to see it for this county. These guides explain the main ones:</p>
      <ul>{LANDING_GUIDES.map(guide => <li key={guide.slug}><Link href={`/explore/${guide.slug}`}>{guide.title}</Link></li>)}</ul>
      <p><Link href="/labs/observatory">Compare all 105 counties in the County Observatory →</Link></p>
      <h2>About these numbers</h2>
      <p className={styles.source}>Source: U.S. Census Bureau, American Community Survey 5-year estimates for {earlier.period} and {latest.period}, with the published 90% margins of error. These are survey estimates for a five-year period, not a count for a single year. Dollar amounts are in the dollars of each period&rsquo;s last year and are not adjusted for inflation, so this page does not compare them across periods. A figure is described as up or down only when the difference is larger than the newer estimate&rsquo;s margin of error.</p>
      <p className={explore.caution}>Census estimates are public statistical context from their provider, not Kansas Frontier Matrix evidence.</p>
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
