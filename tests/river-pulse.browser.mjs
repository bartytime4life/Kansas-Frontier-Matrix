// Real, hydrated application acceptance. Run explicitly against a built loopback
// candidate; this file is deliberately outside the ordinary *.test.mjs suite.
import assert from 'node:assert/strict';
import test from 'node:test';
import { spawn } from 'node:child_process';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { createInterceptionErrorTracker } from './browser-interception.mjs';
import { isolateBrowserNetwork } from './browser-network.mjs';

function fixture() {
  const end = Math.floor(Date.now() / 900000) * 900000;
  const times = Array.from({length:12}, (_,i) => new Date(end-(11-i)*900000).toISOString());
  return {
    format:'kfm-usgs-streamflow-v1',feed:'usgs-streamflow',state:'ready',retrievedAt:new Date().toISOString(),
    query:{mode:'recent-series',start:times[0],end:times.at(-1),parameterCode:'00060'},
    stations:[{stationId:'USGS-06864500',name:'Synthetic dismissal test gauge',longitude:-98.4,latitude:38.5953,agencyCode:'USGS',siteTypeCode:'ST'}],
    observations:times.map((observedAt,i)=>({stationId:'USGS-06864500',observedAt,value:100+i,unit:'ft3/s',parameterCode:'00060',statisticId:'00000',approvalStatus:'Provisional',qualifiers:['P'],lastModified:null})),
    source:'https://api.waterdata.usgs.gov/ogcapi/v0/',limitation:'SYNTHETIC TEST FIXTURE; never a provider observation.',truncated:false,interpolation:false,evidenceRole:'EXTERNAL_CONTEXT_ONLY',
  };
}

const origin = new URL(process.env.KFM_NODE_TEST_ORIGIN ?? 'http://127.0.0.1:5182');
assert.equal(origin.protocol, 'http:');
assert.ok(['127.0.0.1', 'localhost', '[::1]'].includes(origin.hostname), 'fixtures must never target a hosted service');
assert.equal(origin.pathname, '/');
assert.equal(origin.search, '');
assert.equal(origin.username + origin.password, '');
const chrome = process.env.KFM_TEST_CHROME ?? 'google-chrome';
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
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

// Uses the actual production page/CSS with loopback-only synthetic observations.
// External provider calls are blocked; these are interaction tests, not data acceptance.
async function pageSession(b, { width, height, touch, motion }) {
  const riverFixture=fixture();
  let riverResponses=0;
  const { targetId } = await b.call('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await b.call('Target.attachToTarget', { targetId, flatten: true });
  const call = (method, params = {}) => b.call(method, params, sessionId);
  const interceptions = createInterceptionErrorTracker();
  b.checks.push(() => interceptions.assertHealthy());
  b.listeners.add(message => {
    if (message.sessionId !== sessionId) return;
    if (message.method === 'Network.loadingFailed') interceptions.loadingFailed(message.params);
    if (message.method === 'Network.requestWillBeSent') interceptions.requestWillBeSent(message.params);
    if (message.method === 'Page.frameNavigated') interceptions.frameNavigated(message.params);
    if (message.method !== 'Fetch.requestPaused') return;
    const { requestId, request, networkId } = message.params, url = new URL(request.url);
    const river = url.pathname === '/api/hydrology/streamflow';
    const operation = url.pathname.startsWith('/api/') && url.pathname !== '/api/build'
      ? call('Fetch.fulfillRequest', { requestId, responseCode: river ? 200 : 503, responseHeaders: [{ name:'Content-Type',value:'application/json' }], body:Buffer.from(JSON.stringify(river ? riverFixture : {error:'Isolated dismissal test: unrelated provider unavailable'})).toString('base64') }).then(result=>{if(river) riverResponses++;return result;})
      : call('Fetch.continueRequest', {requestId});
    void operation
      .catch(error => interceptions.failed(error, { requestNavigation: 0, navigation: 0, networkId, url: request.url }));
  });
  await call('Page.enable');
  await call('Runtime.enable');
  await call('Network.enable');
  await call('Emulation.setDeviceMetricsOverride', {width,height,deviceScaleFactor:1,mobile:touch});
  await call('Emulation.setTouchEmulationEnabled', {enabled:touch});
  await call('Emulation.setEmulatedMedia', {features:[{name:'prefers-reduced-motion',value:motion}]});
  await isolateBrowserNetwork(call, origin);
  const evaluate = async expression => {
    const result = await call('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
    if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
    await interceptions.assertHealthy();
    return result.result.value;
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
    // Native details and scrolling can finish painting after their DOM state.
    // Wait for the same strict hit test that is asserted below; never force a
    // click through a drawer or hide evidence to make an action reachable.
    await wait(
      `(() => { const e=document.querySelector(${JSON.stringify(selector)}),r=e?.getBoundingClientRect();return r && r.width>0 && r.height>0 && e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2)); })()`,
      `painted target ${selector}`,
    );
    const r = await rect(selector), x = r.x + r.width / 2, y = r.y + r.height / 2;
    assert.ok(x > 0 && x < width && y > 0 && y < height, `reachable target ${selector}`);
    assert.ok(await evaluate(`document.querySelector(${JSON.stringify(selector)}).contains(document.elementFromPoint(${x},${y}))`), `unobscured target ${selector} ${JSON.stringify(r)}: ${await evaluate(`JSON.stringify({hit:document.elementFromPoint(${x},${y})?.outerHTML.slice(0,300),panel:document.querySelector('.hydrology-observatory')?.getBoundingClientRect().toJSON(),header:document.querySelector('.hydrology-header')?.getBoundingClientRect().toJSON(),scrollPadding:getComputedStyle(document.querySelector('.hydrology-observatory')??document.body).scrollPaddingTop})`)}`);
    if (touch) {
      await call('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x, y }] });
      await call('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] });
    } else {
      await call('Input.dispatchMouseEvent', { type: 'mousePressed', x, y, button: 'left', clickCount: 1 });
      await call('Input.dispatchMouseEvent', { type: 'mouseReleased', x, y, button: 'left', clickCount: 1 });
    }
  };
  await call('Page.navigate', { url: new URL('?l=&ctx=usgs-streamflow,nws-radar', origin).href });
  await wait(`history.state?.kfmExplorerView && document.querySelector('.map-chrome-dock')`, 'hydration');
  const waitForRiverResponseAfter=async count=>{
    const deadline=Date.now()+15000;
    while(riverResponses<=count && Date.now()<deadline) await pause(25);
    assert.ok(riverResponses>count,'station-change refresh response completed');
    await wait(`document.querySelector('.hydrology-observatory')?.dataset.state==='ready' && document.querySelector('.hydrology-observatory')?.getAttribute('aria-busy')==='false'`, 'station refresh rendered');
    await evaluate('new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))');
  };
  return { call, evaluate, wait, key, rect, activate, riverResponseCount:()=>riverResponses, waitForRiverResponseAfter };
}

for (const layout of [
  {width:320,height:568,touch:true,motion:'no-preference'},
  {width:390,height:844,touch:true,motion:'reduce'},
  {width:568,height:320,touch:true,motion:'no-preference'},
  {width:844,height:390,touch:true,motion:'no-preference'},
  {width:1440,height:900,touch:false,motion:'no-preference'},
]) test(`River Pulse dismissal at ${layout.width}x${layout.height}, ${layout.touch?'touch':'mouse'}, ${layout.motion}`, {timeout:90000}, async t => {
  const b=await browser(t),p=await pageSession(b,layout);
  await p.wait(`document.querySelector('.living-welcome [aria-label="Close quick start"]')`, 'welcome hydrated');
  await p.activate('[aria-label="Close quick start"]');
  await p.wait(`!document.querySelector('.explorer-guide') && document.querySelector('#map-canvas canvas')`, 'map ready');
  const open = async () => {
    if(!await p.evaluate(`document.querySelector('[aria-label="More site actions"]').closest('details').open`)) await p.activate('[aria-label="More site actions"]');
    await p.wait(`document.querySelector('[aria-label="More site actions"]').closest('details').open`, 'More disclosure opened');
    await p.evaluate('new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))');
    await p.activate('.status-header-action');
    await p.wait(`document.querySelector('.repository-overlay')?.hidden===false`, 'status dialog shown');
    await p.evaluate('new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))');
    await p.activate('.status-map-links button:nth-child(2)');
    await p.wait(`document.querySelector('.hydrology-observatory')`, 'River Pulse open');
    // Status is nested in More; close the native popover without hiding River Pulse.
    if(await p.evaluate(`document.querySelector('[aria-label="More site actions"]').closest('details').open`)) await p.activate('[aria-label="More site actions"]');
    // Reopen schedules map-focus restoration; let that action finish before
    // attempting keyboard traversal inside the newly mounted dock.
    await p.evaluate('new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))');
  };
  const snapshot = () => p.evaluate(`JSON.stringify({view:history.state.kfmExplorerView,station:document.querySelector('.hydrology-station-control select')?.value,frame:document.querySelector('.hydrology-clock time')?.dateTime,drawer:document.querySelector('.evidence-drawer')?.innerHTML})`);
  const closeTarget = async () => {
    const r=await p.rect('.hydrology-close');
    assert.ok(r.width>=44 && r.height>=44,'44px dismissal target');
    assert.ok(r.x>=0 && r.y>=0 && r.x+r.width<=layout.width && r.y+r.height<=layout.height,'close fits viewport');
    assert.ok(await p.evaluate(`(()=>{const e=document.querySelector('.hydrology-close'),r=e.getBoundingClientRect();return e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2));})()`),'close is unobscured');
    return r;
  };
  const closed = async () => {
    await p.wait(`!document.querySelector('.hydrology-observatory')`, 'panel dismissed');
    await p.wait(`document.activeElement?.id==='map-canvas' || document.querySelector('#map-canvas')?.contains(document.activeElement)`, 'map focus restored');
  };
  assert.ok(await p.evaluate(`!!document.querySelector('.qwen-header-entry')?.closest('header.topbar')`), 'AI chat has one stable header home');
  assert.equal(await p.evaluate(`document.querySelectorAll('.qwen-map-launch').length`), 0, 'floating chat duplicate is removed');
  assert.ok(await p.evaluate(`!!document.querySelector('.maplibregl-ctrl-attrib')?.closest('.maplibregl-ctrl-top-right')`), 'information belongs to the navigation rail');
  const chatHome = await p.rect('.qwen-header-entry');
  const creditHome = await p.rect('.maplibregl-ctrl-attrib-button');
  await open();
  assert.deepEqual(await p.rect('.qwen-header-entry'), chatHome, 'opening River Pulse never moves chat');
  assert.deepEqual(await p.rect('.maplibregl-ctrl-attrib-button'), creditHome, 'opening River Pulse never moves information');
  await p.wait(`document.querySelector('.hydrology-station-control select').options.length===2`, 'synthetic observation fixture loaded');
  const presentationSnapshot = await snapshot();
  assert.equal(await p.evaluate(`document.querySelector('.river-map-presentation button:first-child').getAttribute('aria-pressed')`), 'true', 'quiet River view is the default');
  await p.activate('.river-map-presentation button:last-child');
  await p.wait(`document.querySelector('.river-map-presentation button:last-child').getAttribute('aria-pressed')==='true'`, 'gauge conditions selected');
  assert.equal(await snapshot(), presentationSnapshot, 'conditions retain camera, station, observation and evidence');
  await p.activate('.river-map-presentation button:first-child');
  assert.equal(await snapshot(), presentationSnapshot, 'River view retains camera, station, observation and evidence');
  // Native selection, exact-frame stepping and keyboard traversal.
  const responsesBeforeSelection=p.riverResponseCount();
  await p.evaluate(`document.querySelector('.hydrology-station-control select').focus()`);
  await p.key('ArrowDown','ArrowDown',40);
  await p.key('Tab','Tab',9);
  await p.wait(`document.querySelector('.hydrology-station-control select').value==='USGS-06864500'`, 'station selected');
  await p.waitForRiverResponseAfter(responsesBeforeSelection);
  await p.activate('[aria-label="Previous exact streamflow frame"]');
  if(!layout.touch) {
    await p.activate('.hydrology-close');await closed();
    await p.activate('#map-canvas canvas');
    await p.wait(`document.querySelector('.evidence-drawer').dataset.open==='true' && document.querySelector('.evidence-drawer').textContent.includes('Synthetic dismissal test gauge')`, 'actual map observation selected in evidence');
    await open();
  }
  const before = await snapshot();
  for (const expanded of [false,true]) {
    if(expanded) await p.activate('.river-expand');
    await p.wait(`document.querySelector('.hydrology-observatory').dataset.expanded===${JSON.stringify(String(expanded))}`, 'panel size');
    // Wheel/touch gestures scroll the actual panel, never the map or document.
    await p.evaluate(`document.querySelector('.hydrology-observatory').scrollTop=0`);
    const r=await p.rect('.hydrology-observatory');
    // Begin in inert padding so a native swipe cannot activate Latest or Play.
    const x=r.x+r.width-4,y=r.y+r.height-8;
    assert.ok(await p.evaluate(`(()=>{const e=document.elementFromPoint(${x},${y});return e?.closest('.hydrology-observatory') && !e.closest('button,input,select,a');})()`),'scroll gesture begins outside interactive controls');
    if(layout.touch) {
      await p.call('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x,y}]});
      for(let i=1;i<=8;i++){await p.call('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x,y:y-i*7}]});await pause(20);}
      await p.call('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
    } else await p.call('Input.dispatchMouseEvent',{type:'mouseWheel',x,y,deltaX:0,deltaY:240});
    await p.wait(`document.querySelector('.hydrology-observatory').scrollTop>10`, 'native panel scrolling');
    let previousScroll=-1;
    for(let i=0;i<30;i++) {
      const next=await p.evaluate(`document.querySelector('.hydrology-observatory').scrollTop`);
      if(i>0 && Math.abs(next-previousScroll)<1) break;
      previousScroll=next;await pause(100);
    }
    // Check the final scroll position too: the sticky header must persist.
    await p.evaluate(`document.querySelector('.hydrology-observatory').scrollTop=100000`);
    await closeTarget();
    const switcher=await p.rect('.hydrology-observatory .live-observation-switcher'),close=await p.rect('.hydrology-close');
    assert.ok(switcher.y+switcher.height<=close.y || switcher.x+switcher.width<=close.x,'sticky source tabs and close never overlap');
    for(const selector of ['.hydrology-observatory .live-observation-switcher button:first-child','.hydrology-observatory .live-observation-switcher button:last-child']) {
      const r=await p.rect(selector);
      assert.ok(r.height>=44,'source switch is a touch-sized target');
      assert.ok(await p.evaluate(`(()=>{const e=document.querySelector(${JSON.stringify(selector)}),r=e.getBoundingClientRect();return e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2));})()`),'source switch remains hit-testable after scrolling');
    }
    assert.equal(await p.evaluate('window.scrollY'),0,'no document scroll');
    assert.equal(await snapshot(),before,'scroll and expansion preserve selection, frame, layers and evidence');
    await p.activate('.hydrology-close');
    await closed();
    await open();
    assert.equal(await snapshot(),before,'reopen preserves selection, frame, layers and evidence');
  }
  await p.activate('.hydrology-observatory .live-observation-switcher button:last-child');
  await p.wait(`document.querySelector('.noaa-radar-loop')`, 'native source switch to radar');
  await p.activate('.noaa-radar-loop .live-observation-switcher button:first-child');
  await p.wait(`document.querySelector('.hydrology-observatory')`, 'native source switch back to River Pulse');
  assert.equal(await snapshot(),before,'source switching retains station, frame, layers and evidence');
  // Playback stops on dismissal and stays stopped after reopen.
  if(layout.motion!=='reduce') {
    await p.activate('.hydrology-play');
    await p.wait(`document.querySelector('.hydrology-observatory').dataset.playing==='true'`, 'playback started');
  }
  await p.evaluate(`document.querySelector('.hydrology-settings select').focus()`);
  await p.key('Escape','Escape',27);
  await closed();
  await open();
  assert.equal(await p.evaluate(`document.querySelector('.hydrology-observatory').dataset.playing`),'false','reopens paused');
  const paused=await snapshot();
  await pause(1100);
  assert.equal(await snapshot(),paused,'dismissed playback never advances retained frame');
  // Close from map focus, then reopen and activate the close button by keyboard.
  await p.evaluate(`document.querySelector('#map-canvas').focus()`);
  await p.key('Escape','Escape',27);
  await closed();
  await open();
  await p.evaluate(`document.querySelector('.hydrology-close').focus()`);
  await p.key('Tab','Tab',9,8);
  await p.key('Tab','Tab',9);
  assert.equal(await p.evaluate(`document.activeElement?.getAttribute('aria-label')`),'Close River Pulse','close is in keyboard order');
  await p.key('Enter','Enter',13);
  await closed();
  t.diagnostic(JSON.stringify(layout));
});

