import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

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
let headerChatClick;
function findHeaderChat(node) {
  if (ts.isJsxOpeningElement(node) && node.tagName.getText(ast) === 'button') {
    const attrs = node.attributes.properties;
    if (attrs.some(a => a.name?.getText(ast) === 'aria-label' && a.initializer?.text === 'Chat with KFM about this map view')) {
      headerChatClick = attrs.find(a => a.name?.getText(ast) === 'onClick').initializer.expression.getText(ast);
    }
  }
  ts.forEachChild(node, findHeaderChat);
}
findHeaderChat(ast);
function execute(name, scope) {
  assert.ok(callbacks.has(name), `run the actual ${name} handler`);
  const code = ts.transpileModule(`return ${callbacks.get(name)};`, {compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
  return new Function(...Object.keys(scope), code)(...Object.values(scope));
}

test('header Chat selects Ask after Find, retains the draft and keeps its explicit focus-return target',()=>{
  const trigger = {}, input = {value:'Ellsworth county'}, opened = [], closed = [];
  let draft = {id:7,value:'Ellsworth county',intent:'find'};
  const scope = {
    qwenOpen:false,globalSearchInputRef:{current:input},setPrimaryWorkspace(){},
    openQwenCompanion:(...args)=>opened.push(args),
    setAssistantDraftRequest:update=>{draft=update(draft);},
    closeQwenCompanion:target=>closed.push(target),
  };
  scope.openAtlasComposer=execute('openAtlasComposer',scope);
  assert.ok(headerChatClick);
  const click = () => new Function(...Object.keys(scope),ts.transpileModule(`return ${headerChatClick};`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText)(...Object.values(scope));
  click()({currentTarget:trigger});
  assert.deepEqual(draft,{id:8,value:'Ellsworth county',intent:'explore'});
  assert.deepEqual(opened,[[trigger,'composer']]);
  scope.qwenOpen=true;click()({currentTarget:trigger});
  assert.deepEqual(closed,[trigger]);assert.equal(draft.id,8,'closing the open panel does not rewrite its draft');
});

test('opening Find or a suggested question gives one focus owner to the composer',()=>{
  for(const isCompact of [false,true]) for(const intent of ['find','explore']) {
    const timers=[],frames=[],focused=[],changes=[],trigger={kind:'trigger'},input={value:'Retained draft',focus:()=>focused.push('composer')};
    const scope={
      isCompact,HTMLElement:class {},document:{activeElement:trigger},qwenReturnRef:{current:null},
      globalSearchInputRef:{current:input},qwenPanelRef:{current:{querySelector:()=>({focus:()=>focused.push('close')})}},
      setQwenOpen:value=>changes.push(['open',value]),setHelpOpen:()=>{},dismissMapUtilityWithoutFocus:()=>{},
      setGuideOpen:value=>changes.push(['guide',value]),setWelcomeSourcesOpen:value=>changes.push(['sources',value]),
      setLeftOpen:()=>{},setRightOpen:()=>{},setTimelineOpen:()=>{},setPrimaryWorkspace:value=>changes.push(['workspace',value]),
      setAssistantDraftRequest:update=>changes.push(['draft',update({id:4,value:'Old request'})]),
      window:{setTimeout:fn=>timers.push(fn),requestAnimationFrame:fn=>frames.push(fn)},
    };
    scope.openQwenCompanion=execute('openQwenCompanion',scope);
    execute('openAtlasComposer',scope)(intent,intent==='explore'?'Explain this county':undefined);
    assert.deepEqual(focused,[],'focus is deferred until the opening render commits');
    // Both scheduling queues are drained: a later close-button callback must
    // never steal focus after the composer has accepted a visitor's first key.
    frames.forEach(fn=>fn());timers.forEach(fn=>fn());
    assert.deepEqual(focused,['composer']);
    assert.ok(changes.some(([name,value])=>name==='open'&&value===true));
    assert.ok(changes.some(([name,value])=>name==='guide'&&value===false));
    assert.deepEqual(changes.find(([name])=>name==='draft')[1],{id:5,value:intent==='find'?'Retained draft':'Explain this county',intent});
    focused.length=0;timers.length=0;frames.length=0;
    scope.openQwenCompanion(trigger);timers.forEach(fn=>fn());
    assert.deepEqual(focused,['close'],'other chat launchers retain their close-control focus destination');
    assert.equal(scope.qwenReturnRef.current,trigger,'the caller remains the return-focus target');
  }
});

test('phone drawing controls reveal the map and defer its focus without changing desktop panels',()=>{
  const actions=new Map();
  function collect(node){
    if(ts.isJsxOpeningElement(node)&&node.tagName.getText(ast)==='button'){
      const attrs=node.attributes.properties;
      const label=attrs.find(a=>a.name?.getText(ast)==='aria-label')?.initializer?.text;
      if(['Point','Line','Polygon'].includes(label)) actions.set(label,attrs.find(a=>a.name?.getText(ast)==='onClick').initializer.expression.getText(ast));
    }
    ts.forEachChild(node,collect);
  }
  collect(ast);
  for(const isCompact of [false,true])for(const [label,mode] of [['Point','point'],['Line','distance'],['Polygon','area']]){
    const calls=[],frames=[];
    const beginMapMeasurement=execute('beginMapMeasurement',{
      isCompact,toggleMeasure:value=>calls.push(['measure',value]),
      dismissMapUtilityWithoutFocus:()=>calls.push(['dismiss']),
      window:{requestAnimationFrame:fn=>frames.push(fn)},
      mapContainerRef:{current:{focus:options=>calls.push(['focus',options])}},
    });
    assert.ok(actions.has(label));
    const code=ts.transpileModule(`return ${actions.get(label)};`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
    new Function('beginMapMeasurement',code)(beginMapMeasurement)();
    assert.deepEqual(calls,isCompact?[['measure',mode],['dismiss']]:[['measure',mode]]);
    assert.equal(frames.length,isCompact?1:0);
    frames.forEach(fn=>fn());
    if(isCompact)assert.deepEqual(calls.at(-1),['focus',{preventScroll:true}]);
  }
});
function harness(workspace = 'reports') {
  const state = {primary:workspace, timeline:true, left:true, utility:false, draft:{title:'Preserved owner draft'}, snapshot:{id:'existing-snapshot'}};
  const timers = [], focus = [], calls = [];
  const scope = {
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
test('a base view chosen from Map closes Underground and Compare without replacing retained drafts',()=>{
  for(const mode of ['2d','terrain','globe']) for(const utility of ['compare','navigate']) {
    const h=harness('map');let underground=true; const choices=[];
    Object.assign(h.scope,{mapUtilityView:utility,setUndergroundOpen:v=>underground=v,activateMapRepresentation:v=>choices.push(v)});
    h.state.utility=true;const draft=h.state.draft;
    execute('chooseMapMenuRepresentation',h.scope)(mode);
    assert.equal(underground,false);assert.equal(h.state.utility,utility!=='compare');assert.deepEqual(choices,[mode]);assert.equal(h.state.draft,draft);
  }
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
  open('navigate',trigger);open('navigate',trigger);open('connections',trigger);
  assert.equal(requests,3);assert.equal(h.state.primary,'map');assert.equal(h.state.utility,true);assert.equal(h.state.view,'connections');assert.equal(h.scope.mapUtilityReturnRef.current,trigger);
});

// The actual source-status handler owns a view inside Layers, not a floating PC workbench.
test('source status opens Layers from retained workspaces and defers focus without discarding drafts',()=>{
  for(const workspace of ['map','reports','stories']) {
    const h=harness(workspace), trigger={closest:()=>null}, focused=[];
    Object.assign(h.scope,{
      setGuideOpen:()=>{}, setSourceStatusOpen:v=>{h.state.sources=v;},
      sourceStatusReturnRef:{current:null}, mapContainerRef:{current:{}},
      document:{activeElement:null}, HTMLElement:class {},
      sourceStatusPanelRef:{current:{querySelector:()=>({focus:()=>focused.push(h.state.primary)})}},
    });
    h.scope.window.requestAnimationFrame=fn=>{h.scope.window.setTimeout(fn);return 1;};
    const draft=h.state.draft, snapshot=h.state.snapshot;
    execute('openSourceStatus',h.scope)(trigger);
    assert.equal(h.state.primary,'map');assert.equal(h.state.left,true);
    assert.equal(h.state.mode,'layers');assert.equal(h.state.sources,true);assert.equal(h.state.utility,false);
    assert.equal(h.scope.leftPanelReturnRef.current,trigger);assert.deepEqual(focused,[]);
    h.flush();assert.deepEqual(focused,['map']);
    assert.equal(h.state.draft,draft);assert.equal(h.state.snapshot,snapshot);
  }
});

test('opening source details from a layer keeps the outer Layers return target',()=>{
  const h=harness('map'), outer={id:'layers-trigger'}, inner={closest:()=>({})};
  Object.assign(h.scope,{setGuideOpen:()=>{},setSourceStatusOpen:()=>{},sourceStatusReturnRef:{current:null},sourceStatusPanelRef:{current:null},mapContainerRef:{current:{}},document:{activeElement:null},HTMLElement:class {}});
  h.scope.leftPanelReturnRef.current=outer;h.scope.window.requestAnimationFrame=()=>1;
  execute('openSourceStatus',h.scope)(inner);
  assert.equal(h.scope.leftPanelReturnRef.current,outer);
  assert.equal(h.scope.sourceStatusReturnRef.current,inner);
});
