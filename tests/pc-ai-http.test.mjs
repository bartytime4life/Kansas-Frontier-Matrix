import {test} from 'node:test';
import assert from 'node:assert/strict';
import {startProdServer} from 'vinext/server/prod-server';

test('actual built routes are disabled by default and hold a mismatched origin before private storage',async()=>{
  const savedEnabled=process.env.KFM_PC_ENABLED,savedOrigin=process.env.KFM_PC_ORIGIN;
  process.env.KFM_PC_ENABLED='false';
  const {server,port}=await startProdServer({port:0,host:'127.0.0.1',outDir:process.cwd()+'/dist'});
  const origin='http://127.0.0.1:'+port;
  try{
    const status=await fetch(origin+'/api/pc-ai/status');assert.equal(status.status,200);assert.equal((await status.json()).configured,false);
    const denied=await fetch(origin+'/api/pc-ai/jobs',{method:'POST',headers:{'Content-Type':'application/json',Origin:origin},body:'{}'});assert.equal(denied.status,503);await denied.text();
    process.env.KFM_PC_ENABLED='true';process.env.KFM_PC_ORIGIN='https://kansasfrontiermatrix.com';
    const held=await fetch(origin+'/api/pc-ai/status');assert.equal(held.status,503);assert.equal((await held.json()).reasonCode,'PC_AI_ORIGIN_HOLD');
    const page=await fetch(origin+'/assistant');assert.equal(page.status,200);assert.match(await page.text(),/Ask KFM/);
    const privateRead=await fetch(origin+'/private/kfm-pc-ai-v1/published/accounts-jobs.sqlite');assert.equal(privateRead.status,404);assert.equal((await privateRead.text()).startsWith('SQLite format 3'),false);
  }finally{
    if(savedEnabled===undefined)delete process.env.KFM_PC_ENABLED;else process.env.KFM_PC_ENABLED=savedEnabled;
    if(savedOrigin===undefined)delete process.env.KFM_PC_ORIGIN;else process.env.KFM_PC_ORIGIN=savedOrigin;
    server.closeAllConnections();await new Promise(resolve=>server.close(resolve));
  }
});
