import { readBoundedJson } from "../../../bounded-json";
import { validAreaBounds } from "../../../subsurface-model";
import type { AreaBounds } from "../../../subsurface-model";
import { RESOURCE_SOURCES, parseMineOperations, resourceCount, resourceCountQuery, resourceLocations, resourceQuery, validResourceCountBounds, type ResourceKind } from "../../../underground-resources-model";
/** Public source display context, bounded to the chosen local frame. No source admission. */
export async function GET(request:Request){
  const q=new URL(request.url).searchParams,kind=q.get("kind"),bounds=(q.get("bounds")??"").split(",").map(Number) as AreaBounds;
  const page=q.get("page"),pageNumber=page===null?null:Number(page),limit=pageNumber===null?200:500,mode=q.get("mode");
  if((kind!=="oilgas"&&kind!=="minerals")||(mode==="count"?!validResourceCountBounds(bounds):!validAreaBounds(bounds))||(mode!==null&&mode!=="count")||(mode==="count"&&pageNumber!==null)||(pageNumber!==null&&(!Number.isSafeInteger(pageNumber)||pageNumber<0||pageNumber>2000)))return Response.json({error:"Choose a local Kansas area and resource type."},{status:400});
  const operations=parseMineOperations(q.get("mineTypes"));
  if(!operations||q.getAll("mineTypes").length>1||(kind!=="minerals"&&q.has("mineTypes")))return Response.json({error:"Choose supported mine operation types."},{status:400});
  const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),18000),cancel=()=>controller.abort();
  request.signal.addEventListener("abort",cancel,{once:true});if(request.signal.aborted)cancel();
  try{
    // Workers supports manual/follow; reject redirects through the status check.
    const response=await fetch(mode==="count"?resourceCountQuery(kind,bounds,operations):resourceQuery(kind,bounds,(pageNumber??0)*limit,limit,operations),{signal:controller.signal,redirect:"manual"});
    if(!response.ok)throw new Error("Source unavailable");
    const value=await readBoundedJson(response,1_000_000,controller.signal);
    if(mode==="count")return Response.json({kind,bounds,count:resourceCount(value),retrievedAt:new Date().toISOString()},{headers:{"Cache-Control":"private, max-age=900"}});
    const result=resourceLocations(value,kind,bounds,limit,operations);
    return Response.json({...result,kind,bounds,retrievedAt:new Date().toISOString(),source:RESOURCE_SOURCES[kind as ResourceKind]},{headers:{"Cache-Control":"private, max-age=900"}});
  }catch{return Response.json({error:"This source is unavailable. Retry or choose another resource type."},{status:502});}
  finally{clearTimeout(timer);request.signal.removeEventListener("abort",cancel);}
}
