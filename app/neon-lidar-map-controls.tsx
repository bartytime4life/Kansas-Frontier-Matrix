"use client";

import Link from "next/link";
import { useCallback, useEffect, useId, useMemo, useRef, useState, type RefObject } from "react";
import type { Map as MapLibreMap, MapMouseEvent } from "./maplibre-seam";
import { createAcquisitionSession } from "./acquisition-client";
import { neonElevationDomain, neonLidarProbe, parseNeonLidarPreview, readNeonLidarLocalJson, type NeonLidarMode, type NeonLidarPreview } from "./neon-lidar-preview";
import { applyNeonMapOverlay, buildNeon3DMapData, buildNeonMapData, clearNeonMapOverlay, neonMapBounds, NEON_LOCAL_FILL, NEON_LOCAL_GROUND, NEON_LOCAL_SOURCE } from "./neon-lidar-map";
import { readNeonLidarPilot, type NeonPilotReceipt } from "./neon-lidar-pilot-client";
import { buildNeonStoryStops } from "./neon-lidar-story";
import styles from "./neon-lidar-map-controls.module.css";

type Options = {
  mapRef: RefObject<MapLibreMap | null>; styleReady: boolean; flatMap: boolean;
  atPresent: boolean; reducedMotion: boolean; onFlatMap?: () => void;
  claimedClicksRef?: RefObject<WeakSet<object>>;
};
type CoordinateDraft = { row: string; column: string };
const emptyDraft = (): CoordinateDraft => ({ row: "", column: "" });
const coordinateIndex = (input: string, limit: number) => /^\d+$/.test(input) && Number.isInteger(Number(input)) && Number(input) >= 1 && Number(input) <= limit ? Number(input) - 1 : null;
const meters = (value: number | null) => value === null ? "NoData" : `${value.toFixed(2)} m`;
const modes: { kind: NeonLidarMode; label: string }[] = [{ kind: "dtm", label: "Ground" }, { kind: "dsm", label: "Surface" }, { kind: "chm", label: "Canopy" }];

/** Lives with the map page, so closing Appearance does not remove the local selection. */
export function useNeonLidarMap({ mapRef, styleReady, flatMap, atPresent, reducedMotion, onFlatMap, claimedClicksRef }: Options) {
  const [preview, setPreview] = useState<NeonLidarPreview | null>(null);
  const [pilotReceipt, setPilotReceipt] = useState<NeonPilotReceipt | null>(null);
  const [loadKind, setLoadKind] = useState<"file" | "pilot">("file");
  const [mode, setMode] = useState<NeonLidarMode>("chm");
  const [opacity, setOpacity] = useState(80);
  const [representation, setRepresentation] = useState<"flat" | "columns">("flat");
  const [verticalExaggeration, setVerticalExaggeration] = useState(1);
  const [enabled, setEnabled] = useState(false);
  const [busy, setBusy] = useState(false);
  const [fileError, setFileError] = useState("");
  const [mapError, setMapError] = useState("");
  const [actionError, setActionError] = useState("");
  const sceneRef = useRef({ styleReady, flatMap, atPresent, reducedMotion });
  useEffect(() => { sceneRef.current = { styleReady, flatMap, atPresent, reducedMotion }; }, [styleReady, flatMap, atPresent, reducedMotion]);
  const [applied, setApplied] = useState(false);
  const [coordinateDraft, setCoordinateDraft] = useState(emptyDraft);
  const [session] = useState(createAcquisitionSession);
  const data = useMemo(() => preview ? buildNeonMapData(preview) : null, [preview]);
  const bounds = useMemo(() => preview ? neonMapBounds(preview) : null, [preview]);
  const storyStops = useMemo(() => preview ? buildNeonStoryStops(preview) : [], [preview]);
  const columns = useMemo(() => data && representation === "columns" ? buildNeon3DMapData(data, mode, verticalExaggeration).metadata : null, [data, mode, representation, verticalExaggeration]);
  const elevationDomain = useMemo(() => preview ? neonElevationDomain(preview) : null, [preview]);
  const probe = useMemo(() => {
    if (!preview) return null;
    const row = coordinateIndex(coordinateDraft.row, preview.grid.height), column = coordinateIndex(coordinateDraft.column, preview.grid.width);
    return row === null || column === null ? null : neonLidarProbe(preview, row, column);
  }, [preview, coordinateDraft]);
  const removeOverlay = useCallback(() => {
    const map = mapRef.current;
    if (map) { try { clearNeonMapOverlay(map); } catch { /* The map may already have been disposed. */ } }
  }, [mapRef]);
  useEffect(() => () => { session.cancel(); removeOverlay(); }, [session, removeOverlay]);
  useEffect(() => {
    const map = mapRef.current;
    return () => { if (map) { try { clearNeonMapOverlay(map); } catch { /* The captured renderer may already be disposed. */ } } };
  }, [mapRef, styleReady]);
  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    let disposed = false;
    const sync = () => {
      if (disposed) return;
      try {
        if (!preview || !data || !enabled || !styleReady || !flatMap || !atPresent) {
          clearNeonMapOverlay(map); setApplied(false); setMapError(""); return;
        }
        applyNeonMapOverlay(map, data, mode, opacity / 100, { representation, verticalExaggeration });
        setApplied(opacity > 0); setMapError("");
      } catch {
        try { clearNeonMapOverlay(map); } catch { /* Preserve the mutation failure below. */ }
        setApplied(false); setMapError("The map could not draw this local preview. Hide it or reload the map before trying again.");
      }
    };
    const pick = (event: MapMouseEvent) => {
      if (claimedClicksRef?.current.has(event)) return;
      if (!enabled || !flatMap || !atPresent || !styleReady || !preview || !data || !map.getLayer(NEON_LOCAL_FILL)) return;
      const layers = [NEON_LOCAL_FILL, NEON_LOCAL_GROUND].filter(id => map.getLayer(id));
      const feature = map.queryRenderedFeatures(event.point, { layers }).find(item => item.source === NEON_LOCAL_SOURCE);
      const row = feature?.properties?.row, column = feature?.properties?.column;
      if (typeof row !== "number" || typeof column !== "number" || !neonLidarProbe(preview, row, column)) return;
      setCoordinateDraft(previous => previous.row === String(row + 1) && previous.column === String(column + 1) ? previous : { row: String(row + 1), column: String(column + 1) });
    };
    // Synchronize this local renderer resource, including full basemap style replacements.
    sync();
    map.on("style.load", sync); map.on("click", pick);
    return () => {
      disposed = true; map.off("style.load", sync); map.off("click", pick);
      // Settings reuse the owned source; the renderer-lifetime effect owns final removal.
    };
  }, [mapRef, styleReady, flatMap, atPresent, preview, data, enabled, mode, opacity, representation, verticalExaggeration, claimedClicksRef]);
  async function importFile(file: File | undefined) {
    if (!file) return;
    const request = session.begin();
    removeOverlay(); setPreview(null); setPilotReceipt(null); setLoadKind("file"); setRepresentation("flat"); setVerticalExaggeration(1); setCoordinateDraft(emptyDraft()); setEnabled(false); setApplied(false); setBusy(true); setFileError(""); setMapError(""); setActionError("");
    try {
      const parsed = parseNeonLidarPreview(await readNeonLidarLocalJson(file, request.signal));
      if (!parsed) throw new Error("Preview validation failed. Choose a matching terrain/surface/canopy JSON from the local NEON preparer.");
      if (request.current()) setPreview(parsed);
    } catch (error: unknown) { if (request.current()) setFileError(error instanceof Error ? error.message : "The local preview could not be read."); }
    finally { if (request.current()) setBusy(false); }
  }
  async function loadPilot(explore = false) {
    const request = session.begin(), requestedMap = mapRef.current;
    removeOverlay(); setPreview(null); setPilotReceipt(null); setLoadKind("pilot"); setRepresentation("flat"); setVerticalExaggeration(1); setCoordinateDraft(emptyDraft()); setEnabled(false); setApplied(false); setBusy(true); setFileError(""); setMapError(""); setActionError("");
    try {
      const receipt = await readNeonLidarPilot(request.signal);
      if (request.current()) {
        setPreview(receipt.preview); setPilotReceipt(receipt);
        if (explore) {
          if (mapRef.current !== requestedMap) setActionError("The map changed while the preview loaded. Explore again to frame the current map.");
          else activate3D(receipt.preview, "chm", 3);
        }
      }
    } catch (error: unknown) { if (request.current()) setFileError(error instanceof Error ? error.message : "The Konza Prairie preview is unavailable. Import a prepared file or try again later."); }
    finally { if (request.current()) setBusy(false); }
  }
  function clear() {
    session.cancel(); removeOverlay(); setRepresentation("flat"); setVerticalExaggeration(1); setPreview(null); setPilotReceipt(null); setCoordinateDraft(emptyDraft()); setEnabled(false); setApplied(false); setBusy(false); setFileError(""); setMapError(""); setActionError("");
  }
  function selectAxis(axis: keyof CoordinateDraft, input: string) {
    if (!preview) return;
    setCoordinateDraft(previous => {
      if (previous[axis] === input) return previous;
      const next = { ...previous, [axis]: input };
      if (!previous.row && !previous.column && coordinateIndex(input, preview.grid.width) !== null) next[axis === "row" ? "column" : "row"] = "1";
      return next;
    });
  }
  const canShow = Boolean(preview && data && bounds && styleReady && flatMap && atPresent);
  const sceneBlock = !flatMap ? "Use local sample view first. Statewide Terrain 3D uses a different elevation source."
    : !atPresent ? "Choose Present first. This acquisition cannot represent historical atlas frames."
      : !styleReady ? "Waiting for the map style before 3D can open." : "";
  const canExplore3D = !busy && !sceneBlock && (!preview || Boolean(data && bounds));
  function runtime3DBlock() {
    const current = sceneRef.current, map = mapRef.current;
    if (!map || !current.styleReady) return "The map is not ready for local sample 3D yet.";
    if (!current.flatMap) return "Use local sample view first; globe and statewide Terrain 3D hold this tile.";
    if (!current.atPresent) return "Choose Present first. This acquisition cannot represent a historical frame.";
    try {
      // The host styleReady gate owns safe style generations. isStyleLoaded also waits
      // for unrelated source tiles, which must not block this local dataset.
      if (map.getProjection?.()?.type !== "mercator") return "Local sample 3D requires the Mercator map camera.";
      if (map.getTerrain?.()) return "Turn off the external elevation terrain before exploring local sample 3D.";
    } catch { return "The map's projection and terrain state could not be verified."; }
    return "";
  }
  function activate3D(input: NeonLidarPreview, surface: NeonLidarMode, scale: number) {
    const block = runtime3DBlock();
    if (block) { setActionError(block); return; }
    const map = mapRef.current, localData = buildNeonMapData(input), localBounds = neonMapBounds(input);
    if (!map || !localData || !localBounds) { setActionError("This preview has no supported map georeferencing. Its raster values remain available in Science."); return; }
    try {
      const metadata = buildNeon3DMapData(localData, surface, scale).metadata;
      if (!metadata.eligible_cells) { setActionError("No valid columns are available for this surface. Choose another surface or inspect the source samples."); return; }
      const size = map.getCanvas().getBoundingClientRect(), compact = size.width < 760;
      const padding = compact ? { top: 50, left: 22, right: 22, bottom: Math.round(size.height * 0.55) }
        : { top: 75, left: 60, right: Math.min(500, Math.round(size.width * 0.45)), bottom: 80 };
      if (size.width - padding.left - padding.right < 64 || size.height - padding.top - padding.bottom < 64) {
        setActionError("The map viewport is too small to frame 3D. Enlarge the map and try again."); return;
      }
      // Fit and pitch in one transition: a second camera action could cancel the first.
      map.fitBounds(localBounds, { maxZoom: 16, pitch: 60, bearing: -25, linear: true,
        duration: sceneRef.current.reducedMotion ? 0 : 850, padding });
      setMode(surface); setRepresentation("columns"); setVerticalExaggeration(scale);
      setOpacity(previous => previous > 0 ? previous : 80); setEnabled(true); setActionError("");
    } catch { setActionError("The 3D view could not open. Source samples are retained; try the flat view or reload the map."); }
  }
  async function explore3D() {
    if (busy) return;
    const block = runtime3DBlock();
    if (block) { setActionError(block); return; }
    if (!preview) { await loadPilot(true); return; }
    activate3D(preview, mode, representation === "columns" ? verticalExaggeration : 3);
  }
  function toggle() { if (enabled) { removeOverlay(); setEnabled(false); setApplied(false); } else if (canShow) setEnabled(true); }
  function fit() {
    const map = mapRef.current;
    if (!map || !bounds || !canShow) return;
    try {
      const size = map.getCanvas().getBoundingClientRect();
      const compact = size.width < 760;
      map.fitBounds(bounds, { maxZoom: 15, duration: reducedMotion ? 0 : 550,
        padding: compact ? { top: 50, left: 22, right: 22, bottom: Math.round(size.height * 0.55) } : { top: 75, left: 60, right: Math.min(500, Math.round(size.width * 0.45)), bottom: 80 } });
    } catch { setActionError("The map could not fit this tile. The local file is retained."); }
  }
  function pitch() {
    if (!canShow || !enabled) return;
    try { mapRef.current?.easeTo({ pitch: 55, bearing: -20, duration: reducedMotion ? 0 : 550 }); }
    catch { setActionError("The camera could not pitch this tile. Your source samples are retained."); }
  }
  function plan() {
    setActionError(""); setRepresentation("flat");
    if (!canShow) return;
    try { mapRef.current?.easeTo({ pitch: 0, bearing: 0, duration: reducedMotion ? 0 : 550 }); }
    catch { setActionError("The camera could not return to plan view."); }
  }
  function focusStop(id: string) {
    const stop = storyStops.find(item => item.id === id), map = mapRef.current;
    if (!stop || !map || !canShow || !enabled) return;
    setMode(stop.mode); setCoordinateDraft({ row: String(stop.row + 1), column: String(stop.column + 1) });
    if (!stop.display_center) return;
    try { map.easeTo({ center: stop.display_center, zoom: 16, pitch: representation === "columns" ? 55 : 0, bearing: representation === "columns" ? -20 : 0, duration: reducedMotion ? 0 : 650 }); }
    catch { setActionError("The sampled location is selected, but the camera could not focus it."); }
  }
  const displayError = actionError || mapError;
  const explore3DStatus = displayError || sceneBlock || (busy ? "Loading a preview for the map…" : !preview ? "Loads the Konza pilot, shows columns at 3×, frames the tile and tilts the camera."
    : !data || !bounds ? "This preview needs map georeferencing before 3D can open."
      : representation === "columns" && enabled ? `3D sample columns · ${verticalExaggeration}× relative heights. Explore again to reframe and tilt.`
        : "Shows this tile at 3× relative height, frames it and tilts the camera. Source readings stay unscaled.");
  const status = busy ? loadKind === "pilot" ? "Loading the dev-processed Konza Prairie preview…" : "Reading the selected file locally…" : fileError || displayError || !preview ? fileError || displayError || "No NEON preview loaded. Explore in 3D to load and display Konza Prairie, or load the preview only."
    : !data || !bounds ? "This preview has no supported offline georeferencing. Re-prepare it to show it on the map; the acquisition lab can still inspect its numeric grid."
      : !flatMap ? "Local overlay held in globe or Terrain 3D. Return to 2D to display this tile."
        : !atPresent ? "Local overlay held outside Present. This dated acquisition is not a source for historical atlas frames."
          : !styleReady ? "Local preview ready; waiting for the map style."
            : !enabled ? pilotReceipt ? "Dev-processed provider pilot ready. Explore in 3D, or use Show on map without moving the camera." : "Tile ready locally. Explore in 3D, or use Show on map without moving the camera."
              : opacity === 0 ? "Local overlay hidden at 0% opacity. Increase opacity to show its cells."
                : applied ? "Sampled cells enabled at Present. This is dated context, not live vegetation or KFM evidence." : "Applying local preview to the map…";
  return { preview, pilotReceipt, mode, opacity, enabled, busy, fileError, mapError: displayError, status, canShow, canExplore3D, explore3DStatus, explore3D, applied, flatMap, atPresent, coordinateDraft, probe, elevationDomain,
    importFile, loadPilot, clear, toggle, fit, selectAxis, onFlatMap, representation, setRepresentation, verticalExaggeration, columns, storyStops, pitch, plan, focusStop,
    setVerticalExaggeration: (value: number) => { if (Number.isFinite(value)) setVerticalExaggeration(Math.max(1, Math.min(5, value))); },
    setMode, setOpacity: (value: number) => { if (Number.isFinite(value)) setOpacity(Math.max(0, Math.min(100, value))); } };
}
export type NeonLidarMapController = ReturnType<typeof useNeonLidarMap>;

export function NeonLidarMapBadge({ controller: c }: { controller: NeonLidarMapController }) {
  if (!c.applied || !c.preview || !c.flatMap || !c.atPresent || c.opacity === 0) return null;
  const synthetic = c.preview.data_kind === "synthetic-test";
  return <div className={styles.mapBadge} data-synthetic={synthetic || undefined} role="status" aria-live="polite">
    <strong>{synthetic ? "Synthetic local tile · not observed" : c.pilotReceipt ? "Dev-processed NEON pilot · review pending" : "Local NEON preview · not admitted"}</strong>
    {c.representation === "columns" && <span className={styles.heightBadge}>3D sample columns · {c.verticalExaggeration}× vertical scale · relative sampled heights{c.columns?.baseline_m !== null && c.columns?.baseline_m !== undefined ? ` · baseline ${meters(c.columns.baseline_m)}` : ""}</span>}
    <span>{c.preview.source.site} · catalog {c.preview.source.month} · {c.mode.toUpperCase()} · dated context{c.pilotReceipt?.cache.state === "stale" ? " · stale cache" : ""}</span>
  </div>;
}

export function NeonLidarMapControls({ controller: c }: { controller: NeonLidarMapController }) {
  const id = useId(), preview = c.preview;
  const present = preview?.grid[c.mode].filter(value => value !== null).length ?? 0;
  const above = c.mode === "chm" ? preview?.grid.chm.filter(value => value !== null && value > 30).length ?? 0 : 0;
  return <section className={styles.control} aria-labelledby={`${id}-title`}>
    <div className={styles.heading}><span>LOCAL NEON / TERRAIN + VEGETATION</span><h4 id={`${id}-title`}>Read the landscape together</h4></div>
    <p>One historical 1 km tile. Free, with no subscription.</p>
    <div className={styles.explore3D} aria-busy={c.busy}>
      <button type="button" className={styles.exploreButton} aria-describedby={`${id}-3d-status`} disabled={!c.canExplore3D} onClick={() => void c.explore3D()}>Explore in 3D</button>
      <p id={`${id}-3d-status`} className={c.mapError ? styles.warning : styles.hint} role="status" aria-live="polite">{c.explore3DStatus}</p>
      <div className={styles.quickActions}>{c.preview && <button type="button" disabled={c.busy || !c.canShow} onClick={c.plan}>Return to flat view</button>}{c.busy && <button type="button" onClick={c.clear}>Cancel</button>}</div>
    </div>
    {!c.flatMap && c.onFlatMap && <><button type="button" className={styles.return} onClick={c.onFlatMap}>Use local sample view</button><p className={styles.hint}>Local sample 3D uses the map camera. Statewide Terrain 3D uses a different elevation source and holds this tile.</p></>}
    <div className={styles.sourceActions}><button type="button" disabled={c.busy} onClick={() => void c.loadPilot()}>Load Konza Prairie pilot</button><Link href="/labs/terrain">Terrain Science →</Link></div>
    <p className={c.fileError || c.mapError ? styles.error : styles.status} role="status" aria-live="polite" aria-busy={c.busy}>{c.status}</p>
    {(!preview && !c.busy && !c.fileError) && <p className={styles.hint}>Explore in 3D loads and displays the available Konza Prairie tile in one action. Load the preview only if you want to begin with flat samples. Use <Link href="/labs/terrain">Terrain Science</Link> for distributions, relationships and exports. The pilot covers one tile, not all Kansas.</p>}
    {preview && <>
      {c.pilotReceipt && <div className={styles.pilotReview}><p><strong>Provider preview.</strong> Scientific review pending; independent accuracy and vertical reference are unverified.</p><p className={c.pilotReceipt.cache.state === "stale" ? styles.warning : styles.hint}>Cache {c.pilotReceipt.cache.state} · <time dateTime={c.pilotReceipt.cache.at}>{c.pilotReceipt.cache.at}</time>{c.pilotReceipt.cache.state === "stale" ? ". This cached preview is stale; it is not a new observation." : ". Acquisition dates remain separate from cache time."}</p><p className={styles.warning}>Native CHM maximum {c.pilotReceipt.review.canopy_native_max_m.toFixed(2)} m; {c.pilotReceipt.review.canopy_native_cells_above_50m} native cells above 50 m. Outliers retained for review, not identified as trees.</p></div>}
      {preview.data_kind === "synthetic-test" && <p className={styles.synthetic}><strong>Synthetic test · not observed terrain.</strong> These values do not describe this NEON site.</p>}
      <div className={styles.identity}><strong>{preview.source.site}</strong><span>Catalog {preview.source.month}</span><span>Run {preview.source.acquisition_run}</span><span>{preview.source.release}</span><code>{preview.source.tile}</code></div>
      <div className={styles.modes} role="group" aria-label="Local NEON surface">{modes.map(item => <button type="button" key={item.kind} aria-pressed={c.mode === item.kind} onClick={() => c.setMode(item.kind)}><small>{item.kind.toUpperCase()}</small>{item.label}</button>)}</div>
      <label className={styles.opacity} htmlFor={`${id}-opacity`}>Overlay opacity <output>{c.opacity}%</output><input id={`${id}-opacity`} type="range" min={0} max={100} step={5} value={c.opacity} aria-valuetext={`${c.opacity} percent`} onChange={event => c.setOpacity(Number(event.target.value))} /></label>
      <div className={styles.actions}><button type="button" disabled={!c.enabled && !c.canShow} aria-pressed={c.enabled} onClick={c.toggle}>{c.enabled ? "Hide" : "Show on map"}</button><button type="button" disabled={!c.canShow} onClick={c.fit}>Fit tile</button><button type="button" onClick={c.clear}>Clear</button></div>
      <div className={styles.representation} role="group" aria-label="Sample representation"><button type="button" aria-pressed={c.representation === "flat"} onClick={c.plan}>Flat samples</button><button type="button" aria-pressed={c.representation === "columns"} disabled={!c.canExplore3D} onClick={() => void c.explore3D()}>3D sample columns</button></div>
      {c.representation === "columns" && <div className={styles.columnControls}>
        <label>Vertical exaggeration <output>{c.verticalExaggeration}×</output><input type="range" min={1} max={5} step={0.5} value={c.verticalExaggeration} aria-valuetext={`${c.verticalExaggeration} times; source readings remain unscaled`} onChange={event => c.setVerticalExaggeration(Number(event.target.value))}/></label>
        <button type="button" disabled={!c.canShow || !c.enabled} onClick={c.pitch}>Pitch camera to inspect 3D</button>
        {c.columns && c.columns.omitted_cells > 0 && <p className={styles.warning}>Missing, invalid or over-budget columns are omitted. Local render-height limit: {c.columns.render_height_limit_m.toLocaleString("en-US")} m. Source readings are retained.</p>}
        <p className={styles.hint}>Relative sampled columns, not a surveyed mesh. {c.columns?.baseline_m === null ? "No valid shared baseline." : `Local baseline ${meters(c.columns?.baseline_m ?? null)}.`} {c.columns?.eligible_cells.toLocaleString("en-US")} eligible columns / {c.columns?.omitted_cells.toLocaleString("en-US")} omitted from available display cells. Height scale {c.verticalExaggeration}×; probe values stay unscaled.</p>
      </div>}
      <div className={styles.legend} aria-label={c.mode === "chm" ? "Fixed canopy scale, 0 to 30 meters" : "Shared DTM and DSM elevation scale"}><i /><div><span>{c.mode === "chm" ? "0 m" : c.elevationDomain ? meters(c.elevationDomain[0]) : "No elevation data"}</span><span>{c.mode === "chm" ? "30 m" : c.elevationDomain ? meters(c.elevationDomain[1]) : ""}</span></div></div>
      <p className={styles.hint}>{c.mode === "chm" ? `Canopy scale is fixed; heights above 30 m saturate${above ? ` (${above} samples)` : ""}.` : "Ground and surface share one elevation scale."} NoData cells stay transparent; zero remains valid.</p>
      <p className={styles.hint}>{present.toLocaleString("en-US")} / {preview.grid.width ** 2} samples present · {preview.grid.preview_resolution_m.toLocaleString("en-US", { maximumFractionDigits: 3 })} m display cells from 1 m source.</p>
      <div className={styles.probe}>
        <strong>Shared local sample</strong><p>Click a displayed cell, or enter a row and column.</p>
        <div className={styles.coordinates}><label htmlFor={`${id}-row`}>Row · N → S<input id={`${id}-row`} type="number" min={1} max={preview.grid.height} step={1} placeholder={`1–${preview.grid.height}`} value={c.coordinateDraft.row} onChange={event => c.selectAxis("row", event.target.value)} /></label><label htmlFor={`${id}-column`}>Column · W → E<input id={`${id}-column`} type="number" min={1} max={preview.grid.width} step={1} placeholder={`1–${preview.grid.width}`} value={c.coordinateDraft.column} onChange={event => c.selectAxis("column", event.target.value)} /></label></div>
        {c.probe && <>
          <dl className={styles.values}><div><dt>Ground · DTM</dt><dd>{meters(c.probe.dtm)}</dd></div><div><dt>Surface · DSM</dt><dd>{meters(c.probe.dsm)}</dd></div><div><dt>Provider canopy · CHM</dt><dd>{meters(c.probe.chm)}</dd></div><div><dt>DSM − DTM</dt><dd>{meters(c.probe.surfaceAboveGround)}</dd></div></dl>
          <p className={styles.hint}>Nearest source sample: {c.probe.easting.toFixed(1)} E / {c.probe.northing.toFixed(1)} N, native meters. DSM − DTM is surface above ground, including structures; it is not provider CHM.</p>
          {c.probe.differenceIssue === "negative" && <p className={styles.warning}>Negative source difference retained for QA; not clamped.</p>}
          {c.probe.differenceIssue === "nonfinite" && <p className={styles.warning}>Source difference exceeds numeric limits; needs QA.</p>}
          {c.probe.chm === 0 && <p className={styles.warning}>Zero canopy does not establish bare earth; low vegetation can be suppressed.</p>}
        </>}
      </div>
      {c.storyStops.length > 0 && <details className={styles.story}><summary>Follow the sampled landscape</summary><p className={styles.hint}>Show the tile, then choose a stop. Camera framing uses its display footprint; source coordinates remain in the probe. No autoplay.</p><div>{c.storyStops.map(stop => <button type="button" key={stop.id} disabled={!c.canShow || !c.enabled} onClick={() => c.focusStop(stop.id)}><span>{stop.label}</span><strong>{meters(stop.value_m)}</strong></button>)}</div><p className={styles.hint}>These extrema are from preview samples. {c.pilotReceipt ? "The flagged 83.41 m native CHM maximum is not located by this preview." : "Native extrema cannot be inferred from these samples."}</p></details>}
      <details className={styles.details}><summary>Source, alignment &amp; scientific limits</summary>
        <p>{preview.source.attribution}. Catalog month, run and release are recorded locally; file hashes do not independently authenticate them.</p>
        <p>Ground and surface: DP3.30024.001. Canopy: DP3.30015.001. Vertical reference: {preview.source.vertical_reference}. {preview.source.vertical_reference_basis}</p>
        <p>{preview.georeferencing ? "Map corners are transformed offline by Rasterio/PROJ; height values stay unchanged. Horizontal transformation accuracy and coordinate epoch are unknown." : "No map georeferencing is recorded; re-prepare this file before display."} Polygons mark display-cell footprints; one nearest 1 m sample does not measure all vegetation in that cell. Source registration, map alignment, vertical datum accuracy and survey accuracy remain unverified. Two decimals show precision, not accuracy. 3D columns use a shared local baseline; canopy rises from a neutral sampled-ground pedestal only where DTM exists. Its top is ground plus independent CHM, not DSM or absolute elevation. Unrenderable columns are omitted under the local height budget; their source readings remain unchanged. Exaggeration changes the illustration, never source values. External elevation terrain and globe views remain held.</p>
        <p>This dated acquisition appears as local context at Present. It is excluded from reports, Evidence Drawer and governed source counts. No species, biomass, carbon, growth or change is inferred.</p>
        {c.pilotReceipt && <><p>Native maximum DSM − DTM: {c.pilotReceipt.review.surface_minus_ground_native_max_m.toFixed(2)} m, distinct from provider CHM.</p><ul>{c.pilotReceipt.review.notes.map((note, index) => <li key={index}>{note}</li>)}</ul></>}
        <p>Provider processing runs on the configured data workstation. This remains a preview, with source review pending.</p><div className={styles.links}><Link href="/labs/terrain">Full Science lab →</Link><Link href="/acquisition">Acquisition receipts →</Link><a href="https://www.neonscience.org/resources/learning-hub/tutorials/lidar-uncertainty-r" target="_blank" rel="noreferrer">NEON uncertainty guide ↗</a></div>
      </details>
    </>}
    <details className={styles.details}><summary>Import a prepared local preview</summary><label className={styles.file} htmlFor={`${id}-file`}>Choose prepared preview JSON <small>2 MiB maximum</small><input id={`${id}-file`} type="file" accept="application/json,.json" onChange={event => { void c.importFile(event.target.files?.[0]); event.target.value = ""; }} /></label><p className={styles.hint}>The file stays in this tab; it is not uploaded, saved or admitted. Local and synthetic imports retain their own identity.</p></details>
    {c.busy && <button type="button" onClick={c.clear}>Cancel local read</button>}
    {!preview && !c.busy && c.fileError && <button type="button" onClick={c.clear}>Clear</button>}
  </section>;
}
