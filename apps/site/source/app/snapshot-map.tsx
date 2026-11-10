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
import { readSceneEffects, registerSceneEffects } from "./scene-effects";
import { webgl2Available } from "./webgl-support";

type Camera = { center: [number, number]; zoom: number; bearing: number; pitch: number };
type PreviewAttempt = {
  disposed: boolean;
  expired: boolean;
  failed: boolean;
  deadline: ReturnType<typeof setTimeout> | null;
  beginReadiness: () => void;
};

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
  const attemptRef = useRef<PreviewAttempt | null>(null);
  const [attemptKey, setAttemptKey] = useState(0);
  const [phase, setPhase] = useState<"loading" | "ready" | "error">("loading");
  const [status, setStatus] = useState("Loading map context…");
  const clearDeadline = useCallback((attempt: PreviewAttempt) => {
    if (attempt.deadline !== null) clearTimeout(attempt.deadline);
    attempt.deadline = null;
  }, []);
  const showFailure = useCallback((message: string) => {
    const attempt = attemptRef.current;
    if (!attempt || attempt.disposed || attempt.expired) return;
    attempt.failed = true;
    clearDeadline(attempt);
    setPhase("error");
    setStatus(message);
  }, [clearDeadline]);
  const containMapMutation = useCallback((operation: string, mutation: () => void): boolean => {
    try {
      mutation();
      return true;
    } catch {
      showFailure(`${operation} is unavailable. Retry the preview; scene details and evidence remain readable. MAP_RENDER_FAILED`);
      return false;
    }
  }, [showFailure]);

  const applySnapshot = useCallback((): boolean => {
    const attempt = attemptRef.current;
    if (!attempt || attempt.disposed || attempt.expired) return false;
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
    map.setMaxPitch(state.representation === "Terrain 3D" ? 72 : 60);
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
    if (succeeded && applied) {
      clearDeadline(attempt);
      if (!attempt.failed) {
        setPhase("ready");
        setStatus("Saved map context · provider overlays are not replayed in this preview.");
      }
    }
    return succeeded && applied;
  }, [clearDeadline, containMapMutation]);

  useEffect(() => {
    current.current = snapshot;
  }, [snapshot]);

  useEffect(() => {
    onMove.current = onCameraChange;
  }, [onCameraChange]);

  useEffect(() => {
    if (!container.current) return;
    const attempt: PreviewAttempt = { disposed: false, expired: false, failed: false, deadline: null, beginReadiness: () => undefined };
    attemptRef.current = attempt;
    setPhase("loading");
    setStatus("Loading map context…");
    let observer: ResizeObserver | undefined;
    let ownedMap: MapLibreMap | null = null;
    const active = () => attemptRef.current === attempt && !attempt.disposed && !attempt.expired;
    const removeMap = () => {
      observer?.disconnect();
      const map = ownedMap;
      ownedMap = null;
      if (mapRef.current === map) { mapRef.current = null; appliedBasemap.current = null; }
      try { map?.remove(); } catch { /* A failed renderer must not prevent preview recovery or unmount. */ }
    };
    attempt.beginReadiness = () => {
      // Preserve the whole adapter + initial style deadline. A later basemap
      // change gets a fresh bound; an error stays visible until explicit retry.
      if (!active() || attempt.failed || attempt.deadline !== null) return;
      attempt.deadline = setTimeout(() => {
        if (!active()) return;
        showFailure("The map preview timed out. Retry the preview; scene details and evidence remain readable.");
        attempt.expired = true;
        removeMap();
      }, 15_000);
    };
    attempt.beginReadiness();
    const apply = () => { if (active()) applySnapshot(); };
    loadMapLibre().then((lib) => {
      if (!active() || !container.current) return;
      if (!webgl2Available()) {
        showFailure("Map unavailable: WebGL2 is not supported here. Retry after graphics support is available; scene details and evidence remain readable.");
        return;
      }
      lib.setWorkerUrl("/maplibre/maplibre-gl-worker.mjs");
      const state = current.current;
      const safeCamera: Camera = state.camera.center === "WITHHELD_BROWSER_LOCATION"
        ? { center: [-98.38, 38.48], zoom: 5.4, bearing: 0, pitch: 0 }
        : state.camera as Camera;
      const key = Object.prototype.hasOwnProperty.call(BASEMAPS, state.basemap) ? state.basemap as keyof typeof BASEMAPS : "standard";
      const budget = browserRenderBudget();
      const map = new lib.Map({ transformRequest: basemapCacheRequest, container: container.current, style: BASEMAPS[key].style, ...safeCamera, attributionControl: { compact: true }, pixelRatio: budget.pixelRatio, maxTileCacheSize: Math.min(48, budget.tileCache), maxPitch: state.representation === "Terrain 3D" ? 72 : 60, renderWorldCopies: false });
      ownedMap = map;
      // Snapshots honour the viewer's scene-effect preference for relief lighting.
      registerSceneEffects(map, readSceneEffects());
      mapRef.current = map;
      appliedBasemap.current = key;
      map.addControl(new lib.NavigationControl(), "top-right");
      map.addControl(new lib.ScaleControl({ maxWidth: 80 }), "bottom-left");
      map.on("load", apply);
      map.on("style.load", apply);
      map.on("move", () => {
        if (!active() || syncing.current) return;
        onMove.current?.({ center: map.getCenter().toArray(), zoom: map.getZoom(), bearing: map.getBearing(), pitch: map.getPitch() });
      });
      map.on("error", () => { if (active()) showFailure("Some map context is unavailable. Retry the preview; consult the scene details and evidence. No replacement claim is inferred."); });
      observer = new ResizeObserver(() => { if (active()) containMapMutation("Snapshot map resize", () => map.resize()); });
      observer.observe(container.current);
    }).catch(() => { if (active()) showFailure("Map adapter unavailable. Retry the preview; scene details and evidence remain readable."); });
    return () => { attempt.disposed = true; clearDeadline(attempt); removeMap(); if (attemptRef.current === attempt) attemptRef.current = null; };
  }, [applySnapshot, attemptKey, clearDeadline, containMapMutation, showFailure]);

  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    const key = Object.prototype.hasOwnProperty.call(BASEMAPS, snapshot.basemap) ? snapshot.basemap as keyof typeof BASEMAPS : "standard";
    if (appliedBasemap.current !== key) {
      const attempt = attemptRef.current;
      if (attempt && !attempt.failed) { setPhase("loading"); setStatus("Loading saved basemap…"); }
      attempt?.beginReadiness();
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
    <div ref={container} className="snapshot-map-canvas" aria-busy={phase === "loading"} />
    <figcaption><span role={phase === "error" ? "alert" : "status"}>{status} {phase !== "ready" && "Provider overlays are not replayed in this preview."}</span> <button type="button" aria-busy={phase === "loading"} onClick={() => setAttemptKey(key => key + 1)}>{phase === "loading" ? "Restart preview" : phase === "error" ? "Retry preview" : "Refresh preview"}</button></figcaption>
  </figure>;
}
