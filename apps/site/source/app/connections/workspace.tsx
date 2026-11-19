"use client";
import {useCallback,useEffect,useRef,useState} from "react";
import Link from "next/link";
import dynamic from "next/dynamic";
import {VALUE_COLUMNS,series} from "../connection-series";
import type {Catalog,Receipt,Result} from "../connections-types";
import "./connections.css";
const ConnectionMap=dynamic(()=>import("../connection-map"),{ssr:false,loading:()=> <p>Preparing geometry view…</p>});
const labels:Record<string,string>={CREDENTIAL_REQUIRED:"This product needs its server-side provider credentials.",PROVIDER_REVIEW_REQUIRED:"This source needs its provider terms or rights review.",HOST_OR_CAPTURE_UNAVAILABLE:"Capture or storage is unavailable. Existing history is preserved.",HOST_CAPTURE_HELD:"Hosted capture setup is pending or paused.",PIPELINE_PAUSED_OR_BUSY:"Capture is paused or another writer is running.",COUNT_REQUIRES_NARROWER_QUERY:"The provider count exceeds the pilot bound. Choose a narrower query.",PROVIDER_COOLDOWN:"This provider needs a short pause before a new query.",PROVIDER_RATE_LIMIT:"The provider is limiting requests. Leave a pause before retrying.",CAPTURE_VALIDATION_HELD:"The stored response needs validation review; it is preserved in the receipt list.",PAYLOAD_REJECTED:"The provider returned an unexpected data format.",UPSTREAM_UNAVAILABLE:"The provider is unavailable for this query.",SOURCE_SCOPE_REJECTED:"Returned records did not match the selected Kansas scope."};
const cell=(value:unknown)=>value===null||value===undefined||value===""?"Missing":typeof value==="object"?JSON.stringify(value).slice(0,500):String(value).slice(0,500);
const defaults=(fields:Catalog["sources"][number]["fields"])=>Object.fromEntries(fields.map(f=>[f.key,f.default]));
const preferred:Record<string,string[]>={"water-quality-portal":["Activity_StartDate","Result_Characteristic","Result_Measure","Result_MeasureUnit","Result_ResultDetectionCondition","Result_MeasureQualifierCode","DetectionLimit_MeasureA","DetectionLimit_MeasureUnitA"],"nrcs-scan":["date","value","storedUnitCode","heightDepth","derivedData","qcFlag","qaFlag","origValue"],"census-acs":["NAME","B01003_001E","B01003_001M","B01003_001EA","B19013_001E","B19013_001M","B19013_001EA"],"iem-asos":["station","valid","tmpf","sknt","drct","metar"],"usdm-statistics":["mapDate","validStart","validEnd","none","d0","d1","d2","d3","d4"]};
// Check network values before they enter state: TypeScript annotations do not
// validate JSON, and a bad refresh must not replace a usable catalog/history.
const record=(value:unknown):value is Record<string,unknown>=>!!value&&typeof value==="object"&&!Array.isArray(value);
const strings=(value:unknown):value is string[]=>Array.isArray(value)&&value.every(item=>typeof item==="string");
const byteCount=(value:unknown):value is number=>typeof value==="number"&&Number.isSafeInteger(value)&&value>=0;
const queryRecord=(value:unknown):value is Record<string,string>=>record(value)&&Object.values(value).every(item=>typeof item==="string");
const setupStatus=(value:unknown)=>record(value)&&typeof value.configured==="boolean"&&strings(value.missing)&&strings(value.holds);
const stringLists=(value:unknown)=>record(value)&&Object.values(value).every(strings);
function catalogPayload(value:unknown):value is Catalog {
 if(!record(value)||typeof value.owner!=="boolean"||!record(value.host)||!Array.isArray(value.sources))return false;
 const host=value.host;
 if(typeof host.state!=="string"||typeof host.host!=="string"||typeof host.configured!=="boolean"||typeof host.paused!=="boolean"
  ||!(host.usedBytes===null||byteCount(host.usedBytes))||!byteCount(host.limitBytes)||(host.missing!==undefined&&!strings(host.missing)))return false;
 const ids=new Set<string>();
 return value.sources.every(source=>{
  if(!record(source)||typeof source.id!=="string"||!source.id||ids.has(source.id)||!setupStatus(source)||!byteCount(source.limitBytes)
   ||!["name","kind","state","docs","limitation","releaseState"].every(key=>typeof source[key]==="string")
   ||(source.rights!==undefined&&typeof source.rights!=="string")||!Array.isArray(source.fields))return false;
  ids.add(source.id);
  return source.fields.every(field=>record(field)&&["key","label","type","default"].every(key=>typeof field[key]==="string")
   &&(field.options===undefined||strings(field.options))
   &&[field.min,field.max].every(bound=>bound===undefined||(typeof bound==="number"&&Number.isFinite(bound))))
   &&(source.productStatuses===undefined||(record(source.productStatuses)&&Object.values(source.productStatuses).every(setupStatus)))
   &&(source.productSecrets===undefined||stringLists(source.productSecrets))
   &&(source.productConfirmations===undefined||stringLists(source.productConfirmations));
 });
}
function captureHistory(value:unknown):value is {captures:Receipt[]} {
 if(!record(value)||!Array.isArray(value.captures))return false;
 return value.captures.every(receipt=>record(receipt)&&["captureId","sourceId","retrievedAt","sha256","validation","limitation"].every(key=>typeof receipt[key]==="string")
  &&byteCount(receipt.byteLength)&&byteCount(receipt.entityBytes)&&typeof receipt.partial==="boolean"&&queryRecord(receipt.query)
  &&Array.isArray(receipt.entityHashes)&&receipt.entityHashes.every(entity=>record(entity)&&typeof entity.url==="string"&&typeof entity.sha256==="string"&&typeof entity.contentType==="string"&&byteCount(entity.byteLength)));
}
// Result identity is checked separately from payload shape: a valid result for
// another source/capture must not be presented as the owner's selected record.
function coordinates(value:unknown,depth:number):boolean {
 if(!Array.isArray(value))return false;
 if(depth>0)return value.every(part=>coordinates(part,depth-1));
 return value.length>=2&&value.every(part=>typeof part==="number"&&Number.isFinite(part))
  &&value[0]>=-180&&value[0]<=180&&value[1]>=-90&&value[1]<=90;
}
function capturedFeature(value:unknown):boolean {
 if(!record(value)||value.type!=="Feature"||!record(value.properties))return false;
 if(value.geometry===null)return true;
 const geometry=value.geometry;
 if(!record(geometry)||typeof geometry.type!=="string")return false;
 const depths:Record<string,number>={Point:0,MultiPoint:1,LineString:1,MultiLineString:2,Polygon:2,MultiPolygon:3};
 return Object.hasOwn(depths,geometry.type)&&coordinates(geometry.coordinates,depths[geometry.type]);
}
function capturedRaster(value:unknown):boolean {
 if(!record(value)||!Array.isArray(value.bbox)||value.bbox.length!==4||!value.bbox.every(n=>typeof n==="number"&&Number.isFinite(n)))return false;
 const [west,south,east,north]=value.bbox;
 return west>=-180&&east<=180&&west<east&&south>=-90&&north<=90&&south<north
  &&byteCount(value.width)&&value.width>0&&byteCount(value.height)&&value.height>0&&typeof value.vintage==="string"
  &&(value.acquiredAt===null||(typeof value.acquiredAt==="string"&&Number.isFinite(Date.parse(value.acquiredAt))));
}
function captureResult(value:unknown,sourceId:string,captureId?:string):value is Result {
 if(!record(value)||!record(value.view)||(value.cached!==undefined&&typeof value.cached!=="boolean"))return false;
 const history={captures:[value.receipt]};if(!captureHistory(history))return false;
 const receipt=history.captures[0],view=value.view;
 if(receipt.sourceId!==sourceId||view.sourceId!==sourceId||receipt.validation!=="structure-valid"
  ||!(/^[a-f0-9]{64}$/).test(receipt.captureId)||(captureId!==undefined&&receipt.captureId!==captureId)
  ||!Array.isArray(view.rows)||!view.rows.every(record)||!byteCount(view.total)||view.total<view.rows.length
  ||typeof view.partial!=="boolean"||view.partial!==receipt.partial||typeof view.limitation!=="string"||view.releaseState!=="unreleased"
  ||typeof view.retrievedAt!=="string"||!Number.isFinite(Date.parse(view.retrievedAt))||view.retrievedAt!==receipt.retrievedAt
  ||!queryRecord(view.query))return false;
 const query=view.query;
 return Object.keys(query).length===Object.keys(receipt.query).length&&Object.keys(query).every(key=>query[key]===receipt.query[key])
  &&(view.features===undefined||(Array.isArray(view.features)&&view.features.every(capturedFeature)))
  &&(view.raster===undefined||capturedRaster(view.raster));
}
type ProfileOutcome={sourceId:string}&({state:"quarantined"|"already-captured";captureId:string}|{state:"held";code:string});
type ProfileRun={state:"schedule-disabled"|"complete"|"partial";captured:number;outcomes:ProfileOutcome[]};
function profileRun(value:unknown):value is ProfileRun {
 if(!record(value)||!byteCount(value.captured)||!Array.isArray(value.outcomes))return false;
 if(value.state==="schedule-disabled")return value.captured===0&&value.outcomes.length===0;
 if(value.state!=="complete"&&value.state!=="partial")return false;
 // scheduledProfiles attempts one or two configured plans per run. A held or
 // previously saved capture must never be counted as a newly stored capture.
 if(value.outcomes.length<1||value.outcomes.length>2)return false;
 let stored=0,held=0;
 for(const outcome of value.outcomes){
  if(!record(outcome)||typeof outcome.sourceId!=="string"||!outcome.sourceId)return false;
  if(outcome.state==="held"){
   if(typeof outcome.code!=="string"||!outcome.code)return false;
   held++;
  }else if(outcome.state==="quarantined"||outcome.state==="already-captured"){
   if(typeof outcome.captureId!=="string"||!(/^[a-f0-9]{64}$/).test(outcome.captureId))return false;
   if(outcome.state==="quarantined")stored++;
  }else return false;
 }
 return value.captured===stored&&value.state===(held>0?"partial":"complete");
}
function profileRunMessage(value:ProfileRun):string {
 if(value.state==="schedule-disabled")return "Configured-profile capture is disabled.";
 const reused=value.outcomes.filter(outcome=>outcome.state==="already-captured").length;
 const held=value.outcomes.filter(outcome=>outcome.state==="held").length;
 return `${value.captured} configured-profile capture(s) stored${reused?`; ${reused} previously saved capture(s) reused`:""}${held?`; ${held} profile(s) held. Review source setup and saved captures before retrying`:""}. Review and release remain pending.`;
}
export default function ConnectionsWorkspace(){
 const [catalog,setCatalog]=useState<Catalog|null>(null),[selected,setSelected]=useState("noaa-ncei"),[query,setQuery]=useState<Record<string,string>>({});
 const [result,setResult]=useState<Result|null>(null),[receipts,setReceipts]=useState<Receipt[]>([]),[busy,setBusy]=useState(false),[message,setMessage]=useState(""),[page,setPage]=useState(0),[metric,setMetric]=useState("");
 const [statusBusy,setStatusBusy]=useState(true),[statusError,setStatusError]=useState("");
 const request=useRef<AbortController|null>(null);
 const statusRequest=useRef<AbortController|null>(null);
 const refresh=useCallback(async(signal?:AbortSignal)=>{
  if(signal?.aborted)return;
  statusRequest.current?.abort();
  const controller=new AbortController();statusRequest.current=controller;
  const cancel=()=>controller.abort();signal?.addEventListener("abort",cancel,{once:true});
  let timedOut=false;
  let cancelDeadline=()=>{};
  const deadline=new Promise<never>((_resolve,reject)=>{
   cancelDeadline=()=>reject(controller.signal.reason);
   controller.signal.addEventListener("abort",cancelDeadline,{once:true});
  });
  const timeout=setTimeout(()=>{timedOut=true;controller.abort();},15_000);
  setStatusBusy(true);setStatusError("");
  try{
   const load=async()=>{
   const response=await fetch("/api/connections",{cache:"no-store",signal:controller.signal});
   if(!response.ok)throw new Error("Source status unavailable.");
   const value:unknown=await response.json();if(controller.signal.aborted)return;
   if(!catalogPayload(value))throw new Error("Invalid source status response.");
   setCatalog(value);if(!value.owner){setReceipts([]);setResult(null);}
   setQuery(current=>Object.keys(current).length?current:defaults(value.sources.find(s=>s.id==="noaa-ncei")?.fields??[]));
   if(value.owner){
    const r=await fetch("/api/connections?action=captures",{cache:"no-store",signal:controller.signal});
    if(!r.ok)throw new Error("Capture history unavailable.");
    const v:unknown=await r.json();if(controller.signal.aborted)return;
    if(!captureHistory(v))throw new Error("Invalid capture history response.");
    setReceipts(v.captures);
   }
   };
   await Promise.race([load(),deadline]);
  }catch{if(statusRequest.current===controller&&(!controller.signal.aborted||timedOut))setStatusError(`${timedOut?"Source status took too long to respond.":"Source status is unavailable."} Retry when the host has recovered. Any earlier status below may be out of date.`);}
  finally{clearTimeout(timeout);signal?.removeEventListener("abort",cancel);controller.signal.removeEventListener("abort",cancelDeadline);if(statusRequest.current===controller&&(!controller.signal.aborted||timedOut))setStatusBusy(false);}
 },[]);
 useEffect(()=>{const controller=new AbortController();void Promise.resolve().then(()=>refresh(controller.signal));return()=>{controller.abort();statusRequest.current?.abort();statusRequest.current=null;request.current?.abort();};},[refresh]);
 const source=catalog?.sources.find(s=>s.id===selected);
 const choose=(id:string)=>{request.current?.abort();setBusy(false);setSelected(id);setQuery(defaults(catalog!.sources.find(s=>s.id===id)!.fields));setResult(null);setMessage("");setPage(0);setMetric("");};
 const inspect=async(receipt?:Receipt)=>{
  request.current?.abort();const controller=new AbortController();request.current=controller;setBusy(true);setMessage("");setResult(null);setMessage("");setPage(0);
  try{
   const response=await fetch(receipt?"/api/connections?action=view&id="+receipt.captureId:"/api/connections",receipt?{cache:"no-store",signal:controller.signal}:{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({sourceId:selected,query}),signal:controller.signal});
   const value:unknown=await response.json().catch(()=>null);if(controller.signal.aborted)return;
   if(!response.ok)throw new Error((record(value)&&typeof value.error==="string"?labels[value.error]:undefined)??"This request is held. Check configuration, dates and the source limitations.");
   if(!captureResult(value,receipt?.sourceId??selected,receipt?.captureId))throw new Error("Capture returned invalid data. Please retry.");
   if(receipt){setSelected(receipt.sourceId);setQuery(receipt.query);}
   setResult(value);setMetric((VALUE_COLUMNS[value.view.sourceId]??[]).find(key=>value.view.rows.some((r:Record<string,unknown>)=>r[key]!==undefined))??"");setMessage(value.cached?"Verified saved capture replayed.":"Stored bytes verified. Review and release remain pending.");void refresh();
  }catch(error){if(!controller.signal.aborted)setMessage(error instanceof Error?error.message:"Capture held.");}
  finally{if(!controller.signal.aborted)setBusy(false);}
 };
 const runProfiles=async()=>{
  request.current?.abort();const controller=new AbortController();request.current=controller;setBusy(true);setMessage("");setResult(null);
  try{
   const response=await fetch("/api/connections/run",{method:"POST",signal:controller.signal});
   const value:unknown=await response.json().catch(()=>null);if(controller.signal.aborted)return;
   if(!response.ok)throw new Error("Hosted capture profiles are not configured or enabled.");
   if(!profileRun(value))throw new Error("Profile capture returned invalid data. Review saved captures before retrying.");
   setMessage(profileRunMessage(value));void refresh();
  }catch(error){if(!controller.signal.aborted)setMessage(error instanceof Error?error.message:"Profile capture held.");}
  finally{if(!controller.signal.aborted)setBusy(false);}
 };
 const view=result?.view;
 const keys=view?.rows.length?Array.from(new Set(view.rows.slice(0,20).flatMap(row=>Object.keys(row)))):[];
 const columns=preferred[view?.sourceId??""]??keys.slice(0,8);
 const groups=view&&metric?series(view.sourceId,view.rows,metric):[];
 const rowPage=view?.rows.slice(page*25,(page+1)*25)??[];
 const readiness=source?.productStatuses?.[query.product]??source;
 const productKeys=source?.productSecrets?.[query.product]??[],productHolds=source?.productConfirmations?.[query.product]??[];
 return <main className="connections-workspace"><nav><Link href="/?layers=sources">← Explorer</Link><Link href="/daily-archive">Daily capture &amp; archive</Link><button onClick={()=>void refresh()} type="button" disabled={statusBusy} aria-busy={statusBusy}>{statusBusy?"Refreshing status…":statusError?"Retry source status":"Refresh status"}</button></nav>
  <header><p>Source connections</p><h1>Inspect the data behind Kansas</h1><p>15 additional connections and NOAA NCEI, with bounded capture, durable storage and verified replay. Captures stay private while rights, sensitivity and release review are pending.</p></header>
  {statusBusy&&<p role="status">{catalog?"Refreshing hosted source support…":"Checking hosted source support…"}</p>}
  {statusError&&<p role="alert">{statusError}</p>}
  {catalog&&<>
   <section className="connection-host" aria-label="Host archive status"><strong>{catalog.host.host}</strong><span>{catalog.host.state.replaceAll("-"," ")}</span><p>{catalog.host.usedBytes===null?"Stored bytes have not been verified.":catalog.host.usedBytes.toLocaleString()+" accounted bytes stored."} Archive limit: {catalog.host.limitBytes.toLocaleString()} bytes. {catalog.host.paused?"Capture is paused.":""}</p>{catalog.host.missing?.length? <p>Setup pending: {catalog.host.missing.join(", ")}.</p>:null}<p>{catalog.owner?"Owner access verified. Saved captures are available below.":"Source status is public. Owner sign-in is required to capture or inspect unreleased data."}</p></section>
   <p><button type="button" disabled={busy||!catalog.owner||!catalog.host.configured||catalog.host.paused} onClick={()=>void runProfiles()}>Capture configured profiles</button> Scheduled profiles are disabled until the host configuration is reviewed.</p>
   <div className="connection-layout"><aside aria-label="API connections">{catalog.sources.map(s=><button type="button" key={s.id} aria-pressed={selected===s.id} onClick={()=>choose(s.id)}><strong>{s.name}</strong><span>{s.kind}</span><small>{s.configured?"Adapter ready · review pending":"Credentials or provider review pending"}</small></button>)}</aside>
    <section aria-label="Selected source" className="connection-detail">{source&&<><h2>{source.name}</h2><p className="connection-boundary">{source.limitation}</p><p><a href={source.docs} target="_blank" rel="noreferrer">Provider documentation ↗</a> {source.rights?<a href={source.rights} target="_blank" rel="noreferrer">Rights and attribution ↗</a>:null}</p>
     <form onSubmit={e=>{e.preventDefault();void inspect();}}><div className="connection-fields">{source.fields.map(f=><label key={f.key}>{f.label}{f.options?<select value={query[f.key]??f.default} onChange={e=>{request.current?.abort();setBusy(false);setQuery({...query,[f.key]:e.target.value});setResult(null);setMessage("");}}>{f.options.map(value=><option key={value}>{value}</option>)}</select>:<input required type={f.type==="number"?"number":"date"} step={f.type==="number"?"any":undefined} min={f.min} max={f.max} value={query[f.key]??f.default} onChange={e=>{request.current?.abort();setBusy(false);setQuery({...query,[f.key]:e.target.value});setResult(null);setMessage("");}}/>}</label>)}</div>
      {selected==="noaa-ncei"&&query.product?.startsWith("normals-")?<p>Normals retain their 1991–2020 baseline. Monthly and annual normals ignore the date range; daily normals use a calendar date within one year.</p>:null}
      {selected==="air-quality"?<p>{query.product==="airnow"?"AirNow uses current reporting-area observations; the AQS year/county controls do not apply.":"AQS uses the selected Kansas county in January of the selected year; pointer coordinates do not apply."} {productKeys.length?"A server-side provider key is required.":""}{productHolds.length?" Provider archive authorization is also required.":""}</p>:null}
      <p>Entity limit: {source.limitBytes.toLocaleString()} bytes per response. Metadata and original responses are packaged together for replay; the archive accounts for both.</p>
      <button type="submit" disabled={busy||!catalog.owner||!catalog.host.configured||catalog.host.paused}>{busy?"Capturing and verifying…":"Capture selected query"}</button>
     </form>
     {readiness?.missing.length||readiness?.holds.length?<details><summary>Provider setup and review requirements</summary><p>Enter keys only in the host’s server secrets. Do not paste them into this page or a report.</p><ul>{(readiness?.missing??[]).map(k=><li key={k}>Server credential: {k}</li>)}{(readiness?.holds??[]).map(k=><li key={k}>Recorded provider approval: {k}</li>)}</ul></details>:null}
    </>}
    <p role="status" aria-live="polite">{message}</p>
    {view&&result?<section className="connection-result" aria-label="Verified capture"><h2>{view.raster?"Captured source imagery":view.total.toLocaleString()+" source records"} {view.partial?"· partial response":!view.raster&&view.total===0?"· empty response":""}</h2><p>Retrieved {view.retrievedAt}. Requested support: {JSON.stringify(view.query)}. Unreleased external context; owner review only.</p>
     <p><a href={"/api/connections?action=bundle&id="+result.receipt.captureId}>Download stored response bundle</a> · <a href={"/api/connections?action=entity&id="+result.receipt.captureId}>Download final source entity</a></p>
     {view.features?.length||view.raster?<ConnectionMap view={view} receipt={result.receipt}/>:null}
     {view.rows.length>0?<><div className="connection-table" tabIndex={0}><table><thead><tr>{columns.map(key=><th key={key}>{key}</th>)}</tr></thead><tbody>{rowPage.map((row,i)=><tr key={page*25+i}>{columns.map(key=><td key={key}>{cell(row[key])}</td>)}</tr>)}</tbody></table></div><div className="connection-pagination"><button disabled={page===0} onClick={()=>setPage(page-1)}>Previous records</button><span>{page*25+1}–{Math.min((page+1)*25,view.rows.length)} of {view.rows.length} review rows</span><button disabled={(page+1)*25>=view.rows.length} onClick={()=>setPage(page+1)}>Next records</button></div><details><summary>All fields in these records</summary>{rowPage.map((row,i)=><pre key={i}>{JSON.stringify(row,null,2)}</pre>)}</details></>:<p>{view.raster?"This product returned imagery without tabular observations. Pixel acquisition time and accuracy remain source-specific.":"No source observations returned. Empty coverage does not establish absence or safe conditions."}</p>}
     {(VALUE_COLUMNS[view.sourceId]??[]).some(k=>keys.includes(k))?<label className="connection-metric">Native value preview<select value={metric} onChange={e=>setMetric(e.target.value)}>{(VALUE_COLUMNS[view.sourceId]??[]).filter(k=>keys.includes(k)).map(k=><option key={k}>{k}</option>)}</select></label>:null}
     {groups.slice(0,6).map(group=>{const values=group.points.map(p=>p.value),lo=Math.min(...values),hi=Math.max(...values),range=hi-lo||1;return <figure className="connection-series" key={group.label}><figcaption>{metric} · {group.label}. Native values only; suppressed, missing and unverified sensor values omitted.</figcaption><svg viewBox="0 0 700 220" role="img" aria-label={metric+" in "+group.label}><text x="2" y="16">{hi}</text><text x="2" y="209">{lo}</text>{group.points.slice(0,1000).map((p,i)=><circle key={i} cx={50+i/Math.max(1,group.points.length-1)*630} cy={200-(p.value-lo)/range*180} r="3"><title>{p.label+": "+p.native+" "+group.label}</title></circle>)}</svg><p>Records in provider order. Horizontal spacing does not represent elapsed time or continuous support; no interpolation.</p></figure>;})}
     <details><summary>Provenance and integrity receipt</summary><pre>{JSON.stringify(result.receipt,null,2)}</pre></details>
    </section>:null}
   </section></div>
   {catalog.owner?<section className="connection-history"><h2>Saved API captures</h2><p>Recent API receipts from the host’s bounded history. Each replay checks exact stored identity and hashes. Invalid captures can be downloaded for correction.</p>{receipts.length?<ul>{receipts.map(r=><li key={r.captureId}><strong>{catalog.sources.find(s=>s.id===r.sourceId)?.name??r.sourceId}</strong><span>{r.retrievedAt} · {r.validation}{r.partial?" · partial":""}</span><button disabled={busy||r.validation!=="structure-valid"} onClick={()=>void inspect(r)}>Replay capture</button><a href={"/api/connections?action=bundle&id="+r.captureId}>Stored bundle</a></li>)}</ul>:<p>No saved API captures verified.</p>}</section>:null}
  </>}
 </main>;
}
