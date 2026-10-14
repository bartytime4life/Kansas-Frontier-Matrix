import { kansasKnowledgeRead } from './kansas-knowledge-server';
import { parseKnowledgeRead } from './knowledge-read';

export type PcResearchQuery = {term:string;place:string;start:string;end:string};
/** Uses the existing governed reader; source capture and local files confer no authority. */
export async function pcResearchEvidence(query:PcResearchQuery) {
  const origin=process.env.KFM_PC_ORIGIN;
  if(!origin)return null;
  const response=await kansasKnowledgeRead(new Request(`${origin}/api/governed/v1/knowledge?${new URLSearchParams({term:query.term})}`));
  const result=parseKnowledgeRead(await response.json(),{kind:'search',term:query.term});
  if(result.envelope.outcome!=='ANSWER'||!result.data)return null;
  const records=result.data.records.filter(record=>{
    if(query.place&&!record.location_label.toLowerCase().includes(query.place.toLowerCase()))return false;
    if(query.start&&(!record.time_end||record.time_end<query.start))return false;
    if(query.end&&(!record.time_start||record.time_start>query.end))return false;
    return true;
  });
  const evidence=records.flatMap(record=>record.assertions.filter(assertion=>assertion.status==='documented').map(assertion=>({
    evidenceRef:assertion.evidence_ref,text:assertion.text,status:assertion.status,title:record.title,
    url:`${origin}/knowledge/record?${new URLSearchParams({id:record.record_id})}`,
  })));
  return {releaseId:result.data.release_id,evidence:evidence.slice(0,40),truncated:result.data.has_more||evidence.length>40};
}
