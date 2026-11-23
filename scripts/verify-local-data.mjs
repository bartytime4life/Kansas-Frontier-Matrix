#!/usr/bin/env node
// Sequential, bounded public GETs. The report contains diagnostics rather than response bodies.
import assert from 'node:assert/strict';
import {pathToFileURL} from 'node:url';
import {isDeepStrictEqual} from 'node:util';
import {DATASETS} from './local-data/datasets.mjs';
import {LOCAL_DATA_LIMITS} from './local-data/protocol.mjs';

const SAMPLE_QUERIES = {
  'storm-events': {county:'Riley'},
  'ghcn-stations': {name:'Wichita'},
  'ghcn-daily': {station:'USW00003928',element:'TMAX,PRCP',from:'2025-07-01'},
  'ghcndex-indices': {},
  ghcndex: {station:'USW00003928',index:'TXx',period:'annual'},
  'asos-5min': {station:'KTOP',from:'2000-12-25',to:'2000-12-25'},
  'wind-stations': {name:'Wichita'},
  'wind-observations': {station:'ICT'},
  'wind-daily': {station:'ICT',from:'2025-06-01',to:'2025-06-30'},
  'prism-county': {variable:'tmax',county:'Riley',from:'2024-01',to:'2024-12'},
  'tiger-features': {layer:'county',id:'20161'},
  'nwm-reaches': {name:'Smoky Hill'},
  'nws-alerts': {},
  'usgs-earthquakes': {},
  'usgs-streamflow-sites': {},
  'recovered-observations': {collection:'observations-ahcb-changes'},
  'recovered-bulk': {collection:'bulk-census-decennial-geographies'},
  'archive-search': {q:'Kansas',source:'texts'},
  'near-observations': {collection:'observations-ahcb-county-versions',bbox:'-97.5,37.5,-97,38'},
  'near-bulk': {collection:'bulk-nbi-bridges',bbox:'-97.5,37.5,-97,38'},
  'nwm-streamflow': rows => rows.get('nwm-reaches')?.[0]?.featureId != null
    ? {feature:rows.get('nwm-reaches')[0].featureId} : null,
  'usgs-streamflow': rows => rows.get('usgs-streamflow-sites')?.[0]?.site
    ? {site:rows.get('usgs-streamflow-sites')[0].site} : null,
};
const REFUSALS = [
  ['unknown',404], ['ghcn-daily',400], ['tiger-features?layer=roads',400],
  ['nws-alerts?limit=51',400], ['nws-alerts?offset=-1',400],
  ['nws-alerts?offset=1001',400], ['nws-alerts?bogus=1',400],
  ['nwm-reaches?bbox=-102,37,-94,40',400],
  ['ghcn-daily?station=USW00003928&from=2025-02-30',400], ['nws-alerts?limit=1&limit=2',400],
];
const PREFIX = '/api/local-data';
const isObject = value => value !== null && typeof value === 'object' && !Array.isArray(value);
const READ_ERRORS = new Set(['NO_BODY','BYTE_LIMIT','INVALID_JSON']);

async function readReply(response, item) {
  if (!response.body) throw new Error('NO_BODY');
  const reader = response.body.getReader();
  const chunks = [];
  try {
    for (;;) {
      const {done, value} = await reader.read();
      if (done) break;
      item.bytes += value.byteLength;
      if (item.bytes > LOCAL_DATA_LIMITS.replyBytes) throw new Error('BYTE_LIMIT');
      chunks.push(value);
    }
    try { return JSON.parse(Buffer.concat(chunks).toString('utf8')); }
    catch { throw new Error('INVALID_JSON'); }
  } finally {
    void reader.cancel().catch(() => {});
    reader.releaseLock();
  }
}

export async function verifyLocalData(input, fetcher = fetch) {
  const origin = new URL(input);
  if (origin.protocol !== 'https:' || origin.username || origin.password || origin.pathname !== '/' ||
      origin.search || origin.hash) throw new Error('Use an HTTPS origin');

  const evidence = [], failures = [];
  const check = (label, fn) => {
    try { fn(); }
    catch (error) { failures.push({label, error:error.message}); }
  };

  async function get(path) {
    const item = {path,status:null,bytes:0,ms:0};
    const start = Date.now();
    const signal = AbortSignal.timeout(25_000);
    try {
      const response = await fetcher(new URL(path, origin), {
        redirect:'error', cache:'no-store', signal,
      });
      item.status = response.status;
      const body = await readReply(response, item);
      return {item, body};
    } catch (error) {
      const reason = READ_ERRORS.has(error?.message) ? error.message
        : signal.aborted ? 'TIMEOUT' : 'REQUEST_FAILED';
      failures.push({label:path,error:reason});
      return {item, body:null};
    } finally {
      item.ms = Date.now() - start;
      evidence.push(item);
    }
  }

  const expected = [...DATASETS.keys()].sort();
  assert.deepEqual(Object.keys(SAMPLE_QUERIES).sort(), expected, 'Provide one sample for each registered route');
  const {item:catalogReply, body:catalog} = await get(PREFIX);
  const datasets = new Map();
  check('catalog', () => {
    assert.ok(catalogReply.status === 200 && catalog?.format === 'kfm-local-data-catalog-v1', 'Catalogue unavailable or invalid');
    assert.ok(Array.isArray(catalog.datasets), 'Catalogue is missing datasets');
    for (const dataset of catalog.datasets) {
      assert.ok(isObject(dataset) && typeof dataset.id === 'string', 'Invalid catalogue dataset');
      datasets.set(dataset.id, dataset);
    }
    assert.ok(catalog.datasets.length === expected.length && expected.every(id => datasets.has(id)),
      'Catalogue routes differ from the local registry');
    assert.ok(catalog.online === true, 'Archive relay is offline');
  });
  const {item:buildReply, body:build} = await get('/api/build');
  check('build', () => assert.ok(buildReply.status === 200 && /^sha256:[0-9a-f]{64}$/.test(build?.sourceDigest), 'Build identity unavailable'));

  const samples = new Map(), rows = new Map();
  for (const [id, query] of Object.entries(SAMPLE_QUERIES)) {
    const params = typeof query === 'function' ? query(rows) : query;
    if (!params) {
      failures.push({label:id,error:'Upstream sample did not provide the required identifier'});
      continue;
    }
    const search = new URLSearchParams(params);
    if (id !== 'ghcndex-indices') search.set('limit','2');
    const dataset = DATASETS.get(id);
    try { dataset.parse(Object.fromEntries(search)); }
    catch { failures.push({label:id,error:'Invalid sample parameters'}); continue; }
    const path = PREFIX+'/'+id+(search.size ? '?'+search : '');
    const {item, body} = await get(path);
    samples.set(id, {path,body});
    check(id, () => {
      assert.ok(item.status === 200 && body?.dataset === id && body.format === (dataset.format ?? 'kfm-local-data-v1'),
        'Unexpected status or dataset response');
      const page = body[dataset.rowsKey ?? 'rows'];
      assert.ok(Array.isArray(page) && page.length === body.count && page.length > 0, 'Unexpected sample count');
      assert.ok(Number.isFinite(Date.parse(body.generatedAt)), 'Invalid retrieval timestamp');
      assert.ok(['live','fresh','stale'].includes(body.cache?.state), 'Invalid cache state');
      assert.ok(isObject(body.source) && isObject(datasets.get(id)?.source), 'Source metadata missing');
      assert.ok(isDeepStrictEqual(body.source,datasets.get(id).source), 'Source metadata differs from catalogue');
      if (params.collection) assert.ok(body.collection === params.collection, 'Sample collection does not match the request');
      item.count = body.count;
      item.cache = body.cache.state;
      rows.set(id,page);
    });
  }

  const notes = id => samples.get(id)?.body?.source?.notes;
  for (const id of ['nwm-reaches','nwm-streamflow']) check(id+' limitations', () => {
    assert.ok(/has not admitted/.test(notes(id)) && /pending/.test(notes(id)), 'NWM version caveat missing');
  });
  check('NWS historical disclaimer', () => assert.ok(/not a live alert feed/i.test(notes('nws-alerts')), 'NWS history caveat missing'));
  check('GHCNDEX beta', () => assert.ok(/beta/i.test(notes('ghcndex')), 'GHCNDEX beta caveat missing'));
  check('PRISM acquisition caveat', () => assert.ok(/acquisition dates are not yet verified/i.test(notes('prism-county')), 'PRISM acquisition caveat missing'));

  const initial = samples.get('nws-alerts');
  const again = await get(initial.path);
  check('cache repeat preserves answer', () => {
    assert.ok(again.item.status === 200 && Array.isArray(again.body?.rows) &&
      isDeepStrictEqual(again.body.rows,initial.body?.rows) &&
      again.body.generatedAt === initial.body?.generatedAt, 'Repeated query did not retain its answer');
  });
  const first = await get(PREFIX+'/nws-alerts?limit=1&offset=0');
  const second = await get(PREFIX+'/nws-alerts?limit=1&offset=1');
  check('pagination', () => assert.ok(first.item.status === 200 && second.item.status === 200 &&
    first.body?.rows?.length === 1 && second.body?.rows?.length === 1 &&
    isDeepStrictEqual([first.body.rows[0],second.body.rows[0]],again.body?.rows),
  'Pagination changed the sample rows'));

  for (const [path,status] of REFUSALS) {
    const {item} = await get(PREFIX+'/'+path);
    check(path, () => assert.ok(item.status === status, 'Unexpected refusal status'));
  }

  return {
    origin:origin.origin,
    build:/^sha256:[0-9a-f]{64}$/.test(build?.sourceDigest) ? {sourceDigest:build.sourceDigest} : null,
    routes:{expected:expected.length,verified:rows.size},
    failures,evidence,
  };
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try {
    const result = await verifyLocalData(process.argv[2] ?? 'https://kansasfrontiermatrix.com');
    console.log(JSON.stringify(result,null,2));
    process.exitCode = result.failures.length ? 1 : 0;
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}
