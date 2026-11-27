import assert from "node:assert/strict";
import test from "node:test";
import { forageScenario, pumpingScenario } from "../app/farm-season/scenario-model.mjs";

const pump = { acres: "120", depth: "12", head: "250", efficiency: "70", rate: ".12" };
const forage = { acres: "100", production: "2000", utilization: "30", headCount: "50", intake: "24", days: "60" };

test("pumping converts applied inches across acres to acre-feet and prices electrical input", () => {
  const estimate = pumpingScenario(pump);
  assert.equal(estimate.acreFeet, 120);
  assert.equal(estimate.energyKwh.toFixed(2), "43890.38");
  assert.equal(estimate.energyCost.toFixed(2), "5266.85");
  assert.equal(estimate.costPerAcre.toFixed(2), "43.89");

  const deeperWell = pumpingScenario({ ...pump, head: "500" });
  assert.equal(deeperWell.energyCost, 2 * estimate.energyCost);
});

test("pumping distinguishes a zero-valued scenario from missing or unsupported inputs", () => {
  assert.deepEqual(pumpingScenario({ ...pump, depth: "0", head: "0" }), {
    acreFeet: 0, energyKwh: 0, energyCost: 0, costPerAcre: 0,
  });
  assert.equal(pumpingScenario({ ...pump, rate: "0" }).energyCost, 0);
  for (const invalid of [{ acres: "" }, { depth: "-1" }, { head: "0" }, { rate: "Infinity" },
    { head: "1e2" }, { efficiency: "0" }, { efficiency: "100.01" }]) {
    assert.equal(pumpingScenario({ ...pump, ...invalid }), null);
  }
});

test("forage compares usable dry matter with total demand and identifies a deficit", () => {
  assert.deepEqual(forageScenario(forage), {
    usablePounds: 60000, demandPounds: 72000, balancePounds: -12000, daysOfSupply: 50,
  });
  assert.equal(forageScenario({ ...forage, days: "50" }).balancePounds, 0);
  assert.equal(forageScenario({ ...forage, days: "40" }).balancePounds, 12000);
});

test("forage keeps zero production and rejects missing values or zero intake or herd size", () => {
  assert.deepEqual(forageScenario({ ...forage, production: "0" }), {
    usablePounds: 0, demandPounds: 72000, balancePounds: -72000, daysOfSupply: 0,
  });
  for (const invalid of [{ headCount: "0" }, { headCount: "50.5" }, { days: "1.5" },
    { intake: "0" }, { utilization: "101" }, { production: "" }]) {
    assert.equal(forageScenario({ ...forage, ...invalid }), null);
  }
});

test("built farm planner is reachable from Agriculture & soils and keeps sources beside local tools", async () => {
  const { default: handler } = await import("../dist/server/index.js");
  const topics = await handler(new Request("https://kansasfrontiermatrix.com/topics"));
  assert.equal(topics.status, 200);
  assert.match(await topics.text(), /href="\/farm-season"[^>]*>Farm season planner/);

  const page = await handler(new Request("https://kansasfrontiermatrix.com/farm-season"));
  assert.equal(page.status, 200);
  assert.match(page.headers.get("content-type"), /text\/html/);
  const html = await page.text();
  for (const label of ["Estimate pumping cost", "Estimate forage balance", "Kansas seasonal calendar",
    "KGS WIZARD", "USDA Climate Hubs Grass-Cast", "NOAA CPC seasonal outlooks", "Kansas frost chart"]) {
    assert.ok(html.includes(label), label);
  }
  assert.match(html, /href="https:\/\/kansasfrontiermatrix\.com\/farm-season"/);
});
