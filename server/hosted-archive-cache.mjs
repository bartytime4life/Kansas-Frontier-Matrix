// Only shared public catalogue/record pages. No searches, precise locations,
// live observations, AI conversations, raw databases or private state.
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
import {DATASETS} from '../scripts/local-data/datasets.mjs';
import {RECOVERED_COLLECTIONS} from '../scripts/local-data/recovered.mjs';
import {createSignedPublicCache} from './signed-public-cache.mjs';
export const HOSTED_ARCHIVE_LIMITS=Object.freeze({bytes:512*1024**2,entries:2048,entryBytes:1_004_096,reserveBytes:512*1024**2,freshMs:15*60000,staleMs:7*24*3600000});
const collections=new Map(RECOVERED_COLLECTIONS.map(c=>[c.id,c]));
const exact=(v,keys)=>v&&typeof v==='object'&&!Array.isArray(v)&&Object.keys(v).sort().join(',')===keys.split(',').sort().join(',');
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
// Inputs here are already normalized by the shared dataset parser. First pages
// are reusable across visitors; personalized searches and cursors stay out.
export function archiveQueryEligible(id,q){
 if(!q||typeof q!=='object'||Array.isArray(q))return false;
 if(id==='ghcndex-indices')return exact(q,'');
 if(id==='ghcn-stations')return exact(q,'name,bbox,element,limit,offset')&&q.name===null&&q.bbox===null&&q.element===null&&q.offset===0&&Number.isInteger(q.limit)&&q.limit>=1&&q.limit<=500;
 if(id==='wind-stations')return exact(q,'name,limit,offset')&&q.name===null&&q.offset===0&&Number.isInteger(q.limit)&&q.limit>=1&&q.limit<=100;
 if(id==='recovered-observations'||id==='recovered-bulk')return exact(q,'collection,after,limit,record,field,start')&&collections.get(q.collection)?.database===id.slice(10)&&q.after===null&&q.record===null&&q.field===null&&q.start===0&&Number.isInteger(q.limit)&&q.limit>=1&&q.limit<=50;
 return false;
}
export function archiveCacheKey(id,q){return archiveQueryEligible(id,q)?'archive:'+createHash('sha256').update(JSON.stringify([id,q])).digest('hex'):null;}
export function validArchiveAnswer(v){
 if(!v||!archiveQueryEligible(v.dataset,v.query))return false;
 const dataset=DATASETS.get(v.dataset),recovered=v.dataset.startsWith('recovered-');
 const keys='format,dataset,query,total,count,rows,source,generatedAt'+(recovered?',collection,hasMore,nextCursor,columns,coverage,geometryField':'');
 if(!exact(v,keys)||v.format!==(dataset.format??'kfm-local-data-v1')||!same(v.source,dataset.source)||typeof v.generatedAt!=='string'||!Number.isFinite(Date.parse(v.generatedAt))||!Array.isArray(v.rows)||!Number.isSafeInteger(v.count)||v.count!==v.rows.length||v.count>(v.query.limit??1000)||v.rows.some(row=>!row||typeof row!=='object'||Array.isArray(row)))return false;
 if(recovered){const c=collections.get(v.query.collection);return v.total===null&&v.collection===c.id&&same(v.columns,c.columns)&&v.geometryField===c.geometry&&typeof v.coverage==='string'&&typeof v.hasMore==='boolean'&&(v.nextCursor===null||typeof v.nextCursor==='string');}
 return Number.isSafeInteger(v.total)&&v.total>=v.count;
}
export function createHostedArchiveCache({root=resolve('public/assets/kfm-archive-cache-v1'),secret,origin,clock=Date.now,limits={}}={}){
 const store=createSignedPublicCache({root,secret,origin,clock,limits:{...HOSTED_ARCHIVE_LIMITS,...limits},format:'kfm-hosted-archive-cache-v1',keyPattern:/^archive:[a-f0-9]{64}$/,accept:validArchiveAnswer});
 return Object.freeze({...store,read:(key,validate)=>store.read(key,v=>archiveCacheKey(v.dataset,v.query)===key&&validate(v)),write:(key,value,at)=>archiveCacheKey(value?.dataset,value?.query)===key?store.write(key,value,at):Promise.resolve(false)});
}
