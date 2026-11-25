import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

// The 60-second poll can overlap a slow read; only the newest poll may commit.
async function loop() {
  const reads = [], ticks = [];
  const h = await componentHarness("app/lightning-flash-loop.tsx", {
    "./lightning-archive-control": { LightningArchiveControl: "archive" },
    "./lightning-year-control": { LightningYearControl: "year" },
    "./lightning-flashes": {
      GLM_FLASH_WINDOWS: [180], GLM_NOAA_SOURCE: "noaa",
      glmFlashPlaybackBounds: () => ({ start: 0, end: 1 }), glmFlashBins: () => [],
    },
    "./time-point-layer": { createTimePointLayer: () => ({}) },
    "./bounded-json": { readSuccessfulJson: response => response.json() },
  }, {
    fetch: () => new Promise((resolve, reject) => reads.push({ resolve, reject })),
    window: { setInterval: fn => { ticks.push(fn); return ticks.length; }, clearInterval() {} },
    document: { hidden: false, addEventListener() {}, removeEventListener() {} },
  });
  const props = { map: null, enabled: true, reducedMotion: true, onClose() {} };
  const render = () => { const tree = h.render(h.exports.LightningFlashLoop, props); h.commit(); return tree; };
  return { h, reads, ticks, render };
}
const snapshot = providerCount => ({ json: async () => ({
  evidenceRole: "EXTERNAL_CONTEXT_ONLY", source: "NOAA_GOES19_GLM_VIA_ATMOSTORM", windowMinutes: 180,
  flashes: [], state: "ready", providerCount, providerGeneratedAt: new Date().toISOString(),
}) });
const returned = tree => findNode(tree, n => n.type === "span" && [n.props.children].flat().includes(" returned"))?.props.children;

test("a slow earlier lightning poll cannot overwrite a newer snapshot", async () => {
  const { h, reads, ticks, render } = await loop();
  render(); render();
  assert.equal(reads.length, 1);
  void ticks[0](); // the next 60-second poll starts while the first read is still open
  assert.equal(reads.length, 2);
  reads[1].resolve(snapshot(2)); await settle();
  reads[0].resolve(snapshot(1)); await settle();
  const tree = render();
  assert.equal(tree.props["data-state"], "ready");
  assert.ok([returned(tree)].flat().includes(2), "the newer snapshot stays committed");
  h.dispose();
});

test("a failed earlier lightning poll does not replace a newer snapshot with an error", async () => {
  const { h, reads, ticks, render } = await loop();
  render(); render();
  void ticks[0]();
  reads[1].resolve(snapshot(3)); await settle();
  reads[0].reject(new Error("slow upstream")); await settle();
  const tree = render();
  assert.equal(tree.props["data-state"], "ready");
  assert.ok([returned(tree)].flat().includes(3));
  h.dispose();
});
