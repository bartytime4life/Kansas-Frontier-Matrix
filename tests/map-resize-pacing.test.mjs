import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {runInNewContext} from 'node:vm';
import test from 'node:test';
import ts from 'typescript';
const page=await readFile(new URL('../app/page.tsx',import.meta.url),'utf8');
const tree=ts.createSourceFile('page.tsx',page,ts.ScriptTarget.Latest,true,ts.ScriptKind.TSX);
let observer,quality;
function visit(node){
 if(ts.isNewExpression(node)&&node.expression.getText(tree)==='ResizeObserver')observer=node.arguments[0].getText(tree);
 if(ts.isCallExpression(node)&&node.expression.getText(tree)==='useEffect'&&node.arguments[0]?.getText(tree).includes('Rendering-quality update'))quality=node.getText(tree);
 ts.forEachChild(node,visit);
}visit(tree);assert.ok(observer);assert.ok(quality);
const compile=s=>ts.transpileModule(s,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
test('unchanged pixel ratio never resizes the canvas; a changed ratio applies exactly once',async()=>{
 let ratio=1.5,requested=1.5,resizes=0,handler;
 const ctx={__KFM_WELCOME_RECORDER__:false,localCapturePixelRatioRef:{current:1},useEffect:effect=>effect(),mapRef:{current:{getPixelRatio:()=>ratio,setPixelRatio:value=>{ratio=value;resizes++;}}},renderQuality:'auto',styleReady:true,
 browserRenderBudget:()=>({pixelRatio:requested,imageRequests:10}),runMapMutation:(_label,fn)=>fn(),loadMapLibre:async()=>({setMaxParallelImageRequests(){}}),
 window:{addEventListener:(_event,callback)=>{handler=callback;},removeEventListener(){}}};
 runInNewContext(compile(quality),ctx);handler();assert.equal(resizes,0);
 requested=2;handler();assert.equal(resizes,1);handler();assert.equal(resizes,1);await Promise.resolve();
});
test('a burst of container notifications uses one resize on the next frame and remains reusable',()=>{
 const frames=new Map();let serial=0,resizes=0;
 const ctx={disposed:false,mapResizeFrame:undefined,map:{resize:()=>resizes++},runMapMutation:(_label,fn)=>fn(),
 window:{requestAnimationFrame:fn=>{const id=++serial;frames.set(id,fn);return id;}}};
 runInNewContext(compile(`const observe=${observer};globalThis.observe=observe;`),ctx);
 const entries=[{contentRect:{width:800,height:600}}];ctx.observe(entries);ctx.observe(entries);ctx.observe(entries);
 assert.equal(frames.size,1);for(const[id,fn]of [...frames]){frames.delete(id);fn();}assert.equal(resizes,1);
 ctx.observe(entries);assert.equal(frames.size,1);ctx.disposed=true;for(const fn of frames.values())fn();assert.equal(resizes,1);
});


test('local capture keeps its native pixel ratio across budget changes and releases it without repeated resize',async()=>{
 let ratio=1.25,requested=1.5,resizes=0,handler;
 const captureRatio={current:1.25};
 const ctx={__KFM_WELCOME_RECORDER__:true,localCapturePixelRatioRef:captureRatio,useEffect:effect=>effect(),
 mapRef:{current:{getPixelRatio:()=>ratio,setPixelRatio:value=>{ratio=value;resizes++;}}},renderQuality:'auto',styleReady:true,
 browserRenderBudget:()=>({pixelRatio:requested,imageRequests:10}),runMapMutation:(_label,fn)=>fn(),loadMapLibre:async()=>({setMaxParallelImageRequests(){}}),
 window:{addEventListener:(_event,callback)=>{handler=callback;},removeEventListener(){}}};
 runInNewContext(compile(quality),ctx);assert.equal(resizes,0,'matching native capture ratio does not resize');
 requested=2;handler();assert.equal(resizes,0,'ordinary quality updates cannot churn the active capture canvas');assert.equal(ratio,1.25);
 captureRatio.current=null;handler();assert.equal(ratio,2);assert.equal(resizes,1,'releasing capture restores the current render budget once');
 handler();assert.equal(resizes,1);await Promise.resolve();
});
