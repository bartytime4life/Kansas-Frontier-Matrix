"use client";

import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { EARTH_ENGINE_CONTEXT_LAYERS, earthEngineTileVisibleAtYear, type EarthEngineContextLayerId, type EarthEngineContextManifest } from "./earth-engine-context";
import styles from "./earth-engine-raster-fallback.module.css";

export type EarthEngineDisplayState = {
  visible: Partial<Record<EarthEngineContextLayerId, boolean>>;
  opacity: Partial<Record<EarthEngineContextLayerId, number>>;
};

const tileSize = 256;
const overviewZoom = 8;

export function EarthEngineRasterFallback({ manifest, mapYear, display, onOpenLayers }: {
  manifest: EarthEngineContextManifest;
  mapYear: number;
  display: EarthEngineDisplayState;
  onOpenLayers: () => void;
}) {
  const viewportRef = useRef<HTMLDivElement>(null);
  const dragRef = useRef<{ x: number; y: number } | null>(null);
  const [size, setSize] = useState({ width: 0, height: 0 });
  const [zoom, setZoom] = useState(1);
  const [offset, setOffset] = useState({ x: 0, y: 0 });
  const [loaded, setLoaded] = useState<Set<string>>(() => new Set());
  const [failed, setFailed] = useState<Set<string>>(() => new Set());

  useEffect(() => {
    const node = viewportRef.current;
    if (!node) return;
    const observer = new ResizeObserver(([entry]) => {
      setSize({ width: entry.contentRect.width, height: entry.contentRect.height });
    });
    observer.observe(node);
    return () => observer.disconnect();
  }, []);

  const layers = useMemo(() => EARTH_ENGINE_CONTEXT_LAYERS.flatMap((descriptor) => {
    const layer = manifest.layers.find((item) => item.id === descriptor.id);
    const index = layer?.tileIndexes[String(overviewZoom)];
    return layer?.status === "approved" && index && display.visible[descriptor.id]
      && earthEngineTileVisibleAtYear(descriptor.id, mapYear)
      ? [{ layer, index }] : [];
  }), [display.visible, manifest, mapYear]);

  const bounds = useMemo(() => layers.length ? {
    minX: Math.min(...layers.map(({ index }) => index.minX)),
    maxX: Math.max(...layers.map(({ index }) => index.maxX)),
    minY: Math.min(...layers.map(({ index }) => index.minY)),
    maxY: Math.max(...layers.map(({ index }) => index.maxY)),
  } : null, [layers]);

  const imageUrls = useMemo(() => layers.flatMap(({ layer, index }) => {
    const urls: string[] = [];
    for (let y = index.minY; y <= index.maxY; y++) for (let x = index.minX; x <= index.maxX; x++) {
      urls.push(`/api/earth-engine-context/${encodeURIComponent(manifest.setId)}/${layer.id}/${overviewZoom}/${x}/${y}.png`);
    }
    return urls;
  }), [layers, manifest.setId]);
  const loadedCount = imageUrls.filter((url) => loaded.has(url)).length;
  const failedCount = imageUrls.filter((url) => failed.has(url)).length;
  const width = bounds ? (bounds.maxX - bounds.minX + 1) * tileSize : 0;
  const height = bounds ? (bounds.maxY - bounds.minY + 1) * tileSize : 0;
  const fit = width && height && size.width && size.height
    ? Math.min((size.width - 24) / width, (size.height - 24) / height) : 1;
  const scale = Math.max(0.1, fit) * zoom;
  const reportLoad = useCallback((url: string) => setLoaded((current) => current.has(url) ? current : new Set(current).add(url)), []);
  const reportFailure = useCallback((url: string) => setFailed((current) => current.has(url) ? current : new Set(current).add(url)), []);

  return <section className={styles.viewer} aria-label="Earth Engine raster viewer">
    <header className={styles.header}>
      <div><strong>Earth Engine snapshots · 2D image viewer</strong><small>Installed Kansas tiles · WebGL2 is unavailable in this browser</small></div>
      <div className={styles.controls}>
        <button type="button" onClick={onOpenLayers}>Layers</button>
        <button type="button" aria-label="Zoom out raster viewer" disabled={zoom <= 1} onClick={() => setZoom((value) => Math.max(1, value / 2))}>−</button>
        <button type="button" aria-label="Zoom in raster viewer" disabled={zoom >= 4} onClick={() => setZoom((value) => Math.min(4, value * 2))}>+</button>
        <button type="button" onClick={() => { setZoom(1); setOffset({ x: 0, y: 0 }); }}>Reset view</button>
      </div>
    </header>
    <div ref={viewportRef} className={styles.viewport}
      onPointerDown={(event) => { if (event.button !== 0 || !bounds) return; dragRef.current = { x: event.clientX, y: event.clientY }; event.currentTarget.setPointerCapture(event.pointerId); }}
      onPointerMove={(event) => { if (!dragRef.current) return; const dx = event.clientX - dragRef.current.x, dy = event.clientY - dragRef.current.y; dragRef.current = { x: event.clientX, y: event.clientY }; setOffset((current) => ({ x: current.x + dx, y: current.y + dy })); }}
      onPointerUp={() => { dragRef.current = null; }}
      onPointerCancel={() => { dragRef.current = null; }}>
      {!bounds ? <div className={styles.empty}><strong>Select an Earth Engine layer</strong><p>The installed snapshots will display here without the WebGL map.</p><button type="button" onClick={onOpenLayers}>Open layers</button></div> :
        <div className={styles.mosaic} style={{ width, height, left: (size.width - width * scale) / 2 + offset.x, top: (size.height - height * scale) / 2 + offset.y, transform: `scale(${scale})` }}>
          {layers.map(({ layer, index }) => <div key={layer.id} className={styles.layer} style={{ opacity: display.opacity[layer.id] ?? 0.72 }}>
            {Array.from({ length: index.maxY - index.minY + 1 }, (_, yi) => index.minY + yi).flatMap((y) =>
              Array.from({ length: index.maxX - index.minX + 1 }, (_, xi) => index.minX + xi).map((x) => {
                const url = `/api/earth-engine-context/${encodeURIComponent(manifest.setId)}/${layer.id}/${overviewZoom}/${x}/${y}.png`;
                return failed.has(url) ? null : <img key={url} src={url} alt="" draggable={false} width={tileSize} height={tileSize}
                  style={{ left: (x - bounds.minX) * tileSize, top: (y - bounds.minY) * tileSize }}
                  onLoad={() => reportLoad(url)} onError={() => reportFailure(url)} />;
              }))}
          </div>)}
        </div>}
    </div>
    <footer className={styles.footer}>
      <span role="status">{!bounds ? "No snapshot selected" : loadedCount ? `${loadedCount}/${imageUrls.length} image tiles loaded${failedCount ? ` · ${failedCount} unavailable` : ""}` : failedCount === imageUrls.length ? "Image tiles unavailable" : "Loading image tiles…"}</span>
      <span>{layers.map(({ layer }) => layer.attribution).join(" · ") || "Kansas display context"} · pixels are not KFM evidence</span>
    </footer>
  </section>;
}
