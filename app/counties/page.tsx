import type { Metadata } from "next";
import Link from "next/link";
import { PUBLIC_SITE_ORIGIN } from "../crawler-discovery";
import { COUNTY_PAGES, countyPath } from "../county-pages";
import explore from "../explore/explore.module.css";
import { CountyDirectory } from "./county-directory";

const title = "Kansas counties", description = "All 105 Kansas counties: income, age, housing, education and poverty from the Census Bureau, each with a map of the county.";
export const metadata: Metadata = {
  title: `${title} · Kansas Frontier Matrix`, description, alternates: { canonical: `${PUBLIC_SITE_ORIGIN}/counties` },
  openGraph: { title, description, url: `${PUBLIC_SITE_ORIGIN}/counties`, type: "website", images: [{ url: `${PUBLIC_SITE_ORIGIN}/og-guided.png`, width: 1731, height: 909, alt: "Kansas Frontier Matrix map" }] },
};

export default function Page() {
  return <main className={explore.page}>
    <header className={explore.header}><Link href="/">← Kansas map</Link><Link href="/explore">Map guides</Link></header>
    <article className={explore.article}>
      <h1>Kansas counties</h1>
      <p>Pick a county for its Census Bureau estimates of income, age, housing, education and poverty, and a map that opens on it.</p>
      <CountyDirectory counties={COUNTY_PAGES.map(county => ({ name: county.name, href: countyPath(county) }))} />
      <p><Link href="/labs/observatory">Compare all 105 counties in the County Observatory →</Link> · <Link href="/records">Kansas records →</Link></p>
    </article>
  </main>;
}
