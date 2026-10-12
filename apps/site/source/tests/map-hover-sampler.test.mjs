import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
const source = await readFile(new URL("../app/map-hover-sampler.ts", import.meta.url), "utf8");
const code = ts.transpileModule(source, { compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.ESNext } }).outputText;
const { createMapHoverSampler } = await import(`data:text/javascript;base64,${Buffer.from(code).toString("base64")}`);
function harness() {
  let now = 0, sequence = 0;
  const timers = new Map(), samples = [];
  const sampler = createMapHoverSampler(event => samples.push(event), 80, {
    now: () => now,
    setTimer: (callback, delay) => { const id = ++sequence; timers.set(id, { callback, at: now + delay }); return id; },
    clearTimer: id => timers.delete(id),
  });
  return { sampler, timers, samples, time(value) {
    now = value;
    for (const [id, timer] of [...timers]) if (timer.at <= now) { timers.delete(id); timer.callback(); }
  } };
}
test("hit testing is bounded and the pointer's final position is always sampled", () => {
  const h = harness();
  h.sampler.push("first");
  for (let time = 1; time < 80; time++) { h.time(time); h.sampler.push(time); }
  assert.deepEqual(h.samples, ["first"]); assert.equal(h.timers.size, 1);
  h.time(80); assert.deepEqual(h.samples, ["first", 79]);
  h.time(81); h.sampler.push("final"); h.time(160);
  assert.deepEqual(h.samples, ["first", 79, "final"]);
});
test("pointer exit, camera motion, style replacement and disposal cancel trailing work", () => {
  const h = harness(); h.sampler.push("first"); h.time(10); h.sampler.push("stale");
  h.sampler.cancel(); assert.equal(h.timers.size, 0); h.time(100);
  assert.deepEqual(h.samples, ["first"]);
  h.sampler.push("new style"); assert.deepEqual(h.samples, ["first", "new style"]);
});
test("the production pointer callback queues the latest event and cancels while unavailable", async () => {
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const tree = ts.createSourceFile("page.tsx", page, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
  let registration;
  function visit(node) {
    if (ts.isCallExpression(node) && node.expression.getText(tree) === "map.on"
      && node.arguments[0]?.getText(tree) === '"mousemove"' && ts.isArrowFunction(node.arguments[1])) registration = node.getText(tree);
    ts.forEachChild(node, visit);
  }
  visit(tree); assert.ok(registration);
  let handler, moving = false, cleared = 0, canceled = 0; const samples = [];
  const ready = {current:true}, underground = {current:false}, measure = {current:null}, document = {hidden:false};
  const javascript = ts.transpileModule(registration, {compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
  new Function("map", "hoverSampler", "clearHoverCandidate", "styleGenerationReadyRef", "document", "undergroundOpenRef", "measureModeRef", javascript)(
    {on:(_event, callback)=>{handler=callback;},isMoving:()=>moving},
    {push:event=>samples.push(event),cancel:()=>canceled++},()=>cleared++, ready, document, underground, measure);
  handler("visible"); assert.deepEqual(samples,["visible"]);
  moving=true;handler("pan");moving=false;
  ready.current=false;handler("style");ready.current=true;
  document.hidden=true;handler("hidden");document.hidden=false;
  underground.current=true;handler("cutaway");
  assert.equal(canceled,4);assert.equal(cleared,4);assert.deepEqual(samples,["visible"]);
});
