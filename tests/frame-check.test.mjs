import assert from 'node:assert/strict';
import test from 'node:test';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
const source=await readFile(new URL('../app/frame-check.tsx',import.meta.url),'utf8');
const code=ts.transpileModule(source,{compilerOptions:{target:ts.ScriptTarget.ES2022,module:ts.ModuleKind.CommonJS,jsx:ts.JsxEmit.ReactJSX}}).outputText;
let flowState={cells:[],cues:[]};
const mod={exports:{}};new Function('require','module','exports',code)(id=>id==='./map-performance'?{uploadedGeoJSON:source=>source.data}:id==='./water-flow-sync'?{waterFlowDiagnosticState:()=>flowState}:{},mod,mod.exports);
const {frameStatistics,displaySignature}=mod.exports;
test('reports actual counts and elapsed time without manufacturing 60 FPS',()=>{
 const sixty=frameStatistics(Array(600).fill(1000/60),10000);assert.equal(sixty.fps,60);assert.equal(sixty.over25ms,0);
 const stalled=frameStatistics([...Array(90).fill(16.7),...Array(10).fill(66.7)],3000);assert.ok(stalled.fps<34);assert.equal(stalled.p95Ms,66.7);assert.equal(stalled.over25ms,10);
 assert.equal(frameStatistics([],0).fps,0);assert.equal(frameStatistics([],1000).p95Ms,0);
});
test('camera changes preserve the geometry/value digest; changed coordinates, values or timestamps do not',async()=>{
 const feature={type:'Feature',geometry:{type:'Point',coordinates:[-98,38]},properties:{value:4,unit:'ft',observedAt:'2026-10-12T12:00:00Z'}};
 const source={type:'geojson',data:{type:'FeatureCollection',features:[feature]}};
 const map={getStyle:()=>({sources:{gauge:{type:'geojson',data:'ignored-worker-copy'}}}),getSource:()=>source};
 const before=await displaySignature(map);assert.equal(await displaySignature(map),before);
 for(const modified of [{...feature,geometry:{...feature.geometry,coordinates:[-97,38]}},{...feature,properties:{...feature.properties,value:5}},{...feature,properties:{...feature.properties,observedAt:'2026-10-12T13:00:00Z'}}]){
   source.data.features=[modified];assert.notEqual(await displaySignature(map),before);
 }
});

test('flow provider bends, directions and gauge cues contribute to the display digest',async()=>{
 const map={getStyle:()=>({sources:{}}),getSource:()=>undefined};
 flowState={cells:[{key:'-98.25,38.25',reaches:[{id:'R1',coordinates:[[-98.2,38.3],[-98.1,38.3]],downstream:1}]}],cues:[{moving:false,intensity:.5,tint:'unknown',coordinate:[-98.2,38.3]}]};
 const before=await displaySignature(map);
 flowState.cells[0].reaches[0].coordinates[1]=[-98.15,38.31];
 assert.notEqual(await displaySignature(map),before);
 const bend=await displaySignature(map);flowState.cells[0].reaches[0].downstream=2;
 assert.notEqual(await displaySignature(map),bend);
 const direction=await displaySignature(map);flowState.cues[0].moving=true;
 assert.notEqual(await displaySignature(map),direction);
 flowState={cells:[],cues:[]};
});
