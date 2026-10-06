"use client";

import { useEffect, useId, useMemo, useRef, useState } from "react";
import { createPortal } from "react-dom";
import { EARTH_ENGINE_CONTEXT_LAYERS, EARTH_ENGINE_SOURCE_YEARS, type EarthEngineContextLayerId, type EarthEngineContextManifest } from "./earth-engine-context";
import { EARTH_ENGINE_DISPLAY_RAMPS, earthEngineLegendGradient } from "./earth-engine-data";
import { comparisonCameraOptions, comparisonPair, comparisonTileUrl, comparisonYears, readComparisonTile, synchronizeComparisonMaps, type ComparisonPair } from "./earth-engine-comparison";
import { installMapProtocol, loadMapLibre, type Map as MapLibreMap } from "./maplibre-seam";
import styles from "./earth-engine-comparison.module.css";

type ReadyPair = Extract<ComparisonPair, { kind: "ready" }>;
type Mode = "swipe" | "side-by-side";
const kansas: [[number, number], [number, number]] = [[-102.052, 36.993], [-94.588, 40.004]];

function ComparisonMaps({ pair, mode, divider, onFallback }: { pair: ReadyPair; mode: Mode; divider: number; onFallback: () => void }) {
  const hostA = useRef<HTMLDivElement>(null), hostB = useRef<HTMLDivElement>(null);
  const maps = useRef<MapLibreMap[]>([]);
  const protocol = `kfm-history-${useId().replace(/[^a-z0-9]/gi, "").toLowerCase()}`;
  const [status, setStatus] = useState<[string, string]>(["Loading year A…", "Loading year B…"]);
  useEffect(() => {
    let disposed = false;
    let removeProtocol: (() => void) | undefined;
    let stopSync: (() => void) | undefined;
    const controller = new AbortController(), observer = new ResizeObserver(() => {
      for (const map of maps.current) { try { map.resize(); } catch { /* A removed map cannot resize. */ } }
    });
    const report = (side: number, message: string) => { if (!disposed) setStatus(current => side === 0 ? [message, current[1]] : [current[0], message]); };
    const states = [new Map<string, "loading" | "loaded" | "unavailable">(), new Map<string, "loading" | "loaded" | "unavailable">()];
    const progress = (side: number) => {
      const values = [...states[side].values()];
      const loaded = values.filter(value => value === "loaded").length, failed = values.filter(value => value === "unavailable").length, pending = values.filter(value => value === "loading").length;
      report(side, `${loaded} tiles received${pending ? ` · ${pending} loading` : ""}${failed ? ` · ${failed} unavailable; gaps remain blank` : ""}`);
    };
    loadMapLibre().then(lib => {
      if (disposed || !hostA.current || !hostB.current) return;
      if (!document.createElement("canvas").getContext("webgl2")) { onFallback(); return; }
      lib.setWorkerUrl("/maplibre/maplibre-gl-worker.mjs");
      installMapProtocol(lib, protocol, async (params, abort) => {
        const match = new RegExp(`^${protocol}://([ab])/(\\d+)/(\\d+)/(\\d+)$`).exec(params.url);
        if (!match) throw new Error("Invalid comparison tile request.");
        const side = match[1] === "a" ? 0 : 1, snapshot = side === 0 ? pair.a : pair.b;
        const url = comparisonTileUrl(snapshot, Number(match[2]), Number(match[3]), Number(match[4]));
        if (!url) throw new Error("No prepared tile at this location.");
        const signal = AbortSignal.any([controller.signal, abort.signal]);
        if (states[side].size > 512) states[side].clear();
        states[side].set(url, "loading"); progress(side);
        try {
          const data = await readComparisonTile(url, signal);
          signal.throwIfAborted();
          states[side].set(url, "loaded"); progress(side);
          return { data };
        } catch (error) {
          if (signal.aborted) states[side].delete(url); else states[side].set(url, "unavailable");
          progress(side); throw error;
        }
      });
      removeProtocol = () => lib.removeProtocol(protocol);
      for (const [side, host] of [hostA.current, hostB.current].entries()) {
        const snapshot = side === 0 ? pair.a : pair.b;
        const map = new lib.Map({ container: host, center: [-98.32, 38.5], ...comparisonCameraOptions(pair),
          maxPitch: 0, dragRotate: false, pitchWithRotate: false, touchPitch: false,
          renderWorldCopies: false, attributionControl: false, maxTileCacheSize: 32, pixelRatio: Math.min(2, window.devicePixelRatio || 1),
          style: { version: 8, projection: { type: "mercator" }, sources: {
            snapshot: { type: "raster", tiles: [`${protocol}://${side === 0 ? "a" : "b"}/{z}/{x}/{y}`], tileSize: 256, minzoom: pair.minZoom, maxzoom: pair.maxZoom, bounds: [...kansas[0], ...kansas[1]] },
          }, layers: [{ id: "snapshot", source: "snapshot", type: "raster", paint: { "raster-opacity": 1, "raster-fade-duration": 0, "raster-resampling": pair.id === "ee-cdl" ? "nearest" : "linear" } }] } });
        maps.current.push(map);
        map.touchZoomRotate.disableRotation();
        map.keyboard.disableRotation();
        map.getCanvas().setAttribute("aria-label", `Year ${snapshot.year} imagery map. Arrow keys pan; plus and minus zoom. Both maps move together.`);
        map.on("load", () => { if (!disposed) map.fitBounds(kansas, { padding: 20, duration: 0 }); });
        map.on("error", () => report(side, "Some requested tiles are unavailable. Blank areas are gaps, not measured change."));
        observer.observe(host);
      }
      stopSync = synchronizeComparisonMaps(maps.current);
    }).catch(() => { if (!disposed) { report(0, "WebGL comparison unavailable."); onFallback(); } });
    return () => {
      disposed = true; controller.abort(); observer.disconnect(); stopSync?.();
      for (const map of maps.current) { try { map.remove(); } catch { /* Preserve teardown of the other map. */ } }
      maps.current = []; removeProtocol?.();
    };
  }, [onFallback, pair, protocol]);
  const reset = () => maps.current[0]?.fitBounds(kansas, { padding: 20, duration: 0 });
  return <>
    <div className={styles.navigation}><button type="button" onClick={() => maps.current[0]?.zoomOut({ duration: 0 })}>Zoom out</button><button type="button" onClick={() => maps.current[0]?.zoomIn({ duration: 0 })}>Zoom in</button><button type="button" onClick={reset}>Fit Kansas</button><span>Drag or use arrow keys to pan both maps.</span></div>
    <div className={styles.stage} data-mode={mode}>
      <div ref={hostB} className={styles.mapB} />
      <div ref={hostA} className={styles.mapA} style={mode === "swipe" ? { clipPath: `inset(0 ${100 - divider}% 0 0)` } : undefined} />
      {mode === "swipe" && <div className={styles.divider} aria-hidden="true" style={{ left: `${divider}%` }} />}
    </div>
    <div className={styles.statuses} aria-live="polite"><span>A · {pair.a.year}: {status[0]}</span><span>B · {pair.b.year}: {status[1]}</span></div>
  </>;
}

function ComparisonImages({ pair, mode, divider }: { pair: ReadyPair; mode: Mode; divider: number }) {
  const [images, setImages] = useState<Record<string, string | null>>({});
  const [scale, setScale] = useState(1), [offset, setOffset] = useState({ x: 0, y: 0 });
  const z = pair.overviewZoom;
  const tiles = useMemo(() => z === null ? [] : [pair.a, pair.b].flatMap((snapshot, side) => {
    const index = snapshot.layer.tileIndexes[String(z)];
    const result: { url: string; x: number; y: number; side: number }[] = [];
    for (let y = index.minY; y <= index.maxY; y++) for (let x = index.minX; x <= index.maxX; x++) result.push({ url: comparisonTileUrl(snapshot, z, x, y)!, x, y, side });
    return result;
  }), [pair, z]);
  useEffect(() => {
    const controller = new AbortController(), objectUrls: string[] = [];
    let cursor = 0;
    const load = async () => {
      while (!controller.signal.aborted && cursor < tiles.length) {
        const tile = tiles[cursor++];
        try {
          const bytes = await readComparisonTile(tile.url, controller.signal);
          controller.signal.throwIfAborted();
          const url = URL.createObjectURL(new Blob([bytes], { type: "image/png" })); objectUrls.push(url);
          setImages(current => ({ ...current, [tile.url]: url }));
        } catch { if (!controller.signal.aborted) setImages(current => ({ ...current, [tile.url]: null })); }
      }
    };
    for (let i = 0; i < 4; i++) void load();
    return () => { controller.abort(); for (const url of objectUrls) URL.revokeObjectURL(url); };
  }, [tiles]);
  if (z === null || !tiles.length) return <p role="status">No bounded common overview is prepared for this pair. The dates and source details remain available.</p>;
  const minX = Math.min(...tiles.map(tile => tile.x)), maxX = Math.max(...tiles.map(tile => tile.x)), minY = Math.min(...tiles.map(tile => tile.y)), maxY = Math.max(...tiles.map(tile => tile.y));
  const width = maxX - minX + 1, height = maxY - minY + 1;
  const summary = (side: number) => {
    const selected = tiles.filter(tile => tile.side === side), loaded = selected.filter(tile => typeof images[tile.url] === "string").length, failed = selected.filter(tile => images[tile.url] === null).length;
    return `${loaded}/${selected.length} overview tiles received${failed ? ` · ${failed} unavailable` : ""}`;
  };
  return <>
    <div className={styles.navigation}><button type="button" disabled={scale <= 1} onClick={() => setScale(value => Math.max(1, value / 2))}>Zoom out</button><button type="button" disabled={scale >= 4} onClick={() => setScale(value => Math.min(4, value * 2))}>Zoom in</button><button type="button" aria-label="Pan both images left" onClick={() => setOffset(value => ({ ...value, x: value.x - 10 }))}>←</button><button type="button" aria-label="Pan both images right" onClick={() => setOffset(value => ({ ...value, x: value.x + 10 }))}>→</button><button type="button" aria-label="Pan both images up" onClick={() => setOffset(value => ({ ...value, y: value.y - 10 }))}>↑</button><button type="button" aria-label="Pan both images down" onClick={() => setOffset(value => ({ ...value, y: value.y + 10 }))}>↓</button><button type="button" onClick={() => { setScale(1); setOffset({ x: 0, y: 0 }); }}>Reset view</button></div>
    <div className={styles.stage} data-mode={mode}>{[1, 0].map(side => <div key={side} className={side === 0 ? styles.mapA : styles.mapB} style={side === 0 && mode === "swipe" ? { clipPath: `inset(0 ${100 - divider}% 0 0)` } : undefined}>
      <div className={styles.imagePlane} style={{ aspectRatio: `${width}/${height}`, transform: `translate(${offset.x}%, ${offset.y}%) scale(${scale})` }}>
        {tiles.filter(tile => tile.side === side).map(tile => <div key={tile.url} className={styles.imageTile} style={{ left: `${(tile.x - minX) / width * 100}%`, top: `${(tile.y - minY) / height * 100}%`, width: `${100 / width}%`, height: `${100 / height}%` }}>
          {typeof images[tile.url] === "string" ? <img src={images[tile.url]!} alt="" draggable={false} onError={() => setImages(current => ({ ...current, [tile.url]: null }))} style={{ imageRendering: pair.id === "ee-cdl" ? "pixelated" : "auto" }} /> : <span>{images[tile.url] === null ? "Tile unavailable" : "Loading"}</span>}
        </div>)}
      </div>
    </div>)}{mode === "swipe" && <div className={styles.divider} aria-hidden="true" style={{ left: `${divider}%` }} />}</div>
    <div className={styles.statuses} aria-live="polite"><span>A · {pair.a.year}: {summary(0)}</span><span>B · {pair.b.year}: {summary(1)}</span></div>
    <p>2D image overview · prepared zoom {z}. Zoom magnifies these pixels; it does not add source detail.</p>
  </>;
}

function PairViewer({ pair, mode, divider }: { pair: ReadyPair; mode: Mode; divider: number }) {
  const [images, setImages] = useState(false), [attempt, setAttempt] = useState(0);
  // Stable callback prevents map recreation when the divider or layout changes.
  const fallback = useMemo(() => () => setImages(true), []);
  return <>
    <div className={styles.navigation}><button type="button" onClick={() => setImages(value => !value)}>{images ? "Try WebGL maps" : "Use 2D images"}</button><button type="button" onClick={() => setAttempt(value => value + 1)}>Retry tiles</button></div>
    {images ? <ComparisonImages key={`images-${attempt}`} pair={pair} mode={mode} divider={divider} /> : <ComparisonMaps key={`maps-${attempt}`} pair={pair} mode={mode} divider={divider} onFallback={fallback} />}
  </>;
}

export function EarthEngineComparisonDialog({ manifests, loading, error, onClose }: { manifests: EarthEngineContextManifest[]; loading: boolean; error: string | null; onClose: () => void }) {
  const dialog = useRef<HTMLDialogElement>(null), titleId = useId();
  const products = EARTH_ENGINE_CONTEXT_LAYERS.filter(layer => EARTH_ENGINE_SOURCE_YEARS[layer.id]);
  const [id, setId] = useState<EarthEngineContextLayerId>(() => products.find(layer => comparisonYears(manifests, layer.id).length >= 2)?.id ?? products[0].id);
  const [selected, setSelected] = useState<{ a: number; b: number } | null>(null);
  const [mode, setMode] = useState<Mode>("swipe"), [divider, setDivider] = useState(50);
  const years = comparisonYears(manifests, id), yearA = selected?.a ?? years[0], yearB = selected?.b ?? years.at(-1);
  const pair = useMemo(() => {
    const installed = comparisonYears(manifests, id);
    return comparisonPair(manifests, id, selected?.a ?? installed[0] ?? NaN, selected?.b ?? installed.at(-1) ?? NaN);
  }, [manifests, id, selected]);
  useEffect(() => { dialog.current?.showModal(); }, []);
  return <dialog ref={dialog} className={styles.dialog} aria-labelledby={titleId} onCancel={onClose} onClose={onClose}>
    <header className={styles.header}><div><h2 id={titleId}>Compare imagery years</h2><p>Two approved snapshots of one product · flat Kansas map</p></div><button type="button" onClick={onClose} autoFocus>Close</button></header>
    <div className={styles.selectors}>
      <label>Product<select value={id} onChange={event => { setId(event.target.value as EarthEngineContextLayerId); setSelected(null); }}>{products.map(product => <option key={product.id} value={product.id}>{product.title} · {comparisonYears(manifests, product.id).length} installed years</option>)}</select></label>
      <label>Year A<select disabled={!years.length} value={yearA ?? ""} onChange={event => setSelected({ a: Number(event.target.value), b: yearB ?? Number(event.target.value) })}>{!years.length && <option value="">No installed year</option>}{years.map(year => <option key={year} value={year}>{year}</option>)}</select></label>
      <label>Year B<select disabled={!years.length} value={yearB ?? ""} onChange={event => setSelected({ a: yearA ?? Number(event.target.value), b: Number(event.target.value) })}>{!years.length && <option value="">No installed year</option>}{years.map(year => <option key={year} value={year}>{year}</option>)}</select></label>
      <label>Layout<select value={mode} onChange={event => setMode(event.target.value as Mode)}><option value="swipe">Swipe</option><option value="side-by-side">Side by side</option></select></label>
    </div>
    <p className={styles.boundary}>Visual comparison only. Color differences do not establish measured change, cause, or KFM evidence. Transparent and missing areas remain gaps; acquisition and processing can differ between years.</p>
    {loading || error ? <p role="status">{loading ? "Checking installed snapshots…" : `Snapshot catalog unavailable: ${error}`}</p> : pair.kind === "unavailable" ? <p role="status">{pair.reason} <a href="/earth-engine">Prepare another year</a></p> : <>
      <div className={styles.captions}>{[pair.a, pair.b].map((snapshot, i) => <section key={snapshot.setId} aria-label={`Year ${i === 0 ? "A" : "B"} source details`}><strong>{i === 0 ? "A" : "B"} · {snapshot.layer.period}</strong><span>{snapshot.layer.resolutionMeters.toLocaleString()} m grid · {snapshot.layer.attribution}</span><span className={styles.legend}>{EARTH_ENGINE_DISPLAY_RAMPS[id] && <i aria-hidden="true" style={{ background: earthEngineLegendGradient(EARTH_ENGINE_DISPLAY_RAMPS[id]) }} />}{snapshot.layer.legend}</span><details><summary>Limits and snapshot identity</summary><p>{snapshot.layer.limits}</p><p>{snapshot.setId}</p>{id === "ee-cdl" && <p>Use each year’s reviewed class key; do not infer crop transitions from colors alone.</p>}</details></section>)}</div>
      <PairViewer key={pair.key} pair={pair} mode={mode} divider={divider} />
      {mode === "swipe" && <label className={styles.slider}>Comparison divider · A {divider}% / B {100 - divider}%<input type="range" min="0" max="100" step="1" value={divider} aria-label="Comparison divider" aria-valuetext={`Year A covers ${divider} percent; year B covers ${100 - divider} percent`} onChange={event => setDivider(Number(event.target.value))} /><small>Arrow keys adjust the divider. Home and End show one complete year.</small></label>}
    </>}
  </dialog>;
}

export function EarthEngineComparisonPanel({ manifests, loading, error }: { manifests: EarthEngineContextManifest[]; loading: boolean; error: string | null }) {
  const [open, setOpen] = useState(false);
  const trigger = useRef<HTMLButtonElement>(null), wasOpen = useRef(false);
  useEffect(() => { if (wasOpen.current && !open) trigger.current?.focus(); wasOpen.current = open; }, [open]);
  return <div className={styles.launch}><button ref={trigger} type="button" aria-haspopup="dialog" aria-expanded={open} onClick={() => setOpen(true)}>Compare imagery years</button><small>Swipe or view two installed years side by side.</small>{open && createPortal(<EarthEngineComparisonDialog manifests={manifests} loading={loading} error={error} onClose={() => setOpen(false)} />, document.body)}</div>;
}
