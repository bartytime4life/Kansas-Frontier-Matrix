"use client";

import { useEffect, useMemo, useState } from "react";
import type { ErrorEvent as MapLibreErrorEvent, Map as MapLibreMap } from "./maplibre-seam";
import cdlPalette from "../scripts/earth-engine/cdl_2024_palette.json";
import { EARTH_ENGINE_DATASETS, EARTH_ENGINE_DISPLAY_RAMPS, earthEngineLegendGradient, earthEngineUrl } from "./earth-engine-data";
import { EARTH_ENGINE_CONTEXT_LAYERS, earthEngineTileVisibleAtYear, type EarthEngineContextManifest, type EarthEngineContextLayerId } from "./earth-engine-context";
import type { EarthEngineDisplayState } from "./earth-engine-raster-fallback";
import styles from "./earth-engine-display.module.css";
import { balanceMapRasters, composeMapLayers, requestRasterOpacity } from "./map-layer-composition";

const sourceId = (id: string) => `kfm-ee-context-source-${id}`;
const rasterId = (id: string) => `kfm-ee-context-layer-${id}`;

export function EarthEngineDisplayControls({ map, mapYear, manifest, loading, error, onReload, onSelect2024, onDisplayChange, rendererState }: {
  map: MapLibreMap | null; mapYear: number; manifest: EarthEngineContextManifest | null;
  loading: boolean; error: string | null; onReload: () => void; onSelect2024: () => void;
  onDisplayChange: (display: EarthEngineDisplayState) => void; rendererState: string;
}) {
  const [visible, setVisible] = useState<Partial<Record<EarthEngineContextLayerId, boolean>>>({});
  const [visibilityTouched, setVisibilityTouched] = useState(false);
  const [opacity, setOpacity] = useState<Partial<Record<EarthEngineContextLayerId, number>>>({});
  const [tileFailures, setTileFailures] = useState<Partial<Record<EarthEngineContextLayerId, boolean>>>({});
  const selectedVisible = useMemo(() => !visibilityTouched && rendererState === "unsupported"
    && manifest?.layers.some((layer) => layer.id === "ee-3dep" && layer.status === "approved")
    ? { ...visible, "ee-3dep": true } : visible, [manifest, rendererState, visibilityTouched, visible]);

  useEffect(() => { onDisplayChange({ visible: selectedVisible, opacity }); }, [onDisplayChange, opacity, selectedVisible]);

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
        const allowed = Boolean(layer && layer.status === "approved" && selectedVisible[id] && earthEngineTileVisibleAtYear(id, mapYear) && !tileFailures[id]);
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
          requestRasterOpacity(map, raster, opacity[id] ?? 0.72);
        }
      }
      balanceMapRasters(map);
      composeMapLayers(map);
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
  }, [map, mapYear, manifest, opacity, tileFailures, selectedVisible]);

  return <section id="earth-engine-context-controls" tabIndex={-1} className={styles.panel} aria-labelledby="ee-context-title">
    <header><div><span>INSTALLED MAP LAYERS</span><h2 id="ee-context-title">Earth Engine</h2></div><button type="button" onClick={onReload}>Refresh</button></header>
    <p>{loading ? "Checking the owner-only display set…" : manifest ? "Select a layer to display. Annual layers switch the map to 2024." : error ?? "No reviewed display set is installed yet."}</p>
    {rendererState === "unsupported" && <p role="status">WebGL2 is unavailable here. Selected snapshots open in the 2D image viewer.</p>}
    <details className={styles.boundary}><summary>Display context only</summary><p>Pixel colors are map context, not a KFM evidence claim. Only approved layers can be switched on.</p></details>
    <div className={styles.rows}>{EARTH_ENGINE_CONTEXT_LAYERS.map((descriptor) => {
      const layer = manifest?.layers.find((item) => item.id === descriptor.id);
      const approved = layer?.status === "approved";
      const timeHeld = approved && !earthEngineTileVisibleAtYear(descriptor.id, mapYear);
      const failed = Boolean(tileFailures[descriptor.id]);
      const unavailable = !approved || failed;
      const mapUnavailable = rendererState === "error";
      return <article key={descriptor.id} data-status={timeHeld || unavailable || mapUnavailable ? "held" : selectedVisible[descriptor.id] ? "visible" : "ready"}>
        <div className={styles.rowHead}><label><input type="checkbox" checked={Boolean(selectedVisible[descriptor.id])} disabled={unavailable} onChange={(event) => {
          if (event.target.checked && descriptor.id !== "ee-3dep" && mapYear !== 2024) onSelect2024();
          setVisibilityTouched(true);
          setVisible((current) => ({
            ...current,
            ...(event.target.checked && descriptor.id !== "ee-3dep" && current["ee-3dep"] ? { "ee-3dep": false } : {}),
            [descriptor.id]: event.target.checked,
          }));
        }} /><strong>{descriptor.title}</strong></label><span>{!approved ? "UNAVAILABLE" : failed ? "TILE UNAVAILABLE" : timeHeld ? "2024 ONLY" : selectedVisible[descriptor.id] ? mapUnavailable ? "SELECTED · MAP UNAVAILABLE" : rendererState === "unsupported" ? "SELECTED · 2D VIEWER" : "SELECTED" : "READY"}</span></div>
        <small>{layer?.period ?? descriptor.period} · {layer ? `${layer.resolutionMeters.toLocaleString()} m ${descriptor.id === "ee-chirps" || descriptor.id === "ee-terraclimate" ? "native source grid" : "display grid"}` : "awaiting reviewed export"}</small>
        {selectedVisible[descriptor.id] && <>
          <small>{layer?.attribution ?? descriptor.attribution}</small>
          <div className={styles.legend}><i aria-hidden="true" data-layer={descriptor.id} style={EARTH_ENGINE_DISPLAY_RAMPS[descriptor.id] ? { background: earthEngineLegendGradient(EARTH_ENGINE_DISPLAY_RAMPS[descriptor.id]) } : undefined} /><span>{layer?.legend ?? descriptor.legend}</span></div>
          {approved && <label className={styles.opacity}>Opacity <input aria-label={`${descriptor.title} opacity`} type="range" min="0" max="100" value={Math.round((opacity[descriptor.id] ?? 0.72) * 100)} onChange={(event) => setOpacity((current) => ({ ...current, [descriptor.id]: Number(event.target.value) / 100 }))} /><output>{Math.round((opacity[descriptor.id] ?? 0.72) * 100)}%</output></label>}
          {approved && descriptor.id === "ee-cdl" && <details className={styles.cropKey}><summary>Crop class key · {Object.keys(cdlPalette.classes).length} classes</summary><ul>{Object.entries(cdlPalette.classes).map(([code, value]) => <li key={code}><i aria-hidden="true" style={{ backgroundColor: value.color }} /><span>{code} · {value.label}</span></li>)}</ul></details>}
        </>}
        {timeHeld && selectedVisible[descriptor.id] && <button type="button" onClick={onSelect2024}>Show at 2024</button>}
        {failed && <button type="button" onClick={() => setTileFailures((current) => ({ ...current, [descriptor.id]: false }))}>Retry tiles</button>}
        {layer?.limits && <details><summary>Source details & limits</summary><p>{layer.attribution}</p><p>{layer.legend}</p><p>{layer.limits}</p><a href={earthEngineUrl(EARTH_ENGINE_DATASETS.find((item) => item.id === descriptor.id)!)} target="_blank" rel="noreferrer">Official catalog and attribution ↗</a></details>}
      </article>;
    })}</div>
    <footer>Installed snapshots work in 2D and Globe. Live Earth Engine browsing is not connected.</footer>
  </section>;
}
