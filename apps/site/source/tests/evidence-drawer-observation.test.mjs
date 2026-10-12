import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/evidence-drawer-observation.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  fileName: "evidence-drawer-observation.ts",
}).outputText;
const { riverDrawerObservation } = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

const stationId = "USGS-06864500";
const bundle = {
  state: "ready", truncated: false, retrievedAt: "2026-09-23T21:50:00Z",
  stations: [{ stationId, name: "Smoky Hill River at Ellsworth, KS" }],
  observations: [{ stationId, observedAt: "2026-09-23T21:45:00Z", value: 120 }],
};
const frame = (value, missing = false) => ({ features: [{ properties: {
  stationId, value, missing, displayValue: value === null ? "No observation in tolerance" : `${value} ft3/s`,
  observedAt: missing ? null : "2026-09-23T21:45:00Z", approvalStatus: "Provisional",
  qualifiers: ["P"], trend: "steady", lastModified: null, ageMinutes: 5,
} }] });

test("selected gauge follows the current frame and retains source clocks", () => {
  const loaded = riverDrawerObservation(stationId, bundle, frame(120), "2026-09-23T21:50:00Z", "ready");
  assert.equal(loaded.status, "observation");
  assert.equal(loaded.displayValue, "120 ft3/s");
  assert.equal(loaded.retrievedAt, bundle.retrievedAt);
  assert.equal(loaded.sourceUrl, "https://waterdata.usgs.gov/monitoring-location/06864500/");

  const gap = riverDrawerObservation(stationId, bundle, frame(null, true), "2026-09-23T22:00:00Z", "ready");
  assert.equal(gap.status, "gap");
  assert.equal(gap.displayValue, null, "the earlier reading must not survive an empty frame");
  assert.equal(gap.observedAt, null);
});

test("source error marks a prior response stale and an unknown station cannot inherit another reading", () => {
  const stale = riverDrawerObservation(stationId, bundle, frame(120), "2026-09-23T21:50:00Z", "error");
  assert.equal(stale.status, "stale");
  assert.equal(stale.observedAt, "2026-09-23T21:45:00Z");
  const unavailable = riverDrawerObservation(stationId, null, null, null, "error");
  assert.equal(unavailable.status, "error");
  assert.equal(unavailable.displayValue, null);
  const unknown = riverDrawerObservation("USGS-06864501", bundle, frame(120), "2026-09-23T21:50:00Z", "ready");
  assert.equal(unknown.status, "gap");
  assert.equal(unknown.value, null);
  assert.equal(riverDrawerObservation("https://other.test", bundle, frame(120), null, "ready"), null);
});
