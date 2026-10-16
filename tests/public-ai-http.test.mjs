import test from 'node:test';
import assert from 'node:assert/strict';
import {startProdServer} from 'vinext/server/prod-server';
test('built public chat route is disabled by default and rejects origin mismatch before model start',async()=>{
 const oldEnabled=process.env.KFM_HOSTED_AI,oldOrigin=process.env.KFM_HOSTED_AI_ORIGIN;
 delete process.env.KFM_HOSTED_AI;delete process.env.KFM_HOSTED_AI_ORIGIN;
 const {server,port}=await startProdServer({port:0,host:'127.0.0.1',outDir:process.cwd()+'/dist'});const origin='http://127.0.0.1:'+port;
 try{
  const status=await fetch(origin+'/api/ai/status');assert.equal(status.status,200);assert.equal((await status.json()).requiresLogin,false);
  const disabled=await fetch(origin+'/api/ai/jobs',{method:'POST',headers:{'Content-Type':'application/json',Origin:origin},body:'{}'});assert.equal(disabled.status,503);await disabled.text();
  process.env.KFM_HOSTED_AI='1';process.env.KFM_HOSTED_AI_ORIGIN='https://kansasfrontiermatrix.com';
  const held=await fetch(origin+'/api/ai/status');assert.equal(held.status,503);assert.equal((await held.json()).reasonCode,'AI_ORIGIN_HOLD');
  const page=await fetch(origin+'/');const html=await page.text();assert.match(html,/No account is needed for chat/);assert.match(html,/HOSTED AI/);
  const privateModel=await fetch(origin+'/private/kfm-embedded-smollm2-wasm-20261016/model/onnx/model_q4.onnx');assert.equal(privateModel.status,404);await privateModel.arrayBuffer();
 }finally{
  if(oldEnabled===undefined)delete process.env.KFM_HOSTED_AI;else process.env.KFM_HOSTED_AI=oldEnabled;
  if(oldOrigin===undefined)delete process.env.KFM_HOSTED_AI_ORIGIN;else process.env.KFM_HOSTED_AI_ORIGIN=oldOrigin;
  server.closeAllConnections();await new Promise(resolve=>server.close(resolve));
 }
});
