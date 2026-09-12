"use client";
import { useEffect, useRef, useState } from "react";
import { createPortal } from "react-dom";
import Link from "next/link";
import type { AtmospherePreset, TerrainPresentationState } from "./map-runtime";
import type { OfficialContextId } from "./live-context";
import { SOURCE_DOWNLOADS } from "./source-downloads";
import { QUALITY_LABELS, type RenderQuality } from "./map-performance";

export const DOWNLOAD_NOTICES = [
  { id: "usgs-3dep-hillshade", title: "LiDAR point clouds & detailed elevation", format: "LAZ / GeoTIFF", detail: "Download a work unit with its acquisition date and metadata. The 3D display uses a separate elevation mosaic.", href: "https://apps.nationalmap.gov/lidar-explorer/" },
  { id: "history", title: "Historical topographic maps", format: "GeoTIFF / GeoPDF", detail: "Choose an actual map edition for historical place and landscape context.", href: "https://ngmdb.usgs.gov/topoview/" },
  { id: "noaa-daily-weather", title: "Long NOAA weather records", format: "Station files / CSV", detail: "Older station archives and bulk daily records can be downloaded beyond the map’s bounded queries.", href: "https://www.ncei.noaa.gov/pub/data/ghcn/daily/" },
  { id: "nws-radar", title: "Original NOAA radar archives", format: "NEXRAD files", detail: "Original archived scans are separate from the map’s live loop and historical mosaic playback.", href: "https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar" },
  { id: "noaa-nwm-analysis", title: "National Water Model data files", format: "NetCDF", detail: "Download model products for analysis; the live map service supplies a visualization.", href: "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/" },
] as const;
export type SourceIssue = { id: OfficialContextId; title: string };
export function DataNotices({ issues = [], onRetry, onHide }: { issues?: SourceIssue[]; onRetry?: (id: OfficialContextId) => void; onHide?: (id: OfficialContextId) => void }) {
  const [open, setOpen] = useState(false); const root = useRef<HTMLDivElement>(null); const trigger = useRef<HTMLButtonElement>(null);
  useEffect(() => {
    if (!open) return;
    const outside = (event: PointerEvent) => { if (!root.current?.contains(event.target as Node)) setOpen(false); };
    const escape = (event: KeyboardEvent) => { if (event.key === "Escape") { event.stopPropagation(); setOpen(false); trigger.current?.focus(); } };
    document.addEventListener("pointerdown", outside); root.current?.addEventListener("keydown", escape);
    const node = root.current; return () => { document.removeEventListener("pointerdown", outside); node?.removeEventListener("keydown", escape); };
  }, [open]);
  return <div className="data-notices" ref={root}>
    <button className="data-notices-trigger" ref={trigger} type="button" aria-expanded={open} aria-controls="data-notices-panel" onClick={() => setOpen(!open)} data-attention={issues.length > 0}><span aria-hidden="true">↓</span><span>Data & downloads</span><b aria-label={`${issues.length} source issues; ${DOWNLOAD_NOTICES.length} download collections`}>{issues.length || DOWNLOAD_NOTICES.length}</b></button>
    <span className="sr-only" role="status">{issues.length > 0 ? `${issues.length} selected source${issues.length === 1 ? " needs" : "s need"} attention. Open Data and downloads for recovery options.` : ""}</span>
    {open && <aside id="data-notices-panel" className="data-notices-panel" aria-label="Data downloads and source notifications">
      <header><div><small>SOURCE NOTICES</small><h2>Data & downloads</h2></div><button type="button" onClick={() => { setOpen(false); trigger.current?.focus(); }} aria-label="Close data notifications">×</button></header>
      {issues.length > 0 && <section className="source-issue-list" aria-label="Sources needing attention">{issues.map(issue => <article key={issue.id}><strong>{issue.title}</strong><p>Some data or tiles could not load. Other layers remain available.</p><div>{onRetry && <button type="button" onClick={() => onRetry(issue.id)}>Retry layer</button>}{onHide && <button type="button" onClick={() => onHide(issue.id)}>Hide layer</button>}<a href={SOURCE_DOWNLOADS[issue.id].href} target="_blank" rel="noreferrer">Source data ↗</a></div></article>)}</section>}
      <p className="download-intro">Original files and older archives need a provider download. Some sources also offer live map services.</p>
      {DOWNLOAD_NOTICES.map(item => <article className="download-notice" key={item.id}><div><h3>{item.title}</h3><small>{item.format}</small></div><p>{item.detail}</p><div className="download-notice-actions"><a href={item.href} target="_blank" rel="noreferrer">Open downloads ↗</a><Link href={`/data?source=${item.id}`}>Propose an update</Link></div></article>)}
      <footer><Link href="/data">Upload data for KFM</Link><Link href="/stewards">Steward review</Link></footer>
    </aside>}
  </div>;
}

export function RenderQualityControl({ value, onChange }: { value: RenderQuality; onChange: (value: RenderQuality) => void }) {
  return <label className="render-quality-control"><span>Rendering</span><select aria-label="Map rendering quality" value={value} onChange={e => onChange(e.target.value as RenderQuality)}>{Object.entries(QUALITY_LABELS).map(([id, label]) => <option key={id} value={id}>{label}</option>)}</select></label>;
}

export function TerrainQuickControls({ active, state, exaggeration, lighting, azimuth, heightOverlay, onPreset, onExaggeration, onLighting, onAzimuth, onHeight, onRetry }: {
  active: boolean; state: TerrainPresentationState; exaggeration: number; lighting: AtmospherePreset; azimuth: number; heightOverlay: boolean;
  onPreset: (preset: "natural" | "topographic" | "buildings") => void; onExaggeration: (value: number) => void; onLighting: (value: AtmospherePreset) => void; onAzimuth: (value: number) => void; onHeight: () => void; onRetry: () => void;
}) {
  const [open, setOpen] = useState(false); const ref = useRef<HTMLDivElement>(null); const panel = useRef<HTMLElement>(null);
  useEffect(() => { if (open) panel.current?.querySelector<HTMLButtonElement>("button")?.focus(); }, [open]);
  useEffect(() => { if (!open) return; const close = (e: PointerEvent) => { if (!ref.current?.contains(e.target as Node) && !panel.current?.contains(e.target as Node)) setOpen(false); }; document.addEventListener("pointerdown", close); return () => document.removeEventListener("pointerdown", close); }, [open]);
  return <div className="terrain-quick-controls" ref={ref} onKeyDown={e => { if (e.key === "Escape") { e.stopPropagation(); setOpen(false); ref.current?.querySelector<HTMLButtonElement>("button")?.focus(); } }}>
    <button type="button" aria-expanded={open} aria-controls="terrain-quick-panel" onClick={() => setOpen(!open)}><b>3D settings</b><span aria-hidden="true">⌄</span></button>
    {open && createPortal(<aside id="terrain-quick-panel" ref={panel} className="terrain-quick-panel" role="dialog" aria-modal="false" aria-labelledby="terrain-quick-title"><header><h2 id="terrain-quick-title">Explore in 3D</h2><button type="button" onClick={() => { setOpen(false); ref.current?.querySelector<HTMLButtonElement>("button")?.focus(); }} aria-label="Close 3D settings">×</button></header>
      <div className="terrain-look-presets"><button type="button" onClick={() => onPreset("natural")}><strong>Natural terrain</strong><small>Imagery + physical relief</small></button><button type="button" onClick={() => onPreset("topographic")}><strong>Topographic relief</strong><small>USGS map + terrain</small></button><button type="button" onClick={() => onPreset("buildings")}><strong>3D buildings</strong><small>Mapped heights · zoom in</small></button></div>
      <p>{active ? state === "READY" ? "Display terrain ready" : state === "ERROR" ? "Elevation tiles need attention" : "Loading display terrain…" : "Choose a 3D view to start."}</p>
      {active && state === "ERROR" && <button type="button" onClick={onRetry}>Retry elevation tiles</button>}
      <label><span>Vertical scale <output>{exaggeration.toFixed(1)}×{exaggeration === 1 ? " · physical" : " · exaggerated"}</output></span><input aria-label="Quick terrain vertical scale" type="range" min="0.5" max="2" step="0.1" disabled={!active} value={exaggeration} onChange={e => onExaggeration(Number(e.target.value))} /></label>
      <label><span>Scene light</span><select aria-label="Quick terrain scene light" value={lighting} onChange={e => onLighting(e.target.value as AtmospherePreset)}><option value="clear">Daylight</option><option value="dusk">Dusk</option><option value="night">Low glare</option></select></label>
      <label><span>Light direction <output>{Math.round(azimuth)}°</output></span><input aria-label="Quick terrain light direction" type="range" min="0" max="360" step="5" value={azimuth} onChange={e => onAzimuth(Number(e.target.value))} /></label>
      <button type="button" aria-pressed={heightOverlay} disabled={!active || state === "ERROR"} onClick={onHeight}>{heightOverlay ? "Hide" : "Show"} elevation colors</button>
      <small className="terrain-look-note">Lighting is illustrative. Relief and imagery keep their own source dates; neither reconstructs the selected historical day.</small>
    </aside>, document.body)}
  </div>;
}
