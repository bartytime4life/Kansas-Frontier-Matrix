import { pcAiRuntime } from '../../../../server/pc-ai-handler.mjs';
import { pcResearchEvidence } from '../../../pc-ai-evidence';
export const dynamic='force-dynamic';
async function handle(request:Request){
  // Bind the storage namespace to the actual trusted request origin before
  // opening it. Shared/misapplied preview secrets cannot lock the live store.
  if(process.env.KFM_PC_ENABLED==='true'&&new URL(request.url).origin!==process.env.KFM_PC_ORIGIN){
    return Response.json({reasonCode:'PC_AI_ORIGIN_HOLD'},{status:503,headers:{'Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff'}});
  }
  try{return await pcAiRuntime(pcResearchEvidence)(request);}
  catch{return Response.json({reasonCode:'PC_AI_STORAGE_HOLD'},{status:503,headers:{'Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff'}});}
}
export const GET=handle;
export const POST=handle;
