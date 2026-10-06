import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import ts from 'typescript';
const js=ts.transpileModule(await readFile('app/aquifer-volume.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022,esModuleInterop:true}}).outputText.replace('from "polygon-clipping"',`from ${JSON.stringify(new URL('../node_modules/polygon-clipping/dist/polygon-clipping.esm.js',import.meta.url).href)}`);
const m=await import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
const bounds=[-100.8,38.3,-100.2,38.7];
const square=[[-100.7,38.35],[-100.3,38.35],[-100.3,38.65],[-100.7,38.65],[-100.7,38.35]];
const hole=[[-100.55,38.45],[-100.55,38.55],[-100.45,38.55],[-100.45,38.45],[-100.55,38.45]];
function data(label,count,holeRing=false){return {type:'FeatureCollection',features:Array.from({length:count},(_,i)=>({type:'Feature',properties:{period:'2022–2024',hasValue:i===0,classLabel:i===0?label:'No classified value'},geometry:{type:'MultiPolygon',coordinates:i===0?[[square,...(holeRing?[hole]:[])]]:[]}}))};}
test('aquifer envelope uses full source bounds, never a midpoint or class code',()=>{
  assert.deepEqual(m.envelopeDepths([25,50],[100,150]),{shallowMeters:7.62,deepMeters:60.96});
  assert.throws(()=>m.envelopeDepths([50,25],[100,150]));
  const v=m.buildAquiferVolume(data('25 to 50',10),data('100 to 150',8),bounds);
  assert.equal(v.envelopes.length,1);assert.equal(v.envelopes[0].shallowMeters,7.62);assert.equal(v.envelopes[0].deepMeters,60.96);assert.equal(v.period,'2022–2024');
});
test('polygon intersections preserve holes, and open-ended classes remain held',()=>{
  const v=m.buildAquiferVolume(data('Under 25',10,true),data('Under 50',8),bounds);
  assert.equal(v.envelopes[0].geometry[0].length,2);
  const held=m.buildAquiferVolume(data('Over 350',10),data('Over 300',8),bounds);
  assert.equal(held.envelopes.length,0);assert.equal(held.heldClasses,2);
});
test('spatial scope and source period fail closed',()=>{
  for(const b of [[-102,37,-94,40],[NaN,38,-100,39],[-100,38,-101,39],[-100,0,-99.9,0.1]])assert.equal(m.validVolumeBounds(b),false);
  const bad=data('Under 25',10);bad.features[0].properties.period='1990';assert.throws(()=>m.buildAquiferVolume(bad,data('Under 50',8),bounds));
  assert.throws(()=>m.buildAquiferVolume(data('Under 25',9),data('Under 50',8),bounds));
});
test('surface plane alignment keeps north, south, east and west correctly oriented',()=>{
  assert.equal(m.projectVolumePosition(bounds[0],38.5,bounds).x,-3);assert.equal(m.projectVolumePosition(bounds[2],38.5,bounds).x,3);
  assert.ok(m.projectVolumePosition(-100.5,bounds[3],bounds).z<0);assert.ok(m.projectVolumePosition(-100.5,bounds[1],bounds).z>0);
  const expected=6/(6378137*.6*Math.PI/180*Math.cos(38.5*Math.PI/180));assert.ok(Math.abs(m.volumeDepthScale(bounds)-expected)<1e-12);
});
test('real KGS snapshots match pinned hashes and produce a bounded example',async()=>{
  const data=[];for(const item of m.AQUIFER_VOLUME_ASSETS){const bytes=await readFile(`public${item.url}`);assert.equal(createHash('sha256').update(bytes).digest('hex'),item.sha256);data.push(JSON.parse(bytes));}
  const v=m.buildAquiferVolume(data[0],data[1],bounds);assert.ok(v.envelopes.length>0);assert.equal(v.truncated,false);
  for(const e of v.envelopes)for(const [lon,lat] of e.geometry.flat(2)){assert.ok(lon>=bounds[0]-1e-8&&lon<=bounds[2]+1e-8);assert.ok(lat>=bounds[1]-1e-8&&lat<=bounds[3]+1e-8);assert.ok(e.deepMeters>e.shallowMeters);}
});

import vm from 'node:vm';
import { webcrypto } from 'node:crypto';
const workerText=ts.transpileModule(await readFile('app/aquifer-volume-worker.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText.replace(/^import[^;]+;/m,'const { AQUIFER_VOLUME_ASSETS, buildAquiferVolume } = model;');
function harness(fetcher){const messages=[],scope={postMessage:v=>messages.push(v)};vm.runInNewContext(workerText,{self:scope,model:m,fetch:fetcher,AbortController,Uint8Array,TextDecoder,crypto:webcrypto,setTimeout,clearTimeout,console});return {messages,send:(id,b=bounds)=>scope.onmessage({data:{id,bounds:b}})};}
test('worker rejects tampered or oversized source bytes rather than rendering them',async()=>{
  for(const content of ['{}','x'.repeat(800001)]){const h=harness(async()=>new Response(content));await h.send(1);assert.equal(h.messages.length,1);assert.ok(h.messages[0].error);assert.equal(h.messages[0].volume,undefined);}
});
test('worker caches verified bytes and interrupted requests cannot replace a newer view',async()=>{
  const bytes=await Promise.all(m.AQUIFER_VOLUME_ASSETS.map(a=>readFile(`public${a.url}`)));let requests=0;
  const h=harness(async(url,{signal})=>{requests++;if(requests<=2)await new Promise((resolve,reject)=>signal.addEventListener('abort',()=>reject(new Error('aborted')),{once:true}));return new Response(bytes[url===m.AQUIFER_VOLUME_ASSETS[0].url?0:1]);});
  const old=h.send(1);await h.send(2);await old;assert.deepEqual(h.messages.map(r=>r.id),[2]);assert.ok(h.messages[0].volume.envelopes.length>0);
  await h.send(3);assert.equal(requests,4);assert.deepEqual(h.messages.map(r=>r.id),[2,3]);
});
