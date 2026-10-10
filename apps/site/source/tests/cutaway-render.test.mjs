import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';

const compile=source=>ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
const cameraModule={};vm.runInNewContext(compile(await readFile('app/cutaway-camera.ts','utf8')),{exports:cameraModule});
const source=await readFile('app/aquifer-volume-view.tsx','utf8'),ast=ts.createSourceFile('view.tsx',source,ts.ScriptTarget.Latest,true,ts.ScriptKind.TSX);
const names=['renderSchedule','render','changed','applyPose','cancelDamping','visibilityChanged','lost'],declarations=new Map();
function visit(node){if(ts.isVariableDeclaration(node)&&names.includes(node.name.getText(ast)))declarations.set(node.name.getText(ast),node.getText(ast));ts.forEachChild(node,visit);}visit(ast);
for(const name of names)assert.ok(declarations.has(name),`missing actual view callback ${name}`);

function harness({damping=false,immediate=false}={}){
 const canvas=Object.assign(new EventTarget(),{clientWidth:800,clientHeight:500,style:{}});canvas.ownerDocument=canvas;canvas.getRootNode=()=>canvas;
 const camera=new THREE.PerspectiveCamera(40,1.6,.01,500);camera.position.set(0,2,10);
 const controls=new OrbitControls(camera,canvas);controls.enableDamping=damping;controls.dampingFactor=.14;controls.listenToKeyEvents(canvas);
 const frames=new Map(),draws=[],failures=[],document={hidden:false};let serial=0,cancels=0;
 const pose=()=>({position:camera.position.toArray(),target:controls.target.toArray()});
 const exports={},context={exports,createCutawayRenderSchedule:cameraModule.createCutawayRenderSchedule,camera,controls,renderer:{domElement:canvas},document,
  requestAnimationFrame:fn=>{const id=++serial;frames.set(id,fn);return id},cancelAnimationFrame:id=>frames.delete(id),
  fit:()=>({distance:10}),draw:()=>draws.push(pose()),motion:{cancel(){cancels++}},motionPreference:{matches:!damping},setFailure:message=>failures.push(message),resources:[]};
 // Execute the real view's scheduling, pose, cancellation and visibility callbacks.
 const body=names.map(name=>`const ${immediate&&name==='render'?'render=draw':immediate&&name==='changed'?'changed=draw':declarations.get(name)};`).join('\n');
 vm.runInNewContext(compile(`let disposed=false,contextLost=false,viewOffset=[0,0];${body}\ncontrols.addEventListener('change',changed);Object.assign(exports,{render,applyPose,visibilityChanged,lost,stop(){disposed=true;renderSchedule.dispose();controls.removeEventListener('change',changed);controls.dispose();}});`),context);
 return {api:exports,frames,draws,failures,document,controls,camera,canvas,pose,get cancels(){return cancels},step(){const pending=[...frames.values()];frames.clear();pending.forEach(fn=>fn());},wheel(deltaY){const e=new Event('wheel',{cancelable:true});Object.assign(e,{deltaY,deltaMode:0,clientX:400,clientY:250});canvas.dispatchEvent(e);}};
}

test('actual pose callbacks coalesce explicit and OrbitControls draws and use the final camera',()=>{
 const batched=harness(),before=harness({immediate:true});
 for(let i=1;i<=40;i++)for(const h of [batched,before])h.api.applyPose({position:[i/10,2,10],target:[0,0,0],offset:[0,0]});
 assert.equal(before.draws.length,80,'previous change listener plus explicit pose draw');
 assert.equal(batched.draws.length,0);assert.equal(batched.frames.size,1);batched.step();
 assert.equal(batched.draws.length,1);assert.deepEqual(batched.draws[0],before.draws.at(-1));assert.equal(batched.frames.size,0);
 for(const h of [batched,before])h.api.stop();
});
test('real wheel bursts retain every camera step and target, with one final draw',()=>{
 const a=harness(),b=harness({immediate:true});for(let i=0;i<20;i++)for(const h of [a,b])h.wheel(i<10?100:-100);
 assert.ok(b.draws.length>1);assert.equal(a.frames.size,1);a.step();assert.equal(a.draws.length,1);assert.deepEqual(a.pose(),b.pose());assert.deepEqual(a.draws[0],b.draws.at(-1));a.api.stop();b.api.stop();
});
test('real OrbitControls damping completes without an idle loop or duplicate per-frame draws',()=>{
 const h=harness({damping:true}),event=new Event('keydown',{cancelable:true});Object.assign(event,{key:'ArrowRight',code:'ArrowRight',ctrlKey:false,metaKey:false,shiftKey:false});h.canvas.dispatchEvent(event);
 let count=0;while(h.frames.size&&count++<250){const n=h.draws.length;h.step();assert.equal(h.draws.length,n+1);assert.ok(h.frames.size<=1);}
 assert.ok(count>1&&count<250);assert.equal(h.frames.size,0);assert.deepEqual(h.draws.at(-1),h.pose());h.api.stop();
});
test('hidden or lost contexts cancel pending work, restoration draws current state, and stale callbacks are inert',()=>{
 const h=harness();h.api.render();const stale=[...h.frames.values()][0];h.document.hidden=true;h.api.visibilityChanged();assert.equal(h.frames.size,0);stale();assert.equal(h.draws.length,0);
 h.document.hidden=false;h.api.visibilityChanged();h.step();assert.equal(h.draws.length,1);
 h.api.render();const lost=[...h.frames.values()][0];const event=new Event('webglcontextlost',{cancelable:true});h.api.lost(event);assert.equal(event.defaultPrevented,true);assert.equal(h.frames.size,0);lost();h.api.render();assert.equal(h.frames.size,0);assert.equal(h.draws.length,1);assert.match(h.failures[0],/2D locator/);h.api.stop();
 const disposed=harness();disposed.api.render();const late=[...disposed.frames.values()][0];disposed.api.stop();late();disposed.api.render();assert.equal(disposed.frames.size,0);assert.equal(disposed.draws.length,0);
});
test('reduced-motion updates remain single-frame draws without damping continuation',()=>{
 const h=harness();h.api.applyPose({position:[0,10,.001],target:[0,0,0],offset:[0,0]});h.step();assert.equal(h.draws.length,1);assert.equal(h.frames.size,0);assert.deepEqual(h.draws[0],h.pose());h.api.stop();
});
