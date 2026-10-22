import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
const moduleUrl = source => 'data:text/javascript;base64,' + Buffer.from(ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString('base64');
const waterUrl = moduleUrl(await readFile(new URL('../app/governed-water.ts', import.meta.url), 'utf8'));
const weatherUrl = moduleUrl((await readFile(new URL('../app/governed-weather.ts', import.meta.url), 'utf8')).replace('"./governed-water"', JSON.stringify(waterUrl)));
let bridge = await readFile(new URL('../app/pipeline-server.ts', import.meta.url), 'utf8');
for (const name of ['pipeline-store','pipeline-handler','pipeline-contract']) bridge = bridge.replace(`'../server/${name}.mjs'`, JSON.stringify(new URL(`../server/${name}.mjs`, import.meta.url).href));
bridge = bridge.replace("'./governed-water'", JSON.stringify(waterUrl)).replace("'./governed-weather'", JSON.stringify(weatherUrl));
const { validateGoverned } = await import(moduleUrl(bridge));
const fixture = async (family, name) => JSON.parse(await readFile(new URL(`./fixtures/governed-${family}/${name}.json`, import.meta.url), 'utf8'));

test('MySQL publication bridge reuses actual water evidence/serving gates', async () => {
  const snapshot = await fixture('water', 'snapshot'), decision = await fixture('water', 'decision');
  assert.equal((await validateGoverned('water', { snapshot, decision }, Date.parse('2026-09-30T19:00:00Z'))).envelope.outcome, 'ANSWER');
  await assert.rejects(validateGoverned('water', { snapshot, decision: { ...decision, rights_ref: null } }, Date.parse('2026-09-30T19:00:00Z')), /GOVERNED_RELEASE_WITHHELD/);
  await assert.rejects(validateGoverned('water', { snapshot, decision }, Date.parse('2030-01-01T00:00:00Z')), /GOVERNED_RELEASE_WITHHELD/);
  const held = await fixture('water', 'held-snapshot');
  await assert.rejects(validateGoverned('water', { snapshot: held, decision: { ...decision, package_id: held.manifest.package_id } }, Date.parse('2026-09-30T19:00:00Z')), /GOVERNED_RELEASE_WITHHELD/);
});
