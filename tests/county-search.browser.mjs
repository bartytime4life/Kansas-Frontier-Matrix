// Real, hydrated application acceptance. Run explicitly against a built loopback
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
const countyPath = '/api/live-context?feed=census-counties';
const syntheticFeature = (name, geoid, west) => ({
  type: 'Feature', id: geoid,
  properties: { name, geoid, featureId: `us-census-county-${geoid}`, vintage: '2020' },
  geometry: { type: 'Polygon', coordinates: [[[west, 38.5], [west + .2, 38.5], [west + .2, 38.7], [west, 38.7], [west, 38.5]]] },
});
const features = [syntheticFeature('Ellsworth', '20053', -98.5), syntheticFeature('Saline', '20169', -97.8)];
const payload = (state, rows) => ({
  feed: 'census-counties', state, retrievedAt: new Date().toISOString(), upstreamUpdatedAt: null,
  featureCount: rows.length, data: { type: 'FeatureCollection', features: rows },
  source: 'SYNTHETIC BROWSER FIXTURE ONLY', limitation: 'Invented test geometry; no evidence admission.',
  truncated: state === 'partial',
});
const emptyStyle = { version: 8, sources: {}, layers: [{ id: 'synthetic-background', type: 'background', paint: { 'background-color': '#172832' } }] };

async function browser(t) {
  const profile = await mkdtemp(join(tmpdir(), 'kfm-county-browser-'));
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

async function pageSession(browser, width, height) {
  const { targetId } = await browser.call('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await browser.call('Target.attachToTarget', { targetId, flatten: true });
  const call = (method, params) => browser.call(method, params, sessionId);
  const errors = [], held = [];
  let mode = 'held', fixture = payload('ready', features), httpStatus = 200;
  const fulfill = (requestId, body, responseCode = 200) => call('Fetch.fulfillRequest', {
    requestId, responseCode,
    responseHeaders: [{ name: 'Content-Type', value: 'application/json' }, { name: 'Cache-Control', value: 'no-store' }],
    body: Buffer.from(JSON.stringify(body)).toString('base64'),
  });
  const listener = message => {
    if (message.sessionId !== sessionId || message.method !== 'Fetch.requestPaused') return;
    void (async () => {
      const { requestId, request } = message.params;
      const url = new URL(request.url);
      if (url.origin === origin.origin && url.pathname + url.search === countyPath) {
        if (mode === 'held') held.push(requestId);
        else await fulfill(requestId, fixture, httpStatus);
      } else if (url.origin === origin.origin && url.pathname.startsWith('/api/') && url.pathname !== '/api/build') {
        // No provider, AI, account, storage or release operation is called.
        await fulfill(requestId, { error: 'Synthetic browser isolation: source unavailable.' }, 503);
      } else if (url.origin !== origin.origin && /^https?:/.test(url.protocol)) {
        if (url.pathname.includes('/styles/') || url.pathname.endsWith('/style.json')) await fulfill(requestId, emptyStyle);
        else await call('Fetch.failRequest', { requestId, errorReason: 'BlockedByClient' });
      } else await call('Fetch.continueRequest', { requestId });
    })().catch(error => errors.push(String(error)));
  };
  browser.listeners.add(listener);
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
  const wait = async (expression, label, timeout = 30000) => {
    const deadline = Date.now() + timeout; let last;
    while (Date.now() < deadline) {
      if (errors.length) throw new Error(errors.join('\n'));
      last = await evaluate(`Boolean(${expression})`);
      if (last) return last;
      await pause(50);
    }
    throw new Error(`${label}: ${JSON.stringify(last)}; ${await evaluate(`JSON.stringify({query:document.querySelector('#qwen-map-panel textarea')?.value,status:document.querySelector('#global-search-results')?.innerText,active:document.activeElement?.outerHTML.slice(0,500),drawer:document.querySelector('.evidence-drawer')?.dataset.open,title:document.querySelector('.evidence-drawer h2')?.textContent})`)}`);
  };
  const key = async (key, code, windowsVirtualKeyCode, modifiers = 0) => {
    await call('Input.dispatchKeyEvent', { type: 'rawKeyDown', key, code, windowsVirtualKeyCode, modifiers });
    if (key === 'Enter') await call('Input.dispatchKeyEvent', { type: 'char', key, code, windowsVirtualKeyCode, text: '\r', unmodifiedText: '\r' });
    await call('Input.dispatchKeyEvent', { type: 'keyUp', key, code, windowsVirtualKeyCode, modifiers });
  };
  const fill = async value => {
    await evaluate('document.querySelector("#qwen-map-panel textarea").focus()');
    await key('a', 'KeyA', 65, 2);
    await key('Backspace', 'Backspace', 8);
    if (value) await call('Input.insertText', { text: value });
    await wait(`document.querySelector('#qwen-map-panel textarea').value === ${JSON.stringify(value)}`, 'input updated');
  };
  const snapshot = () => evaluate(`(() => {
    const input = document.querySelector('#qwen-map-panel textarea');
    const popup = document.querySelector('#global-search-results');
    return { query: input?.value, busy: input?.getAttribute('aria-busy'), popup: Boolean(popup),
      status: popup?.querySelector('[role=status]')?.textContent ?? '',
      rows: [...(popup?.querySelectorAll('button') ?? [])].map(row => ({ title: row.querySelector('strong')?.textContent, text: row.textContent })) };
  })()`);
  const open = async (nextMode = 'held', nextFixture = payload('ready', features), status = 200) => {
    mode = nextMode; fixture = nextFixture; httpStatus = status; held.length = 0;
    await call('Page.navigate', { url: origin.href });
    await wait(`document.querySelector('#qwen-map-panel textarea') && document.querySelector('.map-chrome-dock')`, 'application mounted');
    const deadline = Date.now() + 30000;
    while (!held.length && Date.now() < deadline) { if (errors.length) throw new Error(errors.join('\n')); await pause(50); }
    assert.ok(held.length, 'hydrated application started its county request');
    // New disposable profiles see the normal first-visit guide. Close it with
    // native mouse input before typing, so its autofocus cannot steal keys.
    const close = await evaluate(`(() => {const b=document.querySelector('.explorer-guide-close'); if(!b)return null;const r=b.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2};})()`);
    if (close) {
      await call('Input.dispatchMouseEvent', {type:'mousePressed',button:'left',clickCount:1,...close});
      await call('Input.dispatchMouseEvent', {type:'mouseReleased',button:'left',clickCount:1,...close});
      await wait(`!document.querySelector('.explorer-guide')`, 'first-visit guide closed');
    }
    const find = await evaluate(`(() => {const r=document.querySelector('.atlas-scope-control').getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2};})()`);
    await call('Input.dispatchMouseEvent', {type:'mousePressed',button:'left',clickCount:1,...find});
    await call('Input.dispatchMouseEvent', {type:'mouseReleased',button:'left',clickCount:1,...find});
    await wait(`!document.querySelector('#qwen-map-panel').hidden`, 'unified Find composer opened');
    // A real key must reach React before acceptance begins; no private hooks.
    await fill('hydration probe');
    await wait(`document.querySelector('#global-search-results [role=status]')`, 'search hydration');
    await fill('');
  };
  const release = async (body, status = 200) => {
    assert.ok(held.length, 'county request was intercepted, not merely an idle UI');
    mode = 'respond'; fixture = body; httpStatus = status;
    for (const requestId of held.splice(0)) await fulfill(requestId, body, status);
  };
  return { call, evaluate, wait, key, fill, snapshot, open, release, held, errors,
    close: async () => { browser.listeners.delete(listener); await browser.call('Target.closeTarget', { targetId }); },
  };
}

for (const [width, height] of [[1366, 768], [390, 844], [375, 667]]) {
  test(`hydrated county search at ${width}x${height}`, { timeout: 240000 }, async t => {
    const b = await browser(t), p = await pageSession(b, width, height);
    t.after(async () => { try { await p.close(); } catch { /* Browser cleanup may already have closed its targets. */ } });
    await t.test('slow feed, rapid edits and current-query arrival retain usable non-county results', async () => {
      await p.open();
      await p.wait(`document.querySelector('#qwen-map-panel textarea')?.getAttribute('aria-busy') === 'false'`, 'blank search quiet');
      await p.fill('water');
      await p.wait(`document.querySelector('#global-search-results [role=status]')?.textContent === 'Loading county matches…'`, 'real pending county feed');
      assert.ok(p.held.length);
      assert.deepEqual(await p.evaluate(`(() => {const s=document.querySelector('#global-search-results [role=status]');return [s.getAttribute('aria-live'),s.getAttribute('aria-atomic')];})()`), ['polite', 'true']);
      assert.ok((await p.snapshot()).rows.length > 0, 'layer/source matches remain usable while county request is held');
      for (const query of ['Ellsworth', 'Saline', 'Ellsworth', 'Saline']) await p.fill(query);
      await p.release(payload('ready', features));
      await p.wait(`document.querySelector('#global-search-results button strong')?.textContent === 'Saline County'`, 'arrival applies to latest query');
      assert.deepEqual((await p.snapshot()).rows.map(row => row.title), ['Saline County']);
      await p.fill('Ellsworth');
      await p.wait(`document.querySelector('#global-search-results button strong')?.textContent === 'Ellsworth County'`, 'first settled query');
      // Observe actual DOM commits during debounce, not an extracted helper.
      await p.evaluate(`window.__countySearchFrames = []; window.__countySearchObserver = new MutationObserver(() => {
        window.__countySearchFrames.push({query: document.querySelector('#qwen-map-panel textarea').value,
          titles: [...document.querySelectorAll('#global-search-results button strong')].map(row => row.textContent)});
      }); window.__countySearchObserver.observe(document.querySelector('#qwen-map-panel'), {subtree:true, childList:true, attributes:true, characterData:true});`);
      await p.fill('Saline');
      await p.wait(`document.querySelector('#global-search-results button strong')?.textContent === 'Saline County'`, 'changed settled query');
      const frames = await p.evaluate('window.__countySearchObserver.disconnect(); window.__countySearchFrames');
      assert.ok(frames.some(frame => frame.query === 'Saline' && frame.titles.length === 0), 'debounce hides obsolete rows');
      assert.ok(frames.every(frame => frame.query !== 'Saline' || !frame.titles.includes('Ellsworth County')), 'no stale county presented as current');
      t.diagnostic(JSON.stringify({ width, scenario: 'rapid-query', frames }));
    });
    await t.test('completed miss, clear, whitespace, escaping and keyboard county investigation', async () => {
      await p.open();
      await p.release(payload('ready', features));
      await p.wait(`document.querySelector('#qwen-map-panel textarea')?.getAttribute('aria-busy') === 'false'`, 'ready inventory before completed-search cases');
      await p.fill('zzzzzz no county');
      await p.wait(`document.querySelector('#global-search-results [role=status]')?.textContent.startsWith('No matches for')`, 'settled completed miss');
      await p.fill('<img src=x onerror=alert(1)>');
      await p.wait(`document.querySelector('#global-search-results [role=status]')?.textContent.includes('<img src=x')`, 'escaped query text');
      assert.equal(await p.evaluate(`Boolean(document.querySelector('#global-search-results img'))`), false);
      for (const blank of ['', '   ']) { await p.fill(blank); assert.equal((await p.snapshot()).popup, false); }
      await p.fill('Ellsworth');
      await p.wait(`document.querySelector('#global-search-results button strong')?.textContent === 'Ellsworth County'`, 'county available');
      assert.match((await p.snapshot()).rows[0].text, /2020.*source context, not KFM evidence/);
      const layout = await p.evaluate(`(() => {const row=document.querySelector('#global-search-results button'), box=row.getBoundingClientRect(), body=row.closest('[aria-label="Place and layer discovery"]'), bounds=body.getBoundingClientRect(), composer=document.querySelector('#qwen-map-panel textarea').getBoundingClientRect();return {left:box.left,right:box.right,top:box.top,bottom:box.bottom,width:innerWidth,height:innerHeight,overflow:document.documentElement.scrollWidth>innerWidth+1,body:{top:bounds.top,bottom:bounds.bottom,clientHeight:body.clientHeight,scrollHeight:body.scrollHeight,scrollTop:body.scrollTop},composer:{top:composer.top,bottom:composer.bottom}};})()`);
      assert.ok(layout.left >= 0 && layout.right <= width + 1 && layout.top >= 0 && layout.bottom <= height, JSON.stringify(layout));
      assert.ok(layout.top >= layout.body.top && layout.bottom <= layout.body.bottom + 1, 'first result is visible inside its actual scroll region: '+JSON.stringify(layout));
      assert.ok(layout.composer.top >= 0 && layout.composer.bottom <= height, 'composer stays in the viewport: '+JSON.stringify(layout));
      assert.equal(layout.overflow, false, 'no horizontal overflow');
      const beforeTime = await p.evaluate(`document.querySelector('.time-bar select')?.value ?? document.querySelector('select[aria-label="Preview year or earlier era"]')?.value`);
      assert.match(beforeTime ?? '', /^\d+$/, 'actual display time is observed before selection');
      await p.key('ArrowDown', 'ArrowDown', 40);
      await p.wait(`document.activeElement?.closest('#global-search-results') && document.activeElement.textContent.includes('Ellsworth County')`, 'ArrowDown reaches explicit result');
      await p.key('Enter', 'Enter', 13);
      await p.wait(`document.querySelector('.evidence-drawer[data-open="true"] h2')?.textContent.includes('Ellsworth')`, 'county opens Evidence Drawer');
      const investigation = await p.evaluate(`(() => {const d=document.querySelector('.evidence-drawer');return {text:d.innerText,state:d.dataset.state,modal:d.getAttribute('aria-modal'),time:document.querySelector('.time-bar select')?.value ?? document.querySelector('select[aria-label="Preview year or earlier era"]')?.value,search:document.querySelector('#qwen-map-panel textarea').value};})()`);
      assert.match(investigation.text, /Census/i);
      assert.match(investigation.text, /context/i);
      assert.notEqual(investigation.state, 'ANSWER');
      assert.equal(investigation.time, beforeTime);
      assert.equal(investigation.search, '');
      if (width < 600) assert.equal(investigation.modal, 'true');
      await p.key('Escape', 'Escape', 27);
      await p.wait(`document.querySelector('.evidence-drawer')?.dataset.open === 'false' && document.activeElement === document.querySelector('#qwen-map-panel textarea')`, 'Escape returns search focus');
      if (width < 600) {
        await p.key('Escape', 'Escape', 27);
        await p.wait(`document.querySelector('#qwen-map-panel')?.hidden === true && document.activeElement?.matches('.atlas-scope-control')`, 'a separate Escape closes Chat and returns to Find & ask');
      }
      t.diagnostic(JSON.stringify({ width, scenario: 'investigation', layout, state: investigation.state, time: beforeTime }));
    });
    await t.test('failed county response explains coverage and preserves layer/source matches', async () => {
      await p.open(); await p.fill('Ellsworth');
      await p.wait(`document.querySelector('#global-search-results [role=status]')?.textContent === 'Loading county matches…'`, 'pending before failure');
      await p.release({ error: 'Synthetic county outage.' }, 503);
      await p.wait(`document.querySelector('#global-search-results [role=status]')?.textContent.startsWith('County search is unavailable.')`, 'outage feedback');
      assert.deepEqual((await p.snapshot()).rows, []);
      await p.fill('water');
      await p.wait(`document.querySelector('#global-search-results [role=status]')?.textContent === 'County search is unavailable. Showing available matches.'`, 'available matches on outage');
      assert.ok((await p.snapshot()).rows.length > 0);
      assert.equal((await p.snapshot()).busy, 'false');
    });
    await t.test('partial and empty responses cannot assert complete no-match', async () => {
      await p.open(); await p.fill('Ellsworth');
      await p.wait(`document.querySelector('#global-search-results [role=status]')?.textContent === 'Loading county matches…'`, 'pending before partial');
      await p.release(payload('partial', features.slice(0, 1)));
      await p.wait(`document.querySelector('#global-search-results [role=status]')?.textContent === 'County search has limited coverage.'`, 'partial coverage');
      assert.equal((await p.snapshot()).rows[0]?.title, 'Ellsworth County');
      await p.fill('Saline');
      await p.wait(`document.querySelector('#global-search-results [role=status]')?.textContent === 'County search has limited coverage.' && document.querySelectorAll('#global-search-results button').length === 0`, 'partial miss remains bounded');
      await p.open(); await p.fill('Ellsworth');
      await p.wait(`document.querySelector('#global-search-results [role=status]')?.textContent === 'Loading county matches…'`, 'pending before empty');
      await p.release(payload('empty', []));
      await p.wait(`document.querySelector('#global-search-results [role=status]')?.textContent === 'No counties are available to search.'`, 'empty inventory');
      const snapshot = await p.snapshot(); assert.equal(snapshot.busy, 'false'); assert.deepEqual(snapshot.rows, []);
      assert.doesNotMatch(snapshot.status, /No matches/);
      assert.deepEqual(p.errors, []);
    });
  });
}
