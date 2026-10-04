import assert from "node:assert/strict";
import { test } from "node:test";
import { mkdtemp, realpath, rm, symlink, writeFile, mkdir } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import { readPackageObject } from "../scripts/earth-engine/secure-local-read.mjs";

test("local restore reads the opened package object within its byte limit", async () => {
  const temp = await mkdtemp(path.join(tmpdir(), "kfm-package-read-"));
  try {
    const root = path.join(temp, "package");
    await mkdir(root);
    await writeFile(path.join(root, "tile.png"), Buffer.from("exact tile"));
    const canonical = await realpath(root);
    assert.deepEqual(await readPackageObject(canonical, "tile.png", 10), Buffer.from("exact tile"));
    await assert.rejects(readPackageObject(canonical, "tile.png", 9), /size/);
    await assert.rejects(readPackageObject(canonical, "../outside.txt", 100), /escapes root/);
  } finally { await rm(temp, { recursive: true, force: true }); }
});

test("local restore rejects leaf and ancestor symlinks outside the package", async () => {
  const temp = await mkdtemp(path.join(tmpdir(), "kfm-package-link-"));
  try {
    const root = path.join(temp, "package"), outside = path.join(temp, "outside");
    await mkdir(root); await mkdir(outside);
    await writeFile(path.join(outside, "private.txt"), "outside bytes");
    await symlink(path.join(outside, "private.txt"), path.join(root, "leaf.txt"));
    await symlink(outside, path.join(root, "ancestor"));
    const canonical = await realpath(root);
    await assert.rejects(readPackageObject(canonical, "leaf.txt", 100));
    await assert.rejects(readPackageObject(canonical, "ancestor/private.txt", 100), /escapes package root/);
  } finally { await rm(temp, { recursive: true, force: true }); }
});
