import assert from "node:assert/strict";
import test from "node:test";
import { createLocalQwenBridge, LOCAL_QWEN_MODEL, LOCAL_QWEN_MODEL_DIGEST } from "../scripts/local-qwen-bridge.mjs";
import { QWEN_LOCAL_OLLAMA_MIN_VERSION } from "../scripts/qwen-local-contract.mjs";
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
