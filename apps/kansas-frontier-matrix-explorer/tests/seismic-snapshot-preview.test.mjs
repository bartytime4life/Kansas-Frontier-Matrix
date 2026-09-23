import assert from "node:assert/strict";
import { after, test } from "node:test";
import { mkdtempSync, readFileSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createHash } from "node:crypto";
import { createRequire } from "node:module";
import ts from "typescript";

const output = mkdtempSync(join(tmpdir(), "kfm-seismic-test-"));
after(() => rmSync(output, { recursive: true, force: true }));
writeFileSync(join(output, "package.json"), '{"type":"commonjs"}');
for (const name of ["bounded-json", "seismic-snapshot-preview"]) {
  const source = readFileSync(new URL(`../app/${name}.ts`, import.meta.url), "utf8");
  const result = ts.transpileModule(source, { compilerOptions: {
    target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.CommonJS,
  }, reportDiagnostics: true });
  assert.equal(result.diagnostics?.filter((d) => d.category === ts.DiagnosticCategory.Error).length, 0);
  writeFileSync(join(output, `${name}.js`), result.outputText);
}
const require = createRequire(import.meta.url);
const { inspectSeismicSnapshot: inspect, previewScope, SeismicPreviewSession: Session, SEISMIC_PREVIEW_MAX_BYTES } = require(join(output, "seismic-snapshot-preview.js"));
const scope = previewScope(-86400000, 0);
const stamp = "2026-09-22T00:00:00.000Z";
const feature = (id = "synthetic-a", time = -1000, properties = {}) => ({
  type: "Feature", id, geometry: { type: "Point", coordinates: [-98, 38, -0.5] },
  properties: { type: "earthquake", time, updated: null, mag: 0, magType: "ml", status: "reviewed", ...properties },
});
const collection = (features = [feature()]) => ({ type: "FeatureCollection", metadata: { count: features.length, status: 200, generated: 100 }, features });
const bytes = (data) => new TextEncoder().encode(JSON.stringify(data)).buffer;
const load = (data = collection(), selectedScope = scope) => inspect(bytes(data), selectedScope, stamp);
const reject = (mutate) => {
  const data = collection(); mutate(data);
  return assert.rejects(load(data));
};

test("zero and negative measurements, pre-1970 time, and missing update preserved", async () => {
  const result = await load();
  assert.equal(result.events[0].magnitude, 0);
  assert.equal(result.events[0].depthKm, -0.5);
  assert.equal(result.events[0].originMs, -1000);
  assert.equal(result.events[0].updatedMs, null);
  assert.equal(result.origin, "UNVERIFIED_LOCAL_FILE");
  assert.equal(result.admission, "NOT_ADMITTED");
});

test("digest binds exact supplied bytes", async () => {
  const body = bytes(collection());
  const result = await inspect(body, scope, stamp);
  assert.equal(result.sha256, "sha256:" + createHash("sha256").update(Buffer.from(body)).digest("hex"));
});

test("scope and results are immutable", async () => {
  const result = await load();
  assert.ok(Object.isFrozen(result));
  assert.ok(Object.isFrozen(result.scope));
  assert.ok(Object.isFrozen(result.events));
  assert.ok(Object.isFrozen(result.events[0]));
});

test("origin, update, generation and inspection clocks remain separate", async () => {
  const result = await load(collection([feature("x", -1000, { updated: 10 })]));
  assert.equal(result.events[0].updatedMs, 10);
  assert.equal(result.generatedMs, 100);
  assert.equal(result.inspectedAt, stamp);
});

test("valid empty is a successful empty preview", async () => assert.equal((await load(collection([]))).events.length, 0));
test("end boundary is excluded, start included", async () => {
  const result = await load(collection([feature("a", -86400000), feature("b", 0)]));
  assert.deepEqual(result.events.map((e) => e.id), ["a"]);
  assert.equal(result.excludedCount, 1);
});
test("outside Kansas envelope and non-earthquake records disclosed as excluded", async () => {
  const outside = feature("out"); outside.geometry.coordinates = [10, 20, 1];
  const result = await load(collection([outside, feature("blast", -1000, { type: "quarry blast" })]));
  assert.equal(result.excludedCount, 2);
  assert.equal(result.suppliedCount, 2);
});
test("depth is not emitted as a GeoJSON surface altitude", async () => {
  const event = (await load()).events[0];
  assert.equal(event.depthKm, -0.5);
  assert.equal("coordinates" in event, false);
});
test("unknown fields never cross the preview projection", async () => {
  const data = collection(); data.features[0].properties.secret = "do-not-copy";
  assert.equal(JSON.stringify(await load(data)).includes("do-not-copy"), false);
});
test("null magnitude and depth do not become zero", async () => {
  const data = collection(); data.features[0].properties.mag = null; data.features[0].geometry.coordinates[2] = null;
  const event = (await load(data)).events[0];
  assert.equal(event.magnitude, null); assert.equal(event.depthKm, null);
});
test("bad collection count", () => reject((p) => { p.metadata.count = 2; }));
test("bad collection status", () => reject((p) => { p.metadata.status = 500; }));
test("bad geometry type", () => reject((p) => { p.features[0].geometry.type = "LineString"; }));
test("invalid coordinate range", () => reject((p) => { p.features[0].geometry.coordinates[1] = 100; }));
test("missing coordinate is not zero", () => reject((p) => { p.features[0].geometry.coordinates[0] = null; }));
test("string number rejected", () => reject((p) => { p.features[0].properties.mag = "2"; }));
test("fractional epoch rejected", () => reject((p) => { p.features[0].properties.time = -1.5; }));
test("unsafe epoch rejected", () => reject((p) => { p.features[0].properties.time = 9007199254740992; }));
test("duplicate event ID rejected", () => load(collection([feature(), feature()])).then(() => assert.fail("accepted"), () => {}));
test("duplicate alias across records rejected", () => assert.rejects(load(collection([
  feature("a", -1000, { ids: ",a,shared," }), feature("b", -2000, { ids: ",b,shared," }),
]))));
test("invalid IDs rejected", () => reject((p) => { p.features[0].id = "<script>"; }));
test("invalid UTF-8 rejected", () => assert.rejects(inspect(new Uint8Array([255]).buffer, scope, stamp)));
test("malformed JSON rejected", () => assert.rejects(inspect(new TextEncoder().encode("{").buffer, scope, stamp)));
test("over-budget bytes rejected before parse", () => assert.rejects(inspect(new ArrayBuffer(SEISMIC_PREVIEW_MAX_BYTES + 1), scope, stamp)));
test("over-budget feature count rejected", () => assert.rejects(load(collection(Array.from({ length: 10001 }, (_, i) => feature(`x${i}`))))));
test("invalid scope rejected", () => { for (const pair of [[0, 0], [1, 0], [NaN, 0], [-1.1, 0]]) assert.throws(() => previewScope(...pair)); });
test("invalid inspection time rejected", () => assert.rejects(inspect(bytes(collection()), scope, "2026-02-30T00:00:00.000Z")));
test("populated -> empty -> populated clears old selection", async () => {
  const session = new Session(); const populated = await load(); const empty = await load(collection([]));
  session.accept(session.begin(scope), populated); assert.equal(session.select("synthetic-a"), true);
  session.accept(session.begin(scope), empty);
  assert.equal(session.state.selectedId, null); assert.equal(session.state.preview.events.length, 0);
  session.accept(session.begin(scope), populated); assert.equal(session.state.preview.events.length, 1);
});
test("same-window failed import retains explicit stale preview", async () => {
  const session = new Session(); session.accept(session.begin(scope), await load());
  session.fail(session.begin(scope));
  assert.equal(session.state.phase, "STALE_PREVIEW"); assert.equal(session.state.preview.events.length, 1);
});
test("different-window failure cannot reuse old data", async () => {
  const session = new Session(); session.accept(session.begin(scope), await load());
  session.fail(session.begin(previewScope(0, 86400000)));
  assert.equal(session.state.phase, "ERROR"); assert.equal(session.state.preview, null);
});
test("late success or error cannot overwrite newer import", async () => {
  const session = new Session(); const old = session.begin(scope); const next = session.begin(scope);
  assert.equal(session.accept(old, await load()), false); assert.equal(session.fail(old), false);
  assert.equal(session.accept(next, await load(collection([]))), true);
  assert.equal(session.state.preview.events.length, 0);
});
test("clear invalidates outstanding work", async () => {
  const session = new Session(); const ticket = session.begin(scope); session.clear();
  assert.equal(session.accept(ticket, await load()), false); assert.equal(session.fail(ticket), false);
  assert.equal(session.state.phase, "IDLE");
});
test("completed tickets cannot be replayed", async () => {
  const session = new Session(); const ticket = session.begin(scope); session.accept(ticket, await load());
  assert.equal(session.accept(ticket, await load(collection([]))), false); assert.equal(session.fail(ticket), false);
});
test("scope-mismatched result is refused", async () => {
  const session = new Session(); const ticket = session.begin(scope);
  assert.equal(session.accept(ticket, await load(collection(), previewScope(0, 86400000))), false);
});
test("unknown selected ID is refused", () => assert.equal(new Session().select("absent"), false));
test("React panel syntax and Import composition references; no raw HTML sink", () => {
  const panel = readFileSync(new URL("../app/seismic-snapshot-panel.tsx", import.meta.url), "utf8");
  const composition = readFileSync(new URL("../app/waveform-preview-panel.tsx", import.meta.url), "utf8");
  const result = ts.transpileModule(panel, { compilerOptions: { jsx: ts.JsxEmit.ReactJSX, target: ts.ScriptTarget.ES2022 }, reportDiagnostics: true });
  assert.equal(result.diagnostics?.filter((d) => d.category === ts.DiagnosticCategory.Error).length, 0);
  assert.match(composition, /import SeismicSnapshotPanel from "\.\/seismic-snapshot-panel"/);
  assert.match(composition, /<SeismicSnapshotPanel\s*\/>/);
  assert.doesNotMatch(panel, /dangerouslySetInnerHTML|localStorage|sessionStorage|fetch\s*\(|XMLHttpRequest/);
  assert.match(panel, /role="status"/); assert.match(panel, /type="file"/);
});
