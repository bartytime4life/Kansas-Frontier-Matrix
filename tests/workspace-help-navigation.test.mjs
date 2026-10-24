import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
const ast=ts.createSourceFile('page.tsx',await readFile(process.env.KFM_PAGE_PATH??'app/page.tsx','utf8'),ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
const callbacks=new Map();let guideOpenExpression;
function visit(node){
  if(ts.isVariableDeclaration(node)&&node.initializer){
    const init=node.initializer;
    if(ts.isArrowFunction(init))callbacks.set(node.name.getText(ast),init.getText(ast));
    else if(ts.isCallExpression(init)&&init.expression.getText(ast)==='useCallback')callbacks.set(node.name.getText(ast),init.arguments[0].getText(ast));
  }
  if(ts.isJsxSelfClosingElement(node)&&node.tagName.getText(ast)==='ExplorerGuide')guideOpenExpression=node.attributes.properties.find(p=>p.name?.getText(ast)==='open').initializer.expression.getText(ast);
  ts.forEachChild(node,visit);
}
visit(ast);
function evaluate(code,scope){const js=ts.transpileModule(`return ${code};`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;return new Function(...Object.keys(scope),js)(...Object.values(scope));}
test('Quick start reveals the map and reopens retained help from either draft workspace',()=>{
  for(const primaryWorkspace of ['reports','stories','map'])for(const initial of [false,true]){
    const state={primary:primaryWorkspace,open:initial,sources:false},draft={title:'Keep this draft'},snapshot={id:'keep-this-snapshot'};
    const welcomeShowing=initial&&primaryWorkspace==='map';
    evaluate(callbacks.get('toggleExplorerGuide'),{primaryWorkspace,welcomeShowing,setPrimaryWorkspace:v=>state.primary=v,setGuideOpen:v=>state.open=typeof v==='function'?v(state.open):v,setWelcomeSourcesOpen:v=>state.sources=typeof v==='function'?v(state.sources):v,draft,snapshot})();
    assert.equal(state.primary,'map');assert.equal(state.open,true,'the guide opens, or stays open while it is showing');
    // While the welcome covers the map, `?` reveals the map sources instead of closing it.
    assert.equal(state.sources,welcomeShowing);
    assert.equal(draft.title,'Keep this draft');assert.equal(snapshot.id,'keep-this-snapshot');
  }
});
test('the retained guide stays unmounted and cannot autofocus in Reports or Stories',()=>{
  assert.ok(guideOpenExpression);
  for(const primaryWorkspace of ['reports','stories','map']){
    assert.equal(evaluate(guideOpenExpression,{primaryWorkspace,guideOpen:true}),primaryWorkspace==='map');
  }
});
test('source status reveals the map before frame focus and retains the supplied return target',()=>{
  const state={primary:'reports',guide:true,status:false},frames=[],focus=[],returnTarget={closest:()=>null},sourceStatusReturnRef={current:null};
  const scope={setPrimaryWorkspace:v=>state.primary=v,setGuideOpen:v=>state.guide=v,setSourceStatusOpen:v=>state.status=v,setLeftOpen:()=>{},leftPanelReturnRef:{current:null},setMapUtilityOpen:()=>{},setRightOpen:()=>{},setScenePanelOpen:()=>{},setLeftPanelMode:()=>{},sourceStatusReturnRef,sourceStatusPanelRef:{current:{querySelector:()=>({focus:()=>focus.push(state.primary)})}},window:{requestAnimationFrame:fn=>frames.push(fn)}};
  evaluate(callbacks.get('openSourceStatus'),scope)(returnTarget);
  assert.equal(state.primary,'map');assert.equal(state.guide,false);assert.equal(state.status,true);assert.equal(sourceStatusReturnRef.current,returnTarget);
  assert.deepEqual(focus,[]);frames[0]();assert.deepEqual(focus,['map']);
});

// Execute the actual guide click callback so dismissal's synchronous focus return
// is part of the regression, rather than calling the destination in isolation.
const guideAst=ts.createSourceFile('welcome.jsx',await readFile('app/living-welcome/welcome.jsx','utf8'),ts.ScriptTarget.ES2022,true,ts.ScriptKind.JSX);
let guideActionClick,helpOpenEffect;
function guideVisit(node){
  if(ts.isVariableDeclaration(node)&&node.name.getText(guideAst)==='run')guideActionClick=node.initializer.getText(guideAst);
  ts.forEachChild(node,guideVisit);
}
guideVisit(guideAst);
function effectVisit(node){
  if(ts.isCallExpression(node)&&node.expression.getText(ast)==='useEffect'&&node.arguments[0]?.getText(ast).includes('if (!helpOpen) return;'))helpOpenEffect=node.arguments[0].getText(ast);
  ts.forEachChild(node,effectVisit);
}
effectVisit(ast);
test('guide Layers and Time enter committed destinations after dismissal, even when the panel was retained',()=>{
  for(const action of ['layers','time'])for(const retained of [false,true]){
    const frames=[],focus=[],state={open:true,time:retained,status:true,starter:false},target={focus:()=>focus.push(action)};
    const leftPanelRef={current:retained?{}:null},timelineRef={current:retained?{}:null};
    const route=evaluate(callbacks.get('runExplorerGuideAction'),{
      openAtlasPanel:()=>{state.layers=true;},setPrimaryWorkspace:()=>{},setTimelineOpen:v=>state.time=v,
      setSourceStatusOpen:v=>state.status=v,setStarterPanelOpen:v=>state.starter=v,
      primaryWorkspace:'map',undergroundOpen:false,toggleUnderground:()=>{},openQwenCompanion:()=>{},
      window:{requestAnimationFrame:fn=>frames.push(fn)},leftPanelRef,timelineRef,
      visibleFocusableElements:panel=>{assert.equal(panel,action==='layers'?leftPanelRef.current:timelineRef.current);return [target];},
    });
    const close=evaluate(callbacks.get('closeExplorerGuide'),{
      setGuideOpen:v=>state.open=v,setWelcomeSourcesOpen:v=>state.sources=v,writeExplorerGuideDismissed:()=>{},
      document:{activeElement:{closest:()=>({})},querySelector:()=>({focus:()=>focus.push('guide-trigger')})},
    });
    assert.ok(guideActionClick,'the graphical welcome owns the action and dismissal callback');
    evaluate(guideActionClick,{onClose:close,remember:true})(()=>route(action));
    assert.equal(state.open,false);assert.deepEqual(focus,['guide-trigger']);
    assert.equal(frames.length,1,'focus must be scheduled after guide dismissal and panel commit');
    leftPanelRef.current={};timelineRef.current={};frames[0]();
    assert.deepEqual(focus,['guide-trigger',action]);
    assert.equal(action==='layers'?state.layers:state.time,true);
    if(action==='layers'){assert.equal(state.status,false);assert.equal(state.starter,true);}
  }
});
test('detailed map help takes focus after mount and returns it on close without stealing outside focus',()=>{
  assert.ok(helpOpenEffect,'map help needs a committed focus effect');
  for(const helpOpen of [false,true]){
    const focus=[],closeControl={focus:()=>focus.push('help-close')};
    evaluate(helpOpenEffect,{helpOpen,mapGuideRef:{current:{querySelector:selector=>{assert.equal(selector,'[aria-label="Close map guide"]');return closeControl;}}}})();
    assert.deepEqual(focus,helpOpen?['help-close']:[]);
  }
  for(const inside of [false,true]){
    const focus=[],state={open:true},active={};
    const close=evaluate(callbacks.get('closeMapGuide'),{
      setHelpOpen:v=>state.open=v,mapGuideRef:{current:{contains:node=>{assert.equal(node,active);return inside;}}},
      document:{activeElement:active,querySelector:()=>({focus:()=>focus.push('guide-trigger')})},
    });
    close();assert.equal(state.open,false);assert.deepEqual(focus,inside?['guide-trigger']:[]);
  }
});
test('Escape routes detailed help through its focus-restoring close action',()=>{
  let closed=0;
  evaluate(callbacks.get('handleEscape'),{
    repositoryOpen:false,workspaceDetailsRef:{current:{open:false}},sourceStatusOpen:false,qwenOpen:false,mapContextOpen:false,helpOpen:true,
    closeMapGuide:()=>closed++,
  })({key:'Escape'});
  assert.equal(closed,1);
});
test('Escape inside the Map menu does not close the underlying source-status view',()=>{
  let closed=0;
  evaluate(callbacks.get('handleEscape'),{
    repositoryOpen:false,workspaceDetailsRef:{current:{open:false}},sourceStatusOpen:true,
    closeSourceStatus:()=>closed++,
  })({key:'Escape',target:{closest:selector=>{assert.equal(selector,'.map-dock-map-menu');return {};}}});
  assert.equal(closed,0);
});

test('detailed-help Diagnostics waits through the opening paint and re-enters retained tools',()=>{
  for(const initiallyOpen of [false,true]){
    const frames=[],focus=[],state={view:'diagnostics',open:initiallyOpen,help:true},panel={};let painted=false;
    evaluate(callbacks.get('openMapGuideDiagnostics'),{
      openMapUtility:view=>{state.view=view;state.open=true;state.help=false;},
      window:{requestAnimationFrame:fn=>frames.push(fn)},mapUtilityPanelRef:{current:panel},
      visibleFocusableElements:target=>{assert.equal(target,panel);return [{focus:()=>{assert.equal(state.help,false);assert.equal(painted,true,'first animation frame can still be hidden');focus.push('diagnostics-close');}}];},
    })();
    assert.equal(state.help,false);assert.deepEqual(focus,[]);assert.equal(frames.length,1);
    frames[0]();assert.deepEqual(focus,[]);assert.equal(frames.length,2);
    painted=true;frames[1]();assert.deepEqual(focus,['diagnostics-close']);
  }
});
