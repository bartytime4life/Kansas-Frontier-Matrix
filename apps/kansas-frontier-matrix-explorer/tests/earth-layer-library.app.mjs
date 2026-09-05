/** Actual HTTP + Vinext/React composition test. No injected application modules,
 * API doubles, replacement root, renderer claims or public Site access.
 */
import assert from 'node:assert/strict';
import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { chromium } from 'playwright';
const base = new URL(process.env.KFM_APP_URL ?? 'http://127.0.0.1:4173');
assert.ok(['127.0.0.1', 'localhost', '[::1]'].includes(base.hostname), 'Only loopback app testing is permitted');
const output = path.resolve(process.env.KFM_APP_OUTPUT ?? '.sites-runtime/library-app-evidence');
await mkdir(output, { recursive: true });
const results = [], errors = [], external = [];
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 1000 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
await context.route('**/*', route => {
  const url = new URL(route.request().url());
  if (url.origin !== base.origin) { external.push(url.origin); return route.abort(); }
  return route.continue();
});
const page = await context.newPage();
page.setDefaultTimeout(15000);
page.on('pageerror', error => errors.push(error.message));
const dialog = page.locator('dialog.kfm-library-dialog');
const trigger = page.getByRole('button', { name: 'Library', exact: true });
const camera = async () => {
  await page.waitForTimeout(400);
  const params = new URL(page.url()).searchParams;
  return Object.fromEntries(['c','z','b','p','f','t','aoi'].map(k=>[k,params.get(k)]));
};
const layers = () => (new URL(page.url()).searchParams.get('l') ?? '').split(',').filter(Boolean);
const waitLayer = async (id, present) => page.waitForFunction(({id,present}) =>
  (new URL(location.href).searchParams.get('l') ?? '').split(',').includes(id) === present, { id, present });
const open = async () => { await trigger.click(); await dialog.waitFor({ state: 'visible' }); };
const close = async () => { await page.keyboard.press('Escape'); await dialog.waitFor({ state: 'hidden' }); };
const stack = async () => dialog.getByRole('button', { name: 'On map', exact: true }).click();
const run = async (name, fn) => {
  try { await fn(); results.push({ name, status: 'PASS' }); }
  catch(error) { results.push({ name, status: 'FAIL', reason: String(error.message) }); throw error; }
};
let originalCamera, saved;
try {
  await run('actual root HTTP, hydration and existing map shell', async()=>{
    const response = await page.goto(`${base.origin}/?l=kansas-extent&t=2026&c=-98.38,38.48&z=5.45&aoi=-100,37,-97,40`, { waitUntil: 'networkidle' });
    assert.equal(response.status(),200); await trigger.waitFor({state:'visible'});
    await waitLayer('water-context',false);
    assert.equal(await trigger.count(),1); assert.equal(await page.locator('#map-canvas').count(),1);
    assert.match(await page.locator('.map-command-bar').innerText(),/RENDERER HOLD/);
    await page.evaluate(()=>{ window.__testMapNode = document.getElementById('map-canvas'); });
    originalCamera = await camera();
  });
  await run('real layout CSS, isolated dialog placement and eligible default', async()=>{
    await open();
    assert.equal(await dialog.evaluate(el=>el.parentElement.tagName),'BODY');
    assert.equal(await dialog.getByRole('searchbox',{name:'Search layers'}).evaluate(el=>el===document.activeElement),true);
    assert.match(await dialog.innerText(),/No eligible released layers/);
    assert.match(await dialog.innerText(),/Selected analysis bounds/);
    assert.notEqual(await dialog.evaluate(el=>getComputedStyle(el).backgroundColor),'rgba(0, 0, 0, 0)');
  });
  await run('explicit fixture mode and staging without application mutation', async()=>{
    await dialog.getByLabel('Availability',{exact:true}).selectOption('fixtures');
    assert.equal(await dialog.locator('input[data-layer-id]').count(),8);
    await dialog.locator('input[data-layer-id="water-context"]').check();
    await dialog.locator('input[data-layer-id="atmosphere-observations"]').check();
    assert.deepEqual(layers(),['kansas-extent']);
    assert.deepEqual(await camera(),originalCamera);
  });
  await run('batch add commits actual React layer state, fixed order and held posture', async()=>{
    await dialog.getByRole('button',{name:'Add to workspace',exact:true}).click();
    await waitLayer('water-context',true); await waitLayer('atmosphere-observations',true);
    assert.match(await dialog.locator('.kfm-library-notice').innerText(),/2 added/);
    await stack();
    assert.deepEqual(await dialog.locator('.kfm-library-stack-row h4').allTextContents(),
      ['Kansas demonstration extent','Hydrology context','Atmosphere observations']);
    assert.equal(await dialog.getByRole('button',{name:/Move (up|down):/}).count(),6);
    for(const button of await dialog.getByRole('button',{name:/Move (up|down):/}).all()) assert.equal(await button.isDisabled(),true);
    assert.match(await dialog.innerText(),/Renderer held — not drawn/);
    assert.deepEqual(await camera(),originalCamera);
    assert.equal(await page.evaluate(()=>window.__testMapNode===document.getElementById('map-canvas')),true);
  });
  await run('zero opacity reaches app URL and repeated synchronous edits read actual owner', async()=>{
    const opacity=dialog.getByRole('slider',{name:'Opacity Atmosphere observations',exact:true});
    await opacity.evaluate(el=>{el.value='0';el.dispatchEvent(new Event('change',{bubbles:true}));});
    await page.waitForFunction(()=>new URL(location.href).searchParams.get('o')?.includes('atmosphere-observations:0.00'));
    await page.evaluate(()=>{
      for(const value of ['0.3','0.65','0']) {
        const el=document.querySelector('dialog input[aria-label="Opacity Atmosphere observations"]');
        el.value=value;el.dispatchEvent(new Event('change',{bubbles:true}));
      }
    });
    assert.equal(await dialog.getByRole('slider',{name:'Opacity Atmosphere observations',exact:true}).inputValue(),'0');
  });
  await run('hidden row remains session-local; immediate save reads the same state owner', async()=>{
    await dialog.getByRole('checkbox',{name:'Enable Hydrology context',exact:true}).uncheck();
    await waitLayer('water-context',false);
    assert.equal(await dialog.getByRole('checkbox',{name:'Enable Hydrology context',exact:true}).count(),1);
    await page.evaluate(()=>{
      [...document.querySelectorAll('dialog button')].find(x=>x.textContent==='Close').click();
      [...document.querySelectorAll('.map-command-bar button')].find(x=>x.textContent==='Save view').click();
    });
    saved=await page.evaluate(()=>JSON.parse(localStorage.getItem('kfm-map-workspaces-v1'))[0]);
    assert.equal(saved.visibility['water-context'],false);assert.equal(saved.opacity['atmosphere-observations'],0);
    assert.equal('membershipEpoch' in saved,false);assert.equal('members' in saved,false);
  });
  await run('visible operational Layers control and Library share actual state', async()=>{
    // Use the visible operational control, then its label-wrapped custom switch.
    // No force click or synthetic event bypass for this ordinary user interaction.
    await page.getByRole('button',{name:/^Layer catalog\. Choose governed context\./}).click();
    const checkbox = page.getByRole('checkbox',{name:'Show Hydrology context',exact:true});
    assert.equal(await checkbox.isChecked(),false);
    await page.locator('label.visibility-switch').filter({has:checkbox}).click();
    await waitLayer('water-context',true);await open();await stack();
    assert.equal(await dialog.getByRole('checkbox',{name:'Enable Hydrology context',exact:true}).isChecked(),true);
    await close();
    await page.getByRole('button',{name:'Close Layer Catalog',exact:true}).click();
  });
  await run('old-format saved workspace restore is atomic and clears hidden membership and undo', async()=>{
    await page.locator('.map-command-bar').getByRole('button',{name:'Build report',exact:true}).click();
    await page.locator('.saved-workspace-list').getByRole('button',{name:new RegExp('^'+saved.name+' ')}).click();
    await waitLayer('water-context',false);await open();await stack();
    assert.equal(await dialog.getByRole('checkbox',{name:'Enable Hydrology context',exact:true}).count(),0);
    assert.equal(await dialog.getByRole('slider',{name:'Opacity Atmosphere observations',exact:true}).inputValue(),'0');
    assert.equal(await dialog.getByRole('button',{name:'Undo',exact:true}).isDisabled(),true);
    await close();
  });
  await run('browser back and forward invoke restore without remounting map', async()=>{
    await page.waitForTimeout(450);
    await page.evaluate(()=>{
      const url=new URL(location.href);url.searchParams.set('l','kansas-extent,geology-context');url.searchParams.set('t','1910');
      history.pushState(null,'',url);dispatchEvent(new PopStateEvent('popstate'));
    });
    await waitLayer('geology-context',true);await page.waitForTimeout(450);
    await page.goBack();await waitLayer('geology-context',false);await page.waitForTimeout(450);
    await page.goForward();await waitLayer('geology-context',true);await page.waitForTimeout(450);
    assert.equal(await page.evaluate(()=>window.__testMapNode===document.getElementById('map-canvas')),true);
    await open();assert.match(await dialog.innerText(),/Existing year filter: 1910/);
    await dialog.getByLabel('Availability',{exact:true}).selectOption('fixtures');
    await dialog.getByText('Refine search: domain, provider, coverage and time',{exact:true}).click();
    await dialog.getByRole('checkbox',{name:'Matches selected time',exact:true}).check();
    assert.equal(await dialog.locator('input[data-layer-id="atmosphere-observations"]').count(),0);
    await close();
  });
  await run('cancel, Escape focus return and keyboard containment on actual app', async()=>{
    const before=await camera();await open();
    await dialog.getByRole('button',{name:'Clear filters',exact:true}).click();
    await dialog.locator('input[data-layer-id="prairie-context"]').check();
    for(let i=0;i<8;i++) {await page.keyboard.press('Tab');assert.equal(await dialog.evaluate(el=>el.contains(document.activeElement)),true);}
    await close();assert.equal(await trigger.evaluate(el=>el===document.activeElement),true);
    assert.equal(layers().includes('prairie-context'),false);assert.deepEqual(await camera(),before);
  });
  await run('feature inspector routes to the existing panel without fitting or selecting', async()=>{
    const before=await camera();await open();
    await dialog.getByRole('searchbox',{name:'Search layers'}).fill('Hydrology context');
    await page.waitForTimeout(200);
    const card=dialog.locator('.kfm-library-card').filter({has:page.locator('input[data-layer-id="water-context"]')});
    await card.getByText('Details and evidence',{exact:true}).click();
    await card.getByRole('button',{name:'Open feature inspector',exact:true}).click();
    await page.locator('.map-utility-panel[data-open="true"]').waitFor();
    assert.equal(new URL(page.url()).pathname,'/');
    assert.deepEqual(await camera(),before);
    assert.equal(new URL(page.url()).searchParams.get('maptab'),'inspect');
    // Finish the inspector interaction through its visible close control before
    // opening a different modal on the compact viewport. Do not force through it.
    await page.getByRole('button',{name:'Close Map Workbench',exact:true}).click();
    await page.locator('.map-utility-panel[data-open="true"]').waitFor({state:'hidden'});
  });
  await run('mobile actual app dialog text remains visible and fits viewport', async()=>{
    await page.setViewportSize({width:390,height:844});await open();
    const box=await dialog.boundingBox();assert.ok(box.width<=390 && box.x>=-1 && box.x+box.width<=391);
    const boundary=dialog.locator('.kfm-library-boundary');assert.equal(await boundary.isVisible(),true);
    assert.notEqual(await boundary.evaluate(el=>getComputedStyle(el).display),'none');
    assert.equal(await boundary.evaluate(el=>getComputedStyle(el).whiteSpace),'normal');
    await page.screenshot({path:path.join(output,'mobile-app-library.png')});await close();
  });
  await run('repeated modal lifecycle then actual route unmount cleans portal', async()=>{
    await page.setViewportSize({width:1440,height:1000});
    for(let i=0;i<10;i++){await open();await close();}
    assert.equal(await dialog.count(),1);assert.equal(await trigger.count(),1);
    await open();await page.screenshot({path:path.join(output,'desktop-app-library.png')});await close();
    await page.locator('a.about-action[href="/about"]').click();
    await page.waitForURL('**/about');assert.equal(await dialog.count(),0);
    await page.goBack();await trigger.waitFor();assert.equal(await dialog.count(),1);
  });
  await run('no browser application errors or off-origin source requests', async()=>{
    assert.deepEqual(errors,[]);assert.deepEqual(external,[]);
  });
} catch(error) {
  await page.screenshot({path:path.join(output,'failure.png')}).catch(()=>{});
  await writeFile(path.join(output,'failure.html'),await page.content().catch(()=>''));
  process.exitCode=1;
} finally {
  await writeFile(path.join(output,'results.json'),JSON.stringify({
    kind:'ACTUAL_VINEXT_APP_HTTP_REACT_DOM',url:base.origin,node:process.version,browser:browser.version(),
    head:process.env.GITHUB_SHA??'LOCAL_UNPINNED',results,errors,external,
    nonEffects:['No renderer/GPU validation','No live Site version','No deployment or publication','No source admission'],
  },null,2)+'\n');
  console.log(JSON.stringify(results,null,2));await browser.close();
}
