import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
const exp={};vm.runInNewContext(ts.transpileModule(await readFile('worker/staging-assistant.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText,{exports:exp,Request,Response,URL,TextEncoder,TextDecoder,Uint8Array,crypto,AbortSignal,Date,setTimeout,clearTimeout,fetch});
const origin='https://kfm-public-staging-20261012.blackbart-55.chatgpt.site';
const identity={'oai-authenticated-user-id':'synthetic-owner','oai-authenticated-user-email':'synthetic@example.test'};
const req=(path,body,headers=identity)=>new Request(origin+path,{method:body===undefined?'GET':'POST',headers:{...headers,...(body===undefined?{}:{origin,'content-type':'application/json'})},body:body===undefined?undefined:JSON.stringify(body)});
const catalog=async()=>Response.json({envelope:{outcome:'ABSTAIN',reason_code:'NO_APPROVED_PUBLIC_RELEASE'}});
const question={mode:'explore',question:'Explain missing source values',term:'missing',context:{version:1,frame:2026,view:'2D',surface:'map',layers:[],selection:null}};
const setup={KFM_STAGING_QWEN_ORIGIN:'https://q9r9beo47t.preview.c38.airoapp.ai',KFM_STAGING_QWEN_TOKEN:'t'.repeat(43)};
test('Sites account is real optional platform identity; no Node role or password endpoint',async()=>{
 const h=exp.createStagingAssistant({settings:{},catalog});
 const a=await(await h(req('/api/staging/account',undefined,{}))).json();assert.equal(a.account,null);assert.match(a.signIn,/^\/signin-with-chatgpt\?/);
 const b=await(await h(req('/api/staging/account'))).json();assert.equal(b.account,identity['oai-authenticated-user-email']);assert.equal(b.role,null);
 assert.equal((await h(req('/api/ai/sign-in',{username:'a',password:'b'}))).status,404);
});
test('anonymous, forged role, cross-site and unsupported methods never reach Qwen',async()=>{
 let calls=0;const h=exp.createStagingAssistant({settings:setup,catalog,fetcher:async()=>{calls++;throw Error();}});
 assert.equal((await h(req('/api/ai/jobs',question,{'x-role':'administrator'}))).status,401);
 const cross=req('/api/ai/jobs',question);cross.headers.set('origin','https://other.test');assert.equal((await h(cross)).status,403);
 assert.equal((await h(new Request(origin+'/api/ai/status',{method:'DELETE',headers:identity}))).status,404);
 assert.equal(calls,0);
});
test('default-off Qwen status is truthful and does not call the private preview',async()=>{
 let calls=0;const h=exp.createStagingAssistant({settings:{},catalog,fetcher:async()=>{calls++;throw Error();}});
 const s=await(await h(req('/api/ai/status'))).json();assert.equal(s.ready,false);assert.equal(s.reasonCode,'QWEN_CONNECTION_NOT_CONFIGURED');assert.equal(s.evidenceSearchAvailable,true);
 assert.equal((await h(req('/api/ai/jobs',question))).status,503);assert.equal(calls,0);
});
test('Evidence checks re-read this Site catalog and never use remote data or infer authority',async()=>{
 let reads=0;const h=exp.createStagingAssistant({settings:{},catalog:async()=>{reads++;return catalog();},fetcher:async()=>{throw Error('must not call');}});
 const create=await(await h(req('/api/ai/jobs',{...question,mode:'evidence'}))).json();assert.match(create.id,/^evidence_[a-f0-9]{32}$/);
 for(let i=0;i<2;i++){const r=await(await h(req('/api/ai/jobs/'+create.id))).json();assert.equal(r.result.reasonCode,'NO_RELEASED_EVIDENCE');assert.equal(r.result.answer,null);assert.deepEqual(r.result.citations,[]);}
 assert.equal(reads,2);
});
test('Qwen adapter projects bounded display context and keeps identities and secrets server-only',async()=>{
 const calls=[];const now=Date.now();const h=exp.createStagingAssistant({settings:setup,catalog,fetcher:async(url,options)=>{calls.push({url,options});return Response.json({id:'j'.repeat(43),deadline:now+90000});}});
 assert.equal((await h(req('/api/ai/jobs',{...question,context:{...question.context,selection:{kind:'registry',featureId:'held'}}}))).status,403);
 const r=await(await h(req('/api/ai/jobs',{...question,place:'private location',context:{...question.context,arbitrary:'private note'}}))).json();assert.equal(r.id,'j'.repeat(43));
 const c=calls[0],body=JSON.parse(c.options.body);assert.equal(body.place,'');assert.equal(body.context.arbitrary,undefined);assert.equal(c.options.redirect,'error');assert.match(c.options.headers['X-KFM-Site-Actor'],/^[a-f0-9]{64}$/);assert.ok(!JSON.stringify(body).includes(identity['oai-authenticated-user-email']));
 assert.ok(!JSON.stringify(r).includes(setup.KFM_STAGING_QWEN_TOKEN));
});
test('mismatched models, unsupported factual answers, bad URLs and upstream errors fail closed',async()=>{
 for(const settings of [{...setup,KFM_STAGING_QWEN_ORIGIN:'https://evil.test'},setup]){
  const h=exp.createStagingAssistant({settings,catalog,fetcher:async()=>Response.json({provider:'smollm2',ready:true,online:true,model:'old'})});
  assert.equal((await(await h(req('/api/ai/status'))).json()).ready,false);
 }
 const h=exp.createStagingAssistant({settings:setup,catalog,fetcher:async()=>Response.json({id:'j'.repeat(43),state:'completed',deadline:Date.now()+1000,result:{outcome:'ANSWER',reasonCode:'UNVERIFIED_AI_DISCUSSION',answer:'unsupported'}})});
 assert.equal((await h(req('/api/ai/jobs/'+'j'.repeat(43)))).status,503);
});

test('embedded workspace uses platform account navigation and keeps Find separate from unavailable Qwen',async()=>{
 const {componentHarness,findNode,settle}=await import('./component-harness.mjs');
 const calls=[];
 const h=await componentHarness('app/assistant/workspace.tsx',{'./workspace.module.css':{default:new Proxy({},{get:(_,key)=>key})},'../assistant-surfaces.mjs':{assistantSurface:()=>null},'../assistant-investigation':{}},{crypto,queueMicrotask,setInterval:()=>0,clearInterval:()=>{},fetch:async path=>{calls.push(path);return Response.json(path==='/api/staging/account'?{account:null,signIn:'/signin-with-chatgpt?return_to=%2F',signOut:'/signout-with-chatgpt'}:{configured:true,online:false,ready:false,requiresLogin:false,evidenceSearchAvailable:true,reasonCode:'QWEN_CONNECTION_NOT_CONFIGURED'});}});
 const props={active:true,accountRequest:0,onAccount:()=>{},discovery:{query:'',items:[],status:'',busy:false,onQuery:()=>{},onChoose:()=>{}}};
 let tree=h.render(h.exports.default,props);h.commit();await settle();tree=h.render(h.exports.default,props);h.commit();
 const ask=findNode(tree,n=>n.type==='button'&&n.props.children==='Ask');ask.props.onClick();tree=h.render(h.exports.default,props);
 assert.match(JSON.stringify(tree),/GoDaddy Node 22 is not connected/);
 const form=findNode(tree,n=>n.type==='form');const send=findNode(form,n=>n.type==='button'&&n.props.children==='Send');assert.equal(send.props.disabled,true);
 tree=h.render(h.exports.default,{...props,accountRequest:1});h.commit();await settle();tree=h.render(h.exports.default,{...props,accountRequest:1});h.commit();
 const signIn=findNode(tree,n=>n.type==='a'&&n.props.children==='Sign in with ChatGPT');assert.match(signIn.props.href,/^\/signin-with-chatgpt/);assert.equal(signIn.props.target,'_top');
 assert.ok(!calls.some(x=>x.startsWith('/api/pc-ai/')));assert.equal(findNode(tree,n=>n.type==='input'&&n.props.type==='password'),undefined);
 h.dispose();
});
