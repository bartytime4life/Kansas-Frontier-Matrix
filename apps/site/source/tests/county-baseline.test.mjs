import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";

// Compile the real module and its relative imports to data URLs, as the other layer tests do.
const modules = new Map();
async function moduleUrl(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) {
    js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  }
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  modules.set(file, url); return url;
}
const { createCountyBaseline, COUNTY_BASELINE_FRESH_MS, COUNTY_BASELINE_STALE_MS, COUNTY_BASELINE_ATTEMPT_TIMEOUTS_MS } = await import(await moduleUrl("app/county-baseline.ts"));

const counties = (count = 105) => JSON.stringify({ type: "FeatureCollection", features: Array.from({ length: count }, (_, index) => ({
  type: "Feature", geometry: { type: "Polygon", coordinates: [[[-98, 38], [-97, 38], [-97, 39], [-98, 38]]] },
  properties: { GEOID: `20${String(index * 2 + 1).padStart(3, "0")}`, NAME: `County ${index}`, BASENAME: `County ${index}`, AREALAND: 2589988110, AREAWATER: 0, POP100: 5000, HU100: 2000 },
})) });
/** A Census stand-in: each entry in `plan` is one attempt, either a body to return or an Error to throw. */
function census(plan) {
  const calls = [];
  const fetcher = async (url, limit, options) => {
    calls.push({ url, timeoutMs: options?.timeoutMs });
    const next = plan.length > 1 ? plan.shift() : plan[0];
    if (next instanceof Error) throw next;
    return { text: () => next };
  };
  return { fetcher, calls };
}
const hung = () => new Error("This operation was aborted");

test("one good answer serves a day of requests without asking Census again", async () => {
  let time = 1_000;
  const { fetcher, calls } = census([counties()]);
  const baseline = createCountyBaseline(fetcher, () => time);
  const first = await baseline("2020");
  assert.equal(first.data.features.length, 105);
  assert.equal(calls.length, 1); assert.equal(calls[0].timeoutMs, 7_000);
  assert.match(calls[0].url, /tigerWMS_Census2020\/MapServer\/82\/query/);
  time += COUNTY_BASELINE_FRESH_MS - 1;
  const again = await baseline("2020");
  assert.equal(again, first, "the same official answer, with its original retrieval time");
  assert.equal(calls.length, 1);
  time += 1;
  await baseline("2020");
  assert.equal(calls.length, 2, "after a day it is read again");
});

test("a request Census leaves hanging is tried once more, inside the old 18-second allowance", async () => {
  const { fetcher, calls } = census([hung(), counties()]);
  const result = await createCountyBaseline(fetcher)("2020");
  assert.equal(result.data.features.length, 105);
  assert.deepEqual(calls.map(call => call.timeoutMs), [7_000, 11_000]);
  assert.deepEqual([...COUNTY_BASELINE_ATTEMPT_TIMEOUTS_MS], [7_000, 11_000]);
  assert.equal(COUNTY_BASELINE_ATTEMPT_TIMEOUTS_MS.reduce((sum, ms) => sum + ms, 0), 18_000);
});

test("two failures are reported, never papered over, and the next request tries again", async () => {
  const plan = [hung(), new Error("Source unavailable (HTTP 503)."), counties()];
  const { fetcher, calls } = census(plan);
  const baseline = createCountyBaseline(fetcher);
  await assert.rejects(baseline("2020"), /Source unavailable \(HTTP 503\)\./);
  assert.equal(calls.length, 2);
  assert.equal((await baseline("2020")).data.features.length, 105, "a failure is not remembered");
  assert.equal(calls.length, 3);
});

test("an incomplete answer is refused on both attempts", async () => {
  const { fetcher, calls } = census([counties(104)]);
  await assert.rejects(createCountyBaseline(fetcher)("2020"), /Census did not return all 105 Kansas counties\./);
  assert.equal(calls.length, 2);
});

test("requests that arrive together share one read", async () => {
  const { fetcher, calls } = census([counties()]);
  const baseline = createCountyBaseline(fetcher);
  const [counties2020, forFema] = await Promise.all([baseline("2020"), baseline("2020")]);
  assert.equal(counties2020, forFema);
  assert.equal(calls.length, 1);
});

test("each edition is kept on its own", async () => {
  const { fetcher, calls } = census([counties()]);
  const baseline = createCountyBaseline(fetcher);
  const [a, b] = [await baseline("2020"), await baseline("2010")];
  assert.equal(a.edition, "2020"); assert.equal(b.edition, "2010");
  assert.match(calls[1].url, /tigerWMS_Census2010\/MapServer\/100\/query/);
  await baseline("2010"); await baseline("2020");
  assert.equal(calls.length, 2);
});

test("when the day is up and Census is unreachable, the kept answer serves one more day and then the failure shows", async () => {
  let time = 0;
  const plan = [counties(), hung()];
  const { fetcher, calls } = census(plan);
  const baseline = createCountyBaseline(fetcher, () => time);
  const first = await baseline("2020");
  time = COUNTY_BASELINE_FRESH_MS + 5;
  assert.equal(await baseline("2020"), first, "inside the stale window the kept answer is served");
  assert.equal(calls.length, 3, "after two fresh attempts");
  time = COUNTY_BASELINE_STALE_MS - 1;
  assert.equal(await baseline("2020"), first);
  time = COUNTY_BASELINE_STALE_MS;
  await assert.rejects(baseline("2020"), /This operation was aborted/);
  assert.equal(COUNTY_BASELINE_STALE_MS, 2 * COUNTY_BASELINE_FRESH_MS);
});

test("the windows match what the county feed already tells caches", async () => {
  const route = await readFile("app/api/live-context/route.ts", "utf8");
  assert.match(route, /"census-counties": 86_400/);
  assert.match(route, /s-maxage=\$\{cacheSeconds\[feed\]\}, stale-while-revalidate=\$\{cacheSeconds\[feed\]\}/);
  assert.equal(COUNTY_BASELINE_FRESH_MS, 86_400_000);
});
