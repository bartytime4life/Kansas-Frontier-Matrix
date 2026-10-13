import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
async function load(name) {
  const js = ts.transpileModule(await readFile(new URL(`../app/${name}.ts`, import.meta.url), 'utf8'), { compilerOptions: { module:ts.ModuleKind.ESNext, target:ts.ScriptTarget.ES2022 } }).outputText;
  return import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
}
const m = await load('subsurface-materials');
const classify = (description, kind='well', interpreted='') => m.materialFor({top:0,bottom:10,description,interpreted},kind);
test('display textures only classify unambiguous original log material', () => {
  for (const [text,id] of [['brown clay','clay'],['fine sand','sand'],['sandstone','sandstone'],['dark shale','shale'],['rock salt','salt'],['halite','salt'],['galena','ore'],['topsoil','soil'],['coal','coal']]) assert.equal(classify(text),id);
  for (const text of ['no coal','possible salt','sand and clay','trace galena','unknown','soil with oil','water-bearing sand','gas in shale','brine','sand?']) assert.equal(classify(text),'unknown',text);
  assert.equal(classify('unclassified','well','shale'),'unknown');
  assert.equal(classify('sandstone','core'),'inventory');
});
test('oil does not match soil, fluid words never generate resource volumes', () => {
  for(const text of ['oil','oil shale','gas','natural gas','water','salt water','no water','oil-bearing sandstone']) assert.equal(classify(text),'unknown');
});
test('material textures are deterministic, opaque and bounded; inventory stays neutral', () => {
  for(const material of m.MATERIALS) {
    const first=m.materialPixels(material.id);assert.equal(first.length,64*64*4);assert.deepEqual(first,m.materialPixels(material.id));
    for(let i=3;i<first.length;i+=4) assert.equal(first[i],255);
  }
  const neutral=m.materialPixels('inventory');for(let i=4;i<neutral.length;i++) assert.equal(neutral[i],neutral[i%4]);
  for(const size of [0,7,129,Infinity,32.5]) assert.throws(()=>m.materialPixels('sand',size));
});
test('timeline uses dated records; unknown and future records are held at a cutoff', () => {
  const a={sourceTime:'1980-02-29'},b={sourceTime:'2000-01-01'};
  assert.equal(m.recordYear(a),1980);assert.equal(m.atRecordYear(a,1980),true);assert.equal(m.atRecordYear(b,1980),false);
  for(const sourceTime of ['','unknown','1990','1900-02-29','2020-02-31','1800-99-99']) { const record={sourceTime};assert.equal(m.recordYear(record),null);assert.equal(m.atRecordYear(record,2026),false);assert.equal(m.atRecordYear(record,null),true); }
});
