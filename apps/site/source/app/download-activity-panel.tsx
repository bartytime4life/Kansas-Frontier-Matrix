"use client";
import { useState } from "react";
import { EARTH_ENGINE_DATASETS } from "./earth-engine-data";
import { downloadReasons, formatDownloadBytes as bytes, jobStateLabels } from "./local-download-client";
import { publicMapJobLabels, publicMapReason } from "./public-map-client";
import type { ActivityItem } from "./download-activity";
import type { useLocalDownloads } from "./use-local-downloads";
import type { PublicMapDownloads } from "./use-public-map-downloads";
import s from "./downloads/workspace.module.css";

type Controls = { local: ReturnType<typeof useLocalDownloads>; maps: PublicMapDownloads };
const running = (item: ActivityItem) => ["queued", "preparing", "downloading"].includes(item.state);
const title = (item: ActivityItem) => item.kind === "earth-engine" ? `${EARTH_ENGINE_DATASETS.find(source => source.id === item.job.selection.dataset)?.title ?? item.job.selection.dataset} · ${item.job.selection.year ?? "fixed period"}` : item.title;
export function ActivityCard({ item, local, maps, compact = false }: Controls & { item: ActivityItem; compact?: boolean }) {
  const fresh = (item.kind === "earth-engine" ? local.connection : maps.connection) === "connected";
  const cancelling = item.kind === "earth-engine" ? local.cancelling : maps.busy === "cancel";
  const reason = item.job.reason ? item.kind === "earth-engine" ? downloadReasons[item.job.reason] ?? "The worker could not finish. Inspect retained files before retrying." : publicMapReason(item.job.reason) : null;
  const label = item.kind === "earth-engine" ? jobStateLabels[item.state] : publicMapJobLabels[item.job.state];
  const cancel = () => item.kind === "earth-engine" ? local.cancelJob() : maps.cancelJob(item.nativeId);
  return <article className={s.activityCard} data-state={item.state} data-compact={compact} aria-label={title(item)}>
    <div className={s.activityTitle}><div><span className={s.eyebrow}>{item.provider}</span><h3>{title(item)}</h3></div><span className={s.activityState}>{label}</span></div>
    {!fresh && <p className={s.stale}>Last known state · reconnect to verify</p>}
    <div className={s.transferNumbers}><strong>{bytes(item.bytes)}<small> received</small></strong><span>{item.progress.unit === "files" ? `${item.progress.value} / ${item.progress.total} files` : item.progress.unit === "bytes" ? `of ${bytes(item.progress.total!)}` : "Total not known yet"}</span></div>
    {running(item) && (item.progress.total !== null && item.progress.value !== null
      ? <progress value={item.progress.value} max={item.progress.total} aria-label={`${title(item)}: ${item.progress.unit === "files" ? "files completed" : "bytes received"}`} />
      : <progress aria-label={`${title(item)}: total unknown`} />)}
    <div className={s.transferFoot}><span>Maximum <strong>{bytes(item.maxBytes)}</strong></span>{item.active && <button type="button" disabled={!fresh || cancelling} aria-busy={cancelling} onClick={() => void cancel()}>{cancelling ? "Cancelling…" : "Cancel transfer"}</button>}</div>
    {reason && <p className={s.jobReason}>{reason}</p>}
    <p className={s.nextStep}>{item.state === "downloaded" ? "Saved candidate · review needed before map display." : ["cancelled", "failed", "interrupted"].includes(item.state) ? "Retained bytes remain available for inspection." : "You can browse while this continues in the background."}</p>
    {!compact && <details className={s.jobDetails}><summary>Transfer details</summary><dl><div><dt>Destination</dt><dd>{item.job.destination}</dd></div><div><dt>Selected maximum</dt><dd>{bytes(item.maxBytes)} · a stop limit, not a size estimate</dd></div><div><dt>Started</dt><dd><time dateTime={item.createdAt}>{new Date(item.createdAt).toLocaleString()}</time></dd></div><div><dt>Job ID</dt><dd>{item.nativeId}</dd></div>{item.kind === "public-map" && <><div><dt>Stored-file SHA-256</dt><dd>{item.job.sha256 ?? "Not available yet"}</dd></div><div><dt>Provider checksum verification</dt><dd>Not performed. The stored-file hash identifies retained bytes.</dd></div></>}</dl></details>}
  </article>;
}

export function TransferPanel({ items, local, maps, onViewActivity }: Controls & { items: ActivityItem[]; onViewActivity: () => void }) {
  const active = items.find(item => item.active), known = Boolean(local.status && maps.status), connected = local.connection === "connected" && maps.connection === "connected";
  const pending = local.starting || maps.busy === "download";
  const maintenance = local.library?.state === "scanning" || maps.status?.refresh.state === "running";
  return <aside className={s.transferPanel} data-transfer-panel data-active={Boolean(active || maintenance || pending)} data-pending={pending} aria-label="Background activity">
    <header className={s.transferPanelHeader}><span className={s.eyebrow}>ON THIS COMPUTER</span><button type="button" className={s.textButton} onClick={onViewActivity}>All activity <span aria-hidden="true">↗</span></button></header>
    {active ? <ActivityCard item={active} local={local} maps={maps} compact /> : <div className={s.transferIdle}><span className={s.activitySignal} data-connected={connected} aria-hidden="true"/><h3>{pending ? "Confirming transfer…" : maintenance ? "Updating in the background" : connected && known ? "Ready when you are" : "Activity not confirmed"}</h3><p>{pending ? "Checking the operator’s acknowledgement. A current job has not been confirmed yet." : connected && known ? "Choose a source and a size maximum. Your transfer will appear here." : "Connect this computer to check current transfers."}</p>{pending && <progress aria-label="Confirming transfer; progress not available yet" />}</div>}
    {local.library?.state === "scanning" && <div className={s.backgroundTask}><strong>Scanning local library</strong><span>{local.library.scannedFiles.toLocaleString()} files inspected</span><progress aria-label="Library scan; total unknown" /></div>}
    {maps.status?.refresh.state === "running" && <div className={s.backgroundTask}><strong>Refreshing Kansas records</strong><span>Retained catalog stays available</span><progress aria-label="Catalog refresh; total unknown" /></div>}
    <div className={s.panelFoot}><p>Progress updates automatically. Transfers keep running when you leave this page.</p>{items.length > 0 && <button type="button" className={s.textButton} onClick={onViewActivity}>{items.length} recent {items.length === 1 ? "transfer" : "transfers"} →</button>}</div>
  </aside>;
}

export function ActivityWorkspace({ items, local, maps }: Controls & { items: ActivityItem[] }) {
  const [filter, setFilter] = useState("all"), [page, setPage] = useState(0);
  const filtered = items.filter(item => filter === "all" || filter === "active" && running(item) || filter === "saved" && item.state === "downloaded" || filter === "stopped" && ["cancelled", "failed", "interrupted"].includes(item.state));
  const pages = Math.max(1, Math.ceil(filtered.length / 8)), currentPage = Math.min(page, pages - 1);
  return <section aria-labelledby="activity-heading"><header className={s.sectionHeading}><div><p className={s.eyebrow}>TRANSFERS &amp; HISTORY</p><h2 id="activity-heading">Activity</h2></div><label className={s.inlineFilter}>Show<select value={filter} onChange={event => { setFilter(event.target.value); setPage(0); }}><option value="all">All transfers</option><option value="active">Active</option><option value="saved">Saved candidates</option><option value="stopped">Stopped / needs attention</option></select></label></header>
    <p className={s.muted}>Public maps and Earth Engine in one place. File totals and byte totals follow their source.</p>
    {(local.connection !== "connected" || maps.connection !== "connected") && <p className={s.alert}>Some activity is unavailable or last known. Connect above to check both download channels.</p>}
    {local.actionNotice && <p className={s.alert} role="status">{local.actionNotice}</p>}{maps.notice && <p className={s.alert} role="status">{maps.notice}</p>}
    {filtered.length ? <><div className={s.activityList}>{filtered.slice(currentPage * 8, (currentPage + 1) * 8).map(item => <ActivityCard key={item.key} item={item} local={local} maps={maps} />)}</div><nav className={s.pagination} aria-label="Activity pages"><button type="button" disabled={currentPage === 0} onClick={() => setPage(currentPage - 1)}>Previous</button><span>Page {currentPage + 1} of {pages}</span><button type="button" disabled={currentPage + 1 >= pages} onClick={() => setPage(currentPage + 1)}>Next</button></nav></> : <div className={s.empty}><strong>{local.status && maps.status ? filter === "all" ? "No transfers recorded yet" : "No transfers in this view" : "Transfer history is not available yet"}</strong><p>{local.status && maps.status ? "Find data to choose your next source. Opening a source link does not create a local transfer." : "The local operator supplies current and recent jobs when connected."}</p></div>}
  </section>;
}
