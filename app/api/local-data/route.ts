import {localDataCatalogRuntime} from '../../../server/local-data.mjs';
// What the pipeline PC's local databases can answer, and whether the PC is connected.
export const dynamic='force-dynamic';
let runtime:ReturnType<typeof localDataCatalogRuntime>|undefined;
export async function GET(request:Request){
 try{runtime??=localDataCatalogRuntime();return await runtime(request);}
 catch{return Response.json({reasonCode:'LOCAL_DATA_UNAVAILABLE'},{status:503,headers:{'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}});}
}
