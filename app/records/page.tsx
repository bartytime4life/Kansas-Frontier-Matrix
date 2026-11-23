import type { Metadata } from "next";
import Link from "next/link";
import { PUBLIC_SITE_ORIGIN } from "../crawler-discovery";
import { KANSAS_RECORDS } from "../kansas-records";
import explore from "../explore/explore.module.css";
import styles from "../counties/counties.module.css";

const title = "Kansas records", url = `${PUBLIC_SITE_ORIGIN}/records`;
const description = "The most and fewest people, the oldest and longest bridges, the widest and longest tornado paths: the extremes in the public datasets behind the Kansas map, each with its source and limits.";
export const metadata: Metadata = {
  title: `${title} · Kansas Frontier Matrix`, description, alternates: { canonical: url },
  openGraph: { title, description, url, type: "website", images: [{ url: `${PUBLIC_SITE_ORIGIN}/og-guided.png`, width: 1731, height: 909, alt: "Kansas Frontier Matrix map" }] },
  twitter: { card: "summary_large_image", title, description, images: [`${PUBLIC_SITE_ORIGIN}/og-guided.png`] },
};

export default function Page() {
  return <main className={explore.page}>
    <header className={explore.header}><Link href="/">← Kansas map</Link><Link href="/counties">All 105 counties</Link></header>
    <article className={explore.article}>
      <p className={explore.kicker}>The extremes in the data</p>
      <h1>Kansas records</h1>
      <p>Each entry is the largest or smallest value in one public dataset this site already uses. It is a record of that dataset, for the years it covers, and nothing more: the source and its limits are under each group.</p>
      {KANSAS_RECORDS.map(section => <section key={section.id} aria-labelledby={`records-${section.id}`}>
        <h2 id={`records-${section.id}`}>{section.title}</h2>
        <ul className={styles.facts}>{section.items.map(item => <li key={item.label}>
          <span>{item.label}</span><strong>{item.value}</strong>
          <em>{item.href ? (item.href.startsWith("/?") ? <a href={item.href}>{item.where}</a> : <Link href={item.href}>{item.where}</Link>) : item.where}</em>
          {item.note && <em>{item.note}</em>}
        </li>)}</ul>
        <p className={styles.source}>Source: {section.source}. {section.caution}</p>
      </section>)}
      <p className={explore.caution}>These datasets are public context from their providers, not Kansas Frontier Matrix evidence. A record here can change when a provider revises its data.</p>
      <p><Link href="/counties">Look up any county →</Link> · <Link href="/explore">Map guides →</Link></p>
    </article>
  </main>;
}
