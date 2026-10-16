import {mkdir,lstat,chmod,readdir,writeFile,readFile} from 'node:fs/promises';
import {join,resolve} from 'node:path';
import {createHash,randomUUID} from 'node:crypto';
import {HostedAiModel,HOSTED_LIMITS,HOSTED_MODEL} from './hosted-ai.mjs';
export async function qualifyHostedChat({root='/private',modelFactory=()=>new HostedAiModel({modelDirectory:join(root,'kfm-embedded-smollm2-wasm-20261016/model')})}={}){
 const directory=join(root,'kfm-hosted-smollm2-chat-20261016'),rootInfo=await lstat(root);
 if(!rootInfo.isDirectory()||rootInfo.isSymbolicLink())throw Error('ACCEPTANCE_ROOT_UNSAFE');
 try{await mkdir(directory,{mode:0o700});}catch(error){if(error.code!=='EEXIST')throw error;}
 const info=await lstat(directory);if(!info.isDirectory()||info.isSymbolicLink()||info.uid!==process.getuid())throw Error('ACCEPTANCE_DIRECTORY_UNSAFE');
 await chmod(directory,0o700);if((await readdir(directory)).length)throw Error('ACCEPTANCE_ALREADY_ATTEMPTED');
 await writeFile(join(directory,'.attempt'),'kfm.hosted-chat/20261016/v2\n',{flag:'wx',mode:0o600});
 const began=performance.now(),runId=randomUUID(),sources={};let model,result;
 for(const path of ['server/hosted-ai.mjs','server/hosted-ai-worker.mjs','server/embedded-ai-model.json','server/public-ai-handler.mjs'])
  sources[path]=createHash('sha256').update(await readFile(resolve(path))).digest('hex');
 try{
  model=modelFactory();await model.loaded;
  const positive=await model.select('What color is the sample marker?',['The sample marker is blue.','The garden gate is red.']);
  const secondPositive=await model.select('What color is the garden gate?',['The sample marker is blue.','The garden gate is red.']);
  const unsupported=await model.select('In what year was the train built?',['The sample marker is blue.','The garden gate is red.']);
  result={status:positive===1&&secondPositive===2&&(unsupported===0||unsupported===null)?'HOSTED_SELECTION_PASS':'LIMITED',positiveSelection:positive,secondPositiveSelection:secondPositive,unsupportedSelection:unsupported,...(positive===1&&unsupported===0?{}:{reason:'MODEL_SELECTION_UNQUALIFIED'})};
 }catch(error){result={status:'LIMITED',reason:/^[A-Z][A-Z0-9_]{0,63}$/.test(error.code??'')?error.code:'MODEL_UNAVAILABLE'};}
 finally{model?.stop();}
 const receipt={profile:'kfm.hosted-chat/20261016/v2',runId,observedAt:new Date().toISOString(),node:process.versions.node,platform:process.platform,arch:process.arch,model:HOSTED_MODEL,...result,elapsedMs:Math.round(performance.now()-began),peakRssBytes:model?.peakRssBytes??null,limits:HOSTED_LIMITS,sources,scope:'Three fixed synthetic selection/withholding checks; no real KFM/user data, public fixture route, account access, network inference or paid API.',interpretation:'This is bounded runtime/selection evidence, not general model-quality acceptance or a released-knowledge answer.'};
 await writeFile(join(directory,'receipt-'+runId+'.json'),JSON.stringify(receipt,null,2)+'\n',{flag:'wx',mode:0o600});
 return receipt;
}
export async function startHostedChatAcceptance(){
 if(process.env.KFM_HOSTED_AI_ACCEPTANCE!=='1')return;
 if(process.env.KFM_HOSTED_AI==='1'){console.info('KFM hosted chat acceptance: requires public chat disabled.');return;}
 try{const receipt=await qualifyHostedChat();console.info('KFM hosted chat acceptance: '+receipt.status+'; private receipt saved.');}
 catch{console.info('KFM hosted chat acceptance: unavailable or already attempted.');}
}
