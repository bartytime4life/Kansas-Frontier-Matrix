import assert from 'node:assert/strict';
import test from 'node:test';
import {readFile} from 'node:fs/promises';
import path from 'node:path';
import {Miniflare,convertV4MiniflareOptions} from 'miniflare';
import ts from 'typescript';
import {componentHarness,findNode,settle} from './component-harness.mjs';
const compile=async file=>ts.transpileModule(await readFile(new URL('../app/'+file,import.meta.url),'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const url=s=>`data:text/javascript;base64,${Buffer.from(s).toString('base64')}`;
const sub=url((await compile('subsurface-model.ts')).replace('import { atRecordYear } from "./subsurface-materials";','const atRecordYear=()=>true;'));
const modelURL=url((await compile('underground-resources-model.ts')).replace('"./subsurface-model"',JSON.stringify(sub)));
const model=await import(modelURL);
const boundedURL=url(await compile('bounded-json.ts'));
const {GET}=await import(url((await compile('api/subsurface/resources/route.ts')).replace('"../../../bounded-json"',JSON.stringify(boundedURL)).replace('"../../../subsurface-model"',JSON.stringify(sub)).replace('"../../../underground-resources-model"',JSON.stringify(modelURL))));
const bounds=[-99.7,38.7,-99.3,39];
const feature=(id=1,p=[-99.5,38.8])=>({type:'Feature',geometry:{type:'Point',coordinates:p},properties:{OBJECTID:id,KID:50,LEASE_NAME:'Test inventory',WELL_CLASS:'OIL',STATUS:'P&A',ROTARY_TOTAL_DEPTH:500,PRODUCT:'Limestone'}});
test('resource source requests are Kansas bounded, capped, transformed to WGS84 and fixed-host',async()=>{
 const old=globalThis.fetch;let sent;
 globalThis.fetch=async u=>{sent=new URL(u);return Response.json({type:'FeatureCollection',features:[feature()]});};
 try{assert.equal((await GET(new Request('https://kfm.test/api?kind=oilgas&bounds=-104,38,-90,39'))).status,400);assert.equal(sent,undefined);
 const r=await GET(new Request(`https://kfm.test/api?kind=oilgas&bounds=${bounds}`));const v=await r.json();assert.equal(r.status,200);assert.equal(sent.hostname,'services.kansasgis.org');assert.equal(sent.searchParams.get('outSR'),'4326');assert.equal(sent.searchParams.get('resultRecordCount'),'201');assert.equal(v.rows[0].status,'P&A');assert.match(v.source.limitation,/not current production/);assert.ok(v.retrievedAt);
 }finally{globalThis.fetch=old;}
});
test('historical mine partial flags, exact frame, duplicate and malformed positions stay distinct',()=>{
 const v=model.resourceLocations({type:'FeatureCollection',properties:{exceededTransferLimit:true},features:[feature(),feature(),feature(3,[-99.9,38.8]),feature(4,[0,0]),{bad:true}]},'minerals',bounds);
 assert.equal(v.rows.length,1);assert.equal(v.rejected,4);assert.equal(v.partial,true);assert.equal(v.rows[0].material,'Limestone');assert.match(model.RESOURCE_SOURCES.minerals.limitation,/circa 2000/);
 assert.throws(()=>model.resourceLocations({type:'FeatureCollection',features:Array(202).fill(feature())},'oilgas',bounds));
});
test('source failures and excessive response bytes remain unavailable',async()=>{
 const old=globalThis.fetch;
 try{for(const body of ['x'.repeat(1_000_001),JSON.stringify({error:'provider error'})]){globalThis.fetch=async()=>new Response(body);assert.equal((await GET(new Request(`https://kfm.test/api?kind=minerals&bounds=${bounds}`))).status,502);}}finally{globalThis.fetch=old;}
});
test('the real Worker runtime reads resource records and refuses provider redirects',async()=>{
 const root=path.resolve('tests/resource-worker');let redirect=false;const calls=[];
 const contents={
  'index.mjs':'import {GET} from "./route.mjs";export default {fetch:GET};',
  'route.mjs':(await compile('api/subsurface/resources/route.ts')).replace('"../../../bounded-json"','"./bounded.mjs"').replace('"../../../subsurface-model"','"./subsurface.mjs"').replace('"../../../underground-resources-model"','"./resources.mjs"'),
  'bounded.mjs':await compile('bounded-json.ts'),
  'subsurface.mjs':(await compile('subsurface-model.ts')).replace('"./subsurface-materials"','"./materials.mjs"'),
  'materials.mjs':await compile('subsurface-materials.ts'),
  'resources.mjs':(await compile('underground-resources-model.ts')).replace('"./subsurface-model"','"./subsurface.mjs"'),
 };
 const mf=new Miniflare(convertV4MiniflareOptions({modulesRoot:root,modules:Object.entries(contents).map(([name,contents])=>({type:'ESModule',path:path.join(root,name),contents})),compatibilityDate:'2026-08-28',outboundService:async request=>{calls.push(request.url);return redirect?Response.redirect('https://unapproved.example/records'):Response.json({type:'FeatureCollection',features:[feature()]});}}));
 try{
  const request=`https://kfm.test/api/subsurface/resources?kind=oilgas&bounds=${bounds}`;
  const accepted=await mf.dispatchFetch(request);assert.equal(accepted.status,200);assert.equal((await accepted.json()).rows.length,1);assert.equal(calls.length,1);
  redirect=true;assert.equal((await mf.dispatchFetch(request)).status,502);assert.equal(calls.length,2,'redirect target was never requested');
 }finally{await mf.dispose();}
});
test('switching area discards delayed resource response before displaying markers or details',async()=>{
 const requests=[];
 const h=await componentHarness('app/underground-resources.tsx',{'./underground-resources-model':model,'./bounded-json':{readBoundedJson:r=>r.json()},'./subsurface.module.css':{default:new Proxy({},{get:(_,k)=>k})}}, {URLSearchParams,fetch:(u,o)=>new Promise(resolve=>requests.push({u,o,resolve}))});
 let props={map:null,bounds,revision:1,active:true,redacted:false,water:[],onInspect(){}};
 let tree=h.render(h.exports.default,props);h.commit();findNode(tree,n=>n.type==='details').props.onToggle({currentTarget:{open:true}});h.render(h.exports.default,props);h.commit();
 props={...props,bounds:[-99.2,38.7,-99,39],revision:2};h.render(h.exports.default,props);h.commit();assert.equal(requests[0].o.signal.aborted,true);
 requests[0].resolve(Response.json({rows:[{id:'old',name:'STALE',details:[],coordinates:[-99.5,38.8]}],partial:false,rejected:0,retrievedAt:'2026-10-07'}));await settle();
 tree=h.render(h.exports.default,props);assert.doesNotMatch(JSON.stringify(tree),/STALE/);
 requests[1].resolve(Response.json({rows:[],partial:false,rejected:0,retrievedAt:'2026-10-07'}));await settle();h.dispose();
});
