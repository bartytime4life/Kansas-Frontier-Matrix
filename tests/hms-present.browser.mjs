// Hydrated loopback race acceptance. Invented HMS fixtures are never provider evidence.
import assert from 'node:assert/strict';
import test from 'node:test';
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
const origin = new URL(process.env.KFM_NODE_TEST_ORIGIN ?? 'http://127.0.0.1:5182');
assert.equal(origin.protocol, 'http:');
assert.ok(['127.0.0.1', 'localhost', '[::1]'].includes(origin.hostname));
assert.equal(origin.pathname, '/');
assert.equal(origin.search + origin.hash + origin.username + origin.password, '');
const feed = 'noaa-hms-smoke', day = '2026-10-01';
const fixture = dated => ({ feed, state: 'ready', featureCount: 1, retrievedAt: dated ? '2026-10-02T12:00:00Z' : '2026-10-21T12:00:00Z',
  source: 'SYNTHETIC HMS BROWSER FIXTURE', limitation: 'Invented geometry; no evidence admission.', upstreamUpdatedAt: null, truncated: false,
  smokeCoverage: { day: dated ? day : null, firstDay: '2005-08-05', availableDays: [day], missingDays: [] },
  data: { type: 'FeatureCollection', features: [{ type: 'Feature', id: dated ? 'archive' : 'current', geometry: { type: 'Polygon', coordinates: [[[-98.5,38.5],[-98.3,38.5],[-98.3,38.7],[-98.5,38.7],[-98.5,38.5]]] },
    properties: { id: dated ? 'archive' : 'current', title: 'SYNTHETIC HMS FIXTURE', density: 'Light', start: dated ? day+'T12:00:00Z' : '2026-10-21T11:00:00Z', end: dated ? day+'T23:00:00Z' : '2026-10-21T23:00:00Z' } }] },
});
for (const exit of ['advanced Present', 'compact Present', 'restored Present']) test(`pending HMS publication is retired by ${exit}`, { timeout: 90000 }, async t => {
  const browser = await chromium.launch({ executablePath: process.env.KFM_TEST_CHROME, headless: true, args: ['--no-sandbox','--enable-unsafe-swiftshader','--use-angle=swiftshader','--disable-dev-shm-usage'] });
  const page = await browser.newPage({ viewport: { width: 1400, height: 1000 }, reducedMotion: 'reduce' });
  page.setDefaultTimeout(15000);
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  t.after(async () => { await page.screenshot({ path: `/tmp/kfm-hms-${exit.replaceAll(' ', '-')}.png` }).catch(() => {}); await browser.close(); });
  await page.addInitScript(({ feed, day, archived, current }) => {
    localStorage.setItem('kfm.explorer.guide.dismissed.v2','1');
    const original = window.fetch;
    window.__hmsTest = { requests: [], pending: false, released: false, aborted: false, holdCurrent: false, currentWaiters: [] };
    window.fetch = function(input, init) {
      const url = new URL(input instanceof Request ? input.url : String(input), location.href);
      if (url.origin !== location.origin && (url.pathname.includes('/styles/') || url.pathname.endsWith('/style.json')))
        return Promise.resolve(Response.json({ version: 8, sources: {}, layers: [{ id: 'background', type: 'background', paint: { 'background-color': '#172832' } }] }));
      if (url.origin === location.origin && url.pathname === '/api/live-context' && url.searchParams.get('feed') === feed) {
        const dated = url.searchParams.has('day'); window.__hmsTest.requests.push(dated ? 'archive' : 'current');
        if (dated) return new Promise(resolve => {
          window.__hmsTest.pending = true; window.__hmsTest.holdCurrent = true;
          const signal = init?.signal ?? (input instanceof Request ? input.signal : null);
          signal?.addEventListener('abort', () => { window.__hmsTest.aborted = true; }, { once: true });
          // Deliberately ignore abort; cache and ownership guards must reject this response.
          window.__hmsTest.release = () => { window.__hmsTest.released = true; resolve(Response.json(archived)); };
        });
        if (window.__hmsTest.holdCurrent) return new Promise(resolve => window.__hmsTest.currentWaiters.push(() => resolve(Response.json(current))));
        return Promise.resolve(Response.json(current));
      }
      return original.call(this,input,init);
    };
  }, { feed, day, archived: fixture(true), current: fixture(false) });
  await page.route('**/*', route => {
    const url = new URL(route.request().url());
    if (url.origin !== origin.origin) return route.abort();
    if (!url.pathname.startsWith('/api/') || url.pathname === '/api/build') return route.continue();
    return route.fulfill({ status: 503, json: { error: 'Unrelated provider intentionally unavailable in HMS fixture' } });
  });
  const params = new URLSearchParams({ ctx: feed, l: '', t: '2026', layerView: 'selected', topic: 'all' });
  await page.goto(new URL('?'+params,origin).href, { waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => history.state?.kfmExplorerView);
  // The catalog's actual source controls start the independent HmsFrameCache path.
  await page.getByRole('button', { name: /Layers/ }).first().click();
  const playback = page.locator('.hms-playback');
  await playback.locator('xpath=ancestor::details').evaluate(el => { el.open = true; });
  await playback.getByRole('button', { name: 'Check / retry day', exact: true }).waitFor({ state: 'visible' });
  await page.waitForFunction(() => !document.querySelector('.hms-playback button')?.disabled);
  await page.getByLabel('HMS playback day', { exact: true }).fill(day);
  await playback.getByRole('button', { name: 'Check / retry day', exact: true }).click();
  await page.waitForFunction(() => window.__hmsTest.pending);
  const before = new URLSearchParams(await page.evaluate(() => history.state.kfmExplorerView));
  // Close Layers without destroying the mounted HMS component.
  await page.getByRole('button', { name: /Layers/ }).first().click();
  if (exit === 'restored Present') {
    await page.evaluate(() => {
      const p = new URLSearchParams(history.state.kfmExplorerView); p.delete('ctxd'); p.delete('calendar'); p.set('t','2026');
      history.replaceState({ ...history.state, kfmExplorerView: p.toString() }, '', location.href);
      dispatchEvent(new PopStateEvent('popstate', { state: history.state }));
    });
  } else {
    await page.locator('.compact-time-emblem').focus(); await page.keyboard.press('Enter');
    if (exit === 'advanced Present') { await page.locator('.compact-time-legacy > summary').click(); await page.locator('.timeline-reset').click(); }
    else await page.locator('.compact-time-present').click();
  }
  await page.waitForFunction(() => !new URLSearchParams(history.state?.kfmExplorerView).get('ctxd'));
  const canceledBeforeRelease = await page.evaluate(() => window.__hmsTest.aborted);
  await page.evaluate(() => window.__hmsTest.release());
  await page.waitForTimeout(1000);
  const after = new URLSearchParams(await page.evaluate(() => history.state.kfmExplorerView));
  assert.equal(after.get('ctxd') ?? '', '', 'delayed archive cannot restore historical source identity'); assert.equal(after.get('calendar'),null); assert.equal(after.get('ctx'),feed);
  for (const key of ['c','z','b','p','ctxo','l']) assert.equal(after.get(key),before.get(key),'preserve '+key);
  await page.evaluate(() => { window.__hmsTest.holdCurrent = false; window.__hmsTest.currentWaiters.splice(0).forEach(resolve => resolve()); });
  await page.getByRole('button', { name: /Layers/ }).first().click();
  await playback.locator('xpath=ancestor::details').evaluate(el => { el.open = true; });
  await page.waitForFunction(() => document.querySelector('.hms-playback small')?.textContent.includes('retrieved 2026-10-21 12:00 UTC'));
  assert.match(await playback.locator('small').first().textContent(), /latest rolling publication window/);
  assert.equal(canceledBeforeRelease, true, 'exit cancels acquisition before the delayed response');
  assert.deepEqual(errors, []);
  t.diagnostic(JSON.stringify({ exit, ...await page.evaluate(() => ({ requests: window.__hmsTest.requests, aborted: window.__hmsTest.aborted, released: window.__hmsTest.released })) }));
});
