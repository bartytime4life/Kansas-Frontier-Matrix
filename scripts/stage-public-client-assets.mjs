// GoDaddy serves public/assets from durable storage. Stage only the same
// immutable browser files already emitted for dist/client/assets; never prune.
import {lstat,mkdir,readdir,readFile,writeFile,link,unlink} from 'node:fs/promises';
import {createHash,randomUUID} from 'node:crypto';
import {resolve,join} from 'node:path';
import {pathToFileURL} from 'node:url';
import {gzip,brotliCompress,constants} from 'node:zlib';
import {promisify} from 'node:util';
const gzipBytes=promisify(gzip),brotliBytes=promisify(brotliCompress);
const fail=code=>{throw new Error(code);};
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
const allowed=/^[A-Za-z0-9][A-Za-z0-9_.-]{0,180}-[A-Za-z0-9_-]{8,}\.(?:js|css|woff2?|ttf|svg|png|jpe?g|webp|avif|wasm)(?:\.(?:br|gz|zst))?$/;
async function directory(path){const info=await lstat(path);if(!info.isDirectory()||info.isSymbolicLink())fail('CLIENT_ASSET_DIRECTORY_UNSAFE');}
export async function stagePublicClientAssets(root=process.cwd(),{ifBuilt=false,compress=false}={}){
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
 // The pinned runtime negotiates precompressed siblings, but the build does
 // not emit them. Generate only immutable JS/CSS variants, never source data,
 // HTML, APIs, media or reflected/private responses. Originals stay exact.
 const compression={files:0,originalBytes:0,brotliBytes:0,gzipBytes:0};
 if(compress){
  const byName=new Map(items.map(item=>[item.name,item]));
  for(const item of [...items]){
   if(!/\.(?:js|css)$/.test(item.name)||item.size<1024)continue;
   const bytes=await readFile(join(source,item.name));
   if(bytes.length!==item.size)fail('CLIENT_ASSET_SOURCE_CHANGED');
   item.digest=hash(bytes);
   compression.files++;compression.originalBytes+=bytes.length;
   for(const [suffix,variant] of [
    ['br',await brotliBytes(bytes,{params:{[constants.BROTLI_PARAM_QUALITY]:5,[constants.BROTLI_PARAM_MODE]:constants.BROTLI_MODE_TEXT}})],
    ['gz',await gzipBytes(bytes,{level:6})],
   ]){
    if(variant.length>=bytes.length)continue;
    const name=item.name+'.'+suffix,target=join(source,name),temporary=join(source,'.compress-'+randomUUID());
    const verify=async()=>{
     const info=await lstat(target);
     if(!info.isFile()||info.isSymbolicLink()||info.size!==variant.length||hash(await readFile(target))!==hash(variant))fail('CLIENT_ASSET_COMPRESSION_CONFLICT');
    };
    try{
     await writeFile(temporary,variant,{flag:'wx',mode:0o644});
     try{await link(temporary,target);}catch(error){if(error.code!=='EEXIST')throw error;await verify();}
    }finally{await unlink(temporary).catch(()=>{});}
    if(!byName.has(name)){const added={name,size:variant.length};byName.set(name,added);items.push(added);totalBytes+=variant.length;}
    byName.get(name).digest=hash(variant);
    if(totalBytes>256*1024*1024)fail('CLIENT_ASSET_BYTE_LIMIT');
    if(items.length>4096)fail('CLIENT_ASSET_COUNT_LIMIT');
    compression[suffix==='br'?'brotliBytes':'gzipBytes']+=variant.length;
   }
  }
 }
 let added=0,retained=0;
 for(const item of items){
  const bytes=await readFile(join(source,item.name));
  if(bytes.length!==item.size||item.digest&&hash(bytes)!==item.digest)fail('CLIENT_ASSET_SOURCE_CHANGED');
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
 return {files:items.length,bytes:totalBytes,added,retained,...(compress?{compression}:{})};
}
if(process.argv[1]&&import.meta.url===pathToFileURL(resolve(process.argv[1])).href){
 const result=await stagePublicClientAssets(process.cwd(),{ifBuilt:process.argv.includes('--if-built'),compress:process.argv.includes('--compress')});console.info('KFM public client assets staged '+JSON.stringify(result));
}
