import {readFile,mkdir,lstat,chmod,open,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {join,dirname} from 'node:path';
const fail=code=>{throw Object.assign(new Error(code),{code});};
const safeHost = host => host === 'huggingface.co' || host.endsWith('.huggingface.co') || host.endsWith('.hf.co');

async function providerDownload(url, signal) {
  for (let count = 0; count < 6; count++) {
    const target = new URL(url);
    if (target.protocol !== 'https:' || target.username || target.password || target.port || !safeHost(target.hostname)) fail('MODEL_DOWNLOAD_DESTINATION');
    const response = await fetch(target, { redirect: 'manual', signal });
    if ([301, 302, 303, 307, 308].includes(response.status)) {
      const location = response.headers.get('location'); await response.body?.cancel();
      if (!location) fail('MODEL_DOWNLOAD_REDIRECT');
      url = new URL(location, target).href; continue;
    }
    if (!response.ok || !response.body) fail('MODEL_DOWNLOAD_UNAVAILABLE');
    return response;
  }
  fail('MODEL_DOWNLOAD_REDIRECT_LIMIT');
}

async function privateDirectory(path) {
  await mkdir(path, { mode: 0o700, recursive: true });
  const info = await lstat(path);
  if (!info.isDirectory() || info.isSymbolicLink() || info.uid !== process.getuid()) fail('MODEL_DIRECTORY_UNSAFE');
  await chmod(path, 0o700);
}

export async function installModel(directory, manifest) {
  if (manifest.id !== 'onnx-community/Qwen3-0.6B-ONNX' || manifest.revision !== '58ca03a5e7b354b480b1a82b34bde8dc7b854cc0' || manifest.license !== 'apache-2.0') fail('MODEL_MANIFEST_INVALID');
  const allowed = new Set(['README.md', 'config.json', 'generation_config.json', 'onnx/model_int8.onnx', 'tokenizer.json', 'tokenizer_config.json']);
  if (!Array.isArray(manifest.files) || manifest.files.length !== allowed.size || new Set(manifest.files.map(x => x.path)).size !== allowed.size) fail('MODEL_MANIFEST_INVALID');
  for (const entry of manifest.files) {
    if (!allowed.has(entry.path) || !Number.isSafeInteger(entry.size) || entry.size <= 0 || entry.size > 650000000 || !/^[a-f0-9]{64}$/.test(entry.sha256)) fail('MODEL_MANIFEST_INVALID');
  }
  const modelDirectory = join(directory, 'model');
  await privateDirectory(modelDirectory); await privateDirectory(join(modelDirectory, 'onnx'));
  const files = [];
  for (const entry of manifest.files) {
    const signal = AbortSignal.timeout(120000);
    const response = await providerDownload(`https://huggingface.co/${manifest.id}/resolve/${manifest.revision}/${entry.path}`, signal);
    const file = await open(join(modelDirectory, entry.path), 'wx', 0o600);
    const hash = createHash('sha256'), reader = response.body.getReader(); let bytes = 0;
    try {
      while (true) {
        const { done, value } = await reader.read(); if (done) break;
        bytes += value.length; if (bytes > entry.size) fail('MODEL_FILE_SIZE_MISMATCH');
        hash.update(value); await file.writeFile(value);
      }
      await file.sync();
      if (bytes !== entry.size || hash.digest('hex') !== entry.sha256) fail('MODEL_FILE_INTEGRITY_MISMATCH');
      files.push({ path: entry.path, size: bytes, sha256: entry.sha256 });
    } finally { await reader.cancel().catch(() => {}); reader.releaseLock(); await file.close(); }
  }
  await writeFile(join(directory, 'verified-model.json'), JSON.stringify({ ...manifest, files }, null, 2) + '\n', { flag: 'wx', mode: 0o600 });
  return modelDirectory;
}

// Only the fixed application model is prepared. No user URL/path reaches this API.
// Existing/partial attempts are retained for inspection; no automatic overwrite.
export async function ensureHostedModel(directory) {
 try { const info=await lstat(directory);if(!info.isDirectory()||info.isSymbolicLink())fail('MODEL_DIRECTORY_UNSAFE');return; }
 catch(error){if(error.code!=='ENOENT')throw error;}
 const parent=dirname(directory),root=await lstat(dirname(parent));
 if(!root.isDirectory()||root.isSymbolicLink())fail('MODEL_DIRECTORY_UNSAFE');
 await mkdir(parent,{mode:0o700});
 const attempt=await open(join(parent,'.attempt'),'wx',0o600);await attempt.close();
 const manifest=JSON.parse(await readFile(new URL('./embedded-ai-model.json',import.meta.url),'utf8'));
 await installModel(parent,manifest);
}
