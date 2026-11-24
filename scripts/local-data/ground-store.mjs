import {existsSync,readdirSync,writeFileSync,renameSync} from 'node:fs';
import {isAbsolute,join} from 'node:path';
import {randomBytes,createHash} from 'node:crypto';
import {privateViewDir,readPrivateViewFile} from './lidar-view.mjs';
import {normalizeGroundQuery,groundKey,validGroundView} from './ground-model.mjs';
export const groundConfig=(env=process.env)=>typeof env.KFM_GROUND_VIEW_ROOT==='string'&&isAbsolute(env.KFM_GROUND_VIEW_ROOT)?{root:env.KFM_GROUND_VIEW_ROOT}:null;
export const groundSHA=b=>'sha256:'+createHash('sha256').update(b).digest('hex');
export function groundAtomic(dir,name,value){privateViewDir(dir);const bytes=Buffer.from(JSON.stringify(value)+'\n'),tmp=join(dir,'.'+name+'-'+randomBytes(8).toString('hex'));writeFileSync(tmp,bytes,{mode:0o600,flag:'wx'});if(groundSHA(readPrivateViewFile(tmp,2_000_000))!==groundSHA(bytes))throw Error('GROUND_WRITE_READBACK');renameSync(tmp,join(dir,name));return groundSHA(bytes);}
export function initialGround(input,state='processing',reason=null){const query=normalizeGroundQuery(input);return {format:'kfm-ground-view-v1',requestKey:groundKey(query),query,generatedAt:new Date().toISOString(),state,reason,grid:null};}
export function requestGround(config,input){
 if(!config)throw Error('GROUND_NOT_CONFIGURED');const query=normalizeGroundQuery(input),key=groundKey(query);privateViewDir(config.root);
 const jobs=privateViewDir(join(config.root,'jobs'),true),dir=join(jobs,key),initial=()=>initialGround(query),unavailable=reason=>initialGround(query,'unavailable',reason);
 if(!existsSync(dir)&&readdirSync(jobs).length>=2048)return unavailable('The bounded Ground view store is full; existing files remain available.');privateViewDir(dir,true);
 if(existsSync(join(dir,'ready.json'))){const r=JSON.parse(readPrivateViewFile(join(dir,'ready.json'),4096));if(r.requestKey!==key||!/^sha256:[a-f0-9]{64}$/.test(r.sha256??''))throw Error('GROUND_NOT_READY');const v=JSON.parse(readPrivateViewFile(join(dir,'view.json'),900000,r.sha256));if(!validGroundView(v,query))throw Error('GROUND_NOT_READY');
  const age=Date.now()-Date.parse(r.completedAt),attempts=readdirSync(jobs).filter(n=>n.startsWith('.failed-'+key+'-')).length;
  if(v.state!=='unavailable'||!Number.isFinite(age)||age<60000||attempts>=2||readdirSync(jobs).length>=2048)return v;
  try{renameSync(dir,join(jobs,'.failed-'+key+'-'+Date.now()+'-'+randomBytes(4).toString('hex')));privateViewDir(dir,true);}catch(e){if(e.code!=='ENOENT')throw e;return initial();}
 }
 const queue=privateViewDir(join(config.root,'queue'),true),path=join(queue,key+'.json');if(readdirSync(queue).length>=16&&!existsSync(path))return unavailable('The Ground preparation queue is busy. Retry this view shortly.');
 try{writeFileSync(path,JSON.stringify({requestKey:key,query,requestedAt:new Date().toISOString()})+'\n',{mode:0o600,flag:'wx'});}catch(e){if(e.code!=='EEXIST')throw e;}
 return initial();
}
