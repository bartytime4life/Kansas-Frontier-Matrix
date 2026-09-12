"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import type { Map as MapLibreMap } from "maplibre-gl";
import { LAYER_REGISTRY } from "./explorer-data";
import { applyRegistryState, BASEMAPS, setTerrainPresentation, updateAnalysisAreaSource, updateSelectionSource } from "./map-runtime";
import { isFeatureAvailableForTemporalQuery, type TemporalSweepQuery } from "./temporal-sweep";
import type { MapSnapshot } from "./workspace-model";
import { browserRenderBudget } from "./map-performance";

type Camera = { center: [number, number]; zoom: number; bearing: number; pitch: number };

const temporalQueryForSnapshot = (snapshot: MapSnapshot): TemporalSweepQuery => snapshot.temporalSweep
  ? {
    mode: snapshot.temporalSweep.mode,
    frame: snapshot.temporalSweep.frame,
    rangeStart: snapshot.temporalSweep.rangeStart,
    rangeEnd: snapshot.temporalSweep.rangeEnd,
    windowStart: snapshot.temporalSweep.windowStart,
  }
  : {
    mode: "snapshot",
    frame: snapshot.committedTime.start,
    rangeStart: snapshot.committedTime.start,
    rangeEnd: snapshot.committedTime.end,
    windowStart: snapshot.committedTime.start,
  };

const selectionForSnapshot = (snapshot: MapSnapshot, query: TemporalSweepQuery) => {
  const layer = LAYER_REGISTRY.find((candidate) => candidate.id === snapshot.selection?.layerId);
  const selected = layer?.data.features.find((feature) => feature.properties.fid === snapshot.selection?.featureId);
  if (!layer || !selected || !snapshot.visibleLayers.some((item) => item.id === layer.id)) return null;
  if (snapshot.evidenceFilter && snapshot.evidenceFilter !== "ALL" && selected.properties.evidenceState !== snapshot.evidenceFilter) return null;
  return isFeatureAvailableForTemporalQuery(layer, selected.properties.year, query) ? selected : null;
};

/** Read-only rendering adapter: snapshots never admit sources or emit findings. */
export default function SnapshotMap({ snapshot, label, syncCamera, onCameraChange }: {
  snapshot: MapSnapshot;
  label: string;
  syncCamera?: Camera;
  onCameraChange?: (camera: Camera) => void;
}) {
  const container = useRef<HTMLDivElement>(null);
  const mapRef = useRef<MapLibreMap | null>(null);
  const current = useRef(snapshot);
  const onMove = useRef(onCameraChange);
  const syncing = useRef(false);
  const [status, setStatus] = useState("Loading map context…");

  useEffect(() => {
    current.current = snapshot;
  }, [snapshot]);

  useEffect(() => {
    onMove.current = onCameraChange;
  }, [onCameraChange]);

  useEffect(() => {
    if (!container.current) return;
    let disposed = false;
    let observer: ResizeObserver | undefined;
    const apply = () => {
      const map = mapRef.current;
      if (!map?.isStyleLoaded()) return;
      const state = current.current;
      const visible = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, state.visibleLayers.some((item) => item.id === layer.id)]));
      const opacity = Object.fromEntries(state.visibleLayers.map((layer) => [layer.id, layer.opacity]));
      const query = temporalQueryForSnapshot(state);
      applyRegistryState(map, visible, opacity, query.frame, state.visibleLayers.map((layer) => layer.id), state.evidenceFilter ?? "ALL", query);
      map.setProjection({ type: state.projection });
      setTerrainPresentation(map, state.representation === "Terrain 3D", 1);
      updateAnalysisAreaSource(map, state.area.kind === "aoi" ? state.area.bounds : undefined);
      updateSelectionSource(map, selectionForSnapshot(state, query));
    };
    import("maplibre-gl").then((lib) => {
      if (disposed || !container.current) return;
      const probe = document.createElement("canvas").getContext("webgl2");
      if (!probe) {
        setStatus("Map unavailable: WebGL2 is not supported here. Scene details and evidence remain available below.");
        return;
      }
      probe.getExtension("WEBGL_lose_context")?.loseContext();
      lib.setWorkerUrl("/maplibre/maplibre-gl-worker.mjs");
      const state = current.current;
      const safeCamera: Camera = state.camera.center === "WITHHELD_BROWSER_LOCATION"
        ? { center: [-98.38, 38.48], zoom: 5.4, bearing: 0, pitch: 0 }
        : state.camera as Camera;
      const key = Object.prototype.hasOwnProperty.call(BASEMAPS, state.basemap) ? state.basemap as keyof typeof BASEMAPS : "standard";
      const budget = browserRenderBudget();
      const map = new lib.Map({ container: container.current, style: BASEMAPS[key].style, ...safeCamera, attributionControl: { compact: true }, pixelRatio: budget.pixelRatio, maxTileCacheSize: Math.min(48, budget.tileCache), maxPitch: 60, renderWorldCopies: false });
      mapRef.current = map;
      map.addControl(new lib.NavigationControl(), "top-right");
      map.addControl(new lib.ScaleControl({ maxWidth: 80 }), "bottom-left");
      map.on("load", () => { apply(); setStatus("Display context · bounded layers · no admission effect"); });
      map.on("style.load", apply);
      map.on("move", () => {
        if (syncing.current) return;
        onMove.current?.({ center: map.getCenter().toArray(), zoom: map.getZoom(), bearing: map.getBearing(), pitch: map.getPitch() });
      });
      map.on("error", () => setStatus("Some map context is unavailable. Consult the scene details and evidence; no replacement claim is inferred."));
      observer = new ResizeObserver(() => map.resize());
      observer.observe(container.current);
    }).catch(() => { if (!disposed) setStatus("Map adapter unavailable. Scene details and evidence remain readable."); });
    return () => { disposed = true; observer?.disconnect(); mapRef.current?.remove(); mapRef.current = null; };
  }, []);

  useEffect(() => {
    const map = mapRef.current;
    if (!map?.isStyleLoaded()) return;
    const visible = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, snapshot.visibleLayers.some((item) => item.id === layer.id)]));
    const query = temporalQueryForSnapshot(snapshot);
    applyRegistryState(map, visible, Object.fromEntries(snapshot.visibleLayers.map((layer) => [layer.id, layer.opacity])), query.frame, snapshot.visibleLayers.map((layer) => layer.id), snapshot.evidenceFilter ?? "ALL", query);
    map.setProjection({ type: snapshot.projection });
    setTerrainPresentation(map, snapshot.representation === "Terrain 3D", 1);
    updateAnalysisAreaSource(map, snapshot.area.kind === "aoi" ? snapshot.area.bounds : undefined);
    syncing.current = true;
    if (snapshot.camera.center !== "WITHHELD_BROWSER_LOCATION") map.jumpTo(snapshot.camera as Camera);
    syncing.current = false;
    updateSelectionSource(map, selectionForSnapshot(snapshot, query));
  }, [snapshot]);

  useEffect(() => {
    if (!syncCamera || !mapRef.current) return;
    syncing.current = true;
    mapRef.current.jumpTo(syncCamera);
    syncing.current = false;
  }, [syncCamera]);

  return <figure className="snapshot-map-renderer" aria-label={label}>
    <div ref={container} className="snapshot-map-canvas" />
    <figcaption role="status">{status}</figcaption>
  </figure>;
}

export function SynchronizedComparison({ snapshot, layerA, layerB, timeA, timeB }: {
  snapshot: MapSnapshot; layerA: string; layerB: string; timeA: number; timeB: number;
}) {
  const [camera, setCamera] = useState<Camera>();
  const scenes = useMemo(() => [layerA, layerB].map((id, index): MapSnapshot => {
    const layer = LAYER_REGISTRY.find((item) => item.id === id)!;
    const time = index === 0 ? timeA : timeB;
    return { ...snapshot, id: `comparison-${index}`, representation: "2D", projection: "mercator", selection: null,
      committedTime: { start: time, end: time, label: String(time), mode: "instant" },
      temporalSweep: { mode: "snapshot", frame: time, rangeStart: time, rangeEnd: time, windowStart: time, windowFrames: 1, stepRule: "available-events", interpolation: false },
      visibleLayers: [{ id, title: layer.title, domain: layer.domain, order: 0, opacity: 0.85, trustState: "Site-local demo" }],
    };
  }), [snapshot, layerA, layerB, timeA, timeB]);
  // Stable keys preserve both renderers while camera and time are synchronized.
  return <section className="synchronized-comparison" aria-label="Synchronized A/B map comparison">
    <p>Display and demonstration comparison. No admitted change-detection pair; dated fixtures remain discrete. Pan or zoom either map to move both.</p>
    <div className="comparison-maps">{scenes.map((scene, index) => <article key={index}>
      <h4>{index === 0 ? "A" : "B"} · {scene.visibleLayers[0].title} · {scene.committedTime.start}</h4>
      <SnapshotMap snapshot={scene} label={`Comparison ${index === 0 ? "A" : "B"}`} syncCamera={camera} onCameraChange={setCamera} />
    </article>)}</div>
    <p>Keyboard and text alternative: use the Time A / Time B availability table and layer summaries below. Geographic overlap does not establish change or causation.</p>
  </section>;
}
