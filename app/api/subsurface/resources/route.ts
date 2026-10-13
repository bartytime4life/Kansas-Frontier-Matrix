import { readBoundedJson } from "../../../bounded-json";
import { validAreaBounds } from "../../../subsurface-model";
import { RESOURCE_SOURCES, resourceLocations, resourceQuery, type ResourceKind } from "../../../underground-resources-model";
/** Public source display context, bounded to the chosen local frame. No source admission. */
export async function GET(request:Request){
  const q=new URL(request.url).searchParams,kind=q.get("kind"),bounds=(q.get("bounds")??"").split(",").map(Number);
  if((kind!=="oilgas"&&kind!=="minerals")||!validAreaBounds(bounds))return Response.json({error:"Choose a local Kansas area and resource type."},{status:400});
  const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),18000),cancel=()=>controller.abort();
  request.signal.addEventListener("abort",cancel,{once:true});if(request.signal.aborted)cancel();
  try{
    // Workers supports manual/follow; reject redirects through the status check.
    const response=await fetch(resourceQuery(kind,bounds),{signal:controller.signal,redirect:"manual"});
    if(!response.ok)throw new Error("Source unavailable");
    const result=resourceLocations(await readBoundedJson(response,1_000_000,controller.signal),kind,bounds);
    return Response.json({...result,kind,bounds,retrievedAt:new Date().toISOString(),source:RESOURCE_SOURCES[kind as ResourceKind]},{headers:{"Cache-Control":"private, max-age=900"}});
  }catch{return Response.json({error:"This source is unavailable. Retry or choose another resource type."},{status:502});}
  finally{clearTimeout(timer);request.signal.removeEventListener("abort",cancel);}
}
