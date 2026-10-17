// Selected display context is an interpretation aid, never released evidence.
import {readFile,stat} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {gunzipSync} from 'node:zlib';
import {resolve} from 'node:path';
import {assistantSurface} from '../app/assistant-surfaces.mjs';
const object=x=>x!==null&&typeof x==='object'&&!Array.isArray(x);
const text=(x,max)=>typeof x==='string'&&x.length>0&&Buffer.byteLength(x)<=max&&!/[\x00-\x1f\x7f]/.test(x);
const shape=(x,keys)=>object(x)&&Object.keys(x).every(key=>keys.includes(key));
const fail=code=>{throw Object.assign(new Error(code),{code});};
const frame=x=>Number.isInteger(x)&&x>=-5e9&&x<=2200;
export function validAssistantContext(value){
 if(!shape(value,['version','frame','view','layers','selection','surface','filters','comparison'])||value.version!==1||!frame(value.frame)||!text(value.view,40)||!Array.isArray(value.layers)||value.layers.length>14||!value.layers.every(x=>text(x,160)))return false;
 if(value.surface!==undefined&&!assistantSurface(value.surface))return false;
 if(value.filters!==undefined&&(!shape(value.filters,['evidence','temporalMode'])||!['ALL','ANSWER','MISSING_EVIDENCE','SOURCE_STALE','GENERALIZED_GEOMETRY','RESTRICTED_ACCESS','DENIED_BY_POLICY','CORRECTED','SUPERSEDED','ERROR'].includes(value.filters.evidence)||!['snapshot','moving-window','event-stepping','accumulation','comparison'].includes(value.filters.temporalMode)))return false;
 if(value.comparison!==undefined&&(!shape(value.comparison,['frameA','frameB'])||!frame(value.comparison.frameA)||!frame(value.comparison.frameB)))return false;
 const s=value.selection;
 if(s===null)return true;
 if(!object(s))return false;
 if(s.kind==='knowledge')return shape(s,['kind','recordId'])&&text(s.recordId,128)&&/^[a-zA-Z0-9][a-zA-Z0-9._:-]*$/.test(s.recordId);
 if(s.kind==='registry')return shape(s,['kind','layerId','featureId'])&&text(s.layerId,160)&&text(s.featureId,160);
 if(s.kind==='subsurface')return shape(s,['kind','tileId','recordId','intervalIndex'])&&/^tile-[0-9]{1,3}-[0-9]{1,3}$/.test(s.tileId)&&text(s.recordId,160)&&(s.intervalIndex===null||Number.isInteger(s.intervalIndex)&&s.intervalIndex>=0&&s.intervalIndex<2000);
 // A provider's browser snapshot is explicitly unverified; no attributes,
 // coordinates, release fields, URLs or EvidenceRefs can be injected here.
 if(s.kind==='display')return shape(s,['kind','title','source','description','time'])&&text(s.title,240)&&text(s.source,160)&&text(s.description,600)&&text(s.time,160);
 return false;
}
/** @param {{catalog?:(selector:any)=>any,knowledge?:(selector:any)=>any,layers?:(ids:string[])=>string[],publicRoot?:string}} options */
export function createAssistantContextResolver({catalog=()=>null,knowledge=()=>null,layers=()=>[],publicRoot=resolve('public')}={}){
 const asset=async(path,limit)=>{
  if(!/^\/data\/subsurface\/[a-zA-Z0-9._-]+$/.test(path))fail('CONTEXT_UNAVAILABLE');
  const file=resolve(publicRoot,'.'+path),info=await stat(file);
  if(!info.isFile()||info.size>limit)fail('CONTEXT_UNAVAILABLE');
  return readFile(file);
 };
 return async context=>{
  if(!validAssistantContext(context))fail('INVALID_CONTEXT');
  const surface=assistantSurface(context.surface??'map');
  const frame=(surface?.id==='map'||['reports','stories'].includes(surface?.id??'')?'Map year '+context.frame+'; view '+context.view+'. ':'Page '+surface?.title+'. ')
   +(context.filters?'Display filters '+JSON.stringify(context.filters)+'. ':'')
   +(context.comparison?'Comparison frames '+context.comparison.frameA+' and '+context.comparison.frameB+'; matching observations are not established. ':'');
  const layerNames=layers(context.layers).slice(0,8).join(', ');
  const s=context.selection;
  if(!s)return {key:JSON.stringify(context),prompt:frame+'No record selected. Recognized layers: '+(layerNames||'none')+'. Interface guide: '+surface?.guide,label:surface?.title??'Map view',boundary:'Application guide and display context only'};
  if(s.kind==='knowledge'){
   const record=await knowledge(s);
   if(!record||!/^sha256:[a-f0-9]{64}$/.test(record.releaseId??''))fail('CONTEXT_UNAVAILABLE');
   return {key:JSON.stringify(context)+record.releaseId,prompt:'Released record context; generated interpretation is not a factual answer. '+record.prompt,label:record.title,boundary:'Released record references; model interpretation remains unverified',releaseId:record.releaseId,references:record.references};
  }
  if(s.kind==='display')return {key:JSON.stringify(context),prompt:frame+'Unverified browser display snapshot: '+JSON.stringify(s),label:s.title,boundary:'Unverified display snapshot; no released evidence'};
  if(s.kind==='registry'){
   const record=await catalog(s);
   if(!record)fail('CONTEXT_UNAVAILABLE');
   if(record.denied)fail('POLICY_WITHHELD');
   if(record.year!==context.frame&&record.exactTime)fail('CONTEXT_TIME_MISMATCH');
   return {key:JSON.stringify(context),prompt:frame+record.prompt,label:record.title,boundary:'Server-resolved catalog context; no evidence promotion'};
  }
  const manifest=JSON.parse((await asset('/data/subsurface/manifest.json',500000)).toString('utf8'));
  if(manifest.version!==1||!Array.isArray(manifest.tiles)||!Array.isArray(manifest.sources))fail('CONTEXT_UNAVAILABLE');
  const tile=manifest.tiles.find(t=>t.id===s.tileId);
  if(!tile||!/^[a-f0-9]{64}$/.test(tile.sha256))fail('CONTEXT_UNAVAILABLE');
  const bytes=await asset(tile.url,5000000);
  if(createHash('sha256').update(bytes).digest('hex')!==tile.sha256)fail('CONTEXT_UNAVAILABLE');
  const decoded=tile.url.endsWith('.gz')?gunzipSync(bytes,{maxOutputLength:25000000}):bytes;
  if(tile.decodedSha256&&createHash('sha256').update(decoded).digest('hex')!==tile.decodedSha256)fail('CONTEXT_UNAVAILABLE');
  const records=JSON.parse(decoded.toString('utf8'));
  if(!Array.isArray(records))fail('CONTEXT_UNAVAILABLE');
  const r=records.find(r=>r.id===s.recordId&&['kgs-wwc5','kgs-core'].includes(r.sourceId));
  if(!r||!Array.isArray(r.intervals)||!['ft','m'].includes(r.depthUnit))fail('CONTEXT_UNAVAILABLE');
  const interval=s.intervalIndex===null?null:r.intervals[s.intervalIndex];
  if(s.intervalIndex!==null&&!interval)fail('CONTEXT_UNAVAILABLE');
  // Inventory edition and drilling/log date have different meanings.
  const year=Number(/^\d{4}/.exec(r.sourceTime??'')?.[0]);
  if(context.frame<new Date().getUTCFullYear()&&(!year||year>context.frame))fail('CONTEXT_TIME_MISMATCH');
  const source=manifest.sources.find(source=>source.id===r.sourceId);
  if(!source)fail('CONTEXT_UNAVAILABLE');
  const detail=interval?{top:interval.top,bottom:interval.bottom,unit:r.depthUnit,description:String(interval.description).slice(0,500),interpreted:String(interval.interpreted??'').slice(0,120)}:{totalDepth:r.totalDepth,unit:r.depthUnit,intervalCount:r.intervals.length};
  const prompt=frame+'Public KGS source context, NOT admitted evidence. Record '+r.id+'; '+source.title+'; record time '+r.sourceTime+'; archive edition '+source.sourceTime+'. '+JSON.stringify(detail)+'. '+(r.kind==='core'?'Core inventory range does not prove recovery or continuous rock.':'Original logged description; interpreted codes are interpretations. Unknown gaps remain unknown; no continuous geology.');
  const references=[];
  for(const url of [r.sourceUrl,source.url]){
   try{const parsed=new URL(url);if(parsed.protocol==='https:'&&!parsed.username&&!parsed.password&&(parsed.hostname==='kgs.ku.edu'||parsed.hostname.endsWith('.kgs.ku.edu'))&&!references.some(ref=>ref.url===parsed.href))references.push({label:references.length?'Source archive · '+source.sourceTime:source.title,url:parsed.href,role:'SOURCE_CONTEXT'});}catch{/* An absent/unsafe source link is never invented. */}
  }
  return {key:JSON.stringify(context)+':'+tile.sha256,prompt,label:r.id,boundary:'KGS public source context; not admitted evidence',references};
 };
}
