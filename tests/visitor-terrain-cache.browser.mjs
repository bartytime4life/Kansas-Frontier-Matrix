// Real IndexedDB and production readers in a disposable browser; public synthetic fixtures only.
import assert from 'node:assert/strict';
import test from 'node:test';
import {createServer} from 'node:http';
import {readFile,mkdtemp,rm} from 'node:fs/promises';
import {spawn} from 'node:child_process';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import ts from 'typescript';
import {groundFixture} from './kansas-ground-fixtures.mjs';
import {kansasFixture} from './kansas-lidar-fixtures.mjs';
const chrome = process.env.KFM_TEST_CHROME ?? "google-chrome";
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
async function devtools(t) {
  const profile = await mkdtemp(join(tmpdir(), "kfm-visitor-cache-"));
  const child = spawn(chrome, ["--headless=new", "--remote-debugging-pipe", `--user-data-dir=${profile}`, "--no-first-run",
    "--no-default-browser-check", "--disable-background-networking", "--disable-dev-shm-usage", "--enable-unsafe-swiftshader",
    "--use-angle=swiftshader", "--window-size=1440,900", "about:blank"], { stdio: ["ignore", "ignore", "pipe", "pipe", "pipe"] });
  let stderr = "", sequence = 0, buffer = "", closed = false;
  const pending = new Map(), listeners = new Set();
  child.stderr.on("data", chunk => { stderr = (stderr + chunk).slice(-12000); });
  const failPending = error => { closed = true; for (const entry of pending.values()) entry.reject(error); pending.clear(); };
  child.on("error", failPending);
  child.on("exit", code => failPending(new Error(`Chrome exited ${code}: ${stderr}`)));
  child.stdio[4].on("data", chunk => {
    buffer += chunk.toString();
    let index;
    while ((index = buffer.indexOf("\0")) >= 0) {
      const message = JSON.parse(buffer.slice(0, index)); buffer = buffer.slice(index + 1);
      if (message.id) { const item = pending.get(message.id); if (!item) continue; pending.delete(message.id); if (message.error) item.reject(new Error(JSON.stringify(message.error))); else item.resolve(message.result); }
      else for (const listener of listeners) listener(message);
    }
  });
  const call = (method, params = {}, sessionId) => new Promise((resolve, reject) => {
    if (closed) { reject(new Error(`Chrome unavailable: ${stderr}`)); return; }
    const id = ++sequence;
    const timer = setTimeout(() => { pending.delete(id); reject(new Error(`CDP timeout: ${method}; ${stderr}`)); }, 60000);
    pending.set(id, { resolve: value => { clearTimeout(timer); resolve(value); }, reject: error => { clearTimeout(timer); reject(error); } });
    child.stdio[3].write(JSON.stringify({ id, method, params, ...(sessionId ? { sessionId } : {}) }) + "\0");
  });
  t.after(async () => {
    try { await call("Browser.close"); } catch { child.kill(); }
    if (child.exitCode === null) await Promise.race([new Promise(resolve => child.once("exit", resolve)), pause(2000)]);
    if (child.exitCode === null) child.kill("SIGKILL");
    await rm(profile, { recursive: true, force: true, maxRetries: 3, retryDelay: 100 });
  });
  const { targetId } = await call("Target.createTarget", { url: "about:blank" });
  const { sessionId } = await call("Target.attachToTarget", { targetId, flatten: true });
  const pageErrors = [];
  listeners.add(message => { if (message.sessionId === sessionId && message.method === "Runtime.exceptionThrown") pageErrors.push(JSON.stringify(message.params.exceptionDetails).slice(0, 400)); });
  await call("Runtime.enable", {}, sessionId);
  await call("Emulation.setDeviceMetricsOverride", { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false }, sessionId);
  const evaluate = async expression => {
    const result = await call("Runtime.evaluate", { expression, awaitPromise: true, returnByValue: true }, sessionId);
    if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails).slice(0, 600));
    return result.result.value;
  };
  const navigate = url => call("Page.navigate", { url }, sessionId);
  return { evaluate, navigate, pageErrors, call };
}

async function harness(t) {
  const names=['visitor-terrain-cache','kansas-ground','kansas-ground-client','native-lidar','native-lidar-client','kansas-lidar-view','kansas-lidar-client'];
  const modules=new Map(await Promise.all(names.map(async name=>['/'+name,ts.transpileModule(await readFile('app/'+name+'.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText])));
  const ground=groundFixture(),native=kansasFixture(['surface']);
  const fresh=()=>({state:'fresh',at:new Date().toISOString()});ground.receipt.cache=fresh();native.receipt.cache=fresh();native.grid.cache=fresh();
  // Query is internally canonicalized; fixtures already bind its key.
  let requests=0,nativeRequests=0;
  const server=createServer((req,res)=>{const path=new URL(req.url,'http://local').pathname;
    if(modules.has(path)){res.writeHead(200,{'content-type':'text/javascript'});res.end(modules.get(path));return;}
    if(path==='/fixture'){res.writeHead(200,{'content-type':'application/json'});res.end(JSON.stringify({ground,native}));return;}
    if(path==='/api/lidar/view'||path==='/api/lidar/view/'+native.key+'/grid'){nativeRequests++;res.writeHead(200,{'content-type':'application/json'});res.end(JSON.stringify(path.endsWith('/grid')?native.grid:native.receipt));return;}
    if(path==='/api/terrain/ground'){requests++;res.writeHead(200,{'content-type':'application/json'});res.end(JSON.stringify(ground.receipt));return;}
    res.writeHead(200,{'content-type':'text/html'});res.end(`<script type="module">import * as cache from '/visitor-terrain-cache';import * as client from '/kansas-ground-client';window.kfm={cache,client,fixture:await(await fetch('/fixture')).json()};</script>`);
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));t.after(()=>server.close());
  const p=await devtools(t),origin='http://127.0.0.1:'+server.address().port;await p.navigate(origin);
  const deadline=Date.now()+10000;while(!await p.evaluate('!!window.kfm')){if(Date.now()>deadline)throw Error('cache harness startup');await pause(25);}
  return {p,origin,requests:()=>requests,nativeRequests:()=>nativeRequests};
}
test('real IndexedDB temporary copies preserve source values, avoid a repeated Ground request and obey explicit refresh',async t=>{
 const {p,requests}=await harness(t);
 const values=await p.evaluate(`(async()=>{const {cache,client,fixture:{ground:f}}=kfm;await cache.clearVisitorTerrainCache();const first=await client.readKansasGround(f.query,new AbortController().signal);for(let n=0;n<30&&!(await cache.visitorTerrainCacheStatus()).usedBytes;n++)await new Promise(r=>setTimeout(r,20));const second=await client.readKansasGround(f.query,new AbortController().signal);return {same:JSON.stringify(first)===JSON.stringify(second),count:second.grid.ground.length,status:await cache.visitorTerrainCacheStatus()};})()`);
 assert.equal(values.same,true);assert.equal(values.count,9216);assert.equal(requests(),1);assert.ok(values.status.usedBytes>0&&values.status.usedBytes<=values.status.limitBytes);
 await p.evaluate(`kfm.client.readKansasGround(kfm.fixture.ground.query,new AbortController().signal,undefined,{bypassCache:true})`);assert.equal(requests(),2);
 // A new module instance/page still restores only through the production schema parser.
 await p.navigate('about:blank');
});
test('browser cache enforces aggregate bytes/count, expiry, aborted writes, clear-generation and off across independent modules',async t=>{
 const {p}=await harness(t);
 const result=await p.evaluate(`(async()=>{const c=kfm.cache,signal=new AbortController().signal,key=n=>'ground:'+n.toString(16).padStart(64,'0');await c.clearVisitorTerrainCache();
 const lease=await c.openVisitorTerrainEntry(key(100),signal);await c.clearVisitorTerrainCache();await lease.save({late:true},Date.now()+60000);const cleared=(await c.openVisitorTerrainEntry(key(100),signal)).value;
 const other=await import('/visitor-terrain-cache?second');const cross=await other.openVisitorTerrainEntry(key(101),signal);await c.clearVisitorTerrainCache();await cross.save({late:true},Date.now()+60000);const crossCleared=(await c.openVisitorTerrainEntry(key(101),signal)).value;
 for(let n=1;n<=30;n++){const e=await c.openVisitorTerrainEntry(key(n),signal);await e.save({source:n,data:'x'.repeat(600000)},Date.now()+60000);}
 const status=await c.visitorTerrainCacheStatus(),oldest=(await c.openVisitorTerrainEntry(key(1),signal)).value,newest=(await c.openVisitorTerrainEntry(key(30),signal)).value;
 const aborted=new AbortController(),a=await c.openVisitorTerrainEntry(key(102),aborted.signal);aborted.abort();await a.save({aborted:true},Date.now()+60000);
 const e=await c.openVisitorTerrainEntry(key(103),signal);await e.save({expired:true},Date.now()-1);
 const pending=await other.openVisitorTerrainEntry(key(104),signal);await c.setVisitorTerrainCacheEnabled(false);await pending.save({late:true},Date.now()+60000);const off=await c.visitorTerrainCacheStatus();await c.setVisitorTerrainCacheEnabled(true);
 return {cleared,crossCleared,status,oldest,newest:newest?.source,aborted:(await c.openVisitorTerrainEntry(key(102),signal)).value,expired:(await c.openVisitorTerrainEntry(key(103),signal)).value,off,late:(await other.openVisitorTerrainEntry(key(104),signal)).value};})()`);
 assert.equal(result.cleared,null);assert.equal(result.crossCleared,null);assert.ok(result.status.usedBytes>0&&result.status.usedBytes<=result.status.limitBytes);assert.equal(result.oldest,null);assert.equal(result.newest,30);assert.equal(result.aborted,null);assert.equal(result.expired,null);assert.equal(result.off.enabled,false);assert.equal(result.off.usedBytes,0);assert.equal(result.late,null);
});
test('browser cache rejects a poisoned query-bound grid and denied storage falls back to normal delivery',async t=>{
 const {p,requests}=await harness(t);
 const result=await p.evaluate(`(async()=>{const {cache:c,client,fixture:{ground:f}}=kfm;const signal=new AbortController().signal;await c.clearVisitorTerrainCache();const e=await c.openVisitorTerrainEntry('ground:'+f.requestKey,signal);await e.save({...f.receipt,requestKey:'f'.repeat(64)},Date.now()+60000);const valid=await client.readKansasGround(f.query,signal);await c.clearVisitorTerrainCache();Object.defineProperty(window,'indexedDB',{configurable:true,get(){throw Error('storage denied');}});const c2=await import('/visitor-terrain-cache?denied');let status;try{status=await c2.visitorTerrainCacheStatus();}catch(error){return {error:String(error)};}let clearDenied=false;try{await c2.clearVisitorTerrainCache();}catch{clearDenied=true;}return {valid:valid.requestKey===f.requestKey,status,clearDenied};})()`);
 assert.equal(result.error,undefined);assert.equal(result.valid,true);assert.equal(requests(),1);assert.equal(result.status.available,false);assert.equal(result.clearDenied,true);
});

test('native cache restores one complete receipt/grid pair with exact masks and bypasses the point route',async t=>{
 const {p,nativeRequests}=await harness(t);
 const result=await p.evaluate(`(async()=>{const c=kfm.cache,{readKansasLidarView}=await import('/kansas-lidar-client'),f=kfm.fixture.native,s=new AbortController().signal;await c.clearVisitorTerrainCache();const first=await readKansasLidarView(f.query,s);for(let n=0;n<30&&!(await c.visitorTerrainCacheStatus()).usedBytes;n++)await new Promise(r=>setTimeout(r,20));const second=await readKansasLidarView(f.query,s);return {same:JSON.stringify(first)===JSON.stringify(second),points:second.points,canopy:second.grid.canopy,ground:second.grid.ground};})()`);
 assert.equal(result.same,true);assert.equal(result.points,null);assert.deepEqual(result.canopy,[12,null,null,2]);assert.deepEqual(result.ground,[300,null,302,303]);assert.equal(nativeRequests(),2,'only initial receipt and grid; the revisit makes no requests');
});
test('two real tabs share clear/off generation and deliver preference-change notifications',async t=>{
 const {p,origin}=await harness(t),{targetId}=await p.call('Target.createTarget',{url:origin}),{sessionId}=await p.call('Target.attachToTarget',{targetId,flatten:true});
 const second=async expression=>{const r=await p.call('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true},sessionId);if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;};
 const deadline=Date.now()+10000;while(!await second('!!window.kfm')){if(Date.now()>deadline)throw Error('second tab did not load');await pause(25);}
 await second(`(async()=>{window.events=0;window.addEventListener(kfm.cache.TERRAIN_CACHE_EVENT,()=>events++);window.late=await kfm.cache.openVisitorTerrainEntry('ground:'+'c'.repeat(64),new AbortController().signal);})()`);
 await p.evaluate('kfm.cache.clearVisitorTerrainCache()');
 assert.equal(await second(`(async()=>{await late.save({old:true},Date.now()+60000);return(await kfm.cache.openVisitorTerrainEntry('ground:'+'c'.repeat(64),new AbortController().signal)).value;})()`),null);
 await p.evaluate('kfm.cache.setVisitorTerrainCacheEnabled(false)');
 const until=Date.now()+5000;while(!await second('events>0')){if(Date.now()>until)throw Error('storage notification missing');await pause(25);}
 assert.equal((await second('kfm.cache.visitorTerrainCacheStatus()')).enabled,false);
 await p.evaluate('kfm.cache.setVisitorTerrainCacheEnabled(true)');
 const enabledUntil=Date.now()+5000;while(!(await second('kfm.cache.visitorTerrainCacheStatus()')).enabled){if(Date.now()>enabledUntil)throw Error('enable preference not shared');await pause(25);}
 assert.ok(await second('events>=2'));
});
