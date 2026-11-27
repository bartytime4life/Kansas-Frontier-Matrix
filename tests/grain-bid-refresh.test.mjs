import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const report = {
  state: "available",
  sourceId: "usda-kansas-grain-bids",
  format: "kfm-kansas-grain-bids-v1",
  sourceUrl: "https://www.ams.usda.gov/mnreports/ams_2886.pdf",
  unit: "USD/bu",
  releaseId: "a".repeat(64),
  payloadSha256: "b".repeat(64),
  reportDate: "2026-11-25",
  retrievedAt: "2026-11-26T00:00:00.000Z",
  approvalExpiresAt: "2026-11-27T00:00:00.000Z",
  rows: [{ crop: "Corn", region: "Central", low: 4, high: 5, average: 4.5 }],
};

async function market(t) {
  const calls = [];
  const timers = new Map();
  const document = new EventTarget();
  document.visibilityState = "visible";
  const window = new EventTarget();
  class TestDate extends Date { static now() { return Date.parse("2026-11-26T12:00:00Z"); } }
  const harness = await componentHarness("app/field-decision-tools.tsx", {
    "./bounded-json": { readBoundedJson: response => response.json() },
    "./yield-history": { yieldHistory: () => null },
    "./rain-normal": {}, "./moon": {}, "./sun-chart": {}, "./frost-dates": {},
  }, {
    document, window, Date: TestDate,
    fetch(url, options) {
      return new Promise(resolve => calls.push({ url, ...options, resolve }));
    },
    setTimeout(callback, delay) {
      const id = Symbol();
      timers.set(id, { callback, delay });
      return id;
    },
    clearTimeout(id) { timers.delete(id); },
  }, "\nexport { MarketBudget };");
  t.after(() => harness.dispose());

  function render() {
    const tree = harness.render(harness.exports.MarketBudget, { harvests: "", setHarvests() {} });
    harness.commit();
    return tree;
  }
  function toggle(open) {
    const details = { open };
    render().props.onToggle({ target: details, currentTarget: details });
    return render();
  }
  function hasRelease(tree) {
    return Boolean(findNode(tree, node => node.type === "a" && node.props.children === "Download the reviewed price data"));
  }
  function recheck() {
    const [id, timer] = [...timers].find(([, { delay }]) => delay === 60_000);
    timers.delete(id);
    timer.callback();
  }
  const first = toggle(true);
  assert.equal(calls.length, 0);
  findNode(first, node => node.props?.children === "Load reviewed Kansas bids").props.onClick();
  render();
  assert.equal(calls.length, 1);
  assert.equal(calls[0].cache, "no-store");
  calls[0].resolve(Response.json(report));
  await settle();
  assert.equal(hasRelease(render()), true);
  return { calls, timers, document, window, render, toggle, hasRelease, recheck };
}

test("rechecks a viewed release and withholds the selected price during a check and after withdrawal", async t => {
  const view = await market(t);
  function enter(label, value) {
    const field = findNode(view.render(), node => node.type === "label" && node.props.children?.includes(label));
    const input = findNode(field, node => typeof node.props?.onChange === "function");
    input.props.onChange({ target: { value } });
  }
  enter("Price source", "Central");
  enter("Expected yield (bu/ac)", "100");
  enter("Other costs ($/ac)", "100");
  const hasRange = tree => Boolean(findNode(tree, node => node.type === "p" && node.props.children?.includes("Reported range $")));
  const hasBudget = tree => Boolean(findNode(tree, node => node.type === "caption" && node.props.children === "Return above entered costs at the selected bid"));
  assert.equal(hasRange(view.render()), true);
  assert.equal(hasBudget(view.render()), true);

  view.recheck();
  const pending = view.render();
  assert.equal(view.calls.length, 2);
  assert.equal(view.hasRelease(pending), false);
  assert.equal(hasRange(pending), false);
  assert.equal(hasBudget(pending), false);
  view.calls[1].resolve(Response.json({ state: "withheld", reason: "RELEASE_WITHDRAWN" }));
  await settle();
  assert.equal(view.hasRelease(view.render()), false);
  assert.equal(hasRange(view.render()), false);
  assert.equal(hasBudget(view.render()), false);
});

test("suspends hidden and closed bids, aborts in-flight reads, and verifies again on resume", async t => {
  const view = await market(t);
  view.recheck();
  view.render();
  view.document.visibilityState = "hidden";
  view.document.dispatchEvent(new Event("visibilitychange"));
  assert.equal(view.hasRelease(view.render()), false);
  assert.equal(view.calls[1].signal.aborted, true);
  assert.equal(view.timers.size, 0);

  view.document.visibilityState = "visible";
  view.document.dispatchEvent(new Event("visibilitychange"));
  assert.equal(view.hasRelease(view.render()), false);
  assert.equal(view.calls.length, 3);
  view.calls[1].resolve(Response.json(report));
  await settle();
  assert.equal(view.hasRelease(view.render()), false);

  view.toggle(false);
  assert.equal(view.calls[2].signal.aborted, true);
  assert.equal(view.hasRelease(view.toggle(true)), false);
  assert.equal(view.calls.length, 4);
  view.calls[3].resolve(Response.json(report));
  await settle();
  assert.equal(view.hasRelease(view.render()), true);

  view.window.dispatchEvent(new Event("pagehide"));
  assert.equal(view.hasRelease(view.render()), false);
  view.window.dispatchEvent(new Event("pageshow"));
  assert.equal(view.hasRelease(view.render()), false);
  assert.equal(view.calls.length, 5);
});

test("opening or closing a nested tool preserves the current reviewed bid", async t => {
  const view = await market(t);
  for (const open of [true, false]) {
    view.render().props.onToggle({ target: { open }, currentTarget: { open: true } });
    assert.equal(view.hasRelease(view.render()), true);
    assert.equal(view.calls.length, 1);
  }
});
