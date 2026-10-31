import test from 'node:test';
import assert from 'node:assert/strict';
import ts from 'typescript';
import vm from 'node:vm';
import { readFile } from 'node:fs/promises';

const countySource = await readFile(new URL('../app/county-search.ts', import.meta.url), 'utf8');
const county = await import('data:text/javascript;base64,' + Buffer.from(ts.transpileModule(countySource, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText).toString('base64'));
const source = await readFile(new URL('../app/atlas-discovery.ts', import.meta.url), 'utf8');
const compiledModule = { exports: {} };
vm.runInNewContext(ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
}).outputText, {
  module: compiledModule, exports: compiledModule.exports,
  require(id) {
    assert.equal(id, './county-search', 'the local county helper is the only runtime dependency');
    return county;
  },
  fetch() { throw new Error('local discovery must not perform a fetch'); },
});
const { atlasDiscoveryResults } = compiledModule.exports;

const countyFeature = (name, suffix = '053', vintage = '2020') => ({
  type: 'Feature', properties: { name, featureId: `us-census-county-20${suffix}`, geoid: `20${suffix}`, vintage },
});
const payload = { feed: 'census-counties', data: { features: [countyFeature('Ellsworth')] } };
const sourceItem = {
  id: 'usgs-streamflow', title: 'Water measurements', shortTitle: 'Streams',
  organization: 'U.S. Geological Survey', domain: 'Hydrology', endpointLabel: 'River observations',
};
const layer = { id: 'layer:water', kind: 'layer', title: 'Water layers', subtitle: 'Current layer catalog', layerId: 'water' };
const feature = { id: 'feature:river', kind: 'feature', title: 'River reading', subtitle: 'Water · station-01', layerId: 'water', featureId: 'station-01', focus: [-98.2, 38.8] };
const ids = results => Array.from(results, item => item.id);
const normalize = value => JSON.parse(JSON.stringify(value));

test('blank and unsettled queries withhold all prior rows across county states', () => {
  for (const state of ['idle', 'loading', 'ready', 'partial', 'error', 'empty']) {
    for (const query of ['', '   ', 'Ellsworth']) {
      assert.equal(atlasDiscoveryResults(query, 'Water', [layer, feature], [sourceItem], payload, state).length, 0);
    }
    assert.equal(atlasDiscoveryResults('Water', '   ', [layer], [sourceItem], payload, state).length, 0);
  }
  assert.deepEqual(ids(atlasDiscoveryResults('  WATER  ', 'water', [layer, feature], [sourceItem], payload, 'ready')), [
    'source:usgs-streamflow', 'layer:water', 'feature:river',
  ]);
});

test('local layers and features match titles and subtitles without changing their record metadata', () => {
  assert.deepEqual(normalize(atlasDiscoveryResults('station-01', 'station-01', [layer, feature], [], undefined, 'idle')), [feature]);
  assert.deepEqual(normalize(atlasDiscoveryResults('current layer', 'current layer', [layer, feature], [], undefined, 'idle')), [layer]);
  assert.deepEqual(ids(atlasDiscoveryResults('river reading', 'river reading', [layer, feature], [], undefined, 'idle')), ['feature:river']);
  assert.deepEqual(ids(atlasDiscoveryResults('water', 'water', [feature, layer], [], undefined, 'idle')), ['feature:river', 'layer:water']);
});

test('official sources match every existing search field and retain provider context labels', () => {
  for (const term of ['measurements', 'STREAMS', 'geological survey', 'hydrology', 'river observations']) {
    assert.deepEqual(normalize(atlasDiscoveryResults(term, term, [], [sourceItem], undefined, 'error')), [{
      id: 'source:usgs-streamflow', kind: 'source', title: 'Streams',
      subtitle: 'U.S. Geological Survey · Hydrology', officialContextId: 'usgs-streamflow',
    }]);
  }
});

test('official sources are discoverable by dataset identifier and combined provider terms', () => {
  for (const term of ['streamflow', 'usgs-streamflow', 'USGS streamflow', 'streamflow usgs', 'stream flow', 'Streams\t geological   survey']) {
    assert.deepEqual(ids(atlasDiscoveryResults(term, term, [], [sourceItem], undefined, 'idle')), ['source:usgs-streamflow'], term);
  }
});

test('every source query term must match the same source and only discovery metadata is indexed', () => {
  const sources = [
    { ...sourceItem, boundary: 'Not a flood forecast', fallback: 'No radar substitute' },
    { ...sourceItem, id: 'nws-radar', title: 'Radar', shortTitle: 'Reflectivity', organization: 'National Weather Service', domain: 'Weather', endpointLabel: 'Radar tiles' },
  ];
  for (const term of ['streamflow radar', 'streamflow forecast', 'streamflow unknown', 'flood forecast']) {
    assert.deepEqual(ids(atlasDiscoveryResults(term, term, [], sources, undefined, 'ready')), [], term);
  }
  assert.deepEqual(ids(atlasDiscoveryResults('radar weather', 'radar weather', [], sources, undefined, 'ready')), ['source:nws-radar']);
  assert.deepEqual(ids(atlasDiscoveryResults('streamflow unknown', 'streamflow', [], sources, undefined, 'ready')), []);
});

test('current ready or partial Census counties are discoverable by name and FIPS with source edition', () => {
  for (const state of ['ready', 'partial']) {
    for (const term of ['Ellsworth', 'ellsworth county', '20053']) {
      const results = atlasDiscoveryResults(term, term, [], [], payload, state);
      assert.deepEqual(ids(results), ['county:us-census-county-20053']);
      assert.equal(results[0].title, 'Ellsworth County');
      assert.equal(results[0].featureId, 'us-census-county-20053');
      assert.equal(results[0].subtitle, '2020 U.S. Census baseline · source context, not KFM evidence');
    }
  }
});

test('unsearchable county feeds cannot hide available local and provider matches or expose stale county rows', () => {
  for (const state of ['idle', 'loading', 'error', 'empty']) {
    assert.equal(atlasDiscoveryResults('Ellsworth', 'Ellsworth', [], [], payload, state).length, 0);
    assert.deepEqual(ids(atlasDiscoveryResults('water', 'water', [layer], [sourceItem], payload, state)), ['source:usgs-streamflow', 'layer:water']);
  }
  for (const countyPayload of [undefined, { ...payload, feed: 'usgs-streamflow' }, { ...payload, data: { features: [countyFeature('Ellsworth', '053', '2026')] } }]) {
    assert.equal(atlasDiscoveryResults('Ellsworth', 'Ellsworth', [], [], countyPayload, 'ready').length, 0);
  }
});

test('results are bounded at seven, counties are alphabetized first, and provider/index order is stable', () => {
  const counties = { feed: 'census-counties', data: { features: [countyFeature('Water Zebra', '001'), countyFeature('Water Alpha', '003')] } };
  const sources = [sourceItem, { ...sourceItem, id: 'noaa-nwps-gauges', shortTitle: 'Water gauges' }];
  const index = Array.from({ length: 8 }, (_, i) => ({ ...layer, id: `layer:water-${i}` }));
  const expected = [
    'county:us-census-county-20003', 'county:us-census-county-20001',
    'source:usgs-streamflow', 'source:noaa-nwps-gauges',
    'layer:water-0', 'layer:water-1', 'layer:water-2',
  ];
  assert.deepEqual(ids(atlasDiscoveryResults('water', 'water', index, sources, counties, 'ready')), expected);
  assert.deepEqual(ids(atlasDiscoveryResults('water', 'water', index, sources, counties, 'ready')), expected);
  assert.deepEqual(index.map(item => item.id), Array.from({ length: 8 }, (_, i) => `layer:water-${i}`));
  assert.equal(counties.data.features[0].properties.name, 'Water Zebra');
  assert.equal(sources[0], sourceItem);
});

test('discovery preserves text for renderer escaping and does not infer cities or new sources', () => {
  const title = '<img src=x onerror=alert(1)>';
  const unsafe = { ...feature, title, subtitle: 'Untrusted display text' };
  assert.deepEqual(normalize(atlasDiscoveryResults('<img', '<img', [unsafe], [], undefined, 'idle')), [unsafe]);
  assert.deepEqual(ids(atlasDiscoveryResults('Wichita', 'Wichita', [], [], undefined, 'ready')), []);
  assert.deepEqual(ids(atlasDiscoveryResults('Ellsworth', 'Ellsworth', [], [], undefined, 'ready')), []);
});
