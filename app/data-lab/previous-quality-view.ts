import type {Collection} from '../collection-metadata';
import {waterQualityV1Dimensions,waterQualityV2Dimensions} from '../water-quality-context';
import type {LabSnapshot} from '../collection-lab';

const V1='water-quality-2026-11-19-v1',V2='water-quality-2026-11-27-v2';
const object=(value:unknown):value is Record<string,unknown>=>Boolean(value)&&typeof value==='object'&&!Array.isArray(value);

// The v1 dictionary's non-measurement overrides, pinned to 9f910226d043941e349f1bb8aae9b53725bbf4d4.
// Remaining v1 columns used the generic name hints. New definitions must not alter this validator.
const nonMeasurements=new Set([
 'org_identifier','activity_activity_identifier','activity_type_code','activity_media','activity_media_subdivision',
 'activity_start_date','activity_start_time','activity_start_time_zone','activity_depth_height_measure_unit',
 'project_identifier','location_identifier','activity_comment','activity_hydrologic_condition','activity_hydrologic_event',
 'sample_collection_method_identifier','sample_collection_method_identifier_context','result_result_detection_condition',
 'result_characteristic','result_sample_fraction','result_measure_unit','result_measure_qualifier_code',
 'result_measure_status_identifier','result_statistical_base','result_measure_type','result_weight_basis',
 'result_time_basis','result_measure_temperature_basis','result_measure_particle_size_basis','data_quality_precision_value',
 'data_quality_result_comment','usgs_pcode','result_depth_height_measure_unit','result_biological_taxon',
 'result_biological_sample_tissue_anatomy','result_analytical_method_identifier','result_analytical_method_identifier_context',
 'result_analytical_method_name','lab_info_name','lab_info_analysis_start_date','lab_info_laboratory_comment',
 'detection_limit_type_a','detection_limit_measure_unit_a','provider_name',
 'result_method_speciation','result_characteristic_user_supplied','result_cas_number','result_measure_identifier',
 'result_depth_height_altitude_reference_point','activity_bottom_depth_altitude_reference_point','last_change_date',
 'detection_limit_type_b','detection_limit_measure_unit_b','detection_limit_comment_a','detection_limit_comment_b',
 'sample_collection_method_name','result_analytical_method_description','result_analytical_method_qualifier_type',
 'result_comparable_method_modification','result_comparable_method_identifier','result_comparable_method_identifier_context',
]);

// Frozen v1 name hints, applied only after its documented overrides above.
function wasValue(field:string,keys:readonly string[]){
 if(keys.includes(field)||/(_number(?:_\d+)?|_no|_identifier)$/i.test(field)
  ||/^(county|state|tract|block|site|station|block_group|variable|parameter|parameter_cd|element|measureid|characteristic_name)$/i.test(field)
  ||/(^|_)(id|ids|code|fips|geoid|zip|row_number|file_id|site_no|station_id|objectid|lccn)($|_)/i.test(field))return false;
 if(field==='first_max_hour'||/(^|_)(date|time|year|month|day|start|end|begin|issued|valid|edition)($|_)/i.test(field))return false;
 if(/geometry|latitude|longitude|(^|_)(lat|lon|lng|coordinates)($|_)/i.test(field))return false;
 if(/(^|_)(units?|unit_name)($|_)/i.test(field)||/flag|qualifier|quality|status|remark|censor|precision|uncertainty/i.test(field))return false;
 return true;
}

function number(value:unknown):number|null{
 if(typeof value==='string'){
  if(!/^[+-]?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?$/.test(value.trim()))return null;
  value=Number(value.trim());
 }
 return typeof value==='number'&&Number.isFinite(value)&&(!Number.isInteger(value)||Number.isSafeInteger(value))?value:null;
}

function context(field:string,values:Record<string,unknown>){
 const dimensions=waterQualityV1Dimensions['observations-usgs-samples-results'][field]??[];
 const reference=Object.hasOwn(values,'result_depth_height_altitude_reference_point')?values.result_depth_height_altitude_reference_point:null;
 const entries=dimensions.filter(key=>{
  const value=values[key];return ['string','number'].includes(typeof value)&&String(value).trim();
 }).map(key=>[key,String(values[key])]);
 const key={...(field==='result_depth_height_measure'?{
  reference:typeof reference==='string'&&reference.trim()?reference:'Not supplied',
 }:{}),...Object.fromEntries(entries)};
 return Object.keys(key).length?JSON.stringify(key):'Unit and measurement context not supplied';
}

// Reproduce v1's bounded bin edges, including its precision fallback.
function boundaries(min:number,max:number,count:number){
 if(min===max)return [min,max];
 for(let size=Math.min(6,Math.ceil(Math.sqrt(count)));size>1;size--){
  const edges=Array.from({length:size+1},(_,index)=>index===size?max:min+(max-min)*(index/size));
  if(edges.every((edge,index)=>index===0||edge>edges[index-1]))return edges;
 }
 return [min,max];
}

/** Validate a known v1 view from retained rows alone before resetting an obsolete selection. */
export function previousQualityView(collection:Collection,snapshot:LabSnapshot,view:unknown,revision:unknown):boolean{
 if(collection.id!=='observations-usgs-samples-results'||revision!==V1||!object(view)
  ||typeof view.field!=='string'||typeof view.context!=='string'||!collection.columns.includes(view.field)
  ||nonMeasurements.has(view.field)||!wasValue(view.field,collection.keys))return false;
 return matchesPreviousView(snapshot,view as PreviousView,context);
}

type PreviousView={field:string;context:string;range:unknown};
function matchesPreviousView(snapshot:LabSnapshot,view:PreviousView,makeContext:(field:string,values:Record<string,unknown>)=>string){
 const field=view.field,groups=new Map<string,number[]>();
 for(const row of snapshot.rows){
  if(!object(row.values))continue;
  const value=number(row.values[field]);if(value===null)continue;
  const key=makeContext(field,row.values),group=groups.get(key)??[];group.push(value);groups.set(key,group);
 }
 // Historical versions exposed only the first twelve measurement contexts in their profile and view picker.
 const group=[...groups].slice(0,12).find(([key])=>key===view.context)?.[1];
 if(!group?.length)return false;
 if(view.range===null)return true;
 if(!object(view.range)||typeof view.range.lower!=='number'||!Number.isFinite(view.range.lower)
  ||typeof view.range.upper!=='number'||!Number.isFinite(view.range.upper)||typeof view.range.includeUpper!=='boolean')return false;
 const range=view.range,edges=boundaries(Math.min(...group),Math.max(...group),group.length);
 return edges.slice(0,-1).some((lower,index)=>range.lower===lower&&range.upper===edges[index+1]&&range.includeUpper===(index===edges.length-2));
}

/** V2 changed only the two biology contexts; no other field or revision gets this fallback. */
export function previousBiologicalView(collection:Collection,snapshot:LabSnapshot,view:unknown,revision:unknown):boolean{
 if(collection.id!=='observations-usgs-samples-results'||revision!==V2||!object(view)
  ||typeof view.field!=='string'||typeof view.context!=='string'
  ||!['result_biological_group_summary_count','group_summary_weight_measure'].includes(view.field))return false;
 return matchesPreviousView(snapshot,view as PreviousView,(field,values)=>{
  const dimensions=waterQualityV2Dimensions['observations-usgs-samples-results'][field];
  const entries=dimensions.filter(key=>{
   const value=values[key];return ['string','number'].includes(typeof value)&&String(value).trim();
  }).map(key=>[key,String(values[key])]);
  // V2 count had a fixed count unit; weight used only its recorded per-row unit.
  const key={...(field==='result_biological_group_summary_count'?{unit:'count'}:{}),...Object.fromEntries(entries)};
  return Object.keys(key).length?JSON.stringify(key):'Unit and measurement context not supplied';
 });
}
