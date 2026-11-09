import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import ts from 'typescript';

const compile=s=>ts.transpileModule(s,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
function harness(search='?basemapTrace=1') {
  const health={};vm.runInNewContext(compile(readFileSync('app/basemap-health.ts','utf8')),{exports:health});
  const exports={},bindings=new Map(),dom=new Map(),navigation=new Map();
  const spec={type:'raster-dem',tiles:['https://example.invalid/private?token=secret']};
  const source={serialize:()=>spec};
  const window={location:{search},innerWidth:1440,innerHeight:900,addEventListener:(n,f)=>navigation.set(n,f),removeEventListener:n=>navigation.delete(n)};
  const document={hidden:false,addEventListener:(n,f)=>dom.set(n,f),removeEventListener:n=>dom.delete(n)};
  const map={on:(n,f)=>bindings.set(n,f),off:n=>bindings.delete(n),getSource:()=>source,getStyle:()=>({sources:{'basemap-relief-dem':spec,'private-token-secret':spec}})};
  vm.runInNewContext(compile(readFileSync('app/basemap-diagnostics.ts','utf8')),{exports,require:()=>health,window,document,URLSearchParams,performance:{now:()=>100}});
  return {window,document,map,bindings,dom,navigation,start:()=>exports.installBasemapDiagnostics(map,()=>({generation:1,basemap:'midnight'})),spec};
}
test('diagnostic opt-in is local, bounded, redacted, retains first failure and cleans every listener',()=>{
  const h=harness(),stop=h.start();
  const e={sourceId:'basemap-relief-dem',source:h.spec,tile:{state:'errored',tileID:{canonical:{z:6,x:14,y:24}}},error:{status:503,message:'private token secret'}};
  h.bindings.get('error')(e);
  for(let i=0;i<520;i++)h.bindings.get('sourcedata')({...e,tile:{...e.tile,state:'loaded'}});
  h.bindings.get('error')({...e,sourceId:'private-token-secret'});
  h.navigation.get('popstate')();h.dom.get('visibilitychange')();
  const trace=h.window.__kfmBasemapTrace.snapshot();
  assert.equal(trace.events.length,512);assert.ok(trace.droppedEvents>0);assert.equal(trace.firstFailure.status,503);
  assert.equal(trace.firstFailure.source,'basemap-relief-dem');assert.equal(trace.firstFailure.tile,1);
  assert.doesNotMatch(JSON.stringify(trace),/private|secret|example.invalid|canonical|"x"|"y"/);
  trace.firstFailure.viewport[0]=0;assert.equal(h.window.__kfmBasemapTrace.snapshot().firstFailure.viewport[0],1440);
  stop();assert.equal(h.bindings.size,0);assert.equal(h.dom.size,0);assert.equal(h.navigation.size,0);assert.equal(h.window.__kfmBasemapTrace,undefined);
});
test('no diagnostics listeners or exposed trace exist without explicit opt-in',()=>{
  const h=harness('');h.start()();assert.equal(h.bindings.size,0);assert.equal(h.dom.size,0);assert.equal(h.navigation.size,0);assert.equal(h.window.__kfmBasemapTrace,undefined);
});
test('diagnostic collection failures are counted without breaking the map event handler',()=>{
  const h=harness();h.start();h.map.getStyle=()=>{throw new Error('lost style');};
  assert.doesNotThrow(()=>h.bindings.get('error')({}));assert.equal(h.window.__kfmBasemapTrace.snapshot().collectorErrors,1);
});
