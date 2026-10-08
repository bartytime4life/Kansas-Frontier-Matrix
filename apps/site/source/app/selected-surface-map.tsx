"use client";
import { useEffect, useRef, useState } from "react";
import { loadMapLibre, type Map as GLMap } from "./maplibre-seam";
import { browserRenderBudget } from "./map-performance";
import { captureSelectedSurface, surfaceBoundsMatch, surfaceCameraBounds, surfaceSliceStyle, surfaceRasterSampling, constrainSurfaceCenter, type SurfaceCapture, type SurfaceBounds } from "./selected-surface";
import s from "./subsurface.module.css";

export default function SelectedSurfaceMap({ source, bounds, image, active, smooth, onSmooth }: {
  source: GLMap | null; bounds: SurfaceBounds; image: HTMLCanvasElement | null; active: boolean; smooth: boolean; onSmooth: () => void;
}) {
  const host = useRef<HTMLDivElement>(null), view = useRef<GLMap | null>(null);
  const [capture, setCapture] = useState<SurfaceCapture | null>(null), [status, setStatus] = useState("Preparing the selected surface layers…");
  const [zoom, setZoom] = useState<number | null>(null), [canReload, setCanReload] = useState(false), [reload, setReload] = useState(0);
  const camera = useRef<{ area: string; center: [number, number]; zoom: number } | null>(null);
  const area = bounds.join(","), capturedArea = capture?.bounds.join(",");
  const selectedBounds = useRef(bounds), smoothRef = useRef(smooth);
  useEffect(() => { selectedBounds.current = bounds; smoothRef.current = smooth; }, [bounds, smooth]);
  useEffect(() => {
    if (!source) return;
    const read = () => setCanReload(surfaceBoundsMatch(source, selectedBounds.current));
    read(); source.on("moveend", read); source.on("styledata", read);
    return () => { source.off("moveend", read); source.off("styledata", read); };
  }, [source, area]);
  useEffect(() => {
    if (!source) return;
    try {
      const next = captureSelectedSurface(source, selectedBounds.current);
      if (next) setCapture(next);
      else setCapture(previous => previous?.bounds.join(",") === area ? previous : null);
    } catch { setStatus("Surface layers could not be copied. Return the selector to this slice and reload layers."); }
  }, [source, area, image, reload]);
  useEffect(() => {
    if (!active || !capture || capturedArea !== area || !host.current) return;
    let disposed = false, failed = false, map: GLMap | null = null;
    const previousCamera = camera.current?.area === area ? camera.current : null;
    const frame = surfaceCameraBounds(capture.bounds);
    const fitLimit = () => {
      if (!map) return;
      map.setMinZoom(0);
      const fitted = map.cameraForBounds(frame, { padding: 12 });
      if (fitted) map.setMinZoom(fitted.zoom);
    };
    let resizeFrame: number | null = null;
    const observer = new ResizeObserver(() => {
      if (resizeFrame !== null) cancelAnimationFrame(resizeFrame);
      resizeFrame = requestAnimationFrame(() => { resizeFrame = null; if (!disposed && map) { map.resize(); fitLimit(); } });
    });
    setStatus("Loading the selected surface layers…");
    loadMapLibre().then(lib => {
      if (disposed || !host.current) return;
      lib.setWorkerUrl("/maplibre/maplibre-gl-worker.mjs");
      const budget = browserRenderBudget();
      map = new lib.Map({ container: host.current, style: surfaceSliceStyle(capture),
        bounds: frame, fitBoundsOptions: { padding: 12, duration: 0 }, maxBounds: frame,
        // The opaque outside mask permits fitting the entire rectangle at any aspect ratio.
        // Constrain the center instead of cropping the slice to fill the viewport.
        transformConstrain: (center, zoom) => ({ center: new lib.LngLat(...constrainSurfaceCenter(capture.bounds, center)), zoom: Math.max(map?.getMinZoom() ?? 0, Math.min(map?.getMaxZoom() ?? 22, zoom)) }),
        maxPitch: 0, dragRotate: false, pitchWithRotate: false, touchPitch: false, renderWorldCopies: false,
        pixelRatio: budget.pixelRatio, maxTileCacheSize: Math.min(48, budget.tileCache), attributionControl: { compact: true } });
      const surfaceMap = map; view.current = map;
      fitLimit();
      map.touchZoomRotate.disableRotation(); map.keyboard.disableRotation();
      map.getCanvas().setAttribute("aria-label", "Selected surface map. Drag or use arrow keys to pan within this slice; scroll, pinch, plus or minus to zoom.");
      map.addControl(new lib.ScaleControl({ unit: "imperial" }), "bottom-left");
      const remember = () => {
        if (disposed) return;
        const c = surfaceMap.getCenter(); camera.current = { area, center: [c.lng, c.lat], zoom: surfaceMap.getZoom() }; setZoom(surfaceMap.getZoom());
      };
      map.on("moveend", remember);
      map.on("styleimagemissing", event => {
        const image = capture.images.find(image => image.id === event.id);
        if (image && !surfaceMap.hasImage(image.id)) surfaceMap.addImage(image.id, image.data, { pixelRatio: image.pixelRatio, sdf: image.sdf });
      });
      map.on("load", () => {
        if (disposed) return;
        for (const image of capture.images) if (!surfaceMap.hasImage(image.id)) surfaceMap.addImage(image.id, image.data, { pixelRatio: image.pixelRatio, sdf: image.sdf });
        for (const sample of surfaceRasterSampling(capture.style, smoothRef.current)) surfaceMap.setPaintProperty(sample.id, "raster-resampling", sample.value);
        if (previousCamera) surfaceMap.jumpTo({ center: previousCamera.center, zoom: previousCamera.zoom });
        remember();
        if (!failed) setStatus("Surface map ready. The selected slice is fixed; zoom and pan change only this view.");
      });
      map.on("error", () => { failed = true; if (!disposed) setStatus("Some surface layers or tiles are unavailable. Blank areas are gaps, not clear conditions. Reload layers to retry."); });
      observer.observe(host.current);
    }).catch(() => { if (!disposed) setStatus("The surface map could not start. Reload layers to retry."); });
    return () => {
      disposed = true; observer.disconnect(); if (resizeFrame !== null) cancelAnimationFrame(resizeFrame);
      if (view.current === map) view.current = null;
      if (map) { const c = map.getCenter(); camera.current = { area, center: [c.lng, c.lat], zoom: map.getZoom() }; map.remove(); }
    };
  }, [active, capture, capturedArea, area]);
  useEffect(() => {
    if (!capture || !view.current?.isStyleLoaded()) return;
    for (const sample of surfaceRasterSampling(capture.style, smooth)) view.current.setPaintProperty(sample.id, "raster-resampling", sample.value);
  }, [smooth, capture]);
  const fit = () => { if (view.current) view.current.fitBounds(surfaceCameraBounds(bounds), { padding: 12, duration: 0 }); };
  return <div hidden={!active} className={s.surfaceWorkspace}>
    <div className={s.surfaceNavigation} aria-label="Selected surface navigation">
      <button type="button" disabled={!capture} aria-label="Zoom selected surface in" onClick={() => view.current?.zoomIn({ duration: 0 })}>Zoom in</button>
      <button type="button" disabled={!capture} aria-label="Zoom selected surface out" onClick={() => view.current?.zoomOut({ duration: 0 })}>Zoom out</button>
      <button type="button" disabled={!capture} onClick={fit}>Fit selected slice</button>
      <button type="button" aria-pressed={!smooth} onClick={onSmooth}>Crisp imagery</button>
      <button type="button" disabled={!canReload} onClick={() => setReload(value => value + 1)}>Reload surface layers</button>
    </div>
    <p className={s.surfaceHint}>Drag to pan · scroll or pinch to zoom · arrow keys move the map. The selected slice stays fixed.</p>
    <div ref={host} className={s.surfaceMap} role="region" aria-label="Interactive surface of the selected slice" />
    <div className={s.surfaceStatus} role="status"><strong>Display context · not KFM evidence</strong><span>{capture && capturedArea === area ? status : "Surface layers are unavailable for this slice. Show this area in the selector to prepare them."}</span><span>{zoom !== null ? `Surface zoom ${zoom.toFixed(1)} · ` : ""}Fixed slice: {bounds.map(n => n.toFixed(4)).join(", ")}</span></div>
    <details className={s.surfaceSources}><summary>Surface layers, clocks &amp; limits</summary>
      <p>These are the selected map layers copied when the area was applied{capture ? ` (${capture.copiedAt})` : ""}. That is a copy time, not an observation time. Reload surface layers applies current styling and source frames while keeping this slice and its zoom.</p>
      {!canReload && <p>The left map is previewing another area. Return it to this slice, or use Show new area to replace the selection.</p>}
      <p>Raster and vector tiles load available detail as you zoom; provider resolution and coverage still limit detail. Point records keep their coordinates and source values. Live animations and custom canvas effects are not replayed here{capture?.omitted ? `; ${capture.omitted} visible render layers could not be copied` : ""}.</p>
      <p>Earth Engine source years remain independent of map time. NASA thermal raster image date remains unresolved; selectable fire detections retain their checked UTC day and per-point acquisition times. Smoothing changes drawn pixels only. Missing imagery and empty detections are not an all-clear.</p>
    </details>
  </div>;
}
