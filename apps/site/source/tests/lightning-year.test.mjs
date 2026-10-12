import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

async function moduleFor(file) {
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  if (js.includes('from "./lightning-archive"')) js = js.replace('from "./lightning-archive"', `from ${JSON.stringify(await archiveModule)}`);
  return `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
}
const archiveModule = moduleFor("app/lightning-archive.ts");
const year = await import(await moduleFor("app/lightning-year.ts"));
const archive = await import(await archiveModule);
const now = Date.parse("2026-10-04T05:21:00Z");

test("year playback visits every leap-year hour exactly once before looping", () => {
  const range = year.lightningYearRange(2024, now), visited = new Set();
  assert.equal(range.hours, 366 * 24); assert.equal(range.partial, false);
  let cursor = range.start;
  for (let i = 0; i < range.hours; i++) {
    assert.equal(visited.has(cursor), false); visited.add(cursor);
    const query = year.lightningYearQuery(cursor);
    const interval = archive.archiveInterval(query, now);
    assert.equal(interval.start, cursor); assert.equal(interval.end, cursor + year.LIGHTNING_HOUR);
    cursor = year.nextLightningYearHour(cursor, range, true);
  }
  assert.equal(cursor, range.start);
  assert.equal(visited.has(Date.parse("2024-02-29T23:00:00Z")), true);
  assert.equal(year.nextLightningYearHour(range.end - year.LIGHTNING_HOUR, range, false), null);
});

test("partial archive years exclude pre-coverage and incomplete future hours", () => {
  const first = year.lightningYearRange(2017, now), current = year.lightningYearRange(2026, now);
  assert.equal(first.start, Date.parse("2017-07-05T00:00:00Z")); assert.equal(first.partial, true);
  assert.equal(current.end, Date.parse("2026-10-04T05:00:00Z")); assert.equal(current.partial, true);
  const last = year.lightningYearQuery(current.end - year.LIGHTNING_HOUR);
  assert.deepEqual(last, { day: "2026-10-04", hour: 4, minute: 0, duration: 60 });
  assert.equal(year.lightningYearHour(Date.parse("2017-01-01T00:00:00Z"), first), first.start);
  assert.equal(year.lightningYearHour(Date.parse("2026-12-31T00:00:00Z"), current), current.end - year.LIGHTNING_HOUR);
  for (const invalid of [2016, 2027, NaN, 2024.5]) assert.throws(() => year.lightningYearRange(invalid, now));
  assert.throws(() => year.lightningYearRange(2027, Date.parse("2027-01-01T00:15:00Z")));
});

test("calendar jumps stay hour-aligned and preserve real satellite transitions", () => {
  const range = year.lightningYearRange(2025, now);
  const before = year.lightningYearHour(Date.parse("2025-04-04T14:39:01Z"), range);
  const after = year.nextLightningYearHour(before, range, true);
  assert.equal(archive.archiveLocation(before).satellite, 16); assert.equal(archive.archiveLocation(after).satellite, 19);
  assert.throws(() => year.lightningYearQuery(before + 1));
  assert.throws(() => year.nextLightningYearHour(range.end, range, true));
  assert.throws(() => year.lightningYearHour(NaN, range));
});
