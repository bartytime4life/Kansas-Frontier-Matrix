import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
const code = ts.transpileModule(await readFile(new URL('../app/frame-check-model.ts', import.meta.url), 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { comparePacingRecords } = await import(`data:text/javascript;base64,${Buffer.from(code).toString('base64')}`);
const sample = () => ({ format: 'kfm-frame-pacing-v2', workload: { camera: [-98.38,38.48,10.5,0,0], viewport: [1280,576], canvas: [1600,720], selected: ['roads','hydrography'], flow: true, sourceDigest: 'abc', visibleFeatureDigest: 'def' }, browser: { frames: 719, fps: 59.91, p95Ms: 16.8, maxMs: 16.8, over25ms: 0 }, map: { frames: 719, fps: 59.91, p95Ms: 17.2, maxMs: 26, over25ms: 1 }, dataUnchanged: true, workloadUnchanged: true, readiness: {before:true,after:true}, visibility: {visible:true,focused:true,interrupted:false}, moving:true,interrupted:true,steps:48,elapsedMs:12000 });
test('equivalent ready navigation passes with the explicit timer tolerance', () => {
  assert.equal(comparePacingRecords(sample(), sample()).status, 'PASS');
});
test('unequal camera, canvas, selections, flow, and data cannot produce a comparison', () => {
  for (const [key,value] of Object.entries({camera:[-97,38,10.5,0,0],viewport:[1066,420],canvas:[1280,576],selected:['roads'],flow:false,sourceDigest:'changed',visibleFeatureDigest:'other'})) {
    const candidate = sample(); candidate.workload[key] = value;
    assert.equal(comparePacingRecords(sample(), candidate).status, 'INCONCLUSIVE', key);
  }
});
test('legacy, background-throttled, incomplete, unstable and idle runs fail closed', () => {
  for (const patch of [{format:undefined},{workload:{}},{visibility:{visible:true,focused:true,interrupted:true}}, {readiness:{before:false,after:true}}, {steps:47},{elapsedMs:13000},{dataUnchanged:false},{workloadUnchanged:false},{moving:false}]) {
    assert.equal(comparePacingRecords(sample(), {...sample(),...patch}).status, 'INCONCLUSIVE');
  }
});
test('slow candidate is held even when it improves over the baseline', () => {
  const candidate = sample(); candidate.map = {...candidate.map,frames:471,fps:39.25,p95Ms:33.4,maxMs:45,over25ms:190};
  assert.equal(comparePacingRecords(sample(),candidate).status,'HOLD');
});
test('invalid counters never pass', () => {
  for (const patch of [{fps:NaN},{frames:0},{p95Ms:0},{maxMs:0},{over25ms:-1}]) {
    const candidate=sample();candidate.browser={...candidate.browser,...patch};
    assert.equal(comparePacingRecords(sample(),candidate).status,'INCONCLUSIVE');
  }
});
