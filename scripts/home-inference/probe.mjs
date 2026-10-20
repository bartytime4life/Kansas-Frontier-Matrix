#!/usr/bin/env node
// Phase-2 transport proof and phase-5 benchmark for the KFM home gateway.
// Sends synthetic prompts only. Prints a JSON receipt with timings and pass/fail
// checks; it never prints the secret, signatures or Access credentials.
//
//   KFM_HOME_INFERENCE_URL=https://inference.example.org \
//   KFM_HOME_INFERENCE_KEY_ID=staging-202610 KFM_HOME_INFERENCE_SECRET=... \
//   KFM_HOME_INFERENCE_PROFILE=kfm-default-chat KFM_HOME_INFERENCE_DIGEST=sha256:... \
//   [KFM_HOME_INFERENCE_ACCESS_ID=... KFM_HOME_INFERENCE_ACCESS_SECRET=...] \
//   node probe.mjs [--runs 3] [--depth brief|expanded] [--concurrency 2]
import {randomUUID} from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {signRequest,newSecret,verifyResponse} from './signature.mjs';

const SYNTHETIC=['In two sentences, explain what a county seat is.','Give three general reasons rivers change course over time.','Briefly explain the difference between weather and climate.'];

export async function probe({env=process.env,runs=3,depth='brief',concurrency=2,fetchImpl=fetch,clock=Date.now}={}){
 const origin=new URL(env.KFM_HOME_INFERENCE_URL).origin,keyId=env.KFM_HOME_INFERENCE_KEY_ID,secret=env.KFM_HOME_INFERENCE_SECRET;
 const profile=env.KFM_HOME_INFERENCE_PROFILE,digest=env.KFM_HOME_INFERENCE_DIGEST;
 const access=env.KFM_HOME_INFERENCE_ACCESS_ID?{'CF-Access-Client-Id':env.KFM_HOME_INFERENCE_ACCESS_ID,'CF-Access-Client-Secret':env.KFM_HOME_INFERENCE_ACCESS_SECRET??''}:{};
 const checks=[],samples=[];
 const check=(name,ok,detail)=>{checks.push({name,result:ok?'PASS':'FAIL',...(detail===undefined?{}:{detail})});return ok;};
 const send=async(method,path,{body='',sign=true,signing={},headers={},access:withAccess=true}={})=>{
  const auth=sign?signRequest({keyId,secret,method,path,body,now:clock(),...signing}):{};
  const started=clock();
  try{
   const response=await fetchImpl(origin+path,{method,redirect:'manual',signal:AbortSignal.timeout(120000),headers:{...(withAccess?access:{}),...auth,...(body?{'Content-Type':'application/json'}:{}),...headers},body:body||undefined});
   const bytes=Buffer.from(await response.arrayBuffer());
   const authenticated=bytes.length<=65536&&sign&&verifyResponse({secret,requestHeaders:auth,method,path,requestBody:body,status:response.status,body:bytes,headers:response.headers});
   let value=null;try{if(bytes.length<=65536)value=JSON.parse(bytes.toString('utf8'));}catch{}
   return {status:response.ok&&!authenticated?0:response.status,value:authenticated?value:null,authenticated,ms:clock()-started};
  }catch(error){return {status:0,value:null,ms:clock()-started,error:error?.name??'FETCH_FAILED'};}
 };

 // Negative cases first: each must be refused without reaching the model.
 if(Object.keys(access).length){
  const blocked=await send('GET','/v1/health',{sign:false,access:false});
  check('access_policy_blocks_requests_without_service_token',[302,401,403].includes(blocked.status),blocked.status);
 }
 check('unsigned_request_refused',(await send('GET','/v1/health',{sign:false})).status===401);
 check('stale_signature_refused',(await send('GET','/v1/health',{signing:{now:clock()-5*60000}})).status===401);
 check('unknown_key_refused',(await send('GET','/v1/health',{signing:{keyId:'probe-not-a-key',secret:newSecret()}})).status===401);
 const nonce=randomUUID().replaceAll('-','');
 const first=await send('GET','/v1/health',{signing:{nonce}}),replay=await send('GET','/v1/health',{signing:{nonce}});
 check('replayed_request_refused',first.status===200&&replay.status===401,[first.status,replay.status]);
 check('ollama_routes_not_exposed',(await send('GET','/api/tags')).status===401);

 const health=await send('GET','/v1/health');
 const entry=health.value?.profiles?.find?.(item=>item.id===profile);
 check('health_signed_ok',health.status===200,health.status);
 check('health_response_authenticated',health.authenticated===true);
 check('profile_ready',entry?.ready===true,entry?.ready===true?undefined:entry?.reason??'PROFILE_MISSING');
 check('profile_digest_matches_pin',entry?.digest===digest);
 const result={probe:'kfm-home-inference-probe/1',at:new Date(clock()).toISOString(),origin,keyId,profile,model:entry?.model??null,digest:entry?.digest??null,runtime:health.value?.runtime??null,healthMs:health.ms,checks,samples};
 if(!entry?.ready)return finish(result);

 const chat=async prompt=>{
  const body=JSON.stringify({requestId:randomUUID(),profile,depth,messages:[{role:'system',content:'You are a concise assistant. Synthetic benchmark.'},{role:'user',content:prompt}]});
  const response=await send('POST','/v1/chat',{body});
  const bound=response.authenticated&&response.value?.requestId===JSON.parse(body).requestId&&response.value?.profile===profile&&response.value?.digest===digest&&response.value?.model===entry?.model;
  return {status:response.status===200&&!bound?0:response.status,error:response.value?.error??null,wallMs:response.ms,finishReason:response.value?.finishReason??null,chars:typeof response.value?.text==='string'?response.value.text.length:null,...(response.value?.timings??{}),outputTokens:response.value?.usage?.outputTokens??null,promptTokens:response.value?.usage?.promptTokens??null};
 };
 for(let i=0;i<runs;i++)samples.push({run:i+1,kind:'sequential',...await chat(SYNTHETIC[i%SYNTHETIC.length])});
 check('sequential_chats_completed',samples.every(sample=>sample.status===200),samples.map(sample=>sample.status));
 if(concurrency>1){
  const parallel=await Promise.all(Array.from({length:concurrency},(_,i)=>chat(SYNTHETIC[i%SYNTHETIC.length])));
  parallel.forEach((sample,i)=>samples.push({run:runs+i+1,kind:'concurrent',...sample}));
  // Either queued and served, or refused promptly as busy; never a hang or a 5xx.
  check('concurrent_chats_bounded',parallel.every(sample=>sample.status===200||sample.status===429&&sample.wallMs<10000),parallel.map(sample=>sample.status));
 }
 return finish(result);
}

function finish(result){
 const ok=result.samples.filter(sample=>sample.status===200),warm=ok.slice(1);
 const sorted=values=>values.filter(Number.isFinite).sort((a,b)=>a-b);
 const p95=values=>{const list=sorted(values);return list.length?list[Math.min(list.length-1,Math.ceil(list.length*0.95)-1)]:null;};
 result.summary={
  passed:result.checks.every(item=>item.result==='PASS'),
  coldWallMs:ok[0]?.wallMs??null,
  warmWallP95Ms:p95(warm.map(sample=>sample.wallMs)),
  tokensPerSecondMedian:sorted(ok.map(sample=>sample.tokensPerSecond))[Math.floor(ok.length/2)]??null,
  note:'Synthetic prompts only. Measures this path at this time; not a capacity or quality guarantee.',
 };
 return result;
}

if(import.meta.url===pathToFileURL(process.argv[1]??'').href){
 const arg=(name,fallback)=>{const index=process.argv.indexOf('--'+name);return index>0?process.argv[index+1]:fallback;};
 const missing=['KFM_HOME_INFERENCE_URL','KFM_HOME_INFERENCE_KEY_ID','KFM_HOME_INFERENCE_SECRET','KFM_HOME_INFERENCE_PROFILE','KFM_HOME_INFERENCE_DIGEST'].filter(name=>!process.env[name]);
 if(missing.length){console.error('missing environment: '+missing.join(', '));process.exit(2);}
 probe({runs:Math.max(1,Math.min(20,Number(arg('runs',3))||3)),depth:arg('depth','brief')==='expanded'?'expanded':'brief',concurrency:Math.max(1,Math.min(4,Number(arg('concurrency',2))||2))})
  .then(result=>{console.log(JSON.stringify(result,null,1));process.exitCode=result.summary.passed?0:1;});
}
