import { kansasKnowledgeRead } from './kansas-knowledge-server';
import { parseKnowledgeRead } from './knowledge-read';
import type { KnowledgeSearchScope } from './kansas-knowledge';

export type ResearchQuery = KnowledgeSearchScope & {term:string};
/** Reuse the same reviewed reader for a selected record; no local-file fallback. */
export async function recordContext({recordId}:{recordId:string}){
 const origin=process.env.KFM_HOSTED_AI_ORIGIN;
 if(!origin)return null;
 const response=await kansasKnowledgeRead(new Request(origin+'/api/governed/v1/knowledge?'+new URLSearchParams({id:recordId})));
 const result=parseKnowledgeRead(await response.json(),{kind:'record',id:recordId});
 if(result.envelope.outcome!=='ANSWER'||!result.data)return null;
 const record=result.data.records[0];
 return {title:record.title,releaseId:result.data.release_id,prompt:record.title+'; time '+(record.time_start??'unspecified')+' to '+(record.time_end??'unspecified')+'; '+record.assertions.filter(item=>item.status==='documented').slice(0,3).map(item=>item.text).join(' ').slice(0,1000),
 references:[{label:record.title,url:'/knowledge/record?'+new URLSearchParams({id:record.record_id}),role:'RELEASED_RECORD'}]};
}
/** Uses the existing governed reader; source capture and local files confer no authority. */
export async function researchEvidence(query:ResearchQuery, origin=process.env.KFM_HOSTED_AI_ORIGIN) {
  if(!origin)throw new Error('EVIDENCE_WITHHELD');
  const {place,start,end}=query;
  const response=await kansasKnowledgeRead(new Request(`${origin}/api/governed/v1/knowledge?${new URLSearchParams({term:query.term})}`),{place,start,end});
  const result=parseKnowledgeRead(await response.json(),{kind:'search',term:query.term});
  if(result.envelope.outcome==='ABSTAIN'&&['RECORD_NOT_FOUND','NO_APPROVED_KNOWLEDGE'].includes(result.envelope.reason_code)&&response.ok)return null;
  if(!response.ok||result.envelope.outcome!=='ANSWER'||!result.data)throw new Error('EVIDENCE_WITHHELD');
  const evidence=result.data.records.flatMap(record=>record.assertions.filter(assertion=>assertion.status==='documented').map(assertion=>({
    evidenceRef:assertion.evidence_ref,text:assertion.text,status:assertion.status,title:record.title,
    url:`${origin}/knowledge/record?${new URLSearchParams({id:record.record_id})}`,
  })));
  return {releaseId:result.data.release_id,evidence:evidence.slice(0,40),truncated:result.data.has_more||evidence.length>40};
}
