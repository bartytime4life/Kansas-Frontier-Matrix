"use client";

import { useEffect, useMemo, useRef, useState, type FormEvent } from "react";
import type { FeatureCollection, Polygon } from "geojson";
import { browserJsonRequest } from "./browser-json-request";
import { TOPO_PAGE_SIZE, type TopoSearch, type TopoSheet } from "./historical-topo";
import type { GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";

const SOURCE = "kfm-historical-topo-footprint";
const FILL = "kfm-historical-topo-footprint-fill";
const LINE = "kfm-historical-topo-footprint-line";
const RASTER_SOURCE = "kfm-historical-topo-reviewed-source";
const RASTER_LAYER = "kfm-historical-topo-reviewed-raster";
const empty: FeatureCollection<Polygon> = { type: "FeatureCollection", features: [] };
type CatalogResponse = { state: string; sheets: TopoSheet[]; more: boolean; retrievedAt: string; message?: string };
type OverlayResponse = { state: "ready"; sheet: { id: number; scanId: number }; bounds: [number, number, number, number]; minZoom: number; maxZoom: number; sourceUrl: string; sourceSha256: string; packageId: string; reviewedAt: string; tileTemplate: string } | { state: "preparing" | "unavailable"; scanId: number; message: string };
type ReviewCandidate = { state: "staged"; rollback?: boolean; scanId: number; packageId: string; manifestSha256: string; sheet: { id: number; scanId: number }; bounds: [number, number, number, number]; minZoom: number; maxZoom: number; sourceUrl: string; sourceSha256: string; tileCount: number; previewTileTemplate: string; stagedAt?: string };

export function HistoricalTopoControl({ map, styleReady, locationPrivate, flatMap, onFlatMap }: { map: MapLibreMap | null; styleReady: boolean; locationPrivate: boolean; flatMap: boolean; onFlatMap: () => void }) {
  const [from, setFrom] = useState("1930");
  const [through, setThrough] = useState("1960");
  const [scale, setScale] = useState<TopoSearch["scale"]>("all");
  const [name, setName] = useState("");
  const [search, setSearch] = useState<TopoSearch>(() => {
    const center = map?.getCenter();
    return { lng: center?.lng ?? -98.4, lat: center?.lat ?? 38.5, from: 1930, through: 1960, scale: "all", name: "", offset: 0 };
  });
  const [rows, setRows] = useState<TopoSheet[]>([]);
  const [selectedId, setSelectedId] = useState<number | null>(null);
  const [more, setMore] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [retrievedAt, setRetrievedAt] = useState("");
  const [retry, setRetry] = useState(0);
  const [overlayOpacity, setOverlayOpacity] = useState(0.65);
  const selected = useMemo(() => rows.find((row) => row.id === selectedId) ?? null, [rows, selectedId]);
  useEffect(() => {
    if (locationPrivate) return;
    const controller = new AbortController();
    const params = new URLSearchParams(Object.entries(search).map(([key, value]) => [key, String(value)]));
    void (async () => {
      await Promise.resolve();
      if (controller.signal.aborted) return;
      setLoading(true);
      setError("");
      try {
        const { response, body: value } = await browserJsonRequest(`/api/historical-topo?${params}`, { signal: controller.signal, maxBytes: 512 * 1024 });
        const body = value as CatalogResponse;
        if (!response.ok || body.state !== "available" || !Array.isArray(body.sheets)) throw new Error(body.message || "USGS catalog unavailable.");
        if (controller.signal.aborted) return;
        setRows((current) => search.offset === 0 ? body.sheets : [...current, ...body.sheets.filter((sheet) => !current.some((known) => known.id === sheet.id))]);
        setMore(body.more);
        setRetrievedAt(body.retrievedAt);
        setError("");
      } catch (cause) {
        if (!controller.signal.aborted) setError(cause instanceof Error ? cause.message : "USGS catalog unavailable.");
      } finally { if (!controller.signal.aborted) setLoading(false); }
    })();
    return () => controller.abort();
  }, [search, retry, locationPrivate]);

  useEffect(() => {
    if (!map || !styleReady) return;
    try {
      if (!map.getSource(SOURCE)) map.addSource(SOURCE, { type: "geojson", data: empty });
      if (!map.getLayer(FILL)) map.addLayer({ id: FILL, type: "fill", source: SOURCE, paint: { "fill-color": "#f4cf7b", "fill-opacity": 0, "fill-opacity-transition": { duration: 220 } } });
      if (!map.getLayer(LINE)) map.addLayer({ id: LINE, type: "line", source: SOURCE, paint: { "line-color": "#f8df9e", "line-width": 2.3, "line-opacity": 0, "line-opacity-transition": { duration: 220 } } });
    } catch { return; }
    return () => {
      try {
        if (map.getLayer(LINE)) map.removeLayer(LINE);
        if (map.getLayer(FILL)) map.removeLayer(FILL);
        if (map.getSource(SOURCE)) map.removeSource(SOURCE);
      } catch { /* A basemap change may already have removed this temporary overlay. */ }
    };
  }, [map, styleReady]);

  useEffect(() => {
    if (!map || !styleReady) return;
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    try {
      if (reducedMotion) {
        map.setPaintProperty(FILL, "fill-opacity-transition", { duration: 0 });
        map.setPaintProperty(LINE, "line-opacity-transition", { duration: 0 });
      }
      map.setPaintProperty(FILL, "fill-opacity", 0);
      map.setPaintProperty(LINE, "line-opacity", 0);
    } catch { return; }
    const timer = window.setTimeout(() => {
      try {
        (map.getSource(SOURCE) as GeoJSONSource | undefined)?.setData(selected ? { type: "FeatureCollection", features: [selected.footprint] } : empty);
        if (selected) {
          map.setPaintProperty(FILL, "fill-opacity", 0.1);
          map.setPaintProperty(LINE, "line-opacity", 0.95);
        }
      } catch { /* Style replacement may have removed the temporary source. */ }
    }, reducedMotion ? 0 : 130);
    return () => window.clearTimeout(timer);
  }, [map, styleReady, selected]);

  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const center = map?.getCenter();
    if (!center || locationPrivate) return;
    const start = Number(from), end = Number(through);
    if (!Number.isInteger(start) || !Number.isInteger(end) || start < 1800 || end > 2100 || start > end) {
      setError("Choose a valid year range from 1800 to 2100.");
      return;
    }
    setSelectedId(null);
    setMore(false);
    setSearch({ lng: center.lng, lat: center.lat, from: start, through: end, scale, name: name.trim(), offset: 0 });
    setRetry((value) => value + 1);
  }

  return <section className="map-utility-section historical-topo-control" aria-label="Historical topographic sheets">
    <div className="map-utility-section-heading"><span>USGS TOPOVIEW CATALOG · KANSAS</span><h3>Find a Kansas map edition</h3><p>Search Kansas sheets near the map center by name, printed year, and scale. Select a result to see its actual catalog footprint at map scale.</p></div>
    <form className="historical-topo-search" onSubmit={submit}>
      <label className="historical-topo-name">Sheet name <input type="search" maxLength={40} value={name} onChange={(event) => setName(event.target.value)} placeholder="Any name near map center" /></label>
      <div className="historical-topo-range"><label>From year <input type="number" min="1800" max="2100" step="1" value={from} onChange={(event) => setFrom(event.target.value)} /></label><label>Through year <input type="number" min="1800" max="2100" step="1" value={through} onChange={(event) => setThrough(event.target.value)} /></label></div>
      <label>Map scale <select value={scale} onChange={(event) => setScale(event.target.value as TopoSearch["scale"])}><option value="all">Any scale</option><option value="24000">1:24,000</option><option value="62500">1:62,500</option><option value="125000">1:125,000</option><option value="250000">1:250,000</option></select></label>
      <button type="submit" disabled={loading || locationPrivate || !map}>Search near map center</button>
    </form>
    {locationPrivate && <div className="map-utility-boundary" data-tone="privacy"><strong>Private location</strong><p>Use Fit Kansas before searching. This prevents a browser-location-derived camera from being sent to the USGS catalog.</p></div>}
    <div className="historical-topo-status" role="status" aria-live="polite">{locationPrivate ? "Search held while map location is private." : loading ? `Checking USGS Kansas catalog…${rows.length ? " Previous results remain below." : ""}` : error ? `${error}${rows.length ? " Previous search results remain below." : ""}` : `${rows.length} Kansas sheet${rows.length === 1 ? "" : "s"} shown${more ? " · more available" : ""} near ${search.lat.toFixed(2)}°, ${search.lng.toFixed(2)}°`}</div>
    {rows.length > 0 && <div className="historical-topo-results" aria-label="Historical map editions" aria-busy={loading}>{rows.map((sheet) => <button key={sheet.id} type="button" className="historical-topo-result" disabled={loading} aria-pressed={selectedId === sheet.id} onClick={() => { setSelectedId(sheet.id); }}><span className="historical-topo-year">{sheet.year}</span><span><strong>{sheet.name}, {sheet.state}</strong><small>1:{sheet.scale.toLocaleString()} · {sheet.series} · scan {sheet.scanId}</small></span><span aria-hidden="true">⌖</span></button>)}</div>}
    {more && search.offset < 240 && <button className="historical-topo-more" type="button" disabled={loading} onClick={() => setSearch((current) => ({ ...current, offset: current.offset + TOPO_PAGE_SIZE }))}>Show more editions</button>}
    {more && search.offset >= 240 && <p className="historical-topo-limit">More catalog sheets may exist. Narrow the years, scale, name, or map area to continue.</p>}
    {!loading && !error && rows.length === 0 && <div className="map-utility-empty"><strong>No Kansas catalog sheets match this view</strong><p>Use Fit Kansas or move the map into Kansas, widen the years, or remove the name filter. An empty search does not establish that no historical map exists.</p></div>}
    {selected && <HistoricalTopoSheetControl key={`${selected.id}:${selected.scanId}`} selected={selected} map={map} styleReady={styleReady} flatMap={flatMap} onFlatMap={onFlatMap} overlayOpacity={overlayOpacity} setOverlayOpacity={setOverlayOpacity} />}
    <aside className="map-utility-boundary"><strong>Historical map context</strong><p>Only sheets whose USGS primary state is Kansas appear here. A border sheet can extend beyond the state line. Edition and imprint years do not date every feature printed on a sheet. This browser is external context only; it does not add a KFM evidence record or change the active map time.</p><a href="https://ngmdb.usgs.gov/topoview/help/" target="_blank" rel="noreferrer">How USGS TopoView works ↗</a>{retrievedAt && <small>Catalog checked {new Date(retrievedAt).toLocaleString()}</small>}</aside>
  </section>;
}

/** Keyed by catalog edition and scan ID: an unmounted sheet cannot update its successor. */
function HistoricalTopoSheetControl({ selected, map, styleReady, flatMap, onFlatMap, overlayOpacity, setOverlayOpacity }: { selected: TopoSheet; map: MapLibreMap | null; styleReady: boolean; flatMap: boolean; onFlatMap: () => void; overlayOpacity: number; setOverlayOpacity: (value: number) => void }) {
  const [overlay, setOverlay] = useState<OverlayResponse | null>(null);
  const [overlayLoading, setOverlayLoading] = useState(true);
  const [overlayError, setOverlayError] = useState("");
  const [overlayRetry, setOverlayRetry] = useState(0);
  const [overlayVisible, setOverlayVisible] = useState(true);
  const [mapZoom, setMapZoom] = useState(() => map?.getZoom() ?? 0);
  const [mapPitch, setMapPitch] = useState(() => map?.getPitch() ?? 0);
  const [reviewCandidate, setReviewCandidate] = useState<ReviewCandidate | null>(null);
  const [reviewPreview, setReviewPreview] = useState(false);
  const [reviewNote, setReviewNote] = useState("");
  const [reviewBusy, setReviewBusy] = useState(false);
  const action = useRef<AbortController | null>(null);
  useEffect(() => () => action.current?.abort(), []);
  const display = useMemo(() => reviewPreview && reviewCandidate ? { ...reviewCandidate, tileTemplate: reviewCandidate.previewTileTemplate } : overlay?.state === "ready" ? overlay : null, [reviewPreview, reviewCandidate, overlay]);

  useEffect(() => {
    const controller = new AbortController();
    const scanId = selected.scanId;
    void (async () => {
      try {
        const { response, body: value } = await browserJsonRequest(`/api/historical-topo/overlay?scan=${scanId}`, { signal: controller.signal, maxBytes: 16 * 1024 });
        const body = value as OverlayResponse & { error?: string };
        if (!response.ok || !["ready", "preparing", "unavailable"].includes(body.state)) throw new Error(body.error || "Map overlay status is unavailable.");
        if (body.state === "ready" && (body.sheet.id !== selected.id || body.sheet.scanId !== scanId)) throw new Error("The reviewed image does not match this sheet edition.");
        if (!controller.signal.aborted) setOverlay(body);
      } catch (cause) {
        if (!controller.signal.aborted) setOverlayError(cause instanceof Error ? cause.message : "Map overlay status is unavailable.");
      } finally { if (!controller.signal.aborted) setOverlayLoading(false); }
    })();
    return () => controller.abort();
  }, [selected, overlayRetry]);

  useEffect(() => {
    if (!map || !styleReady || !display || !overlayVisible || !flatMap || mapPitch > 0) return;
    try {
      if (map.getLayer(RASTER_LAYER)) map.removeLayer(RASTER_LAYER);
      if (map.getSource(RASTER_SOURCE)) map.removeSource(RASTER_SOURCE);
      map.addSource(RASTER_SOURCE, { type: "raster", tiles: [display.tileTemplate], tileSize: 256, bounds: display.bounds,
        minzoom: display.minZoom, maxzoom: display.maxZoom, attribution: reviewPreview ? "USGS Historical Topographic Map Collection · private review preview" : "USGS Historical Topographic Map Collection · reviewed KFM display carrier" });
      map.addLayer({ id: RASTER_LAYER, type: "raster", source: RASTER_SOURCE, paint: { "raster-opacity": 0, "raster-fade-duration": 0 } }, map.getLayer(FILL) ? FILL : undefined);
    } catch { return; }
    return () => {
      try {
        if (map.getLayer(RASTER_LAYER)) map.removeLayer(RASTER_LAYER);
        if (map.getSource(RASTER_SOURCE)) map.removeSource(RASTER_SOURCE);
      } catch { /* A basemap change may have already removed the raster. */ }
    };
  }, [map, styleReady, display, reviewPreview, overlayVisible, flatMap, mapPitch]);

  useEffect(() => {
    if (!map || !styleReady || !map.getLayer(RASTER_LAYER)) return;
    try { map.setPaintProperty(RASTER_LAYER, "raster-opacity", overlayOpacity); } catch { /* Style replacement. */ }
  }, [map, styleReady, display, overlayVisible, flatMap, mapPitch, overlayOpacity]);

  useEffect(() => {
    if (!map) return;
    const update = () => { setMapZoom(map.getZoom()); setMapPitch(map.getPitch()); };
    map.on("moveend", update);
    return () => { map.off("moveend", update); };
  }, [map]);

  function fitSheet(sheet: TopoSheet) {
    if (!map) return;
    const points = sheet.footprint.geometry.coordinates.flat();
    const [west, south, east, north] = display ? display.bounds : [
      Math.min(...points.map((point) => point[0])), Math.min(...points.map((point) => point[1])),
      Math.max(...points.map((point) => point[0])), Math.max(...points.map((point) => point[1])),
    ];
    const compact = window.innerWidth <= 760;
    map.fitBounds([[west, south], [east, north]], {
      padding: compact ? { top: 55, left: 30, right: 30, bottom: Math.round(window.innerHeight * 0.48) } : { top: 80, left: 80, right: 480, bottom: 80 },
      maxZoom: 12, duration: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 650,
    });
  }

  function refreshOverlay() {
    setOverlay(null); setOverlayError(""); setOverlayLoading(true);
    setOverlayRetry((value) => value + 1);
  }

  function beginAction() {
    action.current?.abort();
    const controller = new AbortController();
    action.current = controller;
    return controller;
  }

  async function requestOverlay(sheet: TopoSheet) {
    const controller = beginAction();
    setOverlayError(""); setOverlayLoading(true);
    try {
      const { response, body } = await browserJsonRequest("/api/historical-topo/overlay", { signal: controller.signal, maxBytes: 4096, method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ id: sheet.id }) });
      if (controller.signal.aborted) return;
      const result = body as { state?: string; error?: string };
      if (!response.ok || !["ready", "preparing"].includes(result.state ?? "")) throw new Error(result.error || "Map request could not be queued.");
      refreshOverlay();
    } catch (cause) {
      if (!controller.signal.aborted) { setOverlayError(cause instanceof Error && cause.name !== "TimeoutError" ? cause.message : "Map request could not be confirmed. Check status before retrying."); setOverlayLoading(false); }
    }
  }

  async function checkReview(sheet: TopoSheet, previous = false) {
    const controller = beginAction();
    setReviewBusy(true); setOverlayError(""); setReviewCandidate(null); setReviewPreview(false); setReviewNote("");
    try {
      const { response, body: value } = await browserJsonRequest(`/api/historical-topo/review?scan=${sheet.scanId}${previous ? "&mode=previous" : ""}`, { signal: controller.signal, maxBytes: 16 * 1024 });
      if (controller.signal.aborted) return;
      const body = value as ReviewCandidate & { error?: string };
      if (!response.ok) throw new Error(body.error || "Review candidate is unavailable.");
      if (body.state !== "staged") { setOverlayError(previous ? "No prior reviewed map is available for rollback." : "This sheet has no staged candidate yet."); return; }
      if (body.sheet.id !== sheet.id || body.sheet.scanId !== sheet.scanId || body.scanId !== sheet.scanId) throw new Error("Prepared candidate does not match this Kansas sheet.");
      setReviewCandidate(body);
    } catch (cause) { if (!controller.signal.aborted) setOverlayError(cause instanceof Error ? cause.message : "Review candidate is unavailable."); }
    finally { if (!controller.signal.aborted) setReviewBusy(false); }
  }

  async function activateCandidate() {
    if (!reviewCandidate || reviewCandidate.sheet.id !== selected.id || reviewCandidate.sheet.scanId !== selected.scanId || reviewNote.trim().length < 10) return;
    const controller = beginAction();
    setReviewBusy(true); setOverlayError("");
    try {
      const { response, body: value } = await browserJsonRequest("/api/historical-topo/activate", { signal: controller.signal, maxBytes: 4096, method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ scanId: reviewCandidate.scanId, packageId: reviewCandidate.packageId, manifestSha256: reviewCandidate.manifestSha256, note: reviewNote.trim(), ...(reviewCandidate.rollback ? { rollback: true } : {}) }) });
      if (controller.signal.aborted) return;
      const body = value as { active?: boolean; error?: string };
      if (!response.ok || !body.active) throw new Error(body.error || "Candidate activation failed.");
      setReviewPreview(false); setReviewCandidate(null); setReviewNote(""); refreshOverlay();
    } catch (cause) { if (!controller.signal.aborted) setOverlayError(cause instanceof Error && cause.name !== "TimeoutError" ? cause.message : "Activation could not be confirmed. Check status before retrying."); }
    finally { if (!controller.signal.aborted) setReviewBusy(false); }
  }

  return <article className="historical-topo-detail"><header><span>SELECTED USGS SHEET</span><strong>{selected.name} · {selected.year}</strong></header><dl><div><dt>Printed map year</dt><dd>{selected.year}</dd></div><div><dt>Imprint year</dt><dd>{selected.imprintYear ?? "Not listed"}</dd></div><div><dt>Print scale</dt><dd>1:{selected.scale.toLocaleString()}</dd></div><div><dt>Scan ID</dt><dd>{selected.scanId}</dd></div><div><dt>Datum</dt><dd>{selected.datum}</dd></div></dl><div className="historical-topo-actions"><button type="button" onClick={() => fitSheet(selected)}>{overlay?.state === "ready" ? "Fit map image" : "Fit actual footprint"}</button><a href={selected.viewerHref} target="_blank" rel="noreferrer">Open USGS TopoView ↗</a></div>
      <div className="historical-topo-overlay-controls" aria-live="polite">
        <strong>{overlayLoading ? "Checking prepared image…" : overlay?.state === "ready" ? "Reviewed map image ready" : overlay?.state === "preparing" ? "Requested for preparation and review" : "Map image not prepared"}</strong>
        {overlay?.state === "ready" && <button type="button" onClick={() => void checkReview(selected, true)} disabled={reviewBusy || overlayLoading}>Inspect previous reviewed version</button>}
        {display ? <>
          {(!flatMap || mapPitch > 0) && <button type="button" onClick={onFlatMap}>View at scale on flat map</button>}
          <label><input type="checkbox" checked={overlayVisible} onChange={(event) => setOverlayVisible(event.target.checked)} /> Show sheet over basemap</label>
          <label>Image opacity <input type="range" min="0" max="100" value={Math.round(overlayOpacity * 100)} onChange={(event) => setOverlayOpacity(Number(event.target.value) / 100)} disabled={!overlayVisible} aria-valuetext={`${Math.round(overlayOpacity * 100)} percent`} /><output>{Math.round(overlayOpacity * 100)}%</output></label>
          <small>USGS scan {selected.scanId} · {reviewPreview ? "private preview; not active" : overlay?.state === "ready" ? `reviewed ${new Date(overlay.reviewedAt).toLocaleString()}` : "not released"} · native detail through map zoom {display.maxZoom}</small>
          {mapZoom > display.maxZoom && <small>Zoomed beyond this scan’s native detail; pixels are enlarged, not new map information.</small>}
        </> : overlay?.state === "preparing" ? <><p>The catalog outline remains visible until the scanned image is prepared, checked, and reviewed.</p><button type="button" onClick={refreshOverlay} disabled={reviewBusy || overlayLoading}>Check status</button><button type="button" onClick={() => void checkReview(selected)} disabled={reviewBusy || overlayLoading}>Inspect prepared candidate</button></> : !overlayLoading && <button type="button" disabled={reviewBusy} onClick={() => void requestOverlay(selected)}>Prepare this Kansas sheet</button>}
        {reviewCandidate && <div className="historical-topo-review"><strong>{reviewCandidate.rollback ? "Owner rollback review" : "Owner candidate review"} · {reviewCandidate.tileCount} verified tile addresses</strong><small>Source digest {reviewCandidate.sourceSha256.slice(0, 16)}… · package {reviewCandidate.packageId}</small><label><input type="checkbox" checked={reviewPreview} onChange={(event) => setReviewPreview(event.target.checked)} /> Preview {reviewCandidate.rollback ? "previous version" : "candidate"} on map</label><label>Review note <textarea value={reviewNote} onChange={(event) => setReviewNote(event.target.value)} maxLength={1000} placeholder="Record image alignment and source checks" /></label><button type="button" disabled={reviewBusy || reviewNote.trim().length < 10} onClick={() => void activateCandidate()}>{reviewCandidate.rollback ? "Restore previous reviewed image" : "Activate reviewed image"}</button></div>}
        {overlayError && <><p role="alert">{overlayError}</p><button type="button" disabled={reviewBusy || overlayLoading} onClick={refreshOverlay}>Check status</button></>}
      </div>
      <p>The historical image is display context. Printed dates do not date every road, building, or other feature shown.</p></article>;
}
