#!/usr/bin/env node
// KFM local-data gateway: answers the website's fixed, read-only questions from the pipeline PC's
// local SQL databases. Loopback only. Every request must carry the website's signature (the
// gateway key, shared with the website alone) and every reply is signed back over the exact
// request, status and bytes, so the relay worker in between can neither forge nor alter either.
// A database is opened read-only for each question, and a dataset whose indexes are missing is
// refused rather than scanned. Uses Node's built-in sqlite; no dependencies.
//
//   KFM_LOCAL_DATA_KEY_FILE=... KFM_LOCAL_DATA_DB=... [KFM_LOCAL_DATA_TIGER_DB=...] [KFM_LOCAL_DATA_NWM_DB=...] node gateway.mjs
import {createServer} from 'node:http';
import {readFileSync,statSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {DatabaseSync} from 'node:sqlite';
import {decodeSecret,verifyRequest,signResponse,createNonceCache,RESPONSE_SIGNATURE_HEADER} from '../home-inference/signature.mjs';
import {LOCAL_DATA_GATEWAY,LOCAL_DATA_ROUTES,LOCAL_DATA_LIMITS,LOCAL_DATA_DATA_PREFIX} from './protocol.mjs';
import {DATASETS} from './datasets.mjs';

const fail=code=>Object.assign(new Error(code),{code});
const LOOPBACK=new Set(['127.0.0.1','::1']);

/** {id, secret} from an owner-only JSON key file. */
export function loadGatewayKey(path){
 if(!path)throw fail('GATEWAY_KEY_NOT_CONFIGURED');
 const stat=statSync(path);
 if(!stat.isFile()||stat.size>4096)throw fail('GATEWAY_KEY_INVALID');
 if(stat.mode&0o077)throw fail('GATEWAY_KEY_PERMISSIONS');
 let value;try{value=JSON.parse(readFileSync(path,'utf8'));}catch{throw fail('GATEWAY_KEY_INVALID');}
 const secret=decodeSecret(value?.secret);
 if(!/^[A-Za-z0-9._-]{1,64}$/.test(value?.id??'')||!secret)throw fail('GATEWAY_KEY_INVALID');
 return {keyId:value.id,secret};
}

/** Index names a dataset needs that its database does not have yet. */
export function missingIndexes(db,dataset){
 if(!dataset.indexes.length)return [];
 const present=new Set(db.prepare(`SELECT name FROM sqlite_master WHERE type='index' AND name IN (${dataset.indexes.map(()=>'?').join(',')})`).all(...dataset.indexes.map(i=>i.name)).map(r=>r.name));
 return dataset.indexes.map(i=>i.name).filter(n=>!present.has(n));
}

/**
 * The gateway as a function of one request, so it can be tested without a socket.
 * databases: {observations, tiger, nwm} file paths (tiger and nwm optional). dbPath is the
 * phase 1 name for databases.observations.
 */
export function createGateway({keyId,secret:rawSecret,dbPath,databases={observations:dbPath},clock=Date.now,open=path=>new DatabaseSync(path,{readOnly:true})}){
 const secret=typeof rawSecret==='string'?decodeSecret(rawSecret):rawSecret;
 if(!Buffer.isBuffer(secret))throw fail('GATEWAY_KEY_INVALID');
 const keys=new Map([[keyId,{id:keyId,secret}]]),nonces=createNonceCache({clock});
 // Per-database memory that outlives one question: index checks that passed, PRISM's grid catalog, TIGER columns.
 const caches=new Map(),cacheFor=path=>{if(!caches.has(path))caches.set(path,new Map());return caches.get(path);};
 const ready=(db,path,dataset)=>{
  const cache=cacheFor(path),key='ready:'+dataset.id;
  if(cache.get(key))return [];
  const missing=missingIndexes(db,dataset);if(!missing.length)cache.set(key,true);
  return missing;
 };
 const withDatabase=(name,fn)=>{
  const path=databases[name];if(!path)throw fail('DATABASE_NOT_CONFIGURED');
  let db;try{db=open(path);}catch{throw fail('DATABASE_UNAVAILABLE');}
  try{return fn(db,path);}finally{try{db.close();}catch{}}
 };

 return function handle({method,path,headers,body=''}){
  const reply=(status,value)=>{
   const bytes=Buffer.from(JSON.stringify({gateway:LOCAL_DATA_GATEWAY,...value}));
   return {status,body:bytes,signature:signResponse({secret,requestHeaders:headers,method,path,requestBody:body,status,body:bytes})};
  };
  if(LOCAL_DATA_ROUTES.get(path)!==method)return reply(404,{error:'ROUTE_NOT_FOUND'});
  // One answer for every authentication failure, so the gateway is not an oracle.
  if(!verifyRequest({headers,method,path,body,keys,nonces,now:clock()}).ok)return reply(401,{error:'UNAUTHORIZED'});

  if(path==='/v1/health'){
   const datasets=[...DATASETS.values()].map(d=>{
    try{const missing=withDatabase(d.db,(db,p)=>ready(db,p,d));return missing.length?{id:d.id,ready:false,reason:'INDEX_MISSING'}:{id:d.id,ready:true};}
    catch(error){return {id:d.id,ready:false,reason:error.code==='DATABASE_NOT_CONFIGURED'?'DATABASE_NOT_CONFIGURED':'DATABASE_UNAVAILABLE'};}
   });
   let stormEvents=null;
   try{stormEvents=withDatabase('observations',db=>db.prepare('SELECT COUNT(*) AS n FROM kfm_storm_event_details').get().n);}catch{}
   return reply(stormEvents===null?503:200,{ok:stormEvents!==null,datasets,stormEvents});
  }

  const dataset=DATASETS.get(path.slice(LOCAL_DATA_DATA_PREFIX.length));
  let query;try{query=dataset.parse(JSON.parse(body));}catch{return reply(400,{error:'QUERY_INVALID'});}
  try{
   const result=withDatabase(dataset.db,(db,dbPath)=>{
    if(ready(db,dbPath,dataset).length)throw fail('DATASET_NOT_READY');
    return dataset.run(db,query,{cache:cacheFor(dbPath)});
   });
   const {rows,total,...extra}=result;
   const answer=reply(200,{format:dataset.format??'kfm-local-data-v1',dataset:dataset.id,query,total,count:rows.length,...extra,[dataset.rowsKey??'rows']:rows,source:dataset.source,generatedAt:new Date(clock()).toISOString()});
   return answer.body.length>LOCAL_DATA_LIMITS.replyBytes?reply(413,{error:'REPLY_TOO_LARGE'}):answer;
  }catch(error){
   return reply(503,{error:error.code==='DATASET_NOT_READY'?'DATASET_NOT_READY':'DATABASE_UNAVAILABLE'});
  }
 };
}

async function readBody(request){
 const chunks=[];let bytes=0;
 const timer=setTimeout(()=>request.destroy(),LOCAL_DATA_LIMITS.gatewayMs);
 try{for await(const chunk of request){bytes+=chunk.length;if(bytes>LOCAL_DATA_LIMITS.requestBytes)throw fail('REQUEST_TOO_LARGE');chunks.push(chunk);}}
 finally{clearTimeout(timer);}
 return Buffer.concat(chunks).toString('utf8');
}

export function startGateway({host='127.0.0.1',port=8788,...options}){
 if(!LOOPBACK.has(host))throw fail('GATEWAY_HOST_NOT_LOOPBACK');
 const handle=createGateway(options);
 const server=createServer(async(request,response)=>{
  let body;try{body=await readBody(request);}catch{response.writeHead(413).end();return;}
  const url=new URL(request.url,'http://localhost');
  if(url.search){response.writeHead(404).end();return;}
  const answer=handle({method:request.method,path:url.pathname,headers:request.headers,body});
  response.writeHead(answer.status,{'Content-Type':'application/json','Cache-Control':'no-store','X-Content-Type-Options':'nosniff',[RESPONSE_SIGNATURE_HEADER]:answer.signature});
  response.end(answer.body);
 });
 server.requestTimeout=LOCAL_DATA_LIMITS.gatewayMs;
 return new Promise((resolve,reject)=>{server.once('error',reject);server.listen(port,host,()=>resolve(server));});
}

/** Database paths from the environment; observations is required, the GeoPackages optional. */
export function databasesFromEnv(env=process.env){
 const file=path=>{if(!path)return undefined;if(!statSync(path).isFile())throw fail('DATABASE_NOT_CONFIGURED');return path;};
 if(!env.KFM_LOCAL_DATA_DB)throw fail('DATABASE_NOT_CONFIGURED');
 return {observations:file(env.KFM_LOCAL_DATA_DB),tiger:file(env.KFM_LOCAL_DATA_TIGER_DB),nwm:file(env.KFM_LOCAL_DATA_NWM_DB)};
}

async function main(){
 let options;
 try{
  const {keyId,secret}=loadGatewayKey(process.env.KFM_LOCAL_DATA_KEY_FILE);
  options={keyId,secret,databases:databasesFromEnv(),port:Number(process.env.KFM_LOCAL_DATA_PORT||8788)};
 }catch(error){console.error(JSON.stringify({event:'config_refused',code:error.code??'CONFIG_INVALID'}));process.exitCode=1;return;}
 const server=await startGateway(options);
 console.log(JSON.stringify({at:new Date().toISOString(),event:'listening',gateway:LOCAL_DATA_GATEWAY,address:`127.0.0.1:${server.address().port}`,databases:Object.keys(options.databases).filter(k=>options.databases[k])}));
 const stop=()=>server.close();process.once('SIGTERM',stop);process.once('SIGINT',stop);
}

if(import.meta.url===pathToFileURL(process.argv[1]??'').href)main();
