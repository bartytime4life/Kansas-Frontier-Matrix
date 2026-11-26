import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness} from './component-harness.mjs';
import {GRAIN_SOURCE,parseGrainReport,validateGrain} from '../server/grain-market.mjs';
import {reports,captureReport,reportChanges} from '../scripts/pc-pipeline/market-watch.mjs';

const code=ts.transpileModule(await readFile('app/yield-history.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const {yieldHistory,pairedSeasons}=await import('data:text/javascript;base64,'+Buffer.from(code).toString('base64'));
const {exports:{farmBudget}}=await componentHarness('app/field-decision-tools.tsx',{'./bounded-json':{},'./rain-normal':{},'./yield-history':{},'./moon':{},'./sun-chart':{},'./frost-dates':{}});
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
