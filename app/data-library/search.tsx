'use client';
import {useEffect,useRef,useState,type FormEvent} from 'react';
import {fetchArchive} from '../archive-layer-data';
import styles from './library.module.css';

// The archive-search dataset (scripts/local-data/texts.mjs): ranked FTS5 hits over newspaper OCR
// pages and archive texts, with the title's place of publication and hits by year and title.
type Source='newspapers'|'texts';
type Hit={id:string;source:Source;title:string|null;snippet:string|null;rank:number|null;issueDate?:string|null;place?:string|null;lccn?:string;sequence?:number|null;pageUrl?:string|null;
 identifier?:string;creator?:string|null;year?:number|null;part?:number|null;itemUrl?:string|null};
type Facets={years:{year:number|null;hits:number}[];titles:{id:string;title:string|null;place:string|null;hits:number}[]};
// The relay's validated envelope (fetchArchive), read with this dataset's row shape.
type SearchAnswer={total:number|null;count:number;rows:Hit[];generatedAt:string;source:{notes:string};totalCapped?:boolean;facets?:Facets};
const OPEN='⟦',CLOSE='⟧',PAGE=20,MAX_OFFSET=1000;
const YEAR=/^\d{4}$/;

/** Matched terms arrive between ⟦ and ⟧; render them as <mark> without interpreting anything else. */
export function Snippet({text}:{text:string|null}){
 if(!text)return <em>No snippet available.</em>;
 const parts=text.split(OPEN);
 return <>{parts.map((part,index)=>{
  if(index===0)return <span key={index}>{part}</span>;
  const end=part.indexOf(CLOSE);
  return end<0?<span key={index}>{part}</span>:<span key={index}><mark>{part.slice(0,end)}</mark>{part.slice(end+1)}</span>;
 })}</>;
}

/** Hits by decade, from the gateway's hits by year; undated items are reported separately. */
export function decades(years:Facets['years']){
 const byDecade=new Map<number,number>();let undated=0;
 for(const y of years){if(y.year===null||!Number.isFinite(y.year)){undated+=y.hits;continue;}const d=Math.floor(y.year/10)*10;byDecade.set(d,(byDecade.get(d)??0)+y.hits);}
 const list=[...byDecade].sort((a,b)=>a[0]-b[0]).map(([decade,hits])=>({decade,hits}));
 return {decades:list,undated,max:Math.max(1,...list.map(d=>d.hits))};
}

export default function ArchiveSearch(){
 const [q,setQ]=useState(''),[source,setSource]=useState<Source>('newspapers'),[from,setFrom]=useState(''),[to,setTo]=useState(''),[title,setTitle]=useState('');
 const [answer,setAnswer]=useState<SearchAnswer|null>(null),[offset,setOffset]=useState(0),[status,setStatus]=useState('Search the digitised newspaper pages and archive texts by word, phrase or year.'),[busy,setBusy]=useState(false);
 const request=useRef<AbortController|null>(null),generation=useRef(0),linked=useRef(false);
 useEffect(()=>()=>request.current?.abort(),[]);
 async function run(nextOffset:number,nextTitle=title,override?:{q:string;source:Source;from:string;to:string}){
  const asked=override??{q,source,from,to};
  const query=asked.q.trim();if(!query){setStatus('Type a word or a "quoted phrase" to search.');return;}
  if(asked.from&&!YEAR.test(asked.from)||asked.to&&!YEAR.test(asked.to)){setStatus('Years are four digits, for example 1893.');return;}
  request.current?.abort();const controller=new AbortController();request.current=controller;const version=++generation.current;
  setBusy(true);setStatus('Searching the archive on the pipeline PC…');
  const timer=setTimeout(()=>controller.abort(),25000);
  try{
   const result=await fetchArchive('archive-search',{q:query,source:asked.source,facets:'1',limit:String(PAGE),offset:String(nextOffset),...(asked.from?{from:asked.from}:{}),...(asked.to?{to:asked.to}:{}),...(nextTitle?{title:nextTitle}:{})},controller.signal) as unknown as SearchAnswer;
   if(version!==generation.current)return;
   setAnswer(result);setOffset(nextOffset);setTitle(nextTitle);
   const total=result.total??0;
   setStatus(total?`${total.toLocaleString()}${result.totalCapped?'+':''} ${asked.source==='newspapers'?'pages':'text parts'} match, ranked by relevance. Showing ${nextOffset+1}–${nextOffset+result.rows.length}.`:'No matches. OCR text is uncorrected: try another spelling, a prefix (wich*) or a wider year range.');
  }catch(error){if(version===generation.current){setAnswer(null);setStatus(controller.signal.aborted?'The archive did not respond in time. Retry when the PC is available.':error instanceof Error?error.message:'Archive unavailable.');}}
  finally{clearTimeout(timer);if(version===generation.current)setBusy(false);}
 }
 function submit(event:FormEvent){event.preventDefault();void run(0,'');}
 useEffect(()=>{
  if(linked.current)return;linked.current=true;
  const params=new URLSearchParams(location.search),linkedQ=(params.get('q')??'').slice(0,200);
  if(!linkedQ.trim())return;
  const linkedSource:Source=params.get('source')==='texts'?'texts':'newspapers',linkedFrom=YEAR.test(params.get('from')??'')?params.get('from')!:'',linkedTo=YEAR.test(params.get('to')??'')?params.get('to')!:'';
  setQ(linkedQ);setSource(linkedSource);setFrom(linkedFrom);setTo(linkedTo);
  void run(0,'',{q:linkedQ,source:linkedSource,from:linkedFrom,to:linkedTo});
  // Runs once from the address bar; later searches come from the form.
  // eslint-disable-next-line react-hooks/exhaustive-deps
 },[]);
 const facets=answer?.facets,decadeChart=facets?decades(facets.years):null;
 const total=answer?.total??0,canNext=answer!==null&&offset+PAGE<total&&offset+PAGE<=MAX_OFFSET;
 return <section className={styles.search} aria-labelledby="archive-search-title">
  <h2 id="archive-search-title">Search the texts</h2>
  <p>Full-text search over the Kansas newspaper pages and public-domain texts the PC has loaded: words, <q>quoted phrases</q>, prefixes such as <code>wich*</code>, and AND, OR, NOT between terms. Results rank the original OCR, so spellings and scanning errors of the period affect what is found.</p>
  <form className={styles.searchForm} onSubmit={submit}>
   <label className={styles.grow}>Words or phrase<input type="search" value={q} onChange={e=>setQ(e.target.value)} placeholder='tornado · "dust storm" · grasshopper*' maxLength={200} required/></label>
   <label>Collection<select value={source} onChange={e=>{setSource(e.target.value as Source);setTitle('');}}><option value="newspapers">Newspaper pages</option><option value="texts">Archive texts</option></select></label>
   <label>From year<input type="text" inputMode="numeric" value={from} onChange={e=>setFrom(e.target.value)} placeholder="1864" maxLength={4} pattern="\d{4}"/></label>
   <label>To year<input type="text" inputMode="numeric" value={to} onChange={e=>setTo(e.target.value)} placeholder="1960" maxLength={4} pattern="\d{4}"/></label>
   <button type="submit" disabled={busy}>Search</button>
  </form>
  <p role="status">{status}</p>
  {title&&answer&&<p className={styles.note}>Showing one title only. <button type="button" disabled={busy} onClick={()=>void run(0,'')}>Show all titles</button></p>}
  {answer&&answer.rows.length>0&&<div className={styles.searchLayout}>
   <div className={styles.hits}>
    {answer.rows.map(hit=><article className={styles.hit} key={hit.id}>
     <h3>{hit.title??(hit.source==='newspapers'?hit.lccn:hit.identifier)}</h3>
     <p className={styles.meta}>{hit.source==='newspapers'
      ?<>{hit.issueDate} · {hit.place??'place not recorded'} · page {hit.sequence??'?'}</>
      :<>{hit.year??'year not recorded'}{hit.creator?` · ${hit.creator}`:''} · part {hit.part??'?'}</>}</p>
     <p className={styles.snippet}><Snippet text={hit.snippet}/></p>
     <p className={styles.meta}>{hit.source==='newspapers'
      ?hit.pageUrl&&<a href={hit.pageUrl} target="_blank" rel="noopener noreferrer">Open this page at the Library of Congress ↗</a>
      :hit.itemUrl&&<a href={hit.itemUrl} target="_blank" rel="noopener noreferrer">Open this item at the Internet Archive ↗</a>}</p>
    </article>)}
    <div className={styles.actions}>
     <button type="button" disabled={busy||offset===0} onClick={()=>void run(Math.max(0,offset-PAGE))}>Previous</button>
     <button type="button" disabled={busy||!canNext} onClick={()=>void run(offset+PAGE)}>Next</button>
     {answer.total!==null&&offset+PAGE>MAX_OFFSET&&<small>The first {MAX_OFFSET.toLocaleString()} ranked hits are browsable; narrow the search to reach the rest.</small>}
    </div>
    <p className={styles.meta}>Received {answer.generatedAt}. {answer.source.notes}</p>
   </div>
   {facets&&decadeChart&&<aside className={styles.facets} aria-label="Hits by decade and title">
    <h3>Hits by decade</h3>
    <ol className={styles.decades}>{decadeChart.decades.map(d=><li key={d.decade}><span>{d.decade}s</span><i style={{width:`${Math.round(100*d.hits/decadeChart.max)}%`}} aria-hidden="true"/><b>{d.hits.toLocaleString()}</b></li>)}</ol>
    {decadeChart.undated>0&&<p className={styles.meta}>{decadeChart.undated.toLocaleString()} without a recorded year.</p>}
    <p className={styles.meta}>Counts are matching {source==='newspapers'?'pages':'text parts'} among the loaded archive, not events; coverage differs by title and year.</p>
    <h3>By title</h3>
    <ul className={styles.titles}>{facets.titles.slice(0,12).map(t=><li key={t.id}><button type="button" disabled={busy} aria-pressed={title===t.id} onClick={()=>void run(0,title===t.id?'':t.id)}><span>{t.title??t.id}</span>{t.place&&<small>{t.place}</small>}<b>{t.hits.toLocaleString()}</b></button></li>)}</ul>
   </aside>}
  </div>}
 </section>;
}
