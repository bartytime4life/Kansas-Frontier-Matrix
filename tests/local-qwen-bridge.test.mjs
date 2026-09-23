import assert from "node:assert/strict";
import test from "node:test";
import { createLocalQwenBridge, LOCAL_PREVIEW_ORIGIN, LOCAL_QWEN_MODEL, SITE_ORIGIN } from "../scripts/local-qwen-bridge.mjs";

const context = {
  camera: { center: [-98, 38.5], zoom: 5, locationRedacted: true },
  basemap: { key: "terrain", title: "Terrain", note: "Context only" },
  time: { value: 2026, label: "2026", era: "present" },
  visibleLayers: [],
  officialSources: [{ id: "usgs", title: "USGS", selected: true, displayed: true, state: "ready", featureCount: 2, retrievedAt: null, evidenceRole: "EXTERNAL_CONTEXT_ONLY" }],
  telemetry: { authority: "SITE_LOCAL_REDACTED_DIAGNOSTIC", renderer: { state: "ready" } },
  selection: null,
  nearbyContext: [],
};

async function withBridge(fetcher, exercise) {
  const server = createLocalQwenBridge({ fetcher });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  try {
    await exercise(`http://127.0.0.1:${server.address().port}`);
  } finally {
    await new Promise((resolve) => server.close(resolve));
  }
}

test("local bridge grants the exact Site origin and fixed installed model", async () => {
  const calls = [];
  await withBridge(async (url, options) => {
    calls.push({ url, options });
    if (url.endsWith("/api/tags")) return Response.json({ models: [{ name: LOCAL_QWEN_MODEL }] });
    return Response.json({ message: { content: "The supplied map shows a selected USGS context source." } });
  }, async (base) => {
    const health = await fetch(`${base}/health`, { headers: { origin: SITE_ORIGIN } });
    assert.equal(health.status, 200);
    assert.equal(health.headers.get("access-control-allow-origin"), SITE_ORIGIN);
    assert.equal(health.headers.get("cache-control"), "no-store");
    assert.deepEqual(await health.json(), { status: "ready", model: LOCAL_QWEN_MODEL });
    const preflight = await fetch(`${base}/ask`, { method: "OPTIONS", headers: { origin: SITE_ORIGIN, "access-control-request-private-network": "true" } });
    assert.equal(preflight.status, 204);
    assert.equal(preflight.headers.get("access-control-allow-private-network"), "true");
    const answer = await fetch(`${base}/ask`, { method: "POST", headers: { origin: SITE_ORIGIN, "content-type": "application/json" }, body: JSON.stringify({ question: "What is visible?", context }) });
    assert.equal(answer.status, 200);
    assert.equal((await answer.json()).status, "ok");
    const localHealth = await fetch(`${base}/health`, { headers: { origin: LOCAL_PREVIEW_ORIGIN } });
    assert.equal(localHealth.status, 200);
    assert.equal(localHealth.headers.get("access-control-allow-origin"), LOCAL_PREVIEW_ORIGIN);
    const localPreflight = await fetch(`${base}/ask`, { method: "OPTIONS", headers: { origin: LOCAL_PREVIEW_ORIGIN, "access-control-request-private-network": "true" } });
    assert.equal(localPreflight.status, 204);
    assert.equal(localPreflight.headers.get("access-control-allow-origin"), LOCAL_PREVIEW_ORIGIN);
    const localAnswer = await fetch(`${base}/ask`, { method: "POST", headers: { origin: LOCAL_PREVIEW_ORIGIN, "content-type": "application/json" }, body: JSON.stringify({ question: "What is visible?", context }) });
    assert.equal(localAnswer.status, 200);
    assert.equal(localAnswer.headers.get("access-control-allow-origin"), LOCAL_PREVIEW_ORIGIN);
    assert.equal((await localAnswer.json()).status, "ok");
  });
  assert.equal(calls.length, 4);
  assert.equal(calls[1].url, "http://127.0.0.1:11434/api/chat");
  const sent = JSON.parse(calls[1].options.body);
  assert.equal(sent.model, LOCAL_QWEN_MODEL);
  assert.equal(sent.stream, false);
  assert.match(sent.messages[1].content, /SITE_LOCAL_REDACTED_DIAGNOSTIC/);
  assert.equal(calls[1].options.redirect, "error");
});

test("local bridge rejects other origins and malformed context without reaching Ollama", async () => {
  let calls = 0;
  await withBridge(async () => { calls++; throw new Error("Unexpected upstream request"); }, async (base) => {
    const foreign = await fetch(`${base}/ask`, { method: "POST", headers: { origin: "https://other.test", "content-type": "application/json" }, body: JSON.stringify({ question: "x", context }) });
    assert.equal(foreign.status, 403);
    assert.equal(foreign.headers.get("access-control-allow-origin"), SITE_ORIGIN);
    const malformed = await fetch(`${base}/ask`, { method: "POST", headers: { origin: SITE_ORIGIN, "content-type": "application/json" }, body: JSON.stringify({ question: "x", context: { ...context, telemetry: { authority: "UNVERIFIED" } } }) });
    assert.equal(malformed.status, 400);
    const oversized = await fetch(`${base}/ask`, { method: "POST", headers: { origin: SITE_ORIGIN, "content-type": "application/json" }, body: JSON.stringify({ question: "x", context: { ...context, padding: "x".repeat(34 * 1024) } }) });
    assert.equal(oversized.status, 413);
  });
  assert.equal(calls, 0);
});
