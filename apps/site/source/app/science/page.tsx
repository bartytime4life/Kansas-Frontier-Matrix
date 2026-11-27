import Link from "next/link";
import climate from "../labs/heat-and-rain/snapshot-manifest.json";
import drought from "../labs/county-drought/snapshot-manifest.json";
import soil from "../labs/soil-profile/snapshot-manifest.json";
import air from "../labs/daily-air-quality/snapshot-manifest.json";
import sunlight from "../labs/sunlight-and-sky/snapshot-manifest.json";
import { nativeScienceDirectory } from "./science-directory.mjs";
import ScienceLauncher from "./science-launcher";
import styles from "./science.module.css";

export const metadata = {
  title: "Science & Labs | Kansas Frontier Matrix",
  description: "Find Kansas science labs, compare years and inspect the data behind each result.",
};

export default function SciencePage() {
  const entries = nativeScienceDirectory({ climate, drought, soil, air, sunlight });
  return <main className={styles.page}><div className={styles.frame}>
    <nav className={styles.navigation} aria-label="Science and Labs navigation">
      <Link href="/">← KFM Explorer</Link>
      <a href="#find-a-lab">Find a lab</a>
      <Link href="/observatory/sources">Data sources</Link>
    </nav>
    <header className={styles.hero}>
      <h1>Science &amp; Labs</h1>
      <p>Find a Kansas question, check where the data reach, and open a lab with the right records.</p>
      <div className={styles.shortcuts}>
        <Link href="/science/compare">Compare two years <span aria-hidden="true">↗</span></Link>
      </div>
    </header>
    <ScienceLauncher entries={entries} />
    <section className={styles.reading} aria-labelledby="science-reading-heading">
      <div><h2 id="science-reading-heading">Work with the evidence</h2><p>Open a lab to inspect its source, date range, and gaps. The year comparison gives each measurement its own chart and exports the records and source details together.</p></div>
      <Link href="/observatory/sources">Explore data sources ↗</Link>
      <Link href="/science/services">Request custom work ↗</Link>
    </section>
  </div></main>;
}
