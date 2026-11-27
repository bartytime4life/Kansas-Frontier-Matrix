import Link from "next/link";
import climate from "../labs/heat-and-rain/snapshot-manifest.json";
import drought from "../labs/county-drought/snapshot-manifest.json";
import soil from "../labs/soil-profile/snapshot-manifest.json";
import air from "../labs/daily-air-quality/snapshot-manifest.json";
import sunlight from "../labs/sunlight-and-sky/snapshot-manifest.json";
import { PUBLIC_SITE_ORIGIN } from "../crawler-discovery";
import { atlasScienceDirectory } from "./atlas-directory.mjs";
import { nativeScienceDirectory } from "./science-directory.mjs";
import ScienceLauncher from "./science-launcher";
import styles from "./science.module.css";

export const metadata = {
  title: "Science & Labs | Kansas Frontier Matrix",
  description: "Find Kansas science labs, data workspaces, and reports in one searchable catalogue.",
  alternates: { canonical: `${PUBLIC_SITE_ORIGIN}/science` },
};

export default function SciencePage() {
  const entries = atlasScienceDirectory(nativeScienceDirectory({ climate, drought, soil, air, sunlight }));
  return <main className={styles.page}><div className={styles.frame}>
    <nav className={styles.navigation} aria-label="Science and Labs navigation">
      <Link href="/">← KFM Explorer</Link>
      <a href="#find-a-lab">Find a lab</a>
      <Link href="/labs#research-labs">Research atlas</Link>
      <Link href="/research">Data sources</Link>
    </nav>
    <header className={styles.hero}>
      <h1>Science &amp; Labs</h1>
      <p>Find a Kansas question, check where the data reach, and open a lab with the right records.</p>
      <div className={styles.shortcuts}>
        <Link href="/science/compare">Compare two years <span aria-hidden="true">↗</span></Link>
        <Link href="/labs/observatory">Explore a county <span aria-hidden="true">↗</span></Link>
        <Link href="/labs/signals">Compare annual signals <span aria-hidden="true">↗</span></Link>
      </div>
    </header>
    <ScienceLauncher entries={entries} />
    <section className={styles.reading} aria-labelledby="science-reading-heading">
      <div><h2 id="science-reading-heading">Work with the evidence</h2><p>Open a lab to inspect its source, date range, and gaps. Use the research notebook to save a view or return to an investigation on this device.</p></div>
      <Link href="/labs/notebook">Research notebook ↗</Link>
      <Link href="/science/services">Request custom work ↗</Link>
    </section>
  </div></main>;
}
