import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

const source=await readFile(new URL('../app/page.tsx',import.meta.url),'utf8');
const ast=ts.createSourceFile('page.tsx',source,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
let effect;
function visit(node){
 if(ts.isCallExpression(node)&&node.expression.getText(ast)==='useEffect'){
  const callback=node.arguments[0]?.getText(ast);
  if(callback?.includes('mapUtilityPanelRef.current')&&callback.includes('const commitFrame'))effect=callback;
 }
 ts.forEachChild(node,visit);
}
visit(ast);
assert.ok(effect,'exercise the actual deferred Map controls entry effect');
const code=ts.transpileModule(`return (${effect})();`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;

function harness({previous=null,owner='trigger',hidden=false,open=true,workspace='map',request=1}={}){
 const nodes=Object.fromEntries(['body','trigger','section','summary','field','outside','close'].map(name=>[name,{getClientRects:()=>[{}]}]));
 if(hidden)nodes[owner].getClientRects=()=>[];
 const document={body:nodes.body,activeElement:nodes[owner]},frames=new Map();
 let sequence=0;
 const panel={contains:node=>['section','summary','field','close'].some(name=>nodes[name]===node)};
 const ref={current:panel},entry={current:previous};
 const focus=[];
 nodes.close.focus=options=>{focus.push(options);document.activeElement=nodes.close;};
 const window={requestAnimationFrame:fn=>{frames.set(++sequence,fn);return sequence;},cancelAnimationFrame:id=>frames.delete(id)};
 const context={document,window,primaryWorkspace:workspace,mapUtilityOpen:open,mapUtilityFocusRequest:request,mapUtilityPanelRef:ref,mapUtilityFocusEntryRef:entry,visibleFocusableElements:node=>{assert.equal(node,panel);return[nodes.close];}};
 const cleanup=new Function(...Object.keys(context),code)(...Object.values(context));
 const frame=()=>{const pending=[...frames.values()];frames.clear();for(const run of pending)run();};
 return{nodes,document,frames,ref,entry,focus,cleanup,frame,flush(){frame();frame();}};
}
const retained={workspace:'map',open:true,request:1};

test('initial entry, restored entry and explicit re-entry reach the first usable control',()=>{
 for(const options of [{},{previous:{...retained,open:false}},{previous:{...retained,workspace:'reports'}},{previous:retained,request:2,owner:'field'}]){
  const h=harness(options);h.flush();assert.equal(h.document.activeElement,h.nodes.close);assert.deepEqual(h.focus,[{preventScroll:true}]);
 }
});
test('section and Advanced summary focus survive an internal tool change',()=>{
 for(const owner of ['section','summary','field']){
  const h=harness({previous:retained,owner});h.flush();
  assert.equal(h.document.activeElement,h.nodes[owner]);assert.deepEqual(h.focus,[]);
 }
});
test('an internal view change recovers focus lost by an unmounted or hidden form',()=>{
 for(const options of [{owner:'body'},{owner:'field',hidden:true}]){
  const h=harness({previous:retained,...options});h.flush();assert.equal(h.document.activeElement,h.nodes.close);
 }
});
test('external tool navigation still hands focus into an already open panel',()=>{
 const h=harness({previous:retained,owner:'outside'});h.flush();assert.equal(h.document.activeElement,h.nodes.close);
});
test('a newer focus choice during either deferred frame wins, including blur to body',()=>{
 for(const afterFirstFrame of [false,true])for(const destination of ['field','outside','body']){
  const h=harness();if(afterFirstFrame)h.frame();h.document.activeElement=h.nodes[destination];h.flush();
  assert.equal(h.document.activeElement,h.nodes[destination]);assert.deepEqual(h.focus,[]);
 }
});
test('cleanup cancels both the opening frame and the nested focus frame',()=>{
 for(const afterFirstFrame of [false,true]){
  const h=harness();if(afterFirstFrame)h.frame();h.cleanup();h.flush();
  assert.equal(h.document.activeElement,h.nodes.trigger);assert.equal(h.frames.size,0);assert.deepEqual(h.focus,[]);
 }
});
test('closed panels and other workspaces do not schedule entry',()=>{
 for(const options of [{open:false},{workspace:'reports'}]){
  const h=harness(options);h.flush();assert.equal(h.frames.size,0);assert.deepEqual(h.focus,[]);
 }
});
test('a removed panel cannot receive deferred focus',()=>{
 const h=harness();h.ref.current=null;h.flush();assert.equal(h.document.activeElement,h.nodes.trigger);assert.deepEqual(h.focus,[]);
});
