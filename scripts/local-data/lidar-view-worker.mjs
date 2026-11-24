#!/usr/bin/env node
// One bounded local preparation actor. Public HTTPS sources are fixed by the
// hash-pinned Kansas catalog; a visitor can supply only a canonical map view.
import {writeFileSync,existsSync,renameSync,unlinkSync,readdirSync,openSync,closeSync,constants,mkdtempSync,statfsSync} from 'node:fs';
import {join,dirname,isAbsolute} from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createHash,randomBytes} from 'node:crypto';
import {spawn} from 'node:child_process';
import {normalizeLidarView,lidarViewKey,validLidarView,validNativeViewManifest,validNativeViewChunk,validLidarGrid} from './lidar-view-model.mjs';
import {loadLidarDiscovery,privateViewDir,readPrivateViewFile,selectViewProjects,initialLidarView,viewAcquisition,viewVertical,lidarViewConfig} from './lidar-view.mjs';
const sha=b=>'sha256:'+createHash('sha256').update(b).digest('hex'),here=dirname(fileURLToPath(import.meta.url));
export const PREPARE_LIMITS=Object.freeze({nodes:128,nativeRecords:2000000,transferBytes:64*1024*1024,hierarchyReplies:64,jobMs:180000,sourceCacheBytes:500*1024**3});
const json=b=>JSON.parse(b.toString('utf8'));
const encode=v=>Buffer.from(JSON.stringify(v)+'\n');
function writeNew(dir,name,bytes){const p=join(dir,name);writeFileSync(p,bytes,{mode:0o600,flag:'wx'});if(sha(readPrivateViewFile(p,Math.max(bytes.length,1)))!==sha(bytes))throw Error('WRITE_READBACK_FAILED');return p;}
function atomic(dir,name,value){const bytes=encode(value),tmp='.'+name+'-'+randomBytes(8).toString('hex');writeNew(dir,tmp,bytes);renameSync(join(dir,tmp),join(dir,name));return sha(bytes);}
export function boundsMercator(b){const R=6378137,rad=Math.PI/180;return [R*b[0]*rad,R*Math.log(Math.tan(Math.PI/4+b[1]*rad/2)),R*b[2]*rad,R*Math.log(Math.tan(Math.PI/4+b[3]*rad/2))];}
export function nodeBounds(cube,key){const [depth,x,y,z]=key.split('-').map(Number),side=(cube[3]-cube[0])/2**depth;return [cube[0]+x*side,cube[1]+y*side,cube[2]+z*side,cube[0]+(x+1)*side,cube[1]+(y+1)*side,cube[2]+(z+1)*side];}
const intersectXY=(a,b)=>a[0]<=b[2]&&a[3]>=b[0]&&a[1]<=b[3]&&a[4]>=b[1];
function sourceUrlValid(url){const {projects}=loadLidarDiscovery();try{const u=new URL(url),parts=u.pathname.split('/');return u.protocol==='https:'&&u.host==='usgs-lidar-public.s3.amazonaws.com'&&!u.search&&!u.hash&&!u.username&&!u.password&&projects.has(parts[1])&&parts.length===4&&['ept-data','ept-hierarchy'].includes(parts[2])&&/^\d{1,2}-\d{1,10}-\d{1,10}-\d{1,10}\.(?:json|laz)$/.test(parts[3])&&(parts[2]==='ept-data'?parts[3].endsWith('.laz'):parts[3].endsWith('.json'));}catch{return false;}}
export function createSourceReader(root,{fetcher=fetch,clock=Date.now,signal}={}){
 const cache=privateViewDir(join(root,'cache'),true);let transfer=0,replies=0;
 const ledgerPath=join(cache,'ledger.json');let stored=existsSync(ledgerPath)?json(readPrivateViewFile(ledgerPath,4096)).bytes:0;
 if(!Number.isSafeInteger(stored)||stored<0||stored>PREPARE_LIMITS.sourceCacheBytes)throw Error('SOURCE_CACHE_LEDGER_INVALID');
 return {get transferBytes(){return transfer;},get replies(){return replies;},async get(url,max){
  if(!sourceUrlValid(url))throw Error('SOURCE_NOT_ALLOWLISTED');signal?.throwIfAborted();const key=createHash('sha256').update(url).digest('hex'),path=join(cache,key+'.bin'),receiptPath=join(cache,key+'.json');
  if(existsSync(receiptPath)){
   const r=json(readPrivateViewFile(receiptPath,4096));if(r.url!==url||!Number.isSafeInteger(r.bytes)||r.bytes<1||r.bytes>max)throw Error('SOURCE_CACHE_INVALID');const bytes=readPrivateViewFile(path,max,r.sha256);if(bytes.length!==r.bytes)throw Error('SOURCE_CACHE_INVALID');transfer+=bytes.length;if(transfer>PREPARE_LIMITS.transferBytes)throw Error('TRANSFER_BUDGET');return {...r,path,bytesValue:bytes};
  }
  let failure;
  for(let attempt=0;attempt<3;attempt++)try{
   const r=await fetcher(url,{redirect:'error',signal:signal?AbortSignal.any([signal,AbortSignal.timeout(15000)]):AbortSignal.timeout(15000)});if(r.status!==200){void r.body?.cancel();throw Error('SOURCE_HTTP_'+r.status);}const encoding=r.headers.get('content-encoding'),declared=encoding&&encoding!=='identity'?0:Number(r.headers.get('content-length'));if(declared>max){void r.body?.cancel();throw Error('SOURCE_SIZE');}
   let length=0;const parts=[];try{for await(const b of r.body){signal?.throwIfAborted();length+=b.length;if(length>max||transfer+length>PREPARE_LIMITS.transferBytes)throw Error('TRANSFER_BUDGET');parts.push(b);}}catch(e){void r.body?.cancel().catch(()=>{});throw e;}
   if(!length||declared&&declared!==length)throw Error('SOURCE_SIZE');if(stored+length>PREPARE_LIMITS.sourceCacheBytes)throw Error('SOURCE_CACHE_BUDGET');
   const disk=statfsSync(cache);if(disk.bavail*disk.bsize<2*1024**3+length)throw Error('SOURCE_DISK_RESERVE');
   const bytes=Buffer.concat(parts),receipt={url,bytes:length,sha256:sha(bytes),capturedAt:new Date(clock()).toISOString(),lastModified:r.headers.get('last-modified'),etag:r.headers.get('etag'),contentEncoding:encoding,providerExpectedSHA256:null};
   // Reserve first: a crash may conservatively overcount, but cannot leave
   // retained source bytes outside the bounded cache ledger. No eviction.
   stored+=length;atomic(cache,'ledger.json',{bytes:stored});
   if(existsSync(path)){if(sha(readPrivateViewFile(path,max))!==receipt.sha256)throw Error('SOURCE_ORPHAN_MISMATCH');}else writeNew(cache,key+'.bin',bytes);writeNew(cache,key+'.json',encode(receipt));transfer+=length;replies++;return {...receipt,path,bytesValue:bytes};
  }catch(e){failure=e;if(signal?.aborted||['TRANSFER_BUDGET','SOURCE_CACHE_BUDGET','SOURCE_DISK_RESERVE','SOURCE_SIZE'].includes(e.message))break;}
  throw failure??Error('SOURCE_UNAVAILABLE');
 }};
}
export async function discoverViewNodes(project,bounds,{complete=false,zoom=14,reader,maxNodes=128,maxRecords=2000000}={}){
 const prefix=project.eptUrl.slice(0,-8),hierarchy=new Map(),queue=['0-0-0-0'],selected=[];let calls=0,records=0,finished=true;
 const mpp=2*Math.PI*6378137/(512*2**zoom),targetDepth=Math.max(0,Math.min(28,Math.ceil(Math.log2((project.octreeBoundsXYZ[3]-project.octreeBoundsXYZ[0])/(project.span*Math.max(.15,mpp))))));
 async function load(key){if(++calls>PREPARE_LIMITS.hierarchyReplies)throw Error('HIERARCHY_BUDGET');const r=await reader.get(prefix+'ept-hierarchy/'+key+'.json',4000000),h=json(r.bytesValue);if(!h||typeof h!=='object'||Array.isArray(h)||Object.keys(h).length>150000)throw Error('HIERARCHY_INVALID');for(const [k,v]of Object.entries(h)){if(!/^\d{1,2}-\d{1,10}-\d{1,10}-\d{1,10}$/.test(k)||!Number.isSafeInteger(v)||v< -1||v>2000000)throw Error('HIERARCHY_INVALID');const [d,x,y,z]=k.split('-').map(Number);if(d>30||[x,y,z].some(n=>n<0||n>=2**d))throw Error('HIERARCHY_INVALID');hierarchy.set(k,v);}if(!hierarchy.has(key)||hierarchy.get(key)<0)throw Error('HIERARCHY_INVALID');}
 await load(queue[0]);
 while(queue.length){const key=queue.shift(),[d,x,y,z]=key.split('-').map(Number);if(!intersectXY(nodeBounds(project.octreeBoundsXYZ,key),bounds))continue;let count=hierarchy.get(key);if(count===-1){await load(key);count=hierarchy.get(key);}if(count===undefined||count===0)continue;
  if(selected.length>=maxNodes||records+count>maxRecords){finished=false;break;}
  selected.push({project,key,count});records+=count;
  if(!complete&&d>=targetDepth)continue;
  for(let a=0;a<2;a++)for(let b=0;b<2;b++)for(let c=0;c<2;c++){const child=`${d+1}-${x*2+a}-${y*2+b}-${z*2+c}`;if(hierarchy.has(child)&&intersectXY(nodeBounds(project.octreeBoundsXYZ,child),bounds))queue.push(child);}
 }
 return {nodes:selected,complete:complete&&finished&&queue.length===0,displayComplete:finished&&queue.length===0,nativeRecords:records,targetDepth,hierarchyReplies:calls};
}
function runPython(python,input,signal){return new Promise((resolve,reject)=>{const child=spawn(python,[join(here,'lidar-decode.py'),input],{stdio:['ignore','pipe','pipe'],signal,env:{...process.env,PYTHONDONTWRITEBYTECODE:'1',OPENBLAS_NUM_THREADS:'1',OMP_NUM_THREADS:'1'}});let stdout='',stderr='';child.stdout.on('data',b=>{stdout+=b;if(stdout.length>16384)child.kill('SIGTERM');});child.stderr.on('data',b=>{stderr+=b;if(stderr.length>16384)child.kill('SIGTERM');});child.once('error',reject);child.once('exit',code=>code===0?resolve(stdout):reject(Object.assign(Error('NATIVE_DECODE_FAILED'),{privateDiagnostic:stderr.slice(-8192)})));});}
export async function prepareLidarView(config,input,{python=process.env.KFM_LIDAR_VIEW_PYTHON,fetcher=fetch}={}){
 if(!python||!isAbsolute(python))throw Error('LIDAR_PYTHON_NOT_CONFIGURED');const query=normalizeLidarView(input),key=lidarViewKey(query);privateViewDir(config.root);const jobs=privateViewDir(join(config.root,'jobs'),true),dir=privateViewDir(join(jobs,key),true);
 const signal=AbortSignal.timeout(PREPARE_LIMITS.jobMs),reader=createSourceReader(config.root,{fetcher,signal});let view=initialLidarView(query);const chosen=selectViewProjects(query),viewBounds=boundsMercator(query.bbox);
 let wantAnalysis=query.layers.some(k=>k==='surface'||k==='canopy')&&view.layers.some(l=>(l.kind==='surface'||l.kind==='canopy')&&l.state==='processing');
 const temp=mkdtempSync(join(dir,'.prepare-'));privateViewDir(temp);let bounds=viewBounds;
 if(wantAnalysis){const input=writeNew(temp,'bounds-input.json',encode({mode:'bounds',query})),support=JSON.parse(await runPython(python,input,signal));if(!Array.isArray(support.support3857)||support.support3857.length!==4||!support.support3857.every(v=>Number.isFinite(v)&&Math.abs(v)<1e8)||support.support3857[0]>=support.support3857[2]||support.support3857[1]>=support.support3857[3]||!Array.isArray(support.boundsUTM)||support.boundsUTM.length!==4||!support.boundsUTM.every(Number.isFinite))throw Error('ANALYSIS_BOUNDS_INVALID');
  const b=support.boundsUTM;if((b[2]-b[0])*(b[3]-b[1])>1050000){wantAnalysis=false;view.layers=view.layers.map(l=>(l.kind==='surface'||l.kind==='canopy')&&query.layers.includes(l.kind)?{...l,state:'detail-required',message:'The projected analysis rectangle exceeds the bounded cell-area budget. Zoom closer; no raster is inferred.'}:l);}else bounds=support.support3857;
 }
 let analysisProject=null,analysisComplete=false,nodes=[],failures=[],displayTruncated=chosen.length>=16;
 if(wantAnalysis&&chosen.length){
  try{const d=await discoverViewNodes(chosen[0],bounds,{complete:true,zoom:query.zoom,reader});nodes=d.nodes;analysisComplete=d.complete;displayTruncated=!d.complete;analysisProject=d.complete?chosen[0].id:null;}catch(e){failures.push(e.message);}
 }
 if((!nodes.length||!wantAnalysis)&&query.layers.includes('points')){
  let nativeCount=0;
  for(const [index,project]of chosen.entries()){
   if(nodes.length>=128||nativeCount>=2000000){displayTruncated=true;break;}
   try{const d=await discoverViewNodes(project,viewBounds,{zoom:query.zoom,reader,maxNodes:Math.max(1,Math.floor((128-nodes.length)/(chosen.length-index))),maxRecords:Math.max(1,Math.floor((2000000-nativeCount)/(chosen.length-index)))});nodes.push(...d.nodes);nativeCount+=d.nativeRecords;displayTruncated ||= !d.displayComplete;}catch(e){failures.push(e.message);}
  }
 }
 // Native files remain immutable in the private URL+hash cache. No bulk archive,
 // credentials, source paths or downloads are exposed through the website.
 const assets=[];
 for(const node of nodes){signal.throwIfAborted();try{const p=node.project,r=await reader.get(p.eptUrl.slice(0,-8)+'ept-data/'+node.key+'.laz',8000000);assets.push({path:r.path,url:r.url,sha256:r.sha256,bytes:r.bytes,pointCount:node.count,project:p.id,eptUrl:p.eptUrl,acquisition:viewAcquisition(p),verticalReference:viewVertical(p)});}catch(e){failures.push(e.message);analysisComplete=false;}}
 const job={requestKey:key,query,assets,crop3857:wantAnalysis?bounds:viewBounds,viewBounds3857:viewBounds,analysisComplete:analysisComplete&&failures.length===0,analysisProject,output:temp};
 const inputPath=writeNew(temp,'input.json',encode(job));
 await runPython(python,inputPath,signal);
 const summary=json(readPrivateViewFile(join(temp,'decode-summary.json'),900000));
 const m=summary.manifest;if(m!==null&&!validNativeViewManifest(m,key))throw Error('NATIVE_MANIFEST_INVALID');
 if(m)for(const c of m.chunks){const bytes=readPrivateViewFile(join(temp,`chunk-${c.id}.json`),900000,c.sha256);if(bytes.length!==c.bytes||!validNativeViewChunk(json(bytes),m,key,c.id))throw Error('NATIVE_CHUNK_INVALID');}
 let grid=null;if(summary.grid){grid=json(readPrivateViewFile(join(temp,'grid.json'),900000));if(!validLidarGrid(grid,key))throw Error('NATIVE_GRID_INVALID');}
 view={...view,generatedAt:summary.createdAt,points:m,grid:summary.grid,reason:failures.length?'Some fixed public source files were unavailable; current support is partial.':null};
 view.layers=view.layers.map(l=>{
  if(l.kind==='ground'||l.state==='idle'||l.state==='detail-required'||l.state==='no-coverage')return l;
  if(l.kind==='points')return {...l,state:m?(failures.length||displayTruncated?'partial':'ready'):'no-coverage',message:m?(displayTruncated?'Native display selection reached a bounded source budget; zoom in for more coverage. Survey provenance is retained.':'Native viewport returns loaded at the disclosed display LOD; per-asset survey provenance is retained.'):'No native returns were captured in this view.'};
  if(!grid)return {...l,state:'detail-required',message:'Complete source hierarchy exceeded the bounded analysis budget or was unavailable. Zoom in; no raster is inferred from display LOD.'};
  const count=summary.gridValidCells[l.kind];return {...l,state:count?(count===grid.width*grid.height?'ready':'partial'):'no-coverage',method:l.kind==='surface'?grid.method.surface:grid.method.canopy,message:count?`${count} supported same-survey cells; null cells remain unobserved.`:l.kind==='canopy'?'No supported classified-vegetation height is available here. Unclassified objects are not canopy.':'No valid first-return surface cells are supported here.'};
 });
 const requested=view.layers.filter(l=>query.layers.includes(l.kind));view.state=requested.some(l=>['ready','partial'].includes(l.state))?(requested.some(l=>l.state!=='ready')?'partial':'ready'):requested.some(l=>l.state==='detail-required')?'detail-required':failures.length?'unavailable':'no-coverage';
 if(!validLidarView(view,query))throw Error('LIDAR_VIEW_INVALID');
 const names=[...(m?['manifest.json',...m.chunks.map(c=>`chunk-${c.id}.json`)]:[]),...(grid?['grid.json']:[])];
 for(const name of names){if(existsSync(join(dir,name)))throw Error('IMMUTABLE_VIEW_EXISTS');renameSync(join(temp,name),join(dir,name));}
 const viewSha256=atomic(dir,'view.json',view),receipt={requestKey:key,viewSha256,gridSha256:grid?sha(readPrivateViewFile(join(dir,'grid.json'),900000)):null,completedAt:new Date().toISOString()};atomic(dir,'ready.json',receipt);
 atomic(dir,'processing-receipt.json',{requestKey:key,decodedNativeRecords:summary.decodedNativeRecords,viewportNativeRecords:summary.viewportNativeRecords,displayRecords:summary.displayRecords,sourceAssets:assets.length,analysisComplete:job.analysisComplete,transferBytes:reader.transferBytes,networkReplies:reader.replies,sourceAdmission:false,scientificAccuracyVerified:false});
 return {requestKey:key,state:view.state,points:m?.pointCount??0,gridValidCells:summary.gridValidCells,sourceAssets:assets.length,analysisComplete:job.analysisComplete};
}
async function main(){const config=lidarViewConfig();if(!config)throw Error('LIDAR_VIEW_NOT_CONFIGURED');privateViewDir(config.root);const queue=privateViewDir(join(config.root,'queue'),true),lock=join(config.root,'actor.lock');let fd;
 if(existsSync(lock)){const pid=Number(readPrivateViewFile(lock,64).toString());if(!Number.isSafeInteger(pid)||pid<1)throw Error('LIDAR_ACTOR_LOCK_INVALID');try{process.kill(pid,0);throw Error('LIDAR_ACTOR_ALREADY_RUNNING');}catch(e){if(e.code!=='ESRCH')throw e;unlinkSync(lock);}}
 try{fd=openSync(lock,constants.O_WRONLY|constants.O_CREAT|constants.O_EXCL|constants.O_NOFOLLOW,0o600);writeFileSync(fd,String(process.pid));}catch{throw Error('LIDAR_ACTOR_ALREADY_RUNNING');}
 const stop=new AbortController();process.once('SIGTERM',()=>stop.abort());process.once('SIGINT',()=>stop.abort());
 try{do{
  const names=readdirSync(queue).filter(n=>/^[a-f0-9]{64}\.json$/.test(n)).sort();
  for(const name of names){if(stop.signal.aborted)break;const path=join(queue,name);let job;
   try{job=json(readPrivateViewFile(path,4096));const query=normalizeLidarView(job.query);if(job.requestKey!==name.slice(0,-5)||lidarViewKey(query)!==job.requestKey)throw Error('QUEUED_QUERY_INVALID');const dir=join(config.root,'jobs',job.requestKey);if(!existsSync(join(dir,'ready.json')))console.log(JSON.stringify(await prepareLidarView(config,query)));unlinkSync(path);
   }catch(e){
    if(job&&/^[a-f0-9]{64}$/.test(job.requestKey??'')){const dir=join(config.root,'jobs',job.requestKey);privateViewDir(dir);const view=initialLidarView(job.query,'unavailable','Bounded native preparation failed. Source files and existing layers remain available; retry another view or inspect source status.');const viewSha256=atomic(dir,'view.json',view);atomic(dir,'ready.json',{requestKey:job.requestKey,viewSha256,gridSha256:null,completedAt:new Date().toISOString()});atomic(dir,'private-failure.json',{code:e.message,diagnostic:e.privateDiagnostic??null});}
    console.error(JSON.stringify({event:'lidar_preparation_failed',code:e.message}));if(existsSync(path))unlinkSync(path);
   }
  }
  if(process.argv.includes('--once'))break;
  await new Promise(resolve=>{const aborted=()=>{clearTimeout(timer);resolve();};const timer=setTimeout(()=>{stop.signal.removeEventListener('abort',aborted);resolve();},1000);stop.signal.addEventListener('abort',aborted,{once:true});});
 }while(!stop.signal.aborted);}finally{closeSync(fd);unlinkSync(lock);}}
if(import.meta.url===pathToFileURL(process.argv[1]??'').href)main().catch(e=>{console.error(JSON.stringify({event:'lidar_actor_stopped',code:e.message}));process.exitCode=1;});
