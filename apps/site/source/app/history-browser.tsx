"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import catalog from "./history-sources.json";
import { canDownloadPublicMap, publicMapSelectedLimit } from "./public-map-catalog";
import { publicMapDownloadState } from "./public-map-download-state";
import type { PublicMapDownloads } from "./use-public-map-downloads";
import { formatDownloadBytes as bytes } from "./local-download-client";
import s from "./downloads/workspace.module.css";
import h from "./history.module.css";

export default function HistoryBrowser({ downloads, blocked = false, onConnect, onViewActivity }: { downloads: PublicMapDownloads; blocked?: boolean; onConnect: () => void; onViewActivity: () => void }) {
  const [query, setQuery] = useState(""), [kind, setKind] = useState("all"), [selected, setSelected] = useState(""), [maximum, setMaximum] = useState("");
  const transferHeading = useRef<HTMLHeadingElement>(null);
  useEffect(() => { if (selected) { transferHeading.current?.scrollIntoView({ block: "center" }); transferHeading.current?.focus({ preventScroll: true }); } }, [selected]);
  const { status, connection, busy, selectAsset } = downloads;
  const records = useMemo(() => catalog.sources.filter(row => (kind === "all" || row.kind === kind) && query.toLowerCase().trim().split(/\s+/).every(word => `${row.title} ${row.publisher} ${row.description} ${row.coverage}`.toLowerCase().includes(word))), [query, kind]);
  const assets = (downloads.catalog?.records ?? []).filter(row => row.sourceId === "history-originals").flatMap(row => row.assets).filter(canDownloadPublicMap);
  const asset = assets.find(item => item.id === selected);
  const limit = asset ? publicMapSelectedLimit(maximum, asset, status?.limitBytes) : null;
  useEffect(() => { selectAsset(asset?.id ?? null); }, [asset?.id, selectAsset]);
  const choose = (id: string) => { const file = assets.find(item => item.id === id); setSelected(id); setMaximum(file?.expectedBytes ? String(Math.ceil(file.expectedBytes / 1048576)) : ""); };
  return <section aria-labelledby="history-title">
    <p className={s.eyebrow}>KANSAS THROUGH ITS SOURCES</p><h2 id="history-title">History &amp; archives</h2>
    <p className={s.muted}>Read a historic book here, save selected originals, or explore the institutions that preserve Kansas history. Collection links open the provider’s catalog; they do not download a collection.</p>
    <div className={h.feature}><div><p className={s.eyebrow}>READ HERE · 1909</p><h3>A history of Kansas</h3><p>Noble L. Prentis · revised by Henrietta V. Race</p><p>Search the complete archival OCR text. Only 740 KiB, loaded when you open the reader.</p><small>Historical perspective and uncorrected OCR; verify quotations against the scanned pages.</small></div><a className={s.primaryLink} href="/history/prentis-1909">Read &amp; search the book →</a></div>
    <div className={h.feature}><div><p className={s.eyebrow}>PEOPLE &amp; EVENTS · SOURCE RESEARCH</p><h3>Kansas lives and historical context</h3><p>Search entries from supplied history and biography sources, with dates, place context, attribution and access notes.</p><small>Research candidates pending review. Repeated names remain separate source assertions.</small></div><a className={s.primaryLink} href="/history/people-events">Browse people &amp; events →</a></div>
    <div className={s.filters}><label>Search history sources<input type="search" value={query} onChange={event => setQuery(event.target.value)} placeholder="County, genealogy, newspapers, maps…" /></label><label>Source type<select value={kind} onChange={event => setKind(event.target.value)}><option value="all">All sources</option><option value="book">Books &amp; PDFs</option><option value="collection">Archives &amp; collections</option><option value="guide">Research guides</option><option value="gis">Maps &amp; GIS discovery</option></select></label></div>
    <p className={s.snapshot} role="status">{records.length} of {catalog.sources.length} sources · checked {catalog.checkedAt.slice(0, 10)} · individual holdings and terms vary</p>
    <ul className={h.sources}>{records.map(row => <li key={row.id}><article>
      <p className={s.eyebrow}>{row.publisher} · {row.kind === "book" ? "BOOK / PDF" : row.kind.toUpperCase()}</p><h3>{row.title}</h3><p>{row.description}</p><p className={h.coverage}>{row.coverage}</p>
      <div className={h.actions}><a href={row.url} target="_blank" rel="noreferrer">{row.kind === "book" ? "Open original at source" : "Explore source"} ↗</a>{row.assetId && assets.some(file => file.id === row.assetId) && <button type="button" aria-expanded={selected === row.assetId} aria-controls="history-transfer" onClick={() => choose(row.assetId)}>Save PDF · {bytes(assets.find(file => file.id === row.assetId)!.expectedBytes!)}</button>}</div>
      {row.assetId && <p className={h.state}>{publicMapDownloadState([row.assetId], status, connection).label} · KFM downloads on this computer</p>}
      <details><summary>Access, reuse &amp; evidence</summary><p>{row.accessNote}</p><p>{row.rights}</p><p>{row.integration}</p>{row.evidenceUrl && <a href={row.evidenceUrl} target="_blank" rel="noreferrer">Source evidence ↗</a>}</details>
    </article></li>)}</ul>
    {!records.length && <p className={s.empty}>No matching sources. Try another term or choose all sources.</p>}
    {asset && <section id="history-transfer" className={h.transfer} aria-label="Save selected history original">
      <h3 ref={transferHeading} tabIndex={-1}>{asset.title}</h3><p>Reported size: {bytes(asset.expectedBytes!)}. Choose a maximum before saving to this computer.</p>
      <label>Maximum download (MiB)<input type="number" min="0.001" step="0.001" value={maximum} onChange={event => setMaximum(event.target.value)} /></label>
      <p>{limit === null ? "Enter a positive maximum at least as large as the reported file." : `This original uses ${bytes(asset.expectedBytes!)}; transfer stops at ${bytes(limit)}. Preparation may need additional space.`}</p>
      {connection !== "connected" && <button type="button" disabled={connection === "connecting"} onClick={onConnect}>{connection === "connecting" ? "Connecting…" : "Connect this computer"}</button>}
      <button type="button" className={s.primaryButton} disabled={connection !== "connected" || !!busy || blocked || !!status?.active || !!status?.queued || limit === null} onClick={() => { if (limit !== null) void downloads.startDownload(asset, limit); }}>Download to this computer</button>
      <button type="button" onClick={onViewActivity}>View activity</button><button type="button" onClick={() => setSelected("")}>Close selection</button>
      <p>Captured originals stay in private local storage with a receipt. Browser saves from provider links are outside KFM tracking. Redistribution and source admission remain separate.</p>
      {downloads.notice && <p role="status">{downloads.notice}</p>}
    </section>}
    <p className={s.muted}>Only the small Prentis OCR text is bundled. The two PDF originals total approximately 49 MiB; other collections have unknown total sizes and are explored at their source. No bulk archive crawl runs in the background.</p>
    <a href="/history/sources.json" download="kfm-history-sources.json">Download source inventory (JSON)</a>
  </section>;
}
