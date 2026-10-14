'use client';
import {useCallback,useEffect,useState} from 'react';
import Link from 'next/link';
import styles from './workspace.module.css';
type Status={configured:boolean;online:boolean;ready:boolean;account:string|null;role?:string|null};
type Result={outcome:string;reasonCode:string;answer:string|null;interpretation:string|null;truncated?:boolean;citations?:{evidenceRef:string;title:string;url:string}[]};
type Job={id:string;state:string;deadline:number;result:Result|null};
async function api(path:string,body?:object,signal?:AbortSignal){
  const response=await fetch('/api/pc-ai/'+path,{method:body?'POST':'GET',credentials:'same-origin',cache:'no-store',signal:signal?AbortSignal.any([signal,AbortSignal.timeout(8000)]):AbortSignal.timeout(8000),headers:body?{'Content-Type':'application/json'}:undefined,body:body?JSON.stringify(body):undefined});
  const result=await response.json();if(!response.ok)throw new Error(result.reasonCode??'PC_AI_UNAVAILABLE');return result;
}
const guidance:Record<string,string>={PC_OFFLINE:'The owner’s PC is offline or its model is unavailable. Try again when it reconnects.',USER_BUSY:'You already have a question in progress.',QUEUE_FULL:'The research queue is full. Try again shortly.',USER_RATE_LIMIT:'You have reached the hourly question limit.',SIGN_IN_DENIED:'Sign-in failed. Check your account details or invitation.',SIGN_IN_RATE_LIMIT:'Too many sign-in attempts. Wait before trying again.',NO_RELEASED_EVIDENCE:'No eligible released evidence is available for this search. KFM has abstained.',RELEASE_CHANGED:'The evidence release changed or became unavailable. The answer has been withheld.',POLICY_WITHHELD:'This question is withheld by KFM’s policy controls.',PC_AI_NOT_CONFIGURED:'The PC assistant is awaiting owner configuration.',PC_AI_STORAGE_HOLD:'The private database is unavailable or held by another process.',INFERENCE_FAILED:'The PC could not complete this inference.',EVIDENCE_NOT_SUPPORTIVE:'The available evidence does not support an answer.'};
export default function AssistantWorkspace(){
  const [status,setStatus]=useState<Status|null>(null),[error,setError]=useState(''),[busy,setBusy]=useState(false),[job,setJob]=useState<Job|null>(null),[activate,setActivate]=useState(false),[invitation,setInvitation]=useState('');
  const refresh=useCallback(async(signal?:AbortSignal)=>{try{setStatus(await api('status',undefined,signal));}catch{if(!signal?.aborted)setStatus(null);}},[]);
  useEffect(()=>{const controller=new AbortController();queueMicrotask(()=>{if(!controller.signal.aborted)void refresh(controller.signal);});const timer=setInterval(()=>void refresh(controller.signal),5000);return()=>{clearInterval(timer);controller.abort();};},[refresh]);
  const id=job?.id,state=job?.state;
  useEffect(()=>{
    if(!id||!['queued','running'].includes(state??''))return;
    const controller=new AbortController();let timer:ReturnType<typeof setTimeout>;
    const poll=async()=>{try{const next:Job=await api('jobs/'+id,undefined,controller.signal);if(!controller.signal.aborted){setJob(next);setError('');if(['queued','running'].includes(next.state))timer=setTimeout(poll,2000);}}
      catch{if(!controller.signal.aborted){setError('Connection interrupted. Your job remains subject to its deadline.');timer=setTimeout(poll,4000);}}};
    void poll();return()=>{controller.abort();clearTimeout(timer);};
  },[id,state]);
  const signIn=async(event:React.FormEvent<HTMLFormElement>)=>{
    event.preventDefault();const form=event.currentTarget,values=new FormData(form);setBusy(true);setError('');
    try{await api('sign-in',{username:values.get('username'),password:values.get('password'),});form.reset();await refresh();}
    catch(reason){setError(guidance[(reason as Error).message]??'Sign-in could not complete.');}finally{setBusy(false);}
  };
  const ask=async(event:React.FormEvent<HTMLFormElement>)=>{
    event.preventDefault();const values=new FormData(event.currentTarget);setBusy(true);setError('');
    try{const created=await api('jobs',{question:values.get('question'),term:values.get('term'),place:values.get('place'),start:values.get('start'),end:values.get('end')});setJob(await api('jobs/'+created.id));}
    catch(reason){setError(guidance[(reason as Error).message]??'Research is unavailable. No fallback answer was generated.');}finally{setBusy(false);}
  };
  const manager=Boolean(status?.account&&['administrator','steward'].includes(status.role??''));
  const invite=async(event:React.FormEvent<HTMLFormElement>)=>{event.preventDefault();const form=event.currentTarget,values=new FormData(form);setBusy(true);setError('');setInvitation('');try{const created=await api('admin/invite',{username:values.get('username'),role:values.get('role')});setInvitation(created.invitation);form.reset();}catch{setError('Invitation could not be created. Check your permissions and account details.');}finally{setBusy(false);}};
  const statusText=!status?'Checking connection':!status.configured?'Awaiting owner setup':!status.online?'Owner’s PC offline':!status.ready?'PC connected; model unavailable':'PC ready';
  return <main className={styles.page}>
    <header><Link href='/'>← Back to the map</Link><p className={styles.eyebrow}>KANSAS FRONTIER MATRIX</p><h1>Ask KFM</h1><p>Research released records across places and time. Qwen runs on the owner’s PC; KFM supplies and checks the evidence.</p><p className={styles.status} role='status'>{statusText}</p></header>
    {error&&<p role='alert' className={styles.notice}>{error}</p>}
    {!status?.account?<section className={styles.card}><h2>Log in</h2><p>Sign in to open your permitted KFM functions. The map remains available without an account.</p>
      <form onSubmit={signIn}><label>Username<input name='username' required minLength={3} maxLength={64} pattern='[a-z0-9][a-z0-9_-]{2,63}' autoComplete='username'/></label>

        <label>Password<input name='password' type='password' required minLength={14} maxLength={128} autoComplete='current-password'/></label>
        <button disabled={busy||!status?.configured}>{busy?'Working…':'Sign in'}</button>
      </form>
    </section>:<section className={styles.card}><div className={styles.row}><h2>Research a question</h2><button className={styles.secondary} disabled={busy} onClick={async()=>{setBusy(true);try{await api('sign-out',{});setJob(null);await refresh();}catch{setError('Sign-out could not complete.');}finally{setBusy(false);}}}>Sign out {status.account}</button></div>
      <form onSubmit={ask}><label>Your question<textarea name='question' rows={4} required maxLength={4096}/></label><label>Search terms<input name='term' required minLength={2} maxLength={120} placeholder='For example: river history'/></label>
        <label>Place filter <span>(optional)</span><input name='place' maxLength={160} placeholder='A named place or county'/></label>
        <div className={styles.row}><label>From <span>(optional)</span><input name='start' type='date'/></label><label>Through <span>(optional)</span><input name='end' type='date'/></label></div>
        <p className={styles.detail}>Date filters exclude undated records. Questions are limited to released evidence; missing records, restricted questions, and unsupported claims produce a clear gap or denial.</p>
        <button disabled={busy||!status.ready||['queued','running'].includes(job?.state??'')}>{busy?'Submitting…':'Ask KFM'}</button>
      </form>
    </section>}
    {manager&&<section className={styles.card}><h2>Steward tools</h2><p>Signed in as {status?.role}. Invitations expire after 24 hours and can be used once.</p><form onSubmit={invite}><label>Account username<input name='username' required minLength={3} maxLength={64} pattern='[a-z0-9][a-z0-9_-]{2,63}'/></label><label>Account role<select name='role'><option value='researcher'>Researcher</option>{status?.role==='administrator'&&<option value='steward'>Steward</option>}</select></label><button disabled={busy}>Create invitation</button></form>{invitation&&<p role='status'>Deliver this code privately: <code>{invitation}</code></p>}<button className={styles.secondary} onClick={()=>setActivate(value=>!value)}>Activate an invited account</button>{activate&&<form onSubmit={async event=>{event.preventDefault();const form=event.currentTarget,values=new FormData(form);setBusy(true);try{await api('activate',{username:values.get('username'),password:values.get('password'),invitation:values.get('invitation')});form.reset();setInvitation('');setActivate(false);await refresh();}catch{setError('Activation failed.');}finally{setBusy(false);}}}><label>Username<input name='username' required autoComplete='username'/></label><label>Invitation code<input name='invitation' type='password' required autoComplete='off'/></label><label>Set password<input name='password' type='password' required minLength={14} maxLength={128} autoComplete='new-password'/></label><button disabled={busy}>Activate account and switch session</button></form>}</section>}
    {job&&<section className={styles.card} aria-live='polite'><div className={styles.row}><h2>{job.result?.outcome??({'queued':'Queued','running':'PC is researching','expired':'Question expired','cancelled':'Question cancelled'}[job.state]??'Research status')}</h2>
      {['queued','running'].includes(job.state)&&<button className={styles.secondary} disabled={busy} onClick={async()=>{setBusy(true);try{await api('jobs/'+job.id+'/cancel',{});setJob(await api('jobs/'+job.id));}catch{setError('Cancellation could not be confirmed.');}finally{setBusy(false);}}}>Cancel question</button>}</div>
      {job.result?.answer&&<><h3>Supported facts</h3><p className={styles.answer}>{job.result.answer}</p></>}
      {job.result?.interpretation&&<><h3>Model interpretation</h3><p className={styles.answer}>{job.result.interpretation}</p></>}
      {job.result&&!job.result.answer&&<p>{guidance[job.result.reasonCode]??'KFM withheld an unsupported result.'}</p>}
      {!!job.result?.citations?.length&&<><h3>Evidence</h3><ul>{job.result.citations.map((citation,index)=><li key={citation.evidenceRef+index}><Link href={citation.url}>{citation.title}</Link><small>{citation.evidenceRef}</small></li>)}</ul></>}
      {job.result?.truncated&&<p className={styles.detail}>This bounded search may omit additional matching records.</p>}
      {['queued','running'].includes(job.state)&&<p className={styles.detail}>One question runs at a time. Jobs expire within three minutes and are not automatically rerun.</p>}
    </section>}
    <footer className={styles.detail}>Generated interpretation does not change evidence, review, policy, or release state. Question and answer payloads expire after 24 hours; minimal job metadata expires after 30 days.</footer>
  </main>;
}
