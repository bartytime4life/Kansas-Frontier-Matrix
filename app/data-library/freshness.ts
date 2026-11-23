// Freshness read from the public catalog (/api/local-data): when the pipeline PC last retrieved the
// newest file behind each dataset and each recovered collection, so "no match" can be told from
// "not loaded yet". The catalog carries it only when the PC has answered health recently; the
// connection flag is separate from those historical load dates.
import {readBoundedJson} from '../bounded-json';
export type Freshness={retrievedAt:string|null;modifiedAt:string|null;sourceId:string|null;file:number|null;basis?:string}|{reason:string;basis?:string};
export type DatasetStatus={ready:boolean;reason?:string;freshness:Freshness|null};
export type CatalogFreshness={state:'live'|'fresh'|'stale'|null;at:string|null;online:boolean;datasets:Map<string,DatasetStatus>;collections:Map<string,Freshness|null>};

const record=(v:unknown):v is Record<string,unknown>=>!!v&&typeof v==='object'&&!Array.isArray(v);
const ISO=/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,3})?Z$/;
const stamp=(v:unknown)=>typeof v==='string'&&ISO.test(v)&&Number.isFinite(Date.parse(v));
const optionalStamp=(v:unknown)=>v===null||stamp(v);

export function readFreshness(value:unknown):Freshness|null{
 if(!record(value))return null;
 if(typeof value.reason==='string')return {reason:value.reason.slice(0,40),...(typeof value.basis==='string'?{basis:value.basis.slice(0,20)}:{})};
 if(!optionalStamp(value.retrievedAt)||!optionalStamp(value.modifiedAt))return null;
 if(value.sourceId!==null&&typeof value.sourceId!=='string')return null;
 if(value.file!==null&&!Number.isSafeInteger(value.file))return null;
 return {retrievedAt:value.retrievedAt as string|null,modifiedAt:value.modifiedAt as string|null,sourceId:typeof value.sourceId==='string'?value.sourceId.slice(0,80):null,file:value.file as number|null,...(typeof value.basis==='string'?{basis:value.basis.slice(0,20)}:{})};
}

/** The catalog may report connection status before it has any load dates. */
export function readCatalogFreshness(value:unknown):CatalogFreshness|null{
 if(!record(value)||value.format!=='kfm-local-data-catalog-v1'||typeof value.online!=='boolean'||!Array.isArray(value.datasets))return null;
 const status=value.status;
 const datasets=new Map<string,DatasetStatus>();
 const collections=new Map<string,Freshness|null>();
 if(status===undefined)return {state:null,at:null,online:value.online,datasets,collections};
 if(!record(status)||(status.state!=='live'&&status.state!=='fresh'&&status.state!=='stale')||!stamp(status.at))return null;
 for(const d of value.datasets){
  if(!record(d)||typeof d.id!=='string'||typeof d.ready!=='boolean')continue;
  datasets.set(d.id,{ready:d.ready,...(typeof d.reason==='string'?{reason:d.reason.slice(0,40)}:{}),freshness:readFreshness(d.freshness)});
 }
 if(record(status.collections))for(const [id,f] of Object.entries(status.collections))if(/^[a-z][a-z0-9-]{0,80}$/.test(id))collections.set(id,readFreshness(f));
 return {state:status.state,at:status.at as string,online:value.online,datasets,collections};
}

/** The day the newest file was retrieved, else the provider's own date, as YYYY-MM-DD; null when unknown. */
export function loadedThrough(f:Freshness|null|undefined):string|null{
 if(!f||'reason' in f)return null;
 const at=f.retrievedAt??f.modifiedAt;
 return at?at.slice(0,10):null;
}

/** One line for a collection or dataset: what was loaded when, from the pipeline's own receipts. */
export function freshnessLine(f:Freshness|null|undefined):string{
 if(!f)return 'Load date not reported.';
 if('reason' in f){
  if(f.reason==='COLLECTION_FILE_KEY_MISSING')return 'This collection has no file-level retrieval metadata.';
  if(f.reason==='INDEX_MISSING')return 'Load date not indexed on the PC yet.';
  if(f.reason==='NO_FILES')return 'No file loaded yet.';
  return 'Load date not available.';
 }
 const parts=[];
 if(f.retrievedAt)parts.push(`newest file retrieved ${f.retrievedAt.slice(0,10)}`);
 if(f.modifiedAt)parts.push(`provider's version of ${f.modifiedAt.slice(0,10)}`);
 if(!parts.length)return 'Loaded, date not recorded.';
 return parts.join(', ')+(f.sourceId?` (${f.sourceId})`:'')+'.';
}

export async function fetchCatalogFreshness(signal:AbortSignal,fetcher=fetch):Promise<CatalogFreshness|null>{
 const response=await fetcher('/api/local-data',{signal,credentials:'same-origin'});
 if(!response.ok){void response.body?.cancel().catch(()=>undefined);return null;}
 let value:unknown;
 try{value=await readBoundedJson(response,256_000,signal);}catch{return null;}
 return readCatalogFreshness(value);
}
