import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,mkdir,writeFile,readFile,readdir,rm,symlink} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {stagePublicClientAssets} from '../scripts/stage-public-client-assets.mjs';
async function fixture(){
 const root=await mkdtemp(join(tmpdir(),'kfm-client-assets-'));
 await mkdir(join(root,'dist/client/assets'),{recursive:true});await mkdir(join(root,'public/assets'),{recursive:true});
 return {root,source:join(root,'dist/client/assets'),target:join(root,'public/assets'),close:()=>rm(root,{recursive:true,force:true})};
}
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
