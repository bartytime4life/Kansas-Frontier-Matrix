import { createPublicKey, verify } from 'node:crypto';
import { ArtifactFiles } from './pipeline-files.mjs';
import { authorize } from './pipeline-auth.mjs';
import { MAX_PACKAGE, CHUNK_SIZE, ORIGIN, boundedBody, parse, canonical, sha, fail, source, digest, timestamp, verifyProfile, recipeDigest, PipelineError } from './pipeline-contract.mjs';
import { validateContext } from './pipeline-normalize.mjs';

const headers = { 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff', 'Referrer-Policy': 'no-referrer' };
const reply = (value, status = 200) => Response.json(value, { status, headers });
function approval(r, env, now) {
  if (!env.KFM_PIPELINE_APPROVER_PUBLIC_KEY) fail('APPROVAL_KEY_REQUIRED');
  if ((env.KFM_PIPELINE_REVOKED_PROFILES ?? '').split(',').includes(r.approval?.profile?.id)) fail('APPROVAL_REVOKED', 403);
  return verifyProfile(r.approval, env.KFM_PIPELINE_APPROVER_PUBLIC_KEY, { now, recipe: r.recipeSha256, sourceId: r.sourceId });
}
function manifest(value) {
  if (!value || value.format !== 'kfm-pc-release-transfer-v1' || Object.keys(value).sort().join(',') !== ['approval','byteLength','expectedActive','format','payloadSha256','recipeSha256','sourceId'].sort().join(',')) fail('MANIFEST_INVALID', 400);
  source(value.sourceId); digest(value.payloadSha256); digest(value.recipeSha256);
  if (!Number.isInteger(value.byteLength) || value.byteLength < 1 || value.byteLength > MAX_PACKAGE || !(value.expectedActive === null || /^[a-f0-9]{64}$/.test(value.expectedActive))) fail('MANIFEST_INVALID', 400);
  return value;
}
async function assembled(files, id, m) {
  const chunks = []; let length = 0;
  for (let i = 0; i < Math.ceil(m.byteLength / CHUNK_SIZE); i++) {
    const chunk = await files.get(id, i, CHUNK_SIZE);
    if (chunk.length !== Math.min(CHUNK_SIZE, m.byteLength - length)) fail('ARTIFACT_INCOMPLETE');
    length += chunk.length; chunks.push(chunk);
  }
  const bytes = Buffer.concat(chunks);
  if (length !== m.byteLength || sha(bytes) !== m.payloadSha256) fail('ARTIFACT_INTEGRITY_FAILED');
  return bytes;
}
/** @param {Request} request @param {{store: any, environment?: any, files?: any, validateGoverned?: any, now?: number}} options */
export async function handlePipeline(request, { store, environment = process.env, files, validateGoverned, now = Date.now() }) {
  const began = Date.now();
  try {
    const url = new URL(request.url);
    if (url.origin !== ORIGIN || environment.KFM_PIPELINE_ENABLED !== 'true' || environment.KFM_RUNTIME_ROLE !== 'published') fail('PIPELINE_DISABLED', 404);
    const action = url.pathname.slice('/api/pipeline/v1/'.length);
    if (!['heartbeat','stage','chunk','release','commit','control'].includes(action) || request.method !== 'POST' || url.search) fail('ROUTE_NOT_FOUND', 404);
    const bytes = await boundedBody(request, action === 'chunk' ? CHUNK_SIZE * 2 : 64 * 1024);
    const body = parse(bytes, CHUNK_SIZE * 2);
    if (action === 'control') {
      if (request.headers.has('origin') || request.headers.has('sec-fetch-site')) fail('OWNER_AUTH_REQUIRED', 401);
      const { command, signature } = body;
      const key = createPublicKey(environment.KFM_PIPELINE_APPROVER_PUBLIC_KEY ?? '');
      if (key.asymmetricKeyType !== 'ed25519' || command?.format !== 'kfm-pipeline-control-v1' || command.origin !== ORIGIN
        || !/^[a-f0-9]{32}$/.test(command.nonce ?? '') || Math.abs(timestamp(command.at) - now) > 60000
        || !verify(null, Buffer.from(canonical(command)), key, Buffer.from(signature ?? '', 'base64url'))
        || !await store.claimNonce(sha(command.nonce), now)) fail('OWNER_AUTH_REQUIRED', 401);
      if (['pause','resume'].includes(command.action)) {
        await store.pool.execute('UPDATE kfm_pipeline_control SET paused=? WHERE id=1', [command.action === 'pause']);
        return reply({ state: command.action === 'pause' ? 'paused' : 'scheduled' });
      }
      if (command.action === 'withdraw') return reply(await store.withdraw(digest(command.releaseId), command.expectedActive, now));
      if (command.action === 'rollback') {
        const r = await store.release(digest(command.releaseId));
        if (!r?.projection || r.state !== 'COMMITTED') fail('ROLLBACK_TARGET_UNAVAILABLE');
        approval(r.manifest, environment, now);
        if (sha(canonical(r.projection)) !== r.manifest.payloadSha256) fail('PROJECTION_INTEGRITY_FAILED');
        if (['water','weather'].includes(r.sourceId)) {
          if (!validateGoverned) fail('GOVERNED_VALIDATOR_REQUIRED');
          await validateGoverned(r.sourceId, r.projection, now);
        } else validateContext(r.projection);
        return reply(await store.rollback(r.id, digest(command.expectedActive), sha(canonical(command)), now));
      }
      fail('CONTROL_INVALID', 400);
    }
    await authorize(request, bytes, store, environment, now);
    if (action === 'heartbeat') {
      if (!['idle','running','held','error'].includes(body.state)) fail('HEARTBEAT_INVALID', 400);
      return reply(await store.heartbeat(body.state, now));
    }
    if (action === 'release') {
      if (body.releaseId) {
        const r = await store.release(digest(body.releaseId));
        if (!r) fail('RELEASE_NOT_FOUND', 404);
        const head = await store.active(r.sourceId);
        return reply({ releaseId: r.id, state: r.state, active: head?.id === r.id, payloadSha256: r.manifest.payloadSha256 });
      }
      const active = await store.active(source(body.sourceId));
      return reply({ releaseId: active?.id ?? null, state: active?.state ?? 'NONE' });
    }
    files ??= new ArtifactFiles(environment.KFM_PIPELINE_ARTIFACT_ROOT ?? '/private/kfm-pipeline/artifacts');
    await files.health();
    if (action === 'stage') {
      const m = manifest(body); approval(m, environment, now);
      await files.health(m.byteLength);
      if (m.recipeSha256 !== await recipeDigest()) fail('RECIPE_CHANGED');
      const id = sha(canonical(m)); const r = await store.stage(id, m, now);
      return reply({ releaseId: id, state: r.state });
    }
    const id = digest(body.releaseId); const r = await store.release(id);
    if (!r || r.state === 'WITHDRAWN') fail('RELEASE_NOT_STAGED');
    approval(r.manifest, environment, now);
    if (r.manifest.recipeSha256 !== await recipeDigest()) fail('RECIPE_CHANGED');
    if (action === 'chunk') {
      if ((await store.ready()).paused) fail('PIPELINE_PAUSED');
      if (r.state !== 'STAGED') fail('RELEASE_ALREADY_COMMITTED');
      const index = body.index;
      if (!Number.isInteger(index) || index < 0 || index >= Math.ceil(r.manifest.byteLength / CHUNK_SIZE)
        || typeof body.data !== 'string' || !/^[A-Za-z0-9+/]+={0,2}$/.test(body.data)) fail('CHUNK_INVALID', 400);
      const chunk = Buffer.from(body.data, 'base64');
      if (chunk.toString('base64') !== body.data || chunk.length !== Math.min(CHUNK_SIZE, r.manifest.byteLength - index * CHUNK_SIZE)) fail('CHUNK_INVALID', 400);
      await files.put(id, index, chunk);
      return reply({ releaseId: id, index, sha256: sha(chunk) });
    }
    if (action === 'commit') {
      if (r.state === 'COMMITTED') return reply(await store.commit(id, r.manifest.expectedActive, null, now));
      const payload = await assembled(files, id, r.manifest); const product = parse(payload);
      if (canonical(product) !== payload.toString()) fail('CANONICAL_PAYLOAD_REQUIRED');
      const committedAt = now + (Date.now() - began);
      approval(r.manifest, environment, committedAt);
      if (['water','weather'].includes(r.sourceId)) {
        if (!validateGoverned) fail('GOVERNED_VALIDATOR_REQUIRED');
        await validateGoverned(r.sourceId, product, committedAt);
      } else {
        validateContext(product);
        if (product.sourceId !== r.sourceId || timestamp(product.retrievedAt) > committedAt + 60000 || committedAt - timestamp(product.retrievedAt) > 7200_000) fail('CAPTURE_TIME_INVALID');
        const previous = await store.active(r.sourceId);
        if (previous?.projection?.retrievedAt && timestamp(product.retrievedAt) < timestamp(previous.projection.retrievedAt)) fail('OLDER_CAPTURE_HELD');
      }
      return reply(await store.commit(id, r.manifest.expectedActive, product, committedAt));
    }
    fail('ROUTE_NOT_FOUND', 404);
  } catch (e) { return reply({ error: e instanceof PipelineError ? e.message : 'PIPELINE_UNAVAILABLE' }, e instanceof PipelineError ? e.status : 503); }
}
/** @param {string} sourceId @param {{store: any, environment?: any, now?: number}} options @param {string|null} [releaseId] */
export async function publicContext(sourceId, { store, environment = process.env, now = Date.now() }, releaseId = null) {
  source(sourceId);
  if (!['usgs-streamflow','nws-alerts','usgs-earthquakes'].includes(sourceId)) fail('SOURCE_NOT_ALLOWED', 400);
  const r = releaseId ? await store.release(digest(releaseId)) : await store.active(sourceId);
  if (!r || r.state !== 'COMMITTED' || r.sourceId !== sourceId || !r.projection) return { state: 'withheld', reason: 'NO_APPROVED_RELEASE', sourceId };
  approval(r.manifest, environment, now);
  if (sha(canonical(r.projection)) !== r.manifest.payloadSha256) fail('PROJECTION_INTEGRITY_FAILED');
  const p = validateContext(r.projection);
  const features = p.data.features.map(f => sourceId === 'nws-alerts' ? { ...f, properties: { ...f.properties, expired: timestamp(f.properties.expires) <= now } } : f);
  const measured = sourceId === 'usgs-streamflow' ? features.filter(f => f.properties.value !== null).map(f => now - timestamp(f.properties.observedAt) <= 7200000) : [];
  return { ...p, data: { ...p.data, features }, releaseId: r.id, state: p.partial ? 'partial' : features.length ? 'available' : 'empty',
    approvalExpiresAt: r.manifest.approval.profile.expiresAt, payloadSha256: r.manifest.payloadSha256,
    measurementFreshness: !measured.length ? 'unknown' : measured.every(Boolean) ? 'current' : measured.some(Boolean) ? 'mixed' : 'stale',
    freshness: now - timestamp(p.retrievedAt) > 7200000 ? 'stale' : 'current' };
}
export async function publicArtifact(sourceId, options, releaseId) {
  // Check the same current rights/revocation/withdrawal gates as the rendered read.
  await publicContext(sourceId, options, releaseId);
  const r = await options.store.release(digest(releaseId));
  if (!r || r.state !== 'COMMITTED' || r.sourceId !== sourceId) fail('RELEASE_WITHHELD', 404);
  approval(r.manifest, options.environment ?? process.env, options.now ?? Date.now());
  const bytes = Buffer.from(canonical(r.projection));
  if (sha(bytes) !== r.manifest.payloadSha256) fail('PROJECTION_INTEGRITY_FAILED');
  return bytes;
}
export async function publicHistory(sourceId, { store, environment = process.env, now = Date.now() }) {
  source(sourceId); const items = [];
  for (const r of await store.history(sourceId)) {
    try { approval(r.manifest, environment, now); items.push({ releaseId: r.releaseId, publishedAt: new Date(r.publishedAt).toISOString() }); }
    catch { /* Expired/revoked profiles cannot advertise downloadable history. */ }
  }
  return { sourceId, items, limit: 20 };
}
