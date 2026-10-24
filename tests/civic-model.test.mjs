import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';

async function moduleUrl(name) {
  let js = ts.transpileModule(await readFile(new URL(`../app/${name}.ts`, import.meta.url), 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  for (const [, dependency] of [...js.matchAll(/from "\.\/([a-z-]+)"/g)]) js = js.replaceAll(`from "./${dependency}"`, `from "${await moduleUrl(dependency)}"`);
  return `data:text/javascript;base64,${Buffer.from(js).toString('base64')}`;
}
const civic = await import(await moduleUrl('civic-model'));
const source = { id: 'test', title: 'Official municipal budgets', organization: 'Test agency', url: 'https://example.gov/budgets', category: 'money', description: 'County and city public finance records', geography: 'Kansas', checkedAt: '2026-10-24', status: 'page-verified', limitation: 'Synthetic test entry', tags: ['tax'] };

test('source filters compose category and every search word without admitting unsafe links', () => {
  const rows = [source, { ...source, id: 'law', category: 'laws', title: 'Bills' }, { ...source, id: 'unsafe', url: 'javascript:alert(1)' }];
  assert.deepEqual(civic.filterCivicSources(rows, 'money', ' CITY tax ').map(row => row.id), ['test']);
  assert.deepEqual(civic.filterCivicSources(rows, 'money', 'missing'), []);
  assert.deepEqual(civic.filterCivicSources(rows, 'all', '').map(row => row.id), ['test', 'law']);
  for (const url of ['http://example.gov', 'https://name:secret@example.gov', 'data:text/html,test', 'not a url']) assert.equal(civic.civicSourceUrl(url), null);
});

// Synthetic repeated boxes exercise framing; these are not real county boundaries.
const feature = (index) => ({ type: 'Feature', geometry: { type: 'Polygon', coordinates: [[[-99, 38], [-98.5, 38], [-98.5, 38.5], [-99, 38.5], [-99, 38]]] }, properties: {
  geoid: `20${String(index * 2 + 1).padStart(3, '0')}`, featureId: `us-census-county-20${String(index * 2 + 1).padStart(3, '0')}`, name: `Synthetic ${index}`, vintage: '2020',
} });
const inventory = () => ({ edition: '2020', data: { type: 'FeatureCollection', features: Array.from({ length: 105 }, (_, index) => feature(index)) } });

test('county context requires the existing 2020 endpoint row count and unambiguous identities', () => {
  assert.equal(civic.civicCounties(inventory()).length, 105);
  for (const change of [value => { value.edition = '2010'; }, value => { value.data.features.pop(); }, value => { value.data.features[1] = value.data.features[0]; },
    value => { value.data.features[0].properties.featureId = 'other'; }, value => { value.data.features[0].properties.name = 'Bad\nname'; },
    value => { value.data.features[0].geometry = { type: 'Point', coordinates: [-99, 38] }; }, value => { value.data.features[0].geometry.coordinates[0][0] = [0, 0]; }]) {
    const value = inventory(); change(value); assert.deepEqual(civic.civicCounties(value), []);
  }
});

test('source pagination reveals every result while resetting immediately for a changed filter', () => {
  const rows = Array.from({ length: 48 }, (_, id) => ({ id }));
  const first = civic.civicSourcePage(rows, 'all', null);
  assert.equal(first.shown, 12); assert.equal(first.total, 48); assert.equal(first.hasMore, true);
  const next = civic.civicSourcePage(rows, 'all', { filterKey: 'all', limit: first.nextLimit });
  assert.equal(next.shown, 24); assert.deepEqual(next.items.map(row => row.id), rows.slice(0, 24).map(row => row.id));
  const last = civic.civicSourcePage(rows, 'all', { filterKey: 'all', limit: 48 });
  assert.equal(last.shown, 48); assert.equal(last.hasMore, false);
  assert.equal(civic.civicSourcePage(rows, 'money', { filterKey: 'all', limit: 48 }).shown, 12);
  assert.equal(civic.civicSourcePage(rows.slice(0, 3), 'all', { filterKey: 'all', limit: 48 }).shown, 3);
  assert.equal(civic.civicSourcePage([], 'all', null).shown, 0);
  for (const limit of [NaN, Infinity, -1, 0, 12.5]) assert.equal(civic.civicSourcePage(rows, 'all', { filterKey: 'all', limit }).shown, 12);
});

test('map navigation uses only the existing county layer and camera parameters', () => {
  const county = civic.civicCounties(inventory())[0];
  const params = new URL(civic.civicMapHref(county), 'https://example.test').searchParams;
  assert.deepEqual([...params.keys()].sort(), ['c', 'ctx', 'z']);
  assert.equal(params.get('ctx'), 'census-counties'); assert.equal(params.get('c'), '-98.75000,38.25000');
  assert.equal(civic.civicMapHref(null), '/?ctx=census-counties');
  assert.equal(civic.civicMapHref({ ...county, center: [Infinity, 38] }), '/?ctx=census-counties');
  assert.equal(civic.civicMapHref({ ...county, center: [-99, 38], zoom: NaN }), '/?ctx=census-counties');
});

test('prepared questions use neutral methods and distinguish directory discovery from evidence', () => {
  const county = civic.civicCounties(inventory())[0];
  const question = civic.civicQuestion('voting', county);
  assert.match(question, /same questions/); assert.match(question, /without recommending a candidate/);
  assert.match(question, /Cite checked sources/); assert.match(question, /directory link alone is not evidence/);
  assert.match(question, new RegExp(county.title));
  assert.match(civic.civicQuestion('wellbeing', null), /trend alone cannot show/);
});

test('private reflection has no persistence, automatic AI handoff or candidate scoring', async () => {
  const ui = await readFile(new URL('../app/civic/civic-atlas.tsx', import.meta.url), 'utf8');
  assert.doesNotMatch(ui, /localStorage|sessionStorage|indexedDB|sendBeacon|\/api\/ai|fetch\([^)]*reflection/);
  assert.match(ui, /const question = civicQuestion\(category, county\)/);
  assert.match(ui, /clipboard\.writeText\(question\)/);
  assert.match(ui, /setLenses\(\[\]\); setReflection\(""\)/);
  assert.match(ui, /No candidate ranking or candidate records are loaded here/);
  assert.match(ui, /poll cannot represent all residents/);
});
