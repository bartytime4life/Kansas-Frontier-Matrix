import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,mkdir,readFile,symlink,rm,writeFile} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {ensureHostedModel,installModel,checkHostedManifest,HOSTED_MODEL_FILES} from '../server/hosted-ai-artifacts.mjs';
test('Qwen identity and manifest paths are checked before download',async()=>{
 const real=JSON.parse(await readFile(new URL('../server/embedded-ai-model.json',import.meta.url),'utf8'));
 for(const change of [{id:'untrusted/model'},{revision:'main'},{license:'unknown'},{files:[...real.files,{path:'../accounts-jobs.sqlite',size:1,sha256:'0'.repeat(64)}]}])
  await assert.rejects(installModel('/does-not-exist',{...real,...change}),/MODEL_MANIFEST_INVALID/);
});
test('existing model directory is retained without overwriting files',async()=>{
 const root=await mkdtemp(join(tmpdir(),'kfm-qwen-artifacts-'));
 try {const dir=join(root,'model');await mkdir(dir,{mode:0o700});await writeFile(join(dir,'retained'),'original');await ensureHostedModel(dir);assert.equal(await readFile(join(dir,'retained'),'utf8'),'original');}
 finally{await rm(root,{recursive:true,force:true});}
});
test('symlinked model directory and interrupted attempt are not reused or erased',async()=>{
 const root=await mkdtemp(join(tmpdir(),'kfm-qwen-artifacts-'));
 try{const parent=join(root,'attempt');await mkdir(parent,{mode:0o700});await writeFile(join(parent,'.attempt'),'retained');await assert.rejects(ensureHostedModel(join(parent,'model')),/EEXIST/);assert.equal(await readFile(join(parent,'.attempt'),'utf8'),'retained');await symlink(parent,join(root,'link'));await assert.rejects(ensureHostedModel(join(root,'link')),/MODEL_DIRECTORY_UNSAFE/);}
 finally{await rm(root,{recursive:true,force:true});}
});
test('derived model manifest pins its weights file and upstream lineage',async()=>{
 const real=JSON.parse(await readFile(new URL('../server/embedded-ai-model.json',import.meta.url),'utf8'));
 checkHostedManifest(real);
 assert.deepEqual(real.files.map(f=>f.path).sort(),[...HOSTED_MODEL_FILES].sort());
 assert.deepEqual(real.derivedFrom,{id:'onnx-community/Qwen3-0.6B-ONNX',revision:'58ca03a5e7b354b480b1a82b34bde8dc7b854cc0',path:'onnx/model_int8.onnx',sha256:'d93222c672992a398eeea3a4a1ca025738efd9a18ba5f1691419ff8ae23a8e75',transform:'scripts/derive-hosted-qwen.py',outputSlices:8});
 assert.throws(()=>checkHostedManifest({...real,files:real.files.filter(f=>f.path!=='onnx/model_int8.onnx_data')}),/MODEL_MANIFEST_INVALID/);
});
