import { pcAiRuntime } from '../../../../server/pc-ai-handler.mjs';
import { pcResearchEvidence } from '../../../pc-ai-evidence';
export const dynamic='force-dynamic';
async function handle(request:Request){
  try{return await pcAiRuntime(pcResearchEvidence)(request);}
  catch{return Response.json({reasonCode:'PC_AI_STORAGE_HOLD'},{status:503,headers:{'Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff'}});}
}
export const GET=handle;
export const POST=handle;
