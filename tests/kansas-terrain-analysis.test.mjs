import test from 'node:test';import assert from 'node:assert/strict';import {readFile} from 'node:fs/promises';import ts from 'typescript';import {groundFixture} from './kansas-ground-fixtures.mjs';
const url=s=>'data:text/javascript;base64,'+Buffer.from(ts.transpileModule(s,{compilerOptions:{target:ts.ScriptTarget.ES2022,module:ts.ModuleKind.ESNext}}).outputText).toString('base64'),groundURL=url(await readFile('app/kansas-ground.ts','utf8')),ground=await import(groundURL),analysis=await import(url((await readFile('app/kansas-terrain-analysis.ts','utf8')).replace("from './kansas-ground'","from '"+groundURL+"'")));
test('Horn slope uses separate WGS84 east/north physical metrics and the unscaled output plane',()=>{
 const f=groundFixture(),g=f.receipt.grid,w=96;g.ground=Array.from({length:9216},(_,i)=>Math.fround(350+.2*(i%w)*g.cellSize3857[0]-.3*Math.floor(i/w)*g.cellSize3857[1]));const before=JSON.stringify(g),a=analysis.analyzeGroundGrid(g),index=48*w+48,cell=ground.groundCell(g,index),metric=analysis.groundMetricScale(cell.latitude),expected=Math.atan(Math.hypot(.2/metric[0],.3/metric[1]))*180/Math.PI;
 assert.notEqual(metric[0],metric[1]);assert.ok(Math.abs(a.slope[index]-expected)<.0002);assert.ok(Math.abs(a.localRelief[index])<.0001);assert.equal(a.slope[0],null);assert.equal(a.localRelief[2*w+2],null);assert.equal(JSON.stringify(g),before);
});
test('raised-cell relief is center minus strict49-cell mean; source gaps never become derivatives',()=>{
 const g=groundFixture().receipt.grid,i=48*96+48;g.ground.fill(0);g.ground[i]=49;let a=analysis.analyzeGroundGrid(g);assert.equal(a.localRelief[i],48);assert.equal(a.slope[i],0);assert.ok(a.slope[i+1]>0);g.ground[i+1]=null;a=analysis.analyzeGroundGrid(g);assert.equal(a.slope[i],null);assert.equal(a.localRelief[i],null);assert.equal(a.localRelief[i+4],null);assert.notEqual(a.localRelief[i+5],null);assert.equal(g.ground[i],49);
});
test('reproducible terrain study keeps exact source/mask/hash and explicit fixed recipe, never display exaggeration or private credentials',()=>{
 const f=groundFixture(),j=JSON.parse(analysis.terrainStudyJSON(f.receipt));assert.equal(j.format,'kfm-terrain-study-v1');assert.equal(j.source.grid.source.sha256,f.receipt.grid.source.sha256);assert.deepEqual(j.source.grid.ground,f.receipt.grid.ground);assert.equal(j.recipe.slope.window,3);assert.equal(j.recipe.localRelief.window,7);assert.equal(j.derived.slope.length,9216);assert.match(j.recipe.scope,/not native survey resolution/);assert.equal(j.exaggeration,undefined);const invalid=structuredClone(f.receipt);invalid.grid.source.requestUrl='https://user:secret@example.test/';assert.throws(()=>analysis.terrainStudyJSON(invalid),/validated/);
});

test('local-relief renderer/legend domain is symmetric with centeredzero, explicit flat fallback and no invented missing spread',()=>{
 assert.deepEqual(analysis.terrainColorDomain([-2,0,7,null],'local-relief'),[-7,7]);assert.deepEqual(analysis.terrainColorDomain([0,0,null],'local-relief'),[0,0]);assert.equal(analysis.terrainColorDomain([null,null],'local-relief'),null);assert.deepEqual(analysis.terrainColorDomain([-2,0,7],'height'),[-2,7]);
});


test('top illumination uses supported unscaled physical gradients and a fixed NW light; holes never invent normals',()=>{
 const w=5,h=5,make=(east,north)=>Array.from({length:w*h},(_,i)=>100+east*(i%w)*2-north*Math.floor(i/w)*3),toward=analysis.terrainGradients(make(1,-1),w,h,()=>[2,3]),away=analysis.terrainGradients(make(-1,1),w,h,()=>[2,3]),i=12;
 assert.deepEqual(toward[i],{east:1,north:-1});assert.deepEqual(away[i],{east:-1,north:1});assert.ok(analysis.terrainIllumination(toward[i])>analysis.terrainIllumination(away[i]));assert.equal(toward[0],null);const masked=make(1,-1);masked[i-1]=null;assert.equal(analysis.terrainGradients(masked,w,h,()=>[2,3])[i],null);assert.equal(analysis.terrainIllumination(null),.82);const flat=analysis.terrainGradients(make(0,0),w,h,()=>[2,3]);assert.ok(Math.abs(analysis.terrainIllumination(flat[i])-(.55+.45*Math.SQRT1_2))<1e-12);assert.equal(analysis.TERRAIN_ANALYSIS_RECIPE.illumination.heights,'Unscaled; independent of visual relief');
});
