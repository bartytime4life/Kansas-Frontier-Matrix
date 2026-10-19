import test from 'node:test';
import assert from 'node:assert/strict';
import {randomUUID} from 'node:crypto';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import * as surfaces from '../app/assistant-surfaces.mjs';
import {componentHarness,findNode,settle} from './component-harness.mjs';

// Structural regression for docs/chat-composer-reach-20261018.md: the question box
// stays pinned while everything else scrolls. Rendered-viewport acceptance stays a
// browser check; this guards the structure that makes it possible.
const source=await readFile(new URL('../app/assistant/workspace.tsx',import.meta.url),'utf8');
const css=(await readFile(new URL('../app/assistant/workspace.module.css',import.meta.url),'utf8')).replace(/\/\*[\s\S]*?\*\//g,'').replace(/\s*([{}:;,])\s*/g,'$1').replace(/\s+/g,' ').trim();
const investigation=await import('data:text/javascript;base64,'+Buffer.from(ts.transpileModule(await readFile(new URL('../app/assistant-investigation.ts',import.meta.url),'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64'));
const rule=selector=>{const match=css.match(new RegExp('(?:^|[}\\n])'+selector.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\{([^}]*)\\}'));assert.ok(match,'missing CSS rule '+selector);return match[1];};
const text=node=>[node?.props?.children].flat(Infinity).map(value=>typeof value==='string'?value:typeof value==='object'?text(value):'').join('');
const all=(node,predicate,found=[])=>{if(!node||typeof node!=='object')return found;if(predicate(node))found.push(node);for(const child of [node.props?.children].flat(Infinity))all(child,predicate,found);return found;};
const focus={title:'Synthetic county',detail:'Synthetic source context',context:{version:1,frame:2026,view:'2D',layers:[],selection:{kind:'knowledge',recordId:'synthetic-one'}}};

const ready=()=>Response.json({configured:true,online:true,ready:true,evidenceSearchAvailable:true,requiresLogin:false});
const children=node=>[node?.props?.children].flat(Infinity).flatMap(child=>child&&typeof child==='object'?(child.type==='fragment'?children(child):[child]):[]);
async function renderChat(fetch=async()=>ready(),props={focus,place:'Synthetic County'}){
 const classes=new Proxy({},{get:(_,key)=>key});
 const h=await componentHarness(new URL('../app/assistant/workspace.tsx',import.meta.url),{'./workspace.module.css':{default:classes},'../assistant-surfaces.mjs':surfaces,'../assistant-investigation':investigation},{fetch,Response,TextEncoder,crypto:{randomUUID},FormData:class {get(){return null;}},queueMicrotask,setInterval:()=>1,clearInterval:()=>{}});
 const render=(next=props)=>{const tree=h.render(h.exports.default,next);h.commit();return tree;};
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
 assert.match(rule('.optionsBody'),/max-height:min\(\d+d?vh,280px\)/);assert.match(rule('.optionsBody'),/overflow-y:auto/);
 assert.match(rule('.composer summary'),/min-height:44px/);assert.match(rule('.actions button'),/min-height:44px/);
 assert.match(css,/@media \(max-height:\d+px\)\{[^@]*\.composer textarea\{[^}]*min-height:44px/);
 assert.match(css,/\.chat button:focus-visible[^{]*\.chat summary:focus-visible[^{]*\.chat textarea:focus-visible[^{]*\{outline:3px solid var\(--chat-wheat\);outline-offset:3px/);
});

test('the pinned form holds answer options, the message box and Send; prompts and the footer live in the scroll region',async()=>{
 const {h,render}=await renderChat();
 try{
  let tree=render();
  const body=findNode(tree,node=>node.props?.className==='body'),form=findNode(tree,node=>node.type==='form'&&node.props.className==='composer');
  assert.ok(body,'scroll region renders');assert.ok(form,'composer form renders');
  assert.equal(findNode(body,node=>node.type==='form'),undefined,'the form is not inside the scroll region');
  for(const predicate of [node=>node.props?.className==='context',node=>node.props?.className==='guide',node=>node.props?.role==='log'&&node.props['aria-label']==='KFM chat conversation'&&node.props['aria-live']==='polite'&&node.props.tabIndex===0,node=>node.props?.['aria-label']==='Suggested questions',node=>node.type==='footer'])assert.ok(findNode(body,predicate));
  const regionOrder=children(body).map(child=>child.props.role==='log'?'log':child.props['aria-label']==='Suggested questions'?'prompts':child.type==='footer'?'footer':child.props.className);
  assert.deepEqual(regionOrder,['context','guide','log','prompts','footer']);
  assert.match(text(findNode(body,node=>node.type==='footer')),/History stays in this tab.*Temporary server questions expire after 15 minutes/);
  const prompts=all(findNode(body,node=>node.props?.['aria-label']==='Suggested questions'),node=>node.type==='button');
  assert.ok(prompts.length>0);for(const button of prompts){assert.equal(button.props.type,'button');assert.equal(button.props.disabled,false);}
  assert.equal(findNode(form,node=>node.props?.['aria-label']==='Suggested questions'),undefined,'prompts are no longer inside the form');

  const formOrder=[form.props.children].flat(Infinity).filter(child=>child&&typeof child==='object');
  assert.equal(formOrder.length,4);
  const [intent,options,messageLabel,actions]=formOrder;
  assert.equal(intent.props['aria-label'],'Composer mode');assert.ok(findNode(intent,node=>node.type==='button'&&text(node)==='Ask'));
  assert.equal(options.type,'details');assert.equal(options.props.className,'options');
  const summary=findNode(options,node=>node.type==='summary');assert.equal(text(summary),'Answer options · Ask');
  assert.ok(findNode(messageLabel,node=>node.type==='textarea'));
  assert.equal(actions.props.className,'actions');
  const submit=findNode(actions,node=>node.type==='button'&&node.props.type!=='button');assert.equal(text(submit),'Send');
  assert.match(text(findNode(actions,node=>node.type==='small')),/unverified discussion/);
  for(const name of ['mode','style','depth','term','place','start','end']){
   assert.ok(findNode(options,node=>node.props?.name===name),name+' stays inside the composer form');
   assert.equal(all(tree,node=>node.props?.name===name).length,1,name+' is rendered once');
  }
  assert.ok(findNode(options,node=>node.type==='details'&&text(findNode(node,child=>child.type==='summary'))==='Evidence search filters'));

  findNode(form,node=>node.type==='button'&&text(node)==='Evidence').props.onClick();
  tree=render();
  const evidenceForm=findNode(tree,node=>node.type==='form'&&node.props.className==='composer');
  assert.equal(text(findNode(evidenceForm,node=>node.type==='summary')),'Answer options · Find evidence');
  assert.ok(findNode(evidenceForm,node=>node.type==='button'&&text(node)==='Search'));
  assert.match(text(findNode(evidenceForm,node=>node.props?.className==='actions')),/Released records/);
 }finally{h.dispose();}
});

test('autoscroll decision: new questions always scroll; status and result changes scroll only a reader near the end',async()=>{
 const {h}=await renderChat();
 try{
  const decide=h.exports.shouldAutoscroll,turn=(id,state,hasResult=false)=>({id,state,hasResult});
  const cases=[
   ['no turns',null,null,true,false],
   ['turns cleared',turn('a','running'),null,true,false],
   ['first question',null,turn('a','preparing'),false,true],
   ['new question while scrolled up',turn('a','completed',true),turn('b','preparing'),false,true],
   ['new question after the ten-turn cap keeps the count unchanged',turn('j','completed',true),turn('k','preparing'),false,true],
   ['poll with no visible change while scrolled up',turn('a','running'),turn('a','running'),false,false],
   ['poll with no visible change near the end',turn('a','running'),turn('a','running'),true,false],
   ['recheck or export rebuilds the latest turn unchanged',turn('a','completed',true),turn('a','completed',true),true,false],
   ['state change near the end',turn('a','queued'),turn('a','running'),true,true],
   ['state change while scrolled up',turn('a','queued'),turn('a','running'),false,false],
   ['result arrives near the end',turn('a','running'),turn('a','completed',true),true,true],
   ['result arrives while scrolled up',turn('a','running'),turn('a','completed',true),false,false],
  ];
  for(const [label,previous,next,nearBottom,expected] of cases)assert.equal(decide(previous,next,nearBottom),expected,label);
 }finally{h.dispose();}
});

test('the effect scrolls the scroll region through the decision helper and tracks the reader position',()=>{
 assert.match(source,/<div ref=\{bodyRef\} className=\{styles\.body\} onScroll=\{\(\)=>\{if\(programmaticScrollRef\.current\)\{programmaticScrollRef\.current=false;return;\}nearBottomRef\.current=conversationEnd\(\)<=80;setAwayFromLatest\(!nearBottomRef\.current\);\}\}>/);
 const start=source.indexOf(' useEffect(()=>{\n  const latest=turns[turns.length-1]');assert.ok(start>=0,'autoscroll effect exists');
 const effect=source.slice(start,source.indexOf('},[turns]);',start)+11);
 assert.match(effect,/shouldAutoscroll\(previous,next,nearBottomRef\.current\)/);assert.match(effect,/body\.scrollTo\(/);assert.match(effect,/\},\[turns\]\);$/);
 assert.doesNotMatch(effect,/logRef\.current\?\.scrollTo/);
});

test('only an error from the visitor\'s own action scrolls to it, without being mistaken for the reader leaving the end',async()=>{
  const {h}=await renderChat();
  let revealsAlert;
  try{revealsAlert=h.exports.revealsAlert;}finally{h.dispose();}
  const background='Connection interrupted. Your accepted question is retained; checking again.';
  assert.equal(revealsAlert('',background),false,'no error');
  assert.equal(revealsAlert(background,background),false,'a background status-poll message stays in place');
  assert.equal(revealsAlert('Cancellation could not be confirmed.',background),true,'a failed visitor action is revealed');
  assert.equal(revealsAlert('Cancellation could not be confirmed.',''),true);
  assert.match(source,/useEffect\(\(\)=>\{const body=bodyRef\.current;if\(!body\|\|body\.scrollTop===0\|\|!revealsAlert\(error,backgroundErrorRef\.current\)\)return;programmaticScrollRef\.current=true;body\.scrollTo\(\{top:0,behavior:'auto'\}\);\},\[error\]\);/,'reveal only on error, never on the background chatFailure refresh');
  assert.match(source,/backgroundErrorRef\.current=message;setError\(message\)/,'status polling records its message as background');
  assert.match(source,/onScroll=\{\(\)=>\{if\(programmaticScrollRef\.current\)\{programmaticScrollRef\.current=false;return;\}nearBottomRef\.current=conversationEnd\(\)<=80;setAwayFromLatest\(!nearBottomRef\.current\);\}\}/,'the reveal scroll keeps the reader position for a later reply');
  assert.doesNotMatch(source,/\[error,chatFailure\]\)|\[exportNotice\]\)/);
  const notices=source.slice(source.indexOf('const notices=<>'),source.indexOf('</>;',source.indexOf('const notices=<>')));
  assert.ok(notices.indexOf("role='alert'")<notices.indexOf('chatStatus?.configured'),'alerts come before the standing model notice');
});

test('status notices and alerts render inside the scroll region, not above the pinned bar',async()=>{
 const inBody=(tree,predicate)=>{const body=findNode(tree,node=>node.props?.className==='body'),outside=children(tree).filter(node=>node.props?.className!=='body'&&node.type!=='form');return Boolean(findNode(body,predicate))&&!outside.some(node=>findNode(node,predicate));};
 const loading=await renderChat(async()=>Response.json({configured:true,online:false,ready:false,evidenceSearchAvailable:true,requiresLogin:false}));
 try{assert.ok(inBody(loading.render(),node=>node.props?.className==='notice'&&/Choose Find evidence/.test(text(node))));}finally{loading.h.dispose();}
 const offline=await renderChat(async()=>Response.json({reasonCode:'AI_UNAVAILABLE'},{status:503}));
 try{assert.ok(inBody(offline.render(),node=>node.props?.role==='alert'&&/Could not connect/.test(text(node))));}finally{offline.h.dispose();}
 const rejected=await renderChat(async(url,options)=>url.endsWith('/status')?ready():options.method==='POST'?Response.json({reasonCode:'USER_BUSY'},{status:429}):ready());
 try{
  let tree=rejected.render();findNode(tree,node=>node.type==='textarea').props.onChange({target:{value:'Explain this county.'}});tree=rejected.render();
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  tree=rejected.render();assert.ok(inBody(tree,node=>node.props?.role==='alert'&&/already have a question in progress/.test(text(node))));
  assert.equal(findNode(findNode(tree,node=>node.type==='form'&&node.props.className==='composer'),node=>node.props?.role==='alert'),undefined);
 }finally{rejected.h.dispose();}
});

test('the pinned action row states each mode\'s trust boundary without opening options',async()=>{
 const line=tree=>text(findNode(findNode(tree,node=>node.props?.className==='actions'),node=>node.type==='small'));
 const plain=await renderChat();
 try{
  let tree=plain.render();assert.match(line(tree),/^Qwen3 0.6B · unverified discussion/);assert.doesNotMatch(line(tree),/no account needed/);
  findNode(tree,node=>node.type==='button'&&text(node)==='Evidence').props.onClick();
  tree=plain.render();assert.match(line(tree),/^Released records · no model required · unsupported answers withheld/);
 }finally{plain.h.dispose();}
 const sample={...focus,context:{...focus.context,selection:{kind:'subsurface',tileId:'tile-160-255',recordId:'synthetic-core',intervalIndex:1}}};
 const source=await renderChat(async()=>ready(),{focus:sample,place:''});
 try{assert.match(line(source.render()),/^Source summary · no model required · not admitted evidence/);}finally{source.h.dispose();}
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
 assert.match(page,/className="qwen-panel atlas-chat-dock" role="dialog"[^>]*aria-labelledby="qwen-panel-title"/);assert.match(page,/<h2 id="qwen-panel-title">Chat with KFM<\/h2>/);
});
