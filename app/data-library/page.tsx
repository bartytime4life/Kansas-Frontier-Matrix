'use client';
import Link from 'next/link';
import {useEffect,useRef,useState} from 'react';
import {RECOVERED_COLLECTIONS,recoveredCollection,recoveredMapUrl} from '../recovered-collections';
import {fetchArchive,rowLabel,textValue,type ArchiveAnswer} from '../archive-layer-data';
import styles from './library.module.css';

function RecordField({value,id,database,record,field}:{value:unknown;id:string;database:string;record:string;field:string}){
 const [part,setPart]=useState<ArchiveAnswer|null>(null),[message,setMessage]=useState(''),[busy,setBusy]=useState(false);
 const request=useRef<AbortController|null>(null);
 useEffect(()=>()=>request.current?.abort(),[]);
 const long=!!value&&typeof value==='object'&&'longField' in value&&'preview' in value;
 async function read(start=0){
  request.current?.abort();const controller=new AbortController();request.current=controller;setBusy(true);setMessage('Loading field…');
  const timer=setTimeout(()=>controller.abort(),25000);
  try{const result=await fetchArchive(`recovered-${database}`,{collection:id,record,field,start:String(start)},controller.signal);if(!controller.signal.aborted){setPart(result);setMessage('');}}
  catch{if(request.current===controller)setMessage('Field unavailable. Retry.');}
  finally{clearTimeout(timer);if(request.current===controller)setBusy(false);}
 }
 if(!long)return <>{textValue(value)}</>;
 return <><p>{String(value.preview)}…</p><button type="button" disabled={busy} onClick={()=>void read()}>Open full field</button>{message&&<p role="status">{message}</p>}{part&&<><p>Characters {part.fieldChunk!.start+1}–{Math.min(part.fieldChunk!.characters,part.fieldChunk!.start+32768)} of {part.fieldChunk!.characters}</p><pre>{textValue((part.rows[0]?.values as Record<string,unknown>)?.[field])}</pre>{part.fieldChunk?.nextStart!==null&&<button type="button" disabled={busy} onClick={()=>void read(part.fieldChunk!.nextStart!)}>Next part</button>}</>}</>;
}

export default function DataLibrary(){
 const [search,setSearch]=useState(''),[id,setId]=useState(''),[selected,setSelected]=useState<string[]>([]);
 const [answer,setAnswer]=useState<ArchiveAnswer|null>(null),[status,setStatus]=useState('Choose a collection to read its records.');
 const [busy,setBusy]=useState(false),[page,setPage]=useState(1);
 const request=useRef<AbortController|null>(null),generation=useRef(0);
 const collection=recoveredCollection(id);
 const matching=RECOVERED_COLLECTIONS.filter(c=>(c.title+' '+c.database).toLowerCase().includes(search.toLowerCase()));
 useEffect(()=>{
  const token=setTimeout(()=>{const value=new URLSearchParams(location.search).get('collection');if(value&&recoveredCollection(value))setId(value);},0);
  return()=>{clearTimeout(token);request.current?.abort();};
 },[]);
 function choose(next:string){request.current?.abort();generation.current++;setId(next);setAnswer(null);setPage(1);setBusy(false);setStatus('Ready to read this collection.');history.replaceState(null,'',`/data-library?collection=${encodeURIComponent(next)}`);}
 async function read(after?:string){
  if(!collection)return;
  request.current?.abort();const controller=new AbortController();request.current=controller;const version=++generation.current;
  setBusy(true);setStatus('Reading archive records…');
  const timer=setTimeout(()=>controller.abort(),25000);
  try{
   const result=await fetchArchive(`recovered-${collection.database}`,{collection:id,limit:'20',...(after?{after}:{})},controller.signal);
   if(version!==generation.current)return;
   setAnswer(result);setPage(n=>after?n+1:1);setStatus(result.count?`${result.count} records on this page. ${result.hasMore?'More pages are available.':'End of this collection.'}`:'This collection has no retained records.');
  }catch(error){if(version===generation.current)setStatus(controller.signal.aborted?'The archive did not respond in time. Retry when the PC is available.':error instanceof Error?error.message:'Archive unavailable.');}
  finally{clearTimeout(timer);if(version===generation.current)setBusy(false);}
 }
 function download(){if(!answer)return;const url=URL.createObjectURL(new Blob([JSON.stringify(answer,null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=url;a.download=`${id}-page-${page}.json`;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
 return <main className={styles.library}>
  <header><Link href="/?panel=layers">← Back to the map</Link><span>KANSAS FRONTIER MATRIX</span><h1>Explore the whole archive</h1><p>Places, measurements, history and the records behind them. Browse original fields, keep source dates in view, and combine collections on the map.</p></header>
  <div className={styles.summary}><strong>{RECOVERED_COLLECTIONS.length} record collections</strong><span>{RECOVERED_COLLECTIONS.filter(c=>c.geometry).length} map options · availability shown on read</span><span>Public source data · archived editions</span></div>
  <div className={styles.layout}>
   <section className={styles.catalog} aria-label="Find a collection">
    <label>Find a collection<input type="search" value={search} onChange={e=>setSearch(e.target.value)} placeholder="Wells, newspapers, Census, schools…"/></label>
    <p>{matching.length} collections · names and source families</p>
    <div className={styles.results}>{matching.map(c=><button type="button" key={c.id} aria-pressed={c.id===id} onClick={()=>choose(c.id)}><strong>{c.title}</strong><small>{c.geometry?'Records + map geometry':'Records & reference tables'} · {c.database==='bulk'?'bulk archive':'observation archive'}</small></button>)}</div>
   </section>
   <section className={styles.content} aria-label="Collection records">
    {collection?<><h2>{collection.title}</h2><p>Original codes, units, missing values and quality flags are preserved. Each record keeps its own date; editions can overlap. These pages are ordered by record identity, not map position.</p>
     <div className={styles.actions}><button type="button" disabled={busy} onClick={()=>void read()}>Read first page</button>{collection.geometry&&<button type="button" aria-pressed={selected.includes(id)} onClick={()=>setSelected(current=>current.includes(id)?current.filter(v=>v!==id):[...current,id])}>{selected.includes(id)?'Remove from map selection':'Add to map selection'}</button>}</div>
     {!collection.geometry&&<p className={styles.note}>Available as source records. This table has no stored GeoJSON geometry; geographic joins require the matching place identity and edition.</p>}
     <details><summary>{collection.columns.length} available fields</summary><p className={styles.fields}>{collection.columns.join(' · ')}</p></details>
    </>:<><h2>Every collection has a place here</h2><p>Start with a collection. Measurements and text remain useful even when they have no location to draw. Geometry collections can be selected together and opened on the map.</p></>}
    <p role="status">{status}</p>
    {answer&&<><div className={styles.actions}><strong>Page {page}</strong><button type="button" onClick={download}>Download this page · JSON</button>{answer.nextCursor&&<button type="button" disabled={busy} onClick={()=>void read(answer.nextCursor!)}>Next records</button>}</div>
     {answer.cache?.state==='stale'&&<p className={styles.note}>Cached records. The PC could not refresh this page; retained source dates still apply.</p>}
     <p className={styles.meta}>Received {answer.generatedAt}. This is retrieval time, not observation time. {answer.source.notes}</p>
     {answer.rows.map((row,index)=><details className={styles.record} key={`${id}-${page}-${String(row.id)}`}><summary>{rowLabel(row,index)}</summary><dl>{Object.entries((row.values??{}) as Record<string,unknown>).map(([key,value])=><div key={key}><dt>{key}</dt><dd><RecordField value={value} id={id} database={collection!.database} record={String(row.id)} field={key}/></dd></div>)}</dl>{!!row.provenance&&<p className={styles.meta}>Source provenance: {textValue(row.provenance)}</p>}</details>)}
    </>}
   </section>
  </div>
  {selected.length>0&&<aside className={styles.tray} aria-label="Selected archive map collections"><div><strong>{selected.length} collections selected</strong><small>Map their first record pages; load further pages in Layers.</small></div><Link href={recoveredMapUrl(selected)}>Open together on map →</Link><button type="button" onClick={()=>setSelected([])}>Clear</button></aside>}
  <footer><Link href="/?panel=layers">Map layers &amp; dated observation tools</Link><p>Record counts are page counts. A partial page is not statewide coverage. Provider attribution remains with the data, including <a href="https://www.openstreetmap.org/copyright">© OpenStreetMap contributors · ODbL</a>.</p></footer>
 </main>;
}
