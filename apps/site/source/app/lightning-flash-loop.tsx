"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import type { ExpressionSpecification, FilterSpecification, GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import { LightningArchiveControl } from "./lightning-archive-control";
import { LightningYearControl } from "./lightning-year-control";
import type { FeatureCollection, Point } from "geojson";
import { GLM_FLASH_WINDOWS, GLM_NOAA_SOURCE, glmFlashPlaybackBounds, glmFlashBins, type GlmFlashSnapshot, type GlmFlashWindow } from "./lightning-flashes";

const SOURCE_ID = "external-noaa-glm-flash-centroids";
const HALO_ID = "external-noaa-glm-flash-halo";
const CORE_ID = "external-noaa-glm-flash-core";
const empty: FeatureCollection<Point> = { type: "FeatureCollection", features: [] };
const utc = (ms: number) => new Date(ms).toISOString().slice(0, 19).replace("T", " ") + " UTC";

function flashCollection(snapshot: GlmFlashSnapshot): FeatureCollection<Point> {
  return { type: "FeatureCollection", features: snapshot.flashes.map((flash) => ({
    type: "Feature", id: flash.id, geometry: { type: "Point", coordinates: [flash.longitude, flash.latitude] },
    properties: { timeMs: flash.timeMs, observedAt: flash.observedAt, energyFj: flash.energyFj, areaKm2: flash.areaKm2 },
  })) };
}

export function LightningFlashLoop({ map, enabled, reducedMotion, onClose }: {
  map: MapLibreMap | null; enabled: boolean; reducedMotion: boolean; onClose: () => void;
}) {
  const [sourceMode, setSourceMode] = useState<"recent" | "archive">("recent");
  const [archiveMode, setArchiveMode] = useState<"year" | "interval">("year");
  const yearMode = sourceMode === "archive" && archiveMode === "year";
  const [windowMinutes, setWindowMinutes] = useState<GlmFlashWindow>(180);
  const [sliceMinutes, setSliceMinutes] = useState<15 | 30 | 60>(15);
  const [displayMode, setDisplayMode] = useState<"slice" | "pulse">("slice");
  const [speed, setSpeed] = useState<0.5 | 1 | 2>(1);
  const [trailSeconds, setTrailSeconds] = useState<30 | 60 | 120>(60);
  const [opacity, setOpacity] = useState(0.88);
  const [loop, setLoop] = useState(true);
  const [playing, setPlaying] = useState(false);
  const [snapshot, setSnapshot] = useState<GlmFlashSnapshot | null>(null);
  const [loadState, setLoadState] = useState<"idle" | "loading" | "ready" | "error">("idle");
  const [refreshKey, setRefreshKey] = useState(0);
  const [cursor, setCursor] = useState(0);
  const [error, setError] = useState("");
  const [now, setNow] = useState(() => Date.now());
  const [styleRevision, setStyleRevision] = useState(0);

  const bounds = useMemo(() => snapshot ? glmFlashPlaybackBounds(snapshot) : null, [snapshot]);
  const archived = sourceMode === "archive" && snapshot?.source === "NOAA_GOES_GLM_ARCHIVE" && Boolean(snapshot.archive);
  const fresh = Boolean(archived || snapshot && now - Date.parse(snapshot.providerGeneratedAt) <= 5 * 60_000);
  const displayReady = enabled && loadState === "ready" && Boolean(snapshot && (archived || sourceMode === "recent" && snapshot.source === "NOAA_GOES19_GLM_VIA_ATMOSTORM" && snapshot.windowMinutes === windowMinutes) && snapshot.state !== "stale") && fresh && Boolean(map);
  const bins = useMemo(() => snapshot ? glmFlashBins(snapshot, sliceMinutes) : [], [snapshot, sliceMinutes]);
  const selectedBin = bins.find((bin, index) => cursor >= bin.start && (cursor < bin.end || index === bins.length - 1 && cursor <= bin.end));
  const sliceMode = displayMode === "slice";
  const collection = useMemo(() => snapshot ? flashCollection(snapshot) : empty, [snapshot]);

  useEffect(() => {
    if (!enabled || sourceMode !== "recent") return;
    const abort = new AbortController();
    let disposed = false;
    const refresh = async () => {
      setLoadState((current) => current === "ready" ? current : "loading");
      try {
        const response = await fetch(`/api/lightning/flashes?minutes=${windowMinutes}`, { signal: abort.signal, cache: "no-store" });
        if (!response.ok) throw new Error("Flash feed unavailable");
        const next: GlmFlashSnapshot = await response.json();
        if (next.evidenceRole !== "EXTERNAL_CONTEXT_ONLY" || next.source !== "NOAA_GOES19_GLM_VIA_ATMOSTORM" || next.windowMinutes !== windowMinutes || !Array.isArray(next.flashes) || next.flashes.length > 5_000 || !["ready", "empty", "partial", "stale"].includes(next.state)) throw new Error("Flash response invalid");
        if (disposed) return;
        setSnapshot(next);
        const nextBounds = glmFlashPlaybackBounds(next);
        setCursor((current) => current >= nextBounds.start && current <= nextBounds.end ? current : nextBounds.start);
        setLoadState("ready");
        setError("");
        if (next.state === "stale") setPlaying(false);
      } catch {
        if (disposed || abort.signal.aborted) return;
        setLoadState("error");
        setPlaying(false);
        setError("Observed flashes are unavailable; the last response is withheld from the map.");
      }
    };
    void refresh();
    const timer = window.setInterval(() => void refresh(), 60_000);
    return () => { disposed = true; abort.abort(); window.clearInterval(timer); };
  }, [enabled, windowMinutes, refreshKey, sourceMode]);

  useEffect(() => {
    if (!enabled || !map) return;
    const apply = () => {
      if (!map.isStyleLoaded()) return;
      if (!map.getSource(SOURCE_ID)) map.addSource(SOURCE_ID, { type: "geojson", data: collection });
      else (map.getSource(SOURCE_ID) as GeoJSONSource).setData(collection);
      if (!map.getLayer(HALO_ID)) map.addLayer({ id: HALO_ID, type: "circle", source: SOURCE_ID, paint: { "circle-color": "#a883ff", "circle-radius": 12, "circle-blur": 0.45, "circle-opacity": 0 } });
      if (!map.getLayer(CORE_ID)) map.addLayer({ id: CORE_ID, type: "circle", source: SOURCE_ID, paint: { "circle-color": "#f6edff", "circle-radius": 3.5, "circle-opacity": 0, "circle-stroke-color": "#a47dff", "circle-stroke-width": 1.5 } });
    };
    const onStyleLoad = () => { apply(); setStyleRevision((revision) => revision + 1); };
    map.on("style.load", onStyleLoad);
    apply();
    return () => { map.off("style.load", onStyleLoad); };
  }, [enabled, map, collection]);

  useEffect(() => {
    if (!map || !map.getLayer(HALO_ID) || !map.getLayer(CORE_ID)) return;
    const shown = displayReady && Boolean(snapshot?.flashes.length);
    map.setLayoutProperty(HALO_ID, "visibility", shown && !reducedMotion ? "visible" : "none");
    map.setLayoutProperty(CORE_ID, "visibility", shown ? "visible" : "none");
    if (!shown) return;
    const age: ExpressionSpecification = ["-", cursor, ["get", "timeMs"]];
    const visible: FilterSpecification = sliceMode && selectedBin ? ["all", [">=", ["get", "timeMs"], selectedBin.start], [selectedBin.end === bounds?.end ? "<=" : "<", ["get", "timeMs"], selectedBin.end]] : ["all", ["<=", ["get", "timeMs"], cursor], [">=", ["get", "timeMs"], cursor - trailSeconds * 1000]];
    map.setFilter(HALO_ID, visible);
    map.setFilter(CORE_ID, visible);
    map.setPaintProperty(HALO_ID, "circle-radius", sliceMode ? 10 : ["interpolate", ["linear"], age, 0, 6, trailSeconds * 1000, 23]);
    map.setPaintProperty(HALO_ID, "circle-opacity", sliceMode ? opacity * 0.25 : ["interpolate", ["linear"], age, 0, opacity * 0.58, trailSeconds * 1000, 0]);
    map.setPaintProperty(CORE_ID, "circle-opacity", sliceMode ? opacity : ["interpolate", ["linear"], age, 0, opacity, trailSeconds * 1000, opacity * 0.2]);
  }, [cursor, displayReady, map, opacity, reducedMotion, snapshot, styleRevision, trailSeconds, sliceMode, selectedBin, bounds]);

  useEffect(() => {
    if (!enabled || !playing || reducedMotion || !bounds || !displayReady || !snapshot?.flashes.length) return;
    const span = bounds.end - bounds.start;
    const timer = window.setInterval(() => setCursor((current) => {
      const next = current + span * speed / 180;
      if (next <= bounds.end) return next;
      if (!loop) { setPlaying(false); return bounds.end; }
      return bounds.start;
    }), 100);
    return () => window.clearInterval(timer);
  }, [bounds, displayReady, enabled, loop, playing, reducedMotion, snapshot?.flashes.length, speed]);

  useEffect(() => {
    const pause = () => { if (document.hidden) setPlaying(false); else { setNow(Date.now()); setRefreshKey((value) => value + 1); } };
    document.addEventListener("visibilitychange", pause);
    return () => document.removeEventListener("visibilitychange", pause);
  }, []);

  useEffect(() => {
    if (!enabled) return;
    const timer = window.setInterval(() => setNow(Date.now()), 10_000);
    return () => window.clearInterval(timer);
  }, [enabled]);

  useEffect(() => {
    if (enabled) return;
    if (!map) return;
    for (const id of [CORE_ID, HALO_ID]) if (map.getLayer(id)) map.removeLayer(id);
    if (map.getSource(SOURCE_ID)) map.removeSource(SOURCE_ID);
  }, [enabled, map]);

  const clearArchive = useCallback(() => { setPlaying(false); setSnapshot(null); setLoadState("idle"); }, []);
  const receiveArchive = useCallback((next: GlmFlashSnapshot) => {
    setSnapshot(next); setCursor(glmFlashPlaybackBounds(next).start); setSliceMinutes(15); setLoadState("ready"); setError("");
  }, []);
  const receiveYear = useCallback((next: GlmFlashSnapshot) => {
    setPlaying(false); setDisplayMode("slice"); setSliceMinutes(60);
    setSnapshot(next); setCursor(glmFlashPlaybackBounds(next).start); setLoadState("ready"); setError("");
  }, []);

  const step = useCallback((direction: -1 | 1) => {
    if (!bounds) return;
    setPlaying(false);
    setCursor((current) => Math.max(bounds.start, Math.min(bounds.end, current + direction * (sliceMode ? sliceMinutes * 60_000 : (bounds.end - bounds.start) / 20))));
  }, [bounds, sliceMode, sliceMinutes]);
  const visibleCount = sliceMode ? selectedBin?.count ?? 0 : snapshot?.flashes.filter((flash) => flash.timeMs <= cursor && flash.timeMs >= cursor - trailSeconds * 1000).length ?? 0;

  if (!enabled) return null;
  return <aside className="glm-flash-studio" aria-label="Observed satellite lightning flash loop" data-state={loadState}>
    <header><div><span>OBSERVED FLASHES · KANSAS AREA</span><strong>{sourceMode === "archive" ? "Lightning through time" : "GOES-19 lightning pulse"}</strong><small>{sourceMode === "archive" ? "NOAA GOES-East archive" : "NOAA GLM via Atmostorm"} · time-stamped cloud-top flash centroids</small></div><button type="button" onClick={onClose} aria-label="Close observed lightning loop">×</button></header>
    <div className="glm-time-resolution" role="group" aria-label="Lightning observation source"><button type="button" aria-pressed={sourceMode === "recent"} onClick={() => { if (sourceMode === "recent") return; setPlaying(false); setSnapshot(null); setLoadState("idle"); setSourceMode("recent"); }}>Recent flashes</button><button type="button" aria-pressed={sourceMode === "archive"} onClick={() => { if (sourceMode === "archive") return; setPlaying(false); setSnapshot(null); setLoadState("idle"); setSourceMode("archive"); }}>Year / month archive</button></div>
    {sourceMode === "archive" && <>
      <div className="glm-time-resolution" role="group" aria-label="Archive playback mode"><button type="button" aria-pressed={archiveMode === "year"} onClick={() => { if (archiveMode !== "year") { clearArchive(); setArchiveMode("year"); } }}>Loop a year</button><button type="button" aria-pressed={archiveMode === "interval"} onClick={() => { if (archiveMode !== "interval") { clearArchive(); setArchiveMode("interval"); } }}>Specific interval</button></div>
      {yearMode ? <LightningYearControl reducedMotion={reducedMotion} onClear={clearArchive} onSnapshot={receiveYear} /> : <LightningArchiveControl onClear={clearArchive} onSnapshot={receiveArchive} />}
    </>}
    <div className="glm-flash-headline"><b>{bounds ? utc(cursor) : "Waiting for observed times"}</b><span>{displayReady ? visibleCount : 0} centroids in selected view · {snapshot?.providerCount ?? 0} returned</span></div>
    <p role="status">{sourceMode === "archive" && !snapshot ? yearMode ? "Choose a year and press Play year. Observations load one hour at a time." : "Select a year, month, day and interval above to load historical lightning." : loadState === "loading" ? "Checking the recent satellite flashes…" : loadState === "error" ? error : !map ? "Map rendering unavailable; no points displayed." : !fresh || snapshot?.state === "stale" ? "Source is more than five minutes old; pulses are withheld." : snapshot?.state === "partial" ? snapshot.partialReason : snapshot?.state === "empty" ? "No quality-accepted flashes returned in this checked window; this is not an all-clear." : "Time slices and pulses follow returned flash times and centroids. Playback compresses time; rings are visual markers, not strike footprints."}</p>
    {!yearMode && <div className="glm-time-resolution" role="group" aria-label="Lightning time resolution">
      {([15, 30, 60] as const).map((minutes) => <button type="button" key={minutes} disabled={Boolean(archived && snapshot && minutes > snapshot.windowMinutes)} aria-pressed={sliceMode && sliceMinutes === minutes} onClick={() => { setPlaying(false); setDisplayMode("slice"); setSliceMinutes(minutes); }}>{minutes === 60 ? "Hourly" : minutes === 30 ? "Half-hour" : "15 minutes"}</button>)}
      <button type="button" aria-pressed={!sliceMode} onClick={() => { setPlaying(false); setDisplayMode("pulse"); }}>Individual pulses</button>

    </div>}
    <small>{sourceMode === "archive" ? yearMode ? "Whole-hour frames advance automatically through the selected year." : "Historical observations for the loaded interval. Change the date and hour to explore another part of the day." : "Latest three hours. Use Year / month archive for older observations."} All times UTC.</small>
    {sliceMode && selectedBin && displayReady && <output className="glm-selected-slice">{utc(selectedBin.start)} – {utc(selectedBin.end)} · {selectedBin.count} returned centroids</output>}
    {!yearMode && <div className="glm-activity" role="group" aria-label="Returned flash activity by time slice">{bins.map((bin) => <button type="button" key={bin.start} disabled={!displayReady} aria-pressed={sliceMode && selectedBin?.start === bin.start} aria-label={`${utc(bin.start)} to ${utc(bin.end)}: ${bin.count} returned flash centroids`} title={`${utc(bin.start)} · ${bin.count} centroids`} onClick={() => { setPlaying(false); setDisplayMode("slice"); setCursor(bin.start); }}><span style={{ height: `${Math.max(3, bin.count / Math.max(1, ...bins.map((x) => x.count)) * 100)}%` }} /><small>{new Date(bin.start).toISOString().slice(11, 16)}</small></button>)}</div>}
    <div className="glm-flash-settings">
      {sourceMode === "recent" && <label>Source window<select value={windowMinutes} onChange={(event) => { setPlaying(false); setWindowMinutes(Number(event.target.value) as GlmFlashWindow); }}>{GLM_FLASH_WINDOWS.map((minutes) => <option key={minutes} value={minutes}>{minutes === 180 ? "Latest 3 hours" : `${minutes} min`}</option>)}</select></label>}
      {!yearMode && <label>Playback speed<select value={speed} onChange={(event) => setSpeed(Number(event.target.value) as 0.5 | 1 | 2)}><option value="0.5">½×</option><option value="1">1×</option><option value="2">2×</option></select></label>}
      {!yearMode && <label>Pulse persistence<select disabled={sliceMode} value={trailSeconds} onChange={(event) => setTrailSeconds(Number(event.target.value) as 30 | 60 | 120)}><option value="30">30 source seconds</option><option value="60">60 source seconds</option><option value="120">120 source seconds</option></select></label>}
      <label>Opacity <output>{Math.round(opacity * 100)}%</output><input type="range" min="0" max="100" value={Math.round(opacity * 100)} onChange={(event) => setOpacity(Number(event.target.value) / 100)} aria-label="Observed flash opacity" /></label>
    </div>
    {!yearMode && <><input className="glm-flash-scrub" type="range" min={bounds?.start ?? 0} max={bounds?.end ?? 1} step="1000" value={bounds ? Math.max(bounds.start, Math.min(bounds.end, cursor)) : 0} disabled={!bounds || !displayReady} onChange={(event) => { setPlaying(false); setCursor(Number(event.target.value)); }} aria-label="Observed flash playback time" aria-valuetext={bounds ? utc(cursor) : "No observed window"} />
    <div className="glm-flash-actions"><button type="button" onClick={() => step(-1)} disabled={!displayReady}>‹ Earlier</button><button type="button" aria-pressed={playing} onClick={() => { if (playing) setPlaying(false); else if (bounds) { if (cursor >= bounds.end) setCursor(bounds.start); setPlaying(true); } }} disabled={!displayReady || reducedMotion || !snapshot?.flashes.length}>{playing ? "Ⅱ Pause" : "▶ Play flashes"}</button><button type="button" onClick={() => step(1)} disabled={!displayReady}>Later ›</button><label><input type="checkbox" checked={loop} onChange={(event) => setLoop(event.target.checked)} /> Loop</label>{sourceMode === "recent" && <button type="button" onClick={() => setRefreshKey((value) => value + 1)}>Refresh</button>}</div></>}
    <div className="glm-flash-status"><span>{snapshot ? `${archived ? "Archive interval ends" : "Provider update"} ${utc(Date.parse(snapshot.providerGeneratedAt))}` : "No provider update"}</span><span>{snapshot?.oldestFlashAt && snapshot.latestFlashAt ? `Returned flash times ${utc(Date.parse(snapshot.oldestFlashAt))} → ${utc(Date.parse(snapshot.latestFlashAt))}` : "No returned flash times"}</span>{snapshot?.nearBorderCount ? <span>{snapshot.nearBorderCount} centroid(s) near the Kansas bounding edge; state-boundary membership is unverified.</span> : null}</div>
    {snapshot?.archive && <small>{snapshot.archive.files}/{snapshot.archive.expectedFiles} expected files loaded · {snapshot.archive.omittedQuality} Kansas-area flashes withheld by provider quality flags. Missing files remain gaps.</small>}
    <details><summary>Source, accuracy and display key</summary><p><i className="glm-key-dot" /> Bright core = returned flash centroid. Violet halo = visual emphasis; in pulse mode its expansion is a time-persistence cue. Neither symbol shows a physical ground strike or the flash footprint.</p><p>GLM sees total lightning, including in-cloud flashes. Its optical pixels are roughly 8–14 km and do not provide every lightning strike or a ground-contact location. Recent-feed results may lag or be capped; archive files can be missing; a quiet map is not an all-clear.</p><p>The NASA LIS/OTD 1995–2014 layer is a separate long-term 0.5° flash-rate composite and never generates these pulses.</p><a href={GLM_NOAA_SOURCE} target="_blank" rel="noreferrer">NOAA GLM product metadata ↗</a><a href="https://registry.opendata.aws/noaa-goes/" target="_blank" rel="noreferrer">NOAA historical archive ↗</a><a href="https://atmostorm.com/api-docs/endpoints#lightning" target="_blank" rel="noreferrer">Atmostorm source API ↗</a></details>
    {reducedMotion && <small>Reduced motion is active: autoplay and pulsing are off. Use the time slider or step buttons.</small>}
    <footer>External observational context only · not an emergency warning service or KFM evidence</footer>
  </aside>;
}
