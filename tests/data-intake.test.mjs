import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import ts from "typescript";
import test from "node:test";
const cache = new Map();
async function moduleUrl(file) {
  file = path.resolve(file); if (cache.has(file)) return cache.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`; cache.set(file,url); return url;
}
const intake = await import(await moduleUrl("app/data-intake.ts"));
const daily = await import(await moduleUrl("app/daily-baseline.ts"));
const upstream = await import(await moduleUrl("app/api/event-atlas/upstream.ts"));
test("intake rejects malformed dates, credential URLs, duplicate file paths and unsupported payloads", () => {
  const fields = { title: "A real source", sourceId: "general", sourceUrl: "https://example.gov/data", description: "Historical public county records", license: "Unknown", sensitivity: "unknown", startDate: "1900-01-01", endDate: "1900-12-31" };
  assert.equal(intake.validateSubmission(fields).startDate, "1900-01-01");
  assert.throws(() => intake.validateSubmission({...fields,startDate:"1900-02-29"}));
  assert.throws(() => intake.validateSubmission({...fields,sourceUrl:"https://user:secret@example.gov"}));
  assert.throws(() => intake.validateUpload("../../data.csv",50));
  assert.throws(() => intake.validateUpload("script.js",50));
  assert.throws(() => intake.validateUpload("data.csv",intake.MAX_UPLOAD_BYTES+1));
  assert.throws(() => intake.validateReview({...fields,status:"submitted"},"accepted","Checked provider terms and data structure."));
});
test("daily baseline advances across midnight and year boundaries without replacing historical stacks", () => {
  assert.equal(daily.currentDayStart(new Date("2026-12-31T23:59:00Z")),"2026-12-31T00:00");
  assert.equal(daily.currentDayStart(new Date("2027-01-01T00:01:00Z")),"2027-01-01T00:00");
  assert.deepEqual(daily.BASELINE_STACKS.overview,["census-counties","usgs-streamflow","usgs-3dhp-hydrography"]);
  assert.equal(daily.BASELINE_STACKS.history,undefined);
});
test("provider redirects are rejected without using the redirect mode unsupported by Workers", async () => {
  const original = globalThis.fetch; let calls = 0;
  globalThis.fetch = async (_url, init) => { calls++; assert.equal(init.redirect,"manual"); return new Response(null,{status:302,headers:{Location:"https://untrusted.test/data"}}); };
  try { await assert.rejects(upstream.boundedFetch("https://tigerweb.geo.census.gov/query",1000),/HTTP 302/); assert.equal(calls,1); }
  finally { globalThis.fetch = original; }
});
