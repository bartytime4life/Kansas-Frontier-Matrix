import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,mkdir,writeFile,readFile,readdir,rm,symlink} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {inventoryPublicClientAssets,stagePublicClientAssets} from '../scripts/stage-public-client-assets.mjs';
import {gunzipSync,brotliDecompressSync} from 'node:zlib';
async function fixture(){
 const root=await mkdtemp(join(tmpdir(),'kfm-client-assets-'));
 await mkdir(join(root,'dist/client/assets'),{recursive:true});await mkdir(join(root,'public/assets'),{recursive:true});
 return {root,source:join(root,'dist/client/assets'),target:join(root,'public/assets'),close:()=>rm(root,{recursive:true,force:true})};
}
test('build compression preserves exact JS/CSS bytes and stages deterministic transport siblings',async t=>{
 const f=await fixture();t.after(f.close);
 const originals={'index-a1b2c3d4.js':'export const sample="Kansas atlas";\n'.repeat(200),'style-a1b2c3d4.css':'.atlas{color:#012345}\n'.repeat(200)};
 for(const [name,value]of Object.entries(originals))await writeFile(join(f.source,name),value);
 await writeFile(join(f.source,'small-a1b2c3d4.js'),'export{}');
 const first=await stagePublicClientAssets(f.root,{compress:true});
 assert.equal(first.files,7);assert.equal(first.compression.files,2);
 assert.ok(first.compression.brotliBytes<first.compression.originalBytes);
 assert.ok(first.compression.gzipBytes<first.compression.originalBytes);
 for(const [name,value]of Object.entries(originals)){
  const original=Buffer.from(value);
  assert.deepEqual(await readFile(join(f.source,name)),original);
  assert.deepEqual(await readFile(join(f.target,name)),original);
  for(const [suffix,decode]of [['gz',gunzipSync],['br',brotliDecompressSync]]){
   const bytes=await readFile(join(f.source,name+'.'+suffix));
   assert.deepEqual(decode(bytes),original,'transport decoding preserves source identity');
   assert.deepEqual(await readFile(join(f.target,name+'.'+suffix)),bytes);
  }
 }
 const again=await stagePublicClientAssets(f.root,{compress:true});
 assert.equal(again.added,0);assert.equal(again.retained,7);assert.deepEqual(again.compression,first.compression);
 assert.equal((await readdir(f.source)).some(name=>name.startsWith('.compress-')),false);
});
test('compression refuses conflicting siblings without overwriting them',async t=>{
 const f=await fixture();t.after(f.close);
 await writeFile(join(f.source,'index-a1b2c3d4.js'),'export const value=123;\n'.repeat(200));
 const target=join(f.source,'index-a1b2c3d4.js.br');await writeFile(target,'held bytes');
 await assert.rejects(stagePublicClientAssets(f.root,{compress:true}),/CLIENT_ASSET_COMPRESSION_CONFLICT/);
 assert.equal(await readFile(target,'utf8'),'held bytes');
});
test('stages exact hashed browser files, keeps previous versions, and reruns deterministically',async()=>{
 const f=await fixture();try{
  await writeFile(join(f.source,'index-Dzf-89L_.js'),'export const value=1;');await writeFile(join(f.source,'style-a1b2c3d4.css'),'body{}');
  await writeFile(join(f.source,'index-Dzf-89L_.js.map'),'not shipped');await writeFile(join(f.target,'older-12345678.js'),'old tab');
  assert.deepEqual(await stagePublicClientAssets(f.root),{files:2,bytes:27,added:2,retained:0});
  assert.equal(await readFile(join(f.target,'index-Dzf-89L_.js'),'utf8'),'export const value=1;');
  assert.equal(await readFile(join(f.target,'older-12345678.js'),'utf8'),'old tab');
  const repeated=await stagePublicClientAssets(f.root);assert.equal(repeated.added,0);assert.equal(repeated.retained,2);
  assert.equal((await readdir(f.target)).some(name=>name.startsWith('.stage-')||name.endsWith('.map')),false);
 }finally{await f.close();}
});
test('changed immutable destinations and symlink targets are held without overwriting them',async()=>{
 for(const symbolic of [false,true]){
  const f=await fixture();try{
   const name='index-12345678.js';await writeFile(join(f.source,name),'new');
   const outside=join(f.root,'preserved');await writeFile(outside,'old');
   if(symbolic)await symlink(outside,join(f.target,name));else await writeFile(join(f.target,name),'old');
   await assert.rejects(stagePublicClientAssets(f.root),/CLIENT_ASSET_IMMUTABLE_CONFLICT/);
   assert.equal(await readFile(outside,'utf8'),'old');assert.equal(await readFile(join(f.target,name),'utf8'),'old');
  }finally{await f.close();}
 }
});
test('refuses source symlinks, unexpected files, empty builds and destination directory symlinks',async()=>{
 for(const kind of ['source-link','unexpected','empty','destination-link']){
  const f=await fixture();try{
   const name='index-12345678.js';
   if(kind==='source-link'){await writeFile(join(f.root,'private'),'never copied');await symlink(join(f.root,'private'),join(f.source,name));}
   if(kind==='unexpected')await writeFile(join(f.source,'private.json'),'never copied');
   if(kind==='destination-link'){await writeFile(join(f.source,name),'new');await rm(f.target,{recursive:true});await symlink(f.root,f.target);}
   await assert.rejects(stagePublicClientAssets(f.root),/CLIENT_ASSET_(?:NAME_UNSAFE|BUILD_MISSING|DIRECTORY_UNSAFE)/);
   assert.equal((await readdir(f.root)).includes('index-12345678.js'),false);
  }finally{await f.close();}
 }
});
test('prebuild may skip an absent build but never an existing malformed one',async()=>{
 const f=await fixture();try{
  await rm(join(f.root,'dist'),{recursive:true});
  assert.equal((await stagePublicClientAssets(f.root,{ifBuilt:true})).skipped,true);
  await assert.rejects(stagePublicClientAssets(f.root),{code:'ENOENT'});
  await mkdir(f.source,{recursive:true});await writeFile(join(f.source,'unhashed.js'),'bad');
  await assert.rejects(stagePublicClientAssets(f.root,{ifBuilt:true}),/CLIENT_ASSET_NAME_UNSAFE/);
 }finally{await f.close();}
});
test('retained inventory identifies review candidates without touching any files',async t=>{
 const f=await fixture();t.after(f.close);
 const files={
  'older-12345678.js':'an earlier browser build',
  'older-12345678.js.br':'paired',
  'alone-12345678.css.gz':'original missing',
  'lost-12345678.js.br':'original is a symlink',
  '.stage-f3081948-ffaa-490b-88bd-edb1ddaf31af':'interrupted staging',
  'unexpected.txt':'unknown file',
 };
 for(const [name,bytes] of Object.entries(files))await writeFile(join(f.target,name),bytes);
 await symlink(join(f.target,'older-12345678.js'),join(f.target,'lost-12345678.js'));
 await mkdir(join(f.target,'unexpected-directory'));
 const expected={
  entries:8,bytes:Object.values(files).reduce((total,bytes)=>total+Buffer.byteLength(bytes),0),
  entryLimit:4096,byteLimit:256*1024*1024,
  compressionWithoutOriginal:[
   {name:'alone-12345678.css.gz',bytes:Buffer.byteLength(files['alone-12345678.css.gz'])},
   {name:'lost-12345678.js.br',bytes:Buffer.byteLength(files['lost-12345678.js.br'])},
  ],
  stagingTemporaries:[
   {name:'.stage-f3081948-ffaa-490b-88bd-edb1ddaf31af',bytes:Buffer.byteLength(files['.stage-f3081948-ffaa-490b-88bd-edb1ddaf31af'])},
  ],
  otherEntries:3,
 };
 assert.deepEqual(await inventoryPublicClientAssets(f.root),expected);
 assert.deepEqual(await inventoryPublicClientAssets(f.root),expected);
 assert.deepEqual(await readdir(f.source),[]);
 assert.deepEqual((await readdir(f.target)).sort(),[...Object.keys(files),'lost-12345678.js','unexpected-directory'].sort());
 for(const [name,bytes] of Object.entries(files))assert.equal(await readFile(join(f.target,name),'utf8'),bytes);
});
test('retained inventory treats missing output as empty and rejects a symlink directory',async t=>{
 const f=await fixture();t.after(f.close);
 await rm(f.target,{recursive:true});
 assert.deepEqual(await inventoryPublicClientAssets(f.root),{
  entries:0,bytes:0,entryLimit:4096,byteLimit:256*1024*1024,
  compressionWithoutOriginal:[],stagingTemporaries:[],otherEntries:0,
 });
 assert.deepEqual(await readdir(join(f.root,'public')),[]);
 await symlink(f.source,f.target);
 await assert.rejects(inventoryPublicClientAssets(f.root),/CLIENT_ASSET_DIRECTORY_UNSAFE/);
});
