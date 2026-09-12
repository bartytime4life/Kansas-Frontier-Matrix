import Link from "next/link";
import type { OfficialContextPayload, OfficialContextSource, OfficialContextState } from "./live-context";
import { SOURCE_DOWNLOADS } from "./source-downloads";

export function SourceQualityRow({ source, state, payload, error, selected, held, onToggle, onRetry }: { source: OfficialContextSource; state: OfficialContextState; payload?: OfficialContextPayload; error?: string; selected: boolean; held: boolean; onToggle: (selected: boolean) => void; onRetry?: () => void }) {
  const status = held ? "Held at this date" : !selected && state === "idle" ? "Off · not checked" : source.kind === "OPERATIONAL_WMS" && state === "ready" ? "Map service" : ({ idle: "Not checked", loading: "Loading", ready: "Loaded", empty: "No records", partial: "Partial", error: "Unavailable" })[state];
  const download = SOURCE_DOWNLOADS[source.id];
  return <article className="source-quality-row" data-state={state}>
    <div className="source-quality-heading"><label><input type="checkbox" checked={selected} onChange={(e) => onToggle(e.target.checked)} /><span>{source.shortTitle}</span></label><b>{status}</b></div>
    <p className="source-quality-clock">{payload ? `${payload.featureCount.toLocaleString()} records · retrieved ${new Date(payload.retrievedAt).toLocaleString()}` : source.cadence}</p>
    {payload?.upstreamUpdatedAt && <p className="source-quality-clock">Source time: {new Date(payload.upstreamUpdatedAt).toLocaleString()}</p>}
    {error && <p className="source-quality-error">{error}</p>}
    {state === "error" && onRetry && <button type="button" onClick={onRetry}>Retry layer</button>}
    <div className="source-quality-actions"><a href={download.href} target={download.href.startsWith("https:") ? "_blank" : undefined} rel="noreferrer">{download.label} ↗</a><Link href={`/data?source=${source.id}`}>Upload / propose update</Link></div>
    <details><summary>Source details & limitations</summary><p>{payload?.limitation || source.boundary}</p><p>{source.freshness}</p>{source.kind === "OPERATIONAL_WMS" && <p>Map service means the renderer has connected to the service. It does not verify every tile, acquisition date, or complete coverage.</p>}<a href={source.sourceUrl} target="_blank" rel="noreferrer">Provider & methodology ↗</a></details>
  </article>;
}
