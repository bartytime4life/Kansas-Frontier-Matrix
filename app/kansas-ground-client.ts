import {groundPath,groundRequestKey,parseGroundReceipt,type GroundQuery,type GroundReceipt} from './kansas-ground';
const LIMIT=1_000_000;
const pause=(signal:AbortSignal)=>new Promise<void>((resolve,reject)=>{const abort=()=>{clearTimeout(timer);reject(signal.reason);},timer=setTimeout(()=>{signal.removeEventListener('abort',abort);resolve();},2000);signal.addEventListener('abort',abort,{once:true});if(signal.aborted)abort();});
/** One bounded provider-DEM request; never requests EPT or native point chunks. */
export async function readKansasGround(query:GroundQuery,caller:AbortSignal,onReceipt?:(receipt:GroundReceipt)=>void):Promise<GroundReceipt>{
 caller.throwIfAborted();const stop=new AbortController(),signal=AbortSignal.any([caller,stop.signal]),timeout=setTimeout(()=>stop.abort(new DOMException('Ground request timed out','TimeoutError')),145000),deadline=Date.now()+120000;let total=0;
 try{
  const key=await groundRequestKey(query);signal.throwIfAborted();
  for(;;){
   const response=await fetch(groundPath(query),{method:'GET',signal,cache:'no-store',credentials:'same-origin',redirect:'error'});
   if(!response.ok){void response.body?.cancel().catch(()=>{});throw Error('Ground grid unavailable. Continuous elevation context remains available.');}
   if(Number(response.headers.get('content-length'))>LIMIT){void response.body?.cancel().catch(()=>{});throw Error('Ground reply exceeded its byte limit.');}
   if(!response.body)throw Error('Missing Ground response.');const reader=response.body.getReader(),decoder=new TextDecoder('utf-8',{fatal:true});let bytes=0,text='';
   const abort=()=>{void reader.cancel(signal.reason).catch(()=>{});};signal.addEventListener('abort',abort,{once:true});
   try{for(;;){signal.throwIfAborted();const chunk=await reader.read();signal.throwIfAborted();if(chunk.done)break;bytes+=chunk.value.byteLength;total+=chunk.value.byteLength;if(bytes>LIMIT||total>16*1024*1024)throw Error('Ground byte budget exceeded.');text+=decoder.decode(chunk.value,{stream:true});}text+=decoder.decode();}
   catch(error){void reader.cancel().catch(()=>{});throw error;}finally{signal.removeEventListener('abort',abort);reader.releaseLock();}
   const receipt=parseGroundReceipt(JSON.parse(text),query,key);if(!receipt)throw Error('Ground grid failed query, footprint or source validation.');signal.throwIfAborted();onReceipt?.(receipt);signal.throwIfAborted();
   if(receipt.state!=='processing'||Date.now()>=deadline)return receipt;
   await pause(signal);
  }
 }catch(error){stop.abort();throw error;}finally{clearTimeout(timeout);}
}
