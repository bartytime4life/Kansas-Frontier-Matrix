import {localLidarViewArtifactRuntime} from "../../../../../../server/local-data.mjs";
export async function GET(request:Request){
 const segments=new URL(request.url).pathname.split("/"),key=segments.at(-2)??"",part=segments.at(-1)??"";
 if(!/^[a-f0-9]{64}$/.test(key)||!(part==="grid"||/^(?:[0-9]|1[0-5])$/.test(part)))return Response.json({reasonCode:"QUERY_INVALID"},{status:400});
 return localLidarViewArtifactRuntime()(request,key,part==="grid"?"grid":Number(part));
}
