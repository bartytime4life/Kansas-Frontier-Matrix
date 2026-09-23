import assert from "node:assert/strict";
import test from "node:test";
import { readFile } from "node:fs/promises";
import ts from "typescript";

const urls = new Map();
async function moduleUrl(name) {
  if (urls.has(name)) return urls.get(name);
  let js = ts.transpileModule(await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8"), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  for (const [, dependency] of [...js.matchAll(/from "\.\/([a-z-]+)"/g)]) js = js.replaceAll(`from "./${dependency}"`, `from "${await moduleUrl(dependency)}"`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  urls.set(name, url);
  return url;
}
const model = await import(await moduleUrl("workspace-model"));
const storage = await import(await moduleUrl("workspace-storage"));
const { LAYER_REGISTRY } = await import(await moduleUrl("explorer-data"));
const evidence = LAYER_REGISTRY.flatMap((layer) => layer.data.features.map(({ properties: p }) => ({
  id: `evidence:${layer.id}:${p.fid}`, layerId: layer.id, featureId: p.fid, title: p.title, domain: layer.domain,
  sourceOrganization: p.sourceOrganization, sourceRole: p.sourceRole, citation: p.citation,
  spatialScope: p.spatialScope, temporalExtent: { start: p.year, end: p.year, label: p.temporalScope, mode: "instant" },
  trustState: model.trustStateFromEvidenceState(p.evidenceState, p.sourceRole), evidenceState: p.evidenceState,
  supports: p.summary, cannotProve: p.generalizationNote, caveat: p.uncertainty, policyStatus: p.releaseState,
  includedByDefault: ["ANSWER", "CORRECTED"].includes(p.evidenceState), displayFocus: [p.focusLng, p.focusLat],
})));
const target = evidence.find((r) => r.featureId === "atmo-topeka-2026");
const snapshot = {
  id: "snapshot-test", createdAt: "2026-09-09T00:00:00Z", area: { kind: "viewport", label: "Kansas" },
  camera: { center: [-98.38, 38.48], zoom: 5.4, pitch: 0, bearing: 0 }, representation: "2D", projection: "mercator", basemap: "standard",
  committedTime: { start: 2026, end: 2026, label: "2026", mode: "instant" },
  visibleLayers: [{ id: target.layerId, title: "Atmosphere", domain: "Atmosphere", opacity: .9, order: 0, trustState: "Synthetic" }],
  selection: null, evidenceRefs: [target.citation], inspectableFeatureIds: [target.featureId],
  inspectableRecordCount: 1, sourceBackedCount: 0, boundedCount: 1, policy: model.policyDecisionFromEvidenceState("ANSWER"),
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

test("report creation includes only evidence inside the captured feature scope", () => {
  const extra = { ...target, id: "out-of-scope", featureId: "different-feature" };
  const report = model.createReportDraft(snapshot, [...evidence, extra]);
  assert.deepEqual(report.includedEvidenceIds, [target.id]);
  assert.equal(report.status, "DRAFT");
  assert.equal(storage.validReportDraft(JSON.parse(JSON.stringify(report))), true);
  assert.equal(storage.validReportDraft({ ...report, status: "PUBLISHED" }), false);
});

test("shared or stored snapshots reject unknown layers, references and invalid cameras", () => {
  assert.equal(storage.validMapSnapshot(snapshot), true);
  assert.equal(storage.validMapSnapshot({
    ...snapshot,
    committedTime: { start: 2024, end: 2026, label: "2024 to 2026 moving window", mode: "interval" },
    temporalSweep: { mode: "moving-window", frame: 2026, rangeStart: 2022, rangeEnd: 2026, windowStart: 2024, windowFrames: 2, stepRule: "available-events", interpolation: false },
  }), true);
  for (const patch of [
    { visibleLayers: [{ ...snapshot.visibleLayers[0], id: "foreign-source" }] },
    { evidenceRefs: ["fabricated-released-claim"] },
    { camera: { ...snapshot.camera, center: [500, 38] } },
    { visibleLayers: [{ ...snapshot.visibleLayers[0], opacity: 8 }] },
    { committedTime: { ...snapshot.committedTime, start: Infinity } },
    { temporalSweep: { mode: "moving-window", frame: 2026, rangeStart: 2022, rangeEnd: 2024, windowStart: 2024, windowFrames: 2, stepRule: "available-events", interpolation: false } },
    { temporalSweep: { mode: "snapshot", frame: 2026, rangeStart: 2026, rangeEnd: 2026, windowStart: 2026, windowFrames: 1, stepRule: "available-events", interpolation: true } },
    { evidenceFilter: "UNREVIEWED_BYPASS" },
  ]) assert.equal(storage.validMapSnapshot({ ...snapshot, ...patch }), false);
});

test("location-redacted snapshots cannot restore precise bounds", () => {
  const redacted = { ...snapshot, camera: { center: "WITHHELD_BROWSER_LOCATION", zoom: "WITHHELD", pitch: "WITHHELD", bearing: "WITHHELD" } };
  assert.equal(storage.validMapSnapshot(redacted), true);
  assert.equal(storage.validMapSnapshot({ ...redacted, area: { ...snapshot.area, bounds: { west: -98.4, east: -98.3, south: 38.4, north: 38.5 } } }), false);
});

test("the four trust scenes bind distinct matching feature, time, camera and policy", () => {
  const story = model.createTrustStory(snapshot, evidence);
  assert.equal(storage.validStoryDraft(JSON.parse(JSON.stringify(story))), true);
  assert.deepEqual(story.scenes.map((scene) => scene.snapshot.committedTime.start), [2026, 2024, 1910, 2026]);
  assert.deepEqual(story.scenes.map((scene) => scene.snapshot.temporalSweep.frame), [2026, 2024, 1910, 2026]);
  assert.equal(story.scenes.every((scene) => scene.snapshot.temporalSweep.mode === "snapshot" && scene.snapshot.temporalSweep.interpolation === false), true);
  assert.deepEqual(story.scenes.map((scene) => scene.snapshot.selection.featureId), ["atmo-topeka-2026", "atmo-hays-2024", "history-route-1910", "planning-generalized-envelope"]);
  assert.equal(story.scenes[3].snapshot.policy.outcome, "DENY");
  assert.equal(story.scenes.every((scene) => scene.snapshot.sourceBackedCount === 0), true);
  assert.notDeepEqual(story.scenes[0].snapshot.camera.center, story.scenes[1].snapshot.camera.center);
  assert.equal(storage.validStoryDraft({ ...story, scenes: [{ ...story.scenes[0], snapshot: {} }] }), false);
});
