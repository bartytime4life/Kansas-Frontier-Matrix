"use client";

import { useCallback, useEffect, useMemo, useRef, useState, type RefObject } from "react";
import type { Map as MapLibreMap, MapLayerMouseEvent, MapMouseEvent } from "./maplibre-seam";
import { readBoundedJson } from "./bounded-json";
import {
  AIRSPACE_COLORS, AIRSPACE_GROUPS, AVIATION_CONTEXT_ASSET, DRONE_RULE_COLORS, airportFeatures, airspaceColumn, airspaceFeatures, airwayFeatures,
  airwaysNearPoint, aviationEditionStatus, distanceKm, droneFeatures, droneVerdictAtPoint, nearestAirport, parseAviationContext,
  type AirspaceGroup, type AirwaySegment, type AviationContext,
} from "./aviation-airspace";
import {
  AVIATION_METAR_API_PATH, AVIATION_PIREP_API_PATH, FLIGHT_CATEGORY_COLORS, basicVfrCheck, metarFeatures, pirepAltitudeLabel, pirepFeatures,
  type AviationWeatherEnvelope, type MetarObservation, type PirepReport,
} from "./aviation-weather";
import { TFR_API_PATH, TFR_HOME, UASFM_API_PATH, UAS_CEILING_COLORS, uasCeilingAt, uasFeatures, type TfrEntry, type UasCell } from "./aviation-drone-data";

const PREFIX = "kfm-aviation";
const SOURCES = ["airspace", "drone", "uas", "airways", "runways", "airports", "metar", "ceilings", "pireps", "pick"].map(name => `${PREFIX}-${name}`);
const LAYERS = ["airspace-3d", "airspace-edge", "airspace-label", "drone-3d", "drone-edge", "uas-3d", "uas-label", "airways-line", "airways-label", "runways-line",
  "airports-dot", "airports-label", "metar-dot", "metar-label", "ceilings-3d", "pireps-3d", "pick-dot"].map(name => `${PREFIX}-${name}`);
const WEATHER_REFRESH_MS = 5 * 60_000;
const TFR_REFRESH_MS = 10 * 60_000;
const EXAGGERATIONS = [1, 3, 6] as const;

type LoadState = "idle" | "loading" | "ready" | "error";
type Picked = Readonly<{ lon: number; lat: number; label: string }>;
type WeatherState<T> = Readonly<{ state: LoadState; envelope: AviationWeatherEnvelope<T> | null; message: string }>;
type FeedState<T> = Readonly<{ state: LoadState; value: T | null }>;
type UasGrid = Readonly<{ retrievedAt: string; cells: readonly UasCell[] }>;
type TfrList = Readonly<{ retrievedAt: string; kansas: readonly TfrEntry[]; total: number }>;

/** Same-origin read of one aviation route; `check` rejects any shape the route did not promise. */
async function readFeed<T>(path: string, signal: AbortSignal, maxBytes: number, check: (value: Record<string, unknown>) => boolean): Promise<T> {
  const response = await fetch(path, { signal, cache: "no-store", credentials: "same-origin" });
  const value = await readBoundedJson(response, maxBytes, signal);
  if (!response.ok || !value || typeof value !== "object" || (value as { evidenceRole?: unknown }).evidenceRole !== "EXTERNAL_CONTEXT_ONLY" || !check(value as Record<string, unknown>)) throw new Error("unavailable");
  return value as T;
}

async function loadContext(signal: AbortSignal): Promise<AviationContext> {
  const response = await fetch(AVIATION_CONTEXT_ASSET.url, { signal, cache: "force-cache" });
  if (!response.ok) throw new Error("The aviation context file is unavailable.");
  const buffer = await response.arrayBuffer();
  if (buffer.byteLength > AVIATION_CONTEXT_ASSET.maxBytes) throw new Error("The aviation context exceeded its size bound.");
  const digest = Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", buffer)), byte => byte.toString(16).padStart(2, "0")).join("");
  if (digest !== AVIATION_CONTEXT_ASSET.sha256) throw new Error("The aviation context did not match its pinned digest.");
  return parseAviationContext(JSON.parse(new TextDecoder().decode(buffer)) as unknown);
}

function isEnvelope<T>(value: unknown): value is AviationWeatherEnvelope<T> {
  return Boolean(value) && typeof value === "object" && (value as { evidenceRole?: unknown }).evidenceRole === "EXTERNAL_CONTEXT_ONLY"
    && Array.isArray((value as { records?: unknown }).records) && typeof (value as { retrievedAt?: unknown }).retrievedAt === "string";
}

const minutesAgo = (iso: string, now: number) => Math.max(0, Math.round((now - Date.parse(iso)) / 60000));
const feet = (value: number) => Number.isFinite(value) ? `${Math.round(value).toLocaleString("en-US")} ft` : "—";

export function AviationControl({ mapRef, styleReady, onSelectionChange }: { mapRef: RefObject<MapLibreMap | null>; styleReady: boolean; onSelectionChange?: (selected: boolean) => void }) {
  const [visible, setVisible] = useState(false);
  const [contextState, setContextState] = useState<LoadState>("idle");
  const [context, setContext] = useState<AviationContext | null>(null);
  const [contextError, setContextError] = useState("");
  const [groups, setGroups] = useState<ReadonlySet<AirspaceGroup>>(() => new Set((Object.keys(AIRSPACE_GROUPS) as AirspaceGroup[]).filter(group => AIRSPACE_GROUPS[group].defaultOn)));
  const [showDrone, setShowDrone] = useState(true);
  const [showAirports, setShowAirports] = useState(true);
  const [airwayKinds, setAirwayKinds] = useState<ReadonlySet<AirwaySegment["type"]>>(() => new Set(["VICTOR", "RNAV_T"]));
  const [showMetar, setShowMetar] = useState(true);
  const [showCeilings, setShowCeilings] = useState(true);
  const [showPireps, setShowPireps] = useState(true);
  const [showUas, setShowUas] = useState(true);
  const [uas, setUas] = useState<FeedState<UasGrid>>({ state: "idle", value: null });
  const [tfrs, setTfrs] = useState<FeedState<TfrList>>({ state: "idle", value: null });
  const [exaggeration, setExaggeration] = useState<(typeof EXAGGERATIONS)[number]>(1);
  const [metar, setMetar] = useState<WeatherState<MetarObservation>>({ state: "idle", envelope: null, message: "" });
  const [pireps, setPireps] = useState<WeatherState<PirepReport>>({ state: "idle", envelope: null, message: "" });
  const [picking, setPicking] = useState(false);
  const [picked, setPicked] = useState<Picked | null>(null);
  const [render, setRender] = useState("Hidden");
  const [clock, setClock] = useState(() => Date.now());
  const contextRequest = useRef<AbortController | null>(null);

  useEffect(() => { onSelectionChange?.(visible); }, [visible, onSelectionChange]);
  useEffect(() => { const timer = setInterval(() => setClock(Date.now()), 60_000); return () => clearInterval(timer); }, []);

  // The pinned NASR product is loaded once, on first use, and verified before parsing.
  useEffect(() => {
    if (!visible || context || contextRequest.current) return;
    const abort = new AbortController();
    contextRequest.current = abort;
    setContextState("loading");
    loadContext(abort.signal).then(value => { setContext(value); setContextState("ready"); })
      .catch(error => { if (abort.signal.aborted) return; setContextError(error instanceof Error ? error.message : "Unavailable."); setContextState("error"); })
      .finally(() => { if (contextRequest.current === abort) contextRequest.current = null; });
  }, [visible, context]);
  useEffect(() => () => contextRequest.current?.abort(), []);

  const refreshWeather = useCallback(async (signal: AbortSignal) => {
    // Earlier observations stay drawn while a refresh is in flight; a failure clears them.
    const read = async <T,>(path: string, set: (value: WeatherState<T>) => void) => {
      try {
        const response = await fetch(path, { signal, cache: "no-store", credentials: "same-origin" });
        const value = await readBoundedJson(response, 4 * 1024 * 1024, signal);
        if (!response.ok || !isEnvelope<T>(value)) throw new Error("unavailable");
        set({ state: "ready", envelope: value, message: "" });
      } catch {
        if (!signal.aborted) set({ state: "error", envelope: null, message: "Unavailable. No cached or synthetic observations are shown." });
      }
    };
    await Promise.all([showMetar ? read<MetarObservation>(AVIATION_METAR_API_PATH, setMetar) : Promise.resolve(),
      showPireps ? read<PirepReport>(AVIATION_PIREP_API_PATH, setPireps) : Promise.resolve()]);
  }, [showMetar, showPireps]);

  useEffect(() => {
    if (!visible || (!showMetar && !showPireps)) return;
    const abort = new AbortController();
    const initial = setTimeout(() => void refreshWeather(abort.signal), 0);
    const interval = setInterval(() => void refreshWeather(abort.signal), WEATHER_REFRESH_MS);
    return () => { abort.abort(); clearTimeout(initial); clearInterval(interval); };
  }, [visible, showMetar, showPireps, refreshWeather]);

  // UAS Facility Map grids change on a 56-day FAA cycle: one read per session.
  useEffect(() => {
    if (!visible || !showUas || uas.state === "ready" || uas.state === "loading") return;
    const abort = new AbortController();
    const start = setTimeout(() => {
      setUas({ state: "loading", value: null });
      readFeed<UasGrid>(UASFM_API_PATH, abort.signal, 16 * 1024 * 1024, value => Array.isArray(value.cells))
        .then(value => setUas({ state: "ready", value })).catch(() => { if (!abort.signal.aborted) setUas({ state: "error", value: null }); });
    }, 0);
    return () => { clearTimeout(start); abort.abort(); };
  }, [visible, showUas, uas.state]);

  useEffect(() => {
    if (!visible) return;
    const abort = new AbortController();
    const load = () => readFeed<TfrList>(TFR_API_PATH, abort.signal, 1024 * 1024, value => Array.isArray(value.kansas))
      .then(value => setTfrs({ state: "ready", value })).catch(() => { if (!abort.signal.aborted) setTfrs({ state: "error", value: null }); });
    const initial = setTimeout(load, 0), interval = setInterval(load, TFR_REFRESH_MS);
    return () => { abort.abort(); clearTimeout(initial); clearInterval(interval); };
  }, [visible]);

  const uasCells = useMemo(() => uas.value?.cells ?? [], [uas.value]);
  const metarRecords = useMemo(() => showMetar ? metar.envelope?.records ?? [] : [], [showMetar, metar.envelope]);
  const pirepRecords = useMemo(() => showPireps ? pireps.envelope?.records ?? [] : [], [showPireps, pireps.envelope]);

  // Install every aviation source/layer together; any toggle rebuilds them from pure feature builders.
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !styleReady) return;
    const remove = () => {
      try {
        for (const id of [...LAYERS].reverse()) if (map.getLayer(id)) map.removeLayer(id);
        for (const id of SOURCES) if (map.getSource(id)) map.removeSource(id);
      } catch { /* Map teardown already removed its sources. */ }
    };
    remove();
    if (!visible || !context) return;
    try {
      const groundAt = (lon: number, lat: number) => nearestAirport(context.airports, lon, lat)?.airport.elevation_ft ?? 0;
      const airports = airportFeatures(context);
      const weatherLayers = metarFeatures(metarRecords, exaggeration);
      const add = (id: string, data: GeoJSON.FeatureCollection) => map.addSource(`${PREFIX}-${id}`, { type: "geojson", data });
      add("airspace", airspaceFeatures(context, groups, exaggeration));
      add("drone", showDrone ? droneFeatures(context, exaggeration) : { type: "FeatureCollection", features: [] });
      add("airways", airwayFeatures(context, airwayKinds));
      add("runways", showAirports ? airports.runways : { type: "FeatureCollection", features: [] });
      add("airports", showAirports ? airports.points : { type: "FeatureCollection", features: [] });
      add("metar", weatherLayers.stations);
      add("ceilings", showCeilings ? weatherLayers.ceilings : { type: "FeatureCollection", features: [] });
      add("pireps", pirepFeatures(pirepRecords, groundAt, exaggeration));
      add("uas", showUas ? uasFeatures(uasCells, exaggeration) : { type: "FeatureCollection", features: [] });
      add("pick", { type: "FeatureCollection", features: picked ? [{ type: "Feature", geometry: { type: "Point", coordinates: [picked.lon, picked.lat] }, properties: {} }] : [] });
      const font = ["Noto Sans Regular"];
      // Translucent shells: the "upside-down wedding cake" of Class B/C reads from the stacked bases and tops.
      map.addLayer({ id: `${PREFIX}-airspace-3d`, type: "fill-extrusion", source: `${PREFIX}-airspace`, paint: {
        "fill-extrusion-color": ["get", "color"], "fill-extrusion-base": ["get", "base"], "fill-extrusion-height": ["get", "top"], "fill-extrusion-opacity": 0.28 } });
      map.addLayer({ id: `${PREFIX}-airspace-edge`, type: "line", source: `${PREFIX}-airspace`, paint: {
        "line-color": ["get", "color"], "line-width": ["match", ["get", "type"], ["CLASS_B", "CLASS_C", "RESTRICTED", "PROHIBITED"], 2.2, 1.3],
        "line-dasharray": ["match", ["get", "type"], ["CLASS_D", "CLASS_E2", "CLASS_E3", "CLASS_E4"], ["literal", [3, 2]], ["literal", [1, 0]]] } });
      map.addLayer({ id: `${PREFIX}-airspace-label`, type: "symbol", source: `${PREFIX}-airspace`, minzoom: 7.5, layout: {
        "text-font": font, "text-field": ["get", "label"], "text-size": 10.5, "text-optional": true, "symbol-placement": "line", "text-max-angle": 30, "symbol-spacing": 420 },
        paint: { "text-color": ["get", "color"], "text-halo-color": "#ffffff", "text-halo-width": 1.4 } });
      map.addLayer({ id: `${PREFIX}-drone-3d`, type: "fill-extrusion", source: `${PREFIX}-drone`, paint: {
        "fill-extrusion-color": ["get", "color"], "fill-extrusion-base": ["get", "base"], "fill-extrusion-height": ["get", "top"], "fill-extrusion-opacity": 0.45 } });
      map.addLayer({ id: `${PREFIX}-drone-edge`, type: "line", source: `${PREFIX}-drone`, paint: { "line-color": ["get", "color"], "line-width": 1.5, "line-opacity": 0.9 } });
      // LAANC grid: each cell rises to the altitude the FAA lets LAANC approve there.
      map.addLayer({ id: `${PREFIX}-uas-3d`, type: "fill-extrusion", source: `${PREFIX}-uas`, minzoom: 8, paint: {
        "fill-extrusion-color": ["get", "color"], "fill-extrusion-base": ["get", "base"], "fill-extrusion-height": ["get", "top"], "fill-extrusion-opacity": 0.5 } });
      map.addLayer({ id: `${PREFIX}-uas-label`, type: "symbol", source: `${PREFIX}-uas`, minzoom: 11.5, layout: {
        "text-font": font, "text-field": ["get", "label"], "text-size": 9.5, "text-optional": true },
        paint: { "text-color": "#1d2f44", "text-halo-color": "#ffffff", "text-halo-width": 1.2 } });
      map.addLayer({ id: `${PREFIX}-airways-line`, type: "line", source: `${PREFIX}-airways`, paint: {
        "line-color": ["case", ["get", "high"], "#5d6d7e", "#2e6f95"], "line-width": 1.2, "line-opacity": 0.75, "line-dasharray": ["literal", [6, 3]] } });
      map.addLayer({ id: `${PREFIX}-airways-label`, type: "symbol", source: `${PREFIX}-airways`, minzoom: 7, layout: {
        "text-font": font, "text-field": ["get", "label"], "text-size": 9.5, "symbol-placement": "line-center", "text-optional": true },
        paint: { "text-color": "#24506b", "text-halo-color": "#ffffff", "text-halo-width": 1.2 } });
      map.addLayer({ id: `${PREFIX}-runways-line`, type: "line", source: `${PREFIX}-runways`, minzoom: 10, paint: { "line-color": "#2b2b2b",
        "line-width": ["interpolate", ["exponential", 2], ["zoom"], 10, 1.5, 16, ["*", ["get", "width_ft"], 0.08]] } });
      map.addLayer({ id: `${PREFIX}-airports-dot`, type: "circle", source: `${PREFIX}-airports`, paint: {
        "circle-radius": ["interpolate", ["linear"], ["zoom"], 5, 3, 10, 6], "circle-color": ["case", ["get", "towered"], "#1f5fbf", "#b5338a"],
        "circle-stroke-color": "#ffffff", "circle-stroke-width": 1.5 } });
      map.addLayer({ id: `${PREFIX}-airports-label`, type: "symbol", source: `${PREFIX}-airports`, minzoom: 8, layout: {
        "text-font": font, "text-field": ["get", "label"], "text-size": 10.5, "text-offset": [0, 1.2], "text-anchor": "top", "text-optional": true },
        paint: { "text-color": "#1d2f44", "text-halo-color": "#ffffff", "text-halo-width": 1.3 } });
      map.addLayer({ id: `${PREFIX}-ceilings-3d`, type: "fill-extrusion", source: `${PREFIX}-ceilings`, paint: {
        "fill-extrusion-color": ["get", "color"], "fill-extrusion-base": ["get", "base"], "fill-extrusion-height": ["get", "top"], "fill-extrusion-opacity": 0.55 } });
      map.addLayer({ id: `${PREFIX}-pireps-3d`, type: "fill-extrusion", source: `${PREFIX}-pireps`, paint: {
        "fill-extrusion-color": ["get", "color"], "fill-extrusion-base": ["get", "base"], "fill-extrusion-height": ["get", "top"], "fill-extrusion-opacity": 0.85 } });
      map.addLayer({ id: `${PREFIX}-metar-dot`, type: "circle", source: `${PREFIX}-metar`, paint: {
        "circle-radius": 6, "circle-color": ["get", "color"], "circle-stroke-color": "#ffffff", "circle-stroke-width": 2 } });
      map.addLayer({ id: `${PREFIX}-metar-label`, type: "symbol", source: `${PREFIX}-metar`, minzoom: 7, layout: {
        "text-font": font, "text-field": ["get", "label"], "text-size": 10, "text-offset": [0, -1.3], "text-anchor": "bottom", "text-optional": true },
        paint: { "text-color": "#1d2f44", "text-halo-color": "#ffffff", "text-halo-width": 1.3 } });
      map.addLayer({ id: `${PREFIX}-pick-dot`, type: "circle", source: `${PREFIX}-pick`, paint: {
        "circle-radius": 7, "circle-color": "rgba(0,0,0,0)", "circle-stroke-color": "#111111", "circle-stroke-width": 2.5 } });
      const choose = (event: MapLayerMouseEvent) => {
        const id = event.features?.[0]?.properties?.faa_id;
        const airport = context.airports.find(item => item.faa_id === id);
        if (airport) setPicked({ lon: airport.lon, lat: airport.lat, label: `${airport.name} (${airport.icao_id ?? airport.faa_id})` });
      };
      const rendered = () => setRender("Map frame drawn");
      map.on("click", `${PREFIX}-airports-dot`, choose);
      map.once("idle", rendered);
      return () => { map.off("click", `${PREFIX}-airports-dot`, choose); map.off("idle", rendered); remove(); };
    } catch {
      // The external renderer failed during source installation; surface that failure immediately.
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setRender("Map rendering unavailable"); remove();
    }
  }, [mapRef, styleReady, visible, context, groups, showDrone, showAirports, airwayKinds, showCeilings, metarRecords, pirepRecords, exaggeration, picked, showUas, uasCells]);

  // Point inspection is opt-in so the page's own click tools keep working.
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !picking) return;
    const clicked = (event: MapMouseEvent) => { setPicked({ lon: event.lngLat.lng, lat: event.lngLat.lat, label: `${event.lngLat.lat.toFixed(4)}, ${event.lngLat.lng.toFixed(4)}` }); setPicking(false); };
    map.getCanvas().style.cursor = "crosshair";
    map.once("click", clicked);
    return () => { map.off("click", clicked); map.getCanvas().style.cursor = ""; };
  }, [mapRef, picking]);

  const edition = context ? aviationEditionStatus(context, clock) : null;
  const shownRender = !visible ? "Hidden" : !context ? contextState === "error" ? "Unavailable" : "Loading" : !styleReady ? "Not ready" : render;
  const inspection = useMemo(() => {
    if (!context || !picked) return null;
    const near = nearestAirport(context.airports, picked.lon, picked.lat);
    const groundFt = near?.airport.elevation_ft ?? 0;
    const column = airspaceColumn(context, picked.lon, picked.lat, groundFt);
    const drone = droneVerdictAtPoint(context, picked.lon, picked.lat);
    const station = metarRecords.map(record => ({ record, km: distanceKm(picked.lon, picked.lat, record.lon, record.lat) })).sort((a, b) => a.km - b.km)[0];
    const usable = station && station.km <= 50 ? station : null;
    const surface = column.find(band => band.floorFtAgl === 0 && band.airspaceClass !== "SUA");
    const surfaceClass = surface && surface.airspaceClass !== "A" ? surface.airspaceClass : "G";
    const vfr = basicVfrCheck(surfaceClass as "B" | "C" | "D" | "E" | "G", usable?.record ?? null);
    const routes = [...new Map(airwaysNearPoint(context, picked.lon, picked.lat).map(segment => [segment.designation, segment])).values()];
    const reports = pirepRecords.filter(report => distanceKm(picked.lon, picked.lat, report.lon, report.lat) <= 60);
    const laanc = uasCeilingAt(uasCells, picked.lon, picked.lat);
    return { near, groundFt, column, drone, station: usable, vfr, routes, reports, laanc };
  }, [context, picked, metarRecords, pirepRecords, uasCells]);

  const toggleGroup = (group: AirspaceGroup, on: boolean) => setGroups(current => { const next = new Set(current); if (on) next.add(group); else next.delete(group); return next; });
  const toggleAirway = (kinds: AirwaySegment["type"][], on: boolean) => setAirwayKinds(current => { const next = new Set(current); for (const kind of kinds) { if (on) next.add(kind); else next.delete(kind); } return next; });
  const tilt = () => mapRef.current?.easeTo({ pitch: 62, bearing: mapRef.current.getBearing() || -18, duration: 900 });

  return <section className="official-context-row" aria-label="Airspace, airports and aviation weather">
    <div className="official-context-primary"><label className="visibility-switch"><input type="checkbox" checked={visible} aria-label={visible ? "Hide airspace and aviation layers" : "Show airspace and aviation layers"} onChange={event => { setVisible(event.target.checked); if (event.target.checked) setRender("Waiting for map frame"); }} /><span aria-hidden="true" /></label><i style={{ "--swatch": AIRSPACE_COLORS.CLASS_C } as React.CSSProperties} /><div><strong>Airspace, airports &amp; aviation weather</strong><small>FAA NASR · NOAA AWC · {visible ? shownRender : "Off"}</small></div></div>
    <details className="specialty-layer-details"><summary>Airspace shells, drone zones, weather &amp; controls</summary><div className="official-context-option-body">
      <p><strong>Not for navigation, flight planning or drone authorization.</strong> Check current FAA charts, NOTAMs and TFRs, and use B4UFLY / LAANC before flying. Temporary flight restrictions are not shown.</p>
      {contextState === "loading" && <p role="status">Loading the pinned FAA NASR airspace product…</p>}
      {contextState === "error" && <p role="status">Airspace context unavailable: {contextError} Nothing is drawn in its place.</p>}
      {edition && <p role="status" data-edition={edition.state}><strong>{edition.state === "CURRENT" ? "Current edition" : edition.state === "PREVIEW" ? "Preview edition" : "Expired edition"}:</strong> {edition.text}</p>}
      {context && <>
        <fieldset><legend>Airspace volumes (3D)</legend>
          {(Object.keys(AIRSPACE_GROUPS) as AirspaceGroup[]).map(group => <label key={group}><input type="checkbox" checked={groups.has(group)} onChange={event => toggleGroup(group, event.target.checked)} /> {AIRSPACE_GROUPS[group].title}</label>)}
          <label>Vertical exaggeration<select value={exaggeration} onChange={event => setExaggeration(Number(event.target.value) as (typeof EXAGGERATIONS)[number])}>{EXAGGERATIONS.map(value => <option key={value} value={value}>{value}×{value === 1 ? " (true scale)" : ""}</option>)}</select></label>
          <button type="button" onClick={tilt}>Tilt map to see shells in 3D</button>
        </fieldset>
        <fieldset><legend>Drones (small UAS), surface to 400 ft AGL</legend>
          <label><input type="checkbox" checked={showDrone} onChange={event => setShowDrone(event.target.checked)} /> Show drone rule slabs</label>
          <ul className="aviation-legend">
            <li><i style={{ background: DRONE_RULE_COLORS.NO_FLY_WITHOUT_PERMISSION }} /> No flight without the using agency&apos;s permission (restricted/prohibited) · 14 CFR 107.45</li>
            <li><i style={{ background: DRONE_RULE_COLORS.ATC_AUTHORIZATION_REQUIRED }} /> FAA/ATC authorization required (LAANC/DroneZone) · 14 CFR 107.41</li>
            <li><i style={{ background: DRONE_RULE_COLORS.CAUTION }} /> Caution: MOA or alert area reaching low altitude</li>
            <li><i style={{ background: DRONE_RULE_COLORS.ABOVE_DRONE_CEILING }} /> Unshaded = Class G: up to 400 ft AGL without ATC authorization · 14 CFR 107.51(b)</li>
          </ul>
          <label><input type="checkbox" checked={showUas} onChange={event => setShowUas(event.target.checked)} /> FAA UAS Facility Map: LAANC ceiling per grid cell (zoom in)</label>
          <ul className="aviation-legend">{UAS_CEILING_COLORS.map(([value, color]) => <li key={value}><i style={{ background: color }} /> {value} ft AGL{value === 0 ? " (no LAANC approval; use DroneZone)" : ""}</li>)}</ul>
          {showUas && <small role="status">UAS Facility Map: {uas.state === "ready" && uas.value ? `${uas.value.cells.length.toLocaleString("en-US")} grid cells` : uas.state === "error" ? "Unavailable. No partial grid is drawn." : "Loading…"}</small>}
          <p><strong>Temporary flight restrictions:</strong> {tfrs.state === "ready" && tfrs.value ? tfrs.value.kansas.length ? `${tfrs.value.kansas.length} Kansas-related of ${tfrs.value.total} active nationwide.` : `None matched Kansas among ${tfrs.value.total} active nationwide.` : tfrs.state === "error" ? "FAA TFR list unavailable." : "Checking…"} <a href={TFR_HOME} target="_blank" rel="noreferrer">Check tfr.faa.gov</a></p>
          {tfrs.value && tfrs.value.kansas.length > 0 && <ul>{tfrs.value.kansas.slice(0, 20).map(entry => <li key={entry.notam}><strong>{entry.notam}</strong>{entry.type ? ` · ${entry.type}` : ""}: {entry.description}</li>)}</ul>}
        </fieldset>
        <fieldset><legend>Airports &amp; air traffic structure</legend>
          <label><input type="checkbox" checked={showAirports} onChange={event => setShowAirports(event.target.checked)} /> Public-use airports and runways ({context.airports.length}; {context.privateUseWithheld} private-use facilities withheld)</label>
          <label><input type="checkbox" checked={airwayKinds.has("VICTOR")} onChange={event => toggleAirway(["VICTOR", "RNAV_T"], event.target.checked)} /> Low airways (Victor, T routes) · 1,200 AGL–below FL180</label>
          <label><input type="checkbox" checked={airwayKinds.has("JET")} onChange={event => toggleAirway(["JET", "RNAV_Q"], event.target.checked)} /> High routes (Jet, Q routes) · FL180–FL450</label>
          <small>Live aircraft positions are not shown: no surveillance feed is licensed for public display (see the aviation intake runbook). Pilot reports below are the observed traffic signal.</small>
        </fieldset>
        <fieldset><legend>Airport weather &amp; pilot reports (live)</legend>
          <label><input type="checkbox" checked={showMetar} onChange={event => setShowMetar(event.target.checked)} /> METAR stations (ASOS/AWOS) by flight category</label>
          <label><input type="checkbox" checked={showCeilings} disabled={!showMetar} onChange={event => setShowCeilings(event.target.checked)} /> Cloud ceilings as discs at reported height</label>
          <label><input type="checkbox" checked={showPireps} onChange={event => setShowPireps(event.target.checked)} /> Pilot reports (PIREP) at reported altitude</label>
          {showPireps && <small>Climb/descent and unknown altitudes remain in the point inspector; no height is drawn for them.</small>}
          <ul className="aviation-legend">{(Object.keys(FLIGHT_CATEGORY_COLORS) as (keyof typeof FLIGHT_CATEGORY_COLORS)[]).map(category => <li key={category}><i style={{ background: FLIGHT_CATEGORY_COLORS[category] }} /> {category}</li>)}</ul>
          {showMetar && <small role="status">METAR: {metar.state === "ready" && metar.envelope ? `${metar.envelope.records.length} stations · retrieved ${minutesAgo(metar.envelope.retrievedAt, clock)} min ago` : metar.state === "error" ? metar.message : "Checking…"}</small>}
          {showPireps && <small role="status">PIREP: {pireps.state === "ready" && pireps.envelope ? `${pireps.envelope.records.length} reports in 3 h${pireps.envelope.records.some(report => report.urgent) ? " · includes URGENT" : ""}` : pireps.state === "error" ? pireps.message : "Checking…"}</small>}
          <small>NOAA/NWS Aviation Weather Center. Observations describe each station site; an absent report is not evidence of good weather or no traffic.</small>
        </fieldset>
        <fieldset><legend>What can fly here, at each height</legend>
          <button type="button" aria-pressed={picking} onClick={() => setPicking(value => !value)}>{picking ? "Click the map… (press again to cancel)" : "Pick a point on the map"}</button>
          <small>Or click an airport dot.</small>
          {inspection && picked && <div className="aviation-column">
            <p><strong>{picked.label}</strong> · ground reference {feet(inspection.groundFt)} MSL{inspection.near ? ` (${inspection.near.airport.faa_id}, ${inspection.near.km.toFixed(1)} km)` : ""}</p>
            <p style={{ borderLeft: `4px solid ${DRONE_RULE_COLORS[inspection.drone.rule.code]}`, paddingLeft: 8 }}><strong>Drone, SFC–400 ft AGL:</strong> {inspection.drone.rule.title}. {inspection.drone.rule.detail} <small>({inspection.drone.governing} · {inspection.drone.rule.cite})</small></p>
            {inspection.laanc && <p><strong>LAANC ceiling here:</strong> {inspection.laanc.ceilingFt} ft AGL{inspection.laanc.airport ? ` (${inspection.laanc.airportName ?? inspection.laanc.airport} grid)` : ""}. {inspection.laanc.ceilingFt === 0 ? "LAANC cannot approve flight in this cell; request a DroneZone authorization." : "LAANC can approve up to this altitude; it is not approval by itself."} <small>(FAA UAS Facility Map)</small></p>}
            {tfrs.value && tfrs.value.kansas.length > 0 && <p><strong>Check TFRs:</strong> {tfrs.value.kansas.length} Kansas-related temporary flight restriction(s) are active; their boundaries are not drawn here.</p>}
            <table><thead><tr><th scope="col">Band</th><th scope="col">Floor → ceiling</th><th scope="col">≈ above ground</th><th scope="col">Who can fly, and how</th></tr></thead>
              <tbody>{[...inspection.column].reverse().map(band => <tr key={band.key}><th scope="row">{band.label}</th><td>{band.floorText} → {band.ceilingText}</td>
                <td>{feet(band.floorFtAgl)} → {feet(band.ceilingFtAgl)}</td><td>{band.manned} <small>({band.cite})</small></td></tr>)}</tbody></table>
            <p><strong>Weather now:</strong> {inspection.station ? <>{inspection.station.record.raw} <small>({inspection.station.km.toFixed(0)} km away, {minutesAgo(inspection.station.record.observedAt, clock)} min old{inspection.station.record.densityAltitudeFt !== null ? `, density altitude ≈ ${feet(inspection.station.record.densityAltitudeFt)}` : ""})</small></> : "No METAR station within 50 km."} {inspection.vfr.text} <small>({inspection.vfr.cite})</small></p>
            {inspection.routes.length > 0 && <p><strong>Airways within 4 NM:</strong> {inspection.routes.map(route => `${route.designation}${route.mea_ft ? ` (MEA ${route.mea_ft.toLocaleString("en-US")})` : ""}`).join(", ")}</p>}
            {inspection.reports.length > 0 && <p><strong>Pilot reports within 60 km (3 h):</strong> {inspection.reports.slice(0, 5).map(report => `${report.raw} (${pirepAltitudeLabel(report)})`).join(" · ")}</p>}
          </div>}
        </fieldset>
        <details><summary>Source, edition &amp; limits</summary>
          <dl><dt>Airspace, airports, airways</dt><dd>FAA NASR cycle {context.nasrCycle} (valid {context.validFrom} to {context.validToExclusive}, exclusive) · product <code>{context.productId.slice(0, 19)}…</code></dd>
            <dt>Weather</dt><dd><a href="https://aviationweather.gov/data/api/" target="_blank" rel="noreferrer">NOAA/NWS Aviation Weather Center Data API</a></dd>
            <dt>Drone grid and TFRs</dt><dd>FAA UAS Facility Maps; FAA TFR list (<a href={TFR_HOME} target="_blank" rel="noreferrer">tfr.faa.gov</a>)</dd>
            <dt>Evidence role</dt><dd>External display context only; not a KFM-released record.</dd></dl>
          <ul>{context.limitations.map(item => <li key={item}>{item}</li>)}</ul>
        </details>
      </>}
    </div></details>
  </section>;
}
