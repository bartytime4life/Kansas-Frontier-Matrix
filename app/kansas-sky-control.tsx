"use client";
import { useCallback, useId, useEffect, useMemo, useRef, useState, useSyncExternalStore, type RefObject } from "react";
import { createPortal } from "react-dom";
import type { Map as MapLibreMap } from "./maplibre-seam";
import { freshAircraft, type Aircraft, type TrafficEnvelope } from "./aviation-traffic";
import { SkyBuffer, animateSkyReplay, animateSkyBuffered, bufferedSkySamples, SKY_LIVE_DELAY_MS, samplesAt, trailSegments, selectedJourney, skyPartNeighbors, nextSkyObservationAfterGap, type SkyPoint } from "./kansas-sky";
import { attachKansasSky, attachKansasSkyFocus } from "./kansas-sky-layer";
import { SkyAircraftBrief, SkyAircraftDossier, SkyAltitudeProfile } from "./kansas-sky-details";
import { leaseProjectionNavigation } from "./globe-context";
import { leaseBorderCurtainSuppression } from "./scene-effects";
import "./kansas-sky.css";

type CatalogFlight = { id:string;title:string;start:string;end:string;url:string;sha256:string;provider:string;license:string;sourceUrl:string;hex?:string;day?:string;pointCount?:number;segmentCount?:number;coverage?:"selected-recordings"|"provider-day-processed";part?:number;partCount?:number };
type ArchiveDay = { day:string;coverage:"selected-recordings"|"provider-day-processed";aircraftCount:number;pointCount:number;indexUrl:string };
type Mode = "live" | "buffered" | "session" | "recorded";
type Camera = "free" | "follow" | "orbit";
const utc=(time:number)=>new Date(time).toISOString().replace("T"," ").replace(/\.\d{3}Z$/," UTC");
const label=(a:Pick<Aircraft,"callsign"|"registration"|"hex">)=>a.callsign??a.registration??a.hex.toUpperCase();
const measure=(n:number|null|undefined,unit:string)=>n===null||n===undefined?"Unavailable":`${Math.round(n).toLocaleString("en-US")} ${unit}`;
const isObject=(v:unknown):v is Record<string,unknown>=>Boolean(v)&&typeof v==="object"&&!Array.isArray(v);
const external=(value:unknown)=>typeof value==="string"&&/^https:\/\/[^\s]+$/.test(value);
const clock=(time:number)=>new Date(time).toISOString().slice(11,19);
const cameraBearing=(current:number,target:number,elapsed:number)=>current+((target-current+540)%360-180)*(1-Math.exp(-Math.max(0,elapsed)/450));
function FlightIcon({kind}:{kind:"play"|"pause"|"path"|"follow"|"orbit"|"restart"|"brief"|"profile"}){
  const shapes={play:"M8 5l10 7-10 7Z",pause:"M8 5v14M16 5v14",path:"M4 18l5-9 6 5 5-10M4 21v-3M9 12v7M15 17v3M20 7v14",follow:"M12 3v4M12 17v4M3 12h4M17 12h4M16 12a4 4 0 1 1-8 0 4 4 0 0 1 8 0",orbit:"M19 5l2 4-4 1M21 9a9 9 0 1 0-1 8M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0",restart:"M5 5v14M18 5l-10 7 10 7Z",brief:"M5 3h10l4 4v14H5ZM9 11h6M9 15h6M9 7h2",profile:"M3 19h18M4 15l4-5 4 3 5-9 3 3"};
  return <svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d={shapes[kind]}/></svg>;
}
// Matches the renderer's approximate height, not an MSL conversion.
const cameraElevation=(map:MapLibreMap,plane:Aircraft)=>plane.onGround||plane.altGeomFt===null&&plane.altBaroFt===null
  ? map.queryTerrainElevation([plane.lon,plane.lat])??0
  : Math.max(0,plane.altGeomFt??plane.altBaroFt??0)*.3048;
const flightPadding=(()=>{const cache=new WeakMap<MapLibreMap,{top:number;bottom:number;left:number;right:number}>();return(map:MapLibreMap,refresh=false)=>{
  const cached=cache.get(map);if(cached&&!refresh)return cached;
  const canvas=map.getCanvas(),narrow=canvas.clientWidth<=760;
  const canvasRect=canvas.getBoundingClientRect?.(),dock=map.getContainer?.().querySelector(".kansas-sky-flight-deck")?.getBoundingClientRect();
  const padding=narrow?{top:95,bottom:Math.max(0,Math.min(canvas.clientHeight-230,dock&&canvasRect?canvasRect.bottom-dock.top+24:Math.min(410,canvas.clientHeight*.55))),left:35,right:35}
    :{top:55,bottom:75,left:55,right:Math.min(canvas.clientWidth-240,dock&&canvasRect?canvasRect.right-dock.left+40:430)};
  cache.set(map,padding);return padding;
};})();
function fitSkyJourney(map:MapLibreMap,points:readonly SkyPoint[],flat:boolean){
  if(!points.length)return;
  const lons=points.map(point=>point.lon),lats=points.map(point=>point.lat);
  // Reserve the dock once. MapLibre cameraForBoxAndBearing adds fitBounds'
  // requested padding to transform.padding; supplying both twice can make the
  // available mobile height negative and leave the old camera unchanged.
  map.setPadding(flightPadding(map,true));map.setCenterElevation(0);
  // Height is approximate; leave room above the ground footprint for the curtain.
  const height=flat?0:Math.max(...points.map(point=>Math.max(0,point.altGeomFt??point.altBaroFt??0)))*.3048;
  const heightMargin=height*1.5/111320;
  const latitudeMargin=heightMargin+(Math.max(...lats)-Math.min(...lats))*.1,longitudeMargin=heightMargin/Math.cos(((Math.max(...lats)+Math.min(...lats))/2)*Math.PI/180)+(Math.max(...lons)-Math.min(...lons))*.1;
  map.fitBounds([[Math.min(...lons)-longitudeMargin,Math.min(...lats)-latitudeMargin],[Math.max(...lons)+longitudeMargin,Math.max(...lats)+latitudeMargin]],{padding:0,pitch:flat?0:55,bearing:0,duration:0,maxZoom:10});
}
async function boundedBytes(url:string,signal:AbortSignal,max:number){
  const response=await fetch(url,{signal,credentials:"same-origin"});if(!response.ok||!response.body)throw new Error("The recorded flight is unavailable.");
  const reader=response.body.getReader(),chunks:Uint8Array[]=[];let size=0;
  try{for(;;){const {done,value}=await reader.read();if(done)break;size+=value.byteLength;if(size>max)throw new Error("The recorded flight exceeds its size bound.");chunks.push(value);}}
  catch(error){await reader.cancel();throw error;}finally{reader.releaseLock();}
  const bytes=new Uint8Array(size);let offset=0;for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.length;}return bytes;
}
function catalog(value:unknown):CatalogFlight[]{
  if(!isObject(value)||value.schemaVersion!==1||!Array.isArray(value.flights)||value.flights.length>10000)throw new Error("The recorded-flight catalog is invalid.");
  const parsed=value.flights.map(v=>{if(!isObject(v)||typeof v.id!=="string"||!/^[a-z0-9-]{1,100}$/.test(v.id)||typeof v.title!=="string"||v.title.length>180||typeof v.url!=="string"||!/^\/data\/aviation\/replays\/(?:days\/\d{4}-\d{2}-\d{2}\/)?[a-z0-9-]+\.json$/.test(v.url)||typeof v.sha256!=="string"||!/^[a-f0-9]{64}$/.test(v.sha256)||typeof v.provider!=="string"||typeof v.license!=="string"||!external(v.sourceUrl)||typeof v.start!=="string"||typeof v.end!=="string"||!Number.isFinite(Date.parse(v.start))||!Number.isFinite(Date.parse(v.end))||Date.parse(v.end)<Date.parse(v.start))throw new Error("The recorded-flight catalog is invalid.");
    if(v.hex!==undefined&&(typeof v.hex!=="string"||!/^~?[a-f0-9]{6}$/.test(v.hex)))throw new Error("Invalid aircraft identity in catalog.");
    for(const key of ["pointCount","segmentCount"])if(v[key]!==undefined&&(!Number.isSafeInteger(v[key])||(v[key] as number)<0))throw new Error("Invalid archive counts.");
    if(v.day!==undefined&&(typeof v.day!=="string"||!/^\d{4}-\d{2}-\d{2}$/.test(v.day)))throw new Error("Invalid archive day.");
    if(v.part!==undefined||v.partCount!==undefined){
      if(!Number.isSafeInteger(v.part)||!Number.isSafeInteger(v.partCount)||(v.part as number)<1||(v.partCount as number)<1||(v.partCount as number)>10000||(v.part as number)>(v.partCount as number)||!v.hex||!v.day)throw new Error("Invalid archive part coverage.");
      if(new Date(Date.parse(v.start)).toISOString().slice(0,10)!==v.day||new Date(Date.parse(v.end)).toISOString().slice(0,10)!==v.day)throw new Error("Archive part crosses its declared UTC day.");
    }
    return v as CatalogFlight;});
  const groups=new Map<string,{count:number;parts:Set<number>}>(),ids=new Set<string>();
  for(const flight of parsed){if(ids.has(flight.id))throw new Error("Duplicate recorded-flight identity.");ids.add(flight.id);if(flight.part===undefined)continue;
    const key=`${flight.provider}:${flight.day}:${flight.hex}`,group=groups.get(key)??{count:flight.partCount!,parts:new Set<number>()};
    if(group.count!==flight.partCount||group.parts.has(flight.part))throw new Error("Archive part coverage is ambiguous.");group.parts.add(flight.part);groups.set(key,group);
  }
  return parsed;
}
function archiveDays(value:unknown):ArchiveDay[]{
  if(!isObject(value)||value.schemaVersion!==1||!Array.isArray(value.days)||value.days.length>3660)throw new Error("Daily archive index is invalid.");
  return value.days.map(day=>{if(!isObject(day)||typeof day.day!=="string"||!/^\d{4}-\d{2}-\d{2}$/.test(day.day)||!["selected-recordings","provider-day-processed"].includes(day.coverage as string)||!Number.isSafeInteger(day.aircraftCount)||(day.aircraftCount as number)<0||!Number.isSafeInteger(day.pointCount)||(day.pointCount as number)<0||typeof day.indexUrl!=="string"||!(day.indexUrl==="/data/aviation/replays/index.json"||day.indexUrl===`/data/aviation/replays/days/${day.day}/index.json`))throw new Error("Daily archive index is invalid.");return day as ArchiveDay;}).sort((a,b)=>b.day.localeCompare(a.day));
}
const flightHex=(flight:CatalogFlight)=>flight.hex??flight.id.match(/(?:^|-)([a-f0-9]{6})(?:-|$)/)?.[1]??null;
function archive(value:unknown,entry:CatalogFlight):ReadonlyMap<string,readonly SkyPoint[]>{
  if(!isObject(value)||value.schemaVersion!==1||value.id!==entry.id||value.provider!==entry.provider||value.license!==entry.license||value.sourceUrl!==entry.sourceUrl||typeof value.sourceSha256!=="string"||!/^[a-f0-9]{64}$/.test(value.sourceSha256)||!Array.isArray(value.points)||value.points.length<1||value.points.length>20000)throw new Error("Recorded-flight identity or provenance does not match.");
  if(entry.pointCount!==undefined&&entry.pointCount!==value.points.length)throw new Error("Recorded-flight observation count does not match.");
  const tracks=new Map<string,SkyPoint[]>();let previous=-Infinity;
  for(const p of value.points){
    if(!isObject(p)||typeof p.hex!=="string"||!/^~?[a-f0-9]{6}$/.test(p.hex)||typeof p.observedAt!=="number"||!Number.isFinite(p.observedAt)||p.observedAt<previous||p.observedAt<Date.parse(entry.start)||p.observedAt>Date.parse(entry.end)||typeof p.lon!=="number"||!Number.isFinite(p.lon)||p.lon< -103.2||p.lon> -93.6||typeof p.lat!=="number"||!Number.isFinite(p.lat)||p.lat<36.2||p.lat>40.9||typeof p.providerId!=="string"||!p.providerId||typeof p.onGround!=="boolean")throw new Error("Recorded-flight samples are invalid.");
    if(entry.hex&&p.hex!==entry.hex)throw new Error("Recorded aircraft does not match the catalog.");
    if(p.breakBefore!==undefined&&typeof p.breakBefore!=="boolean")throw new Error("Recorded-flight break marker is invalid.");
    for(const key of ["altGeomFt","altBaroFt","groundSpeedKt","trackDeg","verticalRateFpm"]){if(p[key]!==null&&(typeof p[key]!=="number"||!Number.isFinite(p[key])))throw new Error("Recorded-flight measurements are invalid.");}
    for(const key of ["rollDeg","indicatedAirSpeedKt","mach","traceFlags"]){if(p[key]!==null&&p[key]!==undefined&&(typeof p[key]!=="number"||!Number.isFinite(p[key])))throw new Error("Recorded-flight measurements are invalid.");}
    if(p.positionQuality!==undefined){if(!isObject(p.positionQuality))throw new Error("Recorded-flight quality is invalid.");for(const v of Object.values(p.positionQuality))if(v!==null&&(typeof v!=="number"||!Number.isFinite(v)))throw new Error("Recorded-flight quality is invalid.");}
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
  const [liveNow,setLiveNow]=useState(()=>Date.now());
  const [cursor,setCursor]=useState(()=>Date.now()),[playing,setPlaying]=useState(false),[speed,setSpeed]=useState(1),[camera,setCamera]=useState<Camera>("free");
  const [reduced,setReduced]=useState(false),[hidden,setHidden]=useState(false),[flights,setFlights]=useState<CatalogFlight[]>([]),[catalogState,setCatalogState]=useState("idle");
  const [recorded,setRecorded]=useState<ReadonlyMap<string,readonly SkyPoint[]>>(new Map()),[entry,setEntry]=useState<CatalogFlight|null>(null),[archiveState,setArchiveState]=useState("idle"),[error,setError]=useState("");
  const [renderError,setRenderError]=useState("");
  const [flightView,setFlightView]=useState(false),[frameRequest,setFrameRequest]=useState(0),[overview,setOverview]=useState(false);
  const [aircraftFilter,setAircraftFilter]=useState(""),[recordingFilter,setRecordingFilter]=useState("");
  const [flightExtra,setFlightExtra]=useState<"profile"|"brief"|null>(null),[focusFlight,setFocusFlight]=useState(true);
  const [showPaths,setShowPaths]=useState(true),[showGuides,setShowGuides]=useState(true),[historyOpen,setHistoryOpen]=useState(false);
  const dayIndexLoaded=useRef(false),catalogCache=useRef(new Map<string,CatalogFlight[]>());
  const [days,setDays]=useState<ArchiveDay[]>([]),[day,setDay]=useState(""),[dayState,setDayState]=useState("idle");
  const [renderMetrics,setRenderMetrics]=useState({aircraft:0,trailVertices:0,heightGuides:0,terrainQueries:0});
  const motionCursor=useRef(cursor),motionState=useRef({tracks:new Map<string,readonly SkyPoint[]>() as ReadonlyMap<string,readonly SkyPoint[]>,envelope:null as (TrafficEnvelope&{receivedAt:number})|null,feedState,selected:null as string|null,camera:"free" as Camera,flat,reduced,enabled,hidden});
  const rangeId=useId(),flightExtraId=useId(), ownCameraMove=useRef(false), latestPicked=useRef<Aircraft|undefined>(undefined);
  const framedRequest=useRef(-1),cameraLeaseActive=flightView||camera!=="free";
  const layer=useRef<ReturnType<typeof attachKansasSky>|null>(null),request=useRef<AbortController|null>(null),catalogRequest=useRef<AbortController|null>(null);
  useEffect(()=>{const media=matchMedia("(prefers-reduced-motion: reduce)");const update=()=>{setReduced(media.matches);if(media.matches){setCamera("free");setPlaying(false);}};update();media.addEventListener("change",update);const visibility=()=>{setHidden(document.hidden);if(document.hidden){setPlaying(false);setCamera("free");setFlightView(false);}};visibility();document.addEventListener("visibilitychange",visibility);return()=>{media.removeEventListener("change",update);document.removeEventListener("visibilitychange",visibility);};},[]);
  useEffect(()=>{if(envelope&&enabled)store.ingest(envelope);},[envelope,enabled,store]);
  useEffect(()=>{store.select(selected);},[selected,store]);
  const [wasEnabled,setWasEnabled]=useState(enabled);
  if(wasEnabled!==enabled){setWasEnabled(enabled);if(!enabled){setPlaying(false);setCamera("free");setFlightView(false);}}
  if(flat&&flightView){setFlightView(false);setCamera("free");}
  useEffect(()=>{if(!enabled)request.current?.abort();},[enabled]);
  useEffect(()=>()=>{request.current?.abort();catalogRequest.current?.abort();},[]);
  useEffect(()=>{onReplayMode?.(enabled&&mode!=="live");return()=>onReplayMode?.(false);},[mode,enabled,onReplayMode]);
  const replaying=mode==="session"||mode==="recorded",currentFeed=mode==="live"||mode==="buffered";
  const tracks=mode==="recorded"?recorded:snapshot.tracks;
  const range=useMemo(()=>{let start=Infinity,end=-Infinity;for(const points of tracks.values()){if(points.length){start=Math.min(start,points[0].observedAt);end=Math.max(end,points[points.length-1].observedAt);}}return Number.isFinite(start)?[start,end] as const:null;},[tracks]);
  const effectiveCursor=currentFeed||!range?cursor:Math.max(range[0],Math.min(range[1],cursor));
  useEffect(()=>{if(!enabled||hidden)return;const tick=()=>{const now=Date.now();setLiveNow(now);if(mode==="live")setCursor(now);};const timer=setInterval(tick,1000);return()=>clearInterval(timer);},[enabled,hidden,mode]);
  useEffect(()=>{if(!playing)motionCursor.current=effectiveCursor;},[effectiveCursor,playing]);
  useEffect(()=>{motionState.current={tracks,envelope,feedState,selected,camera,flat,reduced,enabled,hidden};},[tracks,envelope,feedState,selected,camera,flat,reduced,enabled,hidden]);
  useEffect(()=>{const map=mapRef.current;if(!map||!enabled)return;
    // Layout changes refresh this cache; follow/orbit frames only read it.
    const refresh=()=>flightPadding(map,true);refresh();map.on("resize",refresh);
    const observer=typeof ResizeObserver!=="undefined"?new ResizeObserver(refresh):null;
    observer?.observe(map.getCanvas());const dock=map.getContainer().querySelector(".kansas-sky-flight-deck");if(dock)observer?.observe(dock);
    return()=>{map.off("resize",refresh);observer?.disconnect();};
  },[mapRef,enabled,styleReady,flightView,flightExtra,mapStatusHost]);
  useEffect(()=>{
    if(!enabled||hidden||!replaying||!playing||!range||range[0]===range[1])return;
    let previous=performance.now();
    return animateSkyReplay({start:motionCursor.current,range,speed,reduced,requestFrame:callback=>requestAnimationFrame(callback),cancelFrame:id=>cancelAnimationFrame(id),now:()=>performance.now(),
      render:at=>{motionCursor.current=at;const state=motionState.current;if(!state.enabled||state.hidden||document.hidden)return;
        const next=samplesAt(state.tracks,at);layer.current?.updateAircraft(next);
        const plane=next.find(a=>a.hex===state.selected);latestPicked.current=plane;
        const now=performance.now(),elapsed=Math.min(100,now-previous);previous=now;
        const map=mapRef.current;if(map&&plane&&!state.reduced&&!state.flat&&state.camera!=="free"){
          ownCameraMove.current=true;try{map.jumpTo({center:[plane.lon,plane.lat],pitch:60,bearing:state.camera==="orbit"?map.getBearing()+elapsed*.006:cameraBearing(map.getBearing(),plane.trackDeg??map.getBearing(),elapsed),elevation:cameraElevation(map,plane),padding:flightPadding(map)});}finally{ownCameraMove.current=false;}
        }
      },readout:setCursor,ended:()=>setPlaying(false)});
  },[enabled,hidden,replaying,playing,range,speed,reduced,mapRef]);
  useEffect(()=>{
    if(!enabled||hidden||mode!=="buffered"||reduced)return;
    let previous=performance.now();
    return animateSkyBuffered({requestFrame:callback=>requestAnimationFrame(callback),cancelFrame:id=>cancelAnimationFrame(id),now:()=>performance.now(),wallTime:Date.now,
      render:at=>{const state=motionState.current;if(!state.enabled||state.hidden||state.reduced||document.hidden)return;
        const eligible=new Set(state.feedState==="ready"?freshAircraft(state.envelope,Date.now()).map(plane=>plane.hex):[]),next=bufferedSkySamples(state.tracks,at,eligible);
        layer.current?.updateAircraft(next);const plane=next.find(a=>a.hex===state.selected);latestPicked.current=plane;
        const now=performance.now(),elapsed=Math.min(100,now-previous);previous=now;const map=mapRef.current;
        if(map&&plane&&!state.flat&&state.camera!=="free"){ownCameraMove.current=true;try{map.jumpTo({center:[plane.lon,plane.lat],pitch:60,bearing:state.camera==="orbit"?map.getBearing()+elapsed*.006:cameraBearing(map.getBearing(),plane.trackDeg??map.getBearing(),elapsed),elevation:cameraElevation(map,plane),padding:flightPadding(map)});}finally{ownCameraMove.current=false;}}
      },readout:setCursor});
  },[enabled,hidden,mode,reduced,mapRef]);
  const aircraft=useMemo(()=>mode==="live"?freshAircraft(envelope,effectiveCursor):mode==="buffered"?reduced||feedState!=="ready"?[]:bufferedSkySamples(tracks,effectiveCursor,new Set(freshAircraft(envelope,liveNow).map(plane=>plane.hex))):samplesAt(tracks,effectiveCursor),[mode,envelope,tracks,effectiveCursor,liveNow,reduced,feedState]);
  const trails=useMemo(()=>{
    if(mode!=="recorded"||!selected)return trailSegments(tracks,effectiveCursor,selected?3600000:600000);
    const others=new Map([...tracks].filter(([hex])=>hex!==selected));
    return [...selectedJourney(tracks.get(selected)??[],effectiveCursor),...trailSegments(others,effectiveCursor)];
  },[tracks,effectiveCursor,selected,mode]);
  const feedAge=envelope?liveNow-Date.parse(envelope.retrievedAt):Number.NaN;
  const liveFresh=feedState==="ready"&&Number.isFinite(feedAge)&&feedAge>=-30000&&feedAge<=60000;
  const picked=aircraft.find(a=>a.hex===selected);
  useEffect(()=>{if(!playing&&mode!=="buffered")latestPicked.current=picked;},[picked,playing,mode]);
  const selectedSource=useMemo(()=>{const points=selected?tracks.get(selected):undefined;return points?.findLast(point=>point.observedAt<=effectiveCursor)?.providerId??null;},[tracks,selected,effectiveCursor]);
  const sourceIds=useMemo(()=>[...new Set([...tracks.values()].flatMap(points=>points.map(point=>point.providerId)))].join(", "),[tracks]);
  useEffect(()=>{const map=mapRef.current;if(!map||!styleReady||!enabled||hidden)return;try{layer.current=attachKansasSky(map,hex=>{setSelected(hex);setCamera("free");inspectCallback.current?.();},setRenderError);}catch{queueMicrotask(()=>setRenderError("Aircraft renderer unavailable; use the aircraft list."));}return()=>{layer.current?.dispose();layer.current=null;};},[mapRef,styleReady,enabled,hidden]);
  useEffect(()=>{layer.current?.update(aircraft,trails,selected,flat,showPaths,showGuides);},[aircraft,trails,selected,enabled,hidden,styleReady,flat,showPaths,showGuides]);
  useEffect(()=>{if(!enabled||hidden)return;const timer=setInterval(()=>{const metrics=layer.current?.metrics();if(metrics)setRenderMetrics(metrics);},1000);return()=>clearInterval(timer);},[enabled,hidden]);
  useEffect(()=>{
    const map=mapRef.current;if(!map||!enabled)return;
    let active=true,resizeVersion=0;
    const release=()=>{setCamera("free");setOverview(false);};
    // MapLibre resize emits movestart even when only the Layers panel closed.
    // A resize in this synchronous event batch is not camera navigation.
    const resize=()=>{resizeVersion++;};
    const move=()=>{if(ownCameraMove.current)return;const version=resizeVersion;queueMicrotask(()=>{if(active&&version===resizeVersion)release();});};
    map.on("movestart",move);map.on("resize",resize);
    const canvas=map.getCanvas();canvas.addEventListener("pointerdown",release);canvas.addEventListener("wheel",release,{passive:true});canvas.addEventListener("keydown",release);
    return()=>{active=false;map.off("movestart",move);map.off("resize",resize);canvas.removeEventListener("pointerdown",release);canvas.removeEventListener("wheel",release);canvas.removeEventListener("keydown",release);};
    // The control can mount before mapRef.current exists. Its stable ref object
    // alone cannot notify this effect when the parent finishes map creation.
  },[mapRef,enabled,styleReady]);
  // This camera follows the same approximate display height as the aircraft layer.
  // Restore map ownership on manual movement, hide, disable or unmount.
  useEffect(()=>{
    const map=mapRef.current;
    if(!map||!enabled||hidden||flat||!cameraLeaseActive)return;
    const clamped=map.getCenterClampedToGround(),elevation=map.getCenterElevation(),padding=map.getPadding();
    ownCameraMove.current=true;let releaseNavigation:()=>void;try{releaseNavigation=leaseProjectionNavigation(map);map.setCenterClampedToGround(false);}finally{ownCameraMove.current=false;}
    const reserve=()=>{ownCameraMove.current=true;try{map.setPadding(flightPadding(map,true));}finally{ownCameraMove.current=false;}};
    reserve();map.on("resize",reserve);
    return()=>{map.off("resize",reserve);ownCameraMove.current=true;try{map.setCenterClampedToGround(clamped);map.setCenterElevation(elevation);map.setPadding(padding);releaseNavigation();}finally{ownCameraMove.current=false;}};
  },[mapRef,enabled,hidden,flat,cameraLeaseActive]);
  useEffect(()=>{const map=mapRef.current,plane=latestPicked.current;
    if(!map||!enabled||hidden||flat||!flightView||frameRequest===framedRequest.current)return;
    framedRequest.current=frameRequest;if(!plane||overview)return;
    // Explicit entry is allowed with reduced motion: a single static framing.
    // Manual gestures do not issue a new framing request or release/reacquire the lease.
    ownCameraMove.current=true;try{map.jumpTo({center:[plane.lon,plane.lat],zoom:9.7,pitch:60,bearing:map.getBearing(),elevation:cameraElevation(map,plane),padding:flightPadding(map)});}finally{ownCameraMove.current=false;}
  },[mapRef,enabled,hidden,flat,flightView,frameRequest,overview]);
  useEffect(()=>{const map=mapRef.current;if(!map||!enabled||hidden||!flightView||!focusFlight)return;const restoreCurtain=leaseBorderCurtainSuppression(map),restorePaint=attachKansasSkyFocus(map);return()=>{restorePaint();restoreCurtain();};},[mapRef,enabled,hidden,flightView,focusFlight,styleReady]);
  const openFlightView=()=>{
    if(!mapRef.current||!picked||flat)return;
    setFlightExtra(null);setOverview(false);setFlightView(true);setFrameRequest(value=>value+1);setCamera(reduced?"free":"follow");
  };
  useEffect(()=>{const map=mapRef.current;if(!map||!picked||camera!=="follow"||reduced||flat||hidden||!enabled||playing||mode==="buffered")return;ownCameraMove.current=true;try{map.jumpTo({center:[picked.lon,picked.lat],pitch:60,bearing:picked.trackDeg??map.getBearing(),elevation:cameraElevation(map,picked),padding:flightPadding(map)});}finally{ownCameraMove.current=false;}},[mapRef,picked,camera,reduced,flat,hidden,enabled,playing,mode]);
  useEffect(()=>{const map=mapRef.current;if(!map||camera!=="orbit"||reduced||flat||hidden||!enabled||playing||mode==="buffered")return;
    let active=true,frame=0,last=performance.now();const orbit=(now:number)=>{if(!active)return;const elapsed=Math.min(100,now-last);last=now;const plane=latestPicked.current;if(plane&&!document.hidden){ownCameraMove.current=true;try{map.jumpTo({center:[plane.lon,plane.lat],pitch:60,bearing:map.getBearing()+elapsed*.006,elevation:cameraElevation(map,plane),padding:flightPadding(map)});}finally{ownCameraMove.current=false;}}frame=requestAnimationFrame(orbit);};frame=requestAnimationFrame(orbit);return()=>{active=false;cancelAnimationFrame(frame);};
  },[mapRef,camera,reduced,flat,hidden,enabled,playing,mode]);
  useEffect(()=>{if(!enabled||mode!=="recorded"&&!historyOpen)return;const abort=new AbortController();catalogRequest.current=abort;queueMicrotask(()=>{if(!abort.signal.aborted)setCatalogState("loading");});
    const url=day?`/data/aviation/replays/days/${day}/index.json`:"/data/aviation/replays/index.json";
    const selectedDay=days.find(item=>item.day===day);
    const address=selectedDay?.indexUrl??url,cached=catalogCache.current.get(address);
    if(cached){queueMicrotask(()=>{if(!abort.signal.aborted){setFlights(cached);setCatalogState("ready");}});return()=>abort.abort();}
    boundedBytes(address,abort.signal,4*1024*1024).then(bytes=>{if(!abort.signal.aborted){const parsed=catalog(JSON.parse(new TextDecoder().decode(bytes)));if(catalogCache.current.size>=2)catalogCache.current.delete(catalogCache.current.keys().next().value!);catalogCache.current.set(address,parsed);setFlights(parsed);setCatalogState("ready");}}).catch(()=>{if(!abort.signal.aborted){setFlights([]);setCatalogState("error");}});return()=>abort.abort();
  },[enabled,mode,historyOpen,day,days]);
  useEffect(()=>{if(!enabled||mode!=="recorded"&&!historyOpen||dayIndexLoaded.current)return;const abort=new AbortController();queueMicrotask(()=>{if(!abort.signal.aborted)setDayState("loading");});boundedBytes("/data/aviation/replays/archive-index.json",abort.signal,1024*1024).then(bytes=>{if(!abort.signal.aborted){const parsed=archiveDays(JSON.parse(new TextDecoder().decode(bytes)));dayIndexLoaded.current=true;setDays(parsed);setDay(parsed[0]?.day??"");setDayState("ready");}}).catch(()=>{if(!abort.signal.aborted)setDayState("unavailable");});return()=>abort.abort();},[enabled,mode,historyOpen]);
  const changeMode=useCallback((next:Mode)=>{request.current?.abort();if(archiveState==="loading"){setArchiveState("idle");setEntry(null);}setMode(next);setPlaying(false);setCamera("free");setFlightView(false);setError("");if(next==="live")setCursor(Date.now());else if(next==="buffered"){setCursor(Date.now()-SKY_LIVE_DELAY_MS);setLiveNow(Date.now());}else if(next==="session"){const span=store.buffer.range();if(span)setCursor(span[0]);}else if(entry)setCursor(Date.parse(entry.start));},[archiveState,store,entry]);
  const loadRecorded=async(id:string,keepView=false)=>{request.current?.abort();const flight=flights.find(f=>f.id===id);setMode("recorded");setFlightView(keepView);setRecorded(new Map());setEntry(flight??null);setPlaying(false);setCamera("free");setError("");if(!flight){setArchiveState("idle");return;}const abort=new AbortController();request.current=abort;setArchiveState("loading");try{const bytes=await boundedBytes(flight.url,abort.signal,4*1024*1024);const digest=Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",bytes)),b=>b.toString(16).padStart(2,"0")).join("");if(digest!==flight.sha256)throw new Error("Recorded-flight digest does not match.");const parsed=archive(JSON.parse(new TextDecoder().decode(bytes)),flight);if(abort.signal.aborted||request.current!==abort)return;setRecorded(parsed);setSelected(parsed.keys().next().value??null);setCursor(Date.parse(flight.start));setArchiveState("ready");}catch(e){if(!abort.signal.aborted){setArchiveState("error");setError(e instanceof Error?e.message:"Recorded flight unavailable.");}}};
  const catalogOptions=useMemo(()=>[...tracks].flatMap(([hex,points])=>points.length?[[hex,label(points[points.length-1])] as const]:[]).sort((a,b)=>a[1].localeCompare(b[1])),[tracks]);
  const liveOptions=useMemo(()=>aircraft.map(a=>[a.hex,label(a)] as const).sort((a,b)=>a[1].localeCompare(b[1])),[aircraft]);
  const matchingOptions=useMemo(()=>{const query=aircraftFilter.trim().toLowerCase();return(currentFeed?liveOptions:catalogOptions).filter(([hex,title])=>!query||`${hex} ${title}`.toLowerCase().includes(query));},[aircraftFilter,currentFeed,liveOptions,catalogOptions]);
  const options=matchingOptions.slice(0,3000);
  if(selected&&!options.some(([hex])=>hex===selected)){const retained=catalogOptions.find(([hex])=>hex===selected);if(retained){if(options.length===3000)options.pop();options.push(retained);}}

  const selectedPoints=useMemo(()=>selected?tracks.get(selected)??[]:[],[selected,tracks]);
  useEffect(()=>{
    const map=mapRef.current;if(!map||!enabled||hidden||!flightView||!overview||!selectedPoints.length)return;
    let active=true,frame=0;
    const fit=()=>{cancelAnimationFrame(frame);frame=requestAnimationFrame(()=>{if(!active)return;ownCameraMove.current=true;try{fitSkyJourney(map,selectedPoints,flat);}finally{ownCameraMove.current=false;}});};
    fit();map.on("resize",fit);
    const dock=map.getContainer().querySelector(".kansas-sky-flight-deck"),observer=typeof ResizeObserver!=="undefined"?new ResizeObserver(fit):null;if(dock)observer?.observe(dock);
    return()=>{active=false;cancelAnimationFrame(frame);map.off("resize",fit);observer?.disconnect();};
  },[mapRef,enabled,hidden,flightView,overview,selectedPoints,flat,frameRequest]);
  const retainedDetail=useMemo(()=>{const point=selectedPoints.findLast(p=>p.observedAt<=effectiveCursor)??selectedPoints[0];return point?{...point,observedAt:new Date(point.observedAt).toISOString(),interpolated:false}:undefined;},[selectedPoints,effectiveCursor]);
  const detailAircraft=picked??retainedDetail;
  const nextObservedSegment=replaying?nextSkyObservationAfterGap(selectedPoints,effectiveCursor):null;
  const filteredFlights=useMemo(()=>{const query=recordingFilter.trim().toLowerCase();return flights.filter(f=>!query||`${f.title} ${flightHex(f)??""}`.toLowerCase().includes(query));},[flights,recordingFilter]);
  const historyFlights=useMemo(()=>selected?filteredFlights.filter(f=>flightHex(f)===selected):filteredFlights,[filteredFlights,selected]);
  const listedFlights=filteredFlights.slice(0,200);if(entry&&!listedFlights.some(f=>f.id===entry.id))listedFlights.unshift(entry);
  const seek=(at:number)=>{setPlaying(false);setCursor(at);};
  const overviewJourney=()=>{
    const map=mapRef.current;if(!map||!selectedPoints.length)return;
    setCamera("free");setOverview(true);setFlightView(true);setFrameRequest(value=>value+1);
  };
  const replayJourney=()=>{if(!range||range[0]===range[1])return;motionCursor.current=range[0];latestPicked.current=samplesAt(tracks,range[0]).find(plane=>plane.hex===selected);setCursor(range[0]);setOverview(false);setFlightView(true);setFrameRequest(value=>value+1);setCamera(reduced||flat?"free":"follow");setPlaying(true);};
  const archiveDay=days.find(item=>item.day===day);
  const parts=useMemo(()=>skyPartNeighbors(flights,mode==="recorded"?entry:null),[flights,entry,mode]);
  const status=mode==="buffered"?(reduced?"PAUSED":liveFresh?"DELAYED VIEW":"WAITING"):replaying?"REPLAY":liveFresh?"LIVE FEED":feedState==="error"?"UNAVAILABLE":envelope?"STALE":"WAITING";
  const receiverTime=envelope?Date.parse(envelope.retrievedAt):Number.NaN;
  const mapTime=mode==="buffered"?effectiveCursor:replaying?(range?effectiveCursor:Number.NaN):receiverTime;
  const partControls=parts.multipart&&entry&&<div className="kansas-sky-parts" aria-label="Recorded flight parts"><small><strong>{archiveState==="ready"?"Loaded":"Selected"} part {entry.part} of {entry.partCount}</strong> · {entry.hex?.toUpperCase()} · {entry.day} UTC. Overview and profile show this file only.</small><div><button type="button" disabled={!parts.previous||archiveState==="loading"} onClick={()=>parts.previous&&void loadRecorded(parts.previous.id,flightView)}>Previous part</button><button type="button" disabled={!parts.next||archiveState==="loading"} onClick={()=>parts.next&&void loadRecorded(parts.next.id,flightView)}>Next part</button></div><small>{parts.available} of {parts.expected} parts listed. Each selection verifies one file and pauses at its first observation; gaps between files are not animated.{parts.available<parts.expected?" Some declared parts are absent from this catalog.":""}</small></div>;
  if(!enabled)return null;
  return <>{mapStatusHost&&createPortal(<aside className="kansas-sky-map-status" aria-label="Kansas Sky map time and source status" aria-live="off" data-state={status} data-flight-view={flightView}>
    <strong>{status}</strong><span>Kansas Sky</span>{mode==="buffered"&&envelope&&<small>Receiver checked · {utc(receiverTime)}</small>}
    {Number.isFinite(mapTime)?<time dateTime={new Date(mapTime).toISOString()}>{mode==="buffered"?(reduced?"Displayed · paused · ":"Displayed · 30 s delay · "):mode==="live"?"Receiver checked · ":""}{utc(mapTime)}</time>:<small>{currentFeed?"No receiver timestamp":"No replay observations"}</small>}
  </aside>,mapStatusHost)}{mapStatusHost&&flightView&&createPortal(<section className="kansas-sky-flight-deck" data-extra={flightExtra??"none"} aria-label="Flight view controls" onPointerDown={event=>event.stopPropagation()} onClick={event=>event.stopPropagation()} onDoubleClick={event=>event.stopPropagation()} onWheel={event=>event.stopPropagation()} onKeyDown={event=>event.stopPropagation()}>
    <header><div><small>{mode==="buffered"?"SMOOTH LIVE · 30 S DELAY":mode==="live"?"OBSERVED AIRCRAFT":"KANSAS SKY / RECORDED JOURNEY"}</small><strong>{detailAircraft?label(detailAircraft):"Select an aircraft"}<span>{detailAircraft?.type??"Type unavailable"}</span></strong><span className="sky-flight-source">{mode==="recorded"?`${entry?.day??entry?.start.slice(0,10)??""} · ${entry?.provider??"Source unavailable"} · REPLAY`:mode==="session"?"Session observations · REPLAY":envelope?.provider.title??"Source unavailable"}</span>{!picked&&<small className="sky-flight-gap">Observation gap · no position drawn</small>}</div><button type="button" className="sky-flight-close" aria-label="Close flight view" onClick={()=>{setFlightView(false);setCamera("free");}}>×</button></header>
    <div className="kansas-sky-flight-readout"><span>{measure(picked?.altGeomFt??picked?.altBaroFt,"ft")}<small>{picked?.altGeomFt!=null?"WGS84 · approximate":"Pressure · approximate"}</small></span><span>{measure(picked?.groundSpeedKt,"kt")}<small>{picked?.interpolated?"Interpolated speed":"Reported ground speed"}</small></span></div>
    {replaying&&range&&<label className="sky-dock-timeline"><span>JOURNEY TIME</span><time dateTime={new Date(effectiveCursor).toISOString()}>{clock(effectiveCursor)} <small>UTC</small></time><input type="range" aria-label="Flight view timeline" min={range[0]} max={range[1]} step={100} value={effectiveCursor} aria-valuetext={utc(effectiveCursor)} onChange={event=>{setPlaying(false);setCursor(Number(event.target.value));}}/><span className="sky-timeline-ends"><span>{clock(range[0])}</span><span>{clock(range[1])}</span></span></label>}
    {replaying&&<div className="kansas-sky-flight-actions"><button type="button" className="sky-restart" aria-label={parts.multipart?"Fly this part from start":"Fly from start"} title="Fly from the first retained observation" disabled={!range||range[0]===range[1]} onClick={replayJourney}><FlightIcon kind="restart"/></button><button type="button" className="sky-play" disabled={!range||range[0]===range[1]} aria-pressed={playing} onClick={()=>{if(range&&cursor>=range[1]){motionCursor.current=range[0];setCursor(range[0]);}setPlaying(value=>!value);}}><FlightIcon kind={playing?"pause":"play"}/>{playing?"Pause flight":"Play flight"}</button><label className="sky-speed"><span className="sr-only">Flight view playback speed</span><select aria-label="Flight view playback speed" value={speed} onChange={event=>setSpeed(Number(event.target.value))}>{[1,4,16].map(value=><option key={value} value={value}>{value}×</option>)}</select></label></div>}
    {nextObservedSegment!==null&&<button type="button" className="sky-gap-jump" onClick={()=>{motionCursor.current=nextObservedSegment;latestPicked.current=samplesAt(tracks,nextObservedSegment).find(plane=>plane.hex===selected);seek(nextObservedSegment);}}>Next observed segment · {clock(nextObservedSegment)} UTC →</button>}
    <div className="sky-camera-choices" role="group" aria-label="Flight view camera">{replaying&&<button type="button" disabled={!selectedPoints.length} aria-pressed={overview} onClick={overviewJourney}><FlightIcon kind="path"/>{parts.multipart?"This part":"Whole path"}</button>}<button type="button" disabled={!picked||reduced||flat} aria-pressed={camera==="follow"} onClick={()=>{setOverview(false);setCamera("follow");setFrameRequest(value=>value+1);}}><FlightIcon kind="follow"/>Follow</button><button type="button" disabled={!picked||reduced||flat} aria-pressed={camera==="orbit"} onClick={()=>{setOverview(false);setCamera(camera==="orbit"?"free":"orbit");}}><FlightIcon kind="orbit"/>Orbit</button></div>
    {archiveState==="loading"&&mode==="recorded"&&<small role="status">Verifying the selected part…</small>}{error&&mode==="recorded"&&<small role="alert">{error}</small>}
    <div className="kansas-sky-flight-menu"><button type="button" disabled={!detailAircraft} aria-expanded={flightExtra==="brief"} aria-controls={flightExtraId} onClick={()=>setFlightExtra(value=>value==="brief"?null:"brief")}><FlightIcon kind="brief"/>Aircraft brief<span aria-hidden="true">{flightExtra==="brief"?"−":"+"}</span></button><button type="button" aria-expanded={flightExtra==="profile"} aria-controls={flightExtraId} onClick={()=>setFlightExtra(value=>value==="profile"?null:"profile")}><FlightIcon kind="profile"/>Profile & view<span aria-hidden="true">{flightExtra==="profile"?"−":"+"}</span></button></div>
    <div className="sky-flight-focus"><label><input type="checkbox" checked={focusFlight} onChange={event=>setFocusFlight(event.target.checked)}/> Focus on flight</label><span>{camera==="free"&&!overview?"Free explore · resume Follow":focusFlight?"Chart subdued · restrictions retained":"Full map context"}</span></div>
    {mode==="recorded"&&parts.multipart&&<small className="sky-flight-part-badge">Part {entry?.part}/{entry?.partCount} · this file only</small>}
    <div className="sky-flight-legend" aria-label="Flight path legend"><span className="sky-legend-past">Elapsed route</span>{mode==="recorded"&&<span className="sky-legend-ahead">Recorded ahead</span>}<span className="sky-legend-ground">Terrain guides</span></div>
    {flightExtra&&<div className="sky-flight-expanded" id={flightExtraId}>
      {flightExtra==="profile"?<>{partControls}{replaying&&<button type="button" className="sky-fly-start" disabled={!range||range[0]===range[1]} onClick={replayJourney}>{parts.multipart?"Fly this part from start":"Fly from start"}</button>}{selectedPoints.length>0&&<SkyAltitudeProfile points={selectedPoints} cursor={effectiveCursor} canSeek={replaying} onSeek={seek} compact showRange={false}/>}
        <div className="kansas-sky-guide-toggles"><label><input type="checkbox" checked={showPaths} onChange={event=>setShowPaths(event.target.checked)}/> Flight paths</label><label><input type="checkbox" checked={showGuides} disabled={flat||!showPaths} onChange={event=>setShowGuides(event.target.checked)}/> Height guides</label></div>
        <small>Enlarged aircraft symbol · height approximate. {replaying?"Replay aircraft over current map context. Recorded-ahead paths are observations, not predictions.":mode==="buffered"?"Only bracketed observations are animated, 30 seconds behind now.":"Positions stop at the last observation."}</small></>:
        detailAircraft&&<><SkyAircraftBrief aircraft={detailAircraft} observationCount={selectedPoints.length} gap={!picked}/><SkyAircraftDossier aircraft={detailAircraft} source={currentFeed?envelope?.provider.title??"Unavailable":selectedSource??"Unavailable"}/>{entry&&<p className="sky-brief-provenance"><a href={entry.sourceUrl} target="_blank" rel="noreferrer">Original flight source ↗</a><span>{entry.license} · {archiveState==="ready"?"File SHA-256 verified":"File verification pending"}</span></p>}</>}
    </div>}
  </section>,mapStatusHost)}<section className="kansas-sky" aria-label="Kansas Sky aircraft and replay" data-projection={flat?"2d":"3d"}>
    <header><div><span className="kansas-sky-eyebrow">Aviation · observed tracks</span><h4>Kansas Sky</h4></div><strong className="kansas-sky-badge">{status}</strong></header>
    <div className="kansas-sky-modes" role="group" aria-label="Flight time mode">{([["live","Live"],["session","Replay this session"],["recorded","Recorded flights"],["buffered","Smooth live · 30 s delay"]] as const).map(([id,title])=><button type="button" key={id} aria-pressed={mode===id} disabled={id==="buffered"&&reduced} onClick={()=>changeMode(id)}>{title}</button>)}</div>
    {mode==="recorded"&&<div className="sky-recording-intro"><strong>A journey through Kansas</strong><p>Choose an aircraft. Trace its retained route, explore its height, or follow it through the sky.</p><small>{archiveDay?`${archiveDay.day} UTC · ${archiveDay.aircraftCount.toLocaleString()} aircraft · ${archiveDay.coverage==="selected-recordings"?"Selected recordings only":"Provider day processed; coverage limits remain"}`:"Prepared source observations · gaps remain visible"}</small></div>}
    {mode==="recorded"&&days.length>0&&<label>Recording day<select aria-label="Recording day" value={day} onChange={event=>setDay(event.target.value)}><option value="">Original prepared recordings</option>{days.map(item=><option key={item.day} value={item.day}>{item.day} · {item.aircraftCount} aircraft</option>)}</select></label>}
    {mode==="recorded"&&<label>Find a prepared flight<input type="search" aria-label="Find a prepared flight" value={recordingFilter} onChange={event=>setRecordingFilter(event.target.value)} placeholder="Callsign, hex or date"/></label>}{mode==="recorded"&&<label>Recorded flight<select aria-label="Recorded flight" value={entry?.id??""} onChange={e=>void loadRecorded(e.target.value)}><option value="">Choose a dated flight</option>{listedFlights.map(f=><option key={f.id} value={f.id}>{f.title}</option>)}</select></label>}
    {mode==="recorded"&&partControls}
    {mode==="recorded"&&filteredFlights.length>200&&<small>Showing 200 of {filteredFlights.length.toLocaleString()} matching prepared paths. Search to narrow the list.</small>}
    {mode==="recorded"&&(catalogState==="idle"||catalogState==="loading")&&<p role="status">Loading the recorded-flight catalog…</p>}
    {mode==="recorded"&&catalogState==="ready"&&!flights.length&&<p>No recorded flights are available yet.</p>}
    {mode==="recorded"&&catalogState==="error"&&<p role="alert">The recorded-flight catalog is unavailable.</p>}
    {mode==="recorded"&&archiveState==="loading"&&<p role="status">Verifying source identity and flight digest…</p>}
    {mode==="recorded"&&archiveState==="ready"&&entry&&<div className="sky-recording-selection"><strong>{detailAircraft?label(detailAircraft):entry.title}</strong><small>{selectedPoints.length.toLocaleString()} retained observations · {parts.multipart?`Part ${entry.part} of ${entry.partCount}`:"This recorded file"}</small><small>{clock(Date.parse(entry.start))} → {clock(Date.parse(entry.end))} UTC · {entry.provider}</small><button type="button" onClick={overviewJourney} disabled={!selectedPoints.length}>{parts.multipart?"Open this journey part":"Open retained journey"} ↗</button></div>}
    {error&&<p role="alert">{error}</p>}
    <time className="kansas-sky-clock" dateTime={new Date(effectiveCursor).toISOString()}>{utc(effectiveCursor)}</time>
    {mode==="live"&&<small className="kansas-sky-retained">Latest observations; receiver refresh every 20 seconds. {range?`Retained ${utc(range[0])} → ${utc(range[1])}`:"No session observations retained yet."}</small>}
    {mode==="buffered"&&<p className="kansas-sky-context">{reduced?"Smooth live is paused for reduced motion. Choose Latest observations for current reports.":"One shared clock, 30 seconds behind now."} {aircraft.length?`${aircraft.length} eligible aircraft have observations on both sides of this instant.`:"Waiting for observations on both sides of the delayed clock; missing spans remain empty."} Latest-feed freshness is checked separately. No extrapolation or mixed-time aircraft.</p>}
    {flat&&<p className="kansas-sky-context">2D chart: aircraft and trails are flattened to their geographic positions. All reported heights remain available; no MSL slice membership is inferred.</p>}
    {replaying&&<><div className="kansas-sky-transport"><button type="button" disabled={!range||range[0]===range[1]||archiveState==="loading"&&mode==="recorded"} aria-pressed={playing} onClick={()=>{if(range){if(cursor>=range[1])setCursor(range[0]);else if(cursor<range[0])setCursor(range[0]);}setPlaying(v=>!v);}}>{playing?"Pause":"Play"}</button><label>Speed<select aria-label="Replay speed" value={speed} onChange={e=>setSpeed(Number(e.target.value))}>{[1,4,16].map(v=><option value={v} key={v}>{v}×</option>)}</select></label><button type="button" onClick={()=>changeMode("live")}>Return to live</button></div>
      <label>Flight timeline<input type="range" aria-label="Flight timeline" aria-valuetext={utc(effectiveCursor)} aria-describedby={rangeId} min={range?.[0]??0} max={range?.[1]??1} step={100} value={range?effectiveCursor:0} disabled={!range||range[0]===range[1]} onChange={e=>{setPlaying(false);setCursor(Number(e.target.value));}} /></label>
      <small id={rangeId}>{range?`${utc(range[0])} → ${utc(range[1])}`:"No retained observations in this view."}</small>
      {range&&cursor<range[0]&&<small>Earlier session history expired. Clock, aircraft and timeline now show the earliest retained instant.</small>}
      <p className="kansas-sky-context">Replay aircraft only. Airspace, terrain, weather and restrictions elsewhere on the map are current context, not a reconstruction of this flight’s conditions.</p></>}
    <label>Filter aircraft<input type="search" aria-label="Filter Kansas Sky aircraft" value={aircraftFilter} onChange={event=>setAircraftFilter(event.target.value)} placeholder="Callsign, registration or hex" /></label>
    <small>{matchingOptions.length} matching aircraft; up to 3,000 listed, plus the retained selection. Filtering changes this list only; retained data stays intact.</small>
    <label>Aircraft<select aria-label="Kansas Sky aircraft" value={selected??""} onChange={e=>{setSelected(e.target.value||null);setCamera("free");setFlightView(false);}}><option value="">Choose an aircraft or click its silhouette</option>{options.map(([hex,title])=><option key={hex} value={hex}>{title} · {hex.toUpperCase()}</option>)}</select></label>
    {picked&&<h5>{label(picked)} <span>{picked.type??"Aircraft type unavailable"}</span></h5>}
    <button type="button" className="kansas-sky-open-flight" disabled={!picked||flat} onClick={openFlightView}>View aircraft in 3D ↗</button>
    {replaying&&selected&&<div className="kansas-sky-journey-actions"><button type="button" disabled={!selectedPoints.length} onClick={overviewJourney}>{parts.multipart?"See this retained part":"See entire retained path"}</button><button type="button" disabled={!range||range[0]===range[1]} onClick={replayJourney}>{parts.multipart?"Experience this part":"Experience from the start"}</button></div>}
    {mode==="recorded"&&selected&&<small>Gold: elapsed route. Muted cyan: recorded route ahead of the replay cursor, not a prediction. This {parts.multipart?`part (${entry?.part}/${entry?.partCount})`:"file"} contains {selectedPoints.length.toLocaleString()} observations; unrecorded parts of a crossing remain unknown.</small>}
    <small>{flat?"Choose 3D volumes above to view the flight in space.":"Frame the selected aircraft above the map. Playback and camera controls stay on the map when Layers is closed."}</small>
    <div className="kansas-sky-camera" role="group" aria-label="Aircraft camera">{(["free","follow","orbit"] as const).map(view=><button type="button" key={view} aria-pressed={camera===view} disabled={view!=="free"&&(!picked||reduced||flat)} onClick={()=>setCamera(view)}>{view==="free"?"Free map":view==="follow"?"Follow":"Orbit"}</button>)}</div>
    {reduced&&<small>Reduced motion: camera movement is off. Replay advances only when you press Play.</small>}
    {picked?<><dl className="kansas-sky-instruments"><div><dt>Pressure altitude</dt><dd>{measure(picked.altBaroFt,"ft")}</dd></div><div><dt>Geometric · WGS84</dt><dd>{measure(picked.altGeomFt,"ft")}</dd></div><div><dt>Ground speed</dt><dd>{measure(picked.groundSpeedKt,"kt")}</dd></div><div><dt>Vertical rate</dt><dd>{measure(picked.verticalRateFpm,"ft/min")}</dd></div><div><dt>Track</dt><dd>{measure(picked.trackDeg,"°")}</dd></div><div><dt>Reported roll</dt><dd>{measure(picked.rollDeg,"°")}</dd></div></dl>{picked.emergency&&<p role="status">Reported emergency: {picked.emergency}{picked.squawk?` · squawk ${picked.squawk}`:""}</p>}<small>Source: {currentFeed?envelope?.provider.title??"Unavailable":selectedSource??"Unavailable"} · Position: {picked.positionMethod??"method unavailable"} · {picked.interpolated?"between recorded observations":"reported observation"}. {picked.observedAt?`${picked.timestampBasis==="retrieval-estimate"?"Estimated observation time":"Observed"} ${typeof picked.observedAt==="number"?utc(picked.observedAt):picked.observedAt}`:"Observation time unavailable"}</small>{picked.altGeomFt===null&&picked.altBaroFt===null&&<p>Height unknown: the ground-level marker is a locator, not an observed surface position.</p>}</>:<p role="status">{selected?"No observation for this aircraft at the selected time. Gaps are not filled.":currentFeed?(feedState==="error"?"Live feed unavailable. No stale positions are drawn.":feedState==="ready"?`${aircraft.length} observed aircraft. Select one to inspect or follow.`:"Waiting for aircraft observations…"):"Choose a retained aircraft to inspect its measurements."}</p>}
    <div className="kansas-sky-guide-toggles"><label><input type="checkbox" checked={showPaths} onChange={event=>setShowPaths(event.target.checked)}/> Flight paths</label><label><input type="checkbox" checked={showGuides} disabled={flat||!showPaths} onChange={event=>setShowGuides(event.target.checked)}/> Height guides</label></div>
    <small>{renderMetrics.aircraft} aircraft drawn · {renderMetrics.heightGuides} terrain guides. Rendering may thin historical geometry or reduce redraw frequency before removing aircraft. Terrain endpoints are map context; aircraft heights remain approximate.</small>
    {selectedPoints.length>0&&<SkyAltitudeProfile points={selectedPoints} cursor={effectiveCursor} canSeek={replaying} onSeek={seek}/>}
    {!picked&&retainedDetail&&<small>Brief from a retained observation at {retainedDetail.observedAt}. This is not a position in the current observation gap.</small>}
    {detailAircraft&&<SkyAircraftBrief aircraft={detailAircraft} observationCount={selectedPoints.length} gap={!picked}/>}
    {detailAircraft&&<SkyAircraftDossier aircraft={detailAircraft} source={currentFeed?envelope?.provider.title??"Unavailable":selectedSource??"Unavailable"}/>}
    <details className="kansas-sky-history" open={historyOpen} onToggle={event=>setHistoryOpen(event.currentTarget.open)}><summary>Past flight paths <span>{selected?selected.toUpperCase():"Published recordings"}</span></summary>
      <p>Browse prepared regional observations by UTC day. This catalog reports published coverage; it does not establish that an unattended daily collector is running.</p>
      {dayState==="loading"&&<p role="status">Loading available archive dates…</p>}
      {dayState==="unavailable"&&<p>The daily index is unavailable. The original prepared-flight catalog remains available.</p>}
      <label>Archive day<select aria-label="Archive day" value={day} onChange={event=>setDay(event.target.value)}><option value="">Original prepared recordings</option>{days.map(item=><option key={item.day} value={item.day}>{item.day} · {item.aircraftCount.toLocaleString()} aircraft</option>)}</select></label>
      <label>Find an archived aircraft<input type="search" aria-label="Find an archived aircraft" value={recordingFilter} onChange={event=>setRecordingFilter(event.target.value)} placeholder="Callsign, hex or date"/></label>
      {selected&&<button type="button" onClick={()=>{setSelected(null);setCamera("free");setFlightView(false);}}>Browse all archived aircraft</button>}
      {archiveDay&&<small>{archiveDay.coverage==="provider-day-processed"?"Provider day processed; receiver and download coverage still limit completeness.":"Selected recordings only; this is not a complete day."} {archiveDay.pointCount.toLocaleString()} published observations.</small>}
      {catalogState==="loading"&&<p role="status">Loading prepared paths…</p>}{catalogState==="error"&&<p role="alert">The path catalog is unavailable.</p>}
      {catalogState==="ready"&&!historyFlights.length&&<p>No published path for {selected?.toUpperCase()??"this selection"} on this day. No path is inferred from missing records.</p>}
      <ul>{historyFlights.slice(0,100).map(f=><li key={f.id}><button type="button" aria-pressed={entry?.id===f.id&&mode==="recorded"} onClick={()=>void loadRecorded(f.id)}><strong>{f.title}</strong><span>{utc(Date.parse(f.start))} → {utc(Date.parse(f.end))}</span>{f.pointCount!==undefined&&<span>{f.pointCount.toLocaleString()} observations · {f.segmentCount??"Unknown"} segments</span>}</button></li>)}</ul>
      {historyFlights.length>100&&<small>First 100 paths shown. Select an aircraft to narrow this day.</small>}
      {entry&&<small>File integrity: {archiveState==="ready"?"SHA-256 verified":"Not yet verified"}. <a href={entry.sourceUrl} target="_blank" rel="noreferrer">Original source</a> · {entry.license}</small>}
    </details>
    {renderError&&<p role="status">{renderError}</p>}
    {aircraft.length>3000&&<small>The current view exceeds the 3,000-aircraft drawing bound. Choose an individual prepared path for all its retained observations.</small>}
    {snapshot.truncated&&mode!=="recorded"&&<small>Session memory limit reached; older trail detail was discarded.</small>}
    {envelope?.truncated&&currentFeed&&<small>The receiver response reached a processing bound: this view is truncated, not a complete aircraft census.</small>}
    {!!envelope?.dropped&&currentFeed&&<small>{envelope.dropped} feed records omitted by validation or regional limits.</small>}
    <p className="kansas-sky-limit">Vertical placement is approximate; pressure altitude and WGS84 height are not MSL. Silhouettes are enlarged; a diamond means heading unavailable. No confirmed airspace occupancy, navigation, owner or mission inference. Pan, zoom or use map keys to release the camera. On the globe, select aircraft from this list.</p>
    <small>{mode==="recorded"&&entry?<>Recorded source: <a href={entry.sourceUrl} target="_blank" rel="noreferrer">{entry.provider}</a> · {entry.license}</>:mode==="session"?<>Session sources: {sourceIds||"No retained source"}. Observation times are retained with each sample.</>:envelope?<>Live source: <a href={envelope.provider.homepage} target="_blank" rel="noreferrer">{envelope.provider.title}</a> · {envelope.provider.terms}</>:"Receiver coverage varies; an empty view does not mean an empty sky."}</small>
  </section></>;
}
