"use client";
import Link from "next/link";
import type { AtmospherePreset, TerrainPresentationState } from "./map-runtime";
import type { OfficialContextId } from "./live-context";
import { SOURCE_DOWNLOADS } from "./source-downloads";
import { QUALITY_LABELS, type RenderQuality } from "./map-performance";

export const DOWNLOAD_NOTICES = [
  { id: "usgs-3dep-hillshade", title: "LiDAR point clouds & detailed elevation", format: "LAZ / GeoTIFF", detail: "Download a work unit with its acquisition date and metadata. The 3D display uses a separate elevation mosaic.", href: "https://apps.nationalmap.gov/lidar-explorer/" },
  { id: "geologic-maps", title: "Kansas geologic maps · NGMDB", format: "Map catalog / available files", detail: "Open the supplied Kansas search. The provider may return multiple publishers; filter the provider catalog by publisher and inspect available files.", href: "https://ngmdb.usgs.gov/ngm-bin/ngm_search_dbi.pl?Title=&Author=&map_number=&State=KS&bc_ule=&bc_lre=&g_center=-97.35000%2C+37.82177&g_zoom=2.324&useextents=false&bc_ul=&bc_lr=&publisher_list=usgs&scale=&scale2=&datebgn=&dateend=&format=" },
  { id: "noaa-daily-weather", title: "Long NOAA weather records", format: "Station files / CSV", detail: "Older station archives and bulk daily records can be downloaded beyond the map’s bounded queries.", href: "https://www.ncei.noaa.gov/pub/data/ghcn/daily/" },
  { id: "nws-radar", title: "Original NOAA radar archives", format: "NEXRAD files", detail: "Original archived scans are separate from the map’s live loop and historical mosaic playback.", href: "https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar" },
  { id: "noaa-nwm-analysis", title: "National Water Model data files", format: "NetCDF", detail: "Download model products for analysis; the live map service supplies a visualization.", href: "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/" },
  { id: "noaa-storm-events", title: "Tornado, flood, snow & ice history", format: "Annual CSV.gz", detail: "Download NOAA Storm Events details, locations and fatalities. Event narratives and county records still need spatial review before map admission.", href: "https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/" },
  { id: "historical-networks", title: "Historical cities, roads & trade routes", format: "Map editions / shapefiles", detail: "Use dated USGS/Library of Congress map editions for historical interpretation; use TIGER/Line only as a labeled modern or vintage reference.", href: "https://ngmdb.usgs.gov/topoview/" },
] as const;
export type SourceIssue = { id: OfficialContextId; title: string; detail?: string; downloadHref?: string };
export function LayerSourceNotices({ issues = [], onRetry, onHide }: { issues?: SourceIssue[]; onRetry?: (id: OfficialContextId) => void; onHide?: (id: OfficialContextId) => void }) {
  return <section className="layer-source-notices" aria-label="Source recovery and original files">
    {issues.length > 0 && <section className="source-issue-list" aria-label="Sources needing attention">{issues.map(issue => <article key={issue.id}><strong>{issue.title}</strong><p>{issue.detail ?? "Some data or tiles could not load. Other layers remain available."}</p><div>{onRetry && <button type="button" onClick={() => onRetry(issue.id)}>Retry layer</button>}{onHide && <button type="button" onClick={() => onHide(issue.id)}>Hide layer</button>}<a href={issue.downloadHref ?? SOURCE_DOWNLOADS[issue.id].href} target="_blank" rel="noreferrer">Source data ↗</a></div></article>)}</section>}
    <details className="source-file-archives"><summary>Source files &amp; archives</summary>
      <p>Free provider files retain their own dates, formats and limitations. The map uses bounded hosted source requests.</p>
      {DOWNLOAD_NOTICES.map(item => <article className="download-notice" key={item.id}><div><h3>{item.title}</h3><small>{item.format}</small></div><p>{item.detail}</p><div className="download-notice-actions"><a href={item.href} target="_blank" rel="noreferrer">Open source files ↗</a></div></article>)}
      <Link href="/observatory/sources">Browse dated source coverage ↗</Link>
    </details>
  </section>;
}

export function RenderQualityControl({ value, onChange }: { value: RenderQuality; onChange: (value: RenderQuality) => void }) {
  return <label className="render-quality-control"><span>Rendering</span><select aria-label="Map rendering quality" value={value} onChange={e => onChange(e.target.value as RenderQuality)}>{Object.entries(QUALITY_LABELS).map(([id, label]) => <option key={id} value={id}>{label}</option>)}</select></label>;
}

export function LayerSceneControls({ active, state, selectedLook, terrainProvider, exaggeration, lighting, azimuth, heightOverlay, onPreset, onTerrainProvider, on2D, onExaggeration, onLighting, onAzimuth, onHeight, onRetry }: {
  active: boolean; state: TerrainPresentationState; selectedLook: "natural" | "topographic" | "buildings" | null; terrainProvider: "mapzen" | "usgs-3dep"; exaggeration: number; lighting: AtmospherePreset; azimuth: number; heightOverlay: boolean;
  onPreset: (preset: "natural" | "topographic" | "buildings") => void; onTerrainProvider: (provider: "mapzen" | "usgs-3dep") => void; on2D: () => void; onExaggeration: (value: number) => void; onLighting: (value: AtmospherePreset) => void; onAzimuth: (value: number) => void; onHeight: () => void; onRetry: () => void;
}) {
  const demStatus = !active || state === "OFF" ? "Off" : state === "READY" ? "Ready" : state === "ERROR" ? "Unavailable" : "Loading";
  return <section className="layer-scene-controls" aria-label="3D map appearance" data-dem-state={demStatus.toLowerCase()}>
    <div className="layer-scene-presets" role="group" aria-label="3D view presets">
      <button type="button" aria-pressed={selectedLook === "natural"} onClick={() => onPreset("natural")}><strong>Natural terrain</strong><small>Imagery + relief</small></button>
      <button type="button" aria-pressed={selectedLook === "topographic"} onClick={() => onPreset("topographic")}><strong>Topographic relief</strong><small>Topo map + DEM shading</small></button>
      <button type="button" aria-pressed={selectedLook === "buildings"} onClick={() => onPreset("buildings")}><strong>3D buildings</strong><small>Mapped heights</small></button>
    </div>
    <div className="layer-scene-dem" role="status" aria-live="polite">
      <span className="layer-scene-dem-dot" aria-hidden="true" />
      <span>{terrainProvider === "usgs-3dep" ? "USGS 3DEP DEM" : "Display DEM"} <strong>{demStatus}</strong>{active && <small> · {exaggeration.toFixed(1)}× display</small>}</span>
    </div>
    {active && <div className="layer-scene-actions">{state === "ERROR" && <><button className="layer-scene-retry" type="button" onClick={onRetry}>Retry elevation tiles</button>{terrainProvider === "usgs-3dep" && <button className="layer-scene-retry" type="button" onClick={() => onTerrainProvider("mapzen")}>Use fast display terrain</button>}</>}<button className="layer-scene-2d" type="button" onClick={on2D}>Return to 2D</button></div>}
    <small className="layer-scene-source-note">{terrainProvider === "usgs-3dep" ? "USGS 3DEP uses a mixed-resolution bare-earth DEM mosaic. LiDAR-derived areas vary; exact work-unit accuracy is not established here." : "3DEP hillshade is a separate official layer. Its source date may differ from this Mapzen display DEM."}</small>
    <details className="layer-scene-details">
      <summary>Fine tune 3D <span aria-hidden="true">⌄</span></summary>
      <div className="layer-scene-settings">
        <label htmlFor="layer-scene-source"><span>Terrain elevation source</span><select id="layer-scene-source" disabled={!active} value={terrainProvider} onChange={e => onTerrainProvider(e.target.value as "mapzen" | "usgs-3dep")}><option value="mapzen">Fast global DEM · Mapzen</option><option value="usgs-3dep">USGS 3DEP · Kansas detail</option></select></label>
        <label htmlFor="layer-scene-scale"><span>Vertical scale <output>{exaggeration.toFixed(1)}×{exaggeration === 1 ? " · physical" : " · exaggerated"}</output></span><input id="layer-scene-scale" type="range" min="0.1" max="3" step="0.1" disabled={!active || state === "ERROR"} value={exaggeration} onChange={e => onExaggeration(Number(e.target.value))} /></label>
        <label htmlFor="layer-scene-light"><span>Scene light</span><select id="layer-scene-light" disabled={!active} value={lighting} onChange={e => onLighting(e.target.value as AtmospherePreset)}><option value="clear">Daylight</option><option value="dusk">Dusk</option><option value="night">Low glare</option></select></label>
        <label htmlFor="layer-scene-direction"><span>Light direction <output>{Math.round(azimuth)}°</output></span><input id="layer-scene-direction" type="range" min="0" max="360" step="5" disabled={!active} value={azimuth} onChange={e => onAzimuth(Number(e.target.value))} /></label>
        <button type="button" className="layer-scene-height" aria-pressed={heightOverlay} disabled={!active || state === "ERROR"} onClick={onHeight}>{heightOverlay ? "Hide" : "Show"} elevation colors</button>
        <p>Lighting and elevation colors are illustrative. Imagery and relief keep their own source dates; neither reconstructs the selected historical day.</p>
      </div>
    </details>
  </section>;
}
