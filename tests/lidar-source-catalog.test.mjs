import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
const moduleUrl=source=>'data:text/javascript;base64,'+Buffer.from(source).toString('base64');
const compile=source=>ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const catalogUrl=moduleUrl(compile(await readFile(new URL('../app/lidar-source-catalog.ts',import.meta.url),'utf8')));
const catalog=await import(catalogUrl);
const route=await import(moduleUrl(compile(await readFile(new URL('../app/api/lidar/sources/route.ts',import.meta.url),'utf8')).replace('from "../../../lidar-source-catalog"',`from "${catalogUrl}"`)));

test('the public catalog is the shared metadata projection and starts no acquisition',async()=>{
 const original=globalThis.fetch;let calls=0;
 globalThis.fetch=async()=>{calls++;throw Error('source metadata must not acquire data');};
 try{
  const response=route.GET();assert.equal(response.status,200);
  assert.equal(response.headers.get('X-Content-Type-Options'),'nosniff');
  const result=await response.json();assert.equal(result.format,'kfm-lidar-sources-v1');
  assert.deepEqual(result.sourceFamilies,JSON.parse(JSON.stringify(catalog.KANSAS_LIDAR_SOURCE_CATALOG)));
  assert.deepEqual(result.comparisonRequirements,catalog.LIDAR_COMPARISON_REQUIREMENTS);
  assert.match(result.scope,/not an exhaustive/);assert.equal(calls,0);
 }finally{globalThis.fetch=original;}
});

test('discovery families cannot acquire prepared-science actions or masquerade as a continuous ground grid',()=>{
 const records=catalog.KANSAS_LIDAR_SOURCE_CATALOG;
 assert.equal(new Set(records.map(r=>r.id)).size,records.length);
 for(const record of records){
  assert.equal(catalog.lidarSourceRecord(record.id),record);
  const url=new URL(record.sourceUrl);assert.equal(url.protocol,'https:');assert.equal(url.username,'');assert.equal(url.password,'');
  if(['discovery','access-unverified'].includes(record.readiness))assert.equal(record.actionUrl,undefined);
  if(record.geometry==='orbital-profiles')assert.equal(record.readiness,'discovery');
  if(record.access==='unverified')assert.equal(record.readiness,'access-unverified');
 }
 assert.equal(catalog.lidarSourceRecord('not-configured'),undefined);
 assert.equal(catalog.lidarSourceRecord('usgs-3dep').readiness,'continuous-terrain');
 assert.equal(catalog.lidarSourceRecord('neon').readiness,'sampled-science');
 assert.match(catalog.lidarSourceRecord('noaa-digital-coast').coverage,/Kansas.*not been established/);
});
