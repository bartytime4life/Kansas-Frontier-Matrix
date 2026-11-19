import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';

const url='https://example.org/?topic=water&c=-98.38%2C38.48&t=2026';
const deferred=()=>{let resolve,reject;const promise=new Promise((done,fail)=>{resolve=done;reject=fail;});return {promise,resolve,reject};};

async function harness(initialCopy=Promise.resolve(false)) {
 const writes=[],copies=[],focus=[],selected=[],document={activeElement:null};let closed=0;
 const first={focus(){focus.push('first');document.activeElement=this;}},last={focus(){focus.push('last');document.activeElement=this;}};
 const navigator={clipboard:{writeText(value){writes.push(value);const copy=deferred();copies.push(copy);return copy.promise;}}};
 const trigger={focus:()=>focus.push('trigger')},fallback={focus:()=>focus.push('map')};
 const h=await componentHarness(new URL('../app/map-share-dialog.tsx',import.meta.url),{
  './map-share-dialog.module.css':{default:{}},'./modal-background':{modalReturnTarget:(target,other)=>target??other,modalFocusableElements:()=>[first,field,last]},
 },{navigator,document});
 const events=new Map(),dialog={open:false,showModal(){this.open=true;},close(){this.open=false;},addEventListener(type,fn){events.set(type,fn);},removeEventListener(type){events.delete(type);}};
 const field={focus(){focus.push('link');document.activeElement=this;},select:()=>selected.push('all')};
 const props={request:{url,redacted:false,initialCopy,returnTarget:trigger},fallbackTarget:fallback,onClose:()=>closed++};
 const render=()=>{const tree=h.render(h.exports.MapShareDialog,props);tree.props.ref.current=dialog;findNode(tree,n=>n.type==='textarea').props.ref.current=field;h.commit();return tree;};
 const status=()=>findNode(render(),n=>n.props?.role==='status').props.children;
 const button=name=>findNode(render(),n=>n.type==='button'&&n.props.children===name);
 return {h,props,render,status,button,navigator,writes,copies,focus,selected,dialog,document,first,last,keydown:event=>events.get('keydown')(event),get closed(){return closed;}};
}

test('clipboard denial, missing APIs and throwing accessors resolve to a manual-copy result',async()=>{
 const p=await harness();
 const copying=p.h.exports.copyMapLink(url);p.copies[0].resolve();assert.equal(await copying,true);
 p.navigator.clipboard={writeText(){throw new Error('denied');}};
 assert.equal(await p.h.exports.copyMapLink(url),false);
 delete p.navigator.clipboard;assert.equal(await p.h.exports.copyMapLink(url),false);
 Object.defineProperty(p.navigator,'clipboard',{get(){throw new Error('security policy');}});
 assert.equal(await p.h.exports.copyMapLink(url),false);
});

test('opening selects the complete readonly link and reports successful automatic copying',async()=>{
 const p=await harness(Promise.resolve(true)),tree=p.render();await settle();
 assert.equal(p.dialog.open,true);assert.deepEqual(p.focus,['link']);assert.deepEqual(p.selected,['all']);
 const field=findNode(tree,n=>n.type==='textarea');assert.equal(field.props.readOnly,true);assert.equal(field.props.value,url);
 assert.equal(p.status(),'Link copied.');assert.ok(p.button('Copy again'));assert.equal(p.writes.length,0);
 p.h.dispose();assert.equal(p.dialog.open,false);assert.equal(p.focus.at(-1),'trigger');
});

test('failed copy retains the link and a deliberate retry copies the captured URL',async()=>{
 const p=await harness();p.render();await settle();assert.match(p.status(),/Automatic copying is unavailable/);
 p.button('Select link').props.onClick();assert.equal(p.focus.at(-1),'link');assert.equal(p.selected.length,2);
 p.button('Copy link').props.onClick();assert.match(p.status(),/Copying link/);assert.deepEqual(p.writes,[url]);
 p.copies[0].resolve();await settle();assert.equal(p.status(),'Link copied.');
 p.h.dispose();
});

test('a late initial failure cannot replace a successful newer retry',async()=>{
 const initial=deferred(),p=await harness(initial.promise);p.render();p.button('Copy link').props.onClick();
 p.copies[0].resolve();await settle();assert.equal(p.status(),'Link copied.');
 initial.resolve(false);await settle();assert.equal(p.status(),'Link copied.');p.h.dispose();
});

test('only the latest retry updates feedback and completion after unmount is ignored',async()=>{
 const p=await harness();p.render();await settle();p.button('Copy link').props.onClick();p.button('Copy link').props.onClick();
 p.copies[1].resolve();await settle();assert.equal(p.status(),'Link copied.');
 p.copies[0].reject(new Error('late denied clipboard'));await settle();assert.equal(p.status(),'Link copied.');
 p.button('Copy again').props.onClick();assert.match(p.status(),/Copying link/);p.h.dispose();
 p.copies[2].resolve();await settle();assert.match(p.status(),/Copying link/);
});

test('Escape is owned by the share dialog and native cancel also closes it',async()=>{
 const p=await harness(),tree=p.render();let prevented=0,stopped=0;
 p.keydown({key:'Escape',preventDefault(){prevented++;},stopPropagation(){stopped++;}});
 assert.equal(p.closed,1);assert.equal(prevented,1);assert.equal(stopped,1);
 tree.props.onCancel({preventDefault(){prevented++;}});assert.equal(p.closed,2);assert.equal(prevented,2);
 p.button('Done').props.onClick();assert.equal(p.closed,3);p.h.dispose();
});

test('dialog keystrokes do not reach map shortcuts or suppress native copying and Tab',async()=>{
 const p=await harness();p.render();
 for(const key of ['l','r','/','Tab','c']){
  let stopped=false;p.keydown({key,stopPropagation(){stopped=true;},preventDefault(){assert.fail('native default must remain available');}});assert.equal(stopped,true);
 }
 assert.equal(p.closed,0);p.h.dispose();
});

test('Tab and Shift+Tab wrap at the share dialog boundaries',async()=>{
 const p=await harness();p.render();let prevented=0;
 p.first.focus();p.keydown({key:'Tab',shiftKey:true,stopPropagation(){},preventDefault(){prevented++;}});assert.equal(p.document.activeElement,p.last);
 p.keydown({key:'Tab',shiftKey:false,stopPropagation(){},preventDefault(){prevented++;}});assert.equal(p.document.activeElement,p.first);
 assert.equal(prevented,2);p.h.dispose();
});

test('redaction disclosure is explicit only for a redacted captured link',async()=>{
 const p=await harness();p.props.request={...p.props.request,redacted:true};
 assert.ok(findNode(p.render(),n=>n.type==='p'&&n.props.children==='Location-derived camera replaced with statewide Kansas. The analysis area is omitted.'));
 p.h.dispose();
 const q=await harness();assert.equal(findNode(q.render(),n=>n.type==='p'&&typeof n.props.children==='string'&&n.props.children.includes('Location-derived camera')),undefined);q.h.dispose();
});

const page=ts.createSourceFile('page.tsx',await readFile(new URL('../app/page.tsx',import.meta.url),'utf8'),ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
let share;
function visit(node){if(ts.isVariableDeclaration(node)&&node.name.getText(page)==='shareView')share=node.initializer.getText(page);ts.forEachChild(node,visit);}visit(page);
const shareJs=ts.transpileModule(`return ${share};`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
test('sharing opens the exact captured link even when address-bar updates are refused',()=>{
 for(const redacted of [false,true]){
  const params=new URLSearchParams('topic=water&c=-98.38%2C38.48&t=2026');if(redacted)params.set('privacy','location-camera-redacted');
  const requests=[],copied=[],replaced=[],trigger={},copy=Promise.resolve(false);
  const scope={buildExplorerParams:()=>params,window:{location:{origin:'https://example.org',pathname:'/'}},replaceExplorerHistory:path=>{replaced.push(path);return false;},copyMapLink:value=>{copied.push(value);return copy;},setMapShare:value=>requests.push(value)};
  new Function(...Object.keys(scope),shareJs)(...Object.values(scope))(trigger);
  assert.equal(requests.length,1);assert.equal(requests[0].url,`https://example.org/?${params}`);assert.equal(requests[0].redacted,redacted);
  assert.equal(requests[0].initialCopy,copy);assert.equal(requests[0].returnTarget,trigger);assert.deepEqual(copied,[requests[0].url]);assert.deepEqual(replaced,[`/?${params}`]);
 }
});
