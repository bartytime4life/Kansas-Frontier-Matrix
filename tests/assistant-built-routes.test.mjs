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
  const map=await handler(new Request(origin+'/'));assert.equal(map.status,200);const mapHtml=await map.text();assert.match(mapHtml,/Chat with KFM/);assert.doesNotMatch(mapHtml,/steward-login-button|Administrator|type="password"/);
 }finally{if(previous===undefined)delete process.env.KFM_HOSTED_AI;else process.env.KFM_HOSTED_AI=previous;}
});

test('retired private pages are absent and forged staff headers grant no access',async()=>{
 const {default:handler}=await import('../dist/server/index.js');
 const origin='https://kansasfrontiermatrix.com';
 for(const path of ['/data','/stewards','/source-operations','/governed/water-release','/governed/weather-release','/daily-archive','/earth-engine-context/install','/api/data-submissions']){
  const response=await handler(new Request(origin+path,{headers:{host:'kansasfrontiermatrix.com','x-role':'admin','oai-authenticated-user-id':'203533328'}}));
  assert.equal(response.status,404,path);assert.equal(response.headers.get('location'),null,path);await response.text();
 }
 for(const path of ['/api/governed/water-admin/status','/api/governed/weather-admin/status']){
  const response=await handler(new Request(origin+path,{headers:{host:'kansasfrontiermatrix.com','x-role':'admin','oai-authenticated-user-id':'admin','oai-authenticated-user-email':'steward@example.test'}}));
  assert.equal(response.status,401,path);
 }
});
