import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import { PRIVATE_PROFILE_TEST_ONLY } from './private-profile-test-only.mjs';
const publicProfile = await import(`data:text/javascript;base64,${Buffer.from(ts.transpileModule(await readFile(new URL('../app/public-profile.ts', import.meta.url), 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString('base64')}`);

const ast = ts.createSourceFile('page.tsx', await readFile(process.env.KFM_PAGE_PATH ?? 'app/page.tsx', 'utf8'), ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
const callbacks = new Map();
function visit(node) {
  if (ts.isVariableDeclaration(node) && node.initializer) {
    const init = node.initializer;
    if (ts.isArrowFunction(init)) callbacks.set(node.name.getText(ast), init.getText(ast));
    else if (ts.isCallExpression(init) && init.expression.getText(ast) === 'useCallback') callbacks.set(node.name.getText(ast), init.arguments[0].getText(ast));
  }
  ts.forEachChild(node, visit);
}
visit(ast);
function execute(name, scope) {
  assert.ok(callbacks.has(name), `run the actual ${name} handler`);
  const code = ts.transpileModule(`return ${callbacks.get(name)};`, {compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
  return new Function(...Object.keys(scope), code)(...Object.values(scope));
}
function harness(workspace = 'reports') {
  const state = {primary:workspace, timeline:true, left:true, utility:false, draft:{title:'Preserved owner draft'}, snapshot:{id:'existing-snapshot'}};
  const timers = [], focus = [], calls = [];
  const scope = {
    // TEST-ONLY: retain the private utility focus/callback regression contract.
    IS_PUBLIC_COPY: PRIVATE_PROFILE_TEST_ONLY.IS_PUBLIC_COPY,
    primaryWorkspace:workspace, isCompact:true,
    setPrimaryWorkspace:v=>{state.primary=v;},
    setTimelineOpen:v=>{state.timeline=typeof v==='function'?v(state.timeline):v;},
    setLeftOpen:v=>{state.left=v;}, setLeftPanelMode:v=>{state.mode=v;},
    setMapUtilityOpen:v=>{state.utility=v;}, setMapUtilityView:v=>{state.view=v;},
    setMapUtilityFocusRequest:()=>{},
    setMapContextOpen:()=>{}, setCurrentWorkspace:()=>{}, setRightOpen:()=>{}, dismissMapUtilityWithoutFocus:()=>{},
    setScenePanelOpen:()=>{}, setLocalAtlasPeek:()=>{}, setHelpOpen:()=>{}, setSourceStatusOpen:()=>{},
    mapUtilityReturnRef:{current:null}, sourceSearchFocusPendingRef:{current:false},
    leftPanelReturnRef:{current:null}, leftPanelRef:{current:{}}, visibleFocusableElements:()=>[{focus:()=>focus.push(state.primary)}],
    window:{setTimeout(fn){timers.push(fn);}},
    openMapUtility:v=>{calls.push(v);state.primary='map';}, announce:()=>{},
  };
  return {state,scope,focus,calls,flush:()=>timers.splice(0).forEach(fn=>fn())};
}
test('Layers and Places reveal the map before deferred panel focus without replacing the draft or snapshot',()=>{
  for(const workspace of ['reports','stories']) for(const mode of ['layers','places']) {
    const h=harness(workspace), draft=h.state.draft, snapshot=h.state.snapshot;
    execute('openAtlasPanel',h.scope)(mode);
    assert.equal(h.state.primary,'map'); assert.equal(h.state.left,true); assert.equal(h.state.mode,mode);
    assert.deepEqual(h.focus,[]); h.flush(); assert.deepEqual(h.focus,['map']);
    assert.equal(h.state.draft,draft); assert.equal(h.state.snapshot,snapshot);
  }
});
test('source-search handoff keeps its dedicated search-focus effect',()=>{
  const h=harness();h.scope.sourceSearchFocusPendingRef.current=true;
  execute('openAtlasPanel',h.scope)('layers');h.flush();assert.equal(h.state.primary,'map');assert.deepEqual(h.focus,[]);
});
test('Time reopens a retained open panel from Reports or Stories, while Map still toggles',()=>{
  for(const workspace of ['reports','stories','map']) {
    const h=harness(workspace);execute('toggleTimelinePanel',h.scope)();
    assert.equal(h.state.primary,'map');assert.equal(h.state.timeline,workspace!=='map');
  }
});
test('map utilities and Compare reveal the map before opening the requested tool',()=>{
  const h=harness();execute('openMapUtility',h.scope)('navigate',null);
  assert.equal(h.state.primary,'map');assert.equal(h.state.utility,true);assert.equal(h.state.view,'scene');
  const compare=harness('stories');execute('activateMapRepresentation',compare.scope)('compare');
  assert.equal(compare.state.primary,'map');assert.deepEqual(compare.calls,['compare']);
});

test('map utility focus waits through its opening paint, suppresses draft focus and cancels stale frames',()=>{
  let effect,dependencies;
  function visit(node) {
    if(ts.isCallExpression(node) && node.expression.getText(ast)==='useEffect' && node.arguments[0]?.getText(ast).includes('const panel = mapUtilityPanelRef.current')) {effect=node.arguments[0].getText(ast);dependencies=node.arguments[1].elements.map(n=>n.getText(ast));}
    ts.forEachChild(node,visit);
  }
  visit(ast);assert.ok(effect);assert.ok(dependencies.includes('mapUtilityFocusRequest'),'same-view requests must rerun the committed focus effect');
  const code=ts.transpileModule(`return ${effect};`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
  for(const primaryWorkspace of ['reports','stories','map'])for(const mapUtilityOpen of [false,true])for(const cancelAt of ['commit','paint','after-focus']){
    const frames=[],focused=[],cancelled=new Set();let painted=false;
    const scope={primaryWorkspace,mapUtilityOpen,mapUtilityPanelRef:{current:{}},visibleFocusableElements:()=>[{focus:()=>{assert.equal(painted,true);focused.push(primaryWorkspace);}}],window:{requestAnimationFrame(fn){frames.push(fn);return frames.length;},cancelAnimationFrame(id){cancelled.add(id);}}};
    const cleanup=new Function(...Object.keys(scope),code)(...Object.values(scope))();
    assert.deepEqual(focused,[]);const active=primaryWorkspace==='map'&&mapUtilityOpen;
    assert.equal(frames.length,active?1:0);
    if(!active)continue;
    if(cancelAt==='commit'){cleanup();assert.deepEqual([...cancelled],[1]);continue;}
    frames[0]();assert.deepEqual(focused,[]);assert.equal(frames.length,2);
    if(cancelAt==='paint'){cleanup();assert.deepEqual([...cancelled],[1,2]);continue;}
    painted=true;frames[1]();assert.deepEqual(focused,['map']);cleanup();assert.deepEqual([...cancelled],[1,2]);
  }
});
test('each utility action requests focus even when the same tool is already open',()=>{
  const h=harness('map');let requests=0;h.scope.setMapUtilityFocusRequest=update=>{requests=update(requests);};
  const open=execute('openMapUtility',h.scope),trigger={};
  open('navigate',trigger);open('navigate',trigger);open('localAtlas',trigger);
  assert.equal(requests,3);assert.equal(h.state.primary,'map');assert.equal(h.state.utility,true);assert.equal(h.state.view,'localAtlas');assert.equal(h.scope.mapUtilityReturnRef.current,trigger);
});

test('the real public profile opens map navigation while withholding private utilities and their focus requests',()=>{
  const h=harness('reports');h.scope.IS_PUBLIC_COPY=publicProfile.IS_PUBLIC_COPY;
  let requests=0;h.scope.setMapUtilityFocusRequest=update=>{requests=update(requests);};
  const open=execute('openMapUtility',h.scope);
  for(const view of ['localAtlas','history','import'])open(view,{});
  assert.equal(h.state.primary,'reports');assert.equal(h.state.utility,false);assert.equal(requests,0);
  open('navigate',null);
  assert.equal(h.state.primary,'map');assert.equal(h.state.utility,true);assert.equal(h.state.view,'scene');assert.equal(requests,1);
});
