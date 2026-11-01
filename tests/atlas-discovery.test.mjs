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

test('water keeps River Pulse discoverable ahead of substring-only groundwater context in the actual source metadata', async () => {
  const aquifers = await import('data:text/javascript;base64,' + Buffer.from(ts.transpileModule(await readFile(new URL('../app/aquifer-layers.ts', import.meta.url), 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText).toString('base64'));
  // Read the six existing discovery fields from the real USGS catalogue entry.
  // No provider, renderer, source payload or synthetic source decision is invoked.
  const catalogue = ts.createSourceFile('live-context.ts', await readFile(new URL('../app/live-context.ts', import.meta.url), 'utf8'), ts.ScriptTarget.Latest, true, ts.ScriptKind.TS);
  let river;
  const visit = node => {
    if (ts.isObjectLiteralExpression(node) && node.properties.some(property => ts.isPropertyAssignment(property) && property.name.getText(catalogue) === 'id' && ts.isStringLiteral(property.initializer) && property.initializer.text === 'usgs-streamflow')) {
      river = Object.fromEntries(['id', 'title', 'shortTitle', 'organization', 'domain', 'endpointLabel'].map(name => {
        const property = node.properties.find(property => ts.isPropertyAssignment(property) && property.name.getText(catalogue) === name);
        assert.ok(property && ts.isStringLiteral(property.initializer), name + ' is an observed literal discovery field');
        return [name, property.initializer.text];
      }));
    }
    ts.forEachChild(node, visit);
  };
  visit(catalogue);assert.ok(river, 'the actual River Pulse source was inspected');
  const sources = Object.freeze([...aquifers.AQUIFER_RASTER_SOURCES, ...aquifers.GROUNDWATER_SNAPSHOT_SOURCES, river]);
  const before = JSON.stringify(sources);
  const results = atlasDiscoveryResults('water', 'water', [], sources, undefined, 'loading');
  assert.equal(results.length, 7, 'the display remains bounded');
  assert.ok(ids(results).includes('source:usgs-streamflow'), 'river context is not hidden behind seven groundwater substring matches');
  assert.deepEqual(ids(results).slice(0, 3), ['source:kgs-water-table', 'source:kgs-depth-to-water', 'source:usgs-streamflow']);
  assert.equal(results[2].title, river.shortTitle);assert.equal(results[2].subtitle, `${river.organization} · ${river.domain}`);
  assert.equal(JSON.stringify(sources), before, 'ranking never mutates the source catalogue');
});

test('exact dataset names and identifiers precede word-prefix and broad context matches', () => {
  const sources = [
    { ...sourceItem, id: 'prefix-water', title: 'Water measurements', shortTitle: 'Water measurements' },
    { ...sourceItem, id: 'context-only', title: 'Other measurements', shortTitle: 'Other measurements', domain: 'Water' },
    { ...sourceItem, id: 'exact-water', title: 'Water', shortTitle: 'Water' },
  ];
  assert.deepEqual(ids(atlasDiscoveryResults('  WATER  ', 'water', [], sources, undefined, 'ready')), ['source:exact-water', 'source:prefix-water', 'source:context-only']);
  const identifiers = [{ ...sourceItem, id: 'other-source', title: 'USGS-streamflow observations' }, sourceItem];
  assert.deepEqual(ids(atlasDiscoveryResults('usgs-streamflow', 'usgs-streamflow', [], identifiers, undefined, 'ready')), ['source:usgs-streamflow', 'source:other-source']);
  const unicode = [{ ...sourceItem, id: 'context', title: 'Other measurements', shortTitle: 'Other', domain: 'Águas region' }, { ...sourceItem, id: 'exact', title: 'Água', shortTitle: 'Água' }];
  assert.deepEqual(ids(atlasDiscoveryResults('ÁGUA', 'água', [], unicode, undefined, 'ready')), ['source:exact', 'source:context']);
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

test('results are bounded at seven, counties are alphabetized first, and equal-rank provider/index order is stable', () => {
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
