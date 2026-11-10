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
 },{location:{search},URLSearchParams,...globals});
 const dispose=h.dispose;h.dispose=()=>{dispose();for(const item of pending)item.resolve(response());};
 const render=()=>{const tree=h.render(h.exports.default,{});h.commit();return tree;};
 let tree=render();
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

test('a response arriving after the timeout stays unapplied and can be retried',async()=>{
 let expire;
 const f=await fixture('',{setTimeout:callback=>{expire=callback;return 1;},clearTimeout(){}});
 try{
  f.change('Words or phrase','tornado');f.submit();expire();await f.answer();
  assert.equal(resultTitle(f.tree),undefined);assert.match(status(f.tree),/did not respond in time/);
  f.click('Retry last search');await f.answer();assert.ok(resultTitle(f.tree));
 }finally{f.h.dispose();}
});
