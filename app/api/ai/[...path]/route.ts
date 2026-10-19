import {publicAiRuntime} from '../../../../server/public-ai-handler.mjs';
import {researchEvidence,recordContext} from '../../../hosted-ai-evidence';
import {createAssistantContextResolver} from '../../../../server/assistant-context.mjs';
import {LAYER_REGISTRY} from '../../../explorer-data';
import {OFFICIAL_CONTEXT_SOURCES} from '../../../live-context';
const resolveContext=createAssistantContextResolver({knowledge:recordContext,layers:(ids:string[])=>ids.flatMap(id=>{const layer=LAYER_REGISTRY.find(layer=>layer.id===id);if(layer?.publicStatus==='RESTRICTED')throw new Error('POLICY_WITHHELD');const title=layer?.title??OFFICIAL_CONTEXT_SOURCES.find(source=>source.id===id)?.shortTitle;return title?[title]:[];}),catalog:({layerId,featureId}:{layerId:string;featureId:string})=>{
 const layer=LAYER_REGISTRY.find(layer=>layer.id===layerId);
 const feature=layer?.data.features.find(feature=>feature.properties.fid===featureId);
 if(!layer||!feature)return null;
 const p=feature.properties;
 const denied=layer.publicStatus==='RESTRICTED'||layer.releaseState==='RESTRICTED'||['RESTRICTED_ACCESS','DENIED_BY_POLICY','GENERALIZED_GEOMETRY'].includes(p.evidenceState);
 return {title:p.title,denied,year:p.year,exactTime:layer.temporal?.mode==='exact',prompt:'Catalog display context, not a resolved EvidenceBundle. '+p.title+'; source '+p.sourceOrganization+'; source role '+p.sourceRole+'; time '+p.temporalScope+'; status '+p.evidenceState+'; '+p.summary.slice(0,500)};
}});
export const dynamic='force-dynamic';
async function handle(request:Request){
 if(process.env.KFM_HOSTED_AI==='1'&&new URL(request.url).origin!==process.env.KFM_HOSTED_AI_ORIGIN)
  return Response.json({reasonCode:'AI_ORIGIN_HOLD'},{status:503,headers:{'Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff'}});
 try{return await publicAiRuntime(researchEvidence,resolveContext)(request);}
 catch{return Response.json({reasonCode:'AI_UNAVAILABLE'},{status:503,headers:{'Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff'}});}
}
export const GET=handle;
export const POST=handle;
