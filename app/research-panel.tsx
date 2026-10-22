"use client";

import { useState } from "react";
import { RESEARCH_RADII, researchIdentity, type ResearchContext, type ResearchRadius, type ResearchRecord } from "./research-context";
import styles from "./research.module.css";

export default function ResearchPanel({ context, counties, onCounty, anchorAvailable, onRadius, onInspect, onCenter, onSave, onReport, redacted }: {
  context: ResearchContext; counties: readonly NonNullable<ResearchContext["county"]>[]; onCounty: (county: NonNullable<ResearchContext["county"]> | null) => void; anchorAvailable: boolean; onRadius: (radius: ResearchRadius) => void;
  onInspect: (record: ResearchRecord) => void; onCenter: (record: ResearchRecord) => void;
  onSave: () => void; onReport: () => void; redacted: boolean;
}) {
  const [query, setQuery] = useState(context.anchor.title.slice(0, 80));
  return <section className={styles.dossier} aria-label="Near here place dossier">
    <header><span className={styles.eyebrow}>NEAR HERE · PINNED ANCHOR</span><h3 data-research-heading tabIndex={-1}>{context.anchor.title}</h3><p>Inspecting another result keeps this anchor. Use “Start new dossier here” to change it.</p></header>
    {!anchorAvailable && <p role="status" className={styles.warning}>The anchor is saved context and is unavailable in the current selected data. Nearby results use only eligible data loaded now.</p>}
    <div className={styles.actions}><label>Radius <select value={context.radiusMiles} onChange={event => onRadius(Number(event.target.value) as ResearchRadius)}>{RESEARCH_RADII.map(radius => <option key={radius} value={radius}>{radius} miles</option>)}</select></label><button type="button" onClick={() => onCenter(context.anchor)}>Center anchor</button></div>
    <label>County filter <select value={context.county ? `${context.county.geoid}:${context.county.edition}` : ""} onChange={event => onCounty(counties.find(row => `${row.geoid}:${row.edition}` === event.target.value) ?? null)}>
      <option value="">All loaded points within radius</option>
      {context.county && !counties.some(row => row.geoid === context.county?.geoid && row.edition === context.county?.edition) && <option value={`${context.county.geoid}:${context.county.edition}`}>{context.county.title} · saved boundary unavailable</option>}
      {counties.map(row => <option key={row.geoid} value={`${row.geoid}:${row.edition}`}>{row.title} · {row.edition}</option>)}
    </select></label>
    {!counties.length && <p>Enable the Census counties layer to load county filters. Ellsworth County is available when its baseline loads.</p>}
    {context.county && <p role="status">{context.county.title} · GEOID {context.county.geoid} · {context.county.edition} Census boundary · {context.county.state}. Intersected with the radius; display points only. The boundary is independent of map time.</p>}
    {context.county?.state === "unavailable" && <p className={styles.warning}>County boundary unavailable or edition changed. Results are withheld until that edition is available; the radius has not replaced your county scope.</p>}
    <p className={styles.count} role="status">Showing {context.records.length} of {context.total} eligible loaded records · {context.mapTime}</p>
    <p>Distances use {context.anchor.kind === "registry" ? "the registry’s display anchor" : "the provider’s point location"}. Proximity is discovery context, not evidence of a relationship.</p>
    {context.records.length === 0 && <p className={styles.warning}>No eligible records in the available data within this scope. This is not evidence that none exist.</p>}
    <ol className={styles.results}>{context.records.map(record => <li key={researchIdentity(record)} data-research-record={researchIdentity(record)}>
      <strong>{record.title}</strong><span>{record.distanceMiles.toFixed(1)} mi · {record.kind === "registry" ? "registry-anchor distance" : "provider-point distance"}</span>
      <small>{record.sourceTitle} · {record.evidenceLabel}</small><small>Source time: {record.sourceTime}</small><small>Retrieved: {record.retrievedAt ?? "Not supplied"}</small>
      <details><summary>Limits</summary><p>{record.limitation}</p></details>
      <div className={styles.actions}><button type="button" onClick={() => onInspect(record)}>Inspect</button><button type="button" onClick={() => onCenter(record)}>Center</button>{record.sourceUrl && <a href={record.sourceUrl} target="_blank" rel="noreferrer">Open source ↗</a>}</div>
    </li>)}</ol>
    <details className={styles.coverage}><summary>Loaded-source status &amp; limits ({context.coverage.length})</summary><p>These states describe loaded source responses before county and radius filtering. Ready does not establish complete county or historical coverage.</p>{context.coverage.map(item => <article key={item.sourceId}><strong>{item.title} · {item.state}</strong><small>Retrieved: {item.retrievedAt ?? "Not supplied"}</small><p>{item.limitation}</p></article>)}</details>
    <form action="/knowledge" method="get" className={styles.knowledge}><label htmlFor="research-knowledge-term">Search reviewed knowledge</label><input id="research-knowledge-term" name="term" maxLength={80} value={query} onChange={event => setQuery(event.target.value)} /><button type="submit">Search</button><small>Place-name search is separate from nearby distances. Only released knowledge can appear.</small></form>
    {redacted && <p className={styles.warning}>This view followed browser location. Saved and exported work omit the dossier to protect that location.</p>}
    <div className={styles.actions}><button type="button" onClick={onSave}>Save investigation</button><button type="button" onClick={onReport}>Create report</button></div>
  </section>;
}
