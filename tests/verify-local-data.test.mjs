import test from 'node:test';
import assert from 'node:assert/strict';
import {verifyLocalData} from '../scripts/verify-local-data.mjs';
import {DATASETS,datasetCatalog} from '../scripts/local-data/datasets.mjs';
import {LOCAL_DATA_LIMITS} from '../scripts/local-data/protocol.mjs';

const ORIGIN='https://example.test';
const PRIVATE_FIXTURE='synthetic record text never printed by the verifier';
const at='2026-11-22T12:00:00.000Z';

function fixture({damaged=false}={}) {
  const calls=[];
  return {calls,fetcher:async (url, options) => {
    assert.equal(url.origin,ORIGIN);
    assert.equal(options.redirect,'error');
    assert.equal(options.method,undefined);
    calls.push(url.pathname);
    if (url.pathname === '/api/build') return Response.json({sourceDigest:'sha256:'+'a'.repeat(64),note:PRIVATE_FIXTURE});
    if (url.pathname === '/api/local-data') {
      return Response.json({format:'kfm-local-data-catalog-v1',online:true,
        datasets:datasetCatalog().filter(row=>!damaged || row.id!=='near-bulk')});
    }
    const id=url.pathname.slice('/api/local-data/'.length);
    const dataset=DATASETS.get(id);
    if (!dataset) return Response.json({reasonCode:'DATASET_NOT_FOUND'},{status:404});
    const query=Object.fromEntries(url.searchParams);
    try {
      assert.equal(url.searchParams.size,Object.keys(query).length);
      dataset.parse(query);
    } catch { return Response.json({reasonCode:'QUERY_INVALID'},{status:400}); }
    if (damaged && id==='nwm-reaches') return new Response(PRIVATE_FIXTURE,{status:502});
    if (damaged && id==='archive-search') return new Response('x'.repeat(LOCAL_DATA_LIMITS.replyBytes+1));
    const rows=[0,1].map(row=>({row,featureId:18883064,site:'USGS-06814000',text:PRIVATE_FIXTURE}));
    const offset=Number(query.offset ?? 0);
    const page=rows.slice(offset,offset+Number(query.limit ?? 2));
    return Response.json({
      format:dataset.format ?? 'kfm-local-data-v1',dataset:id,[dataset.rowsKey ?? 'rows']:page,
      count:page.length,collection:query.collection,generatedAt:at,cache:{state:'live',at},source:dataset.source,
    });
  }};
}

test('acceptance verifier checks every registered public reader and reports metadata only', async () => {
  const mock=fixture();
  const report=await verifyLocalData(ORIGIN,mock.fetcher);
  assert.deepEqual(report.failures,[]);
  assert.deepEqual(report.routes,{expected:DATASETS.size,verified:DATASETS.size});
  for(const id of DATASETS.keys())assert.ok(mock.calls.includes('/api/local-data/'+id),id);
  assert.ok(!JSON.stringify(report).includes(PRIVATE_FIXTURE));
  assert.ok(report.evidence.every(item=>!Object.hasOwn(item,'body')));
});

test('catalogue drift, overflow and a missing prerequisite remain individually diagnosable',async () => {
  const mock=fixture({damaged:true});
  const report=await verifyLocalData(ORIGIN,mock.fetcher);
  assert.ok(report.failures.some(row=>row.label==='catalog'&&row.error.includes('routes differ')));
  assert.ok(report.failures.some(row=>row.label.startsWith('/api/local-data/nwm-reaches')&&row.error==='INVALID_JSON'));
  assert.ok(report.failures.some(row=>row.label.startsWith('/api/local-data/archive-search')&&row.error==='BYTE_LIMIT'));
  assert.ok(report.failures.some(row=>row.label==='nwm-streamflow'&&row.error.includes('required identifier')));
  assert.ok(mock.calls.includes('/api/local-data/usgs-streamflow'));
  assert.ok(!JSON.stringify(report).includes(PRIVATE_FIXTURE));
});
