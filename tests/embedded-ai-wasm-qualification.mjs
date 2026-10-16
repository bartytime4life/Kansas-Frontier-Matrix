// CI-only experiment: not imported by the web application.
import {createHash} from 'node:crypto';
import {mkdir,writeFile} from 'node:fs/promises';
import {join} from 'node:path';
import {performance} from 'node:perf_hooks';
import * as ort from 'onnxruntime-web';
import {Tokenizer} from '@huggingface/tokenizers';
if (process.env.CI !== 'true') throw new Error('CI_ONLY');
const id='HuggingFaceTB/SmolLM2-135M-Instruct';
const meta=await fetch('https://huggingface.co/api/models/'+id+'?blobs=true').then(r=>{if(!r.ok)throw new Error('MODEL_METADATA_UNAVAILABLE');return r.json()});
if(!/^[a-f0-9]{40}$/.test(meta.sha)||meta.cardData?.license!=='apache-2.0')throw new Error('MODEL_IDENTITY');
const paths=['README.md','config.json','generation_config.json','onnx/model_q4.onnx','special_tokens_map.json','tokenizer.json','tokenizer_config.json'];
const directory=join(process.env.RUNNER_TEMP,'smollm2-wasm-ci'); await mkdir(join(directory,'onnx'),{recursive:true});
const files=[],data={};
for(const path of paths){
 const entry=meta.siblings.find(x=>x.rfilename===path);
 if(!entry||entry.size>250000000)throw new Error('MODEL_FILE_METADATA');
 const response=await fetch('https://huggingface.co/'+id+'/resolve/'+meta.sha+'/'+path,{signal:AbortSignal.timeout(120000)});
 if(!response.ok)throw new Error('MODEL_DOWNLOAD');
 const bytes=Buffer.from(await response.arrayBuffer()),sha256=createHash('sha256').update(bytes).digest('hex');
 if(bytes.length!==entry.size || (entry.lfs&&sha256!==entry.lfs.sha256))throw new Error('MODEL_INTEGRITY');
 await writeFile(join(directory,path),bytes,{flag:'wx',mode:0o600});
 files.push({path,size:bytes.length,sha256}); data[path]=path.endsWith('.json')?JSON.parse(bytes):bytes;
}
console.log('KFM_WASM_MODEL_MANIFEST '+JSON.stringify({id,revision:meta.sha,license:meta.cardData.license,files}));
const config=data['config.json'],tc=data['tokenizer_config.json'];
console.log('KFM_WASM_CONFIG '+JSON.stringify({config,chat_template:tc.chat_template,eos_token:tc.eos_token}));
ort.env.wasm.numThreads=1;ort.env.wasm.proxy=false;
console.log('KFM_WASM_IMPORT_PASS');
const began=performance.now();
let session=await ort.InferenceSession.create(new Uint8Array(data['onnx/model_q4.onnx']),{executionProviders:['wasm'],executionMode:'sequential',graphOptimizationLevel:'all'});
console.log('KFM_WASM_LOAD '+JSON.stringify({ms:Math.round(performance.now()-began),rss:process.memoryUsage().rss,inputs:session.inputNames,metadata:session.inputMetadata,outputs:session.outputNames}));
const tokenizer=new Tokenizer(data['tokenizer.json'],tc);
const prompt='<|im_start|>system\nAnswer using only the supplied synthetic test sentence.<|im_end|>\n<|im_start|>user\nSynthetic test: The sample marker is blue. What color is the sample marker? Answer with one word.<|im_end|>\n<|im_start|>assistant\n';
const ids=tokenizer.encode(prompt).ids;const generated=[];
const headDim=config.hidden_size/config.num_attention_heads;
let past={},pastLength=0,current=ids,outputs;
const i64=values=>new ort.Tensor('int64',BigInt64Array.from(values.map(BigInt)),[1,values.length]);
for(const name of session.inputNames){
 if(!['input_ids','attention_mask','position_ids'].includes(name)&&!/^past_key_values\.\d+\.(key|value)$/.test(name))throw new Error('UNKNOWN_MODEL_INPUT');
 if(name.startsWith('past_key_values.'))past[name]=new ort.Tensor('float32',new Float32Array(0),[1,config.num_key_value_heads,0,headDim]);
}
const inferenceBegan=performance.now();
try{
 for(let step=0;step<16;step++){
  const feeds={...past,input_ids:i64(current),attention_mask:i64(Array(pastLength+current.length).fill(1))};
  if(session.inputNames.includes('position_ids'))feeds.position_ids=i64(current.map((_,i)=>pastLength+i));
  outputs=await session.run(feeds);
  const logits=outputs.logits;if(!logits||logits.type!=='float32')throw new Error('LOGITS_FORMAT');
  const vocab=logits.dims.at(-1),offset=logits.data.length-vocab;
  let next=0;for(let i=1;i<vocab;i++)if(logits.data[offset+i]>logits.data[offset+next])next=i;
  for(const tensor of Object.values(feeds))tensor.dispose();
  past={};for(const name of session.inputNames.filter(x=>x.startsWith('past_key_values.'))){
   const outputName=name.replace('past_key_values.','present.');if(!outputs[outputName])throw new Error('KV_OUTPUT_MISSING');
   past[name]=outputs[outputName];delete outputs[outputName];
  }
  for(const tensor of Object.values(outputs))tensor.dispose();
  if([].concat(config.eos_token_id??data['generation_config.json'].eos_token_id).includes(next))break;
  generated.push(next);pastLength+=current.length;current=[next];
 }
 const answer=tokenizer.decode(generated,{skip_special_tokens:true});
 console.log('KFM_WASM_RESULT '+JSON.stringify({answer,inferenceMs:Math.round(performance.now()-inferenceBegan),rss:process.memoryUsage().rss,generatedTokens:generated.length}));
 if(!/\bblue\b/i.test(answer))throw new Error('SYNTHETIC_RESPONSE_UNQUALIFIED');
}finally{for(const tensor of Object.values(past))tensor.dispose();await session.release();}
