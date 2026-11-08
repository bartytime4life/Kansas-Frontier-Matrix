import { readBoundedJson } from "../../../bounded-json";
import { validAreaBounds } from "../../../subsurface-model";
import { RESOURCE_SOURCES, oilgasIdsQuery, oilgasPageIds, oilgasRecordsQuery, resourceLocations, resourceQuery, type ResourceKind } from "../../../underground-resources-model";
/** Public source display context, bounded to the chosen local frame. No source admission. */
export async function GET(request:Request){
  const q=new URL(request.url).searchParams,kind=q.get("kind"),bounds=(q.get("bounds")??"").split(",").map(Number);
  const page=q.get("page"),pageNumber=page===null?null:Number(page),limit=pageNumber===null?200:500;
  if((kind!=="oilgas"&&kind!=="minerals")||!validAreaBounds(bounds)||(pageNumber!==null&&(!Number.isSafeInteger(pageNumber)||pageNumber<0||pageNumber>2000)))return Response.json({error:"Choose a local Kansas area and resource type."},{status:400});
  const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),18000),cancel=()=>controller.abort();
  request.signal.addEventListener("abort",cancel,{once:true});if(request.signal.aborted)cancel();
  try{
    // Workers supports manual/follow; reject redirects through the status check.
    const options={signal:controller.signal,redirect:"manual" as const};
    let ids:number[]|undefined;
    if(kind==="oilgas"){
      const idResponse=await fetch(oilgasIdsQuery(bounds),options);
      if(!idResponse.ok)throw new Error("Source unavailable");
      ids=oilgasPageIds(await readBoundedJson(idResponse,5_000_000,controller.signal),(pageNumber??0)*limit,limit);
    }
    const response=ids?.length?await fetch(oilgasRecordsQuery(ids),options):kind==="oilgas"?Response.json({type:"FeatureCollection",features:[]}):await fetch(resourceQuery(kind,bounds,(pageNumber??0)*limit,limit),options);
    if(!response.ok)throw new Error("Source unavailable");
    const source=await readBoundedJson(response,1_000_000,controller.signal);
    if(ids){
      if(!source||typeof source!=="object"||!("features" in source)||!Array.isArray(source.features)||source.features.length!==ids.length)throw new Error("Incomplete source page");
      const received=new Set<number>(),expected=new Set(ids);
      for(const feature of source.features){
        const id=feature?.properties?.OBJECTID;
        if(!expected.has(id)||received.has(id))throw new Error("Unexpected source record");
        received.add(id);
      }
    }
    const result=resourceLocations(source,kind,bounds,limit);
    return Response.json({...result,kind,bounds,retrievedAt:new Date().toISOString(),source:RESOURCE_SOURCES[kind as ResourceKind]},{headers:{"Cache-Control":"private, max-age=900"}});
  }catch{return Response.json({error:"This source is unavailable. Retry or choose another resource type."},{status:502});}
  finally{clearTimeout(timer);request.signal.removeEventListener("abort",cancel);}
}
