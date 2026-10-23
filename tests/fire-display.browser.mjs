// Real MapLibre/Canvas component acceptance with explicitly synthetic data.
// No provider requests or deployed fixture endpoint. The original Explorer
// Evidence Drawer is checked separately through the hydrated application.
import assert from 'node:assert/strict';
import test from 'node:test';
import { spawn } from 'node:child_process';
import { mkdtemp, rm, readFile, mkdir, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { build } from 'esbuild';
import { isolateBrowserNetwork } from './browser-network.mjs';
const origin=new URL(process.env.KFM_NODE_TEST_ORIGIN??'http://127.0.0.1:5182');
assert.equal(origin.protocol,'http:');
assert.ok(['127.0.0.1','localhost','[::1]'].includes(origin.hostname));
assert.equal(origin.pathname,'/'); assert.equal(origin.search+origin.hash+origin.username+origin.password,'');
const chrome=process.env.KFM_TEST_CHROME??'google-chrome';
const pause=ms=>new Promise(resolve=>setTimeout(resolve,ms));
async function browser(t, layout) {
  const profile = await mkdtemp(join(tmpdir(), 'kfm-county-browser-'));
  const child = spawn(chrome, [
    '--headless=new', '--remote-debugging-pipe', `--user-data-dir=${profile}`,
    `--window-size=${Math.max(800,layout.width)},${Math.max(600,layout.height+100)}`,
    '--no-first-run', '--no-default-browser-check', '--disable-background-networking',
    ...(process.getuid?.() === 0 ? ['--no-sandbox'] : []), '--disable-dev-shm-usage', '--enable-unsafe-swiftshader', '--use-angle=swiftshader', 'about:blank',
  ], { stdio: ['ignore', 'ignore', 'pipe', 'pipe', 'pipe'] });
  let stderr = '', sequence = 0, buffer = '', closed = false;
  const pending = new Map(), listeners = new Set(), checks = [];
  child.stderr.on('data', chunk => { stderr = (stderr + chunk).slice(-12000); });
  const failPending = error => { closed = true; for (const entry of pending.values()) entry.reject(error); pending.clear(); };
  child.on('error', failPending);
  child.on('exit', code => failPending(new Error(`Chrome exited ${code}: ${stderr}`)));
  child.stdio[4].on('data', chunk => {
    buffer += chunk.toString();
    let index;
    while ((index = buffer.indexOf('\0')) >= 0) {
      const message = JSON.parse(buffer.slice(0, index)); buffer = buffer.slice(index + 1);
      if (message.id) {
        const item = pending.get(message.id); if (!item) continue;
        pending.delete(message.id);
        if (message.error) item.reject(new Error(JSON.stringify(message.error)));
        else item.resolve(message.result);
      } else for (const listener of listeners) listener(message);
    }
  });
  const call = (method, params = {}, sessionId) => new Promise((resolve, reject) => {
    if (closed) { reject(new Error(`Chrome unavailable: ${stderr}`)); return; }
    const id = ++sequence;
    const timer = setTimeout(() => { pending.delete(id); reject(new Error(`CDP timeout: ${method}; ${stderr}`)); }, 20000);
    pending.set(id, { resolve: value => { clearTimeout(timer); resolve(value); }, reject: error => { clearTimeout(timer); reject(error); } });
    child.stdio[3].write(JSON.stringify({ id, method, params, ...(sessionId ? { sessionId } : {}) }) + '\0');
  });
  t.after(async () => {
    try { for (const check of checks) await check(); } finally {
      try { await call('Browser.close'); } catch { child.kill(); }
      if (child.exitCode === null) await Promise.race([new Promise(resolve => child.once('exit', resolve)), pause(2000)]);
      if (child.exitCode === null) child.kill('SIGKILL');
      await rm(profile, { recursive: true, force: true, maxRetries: 3, retryDelay: 100 });
    }
  });
  t.diagnostic(JSON.stringify(await call('Browser.getVersion')));
  return { call, listeners, checks };
}

const fixture=await build({entryPoints:['tests/fire-display.fixture.mjs'],bundle:true,write:false,format:'esm',platform:'browser',target:'es2022'});
const baseline=process.env.KFM_FIRE_BASELINE_FILE ? await build({entryPoints:['tests/fire-display.fixture.mjs'],bundle:true,write:false,format:'esm',platform:'browser',target:'es2022',plugins:[{name:'pinned-fire-baseline',setup(build){build.onLoad({filter:/app\/fire-detection-style\.ts$/},async ()=>({contents:await readFile(process.env.KFM_FIRE_BASELINE_FILE,'utf8'),loader:'ts',resolveDir:join(process.cwd(),'app')}));}}]}) : null;
const html=`<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Synthetic fire renderer acceptance</title><style>body{margin:0;background:#162d35;color:#fff;font:14px system-ui}header{padding:10px}#map{position:absolute;inset:58px 0 110px}#inspection{position:absolute;bottom:0;height:90px;overflow:auto;max-width:100%;font:12px monospace}canvas{position:absolute}</style><header>SYNTHETIC RENDERER TEST · illustrative flames · dashed outline = satellite pixel, not perimeter</header><div id="map"></div><output id="inspection">Click a synthetic source record</output><script type="module" src="/__fire-acceptance/fixture.mjs"></script></html>`;
for(const layout of [{width:1366,height:900,touch:false},{width:390,height:844,touch:true}]) {
  test(`fire Canvas/WebGL visual matrix ${layout.width}x${layout.height}`,{timeout:180000},async t=>{
    const b=await browser(t,layout);
    const {targetId}=await b.call('Target.createTarget',{url:'about:blank'});
    const {sessionId}=await b.call('Target.attachToTarget',{targetId,flatten:true});
    const call=(method,params={})=>b.call(method,params,sessionId);
    const errors=[]; let fullApp=false; const feedResponses=new Map();
    b.listeners.add(message=>{
      if(message.sessionId!==sessionId||message.method!=='Fetch.requestPaused')return;
      const {requestId,request}=message.params,url=new URL(request.url);
      let apiBody=null;
      if(fullApp && url.pathname.startsWith('/api/')){
        const feed=url.searchParams.get('feed');
        if(url.pathname==='/api/live-context' && ['nasa-gibs-fire-points','nifc-fire-reports'].includes(feed)){
          const day=url.searchParams.get('day')??new Date().toISOString().slice(0,10);
          const properties={featureId:'fixture-'+feed,name:'SYNTHETIC '+feed,confidence:'high',scanKm:0.5,trackKm:0.4,dayNight:'Day',acquiredAt:day+'T12:00:00Z',incidentType:'Incident complex',reportState:'Synthetic browser fixture; current activity not established'};
          const data={type:'FeatureCollection',features:[{type:'Feature',id:properties.featureId,geometry:{type:'Point',coordinates:[-98.4,38.5]},properties}]};
          apiBody=JSON.stringify({feed,state:'ready',retrievedAt:new Date().toISOString(),upstreamUpdatedAt:null,sourceDay:day,featureCount:1,data,source:'https://example.invalid/synthetic-test',limitation:'SYNTHETIC BROWSER FIXTURE',truncated:false});
          feedResponses.set(feed,(feedResponses.get(feed)??0)+1);
        } else if(url.pathname!=='/api/build')apiBody=JSON.stringify({error:'Unrelated provider unavailable in isolated fire test'});
      }
      const body=apiBody??(url.pathname==='/__fire-acceptance/'?(url.searchParams.has('baseline')?html.replace('/fixture.mjs','/baseline.mjs'):html):url.pathname==='/__fire-acceptance/fixture.mjs'?fixture.outputFiles[0].text:url.pathname==='/__fire-acceptance/baseline.mjs'?baseline?.outputFiles[0].text??null:null);
      const op=body!==null?call('Fetch.fulfillRequest',{requestId,responseCode:200,responseHeaders:[{name:'Content-Type',value:apiBody?'application/json':url.pathname.endsWith('.mjs')?'text/javascript':'text/html'}],body:Buffer.from(body).toString('base64')}):call('Fetch.continueRequest',{requestId});
      void op.catch(error=>errors.push(String(error)));
    });
    await call('Page.enable');await call('Runtime.enable');await call('Network.enable');
    await call('Emulation.setDeviceMetricsOverride',{width:layout.width,height:layout.height,deviceScaleFactor:1,mobile:layout.touch});
    await call('Emulation.setTouchEmulationEnabled',{enabled:layout.touch});
    await call('Network.setBlockedURLs',{urlPatterns:[{urlPattern:`${origin.origin}/*`,block:false},{urlPattern:'*://*:*/*',block:true}]});
    await call('Fetch.enable',{patterns:[{urlPattern:`${origin.origin}/__fire-acceptance/*`}]});
    const evaluate=async expression=>{
      const result=await call('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true});
      if(result.exceptionDetails)throw new Error(JSON.stringify(result.exceptionDetails));
      return result.result.value;
    };
    const ready=async()=>{
      const end=Date.now()+30000;
      while(Date.now()<end){if(await evaluate(`document.body?.dataset.ready==='true'`))return;await pause(50);}
      throw new Error('Renderer fixture did not initialize');
    };
    const dir=process.env.KFM_FIRE_SCREENSHOTS;
    const capture=async name=>{if(!dir)return;await mkdir(dir,{recursive:true});const shot=await call('Page.captureScreenshot',{format:'png'});await writeFile(join(dir,`${layout.width}-${name}.png`),Buffer.from(shot.data,'base64'));};
    if(baseline){
      await call('Page.navigate',{url:new URL('/__fire-acceptance/?baseline=1',origin).href});await ready();
      for(const zoom of [8,12,14]){await evaluate(`fireFixture.view({zoom:${zoom}})`);await capture(`before-z${zoom}`);}
    }
    await call('Page.navigate',{url:new URL('/__fire-acceptance/',origin).href});await ready();
    for(const zoom of [4,8,10,12,14,17,20]){
      await evaluate(`fireFixture.view({zoom:${zoom}})`);
      const state=await evaluate('fireFixture.state()');assert.deepEqual(state.errors,[]);assert.equal(state.images.length,3);
      assert.equal(state.layers['external-nasa-gibs-fire-points-flame'].opacity,1);
      await capture(`z${zoom}`);
    }
    for(const view of [{zoom:12,pitch:60,terrain:true},{zoom:12,pitch:60,globe:true},{zoom:5,globe:true},{zoom:14,light:true}]){
      await evaluate(`fireFixture.view(${JSON.stringify(view)})`);assert.deepEqual(await evaluate('fireFixture.errors'),[]);await capture(`view-${view.zoom}-${view.terrain?'terrain':view.globe?'globe':'light'}`);
    }
    await evaluate('fireFixture.view({zoom:12})');
    for(const id of ['fixture-0','fixture-report']){
      const point=await evaluate(`fireFixture.point(${JSON.stringify(id)})`);
      await call('Input.dispatchMouseEvent',{type:'mousePressed',x:point.x,y:point.y-12,button:'left',clickCount:1});
      await call('Input.dispatchMouseEvent',{type:'mouseReleased',x:point.x,y:point.y-12,button:'left',clickCount:1});
      const record=JSON.parse(await evaluate(`document.querySelector('#inspection').textContent`));
      t.diagnostic(JSON.stringify({requested:id,point,selected:record.id}));
      assert.equal(record.id,id);assert.equal(record.source,id==='fixture-report'?'external-nifc-fire-reports':'external-nasa-gibs-fire-points');
    }
    await evaluate('fireFixture.motion(true)');
    const moving=await evaluate('fireFixture.currentFireFrame()');const animatedBefore=await call('Page.captureScreenshot',{format:'png'});await pause(180);const animatedAfter=await call('Page.captureScreenshot',{format:'png'});assert.notEqual(animatedBefore.data,animatedAfter.data,'animation changes actual rendered pixels');
    assert.notEqual(await evaluate('fireFixture.currentFireFrame()'),moving,'visible motion advances the shared cached image frames');
    await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
    await pause(80);assert.equal(await evaluate('fireFixture.currentFireFrame()'),3,'system reduced motion settles on a complete still flame');
    await capture('reduced-motion');
    await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'no-preference'}]});
    await evaluate('fireFixture.motion(false)');
    await evaluate('fireFixture.amount(0)');assert.equal((await evaluate('fireFixture.state()')).layers['external-nasa-gibs-fire-points-flame'].opacity,0);await capture('opacity-zero');
    await evaluate('fireFixture.amount(0.4)');assert.equal((await evaluate('fireFixture.state()')).layers['external-nifc-fire-reports-flame'].opacity,0.4);
    await evaluate('fireFixture.visible(false)');for(const layer of Object.values((await evaluate('fireFixture.state()')).layers))assert.equal(layer.visibility,'none');
    await call('Page.navigate',{url:new URL('/__fire-acceptance/?fallback=1',origin).href});await ready();
    const fallback=await evaluate('fireFixture.state()');assert.deepEqual(fallback.errors,[]);assert.equal(fallback.images.length,0);
    for(const id of ['external-nasa-gibs-fire-points-circle','external-nifc-fire-reports-point'])assert.equal(fallback.layers[id].opacity,1);
    await capture('image-fallback');assert.deepEqual(errors,[]);
    // Full hydrated Explorer: actual map click, selection routing and Evidence
    // Drawer, using loopback-only synthetic provider responses.
    fullApp=true; await isolateBrowserNetwork(call,origin);
    const waitFor=async(expression,label)=>{const end=Date.now()+30000;while(Date.now()<end){if(await evaluate(expression))return;await pause(100);}await capture('failure');throw new Error('Timed out: '+label+'; '+await evaluate('document.body.innerText.slice(-2500)')); };
    await call('Page.addScriptToEvaluateOnNewDocument',{source:`(() => {
      if(!new URLSearchParams(location.search).has('testNoFireCanvas'))return;
      for(const type of [window.OffscreenCanvas,window.HTMLCanvasElement])if(type){
        const original=type.prototype.getContext;
        type.prototype.getContext=function(kind,...args){return kind==='2d'?null:original.call(this,kind,...args);};
      }
    })();`});
    for(const fallbackMode of [false,true])for(const feed of ['nasa-gibs-fire-points','nifc-fire-reports']){
      const prior=feedResponses.get(feed)??0;
      await call('Page.navigate',{url:new URL(`/?c=-98.4,38.5&z=12&l=&ctx=${feed}&motion=off${fallbackMode?'&testNoFireCanvas=1':''}`,origin).href});
      await waitFor(`!!history.state?.kfmExplorerView && !!document.querySelector('#map-canvas canvas') && !document.querySelector('.explorer-guide')`,'Explorer map hydration');
      const end=Date.now()+30000;while((feedResponses.get(feed)??0)<=prior && Date.now()<end)await pause(100);
      assert.ok((feedResponses.get(feed)??0)>prior,'synthetic fire response delivered');
      await evaluate('new Promise(resolve=>{let frames=0;const next=()=>++frames>=30?resolve():requestAnimationFrame(next);requestAnimationFrame(next);})');
      const point=await evaluate(`(()=>{const r=document.querySelector('#map-canvas canvas').getBoundingClientRect();return{x:r.x+r.width/2,y:r.y+r.height/2}})()`);
      // The same centre is an inspectable confidence marker in fallback mode.
      const y=point.y-(fallbackMode?0:12);
      if(layout.touch){await call('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:point.x,y}]});await call('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});}
      else {await call('Input.dispatchMouseEvent',{type:'mousePressed',x:point.x,y,button:'left',clickCount:1});await call('Input.dispatchMouseEvent',{type:'mouseReleased',x:point.x,y,button:'left',clickCount:1});}
      await waitFor(`document.querySelector('.evidence-drawer')?.dataset.open==='true' && document.querySelector('.evidence-drawer h2')?.textContent.includes(${JSON.stringify('SYNTHETIC ')}+${JSON.stringify(feed)})`,'original source record in real Evidence Drawer');
      const text=await evaluate(`document.querySelector('.evidence-drawer').textContent`);
      assert.match(text,feed==='nifc-fire-reports'?/NIFC|IRWIN/:/NASA|VIIRS/);
      assert.match(text,/no KFM EvidenceBundle|not KFM evidence|EXTERNAL_CONTEXT_ONLY|External context/i);
      await capture(`explorer-${feed}-${fallbackMode?'fallback':'flame'}`);
    }
    assert.deepEqual(errors,[]);

  });
}
