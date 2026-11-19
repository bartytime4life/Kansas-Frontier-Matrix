'use client';
import {useEffect,useMemo,useRef,useState,type Dispatch,type SetStateAction} from 'react';
import {loadLabSample,type LabSnapshot} from '../collection-lab';
import {labUrl,type Collection} from '../collection-metadata';
import {recoveredCollection} from '../recovered-collections';
import {documentedField} from '../collection-field-dictionary';
import {MAX_LAB_BUNDLE_BYTES,openLabBundle} from './lab-bundle';
import {connectRecordContexts,recordContextPlans,type ContextSample} from './record-context';
import styles from './lab.module.css';

const statusLabels={one_match:'One match in sample',multiple_matches:'Multiple metadata records',no_match:'No match in sample',missing_key:'Provider key missing'};
const contextFields=['name','site_no','site_type','altitude','vertical_datum','time_series_id','data_type','parameter_code','statistic_id','unit_of_measure','period_begin','period_end'];
export default function RecordContextPanel({collection,snapshot,contexts,onChange,busy}:{
 collection:Collection;snapshot:LabSnapshot;contexts:ContextSample[];onChange:Dispatch<SetStateAction<ContextSample[]>>;busy:boolean;
}){
 const [pending,setPending]=useState(''),[status,setStatus]=useState('');
 const [filter,setFilter]=useState('all');
 const generation=useRef(0),request=useRef<AbortController|null>(null);
 const plans=recordContextPlans(collection.id);
 const report=useMemo(()=>connectRecordContexts(collection,snapshot,contexts),[collection,snapshot,contexts]);
 useEffect(()=>()=>{generation.current++;request.current?.abort();},[snapshot,collection.id]);
 if(!plans.length)return null;
 function begin(target:string){
  request.current?.abort();const attempt=++generation.current;
  setPending(target);setStatus('Reading metadata context…');return attempt;
 }
 function apply(sample:ContextSample,attempt:number){
  if(attempt!==generation.current)return;
  onChange(previous=>[...previous.filter(c=>c.collectionId!==sample.collectionId),sample]);
  setStatus(`${sample.snapshot.rows.length} metadata records attached. Matches describe these loaded samples only.`);
 }
 async function attach(file:File,target:string){
  const attempt=begin(target);
  try{
   if(file.size>MAX_LAB_BUNDLE_BYTES)throw new Error('Choose a Record Lab JSON file under 8 MB.');
   const saved=openLabBundle(await file.text());
   if(saved.collection.id!==target)throw new Error('Choose a saved bundle for '+recoveredCollection(target)!.title+'.');
   apply({collectionId:target,snapshot:saved.snapshot},attempt);
  }catch(error){if(attempt===generation.current)setStatus(error instanceof Error?error.message:'The metadata bundle could not be read.');}
  finally{if(attempt===generation.current)setPending('');}
 }
 async function load(target:string){
  const attempt=begin(target),controller=new AbortController();request.current=controller;
  const timer=setTimeout(()=>controller.abort(),120000);
  try{apply({collectionId:target,snapshot:await loadLabSample(recoveredCollection(target)!,controller.signal)},attempt);}
  catch{if(attempt===generation.current)setStatus(controller.signal.aborted?'Metadata read cancelled or timed out. Existing context was retained.':'Metadata could not be loaded. Existing context was retained.');}
  finally{clearTimeout(timer);if(attempt===generation.current)setPending('');}
 }
 function remove(target:string){
  generation.current++;request.current?.abort();setPending('');
  onChange(previous=>previous.filter(c=>c.collectionId!==target));setStatus('Metadata sample removed. Original records were retained.');
 }
 return <section className={styles.recordContext} aria-labelledby="record-context-title">
  <h3 id="record-context-title">Connect station and series records</h3>
  <p>Match provider keys against a bounded metadata sample. Load a sample or attach a saved Record Lab bundle. Original observations stay intact.</p>
  <div className={styles.contextChoices}>{plans.map(plan=>{
   const target=recoveredCollection(plan.targetCollection)!,attached=contexts.some(c=>c.collectionId===target.id);
   const label=target.id.endsWith('-sites')?'station':'series';
   return <div key={target.id}>
    <h4>{label==='station'?'Station context':'Series context'}</h4>
    <div className={styles.actions}>
     <button type="button" disabled={busy||!!pending} onClick={()=>void load(target.id)}>{attached?'Reload':'Load'} {label} sample</button>
     {attached&&<button type="button" disabled={busy||!!pending} onClick={()=>remove(target.id)}>Remove {label} context</button>}
     <a href={labUrl(target.id)} target="_blank" rel="noopener noreferrer">Open {label} lab →</a>
    </div>
    <label>Attach saved {label} bundle<input type="file" disabled={busy||!!pending} accept=".json,application/json" onChange={event=>{
     const file=event.currentTarget.files?.[0];event.currentTarget.value='';if(file)void attach(file,target.id);
    }}/></label>
   </div>;
  })}</div>
  {pending&&<button type="button" onClick={()=>{generation.current++;request.current?.abort();setPending('');setStatus('Metadata read cancelled. Existing context was retained.');}}>Cancel metadata read</button>}
  <p role="status" aria-live="polite">{status}</p>
  {report.relations.length>0&&<>
   <p className={styles.note}>{report.scope} Capture versions, periods, datums and methods still need review. Matches do not replace observation units or establish AI review.</p>
   <label>Show context links<select value={filter} onChange={e=>setFilter(e.target.value)}>
    <option value="all">All loaded observations</option><option value="one_match">One match in sample</option>
    <option value="multiple_matches">Multiple metadata records</option><option value="no_match">No match in sample</option>
    <option value="missing_key">Missing provider key</option><option value="conflicts">Conflicting series fields</option>
   </select></label>
   {report.relations.map(relation=>{
    const attached=contexts.find(c=>c.collectionId===relation.targetCollection)!;
    const targetRows=new Map(attached.snapshot.rows.map(row=>[String(row.id),row]));
    const filtered=relation.rows.filter(row=>filter==='all'||filter==='conflicts'&&row.matches.some(m=>m.conflicts.length)||filter===row.status);
    return <article key={relation.targetCollection}>
     <h4>{relation.title}</h4>
     <p>{relation.counts.oneMatch} with one match · {relation.counts.multipleMatches} with multiple matches · {relation.counts.noMatch} unmatched · {relation.counts.missingKey} missing keys.</p>
     <p>{relation.targetSample.rows} metadata records loaded{relation.targetSample.hasMore?'; more records remain':''}. {relation.targetSample.stale&&'Metadata includes stale cached records. '}{relation.targetSample.origin==='saved-bundle'&&'Metadata came from a user-supplied file; its references have not been independently verified.'}</p>
     {relation.expectedDataType&&<p>Series namespace: <code>{relation.expectedDataType}</code>. {relation.targetSample.namespaceExcluded} metadata records have another or unknown series type. {relation.counts.conflictingRows} observation rows have conflicting shared fields; {relation.counts.unverifiedRows} lack comparison fields.</p>}
     {relation.targetSample.missingKeys>0&&<p>{relation.targetSample.missingKeys} metadata records lack a provider key.</p>}
     <details><summary>Inspect matches and source records</summary>
      <p>Showing {Math.min(20,filtered.length)} of {filtered.length} rows for this filter, up to five matches per row. The lab JSON retains all links and original records.</p>
      <p className={styles.scrollHint}>Swipe or scroll the table sideways to inspect metadata records and comparison fields.</p>
      <div className={styles.contextTable} role="region" aria-label={relation.title+' identity matches'} tabIndex={0}>
       <table><caption>Identity links within loaded samples · metadata applicability needs review</caption><thead><tr><th>Observation / provider key</th><th>Result</th><th>Metadata records / checks</th></tr></thead><tbody>{filtered.slice(0,20).map(row=><tr key={row.sourceRecordId}>
        <th scope="row"><code>{row.sourceRecordId}</code><br/><code>{row.providerKey??'Not supplied'}</code></th><td>{statusLabels[row.status]}</td>
        <td>{row.matches.slice(0,5).map(match=>{
         const source=targetRows.get(match.targetRecordId)!;
         const values=source.values as Record<string,unknown>;
         return <details key={match.targetRecordId}><summary>Metadata record <code>{match.targetRecordId}</code></summary>
          {match.conflicts.length>0&&<p>Conflicting fields: {match.conflicts.join(', ')}. Review both original records.</p>}
          {match.unverified.length>0&&<p>Comparison fields not supplied: {match.unverified.join(', ')}.</p>}
          <dl>{contextFields.filter(field=>Object.hasOwn(values,field)&&values[field]!==null).map(field=><div key={field}><dt>{field}</dt><dd>{typeof values[field]==='object'?JSON.stringify(values[field]):String(values[field])}{documentedField(relation.targetCollection,field)?.unit&&' '+documentedField(relation.targetCollection,field)!.unit}</dd></div>)}</dl>
          <pre>{JSON.stringify(source,null,2)}</pre>
         </details>;
        })}{!row.matches.length&&'No metadata record linked.'}{row.matches.length>5&&<p>{row.matches.length-5} further matches remain in the lab JSON.</p>}</td>
       </tr>)}</tbody></table>
      </div>
     </details>
     <details><summary>Read times and comparison checks</summary>
      <p>Metadata retrieval times: {relation.targetSample.retrievedAt.map(t=>t??'Not supplied').join(' · ')}. These are not observation dates.</p>
      <ul>{relation.checks.map(check=><li key={check}>{check}</li>)}</ul>
      <a href={relation.documentation.url}>USGS identity definitions</a>
     </details>
    </article>;
   })}
  </>}
 </section>;
}
