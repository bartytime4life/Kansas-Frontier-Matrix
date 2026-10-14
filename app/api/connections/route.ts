import {catalog,captureOne,inputJson,replay} from "../../api-connections-runtime/connections.mjs";
import {hash,ConnectionError} from "../../api-connections-runtime/http-runtime.mjs";
import {connectionEnvironment,connectionOwner,connectionSameOrigin,connectionStore,connectionHostStatus,requireConnectionCapture} from "../../api-connection-host";
export const dynamic="force-dynamic";
const headers={"Cache-Control":"private, no-store","X-Content-Type-Options":"nosniff","Referrer-Policy":"no-referrer"};
const json=(value:unknown,status=200)=>Response.json(value,{status,headers});
const failure=(error:unknown)=>json({error:error instanceof ConnectionError?error.code:"HOST_OR_CAPTURE_UNAVAILABLE",boundary:"No source admission or release."},error instanceof ConnectionError?error.status:503);
export async function GET(request:Request){
 try {
  const p=new URL(request.url).searchParams;
  if([...p.keys()].some(k=>!["action","id"].includes(k)||p.getAll(k).length!==1))return json({error:"QUERY_REJECTED"},400);
  const action=p.get("action")??"catalog";
  if(!["catalog","captures","view","entity","bundle"].includes(action)||action==="catalog"&&p.has("id"))return json({error:"QUERY_REJECTED"},400);
  if(action==="catalog")return json({sources:catalog(connectionEnvironment()),host:await connectionHostStatus(),owner:await connectionOwner(request)});
  if(!await connectionOwner(request))return json({error:"OWNER_ACCESS_REQUIRED"},401);
  const store=await connectionStore();
  if(action==="captures"){if(p.has("id"))return json({error:"QUERY_REJECTED"},400);return json({captures:(await store.list()).filter((x:{format?:string})=>x.format==="kfm-api-connections-v1"),releaseState:"unreleased"});}
  const id=p.get("id")??"";if(!/^[a-f0-9]{64}$/.test(id))return json({error:"QUERY_REJECTED"},400);
  const capture=await store.read(id);
  if(action==="bundle"){
   if(await hash(capture.bytes)!==capture.receipt.sha256)return json({error:"CAPTURE_INTEGRITY_FAILED"},503);
   return new Response(capture.bytes as Uint8Array<ArrayBuffer>,{headers:{...headers,"Content-Type":"application/octet-stream","Content-Disposition":'attachment; filename="kfm-quarantine-'+id+'.json"',"Content-Security-Policy":"sandbox"}});
  }
  const result=await replay(capture);
  if(action==="view")return json({view:result.view,receipt:result.receipt});
  if(!result.entity)return json({error:"CAPTURE_VALIDATION_HELD"},409);
  return new Response(result.entity.bytes as Uint8Array<ArrayBuffer>,{headers:{...headers,"Content-Type":result.entity.format==="png"?"image/png":"application/octet-stream","Content-Disposition":(result.entity.format==="png"?"inline":"attachment")+'; filename="kfm-source-'+id+'.'+result.entity.format+'"',"Content-Security-Policy":"sandbox"}});
 }catch(error){return failure(error);}
}
export async function POST(request:Request){
 try{
  if(!connectionSameOrigin(request)||!await connectionOwner(request))return json({error:"OWNER_ACCESS_REQUIRED"},401);
  const p=new URL(request.url).searchParams;if(p.size)return json({error:"QUERY_REJECTED"},400);
  const body=await inputJson(request);
  if(!body||Object.keys(body).some(k=>!["sourceId","query"].includes(k))||typeof body.sourceId!=="string")return json({error:"QUERY_REJECTED"},400);
  await requireConnectionCapture();
  const result=await captureOne(await connectionStore(),body.sourceId,body.query,{env:connectionEnvironment(),signal:request.signal});
  return json({view:result.view,receipt:result.receipt,cached:result.cached});
 }catch(error){return failure(error);}
}
