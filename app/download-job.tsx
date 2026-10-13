import { EARTH_ENGINE_DATASETS } from "./earth-engine-data";
import { downloadReasons, formatDownloadBytes as bytes, jobStateLabels, type DownloadJob as Job } from "./local-download-client";
import styles from "./downloads/workspace.module.css";

export function DownloadJob({ job, active, connected, cancelling, onCancel, compact = false }: { job: Job; active: boolean; connected: boolean; cancelling: boolean; onCancel: () => void; compact?: boolean }) {
  const running = ["queued", "preparing", "downloading"].includes(job.state);
  const source = EARTH_ENGINE_DATASETS.find(item => item.id === job.selection.dataset);
  return <article className={styles.job} data-state={job.state} data-compact={compact} aria-label={`${source?.title ?? job.selection.dataset}, ${job.selection.year ?? "fixed period"}`}>
    <div className={styles.jobHeading}><div><span className={styles.eyebrow}>{job.selection.year ?? "MIXED / FIXED PERIOD"} · EARTH ENGINE</span><h3>{source?.title ?? job.selection.dataset}</h3></div><span className={styles.jobState}>{jobStateLabels[job.state]}</span></div>
    <div className={styles.jobNumbers}><strong>{bytes(job.bytes)} <span>received</span></strong><span>{job.total > 0 ? `${job.completed.toLocaleString()} / ${job.total.toLocaleString()} files` : `${job.completed.toLocaleString()} files completed · total not known yet`}</span></div>
    {running && (job.total > 0 ? <progress max={job.total} value={job.completed} aria-label={`${source?.title ?? job.selection.dataset} files completed`} /> : <progress aria-label={`${source?.title ?? job.selection.dataset}: preparing, total file count unknown`} />)}
    <div className={styles.jobFoot}><span>Selected maximum <strong>{bytes(job.selection.maxBytes)}</strong><small>A transfer limit, not an estimate of final size.</small></span>{active && <button type="button" disabled={!connected || cancelling} aria-busy={cancelling} onClick={onCancel}>{cancelling ? "Requesting cancellation…" : "Cancel download"}</button>}</div>
    {job.reason && <p className={styles.jobReason}>{downloadReasons[job.reason] ?? "The worker could not finish this selection. Inspect its retained files before retrying."}</p>}
    {job.state === "downloaded" ? <p className={styles.jobNote}>Private candidate captured. Coverage and processing review are still required before map display. <a href="/earth-engine-context/install">Map installer →</a></p>
      : ["cancelled", "interrupted", "failed"].includes(job.state) && <p className={styles.jobNote}>Any captured files remain on this computer for inspection.</p>}
    {!compact && <details className={styles.jobDetails}><summary>Download details</summary><dl><div><dt>Created</dt><dd><time dateTime={job.createdAt}>{job.createdAt}</time></dd></div><div><dt>Destination</dt><dd><code>{job.destination}</code></dd></div><div><dt>Job</dt><dd><code>{job.id}</code></dd></div></dl></details>}
  </article>;
}
