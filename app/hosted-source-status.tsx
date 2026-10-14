"use client";
import { useCallback, useEffect, useState } from "react";
import Link from "next/link";
type CaptureStatus = { state: string; configured: boolean; limitBytes: number; usedBytes: number | null; captures: number | null; lastTick: number | null; sources: { id: string; name: string; intervalMs: number; state: string; checkedAt?: number | null }[] };
const STATUS_LABELS: Record<string, string> = { "storage-not-configured": "Archive setup pending", "configuration-required": "Archive setup pending", "storage-unavailable": "Archive unavailable", paused: "Capture paused", "awaiting-scheduled-tick": "Waiting for scheduled capture" };
export function HostedSourceStatus() {
  const [status, setStatus] = useState<CaptureStatus | null>(null);
  const [failed, setFailed] = useState(false);
  const [loading, setLoading] = useState(true);
  const refresh = useCallback((signal?: AbortSignal) => fetch("/api/source-pipeline/status", { signal, cache: "no-store" })
    .then(response => { if (!response.ok) throw new Error(); return response.json(); })
    .then(value => { if (!signal?.aborted) setStatus(value); })
    .catch(() => { if (!signal?.aborted) setFailed(true); })
    .finally(() => { if (!signal?.aborted) setLoading(false); }), []);
  // Mounted only inside the source panel; no timer or map render-loop work.
  useEffect(() => { const controller = new AbortController(); void refresh(controller.signal); return () => controller.abort(); }, [refresh]);
  return <section className="hosted-source-status" aria-label="Hosted source archive">
    <header><strong>Hosted source archive</strong><span>{failed ? "Status unavailable" : status ? STATUS_LABELS[status.state] ?? "Capture status" : "Checking…"}</span></header>
    <p>Scheduled captures preserve original source data for review. Archived captures remain private and do not change the map’s live layers.</p>
    {status && <><dl><div><dt>Archive limit</dt><dd>80 GB</dd></div><div><dt>Stored</dt><dd>{status.usedBytes === null ? "Not verified" : `${(status.usedBytes / 1e9).toFixed(3)} GB`}</dd></div><div><dt>Captures</dt><dd>{status.captures ?? "Not verified"}</dd></div><div><dt>Last capture check</dt><dd>{status.lastTick ? new Date(status.lastTick).toISOString().replace("T", " ").slice(0, 19) + " UTC" : "Not yet recorded"}</dd></div></dl>
      <ul>{status.sources.map(source => <li key={source.id}><strong>{source.name}</strong><span>{source.state === "quarantined" ? "Captured · awaiting review" : source.state === "quarantined-invalid" ? "Captured · validation needs attention" : source.state === "retry-held" ? "Retry held" : "No verified capture"}</span></li>)}</ul></>}
    <div><button type="button" disabled={loading} onClick={() => { setLoading(true); setFailed(false); void refresh(); }}>{loading ? "Checking…" : "Refresh archive status"}</button><Link href="/connections">API connections and verified replay ↗</Link><Link href="/source-operations">Owner source operations ↗</Link></div>
    <p className="source-archive-limitation">Only the listed feeds have a capture adapter. Provider archives and map tiles keep their separate coverage.</p>
  </section>;
}
