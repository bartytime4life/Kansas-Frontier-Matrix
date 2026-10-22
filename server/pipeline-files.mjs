import { constants, createReadStream } from 'node:fs';
import { lstat, mkdir, open, link, unlink, statfs } from 'node:fs/promises';
import { resolve, dirname, sep } from 'node:path';
import { createHash, randomUUID } from 'node:crypto';
import { fail, digest } from './pipeline-contract.mjs';

export async function directory(path, create = false) {
  if (!path.startsWith('/') || path.split('/').includes('..')) fail('PATH_INVALID');
  let current = '/';
  for (const part of path.split('/').filter(Boolean)) {
    current = resolve(current, part);
    let info;
    try { info = await lstat(current); }
    catch (e) { if (e.code !== 'ENOENT' || !create) throw e; await mkdir(current, { mode: 0o700 }); info = await lstat(current); }
    if (!info.isDirectory() || info.isSymbolicLink()) fail('DIRECTORY_UNSAFE');
  }
}
export async function syncDirectory(path) { const fd = await open(path, 'r'); try { await fd.sync(); } finally { await fd.close(); } }
export async function immutable(path, bytes) {
  await directory(dirname(path), true);
  const temp = path + '.' + randomUUID() + '.part';
  const fd = await open(temp, constants.O_WRONLY | constants.O_CREAT | constants.O_EXCL | constants.O_NOFOLLOW, 0o600);
  try { await fd.writeFile(bytes); await fd.sync(); } finally { await fd.close(); }
  try {
    try { await link(temp, path); await syncDirectory(dirname(path)); }
    catch (e) { if (e.code !== 'EEXIST') throw e; const existing = await readRegular(path, bytes.length); if (!existing.equals(Buffer.from(bytes))) fail('IMMUTABLE_CONFLICT'); }
  } finally { await unlink(temp); }
}
export async function readRegular(path, limit) {
  await directory(dirname(path));
  const fd = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try { const info = await fd.stat(); if (!info.isFile() || info.size > limit) fail('FILE_LIMIT'); return await fd.readFile(); }
  finally { await fd.close(); }
}
export async function hashFile(path) {
  await directory(dirname(path));
  const fd = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try {
    const before = await fd.stat(); if (!before.isFile()) fail('FILE_INVALID');
    const h = createHash('sha256'); let length = 0;
    for await (const chunk of createReadStream('', { fd: fd.fd, autoClose: false })) { h.update(chunk); length += chunk.length; }
    const after = await fd.stat();
    if (length !== before.size || before.size !== after.size || before.mtimeMs !== after.mtimeMs || before.ctimeMs !== after.ctimeMs) fail('FILE_CHANGED');
    return { sha256: h.digest('hex'), bytes: length };
  } finally { await fd.close(); }
}
export async function storageGuard(config, { reserve = 0 } = {}) {
  const root = resolve(config.root); const mount = resolve(config.mount);
  if (root === mount || !root.startsWith(mount + sep) || mount === '/') fail('DEDICATED_DATA_MOUNT_REQUIRED');
  await directory(root); await directory(mount);
  // The OS mount is checked every tick. A missing mount must never redirect writes to root.
  const info = await lstat(mount); const parent = await lstat(dirname(mount));
  if (info.dev === parent.dev || String(info.dev) !== String(config.device)) fail('STORAGE_IDENTITY_CHANGED');
  const marker = (await readRegular(resolve(root, '.kfm-pipeline-store'), 128)).toString().trim();
  if (marker !== config.storeId) fail('STORAGE_IDENTITY_CHANGED');
  const data = await statfs(root); const system = await statfs('/');
  // Linux persistent disk/NAS filesystems only; tmpfs/ramfs/overlay are not a data store.
  if (![0xef53, 0x58465342, 0x9123683e, 0x6969, 0xff534d42, 0xfe534d42, 0x2fc12fc1].includes(data.type >>> 0)) fail('DURABLE_FILESYSTEM_REQUIRED');
  const free = data.bavail * data.bsize; const size = data.blocks * data.bsize;
  if (free - reserve < size * 0.20 || system.bavail * system.bsize < 30 * 1024 ** 3) fail('DISK_RESERVE_REQUIRED');
  return { freeBytes: free, totalBytes: size, reserveBytes: reserve };
}
export class ArtifactFiles {
  constructor(root) { this.root = root; }
  path(release, index) { digest(release); if (!Number.isInteger(index) || index < 0 || index >= 32) fail('CHUNK_INVALID', 400); return resolve(this.root, release, String(index)); }
  async put(release, index, bytes) { await immutable(this.path(release, index), bytes); }
  async get(release, index, limit) { return readRegular(this.path(release, index), limit); }
  async health(reserve = 0) {
    await directory(this.root); const marker = await readRegular(resolve(this.root, '.qualified'), 128);
    if (marker.toString().trim() !== 'kfm-private-artifacts-v1') fail('ARTIFACT_STORAGE_NOT_QUALIFIED');
    const fs = await statfs(this.root);
    if (fs.bavail * fs.bsize - reserve < 256 * 1024 ** 2) fail('ARTIFACT_STORAGE_FULL');
  }
}
