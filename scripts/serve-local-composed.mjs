#!/usr/bin/env node
/** One loopback Explorer: current Node UI plus the preserved native data runtime. */
import { createRequire } from 'node:module';
import { mkdtempSync, readFileSync, rmSync, realpathSync, lstatSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { resolve, join } from 'node:path';
import { pathToFileURL, fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import { startProdServer, nodeToWebRequest, sendWebResponse } from 'vinext/server/prod-server';

export function nativeApiPath(pathname) {
  // Only this reviewed stateless display adapter moves to the current Node build.
  if (pathname === '/api/hydrology/flowlines') return false;
  return pathname.startsWith('/api/') && !/^\/api\/(?:pc-ai|owner|ingestion|source-operations|source-pipeline|pc-storage-probe|reports|capture-worker)(?:\/|$)/.test(pathname);
}
export function acceptedLocalRequest(request, origin) {
  return new URL(request.url).origin === origin && ![...request.headers.keys()].some(name=>name.startsWith('oai-authenticated-'));
}
export function apiOnlyEntry(entry) {
  const needle='return worker.fetch(request, env, ctx);';
  if(!entry.includes(needle)) throw new Error('NATIVE_ENTRY_DRIFT');
  return entry.replace(needle,'if (!new URL(request.url).pathname.startsWith("/api/")) return new Response("Not found", { status: 404 });\n  '+needle);
}
export async function createNativeApi(root, state, port, reviewedImagery=false) {
  root=resolve(root);state=resolve(state);
  if(realpathSync(root)!==root || realpathSync(state)!==state || lstatSync(root).uid!==process.getuid() || lstatSync(root).mode&0o002) throw new Error('LOCAL_INPUT_SYMLINK');
  const identity=JSON.parse(readFileSync(join(root,'local-input-identity.json'),'utf8'));
  if(identity.sourceCommit!=='358280aee889e2e2cf832bd598155ca21653c8de'||identity.siteVersion!==268) throw new Error('NATIVE_SOURCE_IDENTITY');
  if(createHash('sha256').update(JSON.stringify(Object.fromEntries(Object.entries(identity.files).sort(([a],[b])=>a<b?-1:a>b?1:0)))).digest('hex')!=='4d93130fefbdcfe53f6e8cb067c64f1154e84ea6da41095e7229633f496caf91') throw new Error('NATIVE_INVENTORY_DRIFT');
  for(const [name,digest] of Object.entries(identity.files)) {
    if(!name || name.startsWith('/') || name.split('/').includes('..')) throw new Error('NATIVE_INPUT_PATH');
    const target=join(root,name); if(realpathSync(target)!==target || createHash('sha256').update(readFileSync(target)).digest('hex')!==digest) throw new Error('NATIVE_INPUT_DIGEST');
  }
  const {validateSubsurfacePublic}=await import(pathToFileURL(join(root,'scripts/validate-subsurface-public.mjs')).href);
  if(validateSubsurfacePublic(join(root,'dist/client')).length) throw new Error('SUBSURFACE_PUBLICATION_HELD');
  const helpers=await import(pathToFileURL(join(root,'scripts/serve-local-worker.mjs')).href);
  const server=join(root,'dist/server'),client=join(root,'dist/client');
  for(const dir of [root,state,join(state,'v3/d1'),join(state,'v3/r2'),client]) helpers.checkedPath(dir,true);
  const configPath=join(server,'wrangler.json');
  helpers.validateConfiguration(JSON.parse(readFileSync(configPath)),JSON.parse(readFileSync(join(root,'.openai/hosting.json'))));
  const require=createRequire(join(root,'package.json')),runtimeRequire=createRequire(require.resolve('wrangler'));
  if(require('wrangler/package.json').version!=='4.127.1'||runtimeRequire('miniflare/package.json').version!=='5.20260828.0-alpha')throw new Error('LOCAL_RUNTIME_VERSION');
  process.env.WRANGLER_WRITE_LOGS='false';
  const {unstable_getMiniflareWorkerOptions}=require('wrangler');
  const {Miniflare,convertV4MiniflareOptions,Log,LogLevel}=runtimeRequire('miniflare');
  const worker=helpers.prepareWorker(unstable_getMiniflareWorkerOptions(configPath),server,client,helpers.collectModules(server),reviewedImagery,port);
  worker.modules[0].contents=apiOnlyEntry(worker.modules[0].contents);
  const key=helpers.readUsgsApiKey();if(key)worker.bindings.USGS_WATER_API_KEY=key;
  const {readArchiveAccess}=await import(pathToFileURL(join(root,'scripts/archive-access.mjs')).href);
  const archive=readArchiveAccess();if(archive){worker.bindings.KFM_ARCHIVE_LOCAL_OWNER_TOKEN=archive.ownerToken;worker.bindings.KFM_ARCHIVE_WORKER_TOKEN=archive.workerToken;}
  const temp=mkdtempSync(join(tmpdir(),'kfm-composed-api-'));
  const signals=['SIGINT','SIGTERM','SIGHUP'],before=new Map(signals.map(s=>[s,new Set(process.listeners(s))]));
  let runtime;
  try {
    runtime=new Miniflare(convertV4MiniflareOptions({host:'127.0.0.1',port:0,log:new Log(LogLevel.WARN),workers:[worker],resourcePersistencePath:join(state,'v3'),resourceTmpPath:temp}));
    for(const signal of signals)for(const listener of process.listeners(signal))if(!before.get(signal).has(listener))process.removeListener(signal,listener);
    await runtime.ready;
    return {fetch:request=>runtime.dispatchFetch(request.url,{method:request.method,headers:Object.fromEntries(request.headers),...(request.body?{body:request.body,duplex:"half"}:{})}),stop:async()=>{await runtime.dispose();rmSync(temp,{recursive:true,force:true});},identity};
  } catch(error){await runtime?.dispose();rmSync(temp,{recursive:true,force:true});throw error;}
}
export async function serveComposed({nativeRoot,state,port=4173,reviewedImagery=false}) {
  if(!Number.isInteger(port)||port<1024||port>65535||reviewedImagery&&port!==4173)throw new Error('LOCAL_PORT_INVALID');
  const origin=`http://127.0.0.1:${port}`;
  const api=await createNativeApi(nativeRoot,state,port,reviewedImagery);
  process.env.KFM_LOCAL_COMPOSED="1";
  let server;
  try {
    ({server}=await startProdServer({port,host:'127.0.0.1',outDir:resolve('dist')}));
    const listeners=server.listeners('request');if(listeners.length!==1)throw new Error('NODE_HANDLER_DRIFT');
    const handler=listeners[0];server.removeListener('request',handler);let active=0;
    server.on('request',async(req,res)=>{
      if(req.headers.host!==`127.0.0.1:${port}`||Object.keys(req.headers).some(n=>n.startsWith('oai-authenticated-'))){res.writeHead(403,{'Cache-Control':'no-store'});res.end('Local request authority rejected.');return;}
      const url=new URL(req.url,origin);
      if(!nativeApiPath(url.pathname)){handler.call(server,req,res);return;}
      if(active>=32){res.writeHead(503,{'Cache-Control':'no-store','Retry-After':'1'});res.end('Local data runtime busy.');return;}
      active++;
      try {await sendWebResponse(await api.fetch(nodeToWebRequest(req,url.href)),req,res,false);}
      catch{if(!res.headersSent){res.writeHead(503,{'Cache-Control':'no-store'});res.end('Local data runtime unavailable.');}else res.destroy();}
      finally{active--;}
    });
    let stopping;
    const stop=()=>stopping??=(async()=>{await new Promise(r=>{server.close(r);server.closeIdleConnections();});await api.stop();})();
    for(const signal of ['SIGINT','SIGTERM','SIGHUP'])process.once(signal,()=>{stop().then(()=>process.exit(0),()=>process.exit(1));});
    console.log(JSON.stringify({event:'local_composed_ready',origin,nativeSiteVersion:api.identity.siteVersion,nativeSource:api.identity.sourceCommit,existingState:true,authentication:'UNCHANGED',secondaryMapSites:0}));
    return {server,api,stop};
  }catch(error){server?.close();await api.stop();throw error;}
}
if(process.argv[1]&&realpathSync(process.argv[1])===fileURLToPath(import.meta.url)) {
  const args=process.argv.slice(2),options={};
  for(let i=0;i<args.length;i++){if(args[i]==='--native-api-root')options.nativeRoot=args[++i];else if(args[i]==='--state')options.state=args[++i];else if(args[i]==='--port')options.port=Number(args[++i]);else if(args[i]==='--local-reviewed-imagery')options.reviewedImagery=true;else throw new Error('LOCAL_ARGUMENT_INVALID');}
  serveComposed(options).catch(error=>{console.error(JSON.stringify({event:'local_composed_failed',reason:/^[A-Z_]+$/.test(error.message)?error.message:'STARTUP_FAILED'}));process.exitCode=1;});
}
