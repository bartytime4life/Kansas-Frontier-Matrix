import test from 'node:test';
import assert from 'node:assert/strict';
import ts from 'typescript';
import {readFile} from 'node:fs/promises';
const api=await import('data:text/javascript;base64,'+Buffer.from(ts.transpileModule(await readFile(new URL('../app/assistant-investigation.ts',import.meta.url),'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64'));
const context={version:1,frame:2026,view:'2D',layers:['census-counties'],selection:{kind:'subsurface',tileId:'tile-160-255',recordId:'synthetic-core',intervalIndex:1},filters:{evidence:'ALL',temporalMode:'snapshot'},comparison:{frameA:2020,frameB:2026},camera:[-98.123456,38.123456],privateNotes:'DO_NOT_EXPORT'};
const job={id:'private-session-job',state:'completed',deadline:0,checkedAt:'2026-10-18T06:00:00Z',sourceRevision:'sha256:'+'a'.repeat(64),releaseId:null,result:{outcome:'ABSTAIN',reasonCode:'SOURCE_CONTEXT_ONLY',answer:null,interpretation:null,sourceSummary:'Synthetic selected interval: 10–40 ft. Record time 2025; archive edition 2026; collection date unknown.'},context:{label:'Synthetic core',boundary:'KGS source context; not admitted evidence',references:[{label:'KGS original inventory',url:'https://www.kgs.ku.edu/',role:'SOURCE_CONTEXT'}]}};
test('source-summary export carries checked scope, exact source fingerprint, units and dates without admission',()=>{
 const draft=api.buildInvestigationDraft('Explain this interval.',context,job);
 assert.equal(draft.status,'DRAFT');assert.equal(draft.publication,'NOT_PUBLISHED');assert.equal(draft.result.answer,null);assert.equal(draft.result.outcome,'ABSTAIN');
 assert.equal(draft.scope.selection.intervalIndex,1);assert.equal(draft.scope.comparison.frameA,2020);assert.equal(draft.sourceCheck.fingerprint,job.sourceRevision);assert.equal(draft.sourceCheck.releaseId,null);
 const output=JSON.stringify(draft);assert.doesNotMatch(output,/DO_NOT_EXPORT|-98.123456|private-session-job/);assert.match(output,/10–40 ft.*2025.*2026/);
 const markdown=api.investigationMarkdown(draft);assert.match(markdown,/DRAFT · NOT PUBLISHED/);assert.match(markdown,/not admitted evidence/);assert.match(markdown,/https:\/\/www.kgs.ku.edu\//);
});
test('withdrawn, denied and failed checks export only the withholding outcome, with no earlier content or sensitive question',()=>{
 for(const result of [{...job.result,reasonCode:'RELEASE_CHANGED'},{...job.result,outcome:'DENY',reasonCode:'POLICY_WITHHELD'},{...job.result,outcome:'ERROR',reasonCode:'AI_READ_BUSY'}]){
  const draft=api.buildInvestigationDraft('DO_NOT_EXPORT',context,{...job,result});
  assert.equal(draft.scope,null);assert.equal(draft.context,null);assert.equal(draft.result.sourceSummary,null);assert.deepEqual(draft.references,[]);assert.equal(draft.sourceCheck.fingerprint,null);assert.doesNotMatch(JSON.stringify(draft),/DO_NOT_EXPORT|Synthetic selected/);
 }
});
test('malformed and unchecked jobs cannot become downloads; no invented ANSWER can be exported',()=>{
 for(const patch of [{checkedAt:undefined},{sourceRevision:null},{context:null},{state:'running'},{result:null},{result:{...job.result,outcome:'ANSWER'}},{result:{...job.result,reasonCode:'<script>'}}])assert.throws(()=>api.buildInvestigationDraft('Question',context,{...job,...patch}),/INVESTIGATION_NOT_CHECKED/);
});
test('generated text remains labeled and escaped; unsafe links and undeclared attributes do not enter the draft',()=>{
 const draft=api.buildInvestigationDraft('<script>alert(1)</script> [fake](javascript:alert(1))', {...context,selection:{kind:'display',title:'DO_NOT_EXPORT',description:'DO_NOT_EXPORT'}},{...job,result:{...job.result,reasonCode:'UNVERIFIED_AI_DISCUSSION',sourceSummary:'DO_NOT_EXPORT',interpretation:'<img src=x onerror=alert(1)> **invented**',contextLimited:true,outputLimited:true},context:{...job.context,references:[{label:'bad',url:'javascript:alert(1)',role:'SOURCE_CONTEXT'},{label:'foreign',url:'https://evil.example/',role:'SOURCE_CONTEXT'}]}});
 const md=api.investigationMarkdown(draft);assert.doesNotMatch(md,/<script|<img|\[fake\]\(/);assert.match(md,/Generated discussion · unverified/);assert.deepEqual(draft.references,[]);assert.equal(draft.result.sourceSummary,null);assert.doesNotMatch(JSON.stringify(draft),/DO_NOT_EXPORT/);assert.ok(draft.limitations.some(x=>x.includes('incomplete')));
});
test('released references retain their release identity without certifying a model answer',()=>{
 const releaseId='sha256:'+'b'.repeat(64),url='https://kansasfrontiermatrix.com/knowledge/record?id=synthetic-one';
 const draft=api.buildInvestigationDraft('Find a record',null,{...job,releaseId,result:{...job.result,reasonCode:'EVIDENCE_MODEL_UNQUALIFIED',sourceSummary:undefined,citations:[{evidenceRef:'synthetic-ref',title:'Synthetic released fixture',url}]}});
 assert.equal(draft.sourceCheck.releaseId,releaseId);assert.equal(draft.citations[0].url,'/knowledge/record?id=synthetic-one');assert.equal(draft.result.answer,null);
 assert.deepEqual(api.buildInvestigationDraft('Find a record',null,{...job,releaseId:null,result:{...job.result,reasonCode:'EVIDENCE_MODEL_UNQUALIFIED',citations:[{evidenceRef:'synthetic-ref',title:'Synthetic',url}]}}).citations,[]);
});
test('context and evidence-search release identities are preserved separately when they differ',()=>{
 const contextReleaseId='sha256:'+'b'.repeat(64),evidenceReleaseId='sha256:'+'c'.repeat(64);
 const draft=api.buildInvestigationDraft('Find records',null,{...job,releaseId:null,contextReleaseId,evidenceReleaseId,
  context:{...job.context,references:[{label:'Context record',url:'/knowledge/record?id=context-one',role:'RELEASED_RECORD'}]},
  result:{...job.result,reasonCode:'EVIDENCE_MODEL_UNQUALIFIED',citations:[{evidenceRef:'synthetic-ref',title:'Search record',url:'/knowledge/record?id=search-one'}]}});
 assert.equal(draft.sourceCheck.releaseId,null);assert.equal(draft.references[0].releaseId,contextReleaseId);assert.equal(draft.citations[0].releaseId,evidenceReleaseId);assert.match(api.investigationMarkdown(draft),new RegExp(evidenceReleaseId));
});
