import { createHmac, timingSafeEqual, randomBytes } from 'node:crypto';
import { ORIGIN, fail, sha } from './pipeline-contract.mjs';

const message = (method, path, time, nonce, body) => ['KFM-PIPELINE-V1', method, path, time, nonce, sha(body)].join('\n');
export function signRequest({ secret, method, path, body = '', now = Date.now(), nonce = randomBytes(18).toString('base64url') }) {
  if (!/^[a-f0-9]{64}$/.test(secret ?? '')) fail('PIPELINE_KEY_INVALID');
  const time = String(now); const signature = createHmac('sha256', Buffer.from(secret, 'hex')).update(message(method, path, time, nonce, body)).digest('hex');
  return { 'x-kfm-pipeline-time': time, 'x-kfm-pipeline-nonce': nonce, 'x-kfm-pipeline-signature': signature };
}
export async function authorize(request, body, store, environment = process.env, now = Date.now()) {
  const url = new URL(request.url);
  if (environment.KFM_PIPELINE_ENABLED !== 'true' || environment.KFM_RUNTIME_ROLE !== 'published') fail('PIPELINE_DISABLED', 404);
  const secret = environment.KFM_PIPELINE_WORKER_SECRET;
  if (url.origin !== ORIGIN || request.headers.has('origin') || request.headers.has('sec-fetch-site') || !/^[a-f0-9]{64}$/.test(secret ?? '')) fail('PIPELINE_AUTH_REQUIRED', 401);
  const time = request.headers.get('x-kfm-pipeline-time'), nonce = request.headers.get('x-kfm-pipeline-nonce'), signature = request.headers.get('x-kfm-pipeline-signature');
  if (!/^\d{13}$/.test(time ?? '') || Math.abs(now - Number(time)) > 60000 || !/^[A-Za-z0-9_-]{24}$/.test(nonce ?? '') || !/^[a-f0-9]{64}$/.test(signature ?? '')) fail('PIPELINE_AUTH_REQUIRED', 401);
  const expected = signRequest({ secret, method: request.method, path: url.pathname + url.search, body, now: Number(time), nonce })['x-kfm-pipeline-signature'];
  if (!timingSafeEqual(Buffer.from(expected, 'hex'), Buffer.from(signature, 'hex'))) fail('PIPELINE_AUTH_REQUIRED', 401);
  // Persist replay claims across process restarts and replicas.
  if (!await store.claimNonce(sha(nonce), now)) fail('PIPELINE_AUTH_REQUIRED', 401);
}
