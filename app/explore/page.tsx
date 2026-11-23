import type { Metadata } from "next";
import Link from "next/link";
import { PUBLIC_SITE_ORIGIN } from "../crawler-discovery";
import { LANDING_GUIDES, guideMapHref } from "../landing-guides";
import styles from "./explore.module.css";

export const metadata: Metadata = {
  title: "Map guides · Kansas Frontier Matrix",
  description: "Start exploring Kansas with ready-made maps: frontier trails, historic places, wildlife and hunting areas, and drought and water.",
  alternates: { canonical: `${PUBLIC_SITE_ORIGIN}/explore` },
};

export default function ExploreIndex() {
  return <main className={styles.page}>
    <header className={styles.header}><Link href="/">← Kansas map</Link><Link href="/topics">All topics</Link></header>
    <section className={styles.index}>
      <p className={styles.kicker}>KANSAS FRONTIER MATRIX</p>
      <h1>Map guides</h1>
      <p>Each guide opens the Kansas map with a few public layers already turned on, and explains what you are looking at.</p>
      <ul className={styles.cards}>{LANDING_GUIDES.map(guide => <li key={guide.slug}>
        <p className={styles.kicker}>{guide.kicker}</p>
        <h2><Link href={`/explore/${guide.slug}`}>{guide.title}</Link></h2>
        <p>{guide.description}</p>
        <a href={guideMapHref(guide)}>Open the map →</a>
      </li>)}</ul>
      <p><Link href="/counties">Kansas counties: Census estimates and a map for each of the 105 →</Link></p>
      <p><Link href="/records">Kansas records: the extremes in the data behind the map →</Link></p>
    </section>
  </main>;
}
