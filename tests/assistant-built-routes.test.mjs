import test from 'node:test';
import assert from 'node:assert/strict';

// Exercise the production Fetch handler without opening a local TCP listener.
test('built public AI fails closed without host configuration and public pages render',async()=>{
 const previous=process.env.KFM_HOSTED_AI;
 delete process.env.KFM_HOSTED_AI;
 try{
  const {default:handler}=await import('../dist/server/index.js');
  const origin='https://kansasfrontiermatrix.com';
  const status=await handler(new Request(origin+'/api/ai/status'));
  assert.equal(status.status,200);
  const value=await status.json();assert.equal(value.requiresLogin,false);assert.equal(value.configured,false);
  const denied=await handler(new Request(origin+'/api/ai/jobs',{method:'POST',headers:{origin,'content-type':'application/json'},body:JSON.stringify({question:'Explain a layer.',term:'layer'})}));
  assert.equal(denied.status,503);assert.equal((await denied.json()).reasonCode,'HOSTED_AI_NOT_CONFIGURED');
  for(const path of ['/about','/privacy']){
   const response=await handler(new Request(origin+path));assert.equal(response.status,200);
   const html=await response.text();assert.match(html,/Ask KFM/);assert.match(html,/About /);
  }
  const compatibility=await handler(new Request(origin+'/downloads'));assert.equal(compatibility.status,307);assert.equal(compatibility.headers.get('location'),origin+'/?layers=sources');
  const map=await handler(new Request(origin+'/'));assert.equal(map.status,200);const mapHtml=await map.text();assert.match(mapHtml,/Chat with KFM/);assert.match(mapHtml,/steward-login-button[^>]*>[\s\S]*?Administrator/);
 }finally{if(previous===undefined)delete process.env.KFM_HOSTED_AI;else process.env.KFM_HOSTED_AI=previous;}
});

test('unconfigured private workspaces explain the hold and forged staff headers remain denied',async()=>{
 const {default:handler}=await import('../dist/server/index.js');
 const origin='https://kansasfrontiermatrix.com';
 for(const path of ['/data','/stewards']){
  const response=await handler(new Request(origin+path,{headers:{host:'kansasfrontiermatrix.com'}}));
  assert.equal(response.status,200,path);assert.equal(response.headers.get('location'),null,path);
  const html=await response.text();assert.match(html,/Private workspace unavailable on this host/);
  assert.match(html,/Administrator sign-in on the map does not grant access/);
  assert.match(html,/https:\/\/kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site/);
 }
 const local=await handler(new Request('http://127.0.0.1:4173/stewards',{headers:{host:'127.0.0.1:4173'}}));
 assert.equal(local.status,200);assert.match(await local.text(),/Sign in on the private Site/);
 for(const path of ['/api/data-submissions','/api/governed/water-admin/status','/api/governed/weather-admin/status']){
  const response=await handler(new Request(origin+path,{headers:{host:'kansasfrontiermatrix.com','x-role':'admin','oai-authenticated-user-id':'admin','oai-authenticated-user-email':'steward@example.test'}}));
  assert.equal(response.status,401,path);
 }
});
