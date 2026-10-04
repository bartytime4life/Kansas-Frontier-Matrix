import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/governed-water-availability.ts", import.meta.url), "utf8");
const compiled = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const { waterBrowserStateForResponse, waterBrowserLabel, waterEvidenceMatchesSelection, waterExportMatchesSelection } = await import(
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

const stationId = "USGS-06892518";
const fullLayers = JSON.parse(await readFile(new URL("./fixtures/governed-water/layers.json", import.meta.url), "utf8"));
const fullEvidence = JSON.parse(await readFile(new URL("./fixtures/governed-water/evidence.json", import.meta.url), "utf8"));
function selectedResponses() {
  const layers = structuredClone(fullLayers), evidence = structuredClone(fullEvidence);
  layers.data.stations = layers.data.stations.filter(station => station.id === stationId);
  layers.data.observations = layers.data.observations.filter(observation => observation.station_id === stationId);
  evidence.data.entries = evidence.data.entries.filter(entry => entry.station_id === stationId);
  return { layers, evidence };
}

test("selected-station evidence and export accept a matching reviewed projection", () => {
  const { layers, evidence } = selectedResponses();
  assert.equal(waterEvidenceMatchesSelection(fullLayers, evidence, stationId), true);
  assert.equal(waterExportMatchesSelection(layers, evidence, stationId), true);
});

test("selected-station evidence withholds broad, mismatched, or malformed responses", () => {
  const cases = [
    ({ evidence }) => evidence.data.entries.push(structuredClone(fullEvidence.data.entries[1])),
    ({ evidence }) => { evidence.data.entries[0].station_id = "USGS-07156900"; },
    ({ evidence }) => { evidence.data.entries[0].bundle.evidence_refs[1].ref = "kfm:evidence:other"; },
    ({ evidence }) => { evidence.data.released_at = "2026-09-30T18:46:00Z"; },
    ({ evidence }) => { evidence.data.entries = null; },
    ({ layers }) => { layers.data.correction_state = "WITHDRAWN"; },
  ];
  for (const mutate of cases) {
    const pair = selectedResponses(); mutate(pair);
    assert.equal(waterEvidenceMatchesSelection(pair.layers, pair.evidence, stationId), false);
  }
});

test("selected-station export withholds another station even in the same package", () => {
  const cases = [
    ({ layers }) => layers.data.stations.push(structuredClone(fullLayers.data.stations[1])),
    ({ layers }) => layers.data.observations.push(structuredClone(fullLayers.data.observations[1])),
    ({ layers }) => { layers.data.stations[0].id = "USGS-07156900"; },
    ({ layers }) => { layers.data.observations = null; },
    ({ evidence }) => { evidence.data.package_id = "sha256:changed"; },
  ];
  for (const mutate of cases) {
    const pair = selectedResponses(); mutate(pair);
    assert.equal(waterExportMatchesSelection(pair.layers, pair.evidence, stationId), false);
  }
});
