import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createServer } from 'node:http';
import test from 'node:test';
import ts from 'typescript';
import { componentHarness, settle } from './component-harness.mjs';

// Execute the real interval callback and primary-button JSX, with controlled
// transport/storage and clocks. This does not establish browser/provider proof.
const source=await readFile('app/observatory/workspace.tsx','utf8');
const ast=ts.createSourceFile('workspace.tsx',source,ts.ScriptTarget.Latest,true,ts.ScriptKind.TSX);
let callback,primary;
function visit(node){
  if(ts.isVariableDeclaration(node)&&node.name.getText(ast)==='load')callback=node.initializer.arguments[0].getText(ast);
  if(ts.isJsxElement(node)&&node.openingElement.tagName.getText(ast)==='button'&&node.getText(ast).includes('Load exact interval'))primary=node.getText(ast);
  ts.forEachChild(node,visit);
}visit(ast);assert.ok(callback);assert.ok(primary);
function evaluate(expression,bindings){
  bindings={exports:{},...bindings};
  const code=ts.transpileModule(`const result=(${expression});`,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022,jsx:ts.JsxEmit.ReactJSX}}).outputText;
  return new Function(...Object.keys(bindings),code+'return result;')(...Object.values(bindings));
}
const deferred=()=>{let resolve;const promise=new Promise(done=>{resolve=done;});return{promise,resolve};};
const A='1900-05-19T00:00',B='1900-05-20T00:00';
const manifest=(start=A)=>({format:'kfm-event-atlas-v1',start:start+':00.000Z',end:new Date(Date.parse(start+':00Z')+86400000).toISOString(),radar:{scans:[],gaps:[]},smoke:{gaps:[]}});
const flush=async()=>{await settle();await settle();};
async function harness(dispatch,options={}){
  const timers=new Map(),requests=[];let timerId=0;
  const clocks={setTimeout:(fn,delay)=>{const id=++timerId;timers.set(id,{fn,delay});return id;},clearTimeout:id=>timers.delete(id)};
  const {replayRead}=(await componentHarness('app/observatory/load-deadline.ts',{},{Error,...clocks})).exports;
  const state={loading:false,error:'',manifest:null,river:null,calendarLedger:{},radarDownloadStatus:''};
  const generation={current:0},requestRef={current:null};
  const set=key=>value=>{state[key]=typeof value==='function'?value(state[key]):value;};
  const bindings={replayRead,start:A,hours:24,station:options.station??'',riverResolution:'continuous',radarReplayMode:options.radarReplayMode??false,EVENT_MAX_HOURS:24,
    followTodayRef:{current:false},generation,frameGeneration:{current:0},radarDownloadRef:{current:null},requestRef,frameRequest:{current:null},sourceFailures:{current:new Set()},radarSourceTime:{current:null},mapRef:{current:null},urls:{current:new Map()},
    AbortController,URL,URLSearchParams,window:{location:{search:''}},hideEventLayers(){},
    fetch:(url,init)=>{requests.push({url,signal:init.signal});return dispatch(url,init);},
    readRadarIndex:options.readRadarIndex??(()=>Promise.resolve(null)),radarManifestFromCache:options.radarManifestFromCache??(()=>null),
    parseStreamflowBundle:body=>body,eventFrames:data=>[data.start],radarReplayFrames:data=>[data.start],eventHourAvailability:()=>[],
  };
  for(const key of ['followToday','calendarLedger','inspectedFeature','stormFrame','stormAvailability','playing','loading','error','committed','manifest','river','index','cursor','sourceErrors','radarDownloadStatus','loadedRiverResolution','riverMessage'])bindings['set'+key[0].toUpperCase()+key.slice(1)]=set(key);
  const load=evaluate(callback,bindings);
  const button=()=>evaluate(primary,{...state,mapReady:true,require:()=>({jsx:(type,props)=>({type,props})})});
  return{state,requests,timers,load,requestRef,button,expire(){const timer=timers.values().next().value;assert.ok(timer,'actual interval load must install a finite read deadline');assert.ok([15000,30000].includes(timer.delay));timer.fn();}};
}

for(const stage of ['headers','body'])test(`stalled manifest ${stage} restores interval retry, marks unknown coverage failed and rejects late success`,async()=>{
  const slow=deferred();let calls=0;
  const h=await harness(()=>++calls===1?(stage==='headers'?slow.promise:Promise.resolve({ok:true,json:()=>slow.promise})):Promise.resolve(Response.json(manifest())));
  const pending=h.load();await flush();assert.equal(h.button().props.disabled,true);assert.equal(h.state.calendarLedger['1900-05-19'].status,'checking');
  h.expire();await pending;assert.equal(h.requests[0].signal.aborted,true);assert.equal(h.state.loading,false);assert.equal(h.button().props.disabled,false);assert.match(h.state.error,/took too long/);assert.equal(h.state.manifest,null);assert.equal(h.state.calendarLedger['1900-05-19'].status,'failed');assert.equal(h.timers.size,0);
  const retry=h.load();await retry;assert.equal(h.state.manifest.start,manifest().start);assert.equal(h.state.error,'');
  slow.resolve(stage==='headers'?Response.json(manifest(B)):manifest(B));await flush();assert.equal(h.state.manifest.start,manifest().start);assert.equal(h.timers.size,0);
});

for(const stage of ['headers','body'])test(`optional station ${stage} timeout keeps a loaded manifest without claiming empty river coverage`,async()=>{
  const slow=deferred();
  const h=await harness(url=>url.includes('/manifest?')?Promise.resolve(Response.json(manifest())):stage==='headers'?slow.promise:Promise.resolve({ok:true,json:()=>slow.promise}),{station:'USGS-06889000'});
  const pending=h.load();await flush();assert.equal(h.requests.length,2);h.expire();await pending;
  assert.equal(h.state.loading,false);assert.equal(h.state.manifest.start,manifest().start);assert.equal(h.state.river,null);assert.match(h.state.riverMessage,/took too long/);assert.doesNotMatch(h.state.riverMessage,/No observations/);assert.equal(h.state.calendarLedger['1900-05-19'].status,'partial');assert.equal(h.requests[1].signal.aborted,true);assert.equal(h.timers.size,0);
  slow.resolve(stage==='headers'?Response.json({observations:[{value:99}]}):{observations:[{value:99}]});await flush();assert.equal(h.state.river,null);
});

test('manifest timeout retains exact local radar fallback; stalled storage ends loading and cannot publish late status',async()=>{
  for(const stalled of [false,true]){
    const saved=deferred();
    const h=await harness(()=>new Promise(()=>{}),{radarReplayMode:true,readRadarIndex:()=>stalled?saved.promise:Promise.resolve({fixture:true}),radarManifestFromCache:()=>manifest()});
    const pending=h.load();await flush();h.expire();await flush();
    if(stalled){h.expire();await pending;assert.equal(h.state.manifest,null);assert.match(h.state.error,/saved radar.*took too long/i);saved.resolve({fixture:true});await flush();assert.equal(h.state.radarDownloadStatus,'');}
    else{await pending;assert.equal(h.state.manifest.start,manifest().start);assert.match(h.state.radarDownloadStatus,/Other sources were not checked/);}
    assert.equal(h.state.loading,false);assert.equal(h.timers.size,0);
  }
});

test('new interval cancels old reads without letting late completion or deadline clear its busy state',async()=>{
  const old=deferred(),next=deferred();let calls=0;
  const h=await harness(()=>++calls===1?old.promise:next.promise);
  const first=h.load();await flush();const second=h.load(B);await flush();await first;
  assert.equal(h.requests[0].signal.aborted,true);assert.equal(h.state.loading,true);assert.equal(h.timers.size,1);
  old.resolve(Response.json(manifest()));await flush();assert.equal(h.state.manifest,null);assert.equal(h.state.loading,true);
  next.resolve(Response.json(manifest(B)));await second;assert.equal(h.state.manifest.start,manifest(B).start);assert.equal(h.state.loading,false);assert.equal(h.timers.size,0);
});

test('unmount cancellation settles the active load and clears timers without publishing a failure or fallback',async()=>{
  const h=await harness(()=>new Promise(()=>{}),{radarReplayMode:true,readRadarIndex:()=>{assert.fail('cancelled request must not enter local fallback');}});
  const pending=h.load();await flush();h.requestRef.current.abort();await pending;assert.equal(h.state.error,'');assert.equal(h.state.manifest,null);assert.equal(h.timers.size,0);
});

test('ordinary HTTP failure is retryable and a successful station read retains true zero and clears deadlines',async()=>{
  let failed=true;
  const h=await harness(url=>Promise.resolve(url.includes('/manifest?')?(failed?Response.json({message:'Archive unavailable'},{status:503}):Response.json(manifest())):Response.json({observations:[{value:0}],truncated:false})),{station:'USGS-06889000'});
  await h.load();assert.equal(h.state.error,'Archive unavailable');assert.equal(h.button().props.disabled,false);assert.equal(h.timers.size,0);
  failed=false;await h.load();assert.equal(h.state.error,'');assert.equal(h.state.river.observations[0].value,0);assert.equal(h.state.riverMessage,'1 samples loaded');assert.equal(h.timers.size,0);
});

for(const stage of ['headers','body'])test(`native fetch cancels a real loopback HTTP ${stage} stall through the actual load callback`,{timeout:5000},async(t)=>{
  const reached=deferred(),closed=deferred();
  const server=createServer((_req,res)=>{
    res.on('close',()=>closed.resolve());
    if(stage==='body'){res.writeHead(200,{'content-type':'application/json'});res.write('{"format":');}
    reached.resolve();
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  t.after(()=>new Promise(resolve=>{server.closeAllConnections();server.close(resolve);}));
  const origin=`http://127.0.0.1:${server.address().port}`;
  const h=await harness((url,init)=>fetch(origin+url,init));
  const pending=h.load();await reached.promise;await flush();h.expire();await pending;
  assert.match(h.state.error,/took too long/);assert.equal(h.button().props.disabled,false);assert.equal(h.timers.size,0);
  await closed.promise;
});

test('a parent already cancelled starts no read and allocates no deadline',async()=>{
  const timers=new Map();const {replayRead}=(await componentHarness('app/observatory/load-deadline.ts',{}, {
    setTimeout(){assert.fail('already-cancelled work must allocate no timer');},clearTimeout:id=>timers.delete(id),
  })).exports;
  const controller=new AbortController();controller.abort();
  await assert.rejects(replayRead(()=>{assert.fail('already-cancelled work must perform no read');},controller.signal,'timeout'));
  assert.equal(timers.size,0);
});
