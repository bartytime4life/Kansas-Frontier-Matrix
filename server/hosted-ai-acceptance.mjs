import {mkdir,lstat,chmod,readdir,writeFile,readFile} from 'node:fs/promises';
import {join,resolve} from 'node:path';
import {createHash,randomUUID} from 'node:crypto';
import {HostedAiModel,HOSTED_LIMITS,HOSTED_MODEL,hasRepeatedPhrase} from './hosted-ai.mjs';
import {localQwenAnswerHasOverPreciseLocation} from '../scripts/qwen-local-contract.mjs';
export async function qualifyHostedChat({root='/private',modelFactory=()=>new HostedAiModel({modelDirectory:join(root,'kfm-embedded-smollm2-wasm-20261016/model')})}={}){
 const directory=join(root,'kfm-hosted-smollm2-chat-20261016'),rootInfo=await lstat(root);
 if(!rootInfo.isDirectory()||rootInfo.isSymbolicLink())throw Error('ACCEPTANCE_ROOT_UNSAFE');
 try{await mkdir(directory,{mode:0o700});}catch(error){if(error.code!=='EEXIST')throw error;}
 const info=await lstat(directory);if(!info.isDirectory()||info.isSymbolicLink()||info.uid!==process.getuid())throw Error('ACCEPTANCE_DIRECTORY_UNSAFE');
 await chmod(directory,0o700);if((await readdir(directory)).length)throw Error('ACCEPTANCE_ALREADY_ATTEMPTED');
 await writeFile(join(directory,'.attempt'),'kfm.hosted-chat/20261016/v3\n',{flag:'wx',mode:0o600});
 const began=performance.now(),runId=randomUUID(),sources={};let model,result;
 for(const path of ['server/hosted-ai.mjs','server/hosted-ai-worker.mjs','server/embedded-ai-model.json','server/public-ai-handler.mjs'])
  sources[path]=createHash('sha256').update(await readFile(resolve(path))).digest('hex');
 const valid=reply=>typeof reply?.text==='string'&&reply.text.trim().length>=10&&Buffer.byteLength(reply.text)<=4096&&!/https?:\/\/|www\.|\bkfm:/i.test(reply.text)&&!localQwenAnswerHasOverPreciseLocation(reply.text)&&!hasRepeatedPhrase(reply.text);
 try{
  model=modelFactory();await model.loaded;
  const question='Suggest one short fictional story idea involving a blue marker.';
  const first=await model.discuss(question,{style:'plain',depth:'brief',history:[]});
  const followup=await model.discuss('Now suggest a different fictional story idea involving a red kite.',{style:'plain',depth:'brief',history:valid(first)?[{question,reply:first.text}]:[]});
  const qualified=valid(first)&&valid(followup)&&/marker/i.test(first.text)&&/kite/i.test(followup.text)&&first.text.trim()!==followup.text.trim();
  result={status:qualified?'HOSTED_DISCUSSION_PASS':'LIMITED',syntheticDiscussion:valid(first)?first.text:null,syntheticFollowup:valid(followup)?followup.text:null,evidenceSelection:'HELD_UNQUALIFIED',...(qualified?{}:{reason:'DISCUSSION_OUTPUT_UNQUALIFIED'})};
 }catch(error){result={status:'LIMITED',reason:/^[A-Z][A-Z0-9_]{0,63}$/.test(error.code??'')?error.code:'MODEL_UNAVAILABLE'};}
 finally{model?.stop();}
 const receipt={profile:'kfm.hosted-chat/20261016/v3',runId,observedAt:new Date().toISOString(),node:process.versions.node,platform:process.platform,arch:process.arch,model:HOSTED_MODEL,...result,elapsedMs:Math.round(performance.now()-began),peakRssBytes:model?.peakRssBytes??null,limits:HOSTED_LIMITS,sources,scope:'Two fixed fictional discussion/follow-up checks; no real KFM/user data, public fixture route, account access, network inference or paid API.',interpretation:'This qualifies bounded unverified discussion only. Model evidence-selection failed separately and remains disabled; no released-knowledge or general model-quality acceptance is claimed.'};
 await writeFile(join(directory,'receipt-'+runId+'.json'),JSON.stringify(receipt,null,2)+'\n',{flag:'wx',mode:0o600});
 return receipt;
}
export async function startHostedChatAcceptance(){
 if(process.env.KFM_HOSTED_AI_ACCEPTANCE!=='1')return;
 if(process.env.KFM_HOSTED_AI==='1'){console.info('KFM hosted chat acceptance: requires public chat disabled.');return;}
 try{const receipt=await qualifyHostedChat();console.info('KFM hosted chat acceptance: '+receipt.status+'; private receipt saved.');}
 catch{console.info('KFM hosted chat acceptance: unavailable or already attempted.');}
}
