import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,mkdir,readFile,symlink,rm,writeFile} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {ensureHostedModel,installModel} from '../server/hosted-ai-artifacts.mjs';
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
