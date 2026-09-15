import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";

const modules = new Map();
const moduleUrl = async (file) => {
  const resolved = path.resolve(file);
  if (modules.has(resolved)) return modules.get(resolved);
  let js = ts.transpileModule(await readFile(resolved, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) {
    js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(resolved), match[1]) + ".ts"))}`);
  }
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  modules.set(resolved, url);
  return url;
};

const saved = await import(await moduleUrl("app/saved-workspaces.ts"));
const embedded = await import(await moduleUrl("app/embed-runtime.ts"));
const perf = await import(await moduleUrl("app/map-performance.ts"));
const registry = await import(await moduleUrl("app/site-registry.ts"));

const workspace = {
  id: "workspace-1", name: "Kansas view", savedAt: "2026-09-15T16:00:00Z",
  view: { center: [-98.38, 38.48], zoom: 5.45, bearing: 0, pitch: 0 },
  visibility: { "kansas-extent": true }, opacity: { "kansas-extent": 0.5 }, layerOrder: ["kansas-extent"], year: 2026,
  basemap: "standard", projection: "mercator",
  report: { title: "Kansas report", scope: "VIEWPORT", detail: "STANDARD", layerIds: ["kansas-extent"], sections: {}, query: "" },
  selection: null,
};

test("corrupt device-local workspaces cannot replace the Explorer with a blank root", () => {
  assert.deepEqual(saved.parseSavedWorkspaceList(JSON.stringify([null]), 24), { records: [], rejected: true });
  assert.deepEqual(saved.parseSavedWorkspaceList("not-json", 24), { records: [], rejected: true });
  assert.deepEqual(saved.parseSavedWorkspaceList("x".repeat(101), 24, 100), { records: [], rejected: true });
  const mixed = saved.parseSavedWorkspaceList(JSON.stringify([workspace, { ...workspace, id: "" }]), 24);
  assert.equal(mixed.records.length, 1);
  assert.equal(mixed.records[0].id, "workspace-1");
  assert.equal(mixed.rejected, true);
});

test("embedded panels do not rewrite host-controlled history and history failures stay contained", () => {
  let writes = 0;
  const history = { replaceState: () => { writes++; } };
  assert.equal(embedded.replaceExplorerHistory("/?t=2026", true, history), false);
  assert.equal(writes, 0);
  assert.equal(embedded.replaceExplorerHistory("/?t=2026", false, history), true);
  assert.equal(writes, 1);
  assert.equal(embedded.replaceExplorerHistory("/?t=2026", false, { replaceState: () => { throw new Error("denied"); } }), false);
});

test("automatic embedded rendering uses the smallest bounded GPU budget", () => {
  const budget = perf.renderBudget("auto", 3, false, false, true);
  assert.equal(budget.pixelRatio, 1);
  assert.equal(budget.imageRequests, 6);
  assert.equal(budget.tileCache, 48);
  assert.equal(budget.workerCount, 1);
  assert.equal(perf.renderBudget("detail", 3, false, false, true).pixelRatio, 2);
});

test("route and global error surfaces keep client failures visible", async () => {
  const [routeError, globalError, page, snapshot] = await Promise.all([
    readFile(new URL("../app/error.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/global-error.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/page.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/snapshot-map.tsx", import.meta.url), "utf8"),
  ]);
  assert.match(routeError, /Retry in battery saver/);
  assert.match(globalError, /The Explorer could not finish loading/);
  assert.doesNotMatch(page, /\.loseContext\(/);
  assert.doesNotMatch(snapshot, /\.loseContext\(/);
});

test("embedded shells use parent-relative height and explicit shares stay guarded", async () => {
  const [css, observatory] = await Promise.all([
    readFile(new URL("../app/globals.css", import.meta.url), "utf8"),
    readFile(new URL("../app/observatory/workspace.tsx", import.meta.url), "utf8"),
  ]);
  assert.match(css, /\.site-root\s*\{[^}]*height:\s*100%/s);
  assert.match(css, /\.explorer-shell\s*\{[^}]*height:\s*calc\(100% - var\(--topbar\)\)/s);
  assert.doesNotMatch(observatory, /window\.history\.replaceState/);
  assert.match(observatory, /replaceExplorerHistory/);
});

test("every official connection has feature-level traceability", () => {
  assert.equal(registry.SITE_REGISTRY_COUNTS.connections, 15);
  assert.deepEqual(registry.SITE_REGISTRY_VALIDATION, { ok: true, errors: [] });
});
