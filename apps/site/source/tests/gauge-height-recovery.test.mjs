import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { componentHarness, findNode, settle as settleHooks } from "./component-harness.mjs";

// Run the page's actual gauge-only effect and markup, with its real parser and
// streaming reader. This is a lifecycle fixture, not WebGL or provider evidence.
const source = await readFile("app/page.tsx", "utf8");
const start = source.indexOf('  const selectedStageDetail = selectedOfficialContextId === "usgs-streamflow"');
const endToken = '  }, [rightOpen, selected?.externalStationId, selectedOfficialContextId, stageDrawerAttempt]);';
const end = source.indexOf(endToken, start);
const markupStart = source.indexOf('<section className="drawer-data-block" aria-label="USGS gauge height data">');
const markupEnd = source.indexOf("\n                </section>}", markupStart);
assert.ok(start >= 0 && end > start && markupStart >= 0 && markupEnd > markupStart);
const effect = source.slice(start, end + endToken.length);
const markup = source.slice(markupStart, markupEnd) + "</section>";
const bounded = (await componentHarness("app/bounded-json.ts", {}, { TextDecoder, Uint8Array })).exports;
const settle = async () => { await settleHooks(); await settleHooks(); };
const deferred = () => { let resolve; const promise = new Promise(done => { resolve = done; }); return { promise, resolve }; };
const textOf = node => typeof node === "string" || typeof node === "number" ? String(node) : node && typeof node === "object" ? [node.props?.children].flat(Infinity).map(textOf).join(" ").replace(/\s+/g, " ") : "";
const action = tree => findNode(tree, node => node.type === "button");
const A = "USGS-06911900", B = "USGS-06892350";
function stage(stationId = A, value = 3.25) {
  return { kind:"usgs-streamflow-bundle", mode:"station", parameterCode:"00065", queryStart:"2026-11-02T12:00:00.000Z", queryEnd:"2026-11-09T12:00:00.000Z", retrievedAt:"2026-11-09T12:00:00.000Z", partial:false, truncated:false,
    stations:[{ stationId, agencyCode:"USGS", name:`SYNTHETIC ${stationId}`, county:null, huc:null, drainageArea:null, contributingDrainageArea:null, siteTypeCode:"ST", latitude:38.48, longitude:-98.38 }],
    observations:value === undefined ? [] : [{ stationId, parameterCode:"00065", observedAt:"2026-11-09T11:00:00.000Z", value, unit:"ft", approvalStatus:"SYNTHETIC fixture only", qualifiers:[] }] };
}
async function setup(dispatch) {
  const timers = new Map(), requests = []; let timerId = 0;
  const h = await componentHarness("app/evidence-drawer-data.ts", {}, {
    readBoundedJson:bounded.readBoundedJson, drawerTimestamp:time => time,
    setTimeout:(fn, delay) => { const id = ++timerId; timers.set(id, { fn, delay }); return id; }, clearTimeout:id => timers.delete(id),
    fetch:(url, options) => { requests.push({ url, options }); return dispatch(url, options); },
  }, `\nimport { useEffect, useState } from "react";
export default function GaugeFixture({ stationId, rightOpen = true, sourceId = "usgs-streamflow" }) {
  const selected = { externalStationId:stationId }, selectedOfficialContextId = sourceId;
  const selectedRiverObservation = { stationId };
  const [stageDrawerLoad, setStageDrawerLoad] = useState(null);
  const [stageDrawerAttempt, setStageDrawerAttempt] = useState(0);
  ${effect}
  return (${markup});
}`);
  let props = { stationId:A };
  const render = next => { props = { ...props, ...next }; const tree = h.render(h.exports.default, props); h.commit(); return tree; };
  render(); await settle();
  return { h, render, requests, timers, expire() { const entry = [...timers].find(([, value]) => value.delay === 15_000); assert.ok(entry); timers.delete(entry[0]); entry[1].fn(); } };
}

test("stalled headers time out, leave discharge separate, and retry with the unchanged station contract", async () => {
  const late = deferred(); let calls = 0, canceled = false;
  const f = await setup(() => ++calls === 1 ? late.promise : Promise.resolve(Response.json(stage())));
  assert.equal(Boolean(action(f.render()).props.disabled), false); assert.equal(action(f.render()).props.children, "Restart gauge-height check");
  f.expire(); await settle(); let tree = f.render(); assert.match(textOf(tree), /timed out.*Retry this station.*discharge frame and its history remain separate/);
  assert.ok(findNode(tree, node => node.props?.role === "alert")); assert.equal(f.requests[0].options.signal.aborted, true); assert.equal(f.timers.size, 0);
  action(tree).props.onClick(); f.render(); await settle(); tree = f.render(); assert.match(textOf(tree), /Latest returned value: 3.25 ft/);
  assert.equal(f.requests[1].url, `/api/hydrology/streamflow?mode=station&range=7d&station=${A}&parameter=00065&resolution=continuous`);
  late.resolve(new Response(new ReadableStream({ cancel() { canceled = true; } }))); await settle(); assert.equal(canceled, true); assert.match(textOf(f.render()), /3.25 ft/); f.h.dispose();
});

test("the deadline cancels a stalled body and releases its reader before recovery", async () => {
  let canceled = false, calls = 0;
  const response = new Response(new ReadableStream({ start(controller) { controller.enqueue(new TextEncoder().encode('{"kind":')); }, cancel() { canceled = true; } }));
  const f = await setup(() => Promise.resolve(++calls === 1 ? response : Response.json(stage())));
  assert.equal(response.body.locked, true); f.expire(); await settle(); assert.equal(canceled, true); assert.equal(response.body.locked, false);
  action(f.render()).props.onClick(); f.render(); await settle(); assert.match(textOf(f.render()), /3.25 ft/); assert.equal(f.timers.size, 0); f.h.dispose();
});

test("restart replaces a pending read and the old result cannot settle its replacement", async () => {
  const old = deferred(), fresh = deferred(); let calls = 0;
  const f = await setup(() => ++calls === 1 ? old.promise : fresh.promise);
  action(f.render()).props.onClick(); f.render(); await settle(); assert.equal(f.requests[0].options.signal.aborted, true); assert.equal(f.timers.size, 1);
  old.resolve(Response.json(stage(A, 99))); await settle(); assert.doesNotMatch(textOf(f.render()), /99 ft/); assert.match(textOf(f.render()), /Loading station metadata/);
  fresh.resolve(Response.json(stage(A, 4))); await settle(); assert.match(textOf(f.render()), /4 ft/); f.h.dispose();
});

test("station changes including A→B→A never resurrect an earlier attempt", async () => {
  const pending = [deferred(), deferred(), deferred()]; let index = 0;
  const f = await setup(() => pending[index++].promise);
  f.render({ stationId:B }); f.render({ stationId:A }); await settle(); assert.equal(f.requests.length, 3);
  assert.equal(f.requests[0].options.signal.aborted, true); assert.equal(f.requests[1].options.signal.aborted, true);
  pending[0].resolve(Response.json(stage(A, 99))); pending[1].resolve(Response.json(stage(B, 88))); await settle(); assert.match(textOf(f.render()), /Loading station metadata/); assert.doesNotMatch(textOf(f.render()), /99 ft|88 ft/);
  pending[2].resolve(Response.json(stage(A, 5))); await settle(); assert.match(textOf(f.render()), /5 ft/); f.h.dispose();
});

test("close, different source and unmount clear deadlines and suppress late headers and bodies", async () => {
  for (const phase of ["headers", "body"]) for (const exit of ["close", "source", "unmount"]) {
    const late = deferred(); let canceled = false;
    const response = new Response(new ReadableStream({ cancel() { canceled = true; } }));
    const f = await setup(() => phase === "headers" ? late.promise : Promise.resolve(response));
    if (exit === "close") f.render({ rightOpen:false }); else if (exit === "source") f.render({ sourceId:"census-counties" }); else f.h.dispose();
    await settle(); assert.equal(f.requests[0].options.signal.aborted, true); assert.equal(f.timers.size, 0);
    if (phase === "headers") late.resolve(response); await settle(); assert.equal(canceled, true); assert.equal(response.body.locked, false); f.h.dispose();
  }
});

test("HTTP, network, malformed, oversized and wrong-station responses retain recovery instead of false empty", async () => {
  for (const failure of ["http", "network", "malformed", "oversized", "identity"]) {
    let calls = 0;
    const f = await setup(() => {
      if (++calls > 1) { const empty = stage(); empty.observations = []; return Promise.resolve(Response.json(empty)); }
      if (failure === "network") return Promise.reject(new Error("offline"));
      return Promise.resolve(failure === "http" ? new Response("unavailable", { status:503 }) : failure === "malformed" ? new Response("{") : failure === "oversized" ? new Response("x".repeat(8 * 1024 * 1024 + 1)) : Response.json(stage(B)));
    });
    let tree = f.render(); assert.ok(findNode(tree, node => node.props?.role === "alert"), failure); assert.doesNotMatch(textOf(tree), /No measured gauge-height value/); assert.equal(f.timers.size, 0);
    action(tree).props.onClick(); f.render(); await settle(); tree = f.render(); assert.match(textOf(tree), /No measured gauge-height value was returned in this seven-day request/); assert.equal(action(tree).props.children, "Refresh gauge height"); f.h.dispose();
  }
});
