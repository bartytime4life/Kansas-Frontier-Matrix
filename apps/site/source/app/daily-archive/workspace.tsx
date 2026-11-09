"use client";
import Link from "next/link";
import { useCallback, useEffect, useRef, useState, useSyncExternalStore } from "react";
import type { FeatureCollection } from "geojson";
import { DAILY_FEEDS, type ArchiveCatalog, type ArchiveEntry, type ArchivePayload, type DailyFeed } from "../daily-archive";
import { loadMapLibre, type Map as MapLibreMap } from "../maplibre-seam";
import styles from "./archive.module.css";
import { applyArchiveMapData } from "../daily-archive-map";

type Stored = { entry: ArchiveEntry; payload: ArchivePayload; reviews: {state: string; note: string; reviewed_at: string}[] };
type CatalogRead = { day: string; access: string; revision: number; catalog: ArchiveCatalog | null; error: string | null };
const empty: FeatureCollection = { type: "FeatureCollection", features: [] };
const today = () => new Date().toISOString().slice(0, 10);
const subscribeLocal = () => () => {};
const localRuntime = () => window.location.hostname === "127.0.0.1";
class ArchiveRequestError extends Error {
  constructor(message:string,readonly status:number){super(message);}
}
function catalogFailure(error:unknown,local:boolean):string {
  if(error instanceof ArchiveRequestError){
    if(error.status===401)return local?"Archive owner access is required. Enter your local owner access above, then retry the archive check.":"Archive owner access is required. Sign in as an archive owner on the private Site, then retry the archive check.";
    if(error.status===403)return local?"This access cannot open the archive. Use the correct local owner access, then retry the archive check.":"This account cannot open the archive. Use an archive owner account, then retry the archive check.";
    if(error.status>=500)return "Archive status is unavailable. Check archive access and storage setup, then retry the archive check.";
  }
  return "Archive status could not be checked. Check your connection and capture day, then retry the archive check.";
}
async function archiveRequest(path: string, options?: RequestInit, access = "") {
  const headers = new Headers(options?.headers);
  if (access) headers.set("Authorization", `Bearer ${access}`);
  return fetch(`/api/daily-archive${path}`, { cache: "no-store", ...options, headers });
}
async function archiveApi(path: string, options?: RequestInit, access = "") {
  const response = await archiveRequest(path, options, access);
  const body = await response.json();
  if (!response.ok) throw new ArchiveRequestError(body.error || `Archive returned HTTP ${response.status}.`,response.status);
  return body;
}

function ArchiveMap({ payload, counties }: { payload: ArchivePayload | null; counties: FeatureCollection | null }) {
  const container = useRef<HTMLDivElement>(null); const map = useRef<MapLibreMap | null>(null);
  const current = useRef({payload,counties});
  const [mapError, setMapError] = useState(""); const [feature, setFeature] = useState<{ payload: ArchivePayload | null; properties: Record<string,unknown> } | null>(null);
  const update = useCallback(() => {
    const m = map.current; if (!m) return;
    applyArchiveMapData(m, current.current.payload, current.current.counties);
  }, []);
  useEffect(() => {
    let disposed = false;
    void loadMapLibre().then(lib => {
      if (disposed || !container.current) return;
      lib.setWorkerUrl("/maplibre/maplibre-gl-worker.mjs");
      const m = new lib.Map({container:container.current,center:[-98.3,38.5],zoom:5.7,style:{version:8,sources:{counties:{type:"geojson",data:empty},capture:{type:"geojson",data:empty}},layers:[
        {id:"background",type:"background",paint:{"background-color":"#102c38"}},
        {id:"counties-fill",type:"fill",source:"counties",paint:{"fill-color":"#214652","fill-opacity":0.4}},
        {id:"counties-line",type:"line",source:"counties",paint:{"line-color":"#72929b","line-width":0.7}},
        {id:"capture-fill",type:"fill",source:"capture",filter:["==",["geometry-type"],"Polygon"],paint:{"fill-color":"#e7a76f","fill-opacity":0.38}},
        {id:"capture-line",type:"line",source:"capture",filter:["!=",["geometry-type"],"Point"],paint:{"line-color":"#edc59a","line-width":1.5}},
        {id:"capture-point",type:"circle",source:"capture",filter:["==",["geometry-type"],"Point"],paint:{"circle-color":"#77e4ce","circle-radius":5,"circle-stroke-color":"#0c222e","circle-stroke-width":1.5}},
      ]},attributionControl:false});
      map.current=m; m.addControl(new lib.NavigationControl(),"top-right");
      m.addControl(new lib.AttributionControl({compact:false,customAttribution:"Stored source snapshots · county reference edition: 2020 Census"}));
      m.on("load",update); m.on("error",()=>setMapError("Map rendering is unavailable. Source details and stored-file downloads remain available."));
      m.on("click",event=>{ const found=m.queryRenderedFeatures(event.point,{layers:["capture-point","capture-fill","capture-line"]})[0];setFeature(found ? { payload: current.current.payload, properties: found.properties } : null); });
    }).catch(()=>setMapError("Map could not start. Use the stored-file download and source details below."));
    return ()=>{disposed=true;map.current?.remove();map.current=null;};
  },[update]);
  useEffect(()=>{current.current = {payload,counties};update();},[payload,counties,update]);
  return <><div className={styles.map} ref={container} role="region" aria-label="Stored daily capture map of Kansas" />{mapError&&<p role="status">{mapError}</p>}{feature && payload && feature.payload === payload && <div className={styles.details}><h2>Selected feature</h2><pre>{JSON.stringify(feature.properties,null,2)}</pre></div>}</>;
}

export default function DailyArchive() {
  const local=useSyncExternalStore(subscribeLocal,localRuntime,()=>false);const [access,setAccess]=useState("");const [accessInput,setAccessInput]=useState("");
  const api=useCallback((path:string,options?:RequestInit)=>archiveApi(path,options,access),[access]);
  const write = (query: string, body?: unknown) => api(query, { method: "POST", headers: { "X-KFM-Archive-Writer": "daily-v1", "Content-Type": "application/json" }, ...(body === undefined ? {} : { body: JSON.stringify(body) }) });
  const [day,setDay]=useState(today);const [feed,setFeed]=useState<DailyFeed>("usgs-streamflow");const [id,setId]=useState("");
  const [catalogRead,setCatalogRead]=useState<CatalogRead|null>(null);
  const [storedRead,setStored]=useState<{api:typeof api;value:Stored}|null>(null);const [countyRead,setCounties]=useState<{day:string;api:typeof api;entryId:string;data:FeatureCollection}|null>(null);
  const [heldCaptureIds,setHeldCaptureIds]=useState<ReadonlySet<string>>(()=>new Set());const heldCaptureIdsRef=useRef<ReadonlySet<string>>(new Set());
  const [message,setMessage]=useState("");const [busy,setBusy]=useState(false);const [budget,setBudget]=useState("2000000000");const [paused,setPaused]=useState(false);const [note,setNote]=useState("");const [review,setReview]=useState("reviewed");
  const [revision,setRevision]=useState(0);
  const sameCatalogContext=catalogRead?.day===day&&catalogRead.access===access;
  const catalog=sameCatalogContext?catalogRead.catalog:null;
  const catalogPending=!sameCatalogContext||catalogRead.revision!==revision;
  const catalogError=!catalogPending?catalogRead?.error:null;
  const catalogReady=!catalogPending&&!catalogError&&catalog!==null;
  const refresh=()=>{setNote("");setRevision(value=>value+1);};
  const chooseDay=(value:string)=>{if(value!==day){setStored(null);setCounties(null);}setDay(value);setId("");refresh();};
  useEffect(()=>{
    const controller=new AbortController();
    let active=true,timedOut=false,cancelDeadline=()=>{};
    const deadline=new Promise<never>((_resolve,reject)=>{cancelDeadline=()=>reject(controller.signal.reason);controller.signal.addEventListener("abort",cancelDeadline,{once:true});});
    const timer=setTimeout(()=>{timedOut=true;controller.abort();},15_000);
    void Promise.race([api(`?day=${day}`,{signal:controller.signal}),deadline]).then((result:ArchiveCatalog)=>{
      if(!active||controller.signal.aborted)return;
      if(!result||result.day!==day||!Array.isArray(result.entries)||!Array.isArray(result.days)||typeof result.storage?.paused!=="boolean"||!Number.isSafeInteger(result.storage.used)||!Number.isSafeInteger(result.storage.budget))throw new Error("Archive status could not be verified. Retry the archive check.");
      setCatalogRead({day,access,revision,catalog:result,error:null});setBudget(String(result.storage.budget));setPaused(result.storage.paused);setMessage(result.entries.length?"":"No captures for this day. Live data is never substituted.");
    }).catch(error=>{
      if(!active||controller.signal.aborted&&!timedOut)return;
      const reason=timedOut?"Archive status took too long to respond. Retry the archive check.":catalogFailure(error,local);
      setCatalogRead(previous=>({day,access,revision,catalog:previous?.day===day&&previous.access===access?previous.catalog:null,error:reason}));
    }).finally(()=>{clearTimeout(timer);controller.signal.removeEventListener("abort",cancelDeadline);});
    return ()=>{active=false;controller.abort();clearTimeout(timer);};
  },[day,access,revision,api,local]);
  const entries=catalog?.entries.filter(entry=>entry.feed===feed)??[];
  const selected=entries.find(entry=>entry.id===id)??entries.find(entry=>["ready","empty","partial"].includes(entry.status))??entries[0];
  const selectedId=selected?.id;
  const selectedHeld=Boolean(selected&&(selected.review==="held"||heldCaptureIds.has(selected.id)));
  const selectedEligible=Boolean(selected&&["ready","empty","partial"].includes(selected.status)&&!selectedHeld);
  const stored=selectedEligible&&storedRead?.api===api&&storedRead.value.entry.id===selectedId?storedRead.value:null;
  const countyEntry=catalog?.entries.find(entry=>entry.feed==="census-counties"&&["ready","partial"].includes(entry.status)&&entry.review!=="held"&&!heldCaptureIds.has(entry.id));
  const counties=countyEntry&&countyRead?.day===day&&countyRead.api===api&&countyRead.entryId===countyEntry.id?countyRead.data:null;
  useEffect(()=>{
    const controller=new AbortController();
    if(selectedId&&selectedEligible) void api(`?id=${selectedId}`,{signal:controller.signal}).then(result=>{if(!controller.signal.aborted&&!heldCaptureIdsRef.current.has(selectedId))setStored({api,value:result});}).catch(error=>{if(!controller.signal.aborted)setMessage(error.message);});
    return ()=>controller.abort();
  },[selectedId,selected,selectedEligible,revision,api]);
  useEffect(()=>{
    const controller=new AbortController();
    if(countyEntry) void api(`?id=${countyEntry.id}`,{signal:controller.signal}).then(result=>{if(!controller.signal.aborted&&!heldCaptureIdsRef.current.has(countyEntry.id))setCounties({day,api,entryId:countyEntry.id,data:result.payload.data});}).catch(()=>{});
    return ()=>controller.abort();
  },[countyEntry,day,api]);
  async function download(entry:ArchiveEntry) {
    try {
      const response=await archiveRequest(`?id=${entry.id}&action=download`,undefined,access);
      if(!response.ok) throw new Error((await response.json()).error||"Archive download failed.");
      const url=URL.createObjectURL(await response.blob());const link=document.createElement("a");
      link.href=url;link.download=`${entry.day}-${entry.feed}-${entry.id}.json`;link.click();
      setTimeout(()=>URL.revokeObjectURL(url),1000);
    } catch(error) {setMessage((error as Error).message);}
  }
  async function capture() {
    if(!catalogReady||busy||catalog.storage.paused)return;
    setBusy(true);const results:string[]=[];
    for(const source of DAILY_FEEDS){setMessage(`Capturing ${source.title}…`);try{const result=await write(`?action=capture&feed=${source.id}`);results.push(`${source.title}: ${result.status??result.outcome}`);}catch(error){results.push(`${source.title}: ${error instanceof Error?error.message:"failed"}`);}}
    chooseDay(today());setBusy(false);setMessage(results.join(" · "));
  }
  async function saveReview(){
    if(!catalogReady||busy||!selected)return;
    const reviewedId=selected.id,decision=review,submittedNote=note.trim();
    setBusy(true);
    try{
      const acknowledgement=await write("?action=review",{id:reviewedId,state:decision,note:submittedNote});
      const acknowledgedNote=typeof acknowledgement?.note==="string"?acknowledgement.note.trim():submittedNote;
      const held=new Set(heldCaptureIdsRef.current);if(decision==="held")held.add(reviewedId);else held.delete(reviewedId);
      heldCaptureIdsRef.current=held;setHeldCaptureIds(held);
      setCatalogRead(previous=>previous?.catalog?{...previous,catalog:{...previous.catalog,entries:previous.catalog.entries.map(entry=>entry.id===reviewedId?{...entry,review:decision as ArchiveEntry["review"],review_note:acknowledgedNote}:entry)}}:previous);
      if(decision==="held"){
        setStored(previous=>previous?.value.entry.id===reviewedId?null:previous);
        setCounties(previous=>previous?.entryId===reviewedId?null:previous);
      }
      refresh();setMessage("Review recorded. Earlier decisions and source bytes are preserved.");
    }catch(error){setMessage((error as Error).message);}finally{setBusy(false);}
  }
  async function saveSettings(){if(!catalogReady||busy)return;setBusy(true);try{await write("?action=settings",{budget:Number(budget),paused});refresh();setMessage("Capture settings saved.");}catch(error){setMessage((error as Error).message);}finally{setBusy(false);}}
  const source=DAILY_FEEDS.find(source=>source.id===feed)!;
  return <main className={styles.workspace}>
    <header className={styles.header}><div><span className={styles.kicker}>Kansas · retained source snapshots</span><h1>Daily archive</h1></div><nav className={styles.actions}><Link href="/">Explorer</Link><Link href="/observatory">Provider history</Link></nav></header>
    <p>Choose a capture day, inspect its saved map, and record your review. A daily snapshot preserves what the source returned at that moment; it does not guarantee a full day of observations. Capture time, provider time, and review time remain separate.</p>
    {local&&<form className={styles.controls} onSubmit={event=>{event.preventDefault();setStored(null);setCounties(null);setAccess(accessInput);setAccessInput("");refresh();}}><label>Local archive owner access<input type="password" autoComplete="off" value={accessInput} onChange={event=>setAccessInput(event.target.value)}/></label><button type="submit">Unlock archive</button><p>Use your private archive owner token. Access stays in this page until it is closed or reloaded.</p></form>}
    <div className={styles.controls}><label>Capture day (UTC)<input type="date" value={day} min={catalog?.earliestDay??undefined} max={today()} onChange={event=>chooseDay(event.target.value)} /></label><button onClick={()=>chooseDay(today())}>Today</button><button disabled={busy||!catalogReady||catalog?.storage.paused} onClick={()=>void capture()}>Capture today’s sources</button><button disabled={busy} aria-busy={catalogPending} onClick={refresh}>{catalogError?"Retry archive check":"Refresh archive"}</button></div>
    <div role={catalogError?"alert":"status"} className={styles.status}>{catalogPending?"Reading stored coverage…":catalogError??message}{catalog&&!catalogReady&&" Showing previously checked coverage; current status is unverified."}</div>
    {!catalogReady&&<p>Capture and settings changes require a successful archive check. {local?"If access is required, unlock the archive above, then retry.":"If access is required, sign in as an archive owner on the private Site, then retry."}</p>}
    <details><summary>Stored dates · {catalog?`${!catalogReady?"previously checked · ":""}${catalog.days.length} recent capture days`:catalogPending?"checking coverage":"status unavailable"}</summary><p>Up to 366 recent dates are listed. Older captures remain available through the date field. Gaps are not filled.</p><div className={styles.dates}>{catalog?.days.map(item=><button key={item.day} onClick={()=>chooseDay(item.day)}>{item.day}</button>)}</div></details>
    <div className={styles.grid}>
      <aside className={styles.sources} aria-label="Daily source captures">{DAILY_FEEDS.map(source=>{const rows=catalog?.entries.filter(entry=>entry.feed===source.id)??[];const capture=rows.find(entry=>["ready","empty","partial"].includes(entry.status))??rows[0];return <button className={styles.source} key={source.id} aria-pressed={feed===source.id} onClick={()=>{if(feed===source.id)return;setFeed(source.id);setId("");setStored(null);setNote("");}}><strong>{source.title}</strong><small>{!catalogReady?catalog?"Previously checked · ":catalogPending?"Checking saved captures…":"Saved capture status unavailable":""}{catalog?capture?`${capture.status} · ${capture.feature_count??0} features · review ${capture.review}`:catalogReady?"Missing · no capture":"No capture in previously checked coverage":""}</small></button>;})}</aside>
      <section className={styles.viewer} aria-label="Capture review"><h2>{source.title} · {day}</h2><p>{source.scope}. Map symbols locate returned records; they do not estimate conditions between observations.</p>
        <ArchiveMap payload={stored && stored.entry.id===selectedId?stored.payload:null} counties={counties}/>
        {!stored&&<p className={styles.empty}>{!catalog?catalogPending?"Checking saved capture coverage…":"Saved capture coverage is unavailable. Retry the archive check.":!catalogReady&&!selected?"No capture in previously checked coverage. Recheck the archive before treating this as current status.":selectedHeld?"This capture is held and hidden from the map. Its stored file remains inspectable. A hold recorded in this session remains in effect until you save a new review.":selected?.status==="failed"?`Capture failed: ${selected.message}`:selected?.status==="running"?"Capture is running. A completed, verified file is required for display.":selected?"Loading verified stored data…":"No saved data for this source and day."}</p>}
        {selected&&<article className={styles.details}><label>Capture attempt<select value={selected.id} onChange={event=>{setStored(null);setNote("");setId(event.target.value);}}>{entries.map(entry=><option key={entry.id} value={entry.id}>Attempt {entry.attempt} · {entry.status} · {entry.started_at}</option>)}</select></label><dl><dt>Captured</dt><dd>{selected.started_at}</dd><dt>Provider time</dt><dd>{selected.source_time??"Not supplied; see feature timestamps"}</dd><dt>Source day</dt><dd>{selected.source_day??"See source window and edition"}</dd><dt>Stored bytes</dt><dd>{selected.bytes.toLocaleString()}</dd><dt>SHA-256</dt><dd>{selected.sha256??"No completed payload"}</dd><dt>Review</dt><dd>{selected.review}{selected.review_note?` · ${selected.review_note}`:" · awaiting human review"}</dd></dl>
          <p>{stored?.payload.source}</p><p>{selected.message}</p>{selected.object_key&&["ready","empty","partial"].includes(selected.status)&&<button onClick={()=>void download(selected)}>Download retained adapter response</button>}
          {stored&&<details><summary>Feature records · keyboard-accessible map alternative</summary><p>First 100 records below; the download contains all {stored.payload.featureCount}.</p><pre>{JSON.stringify(stored.payload.data.features.slice(0,100),null,2)}</pre></details>}
          {["ready","empty","partial"].includes(selected.status)&&<div className={styles.review}><h2>Record archive review</h2><label>Decision<select value={review} onChange={event=>setReview(event.target.value)}><option value="reviewed">Reviewed for archive context</option><option value="held">Hold and hide from map</option><option value="pending">Return to pending review</option></select></label><label>Review note<textarea maxLength={1000} value={note} onChange={event=>setNote(event.target.value)} /></label><button disabled={busy||!catalogReady||!note.trim()} onClick={()=>void saveReview()}>Save review</button><p>This decision applies to this exact capture. It does not admit a source or authorize evidence, reports, or release.</p>{stored?.reviews.map((item,index)=><p key={index}>{item.reviewed_at} · {item.state} · {item.note}</p>)}</div>}
        </article>}
      </section>
    </div>
    <section className={styles.settings}><h2>Storage & daily capture</h2><p>{catalog?`${!catalogReady?"Previously checked: ":""}${catalog.storage.used.toLocaleString()} bytes stored or reserved of ${catalog.storage.budget.toLocaleString()} bytes allowed.`:catalogPending?"Reading storage status…":"Storage status is unavailable. Retry the archive check."} Nothing is automatically deleted. A full budget stops new captures. Interrupted writes may retain a conservative reservation until inspected.</p><div className={styles.controls}><label>Maximum archive bytes<input type="number" min="16777216" max="1000000000000" step="1" value={budget} disabled={busy||!catalogReady} onChange={event=>setBudget(event.target.value)}/></label><label><span>Pause new captures</span><input type="checkbox" checked={paused} disabled={busy||!catalogReady} onChange={event=>setPaused(event.target.checked)}/></label><button disabled={busy||!catalogReady} onClick={()=>void saveSettings()}>Save capture settings</button></div><p>Scheduled capture runs separately from the browser. A stopped computer cannot collect local snapshots; its next run captures the actual current day. Local and hosted archives have separate storage. These retained adapter responses are external context, pending review; source limitations, partial coverage, and provider revisions remain visible.</p></section>
  </main>;
}
