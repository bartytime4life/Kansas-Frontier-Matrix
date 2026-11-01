import {localDataStormEventsRuntime} from '../../../../server/local-data.mjs';
// Public, read-only Kansas storm events from the pipeline PC's local database (server/local-data.mjs).
export const dynamic='force-dynamic';
let runtime:ReturnType<typeof localDataStormEventsRuntime>|undefined;
export async function GET(request:Request){
 try{runtime??=localDataStormEventsRuntime();return await runtime(request);}
 catch{return Response.json({state:'local-data-offline',reasonCode:'LOCAL_DATA_UNAVAILABLE'},{status:503,headers:{'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}});}
}
