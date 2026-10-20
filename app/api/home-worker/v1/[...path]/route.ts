import {homeWorkerRuntime} from '../../../../../server/home-inference.mjs';
// Outbound-only link for the home inference PC (KFM_HOME_INFERENCE_TRANSPORT=poll).
// Not a browser route: every request is HMAC-signed by the PC's worker key.
export const dynamic='force-dynamic';
let runtime:ReturnType<typeof homeWorkerRuntime>|undefined;
async function handle(request:Request){
 try{runtime??=homeWorkerRuntime();return await runtime(request);}
 catch{return Response.json({reasonCode:'HOME_WORKER_UNAVAILABLE'},{status:503,headers:{'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}});}
}
export const GET=handle;
export const POST=handle;
