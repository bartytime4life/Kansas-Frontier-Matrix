import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
const compile=async path=>ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const uri=s=>`data:text/javascript;base64,${Buffer.from(s).toString('base64')}`;
const bounded=uri(await compile('app/bounded-json.ts'));
const server=await compile('app/crop-casma-preview-server.ts');
const load=()=>import(uri(server.replace('"./bounded-json"',JSON.stringify(bounded))+`\n//${Math.random()}`));
const {previewSourceRow}=await import(uri(await compile('app/crop-casma-preview.ts')));
const xml='<WMS_Capabilities><Name>SMAP-HYB-1KM-DAILY_2026.09.28_PM</Name><Name>SMAP-HYB-1KM-DAILY_2026.09.27_PM</Name></WMS_Capabilities>';
test('capabilities retain only real calendar days from the requested year and PM product',async()=>{
 const {previewDays}=await load();assert.deepEqual(previewDays(xml,2026,'2026-10-09'),['2026-09-28','2026-09-27']);
 assert.deepEqual(previewDays(xml,2025),[]);
 assert.deepEqual(previewDays(xml.replaceAll('09.28','02.30'),2026,'2026-09-27'),['2026-09-27']);
 assert.throws(()=>previewDays('<ServiceException/>',2026));
});
test('preview uses fixed provider and 4326 latitude-first Kansas bounds; rejects unknown days and malformed images',async()=>{
 const original=globalThis.fetch,calls=[];const {cropCasmaPreview}=await load();
 globalThis.fetch=async(url,options)=>{calls.push({url,options});return new Response(String(url).includes('GetCapabilities')?xml:'not a PNG',{headers:{'Content-Type':String(url).includes('GetCapabilities')?'text/xml':'image/png'}});};
 try {
  const available=await (await cropCasmaPreview(new Request('https://site/api'))).json();assert.equal(available.mode,'preview');assert.equal(available.day,'2026-09-28');
  assert.equal((await cropCasmaPreview(new Request('https://site/api?day=2026-09-26'))).status,404);assert.equal(calls.length,1);
  assert.equal((await cropCasmaPreview(new Request('https://site/api?url=https://evil'))).status,400);
  assert.equal((await cropCasmaPreview(new Request('https://site/api?day=2026-09-28'))).status,502);
  const url=new URL(calls.at(-1).url);assert.equal(url.hostname,'cloud.csiss.gmu.edu');assert.equal(url.searchParams.get('CRS'),'EPSG:4326');assert.equal(url.searchParams.get('BBOX'),'36.95,-102.1,40.05,-94.55');assert.equal(calls.at(-1).options.redirect,'manual');
 }finally{globalThis.fetch=original;}
});
test('image reprojection uses monotonic nearest rows with correct north/south placement',()=>{
 const rows=Array.from({length:512},(_,i)=>previewSourceRow(i,512));assert.equal(rows[0],0);assert.equal(rows.at(-1),511);
 assert.ok(rows.every((n,i)=>Number.isInteger(n)&&n>=0&&n<512&&(i===0||n>=rows[i-1])));
 assert.notEqual(rows[256],256,'latitude rows are not incorrectly treated as Mercator rows');
});
