import { ORIGIN, CHUNK_SIZE, canonical, sha, parse, fail } from '../../server/pipeline-contract.mjs';
import { signRequest } from '../../server/pipeline-auth.mjs';

export async function pipelineCall(action, value, secret, { fetcher = fetch } = {}) {
  const body = canonical(value), path = '/api/pipeline/v1/' + action;
  const response = await fetcher(ORIGIN + path, { method: 'POST', redirect: 'manual', signal: AbortSignal.timeout(30000),
    headers: { 'Content-Type': 'application/json', ...signRequest({ secret, method: 'POST', path, body }) }, body });
  const limit = 65536; const reader = response.body?.getReader(); let n = 0; const chunks = [];
  if (reader) try { while (true) { const { value: chunk, done } = await reader.read(); if (done) break; n += chunk.length; if (n > limit) { await reader.cancel(); fail('REMOTE_RESPONSE_LIMIT'); } chunks.push(chunk); } } finally { reader.releaseLock(); }
  const result = parse(Buffer.concat(chunks), limit);
  if (!response.ok) fail(typeof result.error === 'string' && /^[A-Z_]{1,64}$/.test(result.error) ? result.error : 'REMOTE_UNAVAILABLE');
  return result;
}
export async function publish(manifest, payload, secret, options = {}) {
  if (sha(payload) !== manifest.payloadSha256 || payload.length !== manifest.byteLength) fail('LOCAL_ARTIFACT_CHANGED');
  const id = sha(canonical(manifest));
  const staged = await pipelineCall('stage', manifest, secret, options);
  if (staged.releaseId !== id) fail('REMOTE_IDENTITY_MISMATCH');
  if (staged.state !== 'COMMITTED') {
    for (let i = 0; i < Math.ceil(payload.length / CHUNK_SIZE); i++) {
      const chunk = payload.subarray(i * CHUNK_SIZE, (i + 1) * CHUNK_SIZE);
      const readback = await pipelineCall('chunk', { releaseId: id, index: i, data: chunk.toString('base64') }, secret, options);
      if (readback.releaseId !== id || readback.index !== i || readback.sha256 !== sha(chunk)) fail('REMOTE_INTEGRITY_MISMATCH');
    }
  }
  await pipelineCall('commit', { releaseId: id }, secret, options);
  const receipt = await pipelineCall('release', { releaseId: id }, secret, options);
  if (receipt.state !== 'COMMITTED' || receipt.releaseId !== id || receipt.payloadSha256 !== sha(payload)) fail('REMOTE_COMMIT_UNCONFIRMED');
  return receipt;
}
