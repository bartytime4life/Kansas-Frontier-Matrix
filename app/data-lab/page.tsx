'use client';
import Link from 'next/link';
import {useEffect,useMemo,useRef,useState} from 'react';
import {RECOVERED_COLLECTIONS,recoveredCollection,recoveredMapUrl} from '../recovered-collections';
import {collectionMetadata,collectionUrl,collectionPacks,packCollections,RESEARCH_PACKS} from '../collection-metadata';
import {loadLabSample,profileCollection,storyBrief,measurementLayer,type LabSnapshot} from '../collection-lab';
import CollectionMetadataPanel from '../collection-metadata-panel';
import styles from './lab.module.css';

function save(name:string,content:string,type:string){
 const url=URL.createObjectURL(new Blob([content],{type})),a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
}
export default function DataLab(){
 const [id,setId]=useState(''),[search,setSearch]=useState(''),[snapshot,setSnapshot]=useState<LabSnapshot|null>(null);
 const [busy,setBusy]=useState(false),[status,setStatus]=useState('Choose a collection, then load a bounded record sample.');
 const [question,setQuestion]=useState('What do these records contribute to this investigation?');
 const [measure,setMeasure]=useState(''),[context,setContext]=useState('');
 const request=useRef<AbortController|null>(null),version=useRef(0);
 const collection=recoveredCollection(id),profile=useMemo(()=>collection&&snapshot?profileCollection(collection,snapshot):null,[collection,snapshot]);
 const eligible=profile?.fields.filter(f=>f.groups.length)??[],measureGroups=eligible.find(f=>f.name===measure)?.groups??[];
 const layerPreview=useMemo(()=>collection&&snapshot&&measure&&context?measurementLayer(collection,snapshot,measure,context):null,[collection,snapshot,measure,context]);
 const brief=useMemo(()=>collection&&snapshot&&profile?storyBrief(collection,snapshot,question,profile):'',[collection,snapshot,profile,question]);
 const displayFields=useMemo(()=>[...(profile?.fields??[])].sort((a,b)=>Number(b.groups.length>0)-Number(a.groups.length>0)||b.missing-a.missing),[profile]);
 const matching=RECOVERED_COLLECTIONS.filter(c=>(c.title+' '+c.id).toLowerCase().includes(search.toLowerCase()));
 useEffect(()=>{const stop=()=>{version.current++;request.current?.abort();};const timer=setTimeout(()=>{const params=new URLSearchParams(location.search),value=params.get('collection');if(value&&recoveredCollection(value)){setId(value);const p=RESEARCH_PACKS.find(p=>p.id===params.get('pack'));if(p)setQuestion(p.question);}},0);return()=>{clearTimeout(timer);stop();};},[]);
 function choose(next:string){request.current?.abort();version.current++;setId(next);setSnapshot(null);setMeasure('');setContext('');setBusy(false);setStatus('Ready to load this collection.');history.replaceState(null,'',`/data-lab?collection=${encodeURIComponent(next)}`);}
 async function load(){
  if(!collection)return;request.current?.abort();const controller=new AbortController();request.current=controller;const generation=++version.current;
  setBusy(true);setStatus('Reading up to five pages, at most 250 records…');const timer=setTimeout(()=>controller.abort(),120000);
  try{const next=await loadLabSample(collection,controller.signal);if(generation!==version.current)return;setSnapshot(next);setMeasure('');setContext('');setStatus(`${next.rows.length} records loaded from ${next.pages} page(s). ${next.hasMore?'Further records remain.':'No further records were reported at this read.'}`);}
  catch(error){if(generation===version.current)setStatus(controller.signal.aborted?'Read cancelled or timed out. No incomplete sample was substituted.':error instanceof Error?error.message:'The archive could not be read.');}
  finally{clearTimeout(timer);if(generation===version.current)setBusy(false);}
 }
 function bundle(){if(!collection||!snapshot||!profile)return;save(`${collection.id}-lab.json`,JSON.stringify({profile,question,records:snapshot.rows,brief},null,2),'application/json');}
 return <main className={styles.lab}>
  <header><nav aria-label="Data workspace"><Link href="/?panel=layers">Map</Link><Link href="/data-library">Data library</Link></nav><p className={styles.eyebrow}>KANSAS FRONTIER MATRIX · RECORD LAB</p><h1>Find the connections.<br/>Keep the evidence.</h1><p>Explore source fields, missing values, measurement groups and map opportunities. Build a reproducible research brief from actual archive records.</p></header>
  <section className={styles.packs} aria-label="Research starting points"><h2>Start with a question</h2><div>{RESEARCH_PACKS.map(pack=>{
   const collections=packCollections(pack.id),first=collections[0],maps=collections.filter(c=>c.geometry).slice(0,6);
   return <article key={pack.id}><h3>{pack.title}</h3><p>{pack.question}</p><small>{collections.length} related collections</small><div>{first&&<button type="button" onClick={()=>{choose(first.id);setQuestion(pack.question);}}>Investigate records</button>}{maps.length>0&&<Link href={recoveredMapUrl(maps.map(c=>c.id))}>Map {maps.length} collections →</Link>}</div><details><summary>Sources &amp; interpretation</summary><p>{pack.note}</p><ul>{collections.map(c=><li key={c.id}><Link href={collectionUrl(c.id)}>{c.title}</Link></li>)}</ul></details></article>;
  })}</div></section>
  <section className={styles.workbench} aria-label="Record profiling workbench"><h2>Work with the records</h2>
   <div className={styles.controls}><label>Find collections<input type="search" value={search} onChange={e=>setSearch(e.target.value)} placeholder="Water, Census, wells, newspapers…"/></label>
    <label>Collection<select value={id} onChange={e=>choose(e.target.value)}><option value="">Choose one of {RECOVERED_COLLECTIONS.length} collections</option>{collection&&!matching.some(c=>c.id===id)&&<option value={id}>{collection.title}</option>}{matching.map(c=><option key={c.id} value={c.id}>{c.title}</option>)}</select></label></div>
   {collection&&<><CollectionMetadataPanel collection={collection}/><div className={styles.actions}><button type="button" disabled={busy} onClick={()=>void load()}>Load up to 250 records</button>{busy&&<button type="button" onClick={()=>request.current?.abort()}>Cancel read</button>}<Link href={collectionUrl(id)}>Browse original record fields</Link>{collection.geometry&&<Link href={recoveredMapUrl([id])}>Map this collection</Link>}<button type="button" onClick={()=>save(`${id}-metadata.json`,JSON.stringify(collectionMetadata(collection),null,2),'application/json')}>Download metadata</button></div></>}
   <p role="status" aria-live="polite">{status}</p>
   {profile&&collection&&snapshot&&<>
    <div className={styles.metrics}><div><strong>{profile.sample.rows}</strong><span>Loaded records</span></div><div><strong>{profile.fields.length}</strong><span>Retained fields</span></div><div><strong>{profile.spatial.mappable}</strong><span>Usable stored geometries</span></div><div><strong>{profile.provenance.length}</strong><span>Returned source references</span></div></div>
    <p className={styles.note}>{profile.sample.scope} {profile.sample.hasMore?'More records remain outside this sample.':''}{profile.spatial.sampleBoundingBox&&<> Loaded geometry extent (longitude/latitude): {profile.spatial.sampleBoundingBox.join(', ')}. This is a sample extent, not collection coverage.</>}</p>
    {profile.sample.stale&&<p className={styles.note}>Some pages came from stale cache. Source times remain authoritative; reloading does not make historical observations current.</p>}
    <h3>Field completeness &amp; recorded measurements</h3><p>Zero is a value. Blank and absent values stay missing. Identifiers, dates, coordinates and quality flags are excluded from measurement summaries. Provider fill codes are retained; check source definitions before interpretation.</p>
    <p className={styles.scrollHint}>Swipe or scroll the table sideways to compare every column.</p><div className={styles.table} role="region" aria-label="Field completeness table; scroll horizontally for all columns" tabIndex={0}><table><caption>Loaded sample only · units and measurement contexts stay separate</caption><thead><tr><th>Field / role</th><th>Present</th><th>Missing</th><th>Recorded numeric groups</th></tr></thead><tbody>{displayFields.map(f=><tr key={f.name}><th scope="row"><code>{f.name}</code><small>{f.role}</small></th><td>{f.present}</td><td>{f.missing}</td><td>{f.groups.map(g=><p key={g.context}><strong>{g.context}</strong><br/>{g.count} numeric values · min {g.min} · max {g.max} · mean {g.mean??'Unavailable'} · median {g.median}</p>)}{!f.groups.length&&'No eligible numeric measurements'}{f.additionalGroups>0&&<p>{f.additionalGroups} additional groups are outside the 12-group summary; all original values remain in the export.</p>}{f.longFields>0&&<p>{f.longFields} long fields require the full-field reader in the Data library.</p>}{f.exampleValues.length>0&&<p>Recorded time values: {f.exampleValues.join(' · ')}. Field meanings and editions need source documentation.</p>}</td></tr>)}</tbody></table></div>
    <h3>Trace the sources</h3><p>Read times: {profile.sample.retrievedAt.map(v=>v??'Not supplied').join(' · ')}. These are retrieval times, not observation dates.</p>
    {profile.provenance.length?<ul>{profile.provenance.map((p,i)=><li key={i}>{p.sourceId??'Source ID not supplied'} · {p.url?<a href={p.url} target="_blank" rel="noopener noreferrer">Provider source</a>:'Source link not supplied'}<br/><code>SHA256: {p.sha256??'Not supplied'}</code></li>)}</ul>:<p>No per-record lineage was supplied for this sample.</p>}
    {collection.geometry&&eligible.length>0&&<section aria-label="Create a measurement layer"><h3>Create a measurement layer</h3><p>Export validated longitude/latitude XY geometry with one numeric field and one unit/measurement context. Original source geometry remains in the lab JSON. Unlocated records and other contexts stay counted as omissions.</p><div className={styles.controls}><label>Measurement field<select value={measure} onChange={e=>{setMeasure(e.target.value);setContext('');}}><option value="">Choose a numeric field</option>{eligible.map(f=><option key={f.name} value={f.name}>{f.name}</option>)}</select></label><label>Unit &amp; measurement context<select value={context} onChange={e=>setContext(e.target.value)}><option value="">Choose one context</option>{measureGroups.map(g=><option key={g.context} value={g.context}>{g.context}</option>)}</select></label></div>{layerPreview&&<p>{layerPreview.features.length} features · {layerPreview.kfm.omitted.noUsableGeometry} records without usable geometry · {layerPreview.kfm.omitted.notNumeric} without a numeric value · {layerPreview.kfm.omitted.otherContext} in other measurement contexts</p>}<button type="button" disabled={busy||!layerPreview?.features.length} onClick={()=>save(`${id}-${measure}.geojson`,JSON.stringify(layerPreview,null,2),'application/geo+json')}>Download measurement layer · GeoJSON</button></section>}
    <h3>Build a research story</h3><p>Turn the observed sample into a source-linked draft. Questions guide research; the brief does not infer causes, trends or source approval.</p><label>Research question<textarea rows={3} value={question} maxLength={600} onChange={e=>setQuestion(e.target.value)}/></label>
    <div className={styles.actions}>{collectionPacks(id).map(p=><button type="button" key={p.id} onClick={()=>setQuestion(p.question)}>{p.title}</button>)}</div>
    <details><summary>Preview the source-linked brief</summary><pre>{brief}</pre></details>
    <div className={styles.actions}><button type="button" disabled={busy} onClick={bundle}>Download lab data + metadata · JSON</button><button type="button" disabled={busy} onClick={()=>save(`${id}-research-brief.md`,brief,'text/markdown')}>Download story brief · Markdown</button></div>
    <p className={styles.note}>Credit: deterministic KFM record profiling. No AI review or approval is established by this output. Long-field previews remain explicitly marked in exports; use the Data library to read original text in full.</p>
   </>}
  </section>
  <footer><Link href="/data-library">Explore all {RECOVERED_COLLECTIONS.length} collections →</Link> · <a href="/api/collection-metadata">Machine-readable metadata catalog</a><p>Research bundles suggest useful connections. Geographic proximity, shared field names and matching numbers do not establish compatible editions, causation or a completed join.</p></footer>
 </main>;
}
