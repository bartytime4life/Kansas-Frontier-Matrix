"use client";
import Link from "next/link";
import { useMemo, useState } from "react";
import { useLocalDownloads } from "../use-local-downloads";
import { useEarthEngineContext } from "../earth-engine-context-client";
import { earthEngineSetYear } from "../earth-engine-context";
import { EARTH_ENGINE_DATASETS } from "../earth-engine-data";
import { formatDownloadBytes as bytes, libraryRoleLabels } from "../local-download-client";
import { DownloadJob } from "../download-job";
import styles from "./workspace.module.css";

const pageSize = 12, jobsPerPage = 6;
const when = (stamp: string) => new Date(stamp).toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" });
export default function DownloadsWorkspace() {
  const downloads = useLocalDownloads(), reviewed = useEarthEngineContext();
  const { status, library, connection } = downloads;
  const connected = connection === "connected", snapshot = library?.generatedAt ? library : null;
  const scanning = library?.state === "scanning", stale = Boolean(downloads.libraryError || library?.state === "failed" || !connected);
  const [query, setQuery] = useState(""), [role, setRole] = useState("all"), [page, setPage] = useState(0), [jobPage, setJobPage] = useState(0);
  const collections = useMemo(() => (library?.entries ?? []).filter(entry => (role === "all" || entry.role === role) && `${entry.label} ${entry.lane} ${libraryRoleLabels[entry.role]}`.toLowerCase().includes(query.trim().toLowerCase())), [library, query, role]);
  const pages = Math.max(1, Math.ceil(collections.length / pageSize)), currentPage = Math.min(page, pages - 1);
  const shownCollections = collections.slice(currentPage * pageSize, (currentPage + 1) * pageSize);
  const jobs = useMemo(() => [...(status?.jobs ?? [])].sort((a, b) => Number(b.id === status?.active) - Number(a.id === status?.active) || b.createdAt.localeCompare(a.createdAt)), [status]);
  const jobPages = Math.max(1, Math.ceil(jobs.length / jobsPerPage)), currentJobPage = Math.min(jobPage, jobPages - 1);
  const approved = reviewed.manifests.flatMap(manifest => manifest.layers.filter(layer => layer.status === "approved").map(layer => ({ key: `${manifest.setId}/${layer.id}`, title: EARTH_ENGINE_DATASETS.find(source => source.id === layer.id)?.title ?? layer.id, year: layer.id === "ee-3dep" ? "Mixed dates" : earthEngineSetYear(manifest), period: layer.period })));
  return <main className={styles.page}>
    <div className={styles.wrap}>
      <header className={styles.header}><Link href="/" className={styles.brand}>KFM <span>EXPLORER</span></Link><nav aria-label="Data navigation"><Link href="/">Map</Link><Link href="/downloads" aria-current="page">Library &amp; downloads</Link><Link href="/earth-engine">Choose data</Link><Link href="/acquisition">Receipts</Link></nav></header>
      <section className={styles.intro}><div><p className={styles.eyebrow}>YOUR KANSAS DATA WORKBENCH</p><h1>Local library &amp; downloads</h1><p>See what is stored, follow a transfer, and find reviewed map periods.</p></div><Link className={styles.primaryLink} href="/earth-engine">Choose data to download <span aria-hidden="true">↗</span></Link></section>
      <section className={styles.connection} aria-label="Local service connection"><div><span className={styles.connectionDot} data-connected={connected} aria-hidden="true"/><strong>{connected ? "Connected to this computer" : connection === "connecting" ? "Connecting to this computer…" : connection === "unavailable" ? "Local service unavailable" : "Connect to this computer"}</strong>{connected && downloads.lastChecked && <span>Checked <time dateTime={downloads.lastChecked}>{when(downloads.lastChecked)}</time></span>}</div>
        {!connected && <p>{connection === "connecting" ? "Reading job status and local collection summaries." : "The local download service supplies this computer’s library and jobs. Connect here to inspect them."}</p>}
        <button type="button" disabled={connection === "connecting"} aria-busy={connection === "connecting"} onClick={downloads.connect}>{connection === "connecting" ? "Connecting…" : connected ? "Reconnect" : "Connect local downloads"}</button>
        {connection === "unavailable" && <p>Start the local service, then reconnect. <Link href="/earth-engine-downloads/setup">Connection help →</Link></p>}
      </section>
      <p className={styles.srOnly} role="status" aria-live="polite" aria-atomic="true">{downloads.announcement}</p>
      <dl className={styles.summary} aria-label="Library and activity summary">
        <div><dt>Stored on this computer</dt><dd>{snapshot ? bytes(snapshot.totalBytes) : "Unknown"}</dd><small>{snapshot ? `${snapshot.totalFiles.toLocaleString()} files · ${snapshot.entries.length} collections` : scanning ? "First scan in progress" : "A completed local scan is required"}{snapshot && (scanning || stale) ? " · previous scan" : ""}</small></div>
        <div><dt>Earth Engine downloads</dt><dd>{status ? jobs.filter(job => ["queued", "preparing", "downloading"].includes(job.state)).length : "Unknown"}</dd><small>{status ? `${jobs.filter(job => job.state === "downloaded").length} downloaded candidates${!connected ? " · last known" : ""}` : "Connect to read the worker"}</small></div>
        <div><dt>Approved map periods</dt><dd>{reviewed.loading ? "Checking…" : reviewed.error ? "Unavailable" : approved.length}</dd><small>Reviewed periods available for display</small></div>
      </dl>
      <div className={styles.layout}>
        <section className={styles.library} aria-labelledby="library-heading">
          <header className={styles.sectionHeading}><div><p className={styles.eyebrow}>LOCAL COLLECTIONS</p><h2 id="library-heading">Stored library</h2></div><button type="button" disabled={!connected || scanning || downloads.refreshingLibrary} aria-busy={scanning || downloads.refreshingLibrary} onClick={() => void downloads.refreshLibrary()}>{scanning ? "Scan in progress…" : downloads.refreshingLibrary ? "Starting scan…" : "Refresh library"}</button></header>
          <p className={styles.muted}>Private source collections and working files. Storage does not establish reviewed coverage or make a layer available on the map.</p>
          {scanning && <div className={styles.scan}><div><strong>Scanning in the background</strong><span>{library.scannedFiles.toLocaleString()} files inspected</span></div><progress aria-label="Library scan in progress; total file count unknown"/><p>{snapshot ? `Showing the previous completed scan from ${when(snapshot.generatedAt!)}.` : "Collection totals will appear when the first scan finishes."} You can keep using KFM.</p></div>}
          {downloads.libraryError && <p className={styles.alert}>{downloads.libraryError}</p>}
          {library?.state === "failed" && <p className={styles.alert}>This scan could not finish{library.error === "LIBRARY_SCAN_LIMIT" ? " within the scan limit" : library.error === "LIBRARY_SCAN_CHANGED" ? " because stored files changed during inspection" : ""}. {snapshot ? "The previous completed snapshot remains below." : "Current collection totals are unknown."} Refresh to try again.</p>}
          {snapshot && <p className={styles.snapshot}>{scanning || stale ? "Previous completed scan" : "Completed scan"} · <time dateTime={snapshot.generatedAt!}>{when(snapshot.generatedAt!)}</time> · byte counts include this scan’s listed files.</p>}
          <div className={styles.filters}><label>Find a collection<input type="search" placeholder="Source or collection name" value={query} onChange={event => { setQuery(event.target.value); setPage(0); }}/></label><label>Collection role<select value={role} onChange={event => { setRole(event.target.value); setPage(0); }}><option value="all">All roles</option>{Object.entries(libraryRoleLabels).map(([value, label]) => <option key={value} value={value}>{label}</option>)}</select></label></div>
          {snapshot ? <>
            <div className={styles.listHeading}><span>{collections.length} matching collections</span><span>Files / storage</span></div>
            <ul className={styles.collections}>{shownCollections.map(entry => <li key={entry.id}><div><strong>{entry.label}</strong><small>{libraryRoleLabels[entry.role]} · {entry.lane}</small></div><div><strong>{bytes(entry.bytes)}</strong><small>{entry.files.toLocaleString()} files</small></div></li>)}</ul>
            {!collections.length && <p className={styles.empty}>{snapshot.entries.length ? "No collections match these filters. Try a different source name or role." : "The completed scan found no eligible collection files."}</p>}
            <nav className={styles.pagination} aria-label="Collection pages"><button type="button" disabled={currentPage === 0} onClick={() => setPage(currentPage - 1)}>Previous</button><span>Page {currentPage + 1} of {pages}</span><button type="button" disabled={currentPage + 1 >= pages} onClick={() => setPage(currentPage + 1)}>Next</button></nav>
          </> : <div className={styles.empty}><strong>{scanning ? "Measuring the local library" : "Your library has not been measured yet"}</strong><p>{connected ? "A completed scan will show source names, file counts and stored bytes here." : "Connect the local service to inspect stored collections. Imported acquisition receipts are separate snapshots."}</p></div>}
        </section>
        <aside className={styles.reviewed} aria-labelledby="reviewed-heading"><p className={styles.eyebrow}>DISPLAY AVAILABILITY</p><h2 id="reviewed-heading">Ready on the map</h2><p>Approved display periods are checked independently of local storage and download status.</p>
          {reviewed.loading ? <p>Checking installed display sets…</p> : reviewed.error ? <p className={styles.alert}>{reviewed.error}</p> : approved.length ? <ul>{approved.map(item => <li key={item.key}><strong>{item.title}</strong><span>{item.year ?? "Period not specified"}</span><small>{item.period}</small></li>)}</ul> : <p className={styles.empty}>No approved display periods are installed. Downloaded files remain candidates until reviewed.</p>}
          <button type="button" disabled={reviewed.loading} aria-busy={reviewed.loading} onClick={reviewed.reload}>Recheck map periods</button><Link href="/earth-engine-context/install">Open map installer →</Link>
        </aside>
      </div>
      <section className={styles.jobs} aria-labelledby="jobs-heading"><header className={styles.sectionHeading}><div><p className={styles.eyebrow}>BACKGROUND WORK</p><h2 id="jobs-heading">Earth Engine downloads</h2></div><Link href="/earth-engine">Choose another dataset →</Link></header><p className={styles.muted}>Earth Engine downloads continue when you change datasets or leave this page. Other collection acquisition tasks are not shown in this job list; library totals cover raw, work, quarantine, and processed collections.</p>
        {status && !connected && <p className={styles.alert}>These are last known jobs. Their current state is unavailable until the service reconnects.</p>}
        {downloads.actionNotice && <p className={styles.alert}>{downloads.actionNotice}</p>}
        {jobs.length ? <><div className={styles.jobList}>{jobs.slice(currentJobPage * jobsPerPage, (currentJobPage + 1) * jobsPerPage).map(job => <DownloadJob key={job.id} job={job} active={job.id === status?.active} connected={connected} cancelling={downloads.cancelling} onCancel={() => void downloads.cancelJob()} />)}</div>{jobPages > 1 && <nav className={styles.pagination} aria-label="Download pages"><button type="button" disabled={currentJobPage === 0} onClick={() => setJobPage(currentJobPage - 1)}>Previous downloads</button><span>Page {currentJobPage + 1} of {jobPages}</span><button type="button" disabled={currentJobPage + 1 >= jobPages} onClick={() => setJobPage(currentJobPage + 1)}>Next downloads</button></nav>}</>
          : <div className={styles.empty}><strong>{status ? "No Earth Engine downloads recorded yet" : "Earth Engine download status is unavailable"}</strong><p>{status ? "Choose a dataset and period, link your Earth Engine project, and select a size maximum to begin." : "Connect to this computer to read current and recent jobs."}</p><Link href={status ? "/earth-engine" : "/earth-engine-downloads/setup"}>{status ? "Browse available datasets →" : "Local connection help →"}</Link></div>}
      </section>
      <footer className={styles.footer}>Collection and download counts describe this computer. Source coverage, data review and map display remain separate. <Link href="/acquisition">Inspect acquisition receipts →</Link></footer>
    </div>
  </main>;
}
