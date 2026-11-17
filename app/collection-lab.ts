import {collectionMetadata,fieldRole,type Collection} from './collection-metadata';
import {fetchArchive,validArchiveGeometry,type ArchiveAnswer,type ArchiveRow} from './archive-layer-data';

export const LAB_MAX_ROWS=250,LAB_MAX_PAGES=5;
const object=(v:unknown):v is Record<string,unknown> => !!v&&typeof v==='object'&&!Array.isArray(v);
const missing=(v:unknown)=>v===null||v===undefined||typeof v==='string'&&!v.trim();
function numeric(v:unknown):number|null{
 if(typeof v==='string'){
  if(!/^[+-]?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?$/.test(v.trim()))return null;
  v=Number(v.trim());
 }
 return typeof v==='number'&&Number.isFinite(v)&&(!Number.isInteger(v)||Number.isSafeInteger(v))?v:null;
}
const dimensionFields=['unit','units','unit_name','measurement_unit','result_measure_unit_code','variable','parameter_cd','parameter','element','characteristic_name','measureid','qualifier','quality_flag','remark_cd','censoring_code','result_detection_condition'];
function groupKey(values:Record<string,unknown>){
 const dimensions=Object.fromEntries(dimensionFields.filter(k=>!missing(values[k])&&['string','number'].includes(typeof values[k])).map(k=>[k,String(values[k])]));
 return Object.keys(dimensions).length?JSON.stringify(dimensions):'Unit and measurement context not supplied';
}
const safeUrl=(v:unknown)=>{try{if(typeof v!=='string')return null;const u=new URL(v);return u.protocol==='https:'&&!u.username&&!u.password?u.href:null;}catch{return null;}};
export type LabSnapshot={answers:ArchiveAnswer[];rows:ArchiveRow[];hasMore:boolean;pages:number};
/** Same two-reader queue, response limit and cancellation boundary as map reads. */
export async function loadLabSample(c:Collection,signal:AbortSignal,reader=fetchArchive):Promise<LabSnapshot>{
 const answers:ArchiveAnswer[]=[],rows:ArchiveRow[]=[],cursors=new Set<string>(),ids=new Set<string>();let after:string|undefined;
 for(let page=0;page<LAB_MAX_PAGES;page++){
  signal.throwIfAborted();
  const answer=await reader(`recovered-${c.database}`,{collection:c.id,limit:String(Math.min(50,LAB_MAX_ROWS-rows.length)),...(after?{after}:{})},signal);
  if(answer.collection!==c.id||answer.rows.length>50||rows.length+answer.rows.length>LAB_MAX_ROWS)throw new Error('The sample did not match the selected collection or row limit.');
  for(const row of answer.rows){if(typeof row.id!=='string'||ids.has(row.id))throw new Error('Repeated or missing record identity; sample stopped.');ids.add(row.id);}
  rows.push(...answer.rows);answers.push(answer);
  if(!answer.hasMore)break;
  if(!answer.nextCursor||cursors.has(answer.nextCursor)||answer.rows.length===0)throw new Error('Archive pagination did not advance; sample stopped.');
  cursors.add(answer.nextCursor);after=answer.nextCursor;
 }
 signal.throwIfAborted();return {answers,rows,hasMore:answers.at(-1)?.hasMore??false,pages:answers.length};
}
export function profileCollection(c:Collection,snapshot:LabSnapshot){
 const rows=snapshot.rows,fields=c.columns.map(name=>{
  const role=fieldRole(name,c.keys),groups=new Map<string,number[]>();let present=0,numericCount=0,longFields=0;
  const exampleValues:string[]=[];
  for(const row of rows){
   const values=object(row.values)?row.values:{},value=values[name];
   if(missing(value))continue;present++;
   if(object(value)&&value.longField===true){longFields++;continue;}
   if(role==='time'&&exampleValues.length<6&&!exampleValues.includes(String(value)))exampleValues.push(String(value));
   const n=role==='value'?numeric(value):null;
   if(n!==null){numericCount++;const key=groupKey(values);const list=groups.get(key)??[];list.push(n);groups.set(key,list);}
  }
  const summary=[...groups].slice(0,12).map(([context,values])=>{
   values.sort((a,b)=>a-b);const mid=Math.floor(values.length/2);
   const mean=values.reduce((total,v)=>total+v/values.length,0);
   return {context,count:values.length,min:values[0],max:values.at(-1)!,mean:Number.isFinite(mean)?mean:null,median:values.length%2?values[mid]:values[mid-1]/2+values[mid]/2};
  });
  return {name,role,present,missing:rows.length-present,numericCount,longFields,exampleValues,groups:summary,additionalGroups:Math.max(0,groups.size-summary.length)};
 });
 const provenance=new Map<string,{sourceId:string|null;url:string|null;sha256:string|null}>();
 for(const row of rows){if(!object(row.provenance))continue;const p=row.provenance;
  const entry={sourceId:typeof p.source_id==='string'?p.source_id:null,url:safeUrl(p.source_url),sha256:typeof p.sha256==='string'&&/^[a-f\d]{64}$/i.test(p.sha256)?p.sha256:null};
  provenance.set(JSON.stringify(entry),entry);
 }
 let mappable=0,unavailableGeometry=0;const bounds=[Infinity,Infinity,-Infinity,-Infinity];
 if(c.geometry)for(const row of rows){
  const values=object(row.values)?row.values:{};let value=values[c.geometry];
  if(object(value)&&value.longField===true){unavailableGeometry++;continue;}
  try{if(typeof value==='string')value=JSON.parse(value);}catch{continue;}
  const geometry=validArchiveGeometry(value);
  if(geometry&&!(geometry.type==='Point'&&geometry.coordinates[0]===0&&geometry.coordinates[1]===0)){
   mappable++;
   const visit=(v:unknown):void=>{if(!Array.isArray(v))return;if(typeof v[0]==='number'){bounds[0]=Math.min(bounds[0],v[0]);bounds[1]=Math.min(bounds[1],v[1]);bounds[2]=Math.max(bounds[2],v[0]);bounds[3]=Math.max(bounds[3],v[1]);}else v.forEach(visit);};
   if('coordinates' in geometry)visit(geometry.coordinates);
  }
 }
 const base=collectionMetadata(c),lineage=[...provenance.values()],providers=[...new Set(snapshot.answers.map(a=>a.source?.provider).filter(Boolean))];
 return {format:'kfm-collection-profile-v1',collection:{...base,
  temporal:{...base.temporal,retrievedAt:snapshot.answers.map(a=>a.generatedAt??null)},
  provenance:{...base.provenance,provider:providers.length===1?providers[0]:null,sourceUrls:[...new Set(lineage.flatMap(p=>p.url?[p.url]:[]))],digests:[...new Set(lineage.flatMap(p=>p.sha256?[p.sha256]:[]))]}},sample:{rows:rows.length,pages:snapshot.pages,hasMore:snapshot.hasMore,
  scope:'First identity-ordered pages; not a random sample, spatial search, trend or collection total.',
  retrievedAt:snapshot.answers.map(a=>a.generatedAt??null),cache:snapshot.answers.map(a=>a.cache??null),
  stale:snapshot.answers.some(a=>a.cache?.state==='stale'),recordIds:rows.map(r=>r.id)},
  fields,spatial:{mappable,unavailableGeometry,withoutUsableGeometry:c.geometry?rows.length-mappable:null,sampleBoundingBox:mappable?bounds:null},provenance:lineage,
  interpretation:['Numeric summaries describe the loaded values only. Original sentinel values and quality flags are not reinterpreted.',
   'Units and measurement identifiers are profiled in separate groups. Unitless groups need source documentation.',
   'Identifiers, dates, locations and quality flags are excluded from measurement statistics.'],
  credit:{method:'Deterministic KFM browser profile',aiReview:null,approval:null},
 };
}
export function storyBrief(c:Collection,snapshot:LabSnapshot,question:string,prepared?:ReturnType<typeof profileCollection>){
 const profile=prepared??profileCollection(c,snapshot);
 const measurements=profile.fields.flatMap(f=>f.groups.map(g=>`- ${f.name} (${g.context}): ${g.count} numeric values; recorded range ${g.min} to ${g.max}.`));
 return [`# ${c.title}: research brief`,'',`Question: ${question}`,'',
  '## What was read',`${profile.sample.rows} records over ${profile.sample.pages} page(s). ${profile.sample.hasMore?'Further records remain.':'The endpoint reported no further records at this read.'}`,profile.sample.scope,
  profile.sample.stale?'This brief includes stale cached records.':'No returned page was marked stale.',
  `Retrieval timestamps: ${profile.sample.retrievedAt.map(v=>v??'Not supplied').join(', ')}. These are not observation dates.`,
  '', '## Recorded values',...(measurements.slice(0,20).length?measurements.slice(0,20):['No eligible numeric measurements were returned. Inspect source records and field definitions.']),
  ...(measurements.length>20?['Additional measurement groups remain in the profile export.']:[]),
  ...(profile.fields.some(f=>f.additionalGroups>0)?['Some fields exceed the 12-group summary. Omitted-group counts are in the profile; all original values remain in the record export.']:[]),
  '', '## Source time fields',...profile.fields.filter(f=>f.role==='time'&&f.exampleValues.length).map(f=>`- ${f.name}: ${f.exampleValues.join('; ')} (recorded examples, not a complete range or a verified temporal meaning).`),
  '', '## Source lineage',...profile.provenance.map(p=>`- ${p.sourceId??'Source ID not supplied'}; ${p.url??'Source URL not supplied'}; SHA256 ${p.sha256??'not supplied'}`),
  ...(!profile.provenance.length?['Source lineage was not supplied for these records.']:[]),
  '', '## Limits and next steps',...profile.interpretation.map(v=>`- ${v}`),
  '- Verify field definitions, source dates, geographic identifiers and editions before comparison or causal interpretation.',
  '', 'Credit: deterministic KFM record profile. No AI review or approval is established by this brief.',
  '',`Collection: ${collectionMetadata(c).access.library}`,`Record identities: ${profile.sample.recordIds.join('; ')}`].join('\n');
}

/** A separate unit/measurement group becomes one reusable GeoJSON layer. */
export function measurementLayer(c:Collection,snapshot:LabSnapshot,field:string,context:string){
 if(!c.geometry||!c.columns.includes(field)||fieldRole(field,c.keys)!=='value')throw new Error('Choose a measurement field in a geometry collection.');
 const features=[];const omitted={otherContext:0,notNumeric:0,noUsableGeometry:0};
 for(const row of snapshot.rows){
  const values=object(row.values)?row.values:{};
  if(groupKey(values)!==context){omitted.otherContext++;continue;}
  const value=numeric(values[field]);if(value===null){omitted.notNumeric++;continue;}
  let candidate=values[c.geometry];try{if(typeof candidate==='string')candidate=JSON.parse(candidate);}catch{candidate=null;}
  const geometry=validArchiveGeometry(candidate);
  if(!geometry||geometry.type==='Point'&&geometry.coordinates[0]===0&&geometry.coordinates[1]===0){omitted.noUsableGeometry++;continue;}
  const p=object(row.provenance)?row.provenance:{};
  features.push({type:'Feature' as const,id:String(row.id),geometry,properties:{record_id:String(row.id),collection:c.id,field,value,measurement_context:context,
   source_id:typeof p.source_id==='string'?p.source_id:null,source_url:safeUrl(p.source_url),source_sha256:typeof p.sha256==='string'?p.sha256:null}});
 }
 return {type:'FeatureCollection' as const,features,kfm:{format:'kfm-lab-measurement-layer-v1',collection:c.id,field,context,omitted,
  rowsRead:snapshot.rows.length,hasMore:snapshot.hasMore,retrievalTimes:snapshot.answers.map(a=>a.generatedAt??null),
  stale:snapshot.answers.some(a=>a.cache?.state==='stale'),scope:'Loaded identity-ordered records only; validated longitude/latitude XY geometry and recorded numeric values. No geocoding, reprojection or unit conversion. Original geometry remains in the lab record export.',
  reviewCredit:null,approval:null}};
}
