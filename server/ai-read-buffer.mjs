// Process-local admission for source/evidence reads, independent of inference.
export const AI_READ_LIMITS=Object.freeze({active:2,waiting:8,waitMs:1000,windowMs:60000,guestReads:60,processReads:300,guestPending:2,processPending:10});
class AiReadPressure extends Error{
 constructor(code='AI_READ_BUSY',retryAfter=2){super(code);this.retryAfter=retryAfter;}
}
export const isAiReadPressure=error=>error instanceof AiReadPressure;
export function createAiReadBuffer({clock=Date.now}={}){
 let active=0,pending=0,reads=[];const waiting=[],guests=new WeakMap();
 const start=item=>{
  active++;clearTimeout(item.timer);
  // Capacity belongs to the actual resolver, never its caller's timeout race.
  Promise.resolve().then(item.work).then(item.resolve,item.reject).finally(()=>{
   active--;const next=waiting.shift();if(next)start(next);
  });
 };
 return {
  run(work){
   return new Promise((resolve,reject)=>{
    const item={work,resolve,reject};
    if(active<AI_READ_LIMITS.active){start(item);return;}
    if(waiting.length>=AI_READ_LIMITS.waiting){reject(new AiReadPressure());return;}
    item.timer=setTimeout(()=>{const index=waiting.indexOf(item);if(index!==-1){waiting.splice(index,1);reject(new AiReadPressure());}},AI_READ_LIMITS.waitMs);
    waiting.push(item);
   });
  },
  admit(guest){
   const now=clock(),cutoff=now-AI_READ_LIMITS.windowMs;
   reads=reads.filter(at=>at>cutoff);
   let state=guests.get(guest);if(!state){state={reads:[],pending:0};guests.set(guest,state);}
   state.reads=state.reads.filter(at=>at>cutoff);
   if(reads.length>=AI_READ_LIMITS.processReads||state.reads.length>=AI_READ_LIMITS.guestReads){
    const oldest=reads.length>=AI_READ_LIMITS.processReads?reads[0]:state.reads[0];
    throw new AiReadPressure('AI_READ_RATE_LIMIT',Math.max(1,Math.ceil((oldest+AI_READ_LIMITS.windowMs-now)/1000)));
   }
   if(pending>=AI_READ_LIMITS.processPending||state.pending>=AI_READ_LIMITS.guestPending)throw new AiReadPressure();
   reads.push(now);state.reads.push(now);pending++;state.pending++;
   let released=false;return()=>{if(!released){released=true;pending--;state.pending--;}};
  }
 };
}
