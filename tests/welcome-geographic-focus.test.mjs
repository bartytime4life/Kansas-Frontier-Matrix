import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';

const compiled={};
new Function('exports',ts.transpileModule(await readFile('app/living-welcome/geographic-focus.ts','utf8'),{
 compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022},
}).outputText)(compiled);

test('the source spotlight retains provider geometry and values and disappears without its selected record',()=>{
 const sources=new Map(),layers=new Map();
 const map={getSource:id=>sources.get(id),getLayer:id=>layers.get(id),addSource:(id,value)=>sources.set(id,value),addLayer:layer=>layers.set(layer.id,layer),removeLayer:id=>layers.delete(id),removeSource:id=>sources.delete(id)};
 // Deliberately synthetic test record: the renderer cannot insert a real-world
 // population constant, a rectangle in place of a provider polygon, or a label
 // representing a different source year.
 const feature={type:'Feature',properties:{geoid:'20177',name:'Fixture',population:1234},geometry:{type:'Polygon',coordinates:[[[-95.9,39],[-95.7,39],[-95.8,39.2],[-95.9,39]]]}};
 const payload={data:{type:'FeatureCollection',features:[feature]}};
 compiled.syncGeographicFocus(map,'evidence',true,payload);
 assert.equal(sources.get('welcome-census-record-focus').data.features[0],feature,'the exact provider feature reaches the geographic renderer');
 const text=layers.get('welcome-census-record-focus-label').layout['text-field'];
 assert.ok(JSON.stringify(text).includes('["get","population"]'),'the displayed value is read from that feature');
 assert.ok(JSON.stringify(text).includes('["get","name"]'));
 for(const layer of layers.values())assert.equal(layer.source,'welcome-census-record-focus');
 compiled.syncGeographicFocus(map,'evidence',false,payload);
 assert.equal(layers.size,0);assert.equal(sources.size,0);
 compiled.syncGeographicFocus(map,'evidence',true,{data:{type:'FeatureCollection',features:[]}});
 assert.equal(sources.size,0,'missing geography has no substitute outline or population');
 compiled.syncGeographicFocus(map,'evidence',true,payload);
 compiled.syncGeographicFocus(map,'fauna',true,payload);
 assert.equal(layers.size,0);assert.equal(sources.size,0,'the county focus cannot linger on another topic');
});
