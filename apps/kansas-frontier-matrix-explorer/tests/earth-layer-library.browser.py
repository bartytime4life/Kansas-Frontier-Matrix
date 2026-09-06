"""Component-only Chromium regression runner. NOT the Vinext app or a renderer test.
Requires an explicitly supplied CommonJS-compiled source root, Playwright and Chromium.
Uses injected compiled modules in about:blank; network/module delivery is NOT tested.
Uses synthetic fixtures, including a forbidden-existence test; opens no test server.
Never include this fixture/test module in a Site deployment.
"""
from __future__ import annotations
import argparse
import json
import time
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

parser = argparse.ArgumentParser(allow_abbrev=False)
parser.add_argument('--compiled-root', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--chromium', default='/usr/bin/chromium')
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
repo = Path(__file__).resolve().parents[3]
records: list[dict] = []
metrics: dict = {}

JS = '''
const { mountLayerLibrary } = require('./layer-library-view.js');
const M = require('./layer-library-model.js');
const camera = Object.freeze({center:[-98.38,38.48],zoom:5.45,bearing:0,pitch:0});
let workspace = [], inspected = [], writes=0, denyWrite=false, writeMode="normal", attempts=0, api;
let hostKeys=0;document.addEventListener("keydown",()=>hostKeys++);
const card=(id,extra={})=>({id,title:`Fixture ${id}`,description:'Synthetic test metadata; no real Kansas data.',
 provider:'KFM synthetic tests',domain:'Hydrology',representation:'GeoJSON fixture',disclosure:'allow',
 access:'allow',rights:'cleared',sensitivity:'public',release:'unreleased',fixture:true,workspaceAction:'preview',
 runtime:'held',renderGroup:'fixture-pass',coverageLabel:'Illustrative extent',areaMatch:true,
 timeLabel:'Static test metadata',timeMatch:true,sourceId:'synthetic',units:'none',...extra});
let cards=Array.from({length:30},(_,i)=>card(`f${i}`));
cards.push(card('SECRET_EXISTENCE',{disclosure:'deny',provider:'SECRET_PROVIDER'}));
const port={read:()=>{if(writeMode==="readback-throw"&&attempts>0)throw Error("SECRET_READBACK");return workspace;},write:(next,expected)=>{attempts++;
 if(denyWrite || !M.sameWorkspace(expected,workspace))return false;
 if(writeMode==="throw")throw Error("SECRET_HOST_ERROR");
 if(writeMode==="noop")return true;
 workspace=writeMode==="mismatch"?next.slice(0,1):next; writes++;
 if(writeMode==="mutate-throw")throw Error("SECRET_AFTER_WRITE");
 return true;},inspect:id=>inspected.push(id)};
const context=()=>({cards,areaLabel:'Synthetic analysis-area scope',timeLabel:'Host time scope'});
const mount=()=>{api=mountLayerLibrary(document.getElementById('host'),port,context());};
mount();
window.testHost={state:()=>({workspace,camera,inspected,writes,hostKeys,attempts}), api:()=>api,
 reset:()=>{api.destroy();workspace=[];inspected=[];writes=0;denyWrite=false;writeMode="normal";attempts=0;cards=Array.from({length:30},(_,i)=>card(`f${i}`));
 cards.push(card('SECRET_EXISTENCE',{disclosure:'deny',provider:'SECRET_PROVIDER'})); mount();},
 update:(changes)=>{cards=cards.map(c=>changes[c.id]?{...c,...changes[c.id]}:c);api.update(context());},
 failWrites:(v)=>{denyWrite=v},
 writeMode:(v)=>{writeMode=v},
 large:(n)=>{cards=Array.from({length:n},(_,i)=>card(`f${i}`)); api.update(context());},
 metrics:()=>{
  const raw=Array.from({length:10000},(_,i)=>card(`measure${i}`));
  const times=[]; let projected;
  for(let i=0;i<30;i++){const start=performance.now();projected=M.projectCatalog(raw);
   M.selectCards(projected,{...M.EMPTY_FILTERS,mode:'fixtures',query:'measure9'});times.push(performance.now()-start);}
  times.sort((a,b)=>a-b);return {catalogSize:raw.length,trials:times.length,medianMs:(times[14]+times[15])/2,p95Ms:times[28],
   geometryRequests:0,budgetStatus:'MEASURED_INITIAL_BASELINE_NOT_A_RELEASE_BUDGET'};
 },
 cycles:(n)=>{const counts=[];const before=performance.memory?.usedJSHeapSize??null;
  for(let i=0;i<n;i++){api.destroy();api.destroy();mount();api.open();document.querySelector('dialog input[type=search]').value='pending';
   document.querySelector('dialog input[type=search]').dispatchEvent(new Event('input'));api.destroy();
   counts.push(document.querySelectorAll('#host *').length);mount();}
  return {cycles:n,emptyHostNodeCounts:counts,beforeHeapBytes:before,afterHeapBytes:performance.memory?.usedJSHeapSize??null};},
 destroy:()=>api.destroy(), card,
};
'''

try:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=args.chromium,headless=True,args=['--no-sandbox'])
        page = browser.new_page(viewport={'width':1440,'height':1000},reduced_motion='reduce')
        page.set_default_timeout(5000)
        requests=[]; errors=[]
        page.on('request',lambda request:requests.append(request.url))
        page.on('pageerror',lambda error:errors.append(str(error)))
        # Loopback navigation was blocked by this environment's administrator.
        # Do not change browser policies or disable web security. Exercise owned
        # component code in memory instead, without navigating to a blocked URL.
        model = (args.compiled_root/'packages/ui/src/layer-library-model.js').read_text()
        view_module = (args.compiled_root/'packages/ui/src/layer-library-view.js').read_text()
        if 'exports.' not in model or 'exports.' not in view_module:
            raise RuntimeError('Browser diagnostics require CommonJS compilation.')
        page.set_content('<!doctype html><html lang="en"><head><meta name="viewport" content="width=device-width,initial-scale=1"></head><body><h1>Private component validation</h1><p>Synthetic host port. Not the Explorer, a renderer, or released data.</p><span id="host"></span></body></html>')
        page.add_style_tag(content=(repo/'packages/ui/src/layer-library.css').read_text())
        page.add_style_tag(content='body{font:16px system-ui;background:#f3f4ef;margin:24px}#host>button{padding:12px}')
        bundle = ('(()=>{const factories={"./layer-library-model.js":(module,exports,require)=>{\n'
            + model + '\n},"./layer-library-view.js":(module,exports,require)=>{\n'
            + view_module + '\n}};const cache={};function require(id){if(cache[id])return cache[id].exports;'
            + 'if(!factories[id])throw Error("Unknown test module");const module={exports:{}};cache[id]=module;factories[id](module,module.exports,require);return module.exports;}\n'
            + JS + '\n})();')
        page.add_script_tag(content=bundle)
        page.wait_for_function('!!window.testHost')
        initial_requests=len(requests)
        def case(name, action):
            start=time.perf_counter()
            try:
                action(); records.append({'name':name,'status':'PASS','elapsed_ms':round((time.perf_counter()-start)*1000,3)})
            except Exception as exc:
                records.append({'name':name,'status':'FAIL','error':str(exc)})
                page.screenshot(path=str(args.output/'browser-failure.png'),full_page=True)
                raise
        def reset():
            page.evaluate('testHost.reset()'); page.get_by_role('button',name='Library',exact=True).click()
        def fixtures(): page.get_by_label('Availability',exact=True).select_option('fixtures')
        def select(id): page.get_by_role('checkbox',name=f'Select Fixture {id}',exact=True).check()
        def add(): page.get_by_role('button',name='Add to workspace',exact=True).click()
        def stack(): page.get_by_role('button',name='On map',exact=True).click()
        def state(): return page.evaluate('testHost.state()')
        initial_camera=state()['camera']
        def eligible():
            reset(); expect(page.get_by_text('No eligible released layers are supplied by this host.',exact=True)).to_be_visible()
            expect(page.get_by_label('Search layers',exact=True)).to_be_focused()
            assert 'SECRET_EXISTENCE' not in page.locator('body').inner_text()
            assert 'SECRET_PROVIDER' not in page.locator('body').inner_text()
        case('eligible default and disclosure-safe empty state',eligible)
        def staging():
            fixtures(); assert page.locator('.kfm-library-card').count()==24
            select('f0'); select('f1'); assert state()['workspace']==[]
            expect(page.get_by_text('2 selected · 2 new',exact=True)).to_be_visible()
            page.keyboard.press('Escape'); expect(page.get_by_role('button',name='Library',exact=True)).to_be_focused()
            page.get_by_role('button',name='Library',exact=True).click(); assert state()['workspace']==[]
            expect(page.get_by_text('0 selected · 0 new',exact=True)).to_be_visible()
        case('staging cancel Escape and focus restoration',staging)
        def addition():
            fixtures(); select('f0'); select('f1'); add(); assert len(state()['workspace'])==2
            assert state()['camera']==initial_camera
            expect(page.get_by_role('checkbox',name='Select Fixture f0',exact=True)).to_be_disabled()
            stack(); expect(page.get_by_text('Renderer held — not drawn',exact=True)).to_have_count(2)
        case('apply deduplicate and preserve host camera without pretending to render',addition)
        def visibility():
            page.get_by_label('Enable Fixture f0',exact=True).uncheck()
            assert len(state()['workspace'])==2 and not state()['workspace'][0]['visible']
            control=page.get_by_label('Opacity Fixture f0',exact=True)
            control.evaluate('(e)=>{e.value="0.45";e.dispatchEvent(new Event("change",{bubbles:true}))}')
            assert state()['workspace'][0]['opacity']==.45
        case('hidden membership and opacity share one requested stack',visibility)
        def reorder():
            b=page.get_by_role('button',name='Move down: Fixture f0',exact=True)
            b.focus(); page.keyboard.press('Enter'); assert state()['workspace'][0]['id']=='f1'
            expect(page.get_by_role('button',name='Move down: Fixture f0',exact=True)).to_be_disabled()
            page.evaluate('testHost.update({f0:{renderGroup:null}})')
            expect(page.get_by_role('button',name='Move up: Fixture f0',exact=True)).to_be_disabled()
        case('keyboard reorder obeys declared renderer group constraints',reorder)
        def undo():
            reset(); fixtures(); select('f0'); add(); page.get_by_role('button',name='Undo',exact=True).click()
            assert state()['workspace']==[]; assert state()['camera']==initial_camera
        case('undo after current eligibility recheck',undo)
        def cas():
            select('f0'); page.evaluate('testHost.failWrites(true)'); add()
            assert state()['workspace']==[]
            expect(page.get_by_text('The host declined the workspace change.',exact=False)).to_be_visible()
            page.evaluate('testHost.failWrites(false)')
        case('host compare-and-set rejection preserves workspace',cas)
        def withdrawal():
            page.evaluate('testHost.update({f0:{disclosure:"deny"}})')
            expect(page.get_by_text('0 selected · 0 new',exact=True)).to_be_visible()
            assert 'Fixture f0' not in page.locator('dialog').inner_text()
            expect(page.get_by_role('button',name='Add to workspace',exact=True)).to_be_disabled()
        case('staged revocation suppresses old title identity and commit',withdrawal)
        def withdrawn_filters():
            reset(); fixtures()
            page.evaluate('testHost.update({f0:{provider:"WITHDRAWN_PROVIDER"}})')
            page.get_by_text('Refine search: domain, provider, coverage and time',exact=True).click()
            page.get_by_label('Provider',exact=True).select_option('WITHDRAWN_PROVIDER')
            page.evaluate('testHost.update({f0:{disclosure:"deny"}})')
            assert 'WITHDRAWN_PROVIDER' not in page.locator('dialog').inner_text()
            assert page.get_by_label('Provider',exact=True).input_value()==''
        case('withdrawn metadata is removed from filter chips and options',withdrawn_filters)
        def unconfirmed_write():
            reset(); fixtures(); select('f0'); page.evaluate('testHost.writeMode("noop")'); add()
            assert state()['workspace']==[] and state()['attempts']==1
            expect(page.get_by_text('Workspace write was not confirmed by readback.',exact=False)).to_be_visible()
            expect(page.get_by_text('1 selected · 1 new',exact=True)).to_be_visible()
            expect(page.get_by_role('button',name='Undo',exact=True)).to_be_disabled()
        case('truthy write without readback is not success or an undo receipt',unconfirmed_write)
        def host_error():
            reset(); fixtures(); select('f0'); page.evaluate('testHost.writeMode("throw")'); add()
            assert state()['workspace']==[] and state()['attempts']==1
            expect(page.get_by_text('Workspace result could not be confirmed.',exact=False)).to_be_visible()
            assert 'SECRET_HOST_ERROR' not in page.locator('body').inner_text()
            expect(page.get_by_text('1 selected · 1 new',exact=True)).to_be_visible()
        case('host exception is finite redacted and not retried',host_error)
        def readback_error():
            reset(); fixtures(); select('f0'); page.evaluate('testHost.writeMode("readback-throw")'); add()
            assert state()['attempts']==1
            expect(page.get_by_text('Workspace unavailable; no successful change is confirmed.',exact=True)).to_be_visible()
            expect(page.get_by_role('button',name='Add to workspace',exact=True)).to_be_disabled()
            expect(page.get_by_text('1 selected · workspace unavailable',exact=True)).to_be_visible()
            assert 'SECRET_READBACK' not in page.locator('body').inner_text()
        case('persistent readback exception disables mutations without leaking error text',readback_error)
        def after_mutation():
            reset(); fixtures(); select('f0'); page.evaluate('testHost.writeMode("mutate-throw")'); add()
            assert len(state()['workspace'])==1 and state()['attempts']==1
            expect(page.get_by_text('Workspace result could not be confirmed.',exact=False)).to_be_visible()
            expect(page.get_by_role('button',name='Undo',exact=True)).to_be_disabled()
            assert 'SECRET_AFTER_WRITE' not in page.locator('body').inner_text()
        case('mutation then failure is not auto-rolled-back or called applied',after_mutation)
        def mismatch():
            reset(); fixtures(); select('f0'); select('f1'); page.evaluate('testHost.writeMode("mismatch")'); add()
            assert len(state()['workspace'])==1 and state()['attempts']==1
            expect(page.get_by_text('Workspace write was not confirmed by readback.',exact=False)).to_be_visible()
            expect(page.get_by_text('2 selected · 1 new',exact=True)).to_be_visible()
        case('partial host application is detected by exact requested-state readback',mismatch)
        def revoked_write_failure():
            reset(); fixtures(); select('f0'); add(); page.evaluate('testHost.failWrites(true)')
            page.evaluate('testHost.update({f0:{disclosure:"deny"}})')
            assert state()['workspace'][0]['id']=='f0'
            assert 'Fixture f0' not in page.locator('dialog').inner_text()
            expect(page.get_by_text('The host declined the workspace change.',exact=False)).to_be_visible()
            expect(page.get_by_role('button',name='Undo',exact=True)).to_be_disabled()
        case('revocation stays visually suppressed when host cleanup is declined',revoked_write_failure)
        def injection():
            reset(); fixtures()
            page.evaluate('(title)=>testHost.update({f0:{title}})', '<img src="https://evil.invalid/x" onerror="window.owned=1">')
            assert page.locator('dialog img').count()==0
            assert page.evaluate('window.owned===undefined')
            assert all('evil.invalid' not in request for request in requests)
        case('untrusted title remains text without image requests or execution',injection)
        def debounce():
            reset(); fixtures(); search=page.get_by_label('Search layers',exact=True)
            search.fill('absent'); page.get_by_role('button',name='Clear filters',exact=True).click()
            page.wait_for_timeout(200); assert page.locator('.kfm-library-card').count()==24
            search.fill('Fixture f2'); search.fill('Fixture f19'); page.wait_for_timeout(200)
            assert page.locator('.kfm-library-card').count()==1
            assert 'Fixture f19' in page.locator('.kfm-library-results').inner_text()
        case('debounce obsolete query rejection and clear-filter cancellation',debounce)
        def filters():
            page.get_by_role('button',name='Clear filters',exact=True).click()
            page.evaluate('testHost.update({f0:{areaMatch:null},f1:{areaMatch:false},f2:{timeMatch:false}})')
            page.get_by_text("Refine search: domain, provider, coverage and time",exact=True).click()
            page.get_by_label('Known coverage in selected analysis area',exact=True).check()
            assert page.get_by_role('checkbox',name='Select Fixture f0',exact=True).count()==0
            page.get_by_label('Matches selected time',exact=True).check()
            assert page.get_by_role('checkbox',name='Select Fixture f2',exact=True).count()==0
            expect(page.get_by_text('27 disclosable matches',exact=False)).to_be_visible()
        case('coverage and temporal uncertainty remain distinct from positive matches',filters)
        def table():
            page.get_by_role('button',name='Clear filters',exact=True).click()
            page.get_by_role('button',name='Compact table',exact=True).click()
            assert page.locator('tbody tr').count()==24
            select('f0'); page.get_by_role('button',name='Next page',exact=True).click()
            assert page.locator('tbody tr').count()==6
            expect(page.get_by_role("button",name="Previous page",exact=True)).to_be_focused()
            expect(page.get_by_text('1 selected · 1 new',exact=True)).to_be_visible()
        case('compact table paginates without dropping staged selections',table)
        def inspect():
            page.get_by_role('button',name='Previous page',exact=True).click()
            page.locator('tbody tr').first.get_by_text('Details and evidence',exact=True).click()
            page.locator('tbody tr').first.get_by_role('button',name='Open feature inspector',exact=True).click()
            assert state()['inspected']==['f0']; assert state()['camera']==initial_camera
            assert not page.locator('dialog').evaluate('(e)=>e.open')
        case('stable layer identifier reaches host inspector without geometry promotion',inspect)
        def url_state():
            page.evaluate('history.pushState({owner:"host"},"","#explore")')
            before=page.url; reset(); fixtures(); select('f0'); add(); page.keyboard.press('Escape')
            assert page.url==before
        case('component does not rewrite host URL or browser history',url_state)
        def desktop():
            reset(); fixtures(); select('f0'); page.screenshot(path=str(args.output/'library-desktop.png'),full_page=True)
            assert page.locator('canvas').count()==0
        case('desktop component visual capture with no fake renderer',desktop)
        def mobile():
            page.set_viewport_size({'width':390,'height':844}); page.wait_for_timeout(50)
            assert page.locator('dialog').bounding_box()['width']<=390
            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
            page.screenshot(path=str(args.output/'library-mobile.png'),full_page=True)
            page.keyboard.press('Escape'); expect(page.get_by_role('button',name='Library',exact=True)).to_be_focused()
        case('mobile sheet bounds keyboard dismissal and preserved focus',mobile)
        def cycles():
            metrics['repeatedSessions']=page.evaluate('testHost.cycles(50)')
            metrics['repeatedSessions']['heapInterpretation']='COARSE_BROWSER_COUNTER_ONLY; MEMORY_GROWTH_NOT_PROVEN'
            assert set(metrics['repeatedSessions']['emptyHostNodeCounts'])=={0}
            page.wait_for_timeout(200); assert page.locator('dialog').count()==1
        case('fifty repeated sessions cancel timers and dispose all owned DOM',cycles)
        def large():
            page.set_viewport_size({'width':1440,'height':1000})
            start=time.perf_counter(); page.evaluate('testHost.large(5000)'); page.get_by_role('button',name='Library',exact=True).click(); fixtures()
            metrics['catalog5000OpenFixtureMs']=round((time.perf_counter()-start)*1000,3)
            assert page.locator('.kfm-library-card').count()==24
            metrics['metadataMicrobenchmark']=page.evaluate('testHost.metrics()')
        case('large metadata catalog remains page bounded',large)
        def keys():
            reset(); fixtures()
            page.get_by_role('button',name='Compact table',exact=True).focus()
            before=state()['hostKeys']; page.keyboard.press('r')
            assert state()['hostKeys']==before
            for _ in range(30):
                page.keyboard.press('Tab')
                assert page.evaluate('document.querySelector("dialog").contains(document.activeElement)')
        case('native modal focus containment and host shortcut isolation',keys)
        case('no uncaught browser exceptions' ,lambda: (_ for _ in ()).throw(AssertionError(errors)) if errors else None)
        metrics['additionalRequestsDuringLibraryOperations']=len(requests)-initial_requests
        metrics['requestUrls']=requests
        metrics['browserVersion']=browser.version
        metrics['evidenceClass']='ACTUAL_CHROMIUM_DOM_WITH_INJECTED_COMPILED_MODULES_AND_SYNTHETIC_HOST_PORT; NETWORK_MODULE_DELIVERY_REACT_VINEXT_GPU_NOT_PROVEN'
        assert metrics['additionalRequestsDuringLibraryOperations']==0, requests
        browser.close()
finally:
    (args.output/'browser-results.json').write_text(json.dumps({'cases':records,'metrics':metrics},indent=2))
    print(json.dumps({'pass':sum(x['status']=='PASS' for x in records),'fail':sum(x['status']=='FAIL' for x in records),'metrics':metrics},indent=2))
