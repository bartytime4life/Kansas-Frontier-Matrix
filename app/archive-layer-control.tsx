'use client';
import { useEffect, useLayoutEffect, useRef, useState, type RefObject } from 'react';
import type { Map as MapLibreMap, MapLayerMouseEvent } from './maplibre-seam';
import type { Geometry } from 'geojson';
import { ARCHIVE_LAYERS, type ArchiveLayer } from './archive-layer-catalog';
import { archiveArea, archiveDetails, archiveFeatures, archiveQuery, countyShapes, fetchArchive, rowKey, rowLabel, textValue, type ArchiveAnswer } from './archive-layer-data';
import styles from './archive-layer-control.module.css';
import { defaultArchiveView, type ArchiveView, type ArchiveViews } from './archive-layer-view';

type Loaded = { answer: ArchiveAnswer; shapes: Map<string,Geometry>; scope: string; query: Record<string,string> };
type Props = { mapRef: RefObject<MapLibreMap | null>; styleReady: boolean; selected: readonly string[]; shown: ReadonlySet<string>; onChange: (ids: string[]) => void; onInspect: (id: string) => void; pickingEnabled: () => boolean; views: ArchiveViews; onView: (id: string, view: ArchiveView) => void };
const stamp = (value: unknown) => typeof value === 'string' && Number.isFinite(Date.parse(value)) ? new Date(value).toLocaleString() : 'not supplied';

export function ArchiveLayerControl(props: Props) {
  return <>{ARCHIVE_LAYERS.map(layer => <ArchiveLayerRow key={layer.id} {...props} layer={layer}/>)}</>;
}
function ArchiveLayerRow({layer,mapRef,styleReady,selected,shown,onChange,onInspect,pickingEnabled,views,onView}: Props & {layer: ArchiveLayer}) {
  const enabled=selected.includes(layer.id);
  const [loaded,setLoaded]=useState<Loaded|null>(null),[status,setStatus]=useState('Not selected'),[loading,setLoading]=useState(false);
  const [rendered,setRendered]=useState(false),[expanded,setExpanded]=useState(false),[picked,setPicked]=useState<string|null>(null);
  const [month,setMonth]=useState(()=>defaultArchiveView().month),[variable,setVariable]=useState('ppt');
  const [from,setFrom]=useState(()=>`${new Date().getUTCFullYear()}-01-01`),[to,setTo]=useState(()=>new Date().toISOString().slice(0,10));
  const [detail,setDetail]=useState<{title:string; dataset:string; query:Record<string,string>; answer:ArchiveAnswer}|null>(null),[detailStatus,setDetailStatus]=useState('');
  const request=useRef<AbortController|null>(null),detailRequest=useRef<AbortController|null>(null);
  const sequence=useRef(0),enableRef=useRef(enabled),pickRef=useRef({onInspect,pickingEnabled});
  useLayoutEffect(()=>{enableRef.current=enabled;pickRef.current={onInspect,pickingEnabled};},[enabled,onInspect,pickingEnabled]);
  const prepared=loaded?archiveFeatures(layer,loaded.answer.rows,loaded.shapes):null;
  const pickedRow=loaded?.answer.rows.find((row,index)=>rowKey(row,index)===picked);
  const sourceId=`kfm-${layer.id}`,layerIds=[`${sourceId}-fill`,`${sourceId}-line`,`${sourceId}-point`];

  async function load(more=false, restored?: ArchiveView) {
    request.current?.abort(); const controller=new AbortController();request.current=controller;
    const generation=++sequence.current;setLoading(true);if(!more)setRendered(false);setStatus('Loading archive…');setDetail(null);setDetailStatus('');
    detailRequest.current?.abort();
    const previous=more?loaded:null;
    if (!more) {setLoaded(null);setPicked(null);}
    const timer=setTimeout(()=>controller.abort(),90000);
    try {
      const map=mapRef.current;if(!map)throw new Error('Wait for the map before loading a layer.');
      const center=map.getCenter();
      const local=['tiger','stations','reaches'].includes(layer.kind);
      const applied=restored??{month,variable,from,to,area:''};
      const area=local?(applied.area||archiveArea([center.lng,center.lat])):'';
      const query=previous?{...previous.query,...(layer.kind==='recovered'?{after:previous.answer.nextCursor!}:{offset:String(previous.answer.rows.length)})}:archiveQuery(layer,area,applied.month,applied.variable);
      if(layer.kind==='storms'&&!previous) {query.from=applied.from;query.to=applied.to;}
      const answer=await fetchArchive(layer.dataset,query,controller.signal);
      const shapes=layer.kind==='prism'&&answer.count?await countyShapes(controller.signal):new Map<string,Geometry>();
      controller.signal.throwIfAborted();
      if(generation!==sequence.current||!enableRef.current)return;
      const rows=previous?[...previous.answer.rows,...answer.rows]:answer.rows;
      if(rows.length>1000)throw new Error('The display limit is 1,000 records. Narrow the area or date range.');
      setRendered(false);
      setLoaded({answer:{...answer,rows,count:rows.length},shapes,query:previous?.query??query,
        scope:previous?.scope??(local?`1° square around ${(Number(area.split(',')[1])+.5).toFixed(2)}°N, ${Math.abs(Number(area.split(',')[0])+.5).toFixed(2)}°W. Pan and reload to explore another area.`:layer.kind==='prism'?`${applied.month} · ${applied.variable} · 4 km model grid, county summaries`:layer.kind==='storms'?`${applied.from} through ${applied.to} · reported local source times`:'Retained Kansas archive; each record keeps its own dates.')});
      if(!previous)onView(layer.id,{...applied,area});
      setStatus(answer.count?'Data received': 'No records for this selection. Try another area or date.');
    } catch(error) {
      if(generation!==sequence.current||!enableRef.current)return;
      if(!previous)setLoaded(null);setStatus(controller.signal.aborted?'Archive request timed out. Retry when the PC is available.':error instanceof Error?error.message:'Archive unavailable.');
    } finally {clearTimeout(timer);if(generation===sequence.current)setLoading(false);}
  }
  useEffect(()=>{
    const epoch=sequence;
    const timer=setTimeout(()=>{
      if(enabled) {
        setExpanded(true);
        if(!loaded&&styleReady){
          const saved=views[layer.id];
          if(saved){setMonth(saved.month);setVariable(saved.variable);setFrom(saved.from);setTo(saved.to);}
          void load(false,saved);
        }
      }
      else {++epoch.current;request.current?.abort();detailRequest.current?.abort();setLoaded(null);setPicked(null);setDetail(null);setLoading(false);setRendered(false);setStatus('Not selected');}
    },0);
    return ()=>{clearTimeout(timer);++epoch.current;request.current?.abort();detailRequest.current?.abort();};
    // Selection owns acquisition. Initial acquisition waits for a ready map; style changes redraw retained data.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  },[enabled,styleReady]);
  useEffect(()=>{
    const map=mapRef.current;
    if(!enabled||!loaded||!prepared||!styleReady||!map)return;
    let disposed=false;
    const data=prepared.collection;
    const values=data.features.map(f=>f.properties.value).filter((v):v is number=>typeof v==='number');
    const lo=values.length?Math.min(...values):0,hi=values.length?Math.max(...values):0;
    const color=layer.kind==='prism'&&hi>lo?['interpolate',['linear'],['get','value'],lo,'#b9dfe7',hi,'#594d91']:layer.color;
    const cleanup=()=>{for(const id of [...layerIds].reverse())if(map.getLayer(id))map.removeLayer(id);if(map.getSource(sourceId))map.removeSource(sourceId);};
    const pick=(event:MapLayerMouseEvent)=>{
      if(!pickRef.current.pickingEnabled())return;
      const top=map.queryRenderedFeatures(event.point)[0];
      if(top?.source!==sourceId||top.layer.id!==event.features?.[0]?.layer.id)return;
      const key=event.features?.[0]?.properties?.key;
      if(typeof key==='string'){setPicked(key);setExpanded(true);setDetail(null);setDetailStatus('');pickRef.current.onInspect(layer.id);}
    };
    try {
      cleanup();
      const beforePoints=map.getStyle().layers.find(item=>item.id.startsWith('kfm-archive-')&&item.type==='circle')?.id;
      map.addSource(sourceId,{type:'geojson',data,attribution:`${layer.provider} · archive/reference · independent source dates`});
      map.addLayer({id:layerIds[0],type:'fill',source:sourceId,filter:['==',['geometry-type'],'Polygon'],paint:{'fill-color':color as never,'fill-opacity':layer.kind==='prism'?['case',['==',['get','value'],null],0,.55]:.12}},beforePoints);
      map.addLayer({id:layerIds[1],type:'line',source:sourceId,filter:['!=',['geometry-type'],'Point'],paint:{'line-color':layer.color,'line-width':1.5,'line-opacity':.85}},beforePoints);
      map.addLayer({id:layerIds[2],type:'circle',source:sourceId,filter:['==',['geometry-type'],'Point'],paint:{'circle-color':layer.color,'circle-radius':5,'circle-stroke-color':'#102734','circle-stroke-width':1.5}});
      for(const id of layerIds)map.on('click',id,pick);
      const frame=()=>{if(!disposed)setRendered(true);};map.once('idle',frame);map.triggerRepaint();
      return ()=>{disposed=true;map.off('idle',frame);for(const id of layerIds)map.off('click',id,pick);try{cleanup();}catch{/* Style replacement may already have removed this source. */}};
    } catch {
      try{cleanup();}catch{}
      const timer=setTimeout(()=>{setRendered(false);setStatus('The map could not draw these records. The record list remains available.');},0);
      return ()=>clearTimeout(timer);
    }
    // The answer is immutable until a request or selection changes.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  },[enabled,loaded,styleReady,mapRef,layer.id]);
  async function inspect(title:string,dataset:string,query:Record<string,string>){
    detailRequest.current?.abort();const controller=new AbortController();detailRequest.current=controller;setDetail(null);setDetailStatus('Loading records…');
    const timer=setTimeout(()=>controller.abort(),25000);
    try{const answer=await fetchArchive(dataset,query,controller.signal);if(!controller.signal.aborted&&enableRef.current){if(loaded)onView(layer.id,{month,variable,from,to,area:loaded.query.bbox??''});setDetail({title,dataset,query,answer});setDetailStatus(answer.count?'':'No readings in this date range.');}}
    catch{if(detailRequest.current===controller&&!controller.signal.aborted&&enableRef.current)setDetailStatus('Readings unavailable. Check the date range or retry.');}
    finally{clearTimeout(timer);}
  }
  const stale=loaded?.answer.cache?.state==='stale';
  const valueFeatures=prepared?.collection.features.filter(f=>f.properties.value!==null)??[];
  return <article className={`official-context-row ${styles.row}`} hidden={!shown.has(layer.id)} data-archive-layer={layer.id}>
    <div className="official-context-primary"><label className="visibility-switch"><input type="checkbox" aria-label={`${enabled?'Hide':'Show'} ${layer.title}`} checked={enabled} onChange={event=>onChange(event.target.checked?[...selected,layer.id]:selected.filter(id=>id!==layer.id))}/><span aria-hidden="true"/></label><i style={{'--swatch':layer.color} as React.CSSProperties}/><div><strong>{layer.title}</strong><small>{!enabled?'Not selected':loading?'Loading':loaded?`${!prepared?.collection.features.length?'No mappable features':rendered&&styleReady?'Displayed':'Preparing map'} · ${prepared?.collection.features.length??0} features${stale?' · cached, PC unavailable':''}`:status}</small></div></div>
    <details open={expanded} onToggle={event=>setExpanded(event.currentTarget.open)} className="specialty-layer-details"><summary>Archive data &amp; source details</summary><div className={`official-context-option-body ${styles.body}`}>
      <p>{layer.note}</p><small>Shared views restore the applied archive query and reload its first page. Source revisions may change the returned records.</small><a href={layer.sourceUrl} target="_blank" rel="noreferrer">{layer.provider} source documentation ↗</a>
      {layer.kind==='prism'&&<div className={styles.form}><label>Month<input type="month" value={month} onInput={event=>setMonth(event.currentTarget.value)}/></label><label>Climate measure<select value={variable} onChange={event=>setVariable(event.target.value)}>{[['ppt','Precipitation'],['tmax','Maximum temperature'],['tmin','Minimum temperature'],['tmean','Mean temperature'],['tdmean','Dew point'],['vpdmin','Minimum vapor-pressure deficit'],['vpdmax','Maximum vapor-pressure deficit'],['soltotal','Solar irradiance · horizontal'],['solslope','Solar irradiance · terrain slope']].map(([id,label])=><option key={id} value={id}>{label}</option>)}</select></label></div>}
      {['storms','stations','wind','water'].includes(layer.kind)&&<div className={styles.form}><label>From<input type="date" value={from} onInput={event=>{detailRequest.current?.abort();setDetail(null);setDetailStatus('');setFrom(event.currentTarget.value);}}/></label><label>Through<input type="date" value={to} onInput={event=>{detailRequest.current?.abort();setDetail(null);setDetailStatus('');setTo(event.currentTarget.value);}}/></label></div>}
      {enabled&&<button type="button" disabled={loading||!styleReady} onClick={()=>void load()}>{loading?'Loading…':['tiger','stations','reaches'].includes(layer.kind)?'Load around map centre':'Load selected data'}</button>}
      {enabled&&<p role="status">{status}</p>}
      {loaded&&<>
        <p><strong>{loaded.scope}</strong></p><p>{loaded.answer.rows.length}{loaded.answer.total===null?' records loaded; this is a page of the archive':` of ${loaded.answer.total} matching records loaded`}. {prepared?.unlocated||0} lack usable geometry; {prepared?.duplicate||0} duplicate identifiers omitted. {layer.kind==='prism'&&`${prepared?.missingValues||0} counties have no valid numeric fill.`}</p>
        <small>Archive response: {stamp(loaded.answer.generatedAt)}. This is delivery time, not observation time. Cache: {loaded.answer.cache?.state??'not supplied'}.</small>
        {stale&&<p className={styles.notice}>Cached response: the PC could not refresh this query. Treat the retained source dates as authoritative.</p>}
        {valueFeatures.length>0&&<p className={styles.legend}><span style={{background:'#b9dfe7'}}/>{Math.min(...valueFeatures.map(f=>f.properties.value!)).toFixed(2)} → <span style={{background:'#594d91'}}/>{Math.max(...valueFeatures.map(f=>f.properties.value!)).toFixed(2)} {valueFeatures[0].properties.unit} · county mean; unfilled means missing</p>}
        {(loaded.answer.hasMore||loaded.answer.total!==null&&loaded.answer.rows.length<loaded.answer.total)&&loaded.answer.rows.length<1000&&layer.kind!=='prism'&&<button type="button" disabled={loading} onClick={()=>void load(true)}>Load next page</button>}
        {layer.kind==='recovered'&&<a href={`/data-library?collection=${layer.reference}`}>Browse every record page in this collection →</a>}
        <label>Inspect a loaded record<select value={picked??''} onChange={event=>{detailRequest.current?.abort();setPicked(event.target.value||null);setDetail(null);setDetailStatus('');}}><option value="">Choose a record…</option>{loaded.answer.rows.map((row,index)=><option key={`${rowKey(row,index)}-${index}`} value={rowKey(row,index)}>{rowLabel(row,index)}</option>)}</select></label>
        {prepared?.unlocated? <details><summary>Records without map geometry</summary><p>These records remain available in the selector. No county centroid or inferred position is substituted.</p></details>:null}
      </>}
      {pickedRow&&<section className={styles.record}><h4>{rowLabel(pickedRow,0)}</h4><dl>{Object.entries(layer.kind==='recovered'?{...(pickedRow.values as Record<string,unknown>),provenance:pickedRow.provenance}:pickedRow).filter(([key])=>!['geometry','geometry_geojson'].includes(key)).map(([key,value])=><div key={key}><dt>{key}</dt><dd>{textValue(value)}</dd></div>)}</dl>
        {archiveDetails(layer,pickedRow,from,to).map(item=><button type="button" key={item.dataset} onClick={()=>void inspect(item.title,item.dataset,item.query)}>{item.title}</button>)}
      </section>}
      {detailStatus&&<p role="status">{detailStatus}</p>}
      {detail&&<section className={styles.record}><h4>{detail.title}</h4><p>{detail.answer.count ? `Rows ${Number(detail.query.offset??0)+1}–${Number(detail.query.offset??0)+detail.answer.count}` : "No rows"} of {detail.answer.total} matching records. Missing readings are not zero. Quality flags remain attached.</p>{detail.answer.count>0&&detail.answer.total!==null&&Number(detail.query.offset??0)+detail.answer.count<detail.answer.total&&<button type="button" onClick={()=>void inspect(detail.title,detail.dataset,{...detail.query,offset:String(Number(detail.query.offset??0)+detail.answer.count)})}>Next records</button>}{Number(detail.query.offset??0)>0&&<button type="button" onClick={()=>void inspect(detail.title,detail.dataset,{...detail.query,offset:"0"})}>Back to first records</button>}{detail.answer.cache?.state==='stale'&&<p className={styles.notice}>Cached readings; refresh unavailable.</p>}<p>{detail.answer.source.notes}</p><div className={styles.readings}>{detail.answer.rows.map((row,index)=><dl key={index}>{Object.entries(row).map(([key,value])=><div key={key}><dt>{key}</dt><dd>{textValue(value)}</dd></div>)}</dl>)}</div></section>}
    </div></details>
  </article>;
}
