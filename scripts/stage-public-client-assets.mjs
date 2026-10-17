// GoDaddy serves public/assets from durable storage. Stage only the same
// immutable browser files already emitted for dist/client/assets; never prune.
import {lstat,mkdir,readdir,readFile,writeFile,link,unlink} from 'node:fs/promises';
import {createHash,randomUUID} from 'node:crypto';
import {resolve,join} from 'node:path';
import {pathToFileURL} from 'node:url';
const fail=code=>{throw new Error(code);};
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
const allowed=/^[A-Za-z0-9][A-Za-z0-9_.-]{0,180}-[A-Za-z0-9_-]{8,}\.(?:js|css|woff2?|ttf|svg|png|jpe?g|webp|avif|wasm)(?:\.(?:br|gz|zst))?$/;
async function directory(path){const info=await lstat(path);if(!info.isDirectory()||info.isSymbolicLink())fail('CLIENT_ASSET_DIRECTORY_UNSAFE');}
export async function stagePublicClientAssets(root=process.cwd(),{ifBuilt=false}={}){
 root=resolve(root);
 try{for(const part of ['dist','dist/client','dist/client/assets'])await directory(join(root,part));}
 catch(error){if(ifBuilt&&error.code==='ENOENT')return {files:0,bytes:0,added:0,retained:0,skipped:true};throw error;}
 await directory(join(root,'public'));
 const source=join(root,'dist/client/assets'),destination=join(root,'public/assets');
 await mkdir(destination,{recursive:true});await directory(destination);
 const entries=await readdir(source,{withFileTypes:true});
 if(entries.length>4096)fail('CLIENT_ASSET_COUNT_LIMIT');
 const items=[];let totalBytes=0;
 for(const entry of entries){
  if(entry.name.endsWith('.map'))continue;
  if(!entry.isFile()||!allowed.test(entry.name))fail('CLIENT_ASSET_NAME_UNSAFE');
  const info=await lstat(join(source,entry.name));
  if(!info.isFile()||info.isSymbolicLink()||info.size>64*1024*1024)fail('CLIENT_ASSET_FILE_UNSAFE');
  totalBytes+=info.size;if(totalBytes>256*1024*1024)fail('CLIENT_ASSET_BYTE_LIMIT');
  items.push({name:entry.name,size:info.size});
 }
 if(!items.length)fail('CLIENT_ASSET_BUILD_MISSING');
 let added=0,retained=0;
 for(const item of items){
  const bytes=await readFile(join(source,item.name));
  if(bytes.length!==item.size)fail('CLIENT_ASSET_SOURCE_CHANGED');
  const target=join(destination,item.name);
  const verify=async()=>{
   const info=await lstat(target);
   if(!info.isFile()||info.isSymbolicLink()||info.size!==bytes.length||hash(await readFile(target))!==hash(bytes))fail('CLIENT_ASSET_IMMUTABLE_CONFLICT');
  };
  try{await lstat(target);await verify();retained++;continue;}catch(error){if(error.code!=='ENOENT')throw error;}
  const temporary=join(destination,'.stage-'+randomUUID());
  try{
   await writeFile(temporary,bytes,{flag:'wx',mode:0o644});
   // Atomic, no-clobber publication within one filesystem; readers never see
   // partially copied JavaScript. A concurrent identical writer is harmless.
   try{await link(temporary,target);added++;}catch(error){if(error.code!=='EEXIST')throw error;await verify();retained++;}
  }finally{await unlink(temporary).catch(()=>{});}
 }
 return {files:items.length,bytes:totalBytes,added,retained};
}
if(process.argv[1]&&import.meta.url===pathToFileURL(resolve(process.argv[1])).href){
 const result=await stagePublicClientAssets(process.cwd(),{ifBuilt:process.argv.includes('--if-built')});console.info('KFM public client assets staged '+JSON.stringify(result));
}
