import assert from "node:assert/strict";
import { lstat, mkdtemp, mkdir, rm, symlink } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import { inspectLocalPc } from "../scripts/prepare-local-pc.mjs";

async function withHome(fn) {
  const home = await mkdtemp(path.join(os.tmpdir(), "kfm-site-layout-"));
  try { await fn(home); } finally { await rm(home, { recursive: true, force: true }); }
}

test("inspection is read-only; apply creates private folders but leaves KFM data to its owner", async () => {
  await withHome(async (home) => {
    const plan = await inspectLocalPc(home);
    assert.equal(plan.action, "INSPECTED_ONLY");
    assert.deepEqual(plan.directories.map((item) => item.state), ["MISSING", "MISSING", "MISSING"]);
    await assert.rejects(lstat(path.join(home, "Downloads")), { code: "ENOENT" });
    const applied = await inspectLocalPc(home, true);
    assert.equal(applied.public_site_effect, "NONE");
    assert.deepEqual(applied.directories.map((item) => item.state), ["PRESENT", "PRESENT", "PRESENT"]);
    for (const item of applied.directories) assert.equal((await lstat(item.path)).mode & 0o077, 0);
    await assert.rejects(lstat(path.join(home, "KFM-data")), { code: "ENOENT" });
    assert.deepEqual((await inspectLocalPc(home, true)).directories, applied.directories);
  });
});

test("symlink in either target blocks all writes", async () => {
  await withHome(async (home) => {
    await symlink(os.tmpdir(), path.join(home, "KFM-site-recovery"));
    await assert.rejects(inspectLocalPc(home, true), /UNSAFE_PATH_COMPONENT/);
    await assert.rejects(lstat(path.join(home, "Downloads")), { code: "ENOENT" });
  });
});

test("a symlinked reference library blocks download and recovery setup", async () => {
  await withHome(async (home) => {
    await symlink(os.tmpdir(), path.join(home, "KFM-references"));
    await assert.rejects(inspectLocalPc(home, true), /UNSAFE_PATH_COMPONENT/);
    await assert.rejects(lstat(path.join(home, "Downloads")), { code: "ENOENT" });
    await assert.rejects(lstat(path.join(home, "KFM-site-recovery")), { code: "ENOENT" });
  });
});

test("existing permissive recovery folder blocks setup", async () => {
  await withHome(async (home) => {
    await mkdir(path.join(home, "KFM-site-recovery"), { mode: 0o755 });
    await assert.rejects(inspectLocalPc(home, true), /INSECURE_DIRECTORY_MODE/);
    await assert.rejects(lstat(path.join(home, "Downloads")), { code: "ENOENT" });
  });
});
