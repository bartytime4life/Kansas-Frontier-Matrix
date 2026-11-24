import {assembleNativeDataset,parseNativeChunk,parseNativeManifest,type NativeChunk,type NativeDataset} from './native-lidar';
export const NATIVE_REPLY_LIMIT=1_000_000,NATIVE_TOTAL_LIMIT=16*1024*1024;
/** Bounded same-origin reader shared by fixed examples and viewport requests. */
export function createNativeReader(caller:AbortSignal,timeoutMs=60_000){
  caller.throwIfAborted();const stop=new AbortController(),signal=AbortSignal.any([caller,stop.signal]);let total=0;
  const timer=setTimeout(()=>stop.abort(new DOMException('LiDAR request timed out','TimeoutError')),timeoutMs);
  async function read(path:string):Promise<unknown>{
    if(!/^\/api\/lidar\/(?:points(?:\/\d+)?|view(?:\?|\/))/.test(path)||path.includes('://'))throw Error('Unsupported LiDAR path');
    signal.throwIfAborted();const response=await fetch(path,{method:'GET',signal,cache:'no-store',credentials:'same-origin',redirect:'error'});
    if(!response.ok){void response.body?.cancel().catch(()=>{});throw new Error('LiDAR is unavailable. Retry this view later.');}
    const declared=Number(response.headers.get('content-length'));if(declared>NATIVE_REPLY_LIMIT){void response.body?.cancel().catch(()=>{});throw new Error('LiDAR reply exceeded its byte limit');}
    if(!response.body)throw new Error('Missing LiDAR response');const reader=response.body.getReader(),decoder=new TextDecoder('utf-8',{fatal:true});let bytes=0,text='';
    const cancel=()=>{void reader.cancel(signal.reason).catch(()=>{});};signal.addEventListener('abort',cancel,{once:true});
    try{for(;;){signal.throwIfAborted();const chunk=await reader.read();signal.throwIfAborted();if(chunk.done)break;bytes+=chunk.value.byteLength;total+=chunk.value.byteLength;if(bytes>NATIVE_REPLY_LIMIT||total>NATIVE_TOTAL_LIMIT)throw new Error('Native LiDAR byte budget exceeded');text+=decoder.decode(chunk.value,{stream:true});}return JSON.parse(text+decoder.decode()) as unknown;}
    catch(error){void reader.cancel().catch(()=>{});throw error;}finally{signal.removeEventListener('abort',cancel);reader.releaseLock();}
  }
  return {read,signal,abort:()=>stop.abort(),dispose:()=>clearTimeout(timer)};
}
export async function readNativeDataset(manifest:NonNullable<ReturnType<typeof parseNativeManifest>>,read:(path:string)=>Promise<unknown>,signal:AbortSignal,pathFor:(id:number)=>string,onProgress?:(loaded:number,total:number)=>void):Promise<NativeDataset>{
  const chunks:NativeChunk[]=new Array(manifest.chunks.length);let next=0,loaded=0;
  async function worker(){for(;;){signal.throwIfAborted();const id=next++;if(id>=manifest.chunks.length)return;const chunk=parseNativeChunk(await read(pathFor(id)),manifest,id);if(!chunk)throw new Error('Native LiDAR chunk failed identity, attribute or count validation');chunks[id]=chunk;loaded+=chunk.points.length;onProgress?.(loaded,manifest.pointCount);}}
  await Promise.all([worker(),worker()]);signal.throwIfAborted();const dataset=assembleNativeDataset(manifest,chunks);if(!dataset)throw new Error('Native LiDAR capture is incomplete or duplicates source records');return dataset;
}
/** Artifact hashes describe upstream pinned files, not cache-enveloped bodies. */
export async function readNativeLidar(caller:AbortSignal,onProgress?:(loaded:number,total:number)=>void):Promise<NativeDataset>{
  const reader=createNativeReader(caller);
  try{const manifest=parseNativeManifest(await reader.read('/api/lidar/points'));if(!manifest||manifest.format!=='kfm-lidar-points-manifest-v1')throw new Error('Native LiDAR manifest failed validation. No points displayed.');return await readNativeDataset(manifest,reader.read,reader.signal,id=>'/api/lidar/points/'+id,onProgress);}
  catch(error){reader.abort();throw error;}finally{reader.dispose();}
}
