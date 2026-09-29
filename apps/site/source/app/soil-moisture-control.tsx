"use client";

import { useEffect, useRef, useState, type RefObject } from "react";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { SOIL_GUIDE_URL, SOIL_METADATA_URL, SOIL_VIEWS, soilLegendUrl, type SoilView } from "./soil-moisture";

const SOURCE = "external-nasa-smap-soil";
const LAYER = "external-nasa-smap-soil-raster";
type Availability = {
  state: "available" | "unavailable" | "error";
  availableDays: string[];
  latestCommonDay: string | null;
  checkedAt?: string;
  backend?: { state: "ok" | "error"; durationMs: number; cache: "hit" | "miss" | "none"; code?: string };
};
type MapState = { state: "off" | "held" | "loading" | "rendered" | "partial" | "error"; loaded: number; failed: number; renderedAt: string | null; day: string | null; view: SoilView | null };
const off: MapState = { state: "off", loaded: 0, failed: 0, renderedAt: null, day: null, view: null };

export function SoilMoistureControl({ mapRef, styleReady, is2D }: { mapRef: RefObject<MapLibreMap | null>; styleReady: boolean; is2D: boolean }) {
  const [enabled, setEnabled] = useState(false);
  const [depth, setDepth] = useState<"surface" | "root">("surface");
  const [uncertainty, setUncertainty] = useState(false);
  const [day, setDay] = useState("");
  const [opacity, setOpacity] = useState(0.65);
  const [availability, setAvailability] = useState<Availability | null>(null);
  const [checking, setChecking] = useState(false);
  const [mapState, setMapState] = useState<MapState>(off);
  const requestId = useRef(0);
  const view: SoilView = uncertainty ? `${depth}-uncertainty` : depth;

  function clearRaster() {
    const map = mapRef.current;
    if (!map) return;
    if (map.getLayer(LAYER)) map.removeLayer(LAYER);
    if (map.getSource(SOURCE)) map.removeSource(SOURCE);
  }

  async function checkAvailability(retry = false) {
    const id = ++requestId.current;
    setChecking(true);
    try {
      const response = await fetch(`/api/soil-moisture/availability${retry ? "?retry=1" : ""}`, { cache: "no-store" });
      const data = await response.json() as Availability;
      if (id !== requestId.current) return;
      if (!data.availableDays?.includes(day)) clearRaster();
      setAvailability(data);
      setDay(current => data.availableDays?.includes(current) ? current : data.latestCommonDay ?? "");
      if (!response.ok) setMapState({ ...off, state: "error" });
    } catch {
      if (id !== requestId.current) return;
      setAvailability({ state: "error", availableDays: [], latestCommonDay: null, backend: { state: "error", durationMs: 0, cache: "none", code: "SITE_REQUEST_FAILED" } });
      setDay("");
      setMapState({ ...off, state: "error" });
    } finally { if (id === requestId.current) setChecking(false); }
  }

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleReady) return;
    // Removing the source first clears cached imagery from the previous day/view.
    if (map.getLayer(LAYER)) map.removeLayer(LAYER);
    if (map.getSource(SOURCE)) map.removeSource(SOURCE);
    if (!enabled) { setMapState(off); return; }
    if (!is2D) { setMapState({ ...off, state: "held", day, view }); return; }
    if (!day || !availability?.availableDays.includes(day)) { setMapState({ ...off, state: "error", day, view }); return; }
    const tileUrl = `/api/soil-moisture/tile?view=${view}&day=${day}&z={z}&x={x}&y={y}`;
    let active = true;
    setMapState({ state: "loading", loaded: 0, failed: 0, renderedAt: null, day, view });
    map.addSource(SOURCE, { type: "raster", tiles: [tileUrl], tileSize: 256, minzoom: 0, maxzoom: 6, bounds: [-102.1, 36.9, -94.5, 40.1], attribution: "NASA GIBS · SMAP SPL4SMAU V008" });
    map.addLayer({ id: LAYER, type: "raster", source: SOURCE, paint: { "raster-opacity": opacity, "raster-fade-duration": 0 } }, map.getLayer("external-census-counties-fill") ? "external-census-counties-fill" : undefined);
    const onData = (event: unknown) => {
      const e = event as { sourceId?: string; tile?: { state?: string }; coord?: unknown };
      if (!active || e.sourceId !== SOURCE || e.tile?.state !== "loaded" || !e.coord) return;
      setMapState(current => current.day === day && current.view === view ? { ...current, loaded: current.loaded + 1 } : current);
    };
    const onError = (event: unknown) => {
      const e = event as { sourceId?: string };
      if (!active || e.sourceId !== SOURCE) return;
      setMapState(current => current.day === day && current.view === view ? { ...current, failed: current.failed + 1, state: current.loaded ? "partial" : "error" } : current);
    };
    const onRender = () => {
      if (!active || !map.getLayer(LAYER)) return;
      setMapState(current => current.day === day && current.view === view && current.loaded > 0 && !current.renderedAt ? { ...current, state: current.failed ? "partial" : "rendered", renderedAt: new Date().toISOString() } : current);
    };
    map.on("sourcedata", onData);
    map.on("error", onError);
    map.on("render", onRender);
    return () => {
      active = false;
      map.off("sourcedata", onData);
      map.off("error", onError);
      map.off("render", onRender);
      if (map.getLayer(LAYER)) map.removeLayer(LAYER);
      if (map.getSource(SOURCE)) map.removeSource(SOURCE);
    };
  // Opacity is updated separately so moving the slider never reloads tiles.
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [enabled, day, view, availability, styleReady, is2D]);

  useEffect(() => {
    const map = mapRef.current;
    if (map?.getLayer(LAYER)) map.setPaintProperty(LAYER, "raster-opacity", opacity);
  }, [opacity, mapRef, styleReady]);

  const changeDay = (next: string) => { clearRaster(); setMapState({ ...off, state: "loading", day: next, view }); setDay(next); };
  const sourceText = checking ? "Checking NASA…" : availability?.state === "available" ? `Configured SPL4SMAU V008 · latest shared day ${availability.latestCommonDay} 12:00 UTC · NASA days checked ${availability.checkedAt ? new Date(availability.checkedAt).toLocaleString("en-US", { timeZone: "UTC" }) + " UTC" : "unknown"}` : availability?.state === "unavailable" ? "No day shared by all four NASA views in the last 30 days" : availability?.state === "error" ? "NASA availability check failed" : "Not checked";
  const backendText = checking ? "Request in progress" : availability?.backend ? `${availability.backend.state.toUpperCase()} · ${availability.backend.durationMs} ms · cache ${availability.backend.cache}${availability.backend.code ? ` · ${availability.backend.code}` : ""}` : "No request yet";
  const mapText = !enabled ? "Off · no NASA tiles requested" : !is2D ? "Held in 3D or globe view · 2D only" : `${mapState.state.toUpperCase()} · ${SOIL_VIEWS[view].label} · ${day || "no day"} 12:00 UTC · ${mapState.loaded} tiles loaded / ${mapState.failed} failed${mapState.renderedAt ? ` · last rendered ${new Date(mapState.renderedAt).toLocaleString("en-US", { timeZone: "UTC" })} UTC` : " · no confirmed render"}`;

  return <article className="official-context-row soil-moisture-control" data-state={mapState.state} data-visible={enabled}>
    <div className="official-context-primary"><label className="visibility-switch"><input type="checkbox" checked={enabled} aria-label="Show Soil moisture" onChange={event => { const next = event.target.checked; setEnabled(next); if (next) void checkAvailability(); }} /><span aria-hidden="true" /></label><i style={{ "--swatch": "#6dbb9d" } as React.CSSProperties} /><div><strong>Soil moisture</strong><small>NASA SMAP Level-4 · dated modeled visual context · {enabled ? mapState.state : "off"}</small></div></div>
    <div className="official-context-option-body">
      <div className="source-time-actions"><label>Depth<select value={depth} onChange={event => { clearRaster(); setDepth(event.target.value as "surface" | "root"); }}><option value="surface">Surface · 0–5 cm</option><option value="root">Root zone · 0–100 cm</option></select></label><label>View<select value={uncertainty ? "uncertainty" : "moisture"} onChange={event => { clearRaster(); setUncertainty(event.target.value === "uncertainty"); }}><option value="moisture">Moisture</option><option value="uncertainty">Uncertainty</option></select></label><label>UTC day<select aria-label="Soil moisture UTC day" value={day} disabled={!enabled || checking || !availability?.availableDays.length} onChange={event => changeDay(event.target.value)}><option value="">No available day</option>{availability?.availableDays.map(value => <option key={value} value={value}>{value}</option>)}</select></label><button type="button" disabled={!enabled || checking} onClick={() => void checkAvailability(true)}>Retry NASA check</button></div>
      <label className="opacity-control"><span>Opacity <b>{Math.round(opacity * 100)}%</b></span><input type="range" min="0" max="100" value={Math.round(opacity * 100)} aria-label="Soil moisture opacity" onChange={event => setOpacity(Number(event.target.value) / 100)} /></label>
      {enabled && <img src={soilLegendUrl(view)} alt={`NASA legend for ${SOIL_VIEWS[view].label}`} loading="lazy" style={{ maxWidth: "100%", background: "#eef3ed", borderRadius: 4 }} />}
      <div className="source-time-control" role="status" aria-live="polite"><p><strong>Source:</strong> {sourceText}</p><p><strong>Backend:</strong> {backendText}</p><p><strong>Map:</strong> {mapText}</p></div>
      <small>Daily 12:00 UTC modeled snapshots; approximate 9 km scale. Blank coverage or failed tiles cannot be read as dry, safe, or current. Color is visual context, not a numeric moisture reading. 2D only. External context only; no KFM EvidenceBundle or release.</small>
      <div className="source-time-actions"><a href={SOIL_METADATA_URL} target="_blank" rel="noreferrer">NASA layer metadata ↗</a><a href={SOIL_GUIDE_URL} target="_blank" rel="noreferrer">NSIDC product guide ↗</a></div>
    </div>
  </article>;
}
