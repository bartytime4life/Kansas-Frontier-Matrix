import assert from 'node:assert/strict';
import { test, after } from 'node:test';
import { mkdtempSync, rmSync, readFileSync, writeFileSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, resolve, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
import { spawnSync } from 'node:child_process';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '../../..');
const require = createRequire(import.meta.url);
const app = join(root, 'apps/kansas-frontier-matrix-explorer');
// NODE_PATH may resolve an ambient global compiler. Resolution alone is not a lock check.
let compiler;
let compilerVersion;
let compilerMode = 'DECLARED_VERSION_MATCH';
try {
  const manifest = JSON.parse(readFileSync(join(app, 'package.json'), 'utf8'));
  const lock = JSON.parse(readFileSync(join(app, 'package-lock.json'), 'utf8'));
  const expected = manifest.devDependencies?.typescript;
  if (!/^\d+\.\d+\.\d+$/.test(expected ?? '')
      || lock.packages?.['node_modules/typescript']?.version !== expected) {
    throw new Error('TypeScript declaration and app lock do not agree');
  }
  for (const directory of [app, root]) {
    const candidate = join(directory, 'node_modules/typescript/bin/tsc');
    if (!existsSync(candidate)) continue;
    const installed = JSON.parse(readFileSync(join(directory, 'node_modules/typescript/package.json'), 'utf8'));
    if (installed.version === expected) { compiler = candidate; compilerVersion = installed.version; break; }
  }
} catch { /* No implicit ambient/global fallback. */ }
if (!compiler) {
  if (process.env.KFM_ALLOW_GLOBAL_TSC !== '1') {
    throw new Error('Declared TypeScript unavailable or app lock mismatch. Install the repository lock; an ambient diagnostic requires KFM_ALLOW_GLOBAL_TSC=1.');
  }
  compiler = require.resolve('typescript/bin/tsc');
  compilerVersion = require('typescript/package.json').version;
  compilerMode = 'AMBIENT_DIAGNOSTIC_NOT_LOCK_NATIVE';
}
console.log(JSON.stringify({ compilerMode, compilerVersion, compiler,
  installedByteIntegrity: 'NOT_VERIFIED_BY_THIS_TEST' }));
const output = mkdtempSync(join(tmpdir(), 'kfm-library-unit-'));
after(()=>rmSync(output,{recursive:true,force:true}));
writeFileSync(join(output, 'package.json'), '{"type":"module"}');
const files = [
  'packages/ui/src/layer-library-model.ts', 'packages/ui/src/layer-library-view.ts',
  'apps/kansas-frontier-matrix-explorer/app/site-layer-library-metadata.ts',
];
const args = ['--target','ES2022','--module','ES2022','--moduleResolution','bundler','--strict',
  '--lib','ES2022,DOM,DOM.Iterable','--rootDir',root,'--outDir',output,...files.map(x=>join(root,x))];
const build = spawnSync(process.execPath,[compiler,...args],{encoding:'utf8'});
assert.equal(build.status,0,build.stdout+build.stderr);
const M = await import(pathToFileURL(join(output, 'packages/ui/src/layer-library-model.js')).href);
const S = await import(pathToFileURL(join(output, 'apps/kansas-frontier-matrix-explorer/app/site-layer-library-metadata.js')).href);
const card = (id='a', more={}) => ({
  id, title:`Fixture ${id}`, description:'No real observations', provider:'Synthetic test provider', domain:'Hydrology',
  disclosure:'allow', access:'allow', rights:'cleared', sensitivity:'public', release:'unreleased',
  fixture:true, workspaceAction:'preview', runtime:'held', renderGroup:'fixture-pass',
  representation:'GeoJSON', areaMatch:true, timeMatch:true, ...more,
});
const catalog = (...items) => M.projectCatalog(items.length?items:[card('a'),card('b')]);
const ws = (...ids) => ids.map(id=>({id,visible:true,opacity:1}));
const filter = (more={}) => ({...M.EMPTY_FILTERS,mode:'fixtures',...more});

test('projection suppresses denied and unknown disclosure without reading protected fields',()=>{
  const denied={disclosure:'deny',get title(){throw Error('leak')},get id(){throw Error('leak')}};
  assert.deepEqual(M.projectCatalog([denied,{disclosure:'unknown'}]),[]);
});
test('projection strips geometry, tokens, URLs, prompts and unknown object fields',()=>{
  const input=card('a',{token:'secret',url:'https://bad.invalid',prompt:'private'});
  Object.defineProperty(input,'data',{get(){throw Error('geometry read')}});
  const [safe]=catalog(input);
  for(const key of ['token','url','data','prompt']) assert.equal(key in safe,false);
  assert.equal(Object.isFrozen(safe),true);
});
test('duplicates are suppressed rather than silently picking a conflicting ID',()=>{
  assert.deepEqual(catalog(card('a'),card('a',{title:'Conflict'})),[]);
});
test('reserved property names and malformed identifiers cannot become keys',()=>{
  for(const id of ['__proto__','constructor','prototype','a\" onclick=1','']) assert.equal(M.validId(id),false);
  assert.equal(catalog(card('__proto__')).length,0);
});
test('unknown access, rights and sensitivity fail closed independently',()=>{
  for(const values of [{access:'unknown'},{rights:'unknown'},{sensitivity:'unknown'}]) {
    assert.equal(M.availability(catalog(card('a',values))[0]),'unavailable');
  }
});
test('fixture and released status cannot collapse into operational eligibility',()=>{
  const [c]=catalog(card('a',{release:'released',workspaceAction:'add'}));
  assert.equal(M.availability(c),'unavailable');
});
test('operational projection needs separate release, version and evidence inputs',()=>{
  const released=card('r',{fixture:false,release:'released',workspaceAction:'add',datasetVersion:'v1',artifactVersion:'artifact1',evidenceRef:'ref1'});
  assert.equal(M.availability(catalog(released)[0]),'eligible');
  for(const field of ['datasetVersion','artifactVersion','evidenceRef']) assert.equal(M.availability(catalog({...released,[field]:''})[0]),'unavailable');
});
test('default search exposes eligible releases, not fixture previews',()=>{
  assert.equal(M.selectCards(catalog(),M.EMPTY_FILTERS).total,0);
});
test('text, provider, domain and representation filters compose',()=>{
  const c=catalog(card('a'),card('b',{provider:'Other',domain:'Soil'}));
  assert.equal(M.selectCards(c,filter({query:'FIXTURE A',provider:'Synthetic test provider',domain:'Hydrology',representation:'GeoJSON'})).total,1);
});
test('unknown coverage differs from no coverage and neither passes positive filter',()=>{
  const c=catalog(card('a',{areaMatch:null}),card('b',{areaMatch:false}),card('c'));
  assert.equal(c[0].areaMatch,null); assert.equal(c[1].areaMatch,false);
  assert.deepEqual(M.selectCards(c,filter({areaOnly:true})).cards.map(x=>x.id),['c']);
});
test('missing temporal support is not interpolated by filtering',()=>{
  const c=catalog(card('a',{timeMatch:null}),card('b',{timeMatch:false}),card('c'));
  assert.deepEqual(M.selectCards(c,filter({timeOnly:true})).cards.map(x=>x.id),['c']);
});
test('pagination bounds rows, handles filter shrink and invalid page numbers',()=>{
  const c=M.projectCatalog(Array.from({length:71},(_,i)=>card(`f${i}`)));
  assert.equal(M.selectCards(c,filter(),0).cards.length,24);
  assert.equal(M.selectCards(c,filter(),999).page,2);
  assert.equal(M.selectCards(c,filter(),NaN).page,0);
  assert.equal(M.selectCards(c,filter({query:'nonexistent'}),999).page,0);
});
test('catalog cap rejects rather than silently truncating metadata',()=>{
  assert.throws(()=>M.projectCatalog(Array(M.MAX_CATALOG_CARDS+1).fill(card())),RangeError);
});
test('staging is pure and does not alter the workspace or camera',()=>{
  const state={camera:{center:[-98,38],zoom:5},layers:ws('a')}; const before=structuredClone(state);
  assert.deepEqual(M.stagePlan(['b'],state.layers,catalog()).accepted,['b']); assert.deepEqual(state,before);
});
test('duplicate addition is idempotent and explains already-present selections',()=>{
  const result=M.addStaged(['a','a','b'],ws('a'),catalog());
  assert.deepEqual(result.next.map(x=>x.id),['a','b']); assert.match(result.notice,/1 already present/);
});
test('withdrawal between staging and commit excludes without leaking its identifier',()=>{
  const c=catalog(card('a'),card('secret',{release:'withdrawn'}));
  const result=M.addStaged(['secret'],[],c);
  assert.deepEqual(result.next,[]); assert.equal(result.rejected,1); assert.equal(result.notice.includes('secret'),false);
});
test('changed access between selection and commit is rechecked',()=>{
  const result=M.addStaged(['a'],[],catalog(card('a',{access:'deny'})));
  assert.equal(result.rejected,1); assert.deepEqual(result.next,[]);
});
test('selection and workspace size limits are explicit',()=>{
  assert.throws(()=>M.addStaged(Array(101).fill('a'),[],catalog()),RangeError);
  const c=M.projectCatalog(Array.from({length:101},(_,i)=>card(`f${i}`)));
  const result=M.addStaged(['f100'],ws(...c.slice(0,100).map(x=>x.id)),c);
  assert.equal(result.next.length,100); assert.equal(result.rejected,1);
});
test('visibility and opacity edits preserve identity, order and hidden membership',()=>{
  const result=M.editWorkspace(ws('a','b'),catalog(),{kind:'visible',id:'a',value:false});
  assert.equal(result.next[0].visible,false); assert.equal(result.next.length,2);
  const alpha=M.editWorkspace(result.next,catalog(),{kind:'opacity',id:'a',value:.35});
  assert.equal(alpha.next[0].opacity,.35); assert.equal(alpha.next[0].visible,false);
});
test('invalid opacity never succeeds',()=>{
  for(const value of [NaN,Infinity,-1,2]) assert.equal(M.editWorkspace(ws('a'),catalog(),{kind:'opacity',id:'a',value}).rejected,1);
});
test('same declared renderer group permits adjacent keyboard/pointer moves',()=>{
  assert.deepEqual(M.editWorkspace(ws('a','b'),catalog(),{kind:'move',id:'a',direction:1}).next.map(x=>x.id),['b','a']);
});
test('unknown or different renderer groups deny impossible moves',()=>{
  for(const group of [null,'other']) {
    const result=M.editWorkspace(ws('a','b'),catalog(card('a'),card('b',{renderGroup:group})),{kind:'move',id:'a',direction:1});
    assert.equal(result.rejected,1); assert.deepEqual(result.next.map(x=>x.id),['a','b']);
  }
});
test('out-of-range and invalid move directions are rejected',()=>{
  for(const direction of [-1,0,2]) assert.equal(M.editWorkspace(ws('a','b'),catalog(),{kind:'move',id:'a',direction}).rejected,1);
});
test('undo returns prior selection without camera fields',()=>{
  const added=M.addStaged(['b'],ws('a'),catalog());
  const restored=M.undoEdit(added.undo,added.next,catalog()); assert.deepEqual(restored.next,ws('a'));
  assert.equal('camera' in restored,false);
});
test('undo conflicts preserve later user edits',()=>{
  const added=M.addStaged(['b'],ws('a'),catalog());
  const changed=M.editWorkspace(added.next,catalog(),{kind:'opacity',id:'b',value:.5});
  const restored=M.undoEdit(added.undo,changed.next,catalog());
  assert.equal(restored.rejected,1); assert.deepEqual(restored.next,changed.next);
});
test('undo cannot resurrect revoked metadata or a withdrawn layer',()=>{
  const removed=M.editWorkspace(ws('a','b'),catalog(),{kind:'remove',id:'a'});
  const withdrawn=catalog(card('a',{release:'withdrawn'}),card('b'));
  assert.deepEqual(M.undoEdit(removed.undo,removed.next,withdrawn).next,ws('b'));
});
test('checked held layers say not drawn, not loading success',()=>{
  assert.equal(M.nonvisibility(catalog()[0],ws('a')[0]),'Renderer held — not drawn');
});
test('runtime, access, release and nonvisibility are separate axes',()=>{
  assert.equal(M.nonvisibility(catalog(card('a',{runtime:'loading'}))[0],ws('a')[0]),'Loading');
  assert.equal(M.nonvisibility(catalog(card('a',{runtime:'error'}))[0],ws('a')[0]),'Delivery failed');
  assert.equal(M.nonvisibility(catalog()[0],{id:'a',visible:false,opacity:1}),'Disabled');
});
test('normalization rechecks eligibility and never retains unknown references',()=>{
  assert.deepEqual(M.normalizeWorkspace(ws('unknown','a','a'),catalog()),ws('a'));
});
const metadata=(more={})=>({id:'water-context',publicStatus:'GENERALIZED',releaseState:'DEMONSTRATION',title:'Test water',description:'Fixture',domain:'Hydrology',sourceId:'kfm-water',sourceType:'GeoJSON',geometryType:'LineString',bounds:[-102,37,-94,40],validTimeExtent:'2026',sourceTime:'Test',releaseTime:'Demo',attribution:'KFM',evidenceReference:'Per-feature',sensitivityNote:'Not measured',correctionNote:'None',units:'none',...more});
test('site projection never reads geometry or per-feature properties',()=>{
  const source=metadata();
  Object.defineProperties(source,{data:{get(){throw Error('geometry fetch')}},renderers:{get(){throw Error('renderer read')}}});
  assert.equal(S.projectSiteDemoCards([source],null,()=>true).length,1);
});
test('site projection suppresses restricted metadata before inspecting titles',()=>{
  const source=metadata({publicStatus:'RESTRICTED'});
  Object.defineProperty(source,'title',{get(){throw Error('leak')}});
  assert.deepEqual(S.projectSiteDemoCards([source],null,()=>{throw Error('time leak')}),[]);
});
test('site projection excludes unlisted IDs and future production release claims',()=>{
  assert.deepEqual(S.projectSiteDemoCards([metadata({id:'unreviewed-new-source'})],null,()=>true),[]);
  assert.deepEqual(S.projectSiteDemoCards([metadata({releaseState:'RELEASED'})],null,()=>true),[]);
});
test('site projection preserves unknown versions and independently labels fixture/generalization',()=>{
  const [c]=S.projectSiteDemoCards([metadata()],null,()=>null);
  assert.equal(c.datasetVersion,''); assert.equal(c.artifactVersion,''); assert.equal(c.fixture,true);
  assert.equal(c.generalized,true); assert.equal(c.release,'unreleased'); assert.equal(c.timeMatch,null);
});
test('bbox coverage is inclusive, bounded and explicitly unknown for unsupported cases',()=>{
  const area={west:-100,south:38,east:-98,north:39};
  assert.equal(S.boundingBoxMatch([-102,37,-100,38],area),true);
  assert.equal(S.boundingBoxMatch([-110,37,-105,38],area),false);
  for(const bounds of [[170,-1,-170,1],[NaN,0,1,1],[-200,0,1,1],[0,10,1,5]]) assert.equal(S.boundingBoxMatch(bounds,area),null);
  assert.equal(S.boundingBoxMatch([-102,37,-94,40],null),null);
});
test('site time is delegated to the existing host adapter, not a new time subsystem',()=>{
  let calls=0; const source=metadata(); const [c]=S.projectSiteDemoCards([source],null,layer=>{calls++; assert.equal(layer,source); return false});
  assert.equal(c.timeMatch,false); assert.equal(calls,1);
});
test('shared UI source has no network, HTML parser, model or map acquisition',()=>{
  for(const file of files.slice(0,2)) {
    const s=readFileSync(join(root,file),'utf8');
    assert.doesNotMatch(s,/\bfetch\s*\(|XMLHttpRequest|innerHTML|insertAdjacentHTML|eval\s*\(|new\s+Function|navigator\.geolocation|localStorage|maplibre-gl/);
  }
});

// Newly added layers inherit the host's existing preference or metadata default.
test('addition preserves opacity defaults and leaves existing layer preferences unchanged',()=>{
  const c=catalog(card('a',{defaultOpacity:.25}),card('b',{defaultOpacity:.5}));
  const current=[{id:'a',visible:false,opacity:.33}];
  const next=M.addStaged(['a','b'],current,c).next;
  assert.equal(next[0].opacity,.33); assert.equal(next[0].visible,false);
  assert.equal(next[1].opacity,.5);
  assert.equal(M.addStaged(['a'],[],c).next[0].opacity,.25);
});


test('confirmed writes require matching readback, not a truthy return',()=>{
  for (const response of [undefined, null, 1, "true", true]) {
    let calls=0; const port={read:()=>ws('a'),write:()=>{calls++;return response;}};
    const result=M.confirmWorkspaceWrite(port,ws('a','b'),ws('a'));
    assert.equal(result.outcome,'UNCONFIRMED'); assert.equal(calls,1);
  }
});
test('compare-and-set checks the current port before sending a write',()=>{
  let calls=0;const port={read:()=>ws('b'),write:()=>{calls++;return true;}};
  assert.equal(M.confirmWorkspaceWrite(port,ws('a','b'),ws('a')).outcome,'CONFLICT');
  assert.equal(calls,0);
});
test('explicit rejection is not an applied change',()=>{
  let calls=0;const port={read:()=>ws('a'),write:()=>{calls++;return false;}};
  assert.equal(M.confirmWorkspaceWrite(port,ws('a','b'),ws('a')).outcome,'CONFLICT');
  assert.equal(calls,1);
});
test('successful synchronous write has exactly one write and two reads',()=>{
  let state=ws('a'),writes=0,reads=0;
  const port={read:()=>{reads++;return state;},write:(next,expected)=>{
    writes++;assert.deepEqual(expected,ws('a'));state=next;return true;
  }};
  assert.equal(M.confirmWorkspaceWrite(port,ws('a','b'),ws('a')).outcome,'APPLIED');
  assert.equal(writes,1);assert.equal(reads,2);assert.deepEqual(state,ws('a','b'));
});
test('already matching intent makes no redundant write',()=>{
  let calls=0;const port={read:()=>ws('a'),write:()=>{calls++;return true;}};
  assert.equal(M.confirmWorkspaceWrite(port,ws('a'),ws('a')).outcome,'APPLIED');assert.equal(calls,0);
});
test('write exceptions never disclose error payloads or retry',()=>{
  let calls=0;const port={read:()=>ws('a'),write:()=>{calls++;throw Error('SECRET_CREDENTIAL');}};
  const result=M.confirmWorkspaceWrite(port,ws('a','b'),ws('a'));
  assert.equal(result.outcome,'ERROR');assert.equal(JSON.stringify(result).includes('SECRET_CREDENTIAL'),false);
  assert.equal(calls,1);
});
test('mutation followed by failure is not falsely described as no change',()=>{
  let state=ws('a'),calls=0;const port={read:()=>state,write:next=>{
    calls++;state=next;throw Error('failure after mutation');
  }};
  const result=M.confirmWorkspaceWrite(port,ws('a','b'),ws('a'));
  assert.equal(result.outcome,'ERROR');assert.deepEqual(state,ws('a','b'));assert.equal(calls,1);
  assert.doesNotMatch(result.notice,/no change|nothing changed|restored/i);
});
test('readback failures and mismatches never retry or compensate',()=>{
  for (const mode of ['throw','mismatch']) {
    let state=ws('a'),writes=0;
    const port={read:()=>{if(writes&&mode==='throw')throw Error('SECRET_READ');return state;},
      write:()=>{writes++;state=ws('b');return true;}};
    const result=M.confirmWorkspaceWrite(port,ws('a','b'),ws('a'));
    assert.equal(result.outcome,mode==='throw'?'ERROR':'UNCONFIRMED');assert.equal(writes,1);
    assert.equal(JSON.stringify(result).includes('SECRET_READ'),false);
  }
});
test('write inputs are detached immutable value snapshots',()=>{
  const original=ws('a','b');let state=ws('a');let written;
  const port={read:()=>state,write:(next)=>{
    written=next;original[1].opacity=.2;state=next;return true;
  }};
  assert.equal(M.confirmWorkspaceWrite(port,original,ws('a')).outcome,'APPLIED');
  assert.notEqual(written,original);assert.equal(written[1].opacity,1);
  assert.equal(Object.isFrozen(written),true);assert.equal(Object.isFrozen(written[0]),true);
});
test('malformed and oversized host state sends no write',()=>{
  for(const value of [null,{},Array(101).fill(ws('a')[0]),ws('a','a'),[{id:'a',visible:true,opacity:NaN}]] ){
    let writes=0;const port={read:()=>value,write:()=>{writes++;return true;}};
    assert.equal(M.confirmWorkspaceWrite(port,ws('a','b'),ws('a')).outcome,'ERROR');assert.equal(writes,0);
  }
});
