"use client";
import { useEffect, useMemo, useState } from "react";
import type { GeoJSONSource, Map as MapLibreMap, MapMouseEvent } from "./maplibre-seam";
import type { AreaBounds, Borehole } from "./subsurface-model";
import { RESOURCE_SOURCES, type ResourceKind, type ResourceLocation } from "./underground-resources-model";
import { readBoundedJson } from "./bounded-json";
import s from "./subsurface.module.css";
type Result={key:string;rows:ResourceLocation[];partial:boolean;rejected:number;retrievedAt:string};
export default function UndergroundResources({map,bounds,revision,active,redacted,water,onInspect}:{map:MapLibreMap|null;bounds:AreaBounds|null;revision:number;active:boolean;redacted:boolean;water:Borehole[];onInspect:(r:Borehole)=>void}){
  const [open,setOpen]=useState(false),[kind,setKind]=useState<ResourceKind|"water">("oilgas"),[result,setResult]=useState<Result|null>(null),[failure,setFailure]=useState<{key:string;message:string}|null>(null),[retry,setRetry]=useState(0),[selected,setSelected]=useState("");
  const key=JSON.stringify([bounds,revision,kind,retry]);
  const enabled=open&&active&&!redacted&&!!bounds;
  const current=result?.key===key?result:null;
  const rows=useMemo(()=>current?.rows??[],[current]);
  const selectedRow=rows.find(r=>r.id===selected);
  useEffect(()=>{
    if(!enabled||kind==="water"||!bounds)return;
    const controller=new AbortController();
    (async()=>{try{
      const response=await fetch(`/api/subsurface/resources?${new URLSearchParams({kind,bounds:bounds.join(",")})}`,{signal:controller.signal});
      if(!response.ok)throw new Error("Resource source is unavailable. Try again.");
      const v=await readBoundedJson(response,1_000_000,controller.signal) as Omit<Result,"key">;
      if(!Array.isArray(v.rows)||v.rows.length>200||typeof v.partial!=="boolean"||typeof v.retrievedAt!=="string")throw new Error("Unrecognized source response.");
      if(!controller.signal.aborted)setResult({...v,key});
    }catch(e){if(!controller.signal.aborted)setFailure({key,message:e instanceof Error?e.message:"Resource source unavailable."});}})();
    return()=>controller.abort();
  },[enabled,key,kind,bounds]);
  useEffect(()=>{
    if(!map||!enabled||kind==="water")return;
    const source="kfm-underground-resource-locations",layer=source+"-points";
    const draw=()=>{
      if(!map.isStyleLoaded())return;
      const data={type:"FeatureCollection" as const,features:rows.map(r=>({type:"Feature" as const,geometry:{type:"Point" as const,coordinates:r.coordinates},properties:{id:r.id,selected:r.id===selected}}))};
      if(!map.getSource(source))map.addSource(source,{type:"geojson",data});else(map.getSource(source) as GeoJSONSource).setData(data);
      if(!map.getLayer(layer))map.addLayer({id:layer,type:"circle",source,paint:{"circle-radius":["case",["get","selected"],8,5],"circle-color":kind==="oilgas"?"#e8aa60":"#c299db","circle-stroke-color":"#102126","circle-stroke-width":2}});
    };
    const click=(e:MapMouseEvent)=>{if(!map.getLayer(layer))return;const f=map.queryRenderedFeatures(e.point,{layers:[layer]})[0];if(f?.properties?.id)setSelected(String(f.properties.id));};
    draw();map.on("styledata",draw);map.on("click",click);
    return()=>{map.off("styledata",draw);map.off("click",click);try{if(map.getLayer(layer))map.removeLayer(layer);if(map.getSource(source))map.removeSource(source);}catch{}};
  },[map,enabled,kind,rows,selected]);
  const source=kind==="water"?null:RESOURCE_SOURCES[kind];
  return <details className={s.resourcePanel} onToggle={e=>setOpen(e.currentTarget.open)}><summary>Water, oil, gas &amp; minerals</summary>
    {!bounds?<p>Show an area to find its resource locations.</p>:redacted?<p>Location details are hidden in this view.</p>:<>
      <label>Resource <select aria-label="Underground resource type" value={kind} onChange={e=>{setKind(e.target.value as ResourceKind|"water");setSelected("");}}><option value="oilgas">Oil &amp; gas wells</option><option value="minerals">Mines &amp; minerals</option><option value="water">Water well logs</option></select></label>
      {kind==="water"?<><p>{water.length} loaded well logs at the selected record time. Open a record for its water-use, depth and interval descriptions.</p><div className={s.resourceList}>{water.map(r=><button type="button" key={r.id} onClick={()=>onInspect(r)}>{r.name}</button>)}</div></>:<>
        {!current&&failure?.key!==key?<p role="status">Loading source locations…</p>:failure?.key===key&&!current?<p role="status">{failure.message} <button type="button" onClick={()=>setRetry(v=>v+1)}>Retry</button></p>:<p role="status">{rows.length} locations{current?.partial?" · first 200, zoom in for more detail":""}{current?.rejected?` · ${current.rejected} invalid or duplicate records withheld`:""}. {rows.length===0?"No records returned for this area; absence is not proof that no resource exists.":"Select a point or record."}</p>}
        <div className={s.resourceList}>{rows.map(r=><button type="button" key={r.id} aria-pressed={r.id===selected} onClick={()=>setSelected(r.id)}><strong>{r.name}</strong><small>{r.material} · recorded {r.status}</small></button>)}</div>
        {selectedRow&&<div className={s.resourceDetail}><strong>{selectedRow.name}</strong><p>{selectedRow.coordinates[1].toFixed(5)}° N, {Math.abs(selectedRow.coordinates[0]).toFixed(5)}° W · source position</p><dl>{selectedRow.details.map(([k,v])=><div key={k}><dt>{k}</dt><dd>{v}</dd></div>)}</dl></div>}
        <p className={s.muted}>{source?.limitation} These locations do not change with the well-log time slider.</p><a href={source?.link} target="_blank" rel="noreferrer">KGS source &amp; methods ↗</a>{current&&<small> Retrieved {new Date(current.retrievedAt).toLocaleDateString()}</small>}
      </>}
    </>}
  </details>;
}
