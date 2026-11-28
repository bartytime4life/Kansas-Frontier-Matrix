import type {Collection} from '../collection-metadata';
import type {LabSnapshot} from '../collection-lab';

const object=(value:unknown):value is Record<string,unknown>=>Boolean(value)&&typeof value==='object'&&!Array.isArray(value);

// These fields were measurements under the generic name hints in f9720f9761865a72600812e66bc9b485a95a3ba0.
// Keep this allowlist independent of new dictionary roles. Item 68 was already
// classified as location, and date items 90/93 were already time fields.
const previousMeasurements=new Set([
 'record_type_005a','design_load_031',
 'deck_cond_058','superstructure_cond_059','substructure_cond_060','channel_cond_061','culvert_cond_062',
 'opr_rating_meth_063','inv_rating_meth_065','bridge_condition','lowest_rating','structural_eval_067','undclrence_eval_069',
 'posting_eval_070','waterway_eval_071','appr_road_eval_072','fracture_092a','undwater_look_see_092b','spec_inspect_092c',
]);

// Frozen generic context order. Old bundles can retain these keys in their
// original records even though the native NBI catalog does not declare them.
const dimensions=[
 'unit','units','unit_name','measurement_unit','result_measure_unit_code',
 'variable','parameter_cd','parameter','element','characteristic_name','measureid',
 'qualifier','quality_flag','remark_cd','censoring_code','result_detection_condition',
];

function numeric(value:unknown):number|null{
 if(typeof value==='string'){
  if(!/^[+-]?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?$/.test(value.trim()))return null;
  value=Number(value.trim());
 }
 return typeof value==='number'&&Number.isFinite(value)&&(!Number.isInteger(value)||Number.isSafeInteger(value))?value:null;
}

function context(values:Record<string,unknown>){
 const entries=dimensions.filter(key=>{
  const value=values[key];return ['string','number'].includes(typeof value)&&String(value).trim();
 }).map(key=>[key,String(values[key])]);
 return entries.length?JSON.stringify(Object.fromEntries(entries)):'Unit and measurement context not supplied';
}

// Reproduce the old distribution's exact bin edges and precision fallback.
function boundaries(min:number,max:number,count:number){
 if(min===max)return [min,max];
 for(let size=Math.min(6,Math.ceil(Math.sqrt(count)));size>1;size--){
  const edges=Array.from({length:size+1},(_,index)=>index===size?max:min+(max-min)*(index/size));
  if(edges.every((edge,index)=>index===0||edge>edges[index-1]))return edges;
 }
 return [min,max];
}

/** Validate an obsolete NBI selection from its original rows before clearing it. */
export function previousNbiView(collection:Collection,snapshot:LabSnapshot,view:unknown,revision:unknown):boolean{
 if(collection.id!=='bulk-nbi-bridges'||revision!=null||snapshot.rows.length>250||!object(view)
  ||typeof view.field!=='string'||typeof view.context!=='string'||!collection.columns.includes(view.field)
  ||collection.keys.includes(view.field)||!previousMeasurements.has(view.field))return false;
 const groups=new Map<string,number[]>();
 for(const row of snapshot.rows){
  if(!object(row.values))continue;
  const value=numeric(row.values[view.field]);if(value===null)continue;
  const key=context(row.values),group=groups.get(key)??[];group.push(value);groups.set(key,group);
 }
 // Both first-twelve and all-context pickers emitted null dictionary revisions.
 // Accept any exact context from the bounded retained rows; do not change the
 // separately versioned historical USGS validators' first-twelve limits.
 const group=groups.get(view.context);
 if(!group?.length)return false;
 if(view.range===null)return true;
 if(!object(view.range)||typeof view.range.lower!=='number'||!Number.isFinite(view.range.lower)
  ||typeof view.range.upper!=='number'||!Number.isFinite(view.range.upper)||typeof view.range.includeUpper!=='boolean')return false;
 const range=view.range,edges=boundaries(Math.min(...group),Math.max(...group),group.length);
 return edges.slice(0,-1).some((lower,index)=>range.lower===lower&&range.upper===edges[index+1]&&range.includeUpper===(index===edges.length-2));
}
