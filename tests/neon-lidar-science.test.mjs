import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { recordModel, recordsCSV, analysisContextCSV } from '../app/living-welcome/stories/record-model.mjs';
import { scienceMetrics, scientificSummary, relationship } from '../app/living-welcome/stories/science-model.mjs';

const moduleUrl = source => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString('base64')}`;
const previewUrl = moduleUrl(await readFile('app/neon-lidar-preview.ts', 'utf8'));
const boundedUrl = moduleUrl(await readFile('app/bounded-json.ts', 'utf8'));
const pilotUrl = moduleUrl((await readFile('app/neon-lidar-pilot-client.ts', 'utf8')).replace('"./bounded-json"', JSON.stringify(boundedUrl)).replace('"./neon-lidar-preview"', JSON.stringify(previewUrl)));
const adapterUrl = moduleUrl((await readFile('app/neon-lidar-science.ts', 'utf8')).replace('"./neon-lidar-pilot-client"', JSON.stringify(pilotUrl)).replace('"./neon-lidar-preview"', JSON.stringify(previewUrl)));
const { createNeonScienceDataset, neonScienceDatasetJSON } = await import(adapterUrl);

function fixture() {
  const width = 8, tile = 'NEON_D06_KONZ_DP3_706000_4336000';
  return {
    format: 'kfm-neon-relay-pilot-v1', generatedAt: '2026-11-23T12:00:00Z',
    cache: { state: 'fresh', at: '2026-11-23T13:00:00Z' },
    review: { status: 'pending', scientific_accuracy_verified: false, source_admitted: false,
      canopy_native_max_m: 83.41000366210938, canopy_native_cells_above_50m: 5,
      surface_minus_ground_native_max_m: 32.5, notes: ['Analytic test fixture: invented test values, not real NEON observations.'] },
    preview: {
      schema_version: 'kfm-neon-lidar-preview-v1', data_kind: 'provider-files', generated_at: '2026-11-23T11:00:00Z',
      lifecycle: 'local-preview-only', source_admitted: false, released: false,
      source: {
        site: 'KONZ', month: '2024-09', acquisition_run: '2024_KONZ_10', release: 'RELEASE-2026', tile,
        attribution: 'Analytic test fixture only', horizontal_crs: 'PROJCRS["Test UTM grid"]',
        vertical_reference: 'Test vertical reference', vertical_reference_basis: 'Test metadata',
        canopy_floor_m: null, canopy_floor_basis: 'Unknown test sensor',
        files: ['dtm','dsm','chm'].map((kind,index) => ({ kind, name: `${tile}_${kind.toUpperCase()}.tif`, product: kind==='chm'?'DP3.30015.001':'DP3.30024.001', bytes: 1000+index, sha256: 'abc'[index].repeat(64) })),
      },
      grid: { width, height: width, bounds: [706000,4336000,707000,4337000], source_resolution_m: 1,
        preview_resolution_m: 125, sampling: 'nearest-neighbor',
        dtm: Array(64).fill(-2.125), dsm: Array(64).fill(4.25), chm: Array(64).fill(3.75) },
    },
  };
}

test('science rows preserve source numbers, native sample positions and independent canopy', () => {
  const input = fixture(), before = structuredClone(input), result = createNeonScienceDataset(input);
  assert.ok(result); assert.deepEqual(input,before);
  const first = result.bundle.data.records[0], last = result.bundle.data.records.at(-1);
  assert.equal(result.bundle.data.records.length,64);
  assert.deepEqual([first.row,first.column,first.easting_m,first.northing_m],[1,1,706062.5,4336937.5]);
  assert.deepEqual([last.row,last.column,last.easting_m,last.northing_m],[8,8,706937.5,4336062.5]);
  assert.deepEqual([first.dtm_m,first.dsm_m,first.chm_m,first.surface_above_ground_m],[-2.125,4.25,3.75,6.375]);
  assert.notEqual(first.chm_m,first.surface_above_ground_m);
  assert.equal(new Set(result.bundle.data.records.map(row=>row.id)).size,64);
});

test('null, valid zero, negative differences and overflow remain distinguishable', () => {
  const input=fixture(),g=input.preview.grid;
  g.dtm[0]=null;g.dsm[0]=0;g.chm[0]=0;
  g.dtm[1]=2;g.dsm[1]=-1;
  g.dtm[2]=-1e308;g.dsm[2]=1e308;
  const rows=createNeonScienceDataset(input).bundle.data.records;
  assert.deepEqual([rows[0].dtm_m,rows[0].dsm_m,rows[0].chm_m,rows[0].surface_above_ground_m,rows[0].difference_status],[null,0,0,null,'missing']);
  assert.equal(rows[1].surface_above_ground_m,-3);assert.equal(rows[1].difference_status,'negative');
  assert.equal(rows[2].surface_above_ground_m,null);assert.equal(rows[2].difference_status,'nonfinite');
});

test('source/schema/admission gates apply before a science dataset can be created', () => {
  const mutations=[x=>x.review.scientific_accuracy_verified=true,x=>x.review.source_admitted=true,
    x=>x.preview.data_kind='synthetic-test',x=>x.preview.source.site='KONA',x=>x.preview.grid.dtm.pop(),
    x=>x.preview.grid.chm[0]=Infinity,x=>x.preview.released=true,x=>x.cache.state='current-observation'];
  for(const mutate of mutations){const input=fixture();mutate(input);assert.equal(createNeonScienceDataset(input),null);}
  for(const input of [null,{},[],fixture().preview])assert.equal(createNeonScienceDataset(input),null);
});

test('all three raw identities survive without invented retrieval times or geography/time coordinates', () => {
  const data=createNeonScienceDataset(fixture()).bundle.data,model=recordModel({data});
  assert.deepEqual(data.sourceSnapshots.map(x=>x.rawSha256),['a','b','c'].map(x=>x.repeat(64)));
  assert.ok(data.sourceSnapshots.every(x=>x.retrievedAt===null&&x.queryUrl===null));
  assert.equal(model.first,null);assert.equal(model.last,null);
  assert.equal(model.categories.length,1);
  assert.deepEqual(scienceMetrics(model).map(x=>x.key),['dtm_m','dsm_m','chm_m','surface_above_ground_m']);
  assert.ok(data.records.every(x=>!('geometry' in x)&&!('latitude' in x)&&!('longitude' in x)&&!('year' in x)&&!('date' in x)));
  assert.equal(data.analysisContext.time.observation_date,null);
  assert.equal(data.analysisContext.time.original_file_retrieval_times,null);
  assert.equal(data.analysisContext.time.cache.at,'2026-11-23T13:00:00Z');
});

test('existing science tools compute known sparse quartiles and sample SD from exactly these rows', () => {
  const input=fixture();input.preview.grid.chm.fill(null);input.preview.grid.chm.splice(0,4,0,1,3,6);
  const rows=createNeonScienceDataset(input).bundle.data.records,summary=scientificSummary(rows,'chm_m');
  assert.deepEqual([summary.total,summary.count,summary.missing,summary.mean,summary.median,summary.q1,summary.q3],[64,4,60,2.5,2,.75,3.75]);
  assert.ok(Math.abs(summary.standardDeviation-Math.sqrt(7))<1e-12);
});

test('relationship tool uses complete pairs and keeps provider canopy separate from the derived difference', () => {
  const input=fixture(),g=input.preview.grid;for(const key of ['dtm','dsm','chm'])g[key].fill(null);
  for(let i=0;i<5;i++){g.dtm[i]=100;g.dsm[i]=102+2*i;g.chm[i]=i===4?null:i;}
  const dataset=createNeonScienceDataset(input),fit=relationship(dataset.bundle.data.records,'chm_m','surface_above_ground_m');
  assert.equal(fit.count,4);assert.equal(fit.excluded,60);assert.equal(fit.pearson,1);assert.equal(fit.spearman,1);assert.equal(fit.slope,2);assert.equal(fit.intercept,2);
  assert.match(dataset.bundle.data.limits.join(' '),/spatially dependent/);
  assert.match(dataset.bundle.data.limits.join(' '),/arithmetically correlated/);
});

test('record CSV retains numeric zeros/nulls, all hashes and source/cache/review context', () => {
  const input=fixture();input.preview.grid.dtm[0]=null;input.preview.grid.chm[0]=0;input.cache.state='stale';
  const dataset=createNeonScienceDataset(input),csv=recordsCSV(dataset.bundle),[head,row]=csv.rows;
  const value=key=>row[head.indexOf(key)];
  assert.equal(value('chm_m'),0);assert.equal(value('dtm_m'),'');assert.equal(value('surface_above_ground_m'),'');
  assert.equal(value('snapshot_sha256'),['a','b','c'].map(x=>x.repeat(64)).join(' | '));
  assert.equal(value('snapshot_retrieved_at'),' |  | ');
  const context=JSON.parse(value('analysis_context'));
  assert.equal(context.source.catalog_month,'2024-09');assert.equal(context.time.cache.state,'stale');
  assert.equal(context.review.source_admitted,false);assert.equal(context.review.scientific_accuracy_verified,false);
  assert.equal(context.review.canopy_native_max_m,83.41000366210938);
  assert.equal(context.sampling.display_resolution_m,125);assert.equal(context.references.height_values_transformed,false);
});

test('portable science JSON regenerates derived rows and preserves the receipt instead of exporting altered results', () => {
  const dataset=createNeonScienceDataset(fixture());dataset.bundle.data.records[0].chm_m=999;
  const saved=JSON.parse(neonScienceDatasetJSON(dataset));
  assert.equal(saved.format,'kfm-neon-science-v1');assert.equal(saved.bundle.data.records[0].chm_m,3.75);
  assert.equal(saved.receipt.review.scientific_accuracy_verified,false);
  dataset.receipt.review.source_admitted=true;
  assert.throws(()=>neonScienceDatasetJSON(dataset),/no longer valid/);
});

test('existing CSV shapes stay unchanged and malformed/oversized analysis context refuses export', () => {
  const bundle={story:'existing',sources:[],data:{columns:[{key:'value',type:'number'}],records:[{value:0}]}};
  assert.deepEqual(recordsCSV(bundle).rows,[['value','source_urls','snapshot_retrieved_at','snapshot_sha256'],[0,'','','']]);
  assert.equal(analysisContextCSV(undefined),null);
  const cycle={};cycle.self=cycle;
  for(const value of [null,[],0,'text',cycle,{text:'x'.repeat(24000)}])assert.throws(()=>analysisContextCSV(value),/Invalid analysis context/);
});
