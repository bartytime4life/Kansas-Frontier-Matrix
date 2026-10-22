#!/usr/bin/env node
import { generateKeyPairSync, createPublicKey, sign, randomBytes } from 'node:crypto';
import { lstat, statfs, readdir } from 'node:fs/promises';
import { resolve, dirname, relative } from 'node:path';
import { fileURLToPath } from 'node:url';
import { captureRequest, fetchCapture } from '../../server/ingestion-sources.mjs';
import { normalizeCapture } from '../../server/pipeline-normalize.mjs';
import { canonical, sha, parse, recipeDigest, verifyProfile, fail, MAX_PACKAGE, ORIGIN } from '../../server/pipeline-contract.mjs';
import { directory, immutable, readRegular, hashFile, storageGuard } from '../../server/pipeline-files.mjs';
import { Journal } from './journal.mjs';
import { loadConfig, tick } from './worker.mjs';
import { pipelineCall, publish } from './publisher.mjs';

const checkout = resolve(fileURLToPath(new URL('../..', import.meta.url)));
const bytes = value => Buffer.from(canonical(value));
async function rootPath(value) {
  if (!value?.startsWith('/')) fail('ABSOLUTE_ROOT_REQUIRED');
  const path = resolve(value);
  if (path === '/' || path === checkout || path.startsWith(checkout + '/') || checkout.startsWith(path + '/')) fail('DATA_ROOT_MUST_BE_OUTSIDE_CHECKOUT');
  await directory(path, true);
  if ((await lstat(path)).mode & 0o077) fail('PRIVATE_ROOT_REQUIRED');
  return path;
}
async function walk(path, prefix = '') {
  const results = [];
  for (const entry of await readdir(path, { withFileTypes: true })) {
    if (entry.isSymbolicLink()) fail('BACKUP_SYMLINK_REJECTED');
    const name = prefix + entry.name; const full = resolve(path, entry.name);
    if (entry.isDirectory()) results.push(...await walk(full, name + '/'));
    else if (entry.isFile()) results.push({ path: name, ...await hashFile(full) });
    else fail('BACKUP_SPECIAL_FILE_REJECTED');
    if (results.length > 1000000) fail('INVENTORY_FILE_LIMIT');
  }
  return results;
}
export async function cli(argv) {
  const [command, ...args] = argv;
  if (command === 'inventory') {
    const fs = await statfs('/');
    return { format: 'kfm-pipeline-inventory-v1', node: process.versions.node, systemFreeBytes: fs.bavail * fs.bsize,
      recipeSha256: await recipeDigest(), mountIdentityRequired: true, configured: false, productionChanged: false };
  }
  if (command === 'keys') {
    const root = await rootPath(args[0]);
    const pair = generateKeyPairSync('ed25519');
    await immutable(resolve(root, 'approver-private.pem'), Buffer.from(pair.privateKey.export({ format: 'pem', type: 'pkcs8' })));
    await immutable(resolve(root, 'approver-public.pem'), Buffer.from(pair.publicKey.export({ format: 'pem', type: 'spki' })));
    return { state: 'created', privateKeyRemainsLocal: true, note: 'Run on the original PC; install only the public key on GoDaddy and the worker.' };
  }
  if (command === 'profile-template') {
    if (!['usgs-streamflow','nws-alerts','water','weather'].includes(args[0])) fail('SOURCE_NOT_ALLOWED');
    return { format: 'kfm-pc-release-delegation-v1', id: 'owner-selected-profile-id', sourceId: args[0], recipeSha256: await recipeDigest(), approver: '',
      validFrom: new Date().toISOString(), expiresAt: new Date(Date.now() + 7 * 86400000).toISOString(),
      rights: 'REVIEW_REQUIRED', sensitivity: 'REVIEW_REQUIRED', sourceRef: '', rightsRef: '', reviewRef: '', releaseProfileRef: '',
      maxBytes: MAX_PACKAGE, maxRows: 1000, staleAfterSeconds: 7200, role: ['water','weather'].includes(args[0]) ? 'governed-package' : 'external-context' };
  }
  if (command === 'approve') {
    const p = parse(await readRegular(resolve(args[0]), 16384)); const privateKey = await readRegular(resolve(args[1]), 8192);
    const signed = { profile: p, signature: sign(null, bytes(p), privateKey).toString('base64url') };
    verifyProfile(signed, createPublicKey(privateKey).export({ format: 'pem', type: 'spki' }), { sourceId: p.sourceId, recipe: await recipeDigest() });
    await immutable(resolve(args[2]), bytes(signed)); return { state: 'approved', profileId: p.id, expiresAt: p.expiresAt };
  }
  if (command === 'control') {
    const input = parse(await readRegular(resolve(args[0]), 8192)); const key = await readRegular(resolve(args[1]), 8192);
    const cmd = { ...input, format: 'kfm-pipeline-control-v1', origin: ORIGIN, at: new Date().toISOString(), nonce: randomBytes(16).toString('hex') };
    const body = { command: cmd, signature: sign(null, bytes(cmd), key).toString('base64url') };
    const response = await fetch(ORIGIN + '/api/pipeline/v1/control', { method: 'POST', redirect: 'manual', signal: AbortSignal.timeout(30000), headers: { 'Content-Type': 'application/json' }, body: canonical(body) });
    const result = parse(await response.text(), 16384); if (!response.ok) fail('OWNER_CONTROL_UNCONFIRMED'); return result;
  }
  if (command === 'rehearse') {
    const root = await rootPath(args[0]); const results = [];
    // Bounded manual acquisition on the system disk; never enables a schedule or publication.
    const fs = await statfs(root); if (fs.bavail * fs.bsize < 30 * 1024 ** 3 + 64 * 1024 ** 2) fail('DISK_RESERVE_REQUIRED');
    for (const id of ['usgs-streamflow','nws-alerts']) {
      try {
        const request = captureRequest(id); const capture = await fetchCapture(request, { apiKey: process.env.USGS_WATER_API_KEY });
        const raw = resolve(root, 'data/quarantine', id, 'objects/sha256', sha(capture.bytes), 'payload');
        await immutable(raw, capture.bytes);
        await immutable(resolve(root, 'data/receipts/ingest/pc-pipeline', sha(bytes(capture.receipt)) + '.json'), bytes(capture.receipt));
        const product = normalizeCapture(request, capture);
        const path = resolve(root, 'data/processed', id, sha(product.bytes) + '.json'); await immutable(path, product.bytes);
        results.push({ sourceId: id, state: 'candidate-only', bytes: capture.bytes.length, features: product.product.data.features.length, productPath: relative(root, path) });
      } catch (e) { results.push({ sourceId: id, state: 'held', reason: /^[A-Z_]{1,64}$/.test(e.message) ? e.message : 'ACQUISITION_FAILED' }); }
    }
    return { state: 'private-rehearsal', published: false, results };
  }
  if (command === 'init') {
    const mount = resolve(args[1]); await directory(mount);
    const device = (await lstat(mount)).dev;
    if (device === (await lstat(dirname(mount))).dev) fail('DEDICATED_DATA_MOUNT_REQUIRED');
    const root = await rootPath(args[0]); const storeId = randomBytes(16).toString('hex');
    const config = { format: 'kfm-pc-pipeline-config-v1', root, mount, device, storeId, sources: ['usgs-streamflow','nws-alerts'], publish: false, approvalDirectory: '/etc/kfm-pipeline/approvals' };
    await immutable(resolve(root, '.kfm-pipeline-store'), Buffer.from(storeId));
    await storageGuard(config);
    await immutable(resolve(args[2]), bytes(config)); return { state: 'initialized', publish: false, configPath: args[2] };
  }
  if (command === 'tick') return tick(await loadConfig(resolve(args[0])));
  if (command === 'status') {
    const config = await loadConfig(resolve(args[0])); await storageGuard(config);
    const j = await Journal.open(resolve(config.root, 'pipeline-journal.sqlite'));
    try { return { storage: 'verified', jobs: j.status() }; } finally { j.close(); }
  }
  if (command === 'stage-package') {
    const config = await loadConfig(resolve(args[0])); await storageGuard(config);
    const sourceId = args[1]; if (!['water','weather'].includes(sourceId)) fail('SOURCE_NOT_ALLOWED');
    const snapshot = parse(await readRegular(resolve(args[2]), MAX_PACKAGE)); const decision = parse(await readRegular(resolve(args[3]), 8192));
    const payload = bytes({ snapshot, decision }); if (payload.length > MAX_PACKAGE) fail('BYTE_LIMIT');
    const approval = parse(await readRegular(resolve(config.approvalDirectory, sourceId + '.json'), 32768));
    const secret = (await readRegular(resolve(process.env.CREDENTIALS_DIRECTORY ?? '/nonexistent', 'pipeline-worker-key'), 128)).toString().trim();
    const current = await pipelineCall('release', { sourceId }, secret);
    const m = { format: 'kfm-pc-release-transfer-v1', sourceId, recipeSha256: await recipeDigest(), byteLength: payload.length, payloadSha256: sha(payload), approval, expectedActive: current.releaseId };
    const receipt = await publish(m, payload, secret);
    await immutable(resolve(config.root, 'data/receipts/pipeline/published', receipt.releaseId + '.json'), bytes(receipt)); return receipt;
  }
  if (command === 'ftps-mirror') {
    const config = await loadConfig(resolve(args[0])); await storageGuard(config);
    const id = args[1]; if (!/^[a-f0-9]{64}$/.test(id)) fail('DIGEST_INVALID');
    const manifest = parse(await readRegular(resolve(config.root, 'data/receipts/pipeline/transfers', id + '.json'), 65536));
    const payload = await readRegular(resolve(args[2]), MAX_PACKAGE);
    const credentials = process.env.CREDENTIALS_DIRECTORY; if (!credentials) fail('SYSTEMD_CREDENTIAL_REQUIRED');
    const secret = (await readRegular(resolve(credentials, 'pipeline-worker-key'), 128)).toString().trim();
    const receipt = await pipelineCall('release', { releaseId: id }, secret);
    const ftps = parse(await readRegular(resolve(credentials, 'ftps.json'), 16384));
    const { mirrorFtps } = await import('./ftps.mjs');
    const result = await mirrorFtps(ftps, manifest, payload, receipt);
    await immutable(resolve(config.root, 'data/receipts/pipeline/ftps', id + '.json'), bytes(result)); return result;
  }
  if (command === 'backup') {
    const config = await loadConfig(resolve(args[0])); await storageGuard(config);
    const backupConfig = await loadConfig(resolve(args[1])); await storageGuard(backupConfig);
    const destination = await rootPath(backupConfig.root);
    if ((await lstat(destination)).dev === (await lstat(config.root)).dev) fail('INDEPENDENT_BACKUP_REQUIRED');
    await immutable(resolve(config.root, 'data/receipts/pipeline/configs', sha(bytes(config)) + '.json'), bytes(config));
    const journalPath = resolve(config.root, 'pipeline-journal.sqlite');
    try {
      await lstat(journalPath);
      const j = await Journal.open(journalPath);
      const snapshots = resolve(config.root, 'data/receipts/pipeline/journal-snapshots'); await directory(snapshots, true);
      const snapshot = resolve(snapshots, randomBytes(16).toString('hex') + '.sqlite');
      try { j.db.prepare('VACUUM INTO ?').run(snapshot); } finally { j.close(); }
      const check = await hashFile(snapshot);
      await immutable(resolve(config.root, 'data/receipts/pipeline/journal-backups', check.sha256 + '.json'), bytes({ ...check, file: snapshot.split('/').at(-1) }));
    } catch (e) { if (e.code !== 'ENOENT') throw e; }
    const inventory = await walk(resolve(config.root, 'data'));
    await storageGuard(backupConfig, { reserve: inventory.reduce((n, item) => n + item.bytes, 0) });
    for (const item of inventory) {
      const input = resolve(config.root, 'data', item.path); const output = resolve(destination, 'data', item.path);
      // Stream large originals in bounded memory; immutable capture code owns this copy.
      const { captureFile } = await import('./copy.mjs'); await captureFile(input, output, item);
    }
    const id = sha(bytes(inventory));
    await immutable(resolve(destination, 'backup-manifests', id + '.json'), bytes({ format: 'kfm-pc-data-backup-v1', files: inventory,
      storeId: config.storeId, sourceDevice: String((await lstat(config.root)).dev), backupDevice: String((await lstat(destination)).dev), inventorySha256: id }));
    return { state: 'verified-copy', files: inventory.length, inventorySha256: id, restoreTestRequired: true };
  }
  if (command === 'verify-backup') {
    const manifest = parse(await readRegular(resolve(args[0]), 64 * 1024 ** 2), 64 * 1024 ** 2);
    if (manifest.format !== 'kfm-pc-data-backup-v1' || !Array.isArray(manifest.files) || manifest.files.length > 1000000) fail('BACKUP_MANIFEST_INVALID');
    for (const item of manifest.files) {
      if (typeof item.path !== 'string' || item.path.startsWith('/') || item.path.split('/').some(p => !p || p === '..' || p === '.') || item.path.includes('\\')) fail('BACKUP_PATH_INVALID');
      const observed = await hashFile(resolve(args[1], 'data', item.path));
      if (observed.bytes !== item.bytes || observed.sha256 !== item.sha256) fail('BACKUP_INTEGRITY_FAILED');
    }
    return { state: 'verified', files: manifest.files.length };
  }
  if (command === 'restore-test') {
    const manifest = parse(await readRegular(resolve(args[0]), 64 * 1024 ** 2), 64 * 1024 ** 2);
    if (manifest.format !== 'kfm-pc-data-backup-v1' || !Array.isArray(manifest.files) || manifest.files.length > 1000000 || sha(bytes(manifest.files)) !== manifest.inventorySha256
      || String((await lstat(resolve(args[1]))).dev) !== manifest.backupDevice || manifest.backupDevice === manifest.sourceDevice) fail('BACKUP_MANIFEST_INVALID');
    const restored = await rootPath(args[2]); if ((await readdir(restored)).length) fail('RESTORE_TARGET_MUST_BE_EMPTY');
    const { captureFile } = await import('./copy.mjs');
    for (const item of manifest.files) {
      if (typeof item.path !== 'string' || item.path.startsWith('/') || item.path.split('/').some(p => !p || p === '..' || p === '.') || item.path.includes('\\')) fail('BACKUP_PATH_INVALID');
      await captureFile(resolve(args[1], 'data', item.path), resolve(restored, 'data', item.path), item);
    }
    const receipt = { format: 'kfm-pipeline-restore-receipt-v1', state: 'verified', storeId: manifest.storeId, sourceDevice: manifest.sourceDevice,
      backupDevice: manifest.backupDevice, inventorySha256: manifest.inventorySha256, files: manifest.files.length, restoredAt: new Date().toISOString() };
    await immutable(resolve(restored, 'restore-receipt.json'), bytes(receipt)); return receipt;
  }
  return { usage: 'inventory | keys DIR | profile-template SOURCE | approve PROFILE PRIVATE_KEY OUTPUT | control COMMAND PRIVATE_KEY | rehearse PRIVATE_ROOT | init ROOT MOUNT CONFIG | tick CONFIG | status CONFIG | stage-package CONFIG water|weather SNAPSHOT DECISION | ftps-mirror CONFIG RELEASE_ID PUBLIC_PRODUCT | backup CONFIG BACKUP_CONFIG | verify-backup MANIFEST ROOT | restore-test MANIFEST BACKUP_ROOT EMPTY_RESTORE_ROOT' };
}
if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try { console.log(canonical(await cli(process.argv.slice(2)))); }
  catch (e) { console.error(canonical({ state: 'held', reason: /^[A-Z_]{1,64}$/.test(e.message) ? e.message : 'PIPELINE_OPERATION_FAILED' })); process.exitCode = 1; }
}
