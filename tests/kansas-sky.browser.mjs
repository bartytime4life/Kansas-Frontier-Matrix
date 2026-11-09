// Real, hydrated application acceptance. Run explicitly against a built loopback
// candidate; this file is deliberately outside the ordinary *.test.mjs suite.
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import test from 'node:test';
import { spawn } from 'node:child_process';
import { mkdtemp, rm, mkdir, readFile, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { createInterceptionErrorTracker } from './browser-interception.mjs';
import { installSkyRenderObserver } from './kansas-sky-render-observer.mjs';

const origin = new URL(process.env.KFM_NODE_TEST_ORIGIN ?? 'http://127.0.0.1:5182');
assert.equal(origin.protocol, 'http:');
assert.ok(['127.0.0.1', 'localhost', '[::1]'].includes(origin.hostname), 'fixtures must never target a hosted service');
assert.equal(origin.pathname, '/');
assert.equal(origin.search, '');
assert.equal(origin.username + origin.password, '');
const chrome = process.env.KFM_TEST_CHROME ?? 'google-chrome';
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
// Explicit synthetic browser fixtures. Never provider or physical-device evidence.
const at = Date.parse('2026-11-03T12:00:00Z');
const aircraft = {hex:'abc123',callsign:'TEST123',registration:null,type:'C172',category:'A1',lon:-98.35,lat:38.5,onGround:false,altBaroFt:5000,altGeomFt:5200,groundSpeedKt:100,trackDeg:90,verticalRateFpm:200,squawk:null,emergency:null,positionAgeS:0,military:false,rollDeg:null,positionMethod:'adsb_icao'};
const record = {schemaVersion:1,id:'synthetic-browser',provider:'Synthetic browser fixture',license:'Test fixture only',sourceUrl:'https://example.invalid/synthetic',sourceSha256:'0'.repeat(64),points:[{...aircraft,observedAt:at,providerId:'synthetic'},{...aircraft,lon:-98.3,observedAt:at+30000,providerId:'synthetic'},{...aircraft,lon:-98.2,observedAt:at+120000,providerId:'synthetic',breakBefore:true}]};
const recordText = JSON.stringify(record);
const catalog = {schemaVersion:1,flights:[{id:record.id,title:'SYNTHETIC browser flight',start:new Date(at).toISOString(),end:new Date(at+120000).toISOString(),url:'/data/aviation/replays/days/2026-11-03/synthetic-browser.json',hex:aircraft.hex,day:'2026-11-03',part:1,partCount:1,pointCount:record.points.length,segmentCount:2,sha256:createHash('sha256').update(recordText).digest('hex'),provider:record.provider,license:record.license,sourceUrl:record.sourceUrl}]};
// Discovery selects the newest published day. The legacy catalog is deliberately
// empty so a missing day fetch cannot accidentally satisfy the replay assertion.
const archiveIndex = {schemaVersion:1,days:[{day:'2026-11-03',coverage:'selected-recordings',aircraftCount:1,pointCount:record.points.length,indexUrl:'/data/aviation/replays/days/2026-11-03/index.json'}]};
const archiveResponses = new Map([
  ['/data/aviation/replays/archive-index.json',JSON.stringify(archiveIndex)],
  ['/data/aviation/replays/index.json',JSON.stringify({schemaVersion:1,flights:[]})],
  [archiveIndex.days[0].indexUrl,JSON.stringify(catalog)],
  [catalog.flights[0].url,recordText],
]);
// County search preloads independently of aircraft picking. Give it a terminal,
// valid fixture so recovery retries cannot masquerade as click-triggered reads.
const counties = {feed:'census-counties',state:'empty',retrievedAt:new Date().toISOString(),upstreamUpdatedAt:null,featureCount:0,data:{type:'FeatureCollection',features:[]},source:'SYNTHETIC BROWSER FIXTURE ONLY',limitation:'Empty test inventory; no evidence admission.',truncated:false};

async function browser(t) {
  const profile = await mkdtemp(join(tmpdir(), 'kfm-county-browser-'));
  const child = spawn(chrome, [
    '--headless=new', '--remote-debugging-pipe', `--user-data-dir=${profile}`,
    '--no-first-run', '--no-default-browser-check', '--disable-background-networking',
    ...(process.getuid?.() === 0 ? ['--no-sandbox'] : []), '--disable-dev-shm-usage', '--enable-unsafe-swiftshader', '--use-angle=swiftshader', 'about:blank',
  ], { stdio: ['ignore', 'ignore', 'pipe', 'pipe', 'pipe'] });
  let stderr = '', sequence = 0, buffer = '', closed = false;
  const pending = new Map(), listeners = new Set(), checks = [];
  child.stderr.on('data', chunk => { stderr = (stderr + chunk).slice(-12000); });
  const failPending = error => { closed = true; for (const entry of pending.values()) entry.reject(error); pending.clear(); };
  // Keep a blocked browser/pipe failure diagnostic instead of an unhandled
  // stream error that loses Chrome's startup reason.
  for(const stream of [child.stdio[3],child.stdio[4]])stream.on('error',error=>failPending(new Error(`Chrome transport unavailable: ${error.message}; ${stderr}`)));
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

// Uses the production page/CSS with isolated aviation and county fixtures.
// Build identity and airport availability reach loopback; external traffic is blocked.
async function pageSession(b, { width, height, touch, motion, repaint, tileErrorDelay, basemapTrace = false }) {
  const { targetId } = await b.call('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await b.call('Target.attachToTarget', { targetId, flatten: true });
  const call = (method, params = {}) => b.call(method, params, sessionId);
  const interceptions = createInterceptionErrorTracker();
  let feedFailed=false, countyRequests=0;
  const archiveRequests=[];
  const network=[],requests=new Map();let droppedNetworkEvents=0,firstNetworkFailure=null;
  // This listener exists before Network.enable and the first Page.navigate.
  // Synthetic fixture traffic only; exported rows contain no URLs/coordinates.
  const recordNetwork=(message)=>{
    if(!basemapTrace||!['Network.requestWillBeSent','Network.responseReceived','Network.loadingFailed','Network.loadingFinished'].includes(message.method))return;
    const e=message.params;
    if(message.method==='Network.requestWillBeSent'){
      const u=new URL(e.request.url);
      const lane=u.hostname==='s3.amazonaws.com'&&u.pathname.startsWith('/elevation-tiles-prod/terrarium/')?'basemap-relief'
        :u.hostname==='tiles.openfreemap.org'?'basemap-vector'
        :u.origin===origin.origin&&u.pathname==='/api/governed/v1/layers'?'governed-catalog':'other';
      if(requests.size>=2048){droppedNetworkEvents++;return;}
      requests.set(e.requestId,{request:requests.size+1,lane});
    }
    const request=requests.get(e.requestId);if(!request)return;
    if(network.length===512){network.shift();droppedNetworkEvents++;}
    const row={...request,event:message.method,at:e.timestamp,wallTime:e.wallTime??null,
      status:e.response?.status??null,cancelled:e.canceled===true||e.errorText==='net::ERR_ABORTED'};
    if(!firstNetworkFailure&&!row.cancelled&&(row.status>=400||message.method==='Network.loadingFailed'))firstNetworkFailure=row;
    network.push(row);
  };
  b.checks.push(() => interceptions.assertHealthy());
  b.listeners.add(message => {
    if (message.sessionId !== sessionId) return;
    recordNetwork(message);
    if (message.method === 'Network.loadingFailed') interceptions.loadingFailed(message.params);
    if (message.method === 'Network.requestWillBeSent') interceptions.requestWillBeSent(message.params);
    if (message.method === 'Page.frameNavigated') interceptions.frameNavigated(message.params);
    if (message.method !== 'Fetch.requestPaused') return;
    const { requestId, request, networkId } = message.params, url = new URL(request.url);
    if(url.origin===origin.origin&&url.pathname.startsWith('/api/')&&/count(?:y|ies)|census-counties/i.test(url.pathname+url.search))countyRequests++;
    if(url.origin===origin.origin && /^\/assets\/maplibre-gl-[\w-]+\.js$/.test(url.pathname)){
      void readFile(`dist/client${url.pathname}`,'utf8').then(js=>{
        const name=js.match(/([\w$]+) as Map,/)[1];assert.ok(name,'instrument actual built Map class in this disposable response only');
        // A continuously repainting real map must become usable without idle.
        js+=`\n;{const addControl=${name}.prototype.addControl;${name}.prototype.addControl=function(...args){if(!window.__skyMap){window.__skyMap=this;window.__skyIdleCount=0;window.__skyMapFrames=0;window.__skyReadiness=[];this.on('idle',()=>window.__skyIdleCount++);const snapshot=(event)=>{const state={event,at:Math.round(performance.now()),styleLoaded:this.isStyleLoaded(),skyLayer:!!this.getLayer('kfm-kansas-sky'),portal:!!document.querySelector('.kansas-sky-map-status')};const last=window.__skyReadiness.at(-1);if(event!=='render'||!last||state.styleLoaded!==last.styleLoaded||state.skyLayer!==last.skyLayer||state.portal!==last.portal){window.__skyReadiness.push(state);if(window.__skyReadiness.length>40)window.__skyReadiness.shift();}};this.on('render',()=>{window.__skyMapFrames++;snapshot('render');});this.on('load',()=>snapshot('load'));this.on('style.load',()=>snapshot('style.load'));if(${Boolean(repaint)})this.repaint=true;}return addControl.apply(this,args);};}\n`;
        js+=`\n;(${installSkyRenderObserver.toString()})(${name});\n`;
        return call('Fetch.fulfillRequest',{requestId,responseCode:200,responseHeaders:[{name:'Content-Type',value:'text/javascript'}],body:Buffer.from(js).toString('base64')});
      }).catch(error=>interceptions.failed(error,{requestNavigation:0,navigation:0,networkId,url:request.url}));return;
    }
    if(feedFailed&&url.pathname==='/api/aviation/traffic'){void call('Fetch.fulfillRequest',{requestId,responseCode:503,body:Buffer.from('{"error":"Synthetic receiver failure"}').toString('base64')}).catch(error=>interceptions.failed(error,{requestNavigation:0,navigation:0,networkId,url:request.url}));return;}
    const archivePath=url.origin===origin.origin&&url.pathname.startsWith('/data/aviation/replays/');
    if(archivePath){
      archiveRequests.push(url.pathname);
      // Never let an omitted fixture read a real published recording.
      if(!archiveResponses.has(url.pathname)){
        interceptions.failed(new Error(`Unprepared synthetic archive request: ${url.pathname}`),{requestNavigation:0,navigation:0,networkId,url:request.url});
        void call('Fetch.fulfillRequest',{requestId,responseCode:404,body:Buffer.from('{"error":"Unprepared synthetic archive path"}').toString('base64')}).catch(error=>interceptions.failed(error,{requestNavigation:0,navigation:0,networkId,url:request.url}));return;
      }
    }
    const synthetic = url.pathname === '/api/aviation/traffic' ? JSON.stringify({retrievedAt:new Date().toISOString(),evidenceRole:'EXTERNAL_CONTEXT_ONLY',provider:{id:'adsb-lol',title:'Synthetic test receiver',homepage:'https://example.invalid/',terms:'Test only'},records:[{...aircraft,observedAt:new Date().toISOString()}],dropped:0,limitation:'Synthetic fixture'})
      : archivePath ? archiveResponses.get(url.pathname)
      : url.pathname === '/api/live-context' && url.searchParams.get('feed') === 'census-counties' ? JSON.stringify(counties) : null;
    const operation = synthetic !== null ? call('Fetch.fulfillRequest', {requestId,responseCode:200,responseHeaders:[{name:'Content-Type',value:'application/json'}],body:Buffer.from(synthetic).toString('base64')}) : url.origin !== origin.origin
      ? (/\/styles\/|\/style\.json$/.test(url.pathname)
        ? call('Fetch.fulfillRequest', { requestId, responseCode: 200, responseHeaders: [{ name: 'Content-Type', value: 'application/json' }], body: Buffer.from(JSON.stringify({ version: 8, sources: {}, layers: [{ id: 'layout-test-background', type: 'background', paint: { 'background-color': '#172832' } }] })).toString('base64') })
        : (tileErrorDelay ? pause(tileErrorDelay).then(()=>call('Fetch.failRequest', { requestId, errorReason: 'BlockedByClient' })) : call('Fetch.failRequest', { requestId, errorReason: 'BlockedByClient' })))
      : url.pathname.startsWith('/api/') && !['/api/build', '/api/aviation/airports'].includes(url.pathname)
        ? call('Fetch.fulfillRequest', { requestId, responseCode: 503, responseHeaders: [{ name: 'Content-Type', value: 'application/json' }], body: Buffer.from('{"error":"Layout test: unrelated source unavailable"}').toString('base64') })
        : call('Fetch.continueRequest', { requestId });
    void operation
      .catch(error => interceptions.failed(error, { requestNavigation: 0, navigation: 0, networkId, url: request.url }));
  });
  await call('Page.enable');
  await call('Runtime.enable');
  await call('Network.enable');
  await call('Fetch.enable', { patterns: [{ urlPattern: 'http*' }] });
  await call('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: false });
  await call('Emulation.setTouchEmulationEnabled', { enabled: touch });
  await call('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: motion }] });
  await call('Page.addScriptToEvaluateOnNewDocument', { source: "localStorage.setItem('kfm.explorer.guide.dismissed.v2','1');window.__skyErrors=[];window.addEventListener('error',e=>window.__skyErrors.push(e.message));window.addEventListener('unhandledrejection',e=>window.__skyErrors.push(String(e.reason?.message??e.reason)));" });
  const evaluate = async expression => {
    try {
      const result = await call('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
      if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
      await interceptions.assertHealthy();
      return result.result.value;
    } catch (error) {
      throw new Error(`Runtime.evaluate failed for ${expression.slice(0,1200)}: ${error.message}`, {cause:error});
    }
  };
  const wait = async (expression, label) => {
    const deadline = Date.now() + 15000;
    while (Date.now() < deadline) {
      if (await evaluate(`Boolean(${expression})`)) return;
      await pause(50);
    }
    throw new Error(`Timed out: ${label}`);
  };
  const key = async (key, code, windowsVirtualKeyCode, modifiers = 0) => {
    await call('Input.dispatchKeyEvent', { type: 'rawKeyDown', key, code, windowsVirtualKeyCode, modifiers });
    if (key === 'Enter') await call('Input.dispatchKeyEvent', { type: 'char', key, code, windowsVirtualKeyCode, text: '\r', unmodifiedText: '\r' });
    await call('Input.dispatchKeyEvent', { type: 'keyUp', key, code, windowsVirtualKeyCode, modifiers });
  };
  const rect = selector => evaluate(`(() => { const r=document.querySelector(${JSON.stringify(selector)}).getBoundingClientRect(); return {x:r.x,y:r.y,width:r.width,height:r.height}; })()`);
  const activate = async selector => {
    // Scroll through the real scroll container, then deliver native pointer input.
    await evaluate(`document.querySelector(${JSON.stringify(selector)}).scrollIntoView({block:'center',behavior:'instant'})`);
    const r = await rect(selector), x = r.x + r.width / 2, y = r.y + r.height / 2;
    assert.ok(x > 0 && x < width && y > 0 && y < height, `reachable target ${selector}`);
    assert.ok(await evaluate(`document.querySelector(${JSON.stringify(selector)}).contains(document.elementFromPoint(${x},${y}))`), `unobscured target ${selector}`);
    if (touch) {
      await call('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x, y }] });
      await call('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] });
    } else {
      await call('Input.dispatchMouseEvent', { type: 'mousePressed', x, y, button: 'left', clickCount: 1 });
      await call('Input.dispatchMouseEvent', { type: 'mouseReleased', x, y, button: 'left', clickCount: 1 });
    }
  };
  const visibleFocus = () => evaluate(`(() => {
    const e=document.activeElement,r=e.getBoundingClientRect(),panel=document.querySelector('.layer-panel').getBoundingClientRect(),head=document.querySelector(innerHeight<=600 ? '.layer-panel .panel-heading' : '.layer-panel-explore > summary').getBoundingClientRect(),style=getComputedStyle(e);
    return { tag:e.tagName,text:e.textContent,top:r.top,bottom:r.bottom,hit:e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2)),within:r.top>=Math.max(head.bottom,panel.top)-1&&r.bottom<=Math.min(panel.bottom,innerHeight)+1,outline:style.outlineStyle,outlineWidth:parseFloat(style.outlineWidth),focusVisible:e.matches(':focus-visible') };
  })()`);
  await call('Page.navigate', { url: new URL(basemapTrace?'?l=&ctx=&base=midnight&mapui=open&maptab=scene&basemapTrace=1':'?l=&ctx=', origin).href });
  await wait(`history.state?.kfmExplorerView && document.querySelector('.map-chrome-dock')`, 'hydration');
  return { call, evaluate, wait, key, rect, activate, visibleFocus, failFeed:()=>{feedFailed=true;}, countyRequestCount:()=>countyRequests, archiveRequests:()=>[...archiveRequests], networkSnapshot:()=>({events:[...network],firstFailure:firstNetworkFailure,droppedEvents:droppedNetworkEvents,boundary:'SYNTHETIC loopback fixture; capture enabled before initial navigation. Provider lanes and catalog remain separate.'}) };
}


test('Kansas Sky basemap warning lifecycle records first failure and preserves real failures across resizing', {timeout:120000}, async t=>{
  const b=await browser(t),p=await pageSession(b,{width:1440,height:900,touch:false,motion:'no-preference',basemapTrace:true});
  const warning=`[...document.querySelectorAll('.runtime-degraded-banner')].some(e=>/basemap tiles are unavailable|basemap source reported an error/i.test(e.textContent))`;
  const snapshot=()=>p.evaluate(`({fixture:'SYNTHETIC',trace:window.__kfmBasemapTrace?.snapshot()??null,style:{name:window.__skyMap?.getStyle()?.name??null,loaded:window.__skyMap?.isStyleLoaded()??false,relief:!!window.__skyMap?.getSource('basemap-relief-dem'),fixtureBackground:!!window.__skyMap?.getLayer('layout-test-background')},selected:document.querySelector('select[aria-label="Appearance basemap"]')?.value??null,banners:[...document.querySelectorAll('.runtime-degraded-banner')].map(e=>e.textContent),errors:window.__skyErrors??[]})`);
  b.checks.unshift(async()=>{
    const state=await snapshot();
    t.diagnostic(JSON.stringify({...state,trace:state.trace?{...state.trace,events:state.trace.events.slice(-15)}:null}));
    if(process.env.KFM_SKY_SCREENSHOTS){await mkdir(process.env.KFM_SKY_SCREENSHOTS,{recursive:true});await writeFile(join(process.env.KFM_SKY_SCREENSHOTS,'basemap-warning-final-or-failure.json'),JSON.stringify({...state,network:p.networkSnapshot()},null,2));}
  });
  await p.wait(`window.__skyMap?.getSource('basemap-relief-dem') && window.__kfmBasemapTrace`, 'diagnostics attached to running Midnight map');
  await p.wait(warning,'actual deliberately blocked relief source remains visibly warned');
  const first=await p.evaluate(`window.__kfmBasemapTrace.snapshot().firstFailure`);
  assert.ok(first,'first map error retained before recovery');
  const generation=await p.evaluate(`window.__kfmBasemapTrace.snapshot().events.at(-1).generation`);
  await p.evaluate(`(()=>{const s=document.querySelector('select[aria-label="Appearance basemap"]');s.value='standard';s.dispatchEvent(new Event('change',{bubbles:true}));})()`);
  await p.wait(`window.__skyMap.isStyleLoaded() && !window.__skyMap.getSource('basemap-relief-dem') && !(${warning})`, 'successful blank fixture style retires abandoned relief warning');
  assert.deepEqual(await p.evaluate(`window.__kfmBasemapTrace.snapshot().firstFailure`),first,'first failure survives style recovery');
  await p.evaluate(`(()=>{const s=document.querySelector('select[aria-label="Appearance basemap"]');s.value='midnight';s.dispatchEvent(new Event('change',{bubbles:true}));})()`);
  await p.wait(warning,'new real fixture failure is not hidden by recovery reset');
  await p.call('Emulation.setDeviceMetricsOverride',{width:375,height:844,deviceScaleFactor:1,mobile:false});
  await p.wait(`innerWidth===375`,'phone viewport');
  await p.call('Emulation.setDeviceMetricsOverride',{width:1440,height:900,deviceScaleFactor:1,mobile:false});
  await p.wait(`innerWidth===1440 && window.__kfmBasemapTrace.snapshot().events.some(e=>e.event==='resize')`,'desktop viewport and resize trace');
  assert.equal(await p.evaluate(`Boolean(${warning})`),true,'still-failed source stays warned after resizing');
  const trace=await p.evaluate(`window.__kfmBasemapTrace.snapshot()`),network=p.networkSnapshot();
  assert.ok(trace.events.some(e=>e.generation>generation));assert.equal(trace.collectorErrors,0);
  assert.ok(network.events.some(e=>e.lane==='basemap-relief'),'network capture includes provider lane from beginning');
  assert.ok(network.events.some(e=>e.event==='Network.requestWillBeSent'));
  if(process.env.KFM_SKY_SCREENSHOTS){await mkdir(process.env.KFM_SKY_SCREENSHOTS,{recursive:true});await writeFile(join(process.env.KFM_SKY_SCREENSHOTS,'basemap-warning-lifecycle.json'),JSON.stringify({fixture:'SYNTHETIC',trace,network},null,2));}
  assert.deepEqual(await p.evaluate(`window.__skyErrors`),[]);
});

for (const {repaint,tileErrorDelay} of [{repaint:false,tileErrorDelay:0},{repaint:true,tileErrorDelay:0},{repaint:false,tileErrorDelay:1200}]) for (const layout of [{width:1440,height:900,touch:false,motion:'no-preference'},{width:390,height:844,touch:true,motion:'reduce'}]) test(`Kansas Sky synthetic live/replay controls ${layout.width}px${repaint?' with continuous repaint':''}${tileErrorDelay?' with late tile failures':''}`,{timeout:120000},async t=>{
  const artifactKey=`${layout.width}${repaint?'-repainting':''}${tileErrorDelay?'-late-tiles':''}`;
  const b=await browser(t),p=await pageSession(b,{...layout,repaint,tileErrorDelay});
  if(process.env.KFM_SKY_SCREENSHOTS)b.checks.unshift(async()=>{
    await mkdir(process.env.KFM_SKY_SCREENSHOTS,{recursive:true});
    const shot=await p.call('Page.captureScreenshot',{format:'png'});
    await writeFile(join(process.env.KFM_SKY_SCREENSHOTS,`sky-synthetic-final-or-failure-${artifactKey}.png`),Buffer.from(shot.data,'base64'));
    await writeFile(join(process.env.KFM_SKY_SCREENSHOTS,`sky-synthetic-final-or-failure-${artifactKey}.json`),JSON.stringify(await p.evaluate(`({fixture:'SYNTHETIC',render:window.__skyRender??null,map:window.__skyMap?{styleLoaded:window.__skyMap.isStyleLoaded(),loaded:window.__skyMap.loaded(),moving:window.__skyMap.isMoving(),connected:window.__skyMap.getCanvas().isConnected,repaint:window.__skyMap.repaint,skyLayer:!!window.__skyMap.getLayer('kfm-kansas-sky'),idleEvents:window.__skyIdleCount,frames:window.__skyMapFrames,readiness:window.__skyReadiness,renderListeners:(window.__skyMap._listeners?.render??[]).slice(0,12).map(fn=>fn.toString().slice(0,300))}:null,manualGesture:window.__skyManualGesture??null,hidden:document.hidden,aviation:document.querySelector('input[aria-label="Hide airspace and aviation layers"]')?.closest('.official-context-primary')?.textContent??null,control:document.querySelector('.kansas-sky')?.textContent??null,errors:window.__skyErrors??[],viewport:[innerWidth,innerHeight],bodyWidth:document.documentElement.scrollWidth})`),null,2));
  });
  await p.evaluate(`(()=>{const visible=e=>e&&e.getBoundingClientRect().width>0&&e.getBoundingClientRect().height>0;for(const selector of ['.map-dock-actions > button:nth-child(2)','.map-mobile-actions button:first-child']){const button=document.querySelector(selector);if(visible(button)){button.click();return;}}const menu=document.querySelector('.map-dock-map-menu');if(menu)menu.open=true;document.querySelector('.map-dock-menu-quick button:nth-child(2)')?.click();})()`);
  await p.wait(`document.querySelector('.layer-panel').getAttribute('aria-hidden')==='false'`,'normal Layers panel open');

  // Open real panel disclosures without changing app state, then activate the real visibility input.
  await p.evaluate(`(() => {for(const e of document.querySelectorAll('details')) if(e.querySelector('input[aria-label="Show airspace and aviation layers"]'))e.open=true; document.querySelector('input[aria-label="Show airspace and aviation layers"]').click();})()`);
  await p.wait(`document.querySelector('.kansas-sky')`,'sky control loaded from real NASR context');
  await p.wait(`window.__skyMap?.getLayer('kfm-kansas-sky') && window.__skyRender?.aircraftVertices>0`,'real custom aircraft layer issues GPU triangle draws');
  if(repaint)assert.deepEqual(await p.evaluate(`({repaint:window.__skyMap.repaint,idleEvents:window.__skyIdleCount})`),{repaint:true,idleEvents:0},'initial aircraft drawing does not depend on idle');
  await p.evaluate(`void window.__skyMap.jumpTo({center:[-98.35,38.5],zoom:7,pitch:55})`);
  await p.wait(`document.querySelector('.kansas-sky select[aria-label="Kansas Sky aircraft"] option[value="abc123"]')`,'observed synthetic aircraft');
  await p.evaluate(`(() => {const e=document.querySelector('.kansas-sky');for(let p=e.parentElement;p;p=p.parentElement){if(p.tagName==='DETAILS')p.open=true;}const panel=document.querySelector('.layer-panel');if(panel?.getAttribute('aria-hidden')==='true'){const button=[...document.querySelectorAll('button')].find(b=>b.textContent.trim()==='Layers');button?.click();}})()`);
  await pause(500);
  // A real map silhouette click must reveal its inspector from the inert, closed panel.
  await p.evaluate(`(()=>{window.__skyMap.jumpTo({center:[-98.35,38.5],zoom:7,pitch:0,bearing:0});document.querySelector('.kansas-sky').closest('details').open=false;})()`);
  await p.activate('[aria-label="Close Explorer navigation"]');
  await p.wait(`document.querySelector('.layer-panel').getAttribute('aria-hidden')==='true'`,'Layers closed before map inspection');
  assert.equal(await p.evaluate(`document.querySelector('[aria-label="Kansas Sky aircraft"]').value`),'','aircraft not selected before click');
  await pause(500);
  const countyRequestsBeforeAircraft=p.countyRequestCount();
  assert.equal(countyRequestsBeforeAircraft,1,'one independent county preload precedes aircraft inspection');
  // Late tile responses can leave the real loading overlay above a drawn map.
  // Wait for the same hit target that activate asserts; never tap through it.
  await p.wait(`(()=>{const canvas=document.querySelector('.maplibregl-canvas'),r=canvas?.getBoundingClientRect();return r && r.width>0 && r.height>0 && canvas.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2));})()`,'map canvas ready for aircraft inspection');
  await p.activate('.maplibregl-canvas');
  await p.wait(`document.querySelector('.layer-panel').getAttribute('aria-hidden')==='false' && document.querySelector('.kansas-sky h5')?.textContent.includes('TEST123')`,'map click opens aircraft instruments');
  await p.wait(`document.activeElement===document.querySelector('[aria-label="Kansas Sky aircraft"]')`,'aircraft selector receives focus after panel opens');
  assert.equal(p.countyRequestCount(),countyRequestsBeforeAircraft,'aircraft inspection does not request county context beneath it');
  assert.equal(await p.evaluate(`document.querySelector('[data-layer-view="selected"]').getAttribute('aria-pressed')`),'true','On map view reveals aircraft controls');
  assert.equal(await p.evaluate(`document.querySelector('.kansas-sky').closest('details').open`),true,'Aviation disclosure opened');
  assert.equal(await p.evaluate(`document.querySelector('input[aria-label="Hide airspace and aviation layers"]').checked`),true,'inspection keeps Aviation enabled');
  await p.wait(`(()=>{const e=document.querySelector('[aria-label="Kansas Sky aircraft"]'),r=e.getBoundingClientRect(),h=document.querySelector('.kansas-sky h5').getBoundingClientRect();return r.width>0&&r.top>=0&&r.bottom<=innerHeight&&!e.closest('[inert]')&&e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2))&&h.top>=0&&h.bottom<=innerHeight;})()`,'selected aircraft and instruments heading are visible and interactive');
  await p.evaluate(`void window.__skyMap.jumpTo({pitch:55})`);
  assert.match(await p.evaluate(`document.querySelector('.kansas-sky').textContent`),/Pressure altitude[\s\S]*Geometric · WGS84/);
  assert.match(await p.evaluate(`document.querySelector('.kansas-sky').textContent`),/Reported rollUnavailable/);
  await p.evaluate(`document.querySelector('.kansas-sky-modes button:nth-child(3)').click()`);
  await p.wait(`document.querySelector('[aria-label="Archive day"]').value==='2026-11-03' && document.querySelector('[aria-label="Recorded flight"] option[value="synthetic-browser"]')`,'discovered daily catalog');
  assert.ok(p.archiveRequests().includes('/data/aviation/replays/archive-index.json'),'daily archive discovery was requested');
  assert.ok(p.archiveRequests().includes(archiveIndex.days[0].indexUrl),'the selected daily catalog was requested');
  await p.evaluate(`(() => {const e=document.querySelector('[aria-label="Recorded flight"]');e.value='synthetic-browser';e.dispatchEvent(new Event('change',{bubbles:true}));})()`);
  await p.wait(`document.querySelector('.kansas-sky h5')?.textContent.includes('TEST123') && document.querySelector('[aria-label="Flight timeline"]').min===''+${at}`,'digest-verified replay');
  assert.ok(p.archiveRequests().includes(catalog.flights[0].url),'the catalog-declared daily flight file was requested');
  assert.match(await p.evaluate(`document.querySelector('.kansas-sky-history').textContent`),/File integrity: SHA-256 verified/);
  assert.equal(await p.evaluate(`document.querySelector('.kansas-sky-badge').textContent`),'REPLAY');
  assert.match(await p.evaluate(`document.querySelector('.kansas-sky-context').textContent`),/not a reconstruction/);
  if(layout.motion!=='reduce'){
    await p.evaluate(`document.querySelector('.kansas-sky-camera button:nth-child(2)').click()`);
    await p.wait(`document.querySelector('.kansas-sky-camera button:nth-child(2)').getAttribute('aria-pressed')==='true'`,'follow camera enabled');
    const canvas=await p.rect('.maplibregl-canvas');
    const x=Math.min(layout.width-20,canvas.x+canvas.width*.9),y=canvas.y+canvas.height*.55;
    // Retain actual delivery and camera state around the unchanged native drag.
    // This trace never drives the camera or substitutes for the release assertion.
    const gestureHits=await p.evaluate(`(()=>{
      const map=window.__skyMap,canvas=map.getCanvas();
      const camera=()=>document.querySelector('.kansas-sky-camera button[aria-pressed="true"]')?.textContent??null;
      const target=e=>e instanceof Element?{tag:e.tagName,id:e.id,classes:String(e.className).slice(0,160),canvas:e===canvas}:null;
      const trace=window.__skyManualGesture={start:{x:${x},y:${y}},end:{x:${x-35},y:${y+10}},canvasBounds:canvas.getBoundingClientRect().toJSON(),moveStartListenersBefore:map._listeners?.movestart?.length??0,events:[]};
      const record=(stage,e)=>{if(trace.events.length<16)trace.events.push({stage,at:Math.round(performance.now()),camera:camera(),target:target(e?.target),originalEvent:e?.originalEvent?.type??null});};
      const documentDown=e=>record('document-pointerdown',e),canvasDown=e=>record('canvas-pointerdown',e),start=e=>record('movestart',e),end=e=>record('moveend',e);
      document.addEventListener('pointerdown',documentDown,true);canvas.addEventListener('pointerdown',canvasDown);map.on('movestart',start);map.on('moveend',end);
      window.__skyStopManualTrace=()=>{record('assertion-finished');trace.finalCamera=camera();document.removeEventListener('pointerdown',documentDown,true);canvas.removeEventListener('pointerdown',canvasDown);map.off('movestart',start);map.off('moveend',end);delete window.__skyStopManualTrace;};
      record('before-input');return [document.elementFromPoint(${x},${y})===canvas,document.elementFromPoint(${x-35},${y+10})===canvas];
    })()`);
    try{
      assert.deepEqual(gestureHits,[true,true],'native drag endpoints hit the unobstructed map canvas');
      await p.call('Input.dispatchMouseEvent',{type:'mousePressed',x,y,button:'left',clickCount:1});
      await p.call('Input.dispatchMouseEvent',{type:'mouseMoved',x:x-35,y:y+10,button:'left',buttons:1});
      await p.call('Input.dispatchMouseEvent',{type:'mouseReleased',x:x-35,y:y+10,button:'left',clickCount:1});
      await p.wait(`document.querySelector('.kansas-sky-camera button:first-child').getAttribute('aria-pressed')==='true'`,'manual map gesture cancels following');
    }finally{await p.evaluate(`window.__skyStopManualTrace?.()`);}
    await p.evaluate(`document.querySelector('.kansas-sky-camera button:nth-child(2)').click()`);
    await p.wait(`document.querySelector('.kansas-sky-camera button:nth-child(2)').getAttribute('aria-pressed')==='true'`,'follow reenabled');
    await p.evaluate(`(()=>{const control=document.querySelector('.maplibregl-ctrl-zoom-in');if(control)control.click();else window.__skyMap.zoomIn({duration:0});})()`);
    await p.wait(`document.querySelector('.kansas-sky-camera button:first-child').getAttribute('aria-pressed')==='true'`,'manual navigation zoom cancels following');

  }

  await p.evaluate(`document.querySelector('[aria-label="Flight timeline"]').focus()`);
  await p.key('ArrowRight','ArrowRight',39);
  assert.ok(Number(await p.evaluate(`document.querySelector('[aria-label="Flight timeline"]').value`))>at,'keyboard scrubbing advances recorded time');
  assert.match(await p.evaluate(`document.querySelector('[aria-label="Flight timeline"]').getAttribute('aria-valuetext')`),/2026-11-03 .* UTC/,'accessible timeline announces UTC rather than epoch milliseconds');
  assert.equal(await p.evaluate(`document.documentElement.scrollWidth <= innerWidth`),true,'no document overflow');
  if(layout.motion==='reduce')assert.equal(await p.evaluate(`document.querySelector('.kansas-sky-camera button:nth-child(2)').disabled`),true,'reduced motion disables camera following');
  assert.equal(await p.evaluate(`document.querySelector('.kansas-sky').textContent.includes('renderer unavailable')`),false,'no shader fallback');
  // Normal Aviation controls remain editable. 2D means geographic silhouettes,
  // not falsely elevated glyphs drawn over a flattened sectional-style chart.
  await p.evaluate(`document.querySelector('input[name="kfm-aviation-view"][type="radio"]:not(:checked)').click()`);
  await p.wait(`document.querySelector('.kansas-sky').dataset.projection==='2d' && window.__skyRender.maxZ===0`,'2D geometry is genuinely flat');
  assert.equal(await p.evaluate(`document.querySelector('.kansas-sky-camera button:nth-child(2)').disabled`),true);
  await p.evaluate(`document.querySelector('input[name="kfm-aviation-view"][type="radio"]:not(:checked)').click()`);
  await p.wait(`document.querySelector('.kansas-sky').dataset.projection==='3d' && window.__skyRender.maxZ>0`,'3D altitude geometry restored');
  const airportsBefore=await p.evaluate(`document.querySelector('input[aria-label="Hide airspace and aviation layers"]').checked`);
  assert.equal(airportsBefore,true,'working aviation layer remains selected');
  const airportToggle=`[...document.querySelectorAll('.official-context-row label')].find(e=>e.textContent.includes('Public-use airports and runways')).querySelector('input')`;
  const airportState=await p.evaluate(`(${airportToggle}).checked`);
  await p.evaluate(`(${airportToggle}).click()`);
  assert.equal(await p.evaluate(`(${airportToggle}).checked`),!airportState,'ordinary airport layer remains independently editable during replay');
  await p.evaluate(`(${airportToggle}).click()`);

  // Reload the actual style, not a fake event; the custom layer reinstalls.
  await p.evaluate(`new Promise(resolve=>{
    window.__skyMap.once('style.load',()=>{
      window.__skyReloadCheckpoint={render:window.__skyRender,frames:window.__skyRender.frames};
      resolve();
    });
    window.__skyMap.setStyle({version:8,sources:{},layers:[{id:'synthetic-style-reload',type:'background',paint:{'background-color':'#172832'}}]});
  })`);
  await p.wait(`window.__skyMap.getLayer('synthetic-style-reload') && window.__skyMap.isStyleLoaded()
    && window.__skyMap.getLayer('kfm-kansas-sky') && window.__skyRender.aircraftVertices>0
    && (window.__skyRender!==window.__skyReloadCheckpoint.render || window.__skyRender.frames>window.__skyReloadCheckpoint.frames)`,'settled replacement style renders a fresh aircraft frame');
  if(repaint)assert.equal(await p.evaluate(`window.__skyIdleCount`),0,'replacement style recovery also precedes idle');
  await p.evaluate(`document.querySelector('.kansas-sky-clock').scrollIntoView({block:'center',behavior:'instant'})`);
  await p.wait(`document.querySelector('.toast')?.dataset.visible!=='true'`,'transient status toast settled before controls capture');
  if(process.env.KFM_SKY_SCREENSHOTS){
    await mkdir(process.env.KFM_SKY_SCREENSHOTS,{recursive:true});
    const capture=await p.call('Page.captureScreenshot',{format:'png'});
    await writeFile(join(process.env.KFM_SKY_SCREENSHOTS,`sky-synthetic-controls-${artifactKey}.png`),Buffer.from(capture.data,'base64'));
    await writeFile(join(process.env.KFM_SKY_SCREENSHOTS,`sky-synthetic-render-${artifactKey}.json`),JSON.stringify(await p.evaluate(`({fixture:'SYNTHETIC',render:window.__skyRender,clock:document.querySelector('.kansas-sky-clock').textContent,layer:window.__skyMap.getLayer('kfm-kansas-sky').type})`),null,2));
  }
  // Inspect actual built rendering at the second recorded observation: both
  // the aircraft glyph and its measured route must issue distinct GPU draws.
  // Cinematic selected paths are triangle strips; counting only gl.LINES
  // misclassifies a rendered route as absent and route triangles as aircraft.
  // Temporarily use the real airspace controls for an unobscured map capture;
  // the preceding interaction checks already establish editable coexistence.
  const airspaceVolumes=`[...document.querySelectorAll('.official-context-row fieldset')].find(fieldset=>fieldset.querySelector('legend')?.textContent==='Airspace volumes')`;
  const enabledVolumeIndices=await p.evaluate(`(()=>{const inputs=[...(${airspaceVolumes}).querySelectorAll('input[type="checkbox"]')];const enabled=inputs.flatMap((input,index)=>input.checked?[index]:[]);for(const index of enabled)inputs[index].click();return enabled;})()`);
  await p.wait(`![...(${airspaceVolumes}).querySelectorAll('input[type="checkbox"]')].some(input=>input.checked)`,'airspace volumes temporarily hidden through their controls');
  await p.evaluate(`(()=>{const e=document.querySelector('[aria-label="Flight timeline"]');const setter=Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set;setter.call(e,${at+30000});e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}));window.__skyMap.jumpTo({center:[-98.325,38.52],zoom:10,pitch:45,bearing:0});})()`);
  await p.wait(`window.__skyRender.aircraftVertices>0 && (window.__skyRender.pathTriangles>=6 || window.__skyRender.lineTrailVertices>=2) && Number(document.querySelector('[aria-label="Flight timeline"]').value)===${at+30000}`,'second observed sample renders aircraft and retained trail');
  await p.activate('[aria-label="Close Explorer navigation"]');
  await p.wait(`document.querySelector('.layer-panel').getAttribute('aria-hidden')==='true' && !window.__skyMap.isMoving() && document.querySelector('.toast')?.dataset.visible!=='true'`,'unobstructed replay map ready');
  // Wait for the close transition to release the whole map, using rendered geometry.
  await p.wait(`document.querySelector('.layer-panel').getAnimations().every(animation=>animation.playState!=='running')`,'closed Layers no longer covers flight view');
  await p.wait(`document.querySelector('.kansas-sky-map-status')?.dataset.state==='REPLAY' && document.querySelector('.kansas-sky-map-status time')?.dateTime===${JSON.stringify(new Date(at+30000).toISOString())}`,'closed-panel map still labels replay and its synchronized UTC instant');
  assert.equal(await p.evaluate(`(()=>{const badge=document.querySelector('.kansas-sky-map-status'),r=badge.getBoundingClientRect();return !badge.closest('.layer-panel')&&badge.checkVisibility()&&r.left>=0&&r.right<=innerWidth&&r.top>=0&&r.bottom<=innerHeight&&getComputedStyle(badge).pointerEvents==='none'&&(()=>{const time=badge.querySelector('time'),t=time?.getBoundingClientRect();return t&&t.width>0&&t.height>0&&document.elementFromPoint(t.x+t.width/2,t.y+t.height/2)?.classList.contains('maplibregl-canvas');})()&&![...document.querySelectorAll('.maplibregl-ctrl button,.runtime-degraded-banner,.build-year-warning,.no-time-data,.map-mobile-actions,.map-tool-rail button')].some(button=>{const b=button.getBoundingClientRect();return button.checkVisibility()&&b.width>0&&b.height>0&&b.left<r.right&&b.right>r.left&&b.top<r.bottom&&b.bottom>r.top;});})()`),true,'replay date is visible without intercepting input or overlapping degradation notices, source notices or map controls');
  // The source/time label still passes pointer input through; the explicitly
  // interactive Find action must receive its own hit and open the real list.
  assert.equal(await p.evaluate(`(()=>{const button=document.querySelector('[aria-label="Find aircraft"]'),r=button.getBoundingClientRect();return r.width>=30&&r.height>=30&&button.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2));})()`),true,'Find aircraft is a visible unobstructed target');
  await p.activate('[aria-label="Find aircraft"]');
  await p.wait(`document.querySelector('.layer-panel').getAttribute('aria-hidden')==='false' && document.activeElement===document.querySelector('[aria-label="Kansas Sky aircraft"]')`,'Find aircraft opens the existing list and transfers keyboard focus');
  await p.activate('[aria-label="Close Explorer navigation"]');
  await p.wait(`document.querySelector('.layer-panel').getAttribute('aria-hidden')==='true' && document.querySelector('.layer-panel').getAnimations().every(animation=>animation.playState!=='running')`,'Find list closes without replacing the aircraft scene');
  if(process.env.KFM_SKY_SCREENSHOTS){
    const capture=await p.call('Page.captureScreenshot',{format:'png'});
    await writeFile(join(process.env.KFM_SKY_SCREENSHOTS,`sky-synthetic-aircraft-trail-${artifactKey}.png`),Buffer.from(capture.data,'base64'));
    await writeFile(join(process.env.KFM_SKY_SCREENSHOTS,`sky-synthetic-aircraft-trail-${artifactKey}.json`),JSON.stringify(await p.evaluate(`({fixture:'SYNTHETIC',basemap:'isolated fixture background',airspaceVolumes:'off through existing controls for this capture; restored afterward',sampleTime:${at+30000},statusBounds:document.querySelector('.kansas-sky-map-status').getBoundingClientRect().toJSON(),degradationNotices:[...document.querySelectorAll('.runtime-degraded-banner')].filter(e=>e.checkVisibility()).map(e=>({text:e.textContent,bounds:e.getBoundingClientRect().toJSON()})),render:window.__skyRender,camera:{center:window.__skyMap.getCenter().toArray(),zoom:window.__skyMap.getZoom(),pitch:window.__skyMap.getPitch()},mode:document.querySelector('.kansas-sky-badge').textContent})`),null,2));
  }
  await p.evaluate(`(()=>{const visible=e=>e&&e.getBoundingClientRect().width>0&&e.getBoundingClientRect().height>0;for(const selector of ['.map-dock-actions > button:nth-child(2)','.map-mobile-actions button:first-child']){const button=document.querySelector(selector);if(visible(button)){button.click();return;}}const menu=document.querySelector('.map-dock-map-menu');if(menu)menu.open=true;document.querySelector('.map-dock-menu-quick button:nth-child(2)')?.click();})()`);
  await p.wait(`document.querySelector('.layer-panel').getAttribute('aria-hidden')==='false'`,'Layers restored after flight map capture');
  await p.evaluate(`(()=>{const inputs=[...(${airspaceVolumes}).querySelectorAll('input[type="checkbox"]')];for(const index of ${JSON.stringify(enabledVolumeIndices)})if(!inputs[index].checked)inputs[index].click();})()`);
  assert.deepEqual(await p.evaluate(`[...(${airspaceVolumes}).querySelectorAll('input[type="checkbox"]')].flatMap((input,index)=>input.checked?[index]:[])`),enabledVolumeIndices,'airspace selections restored after isolated rendering capture');
  // The 90-second source gap contains no invented aircraft.
  await p.evaluate(`(()=>{const e=document.querySelector('[aria-label="Flight timeline"]');const setter=Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set;setter.call(e,${at+60000});e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}));})()`);
  await p.wait(`document.querySelector('.kansas-sky').textContent.includes('No observation for this aircraft') && window.__skyRender.aircraftVertices===0`,'gap refuses fabricated positions');
  await p.evaluate(`document.querySelector('.kansas-sky-transport button:last-child').click()`);
  await p.wait(`document.querySelector('.kansas-sky-badge').textContent==='LIVE FEED' && document.querySelector('.kansas-sky-map-status')?.dataset.state==='LIVE FEED'`,'return live updates both panel and persistent map status');
  p.failFeed();
  // Re-enable the real traffic toggle to request the synthetic outage immediately,
  // preserving normal production polling cadence rather than overriding timers.
  await p.evaluate(`(()=>{const e=[...document.querySelectorAll('.official-context-row label')].find(e=>e.textContent.includes('Kansas Sky · observed aircraft')).querySelector('input');e.click();})()`);
  await p.wait(`!document.querySelector('.kansas-sky')`,'traffic toggle off');
  await p.evaluate(`(()=>{const e=[...document.querySelectorAll('.official-context-row label')].find(e=>e.textContent.includes('Kansas Sky · observed aircraft')).querySelector('input');e.click();})()`);
  await p.wait(`document.querySelector('.kansas-sky-badge')?.textContent==='UNAVAILABLE' && document.querySelector('.kansas-sky-map-status')?.dataset.state==='UNAVAILABLE' && window.__skyRender.aircraftVertices===0`,'provider failure removes current positions and live badge');

  await p.evaluate(`document.querySelector('input[aria-label="Hide airspace and aviation layers"]').click()`);
  await p.wait(`!document.querySelector('.kansas-sky') && !document.querySelector('.kansas-sky-map-status')`,'hidden layer tears down control and map status');
});
