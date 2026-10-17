// Selected display context is an interpretation aid, never released evidence.
import {readFile,stat} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {gunzipSync} from 'node:zlib';
import {resolve} from 'node:path';
const object=x=>x!==null&&typeof x==='object'&&!Array.isArray(x);
const text=(x,max)=>typeof x==='string'&&x.length>0&&Buffer.byteLength(x)<=max&&!/[\x00-\x1f\x7f]/.test(x);
const shape=(x,keys)=>object(x)&&Object.keys(x).every(key=>keys.includes(key));
const fail=code=>{throw Object.assign(new Error(code),{code});};
export function validAssistantContext(value){
 if(!shape(value,['version','frame','view','layers','selection'])||value.version!==1||!Number.isInteger(value.frame)||value.frame< -5e9||value.frame>2200||!text(value.view,40)||!Array.isArray(value.layers)||value.layers.length>14||!value.layers.every(x=>text(x,160)))return false;
 const s=value.selection;
 if(s===null)return true;
 if(!object(s))return false;
 if(s.kind==='registry')return shape(s,['kind','layerId','featureId'])&&text(s.layerId,160)&&text(s.featureId,160);
 if(s.kind==='subsurface')return shape(s,['kind','tileId','recordId','intervalIndex'])&&/^tile-[0-9]{1,3}-[0-9]{1,3}$/.test(s.tileId)&&text(s.recordId,160)&&(s.intervalIndex===null||Number.isInteger(s.intervalIndex)&&s.intervalIndex>=0&&s.intervalIndex<2000);
 // A provider's browser snapshot is explicitly unverified; no attributes,
 // coordinates, release fields, URLs or EvidenceRefs can be injected here.
 if(s.kind==='display')return shape(s,['kind','title','source','description','time'])&&text(s.title,240)&&text(s.source,160)&&text(s.description,600)&&text(s.time,160);
 return false;
}
/** @param {{catalog?:(selector:any)=>any,publicRoot?:string}} options */
export function createAssistantContextResolver({catalog=()=>null,publicRoot=resolve('public')}={}){
 const asset=async(path,limit)=>{
  if(!/^\/data\/subsurface\/[a-zA-Z0-9._-]+$/.test(path))fail('CONTEXT_UNAVAILABLE');
  const file=resolve(publicRoot,'.'+path),info=await stat(file);
  if(!info.isFile()||info.size>limit)fail('CONTEXT_UNAVAILABLE');
  return readFile(file);
 };
 return async context=>{
  if(!validAssistantContext(context))fail('INVALID_CONTEXT');
  const frame='Map display year '+context.frame+' (not a collection or drilling date); view '+context.view+'. ';
  const s=context.selection;
  if(!s)return {key:JSON.stringify(context),prompt:frame+'No record selected. Visible layer IDs: '+context.layers.join(', '),label:'Map view',boundary:'Display context only'};
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
  // A small generative model is not qualified to turn inventory dates/ranges
  // into claims about collection, recovery or surrounding geology. Return a
  // deterministic source summary instead of generating a factual explanation.
  const depth=value=>Number.isFinite(value)&&value>=0?String(value):'not supplied';
  const description=value=>typeof value==='string'?value.replace(/[\x00-\x1f\x7f]/g,' ').slice(0,500):'not supplied';
  const sourceSummary=[
   'Source: '+description(source.title)+'. Record: '+r.id+'.',
   'Map display year: '+context.frame+'. Source record time: '+description(r.sourceTime)+'. Archive edition: '+description(source.sourceTime)+'. These dates do not establish a collection or drilling date.',
   interval?'Selected recorded interval: '+depth(interval.top)+'–'+depth(interval.bottom)+' '+r.depthUnit+'. Original source description: '+description(interval.description)+'.'+(interval.interpreted?' KGS interpretation: '+description(interval.interpreted)+'.':''):'Recorded '+(r.kind==='core'?'inventory':'log')+' depth: '+depth(r.totalDepth)+' '+r.depthUnit+'. Source intervals: '+r.intervals.length+'.',
   r.kind==='core'?'Collection/drilling date and recovery are not established by this inventory context. An archived range does not prove continuous rock or surrounding geology.':'A log describes its recorded location. Unknown gaps and surrounding geology remain unknown.',
   'Source context only, not admitted evidence. Unsupported questions are withheld; this summary does not establish engineering suitability, resource extent or permissions.'
  ].join(' ');
  return {key:JSON.stringify(context)+':'+tile.sha256,prompt,sourceSummary,label:r.id,boundary:'KGS public source context; not admitted evidence'};
 };
}
