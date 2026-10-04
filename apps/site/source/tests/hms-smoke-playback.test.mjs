import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";
async function load(file) {
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await load(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  return `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
}
const { HmsFrameCache, hmsValidDay, hmsAdvance, HMS_FIRST_DAY } = await import(await load("app/hms-smoke-playback.ts"));
const { localImageryReadAllowed } = await import(await load("app/earth-engine-local-read.ts"));
const frame = day => ({ retrievedAt: "2026-10-02T12:00:00Z", feed: "noaa-hms-smoke", state: "empty", smokeCoverage: { day, availableDays: [day], missingDays: [] }, data: { type: "FeatureCollection", features: [] }, featureCount: 0 });
test("HMS archive starts at the connected KML publication and uses exact UTC days", () => {
  assert.equal(HMS_FIRST_DAY, "2005-08-05"); assert.equal(hmsValidDay("2005-08-04"), false);
  assert.equal(hmsValidDay("2024-02-30"), false); assert.equal(hmsValidDay("2099-01-01"), false);
  assert.equal(hmsAdvance("2024-02-28", 1), "2024-02-29"); assert.equal(hmsAdvance("2024-02-29", 1), "2024-03-01");
});
test("HMS lazy frame cache is bounded and does not relabel missing days as empty", async () => {
  let calls = 0;
  const cache = new HmsFrameCache(async url => { calls++; return Response.json(frame(new URL(url, "https://local.test").searchParams.get("day"))); });
  const signal = new AbortController().signal;
  for (const day of ["2005-08-05", "2005-08-06", "2005-08-07", "2005-08-08"]) await cache.get(day, signal);
  assert.equal(cache.size, 3); assert.equal(calls, 4);
  await cache.get("2005-08-08", signal); assert.equal(calls, 4);
  await cache.get("2005-08-05", signal); assert.equal(calls, 5);
  const wrong = new HmsFrameCache(async () => Response.json(frame("2005-08-05")));
  await assert.rejects(wrong.get("2005-08-06", signal)); assert.equal(wrong.size, 0);
  const gap = new HmsFrameCache(async () => Response.json({ ...frame("2005-08-06"), smokeCoverage: { day:"2005-08-06", availableDays:["2005-08-05"], missingDays:["2005-08-06"] } }));
  await assert.rejects(gap.get("2005-08-06", signal)); assert.equal(gap.size, 0);
});
test("HMS cancellation cannot populate the next frame", async () => {
  const abort = new AbortController();
  const cache = new HmsFrameCache(async () => { abort.abort(); return Response.json(frame("2005-08-05")); });
  await assert.rejects(cache.get("2005-08-05", abort.signal)); assert.equal(cache.size, 0);
});
test("local imagery read mode is explicit, exact-origin, read-only and denies cross-site requests", () => {
  const origin = "http://127.0.0.1:4173", route = "/api/earth-engine-context/catalog";
  assert.equal(localImageryReadAllowed(new Request(origin+route), origin), true);
  assert.equal(localImageryReadAllowed(new Request(origin+route), undefined), false);
  for (const host of ["https://site.example", "http://127.0.0.1:4174", "http://localhost:4173", "http://127.0.0.1.evil.test:4173"]) assert.equal(localImageryReadAllowed(new Request(host+route), origin), false);
  for (const suffix of ["/stage", "/activate", "/install"]) assert.equal(localImageryReadAllowed(new Request(origin+"/api/earth-engine-context"+suffix), origin), false);
  assert.equal(localImageryReadAllowed(new Request(origin+route,{method:"POST"}),origin),false);
  assert.equal(localImageryReadAllowed(new Request(origin+route,{headers:{Origin:"https://evil.test"}}),origin),false);
  assert.equal(localImageryReadAllowed(new Request(origin+route,{headers:{"Sec-Fetch-Site":"cross-site"}}),origin),false);
});

test("fade uses opacity only and settles cancellation and renderer failures", async () => {
  const { hmsFade } = await import(await load("app/hms-smoke-playback.ts"));
  const savedRaf = globalThis.requestAnimationFrame, savedCancel = globalThis.cancelAnimationFrame;
  globalThis.requestAnimationFrame = callback => setTimeout(() => callback(performance.now() + 1000), 0);
  globalThis.cancelAnimationFrame = clearTimeout;
  try {
    const values = [];
    await hmsFade(1, 0, new AbortController().signal, value => values.push(value));
    assert.deepEqual(values, [0]);
    await assert.rejects(hmsFade(0, 1, new AbortController().signal, () => { throw new Error("style removed"); }), /style removed/);
    const controller = new AbortController();
    const pending = hmsFade(0, 1, controller.signal, () => assert.fail("aborted frame painted"));
    controller.abort(); await assert.rejects(pending, /Cancelled/);
  } finally { globalThis.requestAnimationFrame = savedRaf; globalThis.cancelAnimationFrame = savedCancel; }
});
