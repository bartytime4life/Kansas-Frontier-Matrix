import assert from "node:assert/strict";
import { chmodSync, lstatSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, symlinkSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import test from "node:test";
import { initializeArchiveAccess, readArchiveAccess } from "../scripts/archive-access.mjs";
import { checkDailyArchive } from "../scripts/capture-daily-archive.mjs";
test("archive capabilities require a private owned file and distinct bounded credentials",()=>{
 const root=mkdtempSync(path.join(tmpdir(),"kfm-archive-access-"));const file=path.join(root,"access");const access={ownerToken:"o".repeat(43),workerToken:"w".repeat(43)};
 try {
  assert.equal(readArchiveAccess(file),null);
  writeFileSync(file,JSON.stringify(access),{mode:0o600});assert.deepEqual(readArchiveAccess(file),access);
  chmodSync(file,0o644);assert.throws(()=>readArchiveAccess(file),/UNSAFE/);chmodSync(file,0o600);
  symlinkSync(file,path.join(root,"link"));assert.throws(()=>readArchiveAccess(path.join(root,"link")),/UNSAFE/);
  for(const value of [null,{}, {...access,workerToken:access.ownerToken},{...access,workerToken:"short"},{...access,ownerToken:"x\n".repeat(43)}]) {writeFileSync(file,JSON.stringify(value));assert.throws(()=>readArchiveAccess(file),/INVALID/);}
  writeFileSync(file,"x".repeat(4097));assert.throws(()=>readArchiveAccess(file),/UNSAFE/);
 } finally {rmSync(root,{recursive:true,force:true});}
});

test("opt-in setup creates private credentials once and preserves files that require review", () => {
 const root = mkdtempSync(path.join(tmpdir(), "kfm-archive-initialize-"));
 const folder = path.join(root, ".config", "kfm");
 const file = path.join(folder, "daily-archive-access");
 try {
  assert.equal(initializeArchiveAccess(file), "initialized");
  assert.equal(lstatSync(folder).mode & 0o777, 0o700);
  assert.equal(lstatSync(file).mode & 0o777, 0o600);
  const access = readArchiveAccess(file);
  for (const value of Object.values(access)) assert.match(value, /^[A-Za-z0-9_-]{43}$/);
  assert.notEqual(access.ownerToken, access.workerToken);
  assert.equal(initializeArchiveAccess(file), "already-configured");
  assert.deepEqual(readArchiveAccess(file), access);
  assert.deepEqual(readdirSync(folder), ["daily-archive-access"]);
  writeFileSync(file, "invalid operator fixture");
  assert.throws(() => initializeArchiveAccess(file), /ARCHIVE_ACCESS_FILE_INVALID/);
  assert.equal(readFileSync(file, "utf8"), "invalid operator fixture");
  chmodSync(file, 0o644);
  assert.throws(() => initializeArchiveAccess(file), /ARCHIVE_ACCESS_FILE_UNSAFE/);
  chmodSync(folder, 0o722);
  assert.throws(() => initializeArchiveAccess(file), /ARCHIVE_ACCESS_DIRECTORY_UNSAFE/);
  mkdirSync(path.join(root, "missing"));
  symlinkSync(folder, path.join(root, "missing", "kfm"));
  assert.throws(() => initializeArchiveAccess(path.join(root, "missing", "kfm", "new")), /ARCHIVE_ACCESS_DIRECTORY_UNSAFE/);
 } finally { rmSync(root, { recursive: true, force: true }); }
});

test("archive readiness only reads the worker status and distinguishes rejection and unavailable storage", async () => {
 const origin = "http://127.0.0.1:4173";
 const worker = "w".repeat(43);
 const noTransport = () => assert.fail("request must be declined before transport");
 await assert.rejects(checkDailyArchive("https://evil.test", noTransport, worker), /UNSUPPORTED_ARCHIVE_ORIGIN/);
 await assert.rejects(checkDailyArchive(origin, noTransport), /ARCHIVE_WORKER_ACCESS_REQUIRED/);
 for (const paused of [false, true]) {
  const result = await checkDailyArchive(origin, async (url, options) => {
   assert.equal(url, origin + "/api/daily-archive?action=status");
   assert.equal(options.method, undefined);
   assert.equal(options.redirect, "error");
   assert.equal(options.headers.Authorization, `Bearer ${worker}`);
   return Response.json({ day: "2026-11-27", entries: [], storage: { paused, internal: "private fixture" } });
  }, worker);
  assert.deepEqual(result, { outcome: paused ? "paused" : "ready" });
 }
 for (const status of [401, 403]) {
  await assert.rejects(checkDailyArchive(origin, async () => new Response("private fixture", { status }), worker), { message: "ARCHIVE_WORKER_ACCESS_REJECTED" });
 }
 await assert.rejects(checkDailyArchive(origin, async () => new Response("private fixture", { status: 503 }), worker), { message: "ARCHIVE_UNAVAILABLE_HTTP_503" });
 await assert.rejects(checkDailyArchive(origin, async () => Response.json({ storage: { paused: false } }), worker), { message: "ARCHIVE_STATUS_INVALID" });
 await assert.rejects(checkDailyArchive(origin, async () => { throw new Error("private fixture"); }, worker), { message: "ARCHIVE_STATUS_REQUEST_FAILED" });
});
