import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = ts.transpileModule(await readFile(new URL("../app/observatory/frame-data.ts", import.meta.url), "utf8"), {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const { reuseUnchanged, sameFeatures } = await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);

const gauge = (value) => ({ type: "Feature", geometry: { type: "Point", coordinates: [-96.3, 39.2] }, properties: { stationId: "USGS-06889000", value, missing: false } });
const collection = (...features) => ({ type: "FeatureCollection", features });

test("a rebuilt frame with equal content reuses the collection the source holds", () => {
  const held = collection(gauge(410));
  // The streamflow frame builder returns fresh objects every step.
  assert.equal(reuseUnchanged(held, collection(gauge(410))), held);
  const changed = collection(gauge(455));
  assert.equal(reuseUnchanged(held, changed), changed);
  const fresh = collection(gauge(410));
  assert.equal(reuseUnchanged(undefined, fresh), fresh, "nothing held yet: upload the frame");
});

test("feature order and count are part of a frame's identity", () => {
  const a = gauge(1), b = gauge(2);
  assert.equal(sameFeatures(collection(a, b), collection(a, b)), true);
  assert.equal(sameFeatures(collection(a, b), collection(b, a)), false);
  assert.equal(sameFeatures(collection(a, b), collection(a)), false);
  assert.equal(sameFeatures(collection(), collection()), true);
});

test("the Observatory hides only tracks whose data changes for the requested time", async () => {
  const workspace = await readFile(new URL("../app/observatory/workspace.tsx", import.meta.url), "utf8");
  const step = workspace.slice(workspace.indexOf("const token = ++frameGeneration.current;"), workspace.indexOf("const apply = async () => {"));
  assert.ok(step.length > 0);
  // Hiding every event layer each step blanked unchanged smoke and river layers on every frame.
  assert.doesNotMatch(step, /hideEventLayers\(false\)/);
  assert.match(step, /reuseUnchanged\(uploadedGeoJSON\(/);
  assert.match(step, /geoJSONHasData\(held, frameData\.get\(sourceId\)!\)\) changing\.push\(track\)/);
});
