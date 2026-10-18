import test from 'node:test';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const require=createRequire(import.meta.url),braces=require('braces');
const blocked=fn=>assert.throws(fn,error=>error instanceof RangeError&&error.message==='braces nesting exceeds fixed depth limit (128)');
const nested=(n,open='{',close='}')=>open.repeat(n)+'x'+close.repeat(n);
test('the installed package is the inspected archive, without an invented upstream version',()=>{
 assert.equal(require('braces/package.json').version,'3.0.3');
 assert.equal(require('braces/package.json').kfmPatch,'depth-limit-128-v1');
 assert.equal(createHash('sha256').update(readFileSync(new URL('../vendor/braces-3.0.3-kfm.1.tgz',import.meta.url))).digest('hex'),'760bbcd249170e0d5f57195bb643d2b2228cd21e562fb32fca527cadcfc53643');
});
test('public and internal walkers bound brace, parenthesis, mixed and malformed patterns',()=>{
 for(const pattern of [nested(4400),nested(4400,'(',')'),nested(2200,'{(',')}'),'{'.repeat(200)+'x..y,z']) {
  for(const op of ['parse','compile','expand','stringify'])blocked(()=>braces[op](pattern));
  blocked(()=>braces(['ordinary',pattern]));
 }
 for(const op of ['compile','expand','stringify']) {
  const root={type:'root',nodes:[]};let current=root;
  for(let i=0;i<140;i++){const node={type:'paren',nodes:[],parent:current};current.nodes=[node];current=node;}
  current.nodes=[{type:'text',value:'x'}];
  blocked(()=>braces[op](root));blocked(()=>require('braces/lib/'+op)(root));
 }
});
test('cyclic child and parent paths terminate at the same non-configurable bound',()=>{
 for(const op of ['compile','expand','stringify']){
  const root={type:'root',nodes:[]};root.nodes=[root];blocked(()=>braces[op](root,{maxDepth:Infinity}));
 }
 const paren={type:'paren',nodes:[{type:'text',value:'x'}]};paren.parent=paren;
 blocked(()=>braces.expand({type:'root',nodes:[paren]}));
 blocked(()=>braces.expand(paren));
});
test('malformed AST array values cannot reach recursive coercion or expansion helpers',()=>{
 let value='x';for(let i=0;i<5000;i++)value=[value];
 for(const op of ['compile','expand','stringify']) {
  assert.throws(()=>braces[op]({type:'root',nodes:[{type:'text',value}]}),/AST values must be strings/);
 }
 blocked(()=>require('braces/lib/utils').flatten(value));
 const cycle=[];cycle.push(cycle);blocked(()=>require('braces/lib/utils').flatten(cycle));
});
test('ordinary glob semantics, literal delimiters and existing range limits remain',()=>{
 assert.deepEqual(braces.expand('map/{roads,water}/{2024..2026}'),['map/roads/2024','map/roads/2025','map/roads/2026','map/water/2024','map/water/2025','map/water/2026']);
 assert.deepEqual(braces.expand('{01..05..2}'),['01','03','05']);
 assert.deepEqual(braces.expand('{,a,a}',{noempty:true,nodupes:true}),['a']);
 for(const input of ['\\{'.repeat(1000),'"'+'{'.repeat(1000)+'"','['+'{'.repeat(1000)+']'])assert.doesNotThrow(()=>braces.compile(input));
 assert.equal(braces.stringify(braces.parse('foo/{a,{b,c}}')),'foo/{a,{b,c}}');
 assert.doesNotThrow(()=>braces.compile(nested(127)));blocked(()=>braces.compile(nested(128)));
 assert.throws(()=>braces.expand('{1..1001}'),/range limit/);
 assert.throws(()=>braces.parse('x'.repeat(10001)),/max characters/);
});
test('both build-tool fast-glob dependency paths use the bounded implementation',()=>{
 const globs=[require('fast-glob'),createRequire(require.resolve('vite-plugin-dynamic-import'))('fast-glob')];
 for(const glob of globs){
  blocked(()=>glob.generateTasks(nested(4400)));
  blocked(()=>glob.generateTasks('map/*.ts',{ignore:[nested(4400)]}));
  assert.ok(glob.generateTasks('map/{water,roads}/*.ts').length);
 }
});
