import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,rm,mkdir,writeFile,symlink} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {qualifyHostedChat,readHostedChatReceipt} from '../server/hosted-ai-acceptance.mjs';

async function screen(replies){
 const root=await mkdtemp(join(tmpdir(),'kfm-chat-screen-'));
 let stopped=false,index=0;
 const calls=[];
 const model={loaded:Promise.resolve(),peakRssBytes:1,
  async discuss(question,options){calls.push({question,options});return {text:replies[index++],outputLimited:false};},
  stop(){stopped=true;}};
 try{const receipt=await qualifyHostedChat({root,modelFactory:()=>model});return {receipt,summary:await readHostedChatReceipt({root}),calls,stopped};}
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
 const {receipt,summary}=await screen([correct[0],'Send the map today.',...correct.slice(2)]);
 assert.equal(receipt.status,'LIMITED');assert.equal(receipt.checks[1].qualified,false);
 assert.equal(summary.reason,'DISCUSSION_OUTPUT_UNQUALIFIED');
 assert.equal(summary.checks[1].qualified,false);
 assert.equal(JSON.stringify(summary).includes('Send the map'),false);
 assert.equal(Object.hasOwn(summary,'sources'),false);
});
test('a two-sentence greeting and a follow-up without the kite remain unqualified',async()=>{
 const {receipt}=await screen(['Hello! How can I help?',correct[1],correct[2],'The girl keeps drawing.']);
 assert.equal(receipt.status,'LIMITED');assert.equal(receipt.checks[0].qualified,false);assert.equal(receipt.checks[3].qualified,false);
});
test('the private receipt reader refuses symbolic links before reading contents',async()=>{
 const root=await mkdtemp(join(tmpdir(),'kfm-chat-receipt-'));
 try{
  const directory=join(root,'kfm-hosted-smollm2-360m-q4-chat-20261016-concise-sampled-v1');
  await mkdir(directory,{mode:0o700});
  const target=join(root,'synthetic-only.json');await writeFile(target,'{}',{mode:0o600});
  await symlink(target,join(directory,'receipt-11111111-1111-1111-1111-111111111111.json'));
  await assert.rejects(()=>readHostedChatReceipt({root}),error=>error.code==='ELOOP');
 }finally{await rm(root,{recursive:true,force:true});}
});

