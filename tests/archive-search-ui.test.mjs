import assert from 'node:assert/strict';
import test from 'node:test';
import { componentHarness, findNode, settle } from './component-harness.mjs';

const button=(tree,text)=>findNode(tree,n=>n.type==='button'&&n.props.children===text);
const status=tree=>findNode(tree,n=>n.props?.role==='status').props.children;
const resultTitle=tree=>findNode(tree,n=>n.props?.id==='archive-results-title');
const field=(tree,name)=>findNode(tree,n=>n.type==='label'&&n.props.children[0]===name).props.children[1];
function response(count=2,total=35,source='newspapers'){
 return {count,total,rows:Array.from({length:count},(_,id)=>({id:String(id),source,title:'Synthetic Gazette',snippet:'Synthetic OCR',issueDate:'1893-01-01'})),
  generatedAt:'2026-11-10T00:00:00Z',source:{notes:'Synthetic UI test only'},facets:{years:[{year:1893,hits:total}],titles:[{id:'sn12345678',title:'Synthetic Gazette',hits:total}]}};
}
async function fixture(search='',globals={}){
 const pending=[],calls=[];
 const h=await componentHarness('app/data-library/search.tsx',{
  '../archive-layer-data':{fetchArchive:(dataset,query,signal)=>{calls.push({dataset,query,signal});return new Promise((resolve,reject)=>pending.push({resolve,reject}));}},
  './library.module.css':{default:new Proxy({},{get:(_t,key)=>key})},
 },{location:{search},URLSearchParams,queueMicrotask,...globals});
 const dispose=h.dispose;h.dispose=()=>{dispose();for(const item of pending)item.resolve(response());};
 const render=()=>{const tree=h.render(h.exports.default,{});globals.mount?.(tree);h.commit();return tree;};
 let tree=render();await settle();tree=render();
 return {h,pending,calls,render,get tree(){return tree;},refresh(){tree=render();return tree;},
  change(name,value){field(tree,name).props.onChange({target:{value}});tree=render();},
  submit(){findNode(tree,n=>n.type==='form').props.onSubmit({preventDefault(){}});tree=render();},
  click(text){button(tree,text).props.onClick();tree=render();},
  async answer(value=response()){pending.shift().resolve(value);await settle();tree=render();},
  async fail(){pending.shift().reject(new Error('Synthetic archive outage'));await settle();tree=render();},
 };
}

test('draft edits do not relabel results, title facets or pagination',async()=>{
 const f=await fixture();try{
  f.change('Words or phrase','tornado');f.change('From year','1890');f.change('To year','1899');f.submit();await f.answer();
  f.change('Words or phrase','prairie');f.change('Collection','texts');f.change('From year','1895');
  assert.equal(f.calls.length,1,'drafts do not contact the provider');
  const title=resultTitle(f.tree).props.children.join('');assert.equal(title,'Results for “tornado”');
  assert.ok(findNode(f.tree,n=>n.type==='p'&&JSON.stringify(n.props.children??'').includes('Form changes have not been applied')));
  assert.ok(findNode(f.tree,n=>n.type==='p'&&JSON.stringify(n.props.children??'').includes('Counts are matching')&&n.props.children.includes('pages')));
  f.click('Next');assert.deepEqual({...f.calls.at(-1).query},{q:'tornado',source:'newspapers',facets:'1',limit:'20',offset:'2',from:'1890',to:'1899'});
  await f.answer();
  findNode(f.tree,n=>n.type==='button'&&n.props['aria-pressed']===false).props.onClick();f.refresh();
  assert.equal(f.calls.at(-1).query.q,'tornado');assert.equal(f.calls.at(-1).query.source,'newspapers');
  assert.equal(f.calls.at(-1).query.title,'sn12345678');assert.equal(f.calls.at(-1).query.offset,'0');await f.answer();
  f.submit();assert.equal(f.calls.at(-1).query.q,'prairie');assert.equal(f.calls.at(-1).query.source,'texts');assert.equal(f.calls.at(-1).query.title,undefined);await f.answer(response(1,1,'texts'));
 }finally{f.h.dispose();}
});

test('short pages advance by returned rows and Previous retraces actual page starts',async()=>{
 const f=await fixture();try{
  f.change('Words or phrase','tornado');f.submit();await f.answer(response(3));
  f.click('Next');assert.equal(f.calls.at(-1).query.offset,'3');await f.answer(response(2));
  f.click('Next');assert.equal(f.calls.at(-1).query.offset,'5');await f.answer(response(4));
  f.click('Previous');assert.equal(f.calls.at(-1).query.offset,'3');await f.answer(response(2));
  f.click('Previous');assert.equal(f.calls.at(-1).query.offset,'0');await f.answer(response(3));
  assert.equal(button(f.tree,'Previous').props.disabled,true);
 }finally{f.h.dispose();}
});

test('the first 1000 hits are a real boundary, including a one-row final page',async()=>{
 const f=await fixture();try{
  f.change('Words or phrase','tornado');f.submit();await f.answer(response(20,2000));
  while(Number(f.calls.at(-1).query.offset)<980){f.click('Next');await f.answer(response(20,2000));}
  f.click('Previous');await f.answer(response(19,2000));
  f.click('Next');assert.equal(f.calls.at(-1).query.offset,'979');await f.answer(response(20,2000));
  f.click('Next');assert.equal(f.calls.at(-1).query.offset,'999');assert.equal(f.calls.at(-1).query.limit,'1');
  await f.answer(response(1,2000));assert.equal(button(f.tree,'Next').props.disabled,true);assert.match(status(f.tree),/Showing 1,?000–1,?000/);
 }finally{f.h.dispose();}
});

test('year validation explains reversed ranges before any network request',async()=>{
 const f=await fixture();try{
  f.change('Words or phrase','tornado');f.change('From year','1900');f.change('To year','1890');f.submit();
  assert.equal(f.calls.length,0);assert.match(findNode(f.tree,n=>n.props?.role==='alert').props.children,/From year/);
  f.change('From year','18');f.submit();assert.equal(f.calls.length,0);assert.match(findNode(f.tree,n=>n.props?.role==='alert').props.children,/four digits/);
  f.change('From year','1890');f.submit();assert.equal(f.calls.length,1);await f.answer();assert.equal(findNode(f.tree,n=>n.props?.role==='alert'),undefined);
 }finally{f.h.dispose();}
});

test('Cancel releases the form, focuses the query, and rejects a late completion',async()=>{
 const f=await fixture();try{
  f.change('Words or phrase','tornado');f.submit();await f.answer();
  let focused=0;field(f.tree,'Words or phrase').props.ref.current={focus:()=>focused++};
  f.change('Words or phrase','prairie');f.submit();const signal=f.calls.at(-1).signal;
  f.click('Cancel search');assert.equal(signal.aborted,true);assert.equal(focused,1);assert.equal(button(f.tree,'Search').props.disabled,false);
  await f.answer(response(1,1,'texts'));assert.equal(resultTitle(f.tree).props.children.join(''),'Results for “tornado”');
  assert.match(status(f.tree),/cancelled/);assert.equal(button(f.tree,'Retry last search'),undefined);
 }finally{f.h.dispose();}
});

test('Retry uses the failed request rather than unsent form edits and retains prior results',async()=>{
 const f=await fixture();try{
  f.change('Words or phrase','tornado');f.submit();await f.answer();
  f.click('Next');const failed={...f.calls.at(-1).query};await f.fail();
  assert.ok(resultTitle(f.tree));assert.equal(button(f.tree,'Search').props.disabled,false);
  let focused=0;field(f.tree,'Words or phrase').props.ref.current={focus:()=>focused++};
  f.change('Words or phrase','prairie');f.change('Collection','texts');f.click('Retry last search');assert.equal(focused,1);assert.deepEqual({...f.calls.at(-1).query},failed);
  await f.answer();assert.equal(button(f.tree,'Retry last search'),undefined);
 }finally{f.h.dispose();}
});

test('newer searches and unmount discard obsolete responses',async()=>{
 const f=await fixture();
 f.change('Words or phrase','tornado');f.submit();f.change('Words or phrase','prairie');f.submit();
 assert.equal(f.calls[0].signal.aborted,true);
 f.pending[1].resolve(response(1,1));await settle();f.refresh();assert.equal(resultTitle(f.tree).props.children.join(''),'Results for “prairie”');
 f.pending[0].resolve(response(2,2));f.pending.splice(0,2);await settle();f.refresh();assert.equal(resultTitle(f.tree).props.children.join(''),'Results for “prairie”');
 f.submit();f.h.dispose();assert.equal(f.calls.at(-1).signal.aborted,true);await f.answer();
 assert.equal(button(f.tree,'Retry last search'),undefined);
});

test('deep links initialize the submitted query and zero-row pages never report an inverted range',async()=>{
 const f=await fixture('?q=prairie&source=texts&from=1890&to=1900');try{
  assert.equal(f.calls.length,1);assert.equal(f.calls[0].query.source,'texts');assert.equal(f.calls[0].query.from,'1890');
  await f.answer(response(0,0,'texts'));assert.match(status(f.tree),/No matches/);assert.equal(button(f.tree,'Next').props.disabled,true);
  f.submit();await f.answer(response(0,5,'texts'));assert.doesNotMatch(status(f.tree),/Showing 1–0/);assert.match(status(f.tree),/No further matches/);
 }finally{f.h.dispose();}
});

test('linked searches preserve valid newspaper and book titles and reject malformed title inputs',async()=>{
 const valid=await fixture('?q=railroad&source=newspapers&from=1900&to=1900&title=SN84029386');
 const foreign=await fixture('?q=railroad&source=texts&title=%00invalid');
 const book=await fixture('?q=prairie&source=texts&title=prairie_1900');
 const invalid=await fixture('?q=railroad&source=newspapers&title=unrecognized');
 try{
  assert.equal(valid.calls[0].query.title,'sn84029386');
  assert.equal(foreign.calls[0].query.title,undefined);
  assert.equal(book.calls[0].query.title,'prairie_1900');
  assert.equal(invalid.calls[0].query.title,undefined);
 }finally{valid.h.dispose();foreign.h.dispose();book.h.dispose();invalid.h.dispose();}
});

test('a response arriving after the timeout stays unapplied and can be retried',async()=>{
 let expire;
 const f=await fixture('',{setTimeout:callback=>{expire=callback;return 1;},clearTimeout(){}});
 try{
  f.change('Words or phrase','tornado');f.submit();expire();await f.answer();
  assert.equal(resultTitle(f.tree),undefined);assert.match(status(f.tree),/did not respond in time/);
  f.click('Retry last search');await f.answer();assert.ok(resultTitle(f.tree));
 }finally{f.h.dispose();}
});


test('only accepted search filters update a reloadable address while preserving collection browsing',async()=>{
 const location={search:'?find=climate&mapped=1',hash:''},writes=[],history={state:{retained:'router'},replaceState(state,_title,url){writes.push({state,url});const u=new URL(url,'https://example.test');location.search=u.search;location.hash=u.hash;}};
 const f=await fixture('',{location,history});try{
  f.change('Words or phrase','dust storm');f.change('From year','1900');f.change('To year','1920');f.submit();
  assert.equal(writes.length,0,'pending searches do not change the reload target');await f.answer();
  const link=new URL(writes.at(-1).url,'https://example.test');
  assert.equal(link.hash,'#archive-text-search');assert.equal(link.searchParams.get('q'),'dust storm');assert.equal(link.searchParams.get('from'),'1900');assert.equal(link.searchParams.get('to'),'1920');
  assert.equal(link.searchParams.get('find'),'climate');assert.equal(link.searchParams.get('mapped'),'1');assert.equal(writes.at(-1).state,history.state);
  f.change('Words or phrase','prairie');assert.equal(writes.length,1,'drafts do not replace the accepted query');
  f.submit();await f.fail();assert.equal(writes.length,1,'failures retain the accepted address');
  f.submit();f.click('Cancel search');await f.answer();assert.equal(writes.length,1,'cancelled late responses cannot rewrite history');
 }finally{f.h.dispose();}
});

function focusFixture(){
 const events=[],body={},outside={},document={body,activeElement:body};
 const result={focus(){events.push('results focus');document.activeElement=result;},scrollIntoView(){events.push('results scroll');}};
 const heading={focus(){events.push('search focus');document.activeElement=heading;},scrollIntoView(){events.push('search scroll');}};
 return {events,document,outside,globals:{document,mount(tree){
  const section=findNode(tree,n=>n.type==='section'&&n.props['aria-labelledby']==='archive-search-title');if(section.props.ref)section.props.ref.current={contains:active=>active!==outside};
  const title=findNode(tree,n=>n.props?.id==='archive-search-title');if(title.props.ref)title.props.ref.current=heading;
  const results=resultTitle(tree);if(results?.props.ref)results.props.ref.current=result;
 }}};
}

test('successful page navigation exposes the new results; failed and cancelled work does not move focus',async()=>{
 const focus=focusFixture(),f=await fixture('',focus.globals);try{
  f.change('Words or phrase','tornado');f.submit();await f.answer();
  assert.deepEqual(focus.events,['results focus','results scroll']);assert.equal(resultTitle(f.tree).props.tabIndex,-1);
  f.click('Next');assert.equal(focus.events.length,2);await f.answer();assert.equal(focus.events.length,4);
  f.click('Next');await f.fail();assert.equal(focus.events.length,4);
  f.submit();f.click('Cancel search');await f.answer();assert.equal(focus.events.length,4);
  f.submit();focus.document.activeElement=focus.outside;await f.answer();assert.equal(focus.events.length,4,'a reader who moved elsewhere keeps focus');
 }finally{f.h.dispose();}
});

test('a linked search exposes its form on arrival without a later background focus jump',async()=>{
 const focus=focusFixture(),f=await fixture('?q=prairie&source=texts',focus.globals);try{
  assert.deepEqual(focus.events,['search focus','search scroll']);await f.answer();assert.equal(focus.events.length,2);
 }finally{f.h.dispose();}
 const collectionFocus=focusFixture(),c=await fixture('?q=prairie&collection=bulk-newspaper-pages',collectionFocus.globals);try{
  assert.deepEqual(collectionFocus.events,[],'an explicit collection deep link remains the destination');
 }finally{c.h.dispose();}
});


test('reusable search links retain the accepted title and safely encode the query',async()=>{
 const f=await fixture();try{
  const query={q:'prairie & "Kansas"',source:'texts',from:'1890',to:'1900',title:'prairie_1900'};
  const u=new URL(f.h.exports.archiveSearchLocation('?find=climate&title=old',query),'https://example.test');
  assert.equal(u.pathname,'/data-library');assert.equal(u.hash,'#archive-text-search');
  for(const [key,value] of Object.entries(query))assert.equal(u.searchParams.get(key),value);
  assert.equal(u.searchParams.get('find'),'climate');
 }finally{f.h.dispose();}
});
