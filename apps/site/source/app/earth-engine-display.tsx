"use client";

import { useEffect, useMemo, useState } from "react";
import Link from "next/link";
import type { ErrorEvent as MapLibreErrorEvent, Map as MapLibreMap } from "./maplibre-seam";
import cdlPalette from "../scripts/earth-engine/cdl_2024_palette.json";
import { EARTH_ENGINE_DATASETS, EARTH_ENGINE_DISPLAY_RAMPS, earthEngineLegendGradient, earthEngineUrl } from "./earth-engine-data";
import { EARTH_ENGINE_CONTEXT_LAYERS, EARTH_ENGINE_SOURCE_YEARS, earthEngineSetYear, type EarthEngineContextManifest, type EarthEngineContextLayerId } from "./earth-engine-context";
import type { EarthEngineDisplayState } from "./earth-engine-raster-fallback";
import styles from "./earth-engine-display.module.css";
import { balanceMapRasters, composeMapLayers, requestRasterOpacity } from "./map-layer-composition";
import { EarthEngineComparisonPanel } from "./earth-engine-comparison-panel";

const sourceId = (id: string) => `kfm-ee-context-source-${id}`;
const rasterId = (id: string) => `kfm-ee-context-layer-${id}`;
const installedFor = (manifests: EarthEngineContextManifest[], id: EarthEngineContextLayerId, year: number) =>
  manifests.find((manifest) => earthEngineSetYear(manifest) === year && manifest.layers.some((layer) => layer.id === id && layer.status === "approved"));
const isSourceYear = (id: EarthEngineContextLayerId, year: number | undefined): year is number => {
  const bounds = EARTH_ENGINE_SOURCE_YEARS[id];
  return year !== undefined && Number.isInteger(year) && Boolean(bounds && year >= bounds[0] && year <= bounds[1]);
};

export function EarthEngineDisplayControls({ map, mapYear, manifests, loading, error, onReload, onDisplayChange, rendererState }: {
  map: MapLibreMap | null; mapYear: number; manifests: EarthEngineContextManifest[];
  loading: boolean; error: string | null; onReload: () => void;
  onDisplayChange: (display: EarthEngineDisplayState) => void; rendererState: string;
}) {
  const [visible, setVisible] = useState<Partial<Record<EarthEngineContextLayerId, boolean>>>({});
  const [visibilityTouched, setVisibilityTouched] = useState(false);
  const [opacity, setOpacity] = useState<Partial<Record<EarthEngineContextLayerId, number>>>({});
  const [yearChoice, setYearChoice] = useState<Partial<Record<EarthEngineContextLayerId, number>>>({});
  const [tileFailures, setTileFailures] = useState<Record<string, boolean>>({});
  const retryTiles = (id?: EarthEngineContextLayerId) => {
    if (map?.isStyleLoaded()) for (const layer of EARTH_ENGINE_CONTEXT_LAYERS) {
      if (id && id !== layer.id) continue;
      if (map.getLayer(rasterId(layer.id))) map.removeLayer(rasterId(layer.id));
      if (map.getSource(sourceId(layer.id))) map.removeSource(sourceId(layer.id));
    }
    setTileFailures(current => id ? Object.fromEntries(Object.entries(current).filter(([key]) => !key.endsWith(`/${id}`))) : {});
  };
  const baseline = manifests.find((item) => earthEngineSetYear(item) === 2024);
  const selectedYears = useMemo(() => Object.fromEntries(EARTH_ENGINE_CONTEXT_LAYERS.filter((item) => item.id !== "ee-3dep").map((item) => {
    const bounds = EARTH_ENGINE_SOURCE_YEARS[item.id]!;
    const installed = manifests.filter((manifest) => manifest.layers.some((layer) => layer.id === item.id && layer.status === "approved"))
      .map(earthEngineSetYear).filter((year): year is number => year !== null && isSourceYear(item.id, year)).sort((a, b) => b - a);
    const choice = yearChoice[item.id];
    return [item.id, isSourceYear(item.id, choice) ? choice : installed[0] ?? Math.max(bounds[0], Math.min(bounds[1], 2024))];
  })) as Partial<Record<EarthEngineContextLayerId, number>>, [manifests, yearChoice]);
  const selectedVisible = useMemo(() => !visibilityTouched && rendererState === "unsupported"
    && baseline?.layers.some((layer) => layer.id === "ee-3dep" && layer.status === "approved")
    ? { ...visible, "ee-3dep": true } : visible, [baseline, rendererState, visibilityTouched, visible]);

  useEffect(() => { onDisplayChange({ visible: selectedVisible, opacity, years: selectedYears }); }, [onDisplayChange, opacity, selectedVisible, selectedYears]);

  useEffect(() => {
    if (!map) return;
    const remove = () => {
      for (const descriptor of EARTH_ENGINE_CONTEXT_LAYERS) {
        if (map.getLayer(rasterId(descriptor.id))) map.removeLayer(rasterId(descriptor.id));
        if (map.getSource(sourceId(descriptor.id))) map.removeSource(sourceId(descriptor.id));
      }
    };
    return remove;
  }, [map]);

  useEffect(() => {
    if (!map) return;
    const apply = () => {
      if (!map.isStyleLoaded()) return;
      for (const descriptor of EARTH_ENGINE_CONTEXT_LAYERS) {
        const id = descriptor.id;
        const manifest = installedFor(manifests, id, id === "ee-3dep" ? 2024 : selectedYears[id] ?? 2024);
        const layer = manifest?.layers.find((item) => item.id === id);
        const source = sourceId(id), raster = rasterId(id);
        const tileUrl = manifest ? `/api/earth-engine-context/${encodeURIComponent(manifest.setId)}/${id}/{z}/{x}/{y}.png` : "";
        const prior = map.getSource(source) as { tiles?: string[] } | undefined;
        if (prior && prior.tiles?.[0] !== tileUrl) {
          if (map.getLayer(raster)) map.removeLayer(raster);
          map.removeSource(source);
        }
        const allowed = Boolean(layer && selectedVisible[id] && !tileFailures[`${manifest!.setId}/${id}`]);
        if (layer && !map.getSource(source)) {
          const zooms = Object.keys(layer.tileIndexes).map(Number);
          map.addSource(source, { type: "raster", tiles: [tileUrl], tileSize: 256, minzoom: Math.min(...zooms), maxzoom: Math.max(...zooms), bounds: [-102.052, 36.993, -94.588, 40.004] });
        }
        if (layer && !map.getLayer(raster)) map.addLayer({ id: raster, source, type: "raster", layout: { visibility: allowed ? "visible" : "none" }, paint: { "raster-opacity": opacity[id] ?? 0.72, "raster-resampling": id === "ee-cdl" ? "nearest" : "linear", "raster-fade-duration": 0 } });
        if (map.getLayer(raster)) {
          map.setLayoutProperty(raster, "visibility", allowed ? "visible" : "none");
          requestRasterOpacity(map, raster, opacity[id] ?? 0.72);
        }
        if (!layer && map.getSource(source)) {
          if (map.getLayer(raster)) map.removeLayer(raster);
          map.removeSource(source);
        }
      }
      balanceMapRasters(map);
      composeMapLayers(map);
    };
    const onError = (event: MapLibreErrorEvent) => {
      const message = event.error?.message ?? "";
      for (const manifest of manifests) for (const descriptor of EARTH_ENGINE_CONTEXT_LAYERS) {
        if (message.includes(`/api/earth-engine-context/${manifest.setId}/${descriptor.id}/`)) {
          const key = `${manifest.setId}/${descriptor.id}`;
          setTileFailures((current) => current[key] ? current : { ...current, [key]: true });
        }
      }
    };
    map.on("style.load", apply);
    map.on("error", onError);
    apply();
    return () => { map.off("style.load", apply); map.off("error", onError); };
  }, [map, manifests, opacity, selectedVisible, selectedYears, tileFailures]);

  return <section id="earth-engine-context-controls" tabIndex={-1} className={styles.panel} aria-labelledby="ee-context-title">
    <header><div><span>INSTALLED MAP LAYERS</span><h2 id="ee-context-title">Earth Engine</h2></div><button type="button" onClick={() => { retryTiles(); onReload(); }}>Refresh</button></header>
    <p role="status">{loading ? "Checking reviewed display sets…" : manifests.length ? `${manifests.length} approved year set${manifests.length === 1 ? "" : "s"} installed. Choose a year within each layer.` : error ?? "No reviewed display set is activated yet."}</p>
    {!loading && !manifests.length && <p><Link href="/earth-engine">Prepare Kansas Earth Engine imagery ↗</Link> · <Link href="/earth-engine-context/install">Install a reviewed display set ↗</Link></p>}
    {rendererState === "unsupported" && <p role="status">WebGL2 is unavailable here. Selected snapshots open in the 2D image viewer.</p>}
    <details className={styles.boundary}><summary>Display context only</summary><p>Pixel colors are map context, not a KFM evidence claim. A source year is not an installed map year. Each layer uses its own selected year, which may differ from map time {mapYear > 0 ? mapYear : "range"}.</p></details>
    <EarthEngineComparisonPanel manifests={manifests} loading={loading} error={error} />
    <div className={styles.rows}>{EARTH_ENGINE_CONTEXT_LAYERS.map((descriptor) => {
      const bounds = EARTH_ENGINE_SOURCE_YEARS[descriptor.id];
      const selectedYear = descriptor.id === "ee-3dep" ? 2024 : selectedYears[descriptor.id] ?? 2024;
      const manifest = installedFor(manifests, descriptor.id, selectedYear);
      const layer = manifest?.layers.find((item) => item.id === descriptor.id);
      const installed = Boolean(layer);
      const failed = Boolean(manifest && tileFailures[`${manifest.setId}/${descriptor.id}`]);
      const selected = Boolean(selectedVisible[descriptor.id]);
      const mapUnavailable = rendererState === "error";
      const years = bounds ? Array.from({ length: bounds[1] - bounds[0] + 1 }, (_, index) => bounds[1] - index) : [];
      const installedYears = manifests.filter((item) => item.layers.some((entry) => entry.id === descriptor.id && entry.status === "approved"))
        .map(earthEngineSetYear).filter((value): value is number => value !== null);
      return <article key={descriptor.id} data-status={!installed || failed || mapUnavailable ? "held" : selected ? "visible" : "ready"}>
        <div className={styles.rowHead}><label><input type="checkbox" checked={selected} disabled={!installed || failed} onChange={(event) => {
          setVisibilityTouched(true);
          setVisible((current) => ({ ...current, [descriptor.id]: event.target.checked }));
        }} /><strong>{descriptor.title}</strong></label><span>{!installed ? "YEAR NOT INSTALLED" : failed ? "TILE UNAVAILABLE" : selected ? mapUnavailable ? "SELECTED · MAP UNAVAILABLE" : rendererState === "unsupported" ? "SELECTED · 2D VIEWER" : "SELECTED" : "READY"}</span></div>
        {bounds ? <label className={styles.year}>Image year <select value={selectedYear} aria-label={`${descriptor.title} image year`} onChange={(event) => {
          const year = Number(event.target.value);
          if (isSourceYear(descriptor.id, year)) setYearChoice((current) => ({ ...current, [descriptor.id]: year }));
        }}>{years.map((year) => <option key={year} value={year}>{year}{installedYears.includes(year) ? " · installed" : " · prepare"}</option>)}</select></label> : <small>Mixed acquisition dates · no annual year selection</small>}
        <small>{layer?.period ?? (bounds ? `${selectedYear} source year · imagery not prepared` : descriptor.period)} · {layer ? `${layer.resolutionMeters.toLocaleString()} m ${descriptor.id === "ee-chirps" || descriptor.id === "ee-terraclimate" ? "native source grid" : "display grid"}` : "no reviewed pixels for this choice"}</small>
        {!installed && bounds && <small><Link href={`/earth-engine?dataset=${descriptor.id}&year=${selectedYear}`}>Prepare {selectedYear} {descriptor.title} ↗</Link> · Source coverage does not confirm usable Kansas pixels.</small>}
        {selected && layer && <><small>{layer.attribution}</small><div className={styles.legend}><i aria-hidden="true" data-layer={descriptor.id} style={EARTH_ENGINE_DISPLAY_RAMPS[descriptor.id] ? { background: earthEngineLegendGradient(EARTH_ENGINE_DISPLAY_RAMPS[descriptor.id]) } : undefined} /><span>{layer.legend}</span></div>
          <label className={styles.opacity}>Opacity <input aria-label={`${descriptor.title} opacity`} type="range" min="0" max="100" value={Math.round((opacity[descriptor.id] ?? 0.72) * 100)} onChange={(event) => setOpacity((current) => ({ ...current, [descriptor.id]: Number(event.target.value) / 100 }))} /><output>{Math.round((opacity[descriptor.id] ?? 0.72) * 100)}%</output></label>
          {descriptor.id === "ee-cdl" && selectedYear === 2024 && <details className={styles.cropKey}><summary>Crop class key · {Object.keys(cdlPalette.classes).length} classes</summary><ul>{Object.entries(cdlPalette.classes).map(([code, value]) => <li key={code}><i aria-hidden="true" style={{ backgroundColor: value.color }} /><span>{code} · {value.label}</span></li>)}</ul></details>}
          {descriptor.id === "ee-cdl" && selectedYear !== 2024 && <small>Historical class meanings require the selected year’s reviewed key.</small>}
        </>}
        {failed && manifest && <button type="button" onClick={() => retryTiles(descriptor.id)}>Retry tiles</button>}
        {layer?.limits && <details><summary>Source details & limits</summary><p>{layer.attribution}</p><p>{layer.legend}</p><p>{layer.limits}</p><a href={earthEngineUrl(EARTH_ENGINE_DATASETS.find((item) => item.id === descriptor.id)!)} target="_blank" rel="noreferrer">Official catalog and attribution ↗</a></details>}
      </article>;
    })}</div>
    <footer>Only activated snapshots render. Live Earth Engine browsing is not connected.</footer>
  </section>;
}
