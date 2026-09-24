"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import { EARTH_ENGINE_ACCESS, EARTH_ENGINE_DATASETS, buildEarthEngineRecipe, earthEngineUrl } from "./earth-engine-data";
import { GLOBE_VIEWPOINTS, type GlobeCameraReading, type GlobeViewpoint } from "./globe-context";
import styles from "./earth-engine-globe.module.css";

export function EarthEngineGlobe({ camera, moving, rendererState, basemap, mapYear, mapTime, onViewpoint, onClose }: {
  camera: GlobeCameraReading | null; moving: boolean; rendererState: string; basemap: string;
  mapYear: number; mapTime: string; onViewpoint: (viewpoint: GlobeViewpoint) => void; onClose: () => void;
}) {
  const [datasetId, setDatasetId] = useState("ee-sentinel2");
  const [yearText, setYearText] = useState("2025");
  const [message, setMessage] = useState("");
  const heading = useRef<HTMLHeadingElement>(null);
  useEffect(() => { heading.current?.focus(); }, []);
  const dataset = EARTH_ENGINE_DATASETS.find((item) => item.id === datasetId)!;
  const annual = dataset.temporalMode === "annual";
  const year = annual ? Number(yearText) : undefined;
  const canUseMapYear = annual && Number.isInteger(mapYear) && mapYear >= dataset.firstYear! && mapYear <= dataset.lastYear!;
  let recipe = "", error = "";
  try { recipe = buildEarthEngineRecipe(dataset.id, year); } catch (cause) { error = cause instanceof Error ? cause.message : "Check the recipe year."; }

  function choose(id: string) {
    const next = EARTH_ENGINE_DATASETS.find((item) => item.id === id)!;
    setDatasetId(id); setYearText(String(next.lastYear ?? 2025)); setMessage("");
  }
  async function copy() {
    try { await navigator.clipboard.writeText(recipe); setMessage("Recipe copied. Review and run it in your Earth Engine project."); }
    catch { setMessage("Clipboard unavailable. Use Download recipe instead."); }
  }
  function download() {
    const url = URL.createObjectURL(new Blob([recipe], { type: "text/javascript" }));
    const link = document.createElement("a"); link.href = url; link.download = `kfm-${dataset.id}-${year ?? "fixed-product"}.js`;
    document.body.append(link); link.click(); link.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
    setMessage("Recipe download prepared. No Earth Engine query has been run.");
  }

  return <aside id="earth-engine-globe-panel" className={styles.panel} aria-labelledby="earth-engine-globe-title" onKeyDown={(event) => { if (event.key === "Escape") { event.stopPropagation(); onClose(); } }}>
    <header><div><span className={styles.kicker}>GLOBE WORKSPACE</span><h2 ref={heading} tabIndex={-1} id="earth-engine-globe-title">Earth Engine</h2></div><button type="button" onClick={onClose} aria-label="Close Earth Engine globe panel">×</button></header>
    <div className={styles.viewpoints} aria-label="Globe viewpoints">{(Object.keys(GLOBE_VIEWPOINTS) as GlobeViewpoint[]).map((key) => <button type="button" key={key} onClick={() => onViewpoint(key)}>{GLOBE_VIEWPOINTS[key].label}</button>)}</div>
    <section className={styles.telemetry} aria-label="Map camera telemetry">
      <div className={styles.sectionTitle}><h3>Map camera</h3><span>{moving ? "Moving · last settled view" : "Last settled view"}</span></div>
      {camera ? <><dl><div><dt>Center · lon, lat</dt><dd>{camera.longitude.toFixed(3)}°, {camera.latitude.toFixed(3)}°</dd></div><div><dt>Zoom</dt><dd>{camera.zoom.toFixed(2)}</dd></div><div><dt>Bearing / pitch</dt><dd>{camera.bearing.toFixed(1)}° / {camera.pitch.toFixed(1)}°</dd></div><div><dt>Projection</dt><dd>{camera.projection === "globe" ? "Globe requested from renderer" : camera.projection === "mercator" ? "Mercator · globe not yet applied" : "Unverified"}</dd></div><div><dt>Style / visible tiles</dt><dd>{camera.styleLoaded ? "Style loaded" : "Style loading"} / {camera.tilesLoaded ? "loaded" : "pending"}</dd></div></dl><small>Sampled {camera.sampledAt.replace("T", " ").replace(/\.\d+Z$/, " UTC")}. Map readings, not satellite telemetry.</small></> : <p>Camera readings unavailable until the map can be sampled.</p>}
      <p className={styles.runtime}>Map: {rendererState}. Basemap: {basemap}. At close zooms the globe transitions toward a local map.</p>
    </section>
    <div className={styles.connection}><strong>Earth Engine not connected</strong><p>No Earth Engine imagery or sensor telemetry is displayed. The globe shows the attributed basemap and selected KFM context layers.</p></div>
    <label className={styles.field}>Dataset<select value={datasetId} onChange={(event) => choose(event.target.value)}>{EARTH_ENGINE_DATASETS.map((item) => <option key={item.id} value={item.id}>{item.title}</option>)}</select></label>
    <p>{dataset.use}</p><code className={styles.asset}>{dataset.asset}</code>
    <dl className={styles.metadata}><div><dt>Provider</dt><dd>{dataset.provider}</dd></div><div><dt>Pixel size</dt><dd>{dataset.resolution}</dd></div><div><dt>Source time</dt><dd>{dataset.coverage} · {dataset.cadence}</dd></div><div><dt>Map time</dt><dd>{mapTime}</dd></div><div><dt>Recipe area</dt><dd>Kansas · TIGER 2018 boundary. Changing the viewpoint does not change the analysis area.</dd></div></dl>
    {annual ? <div className={styles.year}><label className={styles.field}>Recipe year<input type="number" min={dataset.firstYear!} max={dataset.lastYear!} step={1} value={yearText} aria-invalid={Boolean(error)} aria-describedby="globe-recipe-error" onChange={(event) => { setYearText(event.target.value); setMessage(""); }} /></label><button type="button" disabled={!canUseMapYear} onClick={() => { setYearText(String(mapYear)); setMessage(""); }}>Use map year</button><p>{canUseMapYear ? year === mapYear ? "Same calendar year; the recipe summarizes the full year, not the selected map instant." : "The recipe year differs from the map year." : "The selected map time is outside this recipe’s supported complete years."}</p></div> : <p className={styles.connection}>Fixed product with its own time span. The map clock does not retime this dataset.</p>}
    <p id="globe-recipe-error" role="alert" className={styles.error}>{error}</p>
    <div className={styles.actions}><button type="button" className={styles.primary} disabled={Boolean(error)} onClick={download}>Download recipe</button><button type="button" disabled={Boolean(error)} onClick={() => void copy()}>Copy recipe</button></div>
    <p role="status" className={styles.message}>{message}</p>
    <details><summary>Source limits & reuse</summary><p>{dataset.limitation}</p><p>{dataset.terms}</p><a href={earthEngineUrl(dataset)} target="_blank" rel="noreferrer">Official dataset & citation ↗</a></details>
    <footer><Link href="/earth-engine">Full catalog & comparison ↗</Link><a href={EARTH_ENGINE_ACCESS} target="_blank" rel="noreferrer">Earth Engine access setup ↗</a></footer>
  </aside>;
}
