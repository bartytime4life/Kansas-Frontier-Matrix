import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,mkdir,readFile,symlink,rm,writeFile,stat,link,readdir,chmod} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join,dirname} from 'node:path';
import {createHash} from 'node:crypto';
import {verifyInstalledModel,checkHostedManifest,HOSTED_MODEL_FILES} from '../server/hosted-ai-artifacts.mjs';
import {HOSTED_MODEL_DIRECTORY} from '../server/hosted-ai.mjs';
const real=JSON.parse(await readFile(new URL('../server/embedded-ai-model.json',import.meta.url),'utf8'));

// A small stand-in model: the real file set, tiny contents, matching manifest.
async function install({mode=0o644}={}){
 const root=await mkdtemp(join(tmpdir(),'kfm-qwen-artifacts-')),dir=join(root,'cache','model');
 await mkdir(join(dir,'onnx'),{recursive:true,mode:0o755});await chmod(join(root,'cache'),0o755);await chmod(dir,0o755);await chmod(join(dir,'onnx'),0o755);
 const files=[];
 for(const path of HOSTED_MODEL_FILES){const bytes=Buffer.from('synthetic '+path);await writeFile(join(dir,path),bytes,{mode});files.push({path,size:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex')});}
 return {root,dir,manifest:{...real,files}};
}
test('manifest identity and paths are checked before any file is read',async()=>{
 for(const change of [{id:'untrusted/model'},{installation:'download'},{license:'unknown'},{files:[...real.files,{path:'../accounts-jobs.sqlite',size:1,sha256:'0'.repeat(64)}]}])
  await assert.rejects(verifyInstalledModel('/does-not-exist',{...real,...change}),/HOSTED_MODEL_IDENTITY/);
});
test('derived model manifest pins its weights file, install path and upstream lineage',()=>{
 checkHostedManifest(real);
 assert.deepEqual(real.files.map(f=>f.path).sort(),[...HOSTED_MODEL_FILES].sort());
 assert.equal(real.installPath,HOSTED_MODEL_DIRECTORY);
 assert.deepEqual(real.derivedFrom,{id:'onnx-community/Qwen3-0.6B-ONNX',revision:'58ca03a5e7b354b480b1a82b34bde8dc7b854cc0',path:'onnx/model_int8.onnx',sha256:'d93222c672992a398eeea3a4a1ca025738efd9a18ba5f1691419ff8ae23a8e75',transform:'scripts/derive-hosted-qwen.py',outputSlices:8});
 assert.throws(()=>checkHostedManifest({...real,files:real.files.filter(f=>f.path!=='onnx/model_int8.onnx_data')}),/MODEL_MANIFEST_INVALID/);
});
test('a missing upload is reported without creating anything',async()=>{
 const root=await mkdtemp(join(tmpdir(),'kfm-qwen-artifacts-'));
 try{await assert.rejects(verifyInstalledModel(join(root,'cache','model'),real),/HOSTED_MODEL_NOT_INSTALLED/);assert.deepEqual(await readdir(root),[]);}
 finally{await rm(root,{recursive:true,force:true});}
});
test('an uploaded model is verified and tightened to owner-only permissions',async()=>{
 const {root,dir,manifest}=await install();
 try{
  assert.equal(await verifyInstalledModel(dir,manifest),dir);
  for(const path of [dirname(dir),dir,join(dir,'onnx')])assert.equal((await stat(path)).mode&0o777,0o700);
  for(const path of HOSTED_MODEL_FILES)assert.equal((await stat(join(dir,path))).mode&0o777,0o600);
 }finally{await rm(root,{recursive:true,force:true});}
});
test('changed bytes, missing files, links and hard links are refused',async()=>{
 const {root,dir,manifest}=await install();
 try{
  await writeFile(join(dir,'config.json'),'synthetic config.jsoX');
  await assert.rejects(verifyInstalledModel(dir,manifest),/HOSTED_MODEL_INTEGRITY/);
  await rm(join(dir,'config.json'));
  await assert.rejects(verifyInstalledModel(dir,manifest),/HOSTED_MODEL_NOT_INSTALLED/);
  await symlink(join(dir,'README.md'),join(dir,'config.json'));
  await assert.rejects(verifyInstalledModel(dir,manifest),/HOSTED_MODEL_FILES_UNSAFE/);
  await rm(join(dir,'config.json'));await link(join(dir,'README.md'),join(dir,'config.json'));
  await assert.rejects(verifyInstalledModel(dir,manifest),/HOSTED_MODEL_FILES_UNSAFE/);
  await symlink(dir,join(root,'linked'));
  await assert.rejects(verifyInstalledModel(join(root,'linked'),manifest),/HOSTED_MODEL_FILES_UNSAFE/);
 }finally{await rm(root,{recursive:true,force:true});}
});
