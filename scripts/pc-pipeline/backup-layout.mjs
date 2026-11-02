import { resolve } from 'node:path';
import { canonical, sha, fail } from '../../server/pipeline-contract.mjs';

export function validateBackup(manifest) {
  if (!['kfm-pc-data-backup-v1','kfm-pc-data-backup-v2'].includes(manifest.format) || !Array.isArray(manifest.files) || manifest.files.length > 1000000
    || sha(Buffer.from(canonical(manifest.files))) !== manifest.inventorySha256) fail('BACKUP_MANIFEST_INVALID');
  if (manifest.separateBackup !== undefined && (!Array.isArray(manifest.separateBackup) || manifest.separateBackup.length > 8
    || manifest.separateBackup.some(p => typeof p !== 'string'))) fail('BACKUP_MANIFEST_INVALID');
  const seen = new Set();
  for (const item of manifest.files) {
    if (typeof item.path !== 'string' || item.path.startsWith('/') || item.path.split('/').some(p => !p || p === '..' || p === '.') || item.path.includes('\\')
      || !/^[a-f0-9]{64}$/.test(item.sha256 ?? '') || !Number.isSafeInteger(item.bytes) || item.bytes < 0 || seen.has(item.path)) fail('BACKUP_PATH_INVALID');
    seen.add(item.path);
  }
  return manifest;
}
// A working database named in config.separateBackup has its own verified snapshot job. Its SQLite
// sidecar files belong to it, so the per-file backup leaves all of them out.
export function separatelyBackedUp(paths = []) {
  const skip = new Set(paths.flatMap(p => [p, p + '-journal', p + '-wal', p + '-shm']));
  return path => skip.has(path);
}
export function backupObjectPath(root, item, format = 'kfm-pc-data-backup-v2') {
  if (!/^[a-f0-9]{64}$/.test(item.sha256 ?? '')) fail('DIGEST_INVALID');
  return format === 'kfm-pc-data-backup-v2' ? resolve(root, 'objects/sha256', item.sha256, 'payload') : resolve(root, 'data', item.path);
}
