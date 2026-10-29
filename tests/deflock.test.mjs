import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import ts from 'typescript';

async function compile(file, deps = {}) {
  const exports = {};
  new Function('exports', 'require', ts.transpileModule(await readFile(file, 'utf8'), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText)(exports, name => {
    if (name in deps) return deps[name]; throw new Error(`Unexpected import ${name}`);
  }); return exports;
}
const d = await compile('app/deflock.ts');
const bounded = await compile('app/bounded-json.ts');
const reader = await compile('app/api/live-context/deflock.ts', { '../../bounded-json': bounded, '../../deflock': d });
const now = new Date('2026-10-28T18:00:00Z');
// Synthetic points: not a real camera inventory.
const node = (id, lon = -97.37123, lat = 37.67123) => ({ type: 'node', id, lon, lat, tags: { man_made: 'surveillance', 'surveillance:type': 'ALPR', operator: 'SHOULD_NOT_LEAVE_ADAPTER', image: 'https://untrusted.invalid/image', direction: '90', note: '<script>alert(1)</script>' } });
const raw = (nodes = [node(1), node(2, -97.36123)]) => ({ osm3s: { timestamp_osm_base: '2026-10-28T17:00:00Z' }, elements: [{ type: 'area', id: 3600161161 }, ...nodes] });

test('generalization preserves counts and stable cells while dropping exact positions, IDs and every tag', () => {
  const result = d.parseDeflock(raw(), now);
  assert.equal(result.state, 'ready'); assert.equal(result.featureCount, 1);
  const [f] = result.data.features;
  assert.equal(f.properties.reportCount, 2);
  assert.deepEqual(f.geometry.coordinates, [[[-97.4, 37.65], [-97.35, 37.65], [-97.35, 37.7], [-97.4, 37.7], [-97.4, 37.65]]]);
  assert.equal(f.properties.evidenceRole, 'EXTERNAL_CONTEXT_ONLY');
  assert.equal(f.properties.license, 'https://opendatacommons.org/licenses/odbl/1-0/');
  for (const forbidden of ['-97.37123', '37.67123', 'SHOULD_NOT_LEAVE_ADAPTER', 'untrusted.invalid', '<script>', 'direction', 'osmId']) assert.ok(!JSON.stringify(result).includes(forbidden), forbidden);
  assert.deepEqual(d.parseDeflock(raw(raw().elements.slice(1).reverse()), now).data, result.data);
  assert.notEqual(result.upstreamUpdatedAt, result.retrievedAt);
  assert.match(result.limitation, /not installation, observation or verification time/);
});

test('empty is distinct from missing area, upstream error, ambiguous source, malformed time and over-cap response', () => {
  assert.equal(d.parseDeflock(raw([]), now).state, 'empty');
  for (const bad of [null, { elements: [] }, { ...raw(), remark: 'runtime error: timed out' }, { ...raw(), elements: [] },
    raw([{ type: 'area', id: 3 }]), { ...raw(), osm3s: { timestamp_osm_base: 'tomorrow' } },
    { ...raw(), osm3s: { timestamp_osm_base: '2027-01-01T00:00:00Z' } }, raw(Array.from({ length: 5001 }, (_, i) => node(i + 1))), raw([node(1), node(1)])]) assert.throws(() => d.parseDeflock(bad, now));
});

test('invalid, non-ALPR, out-of-bounds and inactive-tagged reports are visibly withheld', () => {
  const result = d.parseDeflock(raw([node(1), node(2, -120), node(3, NaN), { ...node(4), tags: { ...node(4).tags, disused: 'yes' } },
    { ...node(5), tags: { man_made: 'surveillance', 'surveillance:type': 'camera' } }, { ...node(6), lat: '37.6' }]), now);
  assert.equal(result.state, 'partial'); assert.equal(result.data.features[0].properties.reportCount, 1);
  assert.match(result.limitation, /5 invalid, out-of-scope or inactive-tagged records withheld/);
});

test('concurrent reads coalesce; the one-hour cache preserves retrieval time and never returns expired data after failure', async () => {
  let time = now.getTime(), calls = 0, fail = false, release;
  const gate = new Promise(resolve => { release = resolve; });
  const read = reader.createDeflockReader(async (url, options) => {
    calls++; assert.equal(new URL(url).origin, 'https://overpass-api.de'); assert.equal(options.redirect, 'manual');
    assert.match(new URL(url).searchParams.get('data'), /"ISO3166-2"="US-KS"/);
    assert.match(new URL(url).searchParams.get('data'), /out body 5001/);
    await gate;
    if (fail) throw new Error('secret provider failure');
    return Response.json(raw());
  }, () => time);
  const promises = Array.from({ length: 25 }, () => read());
  assert.equal(calls, 1); release(); const results = await Promise.all(promises);
  assert.ok(results.every(r => r === results[0]));
  time += 3_599_999; assert.equal((await read()).retrievedAt, results[0].retrievedAt); assert.equal(calls, 1);
  time++; fail = true; await assert.rejects(read(), /unavailable/); assert.equal(calls, 2);
  await assert.rejects(read(), e => !e.message.includes('secret')); assert.equal(calls, 2, 'failure cooldown prevents a request storm');
  time += 60_000; fail = false; assert.notEqual((await read()).retrievedAt, results[0].retrievedAt); assert.equal(calls, 3);
});

test('redirects, failed status, declared oversize and streamed oversize responses fail closed', async () => {
  for (const response of [new Response('', { status: 302, headers: { location: 'http://127.0.0.1/' } }), new Response('', { status: 429 }),
    new Response('{}', { headers: { 'content-length': String(2 * 1024 * 1024 + 1) } }), new Response(' '.repeat(2 * 1024 * 1024 + 1))]) {
    const read = reader.createDeflockReader(async () => response, () => now.getTime());
    await assert.rejects(read(), /unavailable/);
  }
});

test('the existing route exposes only the fixed current feed, with no coordinates, arbitrary queries or historical dates', async () => {
  let calls = 0;
  const route = await compile('app/api/live-context/route.ts', {
    './deflock': { readDeflock: async () => { calls++; return d.parseDeflock(raw(), now); } },
    'cloudflare:workers': { env: {} }, 'next/server': { NextResponse: Response }, '../../bounded-json': bounded,
    '../../event-atlas': { eventDay: value => /^\d{4}-\d{2}-\d{2}$/.test(value) }, '../event-atlas/upstream': {}, '../../county-baseline': {}, '../../fema-declarations': {}, '@mapbox/vector-tile': {}, pbf: {},
  });
  const req = query => ({ nextUrl: new URL(`https://kfm.invalid/api/live-context?${query}`), signal: new AbortController().signal });
  for (const query of ['feed=deflock-alpr&url=https://evil.invalid', 'feed=deflock-alpr&longitude=-97', 'feed=deflock-alpr&day=2026-10-01', 'feed=deflock-alpr&feed=deflock-alpr', 'feed=deflock-alpr&data=anything']) assert.equal((await route.GET(req(query))).status, 400);
  assert.equal(calls, 0);
  const response = await route.GET(req('feed=deflock-alpr'));
  assert.equal(response.status, 200); assert.equal(response.headers.get('cache-control'), 'no-store');
  assert.equal((await response.json()).feed, 'deflock-alpr'); assert.equal(calls, 1);
});

const modules = new Map();
async function moduleUrl(file) {
  file = path.resolve(file); if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + '.ts'))}`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString('base64')}`; modules.set(file, url); return url;
}
const context = await import(await moduleUrl('app/live-context.ts'));
const workspaces = await import(await moduleUrl('app/layer-workspaces.ts'));
const maps = await import(await moduleUrl('app/category-maps.ts'));
test('transport search finds DeFlock, starter maps leave it off, and historical frames suppress it', () => {
  assert.equal(context.defaultOfficialContextVisibility()['deflock-alpr'], false);
  assert.ok(!maps.categoryMap('transport').starters.includes('deflock-alpr'));
  assert.deepEqual(workspaces.filterOfficialSources(context.OFFICIAL_CONTEXT_SOURCES, 'transport', 'deflock').map(s => s.id), ['deflock-alpr']);
  assert.deepEqual(context.OFFICIAL_CONTEXT_TEMPORAL_SUPPORT['deflock-alpr'].supportedFrames, [context.OFFICIAL_CONTEXT_PRESENT_FRAME]);
});

test('map cells and counts restore after style replacement, respect hide/opacity and validate as MapLibre styles', async () => {
  const make = () => {
    const sources = new Map(), layers = new Map();
    const map = { getSource: id => sources.get(id), getLayer: id => layers.get(id), getStyle: () => ({ layers: [...layers.values()] }), getProjection: () => ({ type: 'mercator' }),
      addSource(id, spec) { sources.set(id, { ...spec, setData(data) { this.data = data; } }); }, addLayer(l) { layers.set(l.id, structuredClone(l)); },
      moveLayer(id) { const l = layers.get(id); layers.delete(id); layers.set(id, l); },
      getLayoutProperty: (id, key) => layers.get(id)?.layout?.[key], getPaintProperty: (id, key) => layers.get(id)?.paint?.[key],
      setLayoutProperty(id, key, v) { const l = layers.get(id); l.layout = { ...l.layout, [key]: v }; }, setPaintProperty(id, key, v) { const l = layers.get(id); l.paint = { ...l.paint, [key]: v }; } };
    return { map, sources, layers };
  };
  const vis = Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s => [s.id, false]));
  const opacity = context.defaultOfficialContextOpacity(), payload = d.parseDeflock(raw(), now);
  const h = make(); context.applyOfficialContextState(h.map, vis, opacity, {});
  assert.ok(!h.sources.has('external-deflock-alpr'), 'off creates no source');
  vis['deflock-alpr'] = true; opacity['deflock-alpr'] = 0.4;
  const { validateStyleMin } = await import('@maplibre/maplibre-gl-style-spec');
  for (const harness of [h, make()]) {
    context.applyOfficialContextState(harness.map, vis, opacity, { 'deflock-alpr': payload });
    const layers = [...harness.layers.values()].filter(l => l.source === 'external-deflock-alpr');
    assert.equal(layers.length, 3); assert.equal(layers.find(l => l.type === 'fill').paint['fill-opacity'], 0.4);
    assert.deepEqual(validateStyleMin({ version: 8, glyphs: 'https://example.invalid/{fontstack}/{range}.pbf', sources: { 'external-deflock-alpr': { type: 'geojson', data: payload.data } }, layers }).map(e => e.message), []);
    context.applyOfficialContextState(harness.map, { ...vis, 'deflock-alpr': false }, opacity, { 'deflock-alpr': payload });
    for (const l of layers) assert.equal(harness.layers.get(l.id).layout.visibility, 'none');
    context.clearOfficialContextFeed(harness.map, 'deflock-alpr'); assert.equal(harness.sources.get('external-deflock-alpr').data.features.length, 0);
  }
});
