"use client";

import { Fragment, useCallback, useEffect, useMemo, useRef, useState } from "react";
import Link from "next/link";
import { currentDayStart, currentUtcDay, latestSafeCursor } from "../daily-baseline";
import { browserRenderBudget, updateGeoJSON } from "../map-performance";
import { DataNotices } from "../map-toolbar";
import type { Map as GLMap, GeoJSONSource } from "maplibre-gl";
import { BASEMAPS } from "../map-runtime";
import {
  EVENT_BOUNDS,
  EVENT_EARLIEST_DAY,
  EVENT_MAX_HOURS,
  advanceEventDay,
  eventDayHours,
  eventFrames,
  eventHourAvailability,
  eventWeekDays,
  radarAt,
  smokeAt,
  type EventManifest,
} from "../event-atlas";
import { parseStreamflowBundle, buildStreamflowFrame, buildHydrographSegments, type StreamflowBundle } from "../streamflow";

type TrackId = "radar" | "smoke" | "river" | "geology" | "flora" | "fauna" | "resources" | "counties" | "weather" | "earthquakes" | "shake";
type ContextTrack = "counties" | "weather" | "earthquakes" | "shake";
type ContextRecord = { data: GeoJSON.FeatureCollection; message: string; date: string; source: string };
type RiverCoverage = { station: string; daily: { start: string; end: string } | null; continuous: { start: string; end: string } | null; partial: boolean; message: string };
type Track = { id: TrackId; name: string; axis: string; detail: string; color: string; source: string };
type ArchiveDayStatus = "checking" | "available" | "partial" | "empty" | "failed";
type ArchiveDayLedger = Readonly<{ status: ArchiveDayStatus; supportedHours: readonly number[]; message?: string }>;
type CalendarCellState = "supported" | "gap" | "checking" | "failed" | "unqueried" | "future";
const TRACKS: Track[] = [
  { id: "earthquakes", name: "USGS earthquake history", axis: "Catalog event time", color: "#f2a58f", source: "https://earthquake.usgs.gov/fdsnws/event/1/", detail: "Actual USGS earthquake catalog events within the selected day. Points appear at their event time and remain for the loaded interval. Catalog completeness varies over time; no returned event is not proof of no earthquake." },
  { id: "shake", name: "Raspberry Shake stations", axis: "Station operating epoch", color: "#ec99cf", source: "https://manual.raspberryshake.org/fdsn.html", detail: "AM network station metadata for the selected day, including closed stations where their operating epoch overlaps. This is a real station connection; waveform traces remain on the provider's service. FDSN waveform delivery is delayed at least 30 minutes and is not an earthquake catalog." },
  { id: "weather", name: "NOAA daily weather history", axis: "Daily station summary", color: "#f1cc78", source: "https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily", detail: "NOAA GHCN daily station records: maximum/minimum temperature and precipitation. Includes historical cooperative stations and airports. Daily summaries stay pinned to their date throughout the 24-hour sweep and do not create hourly observations." },
  { id: "counties", name: "County baseline", axis: "Independent Census edition", color: "#8ed9d0", source: "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb", detail: "All 105 Kansas counties: Census geometry, population, housing units, and land/water area for the selected 2010 or 2020 edition. Click a county to inspect its baseline. The edition remains independent of the event date; it is not an 1800s boundary reconstruction." },
  { id: "radar", name: "Radar reflectivity", axis: "5-minute mosaic validity", color: "#72ddc0", source: "https://mesonet.agron.iastate.edu/docs/nexrad_composites/", detail: "NOAA/NWS → Iowa State IEM. Mosaic slots, not simultaneous scans; inputs may be 15 minutes old. Blank can mean no echo or missing coverage." },
  { id: "smoke", name: "Smoke footprint", axis: "Satellite-analysis interval", color: "#e7b783", source: "https://www.ospo.noaa.gov/products/land/hms.html", detail: "NOAA HMS polygon Start ≤ cursor < End. Light / medium / heavy / unknown column density. Not surface PM2.5, altitude, or wind-driven transport." },
  { id: "river", name: "River pulse", axis: "Observation time · 30-min hold", color: "#7edceb", source: "https://api.waterdata.usgs.gov/", detail: "USGS discharge 00060 in ft³/s. Exact selected-station samples; held for at most 30 minutes and explicitly timestamped. No interpolation or flood classification." },
  { id: "geology", name: "Kansas surface geology", axis: "Static mapped geology · edition unverified", color: "#d6a9df", source: "https://kgs.ku.edu/geology-and-mineral-resources", detail: "Official KGS cached geology carrier; its item does not supply an edition or reuse license. It is not the newer GeMS service. Unit color encodes mapped surface geology, not reconstruction at the event date. Rock age and map edition are different clocks." },
  { id: "flora", name: "Flora occurrences", axis: "Observation year · aggregate", color: "#a9df75", source: "https://techdocs.gbif.org/en/openapi/v2/maps", detail: "GBIF Plantae (taxon 6), dated occurrence density in coarse hexagons. Source tiles capped at zoom 6 before delivery. Includes collection/specimen records; not vegetation cover, effort-adjusted abundance, or absence." },
  { id: "fauna", name: "Fauna occurrences", axis: "Observation year · aggregate", color: "#d4b5fa", source: "https://techdocs.gbif.org/en/openapi/v2/maps", detail: "GBIF Animalia (taxon 1), coarse dated occurrence density. No exact points or movement trajectories. Uneven sampling and mobilization strongly affect coverage; no records is not absence." },
  { id: "resources", name: "Resource-map symbols", axis: "Pinned topographic edition · county", color: "#e5c46b", source: "https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/USGS_Topographic_Mine_Symbols/FeatureServer/8", detail: "USGS historical 1:24,000 topographic mine symbols aggregated by modern Census county before delivery. Map edition is not mine operating time. Counts are symbols, not unique mines, production, reserves, ownership, or economic potential. This is an older compilation, not the latest USMIN release." },
];
const INITIAL = { radar: true, smoke: true, river: true, geology: false, flora: false, fauna: false, resources: false, counties: true, weather: false, earthquakes: false, shake: false };
const INITIAL_OPACITY = { radar: .8, smoke: .45, river: 1, geology: .5, flora: .7, fauna: .7, resources: .65, counties: .25, weather: .85, earthquakes: .9, shake: .85 };
const LAYERS: Record<TrackId, string[]> = { counties: ["ea-counties", "ea-county-lines"], weather: ["ea-weather"], earthquakes: ["ea-earthquakes"], shake: ["ea-shake"], radar: ["ea-radar"], smoke: ["ea-smoke-fill", "ea-smoke-edge"], river: ["ea-river-glow", "ea-river"], geology: ["ea-geology"], flora: ["ea-flora"], fauna: ["ea-fauna"], resources: ["ea-resources"] };
const PRESETS = [
  { label: "Greensburg radar · May 2007", start: "2007-05-05T01:00", hours: 6 },
  { label: "Plains storms · May 2024", start: "2024-05-19T21:00", hours: 6 },
  { label: "Smoke archive · June 2023", start: "2023-06-07T12:00", hours: 6 },
];
const EMPTY = { type: "FeatureCollection" as const, features: [] };
const timestamp = (value: string | null) => value ? value.replace("T", " · ").replace(".000Z", " UTC") : "No committed frame";
const localTimestamp = (value: string | null) => value ? new Intl.DateTimeFormat("en-US", { timeZone: "America/Chicago", dateStyle: "medium", timeStyle: "short" }).format(new Date(value)) + " · Central" : "";
const dayFormatter = new Intl.DateTimeFormat("en-US", { timeZone: "UTC", weekday: "short", month: "short", day: "numeric" });
const monthFormatter = new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "long", year: "numeric" });
const calendarDayLabel = (day: string) => dayFormatter.format(new Date(`${day}T00:00:00.000Z`));
const calendarMonthLabel = (day: string) => monthFormatter.format(new Date(`${day}T00:00:00.000Z`));
const hourLabel = (hour: number) => `${String(hour).padStart(2, "0")}:00`;

function addRaster(map: GLMap, id: string, tiles: string, maxzoom: number, attribution: string, opacity = 1, tileSize = 256) {
  map.addSource(id, { type: "raster", tiles: [tiles], tileSize, maxzoom, bounds: [...EVENT_BOUNDS], attribution });
  map.addLayer({ id, type: "raster", source: id, layout: { visibility: "none" }, paint: { "raster-opacity": opacity, "raster-fade-duration": 0 } });
}
function removeLayerSource(map: GLMap, id: string) { if (map.getLayer(id)) map.removeLayer(id); if (map.getSource(id)) map.removeSource(id); }
function riverAt(bundle: StreamflowBundle, cursor: string, resolution: "daily" | "continuous") {
  if (resolution === "continuous") return buildStreamflowFrame(bundle, cursor, 30);
  const record = bundle.observations.find((row) => row.statisticId === "00003" && row.observedAt.slice(0,10) === cursor.slice(0,10));
  return record ? buildStreamflowFrame({ ...bundle, observations: [record] }, record.observedAt, 0) : EMPTY;
}

export default function EventObservatory() {
  const container = useRef<HTMLDivElement>(null), mapRef = useRef<GLMap | null>(null);
  const generation = useRef(0), requestRef = useRef<AbortController | null>(null), frameRequest = useRef<AbortController | null>(null);
  const urls = useRef(new Map<string, string>()), frameGeneration = useRef(0);
  const radarSourceTime = useRef<string | null>(null), sourceFailures = useRef(new Set<string>());
  const [geologyLegend, setGeologyLegend] = useState<{ label: string; image: string }[]>([]);
  const [mapReady, setMapReady] = useState(false), [mapMessage, setMapMessage] = useState("Opening the Kansas map…");
  const [start, setStart] = useState(currentDayStart), [hours, setHours] = useState(24), [station, setStation] = useState("USGS-06889000");
  const initialLoad = useRef(false), followTodayRef = useRef(true);
  const [followToday, setFollowToday] = useState(true);
  const [manifest, setManifest] = useState<EventManifest | null>(null), [river, setRiver] = useState<StreamflowBundle | null>(null), [riverMessage, setRiverMessage] = useState("Not loaded");
  const [loading, setLoading] = useState(false), [error, setError] = useState(""), [index, setIndex] = useState(0), [cursor, setCursor] = useState<string | null>(null), [committed, setCommitted] = useState<string | null>(null), [buffering, setBuffering] = useState(false), [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState(1), [loop, setLoop] = useState(false), [reduced, setReduced] = useState(false);
  const [visible, setVisible] = useState<Record<TrackId, boolean>>(INITIAL), [opacity, setOpacity] = useState<Record<TrackId, number>>(INITIAL_OPACITY), [order, setOrder] = useState<TrackId[]>(TRACKS.map((t) => t.id));
  const opacityRef = useRef(opacity);
  const [selectedTrack, setSelectedTrack] = useState<TrackId>("radar"), [base, setBase] = useState<"reference" | "satellite">("reference"), [baseDay, setBaseDay] = useState<string | null>(null), [copied, setCopied] = useState(false);
  const [sourceErrors, setSourceErrors] = useState<Record<string, string>>({});
  const [contextData, setContextData] = useState<Partial<Record<ContextTrack, ContextRecord>>>({});
  const [contextMessages, setContextMessages] = useState<Partial<Record<ContextTrack, string>>>({});
  const [countyEdition, setCountyEdition] = useState("2020");
  const [inspectedFeature, setInspectedFeature] = useState<{ track: TrackId; properties: Record<string, unknown> } | null>(null);
  const [riverResolution, setRiverResolution] = useState<"continuous" | "daily">("continuous");
  const [loadedRiverResolution, setLoadedRiverResolution] = useState<"continuous" | "daily">("continuous");
  const [riverCoverage, setRiverCoverage] = useState<RiverCoverage | null>(null), [coverageMessage, setCoverageMessage] = useState("");
  const [layersOpen, setLayersOpen] = useState(false), [detailsOpen, setDetailsOpen] = useState(false);
  const [calendarOpen, setCalendarOpen] = useState(false), [chartsOpen, setChartsOpen] = useState(false);
  const [resourceEdition, setResourceEdition] = useState("1984"), [resourceData, setResourceData] = useState<GeoJSON.FeatureCollection | null>(null), [resourceMessage, setResourceMessage] = useState("Not loaded");
  const [calendarAnchor, setCalendarAnchor] = useState(currentUtcDay);
  const [calendarLedger, setCalendarLedger] = useState<Record<string, ArchiveDayLedger>>({});
  const [calendarNow, setCalendarNow] = useState(() => Date.now());
  const frames = useMemo(() => manifest ? eventFrames(manifest, loadedRiverResolution === "daily" ? [] : river?.observations) : [], [manifest, river, loadedRiverResolution]);
  const requested = cursor ?? frames[index] ?? null;
  const activeRadar = manifest && committed ? radarAt(manifest.radar.scans, committed) : null;
  const activeSmoke = useMemo(() => manifest && committed ? smokeAt(manifest.smoke.data, committed) : EMPTY, [manifest, committed]);
  const riverFrame = useMemo(() => river && committed ? riverAt(river, committed, loadedRiverResolution) : null, [river, committed, loadedRiverResolution]);
  const gauge = riverFrame?.features[0]?.properties;
  const series = useMemo(() => manifest ? river?.observations.filter((o) => o.observedAt >= manifest.start && o.observedAt < manifest.end) ?? [] : [], [river, manifest]);
  const graph = useMemo(() => buildHydrographSegments(series, { width: 520, height: 100, padding: 7, gapMinutes: 30 }), [series]);
  const numbers = series.flatMap((o) => o.value === null ? [] : [o.value]);
  const chosen = TRACKS.find((track) => track.id === selectedTrack)!;
  const selectedCalendarDay = start.slice(0, 10);
  const calendarDays = useMemo(() => eventWeekDays(calendarAnchor), [calendarAnchor]);
  const calendarHours = useMemo(() => eventDayHours(selectedCalendarDay), [selectedCalendarDay]);
  const calendarToday = useMemo(() => new Date(calendarNow).toISOString().slice(0, 10), [calendarNow]);

  const hideEventLayers = useCallback((all = true) => {
    const map = mapRef.current;
    if (!map) return;
    for (const key of Object.keys(LAYERS) as TrackId[]) if (all || ["radar","smoke","river","weather","earthquakes","shake"].includes(key)) for (const id of LAYERS[key]) if (map.getLayer(id)) map.setLayoutProperty(id, "visibility", "none");
    if (all && map.getLayer("ea-satellite")) map.setLayoutProperty("ea-satellite", "visibility", "none");
  }, []);

  useEffect(() => {
    let disposed = false;
    const media = window.matchMedia("(prefers-reduced-motion: reduce)");
    const change = () => { setReduced(media.matches); setPlaying(false); }; change(); media.addEventListener("change", change);
    const stop = () => { if (document.hidden) setPlaying(false); };
    const key = (event: KeyboardEvent) => { if (event.key === "Escape") { setPlaying(false); setLayersOpen(false); setCalendarOpen(false); setDetailsOpen(false); } };
    document.addEventListener("visibilitychange", stop); window.addEventListener("keydown", key);
    queueMicrotask(() => {
      if (disposed) return;
      const p = new URLSearchParams(window.location.search);
      if (/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$/.test(p.get("start") ?? "")) { setStart(p.get("start")!); setCalendarAnchor(p.get("start")!.slice(0,10)); followTodayRef.current = false; setFollowToday(false); }
      if ([1,6,24].includes(Number(p.get("hours")))) setHours(Number(p.get("hours")));
      if (/^USGS-\d{8,15}$/.test(p.get("station") ?? "")) setStation(p.get("station")!);
      if (p.has("station") && p.get("station") === "") setStation("");
      if (p.has("layers")) { const ids = p.get("layers")!.split(","); setVisible(Object.fromEntries(TRACKS.map((t) => [t.id, ids.includes(t.id)])) as Record<TrackId,boolean>); }
      if (p.get("base") === "satellite") setBase("satellite");
      if (p.get("resolution") === "daily") setRiverResolution("daily");
      if (["2010", "2020"].includes(p.get("county") ?? "")) setCountyEdition(p.get("county")!);
      if (/^\d{4}$/.test(p.get("edition") ?? "") && Number(p.get("edition")) >= 1934 && Number(p.get("edition")) <= 1996) setResourceEdition(p.get("edition")!);
      if (p.has("order")) { const ids = p.get("order")!.split(","); if (ids.length === TRACKS.length && new Set(ids).size === TRACKS.length && ids.every((id) => TRACKS.some((t) => t.id === id))) setOrder(ids as TrackId[]); }
      if (p.has("opacity")) { const values = p.get("opacity")!.split(",").map(Number); if (values.length === TRACKS.length && values.every((v) => Number.isFinite(v) && v >= 0 && v <= 1)) setOpacity(Object.fromEntries(TRACKS.map((t,i) => [t.id,values[i]])) as Record<TrackId,number>); }
    });
    return () => { disposed = true; media.removeEventListener("change", change); document.removeEventListener("visibilitychange", stop); window.removeEventListener("keydown", key); };
  }, []);

  useEffect(() => { if (eventDayHours(start.slice(0, 10)).length) setCalendarAnchor(start.slice(0, 10)); }, [start]);
  useEffect(() => { const id = requestAnimationFrame(() => mapRef.current?.resize()); return () => cancelAnimationFrame(id); }, [layersOpen, detailsOpen, chartsOpen]);
  useEffect(() => { const timer = window.setInterval(() => setCalendarNow(Date.now()), 60_000); return () => clearInterval(timer); }, []);
  useEffect(() => {
    opacityRef.current = opacity;
    const map = mapRef.current; if (!map || !mapReady) return;
    for (const track of TRACKS) for (const id of LAYERS[track.id]) {
      const layer = map.getLayer(id); if (!layer) continue;
      const value = opacity[track.id];
      if (layer.type === "raster") map.setPaintProperty(id, "raster-opacity", value);
      if (layer.type === "fill") map.setPaintProperty(id, "fill-opacity", value);
      if (layer.type === "line") map.setPaintProperty(id, "line-opacity", value);
      if (layer.type === "circle") { map.setPaintProperty(id, "circle-opacity", value * (id.endsWith("glow") ? .2 : 1)); map.setPaintProperty(id, "circle-stroke-opacity", value); }
    }
  }, [opacity, mapReady]);
  useEffect(() => { if (calendarOpen) document.querySelector<HTMLButtonElement>("#archive-calendar button")?.focus(); }, [calendarOpen]);

  useEffect(() => {
    const controller = new AbortController();
    setRiverCoverage(null); setCoverageMessage(""); setCalendarLedger({});
    if (!/^USGS-\d{8,15}$/.test(station)) return () => controller.abort();
    const timer = window.setTimeout(async () => {
      setCoverageMessage("Checking station record…");
      try {
        const response = await fetch(`/api/hydrology/coverage?station=${encodeURIComponent(station)}`, { signal: controller.signal });
        const data = await response.json();
        if (!response.ok || data.station !== station) throw new Error(data.message ?? "Station coverage unavailable");
        if (!controller.signal.aborted) { setRiverCoverage(data); setCoverageMessage(data.message); }
      } catch (error) { if (!controller.signal.aborted) setCoverageMessage(error instanceof Error ? error.message : "Coverage unavailable"); }
    }, 400);
    return () => { clearTimeout(timer); controller.abort(); };
  }, [station]);

  useEffect(() => {
    const controller = new AbortController();
    const day = requested?.slice(0,10) ?? manifest?.start.slice(0,10);
    for (const id of ["counties", "weather", "earthquakes", "shake"] as ContextTrack[]) {
      const date = id === "counties" ? countyEdition : day;
      if (!visible[id] || !date || contextData[id]?.date === date) continue;
      const path = id === "counties" ? `/api/event-atlas/counties?edition=${date}` : id === "weather" ? `/api/event-atlas/weather?day=${date}` : `/api/live-context?feed=${id === "shake" ? "raspberry-shake-stations" : "usgs-earthquakes"}&day=${date}`;
      setContextMessages((current) => ({ ...current, [id]: "Loading source records…" }));
      void fetch(path, { signal: controller.signal }).then(async (response) => {
        const data = await response.json();
        if (!response.ok || data.data?.type !== "FeatureCollection" || !Array.isArray(data.data.features)) throw new Error(data.message ?? data.error ?? "Source response unavailable");
        if (controller.signal.aborted) return;
        sourceFailures.current.delete(`ea-${id}-data`);
        const message = data.limitation ?? data.message ?? `${data.data.features.length} records loaded`;
        setContextData((current) => ({ ...current, [id]: { data: data.data, date, message, source: data.source } }));
        setContextMessages((current) => ({ ...current, [id]: `${data.data.features.length} records · ${date}` }));
      }).catch((error) => { if (!controller.signal.aborted) setContextMessages((current) => ({ ...current, [id]: `Unavailable: ${error.message}` })); });
    }
    return () => controller.abort();
    // Cached records are keyed by their provider date, not by playback position.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [manifest?.start, requested?.slice(0,10), countyEdition, visible.counties, visible.weather, visible.earthquakes, visible.shake]);

  useEffect(() => {
    let disposed = false;
    const cachedUrls = urls.current;
    import("maplibre-gl").then((gl) => {
      if (disposed || !container.current) return;
      gl.setWorkerUrl("/maplibre/maplibre-gl-worker.mjs");
      const budget = browserRenderBudget(); gl.setMaxParallelImageRequests(budget.imageRequests);
      const map = new gl.Map({ container: container.current, style: BASEMAPS.streets.style, center: [-98.35,38.5], zoom: 6, minZoom: 4, maxZoom: 12, maxBounds: [[-104,35],[-92,42]], attributionControl: { compact: true }, pixelRatio: budget.pixelRatio, maxTileCacheSize: budget.tileCache, renderWorldCopies: false });
      mapRef.current = map;
      map.addControl(new gl.NavigationControl({ visualizePitch: false }), "top-right");
      map.addControl(new gl.ScaleControl({ unit: "imperial" }), "bottom-left");
      map.on("load", () => {
        if (disposed) return;
        addRaster(map, "ea-geology", "https://tiles.arcgis.com/tiles/ZOdjAzAQ2B0f85zi/arcgis/rest/services/Kansas_geology/MapServer/tile/{z}/{y}/{x}", 12, "Kansas Geological Survey · cached mapped geology");
        map.addSource("ea-resource-data", { type: "geojson", data: EMPTY });
        map.addLayer({ id: "ea-resources", type: "fill", source: "ea-resource-data", layout: { visibility: "none" }, filter: [">", ["get", "symbols"], 0], paint: { "fill-color": ["interpolate", ["linear"], ["get", "symbols"], 1, "#706334", 10, "#d1ae51", 100, "#ffe195"], "fill-opacity": .65, "fill-outline-color": "#ebd38d" } });
        map.addSource("ea-smoke", { type: "geojson", data: EMPTY });
        for (const id of ["counties", "weather", "earthquakes", "shake"]) map.addSource(`ea-${id}-data`, { type: "geojson", data: EMPTY });
        map.addLayer({ id: "ea-counties", source: "ea-counties-data", type: "fill", layout: { visibility: "none" }, paint: { "fill-color": "#71a9a3", "fill-opacity": .25 } });
        map.addLayer({ id: "ea-county-lines", source: "ea-counties-data", type: "line", layout: { visibility: "none" }, paint: { "line-color": "#b9e9e0", "line-width": 1.3, "line-opacity": .6 } });
        for (const id of ["weather", "earthquakes", "shake"] as const) map.addLayer({ id: `ea-${id}`, source: `ea-${id}-data`, type: "circle", layout: { visibility: "none" }, paint: { "circle-radius": id === "earthquakes" ? ["+", 4, ["*", 2, ["max", 0, ["coalesce", ["get", "magnitude"], 0]]]] : 7, "circle-color": TRACKS.find((track) => track.id === id)!.color, "circle-stroke-color": "#123336", "circle-stroke-width": 1.5 } });
        map.on("click", (event) => {
          const features = map.queryRenderedFeatures(event.point, { layers: ["ea-weather", "ea-earthquakes", "ea-shake", "ea-counties", "ea-river"] });
          const feature = features[0]; if (!feature) return;
          const track = feature.layer.id.replace("ea-", "") as TrackId;
          setInspectedFeature({ track, properties: feature.properties }); setSelectedTrack(track); setDetailsOpen(true); setLayersOpen(false); setPlaying(false);
        });
        map.addLayer({ id: "ea-smoke-fill", source: "ea-smoke", type: "fill", layout: { visibility: "none" }, paint: { "fill-color": ["match", ["get", "density"], "Light", "#e5d9b1", "Medium", "#dca261", "Heavy", "#bd6242", "#a6acaf"], "fill-opacity": .45 } });
        map.addLayer({ id: "ea-smoke-edge", source: "ea-smoke", type: "line", layout: { visibility: "none" }, paint: { "line-color": "#f0c89b", "line-width": 1.2, "line-opacity": .7 } });
        map.addSource("ea-river-data", { type: "geojson", data: EMPTY });
        map.addLayer({ id: "ea-river-glow", source: "ea-river-data", type: "circle", layout: { visibility: "none" }, filter: ["==", ["get", "missing"], false], paint: { "circle-radius": ["+", 12, ["*", 5, ["get", "visualMagnitude"]]], "circle-color": "#70e0ef", "circle-opacity": .2, "circle-blur": .6 } });
        map.addLayer({ id: "ea-river", source: "ea-river-data", type: "circle", layout: { visibility: "none" }, filter: ["==", ["get", "missing"], false], paint: { "circle-radius": ["+", 4, ["*", 2.5, ["get", "visualMagnitude"]]], "circle-color": ["match", ["get", "trend"], "rising", "#5cf1da", "falling", "#729ffa", "#d8f6ff"], "circle-stroke-color": "#ffffff", "circle-stroke-width": 1.5 } });
        setMapReady(true); setMapMessage("Modern OpenStreetMap reference · not historical boundaries");
      });
      map.on("error", (event) => {
        const source = (event as { sourceId?: string }).sourceId;
        if (source?.startsWith("ea-")) { sourceFailures.current.add(source); setSourceErrors((current) => ({ ...current, [source]: "Source image unavailable for this view" })); setPlaying(false); }
        else setMapMessage("Reference map may be incomplete. Source attribution and dated overlays remain separate.");
      });
      map.on("dragstart", () => setPlaying(false)); map.on("zoomstart", () => setPlaying(false));
    }).catch(() => setMapMessage("Map unavailable. WebGL2 and the map runtime are required; the source notes remain readable."));
    return () => { disposed = true; requestRef.current?.abort(); frameRequest.current?.abort(); mapRef.current?.remove(); mapRef.current = null; for (const url of cachedUrls.values()) URL.revokeObjectURL(url); cachedUrls.clear(); };
  }, []);

  useEffect(() => {
    if (selectedTrack !== "geology" || geologyLegend.length) return;
    const controller = new AbortController();
    fetch("/api/event-atlas/geology-legend", { signal: controller.signal }).then(async (response) => {
      if (!response.ok) return; const body = await response.json(); if (!controller.signal.aborted && Array.isArray(body.items)) setGeologyLegend(body.items);
    }).catch(() => undefined);
    return () => controller.abort();
  }, [selectedTrack, geologyLegend.length]);

  useEffect(() => {
    if (!visible.resources) return;
    const controller = new AbortController();
    queueMicrotask(() => { if (!controller.signal.aborted) { setResourceData(null); setResourceMessage("Loading county aggregates…"); } });
    const map = mapRef.current;
    if (map?.getSource("ea-resource-data")) (map.getSource("ea-resource-data") as GeoJSONSource).setData(EMPTY);
    fetch(`/api/event-atlas/resources?edition=${resourceEdition}`, { signal: controller.signal }).then(async (response) => {
      const data = await response.json(); if (!response.ok || data.type !== "FeatureCollection") throw new Error(data.message ?? "Resource context unavailable");
      if (!controller.signal.aborted) { setResourceData(data); setResourceMessage(`${resourceEdition} edition · ${data.features.reduce((sum: number,f: GeoJSON.Feature) => sum + Number(f.properties?.symbols ?? 0),0)} map symbols by county`); }
    }).catch((failure) => { if (!controller.signal.aborted) setResourceMessage(failure instanceof Error ? failure.message : "Resource context unavailable"); });
    return () => controller.abort();
  }, [visible.resources, resourceEdition]);

  const load = useCallback(async (nextStart = start, nextHours = hours, preferredCursor?: string, resolution = riverResolution, automatic = false) => {
    if (!automatic) { followTodayRef.current = false; setFollowToday(false); }
    const calendarDay = nextStart.slice(0, 10);
    const fullDaySweep = nextHours === EVENT_MAX_HOURS && nextStart === `${calendarDay}T00:00`;
    const token = ++generation.current; ++frameGeneration.current;
    requestRef.current?.abort(); frameRequest.current?.abort();
    setCalendarLedger((current) => Object.fromEntries(Object.entries(current).filter(([,entry]) => entry.status !== "checking")));
    setInspectedFeature(null);
    const controller = new AbortController(); requestRef.current = controller;
    if (fullDaySweep) setCalendarLedger((current) => ({ ...current, [calendarDay]: { status: "checking", supportedHours: [] } }));
    setPlaying(false); setLoading(true); setError(""); setCommitted(null); setManifest(null); setRiver(null); setIndex(0); setCursor(null); setSourceErrors({}); hideEventLayers();
    sourceFailures.current.clear(); radarSourceTime.current = null;
    const map = mapRef.current;
    if (map?.getLayer("ea-radar")) map.removeLayer("ea-radar");
    if (map?.getSource("ea-radar-image")) map.removeSource("ea-radar-image");
    for (const url of urls.current.values()) URL.revokeObjectURL(url); urls.current.clear();
    try {
      const response = await fetch(`/api/event-atlas/manifest?${new URLSearchParams({ start: nextStart + ":00Z", hours: String(nextHours) })}`, { signal: controller.signal });
      const data = await response.json();
      if (!response.ok || data.format !== "kfm-event-atlas-v1") throw new Error(data.message ?? "The interval could not be loaded.");
      let bundle: StreamflowBundle | null = null;
      let message = "No station selected";
      if (station) {
        try {
          const hydro = await fetch(`/api/hydrology/streamflow?${new URLSearchParams({ mode: "station", range: "24h", parameter: "00060", station, end: data.end, resolution })}`, { signal: controller.signal });
          const body = await hydro.json(); if (!hydro.ok) throw new Error(body.message ?? "Station data unavailable");
          bundle = parseStreamflowBundle(body); message = bundle.observations.length ? `${bundle.observations.length} samples loaded${bundle.truncated ? " · PARTIAL" : ""}` : "No observations returned for this station and interval";
        } catch (failure) { message = failure instanceof Error ? failure.message : "River observations unavailable"; }
      }
      if (token !== generation.current || controller.signal.aborted) return;
      setRiver(bundle); setLoadedRiverResolution(resolution); setRiverMessage(message); setManifest(data);
      const sequence = eventFrames(data, resolution === "daily" ? [] : bundle?.observations);
      const linked = preferredCursor ?? new URLSearchParams(window.location.search).get("cursor");
      const validCursor = typeof linked === "string"
        && /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{3})?Z$/.test(linked)
        && Number.isFinite(Date.parse(linked))
        && linked >= data.start
        && linked < data.end;
      const nextCursor = validCursor && linked ? linked : data.start;
      setCursor(nextCursor);
      const sequenceIndex = sequence.findIndex((time) => time >= nextCursor);
      setIndex(sequenceIndex >= 0 ? sequenceIndex : Math.max(0, sequence.length - 1));
      if (fullDaySweep) {
        const availability = eventHourAvailability(data, resolution === "daily" ? [] : bundle?.observations, calendarDay);
        const supportedHours = availability.filter((hour) => hour.supported).map((hour) => hour.hour);
        const sourceIncomplete = data.radar.gaps.length > 0 || data.smoke.gaps.length > 0 || Boolean(station && (!bundle || bundle.truncated));
        const status: ArchiveDayStatus = supportedHours.length
          ? sourceIncomplete ? "partial" : "available"
          : sourceIncomplete ? "partial" : "empty";
        setCalendarLedger((current) => ({ ...current, [calendarDay]: {
          status,
          supportedHours,
          message: sourceIncomplete ? "One or more source archives could not be checked." : undefined,
        } }));
      }
    } catch (failure) {
      if (token !== generation.current || controller.signal.aborted) return;
      const message = failure instanceof Error ? failure.message : "Archive unavailable";
      setError(message);
      if (fullDaySweep) setCalendarLedger((current) => ({ ...current, [calendarDay]: { status: "failed", supportedHours: [], message } }));
    }
    finally { if (token === generation.current) setLoading(false); }
  }, [start, hours, station, riverResolution, hideEventLayers]);

  const loadToday = useCallback(() => {
    const today = currentDayStart(); setStart(today); setCalendarAnchor(today.slice(0,10)); setHours(24);
    setFollowToday(true); followTodayRef.current = true;
    void load(today, 24, latestSafeCursor(), riverResolution, true);
  }, [load, riverResolution]);

  useEffect(() => {
    if (!mapReady || initialLoad.current) return;
    initialLoad.current = true;
    if (followTodayRef.current) loadToday();
    else void load();
  }, [mapReady, load, loadToday]);

  useEffect(() => {
    const refresh = () => { if (followTodayRef.current && !document.hidden && !loading && !playing) loadToday(); };
    const timer = window.setInterval(refresh, 300_000);
    const visible = () => { if (start.slice(0,10) !== currentUtcDay()) refresh(); };
    document.addEventListener("visibilitychange", visible);
    return () => { clearInterval(timer); document.removeEventListener("visibilitychange", visible); };
  }, [loadToday, loading, playing, start]);

  const getRadarImage = useCallback(async (time: string, signal: AbortSignal) => {
    const cached = urls.current.get(time); if (cached) return cached;
    const response = await fetch(`/api/event-atlas/radar-frame?time=${encodeURIComponent(time)}`, { signal });
    if (!response.ok || response.headers.get("x-radar-mosaic-time") !== time) throw new Error("The exact radar image could not be confirmed.");
    const blob = await response.blob();
    const bitmap = await createImageBitmap(blob);
    if (bitmap.width !== 1024 || bitmap.height !== 600) { bitmap.close(); throw new Error("Unexpected radar dimensions."); }
    bitmap.close(); if (signal.aborted) throw new Error("Cancelled frame.");
    const url = URL.createObjectURL(blob); urls.current.set(time, url);
    return url;
  }, []);

  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !manifest || !requested || loading) return;
    const token = ++frameGeneration.current;
    frameRequest.current?.abort(); const controller = new AbortController(); frameRequest.current = controller;
    setBuffering(true); setError(""); hideEventLayers(false);
    for (const id of order) if (!visible[id]) for (const layer of LAYERS[id]) if (map.getLayer(layer)) map.setLayoutProperty(layer,"visibility","none");
    const apply = async () => {
      const scan = visible.radar ? radarAt(manifest.radar.scans, requested) : null;
      let imageUrl: string | null = null;
      try { if (scan) imageUrl = await getRadarImage(scan.time, controller.signal); }
      catch (failure) { if (controller.signal.aborted) return; throw failure; }
      if (token !== frameGeneration.current || controller.signal.aborted) return;
      if (imageUrl && radarSourceTime.current !== scan?.time) {
          // Drop the prior texture before creating this exact frame: an image
          // error must never leave old radar pixels under a new timestamp.
          if (map.getLayer("ea-radar")) map.removeLayer("ea-radar");
          if (map.getSource("ea-radar-image")) map.removeSource("ea-radar-image");
          sourceFailures.current.delete("ea-radar-image");
          map.addSource("ea-radar-image", { type: "image", url: imageUrl, coordinates: [[EVENT_BOUNDS[0], EVENT_BOUNDS[3]], [EVENT_BOUNDS[2], EVENT_BOUNDS[3]], [EVENT_BOUNDS[2], EVENT_BOUNDS[1]], [EVENT_BOUNDS[0], EVENT_BOUNDS[1]]] });
          map.addLayer({ id: "ea-radar", type: "raster", source: "ea-radar-image", layout: { visibility: "none" }, paint: { "raster-opacity": opacity.radar, "raster-fade-duration": 0 } });
          radarSourceTime.current = scan?.time ?? null;
      }
      updateGeoJSON(map.getSource("ea-smoke") as GeoJSONSource, smokeAt(manifest.smoke.data, requested));
      updateGeoJSON(map.getSource("ea-river-data") as GeoJSONSource, river ? riverAt(river, requested, loadedRiverResolution) : EMPTY);
      updateGeoJSON(map.getSource("ea-resource-data") as GeoJSONSource, resourceData ?? EMPTY);
      const day = requested.slice(0,10), year = day.slice(0,4);
      for (const id of ["counties", "weather", "earthquakes", "shake"] as ContextTrack[]) {
        const entry = contextData[id];
        let data = entry?.date === (id === "counties" ? countyEdition : day) ? entry.data : EMPTY;
        if (id === "earthquakes") data = { ...data, features: data.features.filter((feature) => Date.parse(String(feature.properties?.observedAt)) <= Date.parse(requested)) };
        if (id === "shake") data = { ...data, features: data.features.filter((feature) => {
          const start = String(feature.properties?.startTime ?? ""), end = String(feature.properties?.endTime ?? "");
          const epoch = (value: string) => Date.parse(/(Z|[+-]\d{2}:\d{2})$/.test(value) ? value : value + "Z");
          return (!start || epoch(start) <= Date.parse(requested)) && (!end || epoch(end) > Date.parse(requested));
        }) };
        updateGeoJSON(map.getSource(`ea-${id}-data`) as GeoJSONSource, data);
      }
      for (const kind of ["flora", "fauna"] as const) {
        const id = `ea-${kind}`, marker = `${year}:${kind}`;
        const source = map.getSource(id) as (ReturnType<GLMap["getSource"]> & { _eventYear?: string });
        if (visible[kind] && (!source || source._eventYear !== marker)) {
          removeLayerSource(map, id);
          addRaster(map, id, `${window.location.origin}/api/event-atlas/tile?kind=${kind}&date=${day}&z={z}&x={x}&y={y}`, 6, "GBIF occurrence contributors · annual generalized records", 1, 512);
          (map.getSource(id) as typeof source)._eventYear = marker;
        }
      }
      const satelliteDay = base === "satellite" && manifest.imagery.dates.includes(day) ? day : null;
      const satellite = map.getSource("ea-satellite") as (ReturnType<GLMap["getSource"]> & { _eventDay?: string });
      if (satelliteDay && (!satellite || satellite._eventDay !== satelliteDay)) {
        removeLayerSource(map, "ea-satellite"); addRaster(map, "ea-satellite", `${window.location.origin}/api/event-atlas/tile?kind=satellite&date=${satelliteDay}&z={z}&x={x}&y={y}`, 9, "NASA GIBS · Terra MODIS daily imagery");
        (map.getSource("ea-satellite") as typeof satellite)._eventDay = satelliteDay;
      }
      // Keep dynamic pixels hidden until the exact image source is ready. No
      // old frame is presented under the newly requested time while buffering.
      await new Promise<void>((resolve, reject) => {
        const sourceIds = ["ea-smoke", "ea-river-data", "ea-resource-data", ...(imageUrl ? ["ea-radar-image"] : [])];
        const check = () => { if (sourceIds.some((id) => sourceFailures.current.has(id))) finish(new Error("A requested source failed; the frame was withheld.")); else if (sourceIds.every((id) => map.isSourceLoaded(id))) finish(); };
        const fail = () => finish(new Error("Radar image loading was cancelled."));
        const timer = window.setTimeout(() => finish(new Error("The requested map sources did not finish loading.")), 15_000);
        const finish = (failure?: Error) => { window.clearTimeout(timer); map.off("sourcedata", check); map.off("error", check); controller.signal.removeEventListener("abort", fail); if (failure) reject(failure); else resolve(); };
        map.on("sourcedata", check); map.on("error", check); controller.signal.addEventListener("abort", fail, { once: true }); check();
      });
      if (token !== frameGeneration.current || controller.signal.aborted) return;
      setBaseDay(satelliteDay);
      if (map.getLayer("ea-satellite")) map.setLayoutProperty("ea-satellite", "visibility", satelliteDay ? "visible" : "none");
      if (map.getLayer("ea-satellite")) { const firstOverlay = map.getStyle().layers.find((l) => l.id.startsWith("ea-") && l.id !== "ea-satellite"); if (firstOverlay) map.moveLayer("ea-satellite", firstOverlay.id); }
      // Reference roads are explicitly modern; they are not shown beneath a
      // failed historical imagery request as a substitute for that acquisition.
      for (const layer of map.getStyle().layers) if (!layer.id.startsWith("ea-") && layer.type !== "background") map.setLayoutProperty(layer.id, "visibility", base === "reference" ? "visible" : "none");
      for (const id of [...order].reverse()) for (const layer of LAYERS[id]) {
        if (!map.getLayer(layer)) continue;
        map.moveLayer(layer);
        map.setLayoutProperty(layer, "visibility", visible[id] && (id !== "radar" || !!imageUrl) ? "visible" : "none");
        const type = map.getLayer(layer)!.type;
        if (type === "raster") map.setPaintProperty(layer, "raster-opacity", opacityRef.current[id]);
        if (type === "fill") map.setPaintProperty(layer, "fill-opacity", opacityRef.current[id]);
        if (type === "line") map.setPaintProperty(layer, "line-opacity", opacityRef.current[id]);
        if (type === "circle") map.setPaintProperty(layer, "circle-opacity", opacityRef.current[id] * (layer.endsWith("glow") ? .2 : 1));
        if (type === "circle") map.setPaintProperty(layer, "circle-stroke-opacity", opacityRef.current[id]);
      }
      setCommitted(requested); setBuffering(false);
      // Bounded look-ahead, never a latest-frame fallback. Keep at most 8
      // decoded URLs; no complete-archive prefetch or unbounded image queue.
      const keep = new Set([scan?.time, ...manifest.radar.scans.filter((s) => s.time > requested).slice(0,2).map((s) => s.time)]);
      for (const [time,url] of urls.current) if (urls.current.size > 8 && !keep.has(time)) { URL.revokeObjectURL(url); urls.current.delete(time); }
      if (visible.radar) for (const next of manifest.radar.scans.filter((s) => s.time > requested).slice(0,2)) void getRadarImage(next.time, controller.signal).catch(() => undefined);
    };
    void apply().catch((failure) => {
      if (token !== frameGeneration.current || controller.signal.aborted) return;
      hideEventLayers(); setBuffering(false); setPlaying(false); setError(failure instanceof Error ? failure.message : "This frame is unavailable.");
    });
    return () => controller.abort();
  }, [manifest, requested, river, loadedRiverResolution, resourceData, contextData, countyEdition, mapReady, visible, order, base, loading, getRadarImage, hideEventLayers]);

  useEffect(() => {
    if (!playing || buffering || loading || !committed || committed !== requested || error) return;
    const timer = window.setTimeout(() => {
      if (index + 1 < frames.length) { setIndex(index + 1); setCursor(frames[index + 1]); }
      else if (loop) { setIndex(0); setCursor(frames[0] ?? null); }
      else setPlaying(false);
    }, 1100 / speed);
    return () => window.clearTimeout(timer);
  }, [playing, buffering, loading, committed, requested, error, index, frames, loop, speed]);

  const jump = (next: number) => {
    followTodayRef.current = false; setFollowToday(false);
    const target = Math.max(0, Math.min(frames.length - 1, next));
    setPlaying(false); setIndex(target); setCursor(frames[target] ?? null);
  };
  const share = async () => {
    if (!manifest) return;
    const loadedHours = Math.ceil((Date.parse(manifest.end) - Date.parse(manifest.start)) / 3_600_000);
    const params = new URLSearchParams({ start: manifest.start.slice(0,16), hours: String(loadedHours <= 1 ? 1 : loadedHours <= 6 ? 6 : 24), station: river?.stations[0]?.stationId ?? "", resolution: loadedRiverResolution, county: countyEdition, base, edition: resourceEdition, order: order.join(","), opacity: TRACKS.map((t) => opacity[t.id]).join(","), layers: order.filter((id) => visible[id]).join(","), ...(committed ? { cursor: committed } : {}) });
    const link = `${window.location.origin}/observatory?${params}`;
    window.history.replaceState(null, "", link);
    try { await navigator.clipboard.writeText(link); setCopied(true); } catch { setCopied(false); setError("The address bar now contains the replay link. Copy it to share this view."); }
  };
  const trackStatus = (id: TrackId) => {
    if (!manifest) return "Not loaded";
    if (sourceErrors[`ea-${id}`]) return "SOURCE TILES PARTIAL / FAILED";
    if (id === "radar") return activeRadar ? `${activeRadar.product.toUpperCase()} · ${activeRadar.time.slice(11,16)} UTC` : "Gap · no supported mosaic";
    if (id === "smoke") return `${activeSmoke.features.length} supported polygons${manifest.smoke.gaps.length ? " · partial archive" : ""}`;
    if (["counties", "weather", "earthquakes", "shake"].includes(id)) return contextMessages[id as ContextTrack] ?? "Enable to load source records";
    if (id === "river") return gauge && !gauge.missing ? `${gauge.displayValue}${loadedRiverResolution === "daily" ? " · daily mean" : ""}` : river ? "Gap · no supported sample at cursor" : riverMessage;
    if (id === "geology") return "Static geology · edition not confirmed";
    if (id === "resources") return resourceMessage;
    return `${committed?.slice(0,4) ?? manifest.start.slice(0,4)} records · coarse hexagons`;
  };
  const calendarCellState = (day: string, hour: number): CalendarCellState => {
    const slot = `${day}T${String(hour).padStart(2, "0")}:00:00.000Z`;
    if (Date.parse(slot) >= calendarNow) return "future";
    const ledger = calendarLedger[day];
    if (!ledger) return "unqueried";
    if (ledger.status === "checking") return "checking";
    if (ledger.status === "failed") return "failed";
    return ledger.supportedHours.includes(hour) ? "supported" : ledger.status === "partial" ? "failed" : "gap";
  };
  const calendarStateLabel = (state: CalendarCellState) => ({
    supported: "one or more observations within this hour; gaps may remain",
    gap: "checked gap; no confirmed dynamic data",
    checking: "checking source coverage",
    failed: "source check failed",
    unqueried: "not checked yet",
    future: "not yet elapsed",
  })[state];
  const calendarDayStatus = (day: string) => {
    const ledger = calendarLedger[day];
    if (!ledger) return day > calendarToday ? "Not yet" : "Not checked";
    if (ledger.status === "checking") return "Checking…";
    if (ledger.status === "failed") return "Check failed";
    if (ledger.status === "empty") return "Checked gap";
    return `${ledger.supportedHours.length}/24 with records${ledger.status === "partial" ? " · partial" : ""}`;
  };
  const selectCalendarSlot = (day: string, hour = 0) => {
    const target = `${day}T${String(hour).padStart(2, "0")}:00:00.000Z`;
    if (Date.parse(target) >= calendarNow) return;
    const dayStart = `${day}T00:00`;
    setPlaying(false); setStart(dayStart); setHours(EVENT_MAX_HOURS); setCalendarAnchor(day);
    const isLoadedDay = manifest?.start === `${dayStart}:00.000Z` && hours === EVENT_MAX_HOURS && !loading && riverResolution === loadedRiverResolution && (!station || river?.stations[0]?.stationId === station);
    if (isLoadedDay) {
      setCursor(target);
      const matchingFrame = frames.findIndex((time) => time >= target);
      if (matchingFrame >= 0) setIndex(matchingFrame);
      return;
    }
    void load(dayStart, EVENT_MAX_HOURS, target);
  };
  const shiftCalendarWeek = (direction: -1 | 1) => {
    const next = advanceEventDay(calendarAnchor, direction * 7);
    if (!next) return;
    const nextWeek = eventWeekDays(next);
    if (!nextWeek.some((day) => day >= EVENT_EARLIEST_DAY && day <= calendarToday)) return;
    setCalendarAnchor(next);
  };
  const previousCalendarAnchor = advanceEventDay(calendarAnchor, -7);
  const nextCalendarAnchor = advanceEventDay(calendarAnchor, 7);
  const canMoveToPreviousWeek = Boolean(previousCalendarAnchor && eventWeekDays(previousCalendarAnchor).some((day) => day >= EVENT_EARLIEST_DAY));
  const canMoveToNextWeek = Boolean(nextCalendarAnchor && eventWeekDays(nextCalendarAnchor).some((day) => day <= calendarToday));

  return <main className="event-workspace">
    <header className="event-header"><div><Link href="/">← Explorer</Link><span>KANSAS FRONTIER MATRIX</span><h1>Event Observatory</h1></div><nav className="event-source-actions"><DataNotices /><Link href="/data">Contribute data</Link><Link href="/stewards">Steward desk</Link><Link href="/observatory/sources" className="event-source-link">Sources & coverage ↗</Link></nav></header>
    <section className="event-calendar-sweep" id="archive-calendar" hidden={!calendarOpen} aria-labelledby="event-calendar-title">
      <div className="event-panel-heading"><strong>Calendar · 24 hours per day</strong><button type="button" onClick={() => setCalendarOpen(false)} aria-label="Close calendar">×</button></div>
      <label className="event-calendar-date">Jump to a date<input type="date" min={EVENT_EARLIEST_DAY} max={calendarToday} value={calendarAnchor} onChange={(event) => { if (eventDayHours(event.target.value).length) setCalendarAnchor(event.target.value); }} /></label>
      <header className="event-calendar-heading"><div><span className="event-kicker">24-HOUR ARCHIVE CALENDAR · UTC</span><h2 id="event-calendar-title">Every date stays selectable. Every hour stays visible.</h2><p>Select a day to load its complete 24-hour window. Checked gaps remain in place as gaps—never zeroes, substitutions, or removed time.</p></div><div className="event-calendar-navigation"><button type="button" onClick={() => shiftCalendarWeek(-1)} disabled={!canMoveToPreviousWeek} aria-label="Show previous calendar week">←</button><strong>{calendarDays.length ? `${calendarDayLabel(calendarDays[0])} – ${calendarDayLabel(calendarDays.at(-1)!)}` : calendarMonthLabel(calendarAnchor)}</strong><button type="button" onClick={() => shiftCalendarWeek(1)} disabled={!canMoveToNextWeek} aria-label="Show next calendar week">→</button></div></header>
      <div className="event-calendar-legend"><span><i data-state="supported" />Confirmed dynamic support</span><span><i data-state="gap" />Checked gap</span><span><i data-state="unqueried" />Not checked</span><span><i data-state="future" />Not yet elapsed</span><small>Archive calendar starts {EVENT_EARLIEST_DAY}; source-specific availability is checked only when that day is loaded.</small></div>
      <div className="event-calendar-scroll"><div className="event-calendar-grid" role="group" aria-label="Seven-day, 24-hour UTC archive calendar">
        <span className="event-calendar-corner" aria-hidden="true">UTC</span>
        {calendarDays.map((day) => {
          const outsideArchive = day < EVENT_EARLIEST_DAY || day > calendarToday;
          return <button key={`day:${day}`} type="button" className="event-calendar-day" data-selected={day === selectedCalendarDay} disabled={outsideArchive} aria-pressed={day === selectedCalendarDay} onClick={() => selectCalendarSlot(day)}><strong>{calendarDayLabel(day)}</strong><small>{day < EVENT_EARLIEST_DAY ? "Before archive" : calendarDayStatus(day)}</small></button>;
        })}
        {calendarHours.map((slot) => <Fragment key={`hour:${slot.hour}`}>
          <span className="event-calendar-hour" aria-hidden="true">{hourLabel(slot.hour)}</span>
          {calendarDays.map((day) => {
            const state = calendarCellState(day, slot.hour);
            const active = requested?.slice(0, 13) === `${day}T${String(slot.hour).padStart(2, "0")}`;
            const disabled = day < EVENT_EARLIEST_DAY || state === "future";
            const glyph = state === "supported" ? "●" : state === "gap" ? "—" : state === "checking" ? "…" : state === "failed" ? "!" : state === "future" ? "·" : "?";
            return <button key={`${day}:${slot.hour}`} type="button" className="event-calendar-cell" data-state={state} data-selected={active} disabled={disabled} aria-current={active ? "time" : undefined} aria-label={`${calendarDayLabel(day)} ${hourLabel(slot.hour)} UTC: ${calendarStateLabel(state)}. ${disabled ? "Unavailable" : "Select this hour and load the day."}`} title={`${calendarDayLabel(day)} ${hourLabel(slot.hour)} UTC · ${calendarStateLabel(state)}`} onClick={() => selectCalendarSlot(day, slot.hour)}><span aria-hidden="true">{glyph}</span></button>;
          })}
        </Fragment>)}
      </div></div>
    </section>
    <form className="event-query" onSubmit={(event) => { event.preventDefault(); void load(); }}>
      <label>Exact start · UTC<input type="datetime-local" value={start} min={`${EVENT_EARLIEST_DAY}T00:00`} max={`${calendarToday}T23:55`} step="300" onChange={(event) => { followTodayRef.current = false; setFollowToday(false); setPlaying(false); setStart(event.target.value); }} required /></label>
      <label>Window<select value={hours} onChange={(event) => { setPlaying(false); setHours(Number(event.target.value)); }}><option value={1}>1 hour</option><option value={6}>6 hours</option><option value={24}>24 hours</option></select></label>
      <label>USGS station<input value={station} onChange={(event) => { setPlaying(false); setStation(event.target.value); }} pattern="USGS-[0-9]{8,15}" placeholder="USGS-06889000" aria-label="USGS station identifier for historical discharge" /></label>
      <label>River records<select value={riverResolution} onChange={(event) => { setPlaying(false); setRiverResolution(event.target.value as typeof riverResolution); setCalendarLedger({}); }}><option value="continuous">Continuous samples</option><option value="daily">Daily means · older archive</option></select></label>
      <button className="event-primary" disabled={loading || !mapReady}>{loading ? "Reading archives…" : "Load exact interval"}</button>
      <button type="button" onClick={() => { const value = new Date(Date.now() - 3_600_000); value.setUTCMinutes(Math.floor(value.getUTCMinutes()/5)*5,0,0); const s = value.toISOString().slice(0,16); setStart(s); setHours(1); void load(s,1); }}>Recent hour</button>
      <button type="button" onClick={share} disabled={!committed}>{copied ? "Replay link copied" : "Share replay"}</button>
    </form>
    <div className="event-record-range"><span>{riverCoverage ? `${riverResolution === "daily" ? "Daily means" : "Continuous"}: ${riverCoverage[riverResolution]?.start.slice(0,10) ?? "no declared record"} → ${riverCoverage[riverResolution]?.end.slice(0,10) ?? "—"}${riverCoverage.partial ? " · partial metadata" : ""}` : coverageMessage || "Choose a station to discover its record"}</span><button type="button" disabled={!riverCoverage?.daily || loading} onClick={() => { const day = riverCoverage?.daily?.start.slice(0,10); if (!day) return; setRiverResolution("daily"); setStart(`${day}T00:00`); setHours(24); void load(`${day}T00:00`,24,undefined,"daily"); }}>Oldest daily record</button><button type="button" disabled={!riverCoverage?.continuous || loading} onClick={() => { const day = riverCoverage?.continuous?.start.slice(0,10); if (!day) return; setRiverResolution("continuous"); setStart(`${day}T00:00`); setHours(24); void load(`${day}T00:00`,24,undefined,"continuous"); }}>Oldest continuous</button><button type="button" disabled={loading} onClick={loadToday}>{followToday ? "Following today · refreshes every 5 min" : "Follow today / latest"}</button></div>
    <nav className="event-map-toolbar" aria-label="Map panels"><button type="button" aria-expanded={layersOpen} onClick={() => { setLayersOpen(!layersOpen); setDetailsOpen(false); setCalendarOpen(false); }}>Layers · {Object.values(visible).filter(Boolean).length}</button><button type="button" aria-expanded={calendarOpen} aria-controls="archive-calendar" onClick={() => { setCalendarOpen(!calendarOpen); setLayersOpen(false); setDetailsOpen(false); }}>Calendar</button><button type="button" onClick={() => { const day = advanceEventDay(selectedCalendarDay, -1); if (day && day >= EVENT_EARLIEST_DAY) selectCalendarSlot(day); }} disabled={selectedCalendarDay <= EVENT_EARLIEST_DAY}>← Day</button><button type="button" onClick={() => selectCalendarSlot(selectedCalendarDay)}>Load full 24 hours</button><button type="button" onClick={() => { const day = advanceEventDay(selectedCalendarDay, 1); if (day && day <= calendarToday) selectCalendarSlot(day); }} disabled={selectedCalendarDay >= calendarToday}>Day →</button><span /><button type="button" aria-expanded={chartsOpen} onClick={() => setChartsOpen(!chartsOpen)}>Charts</button><button type="button" aria-expanded={detailsOpen} onClick={() => { setDetailsOpen(!detailsOpen); setLayersOpen(false); setCalendarOpen(false); }}>Sources & quality</button></nav>
    <section className="event-body" data-layers-open={layersOpen} data-details-open={detailsOpen}>
      <aside className="event-mixer" hidden={!layersOpen} aria-label="Animation layer mixer"><div className="event-panel-heading"><strong>Layers & opacity</strong><button type="button" onClick={() => setLayersOpen(false)} aria-label="Close layers">×</button></div><div className="event-section-heading"><span>LAYER MIXER</span><small>Top row draws on top</small></div>
        {order.map((id, position) => { const track = TRACKS.find((t) => t.id === id)!; return <article key={id} className="event-track" data-selected={selectedTrack === id} style={{ "--track-color": track.color } as React.CSSProperties}>
          <div className="event-track-title"><input type="checkbox" checked={visible[id]} aria-label={`Show ${track.name}`} onChange={(event) => { setPlaying(false); setVisible((current) => ({ ...current, [id]: event.target.checked })); }} /><button type="button" onClick={() => { setPlaying(false); setSelectedTrack(id); setDetailsOpen(true); setLayersOpen(false); }}>{track.name}</button><span aria-hidden="true">●</span></div>
          <small>{track.axis}</small><p>{trackStatus(id)}</p>

          <div className="event-track-controls"><input type="range" min="0" max="1" step="0.05" value={opacity[id]} onChange={(event) => { setPlaying(false); setOpacity((current) => ({ ...current, [id]: Number(event.target.value) })); }} aria-label={`${track.name} opacity`} /><output>{Math.round(opacity[id]*100)}%</output><button type="button" disabled={position === 0} aria-label={`Move ${track.name} up`} onClick={() => { setPlaying(false); setOrder((current) => { const next = [...current]; [next[position-1],next[position]]=[next[position],next[position-1]]; return next; }); }}>↑</button><button type="button" disabled={position === order.length-1} aria-label={`Move ${track.name} down`} onClick={() => { setPlaying(false); setOrder((current) => { const next = [...current]; [next[position+1],next[position]]=[next[position],next[position+1]]; return next; }); }}>↓</button></div>
        </article>; })}
        <label className="event-base-choice">County baseline edition<select value={countyEdition} onChange={(event) => { setPlaying(false); setCountyEdition(event.target.value); setInspectedFeature(null); }}><option value="2020">2020 Census · all 105 counties</option><option value="2010">2010 Census · all 105 counties</option></select></label>
        <label className="event-base-choice">Map beneath the layers<select value={base} onChange={(event) => { setPlaying(false); setBase(event.target.value as typeof base); }}><option value="reference">Modern reference map</option><option value="satellite">Historical daily satellite imagery</option></select></label>
        {visible.resources && <label className="event-base-choice">Resource-map edition (independent clock)<input type="number" min="1934" max="1996" value={resourceEdition} onChange={(event) => { setPlaying(false); setResourceEdition(event.target.value); }} /></label>}
        <p className="event-small">Daily imagery is acquisition-dated, not historical roads or boundaries. Geology and annual occurrences keep their own clocks.</p>
      </aside>
      <section className="event-map-panel" aria-label="Layered historical Kansas map"><div ref={container} className="event-map" />
        <div className="event-map-caption"><span>{base === "satellite" ? baseDay ? `NASA MODIS · acquisition day ${baseDay}${sourceErrors["ea-satellite"] ? " · tiles partial / failed" : ""}` : "No confirmed imagery for this date" : mapMessage}</span><strong>{committed ? timestamp(committed) : "Choose an interval to begin"}</strong><small>{localTimestamp(committed)}</small></div>
        {(loading || buffering) && <div className="event-buffer" role="status">{loading ? "Reading dated source records…" : `Buffering ${requested?.slice(11,19)} UTC · temporal pixels withheld`}</div>}
        {error && <div className="event-error" role="alert">{error}{manifest && <button type="button" onClick={() => { setVisible((current) => ({ ...current, radar: false })); setError(""); }}>Continue without radar</button>}</div>}
        {!manifest && !loading && <div className="event-intro"><span>THE PAST, IN MOTION</span><h2>Layer an event.<br />See what changed.</h2><p>Choose a date or start with a Kansas archive window. Every layer states the time it actually represents.</p>{PRESETS.map((preset) => <button key={preset.start} type="button" disabled={!mapReady} onClick={() => { setStart(preset.start); setHours(preset.hours); void load(preset.start,preset.hours); }}>{preset.label} <span>↗</span></button>)}</div>}
        <div className="event-map-legend"><span><i style={{background:"#70e0ef"}} />Discharge radius: log-scaled · color: sample trend</span><span><i style={{background:"#dca261"}} />HMS: light → medium → heavy · gray unknown</span><span>Radar colors: source reflectivity · <a href="https://mesonet.agron.iastate.edu/docs/nexrad_composites/" target="_blank" rel="noreferrer">product legend ↗</a></span></div>
      </section>
      <aside className="event-inspector" hidden={!detailsOpen}><div className="event-panel-heading"><strong>Sources & quality</strong><button type="button" onClick={() => setDetailsOpen(false)} aria-label="Close sources">×</button></div><select aria-label="Inspect a source" value={selectedTrack} onChange={(event) => setSelectedTrack(event.target.value as TrackId)}>{TRACKS.map((track) => <option key={track.id} value={track.id}>{track.name}</option>)}</select><span className="event-kicker">LAYER PASSPORT</span><h2>{chosen.name}</h2><p>{chosen.detail}</p><dl><div><dt>Clock</dt><dd>{chosen.axis}</dd></div><div><dt>Current support</dt><dd>{trackStatus(chosen.id)}</dd></div><div><dt>Archive query</dt><dd>{manifest ? `${timestamp(manifest.start)} → ${timestamp(manifest.end)} (end excluded)` : "Not loaded"}</dd></div><div><dt>Retrieved</dt><dd>{manifest ? timestamp(manifest.retrievedAt) : "Not yet"}</dd></div></dl><a href={chosen.source} target="_blank" rel="noreferrer">Inspect source & method ↗</a>
{contextData[chosen.id as ContextTrack] && <p>{contextData[chosen.id as ContextTrack]?.message}</p>}
        {chosen.id === "river" && <p>{loadedRiverResolution === "daily" ? "Daily mean is pinned to its source date. It does not describe changes within the day." : "Continuous samples are held at most 30 minutes. Gaps stay empty."}</p>}
        {inspectedFeature?.track === chosen.id && <section className="event-feature-values"><h3>{String(inspectedFeature.properties.name ?? inspectedFeature.properties.stationName ?? "Selected record")}</h3><dl>{Object.entries(inspectedFeature.properties).filter(([key]) => ["geoid", "population", "housingUnits", "landSquareMiles", "waterSquareMiles", "vintage", "station", "network", "startTime", "endTime", "day", "maximumF", "minimumF", "precipitationInches", "magnitude", "observedAt", "depthKilometers", "approvalStatus"].includes(key)).map(([key,value]) => <div key={key}><dt>{({ geoid: "County FIPS", population: "Population", housingUnits: "Housing units", landSquareMiles: "Land · sq mi", waterSquareMiles: "Water · sq mi", maximumF: "Daily max · °F", minimumF: "Daily min · °F", precipitationInches: "Daily rain · in", vintage: "Census edition", startTime: "Station epoch start", endTime: "Station epoch end", observedAt: "Observation time", depthKilometers: "Depth · km" } as Record<string,string>)[key] ?? key}</dt><dd>{value === null ? "Not supplied" : typeof value === "number" ? value.toLocaleString("en-US", { maximumFractionDigits: 2 }) : String(value)}</dd></div>)}</dl></section>}
        {chosen.id === "shake" && <a href="https://stationview.raspberryshake.org/" target="_blank" rel="noreferrer">Open Raspberry Shake waveform viewer ↗</a>}
        {chosen.id === "radar" && activeRadar && <a href={activeRadar.artifact} target="_blank" rel="noreferrer">Exact mosaic artifact ↗</a>}
        {chosen.id === "smoke" && <p className="event-small">Actual footprint changes are replayed without morphing. Wind tracers and 3D smoke require a verified modeled field and are not supplied by HMS polygons.</p>}
        {chosen.id === "river" && gauge && <p className="event-small">Sample: {timestamp(gauge.observedAt)}. Approval: {gauge.approvalStatus ?? "not supplied"}. Qualifiers: {gauge.qualifiers.join(", ") || "none supplied"}. Trend compares only supported neighboring samples; radius is log-scaled display, not channel width.</p>}
        {manifest && <div className="event-coverage"><h3>Coverage ledger</h3><p>{manifest.radar.scans.length} actual radar artifacts</p><p>{manifest.smoke.data.features.length} smoke intervals intersect Kansas</p><p>{manifest.imagery.dates.length} confirmed satellite acquisition days</p>{manifest.radar.gaps.length > 0 && <p>Radar listing unavailable: {manifest.radar.gaps.join(", ")}</p>}{manifest.smoke.gaps.length > 0 && <p>Smoke file unavailable: {manifest.smoke.gaps.join(", ")}</p>}<small>No data ≠ zero. Displayed sources may be revised by their providers.</small></div>}
        {chosen.id === "geology" && <a href="https://tiles.arcgis.com/tiles/ZOdjAzAQ2B0f85zi/arcgis/rest/services/Kansas_geology/MapServer/legend?f=pjson" target="_blank" rel="noreferrer">Exact KGS raster unit legend ↗</a>}
        {chosen.id === "geology" && geologyLegend.length > 0 && <div className="event-geology-legend">{geologyLegend.map((item,index) => <div key={index}><img src={item.image} alt="" width="20" height="20" /><span>{item.label}</span></div>)}</div>}
        {chosen.id === "resources" && <p className="event-small">County color: 1 → 10 → 100+ map symbols (dark → pale gold). Uncolored counties have no returned symbol for this edition, not proof of no resources.</p>}
        <div className="event-next"><h3>Source-grounded, not simulated</h3><p>No invented storms, smoke transport, animal paths, or resource deposits. Static and annual layers are pinned context alongside the event clock.</p><Link href="/observatory/sources">Research findings & remaining connections →</Link></div>
      </aside>
    </section>
    <footer className="event-timeline"><section className="event-transport"><div><span className="event-kicker">SHARED EVENT CLOCK</span><strong>{timestamp(committed)}</strong><small>{buffering ? "Requested frame is still loading" : `${frames.length} observation times / interval boundaries · no interpolation`}</small></div><div className="event-play-buttons"><button type="button" onClick={() => jump(index-1)} disabled={!frames.length || index===0}>←</button><button type="button" className="event-primary" disabled={!frames.length || !mapReady || loading || !!error || reduced} onClick={() => { if (!playing && index === frames.length-1) { setIndex(0); setCursor(frames[0] ?? null); } setPlaying(!playing); }}>{playing ? "Pause" : "Play"}</button><button type="button" onClick={() => jump(index+1)} disabled={!frames.length || index===frames.length-1}>→</button><label>Speed<select value={speed} onChange={(event) => setSpeed(Number(event.target.value))}><option value={.5}>0.5×</option><option value={1}>1×</option><option value={2}>2×</option></select></label><label><input type="checkbox" checked={loop} onChange={(event) => setLoop(event.target.checked)} /> Loop</label></div></section>
      <input className="event-scrubber" type="range" min="0" max={Math.max(0,frames.length-1)} value={index} disabled={!frames.length} onChange={(event) => jump(Number(event.target.value))} aria-label="Scrub actual event times" aria-valuetext={requested ?? "No interval loaded"} />
      {chartsOpen && manifest && <div className="event-support-tracks" aria-label="Temporal coverage ribbons; dark spans are gaps">{([
        { name: "Radar", color: "#81dec0", intervals: manifest.radar.scans.map((s) => [s.time, new Date(Date.parse(s.time)+300_000).toISOString()]) },
        { name: "Smoke", color: "#dfb580", intervals: manifest.smoke.data.features.map((f) => [f.properties.start,f.properties.end]) },
        { name: "River", color: "#7edceb", intervals: (loadedRiverResolution === "daily" ? [] : series).filter((o) => o.value !== null).map((o) => [o.observedAt,new Date(Date.parse(o.observedAt)+30*60_000).toISOString()]) },
      ]).map((track) => <div key={track.name}><span>{track.name}</span><div>{track.intervals.map(([from,to],i) => { const duration = Date.parse(manifest.end)-Date.parse(manifest.start), left = Math.max(0,Date.parse(from)-Date.parse(manifest.start))/duration*100, right = Math.min(duration,Date.parse(to)-Date.parse(manifest.start))/duration*100; return <button key={i} type="button" aria-label={`${track.name} supported ${timestamp(from)} to ${timestamp(to)}`} title={`${timestamp(from)} → ${timestamp(to)}`} style={{left:`${left}%`,width:`${Math.max(0,right-left)}%`,background:track.color}} onClick={() => jump(Math.max(0,frames.findIndex((t) => t >= from)))} />; })}{committed && <i style={{left:`${(Date.parse(committed)-Date.parse(manifest.start))/(Date.parse(manifest.end)-Date.parse(manifest.start))*100}%`}} />}</div></div>)}</div>}
      <div className="event-range-labels"><span>{manifest?.start.slice(0,16).replace("T"," ")} UTC</span><span>{reduced ? "Reduced motion: use Previous, Next, or scrub" : "Pauses on map interaction, hidden tab, source failure, or Escape"}</span><span>{manifest?.end.slice(0,16).replace("T"," ")} UTC</span></div>
      {chartsOpen && series.length > 0 && <section className="event-hydrograph"><div><strong>{river?.stations[0]?.name}</strong><span>{gauge?.displayValue ?? "No supported value"} · sample {gauge?.observedAt?.slice(11,19) ?? "—"} UTC</span><small>Discharge · ft³/s · {numbers.length ? `${Math.min(...numbers).toLocaleString()}–${Math.max(...numbers).toLocaleString()}` : "no values"} · gaps &gt;30 min are broken</small></div><svg viewBox="0 0 520 100" role="img" aria-label="Historical streamflow hydrograph with gaps"><title>Selected station discharge over the loaded interval</title>{graph.map((segment,index) => <path key={index} d={segment.path} fill="none" stroke="#70e0ef" strokeWidth="2" />)}{committed && series.length > 1 && <line x1={7+(Date.parse(committed)-Date.parse(series[0].observedAt))/(Date.parse(series.at(-1)!.observedAt)-Date.parse(series[0].observedAt))*506} x2={7+(Date.parse(committed)-Date.parse(series[0].observedAt))/(Date.parse(series.at(-1)!.observedAt)-Date.parse(series[0].observedAt))*506} y1="0" y2="100" stroke="#f2d59a" strokeDasharray="3 3" />}</svg></section>}
    </footer>
  </main>;
}
