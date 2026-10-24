// Explicit root installation after storage and independent backup qualification.
import { mkdir, copyFile, chmod, lstat } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';
import { loadConfig } from './worker.mjs';
import { storageGuard, readRegular } from '../../server/pipeline-files.mjs';
import { canonical, parse, fail } from '../../server/pipeline-contract.mjs';
import { copyKit } from './bundle.mjs';

const configPath = process.argv.find(v => v.startsWith('--config='))?.slice(9);
const backupPath = process.argv.find(v => v.startsWith('--backup-receipt='))?.slice(17);
if (!process.argv.includes('--apply')) {
  console.log(canonical({ mode: 'review-only', installRoot: '/opt/kfm-pipeline', configRoot: '/etc/kfm-pipeline', dataMount: '/srv/kfm-data',
    account: 'kfm-pipeline', activates: false, requirements: ['root','verified mount','verified independent backup/restore receipt','config publish=false'] }));
} else {
  if (process.getuid?.() !== 0 || !configPath || !backupPath) fail('ROOT_CONFIG_BACKUP_REQUIRED');
  const config = await loadConfig(configPath); await storageGuard(config);
  if (config.mount !== '/srv/kfm-data' || config.publish !== false) fail('INSTALL_CAPTURE_ONLY_CONFIG_REQUIRED');
  const backup = parse(await readRegular(backupPath, 65536));
  if (backup.format !== 'kfm-pipeline-restore-receipt-v1' || backup.state !== 'verified' || backup.storeId !== config.storeId || String(backup.sourceDevice) !== String(config.device)
    || String(backup.backupDevice) === String(config.device) || !/^[a-f0-9]{64}$/.test(backup.inventorySha256 ?? '') || !(backup.payloadObjects > 0)) fail('VERIFIED_INDEPENDENT_RESTORE_REQUIRED');
  for (const path of ['/opt/kfm-pipeline','/etc/kfm-pipeline','/etc/kfm-pipeline/approvals']) {
    try { await lstat(path); fail('INSTALL_TARGET_EXISTS'); } catch (e) { if (e.code !== 'ENOENT') throw e; }
    await mkdir(path, { recursive: true, mode: 0o750 });
  }
  try { execFileSync('id', ['kfm-pipeline'], { stdio: 'ignore' }); }
  catch { execFileSync('useradd', ['--system','--home-dir','/nonexistent','--shell','/usr/sbin/nologin','kfm-pipeline']); }
  const root = fileURLToPath(new URL('../..', import.meta.url));
  await copyKit('/opt/kfm-pipeline');
  await copyFile(configPath, '/etc/kfm-pipeline/config.json'); await chmod('/etc/kfm-pipeline/config.json', 0o640);
  await copyFile(backupPath, '/etc/kfm-pipeline/restore-receipt.json');
  // Capture-only installation: empty credential is never used until a separate paired setup.
  const { writeFile } = await import('node:fs/promises'); await writeFile('/etc/kfm-pipeline/worker-key', '', { mode: 0o600, flag: 'wx' });
  // Kernel-owned lock spans complete capture/backup operations and releases on process death.
  await writeFile('/srv/kfm-data/.kfm-pipeline.lock', '', { mode: 0o600, flag: 'wx' });
  execFileSync('chown', ['kfm-pipeline:kfm-pipeline','/srv/kfm-data/.kfm-pipeline.lock']);
  for (const unit of ['kfm-pipeline.service','kfm-pipeline.timer','kfm-pipeline-backup.service','kfm-pipeline-backup.timer']) await copyFile(resolve(root, 'scripts/pc-pipeline/systemd', unit), resolve('/etc/systemd/system', unit));
  execFileSync('chown', ['root:kfm-pipeline','/opt/kfm-pipeline','/etc/kfm-pipeline','/etc/kfm-pipeline/config.json','/etc/kfm-pipeline/approvals']);
  // Only the new dedicated store may be handed to the new service account.
  execFileSync('chown', ['-R','kfm-pipeline:kfm-pipeline',config.root]);
  execFileSync('systemctl', ['daemon-reload']);
  console.log(canonical({ state: 'installed', activated: false, next: 'Review units, run one capture-only service invocation, then enable kfm-pipeline.timer.' }));
}
