/// <reference lib="webworker" />
import { AQUIFER_VOLUME_ASSETS, buildAquiferVolume, type VolumeBounds } from "./aquifer-volume";
const scope=self as unknown as DedicatedWorkerGlobalScope;
let controller:AbortController|null=null;
const cache=new Map<string,GeoJSON.FeatureCollection>();
async function asset(index:0|1,signal:AbortSignal){
  const item=AQUIFER_VOLUME_ASSETS[index];if(cache.has(item.url))return cache.get(item.url)!;
  const response=await fetch(item.url,{signal,redirect:"error"});if(!response.ok||!response.body)throw new Error("Aquifer snapshot unavailable");
  const reader=response.body.getReader();let total=0;const chunks:Uint8Array[]=[];
  try{while(true){const {value,done}=await reader.read();if(done)break;total+=value.byteLength;if(total>800000)throw new Error("Aquifer snapshot exceeds limit");chunks.push(value);}}finally{await reader.cancel();reader.releaseLock();}
  const bytes=new Uint8Array(total);let offset=0;for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.length;}
  const digest=Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",bytes)),b=>b.toString(16).padStart(2,"0")).join("");
  if(digest!==item.sha256)throw new Error("Aquifer snapshot failed integrity verification");
  const data=JSON.parse(new TextDecoder().decode(bytes)) as GeoJSON.FeatureCollection;cache.set(item.url,data);return data;
}
scope.onmessage=async(event:MessageEvent<{id:number;bounds:VolumeBounds}>)=>{
  controller?.abort();const active=new AbortController();controller=active;
  const timer=setTimeout(()=>active.abort(),12000);
  try{const [depth,thickness]=await Promise.all([asset(0,active.signal),asset(1,active.signal)]);if(active.signal.aborted)return;
    const volume=buildAquiferVolume(depth,thickness,event.data.bounds);if(!active.signal.aborted)scope.postMessage({id:event.data.id,volume});
  }catch(error){if(controller===active)scope.postMessage({id:event.data.id,error:active.signal.aborted?"Aquifer preparation timed out. Retry this view.":error instanceof Error?error.message:"Aquifer preparation failed"});}
  finally{clearTimeout(timer);}
};
