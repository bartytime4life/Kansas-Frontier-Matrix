import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";
import { makePlan, acquire, replay } from "../app/api-connections-runtime/connections.mjs";

const imports = { "next/link": { default: "a" }, "next/dynamic": { default: () => "connection-map" }, "../connection-series": { VALUE_COLUMNS: {}, series: () => [] }, "./connections.css": {} };
const receipt = () => ({ captureId: "a".repeat(64), sourceId: "noaa-ncei", retrievedAt: "2026-11-19T12:00:00Z", byteLength: 100, entityBytes: 50, sha256: "b".repeat(64), validation: "structure-valid", partial: false, query: {}, limitation: "Fixture", entityHashes: [] });
const result = () => ({ cached: false, receipt: receipt(), view: { sourceId: "noaa-ncei", query: {}, rows: [{ value: 1 }], total: 1, partial: false, retrievedAt: receipt().retrievedAt, limitation: "Fixture", releaseState: "unreleased" } });
const source = id => ({ id, name: id, kind: "table", fields: [], configured: true, missing: [], holds: [], state: "ready", docs: "https://example.test/", limitation: "Fixture", limitBytes: 1000, releaseState: "unreleased" });
const catalog = { owner: true, sources: [source("noaa-ncei"), source("usdm-statistics")], host: { state: "ready", configured: true, paused: false, host: "Fixture", usedBytes: 0, limitBytes: 1000 } };
const response = body => ({ ok: true, json: async () => body });
const panel = tree => findNode(tree, node => node.props?.["aria-label"] === "Verified capture");
const message = tree => findNode(tree, node => node.props?.["aria-live"] === "polite").props.children;
async function setup(capture, history = []) {
  const h = await componentHarness("app/connections/workspace.tsx", imports, { fetch: async (url, options) => url.includes("action=view") || options?.method === "POST" ? capture(url, options) : response(url.includes("action=captures") ? { captures: history } : catalog) });
  const render = () => { const tree = h.render(h.exports.default, {}); h.commit(); return tree; };
  render(); await settle(); await settle();
  return { h, render, submit: () => findNode(render(), node => node.type === "form").props.onSubmit({ preventDefault() {} }) };
}

test("malformed successful captures cannot install a verified panel and a valid retry recovers", async () => {
  const bad = [null, [], {}, { ...result(), view: null }, { ...result(), receipt: null },
    { ...result(), cached: "true" }, { ...result(), view: { ...result().view, rows: null } },
    { ...result(), view: { ...result().view, rows: [null] } }, { ...result(), view: { ...result().view, total: "1" } },
    { ...result(), view: { ...result().view, partial: "false" } }, { ...result(), view: { ...result().view, query: null } },
    { ...result(), view: { ...result().view, features: [null] } },
    { ...result(), view: { ...result().view, features: [{ type: "Feature", properties: {}, geometry: { type: "Point", coordinates: [NaN, 38] } }] } },
    { ...result(), view: { ...result().view, raster: { bbox: [0], width: 768, height: 768, vintage: "Fixture", acquiredAt: null } } },
  ];
  for (const value of bad) {
    let attempts = 0;
    const { h, render, submit } = await setup(async () => response(++attempts === 1 ? value : result()));
    try {
      submit(); await settle(); let tree = render();
      assert.equal(panel(tree), undefined); assert.match(message(tree), /invalid.*retry/i);
      assert.equal(findNode(tree, node => node.type === "button" && node.props.children === "Capture selected query").props.disabled, false);
      submit(); await settle(); tree = render(); assert.ok(panel(tree));
      assert.match(message(tree), /Stored bytes verified/);
    } finally { h.dispose(); }
  }
});

test("source, query, validation and timestamp contradictions cannot become verified capture results", async () => {
  const bad = [
    { ...result(), view: { ...result().view, sourceId: "usdm-statistics" } },
    { ...result(), receipt: { ...receipt(), sourceId: "usdm-statistics" } },
    { ...result(), receipt: { ...receipt(), query: { product: "wrong" } } },
    { ...result(), receipt: { ...receipt(), validation: "invalid" } },
    { ...result(), receipt: { ...receipt(), captureId: "not-an-id" } },
    { ...result(), view: { ...result().view, retrievedAt: "2020-01-01T00:00:00Z" } },
    { ...result(), view: { ...result().view, releaseState: "published" } },
  ];
  for (const value of bad) {
    const { h, render, submit } = await setup(async () => response(value));
    try { submit(); await settle(); const tree = render(); assert.equal(panel(tree), undefined); assert.match(message(tree), /invalid.*retry/i); }
    finally { h.dispose(); }
  }
});

test("saved replay binds the returned receipt to the capture the owner chose", async () => {
  let mismatch = true;
  const { h, render } = await setup(async () => response({ ...result(), receipt: { ...receipt(), captureId: mismatch ? "c".repeat(64) : receipt().captureId } }), [receipt()]);
  try {
    const replayButton = tree => findNode(tree, node => node.type === "button" && node.props.children === "Replay capture");
    replayButton(render()).props.onClick(); await settle(); let tree = render();
    assert.equal(panel(tree), undefined); assert.match(message(tree), /invalid.*retry/i);
    mismatch = false; replayButton(tree).props.onClick(); await settle(); tree = render();
    assert.ok(panel(tree));
    assert.ok(findNode(tree, node => node.type === "a" && node.props.href === `/api/connections?action=bundle&id=${receipt().captureId}`));
  } finally { h.dispose(); }
});

test("non-JSON errors retain a useful message without exposing parser exceptions", async () => {
  const { h, render, submit } = await setup(async () => ({ ok: false, json: async () => { throw new SyntaxError("Unexpected token < private gateway body"); } }));
  try {
    submit(); await settle(); const tree = render(); assert.equal(panel(tree), undefined);
    assert.match(message(tree), /request is held/i); assert.doesNotMatch(message(tree), /Unexpected token|private gateway/);
  } finally { h.dispose(); }
});

test("a real server acquisition and replay remains displayable with its normalized query and receipt", async () => {
  const plan = await makePlan("usdm-statistics", {}, 1704067200000);
  const captured = await acquire(plan, { fetcher: async () => Response.json([{ stateAbbreviation: "KS", statisticFormatID: Number(plan.query.mode), d0: 12 }]) });
  const value = await replay(captured);
  const { h, render, submit } = await setup(async () => response({ view: value.view, receipt: value.receipt }));
  try {
    const tree = render();
    findNode(tree, node => node.type === "button" && findNode(node, child => child.type === "strong" && child.props.children === "usdm-statistics")).props.onClick();
    submit(); await settle(); const rendered = render(); assert.ok(panel(rendered));
    assert.match(message(rendered), /Stored bytes verified/);
  } finally { h.dispose(); }
});
