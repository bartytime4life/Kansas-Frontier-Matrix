"use client";

import { useEffect, useLayoutEffect, useRef, useState, type RefObject } from "react";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { balanceMapRasters, syncMercatorRaster } from "./map-layer-composition";
import { browserJsonRequest } from "./browser-json-request";

const SOURCE = "external-crop-casma-1km";
const LAYER = "external-crop-casma-1km-raster";
type Availability = { state: "available" | "held" | "error"; day?: string; validCells?: number; dataMin?: number; dataMax?: number; sourceUrl?: string; code?: string; coverageState?: string; coverageCheckpoints?: Record<string, number | null> };

function checkedAvailability(value: unknown): Availability {
  if (!value || typeof value !== "object" || Array.isArray(value)) throw new Error("Invalid soil availability");
  const data = value as Record<string, unknown>;
  if (data.state === "held" || data.state === "error") return { state: data.state };
  if (data.state !== "available" || typeof data.day !== "string" || !/^20\d{2}-\d{2}-\d{2}$/.test(data.day)
    || !Number.isFinite(Date.parse(`${data.day}T00:00:00Z`)) || new Date(`${data.day}T00:00:00Z`).toISOString().slice(0, 10) !== data.day
    || !Number.isSafeInteger(data.validCells) || Number(data.validCells) < 1
    || typeof data.dataMin !== "number" || !Number.isFinite(data.dataMin) || typeof data.dataMax !== "number" || !Number.isFinite(data.dataMax)
    || data.dataMin < 0 || data.dataMax > 1 || data.dataMin > data.dataMax
    || !["PARTIAL_AT_CHECKPOINTS", "SAMPLED_ONLY"].includes(String(data.coverageState))
    || !data.coverageCheckpoints || typeof data.coverageCheckpoints !== "object" || Array.isArray(data.coverageCheckpoints)) throw new Error("Invalid soil availability");
  const checkpoints = data.coverageCheckpoints as Record<string, unknown>;
  if (Object.keys(checkpoints).sort().join(",") !== "Dodge City,Kansas City,Salina,Topeka,Wichita"
    || Object.values(checkpoints).some(value => value !== null && (typeof value !== "number" || !Number.isFinite(value) || value < 0 || value > 1))
    || (data.coverageState === "PARTIAL_AT_CHECKPOINTS") !== Object.values(checkpoints).some(value => value === null)) throw new Error("Invalid soil coverage");
  return { state: "available", day: data.day, validCells: Number(data.validCells), dataMin: data.dataMin, dataMax: data.dataMax,
    coverageState: String(data.coverageState), coverageCheckpoints: checkpoints as Record<string, number | null> };
}

export function CropCasmaControl({ mapRef, styleReady, projection, onSelectionChange }: { mapRef: RefObject<MapLibreMap | null>; styleReady: boolean; projection: "mercator" | "globe"; onSelectionChange?: (selected: boolean) => void }) {
  const [availability, setAvailability] = useState<Availability | null>(null);
  const [checking, setChecking] = useState(false);
  const [enabled, setEnabled] = useState(false);
  const [opacity, setOpacity] = useState(0.7);
  const [renderState, setRenderState] = useState<"off" | "loading" | "rendered" | "partial">("off");
  const [revision, setRevision] = useState(0);
  const opacityRef = useRef(opacity);
  const projectionRef = useRef(projection);

  useEffect(() => {
    const abort = new AbortController();
    // This state marks the start of the release check owned by this effect.
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setChecking(true);
    void browserJsonRequest("/api/crop-casma/availability", { signal: abort.signal, maxBytes: 16 * 1024, timeoutMs: 15_000 })
      .then(({ response, body }) => {
        const data = response.ok ? checkedAvailability(body) : { state: "error" as const, code: "BACKEND_UNAVAILABLE" };
        if (!abort.signal.aborted) setAvailability(data);
      })
      .catch(() => { if (!abort.signal.aborted) setAvailability({ state: "error", code: "BACKEND_UNAVAILABLE" }); })
      .finally(() => { if (!abort.signal.aborted) setChecking(false); });
    return () => abort.abort();
  }, [revision]);

  /* eslint-disable react-hooks/set-state-in-effect -- Map source lifecycle reports loading and failure from this effect. */
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleReady || !enabled || availability?.state !== "available" || !availability.day) {
      if (map?.getLayer(LAYER)) map.removeLayer(LAYER);
      if (map?.getSource(SOURCE)) map.removeSource(SOURCE);
      if (map) balanceMapRasters(map);
      setRenderState("off");
      return;
    }
    let active = true, failed = false;
    setRenderState("loading");
    try {
      if (map.getLayer(LAYER)) map.removeLayer(LAYER);
      if (map.getSource(SOURCE)) map.removeSource(SOURCE);
      map.addSource(SOURCE, { type: "raster",
        tiles: [`/api/crop-casma/tile?day=${availability.day}&z={z}&x={x}&y={y}`], tileSize: 256,
        minzoom: 4, maxzoom: 9, bounds: [-102.1, 36.95, -94.55, 40.05],
        attribution: "USDA NASS Crop-CASMA · SMAP Hybrid 1 km · reviewed snapshot" });
      map.addLayer({ id: LAYER, type: "raster", source: SOURCE, layout: { visibility: projectionRef.current === "mercator" && map.getProjection()?.type === "mercator" ? "visible" : "none" },
        paint: { "raster-opacity": opacityRef.current, "raster-resampling": "nearest", "raster-fade-duration": 0 } });
      syncMercatorRaster(map, LAYER, opacityRef.current, projectionRef.current);
    } catch {
      if (map.getLayer(LAYER)) map.removeLayer(LAYER);
      if (map.getSource(SOURCE)) map.removeSource(SOURCE);
      balanceMapRasters(map);
      setRenderState("partial");
      return;
    }
    const onSource = (event: { sourceId?: string; isSourceLoaded?: boolean }) => {
      if (active && event.sourceId === SOURCE && event.isSourceLoaded) setRenderState(failed ? "partial" : "rendered");
    };
    const onError = (event: unknown) => {
      if (active && (event as { sourceId?: string }).sourceId === SOURCE) { failed = true; setRenderState("partial"); }
    };
    map.on("sourcedata", onSource);
    map.on("error", onError);
    const onRender = () => {
      if (map.getLayer(LAYER) && map.getLayoutProperty(LAYER, "visibility") !== (projectionRef.current === "mercator" && map.getProjection()?.type === "mercator" ? "visible" : "none"))
        syncMercatorRaster(map, LAYER, opacityRef.current, projectionRef.current);
    };
    map.on("render", onRender);
    return () => {
      active = false;
      map.off("sourcedata", onSource);
      map.off("error", onError);
      map.off("render", onRender);
      if (map.getLayer(LAYER)) map.removeLayer(LAYER);
      if (map.getSource(SOURCE)) map.removeSource(SOURCE);
      balanceMapRasters(map);
    };
  }, [availability?.day, availability?.state, enabled, mapRef, styleReady]);
  /* eslint-enable react-hooks/set-state-in-effect */

  useLayoutEffect(() => {
    opacityRef.current = opacity;
    projectionRef.current = projection;
    const map = mapRef.current;
    if (map?.getLayer(LAYER)) syncMercatorRaster(map, LAYER, opacity, projection);
  }, [mapRef, opacity, projection, styleReady]);

  useEffect(() => { onSelectionChange?.(enabled); }, [enabled, onSelectionChange]);
  const globeHeld = projection === "globe";
  const available = availability?.state === "available";
  const displayState = enabled && (!available || globeHeld || !styleReady) ? "held" : renderState;
  return <article className="official-context-row crop-casma-control" data-state={displayState} data-visible={enabled && available && !globeHeld && styleReady}>
    <div className="official-context-primary">
      <label className="visibility-switch"><input type="checkbox" checked={enabled} disabled={!enabled && !available}
        aria-label={enabled ? "Hide Crop-CASMA 1 km soil moisture" : "Show Crop-CASMA 1 km soil moisture"}
        onChange={event => { setEnabled(event.target.checked); if (!event.target.checked) setRenderState("off"); }} /><span aria-hidden="true" /></label>
      <i style={{ "--swatch": "#77c5a6" } as React.CSSProperties} />
      <div><strong>Soil moisture · 1 km hybrid</strong><small>USDA NASS Crop-CASMA · derived numeric cells · {enabled ? globeHeld ? "selected · globe held" : displayState : checking ? "checking" : availability?.state ?? "unchecked"}</small></div>
    </div>
    <details className="specialty-layer-details"><summary>Source &amp; controls</summary><div className="official-context-option-body">
      <div className="soil-display-panel"><div><span>SEPARATE REVIEWED PRODUCT</span><strong>{availability?.day ?? "No active day"}</strong><small>1,000 m source grid · volumetric moisture (m³/m³) · no value interpolation</small></div><b data-state={displayState}>{enabled ? globeHeld && available ? "GLOBE HELD" : displayState.toUpperCase() : available ? "READY" : "HELD"}</b></div>
      {availability?.state === "available" ? <>
        <label className="crop-casma-opacity">Opacity <input type="range" min="0" max="100" value={Math.round(opacity * 100)} onChange={event => setOpacity(Number(event.target.value) / 100)} /><output>{Math.round(opacity * 100)}%</output></label>
        <small>Available {availability.day}. Values span {availability.dataMin?.toFixed(3)}–{availability.dataMax?.toFixed(3)} m³/m³ across {availability.validCells?.toLocaleString("en-US")} source cells. Transparent cells have no source value. This is a derived product, not a station observation.</small>
        {availability.coverageState === "PARTIAL_AT_CHECKPOINTS" && <p role="status">Partial source coverage at checked locations: {Object.entries(availability.coverageCheckpoints ?? {}).filter(([, value]) => value === null).map(([name]) => name).join(", ")} have no-data cells on this day. These checks do not define the full coverage boundary.</p>}
      </> : <p>{availability?.state === "error" ? "The reviewed package could not be checked. No 1 km image is shown." : "A 1 km source candidate requires steward review and release before map tiles can be shown."}</p>}
      <div className="soil-source-actions"><button type="button" onClick={() => setRevision(value => value + 1)} disabled={checking}>Recheck release</button><a href="https://nassgeo.csiss.gmu.edu/Crop-CASMA-Developer/wcs/SMAP-HYB-1KM/" target="_blank" rel="noopener noreferrer">Provider guide ↗</a></div>
      <small>The palette colors exact nearest source cells. Zooming in cannot reveal detail below 1 km; this layer has no invented intermediate observations or missing-day loop.</small>
    </div></details>
  </article>;
}
