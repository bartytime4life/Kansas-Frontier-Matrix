import Link from "next/link";
import type { OfficialContextPayload, OfficialContextSource, OfficialContextState } from "./live-context";
import { TERRAIN_DISPLAY_MIN_ZOOM } from "./live-context";
import { terrainRasterNeedsCloserView } from "./terrain-raster-status";
import { SOURCE_DOWNLOADS, sourceDownloadHref } from "./source-downloads";

export function SourceQualityRow({ source, state, payload, error, selected, held, viewZoom, archiveDay, observedAt, checkedAt, onToggle, onRetry }: { source: OfficialContextSource; state: OfficialContextState; payload?: OfficialContextPayload; error?: string; selected: boolean; held: boolean; viewZoom: number; archiveDay?: string; observedAt?: string | null; checkedAt?: string | null; onToggle: (selected: boolean) => void; onRetry?: () => void }) {
  const terrainOverlay = source.id === "usgs-3dep-hillshade" || source.id === "usgs-3dep-slope";
  const zoomLimited = terrainOverlay && terrainRasterNeedsCloserView(selected, held, state, viewZoom);
  const status = !selected ? state === "idle" ? "Off · not checked" : "Off · not displayed" : held ? "Held at this date" : zoomLimited ? `Zoom to ${TERRAIN_DISPLAY_MIN_ZOOM}+ to view` : source.id === "noaa-lightning-density" ? ({ idle: "Not checked", loading: "Loading frame and visible area", ready: "Density in sampled view", empty: "No density in sampled view", partial: "Image or sample unconfirmed", error: "Unavailable" })[state] : state === "loading" && payload ? "Refreshing · prior snapshot" : terrainOverlay && state === "partial" ? "Partial tiles" : terrainOverlay && state === "ready" ? "Tiles loaded" : source.kind === "OPERATIONAL_WMS" && state === "ready" ? "Map service" : ({ idle: "Not checked", loading: "Loading", ready: "Loaded", empty: "No records", partial: "Partial", error: "Unavailable" })[state];
  const download = SOURCE_DOWNLOADS[source.id];
  return <article className="source-quality-row" data-state={state}>
    <div className="source-quality-heading"><label><input type="checkbox" checked={selected} onChange={(e) => onToggle(e.target.checked)} /><span>{source.shortTitle}</span></label><b>{status}</b></div>
    <p className="source-quality-clock">{payload ? `${payload.featureCount.toLocaleString()} records · retrieved ${new Date(payload.retrievedAt).toLocaleString()}` : terrainOverlay ? `Raster tile service · ${source.cadence} · no tile retrieval clock` : source.cadence}</p>
    {source.id === "noaa-lightning-density" && <p className="source-quality-clock">{observedAt ? `Selected NOAA frame ${observedAt} · 15-minute density product; interval boundaries unverified` : "No NOAA observation frame selected"}{checkedAt ? ` · frame list retrieved ${checkedAt}` : ""}</p>}
    {payload?.sourceDay && <p className="source-quality-clock">NASA image day: {payload.sourceDay} UTC{state === "partial" ? " · delayed or incomplete" : ""}</p>}
    {payload?.upstreamUpdatedAt && <p className="source-quality-clock">Source time: {new Date(payload.upstreamUpdatedAt).toLocaleString()}</p>}
    {selected && error && <p className="source-quality-error">{error}</p>}
    {selected && (state === "error" || state === "partial") && onRetry && <button type="button" onClick={onRetry}>Retry layer</button>}
    <div className="source-quality-actions"><a href={sourceDownloadHref(source.id, archiveDay)} target={download.href.startsWith("https:") ? "_blank" : undefined} rel="noreferrer">{download.label}{archiveDay ? ` · ${archiveDay} UTC` : ""} ↗</a><Link href={`/data?source=${source.id}`}>Upload / propose update</Link></div>
    <details><summary>Source details & limitations</summary><p>{payload?.limitation || source.boundary}</p><p>{source.freshness}</p>{terrainOverlay && <p>Terrain image tiles are requested only at zoom {TERRAIN_DISPLAY_MIN_ZOOM} or closer. A connected map source at a wider view does not mean terrain imagery is displayed.</p>}{source.kind === "OPERATIONAL_WMS" && <p>Map service means the renderer has connected to the service. It does not verify every tile, acquisition date, or complete coverage.</p>}<a href={source.sourceUrl} target="_blank" rel="noreferrer">Provider & methodology ↗</a></details>
  </article>;
}
