"use client";

import { useCallback, useEffect, useLayoutEffect, useMemo, useRef, useState } from "react";
import type { GeoJSONSource, Map as MapLibreMap, MapMouseEvent } from "./maplibre-seam";
import { readBoundedJson } from "./bounded-json";
import { startSubsurfaceWorker } from "./subsurface-workers";
import type { AreaBounds, Position, SubsurfaceManifest } from "./subsurface-model";
import { RESOURCE_SOURCES, type ResourceKind, type ResourceLocation } from "./underground-resources-model";
import type { LocatorCluster, LocatorPoint } from "./geology-locator-model";
import { geologyResourceCells, layoutResourceGroups, type ResourceCell, type ResourceGroup } from "./geology-resource-grid";
import { GeologyLayerControls, type GeologyPointVisibility, type GeologyPointKind, type GeologyEarthquakeMode } from "./geology-layer-controls";
import s from "./geology-point-explorer.module.css";

type SourceResult = { rows: ResourceLocation[]; partial: boolean };
type SourceState = { rows: ResourceLocation[]; groups: ResourceGroup[]; unavailable: number; partial: boolean; error: boolean; complete: boolean };
type LocatorState = { total: number; wells: number; cores: number; points: LocatorPoint[]; clusters: LocatorCluster[]; error: boolean; loading: boolean };
type BoreholeDetail = { id: string; name: string; kind: "well" | "core"; coordinates: Position; sourceTime: string; totalDepth: number | null; depthUnit: string; depthReference: string; locationMethod: string; coordinateReference: string; sourceUrl: string; intervalCount: number };
type WorkerResult = { id: number; kind: "geology-points" | "geology-detail"; total?: number; wells?: number; cores?: number; points?: LocatorPoint[]; clusters?: LocatorCluster[]; record?: BoreholeDetail; manifest?: SubsurfaceManifest; error?: string };
type BrowseCategory = "groups" | "wells" | "cores" | "oilgas" | "minerals";
type BrowseItem =
  | { type: "group"; id: string; label: string; detailLabel: string; coordinates: Position; count: number; region: string; wells?: number; cores?: number }
  | { type: "point"; id: string; label: string; point: LocatorPoint | ResourceLocation };
const emptySource = (): SourceState => ({ rows: [], groups: [], unavailable: 0, partial: false, error: false, complete: false });
const emptyLocator = (): LocatorState => ({ total: 0, wells: 0, cores: 0, points: [], clusters: [], error: false, loading: true });
const pendingLocator = emptyLocator();
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

export default function GeologyPointExplorer({ map, enabled, redacted, monitoringVisible, pickingEnabled, visibility, onVisibility, earthquakeMode, onEarthquakeMode, onUnderground, recentTime, dockOpen }: { map: MapLibreMap | null; enabled: boolean; redacted: boolean; monitoringVisible: boolean; pickingEnabled: () => boolean; visibility: GeologyPointVisibility; onVisibility: (kind: GeologyPointKind, shown: boolean) => void; earthquakeMode: GeologyEarthquakeMode; onEarthquakeMode: (mode: GeologyEarthquakeMode) => void; onUnderground: () => void; recentTime?: string | null; dockOpen: boolean }) {
  const [viewport, setViewport] = useState<AreaBounds | null>(null);
  const [frame, setFrame] = useState<AreaBounds | null>(null);
  const [sources, setSources] = useState<Record<ResourceKind, SourceState>>({ oilgas: emptySource(), minerals: emptySource() });
  const [locator, setLocator] = useState<LocatorState>(emptyLocator);
  const [locatorKindsKey, setLocatorKindsKey] = useState("11");
  const [snapshot, setSnapshot] = useState<{ wells: number; cores: number; capturedAt: string } | null>(null);
  const [loading, setLoading] = useState(true);
  const [workerReady, setWorkerReady] = useState(false);
  const [selected, setSelected] = useState("");
  const [detail, setDetail] = useState<BoreholeDetail | null>(null);
  const [detailError, setDetailError] = useState("");
  const [coincident, setCoincident] = useState<string[]>([]);
  const [retainedLocator, setRetainedLocator] = useState<LocatorPoint | null>(null);
  const [retainedResource, setRetainedResource] = useState<ResourceLocation | null>(null);
  const [inspectedGroup, setInspectedGroup] = useState<{ label: string; count: number; region: string; canZoom: boolean; wells?: number; cores?: number } | null>(null);
  const [mobileExpanded, setMobileExpanded] = useState(false);
  const [browseCategory, setBrowseCategory] = useState<BrowseCategory>("groups");
  const [browsePage, setBrowsePage] = useState(0);
  const groupHeadingRef = useRef<HTMLHeadingElement | null>(null);
  const detailHeadingRef = useRef<HTMLHeadingElement | null>(null);
  const workerRef = useRef<Worker | null>(null);
  const countCache = useRef(new Map<string, { count: number; expiresAt: number }>());
  const dataRef = useRef<GeoJSON.FeatureCollection>({ type: "FeatureCollection", features: [] });
  const pickingRef = useRef(pickingEnabled);
  useLayoutEffect(() => { pickingRef.current = pickingEnabled; }, [pickingEnabled]);
  const requestNumber = useRef(0);
  const pointRequest = useRef(0);
  const pointRequestKinds = useRef("11");
  const detailRequest = useRef(0);
  const viewportKey = viewport?.join(",") ?? "";
  const frameKey = frame?.join(",") ?? "";
  const kindsKey = `${Number(visibility.well)}${Number(visibility.core)}`;
  const shownLocator = locatorKindsKey === kindsKey ? locator : pendingLocator;
  const resourceRows = useMemo(() => [...(visibility.oilgas ? sources.oilgas.rows : []), ...(visibility.minerals ? sources.minerals.rows : [])], [sources, visibility.oilgas, visibility.minerals]);
  const resourceGroups = useMemo(() => map ? layoutResourceGroups(
    [...(visibility.oilgas ? sources.oilgas.groups : []), ...(visibility.minerals ? sources.minerals.groups : [])],
    map.getCanvas().clientWidth,
    coordinates => map.project(coordinates),
    point => map.unproject([point.x, point.y]),
  ) : [], [map, sources, viewportKey, visibility.oilgas, visibility.minerals]);
  const browseItems = useMemo((): BrowseItem[] => {
    if (browseCategory === "groups") return [
      ...shownLocator.clusters.map((group, index): BrowseItem => ({ type: "group", id: `locator:${index}`, label: `${formatCount(group.count)} well and core locations · ${formatCount(group.wells)} ${group.wells === 1 ? "well" : "wells"}, ${formatCount(group.cores)} ${group.cores === 1 ? "core" : "cores"}`, detailLabel: group.wells && group.cores ? "WWC5 wells and cores" : group.wells ? "WWC5 wells" : "cores", coordinates: group.coordinates, count: group.count, region: "locator group", wells: group.wells, cores: group.cores })),
      ...resourceGroups.map((group): BrowseItem => ({ type: "group", id: `source:${group.kind}:${group.id}`, label: `${formatCount(group.count)} ${group.kind === "oilgas" ? "oil and gas" : "mine"} source records · regional count`, detailLabel: group.kind === "oilgas" ? "Oil and gas source records" : "Mine source records", coordinates: group.displayCoordinates, count: group.count, region: "whole source count region" })),
    ].sort((a, b) => a.type === "group" && b.type === "group" ? b.coordinates[1] - a.coordinates[1] || a.coordinates[0] - b.coordinates[0] || a.id.localeCompare(b.id) : 0);
    if (browseCategory === "wells" || browseCategory === "cores") return shownLocator.points.filter(point => point.kind === (browseCategory === "wells" ? "well" : "core"))
      .map(point => ({ type: "point", id: point.id, label: `${point.kind === "well" ? "WWC5 well" : "Core"} ${point.id} · ${point.county || "Kansas"}`, point }));
    return resourceRows.filter(point => point.id.startsWith(`${browseCategory}:`) && (!viewport || (point.coordinates[0] >= viewport[0] && point.coordinates[0] <= viewport[2] && point.coordinates[1] >= viewport[1] && point.coordinates[1] <= viewport[3])))
      .map(point => ({ type: "point", id: point.id, label: `${browseCategory === "oilgas" ? "Oil and gas well" : "Mine"} · ${point.name}`, point }));
  }, [browseCategory, shownLocator.clusters, shownLocator.points, resourceGroups, resourceRows, viewportKey]);
  const browsePageCount = Math.max(1, Math.ceil(browseItems.length / 20));
  const visibleBrowsePage = Math.min(browsePage, browsePageCount - 1);
  const visibleBrowseItems = browseItems.slice(visibleBrowsePage * 20, visibleBrowsePage * 20 + 20);
  const selectedResource = resourceRows.find(row => row.id === selected) ?? (retainedResource?.id === selected && visibility[retainedResource.id.startsWith("oilgas:") ? "oilgas" : "minerals"] ? retainedResource : undefined);
  const selectedLocator = shownLocator.points.find(row => row.id === selected) ?? (retainedLocator?.id === selected && visibility[retainedLocator.kind] ? retainedLocator : undefined);
  const detailedFrame = Boolean(viewport && viewport[2] - viewport[0] <= 0.8 && viewport[3] - viewport[1] <= 0.8);

  const inspectGroup = useCallback((group: { label: string; count: number; region: string; coordinates: Position; wells?: number; cores?: number }, fromBrowser = false) => {
    const canZoom = Boolean(map && map.getZoom() < 18);
    setInspectedGroup({ label: group.label, count: group.count, region: group.region, wells: group.wells, cores: group.cores, canZoom });
    setMobileExpanded(true);
    if (fromBrowser) requestAnimationFrame(() => groupHeadingRef.current?.focus());
    if (map && canZoom) map.easeTo({ center: group.coordinates, zoom: Math.min(18, map.getZoom() + 2), duration: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 360, essential: false });
  }, [map]);
  const inspectPoint = useCallback((point: LocatorPoint | ResourceLocation, coincidentIds?: string[], fromBrowser = false) => {
    setSelected(point.id); setDetail(null); setDetailError(""); setInspectedGroup(null);
    setCoincident(coincidentIds ?? [point.id]); setMobileExpanded(true);
    if ("tileId" in point) {
      setRetainedLocator(point); setRetainedResource(null);
      const id = ++requestNumber.current; detailRequest.current = id;
      workerRef.current?.postMessage({ id, kind: "geology-detail", recordId: point.id, tileId: point.tileId });
    } else { setRetainedResource(point); setRetainedLocator(null); }
    if (fromBrowser) requestAnimationFrame(() => detailHeadingRef.current?.focus());
  }, []);

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
          setLocator(previous => result.error ? { ...previous, loading: false, error: true } : {
            total: result.total ?? 0, wells: result.wells ?? 0, cores: result.cores ?? 0,
            points: result.points ?? [], clusters: result.clusters ?? [], loading: false, error: false,
          });
          setLocatorKindsKey(pointRequestKinds.current);
        }
        if (result.kind === "geology-detail" && result.id === detailRequest.current) {
          setDetail(result.record ?? null); setDetailError(result.error ?? "");
        }
      };
      worker.onerror = () => { setLocator(previous => ({ ...previous, loading: false, error: true })); setWorkerReady(false); };
      setWorkerReady(true);
      return () => { worker.onmessage = null; worker.terminate(); workerRef.current = null; setWorkerReady(false); };
    } catch { queueMicrotask(() => setLocator(previous => ({ ...previous, loading: false, error: true }))); }
  }, [enabled, redacted]);

  useEffect(() => {
    if (!workerReady || !viewport || !map) return;
    setLocator(previous => ({ ...previous, loading: true }));
    const id = ++requestNumber.current; pointRequest.current = id;
    pointRequestKinds.current = kindsKey;
    workerRef.current?.postMessage({ id, kind: "geology-points", bounds: viewport, maxPoints: 2500, visible: { well: visibility.well, core: visibility.core },
      columns: Math.max(8, Math.min(24, Math.round(map.getCanvas().clientWidth / 110))),
      rows: Math.max(5, Math.min(16, Math.round(map.getCanvas().clientHeight / 100))) });
  }, [workerReady, viewportKey, map, kindsKey, visibility.well, visibility.core]);

  useEffect(() => {
    const hidden = (selected.startsWith("wwc5-") && !visibility.well) || (selected.startsWith("core-") && !visibility.core)
      || (selected.startsWith("oilgas:") && !visibility.oilgas) || (selected.startsWith("minerals:") && !visibility.minerals);
    if (hidden) { setSelected(""); setDetail(null); setCoincident([]); setInspectedGroup(null); }
    if ((browseCategory === "wells" && !visibility.well) || (browseCategory === "cores" && !visibility.core)
      || (browseCategory === "oilgas" && !visibility.oilgas) || (browseCategory === "minerals" && !visibility.minerals)) setBrowseCategory("groups");
    if (inspectedGroup) setInspectedGroup(null);
  // Selections are invalidated by a visibility change, not by a refreshed count.
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [visibility.well, visibility.core, visibility.oilgas, visibility.minerals]);

  useEffect(() => {
    if (!enabled || redacted || !viewport || !frame) return;
    const controller = new AbortController();
    setLoading(true);
    const count = async (kind: ResourceKind, cell: ResourceCell) => {
      const key = `${kind}:${cell.bounds.join(",")}`;
      const cached = countCache.current.get(key);
      if (cached && cached.expiresAt > Date.now()) return cached.count;
      const query = new URLSearchParams({ kind, bounds: cell.bounds.join(","), mode: "count" });
      const response = await fetch(`/api/subsurface/resources?${query}`, { signal: controller.signal });
      if (!response.ok) throw new Error("Source count unavailable");
      const value = await readBoundedJson(response, 100_000, controller.signal) as { count?: unknown };
      if (!Number.isSafeInteger(value.count) || Number(value.count) < 0) throw new Error("Invalid source count");
      countCache.current.set(key, { count: Number(value.count), expiresAt: Date.now() + 15 * 60_000 });
      return Number(value.count);
    };
    const load = async (kind: ResourceKind): Promise<SourceState> => {
      const cells = detailedFrame ? [{ id: "detail", bounds: frame, coordinates: [(frame[0] + frame[2]) / 2, (frame[1] + frame[3]) / 2] as Position }] : geologyResourceCells(viewport);
      const groups: ResourceGroup[] = [];
      let unavailable = 0, cursor = 0;
      const queryCell = async () => {
        while (cursor < cells.length && !controller.signal.aborted) {
          const cell = cells[cursor++];
          try { const value = await count(kind, cell); if (value > 0) groups.push({ ...cell, count: value, kind }); }
          catch { if (!controller.signal.aborted) unavailable++; }
        }
      };
      await Promise.all(Array.from({ length: Math.min(4, cells.length) }, queryCell));
      if (controller.signal.aborted) return emptySource();
      // Individual details are fetched only after a provider count proves that
      // the entire local result can be paged within a bounded request budget.
      if (detailedFrame && unavailable === 0 && groups.length === 1 && groups[0].count <= 1000) {
        const rows: ResourceLocation[] = [];
        try {
          for (let page = 0; page < 3; page++) {
            const query = new URLSearchParams({ kind, bounds: frame.join(","), page: String(page) });
            const response = await fetch(`/api/subsurface/resources?${query}`, { signal: controller.signal });
            if (!response.ok) throw new Error("Source unavailable");
            const value = await readBoundedJson(response, 1_000_000, controller.signal) as SourceResult;
            if (!Array.isArray(value.rows) || value.rows.length > 500 || typeof value.partial !== "boolean") throw new Error("Invalid source response");
            rows.push(...value.rows);
            if (!value.partial) return rows.length === groups[0].count
              ? { rows, groups: [], unavailable: 0, partial: false, error: false, complete: true }
              : { rows, groups, unavailable: 0, partial: true, error: false, complete: false };
          }
        } catch { if (controller.signal.aborted) return emptySource(); }
        return { rows: [], groups, unavailable: 0, partial: true, error: false, complete: false };
      }
      return { rows: [], groups, unavailable, partial: unavailable > 0, error: unavailable > 0, complete: unavailable === 0 };
    };
    void Promise.all([load("oilgas"), load("minerals")]).then(([oilgas, minerals]) => {
      if (!controller.signal.aborted) { setSources({ oilgas, minerals }); setLoading(false); }
    });
    return () => controller.abort();
  }, [enabled, redacted, frameKey, viewportKey, detailedFrame]);

  useEffect(() => {
    if (!map || !enabled || redacted) return;
    const mount = () => {
      if (!map.isStyleLoaded()) return;
      if (!map.getSource(SOURCE_ID)) map.addSource(SOURCE_ID, { type: "geojson", data: dataRef.current });
      if (!map.getLayer(GEOLOGY_POINT_LAYER_IDS[0])) map.addLayer({ id: GEOLOGY_POINT_LAYER_IDS[0], type: "circle", source: SOURCE_ID, paint: {
        "circle-radius": ["case", ["==", ["get", "kind"], "cluster"], ["interpolate", ["linear"], ["get", "count"], 1, 9, 100, 14, 10000, 21], ["==", ["get", "kind"], "resource-group"], ["interpolate", ["linear"], ["get", "count"], 1, 10, 100, 15, 10000, 22], ["get", "selected"], 8, 5],
        "circle-color": ["match", ["get", "kind"], "well", "#75cfa7", "core", "#8dc3ee", "oilgas", "#ef9d51", "minerals", "#bd92e4", "cluster", ["case", [">", ["get", "cores"], ["get", "wells"]], "#8dc3ee", "#75cfa7"], "resource-group", ["match", ["get", "sourceKind"], "oilgas", "#ef9d51", "#bd92e4"], "#ffffff"],
        "circle-stroke-color": ["case", ["==", ["get", "kind"], "cluster"], ["case", [">", ["get", "cores"], 0], "#8dc3ee", "#10212d"], ["==", ["get", "kind"], "resource-group"], "#f2efe4", "#10212d"], "circle-stroke-width": ["case", ["==", ["get", "kind"], "resource-group"], 2.2, 1.8],
      } });
      if (!map.getLayer(GEOLOGY_POINT_LAYER_IDS[1])) map.addLayer({ id: GEOLOGY_POINT_LAYER_IDS[1], type: "symbol", source: SOURCE_ID, filter: ["in", ["get", "kind"], ["literal", ["cluster", "resource-group"]]], layout: { "text-field": ["get", "countLabel"], "text-size": 11, "text-allow-overlap": false }, paint: { "text-color": "#10212d" } });
    };
    mount(); map.on("styledata", mount);
    return () => { map.off("styledata", mount);
      try { for (const id of [...GEOLOGY_POINT_LAYER_IDS].reverse()) if (map.getLayer(id)) map.removeLayer(id); if (map.getSource(SOURCE_ID)) map.removeSource(SOURCE_ID); } catch { /* A new map style may already have removed them. */ }
    };
  }, [map, enabled, redacted]);

  useEffect(() => {
    if (!map || !enabled || redacted) return;
    const features: GeoJSON.Feature[] = [
      ...shownLocator.points.map(row => ({ type: "Feature" as const, geometry: { type: "Point" as const, coordinates: row.coordinates }, properties: { id: row.id, kind: row.kind, tileId: row.tileId, selected: row.id === selected } })),
      ...shownLocator.clusters.map((row, index) => ({ type: "Feature" as const, geometry: { type: "Point" as const, coordinates: row.coordinates }, properties: { id: `cluster:${index}`, kind: "cluster", count: row.count, countLabel: compactCount(row.count), wells: row.wells, cores: row.cores, west: row.bounds[0], south: row.bounds[1], east: row.bounds[2], north: row.bounds[3] } })),
      ...resourceGroups.map(row => ({ type: "Feature" as const, geometry: { type: "Point" as const, coordinates: row.displayCoordinates }, properties: { id: `group:${row.kind}:${row.id}`, kind: "resource-group", sourceKind: row.kind, count: row.count, countLabel: compactCount(row.count), west: row.bounds[0], south: row.bounds[1], east: row.bounds[2], north: row.bounds[3] } })),
      ...resourceRows.map(row => ({ type: "Feature" as const, geometry: { type: "Point" as const, coordinates: row.coordinates }, properties: { id: row.id, kind: row.id.startsWith("oilgas:") ? "oilgas" : "minerals", selected: row.id === selected } })),
    ];
    const data: GeoJSON.FeatureCollection = { type: "FeatureCollection", features };
    dataRef.current = data;
    if (map.isStyleLoaded() && map.getSource(SOURCE_ID)) (map.getSource(SOURCE_ID) as GeoJSONSource).setData(data);
  }, [map, enabled, redacted, shownLocator, resourceGroups, resourceRows, selected]);

  useEffect(() => {
    if (!map || !enabled || redacted) return;
    const click = (event: MapMouseEvent) => {
      if (!pickingRef.current()) return;
      const layers = GEOLOGY_POINT_LAYER_IDS.filter(id => map.getLayer(id));
      if (!layers.length) return;
      const hits = map.queryRenderedFeatures(event.point, { layers });
      const hit = hits[0], properties = hit?.properties;
      if (typeof properties?.id !== "string") return;
      if (properties.kind === "cluster" || properties.kind === "resource-group") {
        const coordinates = hit.geometry.type === "Point" ? hit.geometry.coordinates : null;
        if (coordinates) inspectGroup({ label: properties.kind === "cluster" ? Number(properties.wells) && Number(properties.cores) ? "WWC5 wells and cores" : Number(properties.wells) ? "WWC5 wells" : "cores" : properties.sourceKind === "oilgas" ? "Oil and gas source records" : "Mine source records", count: Number(properties.count) || 0, region: properties.kind === "cluster" ? "locator group" : "whole source count region", wells: properties.kind === "cluster" ? Number(properties.wells) || 0 : undefined, cores: properties.kind === "cluster" ? Number(properties.cores) || 0 : undefined, coordinates: coordinates as Position });
        return;
      }
      const ids = [...new Set(hits.map(feature => feature.properties?.id).filter((id): id is string => typeof id === "string" && !id.startsWith("cluster:") && !id.startsWith("group:")))];
      const point = shownLocator.points.find(row => row.id === properties.id) ?? resourceRows.find(row => row.id === properties.id);
      if (point) inspectPoint(point, ids);
    };
    map.on("click", click);
    return () => { map.off("click", click); };
  }, [map, enabled, redacted, shownLocator.points, resourceRows, inspectGroup, inspectPoint]);

  if (!enabled || redacted || !map) return null;
  const sourceFailure = (visibility.oilgas && sources.oilgas.error) || (visibility.minerals && sources.minerals.error);
  const groupCount = shownLocator.clusters.length + (visibility.oilgas ? sources.oilgas.groups.length : 0) + (visibility.minerals ? sources.minerals.groups.length : 0);
  const sourceLabel = (source: SourceState) => source.rows.length ? `${formatCount(source.rows.length)} points` : source.groups.length ? `${source.groups.length} regions` : source.error ? "unavailable" : source.complete ? "0 in this view" : "checking…";
  return <aside className={s.card} aria-label="Geology source points" data-mobile-expanded={mobileExpanded} data-dock-open={dockOpen}>
    <div className={s.heading}><strong>GEOLOGY POINTS <span>· KANSAS 2D</span></strong><button type="button" className={s.mobileToggle} aria-expanded={mobileExpanded} aria-controls="geology-source-content" onClick={() => setMobileExpanded(value => !value)}>{mobileExpanded ? "Hide details" : "Show sources"}</button></div>
    <p className={s.mobileSummary} role="status">{shownLocator.loading || loading ? "Updating geology points…" : sourceFailure ? "Some source regions unavailable" : `${formatCount(shownLocator.total)} well and core locations · ${groupCount} groups`}</p>
    <div id="geology-source-content" className={s.content}>
    <details className={s.layerControls}><summary>Layer controls · {Object.values(visibility).filter(Boolean).length} of 4 point types on</summary><GeologyLayerControls compact visibility={visibility} onVisibility={onVisibility} earthquakeMode={earthquakeMode} onEarthquakeMode={onEarthquakeMode} onUnderground={onUnderground} recentTime={recentTime}
      counts={{ well: visibility.well ? shownLocator.loading && shownLocator.total === 0 ? "checking…" : `${formatCount(shownLocator.wells)} in view` : "hidden",
        core: visibility.core ? shownLocator.loading && shownLocator.total === 0 ? "checking…" : `${formatCount(shownLocator.cores)} in view` : "hidden",
        oilgas: visibility.oilgas ? sourceLabel(sources.oilgas) : "hidden", minerals: visibility.minerals ? sourceLabel(sources.minerals) : "hidden" }} /></details>
    <div className={s.key}>
      {monitoringVisible && <span><i className={s.monitoring} /> Monitoring wells</span>}
      {visibility.well && <span><i className={s.well} /> WWC5 · {shownLocator.loading && shownLocator.total === 0 ? "checking…" : `${formatCount(shownLocator.wells)} in view`}</span>}
      {visibility.core && <span><i className={s.core} /> Cores · {shownLocator.loading && shownLocator.total === 0 ? "checking…" : `${formatCount(shownLocator.cores)} in view`}</span>}
      {visibility.oilgas && <span><i className={s.oilgas} /> Oil &amp; gas · {sourceLabel(sources.oilgas)}</span>}
      {visibility.minerals && <span><i className={s.mine} /> Mines · {sourceLabel(sources.minerals)}</span>}
    </div>
    {visibility.well && visibility.core && <p className={s.legendNote}>Blue-rimmed well groups include cores; fill color shows the majority.</p>}
    <p role="status" className={s.status}>{!Object.values(visibility).some(Boolean) ? "All four geology point layers are hidden. Turn on a layer to show its source locations." : locatorKindsKey !== kindsKey ? "Updating enabled well and core groups…" : shownLocator.loading || loading ? "Updating this view · existing marks stay visible" : groupCount ? `${formatCount(shownLocator.total)} enabled well and core locations in view. Select a count group to zoom closer.` : "Individual source locations are selectable at this scale."}</p>
    {!shownLocator.loading && shownLocator.error && <p>Well and core locations are unavailable; their missing markers do not mean no records exist.</p>}
    {!loading && sourceFailure && <p>Some live source regions could not be counted. Missing marks there do not establish zero records.</p>}
    {!loading && ((visibility.oilgas && sources.oilgas.partial) || (visibility.minerals && sources.minerals.partial)) && !sourceFailure && <p>Some local source records lack selectable positions or complete pages. Their source count group remains visible.</p>}
    {inspectedGroup && <div className={s.groupDetail}><button type="button" onClick={() => setInspectedGroup(null)} aria-label="Close group details">×</button><h3 ref={groupHeadingRef} tabIndex={-1}>{formatCount(inspectedGroup.count)} {inspectedGroup.label}</h3>{inspectedGroup.wells !== undefined && inspectedGroup.cores !== undefined && <span>{formatCount(inspectedGroup.wells)} WWC5 {inspectedGroup.wells === 1 ? "well" : "wells"} · {formatCount(inspectedGroup.cores)} {inspectedGroup.cores === 1 ? "core" : "cores"}</span>}<span>{inspectedGroup.region}. {inspectedGroup.canZoom ? "Zoom closer for individual marks where the source can return complete pages." : "At this scale, these records remain grouped when a complete individual result is unavailable."}</span></div>}
    <details className={s.browse}><summary>Browse visible groups and records</summary>
      <label>Show <select value={browseCategory} onChange={event => { setBrowseCategory(event.target.value as BrowseCategory); setBrowsePage(0); }}><option value="groups">Count groups</option><option value="wells">WWC5 wells</option><option value="cores">Cores</option><option value="oilgas">Oil and gas points</option><option value="minerals">Mine points</option></select></label>
      <p className={s.browseCount} aria-live="polite">{browseItems.length ? `${formatCount(browseItems.length)} available in this view · page ${visibleBrowsePage + 1} of ${browsePageCount}` : loading || shownLocator.loading ? "Checking this view…" : "No selectable marks in this category at this scale. Choose count groups or zoom closer."}</p>
      <ol>{visibleBrowseItems.map(item => <li key={item.id}><button type="button" onClick={() => { if (item.type === "group") inspectGroup({ label: item.detailLabel, count: item.count, region: item.region, coordinates: item.coordinates, wells: item.wells, cores: item.cores }, true); else inspectPoint(item.point, undefined, true); }}>{item.type === "group" && map.getZoom() < 18 ? "Zoom to " : "Inspect "}{item.label}</button></li>)}</ol>
      {browsePageCount > 1 && <div className={s.browsePages}><button type="button" disabled={visibleBrowsePage === 0} onClick={() => setBrowsePage(visibleBrowsePage - 1)}>Previous</button><span>Page {visibleBrowsePage + 1} of {browsePageCount}</span><button type="button" disabled={visibleBrowsePage >= browsePageCount - 1} onClick={() => setBrowsePage(visibleBrowsePage + 1)}>Next</button></div>}
    </details>
    <details className={s.coverage}><summary>Coverage &amp; source limits</summary>
      <p>The published KGS WWC5 and Core Library locator{snapshot ? ` contains ${formatCount(snapshot.wells)} wells and ${formatCount(snapshot.cores)} cores in its ${snapshot.capturedAt.slice(0, 10)} source snapshot` : " reports its coverage when available"}. Every valid locator point in view is counted; crowded views group locations. Zoom in to separate them.</p>
      <p>Oil, gas and mine regions use live source counts for each whole map cell, including any sliver beyond the screen edge. Adjacent source envelopes can share boundary records; regional counts must not be added into a statewide unique total. Individual records appear only where a close frame has a verified count of 1,000 or fewer and every page loads. A failed count is unavailable, never zero.</p>
      <p>Coordinates are source locations with varying accuracy, not surveyed underground trajectories. <a href="https://www.kgs.ku.edu/General/copyright.html" target="_blank" rel="noreferrer">KGS use terms ↗</a></p>
      <p>The source of this material is the Kansas Geological Survey website at http://www.kgs.ku.edu/. All Rights Reserved.</p>
    </details>
    {coincident.length > 1 && <label className={s.coincident}>Records under this point <select value={selected} onChange={event => {
      const id = event.target.value;
      const point = shownLocator.points.find(row => row.id === id) ?? resourceRows.find(row => row.id === id);
      if (point) inspectPoint(point, coincident, true);
    }}>{coincident.map(id => <option key={id} value={id}>{id}</option>)}</select></label>}
    {selectedResource && <div className={s.detail}>
      <button type="button" onClick={() => setSelected("")} aria-label="Close point details">×</button>
      <h3 ref={detailHeadingRef} tabIndex={-1}>{selectedResource.name}</h3><p>{selectedResource.material} · recorded {selectedResource.status}</p>
      <p>{selectedResource.coordinates[1].toFixed(5)}° N, {Math.abs(selectedResource.coordinates[0]).toFixed(5)}° W · source position</p>
      <dl>{selectedResource.details.map(([name, value]) => <div key={name}><dt>{name}</dt><dd>{value}</dd></div>)}</dl>
      <p>{selectedResource.id.startsWith("oilgas:") ? RESOURCE_SOURCES.oilgas.limitation : RESOURCE_SOURCES.minerals.limitation}</p>
      <a href={selectedResource.id.startsWith("oilgas:") ? RESOURCE_SOURCES.oilgas.link : RESOURCE_SOURCES.minerals.link} target="_blank" rel="noreferrer">KGS source and methods ↗</a>
    </div>}
    {selectedLocator && <div className={s.detail}>
      <button type="button" onClick={() => setSelected("")} aria-label="Close point details">×</button>
      <h3 ref={detailHeadingRef} tabIndex={-1}>{detail?.name ?? `${selectedLocator.kind === "core" ? "Core" : "Well"} ${selectedLocator.id}`}</h3>
      <p>{selectedLocator.county || "Kansas"} · {selectedLocator.coordinates[1].toFixed(5)}° N, {Math.abs(selectedLocator.coordinates[0]).toFixed(5)}° W</p>
      {detail ? <><dl><div><dt>Source date</dt><dd>{detail.sourceTime}</dd></div><div><dt>Depth</dt><dd>{detail.totalDepth === null ? "Not supplied" : `${detail.totalDepth} ${detail.depthUnit} · ${detail.depthReference}`}</dd></div><div><dt>Location</dt><dd>{detail.locationMethod} · {detail.coordinateReference}</dd></div><div><dt>Logged intervals</dt><dd>{detail.intervalCount}</dd></div></dl>{safeKgsLink(detail.sourceUrl) && <a href={safeKgsLink(detail.sourceUrl)!} target="_blank" rel="noreferrer">Open KGS source record ↗</a>}</> : <p>{detailError || "Loading source record…"}</p>}
      <p>Recorded point and depth reference only. No continuous subsurface model or verified borehole trajectory is implied.</p>
    </div>}
    </div>
  </aside>;
}
