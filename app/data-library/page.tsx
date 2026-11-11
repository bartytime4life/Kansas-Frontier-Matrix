'use client';
import Link from 'next/link';
import {useEffect,useLayoutEffect,useRef,useState} from 'react';
import {RECOVERED_COLLECTIONS,recoveredCollection,recoveredMapUrl} from '../recovered-collections';
import {fetchArchive,rowLabel,textValue,type ArchiveAnswer} from '../archive-layer-data';
import ArchiveSearch from './search';
import {fetchCatalogFreshness,freshnessLine,loadedThrough,type CatalogFreshness} from './freshness';
import styles from './library.module.css';
import {collectionLocation,matchingCollections,comparisonKey,pinComparison,comparisonFields,comparisonValue,comparisonExport,COMPARISON_LIMIT,type ComparedRecord} from './collection-browser';
import browserStyles from './collection-browser.module.css';

function RecordField({value,id,database,record,field}:{value:unknown;id:string;database:string;record:string;field:string}){
 const [part,setPart]=useState<ArchiveAnswer|null>(null),[message,setMessage]=useState(''),[busy,setBusy]=useState(false);
 const request=useRef<AbortController|null>(null);
 useEffect(()=>()=>{const controller=request.current;request.current=null;controller?.abort();},[]);
 const long=!!value&&typeof value==='object'&&'longField' in value&&'preview' in value;
 async function read(start=0){
  request.current?.abort();const controller=new AbortController();request.current=controller;setBusy(true);setMessage('Loading field…');
  const timer=setTimeout(()=>{
   if(request.current!==controller)return;
   request.current=null;controller.abort();setBusy(false);setMessage('Field request timed out. Retry.');
  },25000);
  try{
   const result=await fetchArchive(`recovered-${database}`,{collection:id,record,field,start:String(start)},controller.signal);
   if(request.current!==controller||controller.signal.aborted)return;
   setPart(result);setMessage('');
  }
  catch{if(request.current===controller)setMessage('Field unavailable. Retry.');}
  finally{clearTimeout(timer);if(request.current===controller){request.current=null;setBusy(false);}}
 }
 if(!long)return <>{textValue(value)}</>;
 return <><p>{String(value.preview)}…</p><button type="button" disabled={busy} onClick={()=>void read()}>Open full field</button>{message&&<p role="status">{message}</p>}{part&&<><p>Characters {part.fieldChunk!.start+1}–{Math.min(part.fieldChunk!.characters,part.fieldChunk!.start+32768)} of {part.fieldChunk!.characters}</p><pre>{textValue((part.rows[0]?.values as Record<string,unknown>)?.[field])}</pre>{part.fieldChunk?.nextStart!==null&&<button type="button" disabled={busy} onClick={()=>void read(part.fieldChunk!.nextStart!)}>Next part</button>}</>}</>;
}

export default function DataLibrary(){
 const [search,setSearch]=useState(''),[mappedOnly,setMappedOnly]=useState(false),[id,setId]=useState(''),[selected,setSelected]=useState<string[]>([]),[selectionVisit,setSelectionVisit]=useState(0);
 const [compared,setCompared]=useState<ComparedRecord[]>([]),[comparisonStatus,setComparisonStatus]=useState('');
 const comparisonHeading=useRef<HTMLHeadingElement>(null);
 const [answer,setAnswer]=useState<ArchiveAnswer|null>(null),[status,setStatus]=useState('Choose a collection to read its records.');
 const [busy,setBusy]=useState(false),[page,setPage]=useState(1);
 // When the PC last loaded each collection, from the public catalog; absent until the PC has answered.
 const [fresh,setFresh]=useState<CatalogFreshness|null>(null);
 const request=useRef<AbortController|null>(null),generation=useRef(0);
 const finder=useRef<HTMLInputElement>(null),collectionHeading=useRef<HTMLHeadingElement>(null);
 const collection=recoveredCollection(id);
 const matching=matchingCollections(RECOVERED_COLLECTIONS,search,mappedOnly),hasFilters=Boolean(search.trim()||mappedOnly);
 function syncLocation(nextId=id,find=search,mapped=mappedOnly){
  try{history.replaceState(history.state,'',collectionLocation(location.search,location.hash,nextId,find,mapped));}
  catch{/* Browsing remains usable when the browser cannot update history. */}
 }
 function clearFilters(){setSearch('');setMappedOnly(false);syncLocation(id,'',false);finder.current?.focus();}
 // A deliberate collection choice owns focus after its content has committed.
 // Filtering and background freshness updates leave the reader's focus alone.
 useLayoutEffect(()=>{if(selectionVisit>0){collectionHeading.current?.focus();collectionHeading.current?.scrollIntoView({block:'start',behavior:'auto'});}},[selectionVisit]);
 useEffect(()=>{
  const token=setTimeout(()=>{const params=new URLSearchParams(location.search),value=params.get('collection'),find=(params.get('find')??'').slice(0,80);if(value&&recoveredCollection(value))setId(value);if(find.trim())setSearch(find);setMappedOnly(params.get('mapped')==='1');},0);
  return()=>{clearTimeout(token);generation.current++;request.current?.abort();};
 },[]);
 useEffect(()=>{
  const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),15000);
  fetchCatalogFreshness(controller.signal).then(value=>{if(!controller.signal.aborted)setFresh(value);}).catch(()=>{});
  return()=>{clearTimeout(timer);controller.abort();};
 },[]);
 const collectionFreshness=(collectionId:string)=>fresh?.collections.get(collectionId)??null;
 function choose(next:string){
  if(!recoveredCollection(next))return;
  request.current?.abort();generation.current++;setSelectionVisit(n=>n+1);setId(next);setAnswer(null);setPage(1);setBusy(false);setStatus('Ready to read this collection.');
  syncLocation(next);
 }
 async function read(after?:string){
  if(!collection)return;
  request.current?.abort();const controller=new AbortController();request.current=controller;const version=++generation.current;
  setBusy(true);setStatus('Reading archive records…');
  const timer=setTimeout(()=>controller.abort(),25000);
  try{
   const result=await fetchArchive(`recovered-${collection.database}`,{collection:id,limit:'20',...(after?{after}:{})},controller.signal);
   if(version!==generation.current)return;
   if(controller.signal.aborted){setStatus('The archive did not respond in time. Retry when the PC is available.');return;}
   setAnswer(result);setPage(n=>after?n+1:1);setStatus(result.count?`${result.count} records on this page. ${result.hasMore?'More pages are available.':'End of this collection.'}`:'This collection has no retained records.');
  }catch(error){if(version===generation.current)setStatus(controller.signal.aborted?'The archive did not respond in time. Retry when the PC is available.':error instanceof Error?error.message:'Archive unavailable.');}
  finally{clearTimeout(timer);if(version===generation.current)setBusy(false);}
 }
 function pin(row:ArchiveAnswer['rows'][number]){
  if(!collection||!answer)return;
  const key=comparisonKey(id,row.id);
  if(compared.some(record=>record.key===key)){setCompared(current=>current.filter(record=>record.key!==key));setComparisonStatus('Record removed from comparison.');return;}
  try{setCompared(pinComparison(compared,collection,row,answer));setComparisonStatus('Record pinned. Browse another collection or page to add a comparison.');}
  catch(error){setComparisonStatus(error instanceof Error?error.message:'Could not pin this record.');}
 }
 function removeCompared(key?:string){setCompared(current=>key?current.filter(record=>record.key!==key):[]);setComparisonStatus(key?'Record removed from comparison.':'Comparison cleared.');comparisonHeading.current?.focus();}
 function downloadComparison(){
  const url=URL.createObjectURL(new Blob([JSON.stringify(comparisonExport(compared),null,2)],{type:'application/json'}));
  const a=document.createElement('a');a.href=url;a.download='kfm-archive-comparison.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
 }
 function download(){if(!answer)return;const url=URL.createObjectURL(new Blob([JSON.stringify(answer,null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download=`${id}-page-${page}.json`;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
 return <main className={styles.library}>
  <header><Link href="/?panel=layers">← Back to the map</Link><span>KANSAS FRONTIER MATRIX</span><h1>Explore the whole archive</h1><p>Places, measurements, history and the records behind them. Browse original fields, keep source dates in view, and combine collections on the map.</p></header>
  <div className={styles.summary}><strong>{RECOVERED_COLLECTIONS.length} record collections</strong><span>{RECOVERED_COLLECTIONS.filter(c=>c.geometry).length} map options · availability shown on read</span><span>Full-text search of newspaper pages and archive texts</span><span>Public source data · archived editions</span>{fresh&&<span>Load dates as of {fresh.at.slice(0,16).replace('T',' ')} UTC{fresh.state==='stale'?' (PC away; last known)':''}</span>}</div>
  <ArchiveSearch loadedThrough={{newspapers:loadedThrough(collectionFreshness('bulk-newspaper-pages')),texts:loadedThrough(fresh?.datasets.get('archive-search')?.freshness)}}/>
  {selected.length>0&&<aside className={`${styles.tray} ${browserStyles.selectionTray}`} aria-label="Selected archive map collections"><div><strong>{selected.length} {selected.length===1?'collection':'collections'} selected</strong><small>Map their first record pages; load further pages in Layers.</small></div><Link href={recoveredMapUrl(selected)}>Open together on map →</Link><button type="button" onClick={()=>setSelected([])}>Clear</button></aside>}
  <section className={browserStyles.comparison} aria-labelledby="archive-comparison-heading">
   <h2 id="archive-comparison-heading" tabIndex={-1} ref={comparisonHeading}>Compare the records</h2>
   <p>Pin up to four records while you browse. Kept only until you leave or reload this page.</p>
   {compared.length===0&&<p className={styles.meta}>Read a collection, open a record and choose “Pin for comparison”.</p>}
   <p role="status" aria-live="polite">{comparisonStatus||`${compared.length} of ${COMPARISON_LIMIT} records pinned.`}</p>
   {compared.length>0&&<>
    <p className={styles.note}>Original values: check units, dates and place identities. No automatic matching, conversion or updates.</p>
    <div className={styles.actions}><button type="button" onClick={downloadComparison}>Download comparison · JSON</button><button type="button" onClick={()=>removeCompared()}>Clear comparison</button><span>{compared.length} of {COMPARISON_LIMIT} records · original values</span></div>
    <div className={browserStyles.comparisonScroll} role="region" aria-label="Record comparison; scroll horizontally for more records" tabIndex={0}>
     <table className={browserStyles.comparisonTable}>
      <caption>Original fields and separate source context</caption>
      <thead><tr><th scope="col">Field</th>{compared.map(record=><th scope="col" key={record.key}><strong>{rowLabel(record.row,0)}</strong><small>{record.collection.title} · Record {String(record.row.id)}</small><button type="button" aria-label={`Remove ${record.collection.title} record ${String(record.row.id)} from comparison`} onClick={()=>removeCompared(record.key)}>Remove record</button></th>)}</tr></thead>
      <tbody>
       <tr><th scope="row">Source &amp; retrieval</th>{compared.map(record=><td key={record.key}><p>{record.source.provider||'Provider not supplied'}</p><p>Retrieved {record.retrievedAt} · not observation time</p>{record.cache&&<p>Cache: {record.cache.state} · {record.cache.at}</p>}<details><summary>Source context</summary><p>{record.source.notes}</p><p>{record.source.coverage}</p><pre>{textValue(record.row.provenance)}</pre></details></td>)}</tr>
       {comparisonFields(compared).map(field=><tr key={field}><th scope="row">{field}</th>{compared.map(record=>{const value=comparisonValue(record,field);return <td key={record.key}>{value.length>240?<details><summary>{value.slice(0,200)}…</summary><pre>{value}</pre></details>:value}</td>;})}</tr>)}
      </tbody>
     </table>
    </div>
    <p className={styles.meta}>“Field absent” differs from a supplied null, empty text or zero. Long fields remain marked previews. Download retains each record and its provenance; it does not certify a finding or release data.</p>
   </>}
  </section>
  <div className={styles.layout}>
   <section className={styles.catalog} aria-label="Find a collection">
    <div className={browserStyles.filters}>
     <div className={browserStyles.filterTools}><label>Find a collection<input ref={finder} type="search" value={search} onChange={e=>{setSearch(e.target.value);syncLocation(id,e.target.value,mappedOnly);}} maxLength={80} placeholder="Wells, Census, wind speed…" aria-describedby="collection-results-summary"/></label>{hasFilters&&<button type="button" aria-label="Clear collection filters" onClick={clearFilters}>Clear</button>}</div>
     <label className={browserStyles.mapFilter}><input type="checkbox" checked={mappedOnly} onChange={e=>{setMappedOnly(e.target.checked);syncLocation(id,search,e.target.checked);}}/>With map geometry</label>
     <p className={browserStyles.hint}>Search names, sources and field names. Record availability is checked when you read a collection.</p>
    </div>
    <p id="collection-results-summary" role="status" aria-live="polite" aria-atomic="true">{matching.length} of {RECOVERED_COLLECTIONS.length} collections</p>
    <div className={styles.results}>{matching.map(c=>{const through=loadedThrough(collectionFreshness(c.id));return <button type="button" key={c.id} aria-pressed={c.id===id} onClick={()=>choose(c.id)}><strong>{c.title}</strong><small>{c.geometry?'Records + map geometry':'Records & reference tables'} · {c.database==='bulk'?'bulk archive':'observation archive'}{through?` · loaded ${through}`:''}</small></button>;})}</div>
    {!matching.length&&<div className={browserStyles.empty}><strong>No matching collections</strong><p>{mappedOnly?'Try fewer words or include collections without map geometry.':'Try fewer words, a source family or a field name.'}{collection?' Your collection choice and map selection are unchanged.':''}</p><button type="button" onClick={clearFilters}>Show all collections</button></div>}
   </section>
   <section className={styles.content} aria-label="Collection records">
    {collection?<><h2 ref={collectionHeading} className={browserStyles.heading} tabIndex={-1}>{collection.title}</h2><button type="button" className={browserStyles.back} onClick={()=>finder.current?.focus()}>Back to collection finder</button><p>Original codes, units, missing values and quality flags are preserved. Each record keeps its own date; editions can overlap. These pages are ordered by record identity, not map position.</p>
     {fresh&&<p className={styles.note}>On the PC: {freshnessLine(collectionFreshness(id))} A record missing here may simply not be loaded yet.</p>}
     <div className={styles.actions}><button type="button" disabled={busy} onClick={()=>void read()}>Read first page</button>{compared.length>0&&<a className={browserStyles.mapLink} href="#archive-comparison-heading">Compare pinned records ({compared.length}) ↑</a>}{selected.length>0&&<Link className={browserStyles.mapLink} href={recoveredMapUrl(selected)}>Open selected map ({selected.length}) →</Link>}{collection.geometry&&<button type="button" aria-pressed={selected.includes(id)} onClick={()=>setSelected(current=>current.includes(id)?current.filter(v=>v!==id):[...current,id])}>{selected.includes(id)?'Remove from map selection':'Add to map selection'}</button>}</div>
     {!collection.geometry&&<p className={styles.note}>Available as source records. This table has no stored GeoJSON geometry; geographic joins require the matching place identity and edition.</p>}
     <details><summary>{collection.columns.length} available fields</summary><p className={styles.fields}>{collection.columns.join(' · ')}</p></details>
    </>:<><h2>Every collection has a place here</h2><p>Start with a collection. Measurements and text remain useful even when they have no location to draw. Geometry collections can be selected together and opened on the map.</p></>}
    <p role="status">{status}</p>
    {answer&&<><div className={styles.actions}><strong>Page {page}</strong><button type="button" onClick={download}>Download this page · JSON</button>{answer.nextCursor&&<button type="button" disabled={busy} onClick={()=>void read(answer.nextCursor!)}>Next records</button>}</div>
     {answer.cache?.state==='stale'&&<p className={styles.note}>Cached records. The PC could not refresh this page; retained source dates still apply.</p>}
     <p className={styles.meta}>Received {answer.generatedAt}. This is retrieval time, not observation time. {answer.source.notes}</p>
     {answer.rows.map((row,index)=><details className={styles.record} key={`${id}-${page}-${String(row.id)}`}><summary>{rowLabel(row,index)}</summary><button type="button" aria-pressed={compared.some(record=>record.key===comparisonKey(id,row.id))} onClick={()=>pin(row)}>{compared.some(record=>record.key===comparisonKey(id,row.id))?'Unpin from comparison':'Pin for comparison'}</button><dl>{Object.entries((row.values??{}) as Record<string,unknown>).map(([key,value])=><div key={key}><dt>{key}</dt><dd><RecordField value={value} id={id} database={collection!.database} record={String(row.id)} field={key}/></dd></div>)}</dl>{!!row.provenance&&<p className={styles.meta}>Source provenance: {textValue(row.provenance)}</p>}</details>)}
    </>}
   </section>
  </div>
  <footer><Link href="/?panel=layers">Map layers &amp; dated observation tools</Link><p>Record counts are page counts. A partial page is not statewide coverage. Provider attribution remains with the data, including <a href="https://www.openstreetmap.org/copyright">© OpenStreetMap contributors · ODbL</a>.</p></footer>
 </main>;
}
