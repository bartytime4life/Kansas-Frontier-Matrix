import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const status = (extra = {}) => ({
  format: "kfm-hosted-source-status-v1", releaseState: "unreleased",
  state: "storage-not-configured", configured: false, limitBytes: 80_000_000_000,
  usedBytes: null, captures: null, lastTick: null,
  sources: [{ id: "usgs-streamflow", name: "USGS streamflow", intervalMs: 3_600_000, state: "not-configured" }],
  ...extra,
});
const text = node => node === null || node === undefined || typeof node === "boolean" ? ""
  : typeof node !== "object" ? String(node)
    : [node.props?.children].flat(Infinity).map(text).join(" ").replace(/\s+/g, " ").trim();

test("capture holds explain review, eligible retries and exhausted attempts without exposing provider text", async t => {
  const f = await fixture(t);
  const source = status().sources[0];
  const sources = [
    { ...source, id: 'review', state: 'quarantined' },
    { ...source, id: 'invalid', state: 'quarantined-invalid' },
    { ...source, id: 'retry', state: 'retry-held', attempts: 1, retryAt: 1_800_000_000_000, lastError: 'UPSTREAM_TIMEOUT' },
    { ...source, id: 'exhausted', state: 'retry-held', attempts: 3, retryAt: 1_900_000_000_000, lastError: 'private-provider-text' },
    { ...source, id: 'unknown', state: 'retry-held' },
  ];
  await f.reply(f.requests[0], status({ sources }));
  const output = text(f.render());
  assert.match(output, /approved release are still required/);
  assert.match(output, /validation issue before review/);
  assert.match(output, /source response timed out/);
  assert.match(output, /Retry eligible after 2027-01-15T08:00:00.000Z/);
  assert.match(output, /only when scheduling and storage permit/);
  assert.match(output, /exhausted its three attempts/);
  assert.match(output, /no specific reason was verified/);
  assert.match(output, /retry time has not been verified/);
  assert.doesNotMatch(output, /private-provider-text|2030-03/);
});

async function fixture(t) {
  const requests = [];
  const h = await componentHarness("app/hosted-source-status.tsx", { "next/link": { default: "a" } }, {
    fetch: (url, init) => new Promise((resolve, reject) => requests.push({ url, init, resolve, reject })),
  });
  t.after(() => h.dispose());
  const render = () => { const tree = h.render(h.exports.HostedSourceStatus, {}); h.commit(); return tree; };
  const reply = async (request, body) => { request.resolve({ ok: true, json: async () => body }); await settle(); };
  render();
  return { h, requests, render, reply, refresh: tree => findNode(tree, node => node.type === "button").props.onClick };
}

test("unknown archive totals stay unknown and capture does not imply a public release", async t => {
  const f = await fixture(t);
  assert.equal(f.requests.length, 1);
  assert.equal(f.requests[0].url, "/api/source-pipeline/status");
  assert.equal(f.requests[0].init.cache, "no-store");
  await f.reply(f.requests[0], status());
  const tree = f.render(), output = text(tree);
  assert.match(output, /Archive setup pending/);
  assert.match(output, /Archive limit 80 GB/);
  assert.match(output, /Stored Not verified/);
  assert.match(output, /Captures Not verified/);
  assert.match(output, /Last capture check Not yet recorded/);
  assert.match(output, /Archived captures remain private/);
  assert.match(output, /No verified capture/);
});

test("malformed HTTP-200 status cannot crash the source panel or claim archive totals", async t => {
  const f = await fixture(t);
  await f.reply(f.requests[0], {});
  let tree;
  assert.doesNotThrow(() => { tree = f.render(); });
  assert.match(text(tree), /Status unavailable/);
  assert.doesNotMatch(text(tree), /Archive limit|NaN| GB/);
  assert.equal(findNode(tree, node => node.type === "button").props.disabled, false);
});

test("manual refresh is cancelled on unmount and its late result cannot replace known status", async t => {
  const f = await fixture(t);
  await f.reply(f.requests[0], status({ captures: 2 }));
  f.refresh(f.render())();
  assert.ok(f.requests[1].init.signal, "manual refresh must carry the owned cancellation signal");
  f.h.dispose();
  assert.equal(f.requests[1].init.signal.aborted, true);
  await f.reply(f.requests[1], status({ captures: 99 }));
  assert.match(text(f.render()), /Captures 2/);
  assert.doesNotMatch(text(f.render()), /Captures 99/);
});

test("a superseded refresh cannot overwrite the newer response or end its loading state", async t => {
  const f = await fixture(t);
  await f.reply(f.requests[0], status({ captures: 1 }));
  const refresh = f.refresh(f.render());
  refresh(); refresh(); // Two activations before the disabled button is painted.
  assert.equal(f.requests.length, 3);
  assert.equal(f.requests[1].init.signal?.aborted, true, "the earlier refresh is superseded");
  f.requests[1].reject(new Error("private-provider-failure")); await settle();
  assert.equal(findNode(f.render(), node => node.type === "button").props.disabled, true);
  await f.reply(f.requests[2], status({ captures: 3 }));
  assert.match(text(f.render()), /Captures 3/);
  assert.doesNotMatch(text(f.render()), /Status unavailable|private-provider-failure/);
});

test("HTTP failure retains explicitly stale status and retry recovers without exposing errors", async t => {
  const f = await fixture(t);
  await f.reply(f.requests[0], status({ captures: 4 }));
  f.refresh(f.render())();
  f.requests[1].resolve({ ok: false, json: () => assert.fail("HTTP failure body must not be read") }); await settle();
  let tree = f.render();
  assert.match(text(tree), /Status unavailable/);
  assert.match(text(tree), /last verified response/i);
  assert.match(text(tree), /Captures 4/);
  f.refresh(tree)();
  await f.reply(f.requests[2], status({ captures: 5 }));
  tree = f.render();
  assert.match(text(tree), /Captures 5/);
  assert.doesNotMatch(text(tree), /Status unavailable|last verified response/i);
});

test("late success from a superseded read cannot replace the newest verified response", async t => {
  const f = await fixture(t);
  await f.reply(f.requests[0], status({ captures: 1 }));
  const refresh = f.refresh(f.render()); refresh(); refresh();
  await f.reply(f.requests[2], status({ captures: 7 }));
  await f.reply(f.requests[1], status({ captures: 6 })); // A transport may settle after abort.
  assert.match(text(f.render()), /Captures 7/);
  assert.doesNotMatch(text(f.render()), /Captures 6/);
});

for (const [name, change] of [
  ["wrong format", { format: "not-this-contract" }],
  ["released payload", { releaseState: "released" }],
  ["unknown archive state", { state: "approved" }],
  ["invalid configured marker", { configured: "true" }],
  ["nonfinite capacity", { limitBytes: Infinity }],
  ["negative stored bytes", { usedBytes: -1 }],
  ["fractional capture count", { captures: 1.5 }],
  ["invalid capture timestamp", { lastTick: 9e15 }],
  ["missing source list", { sources: undefined }],
  ["oversized source list", { sources: Array.from({ length: 33 }, (_, i) => ({ id: `source-${i}`, name: "Source", intervalMs: 1000, state: "not-captured" })) }],
  ["duplicate source identity", { sources: [status().sources[0], status().sources[0]] }],
  ["invalid source clock", { sources: [{ ...status().sources[0], checkedAt: -1 }] }],
  ["invalid retry clock", { sources: [{ ...status().sources[0], retryAt: -1 }] }],
  ["fractional attempts", { sources: [{ ...status().sources[0], attempts: 1.5 }] }],
  ["unbounded source name", { sources: [{ ...status().sources[0], name: "x".repeat(161) }] }],
]) {
  test(`status read rejects ${name} without turning it into archive evidence`, async t => {
    const f = await fixture(t);
    await f.reply(f.requests[0], status(change));
    let tree;
    assert.doesNotThrow(() => { tree = f.render(); });
    assert.match(text(tree), /Status unavailable/);
    assert.doesNotMatch(text(tree), /Archive limit|NaN| GB/);
  });
}

test("the displayed limit follows validated status and explicit zero totals remain zero", async t => {
  const f = await fixture(t);
  // Alternate fixture capacity verifies presentation, not a production setting change.
  await f.reply(f.requests[0], status({ limitBytes: 25_500_000_000, usedBytes: 0, captures: 0, lastTick: 0 }));
  const output = text(f.render());
  assert.match(output, /Archive limit 25\.5 GB/);
  assert.match(output, /Stored 0\.000 GB/);
  assert.match(output, /Captures 0/);
  assert.match(output, /1970-01-01 00:00:00 UTC/);
});
