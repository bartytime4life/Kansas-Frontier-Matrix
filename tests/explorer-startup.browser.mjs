// Real, hydrated startup acceptance. Run explicitly against a built loopback
// candidate; this file is deliberately outside the ordinary *.test.mjs suite.
import assert from 'node:assert/strict';
import test from 'node:test';
import { spawn } from 'node:child_process';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

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
  const pending = new Map(), listeners = new Set();
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
    try { await call('Browser.close'); } catch { child.kill(); }
    if (child.exitCode === null) await Promise.race([new Promise(resolve => child.once('exit', resolve)), pause(2000)]);
    if (child.exitCode === null) child.kill('SIGKILL');
    await rm(profile, { recursive: true, force: true, maxRetries: 3, retryDelay: 100 });
  });
  t.diagnostic(JSON.stringify(await call('Browser.getVersion')));
  return { call, listeners };
}

async function pageSession(b, width, height) {
  const { targetId } = await b.call('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await b.call('Target.attachToTarget', { targetId, flatten: true });
  const call = (method, params = {}) => b.call(method, params, sessionId);
  const errors = [];
  const listener = message => {
    if (message.sessionId !== sessionId || message.method !== 'Fetch.requestPaused') return;
    void (async () => {
      const { requestId, request } = message.params, url = new URL(request.url);
      if (url.origin === origin.origin && url.pathname.startsWith('/api/') && url.pathname !== '/api/build') {
        await call('Fetch.fulfillRequest', { requestId, responseCode: 503, responseHeaders: [{ name: 'Content-Type', value: 'application/json' }], body: Buffer.from('{"error":"Isolated navigation test: provider unavailable"}').toString('base64') });
      } else if (url.origin !== origin.origin && /^https?:/.test(url.protocol)) {
        if (url.pathname.includes('/styles/') || url.pathname.endsWith('/style.json')) {
          const style = { version: 8, sources: {}, layers: [{ id: 'test-background', type: 'background', paint: { 'background-color': '#172832' } }] };
          await call('Fetch.fulfillRequest', { requestId, responseCode: 200, body: Buffer.from(JSON.stringify(style)).toString('base64') });
        } else await call('Fetch.failRequest', { requestId, errorReason: 'BlockedByClient' });
      } else await call('Fetch.continueRequest', { requestId });
    })().catch(error => errors.push(String(error)));
  };
  b.listeners.add(listener);
  await call('Page.enable');
  await call('Runtime.enable');
  await call('Network.enable');
  await call('Network.setCacheDisabled', { cacheDisabled: true });
  await call('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: width < 600 });
  await call('Fetch.enable', { patterns: [{ urlPattern: '*' }] });
  const evaluate = async expression => {
    const result = await call('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
    if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
    return result.result.value;
  };
  const wait = async (expression, label) => {
    const deadline = Date.now() + 20000;
    while (Date.now() < deadline) {
      assert.deepEqual(errors, []);
      if (await evaluate(`Boolean(${expression})`)) return;
      await pause(50);
    }
    throw new Error(`${label}: ${await evaluate(`JSON.stringify({url:location.href, guide:!!document.querySelector('.explorer-guide'), topic:document.querySelector('[aria-label="Layer topic"]')?.value, active:document.activeElement?.outerHTML.slice(0,300)})`)}`);
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
  return { call, evaluate, wait, key, open, unobstructed };
}

for (const [width, height] of [[1366, 768], [390, 844]]) {
  test(`startup destinations at ${width}x${height}`, { timeout: 240000 }, async t => {
    const b = await browser(t), p = await pageSession(b, width, height);
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
      assert.equal(await p.evaluate(`document.querySelector('.explorer-guide input').checked`), false);
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
      await p.wait(`document.querySelector('.explorer-guide input')?.checked`, 'manual help retains opt-out');
      await p.key('Escape', 'Escape', 27);
      assert.equal(await p.evaluate(`localStorage.getItem('kfm.explorer.guide.dismissed.v2')`), '1');
      await p.open('/', null, `localStorage.setItem('kfm.explorer.guide.dismissed.v1','1');`);
      await p.wait(`document.querySelector('.explorer-guide')`, 'legacy preference does not imply v2 opt-out');
      await p.open('/', null, `Object.defineProperty(Storage.prototype,'getItem',{value(){throw new DOMException('Storage blocked','SecurityError')}});`);
      await p.wait(`document.querySelector('.explorer-guide')`, 'blocked storage preserves welcome');
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

