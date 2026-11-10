import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

const compile=source=>ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const policy=await import('data:text/javascript;base64,'+Buffer.from(compile(await readFile('app/compact-panels.ts','utf8'))).toString('base64'));
const ids=['tools','chat','evidence','left','time'];
const all=Object.fromEntries(ids.map(id=>[id,true]));
test('the focused open work area wins over competing compact surfaces',()=>{
 for(const id of ids)assert.equal(policy.compactPanelOwner(all,id,false),id);
 assert.equal(policy.compactPanelOwner({...all,left:false},'left',false),'tools','a closed surface cannot become the owner');
});
test('fallback stacking is deterministic and another workspace or dialog blocks background ownership',()=>{
 assert.equal(policy.compactPanelOwner(all,null,false),'tools');
 assert.equal(policy.compactPanelOwner({...all,tools:false},null,false),'chat');
 assert.equal(policy.compactPanelOwner({...all,tools:false,chat:false},null,false),'evidence');
 assert.equal(policy.compactPanelOwner({...all,tools:false,chat:false,evidence:false},null,false),'left');
 assert.equal(policy.compactPanelOwner({tools:false,chat:false,evidence:false,left:false,time:true},null,false),'time');
 assert.equal(policy.compactPanelOwner(Object.fromEntries(ids.map(id=>[id,false])),null,false),null);
 assert.equal(policy.compactPanelOwner(all,'left',true),null);
});

const source=await readFile('app/page.tsx','utf8'),ast=ts.createSourceFile('page.tsx',source,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
let resizeEffect,focusEffect,chatActivity,closeChat;
function visit(node){
 if(ts.isCallExpression(node)&&node.expression.getText(ast)==='useEffect'){
  const body=node.arguments[0]?.getText(ast)??'';
  if(body.includes('const media = window.matchMedia("(max-width: 1100px)")'))resizeEffect=body;
  if(body.includes('const returningToScene'))focusEffect=body;
 }
 if(ts.isVariableDeclaration(node)&&node.name.getText(ast)==='closeQwenCompanion')closeChat=node.initializer.arguments[0].getText(ast);
 if((ts.isJsxSelfClosingElement(node)||ts.isJsxOpeningElement(node))&&node.tagName.getText(ast)==='AssistantWorkspace')chatActivity=node.attributes.properties.find(item=>ts.isJsxAttribute(item)&&item.name.getText(ast)==='active').initializer.expression.getText(ast);
 ts.forEachChild(node,visit);
}visit(ast);assert.ok(resizeEffect);assert.ok(focusEffect);
function execute(effect,scope){return new Function(...Object.keys(scope),compile(`return ${effect};`))(...Object.values(scope))();}
class Node{
 constructor(parentElement=null){this.parentElement=parentElement;this.isConnected=true;this.closed=false;this.visible=true;this.dialog=false;this.events=new Map();}
 getClientRects(){return this.visible?[{}]:[];}
 contains(node){for(let item=node;item;item=item.parentElement)if(item===this)return true;return false;}
 closest(selector){if(selector.includes('inert')&&this.closed||selector.includes('dialog')&&this.dialog)return this;return this.parentElement?.closest(selector)??null;}
 addEventListener(type,fn){this.events.set(type,fn);}removeEventListener(type){this.events.delete(type);}
}
function resizeHarness(patch={}){
 const panels=Object.fromEntries(ids.map(id=>[id,new Node()])),field=new Node(panels.left);
 field.value='Pending investigation';field.selectionStart=3;field.selectionEnd=8;
 const document={activeElement:field},events=new Map(),frames=new Map(),revealed=[],state={open:{...all},compact:false,suspended:false};let sequence=0;
 const media={matches:false,addEventListener:(type,fn)=>events.set('media:'+type,fn),removeEventListener:type=>events.delete('media:'+type)};
 const scope={leftOpen:true,rightOpen:true,mapUtilityOpen:true,qwenOpen:true,timelineOpen:true,primaryWorkspace:'map',guideOpen:false,mapShare:null,repositoryOpen:false,
  compactRef:{current:false},document,HTMLElement:Node,compactPanelOwner:policy.compactPanelOwner,revealPanelControl:(panel,control)=>revealed.push({panel,control}),
  leftPanelRef:{current:panels.left},rightPanelRef:{current:panels.evidence},mapUtilityPanelRef:{current:panels.tools},qwenPanelRef:{current:panels.chat},timelineRef:{current:panels.time},
  window:{matchMedia:()=>media,requestAnimationFrame(fn){const id=++sequence;frames.set(id,fn);return id;},cancelAnimationFrame:id=>frames.delete(id),addEventListener:(type,fn)=>events.set(type,fn),removeEventListener:type=>events.delete(type)},
  setIsCompact:value=>state.compact=value,
  setChatLayoutSuspended:value=>state.suspended=value,
 };
 for(const [id,setter] of Object.entries({left:'setLeftOpen',evidence:'setRightOpen',tools:'setMapUtilityOpen',chat:'setQwenOpen',time:'setTimelineOpen'}))scope[setter]=value=>{state.open[id]=value;panels[id].closed=!value;};
 Object.assign(scope,patch);const start=()=>execute(resizeEffect,scope);
 return{scope,panels,field,document,events,frames,revealed,state,media,start,narrow(){media.matches=true;events.get('media:change')();},flush(){for(const [id,fn]of [...frames]){frames.delete(id);fn();}}};
}
test('a breakpoint retains focused controls and closes competing surfaces without editing their content',()=>{
 for(const id of ids){
  const h=resizeHarness();h.field.parentElement=h.panels[id];const cleanup=h.start();h.narrow();h.flush();
  assert.deepEqual(ids.filter(key=>h.state.open[key]),[id]);assert.equal(h.document.activeElement,h.field);
  assert.equal(h.field.value,'Pending investigation');assert.deepEqual([h.field.selectionStart,h.field.selectionEnd],[3,8]);
  assert.equal(h.revealed.at(-1).control,h.field);cleanup();
 }
});
test('share, repository, welcome, report and independent dialog focus cannot acquire a background modal',()=>{
 for(const patch of [{mapShare:{}},{repositoryOpen:true},{guideOpen:true},{primaryWorkspace:'reports'},{primaryWorkspace:'stories'}]){
  const h=resizeHarness(patch),cleanup=h.start();h.narrow();h.flush();assert.deepEqual(ids.filter(id=>h.state.open[id]),[]);assert.equal(h.revealed.length,0);cleanup();
 }
 const h=resizeHarness(),dialog=new Node();dialog.dialog=true;h.document.activeElement=new Node(dialog);const cleanup=h.start();h.narrow();h.flush();assert.deepEqual(ids.filter(id=>h.state.open[id]),[]);cleanup();
});
test('existing compact openings stay open and wide layouts do not dismiss panels',()=>{
 const h=resizeHarness({compactRef:{current:true}});h.media.matches=true;const cleanup=h.start();assert.deepEqual(h.state.open,all);cleanup();
 const wide=resizeHarness(),dispose=wide.start();assert.deepEqual(wide.state.open,all);assert.equal(wide.state.compact,false);dispose();
});
test('a layout-only chat hide keeps its request lifecycle active; explicit Close and leaving Map deactivate it',()=>{
 assert.ok(chatActivity);assert.ok(closeChat);
 const active=(qwenOpen,chatLayoutSuspended,primaryWorkspace='map')=>new Function('qwenOpen','chatLayoutSuspended','primaryWorkspace',`return ${chatActivity};`)(qwenOpen,chatLayoutSuspended,primaryWorkspace);
 const h=resizeHarness(),cleanup=h.start();h.narrow();
 assert.equal(h.state.open.chat,false);assert.equal(h.state.suspended,true);assert.equal(active(h.state.open.chat,h.state.suspended),true,'layout hiding must not trigger the assistant active=false cancellation contract');
 const scope={qwenReturnRef:{current:null},setQwenOpen:value=>h.state.open.chat=value,setChatLayoutSuspended:value=>h.state.suspended=value,window:{setTimeout(){}},mapContainerRef:{current:null}};
 new Function(...Object.keys(scope),compile(`return ${closeChat};`))(...Object.values(scope))();
 assert.equal(active(h.state.open.chat,h.state.suspended),false);
 assert.equal(active(false,true,'reports'),false);assert.equal(active(false,true,'stories'),false);cleanup();
});
test('resize reveal is coalesced, ignores superseded focus and is cancelled on cleanup',()=>{
 const h=resizeHarness(),cleanup=h.start();h.narrow();h.events.get('resize')();h.events.get('resize')();assert.equal(h.frames.size,1);
 h.document.activeElement=new Node();h.flush();assert.equal(h.revealed.length,0);
 h.document.activeElement=h.field;h.events.get('resize')();cleanup();assert.equal(h.frames.size,0);assert.equal(h.events.size,0);
});
test('compact focus keeps the current control and keeps the nonmodal layer sheet from taking map focus',()=>{
 for(const [inside,modal,expected,visible=true]of [[true,true,0],[false,true,1],[false,false,0],[true,true,1,false]]){
  const panel=new Node(),control=new Node(inside?panel:null),document={activeElement:control};let focused=0;
  control.visible=visible;
  const scope={primaryWorkspace:'map',guideOpen:false,isCompact:true,surfaceInspectionOpen:false,mapUtilityOpen:false,rightOpen:false,leftOpen:true,layerPanelIsModal:modal,terrainSurfaceMode:'off',
   mapUtilityPanelRef:{current:null},rightPanelRef:{current:null},leftPanelRef:{current:panel},document,Element:Node,
   visibleFocusableElements:()=>[{focus:()=>focused++}],closeMapUtility(){},closeRightPanel(){},closeLeftPanel(){},closeTimelinePanel(){}};
  const cleanup=execute(focusEffect,scope);assert.equal(focused,expected);cleanup();assert.equal(panel.events.size,0);
 }
});
test('revealing a clipped control scrolls only inside the retained panel',()=>{
 const previous=globalThis.window;
 try{
  globalThis.window={getComputedStyle:node=>({overflowY:node.overflow})};
  for(const initialTop of [5,40,140]){
   const page=new Node(),panel=new Node(page),scroller=new Node(panel),field=new Node(scroller);let top=initialTop,pageScrolls=0,scrolls=0;
   page.overflow='auto';page.clientHeight=100;page.scrollHeight=900;page.scrollBy=()=>pageScrolls++;
   panel.overflow='hidden';scroller.overflow='auto';scroller.clientTop=0;scroller.clientHeight=100;scroller.scrollHeight=400;
   scroller.getBoundingClientRect=()=>({top:20,bottom:120});scroller.scrollBy=({top:delta})=>{top-=delta;scrolls++;};
   field.getBoundingClientRect=()=>({top,bottom:top+30,height:30});policy.revealPanelControl(panel,field);
   assert.ok(top>=20&&top+30<=120);assert.equal(pageScrolls,0);if(initialTop===40)assert.equal(scrolls,0);
  }
 }finally{if(previous===undefined)delete globalThis.window;else globalThis.window=previous;}
});
