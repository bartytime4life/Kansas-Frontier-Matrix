"use client";
import { useMemo, useState } from "react";
import { canDownloadPublicMap, type PublicMapAsset, type PublicMapRecord } from "./public-map-catalog";
import type { PublicMapDownloads } from "./use-public-map-downloads";
import { formatDownloadBytes as bytes } from "./local-download-client";
import s from "./downloads/workspace.module.css";
import p from "./public-map-browser.module.css";

export const STORM_EVENTS_SOURCE = "publisher-noaa-storm-events";
const KINDS = [["details", "Event details"], ["fatalities", "Fatalities"], ["locations", "Locations"]] as const;
type Kind = typeof KINDS[number][0];
const MAX_QUEUE = 300;

/** The verified files for the chosen kinds and years, oldest year first. */
export function stormEventsSelection(records: readonly PublicMapRecord[], kinds: readonly Kind[], from: number, to: number): PublicMapAsset[] {
  return records
    .filter(row => row.sourceId === STORM_EVENTS_SOURCE && row.mapYear !== null && row.mapYear >= from && row.mapYear <= to)
    .sort((a, b) => a.mapYear! - b.mapYear!)
    .flatMap(row => KINDS.flatMap(([kind]) => kinds.includes(kind) ? row.assets.filter(asset => canDownloadPublicMap(asset) && asset.id === `${row.id}-${kind}`) : []));
}

/** A per-file maximum in MiB; Storm Events sizes are not listed exactly, so it is always explicit. */
export function stormEventsLimit(input: string, ceiling: number): number | null {
  if (!/^\d+(?:\.\d{1,3})?$/.test(input)) return null;
  const value = Math.floor(Number(input) * 1_048_576);
  return Number.isSafeInteger(value) && value > 0 && value <= ceiling ? value : null;
}

export default function StormEventsQueue({ records, downloads, blocked, showNotice, onViewActivity }: { records: readonly PublicMapRecord[]; downloads: PublicMapDownloads; blocked: boolean; showNotice: boolean; onViewActivity?: () => void }) {
  const { status, connection, busy } = downloads, connected = connection === "connected";
  const years = useMemo(() => [...new Set(records.filter(row => row.sourceId === STORM_EVENTS_SOURCE).flatMap(row => row.mapYear === null ? [] : [row.mapYear]))].sort((a, b) => b - a), [records]);
  const latest = years[0] ?? 0;
  const [kinds, setKinds] = useState<Kind[]>(["details"]);
  const [from, setFrom] = useState(""), [to, setTo] = useState(""), [maximum, setMaximum] = useState("");
  const first = Number(from || Math.max(years.at(-1) ?? latest, latest - 9)), last = Number(to || latest);
  const selection = useMemo(() => stormEventsSelection(records, kinds, first, last), [records, kinds, first, last]);
  const limit = stormEventsLimit(maximum, status?.limitBytes ?? 0);
  const queued = status?.queued ?? 0, running = blocked || Boolean(status?.active);
  if (!years.length) return null;
  const toggle = (kind: Kind) => setKinds(current => current.includes(kind) ? current.filter(item => item !== kind) : [...current, kind]);
  return <details className={p.coverage}><summary>Download several Storm Events years<span>{queued ? `${queued} files waiting` : "One file at a time, in the background"}</span></summary>
    <div className={p.selection} aria-label="Storm Events queue">
      <fieldset><legend>Files for each year</legend>{KINDS.map(([kind, label]) => <label key={kind}><input type="checkbox" checked={kinds.includes(kind)} onChange={() => toggle(kind)} />{label}</label>)}</fieldset>
      <label>From year<select value={String(first)} onChange={e => setFrom(e.target.value)}>{[...years].reverse().map(year => <option key={year} value={year}>{year}</option>)}</select></label>
      <label>To year<select value={String(last)} onChange={e => setTo(e.target.value)}>{years.map(year => <option key={year} value={year}>{year}</option>)}</select></label>
      <label>Maximum per file (MiB)<input type="number" inputMode="decimal" min="0.001" step="0.001" value={maximum} onChange={e => setMaximum(e.target.value)} placeholder="Enter a maximum" /></label>
      <p className={p.impact}>{first > last ? "Choose a start year before the end year." : `${selection.length.toLocaleString()} files selected`}{limit !== null && selection.length > 0 && first <= last ? ` · up to ${bytes(limit * selection.length)} in total` : ""}. NCEI does not list exact sizes; each file stops at the maximum.</p>
      {selection.length > MAX_QUEUE && <p role="alert">Choose at most {MAX_QUEUE} files per queue.</p>}
      {maximum && limit === null && <p role="alert">Choose a positive maximum within {bytes(status?.limitBytes ?? 500_000_000_000)}.</p>}
      <button type="button" className={s.primaryButton} disabled={!connected || !!busy || running || limit === null || !selection.length || selection.length > MAX_QUEUE || first > last}
        aria-busy={busy === "download"} onClick={() => { if (limit !== null) void downloads.startQueue(selection, limit); }}>{busy === "download" ? "Queuing files…" : `Queue ${selection.length.toLocaleString()} files`}</button>
      {!connected && <small>Connect to the download service on this computer to queue files.</small>}
      {connected && running && !queued && <small>A transfer is already running. <button type="button" className={s.textButton} onClick={onViewActivity}>View activity</button></small>}
      {queued > 0 && <p>{queued.toLocaleString()} files are waiting after the current download. <button type="button" className={s.textButton} disabled={!!busy} onClick={() => void downloads.cancelQueue()}>Cancel queued files</button> <button type="button" className={s.textButton} onClick={onViewActivity}>View activity</button></p>}
      {showNotice && downloads.notice && <p className={s.alert} role="status">{downloads.notice}</p>}
      <small>Files download one after another and continue while this page is closed. Each is stored as a private, unreviewed candidate under its NCEI name.</small>
    </div>
  </details>;
}
