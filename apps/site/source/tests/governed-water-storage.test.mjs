import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import ts from "typescript";
const compile = text => ts.transpileModule(text, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const moduleUrl = text => 'data:text/javascript;base64,' + Buffer.from(compile(text)).toString('base64');
const waterUrl = moduleUrl(await readFile(new URL('../app/governed-water.ts', import.meta.url), 'utf8'));
const server = (await readFile(new URL('../app/governed-water-server.ts', import.meta.url), 'utf8'))
 .replace('import { env } from "cloudflare:workers";', 'const env = globalThis.__waterStorage.env;')
 .replace('import { getRawDb } from "../db";', 'const getRawDb = () => globalThis.__waterStorage.db;')
 .replace('"./governed-water"', JSON.stringify(waterUrl));
const snapshot = await readFile(new URL('./fixtures/governed-water/snapshot.json', import.meta.url), 'utf8');
const decision = JSON.parse(await readFile(new URL('./fixtures/governed-water/decision.json', import.meta.url), 'utf8'));
const row = {package_id:decision.package_id,decision_json:JSON.stringify(decision),state:'STAGED'};
const env = {BUCKET:{get:async()=>({size:Buffer.byteLength(snapshot),text:async()=>snapshot})}};
globalThis.__waterStorage={env,db:{prepare:()=>({first:async()=>row})}};
const {governedWaterRead} = await import(moduleUrl(server));
const RealDate=Date;
let clock='2026-09-30T19:00:00Z';
class TestDate extends RealDate {constructor(...args){super(...(args.length?args:[clock]));} static now(){return RealDate.parse(clock);}}
async function request(view='layers',query=''){
 const old=globalThis.Date;globalThis.Date=TestDate;
 try{return await governedWaterRead(new Request('https://example.test/api/governed/v1/'+view+query),view);}finally{globalThis.Date=old;}
}
test('D1 and R2 adapter withholds missing, withdrawn and failed storage',async()=>{
 const get=env.BUCKET.get;
 try{
  globalThis.__waterStorage.db={prepare:()=>({first:async()=>null})};
  assert.equal((await (await request()).json()).envelope.reason_code,'NO_APPROVED_SNAPSHOT');
  globalThis.__waterStorage.db={prepare:()=>({first:async()=>({...row,state:'WITHDRAWN'})})};
  assert.equal((await (await request()).json()).data,undefined);
  globalThis.__waterStorage.db={prepare:()=>({first:async()=>row})};
  env.BUCKET.get=async()=>null;
  assert.equal((await request()).status,503);
  env.BUCKET.get=async()=>{throw new Error('private upstream detail');};
  const failed=await request();assert.equal(failed.status,503);assert.doesNotMatch(await failed.text(),/private upstream/);
 }finally{env.BUCKET.get=get;}
});
test('queries are bounded and approval expiry is evaluated after storage read',async()=>{
 globalThis.__waterStorage.db={prepare:()=>({first:async()=>row})};
 assert.equal((await request('layers','?station_id=USGS-06892518&station_id=USGS-07156900')).status,400);
 const get=env.BUCKET.get;
 try{
  env.BUCKET.get=async()=>{clock='2026-10-01T00:00:01Z';return {size:Buffer.byteLength(snapshot),text:async()=>snapshot};};
  const denied=await (await request()).json();assert.equal(denied.envelope.reason_code,'RELEASE_TIME_INVALID');assert.equal(denied.data,undefined);
 }finally{env.BUCKET.get=get;clock='2026-09-30T19:00:00Z';}
});
