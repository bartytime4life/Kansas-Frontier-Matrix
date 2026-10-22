import { constants } from 'node:fs';
import { open, link, unlink } from 'node:fs/promises';
import { dirname } from 'node:path';
import { randomUUID } from 'node:crypto';
import { directory, hashFile, syncDirectory } from '../../server/pipeline-files.mjs';
import { fail } from '../../server/pipeline-contract.mjs';

export async function captureFile(input, output, expected) {
  await directory(dirname(input)); await directory(dirname(output), true);
  try { const old = await hashFile(output); if (old.sha256 !== expected.sha256 || old.bytes !== expected.bytes) fail('BACKUP_CONFLICT'); return; }
  catch (e) { if (e.code !== 'ENOENT') throw e; }
  const temp = output + '.' + randomUUID() + '.part';
  const reader = await open(input, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  const writer = await open(temp, constants.O_CREAT | constants.O_EXCL | constants.O_WRONLY | constants.O_NOFOLLOW, 0o600);
  try {
    const before = await reader.stat(); if (!before.isFile() || before.size !== expected.bytes) fail('BACKUP_INPUT_CHANGED');
    const buffer = Buffer.alloc(1024 * 1024); let offset = 0;
    while (offset < expected.bytes) {
      const { bytesRead } = await reader.read(buffer, 0, Math.min(buffer.length, expected.bytes - offset), offset);
      if (!bytesRead) fail('BACKUP_INPUT_CHANGED');
      let wrote = 0;
      while (wrote < bytesRead) { const result = await writer.write(buffer, wrote, bytesRead - wrote); if (!result.bytesWritten) fail('BACKUP_WRITE_FAILED'); wrote += result.bytesWritten; }
      offset += bytesRead;
    }
    await writer.sync();
    const after = await reader.stat(); if (before.mtimeMs !== after.mtimeMs || before.ctimeMs !== after.ctimeMs || before.size !== after.size) fail('BACKUP_INPUT_CHANGED');
    const check = await hashFile(temp); if (check.sha256 !== expected.sha256 || check.bytes !== expected.bytes) fail('BACKUP_INTEGRITY_FAILED');
    await link(temp, output); await syncDirectory(dirname(output));
  } finally { await reader.close(); await writer.close(); await unlink(temp); }
}
