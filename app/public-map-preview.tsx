"use client";
import { useEffect, useRef, useState } from "react";
import { loadMapLibre, type Map as MapLibreMap, type GeoJSONSource } from "./maplibre-seam";
import { readBoundedJson } from "./bounded-json";
import type { PublicMapRecord } from "./public-map-catalog";
import { parsePublicPreview, PREVIEW_SOURCES, validPreviewBounds, type PublicPreview, type PreviewFeature, type PublicPreviewKind } from "./public-map-preview-model";

/** Opt-in, unsaved context viewer. It never installs a candidate into governed layers. */
export function PublicMapPreview({record}:{record:PublicMapRecord|null}) {
  const kind:PublicPreviewKind|null=(Object.keys(PREVIEW_SOURCES) as PublicPreviewKind[]).find(key=>record?.assets.some(a=>a.kind==="service" && a.url===PREVIEW_SOURCES[key].url))??(record?.publisher==="OSMRE"?"osmre-nmmr":null);
  const [opened,setOpened]=useState(false),[ready,setReady]=useState(false),[busy,setBusy]=useState(false),[message,setMessage]=useState("");
  const [data,setData]=useState<PublicPreview|null>(null),[selected,setSelected]=useState<PreviewFeature|null>(null);
  const container=useRef<HTMLDivElement|null>(null),map=useRef<MapLibreMap|null>(null),pending=useRef<AbortController|null>(null),latest=useRef<PublicPreview|null>(null);
  // A new record resets the viewer during render; the effect only aborts the old record's work.
  const [recordId,setRecordId]=useState(record?.id);
  if (recordId!==record?.id) { setRecordId(record?.id);setOpened(false);setData(null);setSelected(null);setMessage("");setBusy(false); }
  useEffect(()=>{pending.current?.abort();pending.current=null;},[record?.id]);
  useEffect(()=>{
    if (!opened || !container.current || !kind) return;
    let disposed=false;
    void loadMapLibre().then(runtime=>{
      if(disposed || !container.current)return;
      runtime.setWorkerUrl("/maplibre/maplibre-gl-worker.mjs");
      const m=new runtime.Map({container:container.current,style:{version:8,sources:{topo:{type:"raster",tiles:["https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}"],tileSize:256,attribution:"USGS The National Map"}},layers:[{id:"topo",type:"raster",source:"topo"}]},center:record?.point??[-94.9,37.5],zoom:10,minZoom:7,maxZoom:15,attributionControl:{compact:true}});
      map.current=m;m.addControl(new runtime.NavigationControl({showCompass:false}),"top-right");
      m.on("load",()=>{if(disposed)return;m.addSource("public-map-preview",{type:"geojson",data:{type:"FeatureCollection",features:[]},attribution:PREVIEW_SOURCES[kind].attribution});
        m.addLayer({id:"public-map-polygons",type:"fill",source:"public-map-preview",filter:["==","$type","Polygon"],paint:{"fill-color":"#ba7a32","fill-opacity":.3,"fill-outline-color":"#684019"}});
        m.addLayer({id:"public-map-points",type:"circle",source:"public-map-preview",filter:["==","$type","Point"],paint:{"circle-radius":7,"circle-color":"#155e75","circle-stroke-color":"#fff","circle-stroke-width":2}});
        setReady(true);
      });
      m.on("click",e=>{if(!m.getLayer("public-map-polygons")||!m.getLayer("public-map-points"))return;const features=m.queryRenderedFeatures(e.point,{layers:["public-map-polygons","public-map-points"]});if(features[0])setSelected(latest.current?.features.find(f=>f.id===String(features[0].id))??null);});
      m.on("error",()=>{if(!disposed)setMessage("A map resource is unavailable. Source records remain available below when loaded.");});
    }).catch(()=>{if(!disposed)setMessage("WebGL map preview is unavailable on this device.");});
    return()=>{disposed=true;pending.current?.abort();pending.current=null;map.current?.remove();map.current=null;setReady(false);setBusy(false);setData(null);setSelected(null);latest.current=null;};
  },[opened,kind,record?.id,record?.point]);
  const load=async()=>{
    const m=map.current;if(!m||!kind)return;
    const b=m.getBounds(), bounds=[b.getWest(),b.getSouth(),b.getEast(),b.getNorth()];
    if(!validPreviewBounds(bounds)){setMessage("Zoom in to an area within Kansas, at most 0.6 degrees across, then load this area.");return;}
    pending.current?.abort();const request=new AbortController();pending.current=request;setBusy(true);setMessage("");setData(null);setSelected(null);latest.current=null;
    (m.getSource("public-map-preview") as GeoJSONSource)?.setData({type:"FeatureCollection",features:[]});
    try{
      const response=await fetch(`/api/public-maps/preview?${new URLSearchParams({kind,bounds:bounds.join(",")})}`,{signal:request.signal});
      const body=await readBoundedJson(response,4_100_000,request.signal);if(!response.ok)throw new Error("The source is unavailable. No coverage or absence is inferred.");
      const result=parsePublicPreview(body,kind,bounds);const partial=(body as {partial?:boolean}).partial===true;result.partial ||=partial;
      if(request.signal.aborted)return;setData(result);latest.current=result;
      (m.getSource("public-map-preview") as GeoJSONSource).setData(result as Parameters<GeoJSONSource["setData"]>[0]);
      setMessage(`${result.features.length} source features in this area${result.partial?" · partial response":""}. Preview only; not admitted or saved.`);
    }catch(error){if(!request.signal.aborted)setMessage(error instanceof Error?error.message:"Preview unavailable.");}
    finally{if(!request.signal.aborted)setBusy(false);}
  };
  if(!record)return null;
  if(!kind)return <p>Open the original document or GIS release above. A georeferenced preview has not been verified for this record.</p>;
  return <section aria-label="Source map preview">
    <p>{PREVIEW_SOURCES[kind].limitation}</p>
    <button type="button" onClick={()=>setOpened(!opened)}>{opened?"Close map preview":"Open source map preview"}</button>
    {opened&&<><div ref={container} style={{height:360,width:"100%",marginTop:12,border:"1px solid #b3bfc3",borderRadius:8}} aria-label="Interactive source map" />
      <p>Pan and zoom to a Kansas area, then load its records. {kind!=="osmre-nmmr"?"Amber areas: interpreted map units; select one for its source description.":"Blue points: mine-map index locations; select one for its source document information."}</p>
      <button type="button" disabled={!ready||busy} onClick={()=>void load()}>{busy?"Loading source records…":"Load this map area"}</button>
      {busy&&<button type="button" onClick={()=>{pending.current?.abort();setBusy(false);setMessage("Preview cancelled.");}}>Cancel preview</button>}
      <p role="status">{message}</p>
      {!!data?.features.length&&<label>Inspect source feature <select value={selected?.id??""} onChange={e=>setSelected(data.features.find(f=>f.id===e.target.value)??null)}><option value="">Choose a feature</option>{data.features.map(f=><option key={f.id} value={f.id}>{String(f.properties.Name??f.properties.names??f.properties.MapUnit??f.id)} · {f.id}</option>)}</select></label>}
      {selected&&<dl>{Object.entries(selected.properties).filter(([,v])=>v!==null&&v!=="").map(([key,value])=><div key={key}><dt>{key}</dt><dd style={{overflowWrap:"anywhere"}}>{String(value)}</dd></div>)}</dl>}
    </>}
  </section>;
}
