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
import {createDatabaseReader} from './database-reader.mjs';
import {createQueryPool} from './query-pool.mjs';
export {missingIndexes} from './database-reader.mjs';
import {decodeSecret,verifyRequest,signResponse,createNonceCache,RESPONSE_SIGNATURE_HEADER} from '../home-inference/signature.mjs';
import {LOCAL_DATA_GATEWAY,LOCAL_DATA_ROUTES,LOCAL_DATA_LIMITS,LOCAL_DATA_DATA_PREFIX} from './protocol.mjs';
import {DATASETS} from './datasets.mjs';
import {NEON_PREVIEW_ROUTE,loadNeonPreview,neonPreviewConfig} from './neon-preview.mjs';
import {LIDAR_POINTS_ROUTE,loadLidarPoints,lidarPointsConfig} from './lidar-points.mjs';
import {lidarViewConfig,requestLidarView,loadLidarViewReceipt,loadLidarViewArtifact} from './lidar-view.mjs';
import {LIDAR_VIEW_ROUTES,validViewKey} from './lidar-view-model.mjs';
import {GROUND_ROUTE} from './ground-model.mjs';
import {groundConfig,requestGround} from './ground-store.mjs';

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

/**
 * The gateway as a function of one request, so it can be tested without a socket.
 * databases: {observations, tiger, nwm, bulk} file paths (all but observations optional). dbPath is the
 * phase 1 name for databases.observations.
 */
export function createGateway({keyId,secret:rawSecret,dbPath,databases={observations:dbPath},clock=Date.now,neonPreview=null,lidarPoints=null,lidarView=null,ground=null,open,execute}){
 const secret=typeof rawSecret==='string'?decodeSecret(rawSecret):rawSecret;
 if(!Buffer.isBuffer(secret))throw fail('GATEWAY_KEY_INVALID');
 const keys=new Map([[keyId,{id:keyId,secret}]]),nonces=createNonceCache({clock});
 const read=execute??createDatabaseReader({databases,open,clock});

 return function handle({method,path,headers,body='',signal}){
  const reply=(status,value)=>{
   const bytes=Buffer.from(JSON.stringify({gateway:LOCAL_DATA_GATEWAY,...value}));
   return {status,body:bytes,signature:signResponse({secret,requestHeaders:headers,method,path,requestBody:body,status,body:bytes})};
  };
  if(LOCAL_DATA_ROUTES.get(path)!==method)return reply(404,{error:'ROUTE_NOT_FOUND'});
  // One answer for every authentication failure, so the gateway is not an oracle.
  if(!verifyRequest({headers,method,path,body,keys,nonces,now:clock()}).ok)return reply(401,{error:'UNAUTHORIZED'});

  if(path===GROUND_ROUTE){
   try{const input=JSON.parse(body),value=requestGround(ground,input),answer=reply(200,value);return answer.body.length>LOCAL_DATA_LIMITS.replyBytes?reply(413,{error:'REPLY_TOO_LARGE'}):answer;}
   catch(e){return reply(e.message==='QUERY_INVALID'?400:503,{error:e.message==='QUERY_INVALID'?'QUERY_INVALID':'GROUND_NOT_READY'});}
  }

  if(Object.values(LIDAR_VIEW_ROUTES).includes(path)){
   let input;try{input=JSON.parse(body);}catch{return reply(400,{error:'QUERY_INVALID'});}
   const exact=names=>input&&typeof input==='object'&&!Array.isArray(input)&&Object.keys(input).sort().join(',')===names.split(',').sort().join(',');
   try{
    let value;
    if(path===LIDAR_VIEW_ROUTES.view){
     if(exact('requestKey')&&validViewKey(input.requestKey))value=loadLidarViewReceipt(lidarView,input.requestKey);
     else if(exact('bbox,zoom,layers'))value=requestLidarView(lidarView,input);
     else throw Error('QUERY_INVALID');
    }else if(path===LIDAR_VIEW_ROUTES.chunk){
     if(!exact('requestKey,chunkId')||!validViewKey(input.requestKey)||!Number.isInteger(input.chunkId)||input.chunkId<0||input.chunkId>15)throw Error('QUERY_INVALID');
     value=loadLidarViewArtifact(lidarView,input.requestKey,input.chunkId);
    }else{
     if(!exact('requestKey')||!validViewKey(input.requestKey))throw Error('QUERY_INVALID');value=loadLidarViewArtifact(lidarView,input.requestKey,'grid');
    }
    const answer=reply(200,value);return answer.body.length>LOCAL_DATA_LIMITS.replyBytes?reply(413,{error:'REPLY_TOO_LARGE'}):answer;
   }catch(e){return reply(e.message==='QUERY_INVALID'?400:503,{error:e.message==='QUERY_INVALID'?'QUERY_INVALID':'LIDAR_VIEW_NOT_READY'});}
  }

  if(path===LIDAR_POINTS_ROUTE||path.startsWith(LIDAR_POINTS_ROUTE+'/')){
   if(body!=='')return reply(400,{error:'QUERY_INVALID'});
   try{
    const id=path===LIDAR_POINTS_ROUTE?null:Number(path.slice(LIDAR_POINTS_ROUTE.length+1));
    const answer=reply(200,loadLidarPoints(lidarPoints,id));
    return answer.body.length>LOCAL_DATA_LIMITS.replyBytes?reply(413,{error:'REPLY_TOO_LARGE'}):answer;
   }catch{return reply(503,{error:'LIDAR_POINTS_NOT_READY'});}
  }

  if(path===NEON_PREVIEW_ROUTE){
   if(body!=='')return reply(400,{error:'QUERY_INVALID'});
   try{
    const answer=reply(200,loadNeonPreview(neonPreview));
    return answer.body.length>LOCAL_DATA_LIMITS.replyBytes?reply(413,{error:'REPLY_TOO_LARGE'}):answer;
   }catch{return reply(503,{error:'NEON_PREVIEW_NOT_READY'});}
  }

  const databaseError=error=>{
   const code=error?.code;
   if(code==='QUERY_INVALID')return reply(400,{error:code});
   if(code==='REPLY_TOO_LARGE')return reply(413,{error:code});
   return reply(503,{error:['DATASET_NOT_READY','QUERY_TIMEOUT','QUERY_BUSY'].includes(code)?code:'DATABASE_UNAVAILABLE'});
  };
  const run=(operation,format)=>{
   try{
    const value=read(operation,{signal});
    return value&&typeof value.then==='function'?value.then(format).catch(databaseError):format(value);
   }catch(error){return databaseError(error);}
  };
  if(path==='/v1/health')return run({kind:'health'},value=>reply(value.ok?200:503,value));

  const dataset=DATASETS.get(path.slice(LOCAL_DATA_DATA_PREFIX.length));
  let input;try{input=JSON.parse(body);dataset.parse(input);}catch{return reply(400,{error:'QUERY_INVALID'});}
  return run({kind:'dataset',id:dataset.id,input},({query,result})=>{
   const {rows,total,...extra}=result;
   const answer=reply(200,{format:dataset.format??'kfm-local-data-v1',dataset:dataset.id,query,total,count:rows.length,...extra,[dataset.rowsKey??'rows']:rows,source:dataset.source,generatedAt:new Date(clock()).toISOString()});
   return answer.body.length>LOCAL_DATA_LIMITS.replyBytes?reply(413,{error:'REPLY_TOO_LARGE'}):answer;
  });
 };
}

async function readBody(request){
 const chunks=[];let bytes=0;
 const timer=setTimeout(()=>request.destroy(),LOCAL_DATA_LIMITS.gatewayMs);
 try{for await(const chunk of request){bytes+=chunk.length;if(bytes>LOCAL_DATA_LIMITS.requestBytes)throw fail('REQUEST_TOO_LARGE');chunks.push(chunk);}}
 finally{clearTimeout(timer);}
 return Buffer.concat(chunks).toString('utf8');
}

export function startGateway({host='127.0.0.1',port=8788,log=line=>console.log(JSON.stringify(line)),...options}){
 if(!LOOPBACK.has(host))throw fail('GATEWAY_HOST_NOT_LOOPBACK');
 const pool=options.execute?null:createQueryPool({databases:options.databases??{observations:options.dbPath}});
 const handle=createGateway({...options,execute:options.execute??pool.run});
 const server=createServer(async(request,response)=>{
  let body;try{body=await readBody(request);}catch{response.writeHead(413).end();return;}
  const url=new URL(request.url,'http://localhost');
  if(url.search){response.writeHead(404).end();return;}
  const started=Date.now();
  const controller=new AbortController();
  response.once('close',()=>{if(!response.writableEnded)controller.abort();});
  const answer=await handle({method:request.method,path:url.pathname,headers:request.headers,body,signal:controller.signal});
  if(response.destroyed)return;
  response.writeHead(answer.status,{'Content-Type':'application/json','Cache-Control':'no-store','X-Content-Type-Options':'nosniff',[RESPONSE_SIGNATURE_HEADER]:answer.signature});
  response.end(answer.body);
  // One line per question, so use and latency per dataset can be measured from the journal.
  // The route names the dataset; the question's parameters and the answer are never logged.
  const dataset=url.pathname.startsWith(LOCAL_DATA_DATA_PREFIX)?url.pathname.slice(LOCAL_DATA_DATA_PREFIX.length):null;
  log({at:new Date(started).toISOString(),event:'answered',path:LOCAL_DATA_ROUTES.has(url.pathname)?url.pathname:'unknown',dataset:DATASETS.has(dataset)?dataset:null,status:answer.status,ms:Date.now()-started,bytes:answer.body.length});
 });
 server.once('close',()=>{void pool?.close();});
 server.requestTimeout=LOCAL_DATA_LIMITS.gatewayMs;
 return new Promise((resolve,reject)=>{server.once('error',reject);server.listen(port,host,()=>resolve(server));});
}

/** Database paths from the environment; observations is required, GeoPackages and bulk optional. */
export function databasesFromEnv(env=process.env){
 const file=path=>{if(!path)return undefined;if(!statSync(path).isFile())throw fail('DATABASE_NOT_CONFIGURED');return path;};
 if(!env.KFM_LOCAL_DATA_DB)throw fail('DATABASE_NOT_CONFIGURED');
 return {observations:file(env.KFM_LOCAL_DATA_DB),tiger:file(env.KFM_LOCAL_DATA_TIGER_DB),nwm:file(env.KFM_LOCAL_DATA_NWM_DB),bulk:file(env.KFM_LOCAL_DATA_BULK_DB)};
}

async function main(){
 let options;
 try{
  const {keyId,secret}=loadGatewayKey(process.env.KFM_LOCAL_DATA_KEY_FILE);
  options={keyId,secret,databases:databasesFromEnv(),neonPreview:neonPreviewConfig(),lidarPoints:lidarPointsConfig(),lidarView:lidarViewConfig(),ground:groundConfig(),port:Number(process.env.KFM_LOCAL_DATA_PORT||8788)};
 }catch(error){console.error(JSON.stringify({event:'config_refused',code:error.code??'CONFIG_INVALID'}));process.exitCode=1;return;}
 const server=await startGateway(options);
 console.log(JSON.stringify({at:new Date().toISOString(),event:'listening',gateway:LOCAL_DATA_GATEWAY,address:`127.0.0.1:${server.address().port}`,databases:Object.keys(options.databases).filter(k=>options.databases[k])}));
 const stop=()=>server.close();process.once('SIGTERM',stop);process.once('SIGINT',stop);
}

if(import.meta.url===pathToFileURL(process.argv[1]??'').href)main();
