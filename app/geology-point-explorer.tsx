"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import type { GeoJSONSource, Map as MapLibreMap, MapMouseEvent } from "./maplibre-seam";
import { readBoundedJson } from "./bounded-json";
import { startSubsurfaceWorker } from "./subsurface-workers";
import type { AreaBounds, Position, SubsurfaceManifest } from "./subsurface-model";
import { RESOURCE_SOURCES, type ResourceKind, type ResourceLocation } from "./underground-resources-model";
import type { LocatorCluster, LocatorPoint } from "./geology-locator-model";
import s from "./geology-point-explorer.module.css";

type SourceResult = { rows: ResourceLocation[]; partial: boolean };
type SourceState = { rows: ResourceLocation[]; partial: boolean; error: boolean; complete: boolean };
type LocatorState = { total: number; wells: number; cores: number; points: LocatorPoint[]; clusters: LocatorCluster[]; error: boolean; loading: boolean };
type BoreholeDetail = { id: string; name: string; kind: "well" | "core"; coordinates: Position; sourceTime: string; totalDepth: number | null; depthUnit: string; depthReference: string; locationMethod: string; coordinateReference: string; sourceUrl: string; intervalCount: number };
type WorkerResult = { id: number; kind: "geology-points" | "geology-detail"; total?: number; wells?: number; cores?: number; points?: LocatorPoint[]; clusters?: LocatorCluster[]; record?: BoreholeDetail; manifest?: SubsurfaceManifest; error?: string };
const emptySource = (): SourceState => ({ rows: [], partial: false, error: false, complete: false });
const emptyLocator = (): LocatorState => ({ total: 0, wells: 0, cores: 0, points: [], clusters: [], error: false, loading: true });
const KANSAS: AreaBounds = [-102.1, 36.95, -94.55, 40.05];
const SOURCE_ID = "kfm-geology-source-points";
export const GEOLOGY_POINT_LAYER_IDS = [`${SOURCE_ID}-circles`, `${SOURCE_ID}-counts`] as const;
const formatCount = (value: number) => value.toLocaleString("en-US");
const compactCount = (value: number) => value >= 1000 ? `${(value / 1000).toFixed(value >= 10000 ? 0 : 1)}k` : String(value);
const safeKgsLink = (value: string) => { try { const url = new URL(value); return url.protocol === "https:" && (url.hostname === "kgs.ku.edu" || url.hostname.endsWith(".kgs.ku.edu")) ? url.href : null; } catch { return null; } };

/** Resource queries stay local and shrink to the actual viewport as visitors zoom. */
export function geologyPointFrame(center: Position, span: Position): AreaBounds {
  const width = Math.min(0.8, Math.max(0.002, span[0]));
  const height = Math.min(0.8, Math.max(0.002, span[1]));
  const west = Math.max(KANSAS[0], Math.min(center[0] - width / 2, KANSAS[2] - width));
  const south = Math.max(KANSAS[1], Math.min(center[1] - height / 2, KANSAS[3] - height));
  return [Number(west.toFixed(5)), Number(south.toFixed(5)), Number((west + width).toFixed(5)), Number((south + height).toFixed(5))];
}

export default function GeologyPointExplorer({ map, enabled, redacted, monitoringVisible }: { map: MapLibreMap | null; enabled: boolean; redacted: boolean; monitoringVisible: boolean }) {
  const [viewport, setViewport] = useState<AreaBounds | null>(null);
  const [frame, setFrame] = useState<AreaBounds | null>(null);
  const [sources, setSources] = useState<Record<ResourceKind, SourceState>>({ oilgas: emptySource(), minerals: emptySource() });
  const [locator, setLocator] = useState<LocatorState>(emptyLocator);
  const [snapshot, setSnapshot] = useState<{ wells: number; cores: number; capturedAt: string } | null>(null);
  const [loading, setLoading] = useState(false);
  const [workerReady, setWorkerReady] = useState(false);
  const [selected, setSelected] = useState("");
  const [detail, setDetail] = useState<BoreholeDetail | null>(null);
  const [detailError, setDetailError] = useState("");
  const [coincident, setCoincident] = useState<string[]>([]);
  const workerRef = useRef<Worker | null>(null);
  const requestNumber = useRef(0);
  const pointRequest = useRef(0);
  const detailRequest = useRef(0);
  const viewportKey = viewport?.join(",") ?? "";
  const frameKey = frame?.join(",") ?? "";
  const resourceRows = useMemo(() => [...sources.oilgas.rows, ...sources.minerals.rows], [sources]);
  const selectedResource = resourceRows.find(row => row.id === selected);
  const selectedLocator = locator.points.find(row => row.id === selected);
  const detailedFrame = Boolean(frame && frame[2] - frame[0] <= 0.25 && frame[3] - frame[1] <= 0.25);

  useEffect(() => {
    if (!map || !enabled || redacted) return;
    const update = () => {
      const bounds = map.getBounds();
      const west = Math.max(KANSAS[0], bounds.getWest()), east = Math.min(KANSAS[2], bounds.getEast());
      const south = Math.max(KANSAS[1], bounds.getSouth()), north = Math.min(KANSAS[3], bounds.getNorth());
      const next = west < east && south < north ? [west, south, east, north].map(value => Number(value.toFixed(5))) as AreaBounds : null;
      setViewport(previous => previous?.join(",") === next?.join(",") ? previous : next);
      const center = map.getCenter();
      const local = next ? geologyPointFrame([center.lng, center.lat], [bounds.getEast() - bounds.getWest(), bounds.getNorth() - bounds.getSouth()]) : null;
      setFrame(previous => previous?.join(",") === local?.join(",") ? previous : local);
    };
    update(); map.on("moveend", update);
    return () => { map.off("moveend", update); };
  }, [map, enabled, redacted]);

  useEffect(() => {
    if (!enabled || redacted) return;
    try {
      const worker = startSubsurfaceWorker(); workerRef.current = worker;
      worker.onmessage = (event: MessageEvent<WorkerResult>) => {
        const result = event.data;
        if (result.kind === "geology-points" && result.id === pointRequest.current) {
          if (result.manifest?.totals) setSnapshot({ wells: result.manifest.totals.wellCount ?? 0, cores: result.manifest.totals.coreCount ?? 0, capturedAt: result.manifest.capturedAt });
          setLocator(result.error ? { ...emptyLocator(), loading: false, error: true } : {
            total: result.total ?? 0, wells: result.wells ?? 0, cores: result.cores ?? 0,
            points: result.points ?? [], clusters: result.clusters ?? [], loading: false, error: false,
          });
        }
        if (result.kind === "geology-detail" && result.id === detailRequest.current) {
          setDetail(result.record ?? null); setDetailError(result.error ?? "");
        }
      };
      worker.onerror = () => { setLocator({ ...emptyLocator(), loading: false, error: true }); setWorkerReady(false); };
      setWorkerReady(true);
      return () => { worker.onmessage = null; worker.terminate(); workerRef.current = null; setWorkerReady(false); };
    } catch { queueMicrotask(() => setLocator({ ...emptyLocator(), loading: false, error: true })); }
  }, [enabled, redacted]);

  useEffect(() => {
    if (!workerReady || !viewport || !map) return;
    setLocator(emptyLocator()); setSelected(""); setDetail(null); setCoincident([]);
    const id = ++requestNumber.current; pointRequest.current = id;
    workerRef.current?.postMessage({ id, kind: "geology-points", bounds: viewport, maxPoints: 2500,
      columns: Math.max(8, Math.min(24, Math.round(map.getCanvas().clientWidth / 110))),
      rows: Math.max(5, Math.min(16, Math.round(map.getCanvas().clientHeight / 100))) });
  }, [workerReady, viewportKey, map]);

  useEffect(() => {
    if (!enabled || redacted || !frameKey) return;
    const controller = new AbortController();
    setLoading(true); setSelected(""); setDetail(null); setCoincident([]);
    setSources({ oilgas: emptySource(), minerals: emptySource() });
    const load = async (kind: ResourceKind): Promise<SourceState> => {
      const rows: ResourceLocation[] = [];
      const pages = detailedFrame ? 10 : 1;
      try {
        for (let page = 0; page < pages; page++) {
          const query = new URLSearchParams({ kind, bounds: frameKey });
          if (detailedFrame) query.set("page", String(page));
          const response = await fetch(`/api/subsurface/resources?${query}`, { signal: controller.signal, cache: "no-store" });
          if (!response.ok) throw new Error("Source unavailable");
          const value = await readBoundedJson(response, 1_000_000, controller.signal) as SourceResult;
          if (!Array.isArray(value.rows) || value.rows.length > (detailedFrame ? 500 : 200) || typeof value.partial !== "boolean") throw new Error("Invalid source response");
          rows.push(...value.rows);
          if (!value.partial) return { rows, partial: false, error: false, complete: true };
          if (value.rows.length === 0) break;
        }
        return { rows, partial: true, error: false, complete: false };
      } catch { return { rows: [], partial: false, error: !controller.signal.aborted, complete: false }; }
    };
    void Promise.all([load("oilgas"), load("minerals")]).then(([oilgas, minerals]) => {
      if (!controller.signal.aborted) { setSources({ oilgas, minerals }); setLoading(false); }
    });
    return () => controller.abort();
  }, [enabled, redacted, frameKey, detailedFrame]);

  useEffect(() => {
    if (!map || !enabled || redacted) return;
    const features: GeoJSON.Feature[] = [
      ...locator.points.map(row => ({ type: "Feature" as const, geometry: { type: "Point" as const, coordinates: row.coordinates }, properties: { id: row.id, kind: row.kind, tileId: row.tileId, selected: row.id === selected } })),
      ...locator.clusters.map((row, index) => ({ type: "Feature" as const, geometry: { type: "Point" as const, coordinates: row.coordinates }, properties: { id: `cluster:${index}`, kind: "cluster", count: row.count, countLabel: compactCount(row.count), wells: row.wells, cores: row.cores, west: row.bounds[0], south: row.bounds[1], east: row.bounds[2], north: row.bounds[3] } })),
      ...resourceRows.map(row => ({ type: "Feature" as const, geometry: { type: "Point" as const, coordinates: row.coordinates }, properties: { id: row.id, kind: row.id.startsWith("oilgas:") ? "oilgas" : "minerals", selected: row.id === selected } })),
    ];
    const data: GeoJSON.FeatureCollection = { type: "FeatureCollection", features };
    const draw = () => {
      if (!map.isStyleLoaded()) return;
      if (!map.getSource(SOURCE_ID)) map.addSource(SOURCE_ID, { type: "geojson", data });
      else (map.getSource(SOURCE_ID) as GeoJSONSource).setData(data);
      if (!map.getLayer(GEOLOGY_POINT_LAYER_IDS[0])) map.addLayer({ id: GEOLOGY_POINT_LAYER_IDS[0], type: "circle", source: SOURCE_ID, paint: {
        "circle-radius": ["case", ["==", ["get", "kind"], "cluster"], ["interpolate", ["linear"], ["get", "count"], 1, 10, 100, 16, 10000, 24], ["get", "selected"], 8, 5],
        "circle-color": ["match", ["get", "kind"], "well", "#75cfa7", "core", "#8dc3ee", "oilgas", "#ef9d51", "minerals", "#bd92e4", "cluster", "#347d93", "#ffffff"],
        "circle-stroke-color": "#10212d", "circle-stroke-width": 1.8,
      } });
      if (!map.getLayer(GEOLOGY_POINT_LAYER_IDS[1])) map.addLayer({ id: GEOLOGY_POINT_LAYER_IDS[1], type: "symbol", source: SOURCE_ID, filter: ["==", ["get", "kind"], "cluster"], layout: { "text-field": ["get", "countLabel"], "text-size": 11, "text-allow-overlap": true }, paint: { "text-color": "#ffffff" } });
    };
    const click = (event: MapMouseEvent) => {
      const layers = GEOLOGY_POINT_LAYER_IDS.filter(id => map.getLayer(id));
      if (!layers.length) return;
      const hits = map.queryRenderedFeatures(event.point, { layers });
      const hit = hits[0], properties = hit?.properties;
      if (typeof properties?.id !== "string") return;
      if (properties.kind === "cluster") {
        const west = Number(properties.west), south = Number(properties.south), east = Number(properties.east), north = Number(properties.north);
        if ([west, south, east, north].every(Number.isFinite)) map.fitBounds([[west, south], [east, north]], { padding: 75, maxZoom: 18, duration: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 400 });
        return;
      }
      const ids = [...new Set(hits.map(feature => feature.properties?.id).filter((id): id is string => typeof id === "string" && !id.startsWith("cluster:")))];
      setCoincident(ids); setSelected(properties.id); setDetail(null); setDetailError("");
      if ((properties.kind === "well" || properties.kind === "core") && typeof properties.tileId === "string") {
        const id = ++requestNumber.current; detailRequest.current = id;
        workerRef.current?.postMessage({ id, kind: "geology-detail", recordId: properties.id, tileId: properties.tileId });
      }
    };
    draw(); map.on("styledata", draw); map.on("click", click);
    return () => { map.off("styledata", draw); map.off("click", click);
      try { for (const id of [...GEOLOGY_POINT_LAYER_IDS].reverse()) if (map.getLayer(id)) map.removeLayer(id); if (map.getSource(SOURCE_ID)) map.removeSource(SOURCE_ID); } catch { /* A new map style may already have removed them. */ }
    };
  }, [map, enabled, redacted, locator, resourceRows, selected]);

  if (!enabled || redacted || !map) return null;
  const sourceFailure = sources.oilgas.error || sources.minerals.error;
  const displayed = locator.points.length + resourceRows.length;
  return <aside className={s.card} aria-label="Geology source points">
    <strong>2D SOURCE POINTS · KANSAS</strong>
    <div className={s.key}>
      {monitoringVisible && <span><i className={s.monitoring} /> Monitoring wells</span>}
      <span><i className={s.well} /> WWC5 wells · {formatCount(locator.wells)}</span>
      <span><i className={s.core} /> Cores · {formatCount(locator.cores)}</span>
      <span><i className={s.oilgas} /> Oil &amp; gas · {formatCount(sources.oilgas.rows.length)} shown</span>
      <span><i className={s.mine} /> Mines · {formatCount(sources.minerals.rows.length)} shown</span>
    </div>
    <p role="status">{locator.loading || loading ? "Loading geology points…" : locator.clusters.length ? `${formatCount(locator.total)} well and core locations grouped on this view. Select a group or zoom in.` : `${formatCount(displayed)} selectable source points in this view.`}</p>
    {!locator.loading && locator.error && <p>Well and core locations are unavailable; their missing markers do not mean no records exist.</p>}
    {!loading && sourceFailure && <p>One or more live KGS resource sources are unavailable in this view.</p>}
    {!loading && (sources.oilgas.partial || sources.minerals.partial) && <p>Oil, gas and mine marks are a local preview here. Zoom in to load complete local pages; crowded views still show a limit.</p>}
    <details className={s.coverage}><summary>Coverage &amp; source limits</summary>
      <p>The published KGS WWC5 and Core Library locator{snapshot ? ` contains ${formatCount(snapshot.wells)} wells and ${formatCount(snapshot.cores)} cores in its ${snapshot.capturedAt.slice(0, 10)} source snapshot` : " reports its coverage when available"}. Every valid locator point in view is counted; crowded views group locations. Zoom in to separate them.</p>
      <p>Oil, gas and mine records come from live KGS/KDHE services. At a close view, pages load until complete or 5,000 displayed per source; zoom farther to reach dense areas. A blank or failed query does not establish no records.</p>
      <p>Coordinates are source locations with varying accuracy, not surveyed underground trajectories. <a href="https://www.kgs.ku.edu/General/copyright.html" target="_blank" rel="noreferrer">KGS use terms ↗</a></p>
      <p>The source of this material is the Kansas Geological Survey website at http://www.kgs.ku.edu/. All Rights Reserved.</p>
    </details>
    {coincident.length > 1 && <label className={s.coincident}>Records under this point <select value={selected} onChange={event => {
      const id = event.target.value; setSelected(id); setDetail(null); setDetailError("");
      const row = locator.points.find(point => point.id === id);
      if (row) { const requestId = ++requestNumber.current; detailRequest.current = requestId; workerRef.current?.postMessage({ id: requestId, kind: "geology-detail", recordId: row.id, tileId: row.tileId }); }
    }}>{coincident.map(id => <option key={id} value={id}>{id}</option>)}</select></label>}
    {selectedResource && <div className={s.detail}>
      <button type="button" onClick={() => setSelected("")} aria-label="Close point details">×</button>
      <h3>{selectedResource.name}</h3><p>{selectedResource.material} · recorded {selectedResource.status}</p>
      <p>{selectedResource.coordinates[1].toFixed(5)}° N, {Math.abs(selectedResource.coordinates[0]).toFixed(5)}° W · source position</p>
      <dl>{selectedResource.details.map(([name, value]) => <div key={name}><dt>{name}</dt><dd>{value}</dd></div>)}</dl>
      <p>{selectedResource.id.startsWith("oilgas:") ? RESOURCE_SOURCES.oilgas.limitation : RESOURCE_SOURCES.minerals.limitation}</p>
      <a href={selectedResource.id.startsWith("oilgas:") ? RESOURCE_SOURCES.oilgas.link : RESOURCE_SOURCES.minerals.link} target="_blank" rel="noreferrer">KGS source and methods ↗</a>
    </div>}
    {selectedLocator && <div className={s.detail}>
      <button type="button" onClick={() => setSelected("")} aria-label="Close point details">×</button>
      <h3>{detail?.name ?? `${selectedLocator.kind === "core" ? "Core" : "Well"} ${selectedLocator.id}`}</h3>
      <p>{selectedLocator.county || "Kansas"} · {selectedLocator.coordinates[1].toFixed(5)}° N, {Math.abs(selectedLocator.coordinates[0]).toFixed(5)}° W</p>
      {detail ? <><dl><div><dt>Source date</dt><dd>{detail.sourceTime}</dd></div><div><dt>Depth</dt><dd>{detail.totalDepth === null ? "Not supplied" : `${detail.totalDepth} ${detail.depthUnit} · ${detail.depthReference}`}</dd></div><div><dt>Location</dt><dd>{detail.locationMethod} · {detail.coordinateReference}</dd></div><div><dt>Logged intervals</dt><dd>{detail.intervalCount}</dd></div></dl>{safeKgsLink(detail.sourceUrl) && <a href={safeKgsLink(detail.sourceUrl)!} target="_blank" rel="noreferrer">Open KGS source record ↗</a>}</> : <p>{detailError || "Loading source record…"}</p>}
      <p>Recorded point and depth reference only. No continuous subsurface model or verified borehole trajectory is implied.</p>
    </div>}
  </aside>;
}
