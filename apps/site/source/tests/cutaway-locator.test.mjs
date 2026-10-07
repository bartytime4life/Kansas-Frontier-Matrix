import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
const source=ts.transpileModule(await readFile('app/cutaway-locator.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const {cutawayLocatorPlacement,resizeMapAfterLayout}=await import(`data:text/javascript;base64,${Buffer.from(source).toString('base64')}`);
test('selector overlay stays in its slot and below the header after ancestor focus scrolling',()=>{
  for(const scrollTop of [0,27,83])for(const scrollLeft of [0,17]){
    const slot={left:25,top:-91.859,width:320,height:240,bottom:148.141},stage={left:0,top:41,scrollTop,scrollLeft},clip={top:68,bottom:744};
    const p=cutawayLocatorPlacement(slot,stage,clip);
    const actualTop=stage.top+p.top-stage.scrollTop,actualLeft=stage.left+p.left-stage.scrollLeft;
    assert.ok(Math.abs(actualTop-slot.top)<1e-9);assert.equal(actualLeft,slot.left);assert.ok(Math.abs(actualTop+p.clipTop-clip.top)<1e-9);assert.equal(p.visible,true);
  }
});
test('selector clips its bottom and hides completely outside the workspace',()=>{
  const stage={left:0,top:41,scrollTop:27,scrollLeft:0},clip={top:68,bottom:744};
  const bottom=cutawayLocatorPlacement({left:10,top:700,width:320,height:240,bottom:940},stage,clip);assert.equal(bottom.clipBottom,196);assert.equal(bottom.visible,true);
  assert.equal(cutawayLocatorPlacement({left:10,top:-200,width:320,height:240,bottom:40},stage,clip).visible,false);
});
test('layout resize suppression applies only to unchanged cutaway canvas dimensions',()=>{
  let cutaway=true,calls=0;const container={clientWidth:352,clientHeight:240,closest:()=>({querySelector:()=>cutaway?{}:null})},canvas={style:{width:'352px',height:'240px'}};
  const map={getContainer:()=>container,getCanvas:()=>canvas,resize:()=>calls++};
  assert.equal(resizeMapAfterLayout(map),false);container.clientWidth=400;assert.equal(resizeMapAfterLayout(map),true);assert.equal(calls,1);
  canvas.style.width='400px';cutaway=false;assert.equal(resizeMapAfterLayout(map),true);assert.equal(calls,2,'ordinary map behavior stays unchanged');
});
