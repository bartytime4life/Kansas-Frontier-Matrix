// A small, versioned public Ground overview, captured through the verified relay.
// The exact source/retrieval dates and coarse output spacing are retained.
import {constants} from 'node:fs';import {open} from 'node:fs/promises';import {resolve} from 'node:path';import {createHash} from 'node:crypto';
import {validGroundView} from '../scripts/local-data/ground-model.mjs';
export const GROUND_BASELINE=Object.freeze({key:'09c050e21cf4dd304ebd00ffc570deb56719ec33510f493ed4c37860f8cacbc2',sha256:'6bfde1777a0895321d62b6e02d6ae8d801601b39ad27cf6d04c78cf3a4f7cf88',bytes:195650,query:Object.freeze({bbox:Object.freeze([-102.2,36.8,-94.4,40.2]),size:96})});
export async function readGroundBaseline(key,{root=process.cwd()}={}){
 if(key!=='ground:'+GROUND_BASELINE.key)return null;let handle;
 try{handle=await open(resolve(root,'public/data/terrain/kansas-ground-overview-v1.json'),constants.O_RDONLY|constants.O_NOFOLLOW);const stat=await handle.stat();if(!stat.isFile()||stat.size!==GROUND_BASELINE.bytes)return null;const bytes=await handle.readFile();if(bytes.length!==GROUND_BASELINE.bytes||createHash('sha256').update(bytes).digest('hex')!==GROUND_BASELINE.sha256)return null;const value=JSON.parse(bytes);if(!validGroundView(value,GROUND_BASELINE.query))return null;return {value,bytes:bytes.length,at:Date.parse(value.generatedAt),tier:'baseline'};}catch{return null;}finally{if(handle)await handle.close();}
}
