import assert from 'node:assert/strict';
import test from 'node:test';
import { modelUrl } from '../scripts/lib/typescript-model.mjs';
import { componentHarness, findNode, settle } from './component-harness.mjs';

const model=await import(await modelUrl('app/data-library/collection-browser.ts'));
const library=await import(await modelUrl('app/recovered-collections.ts'));
const collections=library.RECOVERED_COLLECTIONS;
const css={default:new Proxy({},{get:(_target,key)=>String(key)})};
const button=(tree,label)=>findNode(tree,n=>n.type==='button'&&n.props.children===label);
const input=tree=>findNode(tree,n=>n.type==='input'&&n.props.type==='search');
const heading=tree=>findNode(tree,n=>n.type==='h2'&&n.props.ref&&n.props.className==='heading');
const card=(tree,id)=>findNode(tree,n=>n.type==='button'&&findNode(n,c=>c.type==='strong'&&c.props.children===library.recoveredCollection(id).title));
const firstMapped=collections.find(c=>c.geometry),firstReference=collections.find(c=>!c.geometry);
const answer={dataset:'recovered-observations',total:null,count:1,rows:[{id:'synthetic-row',values:{name:'Synthetic record'}}],hasMore:false,nextCursor:null,generatedAt:'2026-11-10T00:00:00Z',source:{notes:'Synthetic UI fixture only'}};

test('collection search matches catalog names, source families and fields in any word order',()=>{
 const ids=rows=>rows.map(c=>c.id);
 const a=ids(model.matchingCollections(collections,'KGS API number'));
 assert.ok(a.includes('observations-kgs-wells'));
 assert.deepEqual(ids(model.matchingCollections(collections,'number API KGS')),a);
 assert.deepEqual(ids(model.matchingCollections(collections,'WÉLLS kgs')),ids(model.matchingCollections(collections,'kgs wells')));
 assert.equal(model.matchingCollections(collections,'zzzz_nonexistent_collection').length,0);
});

test('map filtering uses catalog geometry without changing source identity or order',()=>{
 assert.deepEqual(model.matchingCollections(collections,'',true),collections.filter(c=>c.geometry));
 assert.equal(model.matchingCollections(collections,'')[0],collections[0]);
 assert.equal(model.matchingCollections(collections,'wells',true).length,0,'the stored well tables do not claim geometry');
});

test('collection URLs preserve text search, years, anchors and unrelated parameters',()=>{
 const url=new URL(model.collectionLocation('?q=dust+storm&source=texts&from=1890&to=1900&other=retained&find=old','#records','observations-kgs-wells',' KGS API number ',true),'https://example.test');
 assert.deepEqual(Object.fromEntries(url.searchParams),{q:'dust storm',source:'texts',from:'1890',to:'1900',other:'retained',find:'KGS API number',collection:'observations-kgs-wells',mapped:'1'});
 assert.equal(url.hash,'#records');assert.equal(url.pathname,'/data-library');
 const cleared=new URL(model.collectionLocation(url.search,url.hash,'observations-kgs-wells','',false),'https://example.test');
 assert.equal(cleared.searchParams.has('find'),false);assert.equal(cleared.searchParams.has('mapped'),false);assert.equal(cleared.searchParams.get('q'),'dust storm');
 assert.equal(new URL(model.collectionLocation('?q=tornado','','','name',false),'https://example.test').searchParams.has('collection'),false);
});

async function fixture({search='',hash='#collections',historyFails=false}={}){
 const calls=[],pending=[],focus=[],updates=[],startup=[],recordTimers=[],location={search,hash};
 const history={state:{router:'retained'},replaceState(state,_unused,url){
  if(historyFails)throw new Error('History unavailable');
  updates.push({state,url});const parsed=new URL(url,'https://example.test');location.search=parsed.search;location.hash=parsed.hash;
 }};
 const h=await componentHarness('app/data-library/page.tsx',{
  'next/link':{default:'a'},'../recovered-collections':library,
  '../archive-layer-data':{fetchArchive:(dataset,query,signal)=>{calls.push({dataset,query,signal});return new Promise(resolve=>pending.push(resolve));},rowLabel:row=>row.values.name,textValue:String},
  './search':{default:'archive-search'},'./freshness':{fetchCatalogFreshness:async()=>null,loadedThrough:()=>null,freshnessLine:()=>''},
  './collection-browser':model,'./library.module.css':css,'./collection-browser.module.css':css,
 },{URLSearchParams,location,history,setTimeout:(fn,ms)=>ms===0?(startup.push(fn),0):ms===25000?(recordTimers.push(fn),{recordTimer:true}):setTimeout(fn,ms),clearTimeout:token=>{if(!token?.recordTimer)clearTimeout(token);}});
 const dispose=h.dispose;h.dispose=()=>{dispose();for(const resolve of pending)resolve(answer);};
 const render=()=>{
  const tree=h.render(h.exports.default,{});
  input(tree).props.ref.current={focus:()=>focus.push('finder')};
  const title=heading(tree);if(title)title.props.ref.current={focus:()=>focus.push(title.props.children),scrollIntoView(){}};
  findNode(tree,n=>n.props?.id==='archive-comparison-heading').props.ref.current={focus:()=>focus.push('comparison')};
  h.commit();return tree;
 };
 let tree=render();startup.shift()();tree=render();await settle();tree=render();
 return {h,focus,updates,history,location,calls,pending,expireRecord(){recordTimers.shift()();},get tree(){return tree;},refresh(){tree=render();},
  change(value){input(tree).props.onChange({target:{value}});tree=render();},
  mapped(checked){findNode(tree,n=>n.type==='input'&&n.props.type==='checkbox').props.onChange({target:{checked}});tree=render();},
  choose(id){card(tree,id).props.onClick();tree=render();},
  click(label){button(tree,label).props.onClick();tree=render();},
  async answer(value=answer){pending.shift()(value);await settle();tree=render();},
 };
}

test('choosing a collection focuses its committed heading and preserves history state and search context',async()=>{
 const f=await fixture({search:'?q=tornado&source=texts&from=1890&to=1900'});try{
  f.change('KGS API number');f.choose('observations-kgs-wells');
  assert.equal(heading(f.tree).props.children,'KGS Wells');assert.equal(f.focus.at(-1),'KGS Wells');
  assert.equal(f.updates.at(-1).state,f.history.state);const params=new URLSearchParams(f.location.search);
  assert.equal(params.get('q'),'tornado');assert.equal(params.get('source'),'texts');assert.equal(params.get('from'),'1890');assert.equal(params.get('to'),'1900');assert.equal(params.get('find'),'KGS API number');assert.equal(f.location.hash,'#collections');
  assert.equal(f.calls.length,0,'choosing metadata does not read source records');
  f.click('Back to collection finder');assert.equal(f.focus.at(-1),'finder');
  f.choose('observations-kgs-wells');assert.equal(f.focus.at(-1),'KGS Wells','choosing the same collection again still owns focus');
 }finally{f.h.dispose();}
});

test('empty filters recover without clearing the chosen collection or its map selection',async()=>{
 const f=await fixture();try{
  f.choose(firstMapped.id);f.click('Add to map selection');
  f.change('zzzz_nonexistent_collection');assert.ok(findNode(f.tree,n=>n.type==='strong'&&n.props.children==='No matching collections'));
  assert.equal(heading(f.tree).props.children,firstMapped.title);
  f.mapped(true);f.click('Show all collections');
  assert.equal(input(f.tree).props.value,'');assert.equal(f.focus.at(-1),'finder');assert.equal(heading(f.tree).props.children,firstMapped.title);
  assert.ok(button(f.tree,'Remove from map selection'));
  assert.equal(findNode(f.tree,n=>n.type==='input'&&n.props.type==='checkbox').props.checked,false);
  assert.equal(f.calls.length,0);assert.equal(new URLSearchParams(f.location.search).has('find'),false);
 }finally{f.h.dispose();}
});

test('geometry filtering and clearing are bookmarkable and leave focus in the finder',async()=>{
 const f=await fixture();try{
  f.mapped(true);assert.equal(new URLSearchParams(f.location.search).get('mapped'),'1');assert.equal(f.focus.length,0);
  findNode(f.tree,n=>n.type==='button'&&n.props['aria-label']==='Clear collection filters').props.onClick();f.refresh();
  assert.equal(new URLSearchParams(f.location.search).has('mapped'),false);assert.equal(f.focus.at(-1),'finder');assert.equal(f.calls.length,0);
 }finally{f.h.dispose();}
});

test('deep links restore collection and filters without stealing focus or reading records',async()=>{
 const f=await fixture({search:`?collection=${firstMapped.id}&find=wells&mapped=1`});try{
  assert.equal(heading(f.tree).props.children,firstMapped.title);assert.equal(input(f.tree).props.value,'wells');assert.equal(f.focus.length,0);assert.equal(f.calls.length,0);
  assert.equal(findNode(f.tree,n=>n.type==='input'&&n.props.type==='checkbox').props.checked,true);
  assert.ok(findNode(f.tree,n=>n.type==='strong'&&n.props.children==='No matching collections'));
 }finally{f.h.dispose();}
});

test('history failures cannot block a deliberate collection choice',async()=>{
 const f=await fixture({historyFails:true});try{
  f.choose(firstReference.id);assert.equal(heading(f.tree).props.children,firstReference.title);assert.equal(f.focus.at(-1),firstReference.title);assert.equal(f.calls.length,0);
 }finally{f.h.dispose();}
});

test('filtering and record completion do not steal focus, and changing collections rejects late rows',async()=>{
 const f=await fixture();try{
  f.choose(firstReference.id);f.click('Read first page');
  f.choose(firstMapped.id);assert.equal(f.calls[0].signal.aborted,true);const focused=f.focus.length;
  await f.answer();assert.equal(findNode(f.tree,n=>n.type==='button'&&n.props.children==='Download this page · JSON'),undefined);
  f.change('');assert.equal(f.focus.length,focused);
  f.click('Read first page');await f.answer();assert.equal(f.focus.length,focused);assert.ok(button(f.tree,'Download this page · JSON'));
 }finally{f.h.dispose();}
});


test('unmount invalidates a late collection response even when transport ignores abort',async()=>{
 const f=await fixture();try{
  f.choose(firstReference.id);f.click('Read first page');
  const finish=f.pending.shift();f.h.dispose();
  assert.equal(f.calls[0].signal.aborted,true);
  finish(answer);await settle();f.refresh();
  assert.equal(button(f.tree,'Download this page · JSON'),undefined,'a disposed reader cannot retain a late downloadable page');
 }finally{f.h.dispose();}
});

test('a timed-out collection response cannot become a page and an explicit retry still works',async()=>{
 const f=await fixture();try{
  f.choose(firstReference.id);f.click('Read first page');
  f.expireRecord();assert.equal(f.calls[0].signal.aborted,true);
  await f.answer();
  assert.equal(button(f.tree,'Download this page · JSON'),undefined,'abort is a refusal boundary even if transport resolves');
  assert.ok(findNode(f.tree,n=>n.props?.role==='status'&&n.props.children==='The archive did not respond in time. Retry when the PC is available.'));
  assert.equal(button(f.tree,'Read first page').props.disabled,false);
  f.click('Read first page');assert.equal(f.calls[1].signal.aborted,false);
  await f.answer();assert.ok(button(f.tree,'Download this page · JSON'),'a new explicit request can still succeed');
 }finally{f.h.dispose();}
});

async function fieldFixture(){
 const calls=[],pending=[],timers=[];
 const h=await componentHarness('app/data-library/page.tsx',{
  'next/link':{default:'a'},'../recovered-collections':library,
  '../archive-layer-data':{fetchArchive:(dataset,query,signal)=>{calls.push({dataset,query,signal});return new Promise((resolve,reject)=>pending.push({resolve,reject}));},rowLabel:()=>'',textValue:String},
  './search':{default:'archive-search'},'./freshness':{},'./collection-browser':model,'./library.module.css':css,'./collection-browser.module.css':css,
 },{setTimeout:(fn,ms)=>{assert.equal(ms,25000);const timer={fn,cleared:false};timers.push(timer);return timer;},clearTimeout:timer=>{timer.cleared=true;}},'\nexport {RecordField};');
 const props={value:{longField:true,preview:'Recorded preview'},id:'bulk-newspaper-pages',database:'bulk',record:'synthetic-1',field:'text'};
 let tree;
 function render(){tree=h.render(h.exports.RecordField,props);h.commit();}
 render();
 return {h,calls,pending,get tree(){return tree;},refresh:render,
  click(label){button(tree,label).props.onClick();render();},
  expire(){timers.find(timer=>!timer.cleared).fn();render();},
  async finish(index,result){pending[index].resolve(result);await settle();render();},
  async fail(index){pending[index].reject(new Error('synthetic failure'));await settle();render();},
 };
}
const fieldAnswer=(start=0,text='First retained part',nextStart=32768)=>({...answer,rows:[{id:'synthetic-1',values:{text}}],fieldChunk:{field:'text',start,characters:40000,nextStart}});

test('long-field timeout releases retry before transport settles and refuses its late result',async()=>{
 const f=await fieldFixture();try{
  f.click('Open full field');f.expire();
  assert.equal(f.calls[0].signal.aborted,true);
  assert.equal(button(f.tree,'Open full field').props.disabled,false,'timeout must release the reader even if transport never settles');
  assert.ok(findNode(f.tree,n=>n.props?.role==='status'&&/timed out.*Retry/i.test(n.props.children)));
  f.click('Open full field');await f.finish(1,fieldAnswer(0,'Current retry'));
  await f.finish(0,fieldAnswer(0,'Expired result'));
  assert.equal(findNode(f.tree,n=>n.type==='pre').props.children,'Current retry');
 }finally{f.h.dispose();}
});

test('disposed long-field reader ignores late failures as well as late values',async()=>{
 const f=await fieldFixture();try{
  f.click('Open full field');f.h.dispose();
  assert.equal(f.calls[0].signal.aborted,true);
  await f.fail(0);
  assert.equal(findNode(f.tree,n=>n.props?.role==='status').props.children,'Loading field…','no state update belongs to an unmounted reader');
 }finally{f.h.dispose();}
});

test('long-field paging retains its last part on failure and retries the same source offset',async()=>{
 const f=await fieldFixture();try{
  f.click('Open full field');await f.finish(0,fieldAnswer());
  f.click('Next part');await f.fail(1);
  assert.equal(findNode(f.tree,n=>n.type==='pre').props.children,'First retained part');
  assert.ok(findNode(f.tree,n=>n.props?.role==='status'&&n.props.children==='Field unavailable. Retry.'));
  f.click('Next part');await f.finish(2,fieldAnswer(32768,'Last retained part',null));
  assert.deepEqual(f.calls.map(c=>({...c.query})),[
   {collection:'bulk-newspaper-pages',record:'synthetic-1',field:'text',start:'0'},
   {collection:'bulk-newspaper-pages',record:'synthetic-1',field:'text',start:'32768'},
   {collection:'bulk-newspaper-pages',record:'synthetic-1',field:'text',start:'32768'},
  ]);
  assert.ok(f.calls.every(c=>c.dataset==='recovered-bulk'));
  assert.equal(findNode(f.tree,n=>n.type==='pre').props.children,'Last retained part');
  assert.equal(button(f.tree,'Next part'),undefined);
 }finally{f.h.dispose();}
});

const comparisonCollection=library.recoveredCollection('observations-kgs-wells');
function comparisonAnswer(row={id:'same-id',values:{name:'Synthetic well',depth:0},provenance:{receipt:'synthetic'}}){
 return {...answer,collection:comparisonCollection.id,rows:[row],source:{provider:'Synthetic source',notes:'Test only',coverage:'One record'},cache:{state:'stale',at:'2026-11-09T00:00:00Z'}};
}
test('comparison copies source-bound records and keeps the original pinned edition',()=>{
 const a=comparisonAnswer(),original=structuredClone(a.rows[0]);
 const pinned=model.pinComparison([],comparisonCollection,a.rows[0],a);
 a.rows[0].values.depth=12;a.source.notes='Changed';
 assert.deepEqual(pinned[0].row,original);assert.equal(pinned[0].source.notes,'Test only');
 assert.equal(pinned[0].retrievedAt,answer.generatedAt);assert.equal(pinned[0].cache.state,'stale');
 const repeat=model.pinComparison(pinned,comparisonCollection,a.rows[0],a);
 assert.equal(repeat.length,1);assert.equal(repeat[0].row.values.depth,0,'rereading does not silently replace a pinned edition');
 const other={...comparisonCollection,id:'other-source',title:'Other source'};
 const two=model.pinComparison(pinned,other,a.rows[0],{...a,collection:other.id});
 assert.equal(two.length,2,'identical row ids from different collections stay distinct');
 const exported=model.comparisonExport(two);
 assert.equal(exported.status,'personal-comparison-not-a-release');
 assert.deepEqual(JSON.parse(JSON.stringify(exported)).records[0],pinned[0]);
});
test('comparison refuses detached records, mismatched sources, missing identity and bounded-capacity overflow without evicting',()=>{
 const a=comparisonAnswer();
 assert.throws(()=>model.pinComparison([],comparisonCollection,{...a.rows[0]},a),/tied/);
 for(const change of [{dataset:'other'},{collection:'other'}])assert.throws(()=>model.pinComparison([],comparisonCollection,a.rows[0],{...a,...change}),/tied/);
 const missing=comparisonAnswer({values:{depth:1}});assert.throws(()=>model.pinComparison([],comparisonCollection,missing.rows[0],missing),/tied/);
 let pins=[];for(let i=0;i<4;i++){const next=comparisonAnswer({id:String(i),values:{depth:i}});pins=model.pinComparison(pins,comparisonCollection,next.rows[0],next);}
 const fifth=comparisonAnswer({id:'fifth',values:{depth:5}});assert.throws(()=>model.pinComparison(pins,comparisonCollection,fifth.rows[0],fifth),/four records/);assert.equal(pins.length,4);
 const large=comparisonAnswer({id:'large',values:{text:'🌻'.repeat(17000)}});assert.throws(()=>model.pinComparison([],comparisonCollection,large.rows[0],large),/64 KiB/);
 const many=comparisonAnswer({id:'many',values:Object.fromEntries(Array.from({length:201},(_,i)=>['field'+i,i]))});assert.throws(()=>model.pinComparison([],comparisonCollection,many.rows[0],many),/200-field/);
});
test('comparison distinguishes missing, null, zero, false, blank and preview values without conversions or prototype lookup',()=>{
 const row=JSON.parse('{"id":"typed","values":{"zero":0,"null":null,"false":false,"blank":"","units":"ft","date":"1900-01-02","__proto__":"original field","long":{"longField":true,"preview":"excerpt"}}}');
 const a=comparisonAnswer(row),[pin]=model.pinComparison([],comparisonCollection,row,a);
 assert.deepEqual(model.comparisonFields([pin]),Object.keys(row.values));
 for(const [field,expected]of Object.entries({zero:'0',null:'Not supplied (null)',false:'false',blank:'Empty text',absent:'Field absent',toString:'Field absent',units:'ft',date:'1900-01-02',long:'Preview only: excerpt'}))assert.equal(model.comparisonValue(pin,field),expected);
 assert.equal(model.comparisonValue(pin,'__proto__'),'original field');
 assert.deepEqual(pin.row.values.long,row.values.long);
});
test('comparison stays across collection changes, requires explicit pinning, preserves map choices and restores focus on removal',async()=>{
 const f=await fixture();try{
  f.choose(comparisonCollection.id);f.click('Read first page');await f.answer(comparisonAnswer());
  assert.equal(findNode(f.tree,n=>n.type==='table'),undefined);
  f.click('Pin for comparison');assert.ok(findNode(f.tree,n=>n.type==='table'));
  assert.ok(button(f.tree,'Unpin from comparison'));assert.equal(f.calls.length,1,'pinning does not fetch');
  f.choose(firstMapped.id);f.click('Add to map selection');
  assert.ok(findNode(f.tree,n=>n.type==='table'));assert.ok(button(f.tree,'Remove from map selection'));
  const remove=findNode(f.tree,n=>n.type==='button'&&n.props['aria-label']?.startsWith('Remove KGS Wells record'));
  remove.props.onClick();f.refresh();assert.equal(f.focus.at(-1),'comparison');
  assert.equal(findNode(f.tree,n=>n.type==='table'),undefined);assert.ok(button(f.tree,'Remove from map selection'));assert.equal(f.calls.length,1);
 }finally{f.h.dispose();}
});
test('unpinning and clearing affect only comparison memory, not the current response or original data',async()=>{
 const f=await fixture();try{
  const a=comparisonAnswer(),before=structuredClone(a);f.choose(comparisonCollection.id);f.click('Read first page');await f.answer(a);
  f.click('Pin for comparison');f.click('Unpin from comparison');assert.equal(findNode(f.tree,n=>n.type==='table'),undefined);
  f.click('Pin for comparison');f.click('Clear comparison');assert.equal(f.focus.at(-1),'comparison');
  assert.ok(button(f.tree,'Download this page · JSON'));assert.ok(button(f.tree,'Pin for comparison'));assert.deepEqual(a,before);
 }finally{f.h.dispose();}
});
