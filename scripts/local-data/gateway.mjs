#!/usr/bin/env node
// KFM local-data gateway: answers the website's fixed, read-only questions from the pipeline PC's
// local SQL database. Loopback only. Every request must carry the website's signature (the
// gateway key, shared with the website alone) and every reply is signed back over the exact
// request, status and bytes, so the relay worker in between can neither forge nor alter either.
// The database is opened read-only for each question. Uses Node's built-in sqlite; no dependencies.
//
//   KFM_LOCAL_DATA_KEY_FILE=... KFM_LOCAL_DATA_DB=... node gateway.mjs
import {createServer} from 'node:http';
import {readFileSync,statSync} from 'node:fs';
import {pathToFileURL} from 'node:url';
import {DatabaseSync} from 'node:sqlite';
import {decodeSecret,verifyRequest,signResponse,createNonceCache,RESPONSE_SIGNATURE_HEADER} from '../home-inference/signature.mjs';
import {LOCAL_DATA_GATEWAY,LOCAL_DATA_ROUTES,LOCAL_DATA_LIMITS} from './protocol.mjs';
import {parseStormQuery,stormEventsSql,stormEvent,STORM_EVENTS_SOURCE} from './storm-events.mjs';

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

/** The gateway as a function of one request, so it can be tested without a socket. */
export function createGateway({keyId,secret:rawSecret,dbPath,clock=Date.now,open=path=>new DatabaseSync(path,{readOnly:true})}){
 const secret=typeof rawSecret==='string'?decodeSecret(rawSecret):rawSecret;
 if(!Buffer.isBuffer(secret))throw fail('GATEWAY_KEY_INVALID');
 const keys=new Map([[keyId,{id:keyId,secret}]]),nonces=createNonceCache({clock});
 return function handle({method,path,headers,body=''}){
  const reply=(status,value)=>{
   const bytes=Buffer.from(JSON.stringify({gateway:LOCAL_DATA_GATEWAY,...value}));
   return {status,body:bytes,signature:signResponse({secret,requestHeaders:headers,method,path,requestBody:body,status,body:bytes})};
  };
  if(LOCAL_DATA_ROUTES.get(path)!==method)return reply(404,{error:'ROUTE_NOT_FOUND'});
  // One answer for every authentication failure, so the gateway is not an oracle.
  if(!verifyRequest({headers,method,path,body,keys,nonces,now:clock()}).ok)return reply(401,{error:'UNAUTHORIZED'});
  let db;
  try{
   db=open(dbPath);
   if(path==='/v1/health')return reply(200,{ok:true,datasets:['storm-events'],stormEvents:db.prepare('SELECT COUNT(*) AS n FROM kfm_storm_event_details').get().n});
   let query;try{query=parseStormQuery(JSON.parse(body));}catch{return reply(400,{error:'QUERY_INVALID'});}
   const sql=stormEventsSql(query);
   const total=db.prepare(sql.count.sql).get(...sql.count.params).n;
   const events=db.prepare(sql.rows.sql).all(...sql.rows.params).map(stormEvent);
   const answer=reply(200,{format:'kfm-local-data-storm-events-v1',query,total,count:events.length,events,source:STORM_EVENTS_SOURCE,generatedAt:new Date(clock()).toISOString()});
   return answer.body.length>LOCAL_DATA_LIMITS.replyBytes?reply(413,{error:'REPLY_TOO_LARGE'}):answer;
  }catch{return reply(503,{error:'DATABASE_UNAVAILABLE'});}
  finally{try{db?.close();}catch{}}
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

async function main(){
 let options;
 try{
  const {keyId,secret}=loadGatewayKey(process.env.KFM_LOCAL_DATA_KEY_FILE);
  const dbPath=process.env.KFM_LOCAL_DATA_DB;if(!dbPath||!statSync(dbPath).isFile())throw fail('DATABASE_NOT_CONFIGURED');
  options={keyId,secret,dbPath,port:Number(process.env.KFM_LOCAL_DATA_PORT||8788)};
 }catch(error){console.error(JSON.stringify({event:'config_refused',code:error.code??'CONFIG_INVALID'}));process.exitCode=1;return;}
 const server=await startGateway(options);
 console.log(JSON.stringify({at:new Date().toISOString(),event:'listening',gateway:LOCAL_DATA_GATEWAY,address:`127.0.0.1:${server.address().port}`}));
 const stop=()=>server.close();process.once('SIGTERM',stop);process.once('SIGINT',stop);
}

if(import.meta.url===pathToFileURL(process.argv[1]??'').href)main();
