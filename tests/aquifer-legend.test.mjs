import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';

const load=async path=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,()=>({}));return exports;};
const {GROUNDWATER_CLASS_LEGENDS}=await load('app/aquifer-layers.ts');

test('the aquifer legends are the KGS snapshot classes, in feet order, with the colours the map draws',async()=>{
 const feet=label=>label.startsWith('Under ')?0:label.startsWith('Over ')?Number(label.slice(5)):Number(label.split(' to ')[0]);
 for(const [id,legend] of Object.entries(GROUNDWATER_CLASS_LEGENDS)){
  const snapshot=JSON.parse(await readFile(`public/data/groundwater/${id}.geojson`,'utf8'));
  const drawn=new Map(snapshot.features.filter(f=>f.properties.hasValue).map(f=>[f.properties.classLabel,f.properties.color]));
  assert.deepEqual(legend.map(e=>e.label).sort(),[...drawn.keys()].sort(),`${id}: every class the snapshot draws, and no other`);
  for(const entry of legend)assert.equal(entry.color,drawn.get(entry.label),`${id}: ${entry.label} has the snapshot's colour`);
  const order=legend.map(e=>feet(e.label));
  assert.deepEqual(order,[...order].sort((a,b)=>a-b),`${id}: shallow or thin first`);
 }
 assert.equal(GROUNDWATER_CLASS_LEGENDS['kgs-saturated-thickness'].at(-1).label,'Over 300');
 assert.equal(GROUNDWATER_CLASS_LEGENDS['kgs-depth-to-water'].at(-1).label,'Over 350');
});
