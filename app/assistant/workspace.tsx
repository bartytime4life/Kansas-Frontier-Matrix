'use client';
import {useCallback,useEffect,useLayoutEffect,useRef,useState} from 'react';
import styles from './workspace.module.css';
import type {AssistantFocus} from '../assistant-context';
import {assistantSurface} from '../assistant-surfaces.mjs';
import {buildInvestigationDraft,investigationMarkdown,type InvestigationJob} from '../assistant-investigation';
type ChatStatus={configured:boolean;online:boolean;ready:boolean;evidenceSearchAvailable?:boolean;requiresLogin:boolean;model?:string};
type Status={configured:boolean;online:boolean;ready:boolean;account:string|null;role?:string|null};
type Job=Omit<InvestigationJob,'result'>&{result:(NonNullable<InvestigationJob['result']>&{followUpQuestion?:string})|null};
type Turn={question:string;job:Job;contextKey:string;generation:number};
type RequestRun={generation:number;id:string|null;stopped:boolean;poll:AbortController|null;noticeGeneration:number;cancel?:Promise<void>};
type Props={accountRequest?:number;onAccount?:(account:string|null)=>void;place?:string;focus?:AssistantFocus;active?:boolean};
async function api(path:string,body?:object,signal?:AbortSignal){
 const response=await fetch('/api/pc-ai/'+path,{method:body?'POST':'GET',credentials:'same-origin',cache:'no-store',signal:signal?AbortSignal.any([signal,AbortSignal.timeout(8000)]):AbortSignal.timeout(8000),headers:body?{'Content-Type':'application/json'}:undefined,body:body?JSON.stringify(body):undefined});
 const result=await response.json();if(!response.ok)throw new Error(result.reasonCode??'PC_AI_UNAVAILABLE');return result;
}
async function chatApi(path:string,body?:object,signal?:AbortSignal){
 const response=await fetch('/api/ai/'+path,{method:body?'POST':'GET',credentials:'same-origin',cache:'no-store',signal:signal?AbortSignal.any([signal,AbortSignal.timeout(12000)]):AbortSignal.timeout(12000),headers:body?{'Content-Type':'application/json'}:undefined,body:body?JSON.stringify(body):undefined});
 const result=await response.json();if(!response.ok){const seconds=Number(response.headers.get('Retry-After'));throw Object.assign(new Error(result.reasonCode??'AI_UNAVAILABLE'),{retryAfterMs:Number.isFinite(seconds)&&seconds>0?Math.min(60000,Math.max(1000,seconds*1000)):4000});}return result;
}
const guidance:Record<string,string>={MODEL_CONTINUATION_UNAVAILABLE:'There is no unfinished reply available for this guest and source context. Ask a new question.',CONTEXT_UNAVAILABLE:'The selected source could not be resolved. Select the record again or ask about the map without it.',CONTEXT_TIME_MISMATCH:'This record does not support the active map year. Choose its source time and try again.',EVIDENCE_MODEL_UNQUALIFIED:'The small model is not qualified to choose a factual answer. You can inspect the released records below.',UNVERIFIED_AI_DISCUSSION:'Generated discussion is unverified and does not establish KFM facts.',GLOBAL_RATE_LIMIT:'The shared AI allowance is used for this hour. Please try again later.',MODEL_UNAVAILABLE:'The hosted model is unavailable. Please try again later.',MODEL_FOLLOWUP_REPEATED:'The model repeated its earlier reply instead of answering the follow-up, so the duplicate was withheld. Ask a narrower question or inspect the original records.',MODEL_CONTINUATION_REPEATED:'The model repeated its earlier explanation instead of continuing, so the duplicate was withheld. Ask a narrower question or inspect the original records.',MODEL_CONTEXT_LIMIT:'This question and its evidence exceed the small model’s context limit. Try a shorter question or narrower search.',MODEL_OUTPUT_UNQUALIFIED:'The small model could not select a supported answer.',EVIDENCE_WITHHELD:'Eligible evidence could not be verified. No answer was generated.',SESSION_REQUIRED:'This temporary question session expired. Send a new question.',PC_OFFLINE:'Your PC is offline or its model is unavailable.',USER_BUSY:'You already have a question in progress.',QUEUE_FULL:'The research queue is full. Try again shortly.',USER_RATE_LIMIT:'You have reached the hourly question limit.',SIGN_IN_DENIED:'Sign-in failed. Check your account details.',SIGN_IN_RATE_LIMIT:'Too many sign-in attempts. Wait before trying again.',NO_RELEASED_EVIDENCE:'I could not find eligible released evidence for this question. I cannot provide a supported answer yet.',RELEASE_CHANGED:'The evidence changed or became unavailable, so the answer was withheld.',POLICY_WITHHELD:'This question is withheld by KFM’s policy controls.',INFERENCE_FAILED:'The model could not complete this question.',EVIDENCE_NOT_SUPPORTIVE:'The available evidence does not support an answer.'};
Object.assign(guidance,{AI_READ_BUSY:'AI source checks are busy. Please try again shortly; your question has not changed.',AI_READ_RATE_LIMIT:'Status checks are temporarily limited. Please wait before checking the same question again.'});
const running=(job?:Job)=>Boolean(job&&['preparing','queued','running'].includes(job.state));
type TurnSnapshot={id:string;state:string;hasResult:boolean}|null;
// New questions always scroll into view. Status or result changes on the latest turn scroll only a visitor who was
// already reading the end of the conversation; polls, rechecks and exports that change nothing visible never scroll.
export function shouldAutoscroll(previous:TurnSnapshot,next:TurnSnapshot,nearBottom:boolean){if(!next)return false;if(!previous||previous.id!==next.id)return true;if(previous.state===next.state&&previous.hasResult===next.hasResult)return false;return nearBottom;}
// Only an error from the visitor's own action is brought into view; background status-poll messages stay where they are.
export function revealsAlert(error:string,backgroundMessage:string){return Boolean(error)&&error!==backgroundMessage;}
function searchTerm(question:string){let term='';for(const char of question.trim()){if(new TextEncoder().encode(term+char).length>120)break;term+=char;}return term;}
export default function AssistantWorkspace({accountRequest=0,onAccount,place='',focus,active=true}:Props){
 const [mode,setMode]=useState('explore'),[chatStatus,setChatStatus]=useState<ChatStatus|null>(null),[chatFailure,setChatFailure]=useState(''),[status,setStatus]=useState<Status|null>(null),[error,setError]=useState(''),[busy,setBusy]=useState(false),[job,setJob]=useState<Job|null>(null),[turns,setTurns]=useState<Turn[]>([]),[accountOpen,setAccountOpen]=useState(false),[activate,setActivate]=useState(false),[invitation,setInvitation]=useState(''),[question,setQuestion]=useState(''),[jobRetry,setJobRetry]=useState(0),[exportNotice,setExportNotice]=useState('');
 const loginRef=useRef<HTMLInputElement>(null),logRef=useRef<HTMLDivElement>(null),bodyRef=useRef<HTMLDivElement>(null),nearBottomRef=useRef(true),lastTurnRef=useRef<TurnSnapshot>(null),backgroundErrorRef=useRef(''),programmaticScrollRef=useRef(false),actorRef=useRef<string|null>(null);
 const exportController=useRef<AbortController|null>(null),requestRef=useRef<RequestRun|null>(null);
 const [requestNotice,setRequestNotice]=useState(''),[requestPhase,setRequestPhase]=useState('idle'),[scopeGeneration,setScopeGeneration]=useState(0);
 const contextKey=JSON.stringify(focus?.context??null),actorKey=status?.account?status.account+':'+status.role:null;
 const scopeRef=useRef({generation:0,contextKey,actorKey,active,mounted:true});
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
   setBusy(true);setScopeGeneration(scopeRef.current.generation);setRequestPhase('stopping');setJob(current=>current?.id===run.id?null:current);
   setTurns(items=>items.map(turn=>turn.job.id===run.id&&turn.generation===run.generation?{...turn,job:{...turn.job,state:'cancel-requested',result:null,context:null}}:turn));
   setRequestNotice(message+' Server cancellation is not yet confirmed.');
  }
  // Admission may already have created a server job. Keep its bounded response
  // readable so a late opaque ID can be cancelled, never restored to the UI.
  return run.id?cancelAccepted(run):Promise.resolve();
 },[cancelAccepted]);
 useLayoutEffect(()=>{
  const scope=scopeRef.current;if(scope.contextKey===contextKey&&scope.actorKey===actorKey&&scope.active===active)return;
  // Visibility alone does not change a completed investigation's meaning.
  // Closing still stops a live run, whose own invalidation advances generation.
  if(scope.contextKey!==contextKey||scope.actorKey!==actorKey){scope.generation++;setScopeGeneration(scope.generation);}
  scope.contextKey=contextKey;scope.actorKey=actorKey;scope.active=active;
  const exported=exportController.current;exportController.current=null;exported?.abort();if(exported&&!requestRef.current)setBusy(false);
  void stopRequest(active?'Question context changed.':'Chat closed.');
 },[contextKey,actorKey,active,stopRequest]);
 useEffect(()=>{const scope=scopeRef.current;scope.mounted=true;return()=>{scope.mounted=false;scope.generation++;exportController.current?.abort();exportController.current=null;void stopRequest('Chat closed.');};},[stopRequest]);
 const refresh=useCallback(async(signal?:AbortSignal)=>{
  await Promise.allSettled([
   ...(onAccount||accountRequest?[api('status',undefined,signal).then(next=>{if(signal?.aborted)return;setStatus(next);onAccount?.(next?.account??null);},()=>{if(signal?.aborted)return;setStatus(null);onAccount?.(null);})]:[]),
   chatApi('status',undefined,signal).then(next=>{if(signal?.aborted)return;setChatStatus(next);setChatFailure('');},reason=>{if(signal?.aborted)return;setChatStatus(null);setChatFailure(reason instanceof Error&&reason.message==='AI_ORIGIN_HOLD'?'Chat setup needs attention from the site owner. Please try again later.':'Could not connect to hosted AI. Retrying automatically; your draft is still here.');})
  ]);
 },[onAccount,accountRequest]);
 useEffect(()=>{if(!active)return;const controller=new AbortController();queueMicrotask(()=>{if(!controller.signal.aborted)void refresh(controller.signal);});const timer=setInterval(()=>void refresh(controller.signal),5000);return()=>{clearInterval(timer);controller.abort();};},[refresh,active]);
 useEffect(()=>{const actor=status?.account?status.account+':'+status.role:null;if(actor===actorRef.current)return;actorRef.current=actor;exportController.current?.abort();queueMicrotask(()=>{setJob(null);setTurns([]);setInvitation('');setActivate(false);setError('');setExportNotice('');});},[status?.account,status?.role]);
 useEffect(()=>{if(!accountRequest)return;queueMicrotask(()=>{setAccountOpen(true);});},[accountRequest]);
 useEffect(()=>{if(accountOpen&&!status?.account)loginRef.current?.focus();},[accountOpen,status?.account]);
 // The scroll region, not the log, scrolls; bring the end of the latest turn into view above the pinned question bar.
 const conversationEnd=()=>{const body=bodyRef.current,log=logRef.current;return body&&log?log.getBoundingClientRect().bottom-body.getBoundingClientRect().bottom:0;};
 useEffect(()=>{
  const latest=turns[turns.length-1],next:TurnSnapshot=latest?{id:latest.job.id,state:latest.job.state,hasResult:Boolean(latest.job.result)}:null,previous=lastTurnRef.current;lastTurnRef.current=next;
  const body=bodyRef.current;if(!body||!shouldAutoscroll(previous,next,nearBottomRef.current))return;
  body.scrollTo({top:body.scrollTop+conversationEnd(),behavior:'auto'});nearBottomRef.current=true;
 },[turns]);
 // Alerts lead the scroll region (before standing notices). An error from the visitor's own action is brought into view; that
 // programmatic scroll does not count as the reader leaving the conversation end. Background alerts and success notices never scroll.
 useEffect(()=>{const body=bodyRef.current;if(!body||body.scrollTop===0||!revealsAlert(error,backgroundErrorRef.current))return;programmaticScrollRef.current=true;body.scrollTo({top:0,behavior:'auto'});},[error]);
 const id=job?.id,state=job?.state;
 useEffect(()=>{
  const run=requestRef.current;
  if(!id||!run||run.id!==id||!ownsRequest(run)||!['preparing','queued','running'].includes(state??''))return;
  const controller=new AbortController();let timer:ReturnType<typeof setTimeout>,failures=0;
  run.poll=controller;
  const poll=async()=>{try{const next:Job=await chatApi('jobs/'+id,undefined,controller.signal);if(!controller.signal.aborted&&ownsRequest(run)){failures=0;setJob(current=>current?.id===id?next:current);setTurns(items=>items.map(item=>item.job.id===next.id&&item.generation===run.generation?{...item,job:next}:item));setError('');setRequestNotice('');if(running(next))timer=setTimeout(poll,2000);else{requestRef.current=null;setRequestPhase('idle');}}}catch(reason){if(!controller.signal.aborted&&ownsRequest(run)){const failure=reason as Error&{retryAfterMs?:number},pressure=['AI_READ_BUSY','AI_READ_RATE_LIMIT'].includes(failure.message);failures++;const message=failures>=5?'Status is unavailable. Your accepted question is retained. Retry status to check it; a new question will not be submitted.':pressure?'AI source checks are busy. Your accepted question is retained; checking again shortly.':'Connection interrupted. Your accepted question is retained; checking again.';backgroundErrorRef.current=message;setError(message);if(failures<5)timer=setTimeout(poll,failure.retryAfterMs??4000);}}};
  void poll();return()=>{controller.abort();clearTimeout(timer);if(run.poll===controller)run.poll=null;};
 },[id,state,jobRetry,active,contextKey,actorKey,ownsRequest]);
 const signIn=async(event:React.FormEvent<HTMLFormElement>)=>{event.preventDefault();const form=event.currentTarget,values=new FormData(form);setBusy(true);setError('');try{await api('sign-in',{username:values.get('username'),password:values.get('password')});form.reset();setAccountOpen(false);await refresh();}catch(reason){setError(guidance[(reason as Error).message]??'Sign-in could not complete.');}finally{setBusy(false);}};
 const ask=async(event:React.FormEvent<HTMLFormElement>)=>{
  event.preventDefault();const values=new FormData(event.currentTarget),submittedDraft=question,prompt=submittedDraft.trim();if(prompt.length<2||busy||requestRef.current||!active||running(job??undefined))return;
  const run:RequestRun={generation:scopeRef.current.generation,id:null,stopped:false,poll:null,noticeGeneration:scopeRef.current.generation};requestRef.current=run;
  setBusy(true);setRequestPhase('submitting');setError('');setExportNotice('');setRequestNotice('Submitting your question…');
  try{
   const created=await chatApi('jobs',{...(focus?{context:focus.context}:{}),mode,style:values.get('style')||'plain',depth:values.get('depth')||'brief',question:prompt,term:values.get('term')||searchTerm(prompt),place:values.get('place')||'',start:values.get('start')||'',end:values.get('end')||''});
   if(typeof created.id!=='string'||! /^[A-Za-z0-9_-]{1,128}$/.test(created.id))throw new Error('AI_ADMISSION_UNCONFIRMED');
   run.id=created.id;
   if(!ownsRequest(run)){run.stopped=true;await cancelAccepted(run);return;}
   const pending:Job={id:created.id,state:'preparing',deadline:Number.isFinite(created.deadline)?created.deadline:Date.now()+(mode==='explore'?810000:90000),result:null};
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
 const recheck=async(turn:Turn)=>{if(exportController.current&&!exportController.current.signal.aborted)return;const controller=new AbortController();exportController.current=controller;setBusy(true);setError('');try{const next:Job=await chatApi('jobs/'+turn.job.id,undefined,controller.signal);if(controller.signal.aborted)return;setJob(current=>current?.id===next.id?next:current);setTurns(items=>items.map(item=>item.job.id===next.id?{...item,job:next}:item));}catch{if(!controller.signal.aborted)setError('Sources could not be rechecked. This earlier reply may be out of date; your draft is retained.');}finally{if(exportController.current===controller){exportController.current=null;if(scopeRef.current.mounted)setBusy(false);}}};
 const manager=Boolean(status?.account&&['administrator','steward'].includes(status.role??''));
 const invite=async(event:React.FormEvent<HTMLFormElement>)=>{event.preventDefault();const form=event.currentTarget,values=new FormData(form);setBusy(true);setError('');setInvitation('');try{const created=await api('admin/invite',{username:values.get('username'),role:values.get('role')});setInvitation(created.invitation);form.reset();}catch{setError('Invitation could not be created. Check your permissions and account details.');}finally{setBusy(false);}};
 const sourceContext=mode==='explore'&&focus?.context.selection?.kind==='subsurface';
 const canSubmit=Boolean(chatStatus?.configured&&(mode==='evidence'?chatStatus.evidenceSearchAvailable===true:sourceContext||chatStatus.ready));
 const statusText=!chatStatus?(chatFailure?'AI connection unavailable':'Checking hosted AI'):!chatStatus.configured?'Awaiting owner setup':mode==='evidence'?(chatStatus.evidenceSearchAvailable?'Evidence search available':'Evidence search unavailable'):sourceContext?'Source summary available':!chatStatus.online?'AI unavailable':!chatStatus.ready?'Loading model…':'Qwen3 0.6B ready';
 const notices=<>
   {chatFailure&&<p role='alert' className={styles.notice}>{chatFailure}</p>}
   {error&&<p role='alert' className={styles.notice}>{error}</p>}
   {chatStatus?.configured&&!chatStatus.ready&&(sourceContext||chatStatus.evidenceSearchAvailable)&&<p className={styles.notice}>{sourceContext?'Selected sample summaries use the original source and do not require the AI model. General discussion is unavailable.':'AI discussion is unavailable. Choose Find evidence to search released records without waiting for the model. Records may still be unavailable.'}</p>}
   {exportNotice&&<p role='status' className={styles.notice}>{exportNotice}</p>}
  {requestNotice&&<p role='status' className={styles.notice}>{requestNotice}</p>}
 </>;
 return <div className={styles.chat}>
  <div className={styles.toolbar}><span role='status' className={styles.status}>{statusText}</span><span>No login needed</span></div>
  {accountOpen&&notices}
  {accountOpen&&<section className={styles.account} aria-label='Account controls'>
   {!status?.account?<><h3>Administrator sign-in</h3><p>Only account and stewardship tools require sign-in. Public chat is available without it.</p><form onSubmit={signIn}><label>Username<input ref={loginRef} name='username' required minLength={3} maxLength={64} pattern='[a-z0-9][a-z0-9_-]{2,63}' autoComplete='username'/></label><label>Password<input name='password' type='password' required minLength={14} maxLength={128} autoComplete='current-password'/></label><button disabled={busy||!status?.configured}>Sign in</button></form></>:<><p>Signed in as <strong>{status.account}</strong> · {status.role}</p><button disabled={busy} onClick={async()=>{setBusy(true);try{await api('sign-out',{});setJob(null);setTurns([]);setInvitation('');setActivate(false);await refresh();}catch{setError('Sign-out could not complete.');}finally{setBusy(false);}}}>Sign out</button></>}
   {manager&&<details><summary>Steward tools</summary><form onSubmit={invite}><label>Account username<input name='username' required minLength={3} maxLength={64} pattern='[a-z0-9][a-z0-9_-]{2,63}'/></label><label>Account role<select name='role'><option value='researcher'>Researcher</option>{status?.role==='administrator'&&<option value='steward'>Steward</option>}</select></label><button disabled={busy}>Create invitation</button></form>{invitation&&<p>Deliver privately: <code>{invitation}</code></p>}<button type='button' onClick={()=>setActivate(value=>!value)}>Activate an invited account</button>{activate&&<form onSubmit={async event=>{event.preventDefault();const form=event.currentTarget,values=new FormData(form);setBusy(true);try{await api('activate',{username:values.get('username'),password:values.get('password'),invitation:values.get('invitation')});form.reset();setInvitation('');setActivate(false);await refresh();}catch{setError('Activation failed.');}finally{setBusy(false);}}}><label>Username<input name='username' required autoComplete='username'/></label><label>Invitation code<input name='invitation' type='password' required autoComplete='off'/></label><label>Set password<input name='password' type='password' required minLength={14} maxLength={128} autoComplete='new-password'/></label><button disabled={busy}>Activate and switch account</button></form>}</details>}
  </section>}
  {accountOpen&&<button type='button' onClick={()=>setAccountOpen(false)}>Back to public chat</button>}
  {!accountOpen&&<>
  <div ref={bodyRef} className={styles.body} onScroll={()=>{if(programmaticScrollRef.current){programmaticScrollRef.current=false;return;}nearBottomRef.current=conversationEnd()<=80;}}>
  {notices}
  {focus&&<section className={styles.context} aria-label='AI question context' aria-live='polite'><strong>{focus.title}</strong><p>{focus.detail}</p><small>Sent with each question · map display year {focus.context.frame}, not a collection date</small></section>}
  {surface&&<details className={styles.guide}><summary>Help with {surface.title.toLowerCase()}</summary><p>{surface.guide}</p><small>Interface guide · no model required</small>{!['reports','stories'].includes(surface.id)&&<> · <a href={surface.path}>Open this workspace</a></>}</details>}
  <div ref={logRef} className={styles.messages} role='log' aria-label='KFM chat conversation' aria-live='polite' tabIndex={0}>
   <article className={styles.assistant}><small>KFM</small><p>Explore ideas, ask follow-ups and adjust explanations. Explore produces unverified AI discussion; Evidence searches released KFM records.</p><p>No account is needed for chat. Administrator tools use a separate login.</p></article>
   {turns.map(turn=><div key={turn.job.id}><article className={styles.user}><small>YOU</small><p>{turn.question}</p>{turn.job.context&&<small>About: {turn.job.context.label} · {turn.job.context.boundary}</small>}</article><article className={styles.assistant}><small>KFM · {turn.job.result?.reasonCode==='SOURCE_CONTEXT_ONLY'?'SOURCE CONTEXT':turn.job.result?.reasonCode==='UNVERIFIED_AI_DISCUSSION'?'AI DISCUSSION':turn.job.result?.outcome??turn.job.state.toUpperCase()}</small>{turn.job.result?.answer&&<p>{turn.job.result.answer}</p>}{turn.job.result?.sourceSummary&&<><strong>Source summary · not admitted evidence</strong><p>{turn.job.result.sourceSummary}</p></>}{turn.job.result?.interpretation&&<><strong>Generated discussion · unverified</strong><p>{turn.job.result.interpretation}</p></>}{turn.job.result&&!turn.job.result.answer&&!turn.job.result.interpretation&&!turn.job.result.sourceSummary&&<p>{guidance[turn.job.result.reasonCode]??'KFM withheld an unsupported result.'}</p>}{!turn.job.result&&<p>{running(turn.job)?(turn.job.state==='queued'?'Waiting in the AI queue. Your accepted question will run without resubmitting.':turn.job.state==='preparing'?'Checking the question context…':'Generating your reply…'):turn.job.state==='cancelled'?'Question cancelled.':turn.job.state==='cancel-requested'?'Cancellation requested; server confirmation is pending.':turn.job.state==='cancel-unconfirmed'?'Cancellation could not be confirmed; the earlier reply remains hidden.':turn.job.state==='superseded'?'The earlier request ended; its reply remains hidden.':'The question ended without an answer.'}</p>}{!!turn.job.result?.citations?.length&&<ul>{turn.job.result.citations.map((citation,index)=><li key={citation.evidenceRef+index}><a href={citation.url}>{citation.title}</a></li>)}</ul>}{turn.job.result?.truncated&&<p>This bounded search may omit additional records.</p>}{!!turn.job.context?.references?.length&&<section aria-label='Supporting source references'><strong>Sources to inspect</strong><p>Sources were checked for this response. Recheck before reuse.</p><button type='button' disabled={busy} onClick={()=>void recheck(turn)}>Recheck sources</button><ul>{turn.job.context.references.map((ref,index)=><li key={ref.url+index}><a href={ref.url} target='_blank' rel='noreferrer'>{ref.label}</a><small> · {ref.role==='RELEASED_RECORD'?'Released record; interpretation unverified':'External source context; not admitted evidence'}</small></li>)}</ul></section>}{turn.job.result&&<div className={styles.replyActions}><button type='button' disabled={busy||running(job??undefined)} onClick={()=>setQuestion(turn.question)}>Edit and retry</button><button type='button' disabled={busy||running(job??undefined)} onClick={()=>void exportInvestigation(turn,'clipboard')}>Copy investigation</button><button type='button' disabled={busy||running(job??undefined)} onClick={()=>void exportInvestigation(turn,'markdown')}>Download Markdown</button><button type='button' disabled={busy||running(job??undefined)} onClick={()=>void exportInvestigation(turn,'json')}>Download investigation JSON</button><small>Sources rechecked before saving · draft only</small></div>}{turn.job.result?.contextLimited&&<p>Earlier messages were omitted to fit this small model’s context.</p>}{turn.job.result?.outputLimited&&<><p>This reply is incomplete because it reached a bounded resource limit. Continue resumes the unfinished reply in the same source context when it fits the model’s context.</p><button type='button' disabled={busy||running(job??undefined)||turn.job.id!==job?.id||turn.contextKey!==contextKey||turn.generation!==scopeGeneration} onClick={()=>setQuestion('Continue your previous reply from where it stopped. Finish the explanation without repeating it.')}>Continue reply</button></>}{turn.job.result?.followUpQuestion&&<p><strong>Next step</strong><br />{turn.job.result.followUpQuestion}</p>}</article></div>)}
  </div>
  {prompts.length>0&&<div className={styles.prompts} aria-label='Suggested questions'>{prompts.map(prompt=><button type='button' key={prompt} disabled={busy||running(job??undefined)} onClick={()=>setQuestion(prompt)}>{prompt}</button>)}</div>}
  <footer className={styles.footer}>AI discussion does not establish truth · temporary questions expire after 15 minutes.</footer>
  </div>
  <form onSubmit={ask} className={styles.composer}>
   <details className={styles.options}><summary>Answer options · {mode==='evidence'?'Find evidence':'Explore ideas'}</summary><div className={styles.optionsBody}>
   <label>Conversation mode<select name='mode' value={mode} onChange={event=>setMode(event.target.value)}><option value='explore'>Explore ideas</option><option value='evidence'>Find evidence</option></select></label>
   <div className={styles.dates}><label>Explanation style<select name='style'><option value='plain'>Plain language</option><option value='technical'>Technical</option></select></label><label>Reply length<select name='depth' defaultValue='expanded'><option value='brief'>Brief</option><option value='expanded'>More detail</option></select></label></div>
   <small>{mode==='explore'?(sourceContext?'Selected sample replies summarize the original source; they are not admitted evidence.':'Ideas and explanations are generated, unverified discussion.'):'Evidence mode uses only released records; unsupported factual answers are withheld.'}</small>
   <details><summary>Evidence search filters</summary><label>Search terms<input name='term' maxLength={120} placeholder='Defaults to your message'/></label><label>Place filter<input name='place' defaultValue={place} maxLength={160} placeholder='Named place or county'/></label><div className={styles.dates}><label>From<input name='start' type='date'/></label><label>Through<input name='end' type='date'/></label></div><small>Date filters exclude undated records.</small></details>
   </div></details>
   <label><span className={styles.srOnly}>Message KFM</span><textarea value={question} onChange={event=>setQuestion(event.target.value)} rows={2} maxLength={4096} placeholder='Message KFM…'/></label><div className={styles.actions}><small>{mode==='evidence'?'Released records · no model required · unsupported answers withheld':sourceContext?'Source summary · no model required · not admitted evidence':'Qwen3 0.6B on this server · no account needed · unverified discussion'}</small>{requestPhase!=='idle'?<>{running(job??undefined)&&<button type='button' disabled={busy} onClick={()=>setJobRetry(value=>value+1)}>Retry status</button>}<button type='button' disabled={requestPhase==='stopping'} onClick={()=>stopRequest()}>Stop</button></>:<button disabled={busy||!canSubmit||question.trim().length<2}>{busy?'Sending…':mode==='evidence'?'Search':'Send'}</button>}</div>
  </form>
  </>}
 </div>;
}
