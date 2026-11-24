import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';

const source=await readFile('tests/explorer-startup.browser.mjs','utf8');
const ast=ts.createSourceFile('explorer-startup.browser.mjs',source,ts.ScriptTarget.ES2022,true,ts.ScriptKind.JS);
let pressSource;
function visit(node){if(ts.isVariableDeclaration(node)&&node.name.getText(ast)==='press')pressSource=node.initializer.getText(ast);ts.forEachChild(node,visit);}
visit(ast);assert.ok(pressSource);

test('the CI native keyboard action waits for map readiness and real focus ownership before Enter',async()=>{
 for(const delayedReadiness of [true,false]){
  const events=[],document={activeElement:null},close={textContent:'×'};
  const button={disabled:delayedReadiness,textContent:'LiDAR points · off',scrollIntoView(){events.push('scroll');},focus(){events.push(this.disabled?'disabled-focus':'focus');if(!this.disabled&&focusAttempts++>=(delayedReadiness?0:1))document.activeElement=this;}};
  let focusAttempts=0;document.activeElement=close;
  document.querySelectorAll=selector=>{assert.equal(selector,'.category-map-dock button');return [close,button];};
  const evaluate=expression=>new Function('document',`return (${expression});`)(document);
  const p={
   async wait(expression,label){
    assert.match(label,/enabled native action owns keyboard focus/);let ready=false;
    for(let i=0;i<4;i++){if(evaluate(expression)){ready=true;break;}events.push('waiting');button.disabled=false;}
    assert.equal(ready,true);
   },
   async evaluate(expression){return evaluate(expression);},
   async key(key,code,n){assert.equal(key,'Enter');assert.equal(code,'Enter');assert.equal(n,13);assert.equal(button.disabled,false);assert.equal(document.activeElement,button,'the old close/opener must never receive the native-toggle key');events.push('native-key');}
  };
  const press=new Function('p',`return (${pressSource});`)(p);await press('LiDAR points · off');
  assert.ok(events.includes('waiting'),'exercise either delayed map readiness or a competing focus owner');assert.equal(events.includes('disabled-focus'),false);assert.equal(events.at(-1),'native-key');
 }
});

test('exposed native fixture sampling uses the same integer page pixel sent to the real pointer dispatcher',async()=>{
 const {nativeLidarBrowserFixtures}=await import('./native-lidar-browser-fixtures.mjs'),fixtures=await nativeLidarBrowserFixtures(new URL('http://127.0.0.1:5197')),scripts=[];
 await fixtures.setup(async(method,args)=>{if(method==='Page.addScriptToEvaluateOnNewDocument')scripts.push(args.source);});const source=scripts.find(s=>s.includes('window.__nativeFixturePoints='));assert.ok(source);
 const sampled=[],r={left:11.3,top:22.6,width:100,height:100},canvas={getBoundingClientRect:()=>r},window={},document={querySelector:()=>({textContent:'1.0× display'}),elementFromPoint:()=>canvas};
 new Function('window','document',source)(window,document);window.__terrainAcceptanceMap={getLayer:()=>({implementation:{failed:false,pick:point=>{sampled.push(point);return 0;}}}),getCanvas:()=>canvas};window.__nativeFixtureMatrix=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1];const point=window.__nativeVisiblePoint();assert.ok(point);assert.equal(Number.isInteger(point.x),true);assert.equal(Number.isInteger(point.y),true);assert.equal(sampled.at(-1).x,point.x-r.left);assert.equal(sampled.at(-1).y,point.y-r.top);assert.equal(point.record,0);
});
