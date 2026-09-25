"use client";

import { useEffect, useState } from "react";
import type { ErrorEvent as MapLibreErrorEvent, Map as MapLibreMap } from "maplibre-gl";
import cdlPalette from "../scripts/earth-engine/cdl_2024_palette.json";
import { EARTH_ENGINE_DATASETS, earthEngineUrl } from "./earth-engine-data";
import { EARTH_ENGINE_CONTEXT_LAYERS, earthEngineTileVisibleAtYear, type EarthEngineContextManifest, type EarthEngineContextLayerId } from "./earth-engine-context";
import styles from "./earth-engine-display.module.css";

const sourceId = (id: string) => `kfm-ee-context-source-${id}`;
const rasterId = (id: string) => `kfm-ee-context-layer-${id}`;

export function EarthEngineDisplayControls({ map, mapYear, manifest, loading, error, onReload }: {
  map: MapLibreMap | null; mapYear: number; manifest: EarthEngineContextManifest | null;
  loading: boolean; error: string | null; onReload: () => void;
}) {
  const [visible, setVisible] = useState<Partial<Record<EarthEngineContextLayerId, boolean>>>({});
  const [opacity, setOpacity] = useState<Partial<Record<EarthEngineContextLayerId, number>>>({});
  const [tileFailures, setTileFailures] = useState<Partial<Record<EarthEngineContextLayerId, boolean>>>({});

  useEffect(() => () => {
    if (!map) return;
    for (const descriptor of EARTH_ENGINE_CONTEXT_LAYERS) {
      if (map.getLayer(rasterId(descriptor.id))) map.removeLayer(rasterId(descriptor.id));
      if (map.getSource(sourceId(descriptor.id))) map.removeSource(sourceId(descriptor.id));
    }
  }, [map, manifest?.setId]);

  useEffect(() => {
    if (!map || !manifest) return;
    const apply = () => {
      if (!map.isStyleLoaded()) return;
      for (const descriptor of EARTH_ENGINE_CONTEXT_LAYERS) {
        const layer = manifest.layers.find((item) => item.id === descriptor.id);
        const id = descriptor.id;
        const allowed = Boolean(layer && layer.status === "approved" && visible[id] && earthEngineTileVisibleAtYear(id, mapYear) && !tileFailures[id]);
        const source = sourceId(id), raster = rasterId(id);
        if (layer?.status === "approved" && !map.getSource(source)) {
          const zooms = Object.keys(layer.tileIndexes).map(Number);
          map.addSource(source, { type: "raster", tiles: [`/api/earth-engine-context/${encodeURIComponent(manifest.setId)}/${id}/{z}/{x}/{y}.png`], tileSize: 256, minzoom: Math.min(...zooms), maxzoom: Math.max(...zooms), bounds: [-102.052, 36.993, -94.588, 40.004] });
        }
        if (layer?.status === "approved" && !map.getLayer(raster)) {
          map.addLayer({ id: raster, source, type: "raster", layout: { visibility: allowed ? "visible" : "none" }, paint: { "raster-opacity": opacity[id] ?? 0.72 } });
        }
        if (map.getLayer(raster)) {
          map.setLayoutProperty(raster, "visibility", allowed ? "visible" : "none");
          map.setPaintProperty(raster, "raster-opacity", opacity[id] ?? 0.72);
        }
      }
    };
    const onError = (event: MapLibreErrorEvent) => {
      const message = event.error?.message ?? "";
      const descriptor = EARTH_ENGINE_CONTEXT_LAYERS.find((entry) => message.includes(`/api/earth-engine-context/${manifest.setId}/${entry.id}/`));
      if (descriptor) setTileFailures((current) => current[descriptor.id] ? current : { ...current, [descriptor.id]: true });
    };
    map.on("style.load", apply);
    map.on("error", onError);
    apply();
    return () => { map.off("style.load", apply); map.off("error", onError); };
  }, [map, mapYear, manifest, opacity, tileFailures, visible]);

  return <section id="earth-engine-context-controls" className={styles.panel} aria-labelledby="ee-context-title">
    <header><div><span>OWNER-ONLY DISPLAY CONTEXT</span><h2 id="ee-context-title">Earth Engine snapshots</h2></div><button type="button" onClick={onReload}>Check set</button></header>
    <p>{loading ? "Checking the owner-only display set…" : manifest ? "Processed snapshots available. Live Earth Engine remains disconnected." : error ?? "No reviewed display set is installed yet."}</p>
    <p className={styles.boundary}>Pixel colors are map context, not a KFM evidence claim. Only approved layers can be switched on.</p>
    <div className={styles.rows}>{EARTH_ENGINE_CONTEXT_LAYERS.map((descriptor) => {
      const layer = manifest?.layers.find((item) => item.id === descriptor.id);
      const approved = layer?.status === "approved";
      const timeHeld = approved && !earthEngineTileVisibleAtYear(descriptor.id, mapYear);
      const failed = Boolean(tileFailures[descriptor.id]);
      const unavailable = !approved || timeHeld || failed;
      return <article key={descriptor.id} data-status={unavailable ? "held" : visible[descriptor.id] ? "visible" : "ready"}>
        <div className={styles.rowHead}><label><input type="checkbox" checked={Boolean(visible[descriptor.id])} disabled={unavailable} onChange={(event) => setVisible((current) => ({ ...current, [descriptor.id]: event.target.checked }))} /><strong>{descriptor.title}</strong></label><span>{!approved ? "UNAVAILABLE" : timeHeld ? "2024 ONLY" : failed ? "TILE UNAVAILABLE" : visible[descriptor.id] ? "ON" : "READY"}</span></div>
        <small>{layer?.period ?? descriptor.period} · {layer ? `${layer.resolutionMeters.toLocaleString()} m ${descriptor.id === "ee-chirps" || descriptor.id === "ee-terraclimate" ? "native source grid" : "display grid"}` : "awaiting reviewed export"}</small>
        <small>{layer?.attribution ?? descriptor.attribution}</small>
        <div className={styles.legend}><i aria-hidden="true" data-layer={descriptor.id} /><span>{layer?.legend ?? descriptor.legend}</span></div>
        {approved && descriptor.id === "ee-cdl" && <details className={styles.cropKey}><summary>Crop class key · {Object.keys(cdlPalette.classes).length} classes</summary><ul>{Object.entries(cdlPalette.classes).map(([code, value]) => <li key={code}><i aria-hidden="true" style={{ backgroundColor: value.color }} /><span>{code} · {value.label}</span></li>)}</ul></details>}
        {approved && <label className={styles.opacity}>Opacity <input aria-label={`${descriptor.title} opacity`} type="range" min="0" max="100" value={Math.round((opacity[descriptor.id] ?? 0.72) * 100)} onChange={(event) => setOpacity((current) => ({ ...current, [descriptor.id]: Number(event.target.value) / 100 }))} /><output>{Math.round((opacity[descriptor.id] ?? 0.72) * 100)}%</output></label>}
        {timeHeld && <small>Choose the 2024 map year to display this annual product.</small>}
        {failed && <button type="button" onClick={() => setTileFailures((current) => ({ ...current, [descriptor.id]: false }))}>Retry tiles</button>}
        {layer?.limits && <details><summary>Source limits</summary><p>{layer.limits}</p><a href={earthEngineUrl(EARTH_ENGINE_DATASETS.find((item) => item.id === descriptor.id)!)} target="_blank" rel="noreferrer">Official catalog and attribution ↗</a></details>}
      </article>;
    })}</div>
    <footer>Map in 2D and Globe · no Earth Engine credentials in this browser</footer>
  </section>;
}
