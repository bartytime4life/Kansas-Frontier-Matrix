import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,readFile,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import ts from 'typescript';
import {componentHarness,findNode,settle} from './component-harness.mjs';
import {GRAIN_SOURCE,parseGrainReport,validateGrain} from '../server/grain-market.mjs';
import {reports,captureReport,reportChanges,watchMarket} from '../scripts/pc-pipeline/market-watch.mjs';
import {tradeNoticeSignals,watchSupplyChain} from '../scripts/pc-pipeline/supply-chain-watch.mjs';

const code=ts.transpileModule(await readFile('app/yield-history.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const {yieldHistory,pairedSeasons}=await import('data:text/javascript;base64,'+Buffer.from(code).toString('base64'));
const {exports:{farmBudget}}=await componentHarness('app/field-decision-tools.tsx',{'./bounded-json':{},'./rain-normal':{},'./yield-history':{},'./moon':{},'./sun-chart':{},'./frost-dates':{}});

test('deferred farm tools preserve the requested control and never take focus from another control', async () => {
  class HTMLElement {
    dataset = { categoryToolLoading: 'field-almanac' };
  }
  for (const moveFocus of [false, true]) {
    const body = {}, elsewhere = {}, loading = new HTMLElement(), focused = [];
    const document = { body, activeElement: loading };
    const Tools = () => null;
    let imports = 0;
    const h = await componentHarness('app/field-decision-tools-loader.tsx', {
      get './field-decision-tools'() { imports++; return { FieldDecisionTools: Tools }; },
    }, { HTMLElement, document });
    const render = props => h.render(h.exports.FieldDecisionToolsLoader, props);
    const shell = render({ point: null, year: 2024, frost: null });
    assert.equal(imports, 0, 'rendering the shell does not start the import');
    assert.ok(findNode(shell, node => node.props?.['data-category-tool-loading'] === 'field-almanac'));
    shell.props.ref.current = {
      contains: node => node === loading,
      querySelector(selector) {
        assert.equal(selector, '[data-category-tool="field-almanac"]');
        return {
          scrollIntoView: () => focused.push('scrolled'),
          focus: () => focused.push('focused'),
        };
      },
    };
    h.commit(); await settle();
    assert.equal(imports, 1);
    document.activeElement = moveFocus ? elsewhere : body;
    const point = { lon: -98, lat: 38 };
    const result = findNode(render({ point, year: 2025, frost: null }), node => node.type === Tools);
    assert.equal(result.props.point, point);
    assert.equal(result.props.year, 2025);
    h.commit();
    assert.deepEqual(focused, moveFocus ? [] : ['scrolled', 'focused']);
    h.dispose();
  }
});

test('failed farm tools render an inline notice and an explicit reload', async () => {
  let reloads = 0;
  const h = await componentHarness('app/field-decision-tools-loader.tsx', {
    get './field-decision-tools'() { throw new Error('Internal failure'); },
  }, { window: { location: { reload: () => reloads++ } } });
  const render = () => h.render(h.exports.FieldDecisionToolsLoader, { point: null, year: 2024, frost: null });
  render(); h.commit(); await settle();
  const failed = render();
  assert.equal(findNode(failed, node => node.props?.role === 'alert').props.children, 'Farm planning tools could not load.');
  const reload = findNode(failed, node => node.type === 'button');
  assert.equal(reloads, 0);
  reload.props.onClick();
  assert.equal(reloads, 1);
  h.dispose();
});

test('farm budget handles crop failure, entered zero, empty or negative costs and the selected cash price',()=>{
 const b=farmBudget('100','4.5',['20','80','10','250']);
 assert.equal(b.breakEven,3.6);assert.deepEqual(Array.from(b.rows,row=>row.margin),[0,90,180]);
 assert.equal(farmBudget('0','4',['10']).breakEven,null);
 assert.equal(farmBudget('100','',['0']),null);assert.equal(farmBudget('100','4',['']),null);
 assert.equal(farmBudget('100','4',['-1']),null);
});
test('yield baseline holds out each target and refuses duplicate, future, suppressed or interrupted harvests',()=>{
 const series='2019,0\n2020,20\n2021,40\n2022,60\n2023,80\n2024,100';
 const b=yieldHistory(series,2024);
 assert.equal(b.value,60);assert.equal(b.nextYear,2025);assert.equal(b.mae,60);assert.equal(b.previousMae,20);assert.equal(b.trials,1);
 for(const s of [series+'\n2020,42',series+'\n2026,81',series.replace('40','(D)'),series.replace('2022','2018')])assert.equal(yieldHistory(s,2024),null);
 const rains=Array.from(b.observations,([year,amount])=>({year,inches:amount/10}));
 assert.equal(pairedSeasons(b.observations,rains).correlation,1);
 assert.equal(pairedSeasons(b.observations,rains.slice(2)).correlation,null);
 const gapped=rains.map(r=>({...r,inches:r.year===2021?null:1}));
 assert.equal(pairedSeasons(b.observations,gapped).rows.length,5);assert.equal(pairedSeasons(b.observations,gapped).correlation,null);
});
const sample=`Kansas Daily Grain Bids
Grain Report for 10/05/2026 - Final
US #2 Yellow Corn (Bulk)
Country Elevators - Conventional
Region/Location Sale Type Basis (¢/Bu) Basis Change Price($/Bu) Price Change Average Year Ago Freight Delivery
Central Bid -35.00Z UNCH 4.0000-5.0000 UP 0.0500 4.4800 3.9100 DLVD-T Current
Terminal Elevators - Conventional
East Bid -50.00Z UNCH 8.0000 UP 0.0500 8.0000 DLVD-T Current
https://mymarketnews.ams.usda.gov/viewReport/2886`;
const parse=s=>parseGrainReport(s,'c'.repeat(64),'2026-10-06T00:00:00.000Z');
test('cash projection selects only qualified country rows and rejects changed columns, duplicates and non-final editions',()=>{
 const p=parse(sample);assert.equal(p.sourceId,GRAIN_SOURCE);assert.deepEqual(p.rows,[{crop:'Corn',region:'Central',low:4,high:5,average:4.48}]);
 for(const s of [sample.replace('Final','Preliminary'),sample.replace('Price($/Bu)','Price($/Ton)'),sample.replace('4.4800','7.0000'),sample.replace('Terminal Elevators','Country Elevators').replace('East Bid','Central Bid')])assert.throws(()=>parse(s));
 assert.throws(()=>validateGrain({...p,sourceUrl:'https://example.com'}));
});
test('watcher rejects unlisted locations, HTML and excessive bodies and preserves prior signals across outages',async()=>{
 await assert.rejects(captureReport({url:'https://example.com'},()=>assert.fail()),/SOURCE_NOT_ALLOWED/);
 for(const response of [new Response('<html>'),new Response('x',{status:403}),new Response('%PDF-x',{headers:{'Content-Length':'99999999'}})])await assert.rejects(captureReport(reports[0],()=>response));
 const previous=new Map(), signal={sourceId:GRAIN_SOURCE,captureSha256:'a',state:'captured'};
 assert.equal(reportChanges([signal],previous)[0].change,'baseline');
 reportChanges([{sourceId:GRAIN_SOURCE,state:'held'}],previous);
 assert.equal(reportChanges([signal],previous)[0].change,'unchanged');
 assert.equal(reportChanges([{...signal,captureSha256:'b'}],previous)[0].change,'changed');
});

test('CME destinations match the selected crop and have no sorghum proxy',async()=>{
 const h=await componentHarness('app/field-decision-tools.tsx',{'./bounded-json':{},'./rain-normal':{},'./yield-history':{},'./moon':{},'./sun-chart':{},'./frost-dates':{}},{},'\nexport {futuresReferences};');
 assert.deepEqual(Object.entries(h.exports.futuresReferences),[
  ['Corn','https://www.cmegroup.com/markets/agriculture/grains/corn'],
  ['Soybeans','https://www.cmegroup.com/markets/agriculture/oilseeds/soybean'],
  ['Hard red winter wheat','https://www.cmegroup.com/markets/agriculture/grains/kc-wheat'],
 ]);
 assert.equal(h.exports.futuresReferences.Sorghum,undefined);
 h.dispose();
});

test('delivered offer compares like bushels and withholds invalid bid, cost or shrink inputs',async()=>{
 const {exports:{netDeliveredBid}}=await componentHarness('app/field-decision-tools.tsx',{'./bounded-json':{},'./rain-normal':{},'./yield-history':{},'./moon':{},'./sun-chart':{},'./frost-dates':{}});
 const offer={bid:'5.25',hauling:'0.35',drying:'0.1',handling:'0.05',storage:'0.02',shrink:'2'};
 assert.equal(netDeliveredBid(offer),4.625);
 assert.equal(netDeliveredBid({...offer,bid:'5.20',hauling:'.15',shrink:'0'}),4.88);
 assert.equal(netDeliveredBid({...offer,shrink:'100'}),-0.52);
 assert.equal(netDeliveredBid({...offer,bid:'0.0001',hauling:'0',drying:'0',handling:'0',storage:'0',shrink:'99.9999'}),0);
 for(const bid of ['', '-1', '1e1', 'NaN', '5.00001', '1,000', '1000.0001']) assert.equal(netDeliveredBid({...offer,bid}),null);
 assert.equal(netDeliveredBid({...offer,hauling:''}),null);
 assert.equal(netDeliveredBid({...offer,shrink:'100.0001'}),null);
});

const notice = (id, title) => ({
  document_number: id, publication_date: '2026-11-18', title, type: 'Notice',
  pdf_url: `https://www.govinfo.gov/content/pkg/FR-2026-11-18/pdf/${id}.pdf`,
});
const noticePage = (...results) => ({ count: results.length, results });
const cropNotice = notice('2026-12345', 'Sorghum market access');
const unrelatedNotice = notice('2026-23456', 'Advisory committee nominations');

test('trade notice signals validate official links, ignore unrelated titles and are order independent', () => {
  const signals = page => tradeNoticeSignals(Buffer.from(JSON.stringify(page)));
  assert.deepEqual(signals(noticePage(cropNotice, unrelatedNotice)), signals(noticePage(unrelatedNotice, cropNotice)));
  assert.deepEqual(signals(noticePage(unrelatedNotice)), []);
  assert.equal(signals(noticePage(cropNotice))[0].published, '2026-11-18');
  assert.throws(() => signals({ count: 3, results: [cropNotice] }), /TRADE_NOTICE_PAGE_INVALID/);
  assert.throws(() => signals(noticePage(cropNotice, cropNotice)), /TRADE_NOTICE_RECORD_INVALID/);
  assert.throws(() => signals(noticePage({ ...cropNotice, pdf_url: 'https://example.org/notice.pdf' })), /TRADE_NOTICE_RECORD_INVALID/);
});

test('supply-chain capture is optional and writes publisher bytes and receipts only to private lifecycle paths', async t => {
  const root = await mkdtemp(join(tmpdir(), 'kfm-market-watch-'));
  t.after(() => rm(root, { recursive: true, force: true }));
  const requests = [];
  // Minimal workbook markers for this quarantine check. No workbook values are decoded.
  const workbook = Buffer.from('PK\x03\x04[Content_Types].xml xl/workbook.xml');
  const options = {
    guard: async () => {},
    clock: () => new Date('2026-11-26T12:00:00Z'),
    fetcher(url, init) {
      const target = new URL(url);
      requests.push(target);
      assert.equal(init.redirect, 'error');
      if (target.hostname === 'www.federalregister.gov') {
        assert.equal(target.searchParams.get('per_page'), '50');
        return Response.json(noticePage(cropNotice, unrelatedNotice));
      }
      if (target.pathname.endsWith('GTRTable1.xlsx')) return new Response(workbook);
      return new Response(null, { status: 503 });
    },
  };
  const basic = await watchMarket({ root }, options);
  assert.ok(basic.outcomes.every(outcome => !outcome.sourceId.includes('freight') && !outcome.sourceId.includes('ustr')));
  requests.length = 0;
  const expanded = await watchSupplyChain({ root }, options);
  const freight = expanded.outcomes.find(outcome => outcome.sourceId === 'usda-grain-freight-indicators');
  const trade = expanded.outcomes.find(outcome => outcome.sourceId === 'federal-register-ustr-notices');
  assert.equal(requests.filter(url => url.hostname === 'www.federalregister.gov').length, 1);
  assert.deepEqual(await readFile(join(root, 'data/quarantine', freight.sourceId, 'objects/sha256', freight.captureSha256, 'payload')), workbook);
  assert.equal(freight.releaseState, 'unreleased');
  assert.equal(trade.releaseState, 'unreleased');
  assert.deepEqual(trade.notices.map(({ id }) => id), [cropNotice.document_number]);

  const previous = new Map();
  reportChanges([trade], previous);
  assert.equal(reportChanges([{ ...trade, captureSha256: 'different envelope' }], previous)[0].change, 'unchanged');
});
