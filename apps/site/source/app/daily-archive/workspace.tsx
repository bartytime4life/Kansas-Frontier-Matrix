"use client";
import Link from "next/link";
import { useCallback, useEffect, useRef, useState } from "react";
import type { FeatureCollection } from "geojson";
import { DAILY_FEEDS, type ArchiveCatalog, type ArchiveEntry, type ArchivePayload, type DailyFeed } from "../daily-archive";
import { loadMapLibre, type Map as MapLibreMap } from "../maplibre-seam";
import styles from "./archive.module.css";
import { applyArchiveMapData } from "../daily-archive-map";

type Stored = { entry: ArchiveEntry; payload: ArchivePayload; reviews: {state: string; note: string; reviewed_at: string}[] };
const empty: FeatureCollection = { type: "FeatureCollection", features: [] };
const today = () => new Date().toISOString().slice(0, 10);
async function api(path: string, options?: RequestInit) {
  const response = await fetch(`/api/daily-archive${path}`, { cache: "no-store", ...options });
  const body = await response.json();
  if (!response.ok) throw new Error(body.error || `Archive returned HTTP ${response.status}.`);
  return body;
}
const write = (query: string, body?: unknown) => api(query, { method: "POST", headers: { "X-KFM-Archive-Writer": "daily-v1", "Content-Type": "application/json" }, ...(body === undefined ? {} : { body: JSON.stringify(body) }) });

function ArchiveMap({ payload, counties }: { payload: ArchivePayload | null; counties: FeatureCollection | null }) {
  const container = useRef<HTMLDivElement>(null); const map = useRef<MapLibreMap | null>(null);
  const current = useRef({payload,counties}); current.current = {payload,counties};
  const [mapError, setMapError] = useState(""); const [feature, setFeature] = useState<Record<string,unknown> | null>(null);
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
      m.on("click",event=>{ const found=m.queryRenderedFeatures(event.point,{layers:["capture-point","capture-fill","capture-line"]})[0];setFeature(found?.properties??null); });
    }).catch(()=>setMapError("Map could not start. Use the stored-file download and source details below."));
    return ()=>{disposed=true;map.current?.remove();map.current=null;};
  },[update]);
  useEffect(()=>{update();setFeature(null);},[payload,counties,update]);
  return <><div className={styles.map} ref={container} role="region" aria-label="Stored daily capture map of Kansas" />{mapError&&<p role="status">{mapError}</p>}{feature&&<div className={styles.details}><h2>Selected feature</h2><pre>{JSON.stringify(feature,null,2)}</pre></div>}</>;
}

export default function DailyArchive() {
  const [day,setDay]=useState(today);const [feed,setFeed]=useState<DailyFeed>("usgs-streamflow");const [id,setId]=useState("");
  const [catalog,setCatalog]=useState<ArchiveCatalog|null>(null);const [stored,setStored]=useState<Stored|null>(null);const [counties,setCounties]=useState<FeatureCollection|null>(null);
  const [message,setMessage]=useState("");const [busy,setBusy]=useState(false);const [budget,setBudget]=useState("2000000000");const [paused,setPaused]=useState(false);const [note,setNote]=useState("");const [review,setReview]=useState("reviewed");
  const [revision,setRevision]=useState(0);
  const chooseDay=(value:string)=>{setDay(value);setCatalog(null);setStored(null);setCounties(null);setId("");};
  useEffect(()=>{
    const controller=new AbortController();setStored(null);setCounties(null);setCatalog(null);setMessage("Reading stored coverage…");
    void api(`?day=${day}`,{signal:controller.signal}).then((result:ArchiveCatalog)=>{if(controller.signal.aborted)return;setCatalog(result);setBudget(String(result.storage.budget));setPaused(result.storage.paused);setMessage(result.entries.length?"":"No captures for this day. Live data is never substituted.");}).catch(error=>{if(!controller.signal.aborted)setMessage(error.message);});
    return ()=>controller.abort();
  },[day,revision]);
  const entries=catalog?.entries.filter(entry=>entry.feed===feed)??[];
  const selected=entries.find(entry=>entry.id===id)??entries.find(entry=>["ready","empty","partial"].includes(entry.status))??entries[0];
  const selectedId=selected?.id;
  useEffect(()=>{
    const controller=new AbortController();setStored(null);setNote("");
    if(selectedId&&selected&&["ready","empty","partial"].includes(selected.status)&&selected.review!=="held") void api(`?id=${selectedId}`,{signal:controller.signal}).then(result=>{if(!controller.signal.aborted)setStored(result);}).catch(error=>{if(!controller.signal.aborted)setMessage(error.message);});
    return ()=>controller.abort();
  },[selectedId,selected,revision]);
  useEffect(()=>{
    const controller=new AbortController();setCounties(null);
    const entry=catalog?.entries.find(entry=>entry.feed==="census-counties"&&["ready","partial"].includes(entry.status)&&entry.review!=="held");
    if(entry) void api(`?id=${entry.id}`,{signal:controller.signal}).then(result=>{if(!controller.signal.aborted)setCounties(result.payload.data);}).catch(()=>{});
    return ()=>controller.abort();
  },[catalog]);
  async function capture() {
    setBusy(true);const results:string[]=[];
    for(const source of DAILY_FEEDS){setMessage(`Capturing ${source.title}…`);try{const result=await write(`?action=capture&feed=${source.id}`);results.push(`${source.title}: ${result.status??result.outcome}`);}catch(error){results.push(`${source.title}: ${error instanceof Error?error.message:"failed"}`);}}
    chooseDay(today());setRevision(value=>value+1);setBusy(false);setMessage(results.join(" · "));
  }
  async function saveReview(){if(!selected)return;setBusy(true);try{await write("?action=review",{id:selected.id,state:review,note});setStored(null);setRevision(value=>value+1);setMessage("Review recorded. Earlier decisions and source bytes are preserved.");}catch(error){setMessage((error as Error).message);}finally{setBusy(false);}}
  async function saveSettings(){setBusy(true);try{await write("?action=settings",{budget:Number(budget),paused});setRevision(value=>value+1);setMessage("Capture settings saved.");}catch(error){setMessage((error as Error).message);}finally{setBusy(false);}}
  const source=DAILY_FEEDS.find(source=>source.id===feed)!;
  return <main className={styles.workspace}>
    <header className={styles.header}><div><span className={styles.kicker}>Kansas · retained source snapshots</span><h1>Daily archive</h1></div><nav className={styles.actions}><Link href="/">Explorer</Link><Link href="/observatory">Provider history</Link></nav></header>
    <p>Choose a capture day, inspect its saved map, and record your review. A daily snapshot preserves what the source returned at that moment; it does not guarantee a full day of observations. Capture time, provider time, and review time remain separate.</p>
    <div className={styles.controls}><label>Capture day (UTC)<input type="date" value={day} min={catalog?.earliestDay??undefined} max={today()} onChange={event=>chooseDay(event.target.value)} /></label><button onClick={()=>chooseDay(today())}>Today</button><button disabled={busy||catalog?.storage.paused} onClick={()=>void capture()}>Capture today’s sources</button><button disabled={busy} onClick={()=>setRevision(value=>value+1)}>Refresh archive</button></div>
    <div role="status" className={styles.status}>{message}</div>
    <details><summary>Stored dates · {catalog?.days.length??0} recent capture days</summary><p>Up to 366 recent dates are listed. Older captures remain available through the date field. Gaps are not filled.</p><div className={styles.dates}>{catalog?.days.map(item=><button key={item.day} onClick={()=>chooseDay(item.day)}>{item.day}</button>)}</div></details>
    <div className={styles.grid}>
      <aside className={styles.sources} aria-label="Daily source captures">{DAILY_FEEDS.map(source=>{const rows=catalog?.entries.filter(entry=>entry.feed===source.id)??[];const capture=rows.find(entry=>["ready","empty","partial"].includes(entry.status))??rows[0];return <button className={styles.source} key={source.id} aria-pressed={feed===source.id} onClick={()=>{setFeed(source.id);setId("");setStored(null);}}><strong>{source.title}</strong><small>{capture?`${capture.status} · ${capture.feature_count??0} features · review ${capture.review}`:"Missing · no capture"}</small></button>;})}</aside>
      <section className={styles.viewer} aria-label="Capture review"><h2>{source.title} · {day}</h2><p>{source.scope}. Map symbols locate returned records; they do not estimate conditions between observations.</p>
        <ArchiveMap payload={stored && stored.entry.id===selectedId?stored.payload:null} counties={counties}/>
        {!stored&&<p className={styles.empty}>{selected?.review==="held"?"This capture is held and hidden from the map. Its stored file remains inspectable.":selected?.status==="failed"?`Capture failed: ${selected.message}`:selected?.status==="running"?"Capture is running. A completed, verified file is required for display.":selected?"Loading verified stored data…":"No saved data for this source and day."}</p>}
        {selected&&<article className={styles.details}><label>Capture attempt<select value={selected.id} onChange={event=>{setStored(null);setId(event.target.value);}}>{entries.map(entry=><option key={entry.id} value={entry.id}>Attempt {entry.attempt} · {entry.status} · {entry.started_at}</option>)}</select></label><dl><dt>Captured</dt><dd>{selected.started_at}</dd><dt>Provider time</dt><dd>{selected.source_time??"Not supplied; see feature timestamps"}</dd><dt>Source day</dt><dd>{selected.source_day??"See source window and edition"}</dd><dt>Stored bytes</dt><dd>{selected.bytes.toLocaleString()}</dd><dt>SHA-256</dt><dd>{selected.sha256??"No completed payload"}</dd><dt>Review</dt><dd>{selected.review}{selected.review_note?` · ${selected.review_note}`:" · awaiting human review"}</dd></dl>
          <p>{stored?.payload.source}</p><p>{selected.message}</p>{selected.object_key&&["ready","empty","partial"].includes(selected.status)&&<a href={`/api/daily-archive?id=${selected.id}&action=download`}>Download retained adapter response</a>}
          {stored&&<details><summary>Feature records · keyboard-accessible map alternative</summary><p>First 100 records below; the download contains all {stored.payload.featureCount}.</p><pre>{JSON.stringify(stored.payload.data.features.slice(0,100),null,2)}</pre></details>}
          {["ready","empty","partial"].includes(selected.status)&&<div className={styles.review}><h2>Record archive review</h2><label>Decision<select value={review} onChange={event=>setReview(event.target.value)}><option value="reviewed">Reviewed for archive context</option><option value="held">Hold and hide from map</option><option value="pending">Return to pending review</option></select></label><label>Review note<textarea maxLength={1000} value={note} onChange={event=>setNote(event.target.value)} /></label><button disabled={busy||!note.trim()} onClick={()=>void saveReview()}>Save review</button><p>This decision applies to this exact capture. It does not admit a source or authorize evidence, reports, or release.</p>{stored?.reviews.map((item,index)=><p key={index}>{item.reviewed_at} · {item.state} · {item.note}</p>)}</div>}
        </article>}
      </section>
    </div>
    <section className={styles.settings}><h2>Storage & daily capture</h2><p>{catalog?`${catalog.storage.used.toLocaleString()} bytes stored or reserved of ${catalog.storage.budget.toLocaleString()} bytes allowed.`:"Reading storage status…"} Nothing is automatically deleted. A full budget stops new captures. Interrupted writes may retain a conservative reservation until inspected.</p><div className={styles.controls}><label>Maximum archive bytes<input type="number" min="16777216" max="1000000000000" step="1" value={budget} onChange={event=>setBudget(event.target.value)}/></label><label><span>Pause new captures</span><input type="checkbox" checked={paused} onChange={event=>setPaused(event.target.checked)}/></label><button disabled={busy||!catalog} onClick={()=>void saveSettings()}>Save capture settings</button></div><p>Scheduled capture runs separately from the browser. A stopped computer cannot collect local snapshots; its next run captures the actual current day. Local and hosted archives have separate storage. These retained adapter responses are external context, pending review; source limitations, partial coverage, and provider revisions remain visible.</p></section>
  </main>;
}
