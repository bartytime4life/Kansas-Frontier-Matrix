import Link from "next/link";
import SeasonScenarios from "./season-scenarios";
import styles from "./farm-season.module.css";

export const metadata = {
  title: "Kansas farm season planning | Kansas Frontier Matrix",
  alternates: { canonical: "https://kansasfrontiermatrix.com/farm-season" },
  description: "Estimate irrigation energy and forage balance from your own numbers. Compare Kansas seasonal planning references for water, pasture, weather and frost.",
};

const seasonalChecks = [
  {
    name: "Winter · December–February",
    description: "Review well measurements and the utility tariff before setting a pumping budget. Compare dry-matter supply with winter demand.",
    href: "https://geohydro.kgs.ku.edu/geohydro/wizard/",
    source: "KGS WIZARD well measurements",
  },
  {
    name: "Spring · March–May",
    description: "Compare historical station frost and rainfall before choosing a planting or grazing window. Check recent statewide crop progress for context.",
    href: "/labs/heat-and-rain",
    source: "KFM Heat & Rain Lab",
  },
  {
    name: "Summer · June–August",
    description: "Use local pasture observations and possible precipitation scenarios to revise the forage budget. Compare weekly county drought assessments across the recorded summers.",
    href: "/labs/county-drought",
    source: "KFM County Drought Lab",
  },
  {
    name: "Fall · September–November",
    description: "Compare harvest and winter-wheat planting progress. Recheck fall freezes and forage supply before budgeting the next season.",
    href: "https://www.nass.usda.gov/statistics_by_state/Kansas/Publications/Crop_Progress_and_Condition/index.php",
    source: "USDA Kansas Crop Progress",
  },
] as const;

export default function FarmSeasonPage() {
  return <main className={styles.page}>
    <div className={styles.frame}>
      <nav className={styles.nav} aria-label="Farm season navigation">
        <Link href="/">← KFM Explorer</Link>
        <Link href="/science">Kansas science tools</Link>
      </nav>
      <header className={styles.hero}>
        <h1>Plan a Kansas farm season</h1>
        <p>Estimate irrigation electricity and forage balance, then compare your assumptions with Kansas water records, pasture outlooks and frost history.</p>
        <p className={styles.note}>Your entries stay on this page. Reloading clears them.</p>
        <nav className={styles.nav} aria-label="On this page">
          <a href="#pumping">Pumping costs</a>
          <a href="#forage">Forage budget</a>
          <a href="#calendar">Seasonal calendar</a>
          <a href="#references">Sources</a>
        </nav>
      </header>

      <SeasonScenarios />

      <section className={styles.section} id="calendar" aria-labelledby="seasonal-heading">
        <h2 id="seasonal-heading">Kansas seasonal calendar</h2>
        <p>Use the season to find records to check. Timing varies with location, crop, and year.</p>
        <div className={styles.calendar}>
          {seasonalChecks.map(season => <article key={season.name}>
            <h3>{season.name}</h3>
            <p>{season.description}</p>
            {season.href.startsWith("/")
              ? <Link href={season.href}>{season.source}</Link>
              : <a href={season.href}>{season.source}</a>}
          </article>)}
        </div>
      </section>

      <section className={styles.section} id="references" aria-labelledby="seasonal-sources-heading">
        <h2 id="seasonal-sources-heading">Read the source</h2>
        <dl className={styles.sources}>
          <div>
            <dt>Well levels and water use</dt>
            <dd>WIZARD reports measurements at individual wells. WIMAS has dated water-use and rights records, with current standing available from the Kansas Division of Water Resources.</dd>
            <dd className={styles.sourceLinks}>
              <a href="https://geohydro.kgs.ku.edu/geohydro/wizard/">KGS WIZARD</a>
              <a href="https://maps.kgs.ku.edu/gh/geohydro/wimas/">KDA and KGS WIMAS</a>
              <a href="https://www.agriculture.ks.gov/divisions-programs/division-of-water-resources/water-appropriation">KDA Water Appropriation</a>
            </dd>
          </div>
          <div>
            <dt>Grassland productivity</dt>
            <dd>Grass-Cast models grid-scale production for different remaining-season precipitation scenarios. Check the map issue date and use local forage estimates for your budget.</dd>
            <dd className={styles.sourceLinks}><a href="https://www.climatehubs.usda.gov/hubs/northern-plains/tools/grass-cast-grassland-productivity-forecast">USDA Climate Hubs Grass-Cast</a></dd>
          </div>
          <div>
            <dt>Seasonal weather and frost</dt>
            <dd>NOAA outlooks show regional probabilities. KFM’s Heat &amp; Rain Lab shows dated station observations. The free Farmers’ Almanac frost chart and planting-calendar preview are publisher references and do not drive these calculations.</dd>
            <dd className={styles.sourceLinks}>
              <a href="https://www.cpc.ncep.noaa.gov/products/predictions/long_range/">NOAA CPC seasonal outlooks</a>
              <Link href="/labs/heat-and-rain">KFM Heat &amp; Rain Lab</Link>
              <a href="https://www.farmersalmanac.com/average-frost-dates#:~:text=Kansas">Farmers’ Almanac Kansas frost chart</a>
              <a href="https://www.farmersalmanac.com/calendar/gardening">Farmers’ Almanac planting preview</a>
            </dd>
          </div>
        </dl>
      </section>
    </div>
  </main>;
}
