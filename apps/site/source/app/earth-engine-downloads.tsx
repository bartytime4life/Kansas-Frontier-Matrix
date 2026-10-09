"use client";
import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import type { EarthEngineDataset } from "./earth-engine-data";
import { useLocalDownloads, type LocalDownloads } from "./use-local-downloads";
import { DownloadJob } from "./download-job";
import { downloadReasons, formatDownloadBytes as bytes } from "./local-download-client";
import styles from "./earth-engine/workspace.module.css";
export { parseDownloadStatus } from "./local-download-client";

type Props = { dataset: EarthEngineDataset; year: number | undefined; invalid: boolean;
  downloads?: LocalDownloads; blockedByOtherDownload?: boolean; onViewActivity?: () => void; compact?: boolean };
export default function EarthEngineDownloads(props: Props) {
  return props.downloads ? <EarthEngineDownloadForm {...props} downloads={props.downloads} shared /> : <StandaloneEarthEngineDownloads {...props} />;
}
function StandaloneEarthEngineDownloads(props: Props) {
  const downloads = useLocalDownloads();
  return <EarthEngineDownloadForm {...props} downloads={downloads} />;
}
export function EarthEngineDownloadForm({ dataset, year, invalid, downloads, blockedByOtherDownload = false, onViewActivity, compact = false, shared = false }: Props & { downloads: LocalDownloads; shared?: boolean }) {
  const { status, connection } = downloads;
  const [notice, setNotice] = useState(""), [busy, setBusy] = useState<"auth" | "check" | "start" | null>(null);
  const [limit, setLimit] = useState(8_000_000_000), [project, setProject] = useState(""), [authUrl, setAuthUrl] = useState("");
  const alive = useRef(true), pending = useRef<{ key: string; id: string } | null>(null), operating = useRef(false), selection = useRef(0);
  useEffect(() => { alive.current = true; return () => { alive.current = false; }; }, []);
  const connected = connection === "connected", selectedYear = year ?? null;
  const job = status?.jobs.filter(item => item.selection.dataset === dataset.id && item.selection.year === selectedYear).sort((a, b) => b.createdAt.localeCompare(a.createdAt))[0];
  const activeJob = status?.jobs.find(item => item.id === status.active);
  const requestLimit = dataset.recipeKind === "inventory" ? 32_000_000 : limit;
  const selectionKey = JSON.stringify([dataset.id, selectedYear, requestLimit]);
  useEffect(() => { selection.current++; if (pending.current?.key !== selectionKey) pending.current = null; }, [selectionKey]);
  const stored = downloads.library?.entries.filter(entry => entry.lane === "raw" && entry.dataset === dataset.id && entry.period === String(year ?? "fixed")) ?? [];
  const storedFiles = stored.reduce((sum, entry) => sum + entry.files, 0), storedBytes = stored.reduce((sum, entry) => sum + entry.bytes, 0);
  const authPending = ["waiting", "validating"].includes(status?.authentication ?? "");
  useEffect(() => { if (status?.project) setProject(status.project); }, [status?.project]);
  useEffect(() => { if (status?.signedIn) { setAuthUrl(""); setNotice(""); } }, [status?.signedIn]);
  const blocked = blockedByOtherDownload || Boolean(status?.active) || downloads.starting;
  const disabledReason = !connected ? "Connect the local service to begin." : invalid ? "Choose a valid source year above." : !status?.configured ? status?.signedIn ? "Choose a project and check download access." : "Sign in with Google to authorize Earth Engine downloads." : blocked ? "A background download is running or starting. View Activity before starting another." : "This selection starts only when you press Download.";
  async function signIn() {
    if (operating.current || blocked) return;
    operating.current = true;
    setBusy("auth"); setNotice(""); setAuthUrl("");
    try {
      const { response, body } = await downloads.post("/auth/start", {});
      const value = body as { url?: unknown };
      if (!response.ok || !value || typeof value.url !== "string") throw new Error("Sign-in could not start. Finish any running download and try again.");
      const url = new URL(value.url);
      if (url.origin !== "https://accounts.google.com" || url.pathname !== "/o/oauth2/auth") throw new Error("Unexpected sign-in destination.");
      if (alive.current) { setAuthUrl(url.href); window.open(url.href, "_blank", "noopener,noreferrer"); setNotice("Finish Google’s sign-in in the new tab, then return here. If no tab opened, use Continue with Google."); downloads.refresh(); }
    } catch { if (alive.current) setNotice("Could not open Google sign-in. Connect the local service and try again."); }
    finally { operating.current = false; if (alive.current) setBusy(null); }
  }
  async function checkAccess() {
    if (operating.current || blocked || authPending || !connected) return;
    if (project.trim() && !/^[a-z][a-z0-9-]{4,61}[a-z0-9]$/.test(project.trim())) { setNotice("Enter a valid Google Cloud project ID."); return; }
    operating.current = true; setBusy("check"); setNotice("");
    try {
      const { response } = await downloads.post("/auth/check", project.trim() ? { project: project.trim() } : {});
      if (!response.ok) throw new Error("Access check failed");
      if (alive.current) { downloads.refresh(); setNotice("Checking Google permissions…"); }
    } catch { if (alive.current) setNotice("Could not check access. Reconnect the local service and try again."); }
    finally { operating.current = false; if (alive.current) setBusy(null); }
  }
  async function start() {
    if (!status || !status.configured || invalid || operating.current || blocked || !connected) return;
    operating.current = true; downloads.setStarting(true); setBusy("start"); setNotice("");
    const generation = selection.current, key = selectionKey;
    const request = pending.current?.key === key ? pending.current : { key, id: crypto.randomUUID().replaceAll("-", "") };
    pending.current = request;
    let confirmed = false;
    try {
      const { response, body } = await downloads.post("/downloads", { selection: { dataset: dataset.id, year: selectedYear, maxBytes: requestLimit }, requestId: request.id });
      const value = body as { error?: string; id?: string; selection?: { dataset?: string; year?: number | null; maxBytes?: number }; mapReady?: boolean };
      if (!response.ok) throw new Error(downloadReasons[value?.error ?? ""] ?? "Download could not start. Reconnect and check local setup.");
      if (value?.id !== request.id || value.mapReady !== false || JSON.stringify([value.selection?.dataset, value.selection?.year, value.selection?.maxBytes]) !== key) throw new Error("Download start was not confirmed. Check the download center before retrying; a retry retains this request ID.");
      confirmed = true; downloads.confirmStart();
      if (pending.current === request) pending.current = null;
      if (alive.current) { downloads.refresh(); if (selection.current === generation) setNotice("Download started in the background. Follow every job in Library & downloads; you can leave this page."); }
    } catch (error) { if (alive.current && selection.current === generation) setNotice(error instanceof Error ? error.message : "Start was not confirmed. Check background jobs before retrying."); }
    finally { operating.current = false; if (!confirmed) downloads.setStarting(false); if (alive.current) setBusy(null); }
  }
  return <section className={styles.downloadPanel} aria-label="Download selected Earth Engine data">
    <div className={styles.downloadHeading}><h3>Download to KFM</h3>{!compact && <Link href="/downloads">Library &amp; all downloads →</Link>}</div>
    <p>{dataset.recipeKind === "inventory" ? "Capture this year’s source inventory. Raster downloads need a separate choice of variables and processing product." : `Capture the Kansas ${year ?? "fixed"} ${dataset.recipe.toLowerCase()} as GeoTIFF tiles with source IDs and file hashes.`}</p>
    {!shared && <><div className={styles.downloadConnection}><span>{connected ? "Local download service connected" : connection === "connecting" ? "Connecting to this computer…" : connection === "unavailable" ? "Local service unavailable" : "Local service not connected"}</span>{!connected && <button type="button" disabled={connection === "connecting"} aria-busy={connection === "connecting"} onClick={downloads.connect}>{connection === "connecting" ? "Connecting…" : "Connect local downloads"}</button>}</div>
    {!connected && <small>Start the local service on this computer to read jobs and download selected data. <Link href="/earth-engine-downloads/setup">Connection help</Link></small>}</>}
    <section className={styles.signIn} aria-label="Google account and download access">
      <h4>{status?.signedIn ? status.accountEmail ? `Signed in · ${status.accountEmail}` : "Google account connected" : "Connect your Google account"}</h4>
      <p role="status" aria-live="polite">{!connected ? "Connect this computer to check your account." : status?.configured ? `Download access verified · ${status.project}` : status?.authentication === "validating" ? "Checking Google account and project permissions…" : status?.authentication === "waiting" ? "Finish Google sign-in in the opened tab. This page will detect when you return." : status?.signedIn ? "Signed in. Choose an Earth Engine project to enable downloads." : "Sign in once on this computer. KFM detects the result automatically."}</p>
      <button type="button" disabled={!connected || Boolean(busy) || blocked || status?.authentication === "validating"} aria-busy={busy === "auth"} onClick={() => void signIn()}>{busy === "auth" ? "Opening Google sign-in…" : status?.signedIn ? "Use another Google account" : "Sign in with Google"}</button>
      {authUrl && status?.authentication === "waiting" && <a href={authUrl} target="_blank" rel="noreferrer">Continue with Google ↗</a>}
      {["failed", "expired", "declined"].includes(status?.authentication ?? "") && <p>Sign-in {status?.authentication === "failed" ? "could not be verified. Sign in again to grant Earth Engine access" : status?.authentication === "expired" ? "expired" : "was cancelled"}.</p>}
      {status?.signedIn && <>
        {(status.projects?.length ?? 0) > 0 && <label>Your Google Cloud projects<select aria-label="Choose Earth Engine project" value={status.projects?.includes(project) ? project : ""} onChange={event => setProject(event.target.value)}><option value="">Choose a project</option>{status.projects?.map(id => <option key={id} value={id}>{id}</option>)}</select></label>}
        <label>Google Cloud project ID<input autoComplete="off" aria-label="Earth Engine project ID" placeholder="your-earth-engine-project" value={project} maxLength={63} onChange={event => setProject(event.target.value)} /></label>
        <button type="button" disabled={!connected || Boolean(busy) || blocked || authPending || !project.trim()} onClick={() => void checkAccess()}>Check download access</button>
        {status.projectDiscovery === "unavailable" && <p>Google’s project list is unavailable. You can enter an existing project ID above.</p>}
        {status.projectDiscovery === "limited" && <p>Showing a limited project list. Enter another project ID if yours is missing.</p>}
        {status.projectDiscovery === "complete" && !status.projects?.length && <p>No accessible projects were found for this account.</p>}
        {status.authError === "PROJECT_ACCESS_REQUIRED" && <p>This account cannot yet use that project for Earth Engine. Check its Earth Engine registration, API and your project permissions.</p>}
        <small>Google requires a registered Earth Engine project. <a href="https://code.earthengine.google.com/" target="_blank" rel="noreferrer">Choose or register a project in Earth Engine ↗</a>. KFM checks access when you select Check download access.</small>
      </>}
      {!status?.signedIn && <button type="button" disabled={!connected || Boolean(busy) || blocked || authPending} onClick={() => void checkAccess()}>Check existing Google sign-in</button>}
      <small>Google asks for Earth Engine access, your email and read-only access to your project list. Consent and credentials stay on this computer. Free direct-file maps do not need Google sign-in.</small>
    </section>
    <div className={styles.downloadConnection}><div><strong>Already on this computer</strong><p>{downloads.library?.generatedAt ? storedFiles ? `${storedFiles.toLocaleString()} stored files · ${bytes(storedBytes)} for ${year ?? "this period"}` : "No stored files found for this dataset and period in the last library scan." : "Connect and scan My library to check stored files."}</p>{storedFiles > 0 && <small>Stored files may include partial captures; map review is separate.</small>}</div><Link href="/downloads#library">View My library →</Link></div>
    {status && <p className={styles.destination}>Selected destination<code>{status.destination}/{dataset.id}/{year ?? "fixed"}/</code></p>}
    {dataset.recipeKind !== "inventory" ? <label>Maximum download size<select value={limit} onChange={event => setLimit(Number(event.target.value))}>{[32_000_000, 256_000_000, 2_000_000_000, 8_000_000_000, 32_000_000_000, 100_000_000_000, 500_000_000_000].map(value => <option key={value} value={value}>{bytes(value)}</option>)}</select><small>A stop limit you choose, not an estimate of final size.</small></label> : <p>Inventory transfer maximum: {bytes(requestLimit)}.</p>}
    <button type="button" className={styles.primary} disabled={!connected || Boolean(busy) || invalid || !status?.configured || blocked} aria-busy={busy === "start"} aria-describedby="selected-download-reason" onClick={() => void start()}>{busy === "start" ? "Starting download…" : dataset.recipeKind === "inventory" ? "Download inventory" : `Download ${year ?? "dataset"} to KFM`}</button>
    <small id="selected-download-reason">{disabledReason}</small>
    {blocked && onViewActivity && <button type="button" onClick={onViewActivity}>View activity</button>}
    {!shared && (activeJob ?? job) && <><p className={styles.downloadCurrent}>{activeJob && activeJob.id !== job?.id ? "Another selection is running in the background" : "This selection’s latest job"}{!connected ? " · last known status" : ""}</p><DownloadJob job={(activeJob ?? job)!} active={Boolean(activeJob)} connected={connected} cancelling={downloads.cancelling} onCancel={() => void downloads.cancelJob()} compact /></>}
    <p role="status" aria-live="polite" aria-atomic="true">{notice}</p>
    {!shared && <p role="status" aria-live="polite" aria-atomic="true">{downloads.announcement}</p>}
    <details><summary>Local setup &amp; captured data</summary><p>Each click selects one dataset and year. Annual composites are map products, not every original scene. New captures remain private candidates until map review. Existing approved periods remain available.</p><p>RGB and elevation exports use the existing 30 m map grid; Dynamic World keeps a 10 m grid. Climate products retain their documented grids. Partial files remain available after cancellation.</p><Link href="/earth-engine-downloads/setup">Local setup guide →</Link></details>
  </section>;
}
