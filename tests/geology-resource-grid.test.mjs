import assert from 'node:assert/strict';
import test from 'node:test';
import {readFileSync} from 'node:fs';
import ts from 'typescript';

const source=readFileSync(new URL('../app/geology-resource-grid.ts',import.meta.url),'utf8');
const code=ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const {geologyResourceCells,layoutResourceGroups,resourceGroupRadius}=await import(`data:text/javascript;base64,${Buffer.from(code).toString('base64')}`);

test('statewide coverage uses six bounded stable count regions with no interior gaps',()=>{
 const cells=geologyResourceCells([-102.1,36.95,-94.55,40.05]);
 assert.equal(cells.length,6);
 for(const cell of cells){
  assert.ok(cell.bounds[2]-cell.bounds[0]<=3);
  assert.ok(cell.bounds[3]-cell.bounds[1]<=1.6);
  assert.ok(cell.coordinates[0]>=cell.bounds[0]&&cell.coordinates[0]<=cell.bounds[2]);
 }
 const totalArea=cells.reduce((sum,cell)=>sum+(cell.bounds[2]-cell.bounds[0])*(cell.bounds[3]-cell.bounds[1]),0);
 assert.ok(Math.abs(totalArea-7.55*3.1)<0.00001);
});

test('moderate view uses fixed one-degree cells and keeps IDs across a small pan',()=>{
 const a=geologyResourceCells([-100.5,38,-99.5,39]);
 const b=geologyResourceCells([-100.49,38.01,-99.49,39.01]);
 assert.ok(a.length>0&&a.length<=4);
 assert.ok(a.every(cell=>cell.id.startsWith('m:')));
 assert.ok(a.some(cell=>b.some(other=>other.id===cell.id&&other.bounds.join(',')===cell.bounds.join(','))));
});

test('oil and mine count marks stay separated by their radii and a readable gap at desktop and mobile edges',()=>{
 const region={id:'b:0:0',bounds:[-102.1,36.95,-99.583333,38.5]};
 const project=coordinates=>({x:coordinates[0],y:coordinates[1]});
 const unproject=point=>({lng:point.x,lat:point.y});
 for(const width of [1440,768,375])for(const anchor of [5,width/2,width-5]){
  const groups=[{...region,kind:'oilgas',count:49064,coordinates:[anchor,100]},{...region,kind:'minerals',count:795,coordinates:[anchor,100]}];
  const placed=layoutResourceGroups(groups,width,project,unproject);
  const left=placed[0].displayCoordinates[0],right=placed[1].displayCoordinates[0];
  const oilRadius=resourceGroupRadius(groups[0].count),mineRadius=resourceGroupRadius(groups[1].count);
  assert.ok(right-left>=oilRadius+mineRadius+9.99);
  assert.ok(left-oilRadius>=7.99);
  assert.ok(right+mineRadius<=width-7.99);
 }
});
