import {startTerrainPreparationWorker} from './terrain-workers';
import type {PreparedTerrain,TerrainPreparationInput,TerrainPreparationReply} from './terrain-preparation-model';
export const TERRAIN_WORKER_SLOW_MS=1500;
export const TERRAIN_WORKER_TIMEOUT_MS=15000;
type WorkerPort=Pick<Worker,'postMessage'|'terminate'|'onmessage'|'onerror'|'onmessageerror'>;
type Runtime={create:()=>WorkerPort;timer:(fn:()=>void,ms:number)=>ReturnType<typeof setTimeout>;clear:(id:ReturnType<typeof setTimeout>)=>void};
const runtime:Runtime={create:()=>startTerrainPreparationWorker(),timer:(fn,ms)=>globalThis.setTimeout(fn,ms),clear:id=>globalThis.clearTimeout(id)};
type Handlers={ready:(result:PreparedTerrain)=>void;error:(message:string)=>void;slow:()=>void};
let revision=0,active:{cancel:()=>void}|null=null;
function validResult(value:PreparedTerrain,count:number,input:TerrainPreparationInput){
 if(!value||!(value.packed instanceof Float32Array)||value.packed.length%7||value.packed.buffer.byteLength>8_400_000||!(value.eligible instanceof Uint8Array)||value.eligible.length!==count||value.sourceCount!==count||!Number.isInteger(value.eligibleCount)||value.eligibleCount<0||value.eligibleCount>count||!Array.isArray(value.origin)||value.origin.length!==3||!value.origin.every(Number.isFinite))return false;
 if(value.settings?.mode!==input.mode||value.settings?.scale!==input.scale||value.settings?.color!==input.color)return false;
 if(value.eligible.some(v=>v!==0&&v!==1)||value.eligible.reduce((n,v)=>n+v,0)!==value.eligibleCount)return false;
 if(value.analysis&&(!['slope','localRelief','gradients'].every(key=>Array.isArray(value.analysis![key as keyof typeof value.analysis])&&value.analysis![key as keyof typeof value.analysis].length===count)))return false;
 return true;
}
/** Latest job only, including across hook instances in one tab. No CPU fallback. */
export function createTerrainPreparationClient(environment:Runtime=runtime){
 let current:WorkerPort|null=null,job=0,slow:ReturnType<typeof setTimeout>|null=null,deadline:ReturnType<typeof setTimeout>|null=null,disposed=false;
 const cancel=()=>{job=0;if(slow!==null)environment.clear(slow);if(deadline!==null)environment.clear(deadline);slow=deadline=null;if(current){current.onmessage=current.onerror=current.onmessageerror=null;current.terminate();current=null;}if(active?.cancel===cancel)active=null;};
 return {cancel,dispose(){disposed=true;cancel();},prepare(input:TerrainPreparationInput,handlers:Handlers){
  cancel();active?.cancel();if(disposed)return;active={cancel};job=++revision;const id=job;
  const fail=(message:string)=>{if(job!==id)return;cancel();handlers.error(message);};
  try{const worker=environment.create();current=worker;worker.onmessage=(event:MessageEvent<TerrainPreparationReply>)=>{if(job!==id||current!==worker||event.data?.id!==id)return;const reply=event.data;if('error' in reply||!validResult(reply.result,input.grid.width*input.grid.height,input)){fail('This landscape could not be prepared. Source readings and continuous terrain remain available.');return;}const result=reply.result;cancel();handlers.ready(result);};worker.onerror=event=>{event?.preventDefault();fail('Terrain preparation is unavailable on this device. Source readings and continuous terrain remain available.');};worker.onmessageerror=()=>fail('The terrain worker returned an unreadable result. Refresh this view to retry.');slow=environment.timer(()=>{if(job===id)handlers.slow();},TERRAIN_WORKER_SLOW_MS);deadline=environment.timer(()=>fail('Terrain preparation took too long. Continuous terrain and source readings remain available; refresh this view to retry.'),TERRAIN_WORKER_TIMEOUT_MS);worker.postMessage({...input,id});}
  catch{fail('This device cannot start the terrain worker. Continuous terrain and source readings remain available.');}
 }};
}
