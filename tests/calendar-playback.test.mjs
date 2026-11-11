import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';
const js = ts.transpileModule(await readFile('app/calendar-sweep.ts','utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext } }).outputText;
const calendar = await import('data:text/javascript;base64,' + Buffer.from(js).toString('base64'));
test('exhausted checked-empty playback clears intent and does not restart when skipping is disabled', async () => {
  const timers = new Map(); let nextTimer = 0;
  const h = await componentHarness(new URL('../app/compact-time-sweep.tsx', import.meta.url), {
    './calendar-sweep': calendar, './time-emblem': { TimeEmblem: 'emblem' }, './compact-time-sweep.css': {}, './time-controls-focus': { retainTimeControlFocus() {} },
  }, { window: { setTimeout: fn => { timers.set(++nextTimer, fn); return nextTimer; }, clearTimeout: id => timers.delete(id) }, document: { hidden: false, addEventListener() {}, removeEventListener() {} } });
  const props = { value: {day:'2026-10-01',start:'2026-10-01',end:'2026-10-03',step:'days',before:null,showing:'B'},year:2026,years:[2026],today:'2026-10-21',sources:[{id:'quakes',state:'ready'}],open:true,onOpenChange(){},onPresent(){},onEra(){},onSeek: async next => { props.value = next; return {state:'empty', message:'No mapped records'}; } };
  const render = () => { const tree = h.render(h.exports.CompactTimeSweep, props); h.commit(); return tree; };
  const button = (tree, label) => findNode(tree, n => n.props?.['aria-label'] === label);
  const skip = tree => findNode(tree, n => n.type === 'input' && n.props.type === 'checkbox' && n.props.onChange.toString().includes('setSkipGaps'));
  let tree = render();
  for (let i = 0; i < 2; i++) { button(tree,'Next sweep frame').props.onClick(); await settle(); tree = render(); }
  for (let i = 0; i < 2; i++) { button(tree,'Previous sweep frame').props.onClick(); await settle(); tree = render(); }
  // Select the actual skip-empty checkbox, not the decorative animation switch.
  const skipControl = skip(tree);
  skipControl.props.onChange({target:{checked:true}}); tree = render();
  button(tree,'Play time sweep').props.onClick(); tree = render();
  for (const [id, fn] of [...timers]) { timers.delete(id); fn(); }
  await settle(); tree = render();
  assert.ok(button(tree,'Play time sweep'), 'exhaustion must show paused');
  skip(tree).props.onChange({target:{checked:false}}); tree = render();
  assert.ok(button(tree,'Play time sweep'), 'changing skip must not revive play intent');
  h.dispose();
});


test('one stationary clock opens and closes time controls without hover or an animation setting', async () => {
  const h = await componentHarness('app/compact-time-sweep.tsx', {
    './calendar-sweep': calendar, './compact-time-sweep.css': {}, './time-controls-focus': { retainTimeControlFocus() {} },
  }, { window: { requestAnimationFrame: fn => fn(), setTimeout, clearTimeout }, document: { addEventListener() {}, removeEventListener() {} } });
  const props = { value:null,year:2026,years:[2026],today:'2026-10-21',sources:[],open:false,
    onOpenChange(value){props.open=value;},onSeek:async()=>({state:'empty',message:'No records'}),onEra(){},onPresent(){} };
  const render=()=>{const tree=h.render(h.exports.CompactTimeSweep,props);h.commit();return tree;};
  let tree=render();
  const clock=()=>findNode(tree,n=>n.props?.className?.includes('compact-time-clock-toggle'));
  assert.equal(clock().props['aria-expanded'],false);
  assert.equal(clock().props.onPointerEnter,undefined);
  assert.equal(findNode(tree,n=>n.type==='img'&&n.props.src.endsWith('/clock.svg')).props.alt,'');
  clock().props.onClick();tree=render();
  assert.equal(clock().props['aria-expanded'],true);
  assert.ok(findNode(tree,n=>n.props?.role==='dialog'));
  assert.equal(findNode(tree,n=>n.props?.className==='compact-time-animation-choice'),undefined);
  clock().props.onClick();tree=render();
  assert.equal(clock().props['aria-expanded'],false);
  assert.equal(findNode(tree,n=>n.props?.role==='dialog'),undefined);
  clock().props.onKeyDown({key:'ArrowUp',preventDefault(){}});tree=render();
  assert.equal(clock().props['aria-expanded'],true);
  tree.props.onKeyDown({key:'Escape',preventDefault(){},stopPropagation(){}});tree=render();
  assert.equal(clock().props['aria-expanded'],false);
  h.dispose();
});

class PointerNode {
  constructor(parent=null){this.parent=parent;}
  contains(node){for(let item=node;item;item=item.parent)if(item===this)return true;return false;}
}
class PointerElement extends PointerNode {
  constructor(parent=null,controls=null){super(parent);this.controls=controls;}
  closest(selector){const id=selector.match(/^\[aria-controls="([^"]+)"\]$/)?.[1];return id&&this.controls===id?this:this.parent?.closest?.(selector)??null;}
}
async function pointerHarness(t,open=true){
  const listeners=new Map(),root=new PointerElement(),changes=[];
  const h=await componentHarness('app/compact-time-sweep.tsx',{
    './calendar-sweep':calendar,'./compact-time-sweep.css':{},'./time-controls-focus':{retainTimeControlFocus(){}},
  },{Node:PointerNode,Element:PointerElement,window:{requestAnimationFrame:fn=>fn(),setTimeout,clearTimeout},document:{hidden:false,
    addEventListener(type,fn){listeners.set(type,fn);},removeEventListener(type,fn){assert.equal(listeners.get(type),fn);listeners.delete(type);}}});
  const props={value:null,year:2026,years:[2026],today:'2026-10-21',sources:[],open,
    onOpenChange(value){props.open=value;changes.push(value);},onSeek(){throw Error('Pointer routing must not seek a date');},onEra(){},onPresent(){}};
  const render=()=>{const tree=h.render(h.exports.CompactTimeSweep,props);tree.props.ref.current=root;h.commit();return tree;};
  t.after(()=>h.dispose());
  return{props,changes,root,render,pointer:target=>listeners.get('pointerdown')?.({target})};
}
test('the external Time toggle owns its click without a preceding outside-pointer dismissal',async t=>{
  const h=await pointerHarness(t);h.render();
  const trigger=new PointerElement(null,'compact-time-settings'),label=new PointerElement(trigger);
  h.pointer(label);assert.deepEqual(h.changes,[]);assert.equal(h.props.open,true);
  h.props.onOpenChange(!h.props.open);const tree=h.render();
  assert.equal(findNode(tree,n=>n.props?.role==='dialog'),undefined);assert.deepEqual(h.changes,[false]);
});
test('inside controls stay open while unrelated outside controls still dismiss Time',async t=>{
  const h=await pointerHarness(t);h.render();
  h.pointer(new PointerElement(h.root));assert.deepEqual(h.changes,[]);
  h.pointer(new PointerElement(null,'another-panel'));const tree=h.render();
  assert.deepEqual(h.changes,[false]);assert.equal(findNode(tree,n=>n.props?.role==='dialog'),undefined);
  assert.equal(tree.props['data-expanded'],false);
});
test('the clock can retain transport-only mode and an outside pointer still closes it',async t=>{
  const h=await pointerHarness(t,false);let tree=h.render();
  findNode(tree,n=>n.props?.className?.includes('compact-time-clock-toggle')).props.onClick();tree=h.render();
  findNode(tree,n=>n.props?.['aria-label']==='Time sweep settings').props.onClick();tree=h.render();
  assert.equal(h.props.open,false);assert.equal(tree.props['data-expanded'],true);assert.equal(findNode(tree,n=>n.props?.role==='dialog'),undefined);
  h.pointer(new PointerElement());tree=h.render();assert.equal(tree.props['data-expanded'],false);
});
