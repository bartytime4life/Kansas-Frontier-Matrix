"use client";

import { useState } from "react";
import Link from "next/link";
import { ALMANAC_ASSETS, ALMANAC_RESOURCES, ALMANAC_PUBLISHERS, ALMANAC_CHECKED_AT, ALMANAC_TOPICS,
  ALMANAC_ACCESS_LABELS, ALMANAC_KIND_LABELS, filterAlmanacResources, almanacDisplayAsset,
  almanacPublisher, type AlmanacPublisherId, type AlmanacTopic } from "../almanac-resources";
import styles from "./almanacs.module.css";

export default function AlmanacLibrary({ initialFilters = { publisher: "all", topic: "all" } }: { initialFilters?: { publisher: "all" | AlmanacPublisherId; topic: AlmanacTopic } }) {
  const [publisher, setPublisher] = useState<"all" | AlmanacPublisherId>(initialFilters.publisher);
  const [topic, setTopic] = useState<AlmanacTopic>(initialFilters.topic);
  const [query, setQuery] = useState("");
  const resources = filterAlmanacResources(publisher, topic, query);
  const clear = () => { setPublisher("all"); setTopic("all"); setQuery(""); };

  return <main className={styles.page}>
    <nav className={styles.navigation} aria-label="Almanac navigation"><Link href="/">← Kansas map</Link><Link href="/topics">Explore subjects</Link><a href="#almanac-publishers">Publishers &amp; reuse</a></nav>
    <header className={styles.intro}><p>KFM · SOURCE REFERENCES</p><h1>Almanacs, in context</h1>
      <p>Explore Farmers’ Almanac and The Old Farmer’s Almanac together: seasonal outlooks, gardening references, Moon guides and historical material.</p>
      <div className={styles.stats}><span><strong>{ALMANAC_PUBLISHERS.length}</strong> publications</span><span><strong>{ALMANAC_RESOURCES.length}</strong> source references</span><span><strong>{ALMANAC_ASSETS.length}</strong> source images</span></div>
    </header>
    <aside className={styles.boundary}><strong>Different sources, different purposes</strong><p>The current weather image is a publisher prediction. The historical page is an archive document. Modern calendars and articles open at their publishers; they are separate from observations and reviewed KFM evidence. This is a dated reference check, not an automatic data feed.</p></aside>
    <section className={styles.browser} aria-labelledby="almanac-library-title">
      <h2 id="almanac-library-title">Browse available references</h2>
      <div className={styles.filters}>
        <label>Publication<select aria-label="Almanac publication" value={publisher} onChange={event => setPublisher(event.target.value as "all" | AlmanacPublisherId)}><option value="all">Both publications</option>{ALMANAC_PUBLISHERS.map(item => <option key={item.id} value={item.id}>{item.title}</option>)}</select></label>
        <label>Information<select aria-label="Almanac information" value={topic} onChange={event => setTopic(event.target.value as AlmanacTopic)}>{ALMANAC_TOPICS.map(([id, title]) => <option key={id} value={id}>{title}</option>)}</select></label>
        <label>Search<input type="search" aria-label="Search almanac references" value={query} maxLength={200} onChange={event => setQuery(event.target.value)} placeholder="Wichita, winter, Moon, 1861…" /></label>
      </div>
      <div className={styles.results}><output aria-live="polite">{resources.length} of {ALMANAC_RESOURCES.length} references</output>{(publisher !== "all" || topic !== "all" || query) && <button type="button" onClick={clear}>Clear filters</button>}</div>
      <p className={styles.checked}>Checked <time dateTime={ALMANAC_CHECKED_AT}>{ALMANAC_CHECKED_AT.slice(0, 10)} UTC</time>. Access can change; the check date is separate from each source’s edition or forecast period.</p>
      {resources.length === 0 && <div className={styles.empty}><h3>No matching references</h3><p>Try another publication, subject or search term.</p><button type="button" onClick={clear}>Show all references</button></div>}
      <div className={styles.cards}>{resources.map(resource => {
        const source = almanacPublisher(resource.publisherId), asset = almanacDisplayAsset(resource);
        return <article key={resource.id} id={`almanac-${resource.id}`} className={`${styles.card} ${asset ? styles.imageCard : ""}`} data-treatment={resource.treatment} data-access={resource.access}>
          <div className={styles.cardText}><header><span>{source.title}</span><small>{ALMANAC_KIND_LABELS[resource.kind]}</small></header>
            <h3>{resource.title}</h3><p>{resource.summary}</p>
            <dl><div><dt>Scope</dt><dd>{resource.scope}</dd></div><div><dt>Time</dt><dd>{resource.period}</dd></div><div><dt>Access</dt><dd>{ALMANAC_ACCESS_LABELS[resource.access]}</dd></div></dl>
            <p className={styles.limitation}>{resource.limitation}</p>
            <div className={styles.actions}><a href={resource.sourceUrl} target="_blank" rel="noopener noreferrer">Open original source ↗</a>{resource.topics.includes("weather") && <Link href="/?topic=weather">Compare with map weather context →</Link>}{resource.topics.includes("agriculture") && <Link href="/?topic=agriculture">Agriculture map context →</Link>}{resource.topics.includes("sky") && <Link href="/?maptab=scene&mapui=open">Sky &amp; daylight tools →</Link>}</div>
            <details><summary>Access, credits &amp; provenance</summary><p>{resource.accessNote}</p>
              <p><strong>Treatment:</strong> {resource.treatment === "LINK_ONLY" ? "Source link and original KFM description only. No publisher table, article or artwork has been imported." : resource.treatment === "PERMITTED_MAP" ? "Unchanged weather image, displayed under the publisher’s credited-sharing permission." : "Historical image from a Library of Congress collection identified as free to use and reuse."}</p>
              {asset && <><p>{asset.credit}</p><p>{asset.rightsBasis}</p><dl><div><dt>Image size</dt><dd>{asset.bytes.toLocaleString("en-US")} bytes</dd></div><div><dt>SHA-256</dt><dd><code>{asset.sha256}</code></dd></div></dl><a href={asset.sourceAssetUrl} target="_blank" rel="noopener noreferrer">Original image ↗</a></>}
              <p><a href={resource.rightsUrl} target="_blank" rel="noopener noreferrer">Rights reference ↗</a></p>
              <p>Source admission remains pending; no EvidenceBundle, map activation or data release is created by this reference entry.</p>
            </details>
          </div>
          {asset && <figure className={styles.figure}><a href={resource.sourceUrl} target="_blank" rel="noopener noreferrer"><img src={asset.path} width={asset.width} height={asset.height} alt={asset.alt} loading="lazy" /></a><figcaption>{asset.credit} · {resource.period}. <a href={resource.sourceUrl} target="_blank" rel="noopener noreferrer">Publisher / archive source ↗</a></figcaption></figure>}
        </article>;
      })}</div>
    </section>
    <section id="almanac-publishers" className={styles.publishers} aria-labelledby="almanac-publishers-title"><h2 id="almanac-publishers-title">Publishers &amp; reuse</h2>
      <div>{ALMANAC_PUBLISHERS.map(item => <article key={item.id}><h3>{item.title}</h3><p>{item.organization}</p><p>{item.rights}</p><a href={item.url} target="_blank" rel="noopener noreferrer">Publisher website ↗</a><a href={item.rightsUrl} target="_blank" rel="noopener noreferrer">Reuse reference ↗</a></article>)}</div>
      <p>No open bulk data API or redistribution license was verified for the modern calendars. Restricted content stays with the publisher until source-specific permission and KFM admission checks are complete. No subscription, account or background acquisition is configured.</p>
    </section>
  </main>;
}
