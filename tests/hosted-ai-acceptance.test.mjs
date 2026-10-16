import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {qualifyHostedChat} from '../server/hosted-ai-acceptance.mjs';

async function screen(replies){
 const root=await mkdtemp(join(tmpdir(),'kfm-chat-screen-'));
 let stopped=false,index=0;
 const calls=[];
 const model={loaded:Promise.resolve(),peakRssBytes:1,
  async discuss(question,options){calls.push({question,options});return {text:replies[index++],outputLimited:false};},
  stop(){stopped=true;}};
 try{return {receipt:await qualifyHostedChat({root,modelFactory:()=>model}),calls,stopped};}
 finally{await rm(root,{recursive:true,force:true});}
}
const correct=['"Hello, how can I help?"','Please send the map today.','A little girl draws with a blue marker.','The girl then flies a red paper kite.'];
test('quoted single greeting and a little girl satisfy the requested story without rewriting model output',async()=>{
 const {receipt,calls,stopped}=await screen(correct);
 assert.equal(receipt.status,'HOSTED_DISCUSSION_PASS');
 assert.deepEqual(receipt.checks.map(c=>c.text),correct);
 assert.equal(calls[3].options.history[0].reply,correct[2]);
 assert.equal(stopped,true);
});
test('an unchanged imperative still fails the polite rewrite requirement',async()=>{
 const {receipt}=await screen([correct[0],'Send the map today.',...correct.slice(2)]);
 assert.equal(receipt.status,'LIMITED');assert.equal(receipt.checks[1].qualified,false);
});
test('a two-sentence greeting and a follow-up without the kite remain unqualified',async()=>{
 const {receipt}=await screen(['Hello! How can I help?',correct[1],correct[2],'The girl keeps drawing.']);
 assert.equal(receipt.status,'LIMITED');assert.equal(receipt.checks[0].qualified,false);assert.equal(receipt.checks[3].qualified,false);
});
