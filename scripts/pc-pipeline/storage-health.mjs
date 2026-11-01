#!/usr/bin/env node
/** Private, read-only Linux diagnostics. No mounting, repair, self-tests or writes. */
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { realpath, stat, statfs } from 'node:fs/promises';
import { isAbsolute, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const exec = promisify(execFile);
export async function runReadOnly(command, args) {
  const options = { encoding: 'utf8', timeout: 15000, maxBuffer: 2 * 1024 ** 2, env: { ...process.env, LC_ALL: 'C' } };
  try { const { stdout } = await exec(command, args, options); return { status: 0, value: JSON.parse(stdout) }; }
  catch (error) {
    // smartctl returns a bitmask even when it successfully produced diagnostics.
    if (command === 'smartctl' && Number.isInteger(error.code) && error.stdout) {
      try { return { status: error.code, value: JSON.parse(error.stdout) }; } catch { /* Unknown, never healthy. */ }
    }
    return { status: null, value: null };
  }
}

// Input is lsblk --inverse --tree JSON for ONE filesystem's major:minor device.
export function backingDisks(value, device) {
  const disks = new Set(), warnings = new Set(); let complete = true, lvm = false;
  const nodes = value?.blockdevices;
  if (!Array.isArray(nodes) || nodes.length !== 1 || nodes[0]['maj:min'] !== device) return { state: 'unknown', disks: [], warnings: [] };
  const visit = (node, depth = 0) => {
    if (depth > 32 || !node || !['disk', 'part', 'lvm', 'crypt'].includes(node.type)) { complete = false; return; }
    if (node.type === 'lvm') lvm = true;
    if (node.ro === true || node.ro === 1 || node.ro === '1') warnings.add('READ_ONLY_BLOCK_DEVICE');
    if (node.state && !['running', 'live'].includes(node.state)) warnings.add('BLOCK_DEVICE_STATE_REQUIRES_REVIEW');
    if (node.type === 'disk') {
      if (!/^\/dev\/[a-zA-Z0-9_./-]+$/.test(node.name ?? '') || node.children?.length) complete = false;
      else disks.add(node.name);
    } else if (!Array.isArray(node.children) || !node.children.length) complete = false;
    else for (const child of node.children) visit(child, depth + 1);
  };
  visit(nodes[0]);
  if (disks.size > 1) warnings.add('MULTI_DISK_VOLUME_REDUNDANCY_NOT_ESTABLISHED');
  return { state: complete && disks.size ? 'observed' : 'unknown', disks: [...disks].sort(), warnings: [...warnings].sort(), lvm };
}

export function lvmHealth(result, device) {
  const rows = result?.value?.report?.flatMap(report => report.lv ?? []);
  if (result?.status !== 0 || !Array.isArray(rows)) return { state: 'unknown', warnings: [] };
  const matching = rows.filter(row => `${String(row.lv_kernel_major).trim()}:${String(row.lv_kernel_minor).trim()}` === device);
  if (!matching.length) return { state: 'unknown', warnings: [] };
  const warnings = new Set(); let complete = true;
  for (const row of matching) {
    const attr = String(row.lv_attr ?? '').trim();
    if (attr.length < 9 || !String(row.devices ?? '').trim()) complete = false;
    if (attr[8] === 'p' || /unknown|missing/i.test(row.devices ?? '')) warnings.add('LVM_MISSING_PHYSICAL_VOLUME');
    if (attr[4] !== 'a') warnings.add('LVM_NOT_ACTIVE');
    if (String(row.segtype).trim() !== 'linear') complete = false; // Other layouts need their own qualified health checks.
  }
  return { state: warnings.size ? 'warning' : complete ? 'observed' : 'unknown', warnings: [...warnings].sort() };
}

export function separation(a, b) {
  if (a.device && a.device === b.device) return 'shared-filesystem';
  if (a.topology.disks.some(disk => b.topology.disks.includes(disk))) return 'shared-physical-disk';
  return a.topology.state === 'observed' && b.topology.state === 'observed' ? 'distinct-disks-observed' : 'unknown';
}

export function smartHealth(result) {
  const value = result?.value, status = result?.status;
  const warnings = new Set();
  if (!Number.isInteger(status) || status < 0 || status > 255 || !value) return { state: 'unknown', warnings: [] };
  if (status & 0xf8) warnings.add('SMART_STATUS_OR_HISTORY_REQUIRES_REVIEW');
  if (value.smart_status?.passed === false) warnings.add('SMART_HEALTH_FAILED');
  for (const attr of value.ata_smart_attributes?.table ?? []) {
    // These counters are warning evidence, not a prediction of imminent failure.
    if ([5, 187, 188, 197, 198].includes(attr.id) && Number(attr.raw?.value) > 0) warnings.add('ATA_ERROR_COUNTER_REQUIRES_REVIEW');
  }
  const nvme = value.nvme_smart_health_information_log;
  if (Number(nvme?.critical_warning) > 0 || Number(nvme?.media_errors) > 0) warnings.add('NVME_ERROR_REQUIRES_REVIEW');
  return { state: warnings.size ? 'warning' : status === 0 && value.smart_status?.passed === true ? 'no-warning-observed' : 'unknown', warnings: [...warnings].sort() };
}

export async function storageHealth(paths, { smart = false, run = runReadOnly, fs = { realpath, stat, statfs }, now = () => new Date() } = {}) {
  if (!Array.isArray(paths) || paths.length < 2 || paths.length > 3 || paths.some(p => typeof p !== 'string' || !isAbsolute(p))) throw Error('USE_SOURCE_BACKUP_OPTIONAL_ARCHIVE_ABSOLUTE_PATHS');
  const roles = ['source', 'backup', 'archive'], stores = [];
  for (const [index, path] of paths.entries()) {
    const store = { role: roles[index], state: 'unknown', device: null, topology: { state: 'unknown', disks: [], warnings: [] }, warnings: [] };
    stores.push(store);
    try {
      const root = await fs.realpath(path);
      if (!(await fs.stat(root)).isDirectory()) throw Error('NOT_DIRECTORY');
      const mount = await run('findmnt', ['--json', '--target', root, '--output', 'MAJ:MIN,OPTIONS,FSTYPE']);
      const entries = mount.value?.filesystems;
      const found = entries?.length === 1 ? entries[0] : null;
      if (mount.status !== 0 || !/^\d+:\d+$/.test(found?.['maj:min'] ?? '')) throw Error('MOUNT_UNAVAILABLE');
      store.device = found['maj:min'];
      store.filesystem = found.fstype;
      if (String(found.options).split(',').includes('ro')) store.warnings.push('READ_ONLY_FILESYSTEM');
      const capacity = await fs.statfs(root, { bigint: true });
      const free = BigInt(capacity.bavail) * BigInt(capacity.bsize), total = BigInt(capacity.blocks) * BigInt(capacity.bsize);
      store.freeBytes = String(free); store.totalBytes = String(total);
      if (total <= 0n) throw Error('CAPACITY_UNAVAILABLE');
      if (free * 5n < total) store.warnings.push('BELOW_TWENTY_PERCENT_FREE');
      const blocks = await run('lsblk', ['--json', '--inverse', '--paths', '--tree', '--output', 'NAME,TYPE,MAJ:MIN,RO,STATE', '--', '/dev/block/' + store.device]);
      if (blocks.status === 0) store.topology = backingDisks(blocks.value, store.device);
      // A filesystem-level multi-device pool (e.g. Btrfs/ZFS/NAS) is not described by this graph.
      if (!['ext2', 'ext3', 'ext4', 'xfs'].includes(store.filesystem)) store.topology.state = 'unknown';
      store.warnings.push(...store.topology.warnings);
      if (store.topology.lvm) {
        store.lvm = lvmHealth(await run('lvs', ['--readonly', '--reportformat', 'json', '--segments', '--options', 'lv_kernel_major,lv_kernel_minor,lv_attr,segtype,devices']), store.device);
        store.warnings.push(...store.lvm.warnings);
        if (store.lvm.state !== 'observed') store.topology.state = 'unknown';
      }
      store.state = store.topology.state;
      // A second mount read detects common unmount/remount races; this is not a lock or qualification.
      const again = await run('findmnt', ['--json', '--target', root, '--output', 'MAJ:MIN,OPTIONS,FSTYPE']);
      if (again.status !== 0 || JSON.stringify(again.value) !== JSON.stringify(mount.value)) {
        store.state = 'unknown'; store.topology.state = 'unknown'; store.warnings.push('MOUNT_CHANGED_DURING_CHECK');
      }
    } catch { store.state = 'unknown'; store.topology.state = 'unknown'; }
  }
  const devices = [...new Set(stores.flatMap(s => s.topology.disks))].sort();
  const driveHealth = [];
  for (const device of devices) driveHealth.push({ device, ...(smart ? smartHealth(await run('smartctl', ['--json', '--all', '--nocheck=standby,2', device])) : { state: 'not-checked', warnings: [] }) });
  const relationships = [];
  for (let i = 0; i < stores.length; i++) for (let j = i + 1; j < stores.length; j++) relationships.push({ a: stores[i].role, b: stores[j].role, state: separation(stores[i], stores[j]) });
  const warning = stores.some(s => s.warnings.length) || driveHealth.some(d => d.warnings.length) || relationships.some(r => r.state.startsWith('shared-'));
  const unknown = stores.some(s => s.state !== 'observed') || driveHealth.some(d => ['unknown', 'not-checked'].includes(d.state));
  return { format: 'kfm-storage-health-v1', checkedAt: now().toISOString(), state: warning ? 'degraded' : unknown ? 'needs-verification' : 'checked',
    stores, relationships, driveHealth, copyIntegrity: 'not-checked', recovery: 'not-tested', physicalIndependenceQualified: false,
    scope: 'local-block-dependencies-only; host-power-controller-site-and-identity-not-qualified', productionChanged: false };
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const args = process.argv.slice(2), smart = args[0] === '--smart';
    const report = await storageHealth(smart ? args.slice(1) : args, { smart });
    console.log(JSON.stringify(report));
    process.exitCode = report.state === 'checked' ? 0 : report.state === 'degraded' ? 2 : 3;
  } catch { console.error(JSON.stringify({ state: 'held', reason: 'STORAGE_DIAGNOSTIC_USAGE_INVALID' })); process.exitCode = 1; }
}
