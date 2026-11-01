import {localDataWorkerRuntime} from '../../../../../server/local-data.mjs';
// Outbound-only link for the pipeline PC's local-data worker. Not a browser route: every request
// is HMAC-signed by the PC's worker key (server/local-data.mjs, server/home-relay.mjs).
export const dynamic='force-dynamic';
let runtime:ReturnType<typeof localDataWorkerRuntime>|undefined;
async function handle(request:Request){
 try{runtime??=localDataWorkerRuntime();return await runtime(request);}
 catch{return Response.json({reasonCode:'LOCAL_DATA_WORKER_UNAVAILABLE'},{status:503,headers:{'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}});}
}
export const GET=handle;
export const POST=handle;
