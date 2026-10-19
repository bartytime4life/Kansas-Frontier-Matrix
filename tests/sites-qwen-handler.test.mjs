import test from 'node:test';
import assert from 'node:assert/strict';
import {createSitesQwenHandler} from '../server/sites-qwen-handler.mjs';
const origin='https://q9r9beo47t.preview.c38.airoapp.ai',token='s'.repeat(43),actor='a'.repeat(64),site='appgprj_6acd1aafe0d88191a4306ea2ab44ed91';
const req=(path,body,headers={})=>new Request(origin+'/api/sites-qwen/v1/'+path,{method:body===undefined?'GET':'POST',headers:{Authorization:'Bearer '+token,'X-KFM-Site':site,'X-KFM-Site-Actor':actor,...headers},body:body===undefined?undefined:JSON.stringify(body)});
const status=()=>Response.json({provider:'hosted-qwen3',model:'Qwen3-0.6B INT8 · server WebAssembly',ready:true,online:true});
const question={question:'Explain missing values',term:'missing',mode:'explore',context:{version:1,frame:2026,view:'2D',surface:'map',layers:[],selection:null}};
test('adapter is off without a token and refuses wrong token, Site, actor and arbitrary routes',async()=>{
 let calls=0;const handle=async()=>{calls++;return status();};
 assert.equal((await createSitesQwenHandler({origin,handle})(req('status'))).status,401);
 const h=createSitesQwenHandler({token,origin,handle});
 for(const headers of [{Authorization:'Bearer wrong'},{'X-KFM-Site':'other'},{'X-KFM-Site-Actor':'bad'}])assert.ok((await h(req('status',undefined,headers))).status>=400);
 assert.equal((await h(req('../admin/invite',{}))).status,404);assert.equal(calls,0);
});
test('status names only pinned Qwen and never falls back to the previous model',async()=>{
 const h=createSitesQwenHandler({token,origin,handle:async()=>status()});assert.equal((await(await h(req('status'))).json()).model,'onnx-community/Qwen3-0.6B-ONNX');
 const bad=createSitesQwenHandler({token,origin,handle:async()=>Response.json({provider:'hosted-smollm2',ready:true})});assert.equal((await bad(req('jobs',question))).status,503);
});
test('public runtime cookies stay private and actor sessions remain separate',async()=>{
 const calls=[];const handle=async request=>{
  if(new URL(request.url).pathname.endsWith('/status'))return status();
  calls.push({path:new URL(request.url).pathname,cookie:request.headers.get('cookie'),body:request.method==='POST'?await request.json():null});
  return Response.json({id:'j'.repeat(43),deadline:123},{headers:{'Set-Cookie':'__Host-kfm_ai_guest='+'g'.repeat(43)+'; Secure; HttpOnly'}});
 };
 const h=createSitesQwenHandler({token,origin,handle});const result=await h(req('jobs',question));assert.equal(result.headers.get('set-cookie'),null);
 await h(req('jobs/'+'j'.repeat(43)));assert.equal(calls[1].cookie,'__Host-kfm_ai_guest='+'g'.repeat(43));
 assert.equal((await h(req('jobs/'+'j'.repeat(43),undefined,{'X-KFM-Site-Actor':'b'.repeat(64)}))).status,401);
 assert.deepEqual(calls[0].body.context,question.context);
});
test('private selectors and evidence mode cannot cross the service adapter',async()=>{
 const calls=[];const h=createSitesQwenHandler({token,origin,handle:async r=>{calls.push(new URL(r.url).pathname);return status();}});
 assert.equal((await h(req('jobs',{...question,mode:'evidence'}))).status,400);
 assert.equal((await h(req('jobs',{...question,context:{...question.context,selection:{kind:'registry',featureId:'private'}}}))).status,403);
 assert.equal((await h(req('jobs',{...question,context:{...question.context,layers:['private']}}))).status,403);
 assert.ok(calls.every(x=>x.endsWith('/status')));
});
