import { PcAiStore, matchesToken, digest } from './pc-ai-store.mjs';
import { QWEN_LOCAL_MODEL, QWEN_LOCAL_MODEL_DIGEST, isSupportedOllamaVersion, localQwenAnswerHasOverPreciseLocation } from '../scripts/qwen-local-contract.mjs';
import { isSensitiveQwenQuestion } from '../scripts/local-qwen-bridge.mjs';
const HEADERS={'Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff','Vary':'Cookie','Cross-Origin-Resource-Policy':'same-origin'};
const reply=(value,status=200,extra={})=>Response.json(value,{status,headers:{...HEADERS,...extra}});
const envelope=(outcome,reasonCode,answer=null,evidenceRefs=[])=>({outcome,reasonCode,answer,evidenceRefs,interpretation:null});
const packetDigest=packet=>digest(JSON.stringify(packet));
const text=(value,max)=>typeof value==='string'&&value.length>0&&Buffer.byteLength(value)<=max&&!/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/.test(value);
const exactKeys=(object,allowed)=>object&&typeof object==='object'&&!Array.isArray(object)&&Object.keys(object).every(key=>allowed.includes(key));
const day=value=>value===''||/^\d{4}-\d{2}-\d{2}$/.test(value)&&Number.isFinite(Date.parse(value+'T00:00:00Z'))&&new Date(value+'T00:00:00Z').toISOString().slice(0,10)===value;
async function json(request){
  if(!/^application\/json(?:;|$)/i.test(request.headers.get('content-type')??''))throw new Error('JSON_REQUIRED');
  const reader=request.body?.getReader();if(!reader)throw new Error('INVALID_REQUEST');
  const chunks=[];let bytes=0;
  const signal=AbortSignal.timeout(5000);
  const aborted=new Promise((_,reject)=>signal.addEventListener('abort',()=>reject(new Error('BODY_TIMEOUT')),{once:true}));
  try{while(true){const part=await Promise.race([reader.read(),aborted]);if(part.done)break;bytes+=part.value.length;if(bytes>32768)throw new Error('REQUEST_TOO_LARGE');chunks.push(Buffer.from(part.value));}
    const value=JSON.parse(Buffer.concat(chunks).toString('utf8'));if(!value||typeof value!=='object'||Array.isArray(value))throw new Error('INVALID_REQUEST');return value;
  }finally{await reader.cancel().catch(()=>{});reader.releaseLock();}
}
export function validatePcResult(raw,packet){
  if(!exactKeys(raw,['outcome','claims','interpretation'])||!['ANSWER','ABSTAIN','ERROR'].includes(raw.outcome)||!Array.isArray(raw.claims)||raw.claims.length>8)throw new Error('INVALID_MODEL_RESPONSE');
  if(raw.outcome!=='ANSWER'){
    if(raw.claims.length!==0)throw new Error('INVALID_MODEL_RESPONSE');
    return envelope(raw.outcome,raw.outcome==='ABSTAIN'?'EVIDENCE_NOT_SUPPORTIVE':'INFERENCE_FAILED');
  }
  if(!raw.claims.length||!text(raw.interpretation,4000))throw new Error('INVALID_MODEL_RESPONSE');
  if(localQwenAnswerHasOverPreciseLocation(raw.interpretation)||/https?:\/\/|\bkfm:/i.test(raw.interpretation))throw new Error('INVALID_MODEL_RESPONSE');
  const claims=raw.claims.map(claim=>{
    if(!exactKeys(claim,['evidenceRef','text'])||!text(claim.text,800))throw new Error('INVALID_MODEL_RESPONSE');
    const fact=packet.evidence.find(item=>item.evidenceRef===claim.evidenceRef&&item.text===claim.text&&item.status==='documented');
    if(!fact)throw new Error('UNSUPPORTED_CLAIM');
    return fact;
  });
  if(new Set(claims.map(item=>item.evidenceRef+'\n'+item.text)).size!==claims.length)throw new Error('INVALID_MODEL_RESPONSE');
  return {...envelope('ANSWER','RELEASED_EVIDENCE_INTERPRETATION',claims.map(item=>item.text).join('\n'),[...new Set(claims.map(item=>item.evidenceRef))]),
    interpretation:raw.interpretation,citations:claims.map(item=>({evidenceRef:item.evidenceRef,title:item.title,url:item.url})),releaseId:packet.releaseId,truncated:Boolean(packet.truncated)};
}

/** Evidence resolver is server-owned. The browser cannot supply evidence or release state. */
export function createPcAiHandler({store,origin,adminHash,workerHash,resolveEvidence}){
  const session=request=>(request.headers.get('cookie')??'').split(';').map(item=>item.trim()).find(item=>item.startsWith('__Host-kfm_pc_session='))?.slice('__Host-kfm_pc_session='.length)??null;
  const authorized=(request,hash)=>matchesToken((request.headers.get('authorization')??'').replace(/^Bearer /,''),hash);
  const currentPacket=async query=>{
    const result=await resolveEvidence(query);
    if(!result||!Array.isArray(result.evidence)||result.evidence.length>40||!/^sha256:[a-f0-9]{64}$/.test(result.releaseId??''))return null;
    for(const item of result.evidence){
      if(!exactKeys(item,['evidenceRef','text','status','title','url'])||!text(item.evidenceRef,240)||!text(item.text,800)||!text(item.title,200)||item.status!=='documented')throw new Error('EVIDENCE_WITHHELD');
      const url=new URL(item.url,origin);if(url.origin!==origin||!url.pathname.startsWith('/knowledge/record')||url.username||url.password)throw new Error('EVIDENCE_WITHHELD');
    }
    if(!result.evidence.length||Buffer.byteLength(JSON.stringify(result))>24000)return null;
    return result;
  };
  const stillReleased=async packet=>{
    if(!packet)return false;
    const fresh=await currentPacket(packet.query);
    return Boolean(fresh&&packetDigest(fresh)===packet.evidenceDigest);
  };
  return async request=>{
    try{
      const path=new URL(request.url).pathname.replace(/^\/api\/pc-ai\//,'');
      const worker=path.startsWith('worker/'),admin=path.startsWith('admin/');
      if(request.method!=='GET'&&request.method!=='POST')return reply({reasonCode:'METHOD_DENIED'},405);
      if(request.method==='POST'&&!worker&&!admin&&request.headers.get('origin')!==origin)return reply({reasonCode:'ORIGIN_DENIED'},403);
      if((worker||admin)&&request.headers.get('origin')&&request.headers.get('origin')!==origin)return reply({reasonCode:'ORIGIN_DENIED'},403);
      if(worker&&!authorized(request,workerHash)||admin&&!authorized(request,adminHash))return reply({reasonCode:'ACCESS_DENIED'},401);
      if(path==='status'&&request.method==='GET')return reply({configured:true,...store.availability(),model:QWEN_LOCAL_MODEL,account:store.account(session(request))?.username??null});
      if(path==='admin/invite'&&request.method==='POST'){
        const body=await json(request);if(!exactKeys(body,['username']))throw new Error('INVALID_REQUEST');
        return reply(store.invite(body.username),201);
      }
      if(path==='admin/revoke'&&request.method==='POST'){
        const body=await json(request);if(!exactKeys(body,['username']))throw new Error('INVALID_REQUEST');store.revoke(body.username);return reply({revoked:true});
      }
      if(['sign-in','activate'].includes(path)&&request.method==='POST'){
        const body=await json(request);if(!exactKeys(body,path==='activate'?['username','password','invitation']:['username','password']))throw new Error('INVALID_REQUEST');
        if(path==='activate'&&!text(body.invitation,43))throw new Error('INVALID_REQUEST');
        const signed=store.authenticate(body.username,body.password,path==='activate'?body.invitation:null);
        return reply({username:signed.username},200,{'Set-Cookie':`__Host-kfm_pc_session=${signed.session}; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=14400`});
      }
      if(path==='sign-out'&&request.method==='POST'){
        store.signOut(session(request));return reply({signedOut:true},200,{'Set-Cookie':'__Host-kfm_pc_session=; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=0'});
      }
      if(path==='worker/heartbeat'&&request.method==='POST'){
        const body=await json(request);if(!exactKeys(body,['ready','model','digest','version']))throw new Error('INVALID_REQUEST');
        const ready=body.ready===true&&body.model===QWEN_LOCAL_MODEL&&body.digest===QWEN_LOCAL_MODEL_DIGEST&&isSupportedOllamaVersion(body.version);
        store.heartbeat(ready);return reply({ready});
      }
      if(path==='worker/claim'&&request.method==='POST'){
        const body=await json(request);if(Object.keys(body).length)throw new Error('INVALID_REQUEST');
        return reply({job:store.claim()});
      }
      if(path==='worker/check'&&request.method==='POST'){
        const body=await json(request);if(!exactKeys(body,['id','lease']))throw new Error('INVALID_REQUEST');
        return reply({active:Boolean(store.leased(body.id,body.lease))});
      }
      if(path==='worker/result'&&request.method==='POST'){
        const body=await json(request);if(!exactKeys(body,['id','lease','result']))throw new Error('INVALID_REQUEST');
        const job=store.leased(body.id,body.lease);if(!job)return reply({reasonCode:'LEASE_LOST'},409);
        const result=await stillReleased(job.packet)?validatePcResult(body.result,job.packet):envelope('ABSTAIN','RELEASE_CHANGED');
        store.complete(body.id,body.lease,result);return reply({accepted:true});
      }
      const account=store.account(session(request));if(!account)return reply({reasonCode:'SIGN_IN_REQUIRED'},401);
      if(path==='jobs'&&request.method==='POST'){
        const body=await json(request);
        if(!exactKeys(body,['question','term','place','start','end'])||!text(body.question,4096)||!text(body.term,120))throw new Error('INVALID_REQUEST');
        const query={term:body.term,place:body.place??'',start:body.start??'',end:body.end??''};
        if(![query.place,query.start,query.end].every(value=>typeof value==='string')||query.place.length>160||![query.start,query.end].every(day)||query.start&&query.end&&query.start>query.end)throw new Error('INVALID_REQUEST');
        if(!store.availability().ready)throw new Error('PC_OFFLINE');
        const sensitive=isSensitiveQwenQuestion(body.question)||/\b(?:dna|living person|rare species|archaeological site|critical infrastructure)\b/i.test(body.question);
        const evidence=sensitive?null:await currentPacket(query);
        const packet=evidence?{question:body.question,query,...evidence,evidenceDigest:packetDigest(evidence)}:null;
        const id=store.enqueue(account.id,packet,evidence?null:envelope(sensitive?'DENY':'ABSTAIN',sensitive?'POLICY_WITHHELD':'NO_RELEASED_EVIDENCE'));
        return reply({id},202);
      }
      const match=/^jobs\/([A-Za-z0-9_-]{43})(\/cancel)?$/.exec(path);
      if(match){
        const job=store.read(match[1],account.id);if(!job)return reply({reasonCode:'JOB_NOT_FOUND'},404);
        if(match[2]&&request.method==='POST')return reply({cancelled:store.cancel(job.id,account.id)});
        if(!match[2]&&request.method==='GET'){
          const result=job.result?.outcome==='ANSWER'&&!await stillReleased(job.packet)?envelope('ABSTAIN','RELEASE_CHANGED'):job.result;
          return reply({id:job.id,state:job.state,deadline:job.deadline,result});
        }
      }
      return reply({reasonCode:'ROUTE_NOT_FOUND'},404);
    }catch(error){
      const known=['SIGN_IN_DENIED','SIGN_IN_RATE_LIMIT','INVALID_REQUEST','JSON_REQUIRED','REQUEST_TOO_LARGE','BODY_TIMEOUT','PC_OFFLINE','USER_RATE_LIMIT','USER_BUSY','QUEUE_FULL','ACCOUNT_LIMIT','ACCOUNT_EXISTS','INVALID_USERNAME','LEASE_LOST','INVALID_MODEL_RESPONSE','UNSUPPORTED_CLAIM','EVIDENCE_WITHHELD'];
      const code=known.includes(error.message)?error.message:'PC_AI_UNAVAILABLE';
      const status=['SIGN_IN_DENIED'].includes(code)?401:['SIGN_IN_RATE_LIMIT','USER_RATE_LIMIT','QUEUE_FULL'].includes(code)?429:['PC_OFFLINE','PC_AI_UNAVAILABLE'].includes(code)?503:400;
      return reply({reasonCode:code},status);
    }
  };
}

let runtime,failedAt=0;
export function pcAiRuntime(resolveEvidence){
  const environment=process.env;
  const valid=environment.KFM_PC_ENABLED==='true'&&environment.KFM_PC_STORAGE_MODE==='single-writer-confirmed'&&['preview','published'].includes(environment.KFM_PC_ROLE)&&/^https:\/\//.test(environment.KFM_PC_ORIGIN??'')&&/^[a-f0-9]{64}$/.test(environment.KFM_PC_ADMIN_TOKEN_HASH??'')&&/^[a-f0-9]{64}$/.test(environment.KFM_PC_WORKER_TOKEN_HASH??'')&&/^[A-Za-z0-9_-]{43}$/.test(environment.KFM_PC_DATA_KEY??'');
  if(!valid||environment.KFM_PC_ADMIN_TOKEN_HASH===environment.KFM_PC_WORKER_TOKEN_HASH)return async request=>reply({configured:false,online:false,ready:false,reasonCode:'PC_AI_NOT_CONFIGURED'},new URL(request.url).pathname==='/api/pc-ai/status'?200:503);
  if(failedAt&&Date.now()-failedAt<60000)throw new Error('PC_AI_STORAGE_HOLD');
  if(!runtime){
    const url=new URL(environment.KFM_PC_ORIGIN);
    if(url.origin!==environment.KFM_PC_ORIGIN||url.username||url.password||url.port||!['kansasfrontiermatrix.com','q9r9beo47t.preview.c38.airoapp.ai'].includes(url.hostname)||environment.KFM_PC_ROLE==='published'&&url.hostname!=='kansasfrontiermatrix.com'||environment.KFM_PC_ROLE==='preview'&&url.hostname!=='q9r9beo47t.preview.c38.airoapp.ai')throw new Error('PC_AI_ORIGIN_UNQUALIFIED');
    let store;
    try{store=new PcAiStore({root:'/private',role:environment.KFM_PC_ROLE,key:environment.KFM_PC_DATA_KEY});}
    catch(error){failedAt=Date.now();throw error;}
    runtime=createPcAiHandler({store,origin:url.origin,adminHash:environment.KFM_PC_ADMIN_TOKEN_HASH,workerHash:environment.KFM_PC_WORKER_TOKEN_HASH,resolveEvidence});
  }
  return runtime;
}
