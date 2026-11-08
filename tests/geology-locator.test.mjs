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
  assert.ok(mapped.points.length > 0, 'sparse places remain individually selectable beside dense groups');
  assert.ok(mapped.clusters.length > 0);
  assert.equal(mapped.clusters.reduce((sum, cluster) => sum + cluster.count, mapped.points.length), mapped.total);
  assert.equal(mapped.clusters.reduce((sum, cluster) => sum + cluster.cores, mapped.points.filter(point => point.kind === 'core').length), mapped.cores);
});

test('nearby pans keep source groups in fixed geographic cells with exact count conservation', () => {
  const a = mapLocator(entries, [-100.5, 38, -99.5, 39], 40, 8, 6);
  const b = mapLocator(entries, [-100.49, 38.01, -99.49, 39.01], 40, 8, 6);
  assert.equal(a.clusters.reduce((sum, group) => sum + group.count, a.points.length), a.total);
  assert.equal(b.clusters.reduce((sum, group) => sum + group.count, b.points.length), b.total);
  const shared = a.clusters.find(group => b.clusters.some(other => other.bounds.join(',') === group.bounds.join(',')));
  assert.ok(shared, 'at least one shared fixed cell stays anchored during a small pan');
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
