import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import ts from 'typescript';
import { StormDeskNetwork, weatherRequest, summarizeStormDeskNetwork } from '../scripts/storm-desk-network.mjs';

const tile = 'https://nowcoast.noaa.gov/geoserver/weather_radar/wms?request=GetMap&layers=conus_base_reflectivity_mosaic&time=2026-10-28T15%3A00%3A00.000Z&bbox=1,2,3,4';
test('real traffic collector separates duplicate requests, cached repeats, failures and phase crossings', () => {
  const n = new StormDeskNetwork();
  const start = (id, url = tile, session = 'map') => n.event('Network.requestWillBeSent', {requestId:id, request:{url}, timestamp:1}, session);
  start('1'); start('2');
  n.event('Network.responseReceived', {requestId:'1', timestamp:1.1, response:{status:200}}, 'map');
  n.phase = 'paused';
  n.event('Network.loadingFinished', {requestId:'1', timestamp:1.2, encodedDataLength:1200}, 'map');
  n.event('Network.dataReceived', {requestId:'2', encodedDataLength:100}, 'map');
  n.event('Network.loadingFailed', {requestId:'2', timestamp:1.3, errorText:'net::ERR_FAILED'}, 'map');
  start('1', tile, 'worker');
  n.event('Network.requestServedFromCache', {requestId:'1'}, 'worker');
  n.event('Network.loadingFinished', {requestId:'1', timestamp:1.4, encodedDataLength:0}, 'worker');
  const {records} = n.snapshot();
  assert.equal(records[0].phase, 'startup'); assert.equal(records[0].completedPhase, 'paused');
  assert.equal(records[0].encodedBytes, 1200); assert.ok(Math.abs(records[0].responseMs - 100) < 1e-8);
  assert.equal(records[1].concurrentDuplicate, true); assert.equal(records[1].bytesArePartial, true);
  assert.equal(records[1].encodedBytes, 100); assert.equal(records[1].outcome, 'failed');
  assert.equal(records[2].duplicate, true); assert.equal(records[2].concurrentDuplicate, false);
  assert.equal(records[2].cache, true); assert.equal(records[2].encodedBytes, 0);
  assert.ok(!JSON.stringify(records).includes('bbox'), 'URL digest avoids recording coordinates');
  assert.equal(records[0].observedAt, '2026-10-28T15:00:00.000Z');
  const summary = summarizeStormDeskNetwork(n.snapshot());
  assert.equal(summary[0].requests, 2); assert.equal(summary[0].completedEncodedBytes, 1200);
  assert.equal(summary[0].partialEncodedBytes, 100); assert.equal(summary[0].concurrentDuplicates, 1);
});

test('traffic capture is bounded and explicitly incomplete after overflow', () => {
  const n = new StormDeskNetwork(1);
  for (const requestId of ['1','2']) n.event('Network.requestWillBeSent', {requestId, request:{url:tile}, timestamp:1});
  assert.equal(n.snapshot().inFlight.length, 1); assert.equal(n.snapshot().dropped, 1);
  assert.equal(n.snapshot().completeCapture, false);
  const summary = summarizeStormDeskNetwork(n.snapshot());
  assert.equal(summary[0].requests, 1); assert.equal(summary[0].inFlight, 1);
  assert.equal(summary[0].completedEncodedBytes, 0);
  assert.equal(weatherRequest('https://example.com/private?token=secret'), null);
  assert.equal(weatherRequest('https://kansasfrontiermatrix.com/api/noaa-radar/frames').group, 'radar-manifest');
});

function probeHarness(search) {
  const exports = {}, window = {location:{search}}, canvasListeners = new Map(), mapListeners = new Map();
  const canvas = {width:1440,height:900,addEventListener:(name, fn)=>canvasListeners.set(name, fn),removeEventListener:name=>canvasListeners.delete(name)};
  const map = {getCanvas:()=>canvas, getStyle:()=>({sources:{radar:{}}, layers:[{}]}),
    on:(name, fn)=>mapListeners.set(name, fn), off:name=>mapListeners.delete(name)};
  const code = ts.transpileModule(readFileSync('app/storm-desk-performance.ts','utf8'), {compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
  new Function('exports','window','URLSearchParams','performance',code)(exports,window,URLSearchParams,{now:()=>100});
  return {exports,window,map,canvasListeners,mapListeners};
}
test('map probe adds no listeners by default and bounds exact-frame events when opted in', () => {
  const off = probeHarness(''); off.exports.installStormDeskPerformanceProbe(off.map)();
  assert.equal(off.mapListeners.size, 0); assert.equal(off.window.__kfmStormDeskPerf, undefined);
  const h = probeHarness('?stormPerf=1'); const cleanup = h.exports.installStormDeskPerformanceProbe(h.map);
  h.mapListeners.get('render')(); h.canvasListeners.get('webglcontextlost')();
  for(let i=0;i<2050;i++) h.exports.recordStormDeskFrame('confirmed','2026-10-28T15:00:00.000Z');
  const snapshot = h.window.__kfmStormDeskPerf.snapshot();
  assert.equal(snapshot.rendered, 1); assert.equal(snapshot.contextLosses, 1);
  assert.equal(snapshot.events.length, 2048); assert.equal(snapshot.droppedEvents, 2);
  cleanup(); assert.equal(h.window.__kfmStormDeskPerf, undefined);
  assert.equal(h.mapListeners.size, 0); assert.equal(h.canvasListeners.size, 0);
  h.exports.recordStormDeskFrame('stage','2026-10-28T15:00:00.000Z');
});
