import {localLidarPointsRuntime} from '../../../../server/local-data.mjs';
export const dynamic='force-dynamic';
let runtime:ReturnType<typeof localLidarPointsRuntime>|undefined;
export async function GET(request:Request){
 try{runtime??=localLidarPointsRuntime();return await runtime(request);}
 catch{return Response.json({state:'local-data-offline',reasonCode:'LIDAR_POINTS_UNAVAILABLE'},{status:503,headers:{'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}});}
}
