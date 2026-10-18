import {createHash} from 'node:crypto';
import {HOSTED_CONTEXT_TOKENS} from './hosted-ai-prompt.mjs';
// Bound each prefill's all-token logits rather than allocating the full context.
export const HOSTED_PREFILL_TOKENS=64;
const fail=code=>{throw Object.assign(new Error(code),{code});};
export async function generateHosted({session,tokenizer,ort},prompt,maximum,cancel,sample=false,milliseconds=60000,presencePenalty=0,assistantPrefix=""){
 let finishReason='token_limit';const generationBegan=performance.now();
 const ids=tokenizer.encode(prompt).ids;
 if(ids.length>HOSTED_CONTEXT_TOKENS)fail('MODEL_CONTEXT_LIMIT');
 const owned=new Set(),past={};
 const tensor=(type,data,dims)=>{const t=new ort.Tensor(type,data,dims);owned.add(t);return t;};
 const i64=values=>tensor('int64',BigInt64Array.from(values.map(BigInt)),[1,values.length]);
 for(const name of session.inputNames.filter(name=>name.startsWith('past_key_values.')))past[name]=tensor('float32',new Float32Array(0),[1,8,0,128]);
 let pendingInput=ids,pastLength=0;const generated=[];
 const seen=new Set(tokenizer.encode(assistantPrefix).ids);
 let seed=createHash('sha256').update(prompt).digest().readUInt32LE(0);const random=()=>{seed=(1664525*seed+1013904223)>>>0;return seed/4294967296;};
 try{
  while(generated.length<maximum){
   if(performance.now()-generationBegan>=milliseconds){finishReason='time_limit';break;}
   if(Atomics.load(cancel,0))fail('MODEL_CANCELLED');
   const current=pendingInput.slice(0,HOSTED_PREFILL_TOKENS);
   const feeds={...past,input_ids:i64(current),attention_mask:i64(Array(pastLength+current.length).fill(1)),position_ids:i64(current.map((_,i)=>pastLength+i))};
   const outputs=await session.run(feeds);for(const t of Object.values(outputs))owned.add(t);
   if(Atomics.load(cancel,0))fail('MODEL_CANCELLED');
   const logits=outputs.logits;if(!logits||logits.type!=='float32'||logits.dims.at(-1)!==151936)fail('HOSTED_MODEL_LOGITS');
   const retained=new Set();
   for(const name of Object.keys(past)){const value=outputs[name.replace('past_key_values.','present.')];if(!value)fail('HOSTED_MODEL_CACHE');past[name]=value;retained.add(value);}
   pastLength+=current.length;
   pendingInput=pendingInput.slice(current.length);
   // Prompt chunks only warm the cache. Sample once all prompt tokens are seen.
   if(pendingInput.length){
    for(const t of owned)if(!retained.has(t)){t.dispose();owned.delete(t);}
    continue;
   }
   const offset=logits.data.length-151936;let next=0;
   if(sample){
    const candidates=[];
    for(let id=0;id<151936;id++){
     const score=logits.data[offset+id]-(seen.has(id)?presencePenalty:0);if(!Number.isFinite(score)||candidates.length===20&&score<=candidates.at(-1).score)continue;
     candidates.push({id,score});candidates.sort((a,b)=>b.score-a.score);if(candidates.length>20)candidates.pop();
    }
    if(!candidates.length)fail('HOSTED_MODEL_LOGITS');
    const weights=candidates.map(item=>Math.exp((item.score-candidates[0].score)/0.7));const total=weights.reduce((a,b)=>a+b,0);let kept=0;for(let i=0;i<weights.length;i++){if(kept>=total*0.8)weights[i]=0;else kept+=weights[i];}let choice=random()*kept;next=candidates[weights.findLastIndex(x=>x>0)].id;
    for(let i=0;i<candidates.length;i++){choice-=weights[i];if(choice<=0){next=candidates[i].id;break;}}
   }else for(let i=1;i<151936;i++)if(logits.data[offset+i]>logits.data[offset+next])next=i;
   if(!Number.isFinite(logits.data[offset+next]))fail('HOSTED_MODEL_LOGITS');
   for(const t of owned)if(!retained.has(t)){t.dispose();owned.delete(t);}
   if(next===151645){finishReason='stop';break;}
   generated.push(next);seen.add(next);pendingInput=[next];
  }
  return {text:tokenizer.decode(generated,{skip_special_tokens:true}),finishReason};
 }finally{for(const t of owned)t.dispose();}
}
