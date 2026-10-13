import assert from "node:assert/strict";
import { test } from "node:test";
import { readFile } from "node:fs/promises";
import vm from "node:vm";
import ts from "typescript";
const code=ts.transpileModule(await readFile(new URL("../app/subsurface-worker.ts",import.meta.url),"utf8"),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
test("all worker requests return the publication hold without any source reads, including stale cached assets",()=>{
 const messages=[];let reads=0;const self={location:{origin:"https://kfm.invalid"},postMessage:m=>messages.push(m)};
 vm.runInNewContext(code,{self,fetch:()=>{reads++;throw new Error("Legacy assets must never be requested");}});
 for(const [id,kind] of ["prepare","search","probe","area"].entries()) {
  self.onmessage({origin:self.location.origin,data:{id,kind}});const result=messages.at(-1);
  assert.equal(result.id,id);assert.match(result.error,/withheld.*review/);assert.equal(result.columns.length,0);if(kind==="search")assert.equal(result.matches.length,0);else assert.equal("matches" in result,false);assert.equal(result.manifest.tiles.length,0);assert.equal(result.manifest.sources.length,0);
  if(kind==="prepare")assert.equal(result.prepared,true);
 }
 assert.equal(reads,0);
 self.onmessage({origin:"https://foreign.invalid",data:{id:9,kind:"area"}});assert.equal(messages.length,4);
});
