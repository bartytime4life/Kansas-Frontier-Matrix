// Optional, default-off Sites adapter. Reuses the existing public Qwen runtime,
// its model, source restrictions, sessions and global queue/rate budgets.
import {createHmac,timingSafeEqual} from 'node:crypto';
const SITE='appgprj_6acd1aafe0d88191a4306ea2ab44ed91';
const ORIGINS=new Set(['https://kansasfrontiermatrix.com','https://q9r9beo47t.preview.c38.airoapp.ai']);
const reply=(reasonCode,status=503)=>Response.json({reasonCode},{status,headers:{'Cache-Control':'private, no-store'}});
export function createSitesQwenHandler({token,origin,handle,clock=Date.now}){
 const sessions=new Map();
 return async request=>{
  const expected=typeof token==='string'&&/^[A-Za-z0-9_-]{43,128}$/.test(token)?Buffer.from('Bearer '+token):null;
  const actual=Buffer.from(request.headers.get('authorization')??'');
  if(!expected||!ORIGINS.has(origin)||actual.length!==expected.length||!timingSafeEqual(actual,expected)||request.headers.get('x-kfm-site')!==SITE)return reply('SITES_QWEN_UNAUTHORIZED',401);
  const actor=request.headers.get('x-kfm-site-actor')??'';
  if(!/^[a-f0-9]{64}$/.test(actor))return reply('INVALID_ACTOR',400);
  const url=new URL(request.url),path=url.pathname.replace(/^\/api\/sites-qwen\/v1\//,'');
  if(url.search||!((request.method==='GET'&&(path==='status'||/^jobs\/[A-Za-z0-9_-]{43}$/.test(path)))||(request.method==='POST'&&(path==='jobs'||/^jobs\/[A-Za-z0-9_-]{43}\/cancel$/.test(path)))))return reply('ROUTE_NOT_FOUND',404);
  const now=clock();for(const [key,s]of sessions)if(s.expires<=now)sessions.delete(key);
  const owner=createHmac('sha256',token).update(SITE+'\0'+actor).digest('hex');
  const base=origin+'/api/ai/';
  const status=await handle(new Request(base+'status'));
  const state=await status.json();
  // Never run the old SmolLM2 model, PC worker or a different model as fallback.
  if(!status.ok||state.provider!=='hosted-qwen3'||state.model!=='Qwen3-0.6B INT8 · server WebAssembly')return reply('QWEN_MODEL_MISMATCH');
  if(path==='status')return Response.json({...state,model:'onnx-community/Qwen3-0.6B-ONNX'},{headers:{'Cache-Control':'private, no-store'}});
  let body;
  if(request.method==='POST'){
   const reader=request.body?.getReader();if(!reader)return reply('INVALID_REQUEST',400);
   let bytes=0,timer;const parts=[],timeout=new Promise((_,reject)=>{timer=setTimeout(()=>reject(Error('BODY_TIMEOUT')),8000);});
   try{for(;;){const next=await Promise.race([reader.read(),timeout]);if(next.done)break;bytes+=next.value.length;if(bytes>16384)throw Error();parts.push(next.value);}body=JSON.parse(new TextDecoder('utf-8',{fatal:true}).decode(Buffer.concat(parts)));}catch{await reader.cancel().catch(()=>{});return reply('INVALID_REQUEST',400);}finally{clearTimeout(timer);}
   if(path==='jobs'){
    if(!body||typeof body!=='object'||Array.isArray(body)||body.mode!=='explore'||Object.keys(body).some(k=>!['question','term','mode','style','depth','context','investigationId','place','start','end'].includes(k)))return reply('DISCUSSION_ONLY',400);
    const c=body.context;
    if(c!==undefined&&(!c||c.version!==1||c.selection!==null||!Array.isArray(c.layers)||c.layers.length||!Number.isInteger(c.frame)||c.frame< -5e9||c.frame>2200||!['2D','Terrain 3D','Globe','Page'].includes(c.view)))return reply('CONTEXT_WITHHELD',403);
    body={...body,place:'',start:'',end:'',...(c?{context:{version:1,frame:c.frame,view:c.view,surface:'map',layers:[],selection:null}}:{})};
    if(!sessions.has(owner)&&sessions.size>=100)return reply('QUEUE_FULL',429);
   }else if(!body||typeof body!=='object'||Array.isArray(body)||Object.keys(body).length)return reply('INVALID_REQUEST',400);
  }
  const session=sessions.get(owner);
  if(path!=='jobs'&&!session)return reply('SESSION_REQUIRED',401);
  const result=await handle(new Request(base+path,{method:request.method,signal:request.signal,headers:{origin,'content-type':'application/json',...(session?{cookie:session.cookie}:{})},body:body===undefined?undefined:JSON.stringify(body)}));
  const cookie=result.headers.get('set-cookie')?.split(';')[0];
  if(cookie&&/^__Host-kfm_ai_guest=[A-Za-z0-9_-]{43}$/.test(cookie))sessions.set(owner,{cookie,expires:now+3600000});
  // Private Node cookies never cross the adapter. Guest/job ownership stays in Node.
  const headers=new Headers({'Cache-Control':'private, no-store','Content-Type':'application/json','X-Content-Type-Options':'nosniff'});
  if(result.headers.has('retry-after'))headers.set('retry-after',result.headers.get('retry-after'));
  return new Response(result.body,{status:result.status,headers});
 };
}
