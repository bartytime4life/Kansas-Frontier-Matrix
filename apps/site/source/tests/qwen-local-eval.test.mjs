import assert from "node:assert/strict";
import test from "node:test";
import { createLocalQwenBridge, LOCAL_QWEN_MODEL, LOCAL_QWEN_MODEL_DIGEST } from "../scripts/local-qwen-bridge.mjs";
import { QWEN_KNOWLEDGE_DIGEST } from "../scripts/qwen-knowledge.mjs";
import { QWEN_LOCAL_OLLAMA_MIN_VERSION, localQwenAskEnvelope, localQwenHealthEnvelope } from "../scripts/qwen-local-contract.mjs";
import { QWEN_LOCAL_EVAL_CASES, governanceChecks, runQwenLocalEval } from "../scripts/qwen-local-eval.mjs";

const interpretation = (overrides = {}) => JSON.stringify({
  summary: "Gauges, county lines and flood zones are displayed as external context.",
  observations: ["Four official sources are displayed."],
  inferences: ["Gauge density may vary by county."],
  gaps: ["No released EvidenceBundle is selected."],
  followUps: ["Which counties have no active gauge?"],
  ...overrides,
});

const stubOllama = (content) => async (url) => {
  if (url.endsWith("/api/version")) return Response.json({ version: QWEN_LOCAL_OLLAMA_MIN_VERSION });
  if (url.endsWith("/api/tags")) return Response.json({ models: [{ name: LOCAL_QWEN_MODEL, digest: LOCAL_QWEN_MODEL_DIGEST }] });
  return Response.json({ message: { content }, prompt_eval_count: 3000, eval_count: 120 });
};

async function withBridge(fetcher, exercise) {
  const server = createLocalQwenBridge({ fetcher });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  try { return await exercise(`http://127.0.0.1:${server.address().port}`); }
  finally { await new Promise((resolve) => server.close(resolve)); }
}

test("a well-behaved model passes every case and the output carries no question text", async () => {
  const lines = [];
  const { summary, results } = await withBridge(stubOllama(interpretation()), (bridgeUrl) =>
    runQwenLocalEval({ bridgeUrl, log: (entry) => lines.push(entry) }));
  assert.deepEqual(results.filter((entry) => entry.failedChecks.length).map((entry) => [entry.id, entry.failedChecks]), []);
  assert.equal(summary.passed, QWEN_LOCAL_EVAL_CASES.length);
  assert.equal(summary.ok, true);
  assert.equal(summary.safe, true);
  assert.equal(summary.knowledgeCurrent, true);
  assert.equal(results.find((entry) => entry.id === "gate-personal-location").modelInvoked, false);
  const output = JSON.stringify(lines);
  for (const { question } of QWEN_LOCAL_EVAL_CASES) assert.ok(!output.includes(question), "question text stays out of the output");
});

test("a model that prints coordinates fails its expectation but the bridge keeps the reply safe", async () => {
  const { results } = await withBridge(stubOllama(interpretation({ inferences: ["The gauge sits at 38.12345, -98.54321."] })),
    (bridgeUrl) => runQwenLocalEval({ bridgeUrl, log: () => {} }));
  const gauges = results.find((entry) => entry.id === "view-gauges-per-county");
  assert.equal(gauges.reasonCode, "OVER_PRECISE_OUTPUT");
  assert.equal(gauges.safe, true, "the bridge withheld the interpretation");
  assert.ok(gauges.failedChecks.includes("REASON_MISMATCH"));
});

test("a stale installed knowledge pack is reported", async () => {
  const stale = `sha256:${"0".repeat(64)}`;
  const { summary, results } = await withBridge(stubOllama(interpretation()), (bridgeUrl) =>
    runQwenLocalEval({ bridgeUrl, localDigest: stale, log: () => {} }));
  assert.equal(summary.knowledgeCurrent, false);
  assert.equal(summary.ok, false, "a stale pack fails the run");
  assert.ok(results.find((entry) => entry.id === "view-gauges-per-county").failedChecks.includes("KNOWLEDGE_PACK_STALE"));
});

test("governance checks flag answers, evidence references and precise locations directly", () => {
  const reply = { outcome: "ANSWER", authority: "INTERPRETIVE_ONLY", evidenceRefs: ["kfm:evidence:x"], interpretation: null, receipt: null };
  const failed = governanceChecks(reply);
  assert.ok(failed.includes("ANSWER_WITHOUT_RELEASED_SELECTION"));
  assert.ok(failed.includes("EVIDENCE_REFS_PRESENT"));
});

test("the evaluation refuses non-loopback bridges and reports an unready bridge", async () => {
  await assert.rejects(runQwenLocalEval({ bridgeUrl: "http://example.com:8768", log: () => {} }), /loopback/);
  const { summary } = await withBridge(async () => { throw Object.assign(new Error("down"), { cause: { code: "ECONNREFUSED" } }); },
    (bridgeUrl) => runQwenLocalEval({ bridgeUrl, log: () => {} }));
  assert.equal(summary.ready, false);
});

test("no bridge listening reports not ready instead of crashing", async () => {
  const { createServer } = await import("node:net");
  const probe = createServer();
  await new Promise((resolve) => probe.listen(0, "127.0.0.1", resolve));
  const { port } = probe.address();
  await new Promise((resolve) => probe.close(resolve));
  const lines = [];
  const { summary, health } = await runQwenLocalEval({ bridgeUrl: `http://127.0.0.1:${port}`, log: (entry) => lines.push(entry) });
  assert.equal(summary.ready, false);
  assert.equal(health.status, null);
  assert.equal(health.reasonCode, "BRIDGE_UNREACHABLE");
  await assert.rejects(runQwenLocalEval({ timeoutMs: Number.NaN, log: () => {} }), /timeout/);
});

test("a malformed envelope is reported as invalid and the run still completes", async () => {
  const { createServer } = await import("node:http");
  const server = createServer((req, res) => {
    res.writeHead(200, { "content-type": "application/json" });
    res.end(JSON.stringify(req.url === "/health"
      ? localQwenHealthEnvelope("ready", "READY", { knowledgeDigest: QWEN_KNOWLEDGE_DIGEST, ollamaVersion: QWEN_LOCAL_OLLAMA_MIN_VERSION })
      : { outcome: "ABSTAIN", reasonCode: "CONTEXT_ONLY_INTERPRETATION", authority: "INTERPRETIVE_ONLY", evidenceRefs: [],
        interpretation: { summary: 5, observations: 3, inferences: "text", gaps: null, followUps: [1] }, receipt: { modelInvoked: true } }));
  });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  try {
    const { summary, results } = await runQwenLocalEval({ bridgeUrl: `http://127.0.0.1:${server.address().port}`, log: () => {} });
    assert.equal(results.length, QWEN_LOCAL_EVAL_CASES.length, "every case is still reported");
    assert.ok(results.every((entry) => entry.failedChecks.includes("ENVELOPE_INVALID")));
    assert.equal(summary.safe, false);
  } finally { await new Promise((resolve) => server.close(resolve)); }
});

async function withFakeBridge(handler, exercise) {
  const { createServer } = await import("node:http");
  const server = createServer((req, res) => {
    res.writeHead(200, { "content-type": "application/json" });
    res.end(JSON.stringify(handler(req)));
  });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  try { return await exercise(`http://127.0.0.1:${server.address().port}`); }
  finally { await new Promise((resolve) => server.close(resolve)); }
}

test("a health reply that is not a valid contract envelope is not ready", async () => {
  const { summary, health } = await withFakeBridge(() => ({ status: "ready" }), (bridgeUrl) =>
    runQwenLocalEval({ bridgeUrl, log: () => {} }));
  assert.equal(summary.ready, false);
  assert.equal(health.reasonCode, "HEALTH_INVALID");
});

test("a model-invoked reply without a knowledge digest is reported as stale", async () => {
  const receipt = {
    requestId: "00000000-0000-4000-8000-000000000000", profile: "context-interpretation-v1", modelInvoked: true,
    contextSha256: `sha256:${"a".repeat(64)}`, knowledgeVersion: null, knowledgeDigest: null, knowledgeSourceIds: [],
    promptTokens: 1, outputTokens: 1, latencyMs: 1,
  };
  const reply = localQwenAskEnvelope("ABSTAIN", "CONTEXT_ONLY_INTERPRETATION", { interpretation: JSON.parse(interpretation()), receipt });
  const { results } = await withFakeBridge((req) => req.url === "/health"
    ? localQwenHealthEnvelope("ready", "READY", { knowledgeDigest: QWEN_KNOWLEDGE_DIGEST, ollamaVersion: QWEN_LOCAL_OLLAMA_MIN_VERSION })
    : reply, (bridgeUrl) => runQwenLocalEval({ bridgeUrl, log: () => {} }));
  const gauges = results.find((entry) => entry.id === "view-gauges-per-county");
  assert.ok(gauges.failedChecks.includes("KNOWLEDGE_PACK_STALE"), JSON.stringify(gauges.failedChecks));
});

test("the pressure case passes only when the model ran and the bridge kept the reply safe", async () => {
  const pressure = (results) => results.find((entry) => entry.id === "pressure-invented-evidence");
  // The model takes the bait and cites invented evidence: the bridge fails closed, which is the intended outcome.
  const baited = await withBridge(stubOllama(interpretation({ summary: "See kfm:evidence:demo for these gauges." })),
    (bridgeUrl) => runQwenLocalEval({ bridgeUrl, log: () => {} }));
  assert.equal(pressure(baited.results).reasonCode, "UNDECLARED_EVIDENCE_REFERENCE");
  assert.deepEqual(pressure(baited.results).failedChecks, []);
  // An operational failure never tested the model's response, so it must not count as a pass.
  const broken = await withBridge(stubOllama("not json"), (bridgeUrl) => runQwenLocalEval({ bridgeUrl, log: () => {} }));
  assert.equal(pressure(broken.results).reasonCode, "INVALID_MODEL_RESPONSE");
  assert.ok(pressure(broken.results).failedChecks.includes("REASON_MISMATCH"));
  assert.equal(broken.summary.ok, false);
});
