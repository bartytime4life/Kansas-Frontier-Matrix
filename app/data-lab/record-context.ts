import type {Collection} from '../collection-metadata';
import type {LabSnapshot} from '../collection-lab';
import {collectionRelationships} from '../collection-relationships';
import {recoveredCollection} from '../recovered-collections';

export type ContextSample={collectionId:string;snapshot:LabSnapshot};
const sites='observations-usgs-sites',series='observations-usgs-series';
const sourceTypes:Readonly<Record<string,string>>={
 'observations-usgs-daily-values':'Daily values','observations-usgs-peaks':'Peaks',
 'observations-usgs-field-measurements':'Field measurements',
};
export function recordContextPlans(collectionId:string){
 return Object.hasOwn(sourceTypes,collectionId)?collectionRelationships(collectionId).filter(r=>r.targetCollection===sites||r.targetCollection===series):[];
}
const object=(value:unknown):value is Record<string,unknown>=>!!value&&typeof value==='object'&&!Array.isArray(value);
function identifier(values:unknown,field:string):string|null{
 const value=object(values)&&Object.hasOwn(values,field)?values[field]:null;
 return typeof value==='string'&&value.length<=512&&value.trim()?value:null;
}
const scope='Exact provider-key matches within the loaded samples only. A single match is not proof of a unique, current or applicable metadata version. Missing matches do not mean the archive has no context.';
export function connectRecordContexts(collection:Collection,snapshot:LabSnapshot,contexts:readonly ContextSample[]){
 const plans=recordContextPlans(collection.id),seen=new Set<string>();
 if(contexts.length>2)throw new Error('Attach at most one station and one series sample.');
 return {format:'kfm-record-context-links-v1',sourceCollection:collection.id,scope,
  interpretation:[
   'All original observation and context records are retained separately. Matching never fills or overwrites an observation field.',
   'Capture versions, metadata periods, datums, methods and observation quality still need review. No temporal join or unit/coordinate conversion is performed.',
   'User-supplied file references are not independently verified. Identity matches do not establish source approval or AI review.',
  ],
  relations:contexts.map(context=>{
   const plan=plans.find(p=>p.targetCollection===context.collectionId),target=recoveredCollection(context.collectionId);
   if(!plan||!target||seen.has(context.collectionId))throw new Error('This context collection is unsupported or already attached.');
   seen.add(context.collectionId);
   const targetSample=context.snapshot;
   for(const sample of [snapshot,targetSample])if(sample.rows.length>250||sample.pages<1||sample.pages>5||sample.answers.length!==sample.pages){
    throw new Error('Context matching requires bounded Record Lab samples.');
   }
   const key=plan.keys[0],expectedType=context.collectionId===series?sourceTypes[collection.id]:null;
   const index=new Map<string,typeof targetSample.rows>();
   let targetMissingKeys=0,namespaceExcluded=0;
   for(const row of targetSample.rows){
    const value=identifier(row.values,key.target);
    if(value===null){targetMissingKeys++;continue;}
    if(expectedType&&identifier(row.values,'data_type')!==expectedType){namespaceExcluded++;continue;}
    const matches=index.get(value)??[];matches.push(row);index.set(value,matches);
   }
   const compareFields=context.collectionId===series?['monitoring_location_id','parameter_code','statistic_id','unit_of_measure']
    .filter(field=>collection.columns.includes(field)&&target.columns.includes(field)):[];
   const rows=snapshot.rows.map(row=>{
    const value=identifier(row.values,key.source),matches=value===null?[]:index.get(value)??[];
    return {sourceRecordId:String(row.id),providerKey:value,
     status:value===null?'missing_key' as const:!matches.length?'no_match' as const:matches.length===1?'one_match' as const:'multiple_matches' as const,
     matches:matches.map(match=>{
      const conflicts:string[]=[],unverified:string[]=[];
      for(const field of compareFields){
       const a=identifier(row.values,field),b=identifier(match.values,field);
       if(a===null||b===null)unverified.push(field);
       else if(a!==b)conflicts.push(field);
      }
      return {targetRecordId:String(match.id),conflicts,unverified};
     })};
   });
   return {targetCollection:context.collectionId,title:target.title,keys:plan.keys,namespace:plan.namespace,
    expectedDataType:expectedType,checks:plan.checks,documentation:plan.documentation,
    targetSample:{rows:targetSample.rows.length,pages:targetSample.pages,hasMore:targetSample.hasMore,
     origin:targetSample.origin??'archive',retrievedAt:targetSample.answers.map(a=>a.generatedAt??null),
     stale:targetSample.answers.some(a=>a.cache?.state==='stale'),missingKeys:targetMissingKeys,namespaceExcluded},
    counts:{sourceRows:rows.length,oneMatch:rows.filter(r=>r.status==='one_match').length,
     multipleMatches:rows.filter(r=>r.status==='multiple_matches').length,noMatch:rows.filter(r=>r.status==='no_match').length,
     missingKey:rows.filter(r=>r.status==='missing_key').length,
     conflictingRows:rows.filter(r=>r.matches.some(m=>m.conflicts.length)).length,
     unverifiedRows:rows.filter(r=>r.matches.some(m=>m.unverified.length)).length},rows};
  })};
}
export type RecordContextReport=ReturnType<typeof connectRecordContexts>;
export function recordContextBrief(report:RecordContextReport){
 if(!report.relations.length)return '';
 return ['','## Connected metadata samples',report.scope,...report.interpretation,
  ...report.relations.flatMap(r=>[
   '',`### ${r.title}`,`${r.targetSample.rows} metadata records over ${r.targetSample.pages} page(s); ${r.targetSample.hasMore?'further metadata records remain.':'no further records were reported at that read.'}`,
   `Retrieval timestamps: ${r.targetSample.retrievedAt.map(t=>t??'Not supplied').join(', ')}. These are not observation dates.`,
   `Origin: ${r.targetSample.origin}. ${r.targetSample.stale?'Includes stale cached metadata.':''}`,
   `${r.counts.oneMatch} observation rows have one matching metadata record; ${r.counts.multipleMatches} have multiple matches; ${r.counts.noMatch} have no match in this sample; ${r.counts.missingKey} lack a provider key.`,
   `${r.counts.conflictingRows} rows have conflicting shared series fields; ${r.counts.unverifiedRows} lack at least one comparison field. ${r.targetSample.missingKeys} context rows lack a key; ${r.targetSample.namespaceExcluded} use another or unknown series data type.`,
   `Keys: ${r.keys.map(k=>`${k.source} -> ${k.target}`).join(', ')}${r.expectedDataType?`; data_type = ${r.expectedDataType}`:''}.`,
   ...r.checks,`Identity documentation: ${r.documentation.url}; SHA256 ${r.documentation.sha256}.`,
  ]),'','Per-record links, exact source rows, metadata definitions and provenance are retained in the lab JSON.'].join('\n');
}
