import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import * as surfaces from '../app/assistant-surfaces.mjs';
import {componentHarness,findNode,settle} from './component-harness.mjs';

// Structural regression for docs/chat-composer-reach-20261018.md: the question box
// stays pinned while everything else scrolls. Rendered-viewport acceptance stays a
// browser check; this guards the structure that makes it possible.
const source=await readFile(new URL('../app/assistant/workspace.tsx',import.meta.url),'utf8');
const css=await readFile(new URL('../app/assistant/workspace.module.css',import.meta.url),'utf8');
const investigation=await import('data:text/javascript;base64,'+Buffer.from(ts.transpileModule(await readFile(new URL('../app/assistant-investigation.ts',import.meta.url),'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64'));
const rule=selector=>{const match=css.match(new RegExp('(?:^|[}\\n])'+selector.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\{([^}]*)\\}'));assert.ok(match,'missing CSS rule '+selector);return match[1];};
const text=node=>[node?.props?.children].flat(Infinity).map(value=>typeof value==='string'?value:typeof value==='object'?text(value):'').join('');
const all=(node,predicate,found=[])=>{if(!node||typeof node!=='object')return found;if(predicate(node))found.push(node);for(const child of [node.props?.children].flat(Infinity))all(child,predicate,found);return found;};
const focus={title:'Synthetic county',detail:'Synthetic source context',context:{version:1,frame:2026,view:'2D',layers:[],selection:{kind:'knowledge',recordId:'synthetic-one'}}};

async function renderChat(){
 const classes=new Proxy({},{get:(_,key)=>key});
 const ready=()=>Response.json({configured:true,online:true,ready:true,evidenceSearchAvailable:true,requiresLogin:false});
 const h=await componentHarness(new URL('../app/assistant/workspace.tsx',import.meta.url),{'./workspace.module.css':{default:classes},'../assistant-surfaces.mjs':surfaces,'../assistant-investigation':investigation},{fetch:async()=>ready(),Response,TextEncoder,FormData:class {get(){return null;}},queueMicrotask,setInterval:()=>1,clearInterval:()=>{}});
 const render=()=>{const tree=h.render(h.exports.default,{focus,place:'Synthetic County'});h.commit();return tree;};
 render();await settle();
 return {h,render};
}

test('the chat scroll region scrolls and the conversation log no longer scrolls on its own',()=>{
 const body=rule('.body');
 assert.match(body,/overflow-y:auto/);assert.match(body,/min-height:0/);assert.match(body,/overscroll-behavior:contain/);assert.match(body,/flex:1 1 0%/);
 const messages=rule('.messages');
 assert.doesNotMatch(messages,/overflow:auto|overflow-y:auto|flex:1/);assert.match(messages,/overflow:visible/);
 assert.doesNotMatch(css,/\.composer[^{]*\{[^}]*flex-shrink:0/,'the composer must not be a fixed non-shrinking block');
 const composer=rule('.composer');assert.match(composer,/min-height:0/);assert.match(composer,/flex-direction:column/);
 assert.match(rule('.optionsBody'),/max-height:min\(40vh,280px\);overflow-y:auto/);
 assert.match(rule('.composer summary'),/min-height:44px/);assert.match(rule('.actions button'),/min-height:44px/);
 assert.match(css,/@media \(max-height:820px\)\{[^@]*\.composer textarea\{min-height:44px/);
 assert.match(css,/\.chat button:focus-visible[^{]*\.chat summary:focus-visible[^{]*\.chat textarea:focus-visible[^{]*\{outline:3px solid #e3c883;outline-offset:2px\}/);
});

test('the pinned form holds answer options, the message box and Send; prompts and the footer live in the scroll region',async()=>{
 const {h,render}=await renderChat();
 try{
  let tree=render();
  const body=findNode(tree,node=>node.props?.className==='body'),form=findNode(tree,node=>node.type==='form'&&node.props.className==='composer');
  assert.ok(body,'scroll region renders');assert.ok(form,'composer form renders');
  assert.equal(findNode(body,node=>node.type==='form'),undefined,'the form is not inside the scroll region');
  for(const predicate of [node=>node.props?.className==='context',node=>node.props?.className==='guide',node=>node.props?.role==='log'&&node.props['aria-label']==='KFM chat conversation'&&node.props['aria-live']==='polite'&&node.props.tabIndex===0,node=>node.props?.['aria-label']==='Suggested questions',node=>node.type==='footer'])assert.ok(findNode(body,predicate));
  const regionOrder=[body.props.children].flat(Infinity).filter(child=>child&&typeof child==='object').map(child=>child.props.role==='log'?'log':child.props['aria-label']==='Suggested questions'?'prompts':child.type==='footer'?'footer':child.props.className);
  assert.deepEqual(regionOrder,['context','guide','log','prompts','footer']);
  assert.match(text(findNode(body,node=>node.type==='footer')),/^AI discussion does not establish truth · temporary questions expire after 15 minutes\.$/);
  const prompts=all(findNode(body,node=>node.props?.['aria-label']==='Suggested questions'),node=>node.type==='button');
  assert.ok(prompts.length>0);for(const button of prompts){assert.equal(button.props.type,'button');assert.equal(button.props.disabled,false);}
  assert.equal(findNode(form,node=>node.props?.['aria-label']==='Suggested questions'),undefined,'prompts are no longer inside the form');

  const formOrder=[form.props.children].flat(Infinity).filter(child=>child&&typeof child==='object');
  assert.equal(formOrder.length,3);
  const [options,messageLabel,actions]=formOrder;
  assert.equal(options.type,'details');assert.equal(options.props.className,'options');
  const summary=findNode(options,node=>node.type==='summary');assert.equal(text(summary),'Answer options · Explore ideas');
  assert.ok(findNode(messageLabel,node=>node.type==='textarea'));
  assert.equal(actions.props.className,'actions');
  const submit=findNode(actions,node=>node.type==='button'&&node.props.type!=='button');assert.equal(text(submit),'Send');
  assert.match(text(findNode(actions,node=>node.type==='small')),/unverified discussion/);
  for(const name of ['mode','style','depth','term','place','start','end']){
   assert.ok(findNode(options,node=>node.props?.name===name),name+' stays inside the composer form');
   assert.equal(all(tree,node=>node.props?.name===name).length,1,name+' is rendered once');
  }
  assert.ok(findNode(options,node=>node.type==='details'&&text(findNode(node,child=>child.type==='summary'))==='Evidence search filters'));

  findNode(form,node=>node.type==='select'&&node.props.name==='mode').props.onChange({target:{value:'evidence'}});
  tree=render();
  const evidenceForm=findNode(tree,node=>node.type==='form'&&node.props.className==='composer');
  assert.equal(text(findNode(evidenceForm,node=>node.type==='summary')),'Answer options · Find evidence');
  assert.ok(findNode(evidenceForm,node=>node.type==='button'&&text(node)==='Search'));
  assert.match(text(findNode(evidenceForm,node=>node.props?.className==='actions')),/Released records/);
 }finally{h.dispose();}
});

test('new turns scroll the scroll region, not the log, and only once there is a turn',()=>{
 assert.match(source,/<div ref=\{bodyRef\} className=\{styles\.body\}>/);
 const effect=source.split('\n').find(line=>/useEffect\(.*\[turns,job\]\);$/.test(line));
 assert.ok(effect,'autoscroll effect exists');
 assert.match(effect,/bodyRef\.current/);assert.match(effect,/body\.scrollTo\(/);assert.match(effect,/!turns\.length\)return/);
 assert.doesNotMatch(effect,/logRef\.current\?\.scrollTo/);
});

test('the compact chat sheet hides the duplicate heading accessibly and keeps map context to one row',async()=>{
 const sheet=await readFile(new URL('../app/inspection-panel.css',import.meta.url),'utf8');
 const compact=sheet.slice(sheet.indexOf('@media (max-width: 1100px)')),desktop=sheet.slice(sheet.indexOf('@media (min-width: 1101px)'),sheet.indexOf('@media (max-width: 1100px)'));
 assert.ok(compact.length&&desktop.length);
 assert.doesNotMatch(desktop+sheet.slice(0,sheet.indexOf('@media')),/qwen-panel-heading|qwen-context-strip/,'desktop and shared rules are unchanged');
 const block=selector=>{const at=compact.indexOf(selector+' {');assert.ok(at>=0,'missing compact rule '+selector);return compact.slice(at,compact.indexOf('}',at));};
 // Prefix .explorer-shell[data-inspector] > .qwen-panel outranks globals.css (.qwen-panel .qwen-context-strip span, .qwen-context-strip span:nth-child(-n+2)).
 const prefix='.explorer-shell[data-inspector] > .qwen-panel';
 const heading=block(prefix+' .qwen-panel-heading');
 for(const declaration of ['position: absolute','width: 1px','height: 1px','overflow: hidden','clip: rect(0, 0, 0, 0)','white-space: nowrap'])assert.ok(heading.includes(declaration),declaration);
 assert.doesNotMatch(heading,/display:\s*none|visibility:\s*hidden/,'the heading stays the dialog accessible name');
 assert.match(block(prefix+' .qwen-context-strip'),/grid-template-columns: repeat\(4, minmax\(0, 1fr\)\)/);
 assert.match(block(prefix+' .qwen-context-strip span'),/border-bottom: 0;[^}]*border-right: 1px solid var\(--line\)/);
 assert.match(block(prefix+' .qwen-context-strip span:last-child'),/border-right: 0/);
 assert.match(block(prefix+' .qwen-context-strip small'),/font-size: 9px;[^}]*white-space: nowrap/);
 assert.match(block(prefix+' .qwen-context-strip strong'),/text-overflow: ellipsis/);
 const page=await readFile(new URL('../app/page.tsx',import.meta.url),'utf8');
 assert.match(page,/className="qwen-panel" role="dialog"[^>]*aria-labelledby="qwen-panel-title"/);assert.match(page,/<h2 id="qwen-panel-title">Chat with KFM<\/h2>/);
});
