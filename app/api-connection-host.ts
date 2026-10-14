import {getIngestionStore} from "../server/ingestion-store.mjs";
import {authenticateOwner,sameOrigin,workerAuthorized} from "../server/owner-auth.mjs";
import {ingestionConfig} from "../server/ingestion-config.mjs";
export const connectionEnvironment=()=>process.env;
export const connectionOwner=(request:Request)=>authenticateOwner(request);
export const connectionWorker=(request:Request)=>workerAuthorized(request);
export const connectionSameOrigin=(request:Request)=>sameOrigin(request);
export const connectionStore=()=>getIngestionStore();
export async function connectionHostStatus(){const c=ingestionConfig();const missing=[...(!c.database?["database"]:[]),...(!c.tls?["verified database TLS"]:[]),...(!c.authentication?["owner sign-in"]:[]),...(!c.proxy?["trusted public hostname"]:[]),...(!c.capacityConfirmed?["80 GB provider capacity"]:[]),...(!c.enabled?["capture enablement"]:[]),...(!c.production?["published worker role"]:[])];try{if(!c.database||!c.tls)throw new Error();const s=await (await getIngestionStore()).status();return {...s,host:"GoDaddy MySQL",configured:c.ready,state:c.ready?(s.paused?"paused":"ready-for-owner-capture"):"configuration-required",missing};}catch{return {host:"GoDaddy MySQL",configured:false,state:"storage-or-migration-required",usedBytes:null,limitBytes:80000000000,paused:true,missing};}}
export async function requireConnectionCapture(){const status=await connectionHostStatus();if(!status.configured||status.paused)throw new Error("HOST_CAPTURE_HELD");}
