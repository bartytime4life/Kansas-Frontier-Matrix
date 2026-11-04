"use client";
import { useCallback, useId, useEffect, useMemo, useRef, useState, useSyncExternalStore, type RefObject } from "react";
import { createPortal } from "react-dom";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { freshAircraft, type Aircraft, type TrafficEnvelope } from "./aviation-traffic";
import { SkyBuffer, advanceSkyCursor, samplesAt, trailSegments, type SkyPoint } from "./kansas-sky";
import { attachKansasSky } from "./kansas-sky-layer";
import "./kansas-sky.css";

type CatalogFlight = { id:string;title:string;start:string;end:string;url:string;sha256:string;provider:string;license:string;sourceUrl:string };
type Mode = "live" | "session" | "recorded";
type Camera = "free" | "follow" | "orbit";
const utc=(time:number)=>new Date(time).toISOString().replace("T"," ").replace(/\.\d{3}Z$/," UTC");
const label=(a:Pick<Aircraft,"callsign"|"registration"|"hex">)=>a.callsign??a.registration??a.hex.toUpperCase();
const measure=(n:number|null|undefined,unit:string)=>n===null||n===undefined?"Unavailable":`${Math.round(n).toLocaleString("en-US")} ${unit}`;
const isObject=(v:unknown):v is Record<string,unknown>=>Boolean(v)&&typeof v==="object"&&!Array.isArray(v);
const external=(value:unknown)=>typeof value==="string"&&/^https:\/\/[^\s]+$/.test(value);
async function boundedBytes(url:string,signal:AbortSignal,max:number){
  const response=await fetch(url,{signal,credentials:"same-origin"});if(!response.ok||!response.body)throw new Error("The recorded flight is unavailable.");
  const reader=response.body.getReader(),chunks:Uint8Array[]=[];let size=0;
  try{for(;;){const {done,value}=await reader.read();if(done)break;size+=value.byteLength;if(size>max)throw new Error("The recorded flight exceeds its size bound.");chunks.push(value);}}
  catch(error){await reader.cancel();throw error;}finally{reader.releaseLock();}
  const bytes=new Uint8Array(size);let offset=0;for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.length;}return bytes;
}
function catalog(value:unknown):CatalogFlight[]{
  if(!isObject(value)||value.schemaVersion!==1||!Array.isArray(value.flights)||value.flights.length>100)throw new Error("The recorded-flight catalog is invalid.");
  return value.flights.map(v=>{if(!isObject(v)||typeof v.id!=="string"||!/^[a-z0-9-]{1,100}$/.test(v.id)||typeof v.title!=="string"||v.title.length>180||typeof v.url!=="string"||!/^\/data\/aviation\/replays\/[a-z0-9-]+\.json$/.test(v.url)||typeof v.sha256!=="string"||!/^[a-f0-9]{64}$/.test(v.sha256)||typeof v.provider!=="string"||typeof v.license!=="string"||!external(v.sourceUrl)||typeof v.start!=="string"||typeof v.end!=="string"||!Number.isFinite(Date.parse(v.start))||!Number.isFinite(Date.parse(v.end))||Date.parse(v.end)<Date.parse(v.start))throw new Error("The recorded-flight catalog is invalid.");return v as CatalogFlight;});
}
function archive(value:unknown,entry:CatalogFlight):ReadonlyMap<string,readonly SkyPoint[]>{
  if(!isObject(value)||value.schemaVersion!==1||value.id!==entry.id||value.provider!==entry.provider||value.license!==entry.license||value.sourceUrl!==entry.sourceUrl||typeof value.sourceSha256!=="string"||!/^[a-f0-9]{64}$/.test(value.sourceSha256)||!Array.isArray(value.points)||value.points.length<2||value.points.length>20000)throw new Error("Recorded-flight identity or provenance does not match.");
  const tracks=new Map<string,SkyPoint[]>();let previous=-Infinity;
  for(const p of value.points){
    if(!isObject(p)||typeof p.hex!=="string"||!/^~?[a-f0-9]{6}$/.test(p.hex)||typeof p.observedAt!=="number"||!Number.isFinite(p.observedAt)||p.observedAt<previous||p.observedAt<Date.parse(entry.start)||p.observedAt>Date.parse(entry.end)||typeof p.lon!=="number"||!Number.isFinite(p.lon)||p.lon< -103.2||p.lon> -93.6||typeof p.lat!=="number"||!Number.isFinite(p.lat)||p.lat<36.2||p.lat>40.9||typeof p.providerId!=="string"||!p.providerId||typeof p.onGround!=="boolean")throw new Error("Recorded-flight samples are invalid.");
    for(const key of ["altGeomFt","altBaroFt","groundSpeedKt","trackDeg","verticalRateFpm","rollDeg"]){if(p[key]!==null&&p[key]!==undefined&&(typeof p[key]!=="number"||!Number.isFinite(p[key])))throw new Error("Recorded-flight measurements are invalid.");}
    for(const key of ["callsign","registration","type","category","squawk","emergency","positionMethod"]){if(p[key]!==null&&p[key]!==undefined&&(typeof p[key]!=="string"||(p[key] as string).length>100))throw new Error("Recorded-flight labels are invalid.");}
    previous=p.observedAt;const track=tracks.get(p.hex)??[];track.push(p as unknown as SkyPoint);tracks.set(p.hex,track);
  }return tracks;
}

// The session recorder is an external mutable store; React observes immutable
// snapshots rather than reading or mutating refs during render.
function sessionStore() {
  const buffer=new SkyBuffer(),listeners=new Set<()=>void>();
  let snapshot={tracks:new Map(buffer.tracks()),truncated:false};
  const notify=()=>{snapshot={tracks:new Map(buffer.tracks()),truncated:buffer.truncated};listeners.forEach(fn=>fn());};
  return {buffer,read:()=>snapshot,subscribe:(fn:()=>void)=>{listeners.add(fn);return()=>{listeners.delete(fn);};},ingest:(value:TrafficEnvelope)=>{buffer.ingest(value);notify();},select:(hex:string|null)=>{buffer.select(hex);notify();}};
}

export function KansasSkyControl({mapRef,styleReady,enabled,envelope,feedState,flat=false,onReplayMode,onAircraftInspect}:{mapRef:RefObject<MapLibreMap|null>;styleReady:boolean;enabled:boolean;envelope:(TrafficEnvelope&{receivedAt:number})|null;feedState:string;flat?:boolean;onReplayMode?:(replaying:boolean)=>void;onAircraftInspect?:()=>void}){
  const inspectCallback=useRef(onAircraftInspect);
  useEffect(()=>{inspectCallback.current=onAircraftInspect;},[onAircraftInspect]);
  const [mapStatusHost,setMapStatusHost]=useState<HTMLElement|null>(null);
  useEffect(()=>{let current=true;const host=enabled&&styleReady?mapRef.current?.getContainer()??null:null;queueMicrotask(()=>{if(current)setMapStatusHost(host);});return()=>{current=false;};},[mapRef,enabled,styleReady]);
  const [store]=useState(sessionStore);
  const snapshot=useSyncExternalStore(store.subscribe,store.read,store.read);
  const [mode,setMode]=useState<Mode>("live"),[selected,setSelected]=useState<string|null>(null);
  const [cursor,setCursor]=useState(()=>Date.now()),[playing,setPlaying]=useState(false),[speed,setSpeed]=useState(1),[camera,setCamera]=useState<Camera>("free");
  const [reduced,setReduced]=useState(false),[hidden,setHidden]=useState(false),[flights,setFlights]=useState<CatalogFlight[]>([]),[catalogState,setCatalogState]=useState("idle");
  const [recorded,setRecorded]=useState<ReadonlyMap<string,readonly SkyPoint[]>>(new Map()),[entry,setEntry]=useState<CatalogFlight|null>(null),[archiveState,setArchiveState]=useState("idle"),[error,setError]=useState("");
  const [renderError,setRenderError]=useState("");
  const [aircraftFilter,setAircraftFilter]=useState("");
  const rangeId=useId(), ownCameraMove=useRef(false), latestPicked=useRef<Aircraft|undefined>(undefined);
  const layer=useRef<ReturnType<typeof attachKansasSky>|null>(null),request=useRef<AbortController|null>(null),catalogRequest=useRef<AbortController|null>(null);
  useEffect(()=>{const media=matchMedia("(prefers-reduced-motion: reduce)");const update=()=>{setReduced(media.matches);if(media.matches){setCamera("free");setPlaying(false);}};update();media.addEventListener("change",update);const visibility=()=>{setHidden(document.hidden);if(document.hidden){setPlaying(false);setCamera("free");}};visibility();document.addEventListener("visibilitychange",visibility);return()=>{media.removeEventListener("change",update);document.removeEventListener("visibilitychange",visibility);};},[]);
  useEffect(()=>{if(envelope&&enabled)store.ingest(envelope);},[envelope,enabled,store]);
  useEffect(()=>{store.select(selected);},[selected,store]);
  const [wasEnabled,setWasEnabled]=useState(enabled);
  if(wasEnabled!==enabled){setWasEnabled(enabled);if(!enabled){setPlaying(false);setCamera("free");}}
  useEffect(()=>{if(!enabled)request.current?.abort();},[enabled]);
  useEffect(()=>()=>{request.current?.abort();catalogRequest.current?.abort();},[]);
  useEffect(()=>{onReplayMode?.(enabled&&mode!=="live");return()=>onReplayMode?.(false);},[mode,enabled,onReplayMode]);
  const tracks=mode==="recorded"?recorded:snapshot.tracks;
  const range=useMemo(()=>{let start=Infinity,end=-Infinity;for(const points of tracks.values()){if(points.length){start=Math.min(start,points[0].observedAt);end=Math.max(end,points[points.length-1].observedAt);}}return Number.isFinite(start)?[start,end] as const:null;},[tracks]);
  const effectiveCursor=mode==="live"||!range?cursor:Math.max(range[0],Math.min(range[1],cursor));
  useEffect(()=>{if(!enabled||hidden)return;let last=performance.now();const timer=setInterval(()=>{const now=performance.now(),elapsed=now-last;last=now;if(mode==="live")setCursor(Math.floor(Date.now()/1000)*1000);else if(playing&&range)setCursor(at=>{const next=advanceSkyCursor(at,range,elapsed,speed);if(next>=range[1])setPlaying(false);return next;});},200);return()=>clearInterval(timer);},[enabled,hidden,mode,playing,range,speed]);
  const aircraft=useMemo(()=>mode==="live"?freshAircraft(envelope,effectiveCursor):samplesAt(tracks,effectiveCursor),[mode,envelope,tracks,effectiveCursor]);
  const trails=useMemo(()=>trailSegments(tracks,effectiveCursor,selected?3600000:600000),[tracks,effectiveCursor,selected]);
  const feedAge=envelope?cursor-Date.parse(envelope.retrievedAt):Number.NaN;
  const liveFresh=feedState==="ready"&&Number.isFinite(feedAge)&&feedAge>=-30000&&feedAge<=60000;
  const picked=aircraft.find(a=>a.hex===selected);
  useEffect(()=>{latestPicked.current=picked;},[picked]);
  const selectedSource=useMemo(()=>{const points=selected?tracks.get(selected):undefined;return points?.findLast(point=>point.observedAt<=effectiveCursor)?.providerId??null;},[tracks,selected,effectiveCursor]);
  const sourceIds=useMemo(()=>[...new Set([...tracks.values()].flatMap(points=>points.map(point=>point.providerId)))].join(", "),[tracks]);
  useEffect(()=>{const map=mapRef.current;if(!map||!styleReady||!enabled||hidden)return;try{layer.current=attachKansasSky(map,hex=>{setSelected(hex);setCamera("free");inspectCallback.current?.();},setRenderError);}catch{queueMicrotask(()=>setRenderError("Aircraft renderer unavailable; use the aircraft list."));}return()=>{layer.current?.dispose();layer.current=null;};},[mapRef,styleReady,enabled,hidden]);
  useEffect(()=>{layer.current?.update(aircraft,trails,selected,flat);},[aircraft,trails,selected,enabled,hidden,styleReady,flat]);
  useEffect(()=>{const map=mapRef.current;if(!map||!enabled)return;const release=()=>setCamera("free");const move=()=>{if(!ownCameraMove.current)release();};map.on("movestart",move);const canvas=map.getCanvas();canvas.addEventListener("pointerdown",release);canvas.addEventListener("wheel",release,{passive:true});canvas.addEventListener("keydown",release);return()=>{map.off("movestart",move);canvas.removeEventListener("pointerdown",release);canvas.removeEventListener("wheel",release);canvas.removeEventListener("keydown",release);};},[mapRef,enabled]);
  useEffect(()=>{const map=mapRef.current;if(!map||!picked||camera!=="follow"||reduced||flat||hidden||!enabled)return;ownCameraMove.current=true;try{map.jumpTo({center:[picked.lon,picked.lat],pitch:55,bearing:picked.trackDeg??map.getBearing()});}finally{ownCameraMove.current=false;}},[mapRef,picked,camera,reduced,flat,hidden,enabled]);
  useEffect(()=>{const map=mapRef.current;if(!map||camera!=="orbit"||reduced||flat||hidden||!enabled)return;const timer=setInterval(()=>{const plane=latestPicked.current;if(!plane)return;ownCameraMove.current=true;try{map.jumpTo({center:[plane.lon,plane.lat],pitch:55,bearing:map.getBearing()+1.2});}finally{ownCameraMove.current=false;}},200);return()=>clearInterval(timer);},[mapRef,camera,reduced,flat,hidden,enabled]);
  useEffect(()=>{if(mode!=="recorded"||catalogState!=="idle")return;const abort=new AbortController();catalogRequest.current=abort;boundedBytes("/data/aviation/replays/index.json",abort.signal,100000).then(bytes=>{setFlights(catalog(JSON.parse(new TextDecoder().decode(bytes))));setCatalogState("ready");}).catch(()=>{if(!abort.signal.aborted)setCatalogState("error");});},[mode,catalogState]);
  const changeMode=useCallback((next:Mode)=>{request.current?.abort();if(archiveState==="loading"){setArchiveState("idle");setEntry(null);}setMode(next);setPlaying(false);setCamera("free");setError("");if(next==="live")setCursor(Date.now());else if(next==="session"){const span=store.buffer.range();if(span)setCursor(span[0]);}else if(entry)setCursor(Date.parse(entry.start));},[archiveState,store,entry]);
  const loadRecorded=async(id:string)=>{request.current?.abort();const flight=flights.find(f=>f.id===id);setRecorded(new Map());setEntry(flight??null);setPlaying(false);setCamera("free");setError("");if(!flight){setArchiveState("idle");return;}const abort=new AbortController();request.current=abort;setArchiveState("loading");try{const bytes=await boundedBytes(flight.url,abort.signal,4*1024*1024);const digest=Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",bytes)),b=>b.toString(16).padStart(2,"0")).join("");if(digest!==flight.sha256)throw new Error("Recorded-flight digest does not match.");const parsed=archive(JSON.parse(new TextDecoder().decode(bytes)),flight);if(abort.signal.aborted)return;setRecorded(parsed);setSelected(parsed.keys().next().value??null);setCursor(Date.parse(flight.start));setArchiveState("ready");}catch(e){if(!abort.signal.aborted){setArchiveState("error");setError(e instanceof Error?e.message:"Recorded flight unavailable.");}}};
  const catalogOptions=useMemo(()=>[...tracks].flatMap(([hex,points])=>points.length?[[hex,label(points[points.length-1])] as const]:[]).sort((a,b)=>a[1].localeCompare(b[1])),[tracks]);
  const liveOptions=useMemo(()=>aircraft.map(a=>[a.hex,label(a)] as const).sort((a,b)=>a[1].localeCompare(b[1])),[aircraft]);
  const matchingOptions=useMemo(()=>{const query=aircraftFilter.trim().toLowerCase();return(mode==="live"?liveOptions:catalogOptions).filter(([hex,title])=>!query||`${hex} ${title}`.toLowerCase().includes(query));},[aircraftFilter,mode,liveOptions,catalogOptions]);
  const options=matchingOptions.slice(0,3000);
  if(selected&&!options.some(([hex])=>hex===selected)){const retained=catalogOptions.find(([hex])=>hex===selected);if(retained){if(options.length===3000)options.pop();options.push(retained);}}

  const status=mode!=="live"?"REPLAY":liveFresh?"LIVE FEED":feedState==="error"?"UNAVAILABLE":envelope?"STALE":"WAITING";
  const receiverTime=envelope?Date.parse(envelope.retrievedAt):Number.NaN;
  const mapTime=mode!=="live"?(range?effectiveCursor:Number.NaN):receiverTime;
  if(!enabled)return null;
  return <>{mapStatusHost&&createPortal(<aside className="kansas-sky-map-status" aria-label="Kansas Sky map time and source status" aria-live="off" data-state={status}>
    <strong>{status}</strong><span>Kansas Sky</span>
    {Number.isFinite(mapTime)?<time dateTime={new Date(mapTime).toISOString()}>{mode==="live"?"Receiver checked · ":""}{utc(mapTime)}</time>:<small>{mode==="live"?"No receiver timestamp":"No replay observations"}</small>}
  </aside>,mapStatusHost)}<section className="kansas-sky" aria-label="Kansas Sky aircraft and replay" data-projection={flat?"2d":"3d"}>
    <header><div><span className="kansas-sky-eyebrow">Aviation · observed tracks</span><h4>Kansas Sky</h4></div><strong className="kansas-sky-badge">{status}</strong></header>
    <div className="kansas-sky-modes" role="group" aria-label="Flight time mode">{([["live","Live"],["session","Replay this session"],["recorded","Recorded flights"]] as const).map(([id,title])=><button type="button" key={id} aria-pressed={mode===id} onClick={()=>changeMode(id)}>{title}</button>)}</div>
    {mode==="recorded"&&<label>Recorded flight<select aria-label="Recorded flight" value={entry?.id??""} onChange={e=>void loadRecorded(e.target.value)}><option value="">Choose a dated flight</option>{flights.map(f=><option key={f.id} value={f.id}>{f.title}</option>)}</select></label>}
    {mode==="recorded"&&catalogState==="idle"&&<p role="status">Loading the recorded-flight catalog…</p>}
    {mode==="recorded"&&catalogState==="ready"&&!flights.length&&<p>No recorded flights are available yet.</p>}
    {mode==="recorded"&&catalogState==="error"&&<p role="alert">The recorded-flight catalog is unavailable.</p>}
    {mode==="recorded"&&archiveState==="loading"&&<p role="status">Verifying source identity and flight digest…</p>}
    {error&&<p role="alert">{error}</p>}
    <time className="kansas-sky-clock" dateTime={new Date(effectiveCursor).toISOString()}>{utc(effectiveCursor)}</time>
    {mode==="live"&&<small className="kansas-sky-retained">Latest observations; receiver refresh every 20 seconds. {range?`Retained ${utc(range[0])} → ${utc(range[1])}`:"No session observations retained yet."}</small>}
    {flat&&<p className="kansas-sky-context">2D chart: aircraft and trails are flattened to their geographic positions. All reported heights remain available; no MSL slice membership is inferred.</p>}
    {mode!=="live"&&<><div className="kansas-sky-transport"><button type="button" disabled={!range||range[0]===range[1]||archiveState==="loading"&&mode==="recorded"} aria-pressed={playing} onClick={()=>{if(range){if(cursor>=range[1])setCursor(range[0]);else if(cursor<range[0])setCursor(range[0]);}setPlaying(v=>!v);}}>{playing?"Pause":"Play"}</button><label>Speed<select aria-label="Replay speed" value={speed} onChange={e=>setSpeed(Number(e.target.value))}>{[1,4,16].map(v=><option value={v} key={v}>{v}×</option>)}</select></label><button type="button" onClick={()=>changeMode("live")}>Return to live</button></div>
      <label>Flight timeline<input type="range" aria-label="Flight timeline" aria-valuetext={utc(effectiveCursor)} aria-describedby={rangeId} min={range?.[0]??0} max={range?.[1]??1} step={100} value={range?effectiveCursor:0} disabled={!range||range[0]===range[1]} onChange={e=>{setPlaying(false);setCursor(Number(e.target.value));}} /></label>
      <small id={rangeId}>{range?`${utc(range[0])} → ${utc(range[1])}`:"No retained observations in this view."}</small>
      {range&&cursor<range[0]&&<small>Earlier session history expired. Clock, aircraft and timeline now show the earliest retained instant.</small>}
      <p className="kansas-sky-context">Replay aircraft only. Airspace, terrain, weather and restrictions elsewhere on the map are current context, not a reconstruction of this flight’s conditions.</p></>}
    <label>Filter aircraft<input type="search" aria-label="Filter Kansas Sky aircraft" value={aircraftFilter} onChange={event=>setAircraftFilter(event.target.value)} placeholder="Callsign, registration or hex" /></label>
    <small>{matchingOptions.length} matching aircraft; up to 3,000 listed, plus the retained selection. Filtering changes this list only; retained data stays intact.</small>
    <label>Aircraft<select aria-label="Kansas Sky aircraft" value={selected??""} onChange={e=>{setSelected(e.target.value||null);setCamera("free");}}><option value="">Choose an aircraft or click its silhouette</option>{options.map(([hex,title])=><option key={hex} value={hex}>{title} · {hex.toUpperCase()}</option>)}</select></label>
    <div className="kansas-sky-camera" role="group" aria-label="Aircraft camera">{(["free","follow","orbit"] as const).map(view=><button type="button" key={view} aria-pressed={camera===view} disabled={view!=="free"&&(!picked||reduced||flat)} onClick={()=>setCamera(view)}>{view==="free"?"Free map":view==="follow"?"Follow":"Orbit"}</button>)}</div>
    {reduced&&<small>Reduced motion: camera movement is off. Replay advances only when you press Play.</small>}
    {picked?<><h5>{label(picked)} <span>{picked.type??"Aircraft type unavailable"}</span></h5><dl className="kansas-sky-instruments"><div><dt>Pressure altitude</dt><dd>{measure(picked.altBaroFt,"ft")}</dd></div><div><dt>Geometric · WGS84</dt><dd>{measure(picked.altGeomFt,"ft")}</dd></div><div><dt>Ground speed</dt><dd>{measure(picked.groundSpeedKt,"kt")}</dd></div><div><dt>Vertical rate</dt><dd>{measure(picked.verticalRateFpm,"ft/min")}</dd></div><div><dt>Track</dt><dd>{measure(picked.trackDeg,"°")}</dd></div><div><dt>Reported roll</dt><dd>{measure(picked.rollDeg,"°")}</dd></div></dl>{picked.emergency&&<p role="status">Reported emergency: {picked.emergency}{picked.squawk?` · squawk ${picked.squawk}`:""}</p>}<small>Source: {mode==="live"?envelope?.provider.title??"Unavailable":selectedSource??"Unavailable"} · Position: {picked.positionMethod??"method unavailable"} · {picked.interpolated?"between recorded observations":"reported observation"}. {picked.observedAt?`${picked.timestampBasis==="retrieval-estimate"?"Estimated observation time":"Observed"} ${typeof picked.observedAt==="number"?utc(picked.observedAt):picked.observedAt}`:"Observation time unavailable"}</small>{picked.altGeomFt===null&&picked.altBaroFt===null&&<p>Height unknown: the ground-level marker is a locator, not an observed surface position.</p>}</>:<p role="status">{selected?"No observation for this aircraft at the selected time. Gaps are not filled.":mode==="live"?(feedState==="error"?"Live feed unavailable. No stale positions are drawn.":feedState==="ready"?`${aircraft.length} observed aircraft. Select one to inspect or follow.`:"Waiting for aircraft observations…"):"Choose a retained aircraft to inspect its measurements."}</p>}
    {renderError&&<p role="status">{renderError}</p>}
    {snapshot.truncated&&mode!=="recorded"&&<small>Session memory limit reached; older trail detail was discarded.</small>}
    {envelope?.truncated&&mode==="live"&&<small>The receiver response reached a processing bound: this view is truncated, not a complete aircraft census.</small>}
    {!!envelope?.dropped&&mode==="live"&&<small>{envelope.dropped} feed records omitted by validation or regional limits.</small>}
    <p className="kansas-sky-limit">Vertical placement is approximate; pressure altitude and WGS84 height are not MSL. Silhouettes are enlarged; a diamond means heading unavailable. No confirmed airspace occupancy, navigation, owner or mission inference. Pan, zoom or use map keys to release the camera. On the globe, select aircraft from this list.</p>
    <small>{mode==="recorded"&&entry?<>Recorded source: <a href={entry.sourceUrl} target="_blank" rel="noreferrer">{entry.provider}</a> · {entry.license}</>:mode==="session"?<>Session sources: {sourceIds||"No retained source"}. Observation times are retained with each sample.</>:envelope?<>Live source: <a href={envelope.provider.homepage} target="_blank" rel="noreferrer">{envelope.provider.title}</a> · {envelope.provider.terms}</>:"Receiver coverage varies; an empty view does not mean an empty sky."}</small>
  </section></>;
}
