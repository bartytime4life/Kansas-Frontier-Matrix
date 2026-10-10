"use client";

import { useCallback, useEffect, useMemo, useRef, useState, type RefObject } from "react";
import type { Map as MapLibreMap } from "./maplibre-seam";
import {
  SOIL_GEOLOCATION_NOTICE,
  SOIL_GLOBAL_BOUNDS_WGS84,
  SOIL_GUIDE_URL,
  SOIL_METADATA_URL,
  SOIL_PRODUCT_METADATA,
  SOIL_VIEWS,
  soilLegendUrl,
  soilVisualOpacities,
  soilVisualTransition,
  type SoilVisualTransitionKind,
  type SoilView,
  type SoilMapState,
} from "./soil-moisture";

const SOURCES = ["external-nasa-smap-soil-a", "external-nasa-smap-soil-b"] as const;
const LAYERS = ["external-nasa-smap-soil-raster-a", "external-nasa-smap-soil-raster-b"] as const;
type RasterSlot = { index: 0 | 1; day: string; view: SoilView };
const EMPTY_DAYS: readonly string[] = [];
type Depth = "surface" | "root";
type Availability = {
  state: "available" | "unavailable" | "error";
  availableDays: string[];
  latestCommonDay: string | null;
  checkedAt?: string;
  backend?: { state: "ok" | "error"; durationMs: number; cache: "hit" | "miss" | "none"; code?: string };
};
type MapState = {
  state: "off" | "loading" | "blending" | "rendered" | "partial" | "error";
  loaded: number;
  failed: number;
  renderedAt: string | null;
  day: string | null;
  view: SoilView | null;
  visibleDay?: string;
  fromDay?: string;
  toDay?: string;
  transitionKind?: SoilVisualTransitionKind;
  transitionFraction?: number;
};
const OFF: MapState = { state: "off", loaded: 0, failed: 0, renderedAt: null, day: null, view: null };
const utcFrame = (day: string) => day ? day + "T12:00:00Z" : null;

export type SoilMoistureEngineContext = Readonly<{
  enabled: boolean;
  availabilityState: Availability["state"] | "unchecked";
  mapState: MapState["state"];
  selectedView: SoilView;
  selectedDepthCm: readonly [number, number];
  selectedUtcDay: string | null;
  selectedFrameTimeUtc: string | null;
  renderedFrameTimeUtc: string | null;
  renderedAtUtc: string | null;
  retainedFrameTimeUtc: string | null;
  visualTransition: null | Readonly<{ fromFrameTimeUtc: string; toFrameTimeUtc: string; fraction: number; kind: SoilVisualTransitionKind; numericInterpolation: false }>;
  displaySmoothing: "visual blend and bilinear color resampling" | "exact daily image cells";
  playing: boolean;
  rangeStartUtcDay: string | null;
  rangeEndUtcDay: string | null;
  rangeFrameCount: number;
  availableFrameCount: number;
  latestAvailableUtcDay: string | null;
  sourceCheckedAtUtc: string | null;
  product: typeof SOIL_PRODUCT_METADATA.product;
  version: typeof SOIL_PRODUCT_METADATA.version;
  displayCadence: typeof SOIL_PRODUCT_METADATA.displayCadence;
  nativeCadence: typeof SOIL_PRODUCT_METADATA.nativeCadence;
  nativeFormat: typeof SOIL_PRODUCT_METADATA.nativeFormat;
  approximateResolutionKm: typeof SOIL_PRODUCT_METADATA.approximateResolutionKm;
  coverageBoundsWgs84: readonly [number, number, number, number];
  evidenceRole: typeof SOIL_PRODUCT_METADATA.role;
  dataKind: typeof SOIL_PRODUCT_METADATA.dataKind;
  numericPixelsAvailable: false;
  qualityNotice: string | null;
  sourceUrl: string;
  productGuideUrl: string;
}>;

export function SoilMoistureControl({
  mapRef,
  styleReady,
  onEngineContextChange,
  state,
  onChange,
}: {
  mapRef: RefObject<MapLibreMap | null>;
  styleReady: boolean;
  state: SoilMapState;
  onChange: (next: Partial<SoilMapState>) => void;
  onEngineContextChange?: (context: SoilMoistureEngineContext) => void;
}) {
  const { visible: enabled, day, opacity, view } = state;
  const depth: Depth = view.startsWith("surface") ? "surface" : "root";
  const uncertainty = view.endsWith("uncertainty");
  const setEnabled = useCallback((visible: boolean) => onChange({ visible }), [onChange]);
  const setDay = useCallback((day: string) => onChange({ day }), [onChange]);
  const setOpacity = (opacity: number) => onChange({ opacity });
  const setDepth = (depth: Depth) => onChange({ view: (uncertainty ? depth + "-uncertainty" : depth) as SoilView });
  const setUncertainty = (value: boolean) => onChange({ view: (value ? depth + "-uncertainty" : depth) as SoilView });
  const [range, setRange] = useState({ from: "", through: "" });
  const [playing, setPlaying] = useState(false);
  const [speed, setSpeed] = useState<0.5 | 1 | 2>(1);
  const [reducedMotion, setReducedMotion] = useState(false);
  const [presentation, setPresentation] = useState<"smooth" | "exact">("smooth");
  const [availability, setAvailability] = useState<Availability | null>(null);
  const [checking, setChecking] = useState(false);
  const [mapState, setMapState] = useState<MapState>(OFF);
  const requestId = useRef(0);
  const currentSlotRef = useRef<RasterSlot | null>(null);
  const animationRef = useRef<number | null>(null);
  const opacityRef = useRef(opacity);
  const availableDays = availability?.availableDays ?? EMPTY_DAYS;
  const orderedDays = useMemo(() => [...availableDays].reverse(), [availableDays]);
  const rangeDays = useMemo(() => orderedDays.filter(value => value >= range.from && value <= range.through), [orderedDays, range]);
  const frameIndex = Math.max(0, rangeDays.indexOf(day));
  const sourceFrame = utcFrame(day);
  const renderedFrame = mapState.state === "rendered" && mapState.day === day && mapState.view === view && mapState.renderedAt ? sourceFrame : null;
  // Playback may step past a frame with failed tiles; only a complete frame is reported as rendered.
  const frameSettled = (mapState.state === "rendered" || mapState.state === "partial") && mapState.day === day && mapState.view === view;
  const knownIssue = day >= SOIL_GEOLOCATION_NOTICE.startDay && day <= SOIL_GEOLOCATION_NOTICE.endDay;
  const qualityNotice = knownIssue
    ? "NSIDC flagged this date for a geolocation issue; check its current reprocessing notice before analysis."
    : null;

  const clearRaster = useCallback(() => {
    const map = mapRef.current;
    if (animationRef.current !== null) window.cancelAnimationFrame(animationRef.current);
    animationRef.current = null;
    currentSlotRef.current = null;
    if (!map) return;
    for (const layer of LAYERS) if (map.getLayer(layer)) map.removeLayer(layer);
    for (const source of SOURCES) if (map.getSource(source)) map.removeSource(source);
  }, [mapRef]);

  const chooseDay = useCallback((next: string, pause = true) => {
    if (pause) setPlaying(false);
    if (next === day) return;
    setMapState({ ...OFF, state: "loading", day: next, view });
    setDay(next);
  }, [day, view]);

  const checkAvailability = useCallback(async (retry = false) => {
    const id = ++requestId.current;
    setChecking(true);
    setPlaying(false);
    try {
      const response = await fetch("/api/soil-moisture/availability" + (retry ? "?retry=1" : ""), { cache: "no-store" });
      const data = await response.json() as Availability;
      if (id !== requestId.current) return;
      if (!response.ok || data.state === "error" || !Array.isArray(data.availableDays)) throw new Error("NASA availability failed.");
      setAvailability(data);
      const ordered = [...data.availableDays].reverse();
      const latest = ordered.at(-1) ?? "";
      const from = range.from && ordered.includes(range.from) ? range.from : ordered[Math.max(0, ordered.length - 14)] ?? "";
      const through = range.through && ordered.includes(range.through) && range.through >= from ? range.through : latest;
      const nextDay = ordered.includes(day) && day >= from && day <= through ? day : through;
      setRange({ from, through });
      setDay(nextDay);
      if (nextDay !== day) clearRaster();
    } catch {
      if (id !== requestId.current) return;
      clearRaster();
      setAvailability({ state: "error", availableDays: [], latestCommonDay: null, backend: { state: "error", durationMs: 0, cache: "none", code: "NASA_AVAILABILITY_FAILED" } });
      setDay("");
      setRange({ from: "", through: "" });
      setMapState({ ...OFF, state: "error" });
    } finally {
      if (id === requestId.current) setChecking(false);
    }
  }, [clearRaster, day, range.from, range.through]);

  const displayState = enabled && checking ? "loading" : mapState.state;

  useEffect(() => {
    const media = window.matchMedia("(prefers-reduced-motion: reduce)");
    const update = () => {
      setReducedMotion(media.matches);
      if (media.matches) setPlaying(false);
    };
    update();
    media.addEventListener("change", update);
    return () => media.removeEventListener("change", update);
  }, []);

  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    if (!styleReady) { clearRaster(); return; }
    if (!enabled) {
      clearRaster();
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setMapState(OFF);
      return;
    }
    if (!day || !availableDays.includes(day)) {
      clearRaster();
      setMapState({ ...OFF, state: "error", day, view });
      return;
    }
    const incumbent = currentSlotRef.current;
    if (incumbent && !map.getLayer(LAYERS[incumbent.index])) currentSlotRef.current = null;
    const previous = currentSlotRef.current;
    if (previous?.day === day && previous.view === view) return;
    const index: 0 | 1 = previous?.index === 0 ? 1 : 0;
    const source = SOURCES[index];
    const layer = LAYERS[index];
    if (map.getLayer(layer)) map.removeLayer(layer);
    if (map.getSource(source)) map.removeSource(source);
    let active = true;
    let settled = false;
    let loaded = 0;
    let failed = 0;
    let progress = 0;
    setMapState({ state: "loading", loaded: 0, failed: 0, renderedAt: null, day, view, visibleDay: previous?.day });
    try {
      const tileUrl = "/api/soil-moisture/tile?view=" + view + "&day=" + day + "&z={z}&x={x}&y={y}";
      map.addSource(source, {
        type: "raster", tiles: [tileUrl], tileSize: 256, minzoom: 0, maxzoom: 6,
        bounds: SOIL_GLOBAL_BOUNDS_WGS84,
        attribution: "NASA GIBS · SMAP SPL4SMAU V008",
      });
      map.addLayer({
        id: layer, type: "raster", source,
        paint: { "raster-opacity": 0, "raster-fade-duration": 0, "raster-resampling": presentation === "smooth" ? "linear" : "nearest" },
      }, map.getLayer("external-census-counties-fill") ? "external-census-counties-fill" : undefined);
    } catch {
      if (map.getLayer(layer)) map.removeLayer(layer);
      if (map.getSource(source)) map.removeSource(source);
      setMapState({ ...OFF, state: "error", day, view });
      setPlaying(false);
      return;
    }
    const removeSlot = (slot: RasterSlot) => {
      if (map.getLayer(LAYERS[slot.index])) map.removeLayer(LAYERS[slot.index]);
      if (map.getSource(SOURCES[slot.index])) map.removeSource(SOURCES[slot.index]);
    };
    const finish = () => {
      if (!active) return;
      animationRef.current = null;
      map.setPaintProperty(layer, "raster-opacity", opacityRef.current);
      if (previous) removeSlot(previous);
      currentSlotRef.current = { index, day, view };
      setMapState({ state: failed ? "partial" : "rendered", loaded, failed, renderedAt: new Date().toISOString(), day, view });
    };
    const onData = (event: unknown) => {
      const item = event as { sourceId?: string; tile?: { state?: string }; coord?: unknown };
      if (!active || item.sourceId !== source || item.tile?.state !== "loaded" || !item.coord) return;
      loaded += 1;
      if (!settled) setMapState(current => current.day === day && current.view === view
        ? { ...current, loaded } : current);
    };
    const onError = (event: unknown) => {
      const item = event as { sourceId?: string };
      if (!active || item.sourceId !== source) return;
      failed += 1;
      setPlaying(false);
      // A tile can still fail after the frame settles (a later pan or zoom).
      // Report the gap instead of continuing to claim a complete frame.
      if (settled) {
        setMapState(current => current.day === day && current.view === view && current.state !== "blending"
          ? { ...current, failed, state: "partial" } : current);
        return;
      }
      if (!previous && loaded > 0 && map.getLayer(layer)) {
        map.setPaintProperty(layer, "raster-opacity", opacityRef.current);
        currentSlotRef.current = { index, day, view };
      }
      setMapState(current => current.day === day && current.view === view
        ? { ...current, failed, state: loaded ? "partial" : "error" } : current);
    };
    const onRender = () => {
      if (!active || settled || failed || !loaded || !map.getLayer(layer) || !map.isSourceLoaded(source)) return;
      settled = true;
      if (!previous || presentation === "exact" || reducedMotion) { finish(); return; }
      const kind = soilVisualTransition(previous.day, day, previous.view === view);
      const duration = 1350 / speed;
      let startedAt: number | null = null;
      let lastBucket = -1;
      const animate = (now: number) => {
        if (!active || !map.getLayer(layer)) return;
        if (startedAt === null) startedAt = now;
        progress = Math.min(1, (now - startedAt) / duration);
        const [oldOpacity, nextOpacity] = soilVisualOpacities(kind, progress, opacityRef.current);
        map.setPaintProperty(layer, "raster-opacity", nextOpacity);
        if (map.getLayer(LAYERS[previous.index])) map.setPaintProperty(LAYERS[previous.index], "raster-opacity", oldOpacity);
        const bucket = Math.floor(progress * 8);
        if (bucket !== lastBucket) {
          lastBucket = bucket;
          setMapState({ state: "blending", loaded, failed, renderedAt: null, day, view,
            fromDay: previous.day, toDay: day, transitionKind: kind, transitionFraction: progress });
        }
        if (progress < 1) animationRef.current = window.requestAnimationFrame(animate);
        else finish();
      };
      animationRef.current = window.requestAnimationFrame(animate);
    };
    map.on("sourcedata", onData);
    map.on("error", onError);
    map.on("render", onRender);
    return () => {
      active = false;
      map.off("sourcedata", onData);
      map.off("error", onError);
      map.off("render", onRender);
      if (animationRef.current !== null) window.cancelAnimationFrame(animationRef.current);
      animationRef.current = null;
      if (currentSlotRef.current?.index !== index) {
        // Preserve whichever complete image is visually dominant during rapid scrubbing.
        if (settled && progress >= 0.5 && map.getLayer(layer)) {
          if (previous) removeSlot(previous);
          map.setPaintProperty(layer, "raster-opacity", opacityRef.current);
          currentSlotRef.current = { index, day, view };
        } else {
          removeSlot({ index, day, view });
          if (previous && map.getLayer(LAYERS[previous.index])) map.setPaintProperty(LAYERS[previous.index], "raster-opacity", opacityRef.current);
        }
      }
    };
  // Opacity updates below avoid reloading tiles when the slider moves.
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [availableDays, clearRaster, day, enabled, presentation, reducedMotion, styleReady, view]);

  useEffect(() => {
    opacityRef.current = opacity;
    const map = mapRef.current;
    const current = currentSlotRef.current;
    if (current && animationRef.current === null && map?.getLayer(LAYERS[current.index]))
      map.setPaintProperty(LAYERS[current.index], "raster-opacity", opacity);
  }, [mapRef, opacity, styleReady]);

  useEffect(() => {
    const map = mapRef.current;
    for (const layer of LAYERS) if (map?.getLayer(layer))
      map.setPaintProperty(layer, "raster-resampling", presentation === "smooth" ? "linear" : "nearest");
  }, [mapRef, presentation, styleReady]);

  useEffect(() => {
    if (!playing || !enabled || reducedMotion || rangeDays.length < 2 || !frameSettled) return;
    const timer = window.setTimeout(() => {
      const next = rangeDays[(rangeDays.indexOf(day) + 1) % rangeDays.length];
      chooseDay(next, false);
    }, 160 / speed);
    return () => window.clearTimeout(timer);
  }, [chooseDay, day, enabled, frameSettled, playing, rangeDays, reducedMotion, speed]);

  useEffect(() => {
    onEngineContextChange?.({
      enabled,
      availabilityState: availability?.state ?? "unchecked",
      mapState: displayState,
      selectedView: view,
      selectedDepthCm: depth === "surface" ? [0, 5] : [0, 100],
      selectedUtcDay: day || null,
      selectedFrameTimeUtc: sourceFrame,
      renderedFrameTimeUtc: renderedFrame,
      renderedAtUtc: renderedFrame ? mapState.renderedAt : null,
      retainedFrameTimeUtc: mapState.visibleDay && mapState.state !== "blending" ? utcFrame(mapState.visibleDay) : null,
      visualTransition: mapState.state === "blending" && mapState.fromDay && mapState.toDay && mapState.transitionKind
        ? { fromFrameTimeUtc: utcFrame(mapState.fromDay)!, toFrameTimeUtc: utcFrame(mapState.toDay)!,
            fraction: mapState.transitionFraction ?? 0, kind: mapState.transitionKind, numericInterpolation: false }
        : null,
      displaySmoothing: presentation === "smooth" ? "visual blend and bilinear color resampling" : "exact daily image cells",
      playing,
      rangeStartUtcDay: range.from || null,
      rangeEndUtcDay: range.through || null,
      rangeFrameCount: rangeDays.length,
      availableFrameCount: availableDays.length,
      latestAvailableUtcDay: availability?.latestCommonDay ?? null,
      sourceCheckedAtUtc: availability?.checkedAt ?? null,
      product: SOIL_PRODUCT_METADATA.product,
      version: SOIL_PRODUCT_METADATA.version,
      displayCadence: SOIL_PRODUCT_METADATA.displayCadence,
      nativeCadence: SOIL_PRODUCT_METADATA.nativeCadence,
      nativeFormat: SOIL_PRODUCT_METADATA.nativeFormat,
      approximateResolutionKm: SOIL_PRODUCT_METADATA.approximateResolutionKm,
      coverageBoundsWgs84: SOIL_GLOBAL_BOUNDS_WGS84,
      evidenceRole: SOIL_PRODUCT_METADATA.role,
      dataKind: SOIL_PRODUCT_METADATA.dataKind,
      numericPixelsAvailable: false,
      qualityNotice,
      sourceUrl: SOIL_METADATA_URL,
      productGuideUrl: SOIL_GUIDE_URL,
    });
  }, [availability?.checkedAt, availability?.latestCommonDay, availability?.state, availableDays.length, day, depth, displayState, enabled, mapState.fromDay, mapState.renderedAt, mapState.state, mapState.toDay, mapState.transitionFraction, mapState.transitionKind, mapState.visibleDay, onEngineContextChange, playing, presentation, qualityNotice, range.from, range.through, rangeDays.length, renderedFrame, sourceFrame, view]);

  const chooseFrom = (requested: string) => {
    const from = orderedDays.find(value => value >= requested) ?? orderedDays.at(-1);
    if (!from) return;
    const through = range.through < from ? from : range.through;
    setRange({ from, through });
    if (day < from || day > through) chooseDay(from);
  };
  const chooseThrough = (requested: string) => {
    const through = [...orderedDays].reverse().find(value => value <= requested) ?? orderedDays[0];
    if (!through) return;
    const from = range.from > through ? through : range.from;
    setRange({ from, through });
    if (day < from || day > through) chooseDay(through);
  };

  const sourceText = checking ? "Checking NASA availability…" : availability?.state === "available"
    ? "SPL4SMAU V008 · latest shared " + availability.latestCommonDay + " 12:00 UTC"
    : availability?.state === "unavailable" ? "No shared NASA day is available for all four views"
      : availability?.state === "error" ? "NASA availability check failed" : "Check begins when enabled";
  const backendText = availability?.backend
    ? availability.backend.state.toUpperCase() + " · " + availability.backend.durationMs + " ms · cache " + availability.backend.cache
      + (availability.backend.code ? " · " + availability.backend.code : "")
    : "No request yet";
  const mapText = !enabled ? "Off · no tiles requested"
    : displayState.toUpperCase() + " · " + mapState.loaded + " tiles loaded / " + mapState.failed + " failed"
      + (mapState.renderedAt ? " · rendered " + new Date(mapState.renderedAt).toLocaleString("en-US", { timeZone: "UTC" }) + " UTC" : "");
  const transitionText = mapState.state === "blending" && mapState.fromDay
    ? mapState.transitionKind === "adjacent-visual-blend"
      ? `Visual transition ${mapState.fromDay} → ${day} · ${Math.round((mapState.transitionFraction ?? 0) * 100)}%`
      : `Loop reset or missing day · easing ${mapState.fromDay} → ${day} through basemap`
    : null;
  const canPlay = enabled && !checking && !reducedMotion && rangeDays.length > 1 && mapState.state !== "error";

  return <article className="official-context-row soil-moisture-control" data-state={displayState} data-visible={enabled}>
    <div className="official-context-primary">
      <label className="visibility-switch"><input type="checkbox" checked={enabled} aria-label={enabled ? "Hide Soil moisture" : "Show Soil moisture"} onChange={event => {
        const next = event.target.checked;
        setEnabled(next);
        setPlaying(false);
        if (next) void checkAvailability();
      }} /><span aria-hidden="true" /></label>
      <i style={{ "--swatch": "#6dbb9d" } as React.CSSProperties} />
      <div><strong>Soil moisture</strong><small>NASA SMAP Level-4 · modeled surface context · {enabled ? displayState : "off"}</small></div>
    </div>
    <details className="specialty-layer-details"><summary>Dates, playback &amp; details</summary><div className="official-context-option-body">
      <div className="soil-display-panel">
        <div><span>SELECTED NASA FRAME</span><strong>{day || "No date loaded"}</strong><small>12:00 UTC · {SOIL_VIEWS[view].label}</small></div>
        <b data-state={displayState}>{displayState === "rendered" ? "ON MAP" : displayState === "partial" ? "PARTIAL" : displayState.toUpperCase()}</b>
      </div>
      {mapState.visibleDay && mapState.state !== "blending" && mapState.state !== "rendered" &&
        <div className="soil-transition" role="status">Previous NASA frame {mapState.visibleDay} remains visible<small>{mapState.state === "loading" ? "Waiting for the next complete image" : "Next image unavailable; playback paused"}</small></div>}
      {transitionText && <div className="soil-transition" role="status">{transitionText}<small>Display blend only · no measured values between NASA frames</small></div>}
      <div className="source-time-actions soil-view-choices">
        <label>Depth<select value={depth} onChange={event => { setPlaying(false); clearRaster(); setDepth(event.target.value as Depth); }}>
          <option value="surface">Surface · 0–5 cm</option><option value="root">Root zone · 0–100 cm</option>
        </select></label>
        <label>View<select value={uncertainty ? "uncertainty" : "moisture"} onChange={event => { setPlaying(false); clearRaster(); setUncertainty(event.target.value === "uncertainty"); }}>
          <option value="moisture">Moisture</option><option value="uncertainty">Uncertainty</option>
        </select></label>
      </div>
      <section className="soil-timeline" aria-label="NASA soil moisture daily frames">
        <header><span>GIBS DAILY FRAMES · 12:00 UTC</span><strong>{rangeDays.length.toLocaleString("en-US")} in range · {availableDays.length.toLocaleString("en-US")} advertised</strong></header>
        <div className="soil-date-range">
          <label>From<input type="date" aria-label="Soil moisture loop start UTC day" value={range.from} min={orderedDays[0]} max={range.through || orderedDays.at(-1)} disabled={!enabled || checking || !orderedDays.length} onChange={event => chooseFrom(event.target.value)} /></label>
          <label>Through<input type="date" aria-label="Soil moisture loop end UTC day" value={range.through} min={range.from || orderedDays[0]} max={orderedDays.at(-1)} disabled={!enabled || checking || !orderedDays.length} onChange={event => chooseThrough(event.target.value)} /></label>
        </div>
        <div className="soil-playback">
          <button type="button" disabled={!canPlay} onClick={() => setPlaying(current => !current)}>{reducedMotion ? "Paused · reduced motion" : playing ? "Pause loop" : "Play loop"}</button>
          <label>Frames<select value={speed} disabled={!enabled || reducedMotion} aria-label="Soil moisture playback speed" onChange={event => setSpeed(Number(event.target.value) as 0.5 | 1 | 2)}>
            <option value={0.5}>0.5×</option><option value={1}>1×</option><option value={2}>2×</option>
          </select></label>
          <output aria-live="off">{sourceFrame ? sourceFrame.replace("T", " ").replace(":00Z", " UTC") : "No frame selected"}</output>
        </div>
        <label className="soil-display-mode">Display<select value={presentation} aria-label="Soil moisture display style" onChange={event => { setPlaying(false); setPresentation(event.target.value as "smooth" | "exact"); }}>
          <option value="smooth">Smooth visual</option><option value="exact">Exact image cells</option>
        </select></label>
        <input className="soil-frame-slider" type="range" min="0" max={Math.max(0, rangeDays.length - 1)} step="1" value={frameIndex} disabled={!enabled || checking || rangeDays.length < 2} aria-label="Soil moisture exact daily frame" aria-valuetext={sourceFrame ?? "No frame selected"} onChange={event => {
          const next = rangeDays[Number(event.target.value)];
          if (next) chooseDay(next);
        }} />
        <div className="soil-timeline-ends"><small>{range.from || "Earliest"}</small><small>{range.through || "Latest"}</small></div>
        <small>Smooth visual softens image pixels and blends adjacent daily colors. This is display only, not a soil moisture estimate. Missing days and loop resets ease through the basemap; Exact image cells shows the source pixels without blending.</small>
      </section>
      <label className="opacity-control"><span>Surface opacity <b>{Math.round(opacity * 100)}%</b></span><input type="range" min="0" max="100" value={Math.round(opacity * 100)} aria-label="Soil moisture opacity" onChange={event => setOpacity(Number(event.target.value) / 100)} /></label>
      <div className="soil-legend"><span>NASA COLOR SCALE · {uncertainty ? "UNCERTAINTY" : "MOISTURE"}</span>{enabled && <img src={soilLegendUrl(view)} alt={"NASA legend for " + SOIL_VIEWS[view].label} loading="lazy" />}</div>
      {qualityNotice && <p className="soil-quality-note"><strong>Source quality notice · {SOIL_GEOLOCATION_NOTICE.checkedDay}</strong> {qualityNotice} <a href={SOIL_GEOLOCATION_NOTICE.sourceUrl} target="_blank" rel="noreferrer">NSIDC notice ↗</a></p>}
      <details className="soil-source-details"><summary>Source and render details</summary>
        <div className="source-time-control" role="status"><p><strong>Source:</strong> {sourceText}</p><p><strong>Backend:</strong> {backendText}</p><p><strong>Map:</strong> {mapText}</p><p><strong>Checked:</strong> {availability?.checkedAt ? availability.checkedAt : "not yet"}</p></div>
      </details>
      <small className="soil-data-boundary">Global mapped surface, approximately 9 km. Smooth display changes image colors only; it does not infer soil moisture from stations or create numeric measurements. The GIBS color tiles are visual context; numeric pixels are unavailable to the science companion. Native SPL4SMAU HDF5 analysis updates are 3-hourly. Blank coverage and failed tiles are unknown, not dry or safe. External context only; no KFM EvidenceBundle or release.</small>
      <div className="source-time-actions"><button type="button" disabled={!enabled || checking} onClick={() => void checkAvailability(true)}>Retry NASA check</button><a href={SOIL_METADATA_URL} target="_blank" rel="noreferrer">NASA layer metadata ↗</a><a href={SOIL_GUIDE_URL} target="_blank" rel="noreferrer">Native data guide ↗</a></div>
    </div></details>
  </article>;
}
