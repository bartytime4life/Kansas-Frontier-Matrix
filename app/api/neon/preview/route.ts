import {localNeonPreviewRuntime} from '../../../../server/local-data.mjs';
export const dynamic='force-dynamic';
let runtime:ReturnType<typeof localNeonPreviewRuntime>|undefined;
export async function GET(request:Request){
 try{runtime??=localNeonPreviewRuntime();return await runtime(request);}
 catch{return Response.json({state:'local-data-offline',reasonCode:'NEON_PREVIEW_UNAVAILABLE'},{status:503,headers:{'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}});}
}
