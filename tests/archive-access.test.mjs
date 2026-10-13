import assert from "node:assert/strict";
import { chmodSync, mkdtempSync, rmSync, symlinkSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import test from "node:test";
import { readArchiveAccess } from "../scripts/archive-access.mjs";
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
