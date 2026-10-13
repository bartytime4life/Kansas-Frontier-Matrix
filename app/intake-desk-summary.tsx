"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import { INTAKE_DESK_ORIGIN, intakeOverviewRequest, type IntakeOverview } from "./intake-desk-client";
import { automaticLocalConnection, formatDownloadBytes } from "./local-download-client";
import styles from "./intake-desk-summary.module.css";

type State = { phase: "idle" | "checking" | "connected" | "unavailable"; overview: IntakeOverview | null };

/** Read-only summary of the local intake desk; routing actions stay in the desk itself. */
export default function IntakeDeskSummary() {
  const [state, setState] = useState<State>({ phase: "idle", overview: null });
  const life = useRef<AbortController | null>(null);
  const check = useCallback(async () => {
    life.current?.abort();
    const controller = new AbortController();
    life.current = controller;
    setState(previous => ({ ...previous, phase: "checking" }));
    try {
      const overview = await intakeOverviewRequest(controller.signal);
      if (!controller.signal.aborted) setState(overview ? { phase: "connected", overview } : { phase: "unavailable", overview: null });
    } catch {
      if (!controller.signal.aborted) setState({ phase: "unavailable", overview: null });
    }
  }, []);
  useEffect(() => {
    if (automaticLocalConnection(window.location.origin)) queueMicrotask(() => { void check(); });
    return () => life.current?.abort();
  }, [check]);
  const o = state.overview;
  const used = o ? Math.min(100, ((o.budget.committed_bytes + o.budget.planned_bytes) / o.budget.github_limit_bytes) * 100) : 0;
  const reserve = o ? (o.budget.reserved_for_code_and_interface_bytes / o.budget.github_limit_bytes) * 100 : 0;
  return <section className={styles.panel} aria-labelledby="intake-desk-title">
    <div className={styles.head}>
      <div><p className={styles.eyebrow}>RAW DATA INTAKE</p><h2 id="intake-desk-title">Analyze and route stored files</h2></div>
      <a className={styles.open} href={`${INTAKE_DESK_ORIGIN}/`} target="_blank" rel="noopener noreferrer">Open Intake Desk →</a>
    </div>
    {o ? <>
      <dl className={styles.counts}>
        <div><dt>Indexed</dt><dd>{o.files.toLocaleString()}</dd><span>{formatDownloadBytes(o.bytes)}</span></div>
        <div><dt>Ready</dt><dd data-tone="ok">{o.ready.toLocaleString()}</dd></div>
        <div><dt>Needs review</dt><dd data-tone="warn">{o.review.toLocaleString()}</dd></div>
        <div><dt>Blocked</dt><dd data-tone="bad">{o.blocked.toLocaleString()}</dd></div>
      </dl>
      <div className={styles.budget}>
        <div className={styles.bar} role="img" aria-label={`GitHub storage ${formatDownloadBytes(o.budget.committed_bytes)} committed of ${formatDownloadBytes(o.budget.github_limit_bytes)}; ${formatDownloadBytes(o.budget.available_for_new_data_bytes)} free for data`}>
          <span style={{ width: `${used}%` }} data-part="used" /><span style={{ width: `${reserve}%` }} data-part="reserve" />
        </div>
        <p>GitHub: {formatDownloadBytes(o.budget.available_for_new_data_bytes)} free for curated data · {formatDownloadBytes(o.budget.reserved_for_code_and_interface_bytes)} kept for code and interface{o.budget.level !== "ok" ? ` · ${o.budget.level === "warn" ? "nearing the data ceiling" : "over the data ceiling"}` : ""}</p>
      </div>
      <p className={styles.note}>{o.running ? "An analysis is running on this computer." : o.lastRunFinishedAt ? `Last analysis ${new Date(o.lastRunFinishedAt).toLocaleString()}.` : "No analysis has finished yet."} Bulk files stay on this computer; release candidates are plans, not uploads.</p>
    </> : <p className={styles.note}>{state.phase === "checking" ? "Checking the intake desk on this computer…" : state.phase === "unavailable"
      ? "The intake desk is not running. Start it with python3 tools/local_data/intake_service.py from the KFM checkout."
      : "Profile raw files, see where each belongs — local store, database, Git or a GitHub release — and keep GitHub within its storage budget."}</p>}
    {state.phase !== "connected" && <button type="button" className={styles.check} disabled={state.phase === "checking"} onClick={() => void check()}>{state.phase === "checking" ? "Checking…" : "Check intake desk"}</button>}
  </section>;
}
