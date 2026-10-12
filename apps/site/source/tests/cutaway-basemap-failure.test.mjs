import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
const source=await readFile('app/page.tsx','utf8'),ast=ts.createSourceFile('page.tsx',source,ts.ScriptTarget.Latest,true,ts.ScriptKind.TSX);
const performanceModule={};
vm.runInNewContext(ts.transpileModule(await readFile("app/map-performance.ts","utf8"),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText,{exports:performanceModule});
let handler;
function visit(node){if(ts.isCallExpression(node)&&node.expression.getText(ast)==='map.on'&&node.arguments[0]?.getText(ast)==='"error"')handler=node.arguments[1].getText(ast);ts.forEachChild(node,visit)}visit(ast);assert.ok(handler);
const code=ts.transpileModule(`exports.handle=${handler}`,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
test('a selected aerial tile failure leaves cutaway controls usable with explicit missing coverage',()=>{
 const states=[],exports={};const sourceId='kansas-ng911-2024';
 vm.runInNewContext(code,{...performanceModule,exports,basemapRef:{current:'kansas-aerial'},BASEMAPS:{'kansas-aerial':{style:{sources:{[sourceId]:{type:'raster'}}}}},LAYER_REGISTRY:[],OFFICIAL_CONTEXT_BY_SOURCE_ID:{},officialContextForMapSource:()=>undefined,degradedReason:null,setRuntime:state=>states.push(state)});
 exports.handle({sourceId,error:new Error('private provider URL must never enter UI')});
 assert.equal(states[0].kind,'degraded');assert.match(states[0].message,/Gaps are unknown/);assert.match(states[0].message,/controls and records remain available/);assert.doesNotMatch(states[0].message,/private provider/);
});
