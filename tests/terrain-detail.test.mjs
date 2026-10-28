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
