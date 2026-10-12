import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
const source=await readFile(process.env.KFM_UNDERGROUND_LOADER_PATH??'app/underground-panel-loader.tsx','utf8');
const ast=ts.createSourceFile('loader.tsx',source,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
let effect,onFocus,onBlur,dependencies;
function inspect(node){
  if(ts.isCallExpression(node)&&node.expression.getText(ast)==='useEffect'){effect=node.arguments[0].getText(ast);dependencies=node.arguments[1].elements.map(n=>n.getText(ast));}
  if(ts.isJsxAttribute(node)&&node.initializer&&ts.isJsxExpression(node.initializer)){
    if(node.name.getText(ast)==='onFocusCapture')onFocus=node.initializer.expression.getText(ast);
    if(node.name.getText(ast)==='onBlurCapture')onBlur=node.initializer.expression.getText(ast);
  }
  ts.forEachChild(node,inspect);
}
for(const node of ast.statements)if(ts.isFunctionDeclaration(node)&&node.name?.text==='UndergroundPanelLoader')inspect(node.body);
function compile(code,scope){assert.ok(code,'loader needs its committed focus/ownership callback');const js=ts.transpileModule(`return ${code};`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;return new Function(...Object.keys(scope),js)(...Object.values(scope));}
class FakeNode{}
function harness(ready=false,inert=false){
  const state={module:ready?{}:null,failed:false},enteredRef={current:false},loadingOwnsFocusRef={current:false},body=new FakeNode(),outside=new FakeNode(),calls=[];
  const doc={body,activeElement:outside,querySelector:selector=>selector.includes('Underground workspace')?loadedEntry:loadingEntry};
  const owned={loadingOwnsFocusRef,Node:FakeNode};
  const focus=compile(onFocus,owned),blur=compile(onBlur,owned);
  function entry(name){const node=new FakeNode();node.closest=selector=>{assert.equal(selector,'[inert]');return inert?{}:null;};node.focus=options=>{assert.equal(options.preventScroll,true);calls.push(name);doc.activeElement=node;if(name==='loading-close')focus();};return node;}
  const loadingEntry=entry('loading-close'),loadedEntry=entry('workspace-close');
  const scope={state,enteredRef,loadingOwnsFocusRef,document:doc,entryFocusRequest:0,lastEntryRequestRef:{current:0}};
  const run=()=>compile(effect,scope)();
  return {state,enteredRef,loadingOwnsFocusRef,body,outside,calls,doc,loadingEntry,loadedEntry,run,focus,blur,scope};
}
test('a cached Underground workspace enters its close control after mount',()=>{
  const h=harness(true);h.run();assert.deepEqual(h.calls,['workspace-close']);assert.equal(h.doc.activeElement,h.loadedEntry);
});
test('cold loading transfers owned focus after its control is replaced by the real workspace',()=>{
  const h=harness();h.run();assert.deepEqual(h.calls,['loading-close']);assert.equal(h.loadingOwnsFocusRef.current,true);
  // Removal of a focused loading control makes BODY active without blur.
  h.doc.activeElement=h.body;h.state.module={};h.run();
  assert.deepEqual(h.calls,['loading-close','workspace-close']);assert.equal(h.doc.activeElement,h.loadedEntry);
});
test('removing an owned retry control returns to loading controls before the module resolves',()=>{
  const h=harness();h.run();h.state.failed=true;h.run();assert.deepEqual(h.calls,['loading-close']);
  h.focus();h.doc.activeElement=h.body;h.state.failed=false;h.run();
  assert.deepEqual(h.calls,['loading-close','loading-close']);
  h.doc.activeElement=h.body;h.state.module={};h.run();assert.deepEqual(h.calls,['loading-close','loading-close','workspace-close']);
});
test('leaving loading clears ownership and never steals focus back, including from BODY',()=>{
  for(const bodyActive of [false,true]){
    const h=harness();h.run();h.blur({relatedTarget:h.outside,currentTarget:{contains:()=>false}});
    assert.equal(h.loadingOwnsFocusRef.current,false);h.doc.activeElement=bodyActive?h.body:h.outside;h.state.module={};h.run();assert.deepEqual(h.calls,['loading-close']);
  }
});
test('focus within the loading region stays owned, but a null outside blur clears it',()=>{
  const h=harness();h.run();h.blur({relatedTarget:h.loadingEntry,currentTarget:{contains:()=>true}});assert.equal(h.loadingOwnsFocusRef.current,true);
  h.blur({relatedTarget:null,currentTarget:{contains:()=>{throw Error('null is not a DOM Node');}}});assert.equal(h.loadingOwnsFocusRef.current,false);
});
test('a loader under an inert draft workspace does not autofocus behind it',()=>{
  for(const ready of [false,true]){const h=harness(ready,true);h.run();assert.deepEqual(h.calls,[]);}
});

test('an explicit request re-enters retained Underground controls without treating ordinary renders as requests',()=>{
  assert.ok(dependencies.includes('entryFocusRequest'));
  const h=harness(true);h.run();h.doc.activeElement=h.outside;h.run();assert.deepEqual(h.calls,['workspace-close']);
  h.scope.entryFocusRequest++;h.run();assert.deepEqual(h.calls,['workspace-close','workspace-close']);
});
