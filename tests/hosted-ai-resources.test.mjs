import test from 'node:test';
import assert from 'node:assert/strict';
import {readHostedResourceSnapshot,reportHostedResources} from '../server/hosted-ai-resources.mjs';
test('disabled probe performs no read or write',()=>{
 let calls=0;assert.deepEqual(reportHostedResources(false,()=>{calls++;},()=>{calls++;}),{status:'DISABLED'});assert.equal(calls,0);
});
test('unknown and failed observations never imply unlimited capacity',()=>{
 const report=readHostedResourceSnapshot({runtime:{constrainedMemory:()=>0,availableMemory:()=>{throw Error('private');},memoryUsage:()=>({rss:Infinity})},now:()=> 'fixed'});
 assert.equal(report.constrainedMemoryBytes,null);assert.equal(report.availableMemoryBytes,null);assert.equal(report.processRssBytes,null);assert.equal(JSON.stringify(report).includes('private'),false);
});
test('report contains selected fields, not environment or unrelated telemetry',()=>{
 const runtime={versions:{node:'22'},platform:'linux',arch:'x64',env:{SECRET:'never-copy'},constrainedMemory:()=>4*1024**3,availableMemory:()=>3*1024**3,memoryUsage:()=>({rss:100,secret:'never-copy'})};
 const report=readHostedResourceSnapshot({runtime,now:()=> 'fixed'});
 assert.equal(report.constrainedMemoryBytes,4*1024**3);assert.equal(report.processRssBytes,100);assert.equal(JSON.stringify(report).includes('never-copy'),false);assert.equal('env' in report,false);
});
test('diagnostic failure is bounded and omits raw errors',()=>{
 const logs=[];assert.deepEqual(reportHostedResources(true,()=>{throw Error('private path');},v=>logs.push(v)),{status:'UNAVAILABLE'});assert.deepEqual(logs,['KFM_HOSTED_RESOURCE_REPORT_UNAVAILABLE']);
});
