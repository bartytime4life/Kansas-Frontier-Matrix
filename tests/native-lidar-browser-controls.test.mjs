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
