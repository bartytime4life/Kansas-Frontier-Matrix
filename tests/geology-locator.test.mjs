import assert from 'node:assert/strict';
import test from 'node:test';
import { readFileSync } from 'node:fs';
import { gunzipSync } from 'node:zlib';
import ts from 'typescript';

const compile = file => ts.transpileModule(readFileSync(new URL(`../app/${file}`, import.meta.url), 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const url = value => `data:text/javascript;base64,${Buffer.from(value).toString('base64')}`;
const subsurface = url(compile('subsurface-model.ts').replace('import { atRecordYear } from "./subsurface-materials";', 'const atRecordYear=()=>true;'));
const { mapLocator, validGeologyBounds } = await import(url(compile('geology-locator-model.ts').replace('"./subsurface-model"', JSON.stringify(subsurface))));
const entries = JSON.parse(gunzipSync(readFileSync(new URL('../public/data/subsurface/locator.json.gz', import.meta.url))));
const kansas = [-102.1, 36.95, -94.55, 40.05];

test('statewide locator accounts for every published well and core without a first-page cap', () => {
  const mapped = mapLocator(entries, kansas, 2500, 8, 6);
  assert.equal(mapped.total, 321442);
  assert.equal(mapped.wells, 314844);
  assert.equal(mapped.cores, 6598);
  assert.equal(mapped.points.length, 0);
  assert.ok(mapped.clusters.length > 0 && mapped.clusters.length <= 48);
  assert.equal(mapped.clusters.reduce((sum, cluster) => sum + cluster.count, 0), mapped.total);
  assert.equal(mapped.clusters.reduce((sum, cluster) => sum + cluster.cores, 0), mapped.cores);
});

test('zoomed view exposes individual source identities and rejects invalid bounds', () => {
  const [id, , [lon, lat]] = entries.find(row => row[0].startsWith('core-'));
  const bounds = [lon - 0.002, lat - 0.002, lon + 0.002, lat + 0.002];
  const mapped = mapLocator(entries, bounds, 5000, 8, 6);
  assert.equal(mapped.total, mapped.points.length);
  assert.ok(mapped.points.some(point => point.id === id && point.kind === 'core'));
  assert.equal(mapped.clusters.length, 0);
  assert.equal(validGeologyBounds([-120, 0, 0, 90]), false);
});
