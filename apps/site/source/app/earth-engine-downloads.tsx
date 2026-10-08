"use client";
import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import type { EarthEngineDataset } from "./earth-engine-data";
import { useLocalDownloads } from "./use-local-downloads";
import { DownloadJob } from "./download-job";
import { downloadReasons, formatDownloadBytes as bytes } from "./local-download-client";
import styles from "./earth-engine/workspace.module.css";
export { parseDownloadStatus } from "./local-download-client";

export default function EarthEngineDownloads({ dataset, year, invalid }: { dataset: EarthEngineDataset; year: number | undefined; invalid: boolean }) {
  const downloads = useLocalDownloads(), { status, connection } = downloads;
  const [notice, setNotice] = useState(""), [busy, setBusy] = useState<"auth" | "start" | null>(null);
  const [limit, setLimit] = useState(8_000_000_000), [project, setProject] = useState(""), [authUrl, setAuthUrl] = useState("");
  const alive = useRef(true), pending = useRef<{ key: string; id: string } | null>(null);
  useEffect(() => { alive.current = true; return () => { alive.current = false; }; }, []);
  const connected = connection === "connected", selectedYear = year ?? null;
  const job = status?.jobs.filter(item => item.selection.dataset === dataset.id && item.selection.year === selectedYear).sort((a, b) => b.createdAt.localeCompare(a.createdAt))[0];
  const activeJob = status?.jobs.find(item => item.id === status.active);
  const requestLimit = dataset.recipeKind === "inventory" ? 32_000_000 : limit;
  const disabledReason = !connected ? "Connect the local service to begin." : invalid ? "Choose a valid source year above." : !status?.configured ? "Link your Earth Engine project before downloading." : status.active ? "A background download is running. Follow it below or open the download center." : "This selection starts only when you press Download.";
  async function signIn() {
    if (!/^[a-z][a-z0-9-]{4,61}[a-z0-9]$/.test(project.trim())) { setNotice("Enter your Earth Engine Google Cloud project ID."); return; }
    if (busy) return;
    setBusy("auth"); setNotice(""); setAuthUrl("");
    try {
      const { response, body } = await downloads.post("/auth/start", { project: project.trim() });
      const value = body as { url?: unknown };
      if (!response.ok || !value || typeof value.url !== "string") throw new Error("Sign-in could not start. Check the project ID and finish any running download.");
      const url = new URL(value.url);
      if (url.origin !== "https://accounts.google.com" || url.pathname !== "/o/oauth2/auth") throw new Error("Unexpected sign-in destination.");
      if (alive.current) { setAuthUrl(url.href); window.open(url.href, "_blank", "noopener,noreferrer"); setNotice("Finish Google’s sign-in in the new tab, then return here. If no tab opened, use Continue with Google."); downloads.refresh(); }
    } catch { if (alive.current) setNotice("Could not open Google sign-in. Connect the local service and check the project ID, then try again."); }
    finally { if (alive.current) setBusy(null); }
  }
  async function start() {
    if (!status || invalid || busy || !connected) return;
    setBusy("start"); setNotice("");
    const key = JSON.stringify([dataset.id, selectedYear, requestLimit]);
    const request = pending.current?.key === key ? pending.current : { key, id: crypto.randomUUID().replaceAll("-", "") };
    pending.current = request;
    try {
      const { response, body } = await downloads.post("/downloads", { selection: { dataset: dataset.id, year: selectedYear, maxBytes: requestLimit }, requestId: request.id });
      const value = body as { error?: string; id?: string; selection?: { dataset?: string; year?: number | null; maxBytes?: number }; mapReady?: boolean };
      if (!response.ok) { pending.current = null; throw new Error(downloadReasons[value?.error ?? ""] ?? "Download could not start. Reconnect and check local setup."); }
      if (value?.id !== request.id || value.mapReady !== false || JSON.stringify([value.selection?.dataset, value.selection?.year, value.selection?.maxBytes]) !== key) throw new Error("Download start was not confirmed. Check the download center before retrying; a retry retains this request ID.");
      pending.current = null;
      if (alive.current) { downloads.refresh(); setNotice("Download started in the background. Follow every job in Library & downloads; you can leave this page."); }
    } catch (error) { if (alive.current) setNotice(error instanceof Error ? error.message : "Start was not confirmed. Check background jobs before retrying."); }
    finally { if (alive.current) setBusy(null); }
  }
  return <section className={styles.downloadPanel} aria-label="Download selected Earth Engine data">
    <div className={styles.downloadHeading}><h3>Download to KFM</h3><Link href="/downloads">Library &amp; all downloads →</Link></div>
    <p>{dataset.recipeKind === "inventory" ? "Capture this year’s source inventory. Raster downloads need a separate choice of variables and processing product." : `Capture the Kansas ${year ?? "fixed"} ${dataset.recipe.toLowerCase()} as GeoTIFF tiles with source IDs and file hashes.`}</p>
    <div className={styles.downloadConnection}><span>{connected ? "Local download service connected" : connection === "connecting" ? "Connecting to this computer…" : connection === "unavailable" ? "Local service unavailable" : "Local service not connected"}</span>{!connected && <button type="button" disabled={connection === "connecting"} aria-busy={connection === "connecting"} onClick={downloads.connect}>{connection === "connecting" ? "Connecting…" : "Connect local downloads"}</button>}</div>
    {!connected && <small>Start the local service on this computer to read jobs and download selected data. <Link href="/earth-engine-downloads/setup">Connection help</Link></small>}
    <details className={styles.signIn} open={!status?.configured}><summary>{status?.configured ? `Linked project · ${status.project}` : "Link your Earth Engine project"}</summary>
      <label>Google Cloud project ID<input autoComplete="off" aria-label="Earth Engine project ID" placeholder="your-earth-engine-project" value={project} maxLength={63} onChange={event => setProject(event.target.value)} /></label>
      <button type="button" disabled={!connected || Boolean(busy) || Boolean(status?.active) || status?.authentication === "validating"} aria-busy={busy === "auth"} onClick={() => void signIn()}>{busy === "auth" ? "Opening Google sign-in…" : "Sign in with Google Earth Engine"}</button>
      {!connected && <small>Connect local downloads above to enable sign-in.</small>}
      {authUrl && status?.authentication !== "connected" && <a href={authUrl} target="_blank" rel="noreferrer">Continue with Google ↗</a>}
      {status?.authentication === "validating" && <p>Checking your Earth Engine project…</p>}
      {status?.authentication === "waiting" && <p>Finish Google sign-in in the opened tab, then return here.</p>}
      {["failed", "expired", "declined"].includes(status?.authentication ?? "") && <p>Sign-in {status?.authentication === "failed" ? "could not verify project access" : status?.authentication === "expired" ? "expired" : "was cancelled"}. You can try again.</p>}
      <small>Find the project ID in <a href="https://code.earthengine.google.com/" target="_blank" rel="noreferrer">Earth Engine</a>. Google handles account selection and consent; credentials stay on this computer.</small>
    </details>
    {status && <p className={styles.destination}>Selected destination<code>{status.destination}/{dataset.id}/{year ?? "fixed"}/</code></p>}
    {dataset.recipeKind !== "inventory" ? <label>Maximum download size<select value={limit} onChange={event => setLimit(Number(event.target.value))}>{[32_000_000, 256_000_000, 2_000_000_000, 8_000_000_000, 32_000_000_000, 100_000_000_000, 500_000_000_000].map(value => <option key={value} value={value}>{bytes(value)}</option>)}</select><small>A stop limit you choose, not an estimate of final size.</small></label> : <p>Inventory transfer maximum: {bytes(requestLimit)}.</p>}
    <button type="button" className={styles.primary} disabled={!connected || Boolean(busy) || invalid || !status?.configured || Boolean(status?.active)} aria-busy={busy === "start"} aria-describedby="selected-download-reason" onClick={() => void start()}>{busy === "start" ? "Starting download…" : dataset.recipeKind === "inventory" ? "Download inventory" : `Download ${year ?? "dataset"} to KFM`}</button>
    <small id="selected-download-reason">{disabledReason}</small>
    {(activeJob ?? job) && <><p className={styles.downloadCurrent}>{activeJob && activeJob.id !== job?.id ? "Another selection is running in the background" : "This selection’s latest job"}{!connected ? " · last known status" : ""}</p><DownloadJob job={(activeJob ?? job)!} active={Boolean(activeJob)} connected={connected} cancelling={downloads.cancelling} onCancel={() => void downloads.cancelJob()} compact /></>}
    <p role="status" aria-live="polite" aria-atomic="true">{notice}</p>
    <p role="status" aria-live="polite" aria-atomic="true">{downloads.announcement}</p>
    <details><summary>Local setup &amp; captured data</summary><p>Each click selects one dataset and year. Annual composites are map products, not every original scene. New captures remain private candidates until map review. Existing approved periods remain available.</p><p>RGB and elevation exports use the existing 30 m map grid; Dynamic World keeps a 10 m grid. Climate products retain their documented grids. Partial files remain available after cancellation.</p><Link href="/earth-engine-downloads/setup">Local setup guide →</Link></details>
  </section>;
}
