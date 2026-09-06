import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const loadStorage = async () => {
  const source = await readFile(new URL("../app/workspace-storage.ts", import.meta.url), "utf8");
  const typescript = await import("typescript");
  const javascript = typescript.transpileModule(source, {
    compilerOptions: { module: typescript.ModuleKind.ESNext, target: typescript.ScriptTarget.ES2022 },
    fileName: "workspace-storage.ts",
  }).outputText;
  return import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
};

const baseSnapshot = () => ({
  id: "workspace-1",
  name: "Safe workspace",
  savedAt: "2026-09-06T00:00:00.000Z",
  view: { center: [-98.38, 38.48], zoom: 5.45, bearing: 0, pitch: 0 },
  visibility: { "water-context": true },
  opacity: { "water-context": 0.75 },
  layerOrder: ["water-context"],
  year: 2026,
  basemap: "midnight",
  projection: "mercator",
  report: {
    title: "Kansas map data report",
    scope: "VIEWPORT",
    detail: "STANDARD",
    layerIds: ["water-context"],
    sections: { summary: true, findings: true, records: true, evidence: true, limitations: true },
    query: "",
    evidenceFilter: "ALL",
  },
  selection: null,
});

test("restores only bounded, structurally valid workspace snapshots", async () => {
  const storage = await loadStorage();
  const raw = JSON.stringify([baseSnapshot()]);
  const restored = storage.parseSavedWorkspaces(raw);
  assert.equal(restored.length, 1);
  assert.deepEqual(restored[0], JSON.parse(raw)[0]);
  assert.equal(storage.parseSavedWorkspaces(JSON.stringify([{ ...baseSnapshot(), locationCameraRedacted: true }])).length, 1);
  assert.equal(storage.parseSavedWorkspaces(JSON.stringify([{ ...baseSnapshot(), report: undefined }])).length, 1);
});

test("rejects malformed, out-of-context, and prototype-shaped storage entries", async () => {
  const storage = await loadStorage();
  const protoVisibility = JSON.parse("{\"__proto__\":true}");
  const invalidEntries = [
    null,
    { ...baseSnapshot(), id: "" },
    { ...baseSnapshot(), name: "x".repeat(51) },
    { ...baseSnapshot(), savedAt: "not-a-date" },
    { ...baseSnapshot(), view: { ...baseSnapshot().view, center: [-120, 38.48] } },
    { ...baseSnapshot(), view: { ...baseSnapshot().view, zoom: null } },
    { ...baseSnapshot(), opacity: { "water-context": 2 } },
    { ...baseSnapshot(), visibility: protoVisibility },
    { ...baseSnapshot(), report: { ...baseSnapshot().report, evidenceFilter: "toString" } },
    { ...baseSnapshot(), locationCameraRedacted: "yes" },
  ];
  for (const invalid of invalidEntries) assert.deepEqual(storage.parseSavedWorkspaces(JSON.stringify([invalid])), []);

  assert.deepEqual(storage.parseSavedWorkspaces("{not-json"), []);
  assert.deepEqual(storage.parseSavedWorkspaces(JSON.stringify({ ...baseSnapshot() })), []);
  assert.deepEqual(storage.parseSavedWorkspaces("x".repeat(storage.MAX_SERIALIZED_BYTES + 1)), []);
});

test("bounds restore count and deduplicate workspace IDs", async () => {
  const storage = await loadStorage();
  const entries = Array.from({ length: storage.MAX_SAVED_WORKSPACES + 2 }, (_, index) => ({
    ...baseSnapshot(),
    id: `workspace-${index}`,
  }));
  entries.push({ ...baseSnapshot(), id: "workspace-0", name: "duplicate" });
  const restored = storage.parseSavedWorkspaces(JSON.stringify(entries));
  assert.equal(restored.length, storage.MAX_SAVED_WORKSPACES);
  assert.deepEqual(restored.map((entry) => entry.id), Array.from({ length: storage.MAX_SAVED_WORKSPACES }, (_, index) => `workspace-${index}`));
});
