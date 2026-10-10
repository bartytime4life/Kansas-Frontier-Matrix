import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const Panel = () => null, Inspector = () => null;
const undergroundModule = { default: Panel, SubsurfaceInspector: Inspector };
const gate = () => { let resolve, reject; const promise = new Promise((a, b) => { resolve = a; reject = b; }); return { promise, resolve, reject }; };
async function harness(importer) {
  let imports = 0;
  const deps = {};
  Object.defineProperty(deps, "./underground-panel", { get() { imports++; return importer(); } });
  const h = await componentHarness("app/underground-panel-loader.tsx", deps, {}, "\nexports.loadForTest = loadUnderground;");
  return { ...h, count: () => imports, panel(props = {}) { return h.render(h.exports.default, props); } };
}
function status(tree) {
  const node = findNode(tree, n => typeof n.type === "function" && n.type.name === "LoadStatus");
  assert.ok(node); return node.type(node.props);
}

test("the ordinary map does not import Underground until its requested surface mounts", async () => {
  const pending = gate(); const h = await harness(() => pending.promise);
  assert.equal(h.count(), 0);
  let closed = 0;
  const tree = h.panel({ onClose: () => closed++, year: 2026 });
  assert.equal(h.count(), 0, "rendering does not start provider or worker effects");
  assert.equal(tree.props["aria-busy"], true);
  findNode(tree, n => n.type === "button").props.onClick(); assert.equal(closed, 1);
  assert.equal(findNode(status(tree), n => n.type === "p").props.role, "status");
  h.commit(); await settle(); assert.equal(h.count(), 1);
  const a = h.exports.loadForTest(), b = h.exports.loadForTest(); assert.equal(a, b);
  assert.equal(h.count(), 1, "concurrent requests reuse the pending chunk");
  pending.resolve(undergroundModule); await settle(); await a;
  const props = { year: 1998, redacted: true, initialContext: { recordIds: [] }, onClose() {} };
  const loaded = h.panel(props);
  assert.equal(loaded.type, Panel);
  for (const [key, value] of Object.entries(props)) assert.equal(loaded.props[key], value, `forward current ${key}`);
  h.dispose();
});

test("a rejected module has a finite inline error and retry without replacing the map", async () => {
  let attempts = 0;
  const h = await harness(() => { if (++attempts === 1) throw new Error("https://private.invalid/?token=secret"); return undergroundModule; });
  h.panel(); h.commit(); await settle();
  const failed = h.panel(); assert.equal(failed.props["aria-busy"], false);
  const fallback = status(failed);
  assert.equal(findNode(fallback, n => n.type === "p").props.role, "alert");
  assert.doesNotMatch(JSON.stringify(fallback), /private.invalid|token|secret/);
  findNode(fallback, n => n.type === "button").props.onClick();
  assert.equal(h.panel().props["aria-busy"], true);
  h.commit(); await settle();
  assert.equal(h.panel().type, Panel); assert.equal(h.count(), 2); h.dispose();
});

test("closing while the chunk loads does not mount the panel or update the disposed surface", async () => {
  const pending = gate(); const h = await harness(() => pending.promise);
  h.panel(); h.commit(); await settle(); h.dispose();
  pending.resolve(undergroundModule); await settle();
  assert.notEqual(h.panel().type, Panel, "late completion cannot update unmounted component state");
  assert.equal(await h.exports.loadForTest(), undergroundModule, "successful import remains available for a later deliberate reopen");
  assert.equal(h.count(), 1);
});

test("the record inspector uses the shared module and forwards the current record and callbacks", async () => {
  const h = await harness(() => undergroundModule);
  await h.exports.loadForTest();
  const props = { inspection: { record: { id: "well-1" } }, onCenter() {}, onSave() {}, onReport() {} };
  const tree = h.render(h.exports.SubsurfaceInspector, props);
  assert.equal(tree.type, Inspector);
  for (const [key, value] of Object.entries(props)) assert.equal(tree.props[key], value, `forward current ${key}`);
  h.commit(); await settle(); assert.equal(h.count(), 1); h.dispose();
});
