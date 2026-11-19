import assert from 'node:assert/strict';
import {spawn} from 'node:child_process';
import {createHash} from 'node:crypto';
import {mkdir,mkdtemp,readdir,readFile,realpath,rm,stat,writeFile} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {dirname,isAbsolute,relative,resolve,sep} from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {applicationIdentity,verifyHostedIdentity} from './build-identity.mjs';
import {recoveredObservations} from './local-data/recovered.mjs';

const ROOT=fileURLToPath(new URL('../',import.meta.url));
export const ARCHIVE_ORIGIN='https://kansasfrontiermatrix.com';
const COLLECTIONS=new Set(['daily-values','field-measurements','peaks','sites','series'].map(name=>'observations-usgs-'+name));
const inside=(root,path)=>{const part=relative(root,path);return !part||!part.startsWith('..'+sep)&&part!=='..'&&!isAbsolute(part);};

export function verifierOptions(argv,repoRoot=ROOT,cwd=process.cwd()){
 const flags=new Map();
 for(const arg of argv){
  const match=/^--(candidate|output|chrome)=(.+)$/.exec(arg);
  if(!match||flags.has(match[1]))throw new Error('Use unique --candidate=URL, --output=DIR and optional --chrome=PATH arguments.');
  flags.set(match[1],match[2]);
 }
 const candidate=new URL(flags.get('candidate')??'http://127.0.0.1:8797');
 if(candidate.protocol!=='http:'||!['127.0.0.1','localhost','[::1]'].includes(candidate.hostname)||candidate.username||candidate.password||candidate.pathname!=='/'||candidate.search||candidate.hash){
  throw new Error('The candidate must be a loopback HTTP origin without credentials, path or query.');
 }
 if(!flags.has('output'))throw new Error('Choose an empty --output directory outside the application checkout.');
 const output=resolve(cwd,flags.get('output'));
 if(inside(resolve(repoRoot),output))throw new Error('Verification records must stay outside the application checkout.');
 return {candidate:candidate.origin,output,chrome:flags.get('chrome')??'/usr/bin/google-chrome'};
}

/** Only the five existing public USGS record collections can cross this bridge. */
export function archiveRequest(input,candidate){
 const url=new URL(input);
 if(url.origin!==candidate||url.pathname!=='/api/local-data/recovered-observations'||url.username||url.password||url.hash)throw new Error('Unexpected candidate archive route.');
 const search=url.searchParams;
 if([...search.keys()].some(key=>!['collection','limit','after'].includes(key)||search.getAll(key).length!==1))throw new Error('Unexpected or repeated archive parameter.');
 const query=recoveredObservations.parse(Object.fromEntries(search));
 if(!COLLECTIONS.has(query.collection))throw new Error('Only water observation, station and series samples are permitted.');
 return {path:url.pathname+url.search,collection:query.collection,limit:query.limit};
}

export function archivePage(reply,query){
 assert.equal(reply.status,200,'Live archive did not return a record page.');
 assert.match(reply.contentType??'',/^application\/json(?:;|$)/i);
 const answer=JSON.parse(reply.text);
 assert.equal(answer.format,'kfm-local-data-v1');assert.equal(answer.dataset,'recovered-observations');
 assert.equal(answer.collection,query.collection);assert.equal(answer.total,null);
 assert.ok(Array.isArray(answer.rows)&&answer.rows.length<=query.limit&&answer.count===answer.rows.length);
 assert.ok(['live','fresh','stale'].includes(answer.cache?.state),'Archive cache state is missing or unknown.');
 assert.ok(typeof answer.cache.at==='string'&&answer.cache.at.length>0&&answer.cache.at.length<=80);
 return answer;
}

export function expectedExportNames(collection){
 if(!COLLECTIONS.has(collection))throw new Error('Unknown export collection.');
 return [collection+'-lab.json',collection+'-research-brief.md'];
}
export function exportsReady(names,collection){return expectedExportNames(collection).every(name=>names.includes(name));}

export async function prepareVerifierOutput(output,repoRoot=ROOT){
 const repo=await realpath(repoRoot);let ancestor=output;
 while(true){try{await realpath(ancestor);break;}catch(error){if(error.code!=='ENOENT')throw error;ancestor=dirname(ancestor);}}
 if(inside(repo,resolve(await realpath(ancestor),relative(ancestor,output))))throw new Error('Output symlinks must not point into the application checkout.');
 await mkdir(output,{recursive:true});
 if(inside(repo,await realpath(output)))throw new Error('Output symlinks must not point into the application checkout.');
 if((await readdir(output)).length)throw new Error('The output directory must be empty; previous evidence will not be overwritten.');
}

export async function verifyRecordContextLive(options){
 await prepareVerifierOutput(options.output);
 const expected=await applicationIdentity(ROOT);
 const binding=await verifyHostedIdentity(expected,options.candidate);
 assert.equal(binding.outcome,'APPLICATION_INPUTS_MATCH','Rebuild the candidate from this checkout before verifying.');
 const profile=await mkdtemp(resolve(tmpdir(),'kfm-record-context-live-'));
 const child=spawn(options.chrome,['--headless=new','--remote-debugging-pipe',`--user-data-dir=${profile}`,
  '--no-first-run','--no-default-browser-check','--disable-gpu','--disable-background-networking','--disable-dev-shm-usage','about:blank'],
 {stdio:['ignore','ignore','pipe','pipe','pipe']});
 let sequence=0,buffer='',diagnostic='',onRequest;
 const pending=new Map(),errors=[],requests=[],results=[],observed=new Map(),held=[],additionalFiles=[];
 let mode='live';
 const timeout=setTimeout(()=>child.kill(),8*60_000);
 const rejectPending=error=>{for(const item of pending.values())item.reject(error);pending.clear();};
 child.on('error',()=>rejectPending(new Error('Chrome could not start. Set --chrome to an installed Chrome executable.')));
 child.on('exit',()=>rejectPending(new Error('Verification browser exited. '+diagnostic)));
 child.stdio[3].on('error',()=>rejectPending(new Error('Chrome command pipe closed.')));
 child.stdio[4].on('error',()=>rejectPending(new Error('Chrome response pipe closed.')));
 child.stderr.on('data',data=>{diagnostic=(diagnostic+data).slice(-1000);});
 child.stdio[4].on('data',chunk=>{
  buffer+=chunk.toString();let index;
  while((index=buffer.indexOf('\0'))>=0){
   const message=JSON.parse(buffer.slice(0,index));buffer=buffer.slice(index+1);
   if(message.id){
    const handler=pending.get(message.id);
    if(handler){pending.delete(message.id);if(message.error)handler.reject(new Error(message.error.message));else handler.resolve(message.result);}
   }
   if(message.method==='Runtime.exceptionThrown')errors.push(message.params.exceptionDetails.text);
   if(message.method==='Fetch.requestPaused'&&onRequest)onRequest(message).catch(async error=>{
    errors.push(error.message);await call('Fetch.failRequest',{requestId:message.params.requestId,errorReason:'Failed'},message.sessionId).catch(()=>{});
   });
  }
 });
 function call(method,params={},sessionId){return new Promise((resolve,reject)=>{
  const id=++sequence,timer=setTimeout(()=>{pending.delete(id);reject(new Error('Browser timeout: '+method));},60_000);
  pending.set(id,{resolve:value=>{clearTimeout(timer);resolve(value);},reject:error=>{clearTimeout(timer);reject(error);}});
  child.stdio[3].write(JSON.stringify({id,method,params,...(sessionId?{sessionId}:{})})+'\0');
 });}
 const pause=ms=>new Promise(resolve=>setTimeout(resolve,ms));
 async function target(){
  const {targetId}=await call('Target.createTarget',{url:'about:blank'});
  const {sessionId}=await call('Target.attachToTarget',{targetId,flatten:true});
  const send=(method,params={})=>call(method,params,sessionId);
  await send('Runtime.enable');await send('Page.enable');
  const evaluate=async expression=>{
   const result=await send('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true,userGesture:true});
   if(result.exceptionDetails)throw new Error(result.exceptionDetails.exception?.description??result.exceptionDetails.text);
   return result.result.value;
  };
  return {sessionId,send,evaluate};
 }
 async function until(check,label){
  const end=Date.now()+125_000;
  while(Date.now()<end){if(errors.length)throw new Error(errors[0]);if(await check())return;await pause(150);}
  throw new Error('Timed out: '+label);
 }
 let candidate,archive,archiveIdentity;
 try{
  archive=await target();candidate=await target();
  await archive.send('Page.navigate',{url:ARCHIVE_ORIGIN+'/data-lab?collection=observations-usgs-daily-values'});
  await until(()=>archive.evaluate('document.readyState==="complete"'),'public archive browser');
  async function publicRead(path){
   return archive.evaluate(`(async()=>{
    const response=await fetch(${JSON.stringify(path)},{cache:'no-store',credentials:'omit',redirect:'error',signal:AbortSignal.timeout(45000)});
    const reader=response.body.getReader(),chunks=[];let length=0;
    try{while(true){const {done,value}=await reader.read();if(done)break;length+=value.byteLength;if(length>1000000)throw new Error('Oversized public response');chunks.push(value);}}finally{await reader.cancel();}
    const bytes=new Uint8Array(length);let offset=0;for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.length;}
    return {status:response.status,contentType:response.headers.get('content-type'),text:new TextDecoder().decode(bytes)};
   })()`);
  }
  const identityReply=await publicRead('/api/build');assert.equal(identityReply.status,200);
  archiveIdentity=JSON.parse(identityReply.text);assert.equal(archiveIdentity.application,expected.application);
  onRequest=async message=>{
   assert.equal(message.sessionId,candidate.sessionId);
   const {requestId,request}=message.params,query=archiveRequest(request.url,options.candidate);
   assert.equal(request.method,'GET');
   if(mode==='hold'){held.push(requestId);return;}
   if(mode==='offline'){
    await candidate.send('Fetch.fulfillRequest',{requestId,responseCode:503,responseHeaders:[{name:'Content-Type',value:'application/json'}],body:Buffer.from('{"state":"local-data-offline","reasonCode":"LOCAL_DATA_UNAVAILABLE"}').toString('base64')});return;
   }
   assert.ok(requests.length<60,'Public sample request budget exceeded.');
   const reply=await publicRead(query.path),answer=archivePage(reply,query);
   const entry={collection:query.collection,path:query.path,count:answer.count,generatedAt:answer.generatedAt,cache:answer.cache,
    responseSha256:'sha256:'+createHash('sha256').update(reply.text).digest('hex')};
   requests.push(entry);observed.set(query.collection,[...(observed.get(query.collection)??[]),...answer.rows]);
   await writeFile(resolve(options.output,`response-${String(requests.length).padStart(2,'0')}.json`),reply.text);
   await candidate.send('Fetch.fulfillRequest',{requestId,responseCode:reply.status,responseHeaders:[{name:'Content-Type',value:reply.contentType}],body:Buffer.from(reply.text).toString('base64')});
  };
  await candidate.send('Fetch.enable',{patterns:[{urlPattern:options.candidate+'/api/local-data/*',requestStage:'Request'}]});
  const evaluate=candidate.evaluate;
  const button=text=>evaluate(`Array.from(document.querySelectorAll('button')).find(b=>b.textContent.trim()===${JSON.stringify(text)}).click();true`);
  const panel=()=>evaluate('document.querySelector("section[aria-labelledby=record-context-title]")?.textContent??""');
  async function exportFiles(directory,collection){
   const expectedNames=expectedExportNames(collection);
   await mkdir(directory);await call('Browser.setDownloadBehavior',{behavior:'allow',downloadPath:directory,eventsEnabled:true});
   for(const prefix of ['Download lab data + metadata','Download story brief']){
    await evaluate(`Array.from(document.querySelectorAll('button')).find(b=>b.textContent.startsWith(${JSON.stringify(prefix)})).click();true`);
   }
   await until(async()=>exportsReady(await readdir(directory),collection),'connected downloads');
   for(const name of await readdir(directory))if(!expectedNames.includes(name)){
    additionalFiles.push({path:relative(options.output,resolve(directory,name)),bytes:(await stat(resolve(directory,name))).size,
     scope:'Additional browser artifact, excluded from JSON/story export evidence.'});
   }
   const path=resolve(directory,expectedNames[0]);
   return {path,bundle:JSON.parse(await readFile(path,'utf8')),brief:await readFile(resolve(directory,expectedNames[1]),'utf8')};
  }
  for(const name of ['daily-values','field-measurements','peaks']){
   observed.clear();const firstRequest=requests.length,id='observations-usgs-'+name;
   await candidate.send('Emulation.setDeviceMetricsOverride',{width:1440,height:1000,deviceScaleFactor:1,mobile:false});
   await candidate.send('Page.navigate',{url:options.candidate+'/data-lab?collection='+id});
   await until(()=>evaluate(`document.querySelector('select')?.value===${JSON.stringify(id)}`),'candidate collection');
   await button('Load up to 250 records');
   await until(()=>evaluate('!!document.querySelector("#record-context-title")'),'live observations');
   await button('Load station sample');
   await until(async()=>(await panel()).includes('metadata records attached'),'live station metadata');
   if(name!=='field-measurements'){
    await button('Load series sample');
    await until(()=>evaluate('document.querySelectorAll("section[aria-labelledby=record-context-title] article").length===2'),'live series metadata');
   }
   const directory=resolve(options.output,name);await mkdir(directory);
   const exported=await exportFiles(resolve(directory,'original'),id);
   assert.deepEqual(exported.bundle.records,observed.get(id),'Observation values or provenance changed.');
   assert.ok(exported.bundle.records.length>0&&exported.bundle.records.length<=250);
   assert.equal(exported.bundle.contexts.length,name==='field-measurements'?1:2);
   for(const context of exported.bundle.contexts)assert.deepEqual(context.records,observed.get(context.collection),'Metadata values or provenance changed.');
   for(const relation of exported.bundle.connections.relations){
    const counts=relation.counts;
    assert.equal(counts.oneMatch+counts.multipleMatches+counts.noMatch+counts.missingKey,exported.bundle.records.length);
    assert.deepEqual(relation.rows.map(row=>row.sourceRecordId),exported.bundle.records.map(row=>row.id));
    const metadata=exported.bundle.contexts.find(context=>context.collection===relation.targetCollection);
    for(const row of relation.rows)for(const match of row.matches){
     const target=metadata.records.find(record=>record.id===match.targetRecordId);
     assert.ok(target,'A context link references a missing metadata record.');
     assert.equal(target.values[relation.keys[0].target],row.providerKey);
     if(relation.expectedDataType)assert.equal(target.values.data_type,relation.expectedDataType);
    }
   }
   assert.equal(exported.bundle.profile.credit.aiReview,null);assert.match(exported.brief,/Connected metadata samples/);
   let failureRetention=null;
   if(name==='daily-values'){
    mode='hold';await button('Reload series sample');await until(async()=>held.length>0,'cancellable metadata request');
    await button('Cancel metadata read');
    for(const requestId of held)await candidate.send('Fetch.failRequest',{requestId,errorReason:'Aborted'}).catch(()=>{});
    await until(async()=>(await panel()).includes('Metadata read cancelled.'),'cancelled metadata retained');
    mode='offline';await button('Reload series sample');
    await until(async()=>(await panel()).includes('Metadata could not be loaded. Existing context was retained.'),'offline metadata retained');
    mode='live';
    const retained=await exportFiles(resolve(directory,'after-denied-reads'),id);
    assert.deepEqual(retained.bundle.contexts,exported.bundle.contexts);
    assert.deepEqual(retained.bundle.connections,exported.bundle.connections);
    failureRetention={cancelledCandidateRead:true,injectedCandidate503:true,contextsUnchanged:true,productionServicesInterrupted:false};
   }
   await evaluate('Array.from(document.querySelectorAll("summary")).find(s=>s.textContent==="Reopen a saved lab bundle").click();true');
   const document=await candidate.send('DOM.getDocument');
   const {nodeId}=await candidate.send('DOM.querySelector',{nodeId:document.root.nodeId,selector:'input[type=file]'});
   await candidate.send('DOM.setFileInputFiles',{nodeId,files:[exported.path]});
   await until(()=>evaluate(`document.querySelector('[role=status]').textContent.includes('saved records opened')`),'connected bundle reopening');
   const reopened=await exportFiles(resolve(directory,'reopened'),id);
   assert.deepEqual(reopened.bundle.records,exported.bundle.records);
   assert.deepEqual(reopened.bundle.contexts.map(c=>c.records),exported.bundle.contexts.map(c=>c.records));
   assert.deepEqual(reopened.bundle.connections.relations.map(r=>r.rows),exported.bundle.connections.relations.map(r=>r.rows));
   assert.equal(reopened.bundle.question,exported.bundle.question);assert.deepEqual(reopened.bundle.view,exported.bundle.view);
   for(const width of [1440,390]){
    await candidate.send('Emulation.setDeviceMetricsOverride',{width,height:width===390?844:1000,deviceScaleFactor:1,mobile:width===390});
    await evaluate('document.querySelector("section[aria-labelledby=record-context-title] article").scrollIntoView({block:"start"});true');await pause(100);
    assert.equal(await evaluate('document.documentElement.scrollWidth>innerWidth+1'),false);
    await writeFile(resolve(directory,`context-${width}.png`),Buffer.from((await candidate.send('Page.captureScreenshot',{format:'png'})).data,'base64'));
   }
   results.push({collection:id,sourceRecords:exported.bundle.records.length,contextRecords:exported.bundle.contexts.reduce((n,c)=>n+c.records.length,0),
    relations:exported.bundle.connections.relations.map(r=>({target:r.targetCollection,counts:r.counts})),archiveRequests:requests.length-firstRequest,
    originalRowsPreserved:true,reopened:true,desktopOverflow:false,mobileOverflow:false,failureRetention});
   console.log(JSON.stringify({verified:id,records:exported.bundle.records.length,requests:requests.length-firstRequest}));
  }
  assert.deepEqual(errors,[]);
  assert.equal((await applicationIdentity(ROOT)).sourceDigest,expected.sourceDigest,'Application inputs changed during verification.');
  const report={passed:true,checkedAt:new Date().toISOString(),candidate:{origin:options.candidate,...expected},archive:{origin:ARCHIVE_ORIGIN,...archiveIdentity},
   delivery:'Local candidate UI bridged by this browser verifier to actual public archive replies. This does not establish a public deployment of the candidate.',
   recordInstancesPreserved:results.reduce((n,r)=>n+r.sourceRecords+r.contextRecords,0),results,requests,
   cachedRequests:requests.filter(r=>r.cache?.state!=='live').length,liveRequests:requests.filter(r=>r.cache?.state==='live').length,
   failureScope:'Cancellation and 503 were injected only at the local candidate; the production worker and gateway remained running.',additionalFiles,errors};
  await writeFile(resolve(options.output,'verification.json'),JSON.stringify(report,null,2)+'\n');
  return report;
 }catch(error){
  await writeFile(resolve(options.output,'failure.json'),JSON.stringify({passed:false,message:error.message,requests,results,errors},null,2)+'\n');throw error;
 }finally{
  clearTimeout(timeout);try{await call('Browser.close');}catch{child.kill();}
  await pause(300);if(child.exitCode===null)child.kill();await rm(profile,{recursive:true,force:true});
 }
}

if(process.argv[1]&&import.meta.url===pathToFileURL(resolve(process.argv[1])).href){
 if(process.argv.slice(2).includes('--help'))console.log('node scripts/verify-record-context-live.mjs --candidate=http://127.0.0.1:8797 --output=/absolute/empty/directory [--chrome=/usr/bin/google-chrome]\nReads existing public USGS samples through Chrome. Keeps candidate and public build identities separate; writes no application data.');
 else verifyRecordContextLive(verifierOptions(process.argv.slice(2))).then(report=>console.log(JSON.stringify({passed:report.passed,recordInstancesPreserved:report.recordInstancesPreserved,liveRequests:report.liveRequests,cachedRequests:report.cachedRequests}))).catch(error=>{console.error(error.message);process.exitCode=1;});
}
