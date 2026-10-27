"use client";
import Link from "next/link";
import StoragePanel from "./storage-panel";
import { useEffect, useState } from "react";
import { acquisitionJobLabels, parseAcquisitionInventory, formatAcquisitionBytes as size, type AcquisitionInventory } from "../acquisition-inventory";
import { createAcquisitionSession, readAcquisitionLocalJson } from "../acquisition-client";
import { TerrainProvenancePanel } from "../terrain-provenance";
import { parseAcquisitionTerrain, type AcquisitionTerrain } from "../acquisition-terrain";
import styles from "./workspace.module.css";

export default function AcquisitionWorkspace() {
  const [inventory, setInventory] = useState<AcquisitionInventory | null>(null);
  const [notice, setNotice] = useState("Import a local inventory JSON to inspect its recorded status.");
  const [scope, setScope] = useState("all");
  const [query, setQuery] = useState("");
  const [session] = useState(createAcquisitionSession);
  const [terrainSession] = useState(createAcquisitionSession);
  const [terrainDiscovery, setTerrainDiscovery] = useState<AcquisitionTerrain | null>(null);
  const [terrainNotice, setTerrainNotice] = useState("Import a local terrain discovery JSON to inspect its source metadata.");
  useEffect(() => () => session.cancel(), [session]);
  useEffect(() => () => terrainSession.cancel(), [terrainSession]);
  async function importFile(file: File | undefined) {
    if (!file) return;
    const request = session.begin();
    try {
      const result = parseAcquisitionInventory(await readAcquisitionLocalJson(file, request.signal));
      if (!result) throw new Error("Receipt failed validation. Use a kfm-acquisition-inventory-v1 export from the local acquisition tool.");
      if (request.current()) { setInventory(result); setNotice("Local preview loaded. Nothing has been uploaded or acquired."); }
    } catch (error) { if (request.current()) setNotice(error instanceof Error ? error.message : "Receipt cannot be read."); }
  }
  async function importTerrain(file: File | undefined) {
    if (!file) return;
    const request = terrainSession.begin();
    try {
      const result = parseAcquisitionTerrain(await readAcquisitionLocalJson(file, request.signal));
      if (!result) throw new Error("This is not a supported 3DEP snapshot, or it contains invalid or duplicate work-unit identities. The previous preview is retained.");
      if (request.current()) { setTerrainDiscovery(result); setTerrainNotice("Terrain metadata loaded locally. Nothing has been uploaded, saved, or admitted."); }
    } catch (error) { if (request.current()) setTerrainNotice(error instanceof Error ? error.message : "Terrain metadata cannot be read."); }
  }
  const jobs = inventory?.jobs.filter((job) => (scope === "all" || job.scope === scope) && `${job.label} ${job.source_id} ${job.dataset_id} ${job.reason}`.toLowerCase().includes(query.toLowerCase())) ?? [];
  return <main className={styles.page}>
    <header><Link href="/">KFM / Explorer</Link><nav aria-label="Acquisition navigation"><Link href="/earth-engine">History & recipes</Link><Link href="/?layers=sources">Source status &amp; files</Link><Link href="/acquisition" aria-current="page">Acquisition</Link></nav></header>
    <section className={styles.intro}><p className={styles.eyebrow}>LOCAL KANSAS DATA / RECEIPT REVIEW</p><h1>Data acquisition & terrain history</h1><p>Inspect saved acquisition receipts and terrain metadata from a separately configured local worker. This page does not connect to your computer, inspect its storage, or start downloads.</p></section>
    <div className={styles.policy}><strong>Inspect before transferring data</strong><p>Cache budgets belong to the separate local worker. Imported receipts show their recorded budget, selected file limits and capture status; they do not establish current free capacity. Ordinary worker completion requires an expected checksum; a separately recorded local capture without a provider checksum stays an unreviewed protected candidate.</p><p>Review the access for your registered Earth Engine project, remaining quota and export storage before running a recipe. <a href="https://developers.google.com/earth-engine/guides/noncommercial_tiers" target="_blank" rel="noreferrer">Check Earth Engine access and quotas ↗</a></p></div>
    <StoragePanel />
    <section aria-labelledby="receipt-heading" className={styles.panel}>
      <h2 id="receipt-heading">Acquisition receipts</h2><p><Link href="/?layers=sources">Open source status &amp; provider files →</Link></p><p>Inspect a saved status snapshot from the local worker. Files are inspected in this tab; importing a receipt does not upload it, start jobs or admit datasets.</p>
      <div className={styles.controls}><label>Import inventory JSON<input type="file" accept="application/json,.json" onChange={(e) => void importFile(e.target.files?.[0])} /></label></div>
      <p role="status" className={styles.notice}>{notice}</p>
      {inventory && <><p>Captured <time dateTime={inventory.generated_at}>{inventory.generated_at}</time> · Local preview · Candidate data only</p>
        <dl className={styles.stats}><div><dt>Recorded cache budget</dt><dd>{(inventory.cache.limit_bytes / 1_000_000_000).toLocaleString("en-US", { maximumFractionDigits: 9 })} GB · {size(inventory.cache.limit_bytes)}</dd></div><div><dt>Total cache use (includes temporary files)</dt><dd>{inventory.cache.inspected === true ? size(inventory.cache.used_bytes) : "Unknown — cache not inspected"}</dd></div><div><dt>Temporary files</dt><dd>{inventory.cache.inspected === true ? size(inventory.cache.temporary_bytes) : "Unknown"}</dd></div><div><dt>Reproducible completed cache</dt><dd>{inventory.cache.inspected === true ? size(inventory.cache.replaceable_bytes) : "Unknown"}</dd></div></dl>
        <p>This snapshot retains its recorded budget and selected file limits, including jobs recorded before a budget reduction. Change the worker budget through its local configuration; this page only reads imported receipts.</p>
        {inventory.cache.inspected !== true && <p>Cache inspection is {inventory.cache.inspected === false ? "not performed in this snapshot" : "not recorded"}. Available capacity is unknown; a cache budget is not a measurement of free space.</p>}
        {inventory.cache.inspected === true && inventory.cache.used_bytes > inventory.cache.limit_bytes && <p role="alert">This snapshot exceeds its recorded cache budget. Inspect current capacity before starting transfers.</p>}
        <div className={styles.controls}><label>Search jobs<input type="search" value={query} onChange={(e) => setQuery(e.target.value)} /></label><label>Area<select value={scope} onChange={(e) => setScope(e.target.value)}><option value="all">Kansas and global</option><option value="kansas">Kansas</option><option value="global">Global</option></select></label></div>
        <p>{jobs.length} matching jobs. Provider availability is not a download. Dates are the receipt’s recorded scope; unknown dates stay unknown.</p>
        <div className={styles.table} role="region" aria-label="Acquisition jobs" tabIndex={0}><table><thead><tr><th>Collection / source</th><th>Period & area</th><th>Transfer</th><th>Destination</th><th>Status</th></tr></thead><tbody>{jobs.map((job) => <tr key={job.job_id}>
          <td><strong>{job.label}</strong><br /><a href={job.source_url} target="_blank" rel="noreferrer">Provider source ↗</a><details><summary>Source identity</summary><code>{job.dataset_id}</code><p>{job.job_id}</p>{job.rights_url && <a href={job.rights_url} target="_blank" rel="noreferrer">Reuse terms ↗</a>}</details></td>
          <td>{job.temporal_start ?? "Unknown start"} → {job.temporal_end ?? "Unknown end"}<br />{job.scope}</td>
          <td>{size(job.downloaded_bytes)} captured / {job.expected_bytes === null ? "Expected size unknown" : size(job.expected_bytes)}<br />Estimate: {job.estimate_basis}{job.expected_bytes === null && job.approved_max_bytes != null && <p>Selected maximum: {size(job.approved_max_bytes)} · an upper bound, not a predicted final size</p>}{job.expected_bytes !== null && job.expected_bytes > 0 && <progress aria-label={`${job.label} captured bytes`} value={job.downloaded_bytes} max={job.expected_bytes} />}</td>
          <td>{acquisitionJobLabels(job).storage}{job.intended_destination === "local-pc" && <p>Selected destination: local PC</p>}</td>
          <td><strong>{acquisitionJobLabels(job).status}</strong>{acquisitionJobLabels(job).checksum && <p>{acquisitionJobLabels(job).checksum}</p>}<p>{job.reason}</p><small>As of {job.updated_at}</small>{job.sha256 && <details><summary>{acquisitionJobLabels(job).digest}</summary><code>{job.sha256}</code></details>}</td>
        </tr>)}</tbody></table></div>
      </>}
    </section>
    <section className={styles.panel} aria-label="Terrain metadata import"><div className={styles.controls}><label>Import terrain discovery JSON (1 MiB maximum)<input type="file" accept="application/json,.json" onChange={event => void importTerrain(event.target.files?.[0])} /></label></div><p role="status">{terrainNotice}</p>{terrainDiscovery && <p>Local preview · not uploaded · Candidate metadata only</p>}</section>
    <TerrainProvenancePanel discovery={terrainDiscovery ?? undefined} />
    <section className={styles.panel}><h2>Choosing Kansas and global volumes</h2><p>The ordinary worker requires an exact source, selected period, expected byte size or selected maximum, and expected checksum for each file. A separately recorded Earth Engine capture may have only a local readback hash; it remains a protected candidate with no provider-checksum or review claim. Compressed and expanded sizes, resolution, processing needs, destination and free capacity must be recorded before a bulk selection. Unknown values remain unresolved; there is no automatic global-size cutoff.</p><p>The receipt contains selected transfer bytes and the destination recorded when it was captured. Historical provider-hosted selections remain unchanged; new Kansas selections target the local PC. This is not an estimate of every provider archive or a claim that full-history Kansas coverage has been enumerated.</p><Link href="/earth-engine">Explore source history and prepare recipes →</Link></section>
  </main>;
}
