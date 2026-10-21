import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {componentHarness,findNode} from './component-harness.mjs';
import {capabilityPreviews,capabilityNote} from '../app/living-welcome/capability-catalog.mjs';

test('selected capture stops animation when paused, hidden or failed; no video decoder is mounted',async()=>{
 const listeners=new Map(),document={hidden:false,addEventListener:(k,v)=>listeners.set(k,v),removeEventListener:k=>listeners.delete(k)};
 const h=await componentHarness('app/living-welcome/CapabilityPreview.jsx',{}, {document});
 const props={demo:capabilityPreviews('weather')[0]};
 const render=()=>{const t=h.render(h.exports.CapabilityPreview,props);h.commit();return t;};
 let tree=render();assert.equal(findNode(tree,n=>n.type==='video'),undefined);
 assert.equal(findNode(tree,n=>n.type==='img').props.src,props.demo.animation);
 props.paused=true;tree=render();assert.equal(findNode(tree,n=>n.type==='img').props.src,props.demo.poster);
 props.paused=false;document.hidden=true;listeners.get('visibilitychange')();tree=render();assert.equal(findNode(tree,n=>n.type==='img').props.src,props.demo.poster);
 document.hidden=false;listeners.get('visibilitychange')();tree=render();findNode(tree,n=>n.type==='img').props.onError();tree=render();assert.equal(findNode(tree,n=>n.type==='img').props.src,props.demo.poster);
 props.demo=capabilityPreviews('water')[0];tree=render();assert.equal(findNode(tree,n=>n.type==='img').props.src,props.demo.animation,'failure does not contaminate another capture');
 h.dispose();assert.equal(listeners.size,0);
});

test('context reuse and uncaptured workspaces cannot invent observation coverage',()=>{
 assert.match(capabilityPreviews('ecology')[0].context,/no species inventory/);
 assert.match(capabilityPreviews('people')[0].context,/not individual people/);
 for(const id of ['sky','evidence']){assert.deepEqual(capabilityPreviews(id),[]);assert.match(capabilityNote(id),/No verified/);}
});

test('hourglass keeps reduced motion and hidden tabs still without a JavaScript animation timer',async()=>{
 const listeners=new Map(),document={hidden:false,addEventListener:(k,v)=>listeners.set(k,v),removeEventListener:k=>listeners.delete(k)};
 const h=await componentHarness('app/time-emblem.tsx',{}, {document});const props={animated:true,reducedMotion:false};
 const render=()=>{const t=h.render(h.exports.TimeEmblem,props);h.commit();return t;};
 assert.equal(render().props['data-moving'],true);props.reducedMotion=true;assert.equal(render().props['data-moving'],false);
 props.reducedMotion=false;document.hidden=true;listeners.get('visibilitychange')();assert.equal(render().props['data-moving'],false);
 document.hidden=false;listeners.get('visibilitychange')();props.visible=false;assert.equal(render().props['data-moving'],false);
 h.dispose();assert.equal(listeners.size,0);
 const css=await readFile('app/compact-time-sweep.css','utf8');assert.match(css,/hourglass-flip 10\.8s/);assert.match(css,/92\.5926%/);
});

test('delivered animations and generated decoration retain source integrity',async()=>{
 const {createHash}=await import('node:crypto');
 const sha=b=>createHash('sha256').update(b).digest('hex');
 const manifest=JSON.parse(await readFile('public/welcome/animations/provenance.json','utf8'));
 assert.equal(manifest.live,false);assert.equal(manifest.files.length,16);
 for(const file of manifest.files){
  const bytes=await readFile('public'+file.delivery);assert.equal(bytes.length,file.bytes);assert.equal(sha(bytes),file.sha256);
  assert.equal(sha(await readFile('public'+file.source)),file.sourceSha256);
  assert.equal(bytes.subarray(0,4).toString(),'RIFF');assert.equal(bytes.subarray(8,12).toString(),'WEBP');
 }
 const art=JSON.parse(await readFile('public/icons/time-sweep/hourglass-provenance.json','utf8'));
 assert.equal(art.authority,'NONE');assert.equal(sha(await readFile('public/icons/time-sweep/'+art.delivery)),art.deliverySha256);
});
