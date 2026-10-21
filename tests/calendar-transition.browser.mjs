// Explicit hydrated loopback acceptance; requires Playwright on NODE_PATH and
// KFM_TEST_CHROME (or chromium). Fixtures are not provider/WebGL data validation.
import assert from 'node:assert/strict';
import test from 'node:test';
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
const origin = new URL(process.env.KFM_NODE_TEST_ORIGIN ?? 'http://127.0.0.1:5182');
assert.equal(origin.protocol, 'http:');
assert.ok(['127.0.0.1','localhost','[::1]'].includes(origin.hostname));
assert.equal(origin.pathname, '/');
assert.equal(origin.search + origin.hash + origin.username + origin.password, '');
const day = '2026-10-01';
const calendar = { day, start: day, end:'2026-10-21',step:'days',before:null,showing:'B' };
const feed = 'usgs-earthquakes';
const fixture = dated => ({feed,state:'ready',featureCount:1,retrievedAt:dated?'2026-10-02T12:00:00Z':'2026-10-21T12:00:00Z',sourceDay:dated?day:undefined,data:{type:'FeatureCollection',features:[{type:'Feature',id:dated?'archive':'current',geometry:{type:'Point',coordinates:[-98,38]},properties:{id:dated?'archive':'current',title:dated?'ARCHIVE FIXTURE':'CURRENT FIXTURE',magnitude:2,time:dated?'2026-10-01T12:00:00Z':'2026-10-21T11:00:00Z'}}]}});
for (const exit of ['advanced Present','compact Present','annual step']) test(`hydrated ${exit} retires same-year history and preserves selected layers`, {timeout:90000}, async t => {
  const browser = await chromium.launch({ executablePath: process.env.KFM_TEST_CHROME ?? '/usr/bin/chromium', headless:true,args:['--enable-unsafe-swiftshader','--use-angle=swiftshader','--disable-dev-shm-usage'] });

  const page = await browser.newPage({ viewport:{width:1200,height:800}, reducedMotion:'reduce' });
  page.setDefaultTimeout(15000);
  page.setDefaultNavigationTimeout(15000);
  page.on('pageerror', error => t.diagnostic('pageerror: '+error.message));
  const requests = []; let releaseCurrent;
  const gate = new Promise(resolve => { releaseCurrent = resolve; });
  t.after(async () => { releaseCurrent(); await page.screenshot({path:'/tmp/kfm-calendar-browser.png'}).catch(()=>{}); await browser.close(); });
  await page.addInitScript(() => {
    localStorage.setItem('kfm.explorer.guide.dismissed.v2','1');
    const original = window.fetch;
    window.fetch = function(input, init) {
      const url = new URL(input instanceof Request ? input.url : String(input),location.href);
      if (url.origin !== location.origin && (url.pathname.includes('/styles/') || url.pathname.endsWith('/style.json')))
        return Promise.resolve(Response.json({version:8,sources:{},layers:[{id:'background',type:'background',paint:{'background-color':'#172832'}}]}));
      return original.call(this,input,init);
    };
  });
  await page.route('**/*', async route => {
    const url = new URL(route.request().url());
    if (url.origin !== origin.origin) return route.abort();
    if (!url.pathname.startsWith('/api/')) return route.continue();
    if (url.pathname === '/api/live-context' && url.searchParams.get('feed') === feed) {
      const dated = url.searchParams.has('day'); requests.push(dated?'archive':'current');
      if (!dated) await Promise.race([gate,new Promise(resolve=>setTimeout(resolve,10000))]);
      return route.fulfill({json:fixture(dated)});
    }
    return route.fulfill({status:503,json:{error:'Unrelated provider intentionally unavailable in calendar fixture'}});
  });
  const params = new URLSearchParams({ctx:feed,l:'',t:'2026',calendar:JSON.stringify(calendar),ctxd:feed+':'+day});
  await page.goto(new URL('?'+params,origin).href, {waitUntil:'domcontentloaded'});

  await page.waitForFunction(() => history.state?.kfmExplorerView);

  await page.locator('.compact-time-emblem').focus(); await page.keyboard.press('Enter');
  await page.locator('.compact-time-source-details').evaluate(el => { el.open = true; });
  await page.waitForFunction(() => document.querySelector('.compact-time-source-details')?.textContent.includes('1 source records'));
  assert.equal(requests.filter(x=>x==='current').length,0);
  const priorView = new URLSearchParams(await page.evaluate(() => history.state.kfmExplorerView));
  if (exit === 'compact Present') await page.locator('.compact-time-present').click();
  else {
    await page.locator('.compact-time-legacy > summary').click();
    if (exit === 'advanced Present') await page.locator('.timeline-reset').click();
    else await page.locator('.timeline-controls [aria-label="Previous sweep frame"]').click();
  }
  await page.waitForFunction(() => { const p = new URLSearchParams(history.state?.kfmExplorerView); return !p.has('calendar') && !p.get('ctxd'); });
  const saved = new URLSearchParams(await page.evaluate(() => history.state.kfmExplorerView));
  assert.equal(saved.get('ctx'),feed); assert.equal(saved.get('l'),'');
  for (const key of ['c','z','b','p']) assert.equal(saved.get(key),priorView.get(key),'retain camera '+key);
  assert.equal(await page.locator('.compact-time-source-details').textContent().then(text => text.includes('1 source records')),false);
  if (exit === 'annual step') {
    assert.notEqual(saved.get('t'),'2026'); assert.equal(requests.includes('current'),false);
    await page.locator('.timeline-reset').click();
  }
  for (let i=0;i<100 && !requests.includes('current');i++) await page.waitForTimeout(50);
  assert.ok(requests.includes('current'),'Present must request current context after history');
  releaseCurrent();
  await page.waitForTimeout(300);
  if (!await page.getByLabel('Exact map date',{exact:true}).isVisible()) { await page.locator('.compact-time-emblem').focus(); await page.keyboard.press('Enter'); }
  await page.getByLabel('Exact map date',{exact:true}).fill(day);
  await page.waitForFunction(() => new URLSearchParams(history.state?.kfmExplorerView).has('calendar'));
  await page.locator('.compact-time-present').click();
  await page.waitForFunction(() => !new URLSearchParams(history.state?.kfmExplorerView).has('calendar'));
  t.diagnostic(JSON.stringify({exit,requests,sourceClocks:'fixture retrieval timestamps retained',origin:origin.href}));
});
