"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import Link from 'next/link';
type CaptureStatus = { state: string; configured: boolean; limitBytes: number; usedBytes: number | null; captures: number | null; lastTick: number | null; sources: { id: string; name: string; intervalMs: number; state: string; checkedAt?: number | null }[] };
const STATUS_LABELS: Record<string, string> = { "storage-not-configured": "Archive setup pending", "configuration-required": "Archive setup pending", "storage-unavailable": "Archive unavailable", paused: "Capture paused", "awaiting-scheduled-tick": "Waiting for scheduled capture" };
const count = (value: unknown): value is number => typeof value === "number" && Number.isSafeInteger(value) && value >= 0;
const nullableCount = (value: unknown): value is number | null => value === null || count(value);
const timestamp = (value: unknown): value is number | null => value === null || count(value) && value <= 8_640_000_000_000_000;
const boundedText = (value: unknown, limit: number): value is string => typeof value === "string" && value.length > 0 && value.length <= limit && !/[\u0000-\u001f\u007f]/.test(value);
function parseCaptureStatus(value: unknown): CaptureStatus {
  if (!value || typeof value !== "object" || Array.isArray(value)) throw new Error("Invalid archive status");
  const record = value as Record<string, unknown>;
  if (record.format !== "kfm-hosted-source-status-v1" || record.releaseState !== "unreleased"
    || typeof record.state !== "string" || !Object.hasOwn(STATUS_LABELS, record.state) || typeof record.configured !== "boolean"
    || !count(record.limitBytes) || record.limitBytes === 0 || !nullableCount(record.usedBytes) || !nullableCount(record.captures)
    || !timestamp(record.lastTick) || !Array.isArray(record.sources) || record.sources.length > 32) throw new Error("Invalid archive status");
  const ids = new Set<string>();
  const sources = record.sources.map((source: unknown) => {
    if (!source || typeof source !== "object" || Array.isArray(source)) throw new Error("Invalid archive source");
    const row = source as Record<string, unknown>;
    if (!boundedText(row.id, 80) || !/^[a-z0-9][a-z0-9-]*$/.test(row.id) || ids.has(row.id)
      || !boundedText(row.name, 160) || !count(row.intervalMs) || row.intervalMs === 0 || !boundedText(row.state, 32)
      || row.checkedAt !== undefined && !timestamp(row.checkedAt)) throw new Error("Invalid archive source");
    ids.add(row.id);
    return { id: row.id, name: row.name, intervalMs: row.intervalMs, state: row.state, ...(row.checkedAt !== undefined ? { checkedAt: row.checkedAt as number | null } : {}) };
  });
  // Project only the bounded public status fields; capture bodies remain private.
  return { state: record.state, configured: record.configured, limitBytes: record.limitBytes, usedBytes: record.usedBytes, captures: record.captures, lastTick: record.lastTick, sources };
}
export function HostedSourceStatus() {
  const [status, setStatus] = useState<CaptureStatus | null>(null);
  const [failed, setFailed] = useState(false);
  const [loading, setLoading] = useState(true);
  const request = useRef<AbortController | null>(null);
  const refresh = useCallback(() => {
    request.current?.abort();
    const controller = new AbortController(); request.current = controller;
    const current = () => request.current === controller && !controller.signal.aborted;
    return fetch("/api/source-pipeline/status", { signal: controller.signal, cache: "no-store" })
      .then(response => { if (!response.ok) throw new Error("Archive status unavailable"); return response.json(); })
      .then(value => { const checked = parseCaptureStatus(value); if (current()) setStatus(checked); })
      .catch(() => { if (current()) setFailed(true); })
      .finally(() => { if (current()) { setLoading(false); request.current = null; } });
  }, []);
  // Mounted only inside the source panel; no timer or map render-loop work.
  useEffect(() => { void refresh(); return () => { request.current?.abort(); request.current = null; }; }, [refresh]);
  return <section className="hosted-source-status" aria-label="Hosted source archive" aria-busy={loading}>
    <header><strong>Hosted source archive</strong><span>{failed ? "Status unavailable" : loading ? "Checking…" : status ? STATUS_LABELS[status.state] : "Status unavailable"}</span></header>
    <p>Scheduled captures preserve original source data for review. Archived captures remain private and do not change the map’s live layers.</p>
    <p><Link href="/curated">Curated source snapshots, map and downloads</Link></p>
    {failed && <p role="status">Archive status could not be verified. {status ? "Showing the last verified response; refresh to check again." : "No archive totals or capture state are confirmed."}</p>}
    {status && <><dl><div><dt>Archive limit</dt><dd>{status.limitBytes / 1e9} GB</dd></div><div><dt>Stored</dt><dd>{status.usedBytes === null ? "Not verified" : `${(status.usedBytes / 1e9).toFixed(3)} GB`}</dd></div><div><dt>Captures</dt><dd>{status.captures ?? "Not verified"}</dd></div><div><dt>Last capture check</dt><dd>{status.lastTick !== null ? new Date(status.lastTick).toISOString().replace("T", " ").slice(0, 19) + " UTC" : "Not yet recorded"}</dd></div></dl>
      <ul>{status.sources.map(source => <li key={source.id}><strong>{source.name}</strong><span>{source.state === "quarantined" ? "Captured · awaiting review" : source.state === "quarantined-invalid" ? "Captured · validation needs attention" : source.state === "retry-held" ? "Retry held" : "No verified capture"}</span></li>)}</ul></>}
    <div><button type="button" disabled={loading} onClick={() => { setLoading(true); setFailed(false); void refresh(); }}>{loading ? "Checking…" : "Refresh archive status"}</button></div>
    <p className="source-archive-limitation">Only the listed feeds have a capture adapter. Provider archives and map tiles keep their separate coverage.</p>
  </section>;
}
