import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import {settle} from './component-harness.mjs';

const source=ts.createSourceFile('workspace.tsx',await readFile(new URL('../app/assistant/workspace.tsx',import.meta.url),'utf8'),ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
let effect;
function visit(node){
 if(ts.isCallExpression(node)&&node.expression.getText(source)==='useEffect'&&node.arguments[0]?.getText(source).includes('refresh(controller.signal)')&&node.arguments[0].getText(source).includes('setInterval'))effect=node.arguments[0].getText(source);
 ts.forEachChild(node,visit);
}visit(source);assert.ok(effect,'execute the actual readiness polling effect');
const code=ts.transpileModule(`return ${effect};`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
function harness({hidden=false,active=true,mode='explore'}={}){
 const listeners=new Map(),timers=new Map(),requests=[];let finish;
 const document={hidden,addEventListener:(type,fn)=>listeners.set(type,fn),removeEventListener:type=>listeners.delete(type)};
 const scope={document,active,mode,AbortController,queueMicrotask,setInterval:fn=>{timers.set(1,fn);return 1;},clearInterval:id=>timers.delete(id),refresh:signal=>{requests.push(signal);return new Promise(resolve=>{finish=resolve;});}};
 const cleanup=new Function(...Object.keys(scope),code)(...Object.values(scope))();
 return {document,listeners,timers,requests,cleanup,finish:()=>finish?.()};
}
test('hidden chat makes no readiness requests and resumes once visible',async()=>{
 const p=harness({hidden:true});await settle();assert.equal(p.requests.length,0);p.timers.get(1)();await settle();assert.equal(p.requests.length,0);
 p.document.hidden=false;p.listeners.get('visibilitychange')();await settle();assert.equal(p.requests.length,1);
 p.timers.get(1)();p.listeners.get('visibilitychange')();await settle();assert.equal(p.requests.length,1,'slow readiness reads must not overlap');
 p.finish();await settle();p.document.hidden=true;p.timers.get(1)();await settle();assert.equal(p.requests.length,1);
 p.cleanup();assert.equal(p.listeners.size,0);assert.equal(p.timers.size,0);assert.equal(p.requests[0].aborted,true);
});
test('Find mode and closed chat never start readiness polling',async()=>{
 for(const options of [{mode:'find'},{active:false}]){const p=harness(options);await settle();assert.equal(p.timers.size,0);assert.equal(p.requests.length,0);assert.equal(p.listeners.size,0);assert.equal(p.cleanup,undefined);}
});
