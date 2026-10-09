"use client";
import Link from "next/link";
import { useEffect, useMemo, useRef, useState } from "react";
import seed from "./public-map-catalog.json";
import { canDownloadPublicMap, filterPublicMaps, parsePublicMapCatalog, publicMapNmmrLinks, PUBLIC_MAP_PAGE_SIZE, publicMapSelectedLimit, type PublicMapCatalog, type PublicMapFilter, type PublicMapRecord } from "./public-map-catalog";
import { parsePublicMapStatus, publicMapJobLabels, publicMapReason, publicMapRequest, type PublicMapEndpoint, type PublicMapStatus } from "./public-map-client";
import { formatDownloadBytes as bytes } from "./local-download-client";
import { PublicMapPreview } from "./public-map-preview";
import s from "./downloads/workspace.module.css";
import p from "./public-map-browser.module.css";

const defaultFilter: PublicMapFilter = { text: "", publisher: "all", county: "all", year: "all", format: "all", availability: "all" };
const initialCatalog = parsePublicMapCatalog(seed);
const nmmrLinks = publicMapNmmrLinks(initialCatalog);
const stamp = (value: string) => new Date(value).toLocaleString();
const size = (value: number | null) => value === null ? "Size unknown" : bytes(value);
const coverageLabels = { seed: "Starting references · full catalog not checked", partial: "Partial catalog", complete: "Catalog checked", unavailable: "Catalog unavailable" };
const coverageReason = (reason: string) => /CERTIFICATE_VERIFY_FAILED|certificate verify failed|unable to get local issuer certificate/i.test(reason)
  ? "The provider’s secure connection could not be verified. Its current catalog coverage is unknown; retained references remain available."
  : reason;

export default function PublicMapBrowser() {
  const [catalog, setCatalog] = useState<PublicMapCatalog | null>(initialCatalog), [status, setStatus] = useState<PublicMapStatus | null>(null);
  const [connected, setConnected] = useState(false), [connecting, setConnecting] = useState(false), [epoch, setEpoch] = useState(0);
  const [failure, setFailure] = useState(""), [catalogFailure, setCatalogFailure] = useState(""), [notice, setNotice] = useState("");
  const [filter, setFilter] = useState(defaultFilter), [page, setPage] = useState(0), [selectedId, setSelectedId] = useState("");
  const [assetId, setAssetId] = useState(""), [maximum, setMaximum] = useState(""), [busy, setBusy] = useState("");
  const alive = useRef(true), selection = useRef(0), operations = useRef(new Set<AbortController>()), operationBusy = useRef(false);
  useEffect(() => {
    alive.current = true;
    return () => { alive.current = false; for (const controller of operations.current) controller.abort(); };
  }, []);
  useEffect(() => {
    // The loopback Site connects on mount; elsewhere the person connects explicitly.
    if (!epoch && window.location.origin !== "http://127.0.0.1:4173") return;
    const controller = new AbortController(); let timer: ReturnType<typeof setTimeout> | undefined, previousRefresh = "", first = true, catalogPending = true;
    const loadCatalog = async () => {
      try {
        const result = await publicMapRequest("/catalog", controller.signal);
        const parsed = result.response.ok ? parsePublicMapCatalog(result.body) : null;
        if (!parsed) throw new Error("The returned map catalog could not be checked.");
        if (!controller.signal.aborted) { setCatalog(parsed); setCatalogFailure(""); catalogPending = false; }
      } catch { if (!controller.signal.aborted) { catalogPending = true; setCatalogFailure("The current catalog is unavailable. Previously checked metadata remains visible; statewide completeness is unknown."); } }
    };
    const poll = async () => {
      if (first) setConnecting(true);
      try {
        const result = await publicMapRequest("/status", controller.signal);
        const parsed = result.response.ok ? parsePublicMapStatus(result.body) : null;
        if (!parsed) throw new Error("Unrecognized local map service.");
        if (controller.signal.aborted) return;
        setStatus(parsed); setConnected(true); setFailure("");
        if (catalogPending || parsed.refresh.state === "complete" && previousRefresh !== "complete") await loadCatalog();
        previousRefresh = parsed.refresh.state;
      } catch {
        if (!controller.signal.aborted) { setConnected(false); setFailure("Public-map downloads are unavailable on this computer. The catalog below remains browseable; reconnect after the local service is available."); }
      } finally {
        if (!controller.signal.aborted) { first = false; setConnecting(false); timer = setTimeout(() => void poll(), 5000); }
      }
    };
    void poll();
    return () => { controller.abort(); if (timer) clearTimeout(timer); };
  }, [epoch]);
  const rows = useMemo(() => filterPublicMaps(catalog?.records ?? [], filter), [catalog, filter]);
  const selected = catalog?.records.find(row => row.id === selectedId) ?? null;
  const chosenAsset = selected?.assets.find(asset => asset.id === assetId);
  const limit = chosenAsset ? publicMapSelectedLimit(maximum, chosenAsset, status?.limitBytes) : null;
  const pages = Math.max(1, Math.ceil(rows.length / PUBLIC_MAP_PAGE_SIZE)), currentPage = Math.min(page, pages - 1);
  const options = useMemo(() => ({
    publishers: [...new Set(catalog?.records.map(row => row.publisher) ?? [])].sort(), counties: [...new Set(catalog?.records.flatMap(row => row.counties) ?? [])].sort(),
    years: [...new Set(catalog?.records.flatMap(row => row.mapYear === null ? [] : [row.mapYear]) ?? [])].sort((a, b) => b - a),
    formats: [...new Set(catalog?.records.flatMap(row => row.assets.map(asset => asset.format)) ?? [])].sort(),
  }), [catalog]);
  const choose = (row: PublicMapRecord | null) => {
    selection.current++; setSelectedId(row?.id ?? ""); setAssetId(""); setMaximum(""); setNotice("");
  };
  const changeFilter = (key: keyof PublicMapFilter, value: string) => { setFilter(old => ({ ...old, [key]: value })); setPage(0); };
  const action = async (path: PublicMapEndpoint, payload: unknown, success: string, selectionBound = false) => {
    if (!status || !connected || operationBusy.current) return;
    operationBusy.current = true;
    const generation = selection.current, controller = new AbortController(); operations.current.add(controller); setBusy(path); setNotice("");
    try {
      const result = await publicMapRequest(path, controller.signal, payload, status.sessionToken);
      if (!result.response.ok) throw new Error("The local service did not accept this request. Reconnect to check its state before retrying.");
      if (alive.current) {
        if (!selectionBound || selection.current === generation) setNotice(success);
        setEpoch(value => value + 1);
      }
    } catch (cause) {
      if (alive.current && !controller.signal.aborted && (!selectionBound || selection.current === generation)) setNotice(cause instanceof Error ? cause.message : "The request could not be confirmed. Reconnect before retrying.");
    } finally { operations.current.delete(controller); operationBusy.current = false; if (alive.current) setBusy(""); }
  };
  const download = () => {
    if (!chosenAsset || !canDownloadPublicMap(chosenAsset) || limit === null) return;
    void action("/downloads", { requestId: crypto.randomUUID().replaceAll("-", ""), assetId: chosenAsset.id, maxBytes: limit }, "Download requested. Follow its confirmed progress below; stored originals remain candidates.", true);
  };
  const jobs = [...(status?.jobs ?? [])].sort((a, b) => Number(b.id === status?.active) - Number(a.id === status?.active) || b.createdAt.localeCompare(a.createdAt));
  return <section id="public-maps" className={`${s.jobs} ${p.catalog}`} aria-labelledby="public-map-heading">
    <header className={s.sectionHeading}><div><p className={s.eyebrow}>KANSAS MAP COLLECTIONS</p><h2 id="public-map-heading">Mine maps &amp; geologic maps</h2></div><Link href="/">Return to map →</Link></header>
    <p className={s.muted}>Search published map records from OSMRE, USGS and the Kansas Geological Survey. Browse the catalog, inspect a source, then select the files and download maximum that fit this computer.</p>
    <div className={p.actions}><button type="button" disabled={connecting} onClick={() => setEpoch(value => value + 1)}>{connecting ? "Connecting…" : connected ? "Reconnect map downloads" : "Connect map downloads"}</button><button type="button" disabled={!connected || !!busy || status?.refresh.state === "running"} onClick={() => void action("/refresh", {}, "Kansas catalog refresh requested. Source coverage is shown separately below.")}>{status?.refresh.state === "running" ? "Refreshing Kansas catalog…" : "Refresh all Kansas records"}</button><span>{connected ? "Connected to this computer" : "Reference catalog available"}</span></div>
    {failure && <p className={s.alert}>{failure}</p>}{catalogFailure && <p className={s.alert}>{catalogFailure}</p>}
    {status?.refresh.state === "failed" && <p className={s.alert}>Catalog refresh did not finish. The previous records remain visible; inspect each source’s coverage before drawing conclusions.</p>}
    <details className={p.coverage} open><summary>Source coverage · {catalog?.records.length.toLocaleString() ?? 0} indexed records</summary><ul>{catalog?.coverage.map(source => <li key={source.sourceId}>
      <strong>{source.title}</strong><span>{coverageLabels[source.state]} · {source.state === "unavailable" && (source.discoveredCount ?? source.recordCount) === 0 ? "Coverage unknown" : `${(source.discoveredCount ?? source.recordCount).toLocaleString()}${source.expectedCount === null ? " records; total unknown" : ` / ${source.expectedCount.toLocaleString()} records`}`}{source.seedReferenceCount ? ` + ${source.seedReferenceCount} starting references` : ""}</span>
      <p>{coverageReason(source.reason)}</p>{source.checkedAt && <small>Checked {stamp(source.checkedAt)}</small>}
      {source.sourceId === "osmre-nmmr" && <>
        {(nmmrLinks.search || nmmrLinks.request) && <nav className={p.sourceLinks} aria-label="Official NMMR research">
          {nmmrLinks.search && <a href={nmmrLinks.search} target="_blank" rel="noopener noreferrer" aria-label="Search official NMMR catalog (opens in a new tab)">Search official NMMR catalog ↗</a>}
          {nmmrLinks.request && <a href={nmmrLinks.request} target="_blank" rel="noopener noreferrer" aria-label="Request NMMR archival scans (opens in a new tab)">Request NMMR archival scans ↗</a>}
        </nav>}
        <p>Search by state (Kansas), county, commodity or document number. Original archival scans require a separate request. NMMR index points are finding aids, not mine boundaries; search results do not establish complete Kansas coverage.</p>
      </>}
    </li>)}</ul><p>Catalog records are finding aids. No results do not establish absence of mining or a complete geological survey.</p></details>
    <div className={p.filters}>
      <label>Find a map<input type="search" placeholder="Title, publication, county or mine" value={filter.text} onChange={e => changeFilter("text", e.target.value)} /></label>
      <label>Publisher<select value={filter.publisher} onChange={e => changeFilter("publisher", e.target.value)}><option value="all">All publishers</option>{options.publishers.map(value => <option key={value}>{value}</option>)}</select></label>
      <label>County<select value={filter.county} onChange={e => changeFilter("county", e.target.value)}><option value="all">All counties</option><option value="unknown">County not specified</option>{options.counties.map(value => <option key={value}>{value}</option>)}</select></label>
      <label>Map publication year<select value={filter.year} onChange={e => changeFilter("year", e.target.value)}><option value="all">All years</option><option value="unknown">Year unknown</option>{options.years.map(value => <option key={value}>{value}</option>)}</select></label>
      <label>File format<select value={filter.format} onChange={e => changeFilter("format", e.target.value)}><option value="all">All formats</option>{options.formats.map(value => <option key={value}>{value}</option>)}</select></label>
      <label>Availability<select value={filter.availability} onChange={e => changeFilter("availability", e.target.value)}><option value="all">All records</option><option value="download">Verified direct files</option><option value="service">Verified map services</option><option value="request">Request an original</option><option value="metadata">No verified direct file</option></select></label>
    </div>
    <p className={s.snapshot}>{rows.length.toLocaleString()} matching records · map publication year is separate from digital release, retrieval time and mining dates.</p>
    <div className={p.results}>
      <div><ul className={p.records}>{rows.slice(currentPage * PUBLIC_MAP_PAGE_SIZE, (currentPage + 1) * PUBLIC_MAP_PAGE_SIZE).map(row => <li key={row.id}><button type="button" aria-pressed={selectedId === row.id} onClick={() => choose(row)}><strong>{row.title}</strong><span>{row.publisher} · {row.mapYear ?? "Map year unknown"}</span><small>{row.counties.join(", ") || "County not specified"} · {row.assets.some(canDownloadPublicMap) ? "Direct file available" : "Source metadata / request"}</small></button></li>)}</ul>
      {!rows.length && <p className={s.empty}>No catalog records match these filters. Source coverage may be partial or unavailable.</p>}
      <nav className={s.pagination} aria-label="Public map catalog pages"><button type="button" disabled={currentPage === 0} onClick={() => setPage(currentPage - 1)}>Previous maps</button><span>Page {currentPage + 1} of {pages}</span><button type="button" disabled={currentPage + 1 >= pages} onClick={() => setPage(currentPage + 1)}>Next maps</button></nav></div>
      <aside className={p.detail} aria-label="Selected public map">
        {!selected ? <p>Select a map record to inspect its dates, source, scale, rights and available files.</p> : <>
          <h3>{selected.title}</h3><p>{selected.description}</p><dl>
            <div><dt>Publisher / record</dt><dd>{selected.publisher} · {selected.id}</dd></div><div><dt>Map / digital release year</dt><dd>{selected.mapYear ?? "Unknown"} / {selected.digitalYear ?? "Unknown"}</dd></div>
            <div><dt>Scale</dt><dd>{selected.scale === null ? "Not specified" : `${selected.scale}${selected.scaleUnit && !["ratio", "denominator"].includes(selected.scaleUnit) ? ` ${selected.scaleUnit}` : ""}`}</dd></div>
            <div><dt>Original map CRS</dt><dd>{selected.crs ?? "Not supplied by catalog"}</dd></div><div><dt>Spatial accuracy</dt><dd>{selected.spatialAccuracy ?? "Not supplied by catalog"}</dd></div>
            <div><dt>Geometry meaning</dt><dd>{selected.geometryRole || "No geometry supplied"}</dd></div><div><dt>Reuse terms · {selected.rights.status}</dt><dd>{selected.rights.text}</dd></div>
          </dl><div className={p.actions}><a href={selected.metadataUrl} target="_blank" rel="noreferrer">Source record ↗</a>{selected.rights.url && <a href={selected.rights.url} target="_blank" rel="noreferrer">Source terms ↗</a>}<button type="button" onClick={() => choose(null)}>Clear selection</button></div>
          <PublicMapPreview record={selected} />
          <h4>Originals &amp; services</h4><ul className={p.assets}>{selected.assets.map(asset => <li key={asset.id}><strong>{asset.title}</strong><span>{asset.format} · {size(asset.expectedBytes)} · {asset.availability === "verified" ? "Link checked" : asset.availability === "request-only" ? "Request from archive" : "Availability unverified"}</span>
            {canDownloadPublicMap(asset) ? <><a href={asset.url} target="_blank" rel="noreferrer">{["PDF", "JPEG", "JPG", "TIFF", "TIF", "GEOTIFF", "PNG"].includes(asset.format.toUpperCase()) ? "Open original document" : "Open original file"} ↗</a><button type="button" aria-pressed={assetId === asset.id} onClick={() => { selection.current++; setAssetId(asset.id); setMaximum(""); setNotice(""); }}>Select file to download</button></> : <a href={asset.url} target="_blank" rel="noreferrer">{asset.kind === "request" ? "Open archive request page" : asset.kind === "service" ? "Inspect source service" : "Check file with publisher"} ↗</a>}
          </li>)}</ul>
          {chosenAsset && canDownloadPublicMap(chosenAsset) && <div className={p.selection}><strong>Selected: {chosenAsset.title}</strong><p>{chosenAsset.expectedBytes === null ? "The provider has not supplied a reliable size. Choose a maximum; the transfer will stop at that limit." : `Source size: ${bytes(chosenAsset.expectedBytes)}. Choose a maximum at least this large.`}</p>
            <label>Maximum download (MiB)<input type="number" inputMode="decimal" min="0.001" step="0.001" value={maximum} onChange={e => setMaximum(e.target.value)} placeholder="Choose a maximum" /></label><small>1 MiB = 1,048,576 bytes. Limit: {bytes(status?.limitBytes ?? 500_000_000_000)}. Original stays in the private local store.</small>
            {limit !== null && <p>Storage for this original: {chosenAsset.expectedBytes === null ? `up to the selected ${bytes(limit)} maximum` : `${bytes(chosenAsset.expectedBytes)} at the currently reported size`}. Transfer maximum: {bytes(limit)}. Later map preparation may require additional space.</p>}
            {maximum && limit === null && <p role="alert">Choose a positive maximum within the service limit and at least the known file size.</p>}<button type="button" disabled={!connected || !!busy || limit === null || status?.active !== null} onClick={download}>{busy === "/downloads" ? "Requesting download…" : "Download selected original"}</button><p>Capture does not clear source terms or approve map display. A scan requires verified georeferencing before it can be an overlay.</p>
          </div>}
        </>}
      </aside>
    </div>
    {notice && <p className={s.alert} role="status">{notice}</p>}
    <div className={p.downloads}><h3>Public-map downloads</h3>{!connected && jobs.length > 0 && <p className={s.alert}>Last known jobs; reconnect to check their current state.</p>}
      {!jobs.length ? <p className={s.muted}>{connected ? "No map files downloaded yet. Select an original above to set its transfer limit." : "Connect to read this computer’s public-map jobs. Browsing records does not start a download."}</p> : <div className={s.jobList}>{jobs.slice(0, 12).map(job => <article key={job.id} className={s.job} data-state={job.state}><div className={s.jobHeading}><h3>{job.title}</h3><span className={s.jobState}>{publicMapJobLabels[job.state]}</span></div><div className={s.jobNumbers}><strong>{bytes(job.bytes)} <span>received</span></strong><span>{size(job.expectedBytes)} · maximum {bytes(job.maxBytes)}</span></div>
        {["queued", "downloading"].includes(job.state) && (job.expectedBytes === null ? <progress aria-label={`${job.title}: total size unknown`} /> : <progress value={job.bytes} max={job.expectedBytes} aria-label={`${job.title}: bytes received`} />)}
        {job.id === status?.active && <button type="button" disabled={!connected || !!busy} onClick={() => void action("/cancel", { id: job.id }, "Cancellation requested. Any retained bytes remain available for inspection.")}>Cancel map download</button>}
        {job.reason && <p className={s.jobReason}>{publicMapReason(job.reason)}</p>}<p className={s.jobNote}>{job.state === "downloaded" ? "Stored original candidate." : "Captured bytes remain candidates."} Source review, preparation and map availability are separate.</p><details className={s.jobDetails}><summary>File details</summary><dl><div><dt>Destination</dt><dd>{job.destination}</dd></div><div><dt>Stored-file SHA-256</dt><dd>{job.sha256 ?? "Not complete"}</dd></div><div><dt>Provider checksum verification</dt><dd>Not performed. The stored-file hash identifies retained bytes; it does not verify a publisher-supplied checksum.</dd></div><div><dt>Updated</dt><dd>{stamp(job.updatedAt)}</dd></div></dl></details></article>)}</div>}
      {jobs.length > 12 && <p className={s.muted}>Showing the 12 most recent jobs. Earlier originals remain in the local library.</p>}
    </div>
  </section>;
}
