import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';
const compile = async path => ts.transpileModule(await readFile(path, 'utf8'), {compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const url = value => `data:text/javascript;base64,${Buffer.from(value).toString('base64')}`;
const model = await import(url(await compile('app/cache-budget.ts')));
const snapshot = (limitBytes=500e9) => ({schema:'kfm-local-cache-budget/v1',limitBytes,defaultLimitBytes:500e9,usedBytes:3,temporaryBytes:1,replaceableBytes:2,freeBytes:900e9,reserveBytes:1e6,sessionToken:'a'.repeat(43),busy:false});
test('decimal budgets accept above 500 GB without rounding and reject invalid or unsafe amounts',()=>{
 for (const [input,expected] of [['250',250e9],['1000',1e12],['2000.25',2000250000000],['0.000000001',1],['9007199.254740991',Number.MAX_SAFE_INTEGER]]) {assert.equal(model.cacheBudgetBytes(input),expected);assert.equal(model.cacheBudgetBytes(model.cacheBudgetGb(expected)),expected);}
 for (const input of ['','0','-1','1e3','Infinity','NaN','2.1234567891','9007199.254740992','99999999999999']) assert.equal(model.cacheBudgetBytes(input),null);
 assert.ok(model.parseCacheBudget(snapshot(1e12)));assert.ok(model.parseCacheBudget(snapshot(1)),'over-budget use stays visible');
 for (const patch of [{limitBytes:0},{limitBytes:true},{limitBytes:Number.MAX_SAFE_INTEGER+1},{replaceableBytes:4},{sessionToken:'bad'}]) assert.equal(model.parseCacheBudget({...snapshot(),...patch}),null);
});
test('save persists the exact selected value, refreshes status, and survives a remount',async()=>{
 let persisted=500e9,saves=0,refreshes=0;const calls=[];
 const create=async()=>{
  const h=await componentHarness('app/local-cache-settings.tsx',{'./cache-budget':model,'./local-cache-settings.module.css':{default:{}},'./local-download-client':{
   automaticLocalConnection:()=>true,formatDownloadBytes:String,
   localDownloadRequest:async(path,signal,payload,token)=>{calls.push({path,payload,token});if(payload){persisted=payload.limitBytes;saves++;}return {response:{ok:true},body:{...snapshot(persisted),busy:true}};}
  }},{window:{location:{origin:'http://127.0.0.1:4173'}}});
  const render=()=>h.render(h.exports.default,{onSaved:()=>refreshes++});render();h.commit();await settle();return {h,render};
 };
 const {h,render}=await create();let tree=render();
 findNode(tree,n=>n.type==='input').props.onChange({target:{value:'1000'}});tree=render();
 assert.equal(findNode(tree,n=>n.type==='button'&&n.props.type==='submit').props.disabled,false,'active transfers do not block a future budget change');
 findNode(tree,n=>n.type==='form').props.onSubmit({preventDefault(){}});await settle();
 assert.equal(persisted,1e12);assert.equal(saves,1);assert.equal(refreshes,1);assert.equal(calls.at(-1).token,'a'.repeat(43));
 findNode(render(),n=>n.type==='input').props.onChange({target:{value:'250'}});findNode(render(),n=>n.type==='form').props.onSubmit({preventDefault(){}});await settle();
 assert.equal(persisted,250e9);h.dispose();
 const next=await create();assert.equal(findNode(next.render(),n=>n.type==='input').props.value,'250');next.h.dispose();
});
test('legacy jobs remain visible after a budget reduction while new selections respect the saved budget',async()=>{
 const bounded=url(await compile('app/bounded-json.ts'));const catalogUrl=url(await compile('app/public-map-catalog.ts'));
 const client=await import(url((await compile('app/public-map-client.ts')).replace('"./bounded-json"',JSON.stringify(bounded)).replace('"./public-map-catalog"',JSON.stringify(catalogUrl))));
 const job={id:'a'.repeat(32),assetId:'file',title:'Previously selected',state:'cancelled',bytes:5,expectedBytes:null,maxBytes:1e12,sha256:null,destination:'/local',reason:null,mapReady:false,createdAt:'2026-10-09T00:00:00Z',updatedAt:'2026-10-09T00:00:00Z'};
 assert.ok(client.parsePublicMapStatus({schema:'kfm-public-map-download-control/v1',sessionToken:'a'.repeat(43),active:null,limitBytes:250e9,jobs:[job],refresh:{state:'idle'}}));
 const catalog=await import(catalogUrl);assert.equal(catalog.publicMapSelectedLimit('600000',{expectedBytes:null},250e9),null);assert.ok(catalog.publicMapSelectedLimit('600000',{expectedBytes:null},1e12));
 const acquisition=await import(url(await compile('app/acquisition-inventory.ts')));
 const inventory={schema_version:'kfm-acquisition-inventory-v1',lifecycle:'candidate-only',generated_at:'2026-10-09T00:00:00Z',cache:{limit_bytes:1,used_bytes:0,temporary_bytes:0,replaceable_bytes:0,budget_scope:'new-cache-transfers'},jobs:[]};
 assert.equal(acquisition.parseAcquisitionInventory(inventory).cache.budget_scope,'new-cache-transfers');
});
