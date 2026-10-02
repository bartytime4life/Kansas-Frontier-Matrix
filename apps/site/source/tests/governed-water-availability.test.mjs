import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/governed-water-availability.ts", import.meta.url), "utf8");
const compiled = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const { waterBrowserStateForResponse, waterBrowserLabel } = await import(
  `data:text/javascript;base64,${Buffer.from(compiled).toString("base64")}`
);

test("water browser status distinguishes absent release from failed access", () => {
  const noRelease = { envelope: { outcome: "ABSTAIN", reason_code: "NO_APPROVED_SNAPSHOT" } };
  const storageDown = { envelope: { outcome: "ERROR", reason_code: "RELEASE_STORE_UNAVAILABLE" } };
  assert.equal(waterBrowserStateForResponse(noRelease, true), "no-release");
  assert.equal(waterBrowserLabel("no-release"), "No reviewed release active");
  assert.equal(waterBrowserStateForResponse(storageDown, false), "unavailable");
  assert.equal(waterBrowserLabel("unavailable"), "Unavailable");
  assert.equal(waterBrowserStateForResponse(null, true), "unavailable");
});

test("water browser status requires a usable answer before reporting received", () => {
  const answer = { envelope: { outcome: "ANSWER" }, data: { stations: [], observations: [] } };
  assert.equal(waterBrowserStateForResponse(answer, true), "received");
  assert.equal(waterBrowserStateForResponse({ ...answer, data: {} }, true), "withheld");
  assert.equal(waterBrowserStateForResponse(answer, false), "unavailable");
  assert.equal(waterBrowserLabel("withheld"), "Withheld");
});
