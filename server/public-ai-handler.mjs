// Public chat owns only short-lived anonymous jobs; account/admin APIs stay separate.
import {randomBytes,createHash} from 'node:crypto';
import {localQwenAnswerHasOverPreciseLocation} from '../scripts/qwen-local-contract.mjs';
import {isSensitiveQwenQuestion} from '../scripts/local-qwen-bridge.mjs';
import {getHostedAiModel,HOSTED_MODEL,hasRepeatedPhrase,PUBLIC_AI_JOB_MS} from './hosted-ai.mjs';
import {validAssistantContext} from './assistant-context.mjs';
const headers={'Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff','Vary':'Cookie','Cross-Origin-Resource-Policy':'same-origin'};
const reply=(body,status=200,extra={})=>Response.json(body,{status,headers:{...headers,...extra}});
const envelope=(outcome,reasonCode)=>({outcome,reasonCode,answer:null,evidenceRefs:[],interpretation:null});
const token=()=>randomBytes(32).toString('base64url');
const digest=value=>createHash('sha256').update(JSON.stringify(value)).digest('hex');
const text=(x,max)=>typeof x==='string'&&x.length>0&&Buffer.byteLength(x)<=max&&!/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/.test(x);
const date=x=>x===''||/^\d{4}-\d{2}-\d{2}$/.test(x)&&Number.isFinite(Date.parse(x+'T00:00:00Z'))&&new Date(x+'T00:00:00Z').toISOString().slice(0,10)===x;
async function body(request){
 if(!/^application\/json(?:;|$)/i.test(request.headers.get('content-type')??''))throw new Error('INVALID_REQUEST');
 const reader=request.body?.getReader();if(!reader)throw new Error('INVALID_REQUEST');
 const chunks=[];let bytes=0,timer;
 const timeout=new Promise((_,reject)=>{timer=setTimeout(()=>reject(new Error('BODY_TIMEOUT')),5000);});
 try{while(true){const part=await Promise.race([reader.read(),timeout]);if(part.done)break;bytes+=part.value.length;if(bytes>8192)throw new Error('REQUEST_TOO_LARGE');chunks.push(Buffer.from(part.value));}
  const value=JSON.parse(Buffer.concat(chunks).toString());if(!value||typeof value!=='object'||Array.isArray(value))throw new Error('INVALID_REQUEST');return value;
 }finally{clearTimeout(timer);await reader.cancel().catch(()=>{});reader.releaseLock();}
}
export function createPublicAiHandler({origin,resolveEvidence,resolveContext=async()=>{throw new Error('CONTEXT_UNAVAILABLE');},model,clock=Date.now}){
 const sessions=new Map(),jobs=new Map();let requests=[],draining=false;
 const cookie=request=>(request.headers.get('cookie')??'').split(';').map(x=>x.trim()).find(x=>x.startsWith('__Host-kfm_ai_guest='))?.slice(20)??'';
 const cleanup=()=>{
  const now=clock();requests=requests.filter(t=>t>now-3600000);
  for(const [key,value]of sessions){if(value.created<=now-3600000)sessions.delete(key);else value.history=(value.history??[]).filter(item=>item.at>now-900000);}
  for(const [key,job]of jobs){
   if(job.deadline<=now&&['preparing','queued','running'].includes(job.state)){job.abort?.abort();job.state='expired';job.packet=null;job.result=null;job.question='';job.query=null;job.context=null;}
   if(job.created<=now-900000){job.abort?.abort();jobs.delete(key);}
  }
 };
 const cleanupTimer=setInterval(cleanup,30000);cleanupTimer.unref?.();
 const packet=async query=>{
  let timer;const timeout=new Promise((_,reject)=>{timer=setTimeout(()=>reject(new Error('EVIDENCE_WITHHELD')),8000);});
  let value;try{value=await Promise.race([resolveEvidence(query),timeout]);}finally{clearTimeout(timer);}
  if(!value||!Array.isArray(value.evidence)||value.evidence.length>40||!/^sha256:[a-f0-9]{64}$/.test(value.releaseId??'')||Buffer.byteLength(JSON.stringify(value))>24000)return null;
  for(const fact of value.evidence){
   if(!fact||Object.keys(fact).some(k=>!['evidenceRef','text','status','title','url'].includes(k))||!text(fact.evidenceRef,240)||!text(fact.text,800)||!text(fact.title,200)||fact.status!=='documented')throw new Error('EVIDENCE_WITHHELD');
   const url=new URL(fact.url,origin);if(url.origin!==origin||!url.pathname.startsWith('/knowledge/record')||url.username||url.password)throw new Error('EVIDENCE_WITHHELD');
  }
  return value.evidence.length?{releaseId:value.releaseId,evidence:value.evidence,truncated:Boolean(value.truncated)}:null;
 };
 const fresh=async job=>{const value=await packet(job.query);return Boolean(value&&digest(value)===job.evidenceDigest);};
 const evidenceResult=async job=>{
  if(!await fresh(job))return envelope('ABSTAIN','RELEASE_CHANGED');
  // Deterministic discovery does not require inference or factual selection.
  // Keep the answer withheld and expose only the rechecked reader's links.
  return {...envelope('ABSTAIN','EVIDENCE_MODEL_UNQUALIFIED'),citations:job.packet.evidence.slice(0,4).map(fact=>({evidenceRef:fact.evidenceRef,title:fact.title,url:fact.url})),truncated:job.packet.truncated||job.packet.evidence.length>4};
 };
 const completeEvidence=async job=>{
  job.state='running';
  try{
   const result=await evidenceResult(job);
   if(job.state==='running'&&clock()<job.deadline){job.state='completed';job.result=result;}
   else if(job.state==='running'){job.state='expired';job.result=null;}
  }catch{
   if(job.state==='running'){
    job.state=clock()<job.deadline?'completed':'expired';
    job.result=job.state==='completed'?envelope('ABSTAIN','EVIDENCE_WITHHELD'):null;
   }
  }finally{job.question='';if(!job.result?.citations?.length){job.packet=null;job.query=null;}}
 };
 const drain=async()=>{
  if(draining)return;draining=true;
  try{while(true){
   cleanup();const job=[...jobs.values()].find(j=>j.state==='queued');if(!job)break;
   if(!model.ready){job.state='completed';job.result=envelope('ERROR','MODEL_UNAVAILABLE');job.packet=null;job.question='';job.query=null;continue;}
   job.state='running';job.abort=new AbortController();const timer=setTimeout(()=>job.abort.abort(),Math.max(1,job.deadline-clock()));timer.unref?.();
   try{
    if(job.mode==='explore'){
     const session=sessions.get(job.owner);
     const discussion=await model.discuss(job.question,{style:job.style,depth:job.depth,context:job.context?.prompt??'',history:(session?.history??[]).filter(item=>item.contextKey===job.contextKey).map(({question,reply})=>({question,reply}))},job.abort.signal);
     if(job.state!=='running'||job.abort.signal.aborted)continue;
     const output=discussion?.text;
     if(!text(output,4096)||hasRepeatedPhrase(output)||/https?:\/\/|www\.|\bkfm:/i.test(output)||localQwenAnswerHasOverPreciseLocation(output))job.result=envelope('ABSTAIN','MODEL_OUTPUT_UNQUALIFIED');
     else{
      job.result={...envelope('ABSTAIN','UNVERIFIED_AI_DISCUSSION'),interpretation:output,followUpQuestion:'Would you like a deeper explanation, a practical example, or help exploring the relevant map layers?',contextLimited:Boolean(discussion.contextTrimmed),outputLimited:Boolean(discussion.outputLimited)};
      if(session)session.history=[...(session.history??[]).filter(item=>item.contextKey===job.contextKey),{question:job.question,reply:output,contextKey:job.contextKey,at:clock()}].slice(-2);
     }
    }
   }catch(error){if(job.state==='running')job.result=envelope(error.code==='MODEL_CONTEXT_LIMIT'?'ABSTAIN':'ERROR',error.code==='MODEL_CONTEXT_LIMIT'?'MODEL_CONTEXT_LIMIT':'MODEL_UNAVAILABLE');}
   finally{clearTimeout(timer);if(job.state==='running'){job.state=job.abort.signal.aborted?'expired':'completed';if(job.state==='expired')job.result=null;}job.abort=null;job.question='';if(!job.result?.citations?.length){job.packet=null;job.query=null;}}
  }}finally{draining=false;}
 };
 return async request=>{
  cleanup();const path=new URL(request.url).pathname.replace(/^\/api\/ai\//,'');
  if(!['GET','POST'].includes(request.method))return reply({reasonCode:'METHOD_DENIED'},405);
  if(new URL(request.url).origin!==origin)return reply({reasonCode:'AI_ORIGIN_HOLD'},503);
  if(request.method==='POST'&&(request.headers.get('origin')!==origin||request.headers.get('sec-fetch-site')==='cross-site'))return reply({reasonCode:'ORIGIN_DENIED'},403);
  if(path==='status'&&request.method==='GET')return reply({configured:true,online:model.online,ready:model.ready,evidenceSearchAvailable:true,requiresLogin:false,provider:'hosted-smollm2',model:HOSTED_MODEL});
  let guest=cookie(request),session=sessions.get(digest(guest)),extra={};
  try{
   if(path==='jobs'&&request.method==='POST'){
    const value=await body(request);
    if(Object.keys(value).some(k=>!['question','term','place','start','end','mode','style','depth','context'].includes(k))||!text(value.question,4096)||!text(value.term,120))throw new Error('INVALID_REQUEST');
    if(value.context!==undefined&&!validAssistantContext(value.context))throw new Error('INVALID_REQUEST');
    const mode=value.mode??'evidence',style=value.style??'plain',depth=value.depth??'brief';
    if(!['explore','evidence'].includes(mode)||!['plain','technical'].includes(style)||!['brief','expanded'].includes(depth))throw new Error('INVALID_REQUEST');
    const query={term:value.term,place:value.place??'',start:value.start??'',end:value.end??''};
    if(typeof query.place!=='string'||query.place.length>160||!date(query.start)||!date(query.end)||query.start&&query.end&&query.start>query.end)throw new Error('INVALID_REQUEST');
    if(requests.length>=30)throw new Error('GLOBAL_RATE_LIMIT');
    if(!session){
     if(sessions.size>=100)throw new Error('QUEUE_FULL');
     guest=token();session={created:clock(),requests:[],history:[]};sessions.set(digest(guest),session);
     extra={'Set-Cookie':'__Host-kfm_ai_guest='+guest+'; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=3600'};
    }
    session.requests=session.requests.filter(t=>t>clock()-3600000);
    if(session.requests.length>=10)throw new Error('USER_RATE_LIMIT');
    if([...jobs.values()].some(j=>j.owner===digest(guest)&&['preparing','queued','running'].includes(j.state)))throw new Error('USER_BUSY');
    if([...jobs.values()].filter(j=>['preparing','queued','running'].includes(j.state)).length>=3)throw new Error('QUEUE_FULL');
    const now=clock(),job={id:token(),owner:digest(guest),question:value.question,query,mode,style,depth,state:'preparing',created:now,deadline:now+(mode==='explore'?PUBLIC_AI_JOB_MS:90000),packet:null,result:null};
    jobs.set(job.id,job);requests.push(now);session.requests.push(now);
    try{
     const questionScope=value.question+' '+(value.context?JSON.stringify(value.context):'');
     const sensitive=isSensitiveQwenQuestion(questionScope)||/\b(?:dna|living person|rare species|archaeological site|critical infrastructure)\b/i.test(questionScope);
     if(!sensitive&&value.context){
      let timer;
      try{
       job.context=await Promise.race([resolveContext(value.context),new Promise((_,reject)=>{timer=setTimeout(()=>reject(new Error('CONTEXT_UNAVAILABLE')),5000);})]);
       if(!job.context||!text(job.context.prompt,2400)||!text(job.context.label,240)||!text(job.context.boundary,240))throw new Error('CONTEXT_UNAVAILABLE');
       if(job.context.sourceSummary!==undefined&&(!text(job.context.sourceSummary,4096)||isSensitiveQwenQuestion(job.context.sourceSummary)||localQwenAnswerHasOverPreciseLocation(job.context.sourceSummary)))throw new Error('CONTEXT_UNAVAILABLE');
       if(isSensitiveQwenQuestion(job.context.prompt)||localQwenAnswerHasOverPreciseLocation(job.context.prompt))throw new Error('POLICY_WITHHELD');
      }finally{clearTimeout(timer);}
     }
     job.contextKey=job.context?digest({selector:value.context,sourceKey:job.context.key,prompt:job.context.prompt}):'no-context';
     const evidence=sensitive||mode==='explore'?null:await packet(query);
     if(job.state!=='preparing'||clock()>=job.deadline){job.state='expired';return reply({id:job.id},202,extra);}
     if(!sensitive&&mode==='explore'&&value.context?.selection?.kind==='subsurface'){
      // Only the server resolver may supply the summary. Client fields and
      // model prose cannot establish source facts or dates.
      job.state='completed';job.result=job.context?.sourceSummary?{...envelope('ABSTAIN','SOURCE_CONTEXT_ONLY'),sourceSummary:job.context.sourceSummary,followUpQuestion:'Would you like to inspect the original source intervals or compare nearby wells and aquifer ranges?'}:envelope('ABSTAIN','CONTEXT_UNAVAILABLE');job.question='';job.query=null;
     }
     else if(!sensitive&&mode==='explore'){job.state='queued';void drain();}
     else if(!evidence){job.state='completed';job.result=envelope(sensitive?'DENY':'ABSTAIN',sensitive?'POLICY_WITHHELD':'NO_RELEASED_EVIDENCE');job.question='';job.query=null;}
     else{
      job.packet=evidence;job.evidenceDigest=digest(evidence);
      // Return the opaque job promptly; do not queue discovery behind inference.
      void completeEvidence(job);
     }
    }catch(error){if(job.state!=='preparing')return reply({id:job.id},202,extra);const code=['CONTEXT_UNAVAILABLE','CONTEXT_TIME_MISMATCH','POLICY_WITHHELD'].includes(error.message)?error.message:'EVIDENCE_WITHHELD';job.state='completed';job.result=envelope(code==='POLICY_WITHHELD'?'DENY':'ABSTAIN',code);job.question='';job.packet=null;job.query=null;job.context=null;}
    return reply({id:job.id},202,extra);
   }
   const match=/^jobs\/([A-Za-z0-9_-]{43})(\/cancel)?$/.exec(path);
   if(match){
    if(!session)return reply({reasonCode:'SESSION_REQUIRED'},401);
    const job=jobs.get(match[1]);if(!job||job.owner!==digest(guest))return reply({reasonCode:'JOB_NOT_FOUND'},404);
    if(match[2]&&request.method==='POST'){
     const value=await body(request);if(Object.keys(value).length)throw new Error('INVALID_REQUEST');
     const cancelled=['preparing','queued','running'].includes(job.state);if(cancelled){job.state='cancelled';job.abort?.abort();job.packet=null;job.result=null;job.context=null;job.question='';job.query=null;}
     return reply({cancelled});
    }
    if(!match[2]&&request.method==='GET'){
     let result=job.result;
     if(result?.outcome==='ANSWER'||result?.citations?.length){try{if(!await fresh(job))result=envelope('ABSTAIN','RELEASE_CHANGED');}catch{result=envelope('ABSTAIN','RELEASE_CHANGED');}}
     return reply({id:job.id,state:job.state,mode:job.mode,deadline:job.deadline,result,context:job.context?{label:job.context.label,boundary:job.context.boundary}:null});
    }
   }
   return reply({reasonCode:'ROUTE_NOT_FOUND'},404);
  }catch(error){
   const code=['INVALID_REQUEST','BODY_TIMEOUT','REQUEST_TOO_LARGE','GLOBAL_RATE_LIMIT','USER_RATE_LIMIT','USER_BUSY','QUEUE_FULL'].includes(error.message)?error.message:'AI_UNAVAILABLE';
   return reply({reasonCode:code},['GLOBAL_RATE_LIMIT','USER_RATE_LIMIT','QUEUE_FULL'].includes(code)?429:code==='AI_UNAVAILABLE'?503:400,extra);
  }
 };
}
let runtime;
export function publicAiRuntime(resolveEvidence,resolveContext){
 const origin=process.env.KFM_HOSTED_AI_ORIGIN;
 const valid=process.env.KFM_HOSTED_AI==='1'&&['https://kansasfrontiermatrix.com','https://q9r9beo47t.preview.c38.airoapp.ai'].includes(origin);
 if(!valid)return async request=>reply({configured:false,online:false,ready:false,evidenceSearchAvailable:false,requiresLogin:false,reasonCode:'HOSTED_AI_NOT_CONFIGURED'},new URL(request.url).pathname==='/api/ai/status'?200:503);
 if(!runtime)runtime=createPublicAiHandler({origin,resolveEvidence:query=>resolveEvidence(query,origin),resolveContext,model:getHostedAiModel()});
 return runtime;
}
