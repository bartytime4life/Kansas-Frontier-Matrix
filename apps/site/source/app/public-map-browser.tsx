"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import { canDownloadPublicMap, filterPublicMaps, publicMapSelectedLimit, type PublicMapFilter, type PublicMapRecord } from "./public-map-catalog";
import type { PublicMapDownloads } from "./use-public-map-downloads";
import { formatDownloadBytes as bytes } from "./local-download-client";
import { PublicMapPreview } from "./public-map-preview";
import { revealTransferControls } from "./download-focus";
import { publicMapDownloadState, type CardDownloadState } from "./public-map-download-state";
import StormEventsQueue from "./storm-events-queue";
import s from "./downloads/workspace.module.css";
import p from "./public-map-browser.module.css";

const PUBLIC_MAP_PAGE_SIZE = 8;
const downloadMark = (state: CardDownloadState) => <span className={p.downloadState} data-state={state.state} title={state.detail}>
  <svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6" />{state.state === "downloaded" ? <path d="m5 8 2 2 4-4" /> : state.state === "downloading" || state.state === "queued" ? <path d="M8 4v4l2 1" /> : state.state === "unknown" || state.state === "missing" ? <path d="M8 4.5v4M8 11v.5" /> : <path d="M5 8h6" />}</svg>
  <span>{state.label}</span>
</span>;
const defaultFilter: PublicMapFilter = { text: "", publisher: "all", county: "all", year: "all", format: "all" };
// Catalog timestamps are server-rendered: preserve date precision and avoid locale/timezone hydration drift.
const stamp = (value: string) => /^\d{4}-\d{2}-\d{2}$/.test(value) ? value : `${new Date(value).toISOString().replace("T", " ").replace(".000Z", " UTC")}`;
const size = (value: number | null) => value === null ? "Size unknown" : bytes(value);
const coverageLabels = { seed: "Starting references", partial: "Partial catalog", complete: "Catalog checked", unavailable: "Coverage unknown" };
const coverageReason = (reason: string) => /CERTIFICATE_VERIFY_FAILED|certificate verify failed|unable to get local issuer certificate/i.test(reason)
  ? "The provider’s secure connection could not be verified. Current coverage is unknown; retained references remain available." : reason;

export default function PublicMapBrowser({ downloads, blockedByOtherDownload = false, onViewActivity, onConnect, collection = "maps" }: { collection?: "maps" | "satellite"; downloads: PublicMapDownloads; blockedByOtherDownload?: boolean; onViewActivity?: () => void; onConnect?: () => void }) {
  const { catalog, status, connection, busy, selectAsset } = downloads;
  const connected = connection === "connected";
  const [filter, setFilter] = useState(defaultFilter), [page, setPage] = useState(0), [selectedId, setSelectedId] = useState("");
  const [assetId, setAssetId] = useState(""), [maximum, setMaximum] = useState("");
  const heading = useRef<HTMLHeadingElement>(null), resultsHeading = useRef<HTMLHeadingElement>(null), focusSelection = useRef(false), focusReturn = useRef(false), transfer = useRef<HTMLInputElement>(null), transferAction = useRef<HTMLButtonElement>(null), focusTransfer = useRef(false);
  const records = useMemo(() => filterPublicMaps(catalog?.records ?? [], defaultFilter).filter(row => row.sourceId.startsWith("publisher-") === (collection === "satellite")), [catalog, collection]);
  // A discovered source with no records yet (Storm Events before its first refresh) still shows its coverage.
  const coverage = catalog?.coverage.filter(source => records.some(row => row.sourceId === source.sourceId) || source.recordCount === 0 && source.sourceId.startsWith("publisher-") === (collection === "satellite")) ?? [];
  const stormsUnlisted = collection === "satellite" && coverage.some(source => source.sourceId === "publisher-noaa-storm-events" && source.recordCount === 0);
  const selected = records.find(row => row.id === selectedId) ?? null;
  const files = selected?.assets.filter(canDownloadPublicMap) ?? [];
  const chosenAsset = files.find(asset => asset.id === assetId);
  const limit = chosenAsset ? publicMapSelectedLimit(maximum, chosenAsset, status?.limitBytes) : null;
  const rows = useMemo(() => filterPublicMaps(records, filter), [records, filter]);
  const pages = Math.max(1, Math.ceil(rows.length / PUBLIC_MAP_PAGE_SIZE)), currentPage = Math.min(page, pages - 1);
  const applied = Object.entries(filter).filter(([key, value]) => value !== (key === "text" ? "" : "all")).length;
  const extraFilters = [filter.publisher, filter.county, filter.year, filter.format].filter(value => value !== "all").length;
  const options = useMemo(() => ({
    publishers: [...new Set(records.map(row => row.publisher))].sort(), counties: [...new Set(records.flatMap(row => row.counties))].sort(),
    years: [...new Set(records.flatMap(row => row.mapYear === null ? [] : [row.mapYear]))].sort((a, b) => b - a),
    formats: [...new Set(records.flatMap(row => row.assets.filter(canDownloadPublicMap).map(asset => asset.format)))].sort(),
  }), [records]);
  const unavailable = coverage.filter(source => source.state === "unavailable" || source.state === "partial");
  const existing = chosenAsset && publicMapDownloadState([chosenAsset.id], status, connection).state === "downloaded";
  const workerBusy = blockedByOtherDownload || Boolean(status?.active);
  useEffect(() => { selectAsset(chosenAsset?.id ?? null); }, [chosenAsset?.id, selectAsset]);
  useEffect(() => {
    if (focusReturn.current) {
      focusReturn.current = false; resultsHeading.current?.focus({ preventScroll: true });
      if (window.matchMedia("(max-width: 760px)").matches) resultsHeading.current?.scrollIntoView({ block: "start" });
    }
    if (!focusSelection.current) return;
    focusSelection.current = false;
    heading.current?.focus({ preventScroll: true });
    if (window.matchMedia("(max-width: 760px)").matches) heading.current?.scrollIntoView({ block: "start", behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "instant" : "smooth" });
  }, [selectedId]);
  useEffect(() => {
    if (!focusTransfer.current || !transfer.current) return;
    focusTransfer.current = false;
    const field = transfer.current;
    field.focus({ preventScroll: true });
    const reveal = () => { if (document.activeElement === field) revealTransferControls(field, transferAction.current); };
    revealTransferControls(field, transferAction.current);
    window.visualViewport?.addEventListener("resize", reveal);
    window.addEventListener("resize", reveal);
    return () => { window.visualViewport?.removeEventListener("resize", reveal); window.removeEventListener("resize", reveal); };
  }, [assetId]);
  const choose = (row: PublicMapRecord | null) => { focusSelection.current = Boolean(row); focusReturn.current = !row; setSelectedId(row?.id ?? ""); setAssetId(""); setMaximum(""); };
  const changeFilter = (key: keyof PublicMapFilter, value: string) => { setFilter(old => ({ ...old, [key]: value })); setPage(0); };
  const selectFile = (id: string) => {
    const asset = files.find(item => item.id === id);
    setAssetId(id); setMaximum(asset?.expectedBytes ? String(Math.ceil(asset.expectedBytes / 1_048_576)) : ""); focusTransfer.current = true;
  };
  return <section id={collection === "satellite" ? "public-climate" : "public-maps"} className={p.catalog} aria-labelledby={`${collection}-catalog-heading`}>
    <header className={p.catalogHeading}><div><h2 id={`${collection}-catalog-heading`} ref={resultsHeading} tabIndex={-1}>{collection === "satellite" ? "Kansas crops, climate & storms · no login" : "Maps & geology"}</h2><p>{collection === "satellite" ? "Public publisher files: crop and rainfall originals identified through the Earth Engine catalog, and NOAA Storm Events CSV files by year. These national and global originals include Kansas; they are not clipped to the state." : "Free, directly downloadable maps and geologic files for Kansas."}</p></div><span className={p.catalogCount}>{catalog ? records.length.toLocaleString() : "Unknown"}<small>downloadable records</small></span></header>
    <div className={p.searchRow} data-single><label>{collection === "satellite" ? "Search public datasets" : "Search the map catalog"}<input type="search" placeholder={collection === "satellite" ? "Cropland, rainfall, storm events, year…" : "Title, county, publication or mine…"} value={filter.text} onChange={e => changeFilter("text", e.target.value)} /></label></div>
    <div className={p.filterBar}><details className={p.filterDetails}><summary>More filters{extraFilters > 0 ? ` · ${extraFilters} applied` : ""}</summary><div className={p.filters}>
      <label>Publisher<select value={filter.publisher} onChange={e => changeFilter("publisher", e.target.value)}><option value="all">All publishers</option>{options.publishers.map(value => <option key={value}>{value}</option>)}</select></label>
      <label>County<select value={filter.county} onChange={e => changeFilter("county", e.target.value)}><option value="all">All counties</option><option value="unknown">County not specified</option>{options.counties.map(value => <option key={value}>{value}</option>)}</select></label>
      <label>{collection === "satellite" ? "Data year" : "Map publication year"}<select value={filter.year} onChange={e => changeFilter("year", e.target.value)}><option value="all">All years</option><option value="unknown">Year unknown</option>{options.years.map(value => <option key={value}>{value}</option>)}</select></label>
      <label>File format<select value={filter.format} onChange={e => changeFilter("format", e.target.value)}><option value="all">All formats</option>{options.formats.map(value => <option key={value}>{value}</option>)}</select></label>
    </div></details>{applied > 0 && <button type="button" className={s.textButton} onClick={() => { setFilter(defaultFilter); setPage(0); }}>Clear {applied} {applied === 1 ? "filter" : "filters"}</button>}<span>{rows.length.toLocaleString()} results</span></div>
    <details className={p.coverage}><summary>Source coverage{unavailable.length ? <span>{unavailable.map(source => `${source.title}: ${source.state === "unavailable" ? "unknown" : "partial"}`).join(" · ")}</span> : <span>Check dates &amp; completeness</span>}</summary><ul>{coverage.map(source => <li key={source.sourceId}><strong>{source.title}</strong><span>{records.filter(row => row.sourceId === source.sourceId).length.toLocaleString()} downloadable records · {coverageLabels[source.state]} · {source.state === "unavailable" && (source.discoveredCount ?? source.recordCount) === 0 ? "Coverage unknown" : `${(source.discoveredCount ?? source.recordCount).toLocaleString()}${source.expectedCount === null ? " metadata records; total unknown" : ` / ${source.expectedCount.toLocaleString()} metadata records`}`}{source.seedReferenceCount ? ` + ${source.seedReferenceCount} starting references` : ""}</span><p>{coverageReason(source.reason)}</p>{source.checkedAt && <small>Checked {stamp(source.checkedAt)}</small>}
    </li>)}</ul><p>Only records with verified direct files appear in downloads. Missing results do not establish complete geological coverage.</p><button type="button" disabled={!connected || !!busy || status?.refresh.state === "running"} aria-busy={status?.refresh.state === "running"} onClick={() => void downloads.refreshCatalog()}>{status?.refresh.state === "running" ? "Refreshing catalog…" : "Refresh Kansas catalog"}</button></details>
    {stormsUnlisted && <div className={s.alert}><p>NOAA Storm Events files are listed from the NCEI directory when the catalog is refreshed on this computer, because NCEI renames a year&apos;s files when it reissues them.</p><button type="button" disabled={!connected || !!busy || status?.refresh.state === "running"} aria-busy={status?.refresh.state === "running"} onClick={() => void downloads.refreshCatalog()}>{status?.refresh.state === "running" ? "Listing storm event files…" : connected ? "List Storm Events files" : "Connect to list Storm Events files"}</button></div>}
    {collection === "satellite" && <StormEventsQueue records={records} downloads={downloads} blocked={blockedByOtherDownload} showNotice={!selected} onViewActivity={onViewActivity} />}
    {downloads.catalogError && <p className={s.alert}>{downloads.catalogError}</p>}
    {status?.refresh.state === "failed" && <p className={s.alert}>Catalog refresh did not finish. Retained records remain available; current completeness is unknown.</p>}
    <p className={p.statusScope}>Download status · this computer{connected ? " · KFM-tracked files" : " · connect to check"}</p>
    <div className={p.results} data-selection={Boolean(selected)}>
      <div className={p.resultColumn}><ul className={p.records}>{rows.slice(currentPage * PUBLIC_MAP_PAGE_SIZE, (currentPage + 1) * PUBLIC_MAP_PAGE_SIZE).map(row => <li key={row.id}><button type="button" aria-pressed={selectedId === row.id} onClick={() => choose(row)}><span className={p.recordMeta}>{row.publisher} <span>{row.mapYear ?? "Year unknown"}</span></span><strong>{row.title}</strong><small>{collection === "satellite" ? "No login · national/global original" : row.counties.join(", ") || "County not specified"}</small><span className={p.fileHint}>{downloadMark(publicMapDownloadState(row.assets.filter(canDownloadPublicMap).map(asset => asset.id), status, connection))}<span className={p.cardArrow} aria-hidden="true">↗</span></span></button></li>)}</ul>
        {!rows.length && <div className={s.empty}><strong>No matching maps</strong><p>Try fewer filters or a broader search. Only verified direct files are included.</p><button type="button" onClick={() => { setFilter(defaultFilter); setPage(0); }}>Reset search</button></div>}
        <nav className={s.pagination} aria-label="Public map catalog pages"><button type="button" disabled={currentPage === 0} onClick={() => setPage(currentPage - 1)}>Previous</button><span>{currentPage + 1} / {pages}</span><button type="button" disabled={currentPage + 1 >= pages} onClick={() => setPage(currentPage + 1)}>Next</button></nav>
      </div>
      <aside className={p.detail} aria-label={collection === "satellite" ? "Selected public dataset" : "Selected public map"}>
        {!selected ? <div className={p.selectionEmpty}><span className={p.detailMark} aria-hidden="true">↗</span><h3>{collection === "satellite" ? "Select a public dataset" : "Select a map"}</h3><p>See available files, preview source context, and choose what to keep on this computer.</p><small>Browsing never starts a download.</small></div> : <>
          <button type="button" className={s.textButton} onClick={() => choose(null)}>← Back to results</button><p className={s.eyebrow}>{selected.publisher} · {selected.mapYear ?? "Map year unknown"}{selected.scale ? ` · ${selected.scale}${selected.scaleUnit && !["ratio", "denominator"].includes(selected.scaleUnit) ? ` ${selected.scaleUnit}` : ""}` : ""}</p>
          <h3 ref={heading} tabIndex={-1}>{selected.title}</h3>
          {selected.rights.status === "held" && <p className={p.rightsNote}>Source reuse terms are held for review. A local capture does not grant redistribution or map-display approval.</p>}
          <div className={p.fileSection}><h4>Available files</h4><ul className={p.assets}>{files.map(asset => <li key={asset.id}><div><strong>{asset.title}</strong><span>{asset.format} · {size(asset.expectedBytes)} · Link checked</span>{downloadMark(publicMapDownloadState([asset.id], status, connection))}</div>
            <><button type="button" className={s.primaryButton} aria-pressed={assetId === asset.id} onClick={() => selectFile(asset.id)}>Download {asset.format}<span>{size(asset.expectedBytes)}</span></button><a href={asset.url} target="_blank" rel="noreferrer">{["PDF", "JPEG", "JPG", "TIFF", "TIF", "GEOTIFF", "PNG"].includes(asset.format.toUpperCase()) ? "Open original document" : "Open original file"} ↗</a></>
          </li>)}</ul></div>
          {chosenAsset && canDownloadPublicMap(chosenAsset) && <div className={p.selection} aria-label="Selected original transfer"><p className={s.eyebrow}>SAVE TO THIS COMPUTER</p><strong>{chosenAsset.title}</strong>
            {existing && <p className={p.storedNotice}>A completed copy is already stored on this computer. This starts a separate capture. <button type="button" className={s.textButton} onClick={onViewActivity}>View activity</button></p>}
            <p>{chosenAsset.expectedBytes === null ? "Size unknown. Enter a maximum before downloading." : `Reported file size ${bytes(chosenAsset.expectedBytes)}. A rounded-up maximum is ready for you to review.`}</p>
            {!connected && <div className={s.alert}><p>{connection === "unavailable" ? "The local download service could not be reached. Open KFM on this computer or retry the connection." : "Connect to the download service on this computer. No Google account is needed."}</p><button type="button" className={s.primaryButton} disabled={connection === "connecting"} aria-busy={connection === "connecting"} onClick={onConnect ?? downloads.connect}>{connection === "connecting" ? "Connecting…" : "Connect downloads · no login"}</button>{connection === "unavailable" && <p><a href={`http://127.0.0.1:4173/downloads#${collection === "satellite" ? "public-climate" : "public-maps"}`}>Open local KFM downloads →</a></p>}</div>}
            <label>Maximum download (MiB)<input ref={transfer} type="number" inputMode="decimal" min="0.001" step="0.001" value={maximum} onChange={e => setMaximum(e.target.value)} placeholder="Enter a maximum" /></label>
            {limit !== null && <p className={p.impact}>Storage for this original: {chosenAsset.expectedBytes === null ? `up to ${bytes(limit)}` : `${bytes(chosenAsset.expectedBytes)} at the currently reported size`}. Transfer maximum: <strong>{bytes(limit)}</strong>. Preparation may need additional space.</p>}
            {maximum && limit === null && <p role="alert">Choose a positive maximum within {bytes(status?.limitBytes ?? 500_000_000_000)} and at least the known file size.</p>}
            <button ref={transferAction} type="button" className={s.primaryButton} disabled={!connected || !!busy || limit === null || workerBusy} aria-busy={busy === "download"} onClick={() => { if (limit !== null) void downloads.startDownload(chosenAsset, limit); }}>{busy === "download" ? "Starting transfer…" : existing ? "Download a new copy" : "Download to this computer"}</button>
            {connected && workerBusy && <small>A transfer is already running. <button type="button" className={s.textButton} onClick={onViewActivity}>View activity</button></small>}
            <small>1 MiB = 1,048,576 bytes. The maximum is a stop limit. Originals remain private candidates.</small>
          </div>}
          {downloads.notice && <p className={s.alert} role="status">{downloads.notice}</p>}
          {collection === "satellite" ? <p>{selected.description}</p> : <PublicMapPreview record={selected} />}
          <details className={p.metadata}><summary>About this map &amp; source terms</summary><p>{selected.description}</p><dl>
            <div><dt>Publisher / record</dt><dd>{selected.publisher} · {selected.id}</dd></div><div><dt>Map / digital release year</dt><dd>{selected.mapYear ?? "Unknown"} / {selected.digitalYear ?? "Unknown"}</dd></div>
            <div><dt>Scale</dt><dd>{selected.scale ?? "Not supplied"}{selected.scaleUnit && !["ratio", "denominator"].includes(selected.scaleUnit) ? ` ${selected.scaleUnit}` : ""}</dd></div><div><dt>Original map CRS</dt><dd>{selected.crs ?? "Not supplied by catalog"}</dd></div><div><dt>Spatial accuracy</dt><dd>{selected.spatialAccuracy ?? "Not supplied by catalog"}</dd></div><div><dt>Geometry meaning</dt><dd>{selected.geometryRole || "No geometry supplied"}</dd></div><div><dt>Reuse terms · {selected.rights.status}</dt><dd>{selected.rights.text}</dd></div>
          </dl><div className={p.actions}><a href={selected.metadataUrl} target="_blank" rel="noreferrer">Source record ↗</a>{selected.rights.url && <a href={selected.rights.url} target="_blank" rel="noreferrer">Source terms ↗</a>}</div><p>Map dates, digital release, retrieval time and mining dates have separate meanings. Stored originals require source review and verified georeferencing before map display.</p></details>
        </>}
      </aside>
    </div>
  </section>;
}
