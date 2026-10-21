// Real, hydrated startup acceptance. Run explicitly against a built loopback
// candidate; this file is deliberately outside the ordinary *.test.mjs suite.
import assert from 'node:assert/strict';
import test from 'node:test';
import { spawn } from 'node:child_process';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { createInterceptionErrorTracker } from './browser-interception.mjs';
import { isolateBrowserNetwork } from './browser-network.mjs';

const origin = new URL(process.env.KFM_NODE_TEST_ORIGIN ?? 'http://127.0.0.1:5182');
assert.equal(origin.protocol, 'http:');
assert.ok(['127.0.0.1', 'localhost', '[::1]'].includes(origin.hostname), 'fixtures must never target a hosted service');
assert.equal(origin.pathname, '/');
assert.equal(origin.search, '');
assert.equal(origin.username + origin.password, '');
const chrome = process.env.KFM_TEST_CHROME ?? 'google-chrome';
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
async function browser(t) {
  const profile = await mkdtemp(join(tmpdir(), 'kfm-guide-browser-'));
  const child = spawn(chrome, [
    '--headless=new', '--remote-debugging-pipe', `--user-data-dir=${profile}`,
    '--no-first-run', '--no-default-browser-check', '--disable-background-networking',
    '--disable-dev-shm-usage', '--enable-unsafe-swiftshader', '--use-angle=swiftshader', 'about:blank',
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

async function pageSession(b, width, height, networkOptions = {}) {
  const { targetId } = await b.call('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await b.call('Target.attachToTarget', { targetId, flatten: true });
  let navigation = 0, holdWelcome = false;
  const heldWelcomeRequests = [];
  const call = (method, params = {}) => {
    if (method === 'Page.navigate' || method === 'Page.reload') navigation++;
    return b.call(method, params, sessionId);
  };
  const interceptions = createInterceptionErrorTracker();
  b.checks.push(() => interceptions.assertHealthy());
  const listener = message => {
    if (message.sessionId !== sessionId) return;
    if (message.method === 'Network.loadingFailed') interceptions.loadingFailed(message.params);
    if (message.method === 'Network.requestWillBeSent') interceptions.requestWillBeSent(message.params);
    if (message.method === 'Page.frameNavigated') interceptions.frameNavigated(message.params);
    if (message.method === 'Page.frameNavigated' && !message.params.frame.parentId) navigation++;
    if (message.method !== 'Fetch.requestPaused') return;
    const requestNavigation = navigation;
    void (async () => {
      const { requestId, request } = message.params, url = new URL(request.url);
      if (holdWelcome && url.origin === origin.origin && /\/assets\/welcome-[^/]+\.js$/.test(url.pathname)) {
        heldWelcomeRequests.push(requestId);
      } else if (url.origin === origin.origin && url.pathname.startsWith('/api/') && url.pathname !== '/api/build') {
        await call('Fetch.fulfillRequest', { requestId, responseCode: 503, responseHeaders: [{ name: 'Content-Type', value: 'application/json' }], body: Buffer.from('{"error":"Isolated navigation test: provider unavailable"}').toString('base64') });
      } else await call('Fetch.continueRequest', { requestId });
    })().catch(error => {
      interceptions.failed(error, {
        requestNavigation, navigation, networkId: message.params.networkId,
        url: message.params.request.url,
      });
    });
  };
  b.listeners.add(listener);
  await call('Page.enable');
  await call('Runtime.enable');
  await call('Network.enable');
  await call('Network.setCacheDisabled', { cacheDisabled: true });
  await call('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: width < 600 });
  await isolateBrowserNetwork(call, origin, networkOptions);
  const evaluate = async expression => {
    await interceptions.assertHealthy();
    const result = await call('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
    if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
    await interceptions.assertHealthy();
    return result.result.value;
  };
  const wait = async (expression, label) => {
    const deadline = Date.now() + 20000;
    while (Date.now() < deadline) {
      await interceptions.assertHealthy();
      if (await evaluate(`Boolean(${expression})`)) return;
      await pause(50);
    }
    throw new Error(`${label}: ${await evaluate(`JSON.stringify({url:location.href, guide:!!document.querySelector('.explorer-guide'), topic:document.querySelector('[aria-label="Layer topic"]')?.value, active:document.activeElement?.outerHTML.slice(0,300), welcome:(()=>{const root=document.querySelector('.explorer-guide.living-welcome'),map=document.querySelector('.map-stage>.map-canvas');return root?{immersive:root.dataset.immersive,scene:root.querySelector('.motion-atlas')?.dataset.focus,mapOpacity:map?getComputedStyle(map).opacity:null,focusedClass:document.activeElement?.className,focusVisible:document.activeElement?.matches(':focus-visible'),cards:[...root.querySelectorAll('.topic-callout')].map(card=>({classes:card.className,opacity:getComputedStyle(card).opacity,focusVisible:card.matches(':focus-visible'),hovered:card.matches(':hover'),pointerEvents:getComputedStyle(card).pointerEvents}))}:null;})()})`)}`);
  };
  const key = async (key, code, windowsVirtualKeyCode, modifiers = 0) => {
    await call('Input.dispatchKeyEvent', { type: 'rawKeyDown', key, code, windowsVirtualKeyCode, modifiers });
    if (key === 'Enter') await call('Input.dispatchKeyEvent', { type: 'char', key, code, windowsVirtualKeyCode, text: '\r' });
    await call('Input.dispatchKeyEvent', { type: 'keyUp', key, code, windowsVirtualKeyCode, modifiers });
  };
  const open = async (path, preference = null, setup = '') => {
    await call('Storage.clearDataForOrigin', { origin: origin.origin, storageTypes: 'local_storage' });
    // Repeated Page.navigate('/') may reload the same history entry. A clean
    // startup must clear its saved view as well as the localStorage preference.
    const { identifier } = await call('Page.addScriptToEvaluateOnNewDocument', { source: `history.replaceState({},''); ${preference === null ? '' : `localStorage.setItem('kfm.explorer.guide.dismissed.v2', ${JSON.stringify(preference)});`} ${setup}` });
    await call('Page.navigate', { url: new URL(path, origin).href });
    await wait(`document.querySelector('.map-chrome-dock') && history.state?.kfmExplorerView`, 'hydrated URL restoration');
    await call('Page.removeScriptToEvaluateOnNewDocument', { identifier });
    await pause(150);
  };
  const unobstructed = async selector => {
    assert.equal(await evaluate(`!!document.querySelector('.explorer-guide')`), false, 'intentional destination must not be covered by welcome');
    await wait(`(() => {const e=document.querySelector(${JSON.stringify(selector)});return e && !e.closest('[inert], [aria-hidden="true"]') && e.getBoundingClientRect().width > 0;})()`, 'destination visible and interactive');
    assert.equal(await evaluate(`localStorage.getItem('kfm.explorer.guide.dismissed.v2')`), null, 'bypass is not permanent dismissal');
    await evaluate(`document.querySelector(${JSON.stringify(selector)}).focus()`);
    await key('Tab', 'Tab', 9);
    assert.equal(await evaluate(`!!document.activeElement?.closest('[inert], [aria-hidden="true"], .explorer-guide')`), false, 'Tab reaches an available control');
  };
  const holdWelcomeModule = () => { holdWelcome = true; };
  const releaseWelcomeModule = async () => {
    assert.ok(heldWelcomeRequests.length, 'the real lazy welcome module was intercepted');
    holdWelcome = false;
    for (const requestId of heldWelcomeRequests.splice(0)) await call('Fetch.continueRequest', { requestId });
  };
  return { call, evaluate, wait, key, open, unobstructed, holdWelcomeModule, releaseWelcomeModule };
}

test('isolated browser leaves canceled assets unpaused while enforcing network and fixture boundaries', {timeout:30000}, async t => {
  const b=await browser(t);
  const {targetId}=await b.call('Target.createTarget',{url:'about:blank'});
  const {sessionId}=await b.call('Target.attachToTarget',{targetId,flatten:true});
  const call=(method,params={})=>b.call(method,params,sessionId);
  const paused=[],blocked=[],errors=[];
  b.listeners.add(message=>{
    if(message.sessionId!==sessionId)return;
    if(message.method==='Network.loadingFailed')blocked.push(message.params);
    if(message.method==='Fetch.requestPaused'){
      paused.push(message.params.request.url);
      void call('Fetch.fulfillRequest',{requestId:message.params.requestId,responseCode:503,body:Buffer.from('isolated').toString('base64')}).catch(error=>errors.push(String(error)));
    }
  });
  await call('Page.enable');await call('Runtime.enable');await call('Network.enable');
  // This standalone network test removes CSP as a confounder. Product
  // acceptance sessions keep their normal CSP and security settings.
  await call('Page.setBypassCSP',{enabled:true});
  await isolateBrowserNetwork(call,origin);
  await call('Page.navigate',{url:new URL('/robots.txt',origin).href});
  const evaluate=async expression=>{
    const result=await call('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true});
    assert.equal(result.exceptionDetails,undefined);return result.result.value;
  };
  const deadline=Date.now()+10000;
  while(!await evaluate(`location.pathname==='/robots.txt' && !!document.body`)){assert.ok(Date.now()<deadline);await pause(10);}
  assert.equal(await evaluate(`fetch('/welcome/motion/roots.jpg').then(r=>{r.body.cancel();return r.ok})`),true,'real local assets remain available');
  await evaluate(`(async()=>{for(let i=0;i<5;i++){const v=document.createElement('video');v.preload='auto';v.src='/welcome/motion/clouds-preview.webm?cancel='+i;document.body.append(v);v.load();await new Promise(r=>setTimeout(r,10));v.removeAttribute('src');v.load();v.remove();}})()`);
  assert.equal(await evaluate(`fetch('/api/browser-isolation-probe').then(r=>r.status)`),503,'provider/API fixtures remain intercepted');
  assert.deepEqual(await evaluate(`fetch('https://tiles.openfreemap.org/styles/liberty').then(r=>r.json()).then(s=>[s.version,Object.keys(s.sources).length,s.layers[0].id])`),[8,0,'test-background']);
  for(const url of ['https://kfm-network-probe.invalid/data','http://kfm-network-probe.invalid/data',new URL('http://127.0.0.1:5184/').href]) {
    assert.equal(await evaluate(`fetch(${JSON.stringify(url)}).then(()=>false,()=>true)`),true,'off-origin requests must fail');
  }
  while(blocked.filter(e=>e.blockedReason==='inspector').length<3 && Date.now()<deadline)await pause(10);
  assert.ok(blocked.filter(e=>e.blockedReason==='inspector').length>=3,`browser blocking, not DNS failure, prevents off-origin I/O: ${JSON.stringify(blocked)}`);
  assert.deepEqual(paused,[new URL('/api/browser-isolation-probe',origin).href],'images/media/styles never acquire a Fetch interception ID');
  assert.deepEqual(errors,[]);
});

for (const [width, height] of [[1366, 768], [390, 844]]) {
  test(`interrupted welcome dismissal at ${width}x${height}`, { timeout: 90000 }, async t => {
    const b = await browser(t), p = await pageSession(b, width, height);
    p.holdWelcomeModule();
    await p.open('/', null, `for (const method of ['getItem','setItem','removeItem']) Object.defineProperty(Storage.prototype,method,{value(){throw new DOMException('Storage blocked','SecurityError')}});`);
    await p.wait(`document.querySelector('.explorer-guide:not(.living-welcome)')?.contains(document.activeElement)`, 'fallback owns keyboard before lazy download');
    await p.key('Escape', 'Escape', 27);
    await p.wait(`!document.querySelector('.explorer-guide') && document.activeElement.matches('.guide-trigger')`, 'fallback dismissal returns focus despite blocked storage');
    await p.releaseWelcomeModule();
    // Reopening must use the loaded component, proving the delayed module has
    // finished without reopening the dismissed guide or stealing its focus.
    await pause(250);
    assert.equal(await p.evaluate(`!document.querySelector('.explorer-guide') && document.activeElement.matches('.guide-trigger')`), true);
    for (let attempt = 0; attempt < 3; attempt++) {
      await p.key('Enter', 'Enter', 13);
      await p.wait(`document.querySelector('.living-welcome')?.contains(document.activeElement)`, 'loaded welcome owns keyboard on each reopen');
      if (attempt > 0) {
        await p.evaluate(`document.querySelector('.living-welcome input[type="checkbox"]').click()`);
        await p.wait(`document.querySelector('.living-welcome input[type="checkbox"]').checked === ${attempt === 1}`, 'explicit opt-out choice remains usable when storage throws');
      }
      await p.key('Escape', 'Escape', 27);
      await p.wait(`!document.querySelector('.explorer-guide') && document.activeElement.matches('.guide-trigger')`, 'loaded dismissal returns focus');
      await p.key('Escape', 'Escape', 27);
      assert.equal(await p.evaluate(`!document.querySelector('.explorer-guide') && document.activeElement.matches('.guide-trigger')`), true, 'repeated Escape cannot reopen welcome');
    }
  });
  test(`startup destinations at ${width}x${height}`, { timeout: 240000 }, async t => {
    const b = await browser(t), p = await pageSession(b, width, height);
    await t.test('Find and Ask retain DOM order and responsive keyboard access before map controls', async () => {
      await p.open('/', '1');
      assert.equal(await p.evaluate(`(() => {
        const header = document.querySelector('header.topbar');
        const find = header?.querySelector('button.atlas-scope-control');
        const ask = header?.querySelector('button.welcome-ai-entry');
        const controls = header?.querySelector('nav.map-chrome-dock');
        return !!(find && ask && controls
          && find.textContent.includes('Find') && ask.textContent.includes('Ask')
          && [find, ask].every(button => !button.disabled && button.tabIndex === 0
            && !button.closest('[inert], [aria-hidden="true"]')
            && (button.compareDocumentPosition(controls) & Node.DOCUMENT_POSITION_FOLLOWING)));
      })()`), true, 'both named buttons remain before map navigation in the DOM');
      await p.evaluate(`document.querySelector('.atlas-scope-control').focus()`);
      assert.equal(await p.evaluate(`document.activeElement.matches('.atlas-scope-control')`), true);
      // The shipped <=560px layout hides the separate Ask button; Find still
      // opens the shared composer. Preserve that responsive design, while
      // requiring Ask's DOM order at both sizes and its Tab order when shown.
      assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('.welcome-ai-entry')).display !== 'none'`), width > 560);
      if (width > 560) {
        await p.key('Tab', 'Tab', 9);
        assert.equal(await p.evaluate(`document.activeElement.matches('.welcome-ai-entry')`), true);
      }
      let reachedMap = false;
      for (let index = 0; index < 20; index++) {
        await p.key('Tab', 'Tab', 9);
        if (await p.evaluate(`!!document.activeElement.closest('.map-chrome-dock')`)) {
          reachedMap = true;
          break;
        }
      }
      assert.equal(reachedMap, true, 'Tab reaches map controls after Find and Ask');
    });
    await t.test('direct topic and restored shared topic URL', async () => {
      for (const url of ['/?topic=engineering', '/?topic=groundwater&layerView=imagery&c=-98.2,38.6&z=7&t=2026']) {
        await p.open(url);
        await p.wait(`document.querySelector('[aria-label="Layer topic"]')?.value === ${JSON.stringify(new URL(url, origin).searchParams.get('topic'))}`, 'requested topic selected');
        await p.unobstructed('[aria-label="Layer topic"]');
      }
    });
    await t.test('catalogue tool destinations', async () => {
      for (const tool of ['measure', 'compare', 'inspect', 'scene', 'history']) {
        await p.open(`/?maptab=${tool}&mapui=open`);
        await p.wait(`document.querySelector('.map-utility-panel[data-open="true"][data-view="${tool}"]')`, 'requested utility restored');
        await p.unobstructed('.map-utility-panel button');
        await p.key('Escape', 'Escape', 27);
        await p.wait(`document.querySelector('.map-utility-panel')?.getAttribute('aria-hidden') === 'true'`, 'Escape closes requested utility');
      }
    });
    await t.test('normal startup, keyboard close/reopen and saved preferences', async () => {
      await p.open('/');
      await p.wait(`document.querySelector('.explorer-guide')?.contains(document.activeElement)`, 'welcome autofocus');
      assert.equal(await p.evaluate(`document.querySelector('.explorer-guide input[type="checkbox"]').checked`), false);
      await p.key('Tab', 'Tab', 9);
      await p.key('Escape', 'Escape', 27);
      await p.wait(`!document.querySelector('.explorer-guide') && document.activeElement?.matches('.guide-trigger')`, 'Escape returns focus to guide trigger');
      await p.key('Enter', 'Enter', 13);
      await p.wait(`document.querySelector('.explorer-guide')?.contains(document.activeElement)`, 'keyboard guide reopen');
      await p.call('Page.reload');
      await p.wait(`document.querySelector('.explorer-guide')?.contains(document.activeElement)`, 'plain reload retains welcome despite saved default camera');
      await p.open('/', '1');
      assert.equal(await p.evaluate(`!!document.querySelector('.explorer-guide')`), false);
      await p.evaluate(`document.querySelector('.guide-trigger').focus()`);
      await p.key('Enter', 'Enter', 13);
      await p.wait(`document.querySelector('.explorer-guide input[type="checkbox"]')?.checked`, 'manual help retains opt-out');
      await p.key('Escape', 'Escape', 27);
      assert.equal(await p.evaluate(`localStorage.getItem('kfm.explorer.guide.dismissed.v2')`), '1');
      await p.open('/', null, `localStorage.setItem('kfm.explorer.guide.dismissed.v1','1');`);
      await p.wait(`document.querySelector('.explorer-guide')`, 'legacy preference does not imply v2 opt-out');
      await p.open('/', null, `Object.defineProperty(Storage.prototype,'getItem',{value(){throw new DOMException('Storage blocked','SecurityError')}});`);
      await p.wait(`document.querySelector('.explorer-guide')?.contains(document.activeElement)`, 'blocked storage preserves a keyboard-ready welcome');
      await p.key('Escape', 'Escape', 27);
      await p.wait(`!document.querySelector('.explorer-guide')`, 'blocked storage still permits dismissal');
    });
    await t.test('shared camera and retained source-status routes bypass without opt-out', async () => {
      for (const url of ['/?c=-98.2,38.6&z=7&t=2026', '/?layers=sources', '/?maptab=localAtlas']) {
        await p.open(url);
        assert.equal(await p.evaluate(`!!document.querySelector('.explorer-guide')`), false, url);
        assert.equal(await p.evaluate(`localStorage.getItem('kfm.explorer.guide.dismissed.v2')`), null);
      }
    });
    await t.test('real Topics link and browser back/forward', async () => {
      await p.call('Storage.clearDataForOrigin', { origin: origin.origin, storageTypes: 'local_storage' });
      await p.call('Page.navigate', { url: new URL('/topics', origin).href });
      await p.wait(`document.querySelector('a[href="/?topic=engineering"]')`, 'Topics catalogue');
      await p.evaluate(`document.querySelector('a[href="/?topic=engineering"]').focus()`);
      await p.key('Enter', 'Enter', 13);
      await p.wait(`document.querySelector('[aria-label="Layer topic"]')?.value === 'engineering'`, 'real catalogue link');
      await p.unobstructed('[aria-label="Layer topic"]');
      await p.evaluate('history.back()');
      await p.wait(`location.pathname === '/topics' && document.querySelector('a[href="/?topic=engineering"]')`, 'back to catalogue');
      await p.evaluate('history.forward()');
      await p.wait(`document.querySelector('[aria-label="Layer topic"]')?.value === 'engineering'`, 'forward restores topic');
      await p.unobstructed('[aria-label="Layer topic"]');
    });
    await t.test('saved history state and popstate close an already-open guide', async () => {
      await p.open('/', null, `history.replaceState({kfmExplorerView:'topic=water'},'');`);
      await p.wait(`document.querySelector('[aria-label="Layer topic"]')?.value === 'water'`, 'saved tab topic');
      await p.unobstructed('[aria-label="Layer topic"]');
      // Two actual entries: Back returns to a saved topic while welcome is open.
      await p.open('/');
      await p.evaluate(`history.replaceState({...history.state,kfmExplorerView:'topic=engineering'},'','/?topic=engineering');history.pushState({},'','/');`);
      await p.evaluate('history.back()');
      await p.wait(`document.querySelector('[aria-label="Layer topic"]')?.value === 'engineering'`, 'popstate topic');
      await p.unobstructed('[aria-label="Layer topic"]');
      await p.evaluate('history.forward()');
      await p.wait(`location.search === ''`, 'forward to plain map');
      assert.equal(await p.evaluate(`!!document.querySelector('.explorer-guide')`), false, 'history does not automatically reopen welcome');
    });
  });
}

// A tall topic panel must not lose its close button behind the mobile header
// or inside its own scroll content. Exercise hit testing, scrolling and focus.
for (const [width, height] of [[390, 844], [320, 568], [844, 390]]) {
  test(`welcome detail close stays reachable at ${width}x${height}`, { timeout: 60000 }, async t => {
    const b = await browser(t), p = await pageSession(b, width, height);
    await p.open('/');
    await p.wait(`document.querySelector('.living-welcome .topic-weather')`, 'visual welcome loaded');
    const closeGeometry = () => p.evaluate(`(() => {
      const button = document.querySelector('.welcome-dialog-close');
      const r = button.getBoundingClientRect();
      return {top:r.top, bottom:r.bottom, left:r.left, right:r.right, width:r.width, height:r.height,
        hit:document.elementFromPoint(r.left+r.width/2,r.top+r.height/2) === button,
        focus:document.activeElement === button};
    })()`);
    for (const selector of ['.topic-weather', '.topic-history', '.welcome-credits button', '.welcome-footer-actions button:first-child']) {
      await p.evaluate(`document.querySelector(${JSON.stringify(selector)}).focus()`);
      await p.key('Enter', 'Enter', 13);
      await p.wait(`document.activeElement?.matches('.welcome-dialog-close')`, 'detail close receives focus');
      const before = await closeGeometry();
      assert.ok(before.top >= 0 && before.bottom <= height && before.left >= 0 && before.right <= width, JSON.stringify(before));
      assert.ok(before.width >= 44 && before.height >= 44, 'close is a full touch target');
      assert.equal(before.hit, true, 'close is above the header and all clip layers');
      assert.equal(await p.evaluate(`document.querySelector('header.topbar').inert`), true, 'modal isolates background controls');
      await p.evaluate(`(() => {const body=document.querySelector('.welcome-dialog-body');body.scrollTop=body.scrollHeight;})()`);
      assert.ok(await p.evaluate(`document.querySelector('.welcome-dialog-body').scrollTop`) > 0, 'long detail actually scrolled');
      assert.deepEqual(await closeGeometry(), before, 'content scroll cannot move or cover close');
      await p.key('Tab', 'Tab', 9, 8);
      assert.equal(await p.evaluate(`!!document.activeElement?.closest('.welcome-dialog-body')`), true, 'Shift+Tab wraps within modal');
      await p.key('Tab', 'Tab', 9);
      assert.equal((await closeGeometry()).focus, true, 'Tab returns to persistent close');
      // Use a real pointer dispatch at the visible button, not DOM click().
      const x=(before.left+before.right)/2, y=(before.top+before.bottom)/2;
      await p.call('Input.dispatchMouseEvent', {type:'mousePressed', x, y, button:'left', clickCount:1});
      await p.call('Input.dispatchMouseEvent', {type:'mouseReleased', x, y, button:'left', clickCount:1});
      await p.wait(`!document.querySelector('.welcome-dialog')`, 'visible close dismisses detail');
      assert.equal(await p.evaluate(`document.activeElement === document.querySelector(${JSON.stringify(selector)})`), true, 'focus returns to opening control');
      assert.equal(await p.evaluate(`document.querySelector('header.topbar').inert`), false, 'background state restored');
    }
    await p.evaluate(`document.querySelector('.topic-weather').focus()`);
    await p.key('Enter', 'Enter', 13);
    await p.wait(`document.activeElement?.matches('.welcome-dialog-close')`, 'detail reopened');
    await p.key('Escape', 'Escape', 27);
    await p.wait(`!document.querySelector('.welcome-dialog') && document.activeElement?.matches('.topic-weather')`, 'Escape closes only detail and restores its trigger');
    await p.key('Escape', 'Escape', 27);
    await p.wait(`!document.querySelector('.explorer-guide') && document.activeElement?.matches('.guide-trigger')`, 'next Escape closes welcome and returns focus to the guide trigger');
  });
}

// Hover acceptance uses an unpressed native mouse move. A drag can start
// selection/HTML drag-and-drop and suppress the very pointer-enter event under
// test. These cases run only in the isolated CI browser fixture above.
for (const [width, height] of [[1440, 960], [1920, 1080], [375, 844]]) {
  test(`welcome topic geometry and real input at ${width}x${height}`, { timeout: 90000 }, async t => {
    const b = await browser(t), p = await pageSession(b, width, height);
    await p.open('/');
    await p.wait(`document.querySelector('.explorer-guide.living-welcome')?.dataset.renderer === 'native' && document.querySelectorAll('.living-welcome .topic-callout').length === 8`, 'all eight hydrated topic cards');
    const bounds = await p.evaluate(`Array.from(document.querySelectorAll('.living-welcome .topic-callout'), button => {
      const r=button.getBoundingClientRect();
      return {id:button.className.split(' ').find(name=>name.startsWith('topic-')&&name!=='topic-callout'),left:r.left,right:r.right,top:r.top,bottom:r.bottom,width:r.width,height:r.height};
    })`);
    assert.equal(bounds.length, 8);
    for (let index = 0; index < bounds.length; index++) {
      const a = bounds[index];
      assert.ok(a.width > 0 && a.height >= 44 && a.left >= 0 && a.right <= width, `visible usable card width: ${JSON.stringify(a)}`);
      if (width > 600) assert.ok(a.top >= 0 && a.bottom <= height, `desktop card stays within viewport: ${JSON.stringify(a)}`);
      for (const b of bounds.slice(index + 1)) {
        const overlapX = Math.min(a.right, b.right) - Math.max(a.left, b.left);
        const overlapY = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
        assert.ok(overlapX <= .5 || overlapY <= .5, `topic hit areas must not overlap: ${JSON.stringify({a,b,overlapX,overlapY})}`);
      }
    }
    const center = selector => p.evaluate(`(() => {const r=document.querySelector(${JSON.stringify(selector)}).getBoundingClientRect();return {x:r.left+r.width/2,y:r.top+r.height/2};})()`);
    const move = async point => p.call('Input.dispatchMouseEvent', {type:'mouseMoved',...point,button:'none',buttons:0});
    const isolated = (topic, retainedFocus = null) => `(() => {
      const root=document.querySelector('.explorer-guide.living-welcome'),active=root?.querySelector('.topic-${topic}');
      const map=document.querySelector('.map-stage > .map-canvas');
      const retained=${retainedFocus ? `root?.querySelector('.topic-${retainedFocus}')` : 'null'};
      const showRetained=retained?.matches(':focus-visible');
      return root?.dataset.immersive === 'true' && active?.classList.contains('is-active')
        && root.querySelector('.motion-atlas')?.dataset.focus === '${topic}'
        && Number(getComputedStyle(active).opacity) >= .98
        && [...root.querySelectorAll('.topic-callout')].filter(card=>card!==active&&!(card===retained&&showRetained)).every(card=>{const o=Number(getComputedStyle(card).opacity);return o>=.3&&o<=.6&&getComputedStyle(card).pointerEvents!=='none';})
        && (!retained || document.activeElement===retained)
        && (!showRetained || Number(getComputedStyle(retained).opacity)>=.98)
        && map && Number(getComputedStyle(map).opacity)<=.02;
    })()`;
    const restored = `(() => {
      const root=document.querySelector('.explorer-guide.living-welcome'),map=document.querySelector('.map-stage > .map-canvas');
      return root?.dataset.immersive === 'false' && [...root.querySelectorAll('.topic-callout')].every(card=>Number(getComputedStyle(card).opacity)>=.98&&getComputedStyle(card).pointerEvents!=='none')
        && map && Number(getComputedStyle(map).opacity)>=.98;
    })()`;
    // Keep keyboard focus outside every card so it cannot conceal a broken
    // pointer listener or legitimately retain a preview after the mouse exits.
    await p.evaluate(`document.querySelector('.welcome-hero input').focus()`);
    if (width > 600) {
      const blank = await center('.welcome-hero input');
      await move(blank);
      await p.wait(restored, 'all topic cards start available');
      await move(await center('.topic-weather'));
      await p.wait(isolated('weather'), 'unpressed weather hover isolates its actual scene and fades the map');
      // Moving directly into a disappearing neighbour must recover that target
      // after release; an invisible hit region must not trap the previous scene.
      await move(await center('.topic-rivers'));
      await p.wait(isolated('rivers'), 'direct pointer switch reaches the next topic');
      await move(await center('.topic-science'));
      await p.wait(isolated('science'), 'a second pointer switch keeps the latest topic');
      await move(blank);
      await p.wait(restored, 'leaving restores all cards and the real map');
      const hitTests = await p.evaluate(`Array.from(document.querySelectorAll('.living-welcome .topic-callout'),card=>{const r=card.getBoundingClientRect();return document.elementFromPoint(r.left+r.width/2,r.top+r.height/2)?.closest('.topic-callout')===card;})`);
      assert.ok(hitTests.every(Boolean), 'restored cards have no hidden hover blockers');
      await move(await center('.topic-weather'));
      await p.wait(isolated('weather'), 'restored topic accepts a later ordinary hover');
      await move(blank);
      await p.wait(restored, 'repeated exit restores the map without a mouse-focus pin');
      // Hybrid input: real keyboard focus remains on Weather while an ordinary
      // mouse move must still reach the other faded card hit areas directly.
      await p.key('Tab', 'Tab', 9);
      await p.evaluate(`document.querySelector('.topic-weather').focus()`);
      await p.wait(isolated('weather'), 'keyboard Weather focus isolates its topic');
      await p.wait(`document.activeElement?.matches('.topic-weather:focus-visible')`, 'Weather retains legitimate keyboard focus');
      await move(await center('.topic-rivers'));
      await p.wait(isolated('rivers', 'weather'), 'mouse reaches River while keyboard focus stays on Weather');
      assert.equal(await p.evaluate(`document.activeElement===document.querySelector('.topic-weather')`),true,'unpressed mouse entry must not steal Weather DOM focus');
      await move(await center('.topic-science'));
      await p.wait(isolated('science', 'weather'), 'next mouse target wins without clearing keyboard focus');
      assert.equal(await p.evaluate(`document.activeElement===document.querySelector('.topic-weather')`),true,'a second unpressed mouse entry retains Weather DOM focus');
      await p.evaluate(`document.querySelector('.welcome-hero input').focus()`);
      await move(blank);
      await p.wait(restored, 'clearing actual keyboard focus and leaving cards restores the entire map');
    } else {
      assert.equal(await p.evaluate(`(()=>{const root=document.querySelector('.explorer-guide.living-welcome');return root.scrollWidth<=root.clientWidth;})()`), true, 'narrow welcome has no horizontal overflow');
      // A narrow touch layout remains directly operable; it need not synthesize
      // a mouse hover before opening a category or finding the persistent X.
      await p.call('Emulation.setTouchEmulationEnabled', {enabled:true,maxTouchPoints:1});
      await p.evaluate(`document.querySelector('.topic-weather').scrollIntoView({block:'center'});`);
      const point = await center('.topic-weather');
      await p.call('Input.dispatchTouchEvent', {type:'touchStart',touchPoints:[{...point,id:1,radiusX:2,radiusY:2,force:1}]});
      await p.call('Input.dispatchTouchEvent', {type:'touchEnd',touchPoints:[]});
      await p.wait(`document.activeElement?.matches('.welcome-dialog-close')`, 'touch opens weather details without a hover prerequisite');
      const close = await p.evaluate(`(()=>{const button=document.querySelector('.welcome-dialog-close'),r=button.getBoundingClientRect();return {x:r.left+r.width/2,y:r.top+r.height/2,top:r.top,bottom:r.bottom,hit:document.elementFromPoint(r.left+r.width/2,r.top+r.height/2)===button};})()`);
      assert.ok(close.top>=0 && close.bottom<=height && close.hit, '375px phone keeps the close target unobstructed');
      await p.call('Input.dispatchTouchEvent', {type:'touchStart',touchPoints:[{x:close.x,y:close.y,id:1,radiusX:2,radiusY:2,force:1}]});
      await p.call('Input.dispatchTouchEvent', {type:'touchEnd',touchPoints:[]});
      await p.wait(`!document.querySelector('.welcome-dialog')`, 'touch closes the topic detail');
    }
  });
}

// Placement is a contract between actual content rectangles, not a snapshot of
// CSS declarations. Include tall/narrow and short layouts plus historical and
// manual controls, whose extra text previously collided with percentage pins.
for (const [width,height,label] of [[1440,960,'desktop'],[1024,1366,'tall tablet'],[901,1200,'narrow desktop'],[768,1024,'tablet'],[1280,720,'short desktop'],[1024,600,'landscape'],[320,568,'narrow phone'],[640,360,'200 percent layout equivalent']]) {
  test(`welcome content stays composed at ${width}x${height} (${label})`,{timeout:60000},async t=>{
    const b=await browser(t),p=await pageSession(b,width,height,{attribution:'Isolated browser layout fixture attribution — empty local test geometry; no provider observations, rights claims or accepted map data.'});
    if(label==='200 percent layout equivalent')await p.call('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:2,mobile:false});
    await p.open('/');await p.wait(`document.querySelector('.explorer-guide.living-welcome')?.dataset.renderer==='native'&&document.querySelectorAll('.living-welcome .topic-callout').length===8&&document.querySelectorAll('.living-welcome .motion-portal').length===8`,'eight hydrated topics with native scene measurements');
    await p.wait(`(()=>{const attribution=document.querySelector('.maplibregl-ctrl-attrib'),r=attribution?.getBoundingClientRect();return r&&r.width>0&&r.height>0;})()`,'real MapLibre attribution mounted from bounded local style fixture');
    const attributionToggle=await p.evaluate(`(()=>{const node=document.querySelector('.maplibregl-ctrl-attrib');if(!node.classList.contains('maplibregl-compact')||node.classList.contains('maplibregl-compact-show'))return null;const r=node.querySelector('.maplibregl-ctrl-attrib-button').getBoundingClientRect();return {x:r.left+r.width/2,y:r.top+r.height/2};})()`);
    if(attributionToggle){
      await p.call('Input.dispatchMouseEvent',{type:'mousePressed',...attributionToggle,button:'left',clickCount:1});
      await p.call('Input.dispatchMouseEvent',{type:'mouseReleased',...attributionToggle,button:'left',clickCount:1});
      await p.wait(`document.querySelector('.maplibregl-ctrl-attrib').classList.contains('maplibregl-compact-show')`,'native attribution disclosure exposes representative wrapping text');
    }
    assert.match(await p.evaluate(`document.querySelector('.maplibregl-ctrl-attrib').textContent`),/Isolated browser layout fixture attribution/,'attribution geometry proves a labeled fixture only, not accepted map data');
    const checkLayout=async state=>{
      await p.wait(`(()=>{const root=document.querySelector('.explorer-guide.living-welcome'),portals=[...root.querySelectorAll('.motion-portal')];return portals.length===8&&portals.filter(portal=>!portal.classList.contains('is-immersive')).every(portal=>{const anchor=root.querySelector('.'+portal.dataset.category+'-scene');if(!anchor)return false;const a=anchor.getBoundingClientRect(),r=portal.getBoundingClientRect();return Math.abs(a.left+a.width/2-r.left-r.width/2)<1&&Math.abs(a.top+a.height/2-r.top-r.height/2)<1;});})()`,state+': native footage follows actual topic anchors');
      const result=await p.evaluate(`(()=>{
        const root=document.querySelector('.explorer-guide.living-welcome'),stage=root.querySelector('.welcome-map-stage');
        const selectors=['.welcome-hero','.welcome-skip','.topic-callout','.scene-caption','.history-timeline','.welcome-credits','.welcome-footer'];
        const boxes=selectors.flatMap(selector=>[...root.querySelectorAll(selector)].map((node,index)=>{const r=node.getBoundingClientRect();return {name:selector+(selector==='.topic-callout'?':'+node.className:index),left:r.left,right:r.right,top:r.top,bottom:r.bottom,width:r.width,height:r.height};}));
        const rootBox=root.getBoundingClientRect(),header=document.querySelector('header.topbar').getBoundingClientRect(),attribution=document.querySelector('.maplibregl-ctrl-attrib')?.getBoundingClientRect();
        const timeline=[...root.querySelectorAll('.history-timeline button')].map(node=>{const r=node.getBoundingClientRect();return {name:node.textContent,left:r.left,right:r.right,top:r.top,bottom:r.bottom,width:r.width,height:r.height};});
        return {boxes,timeline,root:{left:rootBox.left,right:rootBox.right,top:rootBox.top,bottom:rootBox.bottom,scrollWidth:root.scrollWidth,clientWidth:root.clientWidth},headerBottom:header.bottom,attribution:attribution?{left:attribution.left,right:attribution.right,top:attribution.top,bottom:attribution.bottom,width:attribution.width,height:attribution.height}:null,stageHeight:stage.getBoundingClientRect().height,scrollHeight:root.scrollHeight};
      })()`);
      assert.ok(result.root.top>=result.headerBottom-.5,`${state}: header has its own space ${JSON.stringify(result)}`);
      assert.ok(result.root.scrollWidth<=result.root.clientWidth,`${state}: no horizontal overflow`);
      assert.ok(result.attribution?.width>0&&result.attribution?.height>0,`${state}: real attribution has measured geometry`);
      {
        assert.ok(result.attribution.top>=result.root.bottom-.5&&result.attribution.bottom<=height+.5,`${state}: actual attribution occupies a separate viewport strip ${JSON.stringify(result.attribution)}`);
        assert.ok(result.attribution.left>=-.5&&result.attribution.right<=width+.5,`${state}: attribution outer width stays in the viewport`);
      }
      assert.equal(result.boxes.filter(box=>box.name.startsWith('.topic-callout')).length,8);
      for(const box of result.boxes){
        assert.ok(box.width>0&&box.height>0,`${state}: real content box ${JSON.stringify(box)}`);
        assert.ok(box.left>=result.root.left-.5&&box.right<=result.root.right+.5,`${state}: content stays inside scroll width ${JSON.stringify(box)}`);
      }
      const disjoint=boxes=>{
        for(let i=0;i<boxes.length;i++)for(const other of boxes.slice(i+1)){
          const box=boxes[i],x=Math.min(box.right,other.right)-Math.max(box.left,other.left),y=Math.min(box.bottom,other.bottom)-Math.max(box.top,other.top);
          assert.ok(x<=.5||y<=.5,`${state}: distinct content areas do not overlap ${JSON.stringify({box,other,x,y})}`);
        }
      };
      disjoint(result.boxes);disjoint(result.timeline);
      for(const button of result.timeline)assert.ok(button.height>=44,`${state}: historical chapter is a full touch target`);
    };
    await checkLayout('initial');
    if(width===1440&&height===960){
      assert.equal(await p.evaluate(`(()=>{const root=document.querySelector('.explorer-guide.living-welcome'),footer=root.querySelector('.welcome-footer'),r=root.getBoundingClientRect(),f=footer.getBoundingClientRect();return f.top>=r.top&&f.bottom<=r.bottom+.5;})()`),true,'standard desktop shows the complete footer before scrolling');
    }
    assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('header.topbar')).visibility`),'visible','global header remains available');
    assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('.qwen-map-launch')).visibility`),'hidden','background chat chrome does not peek through welcome');
    assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('.maplibregl-ctrl-scale')).visibility`),'hidden','background scale does not peek through welcome');
    // Attribution is not part of the hidden interaction controls.
    assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('.maplibregl-ctrl-attrib')).visibility`),'visible','actual attribution is preserved');
    await p.key('Tab','Tab',9);await p.evaluate(`document.querySelector('.topic-history').focus()`);
    await p.wait(`document.querySelector('.history-timeline')`,'history timeline occupies its own row');await checkLayout('history selected');
    await p.evaluate(`document.querySelector('.history-timeline button:last-child').focus()`);await p.key('Enter','Enter',13);
    await p.wait(`document.querySelector('[aria-label="Resume automatic scene cycling"]')`,'manual history selection retained');
    assert.equal(await p.evaluate(`[...document.querySelectorAll('.scene-caption>button')].some(button=>button.textContent.includes('End preview'))`),true,'pinned preview exposes its exit');
    await checkLayout('history pinned/manual');
    await p.evaluate(`(()=>{const root=document.querySelector('.explorer-guide.living-welcome');root.scrollTop=root.scrollHeight;})()`);
    await p.wait(`(()=>{const root=document.querySelector('.explorer-guide.living-welcome'),button=root.querySelector('.welcome-footer .welcome-primary'),r=button.getBoundingClientRect(),port=root.getBoundingClientRect();return r.top>=port.top&&r.bottom<=port.bottom+.5&&document.elementFromPoint(r.left+r.width/2,r.top+r.height/2)?.closest('.welcome-primary')===button;})()`,'footer exit remains reachable after scrolling the expanded welcome');
    await p.evaluate(`document.querySelector('.welcome-skip').focus()`);await p.key('Enter','Enter',13);
    await p.wait(`!document.querySelector('.explorer-guide.living-welcome')`,'welcome dismissed');
    assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('.qwen-map-launch')).visibility`),'visible','ordinary map interaction chrome is restored');
    assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('.maplibregl-ctrl-scale')).visibility`),'visible','ordinary map scale is restored');
  });
}
