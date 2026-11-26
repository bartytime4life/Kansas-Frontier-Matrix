import assert from 'node:assert/strict';
import test from 'node:test';
import { terrainHarness } from './terrain-detail-harness.mjs';

function automatic() {
  const h = terrainHarness(); h.view.zoom = 12; h.settle();
  assert.equal(h.provider, 'mapzen', 'the settled-view timer owns the switch');
  h.flushSwitch(); assert.equal(h.provider, 'usgs-3dep');
  return h;
}

test('automatic detail respects zoom, Kansas bounds, scene and cancellation', () => {
  for (const patch of [{ zoom: 11.5 }, { center: [-103, 38] }, { center: [-94, 38] }, { center: [-98, 36] }, { center: [-98, 41] }]) {
    const h = terrainHarness(); Object.assign(h.view, { zoom: 12 }, patch); h.settle(); h.flushSwitch(); assert.equal(h.provider, 'mapzen');
  }
  const h = terrainHarness(); h.scene = 'overview-2d'; h.view.zoom = 12; h.settle(); h.flushSwitch(); assert.equal(h.provider, 'mapzen');
  h.scene = 'elevation-3d'; const cancel = h.settle(); cancel(); h.flushSwitch(); assert.equal(h.provider, 'mapzen');
  h.settle(); h.flushSwitch(); assert.equal(h.provider, 'usgs-3dep'); h.attach(); h.complete();
  assert.equal(h.terrain, 'READY'); assert.equal(h.runtime.kind, 'ready');
});

test('failed automatic 3DEP recovers through Mapzen sourcedata and final idle', () => {
  const h = automatic(), old3dep = h.attach(); h.fail();
  assert.equal(h.provider, 'mapzen'); assert.equal(h.terrain, 'LOADING');
  assert.deepEqual(h.errors(), { runtimeError: null, degradedReason: null, failedSourceIds: [] });
  h.fail(old3dep); // Still attached while the React provider update is pending.
  h.attach(); h.complete();
  assert.equal(h.terrain, 'READY'); assert.equal(h.runtime.kind, 'ready');
  assert.match(h.runtime.message, /interactions proven/);
  assert.equal(h.scope.terrainDetailRef.current.failed, true);
  h.settle(); h.flushSwitch(); assert.equal(h.provider, 'mapzen', 'one fallback per session');
  assert.equal(h.announcements.filter(text => text.includes('did not load')).length, 1);
});

test('late 3DEP failures after source replacement cannot poison the Mapzen recovery', () => {
  const h = automatic(), old3dep = h.attach(); h.fail(); h.attach();
  h.fail(old3dep); h.complete(); h.fail(old3dep); h.idle();
  assert.equal(h.terrain, 'READY'); assert.equal(h.runtime.kind, 'ready');
  assert.deepEqual(h.errors(), { runtimeError: null, degradedReason: null, failedSourceIds: [] });
});

test('a replaced Mapzen source cannot fail a newly selected 3DEP source', () => {
  const h = terrainHarness(), oldMapzen = h.sources.get('kfm-terrain-dem').serialize();
  h.manual('usgs-3dep'); h.attach(); h.fail(oldMapzen); h.complete();
  assert.equal(h.provider, 'usgs-3dep'); assert.equal(h.terrain, 'READY'); assert.equal(h.runtime.kind, 'ready');
});

test('handled automatic and late errors preserve an unrelated runtime failure', () => {
  for (const order of ['before', 'during', 'after']) {
    const h = automatic(), old3dep = h.attach();
    const unrelated = () => h.error({ sourceId: 'catalog-source' });
    if (order === 'before') unrelated();
    h.fail(); if (order === 'during') unrelated();
    h.attach(); h.complete(); if (order === 'after') unrelated();
    h.fail(old3dep); h.idle();
    assert.equal(h.terrain, 'READY'); assert.equal(h.runtime.kind, 'degraded');
    assert.equal(h.errors().runtimeError, 'MAP_SOURCE_ERROR:catalog-source');
    assert.deepEqual(h.errors().failedSourceIds, ['catalog-source']);
  }
});

test('manual provider choices disable automatic switching and keep genuine failures visible', () => {
  for (const provider of ['mapzen', 'usgs-3dep']) {
    const h = terrainHarness(); h.manual(provider); h.view.zoom = 13; h.settle(); h.flushSwitch();
    assert.equal(h.provider, provider); assert.equal(h.scope.terrainDetailRef.current.byHand, true);
    h.attach(); h.fail(); h.idle(); assert.equal(h.provider, provider);
    assert.equal(h.terrain, 'ERROR'); assert.equal(h.runtime.kind, 'degraded');
    assert.deepEqual(h.errors().failedSourceIds, ['kfm-terrain-dem']);
  }
});

test('a genuine Mapzen failure after fallback is still a provider failure', () => {
  const h = automatic(); h.attach(); h.fail(); h.attach(); h.fail(); h.idle();
  assert.equal(h.provider, 'mapzen'); assert.equal(h.terrain, 'ERROR'); assert.equal(h.runtime.kind, 'degraded');
  assert.ok(h.errors().runtimeError); assert.deepEqual(h.errors().failedSourceIds, ['kfm-terrain-dem']);
});


test('provider replacement retires only abandoned relief failures and recovers the actual runtime callback closure',()=>{
 for(const manual of [false,true]){
  const h=manual?terrainHarness():automatic();if(manual)h.manual('usgs-3dep');const old=h.attach();
  h.fail(h.sources.get('basemap-relief-dem').serialize(),'basemap-relief-dem');if(manual)assert.ok(h.scope.basemapHealth.warning());else assert.equal(h.provider,'mapzen','the automatic relief source initiates the same fallback');
  if(manual)h.manual('mapzen');else h.fail(old);
  h.attach();h.complete();assert.equal(h.scope.basemapHealth.warning(),null);assert.equal(h.runtime.kind,'ready');h.fail(old);h.idle();assert.equal(h.runtime.kind,'ready','late old DEM error cannot relatch recovery');
 }
});
test('new provider and unrelated basemap failures survive retirement of the abandoned relief instance',()=>{
 for(const current of [true,false]){
  const h=automatic();h.attach();h.fail(undefined,'basemap-relief-dem');h.fail();
  if(!current){h.sources.set('other-basemap',{serialize:()=>({type:'raster',tiles:['https://example.test/other/{z}/{x}/{y}']})});h.fail(h.sources.get('other-basemap').serialize(),'other-basemap');}
  h.attach();if(current)h.fail(undefined,'basemap-relief-dem');h.complete();assert.equal(h.terrain,'READY');assert.equal(h.runtime.kind,'degraded');assert.ok(h.scope.basemapHealth.warning(),'only abandoned source failures are retired');
 }
});
test('late terrain shadow/color events are identity guarded; handled optional failures do not poison runtime readiness',()=>{
 const h=automatic(),old=h.attach();h.fail();h.attach();h.complete();
 for(const id of [h.scope.TERRAIN_HILLSHADE_SOURCE_ID,h.scope.TERRAIN_COLOR_SOURCE_ID]){h.fail(old,id);h.idle();assert.equal(h.runtime.kind,'ready');h.fail(h.sources.get(id).serialize(),id);h.idle();assert.equal(h.runtime.kind,'ready','optional shading failure is local to its display control');}
});


test('automatic close-wide-close navigation restores detail without pinning the category preset',()=>{
 const h=automatic();h.attach();h.complete();
 h.view.zoom=11;h.settle();h.flushSwitch();assert.equal(h.provider,'usgs-3dep','hysteresis retains detail');
 h.view.zoom=10;h.settle();h.flushSwitch();assert.equal(h.provider,'mapzen');h.attach();h.complete();assert.equal(h.runtime.kind,'ready');
 h.view.zoom=12;h.settle();h.flushSwitch();assert.equal(h.provider,'usgs-3dep');h.attach();h.complete();assert.equal(h.runtime.kind,'ready');
});
test('wide navigation permits one new detail attempt while a stationary source gap never loops',()=>{
 const h=automatic();h.attach();h.fail();h.attach();h.complete();h.settle();h.flushSwitch();assert.equal(h.provider,'mapzen');
 h.view.zoom=10;h.settle();h.flushSwitch();h.view.zoom=12;h.settle();h.flushSwitch();assert.equal(h.provider,'usgs-3dep');
});
test('cancellation of any owned terrain source never becomes a map outage',()=>{
 for(const sourceId of ['kfm-terrain-dem','kfm-terrain-hillshade-dem','kfm-terrain-color-dem','basemap-relief-dem']){
  const h=automatic();h.attach();h.error({sourceId,error:{name:'AbortError'}});h.complete();assert.equal(h.terrain,'READY');assert.equal(h.runtime.kind,'ready');assert.equal(h.provider,'usgs-3dep');
 }
});
test('replacing a failed manual DEM retires its failure without hiding an unrelated failure',()=>{
 for(const unrelated of [false,true]){
  const h=terrainHarness();h.manual('usgs-3dep');h.attach();h.fail();if(unrelated)h.error({sourceId:'catalog-source'});
  h.manual('mapzen');h.attach();h.complete();assert.equal(h.terrain,'READY');assert.equal(h.runtime.kind,unrelated?'degraded':'ready');
  assert.deepEqual(h.errors().failedSourceIds,unrelated?['catalog-source']:[]);
 }
});

test('explicit retry clears only the failed DEM latch and accepts its replacement source',()=>{
 const h=terrainHarness();h.manual('usgs-3dep');h.attach();h.fail();assert.equal(h.terrain,'ERROR');
 h.retryTerrain();h.complete();assert.equal(h.terrain,'READY');assert.equal(h.runtime.kind,'ready');assert.deepEqual(h.errors().failedSourceIds,[]);
});
