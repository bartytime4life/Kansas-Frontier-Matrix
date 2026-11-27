'use client';
import {Suspense,useEffect,useLayoutEffect,useRef,useState,type FormEvent} from 'react';
import {fetchArchive} from '../archive-layer-data';
import {PageAssistant} from '../site-assistant';
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
const NEWSPAPER_TITLE=/^[a-z]{2}\d{8}$/i;
const ARCHIVE_TEXT_TITLE=/^[A-Za-z0-9._-]{1,100}$/;
type SearchQuery={q:string;source:Source;from:string;to:string;title:string};
type SearchRequest={query:SearchQuery;offset:number;previous:number[]};
type SearchPage=SearchRequest&{answer:SearchAnswer;focusResults:boolean};
function exactArchivePhrase(query:string){
 const words=query.trim().split(/\s+/);
 if(words.length<2||words.length>8||words.some(word=>
  !/^[\p{L}\p{N}'’-]{1,40}$/u.test(word)||!/[\p{L}\p{N}]/u.test(word)||/^(AND|OR|NOT)$/i.test(word)))return null;
 const phrase='"'+words.join(' ')+'"';
 return phrase.length<=200?phrase:null;
}
function searchTitle(source:Source,value:string){
 if(source==='newspapers')return NEWSPAPER_TITLE.test(value)?value.toLowerCase():'';
 const identifier=value.trim();
 return ARCHIVE_TEXT_TITLE.test(identifier)?identifier:'';
}
/** Accepted filters only; retain the independent collection finder state. */
export function archiveSearchLocation(search:string,query:SearchQuery){
 const params=new URLSearchParams(search);params.set('q',query.q);params.set('source',query.source);
 for(const [key,value] of [['from',query.from],['to',query.to],['title',searchTitle(query.source,query.title)]]){if(value)params.set(key,value);else params.delete(key);}
 return `/data-library?${params}#archive-text-search`;
}

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

/** loadedThrough: the day the newest newspaper-page file and the newest archive-text file were retrieved, when the catalog reports them. */
export default function ArchiveSearch({loadedThrough}:{loadedThrough?:{newspapers:string|null;texts:string|null}}={}){
 const [q,setQ]=useState(''),[source,setSource]=useState<Source>('newspapers'),[from,setFrom]=useState(''),[to,setTo]=useState('');
 const [page,setPage]=useState<SearchPage|null>(null),[retry,setRetry]=useState<SearchRequest|null>(null);
 const [status,setStatus]=useState('Search the digitised newspaper pages and archive texts by word, phrase or year.'),[busy,setBusy]=useState(false),[formError,setFormError]=useState('');
 const request=useRef<AbortController|null>(null),generation=useRef(0),queryInput=useRef<HTMLInputElement>(null);
 const section=useRef<HTMLElement>(null),searchHeading=useRef<HTMLHeadingElement>(null),resultsHeading=useRef<HTMLHeadingElement>(null);
 useLayoutEffect(()=>{
  if(!page?.focusResults)return;
  const active=typeof document==='undefined'?null:document.activeElement;
  if(active&&active!==document.body&&!section.current?.contains(active))return;
  resultsHeading.current?.focus({preventScroll:true});resultsHeading.current?.scrollIntoView({block:'start',behavior:'auto'});
 },[page]);
 useEffect(()=>()=>{generation.current++;request.current?.abort();},[]);
 async function run(search:SearchRequest,focusResults=false){
  const asked={...search.query,q:search.query.q.trim()};
  let invalid='';
  if(!asked.q)invalid='Type a word or a "quoted phrase" to search.';
  else if(asked.from&&!YEAR.test(asked.from)||asked.to&&!YEAR.test(asked.to))invalid='Years are four digits, for example 1893.';
  else if(asked.from&&asked.to&&asked.from>asked.to)invalid='From year must be earlier than or the same as To year.';
  if(invalid){setFormError(invalid);return;}
  const attempt={...search,query:asked};
  request.current?.abort();const controller=new AbortController();request.current=controller;const version=++generation.current;
  setBusy(true);setRetry(null);setFormError('');setStatus('Searching the archive on the pipeline PC…');
  const timer=setTimeout(()=>controller.abort(),25000);
  try{
   const result=await fetchArchive('archive-search',{q:asked.q,source:asked.source,facets:'1',limit:String(Math.min(PAGE,MAX_OFFSET-search.offset)),offset:String(search.offset),...(asked.from?{from:asked.from}:{}),...(asked.to?{to:asked.to}:{}),...(asked.title?{title:asked.title}:{})},controller.signal) as unknown as SearchAnswer;
   controller.signal.throwIfAborted();
   if(version!==generation.current)return;
   setPage({...attempt,answer:result,focusResults});
   try{
    // A background linked query must not replace an explicit collection/hash destination.
    if(focusResults||!new URLSearchParams(location.search).has('collection')&&(!location.hash||location.hash==='#archive-text-search'))history.replaceState(history.state,'',archiveSearchLocation(location.search,asked));
   }catch{/* Reading remains available when history writes are blocked. */}
   const total=result.total??0;
   setStatus(result.rows.length?`${total.toLocaleString()}${result.totalCapped?'+':''} ${asked.source==='newspapers'?'pages':'text parts'} match, ranked by relevance. Showing ${search.offset+1}–${search.offset+result.rows.length}.`:total?'No further matches were returned on this page. Go back or narrow the search.':'No matches. OCR text is uncorrected: try another spelling, a prefix (wich*) or a wider year range.');
  }catch(error){if(version===generation.current){setRetry(attempt);setStatus(controller.signal.aborted?'The archive did not respond in time. Retry when the PC is available.':error instanceof Error?error.message:'Archive unavailable.');}}
  finally{clearTimeout(timer);if(version===generation.current){setBusy(false);request.current=null;}}
 }
 function cancel(){generation.current++;request.current?.abort();request.current=null;setBusy(false);setRetry(null);setStatus('Search cancelled. No new results were applied.');queryInput.current?.focus();}
 function searchDraft(words:string){
  const activeTitle=page?.query.source===source?page.query.title:'';
  void run({query:{q:words,source,from,to,title:activeTitle},offset:0,previous:[]},true);
 }
 function submit(event:FormEvent){event.preventDefault();searchDraft(q);}
 function editSearch(){queryInput.current?.focus({preventScroll:true});queryInput.current?.scrollIntoView({block:'center',behavior:'auto'});}
 function filterTitle(value:string){if(page)void run({query:{...page.query,title:value},offset:0,previous:[]},true);}
 useEffect(()=>{
  let current=true;
  queueMicrotask(()=>{
   if(!current)return;
   const params=new URLSearchParams(location.search),linkedQ=(params.get('q')??'').slice(0,200);
   if(!linkedQ.trim())return;
   const linkedSource:Source=params.get('source')==='texts'?'texts':'newspapers',linkedFrom=YEAR.test(params.get('from')??'')?params.get('from')!:'',linkedTo=YEAR.test(params.get('to')??'')?params.get('to')!:'';
   const requestedTitle=params.get('title')??'';
   const linkedTitle=searchTitle(linkedSource,requestedTitle);
   setQ(linkedQ);setSource(linkedSource);setFrom(linkedFrom);setTo(linkedTo);
   if(!params.has('collection')&&(!location.hash||location.hash==='#archive-text-search')){searchHeading.current?.focus({preventScroll:true});searchHeading.current?.scrollIntoView({block:'start',behavior:'auto'});}
   void run({query:{q:linkedQ,source:linkedSource,from:linkedFrom,to:linkedTo,title:linkedTitle},offset:0,previous:[]});
  });
  return()=>{current=false;};
 },[]);
 const answer=page?.answer,offset=page?.offset??0,title=page?.query.title??'';
 const facets=answer?.facets,decadeChart=facets?decades(facets.years):null;
 const total=answer?.total??0,nextOffset=offset+(answer?.rows.length??0),canNext=!!answer?.rows.length&&nextOffset<total&&nextOffset<MAX_OFFSET;
 const draftChanged=page&&(q.trim()!==page.query.q||source!==page.query.source||from!==page.query.from||to!==page.query.to);
 const period=page?.query.from&&page.query.to?`${page.query.from}–${page.query.to}`:page?.query.from?`${page.query.from} onward`:page?.query.to?`through ${page.query.to}`:'all loaded years';
 const exactPhrase=exactArchivePhrase(q);
 const collectionName=source==='newspapers'?'Kansas newspapers':'public-domain Kansas texts';
 const assistantQuestion=q.trim()
  ?`Help me refine these archive search terms for ${collectionName}: ${JSON.stringify(q.trim())}. Suggest an exact phrase, alternate wording, and a way to narrow the results.`
  :`How should I turn a topic, place, or event into useful search terms for ${collectionName}?`;
 return <section ref={section} className={styles.search} aria-labelledby="archive-search-title">
  <h2 ref={searchHeading} tabIndex={-1} id="archive-search-title">Search the texts</h2>
  <p>Search digitized Kansas newspapers and public-domain texts. For a name or place, use a quoted phrase so the words match together.</p>
  <form id="archive-search-form" className={styles.searchForm} onSubmit={submit} aria-describedby={formError?"archive-search-error":undefined}>
   <label className={styles.grow}>Words or phrase<input ref={queryInput} type="search" value={q} onChange={e=>setQ(e.target.value)} placeholder='tornado · "dust storm" · grasshopper*' maxLength={200} required/></label>
   <label>Collection<select value={source} onChange={e=>setSource(e.target.value as Source)}><option value="newspapers">Newspaper pages</option><option value="texts">Archive texts</option></select></label>
   <label>From year<input type="text" inputMode="numeric" value={from} onChange={e=>setFrom(e.target.value)} placeholder="1864" maxLength={4} pattern="\d{4}"/></label>
   <label>To year<input type="text" inputMode="numeric" value={to} onChange={e=>setTo(e.target.value)} placeholder="1960" maxLength={4} pattern="\d{4}"/></label>
  </form>
  <div className={styles.searchActions}>
   <button type="submit" form="archive-search-form" disabled={busy}>Search</button>
   {exactPhrase&&<button type="button" disabled={busy} onClick={()=>{queryInput.current?.focus();setQ(exactPhrase);searchDraft(exactPhrase);}}>Match exact phrase</button>}
   {busy&&<button type="button" onClick={cancel}>Cancel search</button>}
   <Suspense fallback={null}><PageAssistant inlineQuestion={assistantQuestion}/></Suspense>
  </div>
  {formError&&<p id="archive-search-error" className={styles.note} role="alert">{formError}</p>}
  <p role="status" aria-live="polite" aria-atomic="true">{status}</p>
  {retry&&!busy&&<button type="button" onClick={()=>{queryInput.current?.focus();void run(retry,true);}}>Retry last search</button>}
  {page&&(busy||retry||draftChanged)&&<p className={styles.note}>{busy?'Searching. Previous results remain below until the new search finishes.':retry?'The last search failed. Previous results remain below.':"Form changes have not been applied. Search to update the results below."}</p>}
  {title&&answer&&<p className={styles.note}>Title filter: {facets?.titles.find(item=>item.id===title)?.title??title} <button type="button" disabled={busy} onClick={()=>filterTitle('')}>Show all titles</button></p>}
  <details className={styles.searchHelp}>
   <summary>Search tips and archive coverage</summary>
   <ul>
    <li><code>barton county</code> finds both words anywhere on the same page. <code>&quot;barton county&quot;</code> finds them together in that order.</li>
    <li><code>&quot;barton county&quot; OR &quot;great bend&quot;</code> includes either phrase. Add <code>AND flood</code> to a phrase to require a topic on the same page.</li>
    <li>Try a newspaper title, year range, alternate spelling, or prefix such as <code>grasshopp*</code>. Scanning errors can hide matches.</li>
   </ul>
   {loadedThrough&&(loadedThrough.newspapers||loadedThrough.texts)&&<p>Most recent additions reported: {loadedThrough.newspapers?`newspaper pages ${loadedThrough.newspapers}`:'newspaper load date unavailable'}, {loadedThrough.texts?`archive texts ${loadedThrough.texts}`:'text load date unavailable'}. Coverage varies by title and year.</p>}
   <a href="/labs/newspaper-pulse">Compare word coverage in Newspaper Pulse →</a>
  </details>
  {answer&&page&&<section className={styles.searchLayout} aria-labelledby="archive-results-title" aria-busy={busy}>
   <div className={styles.hits}>
    <h3 ref={resultsHeading} tabIndex={-1} id="archive-results-title">Results for {/^"[^"]+"$/.test(page.query.q)?page.query.q:`“${page.query.q}”`}</h3>
    <p className={styles.meta}>{page.query.source==='newspapers'?'Newspaper pages':'Archive texts'} · {period}</p>
    <button type="button" className={styles.editSearch} onClick={editSearch}>Edit search</button>
    {answer.rows.map(hit=><article className={styles.hit} key={hit.id}>
     <h4>{hit.title??(hit.source==='newspapers'?hit.lccn:hit.identifier)}</h4>
     <p className={styles.meta}>{hit.source==='newspapers'
      ?<>{hit.issueDate} · {hit.place??'place not recorded'} · page {hit.sequence??'?'}</>
      :<>{hit.year??'year not recorded'}{hit.creator?` · ${hit.creator}`:''} · part {hit.part??'?'}</>}</p>
     <p className={styles.snippet}><Snippet text={hit.snippet}/></p>
     <p className={styles.meta}>{hit.source==='newspapers'
      ?hit.pageUrl&&<a href={hit.pageUrl} target="_blank" rel="noopener noreferrer">Open this page at the Library of Congress ↗</a>
      :hit.itemUrl&&<a href={hit.itemUrl} target="_blank" rel="noopener noreferrer">Open this item at the Internet Archive ↗</a>}</p>
    </article>)}
    <div className={styles.actions}>
     <a href={archiveSearchLocation('',page.query)}>Link to this search</a>
     <button type="button" disabled={busy||!page.previous.length} onClick={()=>void run({query:page.query,offset:page.previous.at(-1)!,previous:page.previous.slice(0,-1)},true)}>Previous</button>
     <button type="button" disabled={busy||!canNext} onClick={()=>void run({query:page.query,offset:nextOffset,previous:[...page.previous,offset]},true)}>Next</button>
     {answer.total!==null&&nextOffset>=MAX_OFFSET&&<small>The first {MAX_OFFSET.toLocaleString()} ranked hits are browsable; narrow the search to reach the rest.</small>}
    </div>
    <p className={styles.meta}>Received {answer.generatedAt}. {answer.source.notes}</p>
   </div>
   {facets&&decadeChart&&<aside className={styles.facets} aria-label="Hits by decade and title">
    <h3>Hits by decade</h3>
    <ol className={styles.decades}>{decadeChart.decades.map(d=><li key={d.decade}><span>{d.decade}s</span><i style={{width:`${Math.round(100*d.hits/decadeChart.max)}%`}} aria-hidden="true"/><b>{d.hits.toLocaleString()}</b></li>)}</ol>
    {decadeChart.undated>0&&<p className={styles.meta}>{decadeChart.undated.toLocaleString()} without a recorded year.</p>}
    <p className={styles.meta}>Counts are matching {page.query.source==='newspapers'?'pages':'text parts'} among the loaded archive, not events; coverage differs by title and year.</p>
    <h3>By title</h3>
    <ul className={styles.titles}>{facets.titles.slice(0,12).map(t=><li key={t.id}><button type="button" disabled={busy} aria-pressed={title===t.id} onClick={()=>filterTitle(title===t.id?'':t.id)}><span>{t.title??t.id}</span>{t.place&&<small>{t.place}</small>}<b>{t.hits.toLocaleString()}</b></button></li>)}</ul>
   </aside>}
  </section>}
 </section>;
}
