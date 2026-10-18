import test from 'node:test';
import assert from 'node:assert/strict';
import {generateHosted} from '../server/hosted-ai-generation.mjs';
import {HOSTED_CONTEXT_TOKENS} from '../server/hosted-ai-prompt.mjs';

function fixture(length,run){
 const tensors=[],calls=[];
 class Tensor{
  constructor(type,data,dims){Object.assign(this,{type,data,dims,disposed:false});tensors.push(this);}
  dispose(){assert.equal(this.disposed,false,'tensor disposed exactly once');this.disposed=true;}
 }
 const tokenizer={encode:text=>({ids:text==='prefix'?[42]:text?Array(length).fill(7):[]}),decode:ids=>ids.join(',')};
 const session={inputNames:['past_key_values.0.key'],async run(feeds){
  calls.push({ids:[...feeds.input_ids.data].map(Number),mask:feeds.attention_mask.dims[1],positions:[...feeds.position_ids.data].map(Number)});
  const logits=new Tensor('float32',new Float32Array(151936).fill(-Infinity),[1,1,151936]);
  const selected=run?.(calls.length,feeds)??151645;logits.data[selected]=100;
  return {logits,'present.0.key':new Tensor('float32',new Float32Array(1),[1,8,calls.at(-1).mask,128])};
 }};
 return {runtime:{session,tokenizer,ort:{Tensor}},tensors,calls};
}
const cancel=()=>new Int32Array(new SharedArrayBuffer(4));
test('chunked prefill preserves every input, mask, position and cache before decoding',async()=>{
 const f=fixture(130,n=>n===3?42:151645);
 const result=await generateHosted(f.runtime,'prompt',3,cancel());
 assert.deepEqual(result,{text:'42',finishReason:'stop'});
 assert.deepEqual(f.calls.map(c=>c.ids.length),[64,64,2,1]);
 assert.deepEqual(f.calls.map(c=>c.mask),[64,128,130,131]);
 assert.deepEqual(f.calls.flatMap(c=>c.positions),Array.from({length:131},(_,i)=>i));
 assert.ok(f.tensors.every(t=>t.disposed));
});
test('full bounded context uses small prefill allocations and refuses overflow before inference',async()=>{
 const f=fixture(HOSTED_CONTEXT_TOKENS);
 await generateHosted(f.runtime,'prompt',1,cancel());
 assert.equal(f.calls.length,32);assert.ok(f.calls.every(c=>c.ids.length===64));
 assert.ok(f.tensors.every(t=>t.disposed));
 const tooLong=fixture(HOSTED_CONTEXT_TOKENS+1);
 await assert.rejects(()=>generateHosted(tooLong.runtime,'prompt',1,cancel()),/MODEL_CONTEXT_LIMIT/);
 assert.equal(tooLong.calls.length,0);
});
test('cancellation during prefill releases outputs and cached inputs without decoding',async()=>{
 const stop=cancel(),f=fixture(130,()=>{Atomics.store(stop,0,1);return 42;});
 await assert.rejects(()=>generateHosted(f.runtime,'prompt',3,stop),/MODEL_CANCELLED/);
 assert.equal(f.calls.length,1);assert.ok(f.tensors.every(t=>t.disposed));
});
test('token and time exhaustion remain explicit incomplete results',async()=>{
 const f=fixture(2,()=>42);
 assert.deepEqual(await generateHosted(f.runtime,'prompt',2,cancel()),{text:'42,42',finishReason:'token_limit'});
 const timed=fixture(2);
 assert.deepEqual(await generateHosted(timed.runtime,'prompt',2,cancel(),false,0),{text:'',finishReason:'time_limit'});
 assert.equal(timed.calls.length,0);assert.ok(timed.tensors.every(t=>t.disposed));
});
