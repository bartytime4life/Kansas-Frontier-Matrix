import {localDataRuntime} from '../../../../server/local-data.mjs';
// Public, read-only datasets from the pipeline PC's local databases (server/local-data.mjs,
// scripts/local-data/datasets.mjs). /api/local-data/storm-events keeps its phase 1 reply shape.
export const dynamic='force-dynamic';
let runtime:ReturnType<typeof localDataRuntime>|undefined;
export async function GET(request:Request){
 try{runtime??=localDataRuntime();return await runtime(request);}
 catch{return Response.json({state:'local-data-offline',reasonCode:'LOCAL_DATA_UNAVAILABLE'},{status:503,headers:{'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}});}
}
