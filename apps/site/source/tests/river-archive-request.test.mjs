import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
const compile = text => ts.transpileModule(text, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const lib = await import(`data:text/javascript;base64,${Buffer.from(compile(await readFile('app/streamflow.ts','utf8'))).toString('base64')}`);
const page = await readFile('app/page.tsx','utf8');
const callback = compile(page.slice(page.indexOf('  const refreshStreamflow ='), page.indexOf('  const refreshSelectedStreamflow =')));

test('actual refresh callback rejects invalid days before aborting an active read, changing owners or requesting current data', async () => {
  const errors = []; let requests = 0, aborts = 0;
  const controller = { signal: { aborted: false }, abort() { aborts++; } };
  const owner = { current: '2024-09-02' }, generation = { current: 7 };
  const bindings = { useCallback: fn => fn, announce: () => {}, buildYearCurrentRef: { current: true }, temporalQueryRef: { current: { frame: 2026 } }, OFFICIAL_CONTEXT_PRESENT_FRAME: 2026, normalizeUsgsStationId: lib.normalizeUsgsStationId, validStreamflowArchiveDay: lib.validStreamflowArchiveDay, currentUtcDay: () => '2026-10-11', setStreamflowError: error => errors.push(error), streamflowRequestRef: { current: controller }, streamflowRequestGenerationRef: generation, streamflowArchiveDayRef: owner, browserJsonRequest: () => { requests++; throw new Error('must not request'); } };
  const refresh = new Function(...Object.keys(bindings), callback + '\nreturn refreshStreamflow;')(...Object.values(bindings));
  for (const day of ['2026-11-11', '2024-02-30', '1799-12-31']) await refresh('24h', 'USGS-06864500', false, day);
  assert.equal(errors.length, 3); assert.ok(errors.every(error => /valid past UTC/.test(error)));
  assert.equal(requests, 0); assert.equal(aborts, 0); assert.equal(generation.current, 7); assert.equal(owner.current, '2024-09-02');
});
