import assert from "node:assert/strict";
import "./cloudflare-register.mjs";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const modules = new Map();
async function moduleUrl(relative) {
  if (modules.has(relative)) return modules.get(relative);
  let source = await readFile(new URL(relative, import.meta.url), "utf8");
  if (relative.includes("/api/event-atlas/") && !relative.endsWith("upstream.ts")) {
    source = source.replaceAll('"../../../event-atlas"', JSON.stringify(await moduleUrl("../app/event-atlas.ts")));
    source = source.replaceAll('"../../../nexrad-storms"', JSON.stringify(await moduleUrl("../app/nexrad-storms.ts")));
    source = source.replaceAll('"../upstream"', JSON.stringify(await moduleUrl("../app/api/event-atlas/upstream.ts")));
  }
  const code = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 }, fileName: relative }).outputText;
  const url = `data:text/javascript;base64,${Buffer.from(code).toString("base64")}`;
  modules.set(relative, url); return url;
}
const storms = await import(await moduleUrl("../app/nexrad-storms.ts"));
const fixture = async (key) => new Uint8Array(await readFile(new URL(`./fixtures/nexrad/${key.toLowerCase()}`, import.meta.url)));
const NST = "ICT_NST_2024_05_19_23_16_04", NMD = "ICT_NMD_2024_05_19_23_16_04";
const listing = (keys) => `<?xml version="1.0"?><ListBucketResult>${keys.map(([key, size]) => `<Contents><Key>${key}</Key><Size>${size}</Size></Contents>`).join("")}<IsTruncated>false</IsTruncated></ListBucketResult>`;

test("storm-tracking product decodes every cell with tracks, motion and exact volume time", async () => {
  const parsed = storms.parseStormProduct(await fixture(NST), NST);
  assert.equal(parsed.volumeTime, "2024-05-19T23:16:04.000Z");
  assert.equal(parsed.cells.length, 34);
  const cell = parsed.cells.find((item) => item.stormId === "X6");
  assert.deepEqual(cell.position, [-97.829, 38.638]);
  assert.equal(cell.past.length, 5); assert.equal(cell.forecast.length, 2);
  assert.equal(cell.motion.toward, "NNE");
  // A busy scan lists 34 of 38 cells in text; the graphic block supplies the rest.
  assert.equal(storms.parseStormProduct(await fixture("DDC_NST_2024_05_19_22_03_21"), "DDC_NST_2024_05_19_22_03_21").cells.length, 38);
});

test("rotation product keeps the algorithm's TVS flag and empty scans stay empty", async () => {
  const parsed = storms.parseStormProduct(await fixture(NMD), NMD);
  assert.equal(parsed.rotations.length, 19);
  assert.ok(parsed.rotations.some((item) => item.rotationClass === "tornado_signature" && item.tvs));
  assert.ok(parsed.rotations.every((item) => item.tvs === (item.rotationClass === "tornado_signature")));
  assert.deepEqual(storms.parseStormProduct(await fixture("ICT_NMD_2024_05_06_18_47_19"), "ICT_NMD_2024_05_06_18_47_19").rotations, []);
});

test("identity, time, truncation and key scope fail closed", async () => {
  const raw = await fixture(NST);
  for (const [bytes, key] of [[raw, "DDC_NST_2024_05_19_23_16_04"], [raw, "ICT_NST_2024_05_19_23_16_05"], [raw, NMD], [raw.subarray(0, raw.length - 40), NST], [new Uint8Array([120, ...raw]), NST]]) {
    assert.throws(() => storms.parseStormProduct(bytes, key));
  }
  for (const key of ["../x", "ICT_N0B_2024_05_19_23_16_04", "KICT_NST_2024_05_19_23_16_04", `${NST}?a=1`]) assert.throws(() => storms.stormObjectUrl(key));
  assert.throws(() => storms.parseStormListing(listing([["ICT_NST_2024_05_20_00_01_00", 10]]), "ICT", "NST", "2024-05-19"));
  assert.throws(() => storms.parseStormListing(listing([[NST, 10]]).replace("false", "true"), "ICT", "NST", "2024-05-19"));
  assert.throws(() => storms.parseStormListing("<!DOCTYPE x><ListBucketResult/>", "ICT", "NST", "2024-05-19"));
});

test("frame selection never carries a scan forward past the 12-minute window", () => {
  const rows = storms.parseStormListing(listing([["ICT_NST_2024_05_19_23_05_32", 10], [NST, 10]]), "ICT", "NST", "2024-05-19");
  assert.equal(storms.latestStormVolume(rows, "2024-05-19T23:20:00.000Z").key, NST);
  assert.equal(storms.latestStormVolume(rows, "2024-05-19T23:10:00.000Z").key, "ICT_NST_2024_05_19_23_05_32");
  assert.equal(storms.latestStormVolume(rows, "2024-05-19T23:40:00.000Z"), null);
  assert.equal(storms.latestStormVolume(rows, "2024-05-19T23:00:00.000Z"), null);
});

test("display frame colors cells by rotation and draws a storm seen by two radars once", async () => {
  const cells = storms.parseStormProduct(await fixture(NST), NST), rotations = storms.parseStormProduct(await fixture(NMD), NMD);
  const shifted = { ...cells, radar: "DDC", cells: cells.cells.map((cell) => ({ ...cell, radar: "DDC", rangeKm: cell.rangeKm + 50 })) };
  const frame = storms.stormFeatures([cells, rotations, shifted], "2024-05-19T23:20:00.000Z");
  const points = frame.features.filter((feature) => feature.properties.kind === "cell");
  assert.equal(points.length, 34);
  assert.ok(points.every((feature) => feature.properties.radar === "KICT" && feature.properties.alsoSeenBy === "Dodge City"));
  const k7 = points.find((feature) => feature.properties.stormId === "K7");
  assert.equal(k7.properties.rotation, "tornado_signature");
  assert.equal(k7.properties.ageMinutes, 4);
  assert.match(storms.describeStormFeature(k7.properties), /not a confirmed tornado/);
});

test("storm route reads only allowlisted archive bytes, caches nothing to disk and reports per-radar gaps", async () => {
  const { GET } = await import(await moduleUrl("../app/api/event-atlas/storms/route.ts"));
  const previous = globalThis.fetch, seen = [];
  const nst = await fixture(NST), nmd = await fixture(NMD);
  globalThis.fetch = async (url) => {
    const value = String(url); seen.push(value);
    assert.ok(value.startsWith("https://unidata-nexrad-level3.s3.amazonaws.com/"));
    if (value.includes("prefix=ICT_NST_2024_05_19_")) return new Response(listing([[NST, nst.length]]));
    if (value.includes("prefix=ICT_NMD_2024_05_19_")) return new Response(listing([[NMD, nmd.length]]));
    if (value.includes("prefix=TWX_")) return new Response("down", { status: 503 });
    if (value.includes("?list-type=2")) return new Response(listing([]));
    if (value.endsWith(NST)) return new Response(nst);
    if (value.endsWith(NMD)) return new Response(nmd);
    return new Response("unexpected", { status: 404 });
  };
  try {
    const response = await GET(new Request("https://app.test/api/event-atlas/storms?time=2024-05-19T23%3A20%3A00.000Z"));
    assert.equal(response.status, 200);
    const body = await response.json();
    assert.equal(body.format, "kfm-nexrad-storms-v1");
    assert.equal(body.counts.cells, 34);
    assert.ok(body.counts.tornadoSignatures > 0);
    assert.deepEqual(body.radars.map((radar) => radar.status), ["ok", "no-scan", "no-scan", "unavailable"]);
    const availability = await (await GET(new Request("https://app.test/api/event-atlas/storms?start=2024-05-19T22%3A00%3A00.000Z&end=2024-05-20T00%3A00%3A00.000Z"))).json();
    assert.deepEqual(availability.radars[0].times, ["2024-05-19T23:16:04.000Z"]);
    for (const query of ["time=latest", "time=2019-12-31T00%3A00%3A00Z", "time=2099-01-01T00%3A00%3A00Z", "start=2024-05-19T00%3A00%3A00Z&end=2024-05-21T00%3A00%3A00Z", "time=2024-05-19T23%3A20%3A00Z&url=https://evil.test"]) {
      assert.equal((await GET(new Request(`https://app.test/api/event-atlas/storms?${query}`))).status, 400, query);
    }
  } finally { globalThis.fetch = previous; }
});

test("a failed rotation product keeps that radar's storm cells", async () => {
  // A fresh module instance so the earlier test's in-memory cache is not reused.
  const cached = await moduleUrl("../app/api/event-atlas/storms/route.ts");
  const fresh = `data:text/javascript;base64,${Buffer.from(Buffer.from(cached.split(",")[1], "base64").toString() + "\n// fresh cache").toString("base64")}`;
  const { GET } = await import(fresh);
  const previous = globalThis.fetch;
  const nst = await fixture(NST), nmd = await fixture(NMD);
  globalThis.fetch = async (url) => {
    const value = String(url);
    if (value.includes("prefix=ICT_NST_2024_05_19_")) return new Response(listing([[NST, nst.length]]));
    if (value.includes("prefix=ICT_NMD_2024_05_19_")) return new Response(listing([[NMD, nmd.length]]));
    if (value.includes("?list-type=2")) return new Response(listing([]));
    if (value.endsWith(NMD)) return new Response("down", { status: 503 });
    if (value.endsWith(NST)) return new Response(nst);
    return new Response("unexpected", { status: 404 });
  };
  try {
    const body = await (await GET(new Request("https://app.test/api/event-atlas/storms?time=2024-05-19T23%3A20%3A00.000Z"))).json();
    assert.equal(body.radars[0].status, "ok");
    assert.match(body.radars[0].message, /rotation unavailable/i);
    assert.equal(body.counts.cells, 34);
    assert.equal(body.counts.rotations, 0);
  } finally { globalThis.fetch = previous; }
});
