"use client";
import { lazy, Suspense, useCallback, useEffect, useLayoutEffect, useMemo, useRef, useState } from "react";
import type { GeoJSONSource, Map as MapLibreMap, MapMouseEvent } from "./maplibre-seam";
import { distanceMeters, inKansas, intervalColor, intervalCsv, intervalIssues, meters, sectionSvg, sourceLink, SUBSURFACE_LIMIT, validPosition, validGeophysicalSurvey, validAreaBounds,
  type AreaBounds, type Borehole, type DepthInterval, type GeophysicalSurvey, type Position, type SectionRecord, type SubsurfaceContext, type SubsurfaceManifest } from "./subsurface-model";
import s from "./subsurface.module.css";
import { startSubsurfaceWorker } from "./subsurface-workers";
import { atRecordYear, recordYear } from "./subsurface-materials";
import { fitRecordedSlice, sliceWindowDepth } from "./subsurface-slice";
import { cutawayLocatorPlacement } from "./cutaway-locator";

const AquiferView = lazy(() => import("./aquifer-volume-view"));
const ThreeView = lazy(() => import("./subsurface-three"));
export type SubsurfaceInspection = { record: Borehole; interval?: DepthInterval };
type Props = {
  map: MapLibreMap | null; initialContext: SubsurfaceContext | null; year: number; redacted: boolean;
  onTerrain: () => void; onFlatMap: () => void; readElevation: (point: Position) => number | null;
  isDrawing: () => boolean; onDraw: () => void; readTransect: () => Position[];
  onContext: (context: SubsurfaceContext) => void; onInspect: (inspection: SubsurfaceInspection) => void;
  onClose: () => void; onSave: () => void; onReport: () => void;
};
type WorkerResult = { id: number; bounds?: AreaBounds; manifest?: SubsurfaceManifest; columns?: SectionRecord[]; total?: number; partial?: boolean; coverage?: string; failures?: string[]; error?: string; matches?: [string, string, Position, string][] };
const EMPTY_ROUTE: Position[] = [];
const EMPTY_COLUMNS: SectionRecord[] = [];
const download = (name: string, value: string | null, type: string) => {
  if (!value) return;
  const url = URL.createObjectURL(new Blob([value], { type })); const a = document.createElement("a"); a.href = url; a.download = name; a.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
};
export default function UndergroundPanel(props: Props) {
  const { map, initialContext, year, redacted, onContext, onInspect } = props;
  const [anchor, setAnchor] = useState<Position>(initialContext?.anchor ?? (map ? [map.getCenter().lng, map.getCenter().lat] : [-95.25, 39]));
  const [pinned, setPinned] = useState(initialContext?.pinned ?? false);
  const [route, setRoute] = useState<Position[]>(initialContext?.transect ?? []);
  const [range, setRange] = useState<[number, number]>(initialContext?.depthRange ?? [0, 100]);
  const [display, setDisplay] = useState<SubsurfaceContext["display"]>(initialContext?.display ?? "aquifer");
  const [exaggeration, setExaggeration] = useState(initialContext?.exaggeration ?? 1);
  const [sources, setSources] = useState(initialContext?.selectedSources ?? ["kgs-wwc5", "kgs-core"]);
  const [manifest, setManifest] = useState<SubsurfaceManifest | null>(null);
  const [appliedArea, setAppliedArea] = useState<AreaBounds|null>(null), [areaRevision,setAreaRevision] = useState(0);
  const expectedArea = useRef<AreaBounds|null>(null);
  const areaCenter = useMemo<Position|null>(()=>appliedArea?[(appliedArea[0]+appliedArea[2])/2,(appliedArea[1]+appliedArea[3])/2]:null,[appliedArea]);
  const areaMode = display === "aquifer" || (display === "3d" && appliedArea !== null);
  const queryAnchor = areaMode && areaCenter ? areaCenter : anchor, queryRoute = areaMode ? EMPTY_ROUTE : route;
  const queryKey = JSON.stringify([areaMode ? "area" : "probe",areaMode ? appliedArea : [anchor,route],sources,year,areaMode ? areaRevision : 0]);
  const expectedQueryKey = useRef(queryKey);
  const [responseColumns, setColumns] = useState<SectionRecord[]>([]), [responseKey,setResponseKey] = useState<string|null>(null);
  // Guard during render, before debounce/effects can publish a new context with old rows.
  const loadedColumns = responseKey === queryKey ? responseColumns : EMPTY_COLUMNS;
  const [recordCutoff, setRecordCutoff] = useState<number | null>(initialContext?.recordCutoff ?? null);
  const [timePlaying, setTimePlaying] = useState(false);
  const [timeStep, setTimeStep] = useState(1500);
  const [reduceMotion, setReduceMotion] = useState(true);
  const columns = useMemo(() => loadedColumns.filter(c => atRecordYear(c.record, recordCutoff)), [loadedColumns, recordCutoff]);
  const visibleRecords = useMemo(() => columns.map(c => c.record), [columns]);
  const recordYears = useMemo(() => [...new Set(loadedColumns.map(c => recordYear(c.record)).filter((y): y is number => y !== null))].sort((a,b) => a-b), [loadedColumns]);
  useEffect(() => { const query = matchMedia("(prefers-reduced-motion: reduce)"); const changed = () => { setReduceMotion(query.matches); if (query.matches) setTimePlaying(false); }; changed(); query.addEventListener("change", changed); return () => query.removeEventListener("change", changed); }, []);
  useEffect(() => { let cancelled = false; queueMicrotask(() => { if (!cancelled) setTimePlaying(false); }); return () => { cancelled = true; }; }, [anchor, route, sources, year, display, areaRevision]);
  useEffect(() => { const pause = () => { if (document.hidden) setTimePlaying(false); }; document.addEventListener("visibilitychange", pause); return () => document.removeEventListener("visibilitychange", pause); }, []);
  useEffect(() => {
    if (!timePlaying || reduceMotion || recordYears.length < 2) return;
    const index = recordYears.findIndex(y => y === recordCutoff);
    if (index === recordYears.length - 1) { let cancelled = false; queueMicrotask(() => { if (!cancelled) setTimePlaying(false); }); return () => { cancelled = true; }; }
    const timer = setTimeout(() => setRecordCutoff(recordYears[index + 1]), timeStep);
    return () => clearTimeout(timer);
  }, [timePlaying, reduceMotion, recordYears, recordCutoff, timeStep]);
  const [coverage, setCoverage] = useState("Source assets are loading.");
  const [requestLoading, setLoading] = useState(true), [partial, setPartial] = useState(false);
  const [workerFailure,setWorkerFailure] = useState("");
  const loading = !workerFailure && (requestLoading || (responseKey !== queryKey && (!areaMode || appliedArea !== null)));
  const [selectedId, setSelectedId] = useState(initialContext?.selectedRecordId ?? initialContext?.recordIds[0] ?? "");
  const [depth, setDepth] = useState(initialContext?.cursorDepth ?? initialContext?.depthRange[0] ?? 0);
  const [descriptionFilter, setDescriptionFilter] = useState(initialContext?.descriptionFilter ?? "");
  const [sliceEnabled, setSliceEnabled] = useState(false);
  const [pickedInterval, setPickedInterval] = useState<{recordId:string; index:number}|null>(null);
  const bodyRef = useRef<HTMLDivElement>(null);
  const sliceWorkspaceRef = useRef<HTMLElement>(null), pendingSliceFocus = useRef(false);
  const sliceRecordRef = useRef("");
  const [height, setHeight] = useState(55);
  const [locatorSlot,setLocatorSlot] = useState<HTMLDivElement|null>(null);
  const initialKansasLocator = useRef(false);
  const [search, setSearch] = useState(""), [matches, setMatches] = useState<NonNullable<WorkerResult["matches"]>>([]);
  const [surveyMethod, setSurveyMethod] = useState("all"), [surveys, setSurveys] = useState<GeophysicalSurvey[]>([]);
  const [surveyError, setSurveyError] = useState("");
  const [surface, setSurface] = useState<{ distance: number; elevation: number | null }[]>([]);
  const worker = useRef<Worker | null>(null), serial = useRef(0), current = useRef(props), pinnedRef = useRef(pinned);
  useEffect(() => { current.current = props; pinnedRef.current = pinned; }, [props, pinned]);
  const selected = columns.find(r => r.record.id === selectedId)?.record ?? columns.find(c => c.record.kind === "well" && c.record.intervals.length)?.record ?? columns[0]?.record;
  const selectedIntervalIndex = pickedInterval && pickedInterval.recordId === selected?.id ? pickedInterval.index : null;
  const sliceFit = selected ? fitRecordedSlice(selected, depth, display === "aquifer" ? selectedIntervalIndex : null) : null;
  const chooseRecord = (id: string) => {
    setSelectedId(id); setDescriptionFilter(""); setPickedInterval(null);
    const record = columns.find(c => c.record.id === id)?.record;
    const fit = record && sliceEnabled ? fitRecordedSlice(record, depth) : null;
    if (fit) { setRange(current => current[0] === fit.range[0] && current[1] === fit.range[1] ? current : fit.range); setDepth(fit.depth); }
    sliceRecordRef.current = id;
  };
  // Time/location filtering can replace the selected record as well as the picker.
  useEffect(() => {
    if (!sliceEnabled || display !== "3d" || !selected || sliceRecordRef.current === selected.id) return;
    let cancelled = false;
    queueMicrotask(() => {
      if (cancelled) return;
      sliceRecordRef.current = selected.id;
      const fit = fitRecordedSlice(selected, depth);
      if (fit) { setRange(current => current[0] === fit.range[0] && current[1] === fit.range[1] ? current : fit.range); setDepth(fit.depth); }
    });
    return () => { cancelled = true; };
  }, [sliceEnabled, display, selected, depth]);
  const openSlice = () => {
    if (!selected || !sliceFit) return;
    setSelectedId(selected.id); setRange(current => current[0] === sliceFit.range[0] && current[1] === sliceFit.range[1] ? current : sliceFit.range); setDepth(sliceFit.depth); setDescriptionFilter("");
    pendingSliceFocus.current = true;
    setSliceEnabled(true); sliceRecordRef.current = selected.id; setDisplay("3d");
  };
  const toggleSlice = (enabled: boolean) => {
    if (!enabled) { setSliceEnabled(false); return; }
    if (!selected) return;
    const nextDepth = sliceWindowDepth(selected, depth, range, descriptionFilter);
    if (nextDepth === null) return;
    // Record replacement may fit later; an appearance toggle never replaces this window.
    sliceRecordRef.current = selected.id; setDepth(nextDepth); setSliceEnabled(true);
  };
  useLayoutEffect(() => {
    if (bodyRef.current) bodyRef.current.scrollTop = 0;
    if (display === "3d" && pendingSliceFocus.current && sliceWorkspaceRef.current) {
      pendingSliceFocus.current = false;
      sliceWorkspaceRef.current.focus({preventScroll:true});
    }
  }, [display]);
  const sourceVersions = useMemo(() => manifest?.sources ?? [], [manifest]);
  const context = useMemo<SubsurfaceContext>(() => ({ version: 1, capturedAt: new Date().toISOString(), anchor, pinned, transect: route,
    depthRange: range, display, exaggeration, recordCutoff, cursorDepth: Math.max(range[0], Math.min(range[1], depth)), selectedRecordId: selectedId, descriptionFilter, selectedSources: sources, sourceVersions,
    recordIds: columns.map(c => c.record.id), records: columns.map(c => c.record), coverage: [display === "aquifer" ? `Selected area: ${appliedArea?.join(", ") ?? "none applied"}. Aquifer envelope and locator image are temporary display derivatives and are not included in this saved KGS column snapshot. Aquifer source period: 2022–2024.` : "Selected underground display remains source context.", recordCutoff === null ? "Record timeline: all loaded records, including undated records." : `Record timeline: dated records through ${recordCutoff}; undated records withheld. This is not past geology.`, loading ? "Source loading: capture contains no current columns yet." : coverage, SUBSURFACE_LIMIT,
      "Core inventory ranges are sampled-envelope descriptions, not verified recovery or true vertical depth. No common elevation datum is available."] }), [anchor, pinned, route, range, display, exaggeration, sources, sourceVersions, columns, coverage, loading, depth, selectedId, descriptionFilter, recordCutoff, appliedArea]);
  useEffect(() => { if (manifest) onContext(context); }, [context, manifest, onContext]);
  useEffect(() => {
    try {
      const w = startSubsurfaceWorker(); worker.current = w;
      w.onmessage = (event: MessageEvent<WorkerResult>) => {
        const r = event.data; if (r.id !== serial.current) return;
        if (!r.matches && !r.error && expectedArea.current && (!r.bounds || r.bounds.some((value,index)=>value!==expectedArea.current![index]))) { setLoading(false); setResponseKey(expectedQueryKey.current); setColumns([]); setCoverage("Source response did not match the selected area; show the area again."); return; }
        setLoading(false); if (r.manifest) setManifest(r.manifest);
        if (r.matches) { setMatches(r.matches); return; }
        setResponseKey(expectedQueryKey.current); setColumns(r.columns ?? []); setPartial(Boolean(r.partial)); setCoverage(r.error ?? r.coverage ?? "No available data.");
      };
      w.onerror = () => { worker.current=null;w.onmessage=null;w.terminate();setWorkerFailure("Source worker unavailable");setLoading(false); setResponseKey(expectedQueryKey.current); setColumns([]); setCoverage("Source loading failed. Close and reopen Underground to retry; no underground conditions are inferred."); };
      return () => { w.onmessage = null; w.terminate(); worker.current = null; };
    } catch { queueMicrotask(() => { setWorkerFailure("Source worker unavailable");setLoading(false); setResponseKey(expectedQueryKey.current); setCoverage("Background data loading is unavailable. Close and reopen Underground to retry."); }); }
  }, []);
  const applyArea = useCallback((bounds: AreaBounds | null) => {
    if (bounds && !validAreaBounds(bounds)) bounds = null;
    // A committed frame is shared with aquifer geometry. Preview pan/zoom is not a query.
    serial.current++; setTimePlaying(false); setColumns([]); setLoading(Boolean(bounds)&&worker.current!==null);
    setAppliedArea(bounds); setAreaRevision(value=>value+1);
    if (bounds) { setAnchor([(bounds[0]+bounds[2])/2,(bounds[1]+bounds[3])/2]); setPinned(true); }
  }, []);
  useEffect(() => {
    if (!worker.current) return;
    const id = ++serial.current;
    expectedArea.current = areaMode ? appliedArea : null;
    expectedQueryKey.current = queryKey;
    const timer = setTimeout(() => {
      setColumns([]);
      if (areaMode && !appliedArea) { setLoading(false); setResponseKey(queryKey); setCoverage("Frame a local area in the selector, then choose Show this area."); return; }
      setLoading(true);
      try{worker.current?.postMessage({ id, kind: areaMode ? "area" : "probe", ...(areaMode ? {bounds:appliedArea} : {}), anchor:queryAnchor, route:queryRoute, sources, year });}catch{worker.current?.terminate();worker.current=null;setWorkerFailure("Source worker unavailable");setLoading(false);setCoverage("Source loading failed. Close and reopen Underground to retry.");}
    }, 140);
    return () => clearTimeout(timer);
  }, [areaMode, appliedArea, areaRevision, queryAnchor, queryRoute, sources, year, queryKey]);
  useEffect(() => {
    if (!map) return;
    current.current.onFlatMap();
    const rotate=map.dragRotate.isEnabled(), pitch=map.touchPitch.isEnabled();
    map.dragRotate.disable();map.touchPitch.disable();
    const north=()=>{if(Math.abs(map.getBearing())>.01||Math.abs(map.getPitch())>.01)map.jumpTo({bearing:0,pitch:0});};map.on("rotateend",north);map.on("pitchend",north);
    return()=>{map.off("rotateend",north);map.off("pitchend",north);if(rotate)map.dragRotate.enable();if(pitch)map.touchPitch.enable();};
  },[map]);
  useEffect(() => {
    if (!map) return;
    const stage = map.getContainer().closest<HTMLElement>(".map-stage");
    stage?.style.setProperty("--underground-height", `${height}%`);
    let resizeFrame:number|null=null;
    const observer = new ResizeObserver(() => {if(resizeFrame!==null)cancelAnimationFrame(resizeFrame);resizeFrame=requestAnimationFrame(()=>{resizeFrame=null;map.resize();});}); observer.observe(map.getContainer());
    map.resize();
    return () => { observer.disconnect(); if(resizeFrame!==null)cancelAnimationFrame(resizeFrame); stage?.style.removeProperty("--underground-height"); map.resize(); };
  }, [map, height, display]);
  useLayoutEffect(() => {
    if (!map || display !== "aquifer" || !locatorSlot) return;
    const stage=map.getContainer().closest<HTMLElement>(".map-stage"),scroller=locatorSlot.closest<HTMLElement>("[data-underground-scroll]");
    if(!stage||!scroller)return;
    const position=()=>{
      const a=locatorSlot.getBoundingClientRect(),b=stage.getBoundingClientRect(),clip=scroller.getBoundingClientRect();
      const placement=cutawayLocatorPlacement(a,{left:b.left,top:b.top,scrollLeft:stage.scrollLeft,scrollTop:stage.scrollTop},clip);
      stage.style.setProperty("--cutaway-locator-left",`${placement.left}px`);stage.style.setProperty("--cutaway-locator-top",`${placement.top}px`);
      stage.style.setProperty("--cutaway-locator-width",`${placement.width}px`);stage.style.setProperty("--cutaway-locator-height",`${placement.height}px`);
      stage.style.setProperty("--cutaway-locator-clip",`inset(${placement.clipTop}px 0 ${placement.clipBottom}px 0)`);
      stage.style.setProperty("--cutaway-locator-visibility",placement.visible?"visible":"hidden");
    };
    let positionFrame:number|null=null;
    const observer=new ResizeObserver(()=>{if(positionFrame!==null)cancelAnimationFrame(positionFrame);positionFrame=requestAnimationFrame(()=>{positionFrame=null;position();});});observer.observe(locatorSlot);observer.observe(stage);observer.observe(scroller);
    scroller.addEventListener("scroll",position,{passive:true});stage.addEventListener("scroll",position,{passive:true});window.addEventListener("resize",position);position();
    // Fit after the selector has its actual compact size. A fresh Underground
    // session starts with Kansas; tool switches keep the user's map position.
    const initialFrame=!initialKansasLocator.current?requestAnimationFrame(()=>{
      map.resize();
      map.fitBounds([[-102.1,36.95],[-94.55,40.05]],{padding:18,duration:0});
      initialKansasLocator.current=true;
    }):null;
    return()=>{if(initialFrame!==null)cancelAnimationFrame(initialFrame);observer.disconnect();if(positionFrame!==null)cancelAnimationFrame(positionFrame);scroller.removeEventListener("scroll",position);stage.removeEventListener("scroll",position);window.removeEventListener("resize",position);for(const key of ["left","top","width","height","clip","visibility"])stage.style.removeProperty(`--cutaway-locator-${key}`);};
  },[map,display,locatorSlot]);
  useEffect(() => {
    if (!map || display !== "aquifer") return;
    // MapLibre's compact attribution starts expanded. Use its own accessible
    // disclosure once on entry so credits stay available without covering the inset.
    const frame=requestAnimationFrame(()=>{
      const attribution=map.getContainer().querySelector(".maplibregl-ctrl-attrib.maplibregl-compact-show");
      attribution?.querySelector<HTMLElement>("summary")?.click();
    });
    return()=>cancelAnimationFrame(frame);
  },[map,display]);
  useEffect(() => {
    if (!map) return;
    let last = 0;
    const move = (e: MapMouseEvent) => {
      if (display === "aquifer" || pinnedRef.current || current.current.isDrawing() || map.isMoving() || performance.now() - last < 300) return;
      const p: Position = [e.lngLat.lng, e.lngLat.lat]; if (inKansas(p)) { last = performance.now(); setAnchor(p); }
    };
    const click = (e: MapMouseEvent) => { if (display === "aquifer" || current.current.isDrawing()) return;
      if (map.getLayer("kfm-underground-context")) {
        const hit = map.queryRenderedFeatures(e.point, {layers:["kfm-underground-context"]}).find(f => typeof f.properties?.recordId === "string");
        if (hit) { setSelectedId(hit.properties!.recordId); setDescriptionFilter(""); setPinned(true); return; }
      } const p: Position = [e.lngLat.lng, e.lngLat.lat]; if (inKansas(p)) { setAnchor(p); setPinned(true); } };
    map.on("mousemove", move); map.on("click", click);
    return () => { map.off("mousemove", move); map.off("click", click); };
  }, [map, display]);
  useEffect(() => {
    if (!map) return;
    const update = () => {
      if (!map.isStyleLoaded()) return;
      const id = "kfm-underground-context";
      const features: GeoJSON.Feature[] = columns.map(c => ({ type: "Feature", properties: { recordId:c.record.id, selected: c.record.id === selected?.id, kind: c.record.kind }, geometry: { type: "Point", coordinates: c.record.coordinates } }));
      features.push({ type: "Feature", properties: { selected: true, kind: "probe" }, geometry: { type: "Point", coordinates: anchor } });
      if (route.length > 1) features.push({ type: "Feature", properties: {}, geometry: { type: "LineString", coordinates: route } });
      const data: GeoJSON.FeatureCollection = { type: "FeatureCollection", features };
      if (!map.getSource(id)) map.addSource(id, { type: "geojson", data }); else (map.getSource(id) as GeoJSONSource).setData(data);
      if (!map.getLayer(`${id}-route`)) map.addLayer({ id: `${id}-route`, type: "line", source: id, filter: ["==", "$type", "LineString"], paint: { "line-color": "#af6639", "line-width": 3, "line-dasharray": [2, 2] } });
      if (!map.getLayer(id)) map.addLayer({ id, type: "circle", source: id, filter: ["==", "$type", "Point"], paint: { "circle-color": ["case", ["==", ["get", "kind"], "probe"], "#aa4b28", ["==", ["get", "kind"], "core"], "#795d9b", "#345e50"], "circle-radius": ["case", ["get", "selected"], 7, 4], "circle-stroke-color": "#fff5d9", "circle-stroke-width": 1.5 } });
    };
    update(); map.on("styledata", update);
    return () => { map.off("styledata", update); for (const id of ["kfm-underground-context", "kfm-underground-context-route"]) if (map.getLayer(id)) map.removeLayer(id); if (map.getSource("kfm-underground-context")) map.removeSource("kfm-underground-context"); };
  }, [map, columns, anchor, route, selected?.id]);
  useEffect(() => {
    if (display !== "surveys" || surveys.length) return;
    const controller = new AbortController();
    void fetch("/data/subsurface/geophysics.json", { signal: controller.signal }).then(r => { if (!r.ok) throw new Error(); return r.json(); }).then(data => {
      if (data.version !== 1 || !Array.isArray(data.surveys)) throw new Error();
      if (!controller.signal.aborted) setSurveys(data.surveys.filter(validGeophysicalSurvey));
    }).catch(() => { if (!controller.signal.aborted) setSurveyError("Published profiles are unavailable."); });
    return () => controller.abort();
  }, [display, surveys.length]);
  const inspect = useCallback((record: Borehole, interval?: DepthInterval) => {
    setSelectedId(record.id); setPickedInterval(interval ? {recordId:record.id,index:record.intervals.indexOf(interval)} : null); if (interval && display !== "3d") setDepth(Math.max(range[0], Math.min(range[1], meters((interval.top + interval.bottom) / 2, record.depthUnit)))); onInspect({ record, interval });
  }, [onInspect, range, display]);
  const inspectHere = () => { const c = map?.getCenter(); if (c && inKansas([c.lng, c.lat])) { setAnchor([c.lng, c.lat]); setPinned(true); } };
  const changedVersions = initialContext?.sourceVersions.some(old => manifest?.sources.some(current => current.id === old.id && current.sha256 !== old.sha256));
  const missing = initialContext?.recordIds.filter(id => !loading && !columns.some(c => c.record.id === id)) ?? [];
  const changeDepth = (index: 0 | 1, value: number) => { if (!Number.isFinite(value)) return; const next: [number, number] = [...range]; next[index] = value; if (next[0] >= 0 && next[1] > next[0] && next[1] <= 12000) { setRange(next); setDepth(Math.max(next[0], Math.min(next[1], depth))); } };
  const recordNavigation = <section className={`${s.timeControls} ${display === "aquifer" ? s.areaTime : ""}`} aria-label="Underground record timeline">
    <div><strong>Record time</strong><small>{recordCutoff === null ? "All loaded records" : `Through ${recordCutoff} · dated records`}</small></div>
    <button type="button" aria-pressed={timePlaying} disabled={!timePlaying && (reduceMotion || recordYears.length < 2 || loading)} onClick={() => { if (!timePlaying && (recordCutoff === null || recordCutoff === recordYears.at(-1))) setRecordCutoff(recordYears[0]); setTimePlaying(v => !v); }}>{timePlaying ? "Pause" : "Play"}</button>
    <input type="range" aria-label="Underground record year" aria-valuetext={recordCutoff === null ? "All loaded records" : `Dated records through ${recordCutoff}`} min="0" max={recordYears.length} value={recordCutoff === null ? recordYears.length : Math.max(0,recordYears.findIndex(y=>y>=recordCutoff))} disabled={!recordYears.length || loading} onChange={e=>{setTimePlaying(false);setRecordCutoff(recordYears[Number(e.target.value)]??null);}} />
    <label>Through <select value={recordCutoff ?? "all"} onChange={e=>{setTimePlaying(false);setRecordCutoff(e.target.value==="all"?null:Number(e.target.value));}}><option value="all">All loaded records</option>{recordCutoff!==null&&!recordYears.includes(recordCutoff)&&<option value={recordCutoff}>{recordCutoff} · saved cutoff</option>}{recordYears.map(y=><option key={y} value={y}>{y}</option>)}</select></label>
    <details className={s.recordTimeDetails}><summary>Time &amp; sources</summary>
      <p>3D space + record availability. {columns.length}/{loadedColumns.length} loaded records pass this filter; {loadedColumns.filter(c=>recordYear(c.record)===null).length} are undated. Aquifer ranges stay fixed to 2022–2024. This does not reconstruct past geology.</p>
      <p>Atlas year {year} applies first to source eligibility. Open Time in the main toolbar to change that year. All loaded records restores undated rows only when the atlas year permits them.</p>
      <label>Playback step <select value={timeStep} onChange={e=>setTimeStep(Number(e.target.value))}><option value={1500}>1.5 seconds</option><option value={3000}>3 seconds</option><option value={5000}>5 seconds</option></select></label>
      {reduceMotion&&<p>Reduced motion is on. Use the year slider or menu to step manually.</p>}
      <div className={s.actions}>{["kgs-wwc5","kgs-core"].map(id=><button type="button" key={id} aria-pressed={sources.includes(id)} onClick={()=>setSources(value=>value.includes(id)?value.filter(source=>source!==id):[...value,id])}>{id==="kgs-wwc5"?"Well logs":"Core inventory"}</button>)}</div>
    </details>
  </section>;
  return <>{display !== "aquifer" && display !== "3d" && <div className={s.locatorBar} aria-label="Underground 2D locator">
    <strong>2D locator</strong><span>{pinned ? "Pinned" : "Pointer preview"} · {anchor[1].toFixed(4)}°, {anchor[0].toFixed(4)}°</span>
    <button type="button" onClick={inspectHere}>Use map center</button><button type="button" onClick={() => { setPinned(true); map?.easeTo({center:anchor,zoom:Math.max(10,map.getZoom()),pitch:0,bearing:0,duration:reduceMotion?0:350}); }}>Find selection</button>
    <button type="button" onClick={props.onFlatMap}>Reset to 2D</button>
  </div>}<section className={`${s.panel} ${s.cutawayPanel} ${display !== "aquifer" && display !== "3d" ? s.specialistPanel : ""} ${display === "3d" ? s.slicePanel : ""}`} data-cutaway-panel={display === "aquifer" ? "true" : undefined} data-slice-panel={display === "3d" ? "true" : undefined} aria-label="Underground workspace">
    <header className={s.header}><div><h2>Underground</h2><p>Depth · space · materials · record time</p></div><span className={s.badge}>Source context</span><button type="button" onClick={props.onClose} aria-label="Close Underground">×</button></header>
    <div ref={bodyRef} className={s.body} data-underground-scroll>
      <nav className={s.workspaceNav} aria-label="Underground views">
        {display !== "aquifer" ? <button type="button" onClick={()=>setDisplay("aquifer")}>← Back to cutaway</button> : <span>Area · space · record time</span>}
        <details className={s.specialistPicker}><summary>{display === "aquifer" ? "Other tools" : "Change tool"}</summary><label>Explore <select aria-label="Underground tool" value={display} onChange={e=>setDisplay(e.target.value as SubsurfaceContext["display"])}><option value="aquifer">Area cutaway</option><option value="3d">Individual log</option><option value="section">Columns &amp; section</option><option value="surveys">Geophysical surveys</option><option value="soil">Soil horizons</option></select></label></details>
      </nav>
      {display === "3d" && <section ref={sliceWorkspaceRef} tabIndex={-1} className={s.sliceWorkspace} aria-label="Slice a recorded column">
        <div className={s.sliceRecordControls}>
          <label>Source record <select value={selected?.id ?? ""} aria-label="Slice source record" disabled={!columns.length || loading} onChange={e => chooseRecord(e.target.value)}>{!columns.length && <option value="">No loaded records</option>}{columns.map(c => <option key={c.record.id} value={c.record.id}>{c.record.name}{c.record.kind === "core" ? " · inventory envelope" : ""}</option>)}</select></label>
          <button type="button" disabled={!sliceFit} onClick={() => { if (sliceFit) { setRange(current => current[0] === sliceFit.range[0] && current[1] === sliceFit.range[1] ? current : sliceFit.range); setDepth(sliceEnabled ? sliceFit.depth : sliceFit.range[0]); setDescriptionFilter(""); } }}>Fit recorded depths</button>

        </div>
        {selected ? <Suspense fallback={<p>Loading optional 3D viewer…</p>}><ThreeView record={selected} onInspect={interval => inspect(selected, interval)} descriptionFilter={descriptionFilter} depthRange={range} depth={depth} exaggeration={exaggeration} slice={sliceEnabled && Boolean(sliceFit)} selectedIndex={selectedIntervalIndex} onDepth={setDepth} onSlice={toggleSlice} /></Suspense> : <p role="status">{loading ? "Loading eligible source records…" : "No record qualifies at this location and time. Return to Area underlay, frame a local area and choose Show this area; unknown ground remains empty."}</p>}
        <details className={s.sliceAdvanced}><summary>Depth window &amp; description filter</summary><div className={s.controls}>
          <label>Depth from <input aria-label="Minimum depth in meters" type="number" min="0" max="11999" value={range[0]} onChange={e => changeDepth(0, Number(e.target.value))} /> to <input aria-label="Maximum depth in meters" type="number" min="1" max="12000" value={range[1]} onChange={e => changeDepth(1, Number(e.target.value))} /> m</label>
          <label>Vertical scale <select value={exaggeration} onChange={e => setExaggeration(Number(e.target.value))}>{[1,2,5,10,20].map(v => <option value={v} key={v}>{v}×</option>)}</select></label>
          <label>Isolate logged description <select value={descriptionFilter} onChange={e => setDescriptionFilter(e.target.value)}><option value="">All recorded descriptions</option>{[...new Set(selected?.intervals.map(i => i.description) ?? [])].slice(0,100).map(d => <option key={d} value={d}>{d.slice(0,100)}</option>)}</select></label>
        </div></details>
      </section>}

      {display !== "aquifer" && <details className={s.probeControls}><summary>Location &amp; source tools</summary>
      {display !== "3d" && <label>Panel height <input type="range" min="35" max="70" value={height} onChange={e=>setHeight(Number(e.target.value))} /></label>}
      <div className={s.metrics}><span><b>{manifest?.totals.wellCount?.toLocaleString() ?? "…"}</b>mapped well records</span><span><b>{manifest?.totals.coreCount?.toLocaleString() ?? "…"}</b>core inventory locations</span><span><b>{pinned ? "Pinned" : "Pointer preview"}</b>{anchor[1].toFixed(4)}°, {anchor[0].toFixed(4)}°</span></div>
      <div className={s.actions}>
        <button type="button" aria-pressed={pinned} onClick={() => setPinned(v => !v)}>{pinned ? "Resume pointer preview" : "Pin this location"}</button>
        <button type="button" onClick={inspectHere}>Inspect here · map center</button>
        <span>Move crosshair:</span>{[["←", -70, 0], ["↑", 0, -70], ["↓", 0, 70], ["→", 70, 0]].map(([label, x, y]) => <button type="button" key={String(label)} aria-label={`Move map ${label}`} onClick={() => map?.panBy([Number(x), Number(y)], { duration: 0 })}>{label}</button>)}
        <button type="button" onClick={props.onDraw}>Draw a section</button><button type="button" onClick={() => { const points = props.readTransect(); if (points.length > 1 && points.length <= 100 && points.every(p => validPosition(p) && inKansas(p))) { setRoute(points); setSurface([]); setAnchor(points[0]); setPinned(true); } else setCoverage("Finish a distance line on the surface map, inside Kansas, then use this section."); }}>Use drawn section</button>
        {route.length > 0 && <button type="button" onClick={() => setRoute([])}>Clear section</button>}
      </div>
      <div className={s.actions}><label>County <select aria-label="Go to county records" value="" onChange={e => { const county = manifest?.counties.find(c => c.name === e.target.value); if (county) { setAnchor(county.coordinates); setPinned(true); map?.easeTo({ center: county.coordinates, zoom: 9, duration: 0 }); } }}><option value="">Choose a county…</option>{manifest?.counties.map(c => <option key={c.name}>{c.name}</option>)}</select></label>
        <form onSubmit={e => { e.preventDefault(); if (search.trim().length < 2) return; setLoading(true); worker.current?.postMessage({ id: ++serial.current, kind: "search", search, anchor, route, sources, year }); }}><input aria-label="Find a well ID or county" placeholder="Well ID or county" value={search} maxLength={100} onChange={e => setSearch(e.target.value)} /><button type="submit">Find statewide</button></form>
        {["kgs-wwc5", "kgs-core"].map(id => <button type="button" key={id} aria-pressed={sources.includes(id)} onClick={() => setSources(v => v.includes(id) ? v.filter(s => s !== id) : [...v, id])}>{id === "kgs-wwc5" ? "Well logs" : "Core inventory"}</button>)}
      </div>
      {matches.length > 0 && <details open><summary>First {matches.length} matching records · choose to inspect</summary><div className={s.cards}>{matches.map(([id, county, coordinates]) => <button className={s.card} type="button" key={id} onClick={() => { setAnchor(coordinates); setSelectedId(id); setPinned(true); setMatches([]); map?.easeTo({ center: coordinates, zoom: 13, duration: 0 }); }}>{id} · {county}</button>)}</div></details>}
      </details>}
      <div hidden={display !== "aquifer"}><Suspense fallback={<p>Preparing the 3D cutaway…</p>}><AquiferView active={display === "aquifer"} map={map} records={visibleRecords} onArea={applyArea} recordsLoading={loading} recordStatus={coverage} partial={partial} recordNavigation={recordNavigation} recordsAvailable={loadedColumns.length} onResetRecords={()=>{setRecordCutoff(null);setSources(["kgs-wwc5","kgs-core"]);setTimePlaying(false);}} locator={{anchor,pinned}} onLocatorSlot={setLocatorSlot} onFlatMap={props.onFlatMap} onLocate={(point,retainView) => { setAnchor(point); setPinned(true); if(!retainView)map?.easeTo({center:point,zoom:12,pitch:0,bearing:0,duration:reduceMotion?0:420}); }} onInspect={inspect} sliceEntry={<details className={s.areaRecordTools}><summary>Inspect an individual log</summary><div className={s.sliceEntry}>
        <span className={s.cutawayEyebrow}>SOURCE DETAIL</span>
        <label>Source record <select aria-label="Source record to slice" value={selected?.id ?? ""} disabled={!columns.length || loading} onChange={e => chooseRecord(e.target.value)}>{!columns.length && <option value="">No loaded records</option>}{columns.map(c => <option key={c.record.id} value={c.record.id}>{c.record.name}{c.record.kind === "core" ? " · inventory envelope" : ""}</option>)}</select></label>
        <button type="button" disabled={!sliceFit || loading} onClick={openSlice}>Open selected log <span aria-hidden="true">↗</span></button>
        <p>{loading ? "Loading eligible source records…" : sliceFit ? `${selected?.name} · ${selected?.kind === "core" ? "inventory envelope only" : "recorded log"}. Open and drag the depth slider to look inside.` : selected ? "This record has no valid interval within 0–12,000 m. Choose another loaded record." : "Show an area in the selector to load its source records."}</p>
      </div></details>} /></Suspense></div>
      {(display === "section" || display === "3d") && loadedColumns.length > 0 && recordNavigation}

      {display === "section" && <details className={s.specialistSettings}><summary>Section depth &amp; scale</summary><div className={s.controls}><label>Depth from <input aria-label="Minimum depth in meters" type="number" min="0" max="11999" value={range[0]} onChange={e => changeDepth(0, Number(e.target.value))} /> to <input aria-label="Maximum depth in meters" type="number" min="1" max="12000" value={range[1]} onChange={e => changeDepth(1, Number(e.target.value))} /> m</label><label>Depth cursor <input type="range" min={range[0]} max={range[1]} step={(range[1] - range[0]) / 500} value={depth} onChange={e => setDepth(Number(e.target.value))} />{depth.toFixed(1)} m</label><label>Vertical scale <select value={exaggeration} onChange={e => setExaggeration(Number(e.target.value))}>{[1,2,5,10,20].map(v => <option value={v} key={v}>{v}×</option>)}</select></label><button type="button" onClick={() => setExaggeration(1)}>1× vertical</button></div></details>}
      {display === "section" && route.length > 1 && <details><summary>Surface elevation context</summary><div className={s.actions}><button type="button" onClick={props.onTerrain}>Enable surface DEM</button><button type="button" onClick={() => { let distance = 0; const samples: { distance: number; elevation: number | null }[] = []; for (let i = 1; i < route.length; i++) { const a = route[i - 1], b = route[i], length = distanceMeters(a, b); for (let j = i === 1 ? 0 : 1; j <= 8; j++) { const f = j / 8; samples.push({ distance: distance + f * length, elevation: props.readElevation([a[0] + f * (b[0] - a[0]), a[1] + f * (b[1] - a[1])]) }); } distance += length; } setSurface(samples); }}>Sample loaded surface terrain</button></div><p className={s.muted}>Uses existing unexaggerated display DEM samples. Vertical reference is provider-dependent; this profile is deliberately separate from drilling depth and is not included in the underground snapshot.</p>{surface.length > 0 && <SurfaceProfile samples={surface} />}</details>}
      <p hidden={display !== "section" && display !== "3d"} className={s.muted} role="status">{loading ? "Loading eligible source tiles…" : coverage} {partial ? "Partial coverage: choose a smaller area or shorten the section for more detail." : ""}</p>
      {changedVersions && <p className={s.limit}>A source edition changed since this investigation was saved. The view uses the current validated assets; prior captured reports retain their dated values.</p>}
      {missing.length > 0 && <p className={s.limit}>Reopened settings: {missing.length} previously captured records are not in the current eligible response. Saved rows have not been substituted.</p>}
      {display === "section" && <div className={`${s.grid} ${s.specialistResult}`}><div className={s.plotScroll}><SectionPlot columns={columns} route={route} range={range} exaggeration={exaggeration} depth={depth} selectedId={selected?.id} onInspect={inspect} /></div><details className={s.sectionRecords}><summary>Loaded source records · {columns.length}</summary><div className={s.cards}>{columns.map(c => <button className={s.card} key={c.record.id} type="button" aria-pressed={selected?.id === c.record.id} onClick={() => inspect(c.record)}><strong>{c.record.name}</strong><small>{c.record.kind === "core" ? "Core inventory envelope" : "Logged description"} · {(c.distanceMeters / 1000).toFixed(2)} km from probe</small>{route.length > 1 && <small>{(c.offsetMeters / 1000).toFixed(2)} km off section</small>}<small>{c.record.intervals.length} intervals · {c.record.sourceTime}</small></button>)}</div></details></div>}

      {display === "surveys" && <div className={s.specialistResult}><h3>Geophysical surveys</h3><details><summary>Survey filters</summary><label>Survey method <select value={surveyMethod} onChange={e => setSurveyMethod(e.target.value)}>{["all", "gpr", "electromagnetic", "electrical", "seismic"].map(m => <option key={m} value={m}>{m === "gpr" ? "Ground-penetrating radar" : m}</option>)}</select></label></details>{surveyError && <p role="status">{surveyError}</p>}{surveys.filter(v => surveyMethod === "all" || v.method === surveyMethod).map(survey => <SurveyView key={survey.id} survey={survey} anchor={anchor} onLocate={p => { setAnchor(p); setPinned(true); map?.easeTo({ center: p, zoom: 13, duration: 0 }); }} />)}{surveys.length > 0 && !surveys.some(v => surveyMethod === "all" || v.method === surveyMethod) && <p>None in the verified available data for this method.</p>}<details><summary>Survey interpretation limits</summary><p className={s.limit}>Kansas River 3D sediment model: blocked until native numerical geometry, references, and reuse terms qualify. Published report images are not used as numerical surfaces. GPR time is not converted to depth without a documented velocity model.</p></details></div>}
      {display === "soil" && <section className={s.specialistResult}><h3>Soil horizons</h3>{redacted ? <p className={s.limit}>Location privacy is active. A soil lookup would send this coordinate to USDA, so it is withheld.</p> : <SoilView key={anchor.join(",")} anchor={anchor} />}</section>}
      <details className={s.exportTools}><summary>Save &amp; export</summary><p>Saved reports and exports contain bounded KGS records; survey profiles and live soil results are not included.</p><div className={s.actions}><button type="button" onClick={props.onSave}>Save investigation</button><button type="button" onClick={props.onReport}>Create report</button><button type="button" disabled={redacted || loading || !columns.length} onClick={() => download("kfm-underground-intervals.csv", intervalCsv(context, redacted), "text/csv")}>Export intervals</button><button type="button" disabled={redacted || loading || !columns.length} onClick={() => download("kfm-underground-section.svg", sectionSvg(context, redacted), "image/svg+xml")}>Export section image</button></div></details>
      {redacted && <p className={s.limit}>Location privacy is active. Underground coordinates, routes, records, and images are withheld from saves and exports.</p>}
      <details><summary>Source editions, rights &amp; coverage</summary><p className={s.limit}>{SUBSURFACE_LIMIT} {display === "section" && "At true scale, shallow intervals may be too small to distinguish across a long transect. Increase the labeled vertical scale to inspect them."}</p>{manifest?.sources.map(source => <p key={source.id}><a href={sourceLink(source.url) ?? undefined} target="_blank" rel="noreferrer">{source.title} ↗</a> · edition {source.sourceTime} · retrieved {source.retrievedAt}<br />{source.limitation}</p>)}<p>The source of this material is the Kansas Geological Survey website at http://www.kgs.ku.edu/. All Rights Reserved. <a href="https://www.kgs.ku.edu/General/copyright.html" target="_blank" rel="noreferrer">KGS use terms</a></p></details>
    </div>
  </section></>;
}

function SectionPlot({ columns, route, range, exaggeration, depth, selectedId, onInspect }: { columns: SectionRecord[]; route: Position[]; range: [number, number]; exaggeration: number; depth: number; selectedId?: string; onInspect: (record: Borehole, interval?: DepthInterval) => void }) {
  const plotted = [...columns].sort((a, b) => route.length > 1 ? a.alongMeters - b.alongMeters : a.distanceMeters - b.distanceMeters).slice(0, 20);
  const length = route.slice(1).reduce((sum, p, i) => sum + distanceMeters(route[i], p), 0);
  const span = range[1] - range[0], truePlotHeight = length > 0 ? Math.max(.2, span / length * 820 * exaggeration) : 265;
  const plotHeight = Math.min(1200, truePlotHeight), svgHeight = Math.max(330, plotHeight + 105);
  const y = (m: number) => 42 + (m - range[0]) / span * plotHeight;
  return <><p className={s.muted}>{route.length > 1 ? `${(length / 1000).toFixed(2)} km section · ${exaggeration}× vertical scale${truePlotHeight > 1200 ? " (height capped; displayed scale is reduced)" : ""}. Each column starts at its own reference depth; this is not a common-elevation section.` : "Nearby recorded columns · equal display spacing, individual reference depths. Vertical scale is diagrammatic until a section is drawn."} Showing {plotted.length}/{columns.length} loaded columns. Select an interval to inspect.</p>
    {plotted.length ? <svg className={s.chart} viewBox={`0 0 960 ${svgHeight}`} role="group" aria-label="Recorded intervals and unknown gaps"><defs><pattern id="unknown-ground" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M0 6L6 0" stroke="#ced2c5" strokeWidth="1" /></pattern></defs>
      {[0,.25,.5,.75,1].map(f => <g key={f}><line x1="60" x2="940" y1={42 + f * plotHeight} y2={42 + f * plotHeight} stroke="#ccd1c6" strokeDasharray="2 5" /><text x="2" y={46 + f * plotHeight}>{(range[0] + span * f).toFixed(0)} m</text></g>)}
      {plotted.map((c, index) => { const x = route.length > 1 && length > 0 ? 75 + c.alongMeters / length * 800 : 75 + index * 820 / Math.max(1, plotted.length); return <g key={c.record.id}><text transform={`translate(${x + 4},29) rotate(-25)`} fontSize="9">{c.record.name}</text><rect x={x} y="42" width="20" height={plotHeight} fill="url(#unknown-ground)" stroke={selectedId === c.record.id ? "#a2512e" : "#9ba692"} />{c.record.intervals.map((i, k) => { const a = Math.max(range[0], meters(i.top, c.record.depthUnit)), b = Math.min(range[1], meters(i.bottom, c.record.depthUnit)); return b <= a ? null : <rect className={s.interval} key={k} tabIndex={0} role="button" aria-label={`${c.record.name}, ${i.top} to ${i.bottom} ${c.record.depthUnit}, ${i.description}`} x={x} y={y(a)} width="20" height={Math.max(.2, y(b) - y(a))} fill={c.record.kind === "core" ? "#9c92b0" : intervalColor(i)} onClick={() => onInspect(c.record, i)} onKeyDown={e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); onInspect(c.record, i); } }}><title>{i.top}–{i.bottom} {c.record.depthUnit}: {i.description}</title></rect>; })}<text transform={`translate(${x},${plotHeight + 56}) rotate(25)`} fontSize="8">{route.length > 1 ? `${(c.offsetMeters / 1000).toFixed(2)} km offset` : c.record.depthReference}</text></g>; })}
      <line x1="60" x2="940" y1={y(depth)} y2={y(depth)} stroke="#ad552e" strokeDasharray="5 3" /><text x="70" y={svgHeight - 8}>Hatching: unknown / unlogged · violet: core inventory envelope · rock colors: supplied descriptions</text>
    </svg> : <div className={s.empty}>None in the available data. Move the pointer, change sources, or choose another county.</div>}</>;
}

function SurveyView({ survey, anchor, onLocate }: { survey: GeophysicalSurvey; anchor: Position; onLocate: (p: Position) => void }) {
  const [id, setId] = useState(survey.profiles[0]?.id ?? ""); const p = survey.profiles.find(p => p.id === id);
  const maxDepth = Math.max(1, ...(p?.samples.map(s => s.depth) ?? [])), maxValue = Math.max(1, ...(p?.samples.map(s => s.value) ?? []));
  const minValue = Math.min(0, ...(p?.samples.map(s => s.value) ?? []));
  const plotted = p?.samples.filter((_, i) => i % Math.max(1, Math.ceil(p.samples.length / 600)) === 0) ?? [];
  return <details><summary>{survey.title} · {survey.status} · {survey.profiles.length} profiles</summary><p>{survey.limitation}</p><p className={s.muted}>Source {survey.sourceTime} · retrieved {survey.retrievedAt}. <a href={sourceLink(survey.sourceUrl) ?? undefined} target="_blank" rel="noreferrer">Open published source ↗</a></p>
    {p && <><label>Profile <select value={id} onChange={e => setId(e.target.value)}>{survey.profiles.map(p => <option key={p.id} value={p.id}>{p.title}</option>)}</select></label> <button type="button" onClick={() => onLocate(p.coordinates)}>Locate profile · {(distanceMeters(anchor, p.coordinates) / 1000).toFixed(1)} km from probe</button><svg className={s.chart} viewBox="0 0 680 320" role="img" aria-label={`${p.title}, measured electrical conductivity versus depth`}><text x="50" y="22">Electrical conductivity {minValue.toFixed(1)}–{maxValue.toFixed(1)} {p.valueUnit}; depth 0–{maxDepth.toFixed(1)} {p.depthUnit} below local surface</text><path d={plotted.map((s, i) => `${i ? "L" : "M"}${50 + (s.value - minValue) / (maxValue - minValue) * 570},${40 + s.depth / maxDepth * 230}`).join(" ")} fill="none" stroke="#976037" strokeWidth="1.5" /><text x="50" y="300">{p.samples.length} original samples · decimated line for display · no lithology conversion</text></svg></>}
  </details>;
}
type SoilResult = { rows: (string | number | null)[][]; retrievedAt: string; partial: boolean; limitation: string; error?: string };
function SoilView({ anchor }: { anchor: Position }) {
  const [data, setData] = useState<SoilResult | null>(null), [state, setState] = useState("Loading soil-map descriptions…");
  useEffect(() => { const controller = new AbortController();
    const timer = setTimeout(() => { void fetch(`/api/subsurface/soil?lon=${anchor[0].toFixed(6)}&lat=${anchor[1].toFixed(6)}`, { signal: controller.signal }).then(r => r.json()).then((d: SoilResult) => { if (controller.signal.aborted) return; if (d.error) setState(d.error); else { setData(d); setState(d.rows.length ? "" : "None in the available soil-map data."); } }).catch(() => { if (!controller.signal.aborted) setState("Soil source unavailable."); }); }, 400);
    return () => { clearTimeout(timer); controller.abort(); };
  }, [anchor]);
  const components = [...new Set(data?.rows.map(row => String(row[3])) ?? [])];
  return <div><p role="status">{state}</p><p className={s.limit}>SSURGO soil-map components are alternatives within a mapped area. They do not identify the exact soil beneath the crosshair.</p>{data && <><p>Retrieved {data.retrievedAt} · {data.partial ? "Partial: 100-horizon limit reached" : `${data.rows.length} horizons returned`} · depths in centimetres below soil surface.</p>{components.map(id => { const rows = data.rows.filter(r => String(r[3]) === id); return <details key={id}><summary>{rows[0][4]} · {rows[0][5]}% of map unit · {rows[0][2]}</summary><ul>{rows.map((r, index) => <li key={index}>{r[8]}: {r[9] ?? "unknown"}–{r[10] ?? "unknown"} cm · sand {r[11] ?? "unknown"}%, silt {r[12] ?? "unknown"}%, clay {r[13] ?? "unknown"}%</li>)}</ul></details>; })}</>}<a href="https://sdmdataaccess.nrcs.usda.gov/" target="_blank" rel="noreferrer">USDA Soil Data Access ↗</a><p className={s.muted}>Live soil responses are not yet captured in the section export; the export includes KGS columns and their source editions only.</p></div>;
}

export function SubsurfaceInspector({ inspection, onCenter, onSave, onReport }: { inspection: SubsurfaceInspection; onCenter: () => void; onSave: () => void; onReport: () => void }) {
  const { record: r, interval } = inspection; const issues = intervalIssues(r.intervals);
  return <div className={s.inspector}><span className={s.badge}>External source context · not admitted evidence</span><h3 tabIndex={-1} data-subsurface-inspector>{r.name}</h3><p>{r.kind === "core" ? "A core inventory envelope documents an archived range; it does not prove complete recovery." : "The original driller's descriptions document this record; standardized codes are KGS interpretations."}</p>
    <dl><dt>Source</dt><dd>{r.sourceId}</dd><dt>Record time</dt><dd>{r.sourceTime || "Not supplied"}</dd><dt>Depth</dt><dd>{r.depthUnit} · {r.depthReference}; no verified trajectory or elevation registration</dd><dt>Location</dt><dd>{r.locationMethod} · {r.coordinateReference}</dd><dt>Intervals</dt><dd>{r.intervals.length}; {issues.gaps.length} internal gaps; {issues.overlaps.length} overlaps retained</dd></dl>
    {interval && <section className={s.selected}><strong>{interval.top}–{interval.bottom} {r.depthUnit}</strong><p>Original: {interval.description}</p>{interval.interpreted && <p>KGS interpreted codes: {interval.interpreted}</p>}<p>Unknown gaps remain unknown; no rock geometry is inferred between observations.</p></section>}
    <div className={s.actions}><button type="button" onClick={onCenter}>Center</button><a href={sourceLink(r.sourceUrl) ?? undefined} target="_blank" rel="noreferrer">Open source ↗</a>{r.photosUrl && <a href={sourceLink(r.photosUrl) ?? undefined} target="_blank" rel="noreferrer">Original core photographs ↗</a>}<button type="button" onClick={onSave}>Save investigation</button><button type="button" onClick={onReport}>Create report</button></div>
    <details><summary>All source intervals</summary><ul>{r.intervals.map((i, index) => <li key={index}><strong>{i.top}–{i.bottom} {r.depthUnit}</strong>: {i.description}{i.interpreted && <><br />KGS interpretation: {i.interpreted}</>}</li>)}</ul></details><p>{SUBSURFACE_LIMIT}</p>
  </div>;
}

function SurfaceProfile({ samples }: { samples: { distance: number; elevation: number | null }[] }) {
  const valid = samples.filter(s => s.elevation !== null); if (!valid.length) return <p>No loaded terrain elevation was available. Enable the surface DEM, wait for it to load, then sample again.</p>;
  const min = Math.min(...valid.map(s => s.elevation!)), max = Math.max(...valid.map(s => s.elevation!)), length = Math.max(1, samples.at(-1)!.distance);
  const path = samples.map((s, index) => { if (s.elevation === null) return ""; const command = index > 0 && samples[index - 1].elevation !== null ? "L" : "M"; return `${command}${45 + s.distance / length * 870},${125 - (s.elevation - min) / Math.max(1, max - min) * 80}`; }).join(" ");
  return <svg className={s.chart} style={{ minHeight: 150 }} viewBox="0 0 960 155" role="img" aria-label="Surface terrain profile, separate from drilling depth"><text x="30" y="25">Display terrain: {min.toFixed(1)}–{max.toFixed(1)} m · independent vertical display scale · {samples.length - valid.length} missing samples remain gaps</text><path d={path} stroke="#44755b" strokeWidth="2" fill="none" /><text x="30" y="148">0 km</text><text x="840" y="148">{(length / 1000).toFixed(2)} km</text></svg>;
}
