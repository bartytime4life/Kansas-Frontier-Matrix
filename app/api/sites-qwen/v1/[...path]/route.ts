import {createSitesQwenHandler} from '../../../../../server/sites-qwen-handler.mjs';
import {GET as publicQwen} from '../../../ai/[...path]/route';
export const dynamic='force-dynamic';
let adapter:ReturnType<typeof createSitesQwenHandler>|undefined;
async function handle(request:Request){
 try{
  adapter??=createSitesQwenHandler({token:process.env.KFM_SITES_QWEN_TOKEN,origin:process.env.KFM_HOSTED_AI_ORIGIN,handle:publicQwen});
  return await adapter(request);
 }catch{return Response.json({reasonCode:'QWEN_CONNECTION_UNAVAILABLE'},{status:503,headers:{'Cache-Control':'private, no-store'}});}
}
export const GET=handle;
export const POST=handle;
