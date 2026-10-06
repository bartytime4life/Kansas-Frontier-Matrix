"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import { ACQUISITION_CACHE_LIMIT, acquisitionJobLabels, ACQUISITION_MAX_BYTES, parseAcquisitionInventory, formatAcquisitionBytes as size, type AcquisitionInventory } from "../acquisition-inventory";
import { browserJsonRequest } from "../browser-json-request";
import { acquisitionRead, createAcquisitionSession, readAcquisitionLocalJson, verifyAcquisitionSave } from "../acquisition-client";
import { TerrainProvenancePanel } from "../terrain-provenance";
import { acquisitionTerrainRead, parseAcquisitionTerrain, verifyAcquisitionTerrainSave, type AcquisitionTerrain } from "../acquisition-terrain";
import styles from "./workspace.module.css";

export default function AcquisitionWorkspace() {
  const [inventory, setInventory] = useState<AcquisitionInventory | null>(null);
  const [notice, setNotice] = useState("Loading saved owner receipt…");
  const [pending, setPending] = useState(false);
  const [local, setLocal] = useState(false);
  const [scope, setScope] = useState("all");
  const [query, setQuery] = useState("");
  const [session] = useState(createAcquisitionSession);
  const [terrainSession] = useState(createAcquisitionSession);
  const [terrainDiscovery, setTerrainDiscovery] = useState<AcquisitionTerrain | null>(null);
  const [terrainNotice, setTerrainNotice] = useState("Loading saved owner terrain metadata…");
  const [terrainLocal, setTerrainLocal] = useState(false);
  const [terrainPending, setTerrainPending] = useState(false);
  useEffect(() => {
    const request = terrainSession.begin();
    void browserJsonRequest("/api/acquisition/terrain", { signal: request.signal, maxBytes: ACQUISITION_MAX_BYTES + 1000 }).then(({ response, body }) => {
      if (!response.ok) throw new Error(response.status === 401 || response.status === 403 ? "Owner sign-in is required to load or save terrain metadata. Local preview remains available." : "Saved terrain metadata is unavailable. Local preview remains available.");
      const parsed = acquisitionTerrainRead(body);
      if (request.current()) { setTerrainDiscovery(parsed); setTerrainLocal(false); setTerrainNotice(parsed ? "Saved terrain metadata loaded. Candidate metadata only." : "No saved terrain metadata. Select a local 3DEP discovery.json to preview it."); }
    }).catch((error: unknown) => { if (request.current()) setTerrainNotice(error instanceof Error ? error.message : "Terrain metadata unavailable."); });
    return () => terrainSession.cancel();
  }, [terrainSession]);
  useEffect(() => {
    const request = session.begin();
    void browserJsonRequest("/api/acquisition", { signal: request.signal, maxBytes: ACQUISITION_MAX_BYTES + 1000 }).then(({ response, body }) => {
      if (!response.ok) throw new Error(response.status === 401 || response.status === 403 ? "Sign in as the owner to load or save receipts. Local preview remains available." : "Saved receipt is unavailable; import a local receipt to inspect it.");
      const parsed = acquisitionRead(body);
      if (request.current()) { setInventory(parsed); setLocal(false); setNotice(parsed ? "Saved receipt loaded. Progress is a snapshot, not a live worker feed." : "No saved acquisition receipt. Import a worker inventory to begin."); }
    }).catch((error: unknown) => { if (request.current()) setNotice(error instanceof Error ? error.message : "Receipt unavailable."); });
    return () => session.cancel();
  }, [session]);
  async function importFile(file: File | undefined) {
    if (!file) return;
    const request = session.begin();
    try {
      const result = parseAcquisitionInventory(await readAcquisitionLocalJson(file, request.signal));
      if (!result) throw new Error("Receipt failed validation. Use a kfm-acquisition-inventory-v1 export from the local acquisition tool.");
      if (request.current()) { setInventory(result); setLocal(true); setNotice("Local preview loaded. Nothing has been uploaded or acquired."); }
    } catch (error) { if (request.current()) setNotice(error instanceof Error ? error.message : "Receipt cannot be read."); }
  }
  async function importTerrain(file: File | undefined) {
    if (!file) return;
    const request = terrainSession.begin();
    try {
      const result = parseAcquisitionTerrain(await readAcquisitionLocalJson(file, request.signal));
      if (!result) throw new Error("This is not a supported 3DEP snapshot, or it contains invalid or duplicate work-unit identities. The previous preview is retained.");
      if (request.current()) { setTerrainDiscovery(result); setTerrainLocal(true); setTerrainNotice("Terrain metadata loaded locally. Nothing has been uploaded, saved, or admitted."); }
    } catch (error) { if (request.current()) setTerrainNotice(error instanceof Error ? error.message : "Terrain metadata cannot be read."); }
  }
  async function saveTerrain() {
    if (!terrainDiscovery || terrainPending) return;
    const request = terrainSession.begin(), submitted = terrainDiscovery;
    setTerrainPending(true);
    try {
      const { response, body } = await browserJsonRequest("/api/acquisition/terrain", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(submitted), signal: request.signal, maxBytes: ACQUISITION_MAX_BYTES + 1000 });
      if (!response.ok) throw new Error(response.status === 401 || response.status === 403 ? "Owner sign-in is required to save terrain metadata." : "Terrain metadata could not be saved. Your local preview is retained.");
      await verifyAcquisitionTerrainSave(body, submitted);
      if (request.current()) { setTerrainLocal(false); setTerrainNotice("Owner terrain metadata saved and verified. This does not fetch point clouds or admit datasets."); }
    } catch (error) { if (request.current()) setTerrainNotice(error instanceof Error ? error.message : "Terrain save failed."); }
    finally { if (request.current()) setTerrainPending(false); }
  }
  async function save() {
    if (!inventory || pending) return;
    const request = session.begin(), submitted = inventory;
    setPending(true);
    try {
      const { response, body } = await browserJsonRequest("/api/acquisition", { method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(submitted), signal: request.signal, maxBytes: ACQUISITION_MAX_BYTES + 1000 });
      if (!response.ok) throw new Error(response.status === 401 || response.status === 403 ? "Owner sign-in is required to save this receipt." : "The receipt could not be saved. Your local preview is retained.");
      await verifyAcquisitionSave(body, submitted);
      if (request.current()) { setLocal(false); setNotice("Owner receipt saved and verified. This does not run downloads or approve data."); }
    } catch (error) { if (request.current()) setNotice(error instanceof Error ? error.message : "Save failed."); }
    finally { if (request.current()) setPending(false); }
  }
  const jobs = inventory?.jobs.filter((job) => (scope === "all" || job.scope === scope) && `${job.label} ${job.source_id} ${job.dataset_id} ${job.reason}`.toLowerCase().includes(query.toLowerCase())) ?? [];
  return <main className={styles.page}>
    <header><Link href="/">KFM / Explorer</Link><nav aria-label="Acquisition navigation"><Link href="/earth-engine">History & recipes</Link><Link href="/acquisition" aria-current="page">Acquisition</Link></nav></header>
    <section className={styles.intro}><p className={styles.eyebrow}>LOCAL KANSAS DATA / 500 GB CACHE</p><h1>Data acquisition & terrain history</h1><p>Selected Kansas history belongs on this PC under Projects/KFM-data. Use the 500 GB replaceable cache for selected downloads; provider originals remain available remotely. You choose which global data and volumes to add.</p></section>
    <div className={styles.policy}><strong>No paid transport or automatic overages</strong><p>Current replaceable cache ceiling: 500 GB (about 465.7 GiB). Existing originals, evidence and backups stay separate and protected. Unbounded sizes and unavailable free capacity hold a transfer. Ordinary worker completion requires an expected checksum; a separately recorded local capture without a provider checksum stays an unreviewed protected candidate.</p><p>The owner reports verified Earth Engine Community eligibility for noncommercial research. The Community tier currently provides 150 EECU-hours per month. Current sign-in, remaining quota and available export storage are unverified. <a href="https://developers.google.com/earth-engine/guides/noncommercial_tiers" target="_blank" rel="noreferrer">Check current free access ↗</a></p></div>
    <section aria-labelledby="receipt-heading" className={styles.panel}>
      <h2 id="receipt-heading">Acquisition receipts</h2><p>Inspect a saved status snapshot from the local worker. Saving a receipt requires owner access; it does not start jobs or admit datasets.</p>
      <div className={styles.controls}><label>Import inventory JSON<input type="file" accept="application/json,.json" disabled={pending} onChange={(e) => void importFile(e.target.files?.[0])} /></label><button onClick={() => void save()} disabled={!inventory || !local || pending}>{pending ? "Saving…" : "Save receipt to private Site"}</button></div>
      <p role="status" className={styles.notice}>{notice}</p>
      {inventory && <><p>Captured <time dateTime={inventory.generated_at}>{inventory.generated_at}</time> · {local ? "Local preview" : "Saved snapshot"} · Candidate data only</p>
        <dl className={styles.stats}><div><dt>Recorded cache budget</dt><dd>{(inventory.cache.limit_bytes / 1_000_000_000).toLocaleString("en-US", { maximumFractionDigits: 9 })} GB · {size(inventory.cache.limit_bytes)}</dd></div><div><dt>Total cache use (includes temporary files)</dt><dd>{inventory.cache.inspected === true ? size(inventory.cache.used_bytes) : "Unknown — cache not inspected"}</dd></div><div><dt>Temporary files</dt><dd>{inventory.cache.inspected === true ? size(inventory.cache.temporary_bytes) : "Unknown"}</dd></div><div><dt>Reproducible completed cache</dt><dd>{inventory.cache.inspected === true ? size(inventory.cache.replaceable_bytes) : "Unknown"}</dd></div></dl>
        {inventory.cache.limit_bytes < ACQUISITION_CACHE_LIMIT && <p>This snapshot records a lower cache budget than the current 500 GB ceiling. Loading or saving it preserves its recorded budget and selected file limits; it does not start transfers.</p>}
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
    <section className={styles.panel} aria-label="Terrain metadata import"><div className={styles.controls}><label>Import terrain discovery JSON (1 MiB maximum)<input type="file" accept="application/json,.json" disabled={terrainPending} onChange={event => void importTerrain(event.target.files?.[0])} /></label><button onClick={() => void saveTerrain()} disabled={!terrainDiscovery || !terrainLocal || terrainPending}>{terrainPending ? "Saving terrain…" : "Save terrain metadata to private Site"}</button></div><p role="status">{terrainNotice}</p>{terrainDiscovery && <p>{terrainLocal ? "Local preview · not uploaded" : "Saved owner snapshot"} · Candidate metadata only</p>}</section>
    <TerrainProvenancePanel discovery={terrainDiscovery ?? undefined} />
    <section className={styles.panel}><h2>Choosing Kansas and global volumes</h2><p>The ordinary worker requires an exact source, selected period, expected byte size or selected maximum, and expected checksum for each file. A separately recorded Earth Engine capture may have only a local readback hash; it remains a protected candidate with no provider-checksum or review claim. Compressed and expanded sizes, resolution, processing needs, destination and free capacity must be recorded before a bulk selection. Unknown values remain unresolved; there is no automatic global-size cutoff.</p><p>The receipt contains selected transfer bytes and the destination recorded when it was captured. Historical provider-hosted selections remain unchanged; new Kansas selections target the local PC. This is not an estimate of every provider archive or a claim that full-history Kansas coverage has been enumerated.</p><Link href="/earth-engine">Explore source history and prepare recipes →</Link></section>
  </main>;
}
