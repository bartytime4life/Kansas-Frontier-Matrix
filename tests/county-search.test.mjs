import test from 'node:test';
import assert from 'node:assert/strict';
import ts from 'typescript';
import vm from 'node:vm';
import {readFile} from 'node:fs/promises';
const source=await readFile(new URL('../app/county-search.ts',import.meta.url),'utf8');
const county=await import('data:text/javascript;base64,'+Buffer.from(ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64'));
const feature={type:'Feature',id:'20053',properties:{name:'Ellsworth',geoid:'20053',featureId:'us-census-county-20053',vintage:'2020'},geometry:{type:'Polygon',coordinates:[[[-98.5,38.5],[-98,38.5],[-98,39],[-98.5,38.5]]]}};
const payload={feed:'census-counties',data:{type:'FeatureCollection',features:[feature]}};

test('loaded Census counties are discoverable by place name, county suffix and FIPS with source edition intact',()=>{
 for(const query of ['Ellsworth','ellsworth county','20053','  ELLSWORTH  ']){
  const results=county.countySearchResults(payload,'ready',query);
  assert.equal(results.length,1);assert.equal(results[0].title,'Ellsworth County');assert.match(results[0].subtitle,/2020.*source context, not KFM evidence/);
 }
 assert.deepEqual(county.countySearchResults(payload,'ready','Saline'),[]);
});
test('loading, failed, empty, foreign and malformed payloads do not expose stale county rows',()=>{
 for(const state of ['idle','loading','error','empty'])assert.deepEqual(county.countySearchResults(payload,state,'Ellsworth'),[]);
 for(const patch of [{feed:'usgs-streamflow'},{data:{features:[]}},{data:{features:[{...feature,properties:{...feature.properties,vintage:'2026'}}]}},{data:{features:[{...feature,properties:{...feature.properties,featureId:'foreign-20053'}}]}}])assert.deepEqual(county.countySearchResults({...payload,...patch},'ready','Ellsworth'),[]);
 assert.deepEqual(county.countySearchResults(payload,'ready',''),[]);
});
test('county framing accepts polygons and multipart geometry, rejects invalid or degenerate coordinates',()=>{
 assert.deepEqual(county.countySearchGeometry(feature),{bounds:[[-98.5,38.5],[-98,39]],focus:[-98.25,38.75]});
 assert.deepEqual(county.countySearchGeometry({...feature,geometry:{type:'MultiPolygon',coordinates:[feature.geometry.coordinates]}}),county.countySearchGeometry(feature));
 for(const geometry of [{type:'Point',coordinates:[-98,38]},{type:'Polygon',coordinates:[]},{type:'Polygon',coordinates:[[[Infinity,38],[-98,39]]]},{type:'Polygon',coordinates:[[[-98,38],[-98,38]]]}])assert.equal(county.countySearchGeometry({...feature,geometry}),null);
});

const page=await readFile(new URL('../app/page.tsx',import.meta.url),'utf8'),tree=ts.createSourceFile('page.tsx',page,ts.ScriptTarget.Latest,true,ts.ScriptKind.TSX);
let choose;
function visit(node){if(ts.isVariableDeclaration(node)&&node.name.getText(tree)==='chooseSearchResult')choose=node.initializer.getText(tree);ts.forEachChild(node,visit);}visit(tree);
test('the actual search action opens the current county in Evidence without WebGL and preserves map time',()=>{
 let current=payload,state='ready';const opened=[],announced=[],visible=[],frames=[];
 const sandbox={...county,officialPayloads:new Proxy({},{get:()=>current}),officialStates:new Proxy({},{get:()=>state}),setPrimaryWorkspace:()=>{},primaryWorkspace:'map',setGlobalQuery:()=>{},announce:v=>announced.push(v),OFFICIAL_CONTEXT_SOURCES:[{id:'census-counties',sourceId:'external-census-counties'}],buildBasemapContext:(feature,...focus)=>({feature,focus}),setOfficialContextVisible:(...v)=>visible.push(v),openSelection:(...v)=>opened.push(v),assistantEvidenceReturnRef:{current:null},globalSearchInputRef:{current:'search-control'},mapRef:{current:null},motionDuration:x=>x,setYear:x=>frames.push(x),window:{setTimeout:()=>{}}};
 const action=vm.runInNewContext(ts.transpileModule('const action='+choose+'; action;',{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText,sandbox);
 const item=county.countySearchResults(payload,'ready','Ellsworth')[0];
 action(item);assert.equal(opened.length,1);assert.equal(opened[0][0].feature.source,'external-census-counties');assert.equal(opened[0][1],'search-control');assert.deepEqual(visible,[['census-counties',true]]);assert.deepEqual(frames,[]);assert.match(announced[0],/Map time is unchanged/);
 current={...payload,data:{features:[]}};action(item);assert.equal(opened.length,1);assert.match(announced.at(-1),/no longer available/);
 current=payload;state='error';action(item);assert.equal(opened.length,1);
});
