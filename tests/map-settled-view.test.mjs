import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { runInNewContext } from "node:vm";
import test from "node:test";
import ts from "typescript";

const compile = source => ts.transpileModule(source, {
  compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.ESNext },
}).outputText;
const performanceSource = await readFile(new URL("../app/map-performance.ts", import.meta.url), "utf8");
const { createSettledMapCommit } = await import(`data:text/javascript;base64,${Buffer.from(compile(performanceSource)).toString("base64")}`);
const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
const tree = ts.createSourceFile("page.tsx", page, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
const parts = {};
function visit(node) {
  if (ts.isVariableDeclaration(node) && ["settledViewCommit", "settledViewWasReplay", "cameraViewsEquivalent"].includes(node.name.getText(tree))) {
    parts[node.name.getText(tree)] = `${node.name.getText(tree) === "settledViewWasReplay" ? "let" : "const"} ${node.getText(tree)};`;
  }
  if (ts.isExpressionStatement(node) && node.getText(tree).startsWith("cancelSettledViewCommit =")) parts.cancel = node.getText(tree);
  if (ts.isCallExpression(node) && node.expression.getText(tree) === "map.on") {
    if (node.arguments[0]?.getText(tree) === '"movestart"' && node.getText(tree).includes("lastKnownGoodViewRef.current")) parts.start = node.getText(tree);
    if (node.arguments[0]?.getText(tree) === '"moveend"' && node.getText(tree).includes("settledViewCommit.schedule()")) parts.end = node.getText(tree);
  }
  ts.forEachChild(node, visit);
}
visit(tree);
for (const name of ["settledViewCommit", "settledViewWasReplay", "cameraViewsEquivalent", "cancel", "start", "end"]) assert.ok(parts[name], name);

function harness() {
  const jobs = [], handlers = {}, views = [], bounds = [], indexes = [], lengths = [];
  let moving = false, longitude = -98, terrainChecks = 0;
  const context = {
    createSettledMapCommit: (commit, isMoving) => createSettledMapCommit(commit, isMoving, job => jobs.push(job)),
    syncTerrainRasterView: () => terrainChecks++,
    map: {
      on: (event, handler) => { handlers[event] = handler; },
      isMoving: () => moving,
      getCenter: () => ({ lng: longitude, lat: 38 }),
      getZoom: () => 10.5, getBearing: () => 0, getPitch: () => 0,
      getVerticalFieldOfView: () => 37,
      getBounds: () => ({ getWest: () => longitude - .1, getEast: () => longitude + .1, getSouth: () => 37.9, getNorth: () => 38.1 }),
    },
    setView: value => views.push(value), setMapViewportBounds: value => bounds.push(value),
    fieldOfViewRef: { current: 36 }, setFieldOfView() {},
    lastKnownGoodViewRef: { current: null }, replayingCameraHistoryRef: { current: false },
    locationDerivedViewRef: { current: false }, cameraHistoryRef: { current: [] }, cameraHistoryIndexRef: { current: -1 },
    setCameraHistoryIndex: value => indexes.push(value), setCameraHistoryLength: value => lengths.push(value),
  };
  runInNewContext(compile(`let cancelSettledViewCommit = () => {};
    ${parts.cameraViewsEquivalent} ${parts.settledViewWasReplay} ${parts.settledViewCommit} ${parts.cancel}
    ${parts.start}; ${parts.end}; globalThis.cancelPending = cancelSettledViewCommit;`), context);
  return { context, views, bounds, indexes, lengths, terrainChecks: () => terrainChecks,
    start() { moving = true; handlers.movestart(); },
    end(value) { moving = false; longitude = value; handlers.moveend(); },
    moving(value) { moving = value; },
    flush() { while (jobs.length) jobs.shift()(); },
  };
}

test("the real movement callbacks skip all interrupted snapshots and commit the final camera and bounds once", () => {
  const h = harness();
  h.start();
  for (let index = 0; index < 48; index++) {
    h.end(-98 + index / 1000); h.start(); h.flush();
  }
  assert.equal(h.views.length, 0); assert.equal(h.bounds.length, 0); assert.equal(h.terrainChecks(), 0);
  h.end(-97.5); h.flush();
  assert.equal(h.views.length, 1); assert.equal(h.views[0].center[0], -97.5);
  assert.equal(h.bounds[0].west, -97.6); assert.equal(h.bounds[0].east, -97.4);
  assert.equal(h.terrainChecks(), 1); assert.deepEqual(h.indexes, [0]); assert.deepEqual(h.lengths, [1]);
});

test("an actual settled jump commits before the next task, and duplicate end events keep the newest camera", async () => {
  let camera = 1; const committed = [];
  const next = createSettledMapCommit(() => committed.push(camera), () => false);
  next.schedule(); camera = 2; next.schedule();
  assert.deepEqual(committed, []);
  await Promise.resolve(); assert.deepEqual(committed, [2]);
  next.schedule(); await Promise.resolve(); assert.deepEqual(committed, [2, 2]);
});

test("late microtasks cannot consume a replacement commit and disposal cancels every pending viewport read", () => {
  const h = harness();
  h.end(-98); h.start(); h.end(-97); h.flush();
  assert.equal(h.views.length, 1); assert.equal(h.views[0].center[0], -97);
  h.end(-96); h.context.cancelPending(); h.flush();
  assert.equal(h.views.length, 1); assert.equal(h.terrainChecks(), 1);
});

test("still-moving cameras never commit; GPS-derived and replayed views retain their history exclusions", () => {
  const h = harness();
  h.end(-98); h.moving(true); h.flush(); assert.equal(h.views.length, 0);
  h.context.locationDerivedViewRef.current = true; h.end(-97); h.flush();
  assert.equal(h.views.length, 1); assert.equal(h.context.cameraHistoryRef.current.length, 0);
  h.context.locationDerivedViewRef.current = false; h.context.replayingCameraHistoryRef.current = true;
  h.end(-96); h.flush(); assert.equal(h.context.replayingCameraHistoryRef.current, false);
  assert.equal(h.context.cameraHistoryRef.current.length, 0);
  h.end(-95); h.flush(); assert.equal(h.context.cameraHistoryRef.current.length, 1);
  h.end(-95); h.flush(); assert.equal(h.context.cameraHistoryRef.current.length, 1);
});

test("interrupting a replay consumes its marker immediately and records the final manual view", () => {
  const h = harness();
  h.context.replayingCameraHistoryRef.current = true;
  h.end(-97); h.start(); h.flush();
  assert.equal(h.context.replayingCameraHistoryRef.current, false);
  assert.equal(h.views.length, 0);
  h.end(-96); h.flush();
  assert.equal(h.context.cameraHistoryRef.current.length, 1);
  assert.equal(h.context.cameraHistoryRef.current[0].center[0], -96);
});
