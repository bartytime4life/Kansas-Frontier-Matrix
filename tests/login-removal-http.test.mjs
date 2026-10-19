import test from 'node:test';
import assert from 'node:assert/strict';
import {startProdServer} from 'vinext/server/prod-server';

test('production app has no login routes and retired sessions cannot unlock private operations',async t=>{
 const {server,port}=await startProdServer({port:0,host:'127.0.0.1',outDir:process.cwd()+'/dist'});
 t.after(()=>new Promise(resolve=>{server.closeAllConnections();server.close(resolve);}));
 const origin='http://127.0.0.1:'+port;
 const retiredHeaders={Cookie:'__Host-kfm-owner='+'a'.repeat(43)+'; __Host-kfm_pc_session='+'b'.repeat(43),'x-role':'administrator','oai-authenticated-user-id':'203533328','oai-authenticated-user-email':'owner@example.test'};
 await t.test('login, activation, invitation and owner session endpoints are absent',async()=>{
  for(const path of ['/signin-with-chatgpt','/signout-with-chatgpt','/callback','/api/owner/sign-in','/api/owner/callback?code=retired&state=retired','/api/owner/session','/api/pc-ai/status','/data','/stewards','/source-operations','/daily-archive','/governed/water-release','/governed/weather-release','/earth-engine-context/install','/api/data-submissions','/api/acquisition','/api/acquisition/terrain']){
   const response=await fetch(origin+path,{headers:retiredHeaders,redirect:'manual'});
   assert.equal(response.status,404,path);assert.equal(response.headers.get('location'),null,path);assert.equal(response.headers.get('set-cookie'),null,path);await response.text();
  }
  for(const path of ['/api/owner/sign-out','/api/pc-ai/sign-in','/api/pc-ai/sign-out','/api/pc-ai/activate','/api/pc-ai/admin/invite','/api/pc-ai/admin/revoke','/api/pc-ai/jobs','/api/pc-ai/worker/claim','/api/source-pipeline/control?action=resume']){
   const response=await fetch(origin+path,{method:'POST',headers:{...retiredHeaders,Origin:origin,'Content-Type':'application/json'},body:'{}',redirect:'manual'});
   assert.equal(response.status,404,path);assert.equal(response.headers.get('set-cookie'),null,path);await response.text();
  }
 });
 await t.test('public pages have no login controls or links to retired destinations',async()=>{
  for(const path of ['/','/?kfm-chat=1','/about','/privacy','/observatory','/observatory/sources','/earth-engine','/acquisition']){
   const response=await fetch(origin+path,{headers:retiredHeaders,redirect:'manual'});assert.equal(response.status,200,path);assert.equal(response.headers.get('location'),null,path);
   const html=await response.text();assert.doesNotMatch(html,/steward-login-button|Administrator sign-in|Sign in with|name="(?:username|password|invitation)"|type="password"|href="[^"\s]*(?:signin-with-chatgpt|api\/owner|data(?:[?#\"]|$)|stewards|daily-archive|source-operations|governed\/(?:water|weather)-release|earth-engine-context\/install)/i,path);
  }
  const status=await fetch(origin+'/api/ai/status');assert.equal(status.status,200);assert.equal((await status.json()).requiresLogin,false);
 });
 await t.test('private reads and mutations stay closed to anonymous and retired credentials',async()=>{
  for(const headers of [{},retiredHeaders]){
   for(const path of ['/api/daily-archive','/api/governed/water-admin/status','/api/governed/weather-admin/status']){
    const response=await fetch(origin+path,{headers});assert.equal(response.status,401,path);assert.equal(response.headers.get('location'),null,path);await response.text();
   }
   const captures=await fetch(origin+'/api/source-pipeline/captures',{headers});assert.equal(captures.status,404);await captures.text();
   for(const [path,method] of [['/api/earth-engine-context/stage','PUT'],['/api/earth-engine-context/activate','POST']]){const response=await fetch(origin+path,{method,headers:{...headers,Origin:origin,'Content-Type':'application/json'},body:'{}'});assert.equal(response.status,401,path);await response.text();}
   const run=await fetch(origin+'/api/source-pipeline/run',{method:'POST',headers:{...headers,Origin:origin}});assert.equal(run.status,401);await run.text();
  }
  for(const path of ['/private/kfm-pc-ai-v1/preview/accounts-jobs.sqlite','/private/kfm-pc-ai-v1/published/accounts-jobs.sqlite']){
   const response=await fetch(origin+path,{headers:retiredHeaders});assert.equal(response.status,404,path);assert.doesNotMatch(await response.text(),/^SQLite format 3/);
  }
 });
});
