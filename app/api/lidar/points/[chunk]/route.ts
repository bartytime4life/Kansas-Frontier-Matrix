import {localLidarPointsRuntime} from '../../../../../server/local-data.mjs';
export const dynamic='force-dynamic';
let runtime:ReturnType<typeof localLidarPointsRuntime>|undefined;
export async function GET(request:Request){
 const id=new URL(request.url).pathname.split('/').pop()??'';
 if(!/^(?:[0-9]|1[0-5])$/.test(id))return Response.json({reasonCode:'QUERY_INVALID'},{status:400,headers:{'Cache-Control':'no-store'}});
 try{runtime??=localLidarPointsRuntime();return await runtime(request,Number(id));}
 catch{return Response.json({state:'local-data-offline',reasonCode:'LIDAR_POINTS_UNAVAILABLE'},{status:503,headers:{'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}});}
}
