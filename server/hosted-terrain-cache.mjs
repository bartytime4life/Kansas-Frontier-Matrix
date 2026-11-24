// Public prepared terrain only. Raw sources, credentials and worker jobs stay on dev.
// GoDaddy documents public/assets as persistent across Node app deployments.
import {constants} from 'node:fs';
import {mkdir,lstat,open,readdir,rename,unlink,rmdir,statfs,realpath} from 'node:fs/promises';
import {resolve,join,parse} from 'node:path';
import {createHash,createHmac,randomBytes,timingSafeEqual} from 'node:crypto';
import {gzip,gunzip} from 'node:zlib';
import {promisify} from 'node:util';
const zip=promisify(gzip),unzip=promisify(gunzip);
export const HOSTED_TERRAIN_LIMITS=Object.freeze({bytes:1024**3,entries:2048,entryBytes:1_004_096,reserveBytes:512*1024**2,freshMs:24*3600000,staleMs:7*24*3600000});
const format='kfm-hosted-terrain-cache-v1',keyPattern=/^(?:ground|view|grid):[a-f0-9]{64}$/;
const exact=(v,keys)=>v&&typeof v==='object'&&!Array.isArray(v)&&Object.keys(v).sort().join(',')===keys.split(',').sort().join(',');
const digest=b=>createHash('sha256').update(b).digest('hex');
const terminal=value=>value&&['ready','partial','no-coverage','detail-required'].includes(value.state)||value&&value.format==='kfm-lidar-grid-v1';

// Directory ancestry is checked on every operation; opening the leaf refuses symlinks.
// This expendable cache never follows a visitor path or removes original/source files.
async function safeDirectory(root,create){
 let cursor=parse(root).root;
 for(const part of root.slice(cursor.length).split('/').filter(Boolean)){
  cursor=join(cursor,part);let st;
  try{st=await lstat(cursor);}catch(e){if(e.code!=='ENOENT'||!create)throw e;try{await mkdir(cursor,{mode:0o755});}catch(x){if(x.code!=='EEXIST')throw x;}st=await lstat(cursor);}
  if(!st.isDirectory()||st.isSymbolicLink())throw Error('TERRAIN_CACHE_PATH');
 }
 if(await realpath(root)!==root)throw Error('TERRAIN_CACHE_PATH');
 return root;
}
export function createHostedTerrainCache({root=resolve('public/assets/kfm-terrain-cache-v1'),secret,origin,clock=Date.now,limits={}}={}){
 const budget={...HOSTED_TERRAIN_LIMITS,...limits},directory=resolve(root);
 if(!secret||typeof origin!=='string')throw Error('TERRAIN_CACHE_CONFIG');
 const sign=(key,at,payload,binding)=>createHmac('sha256',secret).update(JSON.stringify([format,origin,key,at,payload,binding])).digest('hex');
 const file=key=>join(directory,digest(origin+'\n'+key)+'.json.gz');
 const read=async(key,validate,binding='')=>{
  try{
   if(!keyPattern.test(key)||typeof validate!=='function')return null;
   await safeDirectory(directory,false);const handle=await open(file(key),constants.O_RDONLY|constants.O_NOFOLLOW);
   let packed;try{const s=await handle.stat();if(!s.isFile()||s.size<1||s.size>budget.entryBytes)return null;packed=await handle.readFile();}finally{await handle.close();}
   if(packed.length>budget.entryBytes)return null;
   const raw=await unzip(packed,{maxOutputLength:budget.entryBytes}),record=JSON.parse(raw.toString('utf8'));
   if(!exact(record,'format,key,at,payload,binding,mac')||record.format!==format||record.key!==key||record.binding!==binding||!Number.isSafeInteger(record.at)||record.at>clock()+60000||clock()-record.at>=budget.staleMs||typeof record.payload!=='string'||typeof record.mac!=='string'||!/^[a-f0-9]{64}$/.test(record.mac))return null;
   const mac=Buffer.from(sign(key,record.at,record.payload,binding),'hex');if(!timingSafeEqual(mac,Buffer.from(record.mac,'hex')))return null;
   const value=JSON.parse(record.payload);if(!terminal(value)||!validate(value))return null;
   return {value,at:record.at,bytes:Buffer.byteLength(record.payload)};
  }catch{return null;}
 };
 const writeNow=async(key,value,at=clock(),binding='')=>{
  let lock=false,tmp=null;
  try{
   if(!keyPattern.test(key)||!/^([a-f0-9]{64})?$/.test(binding)||!terminal(value)||!Number.isSafeInteger(at)||at>clock()+60000)return false;
   const payload=JSON.stringify(value),record={format,key,at,payload,binding,mac:sign(key,at,payload,binding)},raw=Buffer.from(JSON.stringify(record));if(raw.length>budget.entryBytes)return false;
   const packed=await zip(raw,{level:6});if(packed.length>budget.entryBytes)return false;
   await safeDirectory(directory,true);
   // Exclusive directory lock bounds writes across app processes. A crashed writer's
   // lock older than one minute may be removed only if it is an empty real directory.
   const lockPath=join(directory,'.writer-lock');
   try{await mkdir(lockPath,{mode:0o700});lock=true;}catch(e){
    if(e.code!=='EEXIST')return false;
    const s=await lstat(lockPath);if(!s.isDirectory()||s.isSymbolicLink()||clock()-s.mtimeMs<60000)return false;
    try{await rmdir(lockPath);await mkdir(lockPath,{mode:0o700});lock=true;}catch{return false;}
   }
   const names=await readdir(directory),entries=names.filter(n=>/^[a-f0-9]{64}\.json\.gz$/.test(n));
   let used=0;for(const name of entries){const s=await lstat(join(directory,name));if(!s.isFile()||s.isSymbolicLink())return false;used+=s.size;}
   if(entries.length>=budget.entries&&!entries.includes(file(key).slice(directory.length+1))||used+packed.length>budget.bytes)return false;
   const fs=await statfs(directory);if(fs.bavail*fs.bsize<budget.reserveBytes+packed.length)return false;
   await safeDirectory(directory,false);tmp=join(directory,'.tmp-'+randomBytes(12).toString('hex'));
   const handle=await open(tmp,constants.O_WRONLY|constants.O_CREAT|constants.O_EXCL|constants.O_NOFOLLOW,0o644);try{await handle.writeFile(packed);await handle.sync();}finally{await handle.close();}
   // Same-directory atomic replacement, only a hash-named expendable cache copy.
   await rename(tmp,file(key));tmp=null;return true;
  }catch{return false;}
  finally{if(tmp)await unlink(tmp).catch(()=>{});if(lock)await rmdir(join(directory,'.writer-lock')).catch(()=>{});}
 };
 let tail=Promise.resolve(),waiting=0;
 const write=(...args)=>{
  if(waiting>=16)return Promise.resolve(false);waiting++;const job=tail.then(()=>writeNow(...args));tail=job.catch(()=>false);return job.finally(()=>waiting--);
 };
 return Object.freeze({read,write,root:directory,limits:budget});
}
