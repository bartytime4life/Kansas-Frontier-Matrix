// Real, hydrated startup acceptance. Run explicitly against a built loopback
// candidate; this file is deliberately outside the ordinary *.test.mjs suite.
import assert from 'node:assert/strict';
import test from 'node:test';
import { spawn } from 'node:child_process';
import { mkdtemp, readFile, rm, mkdir, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { createInterceptionErrorTracker } from './browser-interception.mjs';
import { isolateBrowserNetwork } from './browser-network.mjs';
import { terrainBrowserFixtures } from './terrain-detail-browser-fixtures.mjs';
import ts from 'typescript';
import { capabilityPreviews, capabilityNote, categoryGlimpse } from '../app/living-welcome/capability-catalog.mjs';

// Bind acceptance to the existing navigation contract, not a second tile list.
const taxonomy = {};
new Function('exports', ts.transpileModule(await readFile('app/layer-workspaces.ts', 'utf8'), {
  compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
}).outputText)(taxonomy);
const welcomeTopics = taxonomy.TOPIC_STRUCTURE.map(({ id, title, facets, limitation }) => ({ id, title, facets, limitation }));
assert.equal(welcomeTopics.length, 22, 'the shared taxonomy includes Flora, Fauna and crime, justice & public safety');

async function readyWelcome(p) {
  await p.wait(`document.querySelector('.explorer-guide.living-welcome')?.dataset.renderer === 'capability' && ${JSON.stringify(welcomeTopics.map(topic => '.living-welcome .topic-' + topic.id))}.every(selector=>document.querySelector(selector))`, 'all shared domain cards hydrated');
  const actual = await p.evaluate(`Array.from(document.querySelectorAll('.living-welcome .topic-callout'),card=>({id:[...card.classList].find(name=>name.startsWith('topic-')&&name!=='topic-callout')?.slice(6),title:card.querySelector('strong')?.textContent,facets:card.querySelector('small')?.textContent,label:card.getAttribute('aria-label')}))`);
  assert.deepEqual(actual, welcomeTopics.map(topic => ({ id:topic.id, title:topic.title, facets:topic.facets.join(' · '), label:topic.title+': '+topic.facets.join(' · ') })), 'every shared domain appears once, in order, with its actual facets and accessible name');
  assert.equal(await p.evaluate(`document.querySelectorAll('.living-welcome video,.living-welcome .motion-portal').length`), 0, 'the welcome does not mount retired footage players');
  await p.wait(`[...document.querySelectorAll('.living-welcome .topic-callout')].every(card=>Number(getComputedStyle(card).opacity)>=.98)`, 'card arrival completes before geometry checks');
}

// A category card enters Layers. On compact screens that is a real modal:
// leave through its visible control before operating the background map or
// header, rather than trying to focus an intentionally inert element.
async function leaveCompactLayers(p) {
  if (!await p.evaluate(`!!document.querySelector('[aria-label="Map layers"][aria-modal="true"]')`)) return;
  await p.evaluate(`document.querySelector('[aria-label="Close Explorer navigation"]').focus()`);
  assert.equal(await p.evaluate(`document.activeElement?.getAttribute('aria-label')`), 'Close Explorer navigation', 'the visible Layers close control owns keyboard focus');
  await p.key('Enter', 'Enter', 13);
  await p.wait(`document.querySelector('.layer-panel')?.getAttribute('aria-hidden')==='true' && !!document.querySelector('.guide-trigger') && !document.querySelector('.guide-trigger').closest('[inert], [aria-hidden="true"]')`, 'Layers closes and releases background controls');
  await p.wait(`!!document.activeElement?.closest('#map-canvas')`, 'the completed Layers close handoff restores map focus');
}

async function revealControl(p, selector) {
  await p.evaluate(`document.querySelector(${JSON.stringify(selector)}).scrollIntoView({block:'center',inline:'nearest',behavior:'instant'})`);
  await p.wait(`(()=>{const node=document.querySelector(${JSON.stringify(selector)}),r=node?.getBoundingClientRect(),root=document.querySelector('.explorer-guide.living-welcome')?.getBoundingClientRect();return r&&root&&r.width>0&&r.height>=44&&r.left>=root.left-.5&&r.right<=root.right+.5&&r.top>=root.top-.5&&r.bottom<=root.bottom+.5&&node.contains(document.elementFromPoint(r.left+r.width/2,r.top+r.height/2));})()`, 'real control is visible, full-sized and hit-testable: '+selector);
  return p.evaluate(`(()=>{const r=document.querySelector(${JSON.stringify(selector)}).getBoundingClientRect();return {x:r.left+r.width/2,y:r.top+r.height/2};})()`);
}

// Explicit Preview opens the optional stage; primary cards enter the workspace.
async function openStageNotes(p) {
  await p.wait(`document.querySelector('.living-welcome')?.dataset.cinematic==='true'`, 'category takes the stage');
  const selector='.welcome-layer-demo-actions button:last-child';
  await revealControl(p,selector);
  await p.evaluate(`document.querySelector(${JSON.stringify(selector)}).focus()`);
  await p.key('Enter','Enter',13);
  await p.wait(`document.activeElement?.matches('.welcome-dialog-close')`, 'source notes own focus');
}
async function returnStage(p) {
  await p.evaluate(`document.querySelector('.welcome-preview-expand').focus()`);
  await p.key('Enter','Enter',13);
  await p.wait(`document.querySelector('.living-welcome')?.dataset.cinematic==='false'`, 'category grid restored');
}

const origin = new URL(process.env.KFM_NODE_TEST_ORIGIN ?? 'http://127.0.0.1:5182');
assert.equal(origin.protocol, 'http:');
assert.ok(['127.0.0.1', 'localhost', '[::1]'].includes(origin.hostname), 'fixtures must never target a hosted service');
assert.equal(origin.pathname, '/');
assert.equal(origin.search, '');
assert.equal(origin.username + origin.password, '');
const chrome = process.env.KFM_TEST_CHROME ?? 'google-chrome';
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));

// Native geometry fixture: use the actual stateless dock component and production
// CSS without depending on provider tiles or activating any source.
for (const [width, height] of [[320, 568], [390, 844], [568, 320], [760, 700], [1440, 900]]) {
  test(`category dock controls remain unobscured at ${width}x${height}`, { timeout: 30000 }, async t => {
    const { createRequire } = await import('node:module');
    const { renderToStaticMarkup } = await import('react-dom/server');
    const { createElement } = await import('react');
    const dock = {}, looks = {};
    new Function('exports', 'require', ts.transpileModule(await readFile('app/category-map-dock.tsx', 'utf8'), {
      compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX },
    }).outputText)(dock, createRequire(import.meta.url));
    new Function('exports', ts.transpileModule(await readFile('app/category-maps.ts', 'utf8'), {
      compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
    }).outputText)(looks);
    const css = await readFile('app/globals.css', 'utf8') + await readFile('app/category-map-dock.css', 'utf8');
    const b = await browser(t), { targetId } = await b.call('Target.createTarget', { url: 'about:blank' });
    const { sessionId } = await b.call('Target.attachToTarget', { targetId, flatten: true });
    const call = (method, params = {}) => b.call(method, params, sessionId);
    await call('Page.enable'); await call('Runtime.enable'); await call('Network.enable');
    await call('Network.setBlockedURLs', { urls: ['*'] });
    await call('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: false });
    const evaluate = async expression => {
      const result = await call('Runtime.evaluate', { expression, returnByValue: true });
      if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
      return result.result.value;
    };
    const { frameTree } = await call('Page.getFrameTree');
    for (const topic of ['aviation', 'government']) for (const mode of ['2d', 'terrain', 'globe']) {
      const markup = renderToStaticMarkup(createElement(dock.CategoryMapDock, {
        look: looks.CATEGORY_MAPS[topic], mode, depth: 2.5, azimuth: 235, terrainAvailable: true,
      }));
      const header = height < 500 ? 62 : width < 800 ? 126 : 110;
      await call('Page.setDocumentContent', { frameId: frameTree.frame.id, html: `<!doctype html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>${css}</style></head><body style="margin:0"><main class="map-stage" style="position:relative;margin-top:${header}px;height:calc(100dvh - ${header + 28}px)">${markup}<nav class="map-mobile-actions"><button>Map layers<b>6</b></button><button>Places<b>0</b></button><button>Sources</button><button>Time<b>2026</b></button><button>Style</button></nav></main></body></html>` });
      const selectors = ['.category-map-dock-close', ...[1, 2, 3].map(n => `.category-map-dock-modes button:nth-child(${n})`), ...[1, 2].map(n => `.category-map-dock-actions button:nth-child(${n})`)];
      if (mode !== 'globe') selectors.push('.category-map-dock-range input');
      for (const selector of selectors) {
        await evaluate(`document.querySelector(${JSON.stringify(selector)}).scrollIntoView({block:'nearest',inline:'nearest',behavior:'instant'})`);
        const at = await evaluate(`(() => {const e=document.querySelector(${JSON.stringify(selector)}),r=e.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2,hit:e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2)),body:document.documentElement.scrollWidth};})()`);
        assert.ok(at.x > 0 && at.x < width && at.y > 0 && at.y < height, `${topic} ${mode}: ${selector} in viewport`);
        assert.ok(at.hit, `${topic} ${mode}: ${selector} is not covered by map navigation`);
        assert.ok(at.body <= width + 1, 'no document horizontal overflow');
      }
    }
  });
}

test('category evidence summary keeps source qualifications readable on its paper card', { timeout: 30000 }, async t => {
  const b = await browser(t), { targetId } = await b.call('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await b.call('Target.attachToTarget', { targetId, flatten: true });
  const call = (method, params = {}) => b.call(method, params, sessionId);
  await call('Page.enable'); await call('Runtime.enable'); await call('Network.enable');
  await call('Network.setBlockedURLs', { urls: ['*'] });
  const { frameTree } = await call('Page.getFrameTree');
  const globals = await readFile('app/globals.css', 'utf8'), paper = await readFile('app/research.module.css', 'utf8'), facts = await readFile('app/evidence-summary.css', 'utf8');
  const luminance = color => color.match(/[\d.]+/g).slice(0, 3).map(Number).map(v => v / 255).map(v => v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4).reduce((sum, v, i) => sum + v * [.2126, .7152, .0722][i], 0);
  for (const css of [globals + paper + facts, globals + facts + paper]) {
    await call('Page.setDocumentContent', { frameId: frameTree.frame.id, html: `<!doctype html><html><head><style>${css}</style></head><body><section class="summary"><h3>Selected record</h3><dl class="drawer-facts"><div><dt>Source &amp; limits</dt><dd><strong>U.S. Census Bureau</strong> · External context only · no KFM EvidenceBundle<p>Dated source context. Missing coverage does not establish clearance.</p></dd></div></dl></section></body></html>` });
    const result = await call('Runtime.evaluate', { expression: `({background:getComputedStyle(document.querySelector('.summary')).backgroundColor,colors:[...document.querySelectorAll('.drawer-facts dt,.drawer-facts dd,.drawer-facts dd strong,.drawer-facts dd p')].map(e=>getComputedStyle(e).color)})`, returnByValue: true });
    assert.equal(result.exceptionDetails, undefined);
    const { background, colors } = result.result.value;
    for (const color of colors) {
      const a = luminance(color), c = luminance(background), contrast = (Math.max(a, c) + .05) / (Math.min(a, c) + .05);
      assert.ok(contrast >= 4.5, `${color} on ${background}: contrast ${contrast.toFixed(2)} must be at least 4.5`);
    }
  }
});

// CI renders WebGL in SwiftShader, where each welcome map style switch compiles its
// shaders synchronously and holds the page's main thread for 2-5 s. The desktop
// journey switches through every domain, so a call can queue behind two or
// three switches; the test's own timeout still bounds the whole journey.
const CDP_CALL_TIMEOUT_MS = 60000;

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
    const timer = setTimeout(() => { pending.delete(id); reject(new Error(`CDP timeout: ${method} ${String(params.expression ?? '').slice(0, 240)}; ${stderr}`)); }, CDP_CALL_TIMEOUT_MS);
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
  let navigation = 0, holdScene = false;
  const heldSceneRequests = [];
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
      if (await networkOptions.intercept?.(message.params, call)) return;
      if (holdScene && url.origin === origin.origin && /\/assets\/map-engine-[^/]+\.js$/.test(url.pathname)) {
        heldSceneRequests.push(requestId);
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
  await (networkOptions.isolate ?? isolateBrowserNetwork)(call, origin, networkOptions);
  await networkOptions.setup?.(call);
  const evaluate = async expression => {
    await interceptions.assertHealthy();
    const result = await call('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
    if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
    await interceptions.assertHealthy();
    return result.result.value;
  };
  const wait = async (expression, label) => {
    const deadline = Date.now() + (networkOptions.waitTimeoutMs ?? 20000);
    while (Date.now() < deadline) {
      await interceptions.assertHealthy();
      if (await evaluate(`Boolean(${expression})`)) return;
      await pause(50);
    }
    throw new Error(`${label}: ${await evaluate(`JSON.stringify({url:location.href, guide:!!document.querySelector('.explorer-guide'), topic:document.querySelector('[aria-label="Layer topic"]')?.value, active:document.activeElement?.outerHTML.slice(0,300), welcome:(()=>{const root=document.querySelector('.explorer-guide.living-welcome'),map=document.querySelector('.map-stage>.map-canvas');return root?{renderer:root.dataset.renderer,immersive:root.dataset.immersive,scene:root.querySelector('.domain-stage')?.dataset.topic,mapOpacity:map?getComputedStyle(map).opacity:null,focusedClass:document.activeElement?.className,focusVisible:document.activeElement?.matches(':focus-visible'),cards:[...root.querySelectorAll('.topic-callout')].map(card=>({classes:card.className,opacity:getComputedStyle(card).opacity,focusVisible:card.matches(':focus-visible'),hovered:card.matches(':hover'),pointerEvents:getComputedStyle(card).pointerEvents}))}:null;})()})`)}`);
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
  const holdSceneModule = () => { holdScene = true; };
  const waitForSceneModule = async () => {
    const deadline = Date.now() + 20000;
    while (!heldSceneRequests.length && Date.now() < deadline) await pause(25);
    assert.ok(heldSceneRequests.length, 'scene request starts while the welcome is usable');
  };
  const releaseSceneModule = async () => {
    assert.ok(heldSceneRequests.length, 'the real lazy welcome map engine was intercepted');
    holdScene = false;
    for (const requestId of heldSceneRequests.splice(0)) await call('Fetch.continueRequest', { requestId });
  };
  return { call, evaluate, wait, key, open, unobstructed, holdSceneModule, waitForSceneModule, releaseSceneModule };
}

for (const [width, height] of [[2732, 1463], [1280, 800], [829, 823], [390, 844], [320, 568]]) {
  test(`welcome glimpse stays visible and wheel scrolling chains at ${width}x${height}`, { timeout: 90000 }, async t => {
    const b = await browser(t), p = await pageSession(b, width, height);
    await p.open('/?motion=off'); await readyWelcome(p);
    await p.evaluate(`document.querySelector('.topic-aviation').focus()`);
    await p.wait(`document.querySelector('.welcome-preview-brief h2')?.textContent===${JSON.stringify(categoryGlimpse('aviation').title)}`, 'focused category owns the glimpse');
    await p.wait(`document.querySelector('.domain-stage')?.dataset.state!=='loading'`, 'the real fixed backdrop has settled');
    const read = () => p.evaluate(`(() => {
      const root=document.querySelector('.living-welcome'), brief=root.querySelector('.welcome-preview-brief'), r=root.getBoundingClientRect(), a=brief.getBoundingClientRect();
      return { top:root.scrollTop,max:root.scrollHeight-root.clientHeight,brief:{top:a.top,bottom:a.bottom,left:a.left,right:a.right},root:{top:r.top,bottom:r.bottom},inside:brief.scrollHeight-brief.clientHeight,overflow:document.documentElement.scrollWidth>innerWidth+1 };
    })()`);
    // Setup reaches the same lower part of the chooser as normal scrolling;
    // acceptance below uses trusted wheel input, not a scripted scroll substitute.
    await p.evaluate(`(()=>{const root=document.querySelector('.living-welcome');root.scrollTop=(root.scrollHeight-root.clientHeight)*.6;})()`);
    let state=await read();
    assert.ok(state.max>50, 'the category list has a real scroll range');
    assert.equal(state.overflow,false);
    assert.ok(state.brief.top>=state.root.top-1 && state.brief.bottom<=state.root.bottom+1, 'Inside this map remains visible after scrolling through categories');
    const wheel=async (x,y,deltaY) => p.call('Input.dispatchMouseEvent',{type:'mouseWheel',x,y,deltaX:0,deltaY});
    const x=Math.min(width-24,state.brief.right-20), y=Math.min(state.root.bottom-30,state.brief.bottom+36);
    const before=state.top;
    await wheel(x,y,-180);
    await p.wait(`document.querySelector('.living-welcome').scrollTop<${before-20}`, 'exposed map below the box scrolls back up');

    // A long Aviation brief scrolls internally, then hands the gesture to the
    // chooser at either boundary rather than trapping the visitor there.
    await p.evaluate(`(()=>{const root=document.querySelector('.living-welcome'),brief=root.querySelector('.welcome-preview-brief');root.scrollTop=(root.scrollHeight-root.clientHeight)*.5;brief.scrollTop=brief.scrollHeight;})()`);
    state=await read();
    assert.ok(state.inside>0, 'the long source brief exercises nested scrolling');
    const boxX=state.brief.left+(state.brief.right-state.brief.left)*.5,boxY=state.brief.top+36;
    await wheel(boxX,boxY,140);
    await p.wait(`document.querySelector('.living-welcome').scrollTop>${state.top+20}`, 'brief end hands downward scrolling to the chooser');
    await p.evaluate(`document.querySelector('.welcome-preview-brief').scrollTop=0`);
    state=await read();
    await wheel(boxX,Math.max(state.root.top+20,state.brief.top+36),-140);
    await p.wait(`document.querySelector('.living-welcome').scrollTop<${state.top-20}`, 'brief start hands upward scrolling to the chooser');
    await p.evaluate(`(()=>{const root=document.querySelector('.living-welcome');root.scrollTop=root.scrollHeight;})()`);
    state=await read();
    assert.ok(state.brief.top>=state.root.top-1 && state.brief.bottom<=state.root.bottom+1, 'the last categories do not lose their context panel');

    if(process.env.KFM_WORKSPACE_SCREENSHOTS){
      await mkdir(process.env.KFM_WORKSPACE_SCREENSHOTS,{recursive:true});
      const capture=await p.call('Page.captureScreenshot',{format:'png'});
      await writeFile(join(process.env.KFM_WORKSPACE_SCREENSHOTS,`welcome-scroll-${width}x${height}.png`),Buffer.from(capture.data,'base64'));
    }
  });
}

for (const [width, height] of [[1280, 800], [390, 844]]) {
  test(`welcome cards enter editable map layers directly at ${width}x${height}`, { timeout: 90000 }, async t => {
    const b = await browser(t), p = await pageSession(b, width, height);
    await p.open('/?motion=off'); await readyWelcome(p);
    for (const topic of ['aviation', 'geology']) {
      const selector = '.topic-' + topic;
      let point = await revealControl(p, selector);
      if (width > 600) {
        await p.call('Input.dispatchMouseEvent', { type: 'mouseMoved', ...point, button: 'none', buttons: 0 });
        await pause(850);
        assert.equal(await p.evaluate(`document.querySelector('.living-welcome').dataset.cinematic`), 'false', 'hover keeps the chooser available');
        // A glimpse may lift the card slightly, but it must not reflow another target under the pointer.
        const under = await p.evaluate(`(()=>{const hit=document.elementFromPoint(${point.x},${point.y});return hit?.closest('.topic-callout')===document.querySelector(${JSON.stringify(selector)})?'card':String(hit?.closest('button')?.className||hit?.className);})()`);
        assert.equal(under, 'card', `a ${topic} hover glimpse leaves its card under the pointer`);
        // Revalidate the intended hit target after the deliberately slow hover;
        // the welcome may have scrolled/reflowed since its first coordinate read.
        point = await revealControl(p, selector);
        await p.call('Input.dispatchMouseEvent', { type: 'mousePressed', ...point, button: 'left', clickCount: 1 });
        await p.call('Input.dispatchMouseEvent', { type: 'mouseReleased', ...point, button: 'left', clickCount: 1 });
      } else {
        await p.call('Emulation.setTouchEmulationEnabled', { enabled: true, maxTouchPoints: 1 });
        await p.call('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ ...point, id: 1, radiusX: 2, radiusY: 2, force: 1 }] });
        await p.call('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] });
      }
      await p.wait(`!document.querySelector('.living-welcome') && document.querySelector('[aria-label="Layer topic"]')?.value==='${topic}' && document.activeElement?.closest('[aria-label="Map layers"]')`, 'one activation opens the selected workspace and focuses Layers');
      const workspace = await p.evaluate(`(() => { const topic = document.querySelector('[aria-label="Layer topic"]'), panel = topic.closest('aside'), input = panel?.querySelector('input[aria-label="Search map layers"]'); return { inert: !!topic.closest('[inert], [aria-hidden="true"]'), search: !!input && input.getBoundingClientRect().width > 0, dock: !!document.querySelector('.category-map-dock'), overflow: document.documentElement.scrollWidth > innerWidth + 1 }; })()`);
      assert.deepEqual(workspace, { inert: false, search: true, dock: true, overflow: false }, 'real controls are available without another preview step');
      // On compact screens Layers is modal, so leave it through its own control.
      // Desktop keeps the panel open; both retain the panel for the next choice.
      await leaveCompactLayers(p);
      await p.evaluate(`document.querySelector('.guide-trigger').focus()`);
      await p.key('Enter', 'Enter', 13); await readyWelcome(p);
    }
  });
}

for (const width of [320, 390, 768, 1280]) {
  test(`Sky daylight keyboard selection and readable chart at ${width}px`, { timeout: 90000 }, async t => {
    const b = await browser(t), p = await pageSession(b, width, 844);
    await p.call('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
    await p.open('/?motion=off'); await readyWelcome(p);
    const enter = async selector => { await revealControl(p, selector); await p.evaluate(`document.querySelector(${JSON.stringify(selector)}).focus()`); await p.key('Enter', 'Enter', 13); };
    await enter('.topic-preview-sky'); await openStageNotes(p);
    await p.wait(`!!document.querySelector('.welcome-open-map')`, 'Sky map action');
    await enter('.welcome-open-map');
    await p.wait(`!document.querySelector('.living-welcome') && document.querySelector('.category-map-dock header strong')?.textContent==='Sky globe'`, 'real Sky workspace');
    await leaveCompactLayers(p);
    await p.evaluate(`[...document.querySelectorAll('.category-map-dock-tool')].find(b=>b.textContent==='Daylight through the year').focus()`);
    await p.key('Enter', 'Enter', 13);
    await p.wait(`!!document.querySelector('.category-map-dock-sun-location') && !!document.querySelector('[data-band="day"]')`, 'daylight chart');
    const location = async (lat, lon) => {
      await p.evaluate(`document.querySelector('.category-map-dock-sun-location input[name="latitude"]').focus()`);
      await p.key('a', 'KeyA', 65, 2); await p.call('Input.insertText', { text: String(lat) });
      await p.key('Tab', 'Tab', 9);
      assert.equal(await p.evaluate(`document.activeElement.name`), 'longitude');
      await p.key('a', 'KeyA', 65, 2); await p.call('Input.insertText', { text: String(lon) });
      await p.key('Tab', 'Tab', 9);
      assert.equal(await p.evaluate(`document.activeElement.textContent`), 'Chart location');
      await p.key('Enter', 'Enter', 13);
    };
    await location(39.35, -101.71); // Goodland: Mountain local time, explicitly displayed as Central here.
    await p.wait(`document.querySelector('.category-map-dock').textContent.includes('At 39.35°N, 101.71°W')`, 'keyboard-selected Kansas location');
    assert.equal(await p.evaluate(`document.querySelector('.category-map-dock').textContent.includes('All Sun and Moon times use Central time (CDT/CST)')`), true);
    assert.equal(await p.evaluate(`document.querySelector('.category-map-dock').textContent.includes('Mountain clocks read one hour earlier')`), true);
    const before = await p.evaluate(`document.querySelector('[data-band="day"]').getAttribute('d')`);
    await location(39.95, -94.85); // Inside the old rectangle, across the Missouri River from Kansas.
    await p.wait(`document.querySelector('.category-map-dock').textContent.includes('choose coordinates or click inside the state')`, 'outside selection message');
    assert.equal(await p.evaluate(`document.querySelector('[data-band="day"]').getAttribute('d')`), before, 'outside selection preserves the chart');
    const geometry = await p.evaluate(`(() => {const form=document.querySelector('.category-map-dock-sun-location'),figure=document.querySelector('.category-map-dock-hydrograph');return {overflow:document.documentElement.scrollWidth>innerWidth+1,chart:figure.getBoundingClientRect().width,background:getComputedStyle(document.querySelector('.category-map-dock')).backgroundColor,controls:[...form.querySelectorAll('input,button')].map(e=>({w:e.getBoundingClientRect().width,h:e.getBoundingClientRect().height})),legend:[...figure.querySelectorAll('.category-map-dock-fema-families span')].map(e=>({text:e.textContent,color:getComputedStyle(e).color,width:e.getBoundingClientRect().width}))};})()`);
    assert.equal(geometry.overflow, false); assert.ok(geometry.chart > 150 && geometry.chart <= width);
    assert.ok(geometry.controls.every(r=>r.w>30 && r.h>=32));
    assert.deepEqual(geometry.legend.map(e=>e.text), ['Day','Civil twilight','Nautical','Astronomical','Night']);
    const luminance = color => color.match(/[\d.]+/g).slice(0,3).map(Number).map(v=>v/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((sum,v,i)=>sum+v*[.2126,.7152,.0722][i],0);
    const [red,green,blue,alpha=1]=geometry.background.match(/[\d.]+/g).map(Number);
    const background=luminance(`rgb(${[red,green,blue].map(v=>v*alpha+255*(1-alpha)).join(',')})`);
    assert.ok(geometry.legend.every(e=>(luminance(e.color)+.05)/(background+.05)>=4.5), 'legend uses light text, independently of its dark color chips');
    await p.evaluate(`document.querySelector('.category-map-dock-hydrograph').scrollIntoView({block:'center'})`);
    if (process.env.KFM_WORKSPACE_SCREENSHOTS) {
      await mkdir(process.env.KFM_WORKSPACE_SCREENSHOTS, { recursive: true });
      const shot=await p.call('Page.captureScreenshot', { format:'png' });
      await writeFile(join(process.env.KFM_WORKSPACE_SCREENSHOTS, `sky-daylight-${width}.png`), Buffer.from(shot.data,'base64'));
    }
    await p.evaluate(`[...document.querySelectorAll('.category-map-dock button')].find(b=>b.textContent==='Back to the centre of Kansas').focus()`);
    await p.key('Enter','Enter',13);
    await p.wait(`document.querySelector('.category-map-dock').textContent.includes('At the geographic centre of Kansas, Barton County')`, 'keyboard reset');
    await p.evaluate(`[...document.querySelectorAll('.category-map-dock-tool')].find(b=>b.textContent==='Hide daylight through the year').focus()`);
    await p.key('Enter','Enter',13);
    await p.wait(`!document.querySelector('[data-band="day"]')`, 'keyboard hides the chart');
  });
}

for (const width of [1280, 390]) {
  test(`terrain detail automatic fallback and ready recovery at ${width}px (synthetic DEM transport)`, { timeout: 150000 }, async t => {
    const fixtures = await terrainBrowserFixtures(origin);
    const b = await browser(t), p = await pageSession(b, width, 844, fixtures);
    await p.open('/?base=midnight&scene=elevation-3d&c=-98,38.5&z=10.5&p=58&motion=off&panel=scene');
    const ready = provider => `document.querySelector('.terrain-mode-source')?.textContent.includes('${provider} · DEM ready') && document.querySelector('.screenreader-status')?.textContent.includes('interactions proven') && !document.querySelector('.runtime-degraded-banner')`;
    await p.wait(ready('Mapzen'), 'initial Mapzen surface and runtime are ready');
    assert.equal(fixtures.hits.usgs, 0, 'regional view retains Mapzen');
    await p.evaluate(`void window.__terrainAcceptanceMap.jumpTo({zoom:12})`);
    await p.wait(ready('Mapzen'), 'automatic 3DEP outage recovers to Mapzen and runtime ready');
    await p.wait(`window.__terrainAcceptanceAnnouncements?.some(text=>text.includes('did not load'))`, 'fallback announcement');
    assert.ok(fixtures.hits.usgs > 0, 'real 3DEP requests hit the failed transport');
    assert.ok(fixtures.hits.mapzen > 0 && fixtures.hits.instrumented > 0);
    await p.evaluate(`void window.__terrainAcceptanceMap.fire('error',{sourceId:'kfm-terrain-dem',source:{type:'raster-dem',tiles:['/api/3dep-dem-tile?v=2&z={z}&x={x}&y={y}']},error:new Error('Synthetic late 3DEP failure')})`);
    await p.evaluate(`void window.__terrainAcceptanceMap.triggerRepaint()`);
    await p.wait(ready('Mapzen'), 'late replaced-source failure leaves runtime ready');
    const surface = await p.evaluate(`(()=>{const m=window.__terrainAcceptanceMap;return {source:m.getTerrain()?.source,elevation:m.queryTerrainElevation(m.getCenter()),pitch:m.getPitch(),attribution:document.querySelector('.maplibregl-ctrl-attrib')?.textContent,status:document.querySelector('.terrain-mode-source')?.textContent};})()`);
    assert.equal(surface.source, 'kfm-terrain-dem'); assert.ok(surface.elevation > 0 && Number.isFinite(surface.elevation), 'loaded elevation still drives the real terrain mesh');
    assert.ok(surface.pitch > 40); assert.match(surface.attribution, /Mapzen/); assert.doesNotMatch(surface.attribution, /dynamic DEM mosaic/);
    assert.match(surface.status, /coarse beyond z11/);
    const before = await p.evaluate(`window.__terrainAcceptanceMap.getCenter().lng`);
    await p.evaluate(`window.__terrainAcceptanceMap.getCanvas().focus()`); await p.key('ArrowRight', 'ArrowRight', 39);
    await p.wait(`window.__terrainAcceptanceMap.getCenter().lng !== ${before} && !window.__terrainAcceptanceMap.isMoving()`, 'keyboard pan still works in 3D');
    await p.key('ArrowRight', 'ArrowRight', 39, 8);
    await p.wait(`Math.abs(window.__terrainAcceptanceMap.getBearing())>1 && !window.__terrainAcceptanceMap.isMoving()`, 'keyboard 3D rotation still works');
    await p.wait(ready('Mapzen'), 'navigation settles back to ready');
    if (process.env.KFM_WORKSPACE_SCREENSHOTS) {
      await mkdir(process.env.KFM_WORKSPACE_SCREENSHOTS, { recursive: true });
      const capture = await p.call('Page.captureScreenshot', { format: 'png' });
      await writeFile(join(process.env.KFM_WORKSPACE_SCREENSHOTS, `terrain-fallback-${width}.png`), Buffer.from(capture.data, 'base64'));
    }
    t.diagnostic(JSON.stringify({ transport: 'synthetic elevations; no provider I/O', hits: fixtures.hits, surface }));
  });
}

test('terrain detail successful 3DEP and manual provider recovery (synthetic DEM transport)', { timeout: 150000 }, async t => {
  const fixtures = await terrainBrowserFixtures(origin, { fail3dep: false });
  const b = await browser(t), p = await pageSession(b, 1280, 844, fixtures);
  await p.open('/?base=midnight&scene=elevation-3d&c=-98,38.5&z=12&p=58&motion=off&panel=scene');
  const ready = provider => `document.querySelector('.terrain-mode-source')?.textContent.includes('${provider} · DEM ready') && document.querySelector('.screenreader-status')?.textContent.includes('interactions proven') && !document.querySelector('.runtime-degraded-banner')`;
  await p.wait(ready('USGS 3DEP'), 'automatic successful 3DEP is runtime ready');
  assert.match(await p.evaluate(`document.querySelector('.maplibregl-ctrl-attrib').textContent`), /3D Elevation Program/);
  const choose = async provider => p.evaluate(`(()=>{const e=document.querySelector('[aria-label="Terrain elevation source"]');e.value=${JSON.stringify(provider)};e.dispatchEvent(new Event('change',{bubbles:true}));})()`);
  await choose('mapzen'); await p.wait(ready('Mapzen'), 'manual Mapzen choice is ready');
  const requests = fixtures.hits.usgs;
  await p.evaluate(`void window.__terrainAcceptanceMap.jumpTo({zoom:13})`);
  await p.wait(ready('Mapzen'), 'manual choice remains Mapzen past threshold');
  assert.equal(fixtures.hits.usgs, requests, 'manual selection disables automatic detail');
  fixtures.fail3dep(true); await choose('usgs-3dep');
  await p.wait(`document.querySelector('.terrain-mode-source')?.textContent.includes('USGS 3DEP · DEM unavailable') && !!document.querySelector('.runtime-degraded-banner')`, 'genuine manual provider failure remains visible');
  await p.evaluate(`[...document.querySelectorAll('button')].find(e=>e.textContent==='Use display DEM').click()`);
  await p.wait(ready('Mapzen'), 'explicit display DEM action restores terrain and runtime');
  assert.match(await p.evaluate(`document.querySelector('.maplibregl-ctrl-attrib').textContent`), /Mapzen/);
});

// Exercise actual DomainStage failures, rather than injecting React state.
// Provider I/O remains isolated by pageSession; these are UI acceptance checks.
for (const [width,height] of [[1280,800],[390,844],[568,320]]) {
  test(`expanded welcome failure and recovery at ${width}x${height}`,{timeout:150000},async t=>{
    const b=await browser(t),p=await pageSession(b,width,height);
    const activate=async selector=>{
      await revealControl(p,selector);
      await p.evaluate(`document.querySelector(${JSON.stringify(selector)}).focus()`);
      await p.key('Enter','Enter',13);
    };
    const expand=async id=>{
      await activate('.topic-preview-'+id); await openStageNotes(p);
      await p.wait(`document.activeElement?.matches('.welcome-dialog-close')`,'category detail owns focus');
      await activate('.welcome-dialog-body>.welcome-preview-action');
      await p.wait(`document.querySelector('.living-welcome')?.dataset.fullscreen==='true'&&document.activeElement?.matches('.welcome-preview-expand')`,'expanded category returns focus to Return');
    };
    for(const failure of ['webgl','construction']){
      await p.open('/',null,`(() => {
        window.__kfmPreviewFault=${JSON.stringify(failure)};window.__kfmPreviewFaultHits=0;
        const original=HTMLCanvasElement.prototype.getContext;
        HTMLCanvasElement.prototype.getContext=function(type,...args){
          if(/^webgl/.test(type)&&window.__kfmPreviewFault==='webgl'){window.__kfmPreviewFaultHits++;return null;}
          if(/^webgl/.test(type)&&window.__kfmPreviewFault==='construction'&&this.closest('.domain-stage')){window.__kfmPreviewFaultHits++;throw new Error('Isolated preview construction failure');}
          return original.call(this,type,...args);
        };
      })();`);
      await readyWelcome(p);
      await p.wait(`document.querySelector('.domain-stage')?.dataset.state==='unavailable'`,'actual preview reports '+failure+' failure');
      assert.ok(await p.evaluate('window.__kfmPreviewFaultHits>0'),'the intended failure path was exercised');
      await expand('weather');
      const failed=`document.querySelector('.welcome-layer-demo-state')?.textContent==='Map preview unavailable. Open the map to inspect source status.'`;
      await p.wait(failed,'failure replaces loading without a topic identifier');
      assert.equal(await p.evaluate(`document.querySelector('.welcome-layer-demo-state').getAttribute('role')`),'status');
      await activate('.welcome-layer-demo-actions button:first-child');
      await p.wait(failed,'hidden overlays do not mask map failure');
      await p.key('Escape','Escape',27);
      await p.wait(`document.querySelector('.living-welcome').dataset.fullscreen==='false'&&document.activeElement?.matches('.topic-preview-weather')`,'Escape restores categories and focus');
      await expand('history');
      await p.wait(failed,'failure persists when another category is selected');
      await revealControl(p,'.welcome-layer-demo-actions button:last-child');
      await p.evaluate(`document.querySelector('.welcome-layer-demo-actions button:last-child').focus()`);
      assert.equal(await p.evaluate(`document.activeElement?.textContent`),'Source notes & demonstrations');
      await p.key('Enter','Enter',13);
      await p.wait(`document.activeElement?.matches('.welcome-dialog-close')`,'source notes remain keyboard accessible after failure');
      await p.key('Escape','Escape',27);
      await p.wait(`document.activeElement?.matches('.welcome-layer-demo-actions button:last-child')`,'notes restore their exact opening action');
      await p.evaluate(`document.querySelector('.welcome-layer-demo-state').scrollIntoView({block:'nearest',behavior:'instant'})`);
      assert.equal(await p.evaluate(`(()=>{const e=document.querySelector('.welcome-layer-demo-state'),r=e.getBoundingClientRect(),a=e.closest('aside').getBoundingClientRect();return r.top>=a.top&&r.bottom<=a.bottom&&r.left>=0&&r.right<=innerWidth;})()`),true,'failure guidance is readable within the scrolling guide');
      if(process.env.KFM_WORKSPACE_SCREENSHOTS){
        await mkdir(process.env.KFM_WORKSPACE_SCREENSHOTS,{recursive:true});
        const capture=await p.call('Page.captureScreenshot',{format:'png'});
        await writeFile(join(process.env.KFM_WORKSPACE_SCREENSHOTS,`welcome-${failure}-${width}x${height}.png`),Buffer.from(capture.data,'base64'));
      }
      // The complete reverse route from Return bypasses the category rail.
      await p.key('Tab','Tab',9);
      assert.equal(await p.evaluate(`document.activeElement.matches('.welcome-preview-expand')`),true);
      await p.key('Tab','Tab',9,8);
      assert.equal(await p.evaluate('document.activeElement.textContent'),'Source notes & demonstrations');
      await p.key('Tab','Tab',9,8);
      assert.equal(await p.evaluate('document.activeElement.textContent'),'Open this category’s map →');
      await p.key('Enter','Enter',13);
      await p.wait(`!document.querySelector('.living-welcome')&&document.querySelector('.category-map-dock header strong')?.textContent==='Historic atlas'`,'full category map entry remains available');
      await leaveCompactLayers(p);
      // A later mount can recover when WebGL/construction becomes available.
      await p.evaluate('window.__kfmPreviewFault=null');
      await p.evaluate(`document.querySelector('.guide-trigger').focus()`);await p.key('Enter','Enter',13);
      await readyWelcome(p);await expand('weather');
      await p.wait(`document.querySelector('.welcome-layer-demo-state')?.textContent.startsWith('Provider context preview.')`,'recovered map replaces the unavailable message');
      await p.wait(`[...document.querySelectorAll('.welcome-preview-feed-state [data-state="unavailable"]')].length>0`,'unavailable providers retain their separate source labels');
      await activate('.welcome-layer-demo-actions button:first-child');
      await p.wait(`document.querySelector('.welcome-layer-demo-state')?.textContent.startsWith('Base context only.')`,'starter comparison still hides overlays');
      await activate('.welcome-layer-demo-actions button:first-child');
      await p.wait(`document.querySelector('.welcome-layer-demo-state')?.textContent.startsWith('Provider context preview.')`,'starter comparison restores provider context');
    }
  });
}

// Opt-in measurement pass uses the same hydrated app and network isolation as
// navigation acceptance. Timings describe this runner's empty-style/failure
// fixture, never provider cartography, production INP or physical mobile GPUs.
for (const profile of [
  { id: 'desktop', width: 1440, height: 960, ratio: 1, cpu: 1, latency: 0, throughput: -1, reduced: false },
  { id: 'mobile-4x', width: 390, height: 844, ratio: 2, cpu: 4, latency: 80, throughput: 200000, reduced: false },
  { id: 'mobile-reduced', width: 390, height: 844, ratio: 2, cpu: 4, latency: 80, throughput: 200000, reduced: true },
]) {
  test(`welcome performance ${profile.id}`, { skip: process.env.KFM_WELCOME_PERFORMANCE !== '1', timeout: 240000 }, async t => {
    const b = await browser(t), p = await pageSession(b, profile.width, profile.height, { waitTimeoutMs: 60000 });
    const report = { schema: 'kfm-welcome-performance/v1', profile, source: process.env.KFM_PERFORMANCE_SOURCE ?? null, browser: await b.call('Browser.getVersion'),
      scope: 'Built application; isolated empty styles; unavailable API providers; software WebGL; emulated CPU/network. Renderer JS heap excludes workers, native and GPU memory.',
      completed: false, network: { requests: 0, transferredBytes: 0 }, startup: null, frames: [], actions: [], memory: [] };
    const artifactDir = process.env.KFM_WELCOME_PERFORMANCE_ARTIFACTS;
    t.after(async () => {
      t.diagnostic('KFM_WELCOME_PERFORMANCE ' + JSON.stringify(report));
      if (artifactDir) {
        await mkdir(artifactDir, { recursive: true });
        await writeFile(join(artifactDir, profile.id + '.json'), JSON.stringify(report, null, 2) + '\n');
      }
    });
    b.listeners.add(message => {
      if (message.sessionId !== undefined && message.method === 'Network.requestWillBeSent'
        && message.params.request.url.startsWith(origin.origin + '/')) report.network.requests++;
      if (message.method === 'Network.loadingFinished') report.network.transferredBytes += message.params.encodedDataLength;
    });
    await p.call('Emulation.setDeviceMetricsOverride', { width: profile.width, height: profile.height, deviceScaleFactor: profile.ratio, mobile: profile.width < 600 });
    await p.call('Emulation.setCPUThrottlingRate', { rate: profile.cpu });
    await p.call('Network.emulateNetworkConditions', { offline: false, latency: profile.latency, downloadThroughput: profile.throughput, uploadThroughput: profile.throughput });
    await p.call('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: profile.reduced ? 'reduce' : 'no-preference' }] });
    await p.call('Performance.enable');
    await p.call('Page.addScriptToEvaluateOnNewDocument', { source: `(() => {
      window.__kfmWelcomePerf = { lcp: 0, cls: 0, longTasks: [], events: [] };
      for (const type of ['largest-contentful-paint', 'layout-shift', 'longtask', 'event']) {
        if (!PerformanceObserver.supportedEntryTypes.includes(type)) continue;
        new PerformanceObserver(list => { for (const entry of list.getEntries()) {
          const state = window.__kfmWelcomePerf;
          if (type === 'largest-contentful-paint') state.lcp = entry.startTime;
          if (type === 'layout-shift' && !entry.hadRecentInput) state.cls += entry.value;
          if (type === 'longtask' && state.longTasks.length < 500) state.longTasks.push(entry.duration);
          if (type === 'event' && state.events.length < 500) state.events.push({ name: entry.name, durationMs: entry.duration, inputDelayMs: entry.processingStart - entry.startTime });
        }}).observe({ type, buffered: true, ...(type === 'event' ? { durationThreshold: 16 } : {}) });
      }
    })();` });
    const metrics = async () => Object.fromEntries((await p.call('Performance.getMetrics')).metrics.map(({ name, value }) => [name, value]));
    const twoFrames = () => p.evaluate(`new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(() => resolve(performance.now()))))`);
    const sample = async label => {
      const before = await metrics();
      const cadence = await p.evaluate(`new Promise(resolve => {
        const gaps = [], start = performance.now(); let previous = start;
        function frame(now) { gaps.push(now - previous); previous = now;
          if (now - start < 1200) requestAnimationFrame(frame);
          else { gaps.sort((a,b)=>a-b); resolve({ sampleMs: now-start, callbacks: gaps.length, medianGapMs: gaps[Math.floor(gaps.length*.5)], p95GapMs: gaps[Math.floor(gaps.length*.95)], maxGapMs: gaps.at(-1) }); }
        } requestAnimationFrame(frame);
      })`);
      const after = await metrics();
      report.frames.push({ label, ...cadence, taskMs: (after.TaskDuration - before.TaskDuration) * 1000,
        scriptMs: (after.ScriptDuration - before.ScriptDuration) * 1000, layoutMs: (after.LayoutDuration - before.LayoutDuration) * 1000,
        styleMs: (after.RecalcStyleDuration - before.RecalcStyleDuration) * 1000 });
    };
    const keyAction = async (selector, label, condition) => {
      await revealControl(p, selector);
      await p.evaluate(`document.querySelector(${JSON.stringify(selector)}).focus(); window.__kfmWelcomeActionAt = performance.now()`);
      await p.key('Enter', 'Enter', 13);
      await p.wait(condition, label);
      const at = await twoFrames();
      const elapsedMs = at - await p.evaluate('window.__kfmWelcomeActionAt');
      report.actions.push({ label, readinessMsIncludingAutomation: elapsedMs });
      assert.ok(elapsedMs < 15000, label + ' remains usable within the fixture timeout');
    };
    await p.open('/'); await readyWelcome(p); await twoFrames();
    report.startup = await p.evaluate(`({ readyMs: performance.now(), paints: performance.getEntriesByType('paint').map(e=>({name:e.name,ms:e.startTime})), lcpMs: window.__kfmWelcomePerf.lcp })`);
    await p.wait(`document.querySelector('.domain-stage .maplibregl-canvas')`, 'software WebGL preview is actually mounted');
    await p.wait(`document.querySelector('.domain-stage')?.dataset.state==='ready'`, 'default preview draws its first settled fixture frame');
    report.startup.mapReadyMs = await p.evaluate('performance.now()');
    await sample('unselected-still');
    assert.equal(await p.evaluate(`document.querySelectorAll('.domain-stage .maplibregl-canvas').length`), 1, 'one shared preview renderer');
    assert.equal(await p.evaluate(`document.querySelectorAll('.living-welcome video').length`), 0, 'no initial decoder');
    if (profile.reduced) assert.equal(await p.evaluate(`document.querySelector('.living-welcome').dataset.motion`), 'paused');
    for (let cycle = 0; cycle < 3; cycle++) {
      if (cycle) {
        await p.key('Enter', 'Enter', 13);
        await readyWelcome(p);
      }
      await keyAction('.topic-preview-weather', 'weather-stage-' + cycle, `document.querySelector('.living-welcome')?.dataset.cinematic==='true'`);
      await openStageNotes(p);
      assert.equal(await p.evaluate(`document.querySelectorAll('.welcome-dialog video').length`), 0, 'opening a category does not admit a decoder');
      await keyAction('.welcome-dialog-body > .welcome-preview-action', 'expand-map-' + cycle, `document.querySelector('.living-welcome')?.dataset.fullscreen==='true'`);
      await p.wait(`document.querySelector('.domain-stage')?.dataset.topic==='weather'`, 'selected map preview');
      await p.wait(`document.querySelector('.domain-stage')?.dataset.state==='ready'`, 'selected preview draws before sampling');
      await twoFrames();
      assert.equal(await p.evaluate(`document.querySelectorAll('.domain-stage .maplibregl-canvas').length`), 1);
      if (!cycle) {
        await sample('selected-preview');
        if (artifactDir) {
          await mkdir(artifactDir, { recursive: true });
          const capture = await p.call('Page.captureScreenshot', { format: 'png' });
          await writeFile(join(artifactDir, profile.id + '.png'), Buffer.from(capture.data, 'base64'));
        }
      }
      if (!profile.reduced) {
        await keyAction('.welcome-preview-pause', 'pause-' + cycle, `document.querySelector('.living-welcome')?.dataset.motion==='paused'`);
        if (!cycle) await sample('explicitly-paused');
        await keyAction('.welcome-preview-pause', 'resume-' + cycle, `document.querySelector('.living-welcome')?.dataset.motion==='playing'`);
      }
      await p.key('Escape', 'Escape', 27);
      await p.wait(`document.querySelector('.living-welcome')?.dataset.fullscreen==='false'`, 'return to categories');
      await p.key('Escape', 'Escape', 27);
      await p.wait(`!document.querySelector('.living-welcome')&&document.activeElement?.matches('.guide-trigger')`, 'dismissal restores real map controls');
      await twoFrames();
      assert.equal(await p.evaluate(`document.querySelectorAll('.domain-stage .maplibregl-canvas,.capability-preview video').length`), 0, 'preview renderer and decoders leave on dismissal');
      await p.call('HeapProfiler.collectGarbage');
      const heap = await p.call('Runtime.getHeapUsage'), runtime = await metrics();
      report.memory.push({ cycle, usedBytes: heap.usedSize, backingStoreBytes: heap.backingStorageSize ?? null, nodes: runtime.Nodes, documents: runtime.Documents });
    }
    report.retainedGrowthBytes = report.memory.at(-1).usedBytes - report.memory[0].usedBytes;
    assert.ok(report.retainedGrowthBytes < 32 * 1024 * 1024, 'three short reopen cycles do not retain another 32 MiB of renderer JS heap');
    await p.key('Enter', 'Enter', 13); await readyWelcome(p);
    await keyAction('.topic-preview-aviation', 'aviation-stage', `document.querySelector('.living-welcome')?.dataset.cinematic==='true'`);
    await openStageNotes(p);
    const destination = await p.evaluate(`document.querySelector('.welcome-map-look strong').textContent`);
    await keyAction('.welcome-open-map', 'open-category-map', `!document.querySelector('.living-welcome')&&document.querySelector('.category-map-dock header strong')?.textContent===${JSON.stringify(destination)}`);
    assert.equal(await p.evaluate(`document.querySelector('[aria-label="Layer topic"]').value`), 'aviation', 'preview enters the real category workspace');
    report.transition = { topic: 'aviation', dock: destination };
    report.observed = await p.evaluate('window.__kfmWelcomePerf');
    assert.equal(await p.evaluate(`document.querySelectorAll('.domain-stage').length`), 0);
    report.completed = true;
  });
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
    p.holdSceneModule();
    await p.open('/', null, `for (const method of ['getItem','setItem','removeItem']) Object.defineProperty(Storage.prototype,method,{value(){throw new DOMException('Storage blocked','SecurityError')}});`);
    await p.wait(`document.querySelector('.explorer-guide.living-welcome')?.contains(document.activeElement)`, 'animated welcome owns keyboard while the map engine loads');
    assert.equal(await p.evaluate(`document.querySelectorAll('.explorer-guide:not(.living-welcome),.welcome-legacy-questions').length`), 0);
    await p.waitForSceneModule();
    await p.key('Escape', 'Escape', 27);
    await p.wait(`!document.querySelector('.explorer-guide') && document.activeElement.matches('.guide-trigger')`, 'welcome dismissal returns focus despite blocked storage');
    await p.releaseSceneModule();
    // Finishing the delayed scene download must not reopen the welcome or steal focus.
    await pause(250);
    assert.equal(await p.evaluate(`!document.querySelector('.explorer-guide') && document.activeElement.matches('.guide-trigger')`), true);
    for (let attempt = 0; attempt < 3; attempt++) {
      await p.key('Enter', 'Enter', 13);
      await p.wait(`document.querySelector('.living-welcome')?.contains(document.activeElement)`, 'loaded welcome owns keyboard on each reopen');
      if (attempt > 0) {
        await p.evaluate(`document.querySelector('.living-welcome input[type="checkbox"]').click()`);
        await p.wait(`document.querySelector('.living-welcome input[type="checkbox"]').checked === true`, 'explicit opt-out choice remains usable when storage throws');
      }
      await p.key('Escape', 'Escape', 27);
      await p.wait(`!document.querySelector('.explorer-guide') && document.activeElement.matches('.guide-trigger')`, 'loaded dismissal returns focus');
      await p.key('Escape', 'Escape', 27);
      assert.equal(await p.evaluate(`!document.querySelector('.explorer-guide') && document.activeElement.matches('.guide-trigger')`), true, 'repeated Escape cannot reopen welcome');
    }
  });
  test(`startup destinations at ${width}x${height}`, { timeout: 240000 }, async t => {
    const b = await browser(t), p = await pageSession(b, width, height);
    await t.test('Find and Chat retain DOM order and responsive keyboard access before map controls', async () => {
      await p.open('/', '1');
      assert.equal(await p.evaluate(`(() => {
        const header = document.querySelector('header.topbar');
        const find = header?.querySelector('button.atlas-scope-control');
        const ask = header?.querySelector('button.welcome-ai-entry');
        const controls = header?.querySelector('nav.map-chrome-dock');
        return !!(find && ask && controls
          && find.textContent.includes('Find') && ask.textContent.includes('Chat with KFM')
          && [find, ask].every(button => !button.disabled && button.tabIndex === 0
            && !button.closest('[inert], [aria-hidden="true"]')
            && (button.compareDocumentPosition(controls) & Node.DOCUMENT_POSITION_FOLLOWING)));
      })()`), true, 'both named buttons remain before map navigation in the DOM');
      await p.evaluate(`document.querySelector('.atlas-scope-control').focus()`);
      assert.equal(await p.evaluate(`document.activeElement.matches('.atlas-scope-control')`), true);
      // Chat remains available as a compact AI badge on phones.
      // Preserve header DOM order and require its Tab order at both sizes.
      assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('.welcome-ai-entry')).display !== 'none'`), true);
      {
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
      assert.equal(reachedMap, true, 'Tab reaches map controls after Find and Chat');
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
    for (const selector of ['.topic-preview-weather', '.topic-preview-history', '.discovery-hint button']) {
      await p.evaluate(`document.querySelector(${JSON.stringify(selector)}).focus()`);
      await p.key('Enter', 'Enter', 13);
      if(selector.startsWith('.topic-'))await openStageNotes(p);
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
      if (selector === '.discovery-hint button') {
        assert.equal((await closeGeometry()).focus, true, 'notes-only dialog wraps to its sole close without inventing a body control');
      } else {
        assert.equal(await p.evaluate(`!!document.activeElement?.closest('.welcome-dialog-body')`), true, 'Shift+Tab wraps to an available body control');
        assert.equal(await p.evaluate(`(()=>{for(let node=document.activeElement?.parentElement;node&&!node.matches('.welcome-dialog');node=node.parentElement){if(node.matches('details:not([open])')&&!node.querySelector(':scope>summary')?.contains(document.activeElement))return false;}return true;})()`), true, 'closed disclosure descendants never receive wrapped focus');
      }
      await p.key('Tab', 'Tab', 9);
      assert.equal((await closeGeometry()).focus, true, 'Tab returns to persistent close');
      // Use a real pointer dispatch at the visible button, not DOM click().
      const x=(before.left+before.right)/2, y=(before.top+before.bottom)/2;
      await p.call('Input.dispatchMouseEvent', {type:'mousePressed', x, y, button:'left', clickCount:1});
      await p.call('Input.dispatchMouseEvent', {type:'mouseReleased', x, y, button:'left', clickCount:1});
      await p.wait(`!document.querySelector('.welcome-dialog')`, 'visible close dismisses detail');
      if(selector.startsWith('.topic-'))await returnStage(p);
      assert.equal(await p.evaluate(`document.activeElement === document.querySelector(${JSON.stringify(selector)})`), true, 'focus returns to opening control');
      assert.equal(await p.evaluate(`document.querySelector('header.topbar').inert`), false, 'background state restored');
    }
    await p.evaluate(`document.querySelector('.topic-preview-weather').focus()`);
    await p.key('Enter', 'Enter', 13);
    await openStageNotes(p);
    await p.wait(`document.activeElement?.matches('.welcome-dialog-close')`, 'detail reopened');
    await p.key('Escape', 'Escape', 27);
    await p.wait(`!document.querySelector('.welcome-dialog') && document.activeElement?.matches('.welcome-layer-demo-actions button:last-child')`, 'Escape restores the source-notes action');
    await p.key('Escape','Escape',27);
    await p.wait(`document.activeElement?.matches('.topic-preview-weather')`, 'Escape returns to the original card');
    await p.key('Escape', 'Escape', 27);
    await p.wait(`!document.querySelector('.explorer-guide') && document.activeElement?.matches('.guide-trigger')`, 'next Escape closes welcome and returns focus to the guide trigger');
  });
}

// Only initial category setup uses focus(). Every subsequent hop is native
// Tab/Shift+Tab, so the complete journey can detect an intervening rail again.
for (const [width,height] of [[1280,800],[768,1024],[390,844],[320,568],[568,320]]) {
  test(`welcome preview keyboard journey at ${width}x${height}`, {timeout:120000}, async t => {
    const b=await browser(t),p=await pageSession(b,width,height);
    const reduced=height<400;
    if(reduced)await p.call('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
    await p.open('/');await readyWelcome(p);
    const opening=welcomeTopics.at(-1).id;
    await revealControl(p,'.topic-preview-'+opening);
    await p.evaluate(`document.querySelector('.topic-preview-${opening}').focus()`);
    const scroll=await p.evaluate(`document.querySelector('.living-welcome').scrollTop`);
    const focused=async selector=>{
      await p.wait(`document.activeElement?.matches(${JSON.stringify(selector)})`,'native focus reaches '+selector);
      if(selector==='.welcome-dialog-close'){
        // The portalled dialog owns the viewport, independently of the welcome
        // rectangle below the application header.
        await p.wait(`(()=>{const e=document.activeElement,r=e.getBoundingClientRect();return r.height>=44&&r.left>=0&&r.right<=innerWidth&&r.top>=0&&r.bottom<=innerHeight&&e.contains(document.elementFromPoint(r.left+r.width/2,r.top+r.height/2));})()`,'dialog close is visible and hit-testable');
      }else await revealControl(p,selector);
      assert.equal(await p.evaluate(`document.activeElement.matches(':focus-visible')`),true,'keyboard focus remains visible');
    };
    const tab=async(selector,reverse=false)=>{await p.key('Tab','Tab',9,reverse?8:0);await focused(selector);};
    const notes='.welcome-layer-demo-actions button:last-child',map='.welcome-layer-demo-actions button:nth-last-child(2)',back='.welcome-preview-expand';
    const enter=()=>p.key('Enter','Enter',13);
    await enter();await focused(back);
    await tab(notes,true);await tab(map,true);
    await tab(notes);await tab(back);
    // Nested notes return to their exact trigger, by Escape and a real click.
    for(const close of ['Escape','pointer']){
      await tab(notes,true);await enter();await focused('.welcome-dialog-close');
      if(close==='Escape')await p.key('Escape','Escape',27);
      else{
        const point=await p.evaluate(`(()=>{const r=document.querySelector('.welcome-dialog-close').getBoundingClientRect();return{x:r.left+r.width/2,y:r.top+r.height/2};})()`);
        await p.call('Input.dispatchMouseEvent',{type:'mousePressed',...point,button:'left',clickCount:1});
        await p.call('Input.dispatchMouseEvent',{type:'mouseReleased',...point,button:'left',clickCount:1});
      }
      await p.wait(`!document.querySelector('.welcome-dialog')&&document.activeElement?.matches(${JSON.stringify(notes)})`,'notes restore their trigger');
      await tab(back);
    }
    const pauseEnabled=await p.evaluate(`!document.querySelector('.welcome-preview-pause').disabled`);
    const scrollVisible=await p.evaluate(`document.querySelector('.welcome-rail-scroll').getClientRects().length>0`);
    if(pauseEnabled)await tab('.welcome-preview-pause');
    await tab('.welcome-stage-close');
    if(scrollVisible)await tab('[aria-label="Scroll categories left"]');
    await tab('.welcome-rail-card[aria-pressed="true"]');
    assert.equal(await p.evaluate(`document.activeElement.parentElement.getAttribute('role')`),'toolbar');
    assert.match(await p.evaluate(`document.getElementById(document.activeElement.parentElement.getAttribute('aria-describedby')).textContent`),/arrow keys/);
    for(const [key,code,id] of [['End',35,welcomeTopics.at(-1).id],['ArrowRight',39,welcomeTopics[0].id],['ArrowLeft',37,welcomeTopics.at(-1).id],['Home',36,welcomeTopics[0].id]]){
      await p.key(key,key,code);
      await p.wait(`document.activeElement?.dataset.topic==='${id}'&&document.activeElement.getAttribute('aria-pressed')==='true'`,'arrow/Home/End selects and focuses '+id);
      assert.deepEqual(await p.evaluate(`Array.from(document.querySelectorAll('.welcome-rail-card')).filter(e=>e.tabIndex===0).map(e=>e.dataset.topic)`),[id]);
      await focused('.welcome-rail-card[aria-pressed="true"]');
    }
    if(scrollVisible){
      await tab('[aria-label="Scroll categories right"]');
      await tab('.welcome-rail-card[aria-pressed="true"]',true);
      await tab('[aria-label="Scroll categories left"]',true);
    }
    await tab('.welcome-stage-close',true);
    if(pauseEnabled)await tab('.welcome-preview-pause',true);
    await tab(back,true);await enter();
    await p.wait(`document.querySelector('.living-welcome')?.dataset.cinematic==='false'&&document.activeElement?.matches('.topic-preview-${opening}')`,'Return restores the original category after rail switching');
    const returned = await p.evaluate(`(()=>{const root=document.querySelector('.living-welcome'),card=document.querySelector('.topic-preview-${opening}'),r=root.getBoundingClientRect(),c=card.getBoundingClientRect();return {scroll:root.scrollTop,max:Math.max(0,root.scrollHeight-root.clientHeight),cardVisible:c.width>0&&c.height>=44&&c.top>=r.top-.5&&c.bottom<=r.bottom+.5&&c.left>=r.left-.5&&c.right<=r.right+.5};})()`);
    // Reflow can shorten the chooser while previewing. Native scroll restoration
    // clamps at its current maximum; retain exact restoration within that range.
    assert.ok(Math.abs(returned.scroll-Math.min(scroll,returned.max))<=1,'Return restores chooser scroll within the current native scroll range');
    assert.equal(returned.cardVisible,true,'Return keeps the original category action visible');
    // Escape from a stage control restores that same card before the next key.
    await enter();await focused(back);
    if(pauseEnabled)await tab('.welcome-preview-pause');
    await p.key('Escape','Escape',27);
    await p.wait(`document.activeElement?.matches('.topic-preview-${opening}')&&document.querySelector('.living-welcome')?.dataset.cinematic==='false'`,'Escape restores the original category');
    await enter();await focused(back);await tab(notes,true);await tab(map,true);await enter();
    await p.wait(`!document.querySelector('.living-welcome')&&document.querySelector('[aria-label="Layer topic"]')?.value==='${opening}'&&document.querySelector('.category-map-dock')`,'native map action opens the selected primary map');
  });
}

// Hover acceptance uses an unpressed native mouse move. Every shared domain
// remains reachable by scrolling; a longer taxonomy need not fit one viewport.
for (const [width, height] of [[1440, 960], [1920, 1080], [375, 844]]) {
  test(`welcome topic geometry and real input at ${width}x${height}`, { timeout: 120000 }, async t => {
    const b = await browser(t), p = await pageSession(b, width, height);
    await p.open('/');await readyWelcome(p);
    const bounds = await p.evaluate(`Array.from(document.querySelectorAll('.living-welcome .topic-callout'), button => {
      const r=button.getBoundingClientRect();
      return {id:button.className,left:r.left,right:r.right,top:r.top,bottom:r.bottom,width:r.width,height:r.height};
    })`);
    assert.equal(bounds.length,welcomeTopics.length);
    for (let index=0;index<bounds.length;index++) {
      const a=bounds[index];
      assert.ok(a.width>0&&a.height>=44&&a.left>=0&&a.right<=width,`usable card: ${JSON.stringify(a)}`);
      for(const other of bounds.slice(index+1)) {
        const x=Math.min(a.right,other.right)-Math.max(a.left,other.left),y=Math.min(a.bottom,other.bottom)-Math.max(a.top,other.top);
        assert.ok(x<=.5||y<=.5,`topic hit areas must not overlap: ${JSON.stringify({a,other,x,y})}`);
      }
    }
    for(const topic of welcomeTopics)await revealControl(p,'.topic-'+topic.id);
    const center = selector => revealControl(p,selector);
    const move = point => p.call('Input.dispatchMouseEvent',{type:'mouseMoved',...point,button:'none',buttons:0});
    const stage=id=>`document.querySelector('.living-welcome')?.dataset.cinematic==='true'&&document.querySelector('.domain-stage')?.dataset.topic==='${id}'`;
    // Hover keeps the chooser stable even after the former takeover delay.
    // Preview is explicit for both pointer and touch users.
    if(width>600){
      await move(await center('.topic-weather'));
      await pause(850);
      assert.equal(await p.evaluate(`document.querySelector('.living-welcome').dataset.cinematic`),'false','hover never captures navigation');
      const point=await center('.topic-preview-weather');
      await p.call('Input.dispatchMouseEvent',{type:'mousePressed',...point,button:'left',clickCount:1});
      await p.call('Input.dispatchMouseEvent',{type:'mouseReleased',...point,button:'left',clickCount:1});
      await p.wait(stage('weather'),'explicit Preview opens the map stage');
      await move({x:width*.65,y:height*.45});
      await p.wait(stage('weather'),'leaving the former card retains the stage');
    }else{
      await p.call('Emulation.setTouchEmulationEnabled',{enabled:true,maxTouchPoints:1});
      const point=await center('.topic-preview-weather');
      await p.call('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{...point,id:1,radiusX:2,radiusY:2,force:1}]});
      await p.call('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
      await p.wait(stage('weather'),'a single Preview tap opens the map stage');
    }
    assert.equal(await p.evaluate(`document.querySelectorAll('.welcome-rail-card').length`),welcomeTopics.length,'every other category retains a place');
    assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('.discovery-field')).display`),'none','large cards clear the map');
    const geometry=await p.evaluate(`(()=>{const root=document.querySelector('.living-welcome').getBoundingClientRect(),rail=document.querySelector('.welcome-category-rail').getBoundingClientRect(),panel=document.querySelector('.welcome-layer-demo').getBoundingClientRect(),deck=document.querySelector('.welcome-scene-deck').getBoundingClientRect();return {root:{top:root.top,bottom:root.bottom},rail:{top:rail.top,bottom:rail.bottom},panel:{top:panel.top,bottom:panel.bottom},deck:{top:deck.top,bottom:deck.bottom},overflow:document.querySelector('.living-welcome').scrollWidth>innerWidth};})()`);
    assert.equal(geometry.overflow,false,'stage does not overflow horizontally');
    assert.ok(geometry.deck.bottom<=geometry.panel.top,'top controls do not cover the active category');
    assert.ok(geometry.panel.bottom<geometry.rail.top,'active category leaves space above category rail');
    assert.ok(geometry.rail.bottom<=geometry.root.bottom-24,'rail leaves provider credits clear');
    for(const id of ['water','geology','aviation','evidence']){
      const selector=`.welcome-rail-card[data-topic="${id}"]`;
      await revealControl(p,selector);await p.evaluate(`document.querySelector(${JSON.stringify(selector)}).focus()`);await p.key('Enter','Enter',13);
      await p.wait(stage(id),'rail selects '+id+' without reopening the grid');
      assert.equal(await p.evaluate(`document.querySelectorAll('.domain-stage').length`),1,'one shared stage');
    }
    await p.key('Home','Home',36);await p.wait(stage(welcomeTopics[0].id),'Home selects the first story');
    await p.key('End','End',35);await p.wait(stage(welcomeTopics.at(-1).id),'End selects the last story');
    await p.key('ArrowRight','ArrowRight',39);await p.wait(stage(welcomeTopics[0].id),'Right wraps the rail');
    if(process.env.KFM_WORKSPACE_SCREENSHOTS){await mkdir(process.env.KFM_WORKSPACE_SCREENSHOTS,{recursive:true});const capture=await p.call('Page.captureScreenshot',{format:'png'});await writeFile(join(process.env.KFM_WORKSPACE_SCREENSHOTS,`welcome-cinematic-${width}x${height}.png`),Buffer.from(capture.data,'base64'));}
    await returnStage(p);
    assert.equal(await p.evaluate(`document.activeElement.matches('.topic-preview-weather')`),true,'Return restores the original card');
    assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('.discovery-field')).display`),'grid');

  });
}

// Placement follows measured content and the shared taxonomy. Check all rows
// by scrolling, then exercise the current detail/expanded-view equivalents of
// the retired footage timeline and footer. Fixtures establish no accepted data.
for (const [width,height,label] of [[1440,960,'desktop'],[1024,1366,'tall tablet'],[901,1200,'narrow desktop'],[768,1024,'tablet'],[1280,720,'short desktop'],[1024,600,'landscape'],[320,568,'narrow phone'],[640,360,'200 percent layout equivalent']]) {
  test(`welcome content stays composed at ${width}x${height} (${label})`,{timeout:150000},async t=>{
    const b=await browser(t),p=await pageSession(b,width,height,{attribution:'Isolated browser layout fixture attribution — empty geometry; no observations, rights claims or accepted data. <a href="https://openmaptiles.org/">Fixture OpenMapTiles</a> · <a href="https://www.openstreetmap.org/copyright">Fixture OpenStreetMap</a>'});
    if(label==='200 percent layout equivalent')await p.call('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:2,mobile:false});
    await p.open('/');await readyWelcome(p);
    await p.wait(`(()=>{const r=document.querySelector('#map-canvas .maplibregl-ctrl-bottom-right .maplibregl-ctrl-attrib')?.getBoundingClientRect();return r&&r.width>0&&r.height>0;})()`,'real MapLibre attribution mounted in its welcome strip from the bounded local style fixture');
    const checkLayout=async state=>{
      const result=await p.evaluate(`(()=>{
        const root=document.querySelector('.explorer-guide.living-welcome');
        const selectors=['.welcome-hero','.welcome-toolbar','.discovery-hint','.topic-callout','.welcome-preview-expand'];
        const boxes=selectors.flatMap(selector=>[...root.querySelectorAll(selector)].map((node,index)=>{const r=node.getBoundingClientRect();return{name:selector+':'+index,left:r.left,right:r.right,top:r.top,bottom:r.bottom,width:r.width,height:r.height};}));
        const r=root.getBoundingClientRect(),header=document.querySelector('header.topbar').getBoundingClientRect(),a=document.querySelector('#map-canvas .maplibregl-ctrl-attrib')?.getBoundingClientRect();
        return {boxes,root:{left:r.left,right:r.right,top:r.top,bottom:r.bottom,scrollWidth:root.scrollWidth,clientWidth:root.clientWidth},headerBottom:header.bottom,attribution:a?{left:a.left,right:a.right,top:a.top,bottom:a.bottom,width:a.width,height:a.height}:null};
      })()`);
      assert.ok(result.root.top>=result.headerBottom-.5,`${state}: header has its own space ${JSON.stringify(result)}`);
      assert.ok(result.root.scrollWidth<=result.root.clientWidth,`${state}: no horizontal overflow`);
      assert.ok(result.attribution?.width>0&&result.attribution?.height>0,`${state}: real attribution has measured geometry`);
      assert.ok(result.attribution.top>=result.root.bottom-.5&&result.attribution.bottom<=height+.5,`${state}: attribution owns a separate viewport strip ${JSON.stringify(result.attribution)}`);
      assert.ok(result.attribution.left>=-.5&&result.attribution.right<=width+.5,`${state}: attribution outer width stays in the viewport`);
      assert.equal(result.boxes.filter(box=>box.name.startsWith('.topic-callout:')).length,welcomeTopics.length);
      for(let i=0;i<result.boxes.length;i++){
        const box=result.boxes[i];
        assert.ok(box.width>0&&box.height>0,`${state}: real content box ${JSON.stringify(box)}`);
        assert.ok(box.left>=result.root.left-.5&&box.right<=result.root.right+.5,`${state}: content stays inside scroll width ${JSON.stringify(box)}`);
        for(const other of result.boxes.slice(i+1)){
          const x=Math.min(box.right,other.right)-Math.max(box.left,other.left),y=Math.min(box.bottom,other.bottom)-Math.max(box.top,other.top);
          assert.ok(x<=.5||y<=.5,`${state}: distinct content areas do not overlap ${JSON.stringify({box,other,x,y})}`);
        }
      }
    };
    const checkCredits=async state=>{
      const count=await p.evaluate(`[...document.querySelectorAll('#map-canvas .maplibregl-ctrl-attrib-inner a')].filter(a=>a.textContent.startsWith('Fixture ')).length`);
      assert.equal(count,2,'both explicit fixture credits remain in the real attribution control');
      for(let index=0;index<count;index++){
        await p.evaluate(`[...document.querySelectorAll('#map-canvas .maplibregl-ctrl-attrib-inner a')].filter(a=>a.textContent.startsWith('Fixture '))[${index}].scrollIntoView({block:'nearest',inline:'nearest',behavior:'instant'})`);
        const credit=await p.evaluate(`(()=>{const a=[...document.querySelectorAll('#map-canvas .maplibregl-ctrl-attrib-inner a')].filter(a=>a.textContent.startsWith('Fixture '))[${index}],r=a.getBoundingClientRect(),strip=document.querySelector('#map-canvas .maplibregl-ctrl-attrib').getBoundingClientRect(),root=document.querySelector('.explorer-guide.living-welcome').getBoundingClientRect(),style=getComputedStyle(a);return{text:a.textContent,width:r.width,height:r.height,top:r.top,bottom:r.bottom,left:r.left,right:r.right,strip:{top:strip.top,bottom:strip.bottom,left:strip.left,right:strip.right},welcomeBottom:root.bottom,font:parseFloat(style.fontSize),lines:new Set([...a.getClientRects()].map(box=>Math.round(box.top))).size,display:style.display,visibility:style.visibility,hit:document.elementFromPoint(r.left+r.width/2,r.top+r.height/2)?.closest('a')===a,hitBy:(e=>e?e.tagName+'.'+String(e.className||'')+'#'+e.id+' in '+String(e.parentElement?.className||''):'none')(document.elementFromPoint(r.left+r.width/2,r.top+r.height/2))};})()`);
        assert.ok(credit.width>0&&credit.height>0&&credit.font>0&&credit.display!=='none'&&credit.visibility==='visible',`${state}: credit text has actual visible geometry ${JSON.stringify(credit)}`);
        assert.equal(credit.lines,1,`${state}: a credit never wraps inside a provider's name ${JSON.stringify(credit)}`);
        assert.ok(credit.top>=credit.welcomeBottom-.5&&credit.top>=credit.strip.top-.5&&credit.bottom<=credit.strip.bottom+.5&&credit.bottom<=height+.5&&credit.left>=credit.strip.left-.5&&credit.right<=credit.strip.right+.5,`${state}: credit fits its reserved viewport strip ${JSON.stringify(credit)}`);
        assert.equal(credit.hit,true,`${state}: the credit is reachable above clip and background layers ${JSON.stringify(credit)}`);
      }
    };
    await checkLayout('initial');
    if(width===1440){
      await p.evaluate(`document.querySelector('.topic-weather').focus({preventScroll:true})`);
      await p.wait(`document.querySelector('.welcome-preview-brief h2').textContent===${JSON.stringify(categoryGlimpse('weather').title)}`,'shared brief follows keyboard interest');
      // Measure switching between selected glimpses. The initial chooser has
      // different introductory copy and is checked separately by checkLayout.
      const rowTop=()=>p.evaluate(`document.querySelector('.discovery-field--grouped').getBoundingClientRect().top`);
      const before=await rowTop();
      await p.evaluate(`document.querySelector('.topic-history').focus({preventScroll:true})`);
      await p.wait(`document.querySelector('.welcome-preview-brief h2').textContent===${JSON.stringify(categoryGlimpse('history').title)}`,'shared brief follows the next category');
      const after=await rowTop();
      assert.ok(Math.abs(after-before)<2,'switching category glimpses never shifts the category rows: '+JSON.stringify({before,after}));
    }

    if(process.env.KFM_WORKSPACE_SCREENSHOTS){await mkdir(process.env.KFM_WORKSPACE_SCREENSHOTS,{recursive:true});const capture=await p.call('Page.captureScreenshot',{format:'png'});await writeFile(join(process.env.KFM_WORKSPACE_SCREENSHOTS,`welcome-${width}x${height}.png`),Buffer.from(capture.data,'base64'));}
    await checkCredits('initial license strip');
    await p.wait(`!!document.querySelector('.living-welcome .domain-stage .maplibregl-ctrl-attrib')`,'the live welcome map carries its own provider credits');
    if(width<=1100&&height<=480)assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('.welcome-preview-brief')).position`),'static','short landscape keeps the panel in flow so full cards remain reachable');
    for(const topic of welcomeTopics)await revealControl(p,'.topic-'+topic.id);
    assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('header.topbar')).visibility`),'visible','global header remains available');
    for(const selector of ['.maplibregl-ctrl-scale'])assert.equal(await p.evaluate(`getComputedStyle(document.querySelector(${JSON.stringify(selector)})).visibility`),'hidden','background map chrome does not peek through welcome');
    assert.equal(await p.evaluate(`getComputedStyle(document.querySelector('#map-canvas .maplibregl-ctrl-attrib')).visibility`),'visible','real attribution remains available');
    await p.evaluate(`document.querySelector('.guide-trigger').focus()`);await p.key('Enter','Enter',13);
    await p.wait(`document.querySelector('.site-root').dataset.welcomeSources==='open'`,'Map sources opens the current attribution strip');
    await p.wait(`(()=>{const bar=document.querySelector('#map-canvas .maplibregl-ctrl-bottom-right'),strip=document.querySelector('#map-canvas .maplibregl-ctrl-attrib'),root=document.querySelector('.explorer-guide.living-welcome'),r=strip?.getBoundingClientRect(),port=root?.getBoundingClientRect();return bar&&r&&port&&!bar.getAnimations({subtree:true}).some(animation=>animation.pending||animation.playState==='running')&&r.top>=port.bottom-.5&&r.bottom<=innerHeight+.5;})()`,'source-strip entrance finishes inside its reserved viewport');
    await checkLayout('source strip open');
    await checkCredits('expanded source strip');
    assert.match(await p.evaluate(`document.querySelector('#map-canvas .maplibregl-ctrl-attrib').textContent`),/Isolated browser layout fixture attribution/,'source text remains a labeled empty fixture, not accepted observations');
    assert.ok(await p.evaluate(`parseFloat(getComputedStyle(document.querySelector('#map-canvas .maplibregl-ctrl-attrib-inner')).fontSize)>0`),'expanded sources expose readable attribution text');
    const before=await p.evaluate(`({search:location.search,topic:document.querySelector('[aria-label="Layer topic"]').value})`);
    // All domains get a real native-keyboard detail journey on desktop and the
    // smallest phone. Other viewports retain captured and uncaptured examples.
    const detailTopics=(width===1440||width===320)?welcomeTopics:welcomeTopics.filter(topic=>['history','evidence'].includes(topic.id));
    for(const topic of detailTopics){
      await revealControl(p,'.topic-preview-'+topic.id);await p.evaluate(`document.querySelector('.topic-preview-${topic.id}').focus()`);await p.key('Enter','Enter',13);
      await openStageNotes(p);
      await p.wait(`document.activeElement?.matches('.welcome-dialog-close')`,'detail takes focus for '+topic.id);
      const detail=await p.evaluate(`(()=>{const d=document.querySelector('.welcome-dialog');return{role:d.getAttribute('role'),modal:d.getAttribute('aria-modal'),title:d.querySelector('h2')?.textContent,facets:[...d.querySelectorAll('.capability-facets li')].map(n=>n.textContent),notes:[...d.querySelectorAll('.welcome-source-note')].map(n=>n.textContent),video:d.querySelectorAll('video').length};})()`);
      assert.deepEqual({role:detail.role,modal:detail.modal,title:detail.title,facets:detail.facets,video:detail.video},{role:'dialog',modal:'true',title:topic.title,facets:topic.facets,video:0});
      assert.ok(detail.notes.includes(topic.limitation),'source limitations stay attached to '+topic.id);
      const glimpse=categoryGlimpse(topic.id);
      const glimpseText=await p.evaluate(`document.querySelector('.welcome-category-glimpse').textContent`);
      for(const value of Object.values(glimpse))assert.ok(glimpseText.includes(value),'category-specific demonstration and limits: '+topic.id);
      const previews=capabilityPreviews(topic.id);
      if(previews.length){
        const capture=await p.evaluate(`(()=>{const f=document.querySelector('.welcome-dialog .capability-preview');return{id:f?.dataset.demo,caption:f?.querySelector('figcaption')?.textContent,source:f?.querySelector('img')?.getAttribute('src')};})()`);
        assert.equal(capture.id,previews[0].id);assert.equal(capture.source,previews[0].poster,'opening details requests only the captured still');
        for(const text of [previews[0].title,previews[0].sourceTime,previews[0].limitation,previews[0].context].filter(Boolean))assert.ok(capture.caption.includes(text),'capture keeps its time, scope and context');
        assert.ok(capture.caption.includes(previews[0].context?'CONTEXT CAPTURE':'EXPLORER CAPTURE'),'context reuse never becomes domain observation coverage');
        if(topic.id==='weather'&&(width===1440||width===320)){
          await p.evaluate(`document.querySelector('.capability-preview-play').focus()`);await p.key('Enter','Enter',13);
          await p.wait(`(()=>{const video=document.querySelector('.capability-preview video');return video&&video.readyState>=2&&!video.paused;})()`,'native requested tour decodes and plays');
          if(process.env.KFM_WORKSPACE_SCREENSHOTS){const capture=await p.call('Page.captureScreenshot',{format:'png'});await writeFile(join(process.env.KFM_WORKSPACE_SCREENSHOTS,`welcome-weather-${width}x${height}.png`),Buffer.from(capture.data,'base64'));}
          await p.key('Enter','Enter',13);
          await p.wait(`document.querySelector('.capability-preview video')?.paused===true`,'native Pause tour stops the decoder');
        }
        if(previews.length>1){await p.evaluate(`document.querySelector('.welcome-dialog .topic-options button:nth-child(2)').focus()`);await p.key('Enter','Enter',13);await p.wait(`document.querySelector('.welcome-dialog .capability-preview')?.dataset.demo===${JSON.stringify(previews[1].id)}`,'native choice changes only the selected capture');}
      }else{
        assert.equal(await p.evaluate(`!!document.querySelector('.welcome-dialog .capability-preview')`),false);
        assert.ok(detail.notes.includes(capabilityNote(topic.id)),'uncaptured domain discloses the missing verified animation');
      }
      assert.deepEqual(await p.evaluate(`({search:location.search,topic:document.querySelector('[aria-label="Layer topic"]').value})`),before,'preview choices do not navigate or activate source workspaces');
      await p.key('Escape','Escape',27);await returnStage(p);await p.wait(`!document.querySelector('.welcome-dialog')&&document.activeElement?.matches('.topic-preview-${topic.id}')`,'Escape restores the exact opening domain');
    }
    await revealControl(p,'.topic-preview-history');await p.evaluate(`document.querySelector('.topic-preview-history').focus()`);await p.key('Enter','Enter',13);
    await openStageNotes(p);
    await p.wait(`document.activeElement?.matches('.welcome-dialog-close')`,'history detail reopened');
    await p.evaluate(`document.querySelector('.welcome-dialog-body>.welcome-preview-action').focus()`);await p.key('Enter','Enter',13);
    await p.wait(`document.querySelector('.living-welcome')?.dataset.fullscreen==='true'&&document.activeElement?.matches('.welcome-preview-expand')`,'explicit preview hands focus to Return');
    assert.equal(await p.evaluate(`document.querySelector('.domain-stage').dataset.topic`),'history');
    const expanded=await p.evaluate(`(()=>{const root=document.querySelector('.explorer-guide.living-welcome'),grid=root.querySelector('.discovery-field--grouped'),stage=root.querySelector('.domain-stage'),r=stage.getBoundingClientRect(),port=root.getBoundingClientRect();return{hidden:getComputedStyle(grid).display==='none',cards:[...grid.querySelectorAll('button')].filter(button=>button.getClientRects().length>0).length,top:r.top,bottom:r.bottom,portTop:port.top,portBottom:port.bottom};})()`);
    assert.equal(expanded.hidden,true,'expanded map removes the grouped category overlay');
    assert.equal(expanded.cards,0,'hidden category buttons have no visible or tabbable boxes');
    assert.ok(Math.abs(expanded.top-expanded.portTop)<1&&Math.abs(expanded.bottom-expanded.portBottom)<1,'expanded map fills the welcome viewport after opening from a scrolled category: '+JSON.stringify(expanded));
    if(process.env.KFM_WORKSPACE_SCREENSHOTS){const capture=await p.call('Page.captureScreenshot',{format:'png'});await writeFile(join(process.env.KFM_WORKSPACE_SCREENSHOTS,`welcome-expanded-${width}x${height}.png`),Buffer.from(capture.data,'base64'));}
    const previewControls=await p.evaluate(`[...document.querySelectorAll('.welcome-preview-expand,.welcome-preview-pause')].map(button=>{const r=button.getBoundingClientRect();return{text:button.textContent,top:r.top,bottom:r.bottom,left:r.left,right:r.right,width:r.width,height:r.height,hit:button.contains(document.elementFromPoint(r.left+r.width/2,r.top+r.height/2))};})`);
    assert.equal(previewControls.length,2);
    for(const box of previewControls)assert.ok(box.width>0&&box.height>=44&&box.top>=0&&box.bottom<=height&&box.left>=0&&box.right<=width&&box.hit,'Return and Pause keep 44px hit areas and stay visible and operable: '+JSON.stringify(box));
    await p.key('Tab','Tab',9);assert.equal(await p.evaluate(`document.activeElement.matches('.welcome-preview-pause')`),true,'native Tab reaches Pause');
    await p.key('Enter','Enter',13);await p.wait(`document.querySelector('.living-welcome').dataset.motion==='paused'`,'Pause stops the live map drift');
    await p.key('Enter','Enter',13);await p.wait(`document.querySelector('.living-welcome').dataset.motion==='playing'`,'Play resumes after explicit input');
    await p.evaluate(`document.querySelector('.welcome-preview-expand').focus()`);await p.key('Enter','Enter',13);
    await p.wait(`document.querySelector('.living-welcome').dataset.fullscreen==='false'&&document.querySelector('.living-welcome').dataset.active===undefined`,'Return clears the explicit preview pin');
    await checkLayout('returned categories');await revealControl(p,'.topic-evidence');
    await p.evaluate(`document.querySelector('.welcome-preview-expand').focus()`);await p.key('Enter','Enter',13);
    await p.wait(`document.querySelector('.living-welcome').dataset.fullscreen==='true'`,'expanded preview reopens');
    await p.key('Escape','Escape',27);await p.wait(`document.querySelector('.living-welcome').dataset.fullscreen==='false'`,'Escape returns to categories without dismissing welcome');
    await p.evaluate(`document.querySelector('.welcome-skip').focus()`);await p.key('Enter','Enter',13);
    await p.wait(`!document.querySelector('.explorer-guide.living-welcome')&&document.activeElement?.matches('.guide-trigger')`,'current toolbar exit dismisses welcome and returns focus');
    for(const selector of ['.maplibregl-ctrl-scale'])assert.equal(await p.evaluate(`getComputedStyle(document.querySelector(${JSON.stringify(selector)})).visibility`),'visible','ordinary map chrome is restored');
  });
}

// Real component geometry with isolated provider responses; no accepted data is
// inferred from this fixture. These checks deliberately do not inspect welcome
// topic counts, flame pixel colours, or CSS declaration text.
for (const [width, height] of [[1366, 900], [1024, 768], [911, 600], [390, 844]]) {
  test(`compact clock and attribution stay separate at ${width}x${height}`, { timeout: 60000 }, async t => {
    const b = await browser(t), p = await pageSession(b, width, height, { attribution: 'Isolated control geometry fixture: source timing and rights remain unavailable.' });
    await p.open('/?motion=off', '1');
    await p.wait(`document.querySelector('.compact-time-clock-toggle') && document.querySelector('.map-information-home .maplibregl-ctrl-attrib-button')`, 'real time and attribution controls mounted in their final map homes');
    const rects = () => p.evaluate(`(() => {
      const rect = selector => { const r = document.querySelector(selector)?.getBoundingClientRect(); return r ? { left:r.left, right:r.right, top:r.top, bottom:r.bottom, width:r.width, height:r.height } : null; };
      return { header:rect('.topbar'), clock:rect('.compact-time-clock-toggle'), info:rect('.maplibregl-ctrl-attrib-button'), row:rect('.compact-time-row'), settings:rect('.compact-time-popover'), sources:rect('.maplibregl-ctrl-attrib-inner'), scroll:document.querySelector('.map-stage').scrollTop, overflow:document.documentElement.scrollWidth > innerWidth };
    })()`);
    const initial = await rects();
    const clockAppearance = () => p.evaluate(`(() => {
      const button = document.querySelector('.compact-time-clock-toggle'), style = getComputedStyle(button), r = button.getBoundingClientRect();
      return { backgroundAlpha:style.backgroundColor.startsWith('rgba(') ? Number(style.backgroundColor.split(',').at(-1).replace(')','')) : 1,
        border:style.borderTopWidth, shadow:style.boxShadow,
        visible:style.visibility === 'visible' && Number(style.opacity) > .9,
        hit:button.contains(document.elementFromPoint(r.left+r.width/2,r.top+r.height/2)),
        expanded:button.getAttribute('aria-expanded') };
    })()`);
    const idleClock = await clockAppearance();
    const clockPoint = { x:initial.clock.left+initial.clock.width/2, y:initial.clock.top+initial.clock.height/2 };
    await p.call('Input.dispatchMouseEvent', { type:'mouseMoved', ...clockPoint });
    const hoveredClock = await clockAppearance();
    assert.ok(hoveredClock.backgroundAlpha >= .9, 'hover retains an opaque clock surface above light basemaps');
    assert.equal(hoveredClock.border, idleClock.border, 'hover retains the clock border');
    assert.notEqual(hoveredClock.border, '0px');
    assert.equal(hoveredClock.shadow, idleClock.shadow, 'hover retains the clock shadow');
    assert.notEqual(hoveredClock.shadow, 'none');
    assert.ok(hoveredClock.visible && hoveredClock.hit, 'the hovered clock stays visible and hit-testable');
    assert.equal(hoveredClock.expanded, 'false', 'hover does not open or dismiss time controls');
    const clickClock = async () => {
      await p.call('Input.dispatchMouseEvent', { type:'mousePressed', button:'left', clickCount:1, ...clockPoint });
      await p.call('Input.dispatchMouseEvent', { type:'mouseReleased', button:'left', clickCount:1, ...clockPoint });
    };
    await clickClock();
    await p.wait(`document.querySelector('.compact-time-clock-toggle')?.getAttribute('aria-expanded') === 'true' && document.querySelector('.compact-time-popover')`, 'ordinary mouse click opens the hovered clock');
    await pause(250);
    for (const selector of ['.compact-time-row', '.compact-time-popover header', '.topbar']) {
      const point = await p.evaluate(`(() => {const r=document.querySelector(${JSON.stringify(selector)}).getBoundingClientRect();return {x:r.left+r.width/2,y:r.top+r.height/2};})()`);
      await p.call('Input.dispatchMouseEvent', { type:'mouseMoved', ...point });
      assert.equal(await p.evaluate(`document.querySelector('.compact-time-clock-toggle').getAttribute('aria-expanded')`), 'true', 'moving onto and away from '+selector+' keeps time controls open');
    }
    await p.call('Input.dispatchMouseEvent', { type:'mouseMoved', ...clockPoint });
    assert.ok((await clockAppearance()).backgroundAlpha >= .9, 'the expanded clock also retains its hover surface');
    await clickClock();
    await p.wait(`document.querySelector('.compact-time-clock-toggle')?.getAttribute('aria-expanded') === 'false' && !document.querySelector('.compact-time-popover')`, 'the same hovered clock closes settings');
    await p.call('Input.dispatchMouseEvent', { type:'mouseMoved', x:width/2, y:80 });
    await p.evaluate(`document.querySelector('.compact-time-clock-toggle').focus()`);
    await p.key('Enter', 'Enter', 13);
    await p.wait(`document.querySelector('.compact-time-clock-toggle')?.getAttribute('aria-expanded') === 'true' && document.querySelector('.compact-time-popover')`, 'Enter opens settings');
    await pause(250);
    let g = await rects();
    assert.ok(g.settings.top >= g.header.bottom + 4, 'settings header clears the toolbar at short heights');
    assert.ok(g.settings.bottom <= g.row.top - 4, 'settings leave the same clock reachable');
    assert.ok(g.info.bottom <= g.row.top - .5 || g.info.top >= g.row.bottom + .5, 'information button does not occupy the time row');
    assert.ok(g.clock.width >= 44 && g.info.width >= 44, 'touch targets retain their size');
    assert.equal(g.overflow, false);
    await p.evaluate(`document.querySelector('.maplibregl-ctrl-attrib-button').focus()`);
    if (!await p.evaluate(`document.querySelector('.maplibregl-ctrl-attrib').classList.contains('maplibregl-compact-show')`)) await p.key('Enter', 'Enter', 13);
    await pause(100);
    g = await rects();
    assert.ok(g.sources.width > 0 && g.sources.left >= 0 && g.sources.right <= width + 1);
    assert.ok(g.sources.bottom <= g.row.top - 4, 'source information clears the displayed time');
    assert.ok(Math.abs(g.info.left - initial.info.left) < 1 && Math.abs(g.info.top - initial.info.top) < 1, 'source toggle does not move its indicator');
    assert.equal(g.scroll, 0, 'keyboard focus cannot scroll the map and displace controls');
    await p.evaluate(`document.querySelector('.compact-time-clock-toggle').focus()`);
    await p.key('Escape', 'Escape', 27);
    await p.wait(`document.querySelector('.compact-time-clock-toggle')?.getAttribute('aria-expanded') === 'false' && !document.querySelector('.compact-time-popover')`, 'Escape closes settings');
    assert.equal(await p.evaluate(`document.activeElement === document.querySelector('.compact-time-clock-toggle')`), true);
    if (width < 600) {
      await p.key('Enter', 'Enter', 13);
      await p.wait(`document.querySelector('.compact-time-clock-toggle')?.getAttribute('aria-expanded') === 'true'`, 'reopen before touch close');
      await pause(250);
      const r = (await rects()).clock;
      await p.call('Emulation.setTouchEmulationEnabled', { enabled:true, maxTouchPoints:1 });
      await p.call('Input.dispatchTouchEvent', { type:'touchStart', touchPoints:[{ x:r.left+r.width/2, y:r.top+r.height/2 }] });
      await p.call('Input.dispatchTouchEvent', { type:'touchEnd', touchPoints:[] });
      await p.wait(`document.querySelector('.compact-time-clock-toggle')?.getAttribute('aria-expanded') === 'false'`, 'touch closes from the same clock');
    }
  });
}


// First-paint acceptance: a pending restore must never reveal a chooser or map.
test('server markup and startup frames keep the map covered until the welcome decision', { timeout:60000 }, async t => {
  const html=await fetch(origin).then(response=>response.text());
  assert.match(html,/data-startup="pending"/);
  assert.match(html,/class="explorer-startup-cover"/);
  assert.doesNotMatch(html,/What would you like to explore\?|All questions &amp; tools/);
  const b=await browser(t),p=await pageSession(b,1280,800);
  await p.open('/',null,`
    window.__kfmStartupFrames=[];
    function sampleStartup(){
      const root=document.querySelector('.atlas-studio');
      if(root){
        const pending=root.dataset.startup==='pending',cover=document.querySelector('.explorer-startup-cover'),shell=document.querySelector('.explorer-shell');
        const welcome=!!document.querySelector('.living-welcome');
        // A frame can be sampled while the document is still parsing: the root and cover
        // exist but the shell does not yet. An unparsed shell shows no map, so it counts as hidden.
        window.__kfmStartupFrames.push({pending,welcome,shell:!!shell,covered:!!cover&&getComputedStyle(cover).visibility!=='hidden',mapHidden:!shell||getComputedStyle(shell).visibility==='hidden',retired:!!document.querySelector('.explorer-guide:not(.living-welcome)')});
        if(!pending&&welcome)return;
      }
      requestAnimationFrame(sampleStartup);
    }
    requestAnimationFrame(sampleStartup);
  `);
  await readyWelcome(p);
  const frames=await p.evaluate('window.__kfmStartupFrames');
  assert.ok(frames.length>0);
  assert.ok(frames.every(frame=>!frame.retired));
  assert.ok(frames.filter(frame=>frame.pending).every(frame=>frame.covered&&frame.mapHidden),JSON.stringify(frames));
  assert.ok(frames.some(frame=>frame.pending&&frame.shell),'at least one pending frame sees the parsed shell held hidden');
  assert.ok(frames.filter(frame=>!frame.pending).every(frame=>frame.welcome),'first resolved frame shows the graphical welcome');
});

for(const [width,height] of [[1280,800],[768,900],[390,844],[320,740],[568,320]]){
 test('full-width tips and Chat handoff at '+width+'x'+height,{timeout:60000},async t=>{
  const b=await browser(t),p=await pageSession(b,width,height);
  await p.open('/');await readyWelcome(p);
  const geometry=await p.evaluate(`(()=>{
    const rect=e=>{const r=e.getBoundingClientRect();return {left:r.left,right:r.right,width:r.width,height:r.height};};
    const header=document.querySelector('.topbar'),tips=header.querySelector(':scope>.welcome-feature-guide'),chat=header.querySelector('.qwen-header-entry'),map=header.querySelector('.map-chrome-dock');
    return {header:rect(header),tips:rect(tips),chat:rect(chat),map:rect(map),chatClipped:chat.scrollWidth>chat.clientWidth+1,overflow:document.documentElement.scrollWidth>innerWidth,controls:[...tips.querySelectorAll('.welcome-feature-steppers button')].map(rect),duplicates:document.querySelectorAll('.welcome-feature-guide').length};
  })()`);
  if(height>480)assert.ok(geometry.tips.width>=geometry.header.width-34,'tips stretch across the header');
  else assert.ok(geometry.header.height<=54&&geometry.tips.width>200,'short landscape keeps a full reading area without taking map height');
  assert.equal(geometry.duplicates,1);assert.equal(geometry.overflow,false);assert.equal(geometry.chatClipped,false);
  assert.ok(geometry.chat.right<=geometry.map.left+.5,'Chat and map controls do not overlap');
  for(const box of geometry.controls)assert.ok(box.width>=44&&box.height>=44);
  for(let i=0;i<6;i++){
    await p.evaluate(`document.querySelector('.topbar .welcome-feature-steppers button:last-child').focus()`);await p.key('Enter','Enter',13);
    assert.equal(await p.evaluate(`(()=>{const text=document.querySelector('.welcome-feature-item>span:nth-child(2)'),r=text.getBoundingClientRect(),window=text.closest('.welcome-feature-window').getBoundingClientRect();return text.scrollHeight>text.clientHeight+1||r.top<window.top-.5||r.bottom>window.bottom+.5;})()`),false,'every tip is readable');
  }
  await p.evaluate(`document.querySelector('.qwen-header-entry').focus()`);await p.key('Enter','Enter',13);
  await p.wait(`!document.querySelector('.living-welcome')&&document.querySelector('.qwen-map-launch')===null&&document.querySelector('#qwen-map-panel')?.hidden===false&&document.activeElement?.tagName==='TEXTAREA'`,'Chat replaces welcome and focuses composer');
  // Reopening Chat after discovery must select Ask, retaining the visitor's
  // draft instead of silently reopening Find. Exercise the real keyboard path.
  await p.evaluate(`document.querySelector('#qwen-map-panel [aria-label="Composer mode"] button').focus()`);await p.key('Enter','Enter',13);
  await p.wait(`document.querySelector('#qwen-map-panel textarea')?.placeholder==='Find a county, city or layer…'`,'Find mode selected');
  await p.evaluate(`document.querySelector('#qwen-map-panel textarea').focus()`);
  await p.call('Input.insertText',{text:'Ellsworth county'});
  await p.key('Escape','Escape',27);
  await p.wait(`document.querySelector('#qwen-map-panel')?.hidden&&document.activeElement===document.querySelector('.qwen-header-entry')`,'close returns focus to the same Chat button');
  await p.key('Enter','Enter',13);
  await p.wait(`document.querySelector('#qwen-map-panel')?.hidden===false&&document.activeElement?.tagName==='TEXTAREA'&&[...document.querySelectorAll('#qwen-map-panel [aria-label="Composer mode"] button')].some(button=>button.textContent==='Ask'&&button.getAttribute('aria-pressed')==='true')`,'Chat reopens Ask after Find');
  assert.equal(await p.evaluate(`document.querySelector('#qwen-map-panel textarea').value`),'Ellsworth county','changing entry mode retains the unsent draft');
  await p.key('Escape','Escape',27);
  await p.wait(`document.querySelector('#qwen-map-panel')?.hidden&&document.activeElement===document.querySelector('.qwen-header-entry')`,'reopened Chat returns focus to its header trigger');
 });
}

// Persistence acceptance uses a disposable browser profile and the real hydrated
// workspace. All provider/AI APIs are isolated by pageSession; no release occurs.
for (const [width, height] of [[1280, 800], [390, 844], [568, 320]]) {
  test(`draft workspaces preserve independent investigations at ${width}x${height}`, { timeout: 120000 }, async t => {
    const b = await browser(t), p = await pageSession(b, width, height);
    await p.open('/?motion=off', '1');
    await p.wait(`!document.querySelector('.explorer-guide')`, 'saved preference permits map access');
    const button = async (title, scope) => {
      const selector = JSON.stringify(scope), name = JSON.stringify(title);
      await p.evaluate(`(() => {
        const node = [...document.querySelectorAll(${selector} + ' button')].find(node => node.textContent.trim() === ${name});
        if (!node) throw new Error('Missing workspace control: ' + ${name});
        node.scrollIntoView({block:'center', inline:'nearest', behavior:'instant'}); node.focus();
      })()`);
      await p.key('Enter', 'Enter', 13);
      if (title === 'Return to map') await p.wait(`!document.querySelector('.primary-workspace-surface')&&document.querySelector('#map-canvas')?.contains(document.activeElement)`, 'map return focus completes before the next menu action');
    };
    const openMore = async () => {
      if (!await p.evaluate(`document.querySelector('.header-overflow-menu').open`)) {
        await p.evaluate(`document.querySelector('summary[aria-label="More site actions"]').focus()`);
        await p.key('Enter', 'Enter', 13);
      }
      await p.wait(`document.querySelector('.header-overflow-menu').open`, 'More menu open');
    };
    const openFromMap = async mode => {
      await openMore();
      await button(mode, '.header-overflow-workspaces');
      await p.wait(`document.querySelector('.primary-workspace-surface')?.dataset.workspace === ${JSON.stringify(mode.toLowerCase())}`, mode + ' mounted');
      if (mode === 'Reports') await editReport();
    };
    const switchTo = async mode => {
      await button(mode, '[aria-label="Report and story workspaces"]');
      await p.wait(`document.querySelector('.primary-workspace-surface')?.dataset.workspace === ${JSON.stringify(mode.toLowerCase())}`, mode + ' mounted');
      if (mode === 'Reports') await editReport();
    };
    const editReport = async () => {
      await button('Edit report', '.report-view-switch');
      await p.wait(`document.querySelector('.primary-workspace-surface')?.dataset.reportView === 'edit' && !!document.querySelector('.report-title-field input')`, 'the visible Edit report control opens editable fields');
    };
    const fill = async (selector, value) => {
      await p.evaluate(`document.querySelector(${JSON.stringify(selector)}).focus()`);
      await p.key('a', 'KeyA', 65, 2); await p.key('Backspace', 'Backspace', 8);
      await p.call('Input.insertText', { text: value });
      await p.wait(`document.querySelector(${JSON.stringify(selector)})?.value === ${JSON.stringify(value)}`, 'edited title rendered');
    };
    const stored = mode => p.evaluate(`JSON.parse(localStorage.getItem(${JSON.stringify('kfm-' + mode + '-draft-v2')}))`);
    const capture = async name => {
      if (!process.env.KFM_WORKSPACE_SCREENSHOTS) return;
      await p.evaluate(`document.querySelector('#primary-workspace-title')?.scrollIntoView({block:'start',behavior:'instant'})`);
      await mkdir(process.env.KFM_WORKSPACE_SCREENSHOTS, { recursive: true });
      const shot = await p.call('Page.captureScreenshot', { format: 'png' });
      await writeFile(join(process.env.KFM_WORKSPACE_SCREENSHOTS, `${width}x${height}-${name}.png`), Buffer.from(shot.data, 'base64'));
    };
    const nav = '[aria-label="Report and story workspaces"]';
    await openFromMap('Reports');
    await fill('.report-title-field input', 'QA report kept separate');
    // Leave through the actual navigation immediately after the edit, without
    // awaiting the 300 ms debounce. The unmount path must preserve the report.
    await switchTo('Stories');
    const report = await stored('report');
    assert.equal(report.title, 'QA report kept separate');
    assert.equal(await p.evaluate(`document.querySelectorAll('.story-scene-list .scene-select').length`), 1, 'new story contains one captured map scene');
    await fill('.story-draft-fields input', 'QA story kept separate');
    await switchTo('Reports');
    const story = await stored('story');
    assert.equal(story.title, 'QA story kept separate');
    assert.deepEqual(story.scenes[0].snapshot, story.baseSnapshot);
    assert.deepEqual(story.scenes[0].evidenceRefs, story.baseSnapshot.evidenceRefs);
    assert.equal(await p.evaluate(`document.querySelector('.report-title-field input').value`), report.title);
    assert.equal(await p.evaluate(`document.querySelector('.snapshot-context time').dateTime`), report.snapshot.createdAt);
    await fill('.report-title-field input', 'QA latest report before exit');
    await button('Return to map', nav);
    await p.wait(`!document.querySelector('.primary-workspace-surface')`, 'map restored');
    assert.equal((await stored('report')).title, 'QA latest report before exit');
    await openFromMap('Stories');
    assert.equal(await p.evaluate(`document.querySelector('.story-draft-fields input').value`), story.title);
    assert.equal((await stored('story')).baseSnapshot.id, story.baseSnapshot.id);
    await capture('restored-story');
    await button('Return to map', nav);
    const previousDocument = await p.evaluate('performance.timeOrigin');
    await p.call('Page.reload');
    // The old document and SSR markup both contain the map dock; history.state
    // survives reload. Wait for a new document and the real React startup
    // decision before sending keyboard input to hydrated event handlers.
    await p.wait(`performance.timeOrigin !== ${previousDocument} && document.querySelector('.atlas-studio')?.dataset.startup === 'ready' && history.state?.kfmExplorerView && !document.querySelector('.explorer-guide')`, 'new document finished startup after reload');
    try { await openFromMap('Reports'); }
    catch (error) { await capture('reload-failure'); throw error; }
    assert.equal(await p.evaluate(`document.querySelector('.report-title-field input').value`), 'QA latest report before exit');
    assert.equal((await stored('report')).snapshot.id, report.snapshot.id);
    await switchTo('Stories');
    assert.equal(await p.evaluate(`document.querySelector('.story-draft-fields input').value`), story.title);
    await switchTo('Reports');
    await button('Return to map', nav);
    // Deny only draft writes on this disposable page. Unrelated preferences and
    // existing stored drafts are untouched, and Retry must save the same text.
    await p.evaluate(`(() => {
      const original = Storage.prototype.setItem;
      window.__denyDraftWrites = true;
      Storage.prototype.setItem = function(key, value) {
        if (window.__denyDraftWrites && ['kfm-report-draft-v2','kfm-story-draft-v2'].includes(key)) throw new DOMException('Synthetic quota failure', 'QuotaExceededError');
        return original.call(this, key, value);
      };
    })()`);
    await openMore();
    await p.evaluate(`document.querySelector('.new-from-map-action').focus()`);
    await p.key('Enter', 'Enter', 13);
    await p.wait(`document.querySelector('#map-context-card')&&document.activeElement?.matches('[aria-label="Close map context composer"]')`, 'explicit composition opened and its initial focus handoff completed');
    await p.evaluate(`document.querySelector('.map-context-actions button').focus()`);
    await p.key('Enter', 'Enter', 13);
    await p.wait(`document.querySelector('.primary-workspace-surface')?.dataset.workspace === 'reports'`, 'fresh report mounted');
    const freshCapture = await p.evaluate(`document.querySelector('.snapshot-context time').dateTime`);
    assert.notEqual(freshCapture, report.snapshot.createdAt, 'explicit composition created a fresh snapshot');
    await fill('.report-title-field input', 'QA recoverable quota edit');
    await p.wait(`document.querySelector('.draft-state').textContent.includes('Browser storage unavailable')`, 'storage denial is visible');
    assert.equal((await stored('report')).title, 'QA latest report before exit');
    await openFromMap('Reports');
    assert.equal(await p.evaluate(`document.querySelector('.report-title-field input').value`), 'QA recoverable quota edit');
    assert.equal(await p.evaluate(`document.querySelector('.snapshot-context time').dateTime`), freshCapture, 'same-mode header action keeps the active unsaved snapshot');
    await capture('storage-recovery');
    await p.evaluate(`window.__denyDraftWrites = false`);
    await button('Retry saving', '.draft-state');
    await p.wait(`document.querySelector('.draft-state').textContent.includes('Saved on this device')`, 'retry saved editable draft');
    assert.equal((await stored('report')).title, 'QA recoverable quota edit');
    assert.equal((await stored('story')).title, story.title, 'saving the report never replaces the story');
    assert.match(await p.evaluate(`document.querySelector('.draft-state').textContent`), /DRAFT · NOT PUBLISHED/);
    assert.ok(await p.evaluate(`document.documentElement.scrollWidth <= innerWidth + 1`), 'workspace has no document horizontal overflow');
  });
}


// The welcome reuses the pinned local reference; provider/AI I/O stays isolated.
for(const [width,height] of [[1440,960],[390,844]]) test(`aviation welcome zones and modes at ${width}x${height}`,{timeout:90000},async t=>{
 const b=await browser(t),p=await pageSession(b,width,height);
 await p.open('/?motion=off');await readyWelcome(p);
 await p.evaluate(`document.querySelector('.topic-aviation').focus()`);
 await p.wait(`document.querySelector('.welcome-preview-brief .welcome-aviation-status')?.textContent.includes('NASR 2026-10-29')`,'startup focus alone shows the zone hint without opening a demonstration');
 assert.equal(await p.evaluate(`document.querySelectorAll('.welcome-dialog-backdrop,.welcome-layer-demo').length`),0,'the zones are available in the startup view itself');
 assert.equal(await p.evaluate(`document.querySelector('.living-welcome').dataset.fullscreen`),'false');
 const enter=async selector=>{await p.evaluate(`document.querySelector(${JSON.stringify(selector)}).focus()`);await p.key('Enter','Enter',13);};
 await enter('.topic-preview-aviation');await openStageNotes(p);await p.wait(`!!document.querySelector('.welcome-aviation-tools')`,'aviation tools have a real destination');
 await enter('.welcome-aviation-tools button');
 await p.wait(`document.querySelector('.welcome-layer-demo .welcome-aviation-status')?.textContent.includes('NASR 2026-10-29')`,'digest-checked pinned snapshot ready');
 assert.equal(await p.evaluate(`document.querySelectorAll('.domain-stage-map canvas').length`),1,'one preview map for all modes');
 for(const index of [1,2,0]){
  await enter('.welcome-layer-demo .welcome-aviation-modes button:nth-child('+(index+1)+')');
  assert.equal(await p.evaluate(`document.querySelector('.welcome-layer-demo .welcome-aviation-modes button:nth-child(${index+1})').getAttribute('aria-pressed')`),'true');
 }
 await enter('.welcome-layer-demo .welcome-aviation-notes summary');
 assert.match(await p.evaluate(`document.querySelector('.welcome-layer-demo .welcome-aviation-notes').textContent`),/201 airspace volumes; not all are visible.*Only zones are previewed here/);
 await enter('.welcome-layer-demo-actions button');
 await p.wait(`document.querySelector('.welcome-layer-demo .welcome-aviation-status')?.textContent.includes('hidden')`,'comparison hides overlay without claiming unavailable');
 await enter('.welcome-layer-demo-actions button');
 assert.equal(await p.evaluate(`document.documentElement.scrollWidth<=innerWidth`),true);
 await p.key('Escape','Escape',27);await p.wait(`document.querySelector('.living-welcome')?.dataset.fullscreen==='false'`,'Escape returns to categories');
});

test('water animation stays opt-in and does not follow the visitor into unrelated topics',{timeout:90000},async t=>{
 const b=await browser(t),p=await pageSession(b,1280,900);
 const enter=async selector=>{await p.evaluate(`document.querySelector(${JSON.stringify(selector)}).focus()`);await p.key('Enter','Enter',13);};
 await p.open('/?topic=water','1',`localStorage.setItem('kfm-scene-effects-v1',JSON.stringify({waterFlow:true,sunSync:false}));`);
 await p.wait(`!!document.querySelector('.topic-map-look button')`,'Water guide offers its real map');await enter('.topic-map-look button');
 await p.wait(`[...document.querySelectorAll('.category-map-dock-tool')].some(button=>button.textContent==='Show river flow')`,'old saved flow does not auto-start');
 await p.evaluate(`[...document.querySelectorAll('.category-map-dock-tool')].find(button=>button.textContent==='Show river flow').focus()`);await p.key('Enter','Enter',13);
 await p.wait(`!![...document.querySelectorAll('.category-map-dock-tool')].some(button=>button.textContent==='Hide river flow')`,'explicit Water toggle still works');
 await p.evaluate(`[...document.querySelectorAll('.category-map-dock button')].find(button=>button.textContent==='Layers for this map').focus()`);await p.key('Enter','Enter',13);
 await p.wait(`!!document.querySelector('[aria-label="Layer topic"]')`,'layer topic control available');
 await p.evaluate(`(()=>{const select=document.querySelector('[aria-label="Layer topic"]');select.value='aviation';select.dispatchEvent(new Event('change',{bubbles:true}));})()`);
 await p.wait(`JSON.parse(localStorage.getItem('kfm-scene-effects-v1')).waterFlow===false`,'leaving Water shuts off inherited animation');
 await enter('[aria-label="Effects & rendering"]');
 for(const name of ['Cinematic','Natural']){
  await p.evaluate(`(()=>{const button=[...document.querySelectorAll('.scene-panel-body button')].find(node=>node.textContent.startsWith(${JSON.stringify(name)}));button.focus();})()`);await p.key('Enter','Enter',13);
  assert.equal(await p.evaluate(`JSON.parse(localStorage.getItem('kfm-scene-effects-v1')).waterFlow`),false,'visual preset does not enable flow');
 }
});
