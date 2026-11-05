import test from 'node:test';
import assert from 'node:assert/strict';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';

const model=await import(await modelUrl('app/data-library/freshness.ts'));
const fresh={file:14,sourceId:'noaa-storm-events-details',retrievedAt:'2026-11-01T23:30:00.000Z',modifiedAt:'2026-10-26T16:57:18.000Z',basis:'sources'};
const catalog=()=>({format:'kfm-local-data-catalog-v1',online:true,
 datasets:[{id:'storm-events',title:'x',path:'/api/local-data/storm-events',params:{},source:{},ready:true,freshness:fresh},{id:'tiger-features',ready:false,reason:'DATABASE_NOT_CONFIGURED',freshness:{reason:'UNAVAILABLE'}},{id:'plain',title:'no status'}],
 status:{state:'live',at:'2026-11-05T19:00:00.000Z',generatedAt:'2026-11-05T19:00:00.000Z',collections:{'observations-ahcb-changes':fresh,'observations-ahcb-chronology':null,'Bad Id':fresh}}});

test('the catalog freshness is read strictly and the rest of the page keeps working without it',()=>{
 const read=model.readCatalogFreshness(catalog());
 assert.equal(read.state,'live');assert.equal(read.at,'2026-11-05T19:00:00.000Z');assert.equal(read.online,true);
 assert.deepEqual(read.datasets.get('storm-events'),{ready:true,freshness:fresh});
 assert.deepEqual(read.datasets.get('tiger-features'),{ready:false,reason:'DATABASE_NOT_CONFIGURED',freshness:{reason:'UNAVAILABLE'}});
 assert.equal(read.datasets.has('plain'),false,'a dataset without readiness carries no status');
 assert.deepEqual(read.collections.get('observations-ahcb-changes'),fresh);
 assert.equal(read.collections.get('observations-ahcb-chronology'),null);
 assert.equal(read.collections.has('Bad Id'),false);
 // Without a status block (PC never answered) there is nothing to show.
 const bare=catalog();delete bare.status;
 assert.equal(model.readCatalogFreshness(bare),null);
 for(const bad of [null,[],{},{format:'other',datasets:[],status:{state:'live',at:'2026-11-05T19:00:00.000Z'}},{...catalog(),status:{state:'live',at:'yesterday'}}])assert.equal(model.readCatalogFreshness(bad),null);
 // Dates that are not ISO instants are refused rather than shown.
 const odd=catalog();odd.status.collections.x={retrievedAt:'2026-11-01',modifiedAt:null,sourceId:null,file:null};
 assert.equal(model.readCatalogFreshness(odd).collections.get('x'),null);
});

test('loadedThrough and freshnessLine say what was loaded when, and nothing when unknown',()=>{
 assert.equal(model.loadedThrough(fresh),'2026-11-01');
 assert.equal(model.loadedThrough({...fresh,retrievedAt:null}),'2026-10-26');
 assert.equal(model.loadedThrough({...fresh,retrievedAt:null,modifiedAt:null}),null);
 assert.equal(model.loadedThrough({reason:'INDEX_MISSING'}),null);
 assert.equal(model.loadedThrough(null),null);
 assert.equal(model.freshnessLine(fresh),"newest file retrieved 2026-11-01, provider's version of 2026-10-26 (noaa-storm-events-details).");
 assert.equal(model.freshnessLine({...fresh,modifiedAt:null,sourceId:null}),'newest file retrieved 2026-11-01.');
 assert.equal(model.freshnessLine({...fresh,retrievedAt:null,modifiedAt:null}),'Loaded, date not recorded.');
 assert.equal(model.freshnessLine({reason:'INDEX_MISSING'}),'Load date not indexed on the PC yet.');
 assert.equal(model.freshnessLine({reason:'NO_FILES'}),'No file loaded yet.');
 assert.equal(model.freshnessLine(null),'Load date not reported.');
});

test('fetchCatalogFreshness tolerates a failing or malformed catalog',async()=>{
 assert.equal(await model.fetchCatalogFreshness(new AbortController().signal,async()=>new Response('{}',{status:503})),null);
 assert.equal(await model.fetchCatalogFreshness(new AbortController().signal,async()=>new Response('not json',{status:200})),null);
 const read=await model.fetchCatalogFreshness(new AbortController().signal,async(url,init)=>{assert.equal(url,'/api/local-data');assert.equal(init.credentials,'same-origin');return new Response(JSON.stringify(catalog()),{status:200});});
 assert.equal(read.datasets.get('storm-events').freshness.file,14);
});
