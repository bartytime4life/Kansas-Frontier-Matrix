import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, mkdir, writeFile, readFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { backingDisks, separation, smartHealth, lvmHealth, storageHealth, runReadOnly } from '../scripts/pc-pipeline/storage-health.mjs';
import { captureFile } from '../scripts/pc-pipeline/copy.mjs';
import { hashFile } from '../server/pipeline-files.mjs';
import { canonical, sha } from '../server/pipeline-contract.mjs';
import { validateBackup, backupObjectPath } from '../scripts/pc-pipeline/backup-layout.mjs';
import { KIT_FILES } from '../scripts/pc-pipeline/bundle.mjs';

const disk = name => ({ name, type: 'disk', ro: false, state: 'running' });
const volume = (device, names, type = 'lvm') => ({ blockdevices: [{ name: '/dev/mapper/test', type, 'maj:min': device, children: names.map(disk) }] });
const store = (device, names) => ({ device, topology: backingDisks(volume(device, names), device) });
test('same LV, separate partitions, shared PVs and disjoint disks are distinguished', () => {
  assert.equal(separation(store('253:1', ['/dev/sda']), store('253:1', ['/dev/sda'])), 'shared-filesystem');
  assert.equal(separation(store('8:1', ['/dev/sda']), store('8:2', ['/dev/sda'])), 'shared-physical-disk');
  assert.equal(separation(store('253:1', ['/dev/sda', '/dev/sdb']), store('253:2', ['/dev/sdb', '/dev/sdc'])), 'shared-physical-disk');
  assert.equal(separation(store('8:1', ['/dev/sda']), store('8:17', ['/dev/sdb'])), 'distinct-disks-observed');
  assert.deepEqual(store('253:1', ['/dev/sda', '/dev/sdb', '/dev/sdc']).topology.warnings, ['MULTI_DISK_VOLUME_REDUNDANCY_NOT_ESTABLISHED']);
});
test('unknown, unsupported, truncated and mismatched block graphs never prove separation', () => {
  for (const graph of [null, {}, { blockdevices: [] }, volume('1:1', ['/dev/sda']), volume('8:1', [], 'raid1'), volume('8:1', [])]) {
    const topology = backingDisks(graph, '8:1');
    assert.equal(topology.state, 'unknown');
    assert.equal(separation({ device: '8:1', topology }, store('8:17', ['/dev/sdb'])), 'unknown');
  }
  const graph = volume('8:1', ['/dev/sda']); graph.blockdevices[0].children.push({ type: 'part' });
  assert.equal(backingDisks(graph, '8:1').state, 'unknown');
});
test('read-only and non-running block devices produce warnings', () => {
  const graph = volume('253:1', ['/dev/sda']); graph.blockdevices[0].children[0].ro = true;
  graph.blockdevices[0].children[0].state = 'offline';
  assert.deepEqual(backingDisks(graph, '253:1').warnings, ['BLOCK_DEVICE_STATE_REQUIRES_REVIEW', 'READ_ONLY_BLOCK_DEVICE']);
});
test('SMART failures, historical errors, pending sectors and NVMe errors remain visible', () => {
  const check = (status, value) => smartHealth({ status, value });
  assert.equal(check(0, { smart_status: { passed: true } }).state, 'no-warning-observed');
  for (const status of [null, 1, 2, 4]) assert.equal(check(status, {}).state, 'unknown');
  for (const status of [8, 16, 32, 64, 128]) assert.equal(check(status, {}).state, 'warning');
  assert.equal(check(0, { smart_status: { passed: false } }).state, 'warning');
  for (const id of [5, 187, 188, 197, 198]) assert.equal(check(0, { ata_smart_attributes: { table: [{ id, raw: { value: 1 } }] } }).state, 'warning');
  assert.equal(check(0, { nvme_smart_health_information_log: { critical_warning: 1 } }).state, 'warning');
  assert.equal(check(0, { nvme_smart_health_information_log: { media_errors: 2 } }).state, 'warning');
});
const lvs = (devices = '/dev/sda(0)', attr = '-wi-a-----', segtype = 'linear') => ({ status: 0, value: { report: [{ lv: [{ lv_kernel_major: '253', lv_kernel_minor: '1', devices, lv_attr: attr, segtype }] }] } });
test('missing LVM PVs, inactive volumes and unavailable or unsupported reports are explicit', () => {
  assert.equal(lvmHealth(lvs(), '253:1').state, 'observed');
  assert.equal(lvmHealth(lvs('[unknown](0)', '-wi-a---p-'), '253:1').state, 'warning');
  assert.equal(lvmHealth(lvs('/dev/sda(0)', '-wi-------'), '253:1').state, 'warning');
  for (const value of [null, { status: 1 }, lvs(), lvs('/dev/sda', '-wi-a-----', 'raid1')]) {
    assert.equal(lvmHealth(value, value === null || value.status !== 0 ? '253:1' : value.value.report[0].lv[0].segtype === 'raid1' ? '253:1' : '253:2').state, 'unknown');
  }
});
function fixture({ shared = false, low = false, smartStatus = 0, changeMount = false, missingLvm = false } = {}) {
  const calls = []; let mounts = 0;
  const fs = { realpath: async p => p, stat: async () => ({ isDirectory: () => true }), statfs: async () => ({ bavail: low ? 19n : 80n, bsize: 1n, blocks: 100n }) };
  const run = async (command, args) => {
    calls.push([command, args]);
    if (command === 'findmnt') {
      mounts++;
      return { status: 0, value: { filesystems: [{ 'maj:min': changeMount && mounts === 2 ? '8:99' : args.includes('/source') ? '8:1' : '253:1', fstype: 'ext4', options: 'rw,nosuid' }] } };
    }
    if (command === 'lsblk') {
      const mm = args.at(-1).split('/').at(-1);
      return { status: 0, value: volume(mm, [mm === '8:1' || shared ? '/dev/sda' : '/dev/sdb'], mm === '8:1' ? 'part' : 'lvm') };
    }
    if (command === 'lvs') return missingLvm ? { status: null } : lvs();
    if (command === 'smartctl') return { status: smartStatus, value: { smart_status: { passed: true } } };
    throw Error('UNEXPECTED_COMMAND');
  };
  return { calls, fs, run };
}
test('three-store report separates copy integrity, recovery and physical qualification', async () => {
  const f = fixture(); const r = await storageHealth(['/source', '/backup', '/archive'], { ...f, smart: true });
  assert.equal(r.state, 'degraded'); // backup and archive on the same LV
  assert.equal(r.relationships[0].state, 'distinct-disks-observed');
  assert.equal(r.relationships[2].state, 'shared-filesystem');
  assert.equal(r.copyIntegrity, 'not-checked'); assert.equal(r.recovery, 'not-tested');
  assert.equal(r.physicalIndependenceQualified, false); assert.equal(r.productionChanged, false);
  assert.equal(f.calls.filter(([c]) => c === 'smartctl').length, 2); // once per disk
  assert.ok(f.calls.every(([c]) => ['findmnt', 'lsblk', 'lvs', 'smartctl'].includes(c)));
  assert.deepEqual(f.calls.find(([c]) => c === 'smartctl')[1], ['--json', '--all', '--nocheck=standby,2', '/dev/sda']);
});
test('shared PVs, low capacity, SMART failures, missing LVM access and mount races fail visibly', async () => {
  for (const options of [{ shared: true }, { low: true }, { smartStatus: 8 }]) {
    assert.equal((await storageHealth(['/source', '/backup'], { ...fixture(options), smart: true })).state, 'degraded');
  }
  const changed = await storageHealth(['/source', '/backup'], { ...fixture({ changeMount: true }), smart: true });
  assert.equal(changed.state, 'degraded');
  assert.equal(changed.stores[0].topology.state, 'unknown');
  assert.ok(changed.stores[0].warnings.includes('MOUNT_CHANGED_DURING_CHECK'));
  assert.equal((await storageHealth(['/source', '/backup'], { ...fixture({ missingLvm: true }), smart: true })).state, 'needs-verification');
  const f = fixture(); assert.equal((await storageHealth(['/source', '/backup'], f)).state, 'needs-verification');
  assert.ok(!f.calls.some(([c]) => c === 'smartctl'));
  assert.equal((await storageHealth(['/source', '/backup'], { ...fixture(), run: async () => ({ status: null }) })).state, 'needs-verification');
});
test('invalid paths refuse before executing diagnostics; inaccessible data stays unknown', async () => {
  for (const paths of [[], ['/source'], ['relative', '/backup'], ['/source', '/backup', '/archive', '/fourth']]) {
    await assert.rejects(storageHealth(paths, { run: () => { throw Error('must not run'); } }), /ABSOLUTE_PATHS/);
  }
  const r = await storageHealth(['/source', '/backup'], { ...fixture(), fs: { realpath: async () => { throw Error('private-error'); } } });
  assert.equal(r.state, 'needs-verification'); assert.ok(!JSON.stringify(r).includes('private-error'));
});
test('real temporary directories and sentinels remain byte-identical with unavailable topology', async () => {
  const root = await mkdtemp(join(tmpdir(), 'kfm-health-test-'));
  try {
    const paths = [join(root, 'source'), join(root, 'backup')];
    for (const path of paths) { await mkdir(path); await writeFile(join(path, 'preserved-receipt'), 'do not change'); }
    const r = await storageHealth(paths, { run: async () => ({ status: null }) });
    assert.equal(r.state, 'needs-verification');
    for (const path of paths) assert.equal(await readFile(join(path, 'preserved-receipt'), 'utf8'), 'do not change');
  } finally { await rm(root, { recursive: true }); } // only this test's newly created tree
});
test('missing diagnostic executable is bounded and does not expose process errors', async () => {
  assert.deepEqual(await runReadOnly('kfm-nonexistent-readonly-test-command', []), { status: null, value: null });
});

test('diagnostic is present in commit-pinned kit; unsupported pooled filesystems stay unknown', async () => {
  assert.ok(KIT_FILES.includes('scripts/pc-pipeline/storage-health.mjs'));
  const f = fixture();
  const run = async (...args) => {
    const result = await f.run(...args);
    if (args[0] === 'findmnt') result.value.filesystems[0].fstype = 'btrfs';
    return result;
  };
  const report = await storageHealth(['/source', '/backup'], { ...f, run, smart: true });
  assert.equal(report.relationships[0].state, 'unknown');
  assert.equal(report.state, 'needs-verification');
});

test('existing v1/v2 copy primitives restore real fixture bytes and refuse corrupt or conflicting copies', async () => {
  const root = await mkdtemp(join(tmpdir(), 'kfm-recovery-fixture-'));
  try {
    const source = join(root, 'original'); await writeFile(source, Buffer.alloc(2 * 1024 ** 2 + 17, 37));
    const item = { path: 'quarantine/synthetic/payload', ...await hashFile(source) };
    for (const format of ['kfm-pc-data-backup-v1', 'kfm-pc-data-backup-v2']) {
      const backup = join(root, format), object = backupObjectPath(backup, item, format);
      const manifest = { format, files: [item], inventorySha256: sha(canonical([item])) };
      validateBackup(manifest);
      await captureFile(source, object, item);
      const restored = join(root, 'restore', format, item.path);
      await captureFile(object, restored, item);
      assert.deepEqual(await hashFile(restored), { bytes: item.bytes, sha256: item.sha256 });
      await writeFile(object, Buffer.alloc(item.bytes, 38)); // corrupt ONLY this test's temporary copy
      await assert.rejects(captureFile(object, join(root, 'refused', format), item), /BACKUP_INTEGRITY_FAILED/);
      await assert.rejects(captureFile(source, object, item), /BACKUP_CONFLICT/);
      assert.deepEqual(await hashFile(source), { bytes: item.bytes, sha256: item.sha256 });
      assert.equal((await readFile(object))[0], 38); // conflict preserved for investigation
    }
  } finally { await rm(root, { recursive: true }); }
});
