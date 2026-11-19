import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

const code=ts.transpileModule(await readFile('app/time-controls-focus.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const {retainTimeControlFocus}=await import('data:text/javascript;base64,'+Buffer.from(code).toString('base64'));
class Element {
 constructor(name,parent=null){this.name=name;this.parent=parent;this.isConnected=true;this.visible=true;this.disabled=false;this.hidden=false;this.listeners=new Map();this.value='2026-10-12';this.focusCalls=[];}
 contains(node){for(let item=node;item;item=item.parent)if(item===this)return true;return false;}
 matches(selector){return selector===':disabled'?this.disabled:selector==='.compact-time-date-mobile'&&this.name==='mobile';}
 closest(selector){
  if(selector.includes('[hidden]')&&this.hidden||selector==='.compact-time-date'&&this.name==='parts'||selector==='.timeline-panel'&&this.name==='container')return this;
  return this.parent?.closest(selector)??null;
 }
 getClientRects(){return this.visible&&(!this.parent||this.parent.getClientRects().length)?[{}]:[];}
 addEventListener(type,fn){this.listeners.set(type,fn);}removeEventListener(type,fn){assert.equal(this.listeners.get(type),fn);this.listeners.delete(type);}
}
function harness(t,initial='month'){
 const old=new Map(['window','document','HTMLElement','Node','ResizeObserver'].map(key=>[key,{exists:key in globalThis,value:globalThis[key]}]));
 const document=new Element('document'),body=new Element('body'),container=new Element('container',body),root=new Element('root',container),parts=new Element('parts',root);
 const controls={year:new Element('year',parts),month:new Element('month',parts),day:new Element('day',parts),mobile:new Element('mobile',root),step:new Element('step',root),compare:new Element('compare',root),scrubber:new Element('scrubber',root),settings:new Element('settings',root),clock:new Element('clock',root)};
 controls.mobile.visible=initial==='mobile';parts.visible=initial!=='mobile';
 root.querySelector=selector=>controls[({'.compact-time-date-mobile':'mobile','.compact-time-date select':'year','.compact-time-more':'settings','.compact-time-clock-toggle':'clock'})[selector]]??null;
 const window=new Element('window'),frames=new Map();let sequence=0,observer;
 window.requestAnimationFrame=fn=>{frames.set(++sequence,fn);return sequence;};window.cancelAnimationFrame=id=>frames.delete(id);window.getComputedStyle=()=>({visibility:'visible'});
 document.body=body;document.documentElement=new Element('html');document.activeElement=controls[initial];document.hidden=false;
 for(const control of Object.values(controls))control.focus=options=>{control.focusCalls.push(options);document.activeElement=control;document.listeners.get('focusin')?.({target:control});};
 class Observer{constructor(callback){observer={callback,observe(node){this.node=node;},disconnect(){this.disconnected=true;}};return observer;}}
 Object.assign(globalThis,{document,window,HTMLElement:Element,Node:Element,ResizeObserver:Observer});
 const dispose=retainTimeControlFocus(root);let disposed=false;
 const cleanup=()=>{if(disposed)return;disposed=true;dispose();for(const[key,entry]of old){if(entry.exists)globalThis[key]=entry.value;else delete globalThis[key];}};
 t.after(cleanup);
 return{document,window,body,root,container,parts,controls,frames,get observer(){return observer;},cleanup,
  blur(){document.activeElement=body;},resize(){window.listeners.get('resize')();},flush(){for(const[id,fn]of[...frames]){frames.delete(id);fn();}}};
}
test('date parts hand focus to the compact date button without changing the selected date',t=>{
 for(const name of ['year','month','day']){
  const h=harness(t,name);h.parts.visible=false;h.controls.mobile.visible=true;h.blur();
  h.document.listeners.get('focusin')({target:h.body});h.resize();h.flush();
  assert.equal(h.document.activeElement,h.controls.mobile);assert.equal(h.controls[name].value,'2026-10-12');
  assert.deepEqual(h.controls.mobile.focusCalls,[{preventScroll:true}]);
  h.parts.visible=true;h.controls.mobile.visible=false;h.blur();h.resize();h.flush();
  assert.equal(h.document.activeElement,h.controls[name],'expanding restores the same date part');h.cleanup();
 }
});
test('expanding replaces a hidden compact date button with the desktop year control',t=>{
 const h=harness(t,'mobile');h.controls.mobile.visible=false;h.parts.visible=true;h.blur();h.resize();h.flush();
 assert.equal(h.document.activeElement,h.controls.year);
});
test('hidden frame, scrubber and compare controls fall back to visible settings without activating anything',t=>{
 for(const name of ['step','scrubber','compare']){
  const h=harness(t,name);h.controls[name].visible=false;h.blur();h.resize();h.flush();
  assert.equal(h.document.activeElement,h.controls.settings);assert.equal(h.controls[name].value,'2026-10-12');h.cleanup();
 }
});
test('visible controls and deliberate outside focus or pointer actions keep their ownership',t=>{
 const h=harness(t);h.resize();h.flush();assert.equal(h.document.activeElement,h.controls.month);assert.equal(h.controls.month.focusCalls.length,0);
 h.controls.month.visible=false;const outside=new Element('outside',h.body);h.document.activeElement=outside;h.resize();h.flush();assert.equal(h.document.activeElement,outside);
 h.blur();h.document.listeners.get('focusin')({target:outside});h.resize();h.flush();assert.equal(h.document.activeElement,h.body);
 h.document.listeners.get('focusin')({target:h.controls.month});h.document.listeners.get('pointerdown')({target:outside});h.resize();h.flush();assert.equal(h.document.activeElement,h.body);
});
test('a container-only resize coalesces work and cleanup revokes pending focus',t=>{
 const h=harness(t);assert.equal(h.observer.node,h.container);h.controls.month.visible=false;h.blur();h.observer.callback();h.observer.callback();assert.equal(h.frames.size,1);
 h.flush();assert.equal(h.document.activeElement,h.controls.settings);
 h.controls.settings.visible=false;h.observer.callback();const pending=[...h.frames.values()][0];h.cleanup();assert.equal(h.frames.size,0);assert.equal(h.observer.disconnected,true);assert.equal(h.document.listeners.size,0);assert.equal(h.window.listeners.size,0);
 pending();assert.equal(h.controls.clock.focusCalls.length,0);
});
test('a concealed, disconnected or background time surface never reacquires focus',t=>{
 for(const state of ['concealed','disconnected','background']){
  const h=harness(t);h.controls.month.visible=false;h.blur();
  if(state==='concealed')h.root.visible=false;else if(state==='disconnected')h.controls.month.isConnected=false;else h.document.hidden=true;
  h.resize();h.flush();assert.equal(h.document.activeElement,h.body);h.cleanup();
 }
});
