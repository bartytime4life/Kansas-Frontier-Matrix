import test from 'node:test';
import assert from 'node:assert/strict';
import {terrainModules as modules} from './terrain-preparation-harness.mjs';
import {groundFixture} from './kansas-ground-fixtures.mjs';
import {kansasFixture} from './kansas-lidar-fixtures.mjs';
const m=modules['terrain-insights'],analysis=modules['kansas-terrain-analysis'];
function ground(values){const grid=groundFixture().receipt.grid;grid.ground=values??grid.ground;return {key:'ground:16/1/1',grid,mode:'ground',eligible:new Uint8Array(9216).fill(1),start:0,analysis:null};}
test('drawn-only tile statistics exclude unrendered extremes and mask offsets preserve original source indices',()=>{
 const b=ground(new Array(9216).fill(500));b.grid.ground[0]=-200;b.grid.ground[2]=0;b.grid.ground[4]=40;b.grid.ground[6]=9000;b.start=9;b.eligible=new Uint8Array(9225);b.eligible[11]=1;b.eligible[13]=1;b.analysis={slope:new Array(9216).fill(null),localRelief:[],gradients:[]};b.analysis.slope[2]=5;b.analysis.slope[4]=3;
 const result=m.readTerrainInsights(b);assert.equal(result.count,2);assert.deepEqual(result.low,{index:2,value:0});assert.deepEqual(result.high,{index:4,value:40});assert.equal(result.span,40);assert.deepEqual(result.steepest,{index:2,value:5});assert.equal(m.insightEligible(b,0),false);assert.equal(m.insightEligible(b,-1),false);assert.equal(m.insightEligible(b,9216),false);
});
test('source-row curve survives stride-four LOD while keyboard targets include only actual drawn columns',()=>{
 const b=ground();b.eligible.fill(0);for(let col=0;col<96;col+=4)b.eligible[col]=1;const profile=m.terrainRowProfile(b,0);assert.equal(profile.values.length,96);assert.equal(profile.values.filter(v=>v!==null).length,96);assert.equal(profile.indices.length,24);assert.deepEqual(profile.indices.slice(0,3),[0,4,8]);assert.equal(profile.drawn[1],false);assert.equal(m.terrainProfileGeometry(profile).paths.length,1);assert.equal((m.terrainProfileGeometry(profile).paths[0].match(/L/g)??[]).length,95);assert.equal(profile.units,'approximate ground metres');assert.ok(profile.distance>0);assert.ok(profile.distances[1]<b.grid.cellSize3857[0]);assert.equal(profile.distances[0],0);
});
test('NoData breaks paths and isolated negative, zero and flat source readings remain visible without smoothing',()=>{
 const b=ground(new Array(9216).fill(null));b.grid.ground[0]=-5;b.grid.ground[2]=0;b.grid.ground[3]=0;b.grid.ground[5]=-5;const profile=m.terrainRowProfile(b,0),geometry=m.terrainProfileGeometry(profile);assert.equal(profile.low,-5);assert.equal(profile.high,0);assert.equal(geometry.paths.length,3);assert.equal(geometry.paths[0].includes('L'),false);assert.equal(geometry.paths[1].includes('L'),true);assert.equal(geometry.points[1],null);assert.ok(geometry.points[0]);
 b.grid.ground.fill(-12);const flat=m.terrainProfileGeometry(m.terrainRowProfile(b,2));assert.equal(flat.points[0].y,50);assert.equal(flat.points[95].y,50);assert.doesNotMatch(flat.paths.join(''),/NaN|Infinity/);assert.equal(m.readTerrainInsights(b).span,0);
 b.grid.ground.fill(null);const empty=m.readTerrainInsights(b);assert.equal(empty.count,0);assert.equal(empty.span,null);assert.equal(empty.low,null);assert.equal(m.terrainRowProfile(b,0).indices.length,0);assert.equal(m.terrainRowProfile(b,-1),null);assert.equal(m.terrainRowProfile(b,96),null);
});
test('Ground, Surface and Canopy retain their own source quantities; canopy rejects unsupported or negative heights',()=>{
 const grid=kansasFixture(['surface','canopy']).grid;grid.ground=[100,100,null,100];grid.surface=[102,105,108,null];grid.canopy=[2,0,8,-1];const binding={key:'native',grid,mode:'surface',eligible:new Uint8Array(4).fill(1),start:0,analysis:null};
 assert.deepEqual(m.terrainRowProfile(binding,0).values,[102,105]);assert.equal(m.readTerrainInsights(binding).high.value,108);
 binding.mode='canopy';assert.deepEqual(m.terrainRowProfile(binding,0).values,[2,0]);assert.deepEqual(m.terrainRowProfile(binding,1).values,[null,null]);assert.equal(m.readTerrainInsights(binding).count,2);assert.equal(m.readTerrainInsights(binding).high.value,2,'canopy is height above ground, never ground + height');assert.equal(m.readTerrainInsights(binding).steepest,null);assert.equal(m.terrainRowProfile(binding,0).distance,grid.cellSizeM[0]);assert.equal(m.terrainRowProfile(binding,0).units,'UTM grid metres');assert.ok(m.insightCellCenter(binding,0).every(Number.isFinite));
 const bad={...ground(),mode:'surface'};assert.throws(()=>m.readTerrainInsights(bad),/does not match/);assert.throws(()=>m.terrainRowProfile(bad,0),/does not match/);
});
test('binding requires exact grid, mask, quantity, key and offset, not just reused query names',()=>{
 const a=ground(),b={...a};assert.equal(m.sameInsightBinding(a,b),true);for(const patch of [{grid:{...a.grid}},{eligible:new Uint8Array(a.eligible)},{mode:'surface'},{key:'replacement'},{start:1}])assert.equal(m.sameInsightBinding(a,{...a,...patch}),false);assert.equal(m.sameInsightBinding(a,null),false);assert.equal(m.insightCellCenter({...a,eligible:new Uint8Array(9216)},0),null);assert.throws(()=>m.readTerrainInsights({...a,grid:{...a.grid,width:97}}),/bounded/);
});
test('steepest means the largest supported Ground derivative among drawn samples only',()=>{
 const b=ground();b.analysis=analysis.analyzeGroundGrid(b.grid);b.eligible.fill(0);const index=96+1;b.eligible[index]=1;const result=m.readTerrainInsights(b);assert.equal(result.steepest.index,index);assert.equal(result.steepest.value,b.analysis.slope[index]);b.eligible.fill(0);b.eligible[0]=1;assert.equal(m.readTerrainInsights(b).steepest,null,'edges lack complete Horn support');
});
