import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { PUBLIC_SITE_ORIGIN } from "../crawler-discovery";
import { LANDING_GUIDES, guideMapHref, landingGuide } from "../landing-guides";
import { OFFICIAL_CONTEXT_BY_ID } from "../live-context";
import styles from "./explore.module.css";

export function guideMetadata(slug: string): Metadata {
  const guide = landingGuide(slug);
  if (!guide) return {};
  const url = `${PUBLIC_SITE_ORIGIN}/explore/${guide.slug}`;
  return {
    title: `${guide.title} · Kansas Frontier Matrix`,
    description: guide.description,
    alternates: { canonical: url },
    openGraph: { title: guide.title, description: guide.description, url, type: "website", images: [{ url: `${PUBLIC_SITE_ORIGIN}/og-guided.png`, width: 1731, height: 909, alt: "Kansas Frontier Matrix map" }] },
    twitter: { card: "summary_large_image", title: guide.title, description: guide.description, images: [`${PUBLIC_SITE_ORIGIN}/og-guided.png`] },
  };
}

export function GuidePage({ slug }: { slug: string }) {
  const guide = landingGuide(slug);
  if (!guide) notFound();
  const href = guideMapHref(guide);
  return <main className={styles.page}>
    <header className={styles.header}><Link href="/">← Kansas map</Link><Link href="/explore">All guides</Link></header>
    <article className={styles.article}>
      <p className={styles.kicker}>{guide.kicker}</p>
      <h1>{guide.title}</h1>
      {guide.intro.map(paragraph => <p key={paragraph.slice(0, 40)}>{paragraph}</p>)}
      <p><a className={styles.cta} href={href}>Open this map →</a></p>
      <h2>Things to try</h2>
      <ul>{guide.ideas.map(idea => <li key={idea}>{idea}</li>)}</ul>
      {guide.relatedLab && <p><Link href={guide.relatedLab.href}>{guide.relatedLab.label} →</Link></p>}
      <h2>What the map shows</h2>
      <ul className={styles.layers}>{guide.layers.map(id => {
        const source = OFFICIAL_CONTEXT_BY_ID[id];
        return <li key={id}><strong>{source.title}</strong><span>{source.organization}</span><p>{source.legend}</p>
          <a href={source.sourceUrl} target="_blank" rel="noreferrer">Provider page ↗</a></li>;
      })}</ul>
      <p className={styles.caution}>{guide.caution} Map layers are public context from their providers, not Kansas Frontier Matrix evidence.</p>
      <p><a className={styles.cta} href={href}>Open this map →</a></p>
    </article>
    <nav className={styles.related} aria-label="Other guides"><h2>More guides</h2>
      <ul>{LANDING_GUIDES.filter(item => item.slug !== guide.slug).map(item => <li key={item.slug}><Link href={`/explore/${item.slug}`}>{item.title}</Link></li>)}</ul>
    </nav>
  </main>;
}
