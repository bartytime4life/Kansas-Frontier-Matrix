import { pipeline, env } from '@huggingface/transformers';
import { createHash } from 'node:crypto';
env.cacheDir='/tmp/kfm-smollm2-qualification-cache';
env.allowLocalModels=false;
const id='HuggingFaceTB/SmolLM2-360M-Instruct';
const response=await fetch('https://huggingface.co/api/models/'+id+'?blobs=true',{signal:AbortSignal.timeout(20000)});
if(!response.ok)throw new Error('MODEL_METADATA_UNAVAILABLE');
const meta=await response.json();
if(meta.cardData?.license!=='apache-2.0'||!/^[a-f0-9]{40}$/.test(meta.sha))throw new Error('MODEL_IDENTITY_UNQUALIFIED');
const names=['config.json','generation_config.json','tokenizer.json','tokenizer_config.json','special_tokens_map.json','onnx/model_q4.onnx','README.md'];
const files=[];
for(const entry of meta.siblings.filter(x=>names.includes(x.rfilename))) {
  const item={path:entry.rfilename,size:entry.size,sha256:entry.lfs?.sha256};
  if(!item.sha256){
    const r=await fetch('https://huggingface.co/'+id+'/resolve/'+meta.sha+'/'+entry.rfilename,{signal:AbortSignal.timeout(20000)});
    if(!r.ok)throw new Error('MODEL_FILE_UNAVAILABLE');
    const data=Buffer.from(await r.arrayBuffer());
    if(data.length>6*1024*1024)throw new Error('MODEL_METADATA_TOO_LARGE');
    item.sha256=createHash('sha256').update(data).digest('hex');
    item.size=data.length;
  }
  files.push(item);
}
console.log('KFM_PINNED_MODEL '+JSON.stringify({id,revision:meta.sha,license:meta.cardData.license,files}));
const start=performance.now();
const pipe=await pipeline('text-generation',id,{revision:meta.sha,device:'cpu',dtype:'q4',session_options:{intraOpNumThreads:1,interOpNumThreads:1,executionMode:'sequential'}});
console.log('KFM_NATIVE_LOAD '+JSON.stringify({loadMs:Math.round(performance.now()-start),rss:process.memoryUsage().rss}));
const began=performance.now();
const out=await pipe([{role:'system',content:'Answer using only the supplied synthetic test sentence.'},{role:'user',content:'Synthetic test: The sample marker is blue. What color is the sample marker? Answer with one word.'}],{max_new_tokens:16,do_sample:false});
console.log('KFM_MODEL_SMOKE '+JSON.stringify({output:out[0].generated_text.at(-1).content,generationMs:Math.round(performance.now()-began),rss:process.memoryUsage().rss}));
await pipe.dispose();
