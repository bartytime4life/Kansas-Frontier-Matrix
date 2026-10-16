import {publicAiRuntime} from '../../../../server/public-ai-handler.mjs';
import {pcResearchEvidence} from '../../../pc-ai-evidence';
export const dynamic='force-dynamic';
async function handle(request:Request){
 if(process.env.KFM_HOSTED_AI==='1'&&new URL(request.url).origin!==process.env.KFM_HOSTED_AI_ORIGIN)
  return Response.json({reasonCode:'AI_ORIGIN_HOLD'},{status:503,headers:{'Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff'}});
 try{return await publicAiRuntime(pcResearchEvidence)(request);}
 catch{return Response.json({reasonCode:'AI_UNAVAILABLE'},{status:503,headers:{'Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff'}});}
}
export const GET=handle;
export const POST=handle;
