import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compile = async (name, replacements = {}) => {
  let source = await readFile(new URL(`../app/${name}`, import.meta.url), "utf8");
  for (const [from, to] of Object.entries(replacements)) source = source.replaceAll(`"${from}"`, `"${to}"`);
  return `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 }, fileName: name,
  }).outputText).toString("base64")}`;
};
const boundedUrl = await compile("bounded-json.ts");
const { readBoundedJson, JsonLimitError } = await import(boundedUrl);
const qwenContractUrl = new URL("../scripts/qwen-local-contract.mjs", import.meta.url).href;
const qwenContextUrl = await compile("qwen-context.ts", {
  "../scripts/qwen-local-contract.mjs": qwenContractUrl,
  "./qwen-context-safety.mjs": new URL("../app/qwen-context-safety.mjs", import.meta.url).href,
});
const {
  buildCopyableQwenPrompt,
  policyPreservingQwenSample,
} = await import(qwenContextUrl);
const { inspectLocalQwenEvidence } = await import(qwenContractUrl);
const { POST } = await import(await compile("api/qwen/route.ts", {
  "../../bounded-json": boundedUrl,
  "../../qwen-context": qwenContextUrl,
  "../../qwen-context-safety.mjs": new URL("../app/qwen-context-safety.mjs", import.meta.url).href,
}));
const request = (body, headers = {}) => new Request("https://site.test/api/qwen", {
  method: "POST", headers: { "content-type": "application/json", ...headers }, body: JSON.stringify(body),
});

test("streaming JSON enforces actual bytes and cancels without reading to EOF", async () => {
  let canceled = false;
  let pulls = 0;
  const response = new Response(new ReadableStream({
    pull(controller) { pulls++; controller.enqueue(new TextEncoder().encode("x".repeat(40))); },
    cancel() { canceled = true; },
  }), { headers: { "content-length": "1" } });
  await assert.rejects(readBoundedJson(response, 64), JsonLimitError);
  assert.equal(canceled, true);
  assert.ok(pulls <= 3);
  assert.deepEqual(await readBoundedJson(new Response('{"x":"é"}'), 10), { x: "é" });
  await assert.rejects(readBoundedJson(new Response('{"x":"é"}'), 9), JsonLimitError);
  await assert.rejects(readBoundedJson(new Response(Uint8Array.of(0xff)), 8));
});

test("the hosted Qwen route stays dormant and fail closed with zero upstream calls", async () => {
  const keys = ["KFM_QWEN_MODE", "QWEN_ENDPOINT", "QWEN_OLLAMA_URL", "OLLAMA_BASE_URL", "QWEN_API_KEY", "QWEN_MODEL", "OLLAMA_MODEL"];
  const saved = Object.fromEntries(keys.map((key) => [key, process.env[key]]));
  const originalFetch = globalThis.fetch;
  let calls = 0;
  globalThis.fetch = async () => { calls++; throw new Error("NETWORK MUST NOT RUN"); };
  try {
    process.env.KFM_QWEN_MODE = "hosted";
    process.env.QWEN_ENDPOINT = "https://model.test";
    process.env.QWEN_API_KEY = "must-not-be-used";
    for (const body of [null, [], true, "x", {}, { question: "x" }, { question: "x", endpoint: "https://other.test" }]) {
      const response = await POST(request(body));
      assert.equal(response.status, 503, JSON.stringify(body));
      assert.equal(response.headers.get("cache-control"), "no-store");
      const text = await response.text();
      assert.match(text, /Hosted Qwen is disabled/);
      assert.doesNotMatch(text, /must-not-be-used|model\.test/);
    }
    assert.equal((await POST(request({ question: "x" }, { origin: "https://other.test" }))).status, 403);
    assert.equal(calls, 0);
  } finally {
    globalThis.fetch = originalFetch;
    for (const key of keys) { if (saved[key] === undefined) delete process.env[key]; else process.env[key] = saved[key]; }
  }
});

test("Qwen bounded sampling preserves deny-significant records beyond both caps", () => {
  const publicLayer = (index) => ({
    id: `layer-${index}`,
    title: `Layer ${index}`,
    domain: "TEST",
    sourceType: "FIXTURE",
    releaseState: "RELEASED",
    publicStatus: "PUBLIC_SAFE",
    freshnessState: "CURRENT",
    evidenceReference: `kfm:test/layer-${index}`,
  });
  const visibleLayers = Array.from({ length: 15 }, (_, index) => publicLayer(index));
  visibleLayers[14] = { ...visibleLayers[14], releaseState: "RESTRICTED", publicStatus: "RESTRICTED" };
  const sampledLayers = policyPreservingQwenSample(
    visibleLayers,
    14,
    (layer) => layer.releaseState === "RESTRICTED" || layer.publicStatus === "RESTRICTED",
  );
  assert.equal(sampledLayers.length, 14);
  assert.equal(sampledLayers.some((layer) => layer.id === "layer-14"), true);
  assert.equal(inspectLocalQwenEvidence({
    selection: null,
    visibleLayers: sampledLayers,
    nearbyContext: [],
  }).disposition, "withheld");

  const nearbyContext = Array.from({ length: 9 }, (_, index) => ({
    title: `Nearby ${index}`,
    layerTitle: "Layer",
    distanceMiles: index,
    evidenceState: index === 8 ? "DENIED_BY_POLICY" : "ANSWER",
  }));
  const sampledNearby = policyPreservingQwenSample(
    nearbyContext,
    8,
    (item) => item.evidenceState === "RESTRICTED_ACCESS" || item.evidenceState === "DENIED_BY_POLICY",
  );
  assert.equal(sampledNearby.length, 8);
  assert.equal(sampledNearby.some((item) => item.title === "Nearby 8"), true);
  assert.equal(inspectLocalQwenEvidence({
    selection: null,
    visibleLayers: [],
    nearbyContext: sampledNearby,
  }).disposition, "withheld");
});

test("copied Qwen prompts include system rules and redact denied or unsupported selections", () => {
  const evidenceReference = "kfm:test/released-feature";
  const layer = {
    id: "released-layer",
    title: "Released layer",
    domain: "TEST",
    sourceType: "FIXTURE",
    releaseState: "RELEASED",
    publicStatus: "PUBLIC_SAFE",
    freshnessState: "CURRENT",
    evidenceReference,
  };
  const selection = {
    featureId: "released-feature",
    title: "Released feature",
    layerId: layer.id,
    layerTitle: layer.title,
    domain: layer.domain,
    evidenceState: "ANSWER",
    evidenceReference,
    reviewState: "ACCEPTED",
    releaseState: "RELEASED",
    sourceYear: 2026,
    spatialScope: "STATEWIDE",
    summary: "Released fixture summary",
  };
  const context = {
    camera: { center: [-98.4, 38.5], locationRedacted: true, zoom: 6, bearing: 0, pitch: 0, projection: "mercator", representation: "2D map" },
    basemap: { key: "standard", title: "Standard", note: "Context only" },
    time: { value: 2026, label: "2026", era: "Present" },
    visibleLayers: [layer],
    officialSources: [],
    telemetry: {
      authority: "SITE_LOCAL_REDACTED_DIAGNOSTIC",
      renderer: { state: "ready", styleLoaded: true, canvasReady: true, tilesLoaded: true, failedChecks: [] },
      registry: { total: 1, ready: 1, loading: 0, error: 0 },
      radar: { state: "idle", frameTime: null, manifestFresh: false },
      streamflow: { state: "idle", frameTime: null },
    },
    selection,
    nearbyContext: [],
  };
  const supported = buildCopyableQwenPrompt("What supports Released feature?", context);
  assert.match(supported, /System rules: You are the Qwen contextual companion/);
  assert.match(supported, /What supports Released feature\?/);
  assert.match(supported, /kfm:test\/released-feature/);

  const sensitiveQuestion = "Describe PRIVATE_QUESTION_TOKEN at 39.12345, -96.54321";
  const denied = buildCopyableQwenPrompt(sensitiveQuestion, {
    ...context,
    camera: { ...context.camera, center: [-96.54321, 39.12345], locationRedacted: false },
    visibleLayers: [{ ...layer, title: "PRIVATE_LAYER_TOKEN", releaseState: "RESTRICTED", publicStatus: "RESTRICTED", evidenceReference: "kfm:private/layer-token" }],
    selection: {
      ...selection,
      title: "PRIVATE_SELECTION_TOKEN",
      layerTitle: "PRIVATE_LAYER_TOKEN",
      evidenceState: "RESTRICTED_ACCESS",
      evidenceReference: "kfm:private/feature-token",
      releaseState: "RESTRICTED",
      summary: "PRIVATE_SUMMARY_TOKEN",
    },
  });
  assert.match(denied, /Copy outcome: DENY/);
  assert.match(denied, /Reason: POLICY_WITHHELD/);
  assert.match(denied, /System rules: You are the Qwen contextual companion/);
  for (const sensitive of [
    "PRIVATE_QUESTION_TOKEN", "PRIVATE_LAYER_TOKEN", "PRIVATE_SELECTION_TOKEN",
    "PRIVATE_SUMMARY_TOKEN", "kfm:private", "39.12345", "-96.54321",
  ]) assert.doesNotMatch(denied, new RegExp(sensitive.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")));

  const unsupported = buildCopyableQwenPrompt("UNSUPPORTED_QUESTION_TOKEN", {
    ...context,
    selection: {
      ...selection,
      title: "UNSUPPORTED_SELECTION_TOKEN",
      evidenceState: "MISSING_EVIDENCE",
      evidenceReference: "No KFM EvidenceBundle attached",
      reviewState: "PENDING",
      releaseState: "DEMONSTRATION",
      summary: "UNSUPPORTED_SUMMARY_TOKEN",
    },
  });
  assert.match(unsupported, /Copy outcome: ABSTAIN/);
  assert.match(unsupported, /Reason: EVIDENCE_NOT_SUPPORTIVE/);
  assert.doesNotMatch(unsupported, /UNSUPPORTED_(?:QUESTION|SELECTION|SUMMARY)_TOKEN/);

  const incompleteRenderer = { ...context.telemetry.renderer };
  delete incompleteRenderer.tilesLoaded;
  const missingNested = buildCopyableQwenPrompt("MISSING_NESTED_QUESTION_TOKEN", {
    ...context,
    telemetry: { ...context.telemetry, renderer: incompleteRenderer },
  });
  assert.match(missingNested, /Copy outcome: ERROR/);
  assert.match(missingNested, /Reason: EVIDENCE_RESOLUTION_ERROR/);
  assert.doesNotMatch(missingNested, /MISSING_NESTED_QUESTION_TOKEN|kfm:test\/released-feature/);

  const extraNested = buildCopyableQwenPrompt("EXTRA_NESTED_QUESTION_TOKEN", {
    ...context,
    camera: { ...context.camera, privateNote: "EXTRA_NESTED_PRIVATE_TOKEN" },
  });
  assert.match(extraNested, /Copy outcome: ERROR/);
  assert.match(extraNested, /Reason: EVIDENCE_RESOLUTION_ERROR/);
  assert.doesNotMatch(extraNested, /EXTRA_NESTED_(?:QUESTION|PRIVATE)_TOKEN|kfm:test\/released-feature/);
});

test("the repository status route rejects oversized chunked responses", async () => {
  const { GET } = await import(await compile("api/repository-status/route.ts", { "../../bounded-json": boundedUrl, "../../repository-status": await compile("repository-status.ts") }));
  const originalFetch = globalThis.fetch;
  let canceled = false;
  globalThis.fetch = async () => new Response(new ReadableStream({
    pull(controller) { controller.enqueue(new Uint8Array(256 * 1024)); },
    cancel() { canceled = true; },
  }));
  try {
    const response = await GET();
    assert.equal(response.status, 502);
    assert.equal(canceled, true);
    assert.equal((await response.json()).state, "error");
  } finally { globalThis.fetch = originalFetch; }
});
