import * as provider0 from "../../../connectors/nass/quick-stats-api.mjs";
import * as provider1 from "../../../connectors/drought-monitor/statistics-api.mjs";
import * as provider2 from "../../../connectors/kansas/dasc-imagery-api.mjs";
import * as provider3 from "../../../connectors/usgs/nldi-transect-api.mjs";
import * as provider4 from "../../../connectors/microsoft/planetary-computer-api.mjs";
import * as provider5 from "../../../connectors/nrcs/soil-data-access-api.mjs";
import * as provider6 from "../../../connectors/openstreetmap/overpass-api.mjs";
import * as provider7 from "../../../connectors/census/acs-http-api.mjs";
import * as provider8 from "../../../connectors/eia/open-data-api.mjs";
import * as provider9 from "../../../connectors/noaa/ncei-hosted-api.mjs";
import * as provider10 from "../../../connectors/usgs/wqp-api.mjs";
import * as provider11 from "../../../connectors/nrcs/scan-http-api.mjs";
import * as provider12 from "../../../connectors/epa/air-quality-api.mjs";
import * as provider13 from "../../../connectors/loc/maps-api.mjs";
import * as provider14 from "../../../connectors/iem/asos-api.mjs";
import * as provider15 from "../../../connectors/kansas/kanplan-api.mjs";
import {configuration,hash,stable,transport,jsonEntity,csvEntity,fail,ConnectionError} from "../../../packages/connectors-core/src/http-runtime.mjs";
export const PROVIDERS=[provider0,provider1,provider2,provider3,provider4,provider5,provider6,provider7,provider8,provider9,provider10,provider11,provider12,provider13,provider14,provider15];
export const VERSION="kfm-api-connections-v1";
const encoder=new TextEncoder();
const provider=id=>{const p=PROVIDERS.find(p=>p.spec.id===id);if(!p)fail("SOURCE_NOT_ALLOWED");return p;};
export function catalog(env={}) {return PROVIDERS.map(({spec})=>({...spec,...configuration(spec,env),...(spec.productSecrets?{productStatuses:Object.fromEntries(Object.keys(spec.productSecrets).map(product=>[product,configuration(spec,env,{product})]))}:{}),state:configuration(spec,env).configured?"ready-for-owner-capture":"configuration-held",releaseState:"unreleased",evidenceRole:"EXTERNAL_CONTEXT_ONLY"}));}
export async function makePlan(sourceId,query={},at=Date.now()) {
 const p=provider(sourceId);if(!Number.isFinite(at)||at<0)fail("QUERY_REJECTED");
 const planned=p.plan(query),slot=Math.floor(at/p.spec.intervalMs)*p.spec.intervalMs;
 const identity={version:VERSION,sourceId,query:planned.query,slot,requests:planned.requests};
 const id=await hash(encoder.encode(stable(identity)));
 return {...identity,id,limitBytes:Math.ceil(p.spec.limitBytes*1.4)+100000,entityLimitBytes:p.spec.limitBytes,requestedAt:new Date(slot).toISOString()};
}
const b64=bytes=>{let text="";for(let i=0;i<bytes.length;i+=8192)text+=String.fromCharCode(...bytes.subarray(i,i+8192));return btoa(text);};
const unb64=text=>{if(typeof text!=="string"||text.length>4000000||!/^[A-Za-z0-9+/]*={0,2}$/.test(text))fail("CAPTURE_INTEGRITY_FAILED",503);return Uint8Array.from(atob(text),c=>c.charCodeAt(0));};
const decode=(bytes,format)=>format==="png"?bytes:format==="csv"?csvEntity(new TextDecoder("utf-8",{fatal:true}).decode(bytes)):jsonEntity(new TextDecoder("utf-8",{fatal:true}).decode(bytes));
export async function acquire(plan,{env={},fetcher=fetch,signal}={}) {
 const canonical=await makePlan(plan.sourceId,plan.query,plan.slot);
 if(stable(canonical)!==stable(plan))fail("PLAN_INTEGRITY_FAILED");
 const p=provider(plan.sourceId),ready=configuration(p.spec,env,plan.query);
 if(!ready.configured)fail(ready.missing.length?"CREDENTIAL_REQUIRED":"PROVIDER_REVIEW_REQUIRED",409);
 const controller=new AbortController(),abort=()=>controller.abort();signal?.throwIfAborted();signal?.addEventListener("abort",abort,{once:true});
 const timer=setTimeout(abort,30000),startedAt=new Date().toISOString(),entities=[];
 let view=null,validation="invalid",validationError=null;
 try {
  for(const request of plan.requests){
   const response=await transport(request,env,fetcher,controller.signal,request.preflight?65536:plan.entityLimitBytes);
   const entity={url:request.url,method:request.method,format:request.format,body:request.body??null,contentType:response.type,sha256:await hash(response.bytes),receivedSha256:response.originalSha256,credentialRedactions:response.redactions,byteLength:response.bytes.length,entityBase64:b64(response.bytes),etag:response.etag,lastModified:response.modified};
   entities.push(entity);
   let value;
   try{value=decode(response.bytes,request.format);}catch(error){validationError=error instanceof ConnectionError?error.code:"PAYLOAD_REJECTED";if(request.preflight)fail(validationError,502);break;}
   if(request.preflight)p.preflight(value,plan.query);
   else {try{view=p.parse(value,plan.query);validation="structure-valid";}catch(error){validationError=error instanceof ConnectionError?error.code:"PAYLOAD_REJECTED";}}
  }
  const bytes=encoder.encode(JSON.stringify({format:VERSION,sourceId:plan.sourceId,query:plan.query,slot:plan.slot,entities}));
  if(bytes.length>plan.limitBytes)fail("RESPONSE_TOO_LARGE",502);
  const receipt={format:VERSION,captureId:plan.id,sourceId:plan.sourceId,query:plan.query,slot:plan.slot,adapterVersion:VERSION,requestedAt:startedAt,retrievedAt:new Date().toISOString(),sha256:await hash(bytes),byteLength:bytes.length,entityBytes:entities.reduce((sum,e)=>sum+e.byteLength,0),validation,validationError,featureCount:view?.total??null,partial:view?.partial??false,sourceUrl:plan.requests.at(-1).url,entityHashes:entities.map(e=>({url:e.url,sha256:e.sha256,byteLength:e.byteLength,contentType:e.contentType,receivedSha256:e.receivedSha256,credentialRedactions:e.credentialRedactions,etag:e.etag,lastModified:e.lastModified})),lifecycle:"WORK/QUARANTINE",releaseState:"unreleased",rightsReview:"pending",sensitivityReview:"pending",evidenceRole:"EXTERNAL_CONTEXT_ONLY",rightsUrl:p.spec.rights??p.spec.docs,limitation:p.spec.limitation,transforms:["HTTP content decoding and reversible base64 packaging. Any provider-echoed credential is redacted before storage; received and stored entity digests and redaction counts are recorded. Anonymous source entities are unchanged."]};
  return {bytes,receipt};
 }finally{clearTimeout(timer);signal?.removeEventListener("abort",abort);}
}
export async function replay(capture) {
 if(capture.receipt?.format!==VERSION||capture.receipt.lifecycle!=="WORK/QUARANTINE"||capture.receipt.releaseState!=="unreleased"||capture.bytes.length!==capture.receipt.byteLength||await hash(capture.bytes)!==capture.receipt.sha256)fail("CAPTURE_INTEGRITY_FAILED",503);
 const bundle=jsonEntity(new TextDecoder("utf-8",{fatal:true}).decode(capture.bytes));
 const plan=await makePlan(bundle.sourceId,bundle.query,bundle.slot);
 if(plan.id!==capture.receipt.captureId||bundle.format!==VERSION||!Array.isArray(bundle.entities)||bundle.entities.length!==plan.requests.length)fail("CAPTURE_INTEGRITY_FAILED",503);
 const p=provider(bundle.sourceId);let view=null,finalEntity=null;
 for(let i=0;i<bundle.entities.length;i++){
  const e=bundle.entities[i],request=plan.requests[i],bytes=unb64(e.entityBase64);
  if(e.url!==request.url||e.method!==request.method||e.body!==(request.body??null)||e.format!==request.format||bytes.length!==e.byteLength||bytes.length>(request.preflight?65536:plan.entityLimitBytes)||await hash(bytes)!==e.sha256||e.sha256!==capture.receipt.entityHashes[i]?.sha256)fail("CAPTURE_INTEGRITY_FAILED",503);
  const value=decode(bytes,e.format);if(request.preflight)p.preflight(value,plan.query);else{view=p.parse(value,plan.query);finalEntity={bytes,contentType:e.contentType,format:e.format};}
 }
 if(!view||capture.receipt.validation!=="structure-valid")fail("CAPTURE_VALIDATION_HELD",409);
 return {view:{...view,query:plan.query,sourceId:plan.sourceId,limitation:p.spec.limitation,evidenceRole:"EXTERNAL_CONTEXT_ONLY",releaseState:"unreleased",retrievedAt:capture.receipt.retrievedAt},receipt:capture.receipt,entity:finalEntity};
}
export async function captureOne(store,sourceId,query,options={}) {
 const plan=await makePlan(sourceId,query,options.at),ready=configuration(provider(sourceId).spec,options.env,plan.query);
 if(!ready.configured)fail(ready.missing.length?"CREDENTIAL_REQUIRED":"PROVIDER_REVIEW_REQUIRED",409);
 const token=await store.claim(Date.now(),options.actor??"owner-api-capture");if(!token)fail("PIPELINE_PAUSED_OR_BUSY",409);
 let reservation=0;
 try {
  if(!await store.due(plan,token,Date.now())){const saved=await store.read(plan.id);return {...await replay(saved),cached:true};}
  const last=await store.lastAttempt?.(sourceId);const pause=sourceId==="library-of-congress"?3000:1000;
  if(last&&Date.now()-last<pause)fail("PROVIDER_COOLDOWN",429);
  reservation=await store.reserve(plan,token);
  const result=await acquire(plan,options);await store.save(plan,result,token,reservation);reservation=0;
  // Exact stored readback, not a response-only successful fetch.
  return {...await replay(await store.read(plan.id)),cached:false};
 }catch(error){if(reservation)await store.failure(plan,token,"API_CAPTURE_HELD",reservation);throw error;}
 finally{await store.release(token);}
}
export async function inputJson(request) {if(!request.headers.get("content-type")?.startsWith("application/json"))fail("JSON_REQUIRED");const {readBounded}=await import("../../../packages/connectors-core/src/http-runtime.mjs");return jsonEntity(new TextDecoder().decode(await readBounded(request,4096)));}
/** Explicit host profiles only, disabled by default. Each tick attempts at most two. */
/** @param {any} store @param {{env?:Record<string,any>,at?:number,fetcher?:typeof fetch,signal?:AbortSignal}} options */
export async function scheduledProfiles(store,{env={},at=Date.now(),fetcher=fetch,signal}={}) {
 if(env.KFM_API_SCHEDULE_ENABLED!=="true")return {state:"schedule-disabled",captured:0,outcomes:[]};
 const text=env.KFM_API_CAPTURE_PROFILES;
 if(typeof text!=="string"||text.length>4096)fail("SCHEDULE_PROFILES_REQUIRED",409);
 const profiles=jsonEntity(text);
 if(!Array.isArray(profiles)||!profiles.length||profiles.length>16)fail("SCHEDULE_PROFILES_REJECTED",409);
 // Validate every profile before any request, rather than partially executing bad configuration.
 const plans=[];
 for(const profile of profiles){
  if(!profile||typeof profile!=="object"||Object.keys(profile).some(key=>!["sourceId","query","rollingDays"].includes(key)))fail("SCHEDULE_PROFILES_REJECTED",409);
  let query={...profile.query};const p=provider(profile.sourceId);
  if(profile.rollingDays!==undefined){if(!Number.isInteger(profile.rollingDays)||profile.rollingDays<1||profile.rollingDays>31||!p.spec.fields.some(f=>f.key==="start"))fail("SCHEDULE_PROFILES_REJECTED",409);const end=Math.floor(at/86400000)*86400000-86400000;query={...query,start:new Date(end-(profile.rollingDays-1)*86400000).toISOString().slice(0,10),end:new Date(end).toISOString().slice(0,10)};if(profile.sourceId==="iem-asos")query.end=new Date(end+86400000).toISOString().slice(0,10);}
  plans.push(await makePlan(profile.sourceId,query,at));
 }
 const start=Math.floor(at/3600000)*2%plans.length,outcomes=[];let captured=0;
 for(let i=0;i<Math.min(2,plans.length);i++){const plan=plans[(start+i)%plans.length];try{const result=await captureOne(store,plan.sourceId,plan.query,{env,fetcher,signal,at,actor:"capture-worker"});captured+=result.cached?0:1;outcomes.push({sourceId:plan.sourceId,state:result.cached?"already-captured":"quarantined",captureId:result.receipt.captureId});}catch(error){outcomes.push({sourceId:plan.sourceId,state:"held",code:error instanceof ConnectionError?error.code:"HOST_CAPTURE_HELD"});}}
 return {state:outcomes.some(x=>x.state==="held")?"partial":"complete",captured,outcomes};
}
