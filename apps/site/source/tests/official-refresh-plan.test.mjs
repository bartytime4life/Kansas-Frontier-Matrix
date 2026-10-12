import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/official-refresh-plan.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { planOfficialRefresh } = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

const sources = [
  { id: "census-counties", apiPath: "/api/live-context?feed=census-counties" },
  { id: "usgs-streamflow" },
  { id: "nws-radar" },
  { id: "noaa-lightning-density" },
  { id: "noaa-goes-geocolor" },
  { id: "noaa-nwps-gauges" },
  { id: "static-map" },
];
const selected = Object.fromEntries(sources.map(({ id }) => [id, true]));

test("historical frames cannot schedule current-only provider requests", () => {
  const plan = planOfficialRefresh(sources, selected, 2025, 2026, false);
  assert.deepEqual(plan, { feeds: [], radar: false, satellite: false, lightning: false, streamflow: false, hydrology: false, count: 0, reason: "historical" });
});

test("present refresh counts only actual request paths and respects archive selection", () => {
  const plan = planOfficialRefresh(sources, selected, 2026, 2026, true);
  assert.deepEqual(plan.feeds, ["census-counties"]);
  assert.equal(plan.count, 5);
  assert.equal(plan.streamflow, false);
  assert.equal(plan.radar, true);
  assert.equal(plan.satellite, true);
  assert.equal(plan.lightning, true);
  assert.equal(plan.hydrology, true);
  assert.deepEqual(planOfficialRefresh(sources, selected, 2026, 2026, false, { "census-counties": "2025-01-01" }).feeds, []);
  assert.equal(planOfficialRefresh(sources, {}, 2026, 2026, false).reason, "none");
});
