import assert from "node:assert/strict";
import test from "node:test";
import { readFile } from "node:fs/promises";
import ts from "typescript";

const urls = new Map();
const spaUrl = import.meta.resolve("sunrise-sunset-js");
const clippingUrl = new URL("../node_modules/polygon-clipping/dist/polygon-clipping.esm.js", import.meta.url).href;
async function moduleUrl(name) {
  if (urls.has(name)) return urls.get(name);
  let js = ts.transpileModule(await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8"), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  js = js
    .replaceAll('from "sunrise-sunset-js"', `from ${JSON.stringify(spaUrl)}`)
    .replaceAll('from "polygon-clipping"', `from ${JSON.stringify(clippingUrl)}`);
  for (const [, dependency] of [...js.matchAll(/from "\.\/([a-z-]+)"/g)]) js = js.replaceAll(`from "./${dependency}"`, `from "${await moduleUrl(dependency)}"`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  urls.set(name, url);
  return url;
}
const model = await import(await moduleUrl("workspace-model"));
const storage = await import(await moduleUrl("workspace-storage"));
const fire = await import(await moduleUrl("fire-report-analysis"));
const { LAYER_REGISTRY } = await import(await moduleUrl("explorer-data"));
const snapshot = {
  id: "snapshot-test", createdAt: "2026-09-09T00:00:00Z", area: { kind: "viewport", label: "Kansas" },
  camera: { center: [-98.38, 38.48], zoom: 5.4, pitch: 0, bearing: 0 }, representation: "2D", projection: "mercator", basemap: "standard",
  committedTime: { start: 2026, end: 2026, label: "2026", mode: "instant" },
  visibleLayers: [], selection: null, evidenceRefs: [], inspectableFeatureIds: [],
  inspectableRecordCount: 0, sourceBackedCount: 0, boundedCount: 0,
  policy: model.policyDecisionFromEvidenceState("MISSING_EVIDENCE"),
};

test("demonstration support never becomes a source-backed trust label", () => {
  for (const state of ["ANSWER", "CORRECTED"]) {
    assert.equal(model.trustStateFromEvidenceState(state), "Synthetic");
    assert.equal(model.trustStateFromEvidenceState(state, "observed"), "Site-local demo");
  }
  assert.equal(model.policyDecisionFromEvidenceState("DENIED_BY_POLICY").outcome, "DENY");
  assert.equal(model.policyDecisionFromEvidenceState("ERROR").outcome, "ERROR");
  assert.equal(model.policyDecisionFromEvidenceState("MISSING_EVIDENCE").outcome, "ABSTAIN");
});

test("empty domain registry yields a valid draft with no invented evidence", () => {
  assert.equal(LAYER_REGISTRY.length, 0);
  const report = model.createReportDraft(snapshot, []);
  assert.deepEqual(report.includedEvidenceIds, []);
  assert.equal(report.status, "DRAFT");
  assert.equal(storage.validReportDraft(JSON.parse(JSON.stringify(report))), true);
  assert.equal(storage.validReportDraft({ ...report, status: "PUBLISHED" }), false);
});

test("a new story round-trips an empty-registry map without retired demonstration references", () => {
  const values = new Map();
  globalThis.window = { localStorage: { getItem: key => values.get(key) ?? null, setItem: (key, raw) => values.set(key, raw) } };
  try {
    const story = model.createTrustStory(snapshot, []);
    assert.equal(storage.validStoryDraft(story), true);
    assert.equal(story.scenes.length, 1);
    assert.deepEqual(story.scenes[0].snapshot, snapshot, "retain the captured camera, time and policy");
    assert.deepEqual(story.scenes[0].evidenceRefs, []);
    assert.equal(storage.writeDraft(storage.STORY_STORAGE_KEY, story), true);
    assert.deepEqual(storage.readDraft(storage.STORY_STORAGE_KEY), story);
  } finally { delete globalThis.window; }
});

test("story seeding uses only evidence present in the capture and does not bypass registry validation", () => {
  const capture = { ...snapshot, evidenceRefs: ["unadmitted-captured-reference"] };
  const story = model.createTrustStory(capture, [{ citation: "unrelated-reference" }]);
  assert.deepEqual(story.scenes[0].evidenceRefs, []);
  const matching = model.createTrustStory(capture, [{ citation: "unadmitted-captured-reference" }]);
  assert.deepEqual(matching.scenes[0].evidenceRefs, ["unadmitted-captured-reference"]);
  assert.equal(storage.validStoryDraft(matching), false, "available context cannot admit an unknown reference");
});

test("new stories keep location-redacted snapshots redacted and restorable", () => {
  const redacted = { ...snapshot, camera: { center: "WITHHELD_BROWSER_LOCATION", zoom: "WITHHELD", pitch: "WITHHELD", bearing: "WITHHELD" } };
  const story = model.createTrustStory(redacted, []);
  assert.equal(storage.validStoryDraft(story), true);
  assert.deepEqual(story.scenes[0].snapshot, redacted);
  assert.equal(JSON.stringify(story).includes("-98.38"), false);
});

test("validated draft writes preserve prior bytes for unknown references, oversize data and denied storage", () => {
  const values = new Map();
  let writes = 0, denied = false;
  globalThis.window = { localStorage: {
    getItem: key => values.get(key) ?? null,
    setItem(key, raw) { if (denied) throw new Error("quota denied"); writes += 1; values.set(key, raw); },
  } };
  try {
    const story = model.createTrustStory(snapshot, []);
    assert.equal(storage.writeDraft(storage.STORY_STORAGE_KEY, story), true);
    const previous = values.get(storage.STORY_STORAGE_KEY);
    const unadmitted = { ...story, scenes: [{ ...story.scenes[0], evidenceRefs: ["unadmitted-reference"] }] };
    assert.equal(storage.writeDraft(storage.STORY_STORAGE_KEY, unadmitted), false);
    const oversize = { ...story, scenes: Array.from({ length: 64 }, (_, i) => ({ ...story.scenes[0], id: `scene-${i}`, title: "t".repeat(20000), narrative: "n".repeat(20000) })) };
    assert.equal(storage.validStoryDraft(oversize), true, "exercise the serialized read bound separately from field validation");
    assert.equal(storage.writeDraft(storage.STORY_STORAGE_KEY, oversize), false);
    assert.equal(storage.writeDraft("another-storage-key", story), false);
    denied = true;
    assert.equal(storage.writeDraft(storage.STORY_STORAGE_KEY, { ...story, title: "Unsaved newer title" }), false);
    assert.equal(values.get(storage.STORY_STORAGE_KEY), previous);
    assert.equal(writes, 1);
  } finally { delete globalThis.window; }
});

test("fire report draft persists provider context without promoting it to evidence", () => {
  const context = fire.buildFireReportContext("nifc-fire-reports", null, "2026-09-24T14:00:00Z", "partial", "unavailable", []);
  const report = model.createReportDraft(snapshot, [], context);
  assert.equal(report.fireContext.kind, "nifc-fire-reports");
  assert.deepEqual(report.includedEvidenceIds, []);
  assert.match(report.sections.limitations, /No perimeter, current activity/);
  assert.equal(storage.validReportDraft(JSON.parse(JSON.stringify(report))), true);
  assert.equal(storage.validReportDraft({ ...report, fireContext: { ...context, sourceUrl: "https://example.org/" } }), false);
});

test("shared or stored snapshots reject unknown layers, references and invalid cameras", () => {
  assert.equal(storage.validMapSnapshot(snapshot), true);
  assert.equal(storage.validMapSnapshot({
    ...snapshot,
    committedTime: { start: 2024, end: 2026, label: "2024 to 2026 moving window", mode: "interval" },
    temporalSweep: { mode: "moving-window", frame: 2026, rangeStart: 2022, rangeEnd: 2026, windowStart: 2024, windowFrames: 2, stepRule: "available-events", interpolation: false },
  }), true);
  for (const patch of [
    { visibleLayers: [{ id: "water-context", title: "Hydrology context", domain: "Hydrology", opacity: .9, order: 0, trustState: "Synthetic" }] },
    { evidenceRefs: ["fabricated-released-claim"] },
    { camera: { ...snapshot.camera, center: [500, 38] } },
    { visibleLayers: [{ id: "water-context", title: "Hydrology context", domain: "Hydrology", opacity: 8, order: 0, trustState: "Synthetic" }] },
    { committedTime: { ...snapshot.committedTime, start: Infinity } },
    { temporalSweep: { mode: "moving-window", frame: 2026, rangeStart: 2022, rangeEnd: 2024, windowStart: 2024, windowFrames: 2, stepRule: "available-events", interpolation: false } },
    { temporalSweep: { mode: "snapshot", frame: 2026, rangeStart: 2026, rangeEnd: 2026, windowStart: 2026, windowFrames: 1, stepRule: "available-events", interpolation: true } },
    { evidenceFilter: "UNREVIEWED_BYPASS" },
  ]) assert.equal(storage.validMapSnapshot({ ...snapshot, ...patch }), false);
});

test("terrain snapshots preserve the selected DEM and display scale without changing legacy drafts", () => {
  const terrain = { ...snapshot, representation: "Terrain 3D", terrainProvider: "usgs-3dep", terrainExaggeration: 3 };
  assert.equal(storage.validMapSnapshot(terrain), true);
  assert.match(model.terrainSnapshotDescription(terrain), /USGS 3DEP dynamic DEM mosaic at 3\.00×/);
  assert.match(model.terrainSnapshotDescription({ ...terrain, terrainProvider: "mapzen" }), /Mapzen Terrarium DEM at 3\.00×/);
  const legacy = { ...snapshot, representation: "Terrain 3D" };
  assert.equal(storage.validMapSnapshot(legacy), true);
  assert.match(model.terrainSnapshotDescription(legacy), /not recorded in this saved snapshot/);
  assert.equal(model.terrainSnapshotDescription(snapshot), null);
  for (const invalid of [
    { ...terrain, terrainProvider: "other" },
    { ...terrain, terrainExaggeration: 3.1 },
    { ...terrain, terrainExaggeration: undefined },
    { ...snapshot, terrainProvider: "usgs-3dep", terrainExaggeration: 3 },
  ]) assert.equal(storage.validMapSnapshot(invalid), false);
});

test("location-redacted snapshots cannot restore precise bounds", () => {
  const redacted = { ...snapshot, camera: { center: "WITHHELD_BROWSER_LOCATION", zoom: "WITHHELD", pitch: "WITHHELD", bearing: "WITHHELD" } };
  assert.equal(storage.validMapSnapshot(redacted), true);
  assert.equal(storage.validMapSnapshot({ ...redacted, area: { ...snapshot.area, bounds: { west: -98.4, east: -98.3, south: 38.4, north: 38.5 } } }), false);
});
