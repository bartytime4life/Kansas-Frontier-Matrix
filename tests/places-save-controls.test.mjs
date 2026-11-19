import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import {componentHarness,findNode} from './component-harness.mjs';

const trail=await import('data:text/javascript;base64,'+Buffer.from(ts.transpileModule(await readFile(new URL('../app/places-trail.ts',import.meta.url),'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64'));
async function harness(context='places'){
 const focus=[],names=[];let saves=0,undos=0,visible=true,blocked=false;
 const element=label=>({focus(){focus.push(label);},getClientRects:()=>visible?[{}]:[],closest:()=>blocked?{}:null});
 const name=element('name'),undo=element('undo');
 const h=await componentHarness(new URL('../app/places-save-controls.tsx',import.meta.url),{
  './places-trail':trail,'./places-save-controls.module.css':{default:{}},
 });
 const props={context,count:0,name:'',notice:'',removedName:null,focusRequest:null,onName:value=>names.push(value),onSave:()=>saves++,onUndo:()=>undos++};
 const render=()=>{const tree=h.render(h.exports.PlacesSaveControls,props);findNode(tree,n=>n.type==='input').props.ref.current=name;const button=findNode(tree,n=>n.type==='button'&&n.props.children==='Undo removal');if(button)button.props.ref.current=undo;h.commit();return tree;};
 return{h,props,render,focus,names,visibility(value){visible=value;},blocked(value){blocked=value;},get saves(){return saves;},get undos(){return undos;}};
}

test('save forms label their name and capacity and submit through Enter-compatible native form behavior',async()=>{
 for(const context of ['places','workspace']){
  const p=await harness(context),tree=p.render(),input=findNode(tree,n=>n.type==='input');
  assert.equal(findNode(tree,n=>n.type==='label').props.htmlFor,input.props.id);
  assert.ok(findNode(tree,n=>n.type==='p'&&n.props.id===input.props['aria-describedby']));
  input.props.onChange({target:{value:'x'.repeat(100)}});assert.equal(p.names[0].length,50);
  let prevented=false;findNode(tree,n=>n.type==='form').props.onSubmit({preventDefault(){prevented=true;}});
  assert.equal(prevented,true);assert.equal(p.saves,1);p.h.dispose();
 }
});

test('full Places disables the save action and explains how to make room while retaining the entered name',async()=>{
 const p=await harness();p.props.count=12;p.props.name='Pending investigation';const tree=p.render();
 assert.equal(findNode(tree,n=>n.type==='button'&&n.props.type==='submit').props.disabled,true);
 assert.equal(findNode(tree,n=>n.type==='input').props.value,'Pending investigation');
 const capacity=findNode(tree,n=>n.type==='p'&&n.props.id);assert.ok(capacity.props.children.includes(trail.PLACES_FULL_MESSAGE));
 p.h.dispose();
});

test('a removal moves focus to Undo once and undo returns it to the originating name field',async()=>{
 const p=await harness();p.props.removedName='River view';p.props.focusRequest={version:1,context:'places',target:'undo'};
 let tree=p.render();assert.deepEqual(p.focus,['undo']);
 p.props.notice='Storage unavailable; retry undo';p.render();assert.deepEqual(p.focus,['undo'],'feedback updates never redirect focus');
 findNode(tree,n=>n.type==='button'&&n.props.children==='Undo removal').props.onClick();assert.equal(p.undos,1);
 p.props.removedName=null;p.props.focusRequest={version:2,context:'places',target:'name'};p.render();assert.deepEqual(p.focus,['undo','name']);p.h.dispose();
});

test('hidden, inert and other-surface controls cannot claim a removal focus request',async()=>{
 for(const mode of ['other','hidden','inert']){
  const p=await harness('workspace');p.props.removedName='River view';p.props.focusRequest={version:1,context:mode==='other'?'places':'workspace',target:'undo'};
  if(mode==='hidden')p.visibility(false);if(mode==='inert')p.blocked(true);
  p.render();assert.deepEqual(p.focus,[]);p.h.dispose();
 }
});

test('failed writes keep a readable status and the same undo action available',async()=>{
 const p=await harness();p.props.notice='Places could not be updated; existing places are unchanged.';p.props.removedName='River view';
 const tree=p.render(),status=findNode(tree,n=>n.props?.role==='status');assert.equal(status.props['aria-live'],'polite');
 assert.ok(findNode(status,n=>n.type==='p'&&n.props.children===p.props.notice));
 assert.equal(findNode(status,n=>n.type==='button').props['aria-label'],'Undo removal of River view');p.h.dispose();
});
