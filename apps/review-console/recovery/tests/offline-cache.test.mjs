import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

test('offline static module bytes survive Vite Origin variation without relaxing navigation or API handling', async () => {
  const handlers = new Map();
  const matches = [];
  const cached = new Response('cached module');
  const context = {
    self: {location:{origin:'https://desk.example'}, addEventListener:(name,fn)=>handlers.set(name,fn)},
    URL, Response,
    caches: {open:async()=>({match:async(request,options)=>{
      matches.push({request,options});
      return options?.ignoreVary === true ? cached : undefined;
    }})},
    fetch:async()=>{throw Error('local server unavailable');},
  };
  vm.runInNewContext(readFileSync(new URL('../public/recovery-sw.js',import.meta.url),'utf8'),context);
  let response;
  handlers.get('fetch')({request:{url:'https://desk.example/assets/app.js',method:'GET',mode:'cors'},respondWith:p=>{response=p;}});
  assert.equal(await (await response).text(),'cached module');
  assert.equal(matches[0].options.ignoreVary,true);
  response=undefined;
  handlers.get('fetch')({request:{url:'https://desk.example/api/private',method:'GET',mode:'cors'},respondWith:p=>{response=p;}});
  assert.equal(response,undefined,'operational/API requests are not intercepted');
  assert.equal(matches.length,1);
});
