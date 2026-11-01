#!/usr/bin/env node
// KFM local-data worker: the same outbound-only relay loop as the home-inference worker, carrying
// only the local-data gateway's routes. It long-polls the website for signed requests, relays each
// unchanged to the loopback gateway (127.0.0.1:8788 by default) and posts the signed reply back.
// It holds no gateway key, so it cannot create, alter or replay a request or a reply.
//
//   KFM_WORKER_SITE=https://... KFM_WORKER_KEY_FILE=... node worker.mjs [--check]
import {pathToFileURL} from 'node:url';
import {createWorker,loadWorkerConfig} from '../home-inference/worker.mjs';
import {LOCAL_DATA_ROUTES,LOCAL_DATA_WORKER,LOCAL_DATA_LIMITS} from './protocol.mjs';

export const LOCAL_DATA_WORKER_LIMITS=Object.freeze({leaseMs:30000,siteMs:15000,relayMs:LOCAL_DATA_LIMITS.gatewayMs,statusEveryMs:5000,
 leaseBytes:65536,replyBytes:LOCAL_DATA_LIMITS.replyBytes,backoffMinMs:1000,backoffMaxMs:60000});
export const LOCAL_DATA_WORKER_PREFIX='/api/local-data-worker/v1';

export function createLocalDataWorker(config,overrides={}){
 return createWorker({...config,routes:LOCAL_DATA_ROUTES,sitePrefix:LOCAL_DATA_WORKER_PREFIX,version:LOCAL_DATA_WORKER,limits:LOCAL_DATA_WORKER_LIMITS,...overrides});
}

async function main(argv){
 let config;
 try{config=loadWorkerConfig({...process.env,KFM_WORKER_GATEWAY:process.env.KFM_WORKER_GATEWAY||'http://127.0.0.1:8788'});}
 catch(error){console.error(JSON.stringify({event:'config_refused',code:error.code??'CONFIG_INVALID'}));return 1;}
 const worker=createLocalDataWorker(config);
 if(argv[0]==='--check'){
  try{const outcome=await worker.once();console.log(JSON.stringify({event:'check',result:outcome==='idle'?'SITE_ACCEPTS_WORKER_KEY':'RELAYED_ONE_JOB'}));return 0;}
  catch(error){console.error(JSON.stringify({event:'check',result:'FAILED',code:error?.code??'SITE_UNREACHABLE'}));return 1;}
 }
 const controller=new AbortController();
 process.once('SIGTERM',()=>controller.abort());process.once('SIGINT',()=>controller.abort());
 await worker.run(controller.signal);
 return 0;
}

if(import.meta.url===pathToFileURL(process.argv[1]??'').href)main(process.argv.slice(2)).then(code=>{process.exitCode=code;});
