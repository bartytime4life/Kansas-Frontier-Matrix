import {waterQualityDimensions} from './water-quality-context';
import {collectionMetadata,fieldRole,type Collection} from './collection-metadata';
import {documentedField,collectionFieldNotes,recordedUnit,recordedReference} from './collection-field-dictionary';
import {fetchArchive,validArchiveGeometry,type ArchiveAnswer,type ArchiveRow} from './archive-layer-data';

export const LAB_MAX_ROWS=250,LAB_MAX_PAGES=5;
const MAX_DISTRIBUTION_BINS = 6;
const object=(v:unknown):v is Record<string,unknown> => !!v&&typeof v==='object'&&!Array.isArray(v);
const missing=(v:unknown)=>v===null||v===undefined||typeof v==='string'&&!v.trim();
function numeric(v:unknown):number|null{
 if(typeof v==='string'){
  if(!/^[+-]?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?$/.test(v.trim()))return null;
  v=Number(v.trim());
 }
 return typeof v==='number'&&Number.isFinite(v)&&(!Number.isInteger(v)||Number.isSafeInteger(v))?v:null;
}
const defaultDimensions = [
 'unit', 'units', 'unit_name', 'measurement_unit', 'result_measure_unit_code',
 'variable', 'parameter_cd', 'parameter', 'element', 'characteristic_name', 'measureid',
 'qualifier', 'quality_flag', 'remark_cd', 'censoring_code', 'result_detection_condition',
];
const aqsObservationDimensions = [
 'parameter_code', 'parameter_name', 'sample_duration', 'pollutant_standard', 'event_type',
];
const aqsConcentrationDimensions = [...aqsObservationDimensions, 'units_of_measure'];

// The catalog uses provider-specific column names. Context for one numeric field
// must not supply the unit for another field on the same record.
const collectionDimensions: Partial<Record<string, Readonly<Record<string, readonly string[]>>>> = {
 'observations-usgs-sites':{
  drainage_area:['site_type_code'],contributing_drainage_area:['site_type_code'],
  altitude:['altitude_accuracy','site_type_code'],
  well_constructed_depth:['aquifer_type_code'],hole_constructed_depth:['aquifer_type_code'],
 },
 'observations-faa-obstacles': {
  quantity:['verification_status'],
  agl_height_ft:['verification_status','horizontal_accuracy','vertical_accuracy'],
  amsl_height_ft:['verification_status','horizontal_accuracy','vertical_accuracy'],
 },
 'observations-usgs-daily-values': {
  value: ['parameter_code', 'statistic_id', 'unit_of_measure', 'approval_status', 'qualifier'],
 },
 'observations-usgs-field-measurements': {
  value: ['parameter_code', 'unit_of_measure', 'kind', 'reading_type', 'vertical_datum', 'approval_status', 'qualifier',
   'observing_procedure_code','observing_procedure','sublocation_identifier','measuring_agency','control_condition','measurement_rated'],
 },
 'observations-usgs-peaks': {
  value: ['parameter_code', 'unit_of_measure', 'qualifier','peak_since'],
 },
 'observations-aqs-daily': {
  arithmetic_mean: aqsConcentrationDimensions,
  first_max_value: aqsConcentrationDimensions,
  observation_count: aqsObservationDimensions,
  observation_percent: aqsObservationDimensions,
  aqi: aqsObservationDimensions,
 },
 ...waterQualityDimensions,
};

function groupKey(collection: Collection, field: string, values: Record<string, unknown>) {
 const definition=documentedField(collection.id,field);
 const dimensionsByField = collectionDimensions[collection.id];
 const dimensionFields = dimensionsByField ? dimensionsByField[field] ?? [] : defaultDimensions;
 const dimensions = dimensionFields
  .filter(key => !missing(values[key]) && ['string', 'number'].includes(typeof values[key]))
  .map(key => [key, String(values[key])]);
 const context={...(definition?.unit?{unit:definition.unit}:{}),
  ...(definition?.reference||definition?.referenceField?{reference:recordedReference(collection.id,field,values)??'Not supplied'}:{}),...Object.fromEntries(dimensions)};
 return Object.keys(context).length ? JSON.stringify(context) : 'Unit and measurement context not supplied';
}
const safeUrl=(v:unknown)=>{try{if(typeof v!=='string')return null;const u=new URL(v);return u.protocol==='https:'&&!u.username&&!u.password?u.href:null;}catch{return null;}};
type LabRead = Pick<ArchiveAnswer, 'cache'> & {
 generatedAt?: string;
 source?: Pick<ArchiveAnswer['source'], 'provider'>;
};
export type LabSnapshot={answers:LabRead[];rows:ArchiveRow[];hasMore:boolean;pages:number;origin?:'saved-bundle'};
const SAVED_BUNDLE_NOTE = 'These records came from a user-supplied file. Its source references and retrieval times have not been independently checked.';
type DistributionRecord = { id: string; value: number; sourceId: string | null; sourceUrl: string | null };
export type MeasurementBin = {
 lower: number;
 upper: number;
 includeUpper: boolean;
 count: number;
 records: DistributionRecord[];
};
export type MeasurementDistribution = { count: number; bins: MeasurementBin[] };

function isMeasurementField(collection: Collection, field: string) {
 return collection.columns.includes(field) && fieldRole(field, collection.keys,collection.id) === 'value';
}

/** All eligible contexts in the bounded loaded sample, in first-seen order. */
export function measurementContexts(
 collection: Collection,
 snapshot: LabSnapshot,
 field: string,
): { context: string; count: number }[] {
 if (!isMeasurementField(collection, field)) return [];
 const counts = new Map<string, number>();
 for (const row of snapshot.rows) {
  if (!object(row.values) || numeric(row.values[field]) === null) continue;
  const context = groupKey(collection, field, row.values);
  counts.set(context, (counts.get(context) ?? 0) + 1);
 }
 return [...counts].map(([context, count]) => ({ context, count }));
}

function binBoundaries(min: number, max: number, count: number) {
 // Fewer bins keep boundaries distinct when adjacent values are very close.
 for (let size = count; size > 1; size--) {
  const edges = Array.from({ length: size + 1 }, (_, index) =>
   index === size ? max : min + (max - min) * (index / size)
  );
  if (edges.every((edge, index) => index === 0 || edge > edges[index - 1])) return edges;
 }
 return [min, max];
}

/** Profile one measurement context using the same recorded values as the lab summary. */
export function measurementDistribution(
 collection: Collection,
 snapshot: LabSnapshot,
 field: string,
 context: string,
): MeasurementDistribution {
 if (!isMeasurementField(collection, field)) return { count: 0, bins: [] };
 const records: DistributionRecord[] = [];
 let minimum = Infinity;
 let maximum = -Infinity;
 for (const row of snapshot.rows) {
  if (!object(row.values) || typeof row.id !== 'string') continue;
  const value = numeric(row.values[field]);
  if (value === null || groupKey(collection, field, row.values) !== context) continue;
  const provenance = object(row.provenance) ? row.provenance : {};
  records.push({
   id: row.id,
   value,
   sourceId: typeof provenance.source_id === 'string' ? provenance.source_id : null,
   sourceUrl: safeUrl(provenance.source_url),
  });
  minimum = Math.min(minimum, value);
  maximum = Math.max(maximum, value);
 }
 if (records.length === 0) return { count: 0, bins: [] };

 const desiredBins = Math.min(MAX_DISTRIBUTION_BINS, Math.ceil(Math.sqrt(records.length)));
 const boundaries = minimum === maximum ? [minimum, maximum] : binBoundaries(minimum, maximum, desiredBins);
 const bins: MeasurementBin[] = boundaries.slice(0, -1).map((lower, index) => ({
  lower,
  upper: boundaries[index + 1],
  includeUpper: index === boundaries.length - 2,
  count: 0,
  records: [],
 }));
 for (const record of records) {
  const bin = bins.find(candidate => record.value < candidate.upper) ?? bins[bins.length - 1];
  bin.records.push(record);
  bin.count++;
 }
 return { count: records.length, bins };
}

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
  const role=fieldRole(name,c.keys,c.id),definition=documentedField(c.id,name),groups=new Map<string,number[]>();let present=0,numericCount=0,longFields=0;
  const exampleValues:string[]=[];
  for(const row of rows){
   const values=object(row.values)?row.values:{},value=values[name];
   if(missing(value))continue;present++;
   if(object(value)&&value.longField===true){longFields++;continue;}
   if(role==='time'&&exampleValues.length<6&&!exampleValues.includes(String(value)))exampleValues.push(String(value));
   const n=role==='value'?numeric(value):null;
   if(n!==null){numericCount++;const key=groupKey(c,name,values);const list=groups.get(key)??[];list.push(n);groups.set(key,list);}
  }
  const summary=[...groups].slice(0,12).map(([context,values])=>{
   values.sort((a,b)=>a-b);const mid=Math.floor(values.length/2);
   const mean=values.reduce((total,v)=>total+v/values.length,0);
   return {context,count:values.length,min:values[0],max:values.at(-1)!,mean:Number.isFinite(mean)?mean:null,median:values.length%2?values[mid]:values[mid-1]/2+values[mid]/2};
  });
  return {name,role,definition:definition?.definition??null,unit:definition?.unit??null,unitField:definition?.unitField??null,reference:definition?.reference??null,
   present,missing:rows.length-present,numericCount,longFields,exampleValues,groups:summary,additionalGroups:Math.max(0,groups.size-summary.length)};
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
 const providerIds=new Map<string,number>();let missingProviderIdentity=0;
 if(base.providerIdentity)for(const row of rows){
  const values=object(row.values)?row.values:{};
  const keys=base.providerIdentity.fields.map(key=>values[key]);
  if(keys.some(value=>typeof value!=='string'||!value.trim())){missingProviderIdentity++;continue;}
  const key=JSON.stringify(keys);providerIds.set(key,(providerIds.get(key)??0)+1);
 }
 const providerIdentity=base.providerIdentity?{...base.providerIdentity,distinct:providerIds.size,
  repeatedIdentifiers:[...providerIds.values()].filter(n=>n>1).length,
  additionalRows:[...providerIds.values()].reduce((n,count)=>n+count-1,0),missing:missingProviderIdentity,
  scope:'Loaded metadata rows only. Repeated provider IDs are retained; no deduplication, current-version selection or joined observation is established.'}:null;
 return {format:'kfm-collection-profile-v1',collection:{...base,
  temporal:{...base.temporal,retrievedAt:snapshot.answers.map(a=>a.generatedAt??null)},
  provenance:{...base.provenance,provider:providers.length===1?providers[0]:null,sourceUrls:[...new Set(lineage.flatMap(p=>p.url?[p.url]:[]))],digests:[...new Set(lineage.flatMap(p=>p.sha256?[p.sha256]:[]))]}},sample:{rows:rows.length,pages:snapshot.pages,hasMore:snapshot.hasMore,
  scope:snapshot.origin?'Records retained in the saved bundle. The file provides the capture metadata.':'First identity-ordered pages; not a random sample, spatial search, trend or collection total.',
  inputOrigin:snapshot.origin??'archive',
  retrievedAt:snapshot.answers.map(a=>a.generatedAt??null),cache:snapshot.answers.map(a=>a.cache??null),
  stale:snapshot.answers.some(a=>a.cache?.state==='stale'),recordIds:rows.map(r=>r.id)},
  fields,providerIdentity,spatial:{mappable,unavailableGeometry,withoutUsableGeometry:c.geometry?rows.length-mappable:null,sampleBoundingBox:mappable?bounds:null},provenance:lineage,
  interpretation:[...(snapshot.origin?[SAVED_BUNDLE_NOTE]:[]),
   'Numeric summaries describe the loaded values only. Original sentinel values and quality flags are not reinterpreted.',
   'Units and measurement identifiers are profiled in separate groups. Unitless groups need source documentation.',
   'Identifiers, dates, locations, categories and quality flags are excluded from measurement statistics.',
   ...collectionFieldNotes(c.id)],
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
  ...(profile.providerIdentity?[`Provider identity sample: ${profile.providerIdentity.distinct} distinct identifiers; ${profile.providerIdentity.additionalRows} additional rows repeat an identifier; ${profile.providerIdentity.missing} rows lack a complete provider identity. ${profile.providerIdentity.scope}`]:[]),
  '', '## Recorded values',...(measurements.slice(0,20).length?measurements.slice(0,20):['No eligible numeric measurements were returned. Inspect source records and field definitions.']),
  ...(measurements.length>20?['Additional measurement groups remain in the profile export.']:[]),
  ...(profile.fields.some(f=>f.additionalGroups>0)?['Some fields exceed the 12-group summary. Omitted-group counts are in the profile; all original values remain in the record export.']:[]),
  '', '## Source time fields',...profile.fields.filter(f=>f.role==='time'&&f.exampleValues.length).map(f=>`- ${f.name}: ${f.exampleValues.join('; ')} (recorded examples, not a complete range or a verified temporal meaning).`),
  ...(profile.collection.documentation.length?['','## Field definitions and units',
   ...profile.collection.fields.filter(f=>f.definition&&profile.fields.some(p=>p.name===f.name&&(p.groups.length||p.role==='time'||p.role==='quality')))
    .map(f=>`- ${f.name}: ${f.definition}${f.unit?` Unit: ${f.unit}.`:''}${f.unitField?` Unit source: each record's ${f.unitField} field.`:''}${f.reference?` Reference: ${f.reference}.`:''}${f.referenceField?` Reference source: each record's ${f.referenceField} field.`:''}${f.encoding?` Encoding: ${f.encoding}.`:''}`),
   '', '## Field documentation',...profile.collection.documentation.map(d=>
    `- [${d.title}](${d.url})${d.edition?`; documentation edition ${d.edition}`:''}; checked ${d.checkedAt}${d.sha256?`; SHA256 ${d.sha256}`:''}. ${d.scope}`)]:[]),
  ...(profile.collection.relationships.length?['','## Station and series context',
   'These are comparison plans, not joined records. Verify provider namespaces, capture versions and measurement conventions.',
   ...profile.collection.relationships.map(r=>`- [${r.title}](/data-library?collection=${encodeURIComponent(r.targetCollection)}): ${r.keys.map(k=>`${k.source} -> ${k.target}`).join(', ')}. ${r.checks.join(' ')}`)]:[]),
  '', '## Source lineage',
  ...profile.provenance.map(p=>`- ${p.sourceId??'Source ID not supplied'}; ${p.url??'Source URL not supplied'}; SHA256 ${p.sha256??'not supplied'}`),
  ...(!profile.provenance.length?['Source lineage was not supplied for these records.']:[]),
  '', '## Limits and next steps',...profile.interpretation.map(v=>`- ${v}`),
  '- Verify field definitions, source dates, geographic identifiers and editions before comparison or causal interpretation.',
  '', 'Credit: deterministic KFM record profile. No AI review or approval is established by this brief.',
  '',`Collection: ${collectionMetadata(c).access.library}`,`Record identities: ${profile.sample.recordIds.join('; ')}`].join('\n');
}

/** A separate unit/measurement group becomes one reusable GeoJSON layer. */
export function measurementLayer(c:Collection,snapshot:LabSnapshot,field:string,context:string){
 if(!c.geometry||!isMeasurementField(c,field))throw new Error('Choose a measurement field in a geometry collection.');
 const metadata=collectionMetadata(c),definition=metadata.fields.find(f=>f.name===field)!;
 const features=[];const omitted={otherContext:0,notNumeric:0,noUsableGeometry:0};
 for(const row of snapshot.rows){
  const values=object(row.values)?row.values:{};
  if(groupKey(c,field,values)!==context){omitted.otherContext++;continue;}
  const value=numeric(values[field]);if(value===null){omitted.notNumeric++;continue;}
  let candidate=values[c.geometry];try{if(typeof candidate==='string')candidate=JSON.parse(candidate);}catch{candidate=null;}
  const geometry=validArchiveGeometry(candidate);
  if(!geometry||geometry.type==='Point'&&geometry.coordinates[0]===0&&geometry.coordinates[1]===0){omitted.noUsableGeometry++;continue;}
  const p=object(row.provenance)?row.provenance:{};
  features.push({type:'Feature' as const,id:String(row.id),geometry,properties:{record_id:String(row.id),collection:c.id,field,value,measurement_context:context,
   unit:recordedUnit(c.id,field,values),reference:recordedReference(c.id,field,values),
   source_id:typeof p.source_id==='string'?p.source_id:null,source_url:safeUrl(p.source_url),source_sha256:typeof p.sha256==='string'?p.sha256:null}});
 }
 return {type:'FeatureCollection' as const,features,kfm:{format:'kfm-lab-measurement-layer-v1',collection:c.id,field,context,omitted,
  fieldDefinition:definition,contextDefinitions:metadata.fields.filter(f=>[...(collectionDimensions[c.id]?.[field]??[]),definition.referenceField].includes(f.name)),
  documentation:metadata.documentation,interpretation:metadata.fieldNotes,
  rowsRead:snapshot.rows.length,hasMore:snapshot.hasMore,retrievalTimes:snapshot.answers.map(a=>a.generatedAt??null),
  inputOrigin:snapshot.origin??'archive',...(snapshot.origin?{sourceNote:SAVED_BUNDLE_NOTE}:{}),
  stale:snapshot.answers.some(a=>a.cache?.state==='stale'),scope:'Loaded identity-ordered records only; validated longitude/latitude XY geometry and recorded numeric values. No geocoding, reprojection or unit conversion. Original geometry remains in the lab record export.',
  reviewCredit:null,approval:null}};
}
