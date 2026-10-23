'use client';
import {useCallback,useEffect,useLayoutEffect,useRef,useState} from 'react';
import styles from './workspace.module.css';
import type {AssistantContext,AssistantFocus} from '../assistant-context';
import {assistantSurface} from '../assistant-surfaces.mjs';
import {buildInvestigationDraft,investigationMarkdown,type InvestigationJob} from '../assistant-investigation';
type ChatStatus={configured:boolean;online:boolean;ready:boolean;evidenceSearchAvailable?:boolean;model?:string;modelLabel?:string};
// Show a specific model only after the selected remote provider names it.
const chatModelLabel=(status:ChatStatus|null)=>typeof status?.modelLabel==='string'&&/^[\w.:/-]{1,96}$/.test(status.modelLabel)?status.modelLabel:'AI model';
type ChatFailureDetails={code:string;httpStatus?:number};
type Job=Omit<InvestigationJob,'result'>&{result:(NonNullable<InvestigationJob['result']>&{followUpQuestion?:string})|null};
type Turn={question:string;job:Job;contextKey:string;generation:number};
type RequestRun={generation:number;id:string|null;stopped:boolean;poll:AbortController|null;noticeGeneration:number;cancel?:Promise<void>};
export type AssistantDiscovery={query:string;items:readonly {id:string;kind:string;title:string;subtitle:string}[];status:string;busy:boolean;onQuery:(query:string)=>void;onChoose:(id:string)=>void};
type Props={initialMode?:'find'|'explore';place?:string;focus?:AssistantFocus;active?:boolean;discovery?:AssistantDiscovery;inputRef?:React.RefObject<HTMLTextAreaElement|null>;onInspectSources?:(context:AssistantContext,returnElement?:HTMLElement)=>boolean;draftRequest?:{id:number;value:string;intent?:'find'|'explore'|'evidence'}};
async function chatApi(path:string,body?:object,signal?:AbortSignal){
 const response=await fetch('/api/ai/'+path,{method:body?'POST':'GET',credentials:'same-origin',cache:'no-store',signal:signal?AbortSignal.any([signal,AbortSignal.timeout(12000)]):AbortSignal.timeout(12000),headers:body?{'Content-Type':'application/json'}:undefined,body:body?JSON.stringify(body):undefined});
 const seconds=Number(response.headers.get('Retry-After')),details={httpStatus:response.status,retryAfterMs:Number.isFinite(seconds)&&seconds>0?Math.min(60000,Math.max(1000,seconds*1000)):4000};
 let result;
 try{result=await response.json();if(!result||typeof result!=='object'||Array.isArray(result))throw new Error('AI_RESPONSE_INVALID');}
 catch{throw Object.assign(new Error('AI_RESPONSE_INVALID'),details);}
 if(!response.ok)throw Object.assign(new Error(typeof result.reasonCode==='string'?result.reasonCode:'AI_UNAVAILABLE'),details);return result;
}
const guidance:Record<string,string>={MODEL_CONTINUATION_UNAVAILABLE:'There is no unfinished reply available for this guest and source context. Ask a new question.',CONTEXT_UNAVAILABLE:'The selected source could not be resolved. Select the record again or ask about the map without it.',CONTEXT_TIME_MISMATCH:'This record does not support the active map year. Choose its source time and try again.',EVIDENCE_MODEL_UNQUALIFIED:'The small model is not qualified to choose a factual answer. You can inspect the released records below.',UNVERIFIED_AI_DISCUSSION:'Generated discussion is unverified and does not establish KFM facts.',GLOBAL_RATE_LIMIT:'The shared AI allowance is used for this hour. Please try again later.',MODEL_UNAVAILABLE:'The hosted model is unavailable. Please try again later.',MODEL_FOLLOWUP_REPEATED:'The model repeated its earlier reply instead of answering the follow-up, so the duplicate was withheld. Ask a narrower question or inspect the original records.',MODEL_CONTINUATION_REPEATED:'The model repeated its earlier explanation instead of continuing, so the duplicate was withheld. Ask a narrower question or inspect the original records.',MODEL_CONTEXT_LIMIT:'This question and its evidence exceed the small model’s context limit. Try a shorter question or narrower search.',MODEL_OUTPUT_UNQUALIFIED:'The generated reply did not pass the public output checks. Try a general explanation or inspect the source records.',EVIDENCE_WITHHELD:'Eligible evidence could not be verified. No answer was generated.',SESSION_REQUIRED:'This temporary question session expired. Send a new question.',USER_BUSY:'You already have a question in progress.',QUEUE_FULL:'The research queue is full. Try again shortly.',USER_RATE_LIMIT:'You have reached the hourly question limit.',NO_RELEASED_EVIDENCE:'I could not find eligible released evidence for this question. I cannot provide a supported answer yet.',RELEASE_CHANGED:'The evidence changed or became unavailable, so the answer was withheld.',POLICY_WITHHELD:'This request or its attached source includes protected information or host access. I can still help with general questions, explanations and fictional stories.',INFERENCE_FAILED:'The model could not complete this question.',EVIDENCE_NOT_SUPPORTIVE:'The available evidence does not support an answer.'};
Object.assign(guidance,{AI_READ_BUSY:'AI source checks are busy. Please try again shortly; your question has not changed.',AI_READ_RATE_LIMIT:'Status checks are temporarily limited. Please wait before checking the same question again.'});
const running=(job?:Job)=>Boolean(job&&['preparing','queued','running'].includes(job.state));
type TurnSnapshot={id:string;state:string;hasResult:boolean}|null;
// New questions always scroll into view. Status or result changes on the latest turn scroll only a visitor who was
// already reading the end of the conversation; polls, rechecks and exports that change nothing visible never scroll.
export function shouldAutoscroll(previous:TurnSnapshot,next:TurnSnapshot,nearBottom:boolean){if(!next)return false;if(!previous||previous.id!==next.id)return true;if(previous.state===next.state&&previous.hasResult===next.hasResult)return false;return nearBottom;}
// Only an error from the visitor's own action is brought into view; background status-poll messages stay where they are.
export function revealsAlert(error:string,backgroundMessage:string){return Boolean(error)&&error!==backgroundMessage;}
export function DiscussionText({value}:{value:string}){
 return <div className={styles.discussion}>{value.split(/\n\s*\n/).map((block,index)=>{
  const lines=block.trim().split('\n');
  if(lines.every(line=>/^[-*]\s+/.test(line)))return <ul key={index}>{lines.map((line,n)=><li key={n}>{line.replace(/^[-*]\s+/, '')}</li>)}</ul>;
  if(lines.every(line=>/^\d+[.)]\s+/.test(line)))return <ol key={index}>{lines.map((line,n)=><li key={n}>{line.replace(/^\d+[.)]\s+/, '')}</li>)}</ol>;
  if(lines.length===1&&/^#{1,3}\s+/.test(block))return <h4 key={index}>{block.replace(/^#{1,3}\s+/, '')}</h4>;
  return <p key={index}>{block}</p>;
 })}</div>;
}
function searchTerm(question:string){let term='';for(const char of question.trim()){if(new TextEncoder().encode(term+char).length>120)break;term+=char;}return term;}
const newInvestigationId=()=>globalThis.crypto?.randomUUID?.()??null;
export default function AssistantWorkspace({initialMode,place='',focus,active=true,discovery,inputRef,onInspectSources,draftRequest}:Props){
 const [mode,setMode]=useState<'find'|'explore'|'evidence'>(initialMode??(discovery?'find':'explore')),[chatStatus,setChatStatus]=useState<ChatStatus|null>(null),[chatFailure,setChatFailure]=useState(''),[error,setError]=useState(''),[busy,setBusy]=useState(false),[job,setJob]=useState<Job|null>(null),[turns,setTurns]=useState<Turn[]>([]),[question,setQuestion]=useState(''),[jobRetry,setJobRetry]=useState(0),[exportNotice,setExportNotice]=useState('');
 const [investigationId,setInvestigationId]=useState<string|null>(newInvestigationId),[awayFromLatest,setAwayFromLatest]=useState(false);
 const [chatFailureDetails,setChatFailureDetails]=useState<ChatFailureDetails|null>(null);
 const resultListRef=useRef<HTMLDivElement>(null),discoveryBodyRef=useRef<HTMLDivElement>(null);
 useLayoutEffect(()=>{if(mode==='find')discoveryBodyRef.current?.scrollTo({top:0,behavior:'auto'});},[mode,question]);
 const messageRef=useRef<HTMLTextAreaElement>(null),composingRef=useRef(false),investigationRef=useRef(investigationId),draftSeenRef=useRef<number|null>(null);
 const queryChanged=discovery?.onQuery;
 const discoveryCurrent=!discovery||discovery.query.trim().toLowerCase()===question.trim().toLowerCase(),discoveryBusy=Boolean(discovery?.busy)||!discoveryCurrent;
 useEffect(()=>{queryChanged?.(mode==='find'?question:'');},[queryChanged,mode,question]);
 // Apply a requested draft before paint: a passive opening effect can otherwise
 // replace text the visitor has already entered into the newly visible input.
 useLayoutEffect(()=>{if(!draftRequest||draftSeenRef.current===draftRequest.id)return;draftSeenRef.current=draftRequest.id;setQuestion(draftRequest.value);setMode(draftRequest.intent??(queryChanged?'find':'explore'));},[draftRequest,queryChanged]);
 const logRef=useRef<HTMLDivElement>(null),bodyRef=useRef<HTMLDivElement>(null),nearBottomRef=useRef(true),lastTurnRef=useRef<TurnSnapshot>(null),backgroundErrorRef=useRef(''),programmaticScrollRef=useRef(false);
 const exportController=useRef<AbortController|null>(null),requestRef=useRef<RequestRun|null>(null);
 const [requestNotice,setRequestNotice]=useState(''),[requestPhase,setRequestPhase]=useState('idle'),[scopeGeneration,setScopeGeneration]=useState(0);
 const contextKey=JSON.stringify(focus?.context??null);
 const scopeRef=useRef({generation:0,contextKey,active,mounted:true});
 const ownsRequest=useCallback((run:RequestRun)=>scopeRef.current.mounted&&scopeRef.current.active&&!run.stopped&&requestRef.current===run&&scopeRef.current.generation===run.generation,[]);
 const cancelAccepted=useCallback((run:RequestRun)=>{
  if(run.cancel)return run.cancel;
  run.cancel=(async()=>{
   let nextState='cancel-unconfirmed',notice='Server cancellation could not be confirmed. The earlier reply remains hidden; its server deadline still applies.';
   try{const result=await chatApi('jobs/'+run.id+'/cancel',{});nextState=result.cancelled===true?'cancelled':'superseded';notice=result.cancelled===true?'Request cancellation confirmed.':'The earlier request had already ended. Its reply remains hidden.';}catch{/* Local invalidation does not prove server cancellation. */}
   if(scopeRef.current.mounted){
    setTurns(items=>items.map(turn=>turn.job.id===run.id&&turn.generation===run.generation?{...turn,job:{...turn.job,state:nextState,result:null,context:null}}:turn));
    if(scopeRef.current.generation===run.noticeGeneration)setRequestNotice(notice);
   }
   if(requestRef.current===run){requestRef.current=null;if(scopeRef.current.mounted){setBusy(false);setRequestPhase('idle');}}
  })();
  return run.cancel;
 },[]);
 const stopRequest=useCallback((message='Stop requested.')=>{
  const run=requestRef.current;if(!run||run.stopped)return Promise.resolve();
  scopeRef.current.generation++;run.stopped=true;run.noticeGeneration=scopeRef.current.generation;run.poll?.abort();
  if(scopeRef.current.mounted){
   // A server may finish before cancellation; its hidden reply cannot seed a later question.
   const freshPartition=newInvestigationId();investigationRef.current=freshPartition;setInvestigationId(freshPartition);
   setBusy(true);setScopeGeneration(scopeRef.current.generation);setRequestPhase('stopping');setJob(current=>current?.id===run.id?null:current);
   setTurns(items=>items.map(turn=>turn.job.id===run.id&&turn.generation===run.generation?{...turn,job:{...turn.job,state:'cancel-requested',result:null,context:null}}:turn));
   setRequestNotice(message+' Server cancellation is not yet confirmed.');
  }
  // Admission may already have created a server job. Keep its bounded response
  // readable so a late opaque ID can be cancelled, never restored to the UI.
  return run.id?cancelAccepted(run):Promise.resolve();
 },[cancelAccepted]);
 useLayoutEffect(()=>{
  const scope=scopeRef.current;if(scope.contextKey===contextKey&&scope.active===active)return;
  // Visibility alone does not change a completed investigation's meaning.
  // Closing still stops a live run, whose own invalidation advances generation.
  if(scope.contextKey!==contextKey){scope.generation++;setScopeGeneration(scope.generation);const next=newInvestigationId();investigationRef.current=next;setInvestigationId(next);}
  scope.contextKey=contextKey;scope.active=active;
  const exported=exportController.current;exportController.current=null;exported?.abort();if(exported&&!requestRef.current)setBusy(false);
  void stopRequest(active?'Question context changed.':'Chat closed.');
 },[contextKey,active,stopRequest]);
 useEffect(()=>{const scope=scopeRef.current;scope.mounted=true;return()=>{scope.mounted=false;scope.generation++;exportController.current?.abort();exportController.current=null;void stopRequest('Chat closed.');};},[stopRequest]);
 const refresh=useCallback(async(signal?:AbortSignal)=>{
  try{const next=await chatApi('status',undefined,signal);if(signal?.aborted)return;setChatStatus(next);setChatFailure('');setChatFailureDetails(null);}
  catch(reason){
    if(signal?.aborted)return;
    const failure=reason as Error&{httpStatus?:number},httpStatus=failure?.httpStatus,code=['AI_ORIGIN_HOLD','AI_UNAVAILABLE','AI_RESPONSE_INVALID'].includes(failure?.message)?failure.message:failure?.name==='TimeoutError'?'AI_STATUS_TIMEOUT':'AI_CONNECTION_UNAVAILABLE';
    setChatStatus(null);setChatFailureDetails({code,httpStatus:typeof httpStatus==='number'&&Number.isInteger(httpStatus)&&httpStatus>=100&&httpStatus<=599?httpStatus:undefined});
    setChatFailure(code==='AI_ORIGIN_HOLD'?'Chat setup needs attention from the site owner. Please try again later.':'Could not connect to hosted AI. Retrying automatically; your draft is still here.');
  }
 },[]);
 useEffect(()=>{
  if(!active||mode==='find')return;
  const controller=new AbortController();let pending=false;
  // One readiness read at a time: slow connections must not accumulate requests
  // or load the model while the visitor is only finding a place or layer.
  const poll=async()=>{if(pending||controller.signal.aborted)return;pending=true;try{await refresh(controller.signal);}finally{pending=false;}};
  queueMicrotask(()=>{void poll();});const timer=setInterval(poll,5000);
  return()=>{clearInterval(timer);controller.abort();};
 },[refresh,active,mode]);
 // The scroll region, not the log, scrolls; bring the end of the latest turn into view above the pinned question bar.
 const conversationEnd=()=>{const body=bodyRef.current,log=logRef.current;return body&&log?log.getBoundingClientRect().bottom-body.getBoundingClientRect().bottom:0;};
 useEffect(()=>{
  if(mode==='find')return;
  const latest=turns[turns.length-1],next:TurnSnapshot=latest?{id:latest.job.id,state:latest.job.state,hasResult:Boolean(latest.job.result)}:null,previous=lastTurnRef.current;lastTurnRef.current=next;
  const body=bodyRef.current;if(!body||!shouldAutoscroll(previous,next,nearBottomRef.current))return;
  body.scrollTo({top:body.scrollTop+conversationEnd(),behavior:'auto'});nearBottomRef.current=true;setAwayFromLatest(false);
 },[turns,mode]);
 // Alerts lead the scroll region (before standing notices). An error from the visitor's own action is brought into view; that
 // programmatic scroll does not count as the reader leaving the conversation end. Background alerts and success notices never scroll.
 useEffect(()=>{const body=bodyRef.current;if(mode==='find'||!body||body.scrollTop===0||!revealsAlert(error,backgroundErrorRef.current))return;programmaticScrollRef.current=true;body.scrollTo({top:0,behavior:'auto'});},[error,mode]);
 const id=job?.id,state=job?.state;
 useEffect(()=>{
  const run=requestRef.current;
  if(!id||!run||run.id!==id||!ownsRequest(run)||!['preparing','queued','running'].includes(state??''))return;
  const controller=new AbortController();let timer:ReturnType<typeof setTimeout>,failures=0;
  run.poll=controller;
  const poll=async()=>{try{const next:Job=await chatApi('jobs/'+id,undefined,controller.signal);if(!controller.signal.aborted&&ownsRequest(run)){failures=0;setJob(current=>current?.id===id?next:current);setTurns(items=>items.map(item=>item.job.id===next.id&&item.generation===run.generation?{...item,job:next}:item));setError('');setRequestNotice('');if(running(next))timer=setTimeout(poll,2000);else{requestRef.current=null;setRequestPhase('idle');}}}catch(reason){if(!controller.signal.aborted&&ownsRequest(run)){const failure=reason as Error&{retryAfterMs?:number},pressure=['AI_READ_BUSY','AI_READ_RATE_LIMIT'].includes(failure.message);failures++;const message=failures>=5?'Status is unavailable. Your accepted question is retained. Retry status to check it; a new question will not be submitted.':pressure?'AI source checks are busy. Your accepted question is retained; checking again shortly.':'Connection interrupted. Your accepted question is retained; checking again.';backgroundErrorRef.current=message;setError(message);if(failures<5)timer=setTimeout(poll,failure.retryAfterMs??4000);}}};
  void poll();return()=>{controller.abort();clearTimeout(timer);if(run.poll===controller)run.poll=null;};
 },[id,state,jobRetry,active,contextKey,ownsRequest]);
 const ask=async(event:React.FormEvent<HTMLFormElement>)=>{
  event.preventDefault();if(mode==='find'){discovery?.onQuery(question);return;}
  const values=new FormData(event.currentTarget),submittedDraft=question,prompt=submittedDraft.trim();if(prompt.length<2||busy||requestRef.current||!active||running(job??undefined))return;
  if(!investigationRef.current){setError('A secure investigation session is unavailable in this browser. Place and layer discovery remains available.');return;}
  const run:RequestRun={generation:scopeRef.current.generation,id:null,stopped:false,poll:null,noticeGeneration:scopeRef.current.generation};requestRef.current=run;
  setBusy(true);setRequestPhase('submitting');setError('');setExportNotice('');setRequestNotice('Submitting your question…');
  try{
   const created=await chatApi('jobs',{...(focus?{context:focus.context}:{}),investigationId:investigationRef.current,mode,style:values.get('style')||'plain',depth:values.get('depth')||'brief',question:prompt,term:values.get('term')||searchTerm(prompt),place:values.get('place')||'',start:values.get('start')||'',end:values.get('end')||''});
   if(typeof created.id!=='string'||! /^[A-Za-z0-9_-]{1,128}$/.test(created.id))throw new Error('AI_ADMISSION_UNCONFIRMED');
   run.id=created.id;
   if(!ownsRequest(run)){run.stopped=true;await cancelAccepted(run);return;}
   const pending:Job={id:created.id,state:'preparing',deadline:Number.isFinite(created.deadline)?created.deadline:Date.now()+(mode==='explore'?2100000:90000),result:null};
   setJob(pending);setTurns(items=>[...items.slice(-9),{question:prompt,job:pending,contextKey,generation:run.generation}]);setQuestion(current=>current===submittedDraft?'':current);setRequestPhase('accepted');setRequestNotice('Question accepted. Checking its source context…');
  }catch(reason){if(ownsRequest(run)){setRequestNotice('');setError(guidance[(reason as Error).message]??'The request could not be confirmed. Your draft is retained; check the connection before sending again.');}else if(scopeRef.current.mounted&&scopeRef.current.generation===run.noticeGeneration)setRequestNotice('The earlier request could not be confirmed or cancelled. Its reply remains hidden; its server deadline still applies.');if(requestRef.current===run){requestRef.current=null;if(scopeRef.current.mounted){setBusy(false);setRequestPhase('idle');}}}
  finally{if(scopeRef.current.mounted&&requestRef.current===run)setBusy(false);}
 };
 const surface=assistantSurface(focus?.context.surface??'map');
 const prompts:readonly string[]=focus?.context.selection?['Explain this selected record and its limits.',...(focus.context.selection.kind==='subsurface'&&focus.context.selection.intervalIndex!==null?['What does this selected interval mean?']:[]),'What is missing from this source?']:(surface?.prompts??[]);
 const exportInvestigation=async(turn:Turn,format:'clipboard'|'markdown'|'json')=>{
  if(exportController.current&&!exportController.current.signal.aborted)return;
  const controller=new AbortController();exportController.current=controller;
  setBusy(true);setError('');setExportNotice('');
  try{
   // The download/copy uses this fresh server read, never the displayed cache.
   // A source withdrawal replaces the old summary with a withheld draft.
   const next:Job=await chatApi('jobs/'+turn.job.id,undefined,controller.signal);
   if(controller.signal.aborted)return;
   setJob(current=>current?.id===next.id?next:current);
   setTurns(items=>items.map(item=>item.job.id===next.id?{...item,job:next}:item));
   const draft=buildInvestigationDraft(turn.question,JSON.parse(turn.contextKey),next);
   const contents=format==='json'?JSON.stringify(draft,null,2)+'\n':investigationMarkdown(draft);
   if(format==='clipboard')await navigator.clipboard.writeText(contents);
   else{
    const url=URL.createObjectURL(new Blob([contents],{type:format==='json'?'application/json;charset=utf-8':'text/markdown;charset=utf-8'}));
    const anchor=document.createElement('a');anchor.href=url;anchor.download='kfm-investigation-draft.'+(format==='json'?'json':'md');
    try{document.body.append(anchor);anchor.click();}finally{anchor.remove();setTimeout(()=>URL.revokeObjectURL(url),0);}
   }
   if(!controller.signal.aborted)setExportNotice((format==='clipboard'?'Investigation copied.':'Investigation download prepared.')+' Sources rechecked; draft only, not published.');
  }catch{if(!controller.signal.aborted)setError('The investigation could not be saved. Sources must be rechecked first; your question is retained. Try again when the connection is available.');}
   finally{if(exportController.current===controller){exportController.current=null;if(scopeRef.current.mounted)setBusy(false);}}
 };
 const recheck=async(turn:Turn,inspect=false,returnElement?:HTMLElement)=>{if(exportController.current&&!exportController.current.signal.aborted)return;const controller=new AbortController();exportController.current=controller;setBusy(true);setError('');try{const next:Job=await chatApi('jobs/'+turn.job.id,undefined,controller.signal);if(controller.signal.aborted)return;setJob(current=>current?.id===next.id?next:current);setTurns(items=>items.map(item=>item.job.id===next.id?{...item,job:next}:item));if(inspect){if(next.result?.outcome!=='ABSTAIN'||!next.context||['RELEASE_CHANGED','CONTEXT_UNAVAILABLE','CONTEXT_TIME_MISMATCH','EVIDENCE_WITHHELD'].includes(next.result.reasonCode))throw new Error('CONTEXT_WITHHELD');if(onInspectSources?.(JSON.parse(turn.contextKey),returnElement)!==true)setRequestNotice('Exact source inspection is unavailable in the current map scope. The bound source links remain attached to this reply.');}}catch{if(!controller.signal.aborted)setError('Sources could not be rechecked. This earlier reply may be out of date; your draft is retained.');}finally{if(exportController.current===controller){exportController.current=null;if(scopeRef.current.mounted)setBusy(false);}}};
 const newInvestigation=()=>{
  const next=newInvestigationId();if(!next){setError('A fresh conversation cannot be isolated in this browser. Keep this investigation or open a supported secure browser.');return;}
  void stopRequest('Starting a new investigation.');scopeRef.current.generation++;setScopeGeneration(scopeRef.current.generation);
  const exported=exportController.current;exportController.current=null;exported?.abort();if(exported&&!requestRef.current)setBusy(false);
  investigationRef.current=next;setInvestigationId(next);setTurns([]);setJob(null);setQuestion('');setError('');setExportNotice('');setRequestNotice('New investigation. History is held in this tab only; earlier server requests retain their existing expiry.');setAwayFromLatest(false);nearBottomRef.current=true;lastTurnRef.current=null;
  (inputRef??messageRef).current?.focus();
 };
 const jumpToLatest=()=>{const body=bodyRef.current;if(body)body.scrollTo({top:body.scrollTop+conversationEnd(),behavior:'auto'});nearBottomRef.current=true;setAwayFromLatest(false);};
 const sourceContext=mode==='explore'&&focus?.context.selection?.kind==='subsurface';
 const canSubmit=mode==='find'?Boolean(discovery):Boolean(investigationId&&chatStatus?.configured&&(mode==='evidence'?chatStatus.evidenceSearchAvailable===true:sourceContext||chatStatus.ready));
 const statusText=mode==='find'?'Places & layers · no AI required':!chatStatus?(chatFailure?'AI connection unavailable':'Checking hosted AI'):!chatStatus.configured?'Awaiting owner setup':mode==='evidence'?(chatStatus.evidenceSearchAvailable?'Evidence search available':'Evidence search unavailable'):sourceContext?'Source summary available':!chatStatus.online?'AI unavailable':!chatStatus.ready?'Loading model…':chatModelLabel(chatStatus)+' ready';
 const notices=<>
   {!investigationId&&mode!=='find'&&<p role='alert' className={styles.notice}>A secure investigation session is unavailable in this browser. Place and layer discovery remains available.</p>}
   {chatFailure&&<p role='alert' data-ai-error={chatFailureDetails?.code} data-http-status={chatFailureDetails?.httpStatus} className={styles.notice}>{chatFailure}</p>}
   {error&&<p role='alert' className={styles.notice}>{error}</p>}
   {chatStatus?.configured&&!chatStatus.ready&&(sourceContext||chatStatus.evidenceSearchAvailable)&&<p className={styles.notice}>{sourceContext?'Selected sample summaries use the original source and do not require the AI model. ':''}{chatStatus.online?'The model is starting. You can keep using the map or choose Evidence to inspect released records while it loads.':'AI discussion is unavailable. Choose Find evidence to search released records without waiting for the model. Records may still be unavailable.'}</p>}
   {exportNotice&&<p role='status' className={styles.notice}>{exportNotice}</p>}
  {requestNotice&&<p role='status' className={styles.notice}>{requestNotice}</p>}
 </>;
 return <div className={styles.chat} data-mode={mode}>
  <div className={styles.toolbar}><div className={styles.identity}><strong>KFM <span className={styles.aiBadge}>AI assistant</span></strong><span role='status' className={styles.status}>{statusText}</span></div><button type='button' className={styles.secondaryButton} disabled={!investigationId||requestPhase==='stopping'} onClick={newInvestigation} title={investigationId?'Start a separate temporary conversation; preserve the map':'Fresh conversation isolation requires a supported secure browser'}>New chat</button></div>
  {mode==='find'&&<div ref={discoveryBodyRef} className={styles.body} aria-label='Place and layer discovery'>
   {mode==='find'&&discovery&&question.trim()&&<div ref={resultListRef} id='global-search-results' className={styles.searchResults} aria-label='Places and layers'>
    {(discoveryCurrent?discovery.items:[]).map(item=><button type='button' className={styles.searchResult} key={item.id} onClick={()=>{discovery.onChoose(item.id);setQuestion('');}}><small className={styles.searchMeta}>{item.kind}</small><strong>{item.title}</strong><span>{item.subtitle}</span></button>)}
    <p role='status' aria-live='polite' aria-atomic='true'>{discoveryCurrent?(discovery.status||`${discovery.items.length} available matches.`):'Updating search…'}</p>
   </div>}
   {!question.trim()&&<section className={styles.messages}><h3>Find a Kansas place or layer</h3><p>Type a county, place or topic, then choose an available match. Switch to Ask to discuss what you find.</p></section>}
  </div>}
  <div hidden={mode==='find'} ref={bodyRef} className={styles.body} onScroll={()=>{if(programmaticScrollRef.current){programmaticScrollRef.current=false;return;}nearBottomRef.current=conversationEnd()<=80;setAwayFromLatest(!nearBottomRef.current);}}>
  {notices}
  {focus&&<details className={styles.context} aria-label='AI question context'><summary><span className={styles.contextTitle}>{focus.title}</span><small>{focus.context.view} · {focus.context.frame} · {focus.context.layers.length} layers</small></summary><strong>{focus.title}</strong><p>{focus.detail}</p><small>Sent with each question · map display year, not a collection date</small></details>}
  <div ref={logRef} className={styles.messages} role='log' aria-label='KFM chat conversation' aria-live='polite' tabIndex={0}>
   {turns.length===0&&<section className={styles.emptyState} aria-label='Start an investigation'><span className={styles.eyebrow}>EXPLORE WITH AI</span><h3>Where shall we explore?</h3><p>Ask KFM AI about this map or follow an idea. Your map context travels with each question.</p></section>}
   {turns.map(turn=><div key={turn.job.id} className={styles.turn}>
    <article className={styles.user}><small className={styles.turnLabel}>YOU</small><p>{turn.question}</p>{turn.job.context&&<small>About: {turn.job.context.label} · {turn.job.context.boundary}</small>}</article>
    <article className={styles.assistant} data-state={turn.job.state}>
     <small className={styles.turnLabel}>KFM · {turn.job.result?.reasonCode==='SOURCE_CONTEXT_ONLY'?'SOURCE CONTEXT':turn.job.result?.reasonCode==='UNVERIFIED_AI_DISCUSSION'?'AI DISCUSSION · UNVERIFIED':turn.job.result?.outcome??turn.job.state.toUpperCase()}</small>
     {turn.job.result?.answer&&<p>{turn.job.result.answer}</p>}
     {turn.job.result?.sourceSummary&&<><strong>Source summary · not admitted evidence</strong><p>{turn.job.result.sourceSummary.length>240?turn.job.result.sourceSummary.slice(0,240)+'…':turn.job.result.sourceSummary}</p>{turn.job.result.sourceSummary.length>240&&<details><summary>Read full source summary</summary><p>{turn.job.result.sourceSummary}</p></details>}</>}
     {turn.job.result?.interpretation&&<>{DiscussionText({value:turn.job.result.interpretation})}</>}
     {turn.job.result&&!turn.job.result.answer&&!turn.job.result.interpretation&&!turn.job.result.sourceSummary&&<p>{guidance[turn.job.result.reasonCode]??'KFM withheld an unsupported result.'}</p>}
     {!turn.job.result&&<p className={styles.progress} data-state={turn.job.state}>{running(turn.job)&&<span className={styles.progressDot} aria-hidden='true'/>}{running(turn.job)?(turn.job.state==='queued'?'Waiting in the AI queue. Your accepted question will run without resubmitting.':turn.job.state==='preparing'?'Checking the question context…':'Generating your reply…'):turn.job.state==='cancelled'?'Question cancelled.':turn.job.state==='cancel-requested'?'Cancellation requested; server confirmation is pending.':turn.job.state==='cancel-unconfirmed'?'Cancellation could not be confirmed; the earlier reply remains hidden.':turn.job.state==='superseded'?'The earlier request ended; its reply remains hidden.':'The question ended without an answer.'}</p>}
     {turn.job.result?.truncated&&<p>This bounded search may omit additional records.</p>}
     {(!!turn.job.result?.citations?.length||!!turn.job.context?.references?.length)&&<details className={styles.evidencePanel}>
      <summary className={styles.evidenceButton}>Sources & citations · {(turn.job.context?.references?.length??0)+(turn.job.result?.citations?.length??0)}</summary>
      <section aria-label='Supporting source references'><div className={styles.evidenceHeader}><strong>Sources to inspect</strong><button type='button' disabled={busy} onClick={()=>void recheck(turn)}>Recheck sources</button></div><p>Bound to this reply. Sources were checked for this response; recheck before reuse.</p>
       <ul className={styles.evidenceList}>{turn.job.result?.citations?.map((citation,index)=><li key={citation.evidenceRef+index} className={styles.evidenceItem}><a href={citation.url}>{citation.title}</a><small className={styles.evidenceMeta}>{citation.evidenceRef} · released-record reference; interpretation unverified</small></li>)}{turn.job.context?.references?.map((ref,index)=><li key={ref.url+index} className={styles.evidenceItem}><a href={ref.url} target='_blank' rel='noreferrer'>{ref.label}</a><small className={styles.evidenceMeta}>{ref.role==='RELEASED_RECORD'?'Released record; interpretation unverified':'External source context; not admitted evidence'}</small></li>)}</ul>
       {onInspectSources&&turn.contextKey!=='null'&&<button type='button' className={styles.evidenceButton} disabled={busy} onClick={event=>void recheck(turn,true,event.currentTarget)}>Inspect source in Evidence</button>}
      </section>
     </details>}
     {turn.job.result&&<div className={styles.replyActions}>
      <button type='button' disabled={busy||running(job??undefined)} onClick={()=>void exportInvestigation(turn,'clipboard')}>Copy investigation</button>
      <details><summary>Save & retry</summary><div className={styles.evidenceActions}><button type='button' disabled={busy||running(job??undefined)} onClick={()=>{setMode('explore');setQuestion(turn.question);(inputRef??messageRef).current?.focus();}}>Edit and retry</button><button type='button' disabled={busy||running(job??undefined)} onClick={()=>void exportInvestigation(turn,'markdown')}>Download Markdown</button><button type='button' disabled={busy||running(job??undefined)} onClick={()=>void exportInvestigation(turn,'json')}>Download investigation JSON</button><small>Sources rechecked before saving · draft only</small></div></details>
     </div>}
     {turn.job.result?.contextLimited&&<p>Earlier messages were omitted to fit this small model’s context.</p>}
     {turn.job.result?.outputLimited&&<><p>Reply limit reached. Continue in the same source context, or ask a narrower question.</p><button type='button' disabled={busy||running(job??undefined)||turn.job.id!==job?.id||turn.contextKey!==contextKey||turn.generation!==scopeGeneration} onClick={()=>{setMode('explore');setQuestion('Continue your previous reply from where it stopped. Finish the explanation without repeating it.');}}>Continue reply</button></>}
     {turn.job.result?.followUpQuestion&&<details className={styles.nextStep}><summary>Explore next</summary><p>{turn.job.result.followUpQuestion}</p></details>}
    </article>
   </div>)}
  </div>
  {turns.length===0&&prompts.length>0&&<div className={styles.prompts} aria-label='Suggested questions'>{prompts.map(prompt=><button type='button' key={prompt} disabled={busy||running(job??undefined)} onClick={()=>{setMode('explore');setQuestion(prompt);(inputRef??messageRef).current?.focus();}}>{prompt}</button>)}</div>}
  </div>
  {mode!=='find'&&awayFromLatest&&turns.length>0&&<button type='button' className={styles.secondaryButton} onClick={jumpToLatest}>Jump to latest</button>}
  <form onSubmit={ask} className={styles.composer}>
   <div className={styles.composerTools} role='group' aria-label='Composer mode'>
    {discovery&&<button type='button' aria-pressed={mode==='find'} onClick={()=>setMode('find')}>Find</button>}
    <button type='button' aria-pressed={mode==='explore'} onClick={()=>setMode('explore')}>Ask</button>
    {chatStatus?.evidenceSearchAvailable===true&&<button type='button' aria-pressed={mode==='evidence'} onClick={()=>setMode('evidence')}>Evidence</button>}
   </div>
   <details hidden={mode==='find'} className={styles.options}><summary>Options</summary><div className={styles.optionsBody}>
   <input type='hidden' name='mode' value={mode}/>
   <div className={styles.dates}><label>Explanation style<select name='style'><option value='plain'>Plain language</option><option value='technical'>Technical</option></select></label><label>Reply length<select name='depth' defaultValue='expanded'><option value='brief'>Brief</option><option value='expanded'>More detail</option></select></label></div>
   <small>{mode==='find'?'Available place and layer indexes; no inference or evidence admission.':mode==='explore'?(sourceContext?'Selected sample replies summarize the original source; they are not admitted evidence.':'Ideas and explanations are generated, unverified discussion.'):'Evidence mode uses only released records; unsupported factual answers are withheld.'}</small>
   <details><summary>Evidence search filters</summary><label>Search terms<input name='term' maxLength={120} placeholder='Defaults to your message'/></label><label>Place filter<input name='place' defaultValue={place} maxLength={160} placeholder='Named place or county'/></label><div className={styles.dates}><label>From<input name='start' type='date'/></label><label>Through<input name='end' type='date'/></label></div><small>Date filters exclude undated records.</small></details>
  {surface&&<details className={styles.guide}><summary>Help with {surface.title.toLowerCase()}</summary><p>{surface.guide}</p><small>Interface guide · no model required</small>{!['reports','stories'].includes(surface.id)&&<> · <a href={surface.path}>Open this workspace</a></>}</details>}
  <footer className={styles.footer}>History stays in this tab. Queued questions have up to 35 minutes under load; finished server results expire after 15 minutes. Downloads are separate drafts.</footer>
   </div></details>

   <label className={styles.composerField}><span className={styles.srOnly}>Message KFM</span><textarea ref={inputRef??messageRef} value={question} onChange={event=>setQuestion(event.target.value)} onCompositionStart={()=>{composingRef.current=true;}} onCompositionEnd={()=>{composingRef.current=false;}} onKeyDown={event=>{if(event.key==='ArrowDown'&&mode==='find'&&discoveryCurrent&&discovery?.items.length){event.preventDefault();resultListRef.current?.querySelector<HTMLButtonElement>('button')?.focus();return;}if(event.key==='Enter'&&!event.shiftKey&&!event.ctrlKey&&!event.altKey&&!event.metaKey&&!composingRef.current&&!event.nativeEvent.isComposing&&event.nativeEvent.keyCode!==229){event.preventDefault();event.currentTarget.form?.requestSubmit();}}} rows={2} maxLength={4096} placeholder={mode==='find'?'Find a county, city or layer…':'Ask KFM AI about anything…'} aria-describedby='kfm-composer-help' aria-busy={mode==='find'&&discoveryBusy}/></label>
   <div className={styles.actions}><small id='kfm-composer-help'>{mode==='find'?'Local discovery · choose a result to inspect':mode==='evidence'?'Released records · no model required · unsupported answers withheld':sourceContext?'Source summary · no model required · not admitted evidence':'AI can make mistakes · check sources'}<span className={styles.keyboardHint}> · Enter sends · Shift+Enter adds a line</span></small>
    {requestPhase!=='idle'?<>{running(job??undefined)&&<button type='button' disabled={busy} onClick={()=>setJobRetry(value=>value+1)}>Retry status</button>}<button type='button' className={styles.secondaryButton} disabled={requestPhase==='stopping'} onClick={()=>stopRequest()}>Stop</button></>:<button className={styles.sendButton} disabled={busy||!canSubmit||question.trim().length<(mode==='find'?1:2)}>{busy?'Sending…':mode==='find'?'Find':mode==='evidence'?'Search':'Send'}</button>}
   </div>
  </form>
 </div>;
}
