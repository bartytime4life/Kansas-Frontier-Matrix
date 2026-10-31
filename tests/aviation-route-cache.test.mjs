import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';

// next/server's NextResponse is a Response subclass; the plain Response is enough for the cache's contract.
const source=(await readFile('app/aviation-route-cache.ts','utf8')).replace('import { NextResponse } from "next/server";','const NextResponse = Response;');
const cache=await import(`data:text/javascript;base64,${Buffer.from(ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`);
const json=(body,status=200)=>new Response(JSON.stringify(body),{status,headers:{'Content-Type':'application/json','Cache-Control':'public, max-age=15'}});

test('successful responses are replayed within the window and refreshed after it',async()=>{
 cache.clearAviationRouteCache();
 let now=1000,calls=0;const build=async()=>json({n:++calls});
 assert.deepEqual(await (await cache.cachedAviationRoute('k',15_000,build,()=>now)).json(),{n:1});
 now+=14_000;const replay=await cache.cachedAviationRoute('k',15_000,build,()=>now);
 assert.deepEqual(await replay.json(),{n:1});assert.equal(replay.headers.get('cache-control'),'public, max-age=15','headers replay too');
 now+=2_000;assert.deepEqual(await (await cache.cachedAviationRoute('k',15_000,build,()=>now)).json(),{n:2});
 assert.equal(calls,2);
});

test('concurrent viewers share one upstream request; failures are never cached',async()=>{
 cache.clearAviationRouteCache();
 let calls=0,release;const gate=new Promise(resolve=>{release=resolve;});
 const slow=async()=>{calls++;await gate;return json({ok:true});};
 const pending=[1,2,3].map(()=>cache.cachedAviationRoute('shared',60_000,slow));
 release();const bodies=await Promise.all(pending.map(async p=>(await p).json()));
 assert.equal(calls,1);assert.deepEqual(bodies,[{ok:true},{ok:true},{ok:true}]);
 let failures=0;const failing=async()=>{failures++;return json({state:'error'},502);};
 assert.equal((await cache.cachedAviationRoute('bad',60_000,failing)).status,502);
 assert.equal((await cache.cachedAviationRoute('bad',60_000,failing)).status,502);
 assert.equal(failures,2,'an outage is retried on the next request, not replayed');
});

test('every aviation route uses the cache with a provider-respecting window',async()=>{
 const windows={metar:'120_000',pireps:'120_000',traffic:'15_000',tfrs:'300_000','uas-grid':'86_400_000'};
 for(const [route,ttl] of Object.entries(windows)){
  const text=await readFile(`app/api/aviation/${route}/route.ts`,'utf8');
  assert.match(text,new RegExp(`cachedAviationRoute\\("${route}", ${ttl}, \\(\\) => `),route);
 }
 const held=await readFile('app/api/aviation/airports/route.ts','utf8');
 assert.doesNotMatch(held,/cachedAviationRoute/,'the held FAA-candidate route is unchanged');
});

test('opening the aviation category map switches the airspace layer on without a second toggle',async()=>{
 const page=await readFile('app/page.tsx','utf8'),maps=await readFile('app/category-maps.ts','utf8');
 assert.match(maps,/topic: "aviation"[^\n]*overlays: \["aviation"\]/);
 assert.match(page,/setAviationShowRequest\(request => look\.overlays\?\.includes\("aviation"\) \? request \+ 1 : 0\);/,'leaving Aviation clears its show request');
 assert.match(page,/<AviationLayerControl [^>]*showRequest=\{aviationShowRequest\}/);
 const control=await readFile('app/aviation-layer-control.tsx','utf8');
 assert.match(control,/if \(showRequest && !visible\) \{ setVisible\(true\); setRender\("Waiting for map frame"\); \}/);
 assert.doesNotMatch(control,/setVisible\(false\)[^\n]*showRequest/,'a request only ever shows the layer');
});
