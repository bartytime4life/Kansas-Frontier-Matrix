import { IS_PUBLIC_COPY, publicDataAsset, publicAssetLease } from "./public-profile";
import { AQUIFER_VOLUME_ASSETS, buildAquiferVolume, type VolumeBounds } from "./aquifer-volume";
const scope=self as unknown as { onmessage: ((event: MessageEvent<{id:number;bounds:VolumeBounds}>)=>void)|null; postMessage(message:unknown):void; location:{origin:string} };
let controller:AbortController|null=null;
const cache=new Map<string,GeoJSON.FeatureCollection>();
let leaseTimer:ReturnType<typeof setTimeout>|undefined, latestQueryId=0, currentPackage:string|null=null;
let currentLease:{packageId:string;expiresAt:number}|null=null;
async function asset(index:0|1,signal:AbortSignal){
  const item=AQUIFER_VOLUME_ASSETS[index];if(!IS_PUBLIC_COPY&&cache.has(item.url))return cache.get(item.url)!;
  const response=await fetch(IS_PUBLIC_COPY ? publicDataAsset(item.url) : item.url,{signal,redirect:"error",...(IS_PUBLIC_COPY?{cache:"no-store" as const}:{})});if(IS_PUBLIC_COPY){const lease=publicAssetLease(response);if(currentPackage&&currentPackage!==lease.packageId)throw new Error("Public aquifer release changed; retry this area.");currentPackage=lease.packageId;currentLease=lease;clearTimeout(leaseTimer);leaseTimer=setTimeout(()=>{cache.clear();scope.postMessage({id:latestQueryId,error:"Public aquifer release expired; ranges are withheld."});},Math.min(lease.expiresAt-Date.now(),2147483647));}if(!response.ok||!response.body)throw new Error("Aquifer snapshot unavailable");
  const reader=response.body.getReader();let total=0;const chunks:Uint8Array[]=[];
  try{while(true){const {value,done}=await reader.read();if(done)break;total+=value.byteLength;if(total>800000)throw new Error("Aquifer snapshot exceeds limit");chunks.push(value);}}finally{await reader.cancel();reader.releaseLock();}
  const bytes=new Uint8Array(total);let offset=0;for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.length;}
  const digest=Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256",bytes)),b=>b.toString(16).padStart(2,"0")).join("");
  if(digest!==item.sha256)throw new Error("Aquifer snapshot failed integrity verification");
  if(IS_PUBLIC_COPY)publicAssetLease(response);const data=JSON.parse(new TextDecoder().decode(bytes)) as GeoJSON.FeatureCollection;cache.set(item.url,data);return data;
}
scope.onmessage=async(event:MessageEvent<{id:number;bounds:VolumeBounds}>)=>{
  if(event.origin&&event.origin!==self.location.origin)return;
  controller?.abort();const active=new AbortController();controller=active;latestQueryId=event.data.id;if(IS_PUBLIC_COPY){cache.clear();currentPackage=null;currentLease=null;clearTimeout(leaseTimer);}
  const timer=setTimeout(()=>active.abort(),12000);
  try{const [depth,thickness]=await Promise.all([asset(0,active.signal),asset(1,active.signal)]);if(active.signal.aborted)return;
    const volume=buildAquiferVolume(depth,thickness,event.data.bounds);if(!active.signal.aborted)scope.postMessage({id:event.data.id,volume,...(currentLease?{publicLease:currentLease}:{})});
  }catch(error){if(controller===active)scope.postMessage({id:event.data.id,error:active.signal.aborted?"Aquifer preparation timed out. Retry this view.":error instanceof Error?error.message:"Aquifer preparation failed"});}
  finally{clearTimeout(timer);}
};
