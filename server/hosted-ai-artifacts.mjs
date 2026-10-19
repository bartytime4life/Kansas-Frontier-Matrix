import {lstat,chmod} from 'node:fs/promises';
import {createReadStream} from 'node:fs';
import {createHash} from 'node:crypto';
import {join,dirname} from 'node:path';
const fail=code=>{throw Object.assign(new Error(code),{code});};

// The derived model (scripts/derive-hosted-qwen.py) keeps weights in external data
// and evaluates the tied output layer in vocabulary slices to bound memory.
// The operator uploads it to the model directory by hand; the app never downloads it.
export const HOSTED_MODEL_SOURCE = Object.freeze({ id: 'kfm-qwen3-0.6b-int8-sliced-onnx-20261019', installation: 'manual-upload' });
export const HOSTED_MODEL_FILES = Object.freeze(['README.md', 'config.json', 'generation_config.json', 'onnx/model_int8.onnx', 'onnx/model_int8.onnx_data', 'tokenizer.json', 'tokenizer_config.json']);
export function checkHostedManifest(manifest, code = 'MODEL_MANIFEST_INVALID') {
  if (manifest?.id !== HOSTED_MODEL_SOURCE.id || manifest.installation !== HOSTED_MODEL_SOURCE.installation || manifest.license !== 'apache-2.0') fail(code);
  const allowed = new Set(HOSTED_MODEL_FILES);
  if (!Array.isArray(manifest.files) || manifest.files.length !== allowed.size || new Set(manifest.files.map(x => x?.path)).size !== allowed.size) fail(code);
  for (const entry of manifest.files) {
    if (!allowed.has(entry.path) || !Number.isSafeInteger(entry.size) || entry.size <= 0 || entry.size > 800000000 || !/^[a-f0-9]{64}$/.test(entry.sha256)) fail(code);
  }
}

// File Manager uploads arrive group/world-readable. Files this process owns are
// tightened to owner-only; links and files owned by anyone else are refused.
async function ownedPath(path,directory){
  const info=await lstat(path);
  if(info.isSymbolicLink()||info.uid!==process.getuid()||(directory?!info.isDirectory():!info.isFile()||info.nlink!==1))fail('HOSTED_MODEL_FILES_UNSAFE');
  if(info.mode&0o077)await chmod(path,directory?0o700:0o600);
  return info;
}

// Only the fixed application model is accepted. No user URL/path reaches this API.
// Every listed file is size- and SHA-256-checked before the runtime reads it.
export async function verifyInstalledModel(directory, manifest) {
  checkHostedManifest(manifest, 'HOSTED_MODEL_IDENTITY');
  try { await lstat(directory); }
  catch (error) { if (error.code === 'ENOENT') fail('HOSTED_MODEL_NOT_INSTALLED'); throw error; }
  for (const path of [dirname(directory), directory, join(directory, 'onnx')]) await ownedPath(path, true);
  for (const entry of manifest.files) {
    const path = join(directory, entry.path);
    let info;
    try { info = await ownedPath(path, false); }
    catch (error) { if (error.code === 'ENOENT') fail('HOSTED_MODEL_NOT_INSTALLED'); throw error; }
    if (info.size !== entry.size) fail('HOSTED_MODEL_INTEGRITY');
    const hash = createHash('sha256'); for await (const chunk of createReadStream(path)) hash.update(chunk);
    if (hash.digest('hex') !== entry.sha256) fail('HOSTED_MODEL_INTEGRITY');
  }
  return directory;
}
