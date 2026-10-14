import {env} from "cloudflare:workers";
import {getRawDb} from "../db";
import {archiveOwner,archiveWorker} from "./daily-archive-auth";
import {SitesConnectionStore} from "./api-connection-store";
import type {ArchiveBucket} from "./daily-archive-store";
export const connectionEnvironment=()=>env as Record<string,unknown>;
export async function connectionOwner(request:Request){try{await archiveOwner(request);return true;}catch{return false;}}
export const connectionWorker=(request:Request)=>archiveWorker(request);
export function connectionSameOrigin(request:Request){return request.headers.get("origin")===new URL(request.url).origin&&request.headers.get("sec-fetch-site")!=="cross-site";}
export function connectionStore(){const bucket=env.BUCKET as ArchiveBucket|undefined;if(!bucket)throw new Error("STORAGE_NOT_CONFIGURED");return new SitesConnectionStore(getRawDb(),bucket);}
export async function connectionHostStatus(){try{return {...await connectionStore().status(),host:"Sites D1/R2"};}catch{return {host:"Sites D1/R2",configured:false,state:"storage-or-migration-required",usedBytes:null,limitBytes:80000000000,paused:true};}}
export async function requireConnectionCapture(){const state=await connectionHostStatus();if(!state.configured||state.paused)throw new Error("HOST_CAPTURE_HELD");}
