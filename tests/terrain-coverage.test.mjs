import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {componentHarness,findNode} from './component-harness.mjs';
import {compileTerrain} from './terrain-preparation-harness.mjs';
import {groundFixture} from './kansas-ground-fixtures.mjs';
import {kansasFixture} from './kansas-lidar-fixtures.mjs';
const coverage={};new Function('exports','require',compileTerrain(await readFile('app/terrain-coverage.ts','utf8')))(coverage,()=>({KANSAS_LIDAR_WINDOW:[-102.2,36.8,-94.4,40.2]}));
const {terrainCoverage,coverageRect}=coverage;
const bounds=[-96.588,38.987,-96.584,38.991];
const tile=(mode,n,b=bounds)=>({key:`${mode}:17/${n}/1`,zoom:17,bounds:b});
const snapshot=(mode,entries,tiles=entries.map(e=>e.tile))=>({version:1,plan:{key:tiles.map(t=>t.key).join('|'),state:'ready',tiles},entries,pending:tiles.length-entries.length,failed:entries.filter(e=>e.error).length});
const ground=(n=0,b=bounds)=>{const f=groundFixture(b);return {tile:tile('ground',n,b),grid:f.receipt.grid,ground:f.receipt,native:null,state:'ready',error:''};};
const native=(mode,n=0)=>{const f=kansasFixture([mode]);return {tile:tile(mode,n),grid:f.grid,ground:null,native:{receipt:f.receipt,grid:f.grid,points:null},state:'partial',error:''};};
const text=n=>n==null||typeof n==='boolean'?'':typeof n==='string'||typeof n==='number'?String(n):[n?.props?.children].flat(Infinity).map(text).join(' ').replace(/\s+/g,' ');
test('coverage distinguishes supported, NoData, pending, closer and failed tiles without treating a failed request as absence',()=>{
 const a=ground(),b=ground(1),empty=ground(2);b.grid.ground[2]=null;empty.grid.ground.fill(null);
 const closer={tile:tile('ground',3),grid:null,ground:null,native:null,state:'detail-required',error:''},failed={...closer,tile:tile('ground',4),state:'unavailable',error:'Provider timeout'},pending=tile('ground',5);
 const c=terrainCoverage(snapshot('ground',[a,b,empty,closer,failed],[a.tile,b.tile,empty.tile,closer.tile,failed.tile,pending]),'ground');
 assert.deepEqual(c.counts,{supported:1,gaps:1,empty:1,closer:1,unavailable:1,pending:1});assert.equal(c.checked,3);assert.equal(c.total,3*9216);assert.equal(c.supported,2*9216-1);assert.equal(c.tiles.find(t=>t.key===failed.tile.key).supported,null);assert.equal(c.tiles.find(t=>t.key===empty.tile.key).supported,0);
});
test('native canopy support requires nonnegative height and the same grid ground; raw survey footprints never imply cell support',()=>{
 const e=native('canopy');e.grid.canopy=[12,4,-1,2];e.grid.ground=[300,null,302,303];const before=structuredClone(e);
 const c=terrainCoverage(snapshot('canopy',[e]),'canopy');assert.equal(c.supported,2);assert.equal(c.total,4);assert.equal(c.tiles[0].state,'gaps');assert.deepEqual(e,before,'coverage must not change source values');
 const absent={...e,grid:null,state:'no-coverage',native:{...e.native,grid:null}};const no=terrainCoverage(snapshot('canopy',[absent]),'canopy');assert.equal(no.tiles[0].state,'empty');assert.equal(no.tiles[0].supported,null);assert.equal(no.total,0,'survey bounds are not cell counts');
});
test('current-mode query keys, Kansas clipping and geographic ordering prevent old or out-of-window coverage from leaking',()=>{
 const a=ground(1,[-97,38,-96.5,38.5]),b=ground(2,[-97,39,-96.5,39.5]),c=ground(3,[-96,39,-95.5,39.5]),old=native('surface');
 const s=snapshot('ground',[a,b,c,old],[c.tile,a.tile,old.tile,b.tile,tile('ground',4,[-110,30,-109,31])]);
 assert.deepEqual(terrainCoverage(s,'ground').tiles.map(t=>t.key),[b.tile.key,c.tile.key,a.tile.key]);assert.deepEqual(terrainCoverage(s,'canopy').tiles,[]);
 const edge=tile('ground',5,[-103,36,-101,38]),model=terrainCoverage(snapshot('ground',[],[edge]),'ground');assert.deepEqual(model.tiles[0].bounds,[-102.2,36.8,-101,38]);
});
test('source receipt cache time is kept distinct from acquisition; immutable replacement recomputes support',()=>{
 const e=ground();e.ground.cache.state='stale';let c=terrainCoverage(snapshot('ground',[e]),'ground');assert.equal(c.tiles[0].checkedAt,e.ground.cache.at);assert.equal(c.tiles[0].stale,true);assert.equal(c.tiles[0].acquisition,e.grid.source.acquisition);
 const replacement={...e,grid:{...e.grid,ground:e.grid.ground.map(()=>null)}};c=terrainCoverage(snapshot('ground',[replacement]),'ground');assert.equal(c.supported,0);assert.equal(c.tiles[0].state,'empty');
});
test('north-up diagram preserves Mercator adjacency and finite geometry at Kansas edges',()=>{
 const extent=[-98,38,-96,40],west=coverageRect([-98,38,-97,40],extent),east=coverageRect([-97,38,-96,40],extent),north=coverageRect([-98,39,-96,40],extent),south=coverageRect([-98,38,-96,39],extent);
 assert.ok(Math.abs(west.x+west.width-east.x)<1e-10);assert.ok(Math.abs(north.y+north.height-south.y)<1e-10);assert.ok(north.y<south.y);for(const v of [west,east,north,south])assert.ok(Object.values(v).every(Number.isFinite));
});
test('coverage component exposes numbered keyboard-selectable tiles and retires a selected key after pan or mode change',async()=>{
 const h=await componentHarness('app/terrain-coverage-panel.tsx',{'./terrain-coverage':coverage,'./terrain-coverage-panel.module.css':{default:new Proxy({},{get:(_t,k)=>String(k)})}});
 try{const a=ground(1),b=ground(2,[-96.584,38.987,-96.580,38.991]);b.grid.source.acquisition='Second synthetic acquisition';let c=terrainCoverage(snapshot('ground',[a,b]),'ground'),props={coverage:c,navigating:false,preparing:false},ui=h.render(h.exports.TerrainCoveragePanel,props);
 let reveal;ui.props.onToggle({currentTarget:{open:true,querySelector:()=>({scrollIntoView:v=>{reveal=v;}})}});assert.equal(reveal.block,'start');assert.equal(reveal.behavior,'auto');const select=findNode(ui,n=>n.type==='select');assert.equal(select.props['aria-label'],'Inspect requested tile');assert.equal(select.props.children.length,2);select.props.onChange({target:{value:b.tile.key}});ui=h.render(h.exports.TerrainCoveragePanel,props);assert.match(text(ui),/Second synthetic acquisition/);assert.equal(findNode(ui,n=>n.type==='select').props.value,b.tile.key);assert.match(text(ui),/not show survey availability, area percentages or drawing completion/);assert.match(text(ui),/No extra downloads/);
 c=terrainCoverage(snapshot('ground',[a]),'ground');ui=h.render(h.exports.TerrainCoveragePanel,{...props,coverage:c,navigating:true});assert.equal(findNode(ui,n=>n.type==='select').props.value,a.tile.key);assert.doesNotMatch(text(ui),/Second synthetic acquisition/);assert.match(text(ui),/Last settled footprint/);
 const e=native('canopy');ui=h.render(h.exports.TerrainCoveragePanel,{...props,coverage:terrainCoverage(snapshot('canopy',[e]),'canopy'),preparing:true});assert.match(text(ui),/Canopy height/);assert.equal(findNode(ui,n=>n.type==='select').props.value,e.tile.key);assert.match(text(ui),/drawing is still preparing/);
 }finally{h.dispose();}
});
