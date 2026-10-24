// Real, hydrated application acceptance. Run explicitly against a built loopback
// candidate; this file is deliberately outside the ordinary *.test.mjs suite.
import assert from 'node:assert/strict';
import test from 'node:test';
import { spawn } from 'node:child_process';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { createInterceptionErrorTracker } from './browser-interception.mjs';

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

// Uses the production page/CSS. Only the aviation availability request reaches
// the loopback server; unrelated APIs are unavailable and external traffic is blocked.
async function pageSession(b, { width, height, touch, motion }) {
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
    const operation = url.origin !== origin.origin
      ? (/\/styles\/|\/style\.json$/.test(url.pathname)
        ? call('Fetch.fulfillRequest', { requestId, responseCode: 200, responseHeaders: [{ name: 'Content-Type', value: 'application/json' }], body: Buffer.from(JSON.stringify({ version: 8, sources: {}, layers: [{ id: 'layout-test-background', type: 'background', paint: { 'background-color': '#172832' } }] })).toString('base64') })
        : call('Fetch.failRequest', { requestId, errorReason: 'BlockedByClient' }))
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
  await call('Page.addScriptToEvaluateOnNewDocument', { source: "localStorage.setItem('kfm.explorer.guide.dismissed.v2','1');" });
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
  await call('Page.navigate', { url: new URL('?l=&ctx=', origin).href });
  await wait(`history.state?.kfmExplorerView && document.querySelector('.map-chrome-dock')`, 'hydration');
  return { call, evaluate, wait, key, rect, activate, visibleFocus };
}

const layouts = [
  { width: 320, height: 568, touch: true, motion: 'no-preference' },
  { width: 390, height: 844, touch: true, motion: 'reduce' },
  { width: 844, height: 390, touch: true, motion: 'reduce' },
  { width: 768, height: 1024, touch: true, motion: 'no-preference' },
  { width: 1024, height: 768, touch: false, motion: 'reduce' },
  { width: 1440, height: 900, touch: false, motion: 'no-preference' },
];
for (const layout of layouts) test(`aviation disclosures remain reachable at ${layout.width}×${layout.height}, ${layout.touch ? 'touch' : 'mouse'}, ${layout.motion}`, { timeout: 90000 }, async t => {
  const b = await browser(t), p = await pageSession(b, layout);
  const explore = '.layer-panel-explore', aviation = '.aviation-control', evidence = '.aviation-control-body > details', scrollHost = layout.height <= 600 ? '.layer-panel' : explore;
  // The compact header keeps Layers in the Map menu. Follow an actually
  // rendered entry, retaining activate()'s scroll, bounds and native hit tests.
  const directLayers = '.map-dock-actions > button:nth-child(2)';
  const mobileLayers = '.map-mobile-actions button:first-child';
  const visible = selector => p.evaluate(`(() => {const e=document.querySelector(${JSON.stringify(selector)}),r=e?.getBoundingClientRect();return !!r&&r.width>0&&r.height>0;})()`);
  if(await visible(directLayers)) await p.activate(directLayers);
  else if(await visible(mobileLayers)) await p.activate(mobileLayers);
  else {
    await p.activate('.map-dock-map-menu > summary');
    await p.activate('.map-dock-menu-quick button:nth-child(2)');
  }
  await p.wait(`document.querySelector('.layer-panel').getAttribute('aria-hidden')==='false'`, 'layers open');
  await p.wait(`(() => { const r=document.querySelector('.layer-panel').getBoundingClientRect(); return r.x>=0 && r.right<=innerWidth+1 && r.bottom<=innerHeight+1; })()`, 'panel animation settled');
  await pause(300);
  const mapBefore = await p.rect('.map-stage'), panelBefore = await p.rect('.layer-panel');
  await p.activate(explore + ' > summary');
  await p.wait(`document.querySelector('${explore}').open`, 'Explore open');
  // Critical structural assertion: no expandable element is treated as a grid tile.
  assert.equal(await p.evaluate(`document.querySelector('${aviation}').closest('nav') === null`), true, 'expandable aviation content stays outside the compact tool grid');
  assert.equal(await p.evaluate(`document.querySelector('${explore} > nav').children.length`), 5);
  assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('${explore} > nav')).gridTemplateColumns.split(' ').length`), 2);
  await p.evaluate(`document.querySelector('${explore} > summary').focus()`);
  for (const label of ['Views','Places','Event Observatory','Kansas historic maps','Map controls','Aviation research']) {
    await p.key('Tab','Tab',9);
    await pause(100);
    const focus=await p.visibleFocus();
    assert.ok(focus.text.includes(label), 'tool traversal order: '+label);
    assert.ok(focus.within && focus.hit && focus.focusVisible, 'tool focus is visible: '+label);
  }
  await p.activate(aviation + ' > summary');
  await p.wait(`document.querySelector('${aviation}').open`, 'aviation open');
  // Native keyboard disclosure activation and tab order must work without hovering.
  await p.evaluate(`document.querySelector('${aviation} > summary').focus()`);
  for (const tag of ['INPUT','SELECT','BUTTON','BUTTON','SUMMARY']) {
    await p.key('Tab','Tab',9);
    await pause(100);
    const focus=await p.visibleFocus();
    assert.equal(focus.tag,tag,'aviation control traversal order');
    assert.ok(focus.within && focus.hit && focus.focusVisible,'aviation control focus is visible: '+tag);
  }
  await p.key('Enter', 'Enter', 13);
  await p.wait(`document.querySelector('${evidence}').open`, 'Evidence & AI open');
  assert.deepEqual(await p.rect('.map-stage'), mapBefore, 'expansion preserves map geometry');
  assert.deepEqual(await p.rect('.layer-panel'), panelBefore, 'expansion preserves panel bounds');
  const geometry = await p.evaluate(`(() => {
    const e=document.querySelector('${scrollHost}'),r=e.getBoundingClientRect(),panel=document.querySelector('.layer-panel').getBoundingClientRect(),map=document.querySelector('.map-stage').getBoundingClientRect();
    return {height:r.height,client:e.clientHeight,scroll:e.scrollHeight,overflow:getComputedStyle(e).overflowY,panelBottom:panel.bottom,panelTop:panel.top,mapWidth:map.width,mapHeight:map.height,screenWidth:document.documentElement.clientWidth,bodyWidth:document.documentElement.scrollWidth};
  })()`);
  assert.equal(geometry.overflow, 'auto');
  assert.ok(geometry.scroll > geometry.client, 'expanded content scrolls within its bounded region');
  assert.ok(geometry.panelTop >= 0 && geometry.panelBottom <= layout.height + 1, 'panel stays in viewport');
  assert.ok(geometry.mapWidth > 250 && geometry.mapHeight > 200, 'map retains its existing workspace');
  assert.equal(geometry.bodyWidth, geometry.screenWidth, 'no horizontal document overflow');
  // Native Tab scrolling must expose the bottom AI action and source link with
  // an actual visible focus ring, not just make their DOM nodes focusable.
  for (const expected of ['BUTTON', 'A']) {
    await p.key('Tab', 'Tab', 9);
    await pause(200);
    const focus = await p.visibleFocus();
    assert.equal(focus.tag, expected);
    assert.ok(focus.within && focus.hit, 'tabbed control is fully visible below the sticky summary: ' + JSON.stringify(focus));
    assert.ok(focus.focusVisible && focus.outline !== 'none' && focus.outlineWidth >= 2, 'visible keyboard outline');
  }
  await p.key('Tab', 'Tab', 9, 8);
  await p.key('Enter', 'Enter', 13);
  await p.wait(`document.querySelector('${aviation} [role=status]').textContent.startsWith('ABSTAIN')`, 'AI remains abstained');
  // Exercise the actual pointer/touch controls and the real, still-held route.
  await p.activate(aviation + ' button');
  await p.wait(`document.querySelector('${aviation} [role=status]').textContent.includes('No reviewed FAA aviation release')`, 'availability stays held');
  await p.activate(aviation + ' button:nth-of-type(2)');
  assert.equal(await p.evaluate(`document.querySelector('${aviation} select').value`), 'present');
  for (const selector of [`${aviation} input`, `${aviation} select`, `${aviation} button`, `${evidence} > summary`, `${evidence} a`, `${explore} > nav > button`]) {
    const r = await p.rect(selector);
    assert.ok(r.height >= 44, '44px touch target: ' + selector);
    assert.ok(r.width > 0 && r.width <= panelBefore.width, 'control fits panel: ' + selector);
  }
  // Scroll gestures stay in Explore rather than moving the page or map camera.
  await p.evaluate(`document.querySelector('${scrollHost}').scrollTop=0`);
  await pause(100);
  const r = await p.rect(scrollHost), x = r.x + 8, y = r.y + Math.min(r.height - 15, 90);
  const camera = await p.evaluate('history.state.kfmExplorerView');
  if (layout.touch) {
    await p.call('Input.dispatchTouchEvent', { type:'touchStart',touchPoints:[{x,y}] });
    for(let step=1;step<=8;step++) { await p.call('Input.dispatchTouchEvent', {type:'touchMove',touchPoints:[{x,y:y-step*8}]}); await pause(25); }
    await p.call('Input.dispatchTouchEvent', {type:'touchEnd',touchPoints:[]});
  } else await p.call('Input.dispatchMouseEvent', { type:'mouseWheel',x,y,deltaX:0,deltaY:160 });
  await p.wait(`document.querySelector('${scrollHost}').scrollTop>20`, 'native scroll gesture');
  assert.equal(await p.evaluate('window.scrollY'), 0);
  assert.equal(await p.evaluate('history.state.kfmExplorerView'), camera, 'panel scroll preserves camera');
  // Let native touch inertia settle before the next tap.
  let lastScroll = -1;
  for (let attempt=0;attempt<30;attempt++) { const next=await p.evaluate(`document.querySelector('${scrollHost}').scrollTop`); if(attempt>0 && Math.abs(next-lastScroll)<1) break; lastScroll=next; await pause(100); }
  await p.activate(evidence + ' > summary');
  await p.wait(`!document.querySelector('${evidence}').open`, 'Evidence collapses by touch/pointer');
  await p.activate(explore + ' > summary');
  await p.wait(`!document.querySelector('${explore}').open`, 'Explore collapses');
  await p.activate('[aria-label="Close Explorer navigation"]');
  await p.wait(`document.querySelector('.layer-panel').getAttribute('aria-hidden')==='true'`, 'panel closes to reveal map');
  if (layout.motion === 'reduce') assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('.layer-panel')).transitionDuration`), '0s');
  t.diagnostic(JSON.stringify({ ...layout, geometry }));
});
