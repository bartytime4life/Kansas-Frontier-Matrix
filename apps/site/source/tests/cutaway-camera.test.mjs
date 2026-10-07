import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
const compile = source => ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const url = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;
const {betweenCameraPoses,createCutawayCameraMotion,rotateCutawayCamera,bindCameraKeyboardInterruption}=await import(url(compile(await readFile('app/cutaway-camera.ts','utf8'))));
const materials=url(compile(await readFile('app/subsurface-materials.ts','utf8')));
const model=url(compile(await readFile('app/subsurface-model.ts','utf8')).replace('"./subsurface-materials"',JSON.stringify(materials)));
const {cutawayCameraFit}=await import(url(compile(await readFile('app/cutaway-model.ts','utf8')).replace('"./subsurface-model"',JSON.stringify(model))));
const original={position:[0,2,10],target:[0,0,0],offset:[.1,-.2]};
function harness(reduced=false){
  let time=0,pose=structuredClone(original),serial=0;const frames=new Map(),applied=[];
  const motion=createCutawayCameraMotion({read:()=>structuredClone(pose),apply:next=>{pose=structuredClone(next);applied.push(pose)},reducedMotion:()=>reduced,now:()=>time,
    request:callback=>{const id=++serial;frames.set(id,callback);return id},cancel:id=>frames.delete(id)});
  return {motion,frames,applied,get pose(){return pose},step(next){time=next;const pending=[...frames.values()];frames.clear();pending.forEach(callback=>callback(time));}};
}
test('camera transition orbits around the target rather than crossing the model',()=>{
  const from={position:[0,0,10],target:[0,0,0],offset:[0,0]},to={position:[10,0,0],target:[0,0,0],offset:[.2,-.1]};
  const mid=betweenCameraPoses(from,to,.5);assert.ok(Math.abs(Math.hypot(...mid.position)-10)<1e-10);assert.ok(mid.position[0]>7&&mid.position[2]>7);assert.deepEqual(mid.offset,[.1,-.05]);
});
test('camera transition completes exactly and leaves no idle frames',()=>{
  const h=harness(),to={position:[10,4,0],target:[1,2,3],offset:[-.2,.3]};h.motion.move(to,300);
  assert.deepEqual(h.pose,original);h.step(150);assert.notDeepEqual(h.pose,original);assert.notDeepEqual(h.pose,to);assert.equal(h.frames.size,1);
  h.step(300);assert.deepEqual(h.pose,to);assert.equal(h.frames.size,0);
});
test('rapid camera commands replace the in-flight transition from its actual pose',()=>{
  const h=harness();h.motion.move({position:[10,2,0],target:[0,0,0],offset:[0,0]},300);h.step(90);const current=structuredClone(h.pose),stale=[...h.frames.values()][0];
  const next={position:[0,12,0],target:[0,0,0],offset:[0,0]};h.motion.move(next,300);assert.deepEqual(h.pose,current);assert.equal(h.frames.size,1);
  const count=h.applied.length;stale(180);assert.equal(h.applied.length,count);h.step(390);assert.deepEqual(h.pose,next);assert.equal(h.frames.size,0);
});
test('direct manipulation cancels transition without resetting the current camera',()=>{
  const h=harness();h.motion.move({position:[10,2,0],target:[0,0,0],offset:[0,0]});h.step(60);const current=structuredClone(h.pose),stale=[...h.frames.values()][0];
  h.motion.cancel();stale(300);assert.deepEqual(h.pose,current);assert.equal(h.frames.size,0);
});
test('real keyboard events interrupt in-flight camera transitions, including modified arrows, and detach cleanly',()=>{
  const target=new EventTarget(),h=harness();const stop=bindCameraKeyboardInterruption(target,h.motion.cancel);
  const key=(name,modifiers={})=>{const event=new Event('keydown');Object.assign(event,{key:name,...modifiers});target.dispatchEvent(event);};
  const to={position:[10,2,0],target:[0,0,0],offset:[0,0]};
  for(const name of ['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'])for(const modifiers of [{},{ctrlKey:true},{metaKey:true},{shiftKey:true},{altKey:true}]){
    h.motion.move(to);const stale=[...h.frames.values()][0],before=structuredClone(h.pose);key(name,modifiers);assert.equal(h.frames.size,0);stale(300);assert.deepEqual(h.pose,before);
  }
  h.motion.move(to);key('Tab');assert.equal(h.frames.size,1,'unrelated keys retain the transition');
  stop();key('ArrowLeft');assert.equal(h.frames.size,1,'cleanup removes the interruption handler');h.motion.dispose();
});
test('actual OrbitControls keyboard pan and modified rotation survive a pending preset frame',()=>{
  for(const modifiers of [{},{ctrlKey:true},{metaKey:true},{shiftKey:true}]){
    const canvas=Object.assign(new EventTarget(),{clientWidth:800,clientHeight:500,style:{}});canvas.ownerDocument=canvas;canvas.getRootNode=()=>canvas;
    const camera=new THREE.PerspectiveCamera(40,1.6,.01,100);camera.position.set(0,2,10);
    const controls=new OrbitControls(camera,canvas);controls.listenToKeyEvents(canvas);let starts=0;controls.addEventListener('start',()=>starts++);
    let serial=0;const frames=new Map(),read=()=>({position:camera.position.toArray(),target:controls.target.toArray(),offset:[0,0]});
    const motion=createCutawayCameraMotion({read,apply:pose=>{camera.position.fromArray(pose.position);controls.target.fromArray(pose.target);controls.update()},reducedMotion:()=>false,now:()=>0,
      request:callback=>{const id=++serial;frames.set(id,callback);return id},cancel:id=>frames.delete(id)});
    const stop=bindCameraKeyboardInterruption(canvas,motion.cancel);motion.move({position:[0,10,.001],target:[0,0,0],offset:[0,0]});
    const stale=[...frames.values()][0],before=read(),event=new Event('keydown',{cancelable:true});Object.assign(event,{key:'ArrowRight',code:'ArrowRight',...modifiers});canvas.dispatchEvent(event);
    const keyboardPose=read();assert.notDeepEqual(keyboardPose,before,'real controls changed the camera');assert.equal(starts,0,'keyboard path has no pointer start event');
    stale(300);assert.deepEqual(read(),keyboardPose,'interruption prevents a pending preset from overwriting keyboard control');assert.equal(frames.size,0);
    stop();motion.dispose();controls.dispose();
  }
});
test('reduced motion applies the target immediately and disposal makes stale frames inert',()=>{
  const to={position:[10,2,0],target:[0,0,0],offset:[0,0]},h=harness(true);h.motion.move(to);assert.deepEqual(h.pose,to);assert.equal(h.frames.size,0);
  const animated=harness();animated.motion.move(to);const stale=[...animated.frames.values()][0];animated.motion.dispose();stale(300);animated.motion.move(to);assert.deepEqual(animated.pose,original);assert.equal(animated.frames.size,0);
});
test('repeated rotate commands refit shallow desktop corners and labels and preserve deliberate zoom',()=>{
  const width=1080,height=500,depth=.02,length=3.7,fit=direction=>cutawayCameraFit(6,length,depth,width/height,direction,height);
  const initial=fit([.55,.6,1]),target=[0,-depth/2,0];let pose={target,position:new THREE.Vector3(.55,.6,1).normalize().multiplyScalar(initial.distance).add(new THREE.Vector3(...target)).toArray(),offset:[initial.offsetX,initial.offsetY]};
  for(let i=0;i<24;i++){
    pose=rotateCutawayCamera(pose,.3,fit);const camera=new THREE.PerspectiveCamera(40,width/height,.000001,10000);
    camera.setViewOffset(width,height,pose.offset[0]*width/2,-pose.offset[1]*height/2,width,height);camera.position.fromArray(pose.position);camera.lookAt(...pose.target);camera.updateMatrixWorld(true);
    for(const x of [-3,3])for(const y of [0,-depth])for(const z of [-length/2,length/2]){const p=new THREE.Vector3(x,y,z).project(camera);assert.ok(Math.abs(p.x)<1&&Math.abs(p.y)<1,`corner clipped after rotate ${i}`);}
    for(const y of [0,-depth]){const p=new THREE.Vector3(-3.42,y,length/2).project(camera);assert.ok(Math.abs(p.x)+90/width<1&&Math.abs(p.y)+24/height<1,`depth label clipped after rotate ${i}`);}
  }
  const delta=pose.position.map((v,i)=>v-pose.target[i]);pose.position=delta.map((v,i)=>pose.target[i]+v*.7);
  const rotated=rotateCutawayCamera(pose,.3,fit),nextDelta=rotated.position.map((v,i)=>v-rotated.target[i]),nextFit=fit(nextDelta);
  assert.ok(Math.abs(Math.hypot(...nextDelta)/nextFit.distance-.7)<1e-10,'rotation retains the 70 percent fit distance');
});
