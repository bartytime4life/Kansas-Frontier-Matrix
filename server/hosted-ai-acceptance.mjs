import {mkdir,lstat,chmod,readdir,writeFile,readFile} from 'node:fs/promises';
import {join,resolve} from 'node:path';
import {createHash,randomUUID} from 'node:crypto';
import {HostedAiModel,HOSTED_LIMITS,HOSTED_MODEL,hasRepeatedPhrase} from './hosted-ai.mjs';
import {localQwenAnswerHasOverPreciseLocation} from '../scripts/qwen-local-contract.mjs';
export async function qualifyHostedChat({root='/private',discussionProfile='concise-greedy-v1',modelFactory=()=>new HostedAiModel({discussionProfile,modelDirectory:join(root,'kfm-embedded-smollm2-360m-q4-wasm-20261016/model')})}={}){
 if(!['baseline','concise-sampled-v1','concise-greedy-v1'].includes(discussionProfile))throw Error('ACCEPTANCE_PROFILE_INVALID');
 const directory=join(root,'kfm-hosted-smollm2-360m-q4-chat-20261016-'+discussionProfile),rootInfo=await lstat(root);
 if(!rootInfo.isDirectory()||rootInfo.isSymbolicLink())throw Error('ACCEPTANCE_ROOT_UNSAFE');
 try{await mkdir(directory,{mode:0o700});}catch(error){if(error.code!=='EEXIST')throw error;}
 const info=await lstat(directory);if(!info.isDirectory()||info.isSymbolicLink()||info.uid!==process.getuid())throw Error('ACCEPTANCE_DIRECTORY_UNSAFE');
 await chmod(directory,0o700);if((await readdir(directory)).length)throw Error('ACCEPTANCE_ALREADY_ATTEMPTED');
 await writeFile(join(directory,'.attempt'),'kfm.hosted-chat-360m-q4/20261016/v1\n',{flag:'wx',mode:0o600});
 const began=performance.now(),runId=randomUUID(),sources={},checks=[];let model,result;
 for(const path of ['server/hosted-ai.mjs','server/hosted-ai-worker.mjs','server/embedded-ai-model.json','server/public-ai-handler.mjs'])
  sources[path]=createHash('sha256').update(await readFile(resolve(path))).digest('hex');
 // A complete greeting such as "Hello!" is valid; length is not a quality score.
 const valid=reply=>typeof reply?.text==='string'&&reply.text.trim().length>0&&Buffer.byteLength(reply.text)<=4096&&!/https?:\/\/|www\.|\bkfm:/i.test(reply.text)&&!localQwenAnswerHasOverPreciseLocation(reply.text)&&!hasRepeatedPhrase(reply.text);
 const complete=reply=>valid(reply)&&!reply.outputLimited&&/[.!?]["']?\s*$/.test(reply.text);
 try{
  model=modelFactory();await model.loaded;
  const run=async(id,question,qualifies,history=[])=>{
   const started=performance.now();
   const reply=await model.discuss(question,{style:'plain',depth:'brief',history});
   checks.push({id,question,text:valid(reply)?reply.text:null,elapsedMs:Math.round(performance.now()-started),outputLimited:Boolean(reply.outputLimited),qualified:complete(reply)&&qualifies(reply.text)});
   return reply;
  };
  await run('greeting','Say hello in one short sentence.',text=>/\bhello\b/i.test(text)&&text.length<=160&&!/cannot|can.t|don.t|unable|not able/i.test(text)&&(text.match(/[.!?](?:\s|$)/g)??[]).length===1);
  await run('rewrite','Rewrite this as one polite sentence without adding information: "Send the map today."',text=>/\bmap\b/i.test(text)&&/\btoday\b/i.test(text)&&/please|could|would/i.test(text));
  const question='Write one short sentence about a fictional child drawing with a blue marker.';
  const first=await run('story',question,text=>/\bblue\b/i.test(text)&&/\bmarker\b/i.test(text)&&/\bchild\b|\bkid\b/i.test(text));
  await run('followup','Continue that fictional story in one short sentence with the same child flying a red paper kite.',text=>/\bred\b/i.test(text)&&/\bpaper\b/i.test(text)&&/\bkite\b/i.test(text)&&/\bchild\b|\bkid\b/i.test(text),valid(first)?[{question,reply:first.text}]:[]);
  const qualified=checks.length===4&&checks.every(check=>check.qualified);
  result={status:qualified?'HOSTED_DISCUSSION_PASS':'LIMITED',...(qualified?{}:{reason:'DISCUSSION_OUTPUT_UNQUALIFIED'})};
 }catch(error){result={status:'LIMITED',reason:/^[A-Z][A-Z0-9_]{0,63}$/.test(error.code??'')?error.code:'MODEL_UNAVAILABLE'};}
 finally{model?.stop();}
 const receipt={profile:'kfm.hosted-chat-360m-q4/20261016/v1',runId,observedAt:new Date().toISOString(),node:process.versions.node,platform:process.platform,arch:process.arch,model:HOSTED_MODEL,discussionProfile,...result,checks,evidenceSelection:'HELD_UNQUALIFIED',elapsedMs:Math.round(performance.now()-began),peakRssBytes:model?.peakRssBytes??null,limits:HOSTED_LIMITS,sources,scope:'Four fixed greeting/rewriting/fiction/follow-up checks; no real KFM/user data, public fixture route, account access, network inference or paid API.',interpretation:'This is a small bounded quality screen, not general correctness or actual GoDaddy acceptance. Factual selection remains disabled; no released-knowledge acceptance is claimed.'};
 await writeFile(join(directory,'receipt-'+runId+'.json'),JSON.stringify(receipt,null,2)+'\n',{flag:'wx',mode:0o600});
 return receipt;
}
export async function startHostedChatAcceptance(){
 if(process.env.KFM_HOSTED_AI_ACCEPTANCE!=='1')return;
 if(process.env.KFM_HOSTED_AI==='1'){console.info('KFM hosted chat acceptance: requires public chat disabled.');return;}
 try{const receipt=await qualifyHostedChat();console.info('KFM hosted chat acceptance: '+receipt.status+'; private receipt saved.');}
 catch{console.info('KFM hosted chat acceptance: unavailable or already attempted.');}
}
