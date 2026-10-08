"use client";

import { basemapCacheRequest } from "./basemap-cache";
import { useCallback, useEffect, useRef, useState } from "react";
import { loadMapLibre, type Map as MapLibreMap } from "./maplibre-seam";
import { LAYER_REGISTRY } from "./explorer-data";
import { applyRegistryState, BASEMAPS, setTerrainPresentation, updateAnalysisAreaSource, updateSelectionSource } from "./map-runtime";
import { isFeatureAvailableForTemporalQuery, type TemporalSweepQuery } from "./temporal-sweep";
import type { MapSnapshot } from "./workspace-model";
import { browserRenderBudget } from "./map-performance";
import { terrainSourceFor } from "./terrain-sources";

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
  const appliedBasemap = useRef<keyof typeof BASEMAPS | null>(null);
  const [status, setStatus] = useState("Loading map context…");
  const containMapMutation = useCallback((operation: string, mutation: () => void): boolean => {
    try {
      mutation();
      return true;
    } catch {
      setStatus(`${operation} is unavailable. Scene details and evidence remain readable. MAP_RENDER_FAILED`);
      return false;
    }
  }, []);

  const applySnapshot = useCallback((): boolean => {
    let applied = false;
    const succeeded = containMapMutation("Snapshot map update", () => {
    const map = mapRef.current;
    if (!map?.isStyleLoaded()) return;
    const state = current.current;
    const visible = Object.fromEntries(LAYER_REGISTRY.map((layer) => [layer.id, state.visibleLayers.some((item) => item.id === layer.id)]));
    const opacity = Object.fromEntries(state.visibleLayers.map((layer) => [layer.id, layer.opacity]));
    const query = temporalQueryForSnapshot(state);
    applyRegistryState(map, visible, opacity, query.frame, state.visibleLayers.map((layer) => layer.id), state.evidenceFilter ?? "ALL", query);
    map.setProjection({ type: state.projection });
    const terrain = setTerrainPresentation(map, state.representation === "Terrain 3D", state.terrainExaggeration ?? 1, terrainSourceFor(state.terrainProvider ?? "mapzen"));
    if (terrain === "ERROR") throw new Error("Snapshot terrain unavailable");
    updateAnalysisAreaSource(map, state.area.kind === "aoi" ? state.area.bounds : undefined);
    updateSelectionSource(map, selectionForSnapshot(state, query));
    syncing.current = true;
    try {
      // Redacted scenes must not inherit a prior scene's precise location.
      map.jumpTo(state.camera.center === "WITHHELD_BROWSER_LOCATION"
        ? { center: [-98.38, 38.48], zoom: 5.4, bearing: 0, pitch: 0 }
        : state.camera as Camera);
    } finally { syncing.current = false; }
    applied = true;
    });
    if (succeeded && applied) setStatus("Saved map context · provider overlays are not replayed in this preview.");
    return succeeded && applied;
  }, [containMapMutation]);

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
    const apply = () => { applySnapshot(); };
    loadMapLibre().then((lib) => {
      if (disposed || !container.current) return;
      const probe = document.createElement("canvas").getContext("webgl2");
      if (!probe) {
        setStatus("Map unavailable: WebGL2 is not supported here. Scene details and evidence remain available below.");
        return;
      }
      // A detached probe is enough. Forcing WEBGL_lose_context can destabilize
      // the shared GPU surface in embedded Chromium hosts.
      lib.setWorkerUrl("/maplibre/maplibre-gl-worker.mjs");
      const state = current.current;
      const safeCamera: Camera = state.camera.center === "WITHHELD_BROWSER_LOCATION"
        ? { center: [-98.38, 38.48], zoom: 5.4, bearing: 0, pitch: 0 }
        : state.camera as Camera;
      const key = Object.prototype.hasOwnProperty.call(BASEMAPS, state.basemap) ? state.basemap as keyof typeof BASEMAPS : "standard";
      const budget = browserRenderBudget();
      const map = new lib.Map({ transformRequest: basemapCacheRequest, container: container.current, style: BASEMAPS[key].style, ...safeCamera, attributionControl: { compact: true }, pixelRatio: budget.pixelRatio, maxTileCacheSize: Math.min(48, budget.tileCache), maxPitch: 60, renderWorldCopies: false });
      mapRef.current = map;
      appliedBasemap.current = key;
      map.addControl(new lib.NavigationControl(), "top-right");
      map.addControl(new lib.ScaleControl({ maxWidth: 80 }), "bottom-left");
      map.on("load", apply);
      map.on("style.load", apply);
      map.on("move", () => {
        if (syncing.current) return;
        onMove.current?.({ center: map.getCenter().toArray(), zoom: map.getZoom(), bearing: map.getBearing(), pitch: map.getPitch() });
      });
      map.on("error", () => setStatus("Some map context is unavailable. Consult the scene details and evidence; no replacement claim is inferred."));
      observer = new ResizeObserver(() => { containMapMutation("Snapshot map resize", () => map.resize()); });
      observer.observe(container.current);
    }).catch(() => { if (!disposed) setStatus("Map adapter unavailable. Scene details and evidence remain readable."); });
    return () => { disposed = true; observer?.disconnect(); mapRef.current?.remove(); mapRef.current = null; appliedBasemap.current = null; };
  }, [applySnapshot, containMapMutation]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    const key = Object.prototype.hasOwnProperty.call(BASEMAPS, snapshot.basemap) ? snapshot.basemap as keyof typeof BASEMAPS : "standard";
    if (appliedBasemap.current !== key) {
      setStatus("Loading saved basemap…");
      containMapMutation("Snapshot basemap update", () => {
        map.setStyle(BASEMAPS[key].style);
        appliedBasemap.current = key;
      });
    } else applySnapshot();
  }, [applySnapshot, containMapMutation, snapshot]);

  useEffect(() => {
    if (!syncCamera || !mapRef.current) return;
    containMapMutation("Comparison camera update", () => {
      syncing.current = true;
      try { mapRef.current?.jumpTo(syncCamera); } finally { syncing.current = false; }
    });
  }, [containMapMutation, syncCamera]);

  return <figure className="snapshot-map-renderer" aria-label={label}>
    <div ref={container} className="snapshot-map-canvas" />
    <figcaption role="status">{status}</figcaption>
  </figure>;
}
