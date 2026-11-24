// SQLite's synchronous native work cannot be cancelled by a JS timer in its own thread.
// Use a small process pool: the parent stays responsive and can kill an over-budget read.
import {fork} from 'node:child_process';
import {fileURLToPath} from 'node:url';

export const QUERY_LIMITS=Object.freeze({processes:2,queued:4,executionMs:7000,totalMs:8500,heapMiB:256});
const fail=code=>Object.assign(new Error(code),{code});

export function createQueryPool({databases,limits=QUERY_LIMITS,childFile=new URL('./query-process.mjs',import.meta.url)}){
 const slots=[],queue=[];let sequence=0,closed=false;
 const finish=(job,error,value)=>{
  if(job.done)return;job.done=true;clearTimeout(job.timer);
  job.signal?.removeEventListener('abort',job.onAbort);
  const i=queue.indexOf(job);if(i!==-1)queue.splice(i,1);
  if(error)job.reject(fail(error));else job.resolve(value);
 };
 const stop=slot=>{
  if(slot.stopping)return;slot.stopping=true;slot.child.kill('SIGKILL');
 };
 const start=()=>{
  if(closed||slots.length>=limits.processes)return;
  const child=fork(fileURLToPath(childFile),[],{stdio:['ignore','ignore','ignore','ipc'],env:{},execArgv:['--max-old-space-size='+limits.heapMiB]});
  const slot={child,ready:false,job:null,stopping:false};slots.push(slot);
  child.on('message',message=>{
   if(slot.stopping)return;
   if(message?.ready===true&&!slot.ready){slot.ready=true;pump();return;}
   const job=slot.job;if(!job||message?.id!==job.id)return;
   slot.job=null;
   const code=message.error;
   if(code)finish(job,['QUERY_INVALID','DATASET_NOT_READY','REPLY_TOO_LARGE','DATABASE_UNAVAILABLE'].includes(code)?code:'DATABASE_UNAVAILABLE');
   else finish(job,null,message.value);
   pump();
  });
  child.once('error',()=>{if(slot.job)finish(slot.job,'DATABASE_UNAVAILABLE');stop(slot);});
  child.once('close',()=>{
   if(slot.job)finish(slot.job,'DATABASE_UNAVAILABLE');
   const i=slots.indexOf(slot);if(i!==-1)slots.splice(i,1);
   // A bad installation must fail once, not spawn replacements in a tight loop.
   if(!slot.ready)for(const job of [...queue])finish(job,'DATABASE_UNAVAILABLE');
   if(queue.length&&!closed)pump();
  });
  child.send({kind:'init',databases},error=>{if(error)stop(slot);});
 };
 const pump=()=>{
  if(closed)return;
  for(const slot of slots){
   if(!slot.ready||slot.stopping||slot.job)continue;
   let job;while(queue.length&&!job){const next=queue.shift();if(!next.done)job=next;}
   if(!job)break;
   slot.job=job;job.slot=slot;clearTimeout(job.timer);
   const remaining=limits.totalMs-(Date.now()-job.started);
   job.timer=setTimeout(()=>{finish(job,'QUERY_TIMEOUT');stop(slot);},Math.max(1,Math.min(limits.executionMs,remaining)));
   slot.child.send({id:job.id,operation:job.operation},error=>{if(error&&slot.job===job){finish(job,'DATABASE_UNAVAILABLE');stop(slot);}});
  }
  const pending=queue.filter(j=>!j.done).length,idle=slots.filter(s=>!s.job&&!s.stopping).length;
  if(pending>idle&&slots.length<limits.processes){start();pump();}
 };
 const run=(operation,{signal}={})=>new Promise((resolve,reject)=>{
  if(closed)return reject(fail('DATABASE_UNAVAILABLE'));
  if(signal?.aborted)return reject(fail('QUERY_CANCELLED'));
  if(queue.length>=limits.queued)return reject(fail('QUERY_BUSY'));
  const job={id:++sequence,operation,started:Date.now(),resolve,reject,done:false,timer:null,signal,slot:null};
  job.onAbort=()=>{finish(job,'QUERY_CANCELLED');if(job.slot)stop(job.slot);};
  signal?.addEventListener('abort',job.onAbort,{once:true});
  job.timer=setTimeout(()=>finish(job,'QUERY_BUSY'),limits.totalMs);queue.push(job);pump();
 });
 const close=()=>{
  closed=true;for(const job of [...queue])finish(job,'DATABASE_UNAVAILABLE');
  return Promise.all(slots.map(slot=>new Promise(resolve=>{
   slot.child.once('close',resolve);if(slot.job)finish(slot.job,'DATABASE_UNAVAILABLE');stop(slot);
  })));
 };
 return {run,close,get active(){return slots.filter(s=>s.job&&!s.stopping).length;},get children(){return slots.length;},get queued(){return queue.length;}};
}
