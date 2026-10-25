"use client";

import { useCallback, useEffect, useMemo, useRef, useState, type RefObject } from "react";
import type { Map as MapLibreMap, MapLayerMouseEvent, MapMouseEvent } from "./maplibre-seam";
import { readBoundedJson } from "./bounded-json";
import { aviationResearchPoints } from "./aviation-research";
import type { ResearchRecord } from "./research-context";
import { unexaggeratedTerrainElevation } from "./map-runtime";
import { PROFILE_TOP_FT, alongTrackNm, profileBands, profilePath, profileSummary, type ProfileBand, type ProfilePoint, type ProfileVolume } from "./aviation-profile";
import { ALL_ALTITUDES, SLICE_MSL_FEET, SLICE_POINT_TOLERANCE_FT, sliceCollection, sliceTitle, type AltitudeSlice, type AviationView } from "./aviation-chart";
import {
  AIRSPACE_COLORS, AIRSPACE_GROUPS, AVIATION_CONTEXT_ASSET, airspaceLabel, DRONE_RULE_COLORS, airportFeatures, airspaceColumn, airspaceFeatures, airwayFeatures,
  airwaysNearPoint, aviationEditionStatus, distanceKm, droneFeatures, droneVerdictAtPoint, groundAnchors, nearestAirport, pointGroundReference, occupiedAirspace, parseAviationContext,
  type AirspaceGroup, type AirwaySegment, type AviationContext,
} from "./aviation-airspace";
import {
  AVIATION_METAR_API_PATH, AVIATION_PIREP_API_PATH, FLIGHT_CATEGORY_COLORS, basicVfrCheck, metarFeatures, pirepAltitudeLabel, pirepFeatures,
  type AviationWeatherEnvelope, type MetarObservation, type PirepReport,
} from "./aviation-weather";
import { AVIATION_TRAFFIC_API_PATH, TRAFFIC_ALTITUDE_COLORS, aircraftAltitudeMsl, freshAircraft, trafficFeatures, type TrafficEnvelope } from "./aviation-traffic";
import { TFR_API_PATH, TFR_COLOR, TFR_HOME, UASFM_API_PATH, UAS_CEILING_COLORS, formatTfrLimit, tfrFeatures, tfrsAtPoint, uasCeilingAt, uasFeatures, type TfrEntry, type TfrShape, type UasCell } from "./aviation-drone-data";

const PREFIX = "kfm-aviation";
const SOURCES = ["airspace", "drone", "uas", "airways", "runways", "airports", "metar", "ceilings", "pireps", "tfr", "traffic", "profile", "pick"].map(name => `${PREFIX}-${name}`);
const LAYERS = ["airspace-3d", "airspace-edge", "airspace-label", "drone-3d", "drone-edge", "uas-3d", "uas-label", "airways-line", "airways-label", "runways-line",
  "airports-dot", "airports-label", "metar-dot", "metar-label", "ceilings-3d", "pireps-3d", "tfr-3d", "tfr-edge", "tfr-label", "traffic-3d", "traffic-label", "profile-line", "profile-label", "pick-dot"].map(name => `${PREFIX}-${name}`);
const WEATHER_REFRESH_MS = 5 * 60_000;
const TRAFFIC_REFRESH_MS = 20_000;
const TRAFFIC_EXPIRY_TICK_MS = 5_000;
const TFR_REFRESH_MS = 10 * 60_000;
const EXAGGERATIONS = [1, 3, 6] as const;

type LoadState = "idle" | "loading" | "ready" | "error";
type Picked = Readonly<{ lon: number; lat: number; label: string; terrainFt: number | null }>;
type WeatherState<T> = Readonly<{ state: LoadState; envelope: AviationWeatherEnvelope<T> | null; message: string }>;
type FeedState<T> = Readonly<{ state: LoadState; value: T | null }>;
type UasGrid = Readonly<{ retrievedAt: string; cells: readonly UasCell[] }>;
type TfrList = Readonly<{ retrievedAt: string; kansas: readonly TfrEntry[]; total: number; shapes: readonly TfrShape[]; detailsChecked: number; detailsFailed: number }>;

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

// Ground from DEM tiles the viewer already loaded for 3D terrain (opt-in); never a new terrain request. Feet MSL, or null.
const terrainFtAt = (map: MapLibreMap, lon: number, lat: number): number | null => {
  try { const metres = unexaggeratedTerrainElevation(map, [lon, lat]); return metres === null ? null : metres / 0.3048; } catch { return null; }
};
const minutesAgo = (iso: string, now: number) => Math.max(0, Math.round((now - Date.parse(iso)) / 60000));
const feet = (value: number) => Number.isFinite(value) ? `${Math.round(value).toLocaleString("en-US")} ft` : "—";

type SideView = Readonly<{ a: Readonly<{ lon: number; lat: number }>; b: Readonly<{ lon: number; lat: number }>; points: readonly ProfilePoint[]; terrainShare: number }>;
type ProfileAircraft = Readonly<{ hex: string; distanceNm: number; altitudeFt: number; label: string; emergency: boolean }>;

// Limits in feet MSL over a ground elevation; FL is pressure altitude, drawn as MSL like the 3D view.
const mslOf = (reference: string, valueFt: number, groundFt: number) => reference === "SFC" ? groundFt : reference === "AGL" ? groundFt + valueFt
  : reference === "UNL" ? 60000 : valueFt;

/** The side view: distance A→B across, feet MSL up; ground, the 400 ft drone ceiling, every volume crossed, and nearby aircraft. */
function ProfileChart({ points, bands, aircraft }: Readonly<{ points: readonly ProfilePoint[]; bands: readonly ProfileBand[]; aircraft: readonly ProfileAircraft[] }>) {
  const width = 640, height = 300, left = 52, right = 12, top = 12, bottom = 34;
  const totalNm = points[points.length - 1].distanceNm;
  const x = (nm: number) => left + (nm / totalNm) * (width - left - right);
  const y = (ft: number) => top + (1 - Math.min(PROFILE_TOP_FT, Math.max(0, ft)) / PROFILE_TOP_FT) * (height - top - bottom);
  const line = (values: readonly (readonly [number, number])[]) => values.map(([nm, ft], index) => `${index ? "L" : "M"}${x(nm).toFixed(1)},${y(ft).toFixed(1)}`).join("");
  const ground = points.map(point => [point.distanceNm, point.groundFt] as const);
  const altitudeTicks = [0, 2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000];
  const distanceStep = totalNm > 120 ? 40 : totalNm > 60 ? 20 : totalNm > 20 ? 10 : 2;
  return <svg viewBox={`0 0 ${width} ${height}`} width="100%" role="img" aria-label={`Side view from A to B, ${totalNm.toFixed(1)} nautical miles, altitude in feet MSL`} style={{ background: "#f7fafc", border: "1px solid #ccd6e0" }}>
    <rect x={left} y={y(PROFILE_TOP_FT)} width={width - left - right} height={y(18000) - y(PROFILE_TOP_FT)} fill="#d9dee5" />
    <text x={left + 4} y={y(18000) - 4} fontSize="10" fill="#4a5563">Class A from FL180 (whole region)</text>
    {altitudeTicks.map(ft => <g key={ft}><line x1={left} x2={width - right} y1={y(ft)} y2={y(ft)} stroke="#e3e8ee" /><text x={left - 4} y={y(ft) + 3} fontSize="9" textAnchor="end" fill="#4a5563">{ft === 0 ? "0" : `${ft / 1000}k`}</text></g>)}
    {Array.from({ length: Math.floor(totalNm / distanceStep) + 1 }, (_, index) => index * distanceStep).map(nm => <text key={nm} x={x(nm)} y={height - bottom + 13} fontSize="9" textAnchor="middle" fill="#4a5563">{nm}</text>)}
    <text x={(left + width - right) / 2} y={height - 4} fontSize="10" textAnchor="middle" fill="#1d2f44">nautical miles from A · feet MSL</text>
    {bands.flatMap(band => band.segments.map((segment, index) => {
      const span = points.slice(segment.from, segment.to + 1);
      const outline = [...span.map((point, i) => [point.distanceNm, segment.high[i]] as const), ...[...span].reverse().map((point, i) => [point.distanceNm, segment.low[segment.low.length - 1 - i]] as const)];
      const mid = span[Math.floor(span.length / 2)], midIndex = Math.floor(span.length / 2);
      return <g key={`${band.key}:${index}`}><path d={`${line(outline)}Z`} fill={band.color} fillOpacity={band.kind === "tfr" ? 0.35 : 0.18} stroke={band.color} strokeWidth={band.kind === "tfr" ? 2 : 1.2} strokeDasharray={band.kind === "tfr" ? "5 3" : undefined} />
        {x(span[span.length - 1].distanceNm) - x(span[0].distanceNm) > 60 && <text x={x(mid.distanceNm)} y={Math.max(top + 10, y(segment.high[midIndex]) + 11)} fontSize="9.5" textAnchor="middle" fill="#1d2f44">{band.label.split(" · ").slice(0, 2).join(" · ")}</text>}</g>;
    }))}
    <path d={`${line(ground)}L${x(totalNm)},${y(0)}L${x(0)},${y(0)}Z`} fill="#b59a72" fillOpacity={0.85} />
    <path d={line(points.map(point => [point.distanceNm, point.groundFt + 400] as const))} fill="none" stroke="#2f8f4e" strokeWidth={1.4} strokeDasharray="4 3" />
    <text x={width - right - 4} y={y(points[points.length - 1].groundFt + 400) - 4} fontSize="9" textAnchor="end" fill="#2f8f4e">drone ceiling 400 ft AGL</text>
    {aircraft.map(plane => <g key={plane.hex}><circle cx={x(plane.distanceNm)} cy={y(plane.altitudeFt)} r={3.5} fill={plane.emergency ? "#e0301e" : "#1d2f44"} /><text x={x(plane.distanceNm) + 5} y={y(plane.altitudeFt) - 4} fontSize="9" fill="#1d2f44">{plane.label}</text></g>)}
    <text x={x(0)} y={top + 10} fontSize="11" fontWeight="bold" fill="#111">A</text><text x={x(totalNm) - 9} y={top + 10} fontSize="11" fontWeight="bold" fill="#111">B</text>
  </svg>;
}

export function AviationControl({ mapRef, styleReady, onSelectionChange, onResearchRecords, inspectRequest }: { mapRef: RefObject<MapLibreMap | null>; styleReady: boolean; onSelectionChange?: (selected: boolean) => void;
  /** Points this layer offers the "Near here" dossier while shown; null while hidden or loading. */
  onResearchRecords?: (records: readonly ResearchRecord[] | null) => void;
  /** A dossier "Inspect" on an aviation record: open this layer's point inspector there (a new nonce each time). */
  inspectRequest?: Readonly<{ lon: number; lat: number; label: string; nonce: number }> | null }) {
  const [visible, setVisible] = useState(false);
  const [contextState, setContextState] = useState<LoadState>("idle");
  const [context, setContext] = useState<AviationContext | null>(null);
  const [contextError, setContextError] = useState("");
  const [groups, setGroups] = useState<ReadonlySet<AirspaceGroup>>(() => new Set((Object.keys(AIRSPACE_GROUPS) as AirspaceGroup[]).filter(group => AIRSPACE_GROUPS[group].defaultOn)));
  const [showDrone, setShowDrone] = useState(true);
  const [showAirports, setShowAirports] = useState(true);
  const [showPrivate, setShowPrivate] = useState(true);
  const [airwayKinds, setAirwayKinds] = useState<ReadonlySet<AirwaySegment["type"]>>(() => new Set(["VICTOR", "RNAV_T"]));
  const [showMetar, setShowMetar] = useState(true);
  const [showCeilings, setShowCeilings] = useState(true);
  const [showPireps, setShowPireps] = useState(true);
  const [showUas, setShowUas] = useState(true);
  const [showTraffic, setShowTraffic] = useState(true);
  const [traffic, setTraffic] = useState<FeedState<TrafficEnvelope & { receivedAt: number }>>({ state: "idle", value: null });
  const [trafficNow, setTrafficNow] = useState(() => Date.now());
  const [uas, setUas] = useState<FeedState<UasGrid>>({ state: "idle", value: null });
  const [tfrs, setTfrs] = useState<FeedState<TfrList>>({ state: "idle", value: null });
  const [exaggeration, setExaggeration] = useState<(typeof EXAGGERATIONS)[number]>(1);
  const [view, setView] = useState<AviationView>("3d");
  const [slice, setSlice] = useState<AltitudeSlice>(ALL_ALTITUDES);
  const [metar, setMetar] = useState<WeatherState<MetarObservation>>({ state: "idle", envelope: null, message: "" });
  const [pireps, setPireps] = useState<WeatherState<PirepReport>>({ state: "idle", envelope: null, message: "" });
  const [picking, setPicking] = useState(false);
  const [sideStep, setSideStep] = useState<"a" | "b" | null>(null);
  const [sideA, setSideA] = useState<Readonly<{ lon: number; lat: number }> | null>(null);
  const [side, setSide] = useState<SideView | null>(null);
  const [picked, setPicked] = useState<Picked | null>(null);
  const [render, setRender] = useState("Hidden");
  const [clock, setClock] = useState(() => Date.now());
  const contextRequest = useRef<AbortController | null>(null);
  const uasLoaded = useRef(false);

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

  // UAS Facility Map grids change on a 56-day FAA cycle: one successful read per session.
  // The request is keyed to visibility only; its own loading state must not cancel it.
  // Hiding and re-showing the layer retries after a cancelled or failed read.
  useEffect(() => {
    if (!visible || !showUas || uasLoaded.current) return;
    const abort = new AbortController();
    const start = setTimeout(() => {
      setUas({ state: "loading", value: null });
      readFeed<UasGrid>(UASFM_API_PATH, abort.signal, 16 * 1024 * 1024, value => Array.isArray(value.cells))
        .then(value => { uasLoaded.current = true; setUas({ state: "ready", value }); })
        .catch(() => { if (!abort.signal.aborted) setUas({ state: "error", value: null }); });
    }, 0);
    return () => { clearTimeout(start); abort.abort(); };
  }, [visible, showUas]);

  useEffect(() => {
    if (!visible) return;
    const abort = new AbortController();
    const load = () => readFeed<TfrList>(TFR_API_PATH, abort.signal, 4 * 1024 * 1024, value => Array.isArray(value.kansas) && Array.isArray(value.shapes) && typeof value.detailsFailed === "number")
      .then(value => setTfrs({ state: "ready", value })).catch(() => { if (!abort.signal.aborted) setTfrs({ state: "error", value: null }); });
    const initial = setTimeout(load, 0), interval = setInterval(load, TFR_REFRESH_MS);
    return () => { abort.abort(); clearTimeout(initial); clearInterval(interval); };
  }, [visible]);

  // Live positions refresh every 20 seconds while shown; the route's shared cache bounds provider load.
  useEffect(() => {
    if (!visible || !showTraffic) return;
    const abort = new AbortController();
    const load = () => readFeed<TrafficEnvelope>(AVIATION_TRAFFIC_API_PATH, abort.signal, 8 * 1024 * 1024, value => Array.isArray(value.records) && Boolean(value.provider) && typeof value.provider === "object")
      .then(value => setTraffic({ state: "ready", value: { ...value, receivedAt: Date.now() } })).catch(() => { if (!abort.signal.aborted) setTraffic({ state: "error", value: null }); });
    const tick = () => setTrafficNow(Date.now());
    const initial = setTimeout(() => { tick(); void load(); }, 0), interval = setInterval(load, TRAFFIC_REFRESH_MS), expiry = setInterval(tick, TRAFFIC_EXPIRY_TICK_MS);
    // Positions are only meaningful while fresh: turning traffic off drops them, so turning it back on never redraws old aircraft as "now".
    return () => { abort.abort(); clearTimeout(initial); clearInterval(interval); clearInterval(expiry); setTraffic({ state: "idle", value: null }); };
  }, [visible, showTraffic]);

  // Each position expires 60 s after it was observed, between refreshes and if a refresh stalls.
  const trafficRecords = useMemo(() => showTraffic ? freshAircraft(traffic.value, trafficNow) : [], [showTraffic, traffic.value, trafficNow]);
  const uasCells = useMemo(() => uas.value?.cells ?? [], [uas.value]);
  const tfrShapes = useMemo(() => tfrs.value?.shapes ?? [], [tfrs.value]);
  const metarRecords = useMemo(() => showMetar ? metar.envelope?.records ?? [] : [], [showMetar, metar.envelope]);
  // Data mesh: while shown, public-use airports and weather stations join the page's "Near here" dossier for any feature.
  useEffect(() => {
    onResearchRecords?.(visible && context ? aviationResearchPoints({ airports: context.airports, nasrCycle: context.nasrCycle, validFrom: context.validFrom,
      validToExclusive: context.validToExclusive, metars: metarRecords, metarRetrievedAt: metar.envelope?.retrievedAt ?? null }) : null);
  }, [onResearchRecords, visible, context, metarRecords, metar.envelope]);
  useEffect(() => () => onResearchRecords?.(null), [onResearchRecords]);
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
      const anchors = groundAnchors(context.airports);
      const groundAt = (lon: number, lat: number) => nearestAirport(anchors, lon, lat)?.airport.elevation_ft ?? 0;
      const airports = airportFeatures({ airports: context.airports.filter(airport => airport.use === "PRIVATE" ? showPrivate : showAirports) });
      const weatherLayers = metarFeatures(metarRecords, exaggeration);
      const add = (id: string, data: GeoJSON.FeatureCollection) => map.addSource(`${PREFIX}-${id}`, { type: "geojson", data });
      // 2D chart: the same features drawn flat; the altitude slice keeps what exists at one height.
      const flat = view === "2d";
      const at = (data: GeoJSON.FeatureCollection, toleranceFt = 0) => flat ? sliceCollection(data, slice, exaggeration, groundAt, toleranceFt) : data;
      add("airspace", at(airspaceFeatures(context, groups, exaggeration)));
      add("drone", showDrone ? at(droneFeatures(context, exaggeration)) : { type: "FeatureCollection", features: [] });
      add("airways", airwayFeatures(context, airwayKinds));
      add("runways", airports.runways);
      add("airports", airports.points);
      add("metar", weatherLayers.stations);
      add("ceilings", showCeilings ? at(weatherLayers.ceilings, SLICE_POINT_TOLERANCE_FT) : { type: "FeatureCollection", features: [] });
      add("pireps", at(pirepFeatures(pirepRecords, groundAt, exaggeration), SLICE_POINT_TOLERANCE_FT));
      add("uas", showUas ? at(uasFeatures(uasCells, exaggeration)) : { type: "FeatureCollection", features: [] });
      // TFRs are always drawn while the layer is visible: they are the restriction a drone or pilot most needs to see.
      add("tfr", at(tfrFeatures(tfrShapes, groundAt, exaggeration)));
      add("traffic", at(trafficFeatures(trafficRecords, groundAt, exaggeration, (aircraft, ground) => occupiedAirspace(context, aircraft.lon, aircraft.lat, aircraftAltitudeMsl(aircraft) ?? ground, ground)), SLICE_POINT_TOLERANCE_FT));
      add("profile", { type: "FeatureCollection", features: side ? [
        { type: "Feature", geometry: { type: "LineString", coordinates: [[side.a.lon, side.a.lat], [side.b.lon, side.b.lat]] }, properties: { label: "" } },
        { type: "Feature", geometry: { type: "Point", coordinates: [side.a.lon, side.a.lat] }, properties: { label: "A" } },
        { type: "Feature", geometry: { type: "Point", coordinates: [side.b.lon, side.b.lat] }, properties: { label: "B" } }] : [] });
      add("pick", { type: "FeatureCollection", features: picked ? [{ type: "Feature", geometry: { type: "Point", coordinates: [picked.lon, picked.lat] }, properties: {} }] : [] });
      const font = ["Noto Sans Regular"];
      // Every 3D form has a flat twin: extruded from floor to ceiling in 3D, a filled outline in 2D.
      const volume = (name: string, opacity3d: number, opacity2d: number, minzoom?: number) => map.addLayer((flat
        ? { id: `${PREFIX}-${name}-3d`, type: "fill", source: `${PREFIX}-${name}`, ...(minzoom === undefined ? {} : { minzoom }), paint: { "fill-color": ["get", "color"], "fill-opacity": opacity2d } }
        : { id: `${PREFIX}-${name}-3d`, type: "fill-extrusion", source: `${PREFIX}-${name}`, ...(minzoom === undefined ? {} : { minzoom }), paint: {
          "fill-extrusion-color": ["get", "color"], "fill-extrusion-base": ["get", "base"], "fill-extrusion-height": ["get", "top"], "fill-extrusion-opacity": opacity3d } }) as Parameters<MapLibreMap["addLayer"]>[0]);
      // Translucent shells: the "upside-down wedding cake" of Class B/C reads from the stacked bases and tops.
      volume("airspace", 0.28, 0.1);
      map.addLayer({ id: `${PREFIX}-airspace-edge`, type: "line", source: `${PREFIX}-airspace`, paint: {
        "line-color": ["get", "color"], "line-width": ["match", ["get", "type"], ["CLASS_B", "CLASS_C", "RESTRICTED", "PROHIBITED"], 2.2, 1.3],
        "line-dasharray": ["match", ["get", "type"], ["CLASS_D", "CLASS_E2", "CLASS_E3", "CLASS_E4"], ["literal", [3, 2]], ["literal", [1, 0]]] } });
      map.addLayer({ id: `${PREFIX}-airspace-label`, type: "symbol", source: `${PREFIX}-airspace`, minzoom: 7.5, layout: {
        "text-font": font, "text-field": ["get", flat ? "chart" : "label"], "text-size": flat ? 11.5 : 10.5, "text-optional": true, "symbol-placement": "line", "text-max-angle": 30, "symbol-spacing": 420 },
        paint: { "text-color": ["get", "color"], "text-halo-color": "#ffffff", "text-halo-width": 1.4 } });
      volume("drone", 0.45, 0.28);
      map.addLayer({ id: `${PREFIX}-drone-edge`, type: "line", source: `${PREFIX}-drone`, paint: { "line-color": ["get", "color"], "line-width": 1.5, "line-opacity": 0.9 } });
      // LAANC grid: each cell rises to the altitude the FAA lets LAANC approve there.
      volume("uas", 0.5, 0.45, 8);
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
        // Private-use facilities are hollow and smaller: on the map, but visibly not open to the public.
        "circle-radius": ["interpolate", ["linear"], ["zoom"], 5, ["case", ["get", "private"], 2, 3], 10, ["case", ["get", "private"], 4.5, 6]],
        "circle-color": ["case", ["get", "private"], "#ffffff", ["get", "towered"], "#1f5fbf", "#b5338a"],
        "circle-stroke-color": ["case", ["get", "private"], "#6b5876", "#ffffff"], "circle-stroke-width": 1.5 } });
      map.addLayer({ id: `${PREFIX}-airports-label`, type: "symbol", source: `${PREFIX}-airports`, minzoom: 8, layout: {
        "text-font": font, "text-field": ["get", "label"], "text-size": 10.5, "text-offset": [0, 1.2], "text-anchor": "top", "text-optional": true },
        paint: { "text-color": "#1d2f44", "text-halo-color": "#ffffff", "text-halo-width": 1.3 } });
      volume("ceilings", 0.55, 0.5);
      volume("pireps", 0.85, 0.9);
      volume("tfr", 0.4, 0.3);
      map.addLayer({ id: `${PREFIX}-tfr-edge`, type: "line", source: `${PREFIX}-tfr`, paint: { "line-color": TFR_COLOR, "line-width": 2.5, "line-dasharray": ["literal", [4, 2]] } });
      map.addLayer({ id: `${PREFIX}-tfr-label`, type: "symbol", source: `${PREFIX}-tfr`, layout: {
        "text-font": font, "text-field": ["get", "label"], "text-size": 11, "text-optional": true },
        paint: { "text-color": "#9b0014", "text-halo-color": "#ffffff", "text-halo-width": 1.5 } });
      volume("traffic", 0.9, 0.95);
      map.addLayer({ id: `${PREFIX}-traffic-label`, type: "symbol", source: `${PREFIX}-traffic`, minzoom: 8, layout: {
        "text-font": font, "text-field": ["concat", ["get", "label"], "\n", ["get", "airspace"]], "text-size": 10, "text-optional": true, "text-anchor": "top", "text-offset": [0, 0.8] },
        paint: { "text-color": ["case", ["get", "emergency"], "#b3170b", "#1d2f44"], "text-halo-color": "#ffffff", "text-halo-width": 1.3 } });
      map.addLayer({ id: `${PREFIX}-profile-line`, type: "line", source: `${PREFIX}-profile`, filter: ["==", ["geometry-type"], "LineString"], paint: {
        "line-color": "#111111", "line-width": 2.2, "line-dasharray": ["literal", [3, 2]] } });
      map.addLayer({ id: `${PREFIX}-profile-label`, type: "symbol", source: `${PREFIX}-profile`, filter: ["==", ["geometry-type"], "Point"], layout: {
        "text-font": font, "text-field": ["get", "label"], "text-size": 14, "text-allow-overlap": true }, paint: { "text-color": "#111111", "text-halo-color": "#ffffff", "text-halo-width": 2 } });
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
        if (airport) setPicked({ lon: airport.lon, lat: airport.lat, terrainFt: terrainFtAt(map, airport.lon, airport.lat), label: `${airport.name} (${airport.icao_id ?? airport.faa_id}${airport.use === "PRIVATE" ? `, private-use ${airport.facility_type.toLowerCase()}` : ""})` });
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
  }, [mapRef, styleReady, visible, context, groups, showDrone, showAirports, showPrivate, airwayKinds, showCeilings, metarRecords, pirepRecords, exaggeration, picked, showUas, uasCells, trafficRecords, tfrShapes, view, slice, side]);

  // Point inspection is opt-in so the page's own click tools keep working.
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !picking) return;
    const clicked = (event: MapMouseEvent) => { setPicked({ lon: event.lngLat.lng, lat: event.lngLat.lat, terrainFt: terrainFtAt(map, event.lngLat.lng, event.lngLat.lat), label: `${event.lngLat.lat.toFixed(4)}, ${event.lngLat.lng.toFixed(4)}` }); setPicking(false); };
    map.getCanvas().style.cursor = "crosshair";
    map.once("click", clicked);
    return () => { map.off("click", clicked); map.getCanvas().style.cursor = ""; };
  }, [mapRef, picking]);

  // Dossier "Inspect" on an airport or weather station: the airspace column, drone rule and weather at that point.
  const inspectorRef = useRef<HTMLDivElement | null>(null);
  const focusInspector = useRef(false);
  useEffect(() => {
    if (!inspectRequest || !context) return;
    const map = mapRef.current;
    focusInspector.current = true;
    setPicked({ lon: inspectRequest.lon, lat: inspectRequest.lat, label: inspectRequest.label, terrainFt: map ? terrainFtAt(map, inspectRequest.lon, inspectRequest.lat) : null });
  }, [inspectRequest, context, mapRef]);
  useEffect(() => {
    if (focusInspector.current && picked && inspectorRef.current) { focusInspector.current = false; inspectorRef.current.focus(); }
  }, [picked]);

  // Side view: two clicks, A then B. Ground at each sample uses loaded terrain where it agrees with the nearest facility.
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !sideStep || !context) return;
    const clicked = (event: MapMouseEvent) => {
      const at = { lon: event.lngLat.lng, lat: event.lngLat.lat };
      if (sideStep === "a") { setSideA(at); setSideStep("b"); return; }
      if (!sideA) { setSideStep("a"); return; }
      try {
        const anchors = groundAnchors(context.airports);
        let terrain = 0;
        const points = profilePath(sideA, at).map(point => {
          const ground = pointGroundReference(anchors, point.lon, point.lat, terrainFtAt(map, point.lon, point.lat));
          if (ground.method === "TERRAIN_DEM") terrain++;
          return Object.freeze({ ...point, groundFt: ground.ft });
        });
        setSide({ a: sideA, b: at, points, terrainShare: terrain / points.length });
      } catch { setSide(null); }
      setSideStep(null); setSideA(null);
    };
    map.getCanvas().style.cursor = "crosshair";
    map.once("click", clicked);
    return () => { map.off("click", clicked); map.getCanvas().style.cursor = ""; };
  }, [mapRef, sideStep, sideA, context]);

  const profile = useMemo(() => {
    if (!context || !side) return null;
    const types = new Set((Object.keys(AIRSPACE_GROUPS) as AirspaceGroup[]).filter(group => groups.has(group)).flatMap(group => AIRSPACE_GROUPS[group].types));
    const volumes: ProfileVolume[] = [
      ...context.volumes.filter(volume => types.has(volume.type)).map((volume): ProfileVolume => ({ key: volume.id, label: airspaceLabel(volume), color: AIRSPACE_COLORS[volume.type], kind: "airspace",
        bbox: volume.bbox, rings: volume.rings, lowFt: ground => mslOf(volume.floor.reference, volume.floor.value_ft, ground), highFt: ground => mslOf(volume.ceiling.reference, volume.ceiling.value_ft, ground) })),
      ...tfrShapes.map((shape, index): ProfileVolume => ({ key: `tfr:${shape.notam}:${index}`, label: `TFR ${shape.notam}${shape.type ? ` ${shape.type}` : ""} · ${formatTfrLimit(shape.floor)}–${formatTfrLimit(shape.ceiling)}`,
        color: TFR_COLOR, kind: "tfr", bbox: shape.bbox, rings: [shape.ring], lowFt: ground => mslOf(shape.floor.reference, shape.floor.valueFt, ground), highFt: ground => mslOf(shape.ceiling.reference, shape.ceiling.valueFt, ground) })),
    ];
    const bands = profileBands(side.points, volumes);
    const aircraft = trafficRecords.flatMap((record): ProfileAircraft[] => {
      const msl = aircraftAltitudeMsl(record), distanceNm = alongTrackNm(side.a, side.b, record.lon, record.lat);
      return msl === null || distanceNm === null ? [] : [{ hex: record.hex, distanceNm, altitudeFt: msl, emergency: Boolean(record.emergency), label: record.callsign ?? record.registration ?? record.hex.toUpperCase() }];
    });
    return { bands, aircraft, summary: profileSummary(side.points, bands) };
  }, [context, side, groups, tfrShapes, trafficRecords]);

  const edition = context ? aviationEditionStatus(context, clock) : null;
  const shownRender = !visible ? "Hidden" : !context ? contextState === "error" ? "Unavailable" : "Loading" : !styleReady ? "Not ready" : render;
  const inspection = useMemo(() => {
    if (!context || !picked) return null;
    const anchors = groundAnchors(context.airports);
    const ground = pointGroundReference(anchors, picked.lon, picked.lat, picked.terrainFt);
    const groundFt = ground.ft;
    const column = airspaceColumn(context, picked.lon, picked.lat, groundFt);
    const drone = droneVerdictAtPoint(context, picked.lon, picked.lat, groundFt);
    const station = metarRecords.map(record => ({ record, km: distanceKm(picked.lon, picked.lat, record.lon, record.lat) })).sort((a, b) => a.km - b.km)[0];
    const usable = station && station.km <= 50 ? station : null;
    const surface = column.find(band => band.floorFtAgl === 0 && band.airspaceClass !== "SUA");
    const surfaceClass = surface && surface.airspaceClass !== "A" ? surface.airspaceClass : "G";
    const vfr = basicVfrCheck(surfaceClass as "B" | "C" | "D" | "E" | "G", usable?.record ?? null);
    const routes = [...new Map(airwaysNearPoint(context, picked.lon, picked.lat).map(segment => [segment.designation, segment])).values()];
    const reports = pirepRecords.filter(report => distanceKm(picked.lon, picked.lat, report.lon, report.lat) <= 60);
    const laanc = uasCeilingAt(uasCells, picked.lon, picked.lat);
    const aircraft = trafficRecords.map(record => ({ record, km: distanceKm(picked.lon, picked.lat, record.lon, record.lat) }))
      .filter(item => item.km <= 15).sort((a, b) => a.km - b.km).slice(0, 12)
      .map(item => {
        const msl = aircraftAltitudeMsl(item.record);
        const ground = nearestAirport(anchors, item.record.lon, item.record.lat)?.airport.elevation_ft ?? 0;
        return { ...item, msl, airspace: msl === null ? "on the surface" : occupiedAirspace(context, item.record.lon, item.record.lat, msl, ground) };
      });
    const restrictions = tfrsAtPoint(tfrShapes, picked.lon, picked.lat);
    return { ground, groundFt, column, drone, station: usable, vfr, routes, reports, laanc, aircraft, restrictions };
  }, [context, picked, metarRecords, pirepRecords, uasCells, trafficRecords, tfrShapes]);

  const toggleGroup = (group: AirspaceGroup, on: boolean) => setGroups(current => { const next = new Set(current); if (on) next.add(group); else next.delete(group); return next; });
  const toggleAirway = (kinds: AirwaySegment["type"][], on: boolean) => setAirwayKinds(current => { const next = new Set(current); for (const kind of kinds) { if (on) next.add(kind); else next.delete(kind); } return next; });
  const tilt = () => mapRef.current?.easeTo({ pitch: 62, bearing: mapRef.current.getBearing() || -18, duration: 900 });
  // 2D reads like a chart from straight above; 3D tilts so the shells' floors and ceilings show.
  const chooseView = (next: AviationView) => { setView(next); if (next === "2d") mapRef.current?.easeTo({ pitch: 0, duration: 700 }); else tilt(); };
  const sliceValue = slice.kind === "msl" ? String(slice.ft) : slice.kind;

  return <section className="official-context-row" aria-label="Airspace, airports and aviation weather">
    <div className="official-context-primary"><label className="visibility-switch"><input type="checkbox" checked={visible} aria-label={visible ? "Hide airspace and aviation layers" : "Show airspace and aviation layers"} onChange={event => { setVisible(event.target.checked); if (event.target.checked) setRender("Waiting for map frame"); }} /><span aria-hidden="true" /></label><i style={{ "--swatch": AIRSPACE_COLORS.CLASS_C } as React.CSSProperties} /><div><strong>Airspace, airports &amp; aviation weather</strong><small>FAA NASR · NOAA AWC · {visible ? shownRender : "Off"}</small></div></div>
    <details className="specialty-layer-details"><summary>Airspace shells, drone zones, weather &amp; controls</summary><div className="official-context-option-body">
      <p><strong>Not for navigation, flight planning or drone authorization.</strong> Check current FAA charts, NOTAMs and TFRs, and use B4UFLY / LAANC before flying. TFR boundaries are drawn from the FAA detail files; times and exceptions are in each NOTAM.</p>
      {contextState === "loading" && <p role="status">Loading the pinned FAA NASR airspace product…</p>}
      {contextState === "error" && <p role="status">Airspace context unavailable: {contextError} Nothing is drawn in its place.</p>}
      {edition && <p role="status" data-edition={edition.state}><strong>{edition.state === "CURRENT" ? "Current edition" : edition.state === "PREVIEW" ? "Preview edition" : "Expired edition"}:</strong> {edition.text}</p>}
      {context && <>
        <fieldset><legend>Airspace volumes</legend>
          <div role="radiogroup" aria-label="Airspace display"><label><input type="radio" name="kfm-aviation-view" checked={view === "3d"} onChange={() => chooseView("3d")} /> 3D volumes</label>
            <label><input type="radio" name="kfm-aviation-view" checked={view === "2d"} onChange={() => chooseView("2d")} /> 2D chart</label></div>
          {view === "2d" && <><label>Altitude slice<select value={sliceValue} onChange={event => setSlice(event.target.value === "all" ? ALL_ALTITUDES : event.target.value === "drone" ? { kind: "drone" } : { kind: "msl", ft: Number(event.target.value) })}>
              <option value="all">All altitudes</option><option value="drone">Drone altitudes (SFC–400 ft AGL)</option>
              {SLICE_MSL_FEET.map(ft => <option key={ft} value={ft}>{ft.toLocaleString("en-US")} ft MSL</option>)}</select></label>
            <small role="status">2D chart · {sliceTitle(slice)}. Labels read ceiling/floor in hundreds of feet MSL, as on a sectional (ICT 53/27 = 2,700 to 5,300 ft; SFC = surface; AGL is marked).{slice.kind === "msl" ? ` Shapes containing ${slice.ft.toLocaleString("en-US")} ft are shown, with aircraft, pilot reports and cloud bases within ${SLICE_POINT_TOLERANCE_FT.toLocaleString("en-US")} ft.` : ""}{slice.kind === "msl" && slice.ft >= 18000 ? " Class A covers the whole region from FL180 to FL600 and is not drawn as a shape." : ""}{slice.kind === "msl" && slice.ft < 18000 ? " Where no shape is drawn, the airspace is Class E or G (see the airspace column)." : ""}</small></>}
          {(Object.keys(AIRSPACE_GROUPS) as AirspaceGroup[]).map(group => <label key={group}><input type="checkbox" checked={groups.has(group)} onChange={event => toggleGroup(group, event.target.checked)} /> {AIRSPACE_GROUPS[group].title}</label>)}
          <label>Vertical exaggeration (3D)<select disabled={view === "2d"} value={exaggeration} onChange={event => setExaggeration(Number(event.target.value) as (typeof EXAGGERATIONS)[number])}>{EXAGGERATIONS.map(value => <option key={value} value={value}>{value}×{value === 1 ? " (true scale)" : ""}</option>)}</select></label>
          {view === "3d" && <button type="button" onClick={tilt}>Tilt map to see shells in 3D</button>}
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
          <p><strong>Temporary flight restrictions:</strong> {tfrs.state === "ready" && tfrs.value ? tfrs.value.kansas.length ? `${tfrs.value.kansas.length} Kansas-related of ${tfrs.value.total} active nationwide.` : `None matched Kansas among ${tfrs.value.total} active nationwide.` : tfrs.state === "error" ? "FAA TFR list unavailable." : "Checking…"}{tfrs.value ? ` ${tfrs.value.shapes.length} area(s) drawn in red${tfrs.value.detailsFailed > 0 ? `; ${tfrs.value.detailsFailed} of ${tfrs.value.detailsChecked} boundary file(s) could not be read in full, so not every TFR area is drawn` : ""}.` : ""} <a href={TFR_HOME} target="_blank" rel="noreferrer">Check tfr.faa.gov</a></p>
          {tfrs.value && tfrs.value.kansas.length > 0 && <ul>{tfrs.value.kansas.slice(0, 20).map(entry => <li key={entry.notam}><strong>{entry.notam}</strong>{entry.type ? ` · ${entry.type}` : ""}: {entry.description}</li>)}</ul>}
        </fieldset>
        <fieldset><legend>Airports &amp; air traffic structure</legend>
          <label><input type="checkbox" checked={showAirports} onChange={event => setShowAirports(event.target.checked)} /> Public-use airports and runways ({context.airports.filter(airport => airport.use === "PUBLIC").length})</label>
          <label><input type="checkbox" checked={showPrivate} onChange={event => setShowPrivate(event.target.checked)} /> Private-use airports, heliports and strips ({context.airports.filter(airport => airport.use === "PRIVATE").length}; hollow dots, “PVT”). Landing needs the owner’s permission.</label>
          <label><input type="checkbox" checked={airwayKinds.has("VICTOR")} onChange={event => toggleAirway(["VICTOR", "RNAV_T"], event.target.checked)} /> Low airways (Victor, T routes) · 1,200 AGL–below FL180</label>
          <label><input type="checkbox" checked={airwayKinds.has("JET")} onChange={event => toggleAirway(["JET", "RNAV_Q"], event.target.checked)} /> High routes (Jet, Q routes) · FL180–FL450</label>
          <label><input type="checkbox" checked={showTraffic} onChange={event => setShowTraffic(event.target.checked)} /> Live aircraft (ADS-B), drawn at reported altitude and labelled with the airspace they are in</label>
          <ul className="aviation-legend">{TRAFFIC_ALTITUDE_COLORS.map(([value, color]) => <li key={value}><i style={{ background: color }} /> {value === 0 ? "Surface / no altitude" : `${value.toLocaleString("en-US")} ft MSL and above`}</li>)}<li><i style={{ background: "#e0301e" }} /> Emergency squawk (7500/7600/7700)</li></ul>
          {showTraffic && <small role="status">Traffic: {traffic.state === "ready" && traffic.value ? <>{trafficRecords.length} aircraft · retrieved {minutesAgo(traffic.value.retrievedAt, clock) < 1 ? "just now" : `${minutesAgo(traffic.value.retrievedAt, clock)} min ago`} · data <a href={traffic.value.provider.homepage} target="_blank" rel="noreferrer">{traffic.value.provider.title}</a> ({traffic.value.provider.terms}){trafficRecords.some(record => record.emergency) ? " · EMERGENCY squawk present" : ""}</> : traffic.state === "error" ? "Unavailable from every listed receiver network. No cached positions are shown." : "Checking…"}</small>}
          <small>Volunteer receiver coverage: some aircraft, especially low or on the ground, are missing. An empty sky on the map is not evidence of no traffic.</small>
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
          <button type="button" aria-pressed={sideStep !== null} onClick={() => { setSideStep(step => step ? null : "a"); setSideA(null); }}>{sideStep === "a" ? "Click point A… (press again to cancel)" : sideStep === "b" ? "Now click point B…" : "Draw a side view (A to B)"}</button>
          {side && profile && <figure className="aviation-profile">
            <ProfileChart points={side.points} bands={profile.bands} aircraft={profile.aircraft} />
            <figcaption><strong>Side view A→B, {side.points[side.points.length - 1].distanceNm.toFixed(1)} NM.</strong> Shapes show each volume’s floor and ceiling over the ground; the brown profile is {side.terrainShare >= 0.99 ? "terrain elevation" : side.terrainShare > 0 ? "terrain where loaded, otherwise the nearest facility's elevation" : "the nearest facility's elevation (turn on 3D terrain for the local ground)"}; the green dashes are the 400 ft AGL drone ceiling; dots are aircraft within 5 km of the line. Where no shape is drawn the airspace is Class E or G.
              {profile.summary.length > 0 ? <ul>{profile.summary.map(line => <li key={line}>{line}</li>)}</ul> : <> No charted volume or TFR crosses this line.</>}
              <button type="button" onClick={() => setSide(null)}>Clear side view</button></figcaption>
          </figure>}
          {inspection && picked && <div className="aviation-column" data-aviation-inspector tabIndex={-1} ref={inspectorRef}>
            <p><strong>{picked.label}</strong> · ground {feet(inspection.groundFt)} MSL {inspection.ground.method === "TERRAIN_DEM" ? "(terrain elevation at this point)" : inspection.ground.method === "NEAREST_FACILITY" ? `(nearest facility ${inspection.ground.facility}, ${(inspection.ground.km ?? 0).toFixed(1)} km${inspection.ground.terrainRejected ? "; the terrain reading here disagreed by over 1,000 ft and was not used" : "; turn on 3D terrain for the local ground"})` : "(no ground reference)"}</p>
            <p style={{ borderLeft: `4px solid ${DRONE_RULE_COLORS[inspection.drone.rule.code]}`, paddingLeft: 8 }}><strong>Drone, SFC–400 ft AGL:</strong> {inspection.drone.rule.title}. {inspection.drone.rule.detail} <small>({inspection.drone.governing} · {inspection.drone.rule.cite})</small></p>
            {inspection.laanc && <p><strong>LAANC ceiling here:</strong> {inspection.laanc.ceilingFt} ft AGL{inspection.laanc.airport ? ` (${inspection.laanc.airportName ?? inspection.laanc.airport} grid)` : ""}. {inspection.laanc.ceilingFt === 0 ? "LAANC cannot approve flight in this cell; request a DroneZone authorization." : "LAANC can approve up to this altitude; it is not approval by itself."} <small>(FAA UAS Facility Map)</small></p>}
            {inspection.restrictions.length > 0 && <div style={{ borderLeft: `4px solid ${TFR_COLOR}`, paddingLeft: 8 }}><p><strong>Temporary flight restriction here:</strong> flight inside these limits, drones included, is prohibited unless the NOTAM allows it.</p>
              <ul>{inspection.restrictions.map(shape => <li key={`${shape.notam}:${shape.name ?? ""}`}><strong>{shape.notam}</strong>{shape.type ? ` ${shape.type}` : ""}{shape.name ? ` · ${shape.name}` : ""}: {formatTfrLimit(shape.floor)} to {formatTfrLimit(shape.ceiling)}{shape.effective || shape.expires ? ` · ${shape.effective ?? "?"} to ${shape.expires ?? "until further notice"} (UTC)` : ""}</li>)}</ul></div>}
            {tfrs.value && (tfrs.value.kansas.length > 0 || tfrs.value.detailsFailed > 0) && inspection.restrictions.length === 0 && <p><strong>Check TFRs:</strong> {tfrs.value.kansas.length} Kansas-related temporary flight restriction(s) are active, none drawn at this point{tfrs.value.detailsFailed > 0 ? `, but ${tfrs.value.detailsFailed} boundary file(s) could not be read in full, so a restriction here may not be shown` : ""}.</p>}
            <table><thead><tr><th scope="col">Band</th><th scope="col">Floor → ceiling</th><th scope="col">≈ above ground</th><th scope="col">Who can fly, and how</th></tr></thead>
              <tbody>{[...inspection.column].reverse().map(band => <tr key={band.key}><th scope="row">{band.label}</th><td>{band.floorText} → {band.ceilingText}</td>
                <td>{feet(band.floorFtAgl)} → {feet(band.ceilingFtAgl)}</td><td>{band.manned} <small>({band.cite})</small></td></tr>)}</tbody></table>
            <p><strong>Weather now:</strong> {inspection.station ? <>{inspection.station.record.raw} <small>({inspection.station.km.toFixed(0)} km away, {minutesAgo(inspection.station.record.observedAt, clock)} min old{inspection.station.record.densityAltitudeFt !== null ? `, density altitude ≈ ${feet(inspection.station.record.densityAltitudeFt)}` : ""})</small></> : "No METAR station within 50 km."} {inspection.vfr.text} <small>({inspection.vfr.cite})</small></p>
            {inspection.aircraft.length > 0 && <><p><strong>Aircraft within 15 km now:</strong></p><ul>{inspection.aircraft.map(item => <li key={item.record.hex}>{item.record.callsign ?? item.record.registration ?? item.record.hex.toUpperCase()}{item.record.type ? ` (${item.record.type})` : ""} · {item.record.onGround ? "on ground" : item.msl === null ? "altitude n/a" : `${feet(item.msl)} MSL`} · {item.km.toFixed(1)} km · in {item.airspace}{item.record.emergency ? ` · ${item.record.squawk ?? ""} ${item.record.emergency.toUpperCase()}` : ""}</li>)}</ul></>}
            {inspection.routes.length > 0 && <p><strong>Airways within 4 NM:</strong> {inspection.routes.map(route => `${route.designation}${route.mea_ft ? ` (MEA ${route.mea_ft.toLocaleString("en-US")})` : ""}`).join(", ")}</p>}
            {inspection.reports.length > 0 && <p><strong>Pilot reports within 60 km (3 h):</strong> {inspection.reports.slice(0, 5).map(report => `${report.raw} (${pirepAltitudeLabel(report)})`).join(" · ")}</p>}
          </div>}
        </fieldset>
        <details><summary>Source, edition &amp; limits</summary>
          <dl><dt>Airspace, airports, airways</dt><dd>FAA NASR cycle {context.nasrCycle} (valid {context.validFrom} to {context.validToExclusive}, exclusive) · product <code>{context.productId.slice(0, 19)}…</code></dd>
            <dt>Weather</dt><dd><a href="https://aviationweather.gov/data/api/" target="_blank" rel="noreferrer">NOAA/NWS Aviation Weather Center Data API</a></dd>
            <dt>Live traffic</dt><dd><a href="https://adsb.lol/" target="_blank" rel="noreferrer">adsb.lol</a> (ODbL 1.0), else <a href="https://adsb.fi/" target="_blank" rel="noreferrer">adsb.fi</a> open data (non-commercial, attribution)</dd>
            <dt>Drone grid and TFRs</dt><dd>FAA UAS Facility Maps; FAA TFR list and NOTAM detail files (<a href={TFR_HOME} target="_blank" rel="noreferrer">tfr.faa.gov</a>)</dd>
            <dt>Evidence role</dt><dd>External display context only; not a KFM-released record.</dd></dl>
          <ul>{context.limitations.map(item => <li key={item}>{item}</li>)}</ul>
        </details>
      </>}
    </div></details>
  </section>;
}
