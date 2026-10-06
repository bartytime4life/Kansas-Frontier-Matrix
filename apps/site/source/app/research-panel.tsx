"use client";

import { useState } from "react";
import { RESEARCH_RADII, researchIdentity, type ResearchContext, type ResearchRadius, type ResearchRecord } from "./research-context";
import styles from "./research.module.css";

export default function ResearchPanel({ context, anchorAvailable, onRadius, onInspect, onCenter, onSave, onReport, redacted }: {
  context: ResearchContext; anchorAvailable: boolean; onRadius: (radius: ResearchRadius) => void;
  onInspect: (record: ResearchRecord) => void; onCenter: (record: ResearchRecord) => void;
  onSave: () => void; onReport: () => void; redacted: boolean;
}) {
  const [query, setQuery] = useState(context.anchor.title.slice(0, 80));
  return <section className={styles.dossier} aria-label="Near here place dossier">
    <header><span className={styles.eyebrow}>NEAR HERE · PINNED ANCHOR</span><h3 data-research-heading tabIndex={-1}>{context.anchor.title}</h3><p>Inspecting another result keeps this anchor. Use “Start new dossier here” to change it.</p></header>
    {!anchorAvailable && <p role="status" className={styles.warning}>The anchor is saved context and is unavailable in the current selected data. Nearby results use only eligible data loaded now.</p>}
    <div className={styles.actions}><label>Radius <select value={context.radiusMiles} onChange={event => onRadius(Number(event.target.value) as ResearchRadius)}>{RESEARCH_RADII.map(radius => <option key={radius} value={radius}>{radius} miles</option>)}</select></label><button type="button" onClick={() => onCenter(context.anchor)}>Center anchor</button></div>
    <p className={styles.count} role="status">Showing {context.records.length} of {context.total} eligible loaded records · {context.mapTime}</p>
    <p>Distances use {context.anchor.kind === "registry" ? "the registry’s display anchor" : "the provider’s point location"}. Proximity is discovery context, not evidence of a relationship.</p>
    {context.records.length === 0 && <p className={styles.warning}>No eligible records in the available data within this radius. This is not evidence that none exist.</p>}
    <ol className={styles.results}>{context.records.map(record => <li key={researchIdentity(record)} data-research-record={researchIdentity(record)}>
      <strong>{record.title}</strong><span>{record.distanceMiles.toFixed(1)} mi · {record.kind === "registry" ? "registry-anchor distance" : "provider-point distance"}</span>
      <small>{record.sourceTitle} · {record.evidenceLabel}</small><small>Source time: {record.sourceTime}</small><small>Retrieved: {record.retrievedAt ?? "Not supplied"}</small>
      <details><summary>Limits</summary><p>{record.limitation}</p></details>
      <div className={styles.actions}><button type="button" onClick={() => onInspect(record)}>Inspect</button><button type="button" onClick={() => onCenter(record)}>Center</button>{record.sourceUrl && <a href={record.sourceUrl} target="_blank" rel="noreferrer">Open source ↗</a>}</div>
    </li>)}</ol>
    <details className={styles.coverage}><summary>Coverage &amp; source limits ({context.coverage.length})</summary>{context.coverage.map(item => <article key={item.sourceId}><strong>{item.title} · {item.state}</strong><small>Retrieved: {item.retrievedAt ?? "Not supplied"}</small><p>{item.limitation}</p></article>)}</details>
    <form action="/knowledge" method="get" className={styles.knowledge}><label htmlFor="research-knowledge-term">Search reviewed knowledge</label><input id="research-knowledge-term" name="term" maxLength={80} value={query} onChange={event => setQuery(event.target.value)} /><button type="submit">Search</button><small>Place-name search is separate from nearby distances. Only released knowledge can appear.</small></form>
    {redacted && <p className={styles.warning}>This view followed browser location. Saved and exported work omit the dossier to protect that location.</p>}
    <div className={styles.actions}><button type="button" onClick={onSave}>Save investigation</button><button type="button" onClick={onReport}>Create report</button></div>
  </section>;
}
