import assert from "node:assert/strict";
import { EventEmitter } from "node:events";
import test from "node:test";
import { mkdtemp, symlink, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import {
  createLocalQwenBridge,
  createLocalQwenDeadlineSignal,
  isDirectEntryPoint,
  isSensitiveQwenQuestion,
  LOCAL_EXPLORER_ORIGIN,
  LOCAL_PREVIEW_ORIGIN,
  LOCAL_QWEN_MODEL,
  LOCAL_QWEN_MODEL_DIGEST,
  readBoundedLocalQwenBody,
  SITE_ORIGIN,
} from "../scripts/local-qwen-bridge.mjs";
import {
  QWEN_LOCAL_ACCEPTED_REVIEW_STATE,
  QWEN_LOCAL_CONTEXT_WINDOW_TOKENS,
  QWEN_LOCAL_INTERPRETATION_SCHEMA,
  QWEN_LOCAL_KNOWLEDGE_VERSION,
  QWEN_LOCAL_MAX_INTERPRETATION_TOKENS,
  QWEN_LOCAL_MAX_OFFICIAL_SOURCES,
  QWEN_LOCAL_MAX_OUTPUT_TOKENS,
  QWEN_LOCAL_MAX_REQUEST_BYTES,
  QWEN_LOCAL_MODEL_RESPONSE_SCHEMA,
  QWEN_LOCAL_OLLAMA_MIN_VERSION,
  hasRequiredLocalQwenContext,
  inspectLocalQwenEvidence,
  localQwenAnswerHasOverPreciseLocation,
  localQwenAskEnvelope,
  localQwenHealthEnvelope,
  parseLocalQwenAskEnvelope,
} from "../scripts/qwen-local-contract.mjs";
import { QWEN_KNOWLEDGE_DIGEST } from "../scripts/qwen-knowledge.mjs";
import { hasSafeQwenContextShape } from "../app/qwen-context-safety.mjs";

test("direct startup follows the stable Site symlink without starting on import", async () => {
  const directory = await mkdtemp(join(tmpdir(), "kfm-bridge-alias-"));
  const moduleUrl = new URL("../scripts/local-qwen-bridge.mjs", import.meta.url);
  try {
    const alias = join(directory, "current.mjs");
    await symlink(fileURLToPath(moduleUrl), alias);
    assert.equal(isDirectEntryPoint(moduleUrl, alias), true);
    assert.equal(isDirectEntryPoint(moduleUrl, fileURLToPath(import.meta.url)), false);
    assert.equal(isDirectEntryPoint(moduleUrl, join(directory, "missing.mjs")), false);
  } finally { await rm(directory, { recursive: true, force: true }); }
});

const context = Object.freeze({
  camera: { center: [-98, 38.5], locationRedacted: true, zoom: 5, bearing: 0, pitch: 0, projection: "mercator", representation: "2D map" },
  basemap: { key: "terrain", title: "Terrain", note: "Context only" },
  time: { value: 2026, label: "2026", era: "present" },
  visibleLayers: [],
  officialSources: [{ id: "usgs", title: "USGS", selected: true, displayed: true, state: "ready", featureCount: 2, retrievedAt: null, evidenceRole: "EXTERNAL_CONTEXT_ONLY" }],
  telemetry: {
    authority: "SITE_LOCAL_REDACTED_DIAGNOSTIC",
    renderer: { state: "ready", styleLoaded: true, canvasReady: true, tilesLoaded: true, failedChecks: [] },
    registry: { total: 0, ready: 0, loading: 0, error: 0 },
    radar: { state: "idle", frameTime: null, manifestFresh: false },
    streamflow: { state: "idle", frameTime: null },
  },
  selection: null,
  nearbyContext: [],
});

const selectionContext = (evidenceState, evidenceReference, overrides = {}) => {
  const layer = {
    id: "layer-1",
    title: "Synthetic future-released fixture",
    domain: "Synthetic contract test",
    sourceType: "GeoJSON",
    releaseState: "RELEASED",
    publicStatus: "PUBLIC_SAFE",
    freshnessState: "CURRENT",
    evidenceReference,
    ...(overrides.layer ?? {}),
  };
  return {
    ...context,
    visibleLayers: overrides.visibleLayers ?? [layer],
    selection: {
      featureId: "feature-1",
      title: "Synthetic future-released feature",
      layerId: "layer-1",
      layerTitle: "Synthetic future-released fixture",
      domain: "Synthetic contract test",
      evidenceState,
      evidenceReference,
      reviewState: QWEN_LOCAL_ACCEPTED_REVIEW_STATE,
      releaseState: "RELEASED",
      sourceYear: 2026,
      spatialScope: "Synthetic test extent",
      summary: "A bounded synthetic future-release contract fixture; not a live record.",
      ...(overrides.selection ?? {}),
    },
  };
};

const ALL_SELECTION_EVIDENCE_STATES = [
  "ANSWER", "MISSING_EVIDENCE", "SOURCE_STALE", "GENERALIZED_GEOMETRY",
  "RESTRICTED_ACCESS", "DENIED_BY_POLICY", "CORRECTED", "SUPERSEDED", "ERROR",
];
const RESTRICTIVE_EVIDENCE_STATES = new Set(["RESTRICTED_ACCESS", "DENIED_BY_POLICY"]);

const restrictiveSelectionCases = () => {
  const reference = "kfm:evidence:synthetic:restriction-precedence";
  const cases = [];
  for (const evidenceState of ALL_SELECTION_EVIDENCE_STATES) {
    for (const selectionReleaseState of ["RELEASED", "RESTRICTED"]) {
      for (const layerReleaseState of ["RELEASED", "RESTRICTED"]) {
        for (const layerPublicStatus of ["PUBLIC_SAFE", "RESTRICTED"]) {
          if (!RESTRICTIVE_EVIDENCE_STATES.has(evidenceState)
            && selectionReleaseState !== "RESTRICTED"
            && layerReleaseState !== "RESTRICTED"
            && layerPublicStatus !== "RESTRICTED") continue;
          cases.push({
            label: [evidenceState, selectionReleaseState, layerReleaseState, layerPublicStatus].join(" / "),
            context: selectionContext(evidenceState, reference, {
              selection: { releaseState: selectionReleaseState },
              layer: { releaseState: layerReleaseState, publicStatus: layerPublicStatus },
            }),
          });
        }
      }
    }
  }
  return cases;
};

const restrictivePromptCarrierCases = () => {
  const reference = "kfm:evidence:synthetic:prompt-carrier";
  const released = selectionContext("ANSWER", reference);
  const releasedLayer = released.visibleLayers[0];
  const nearby = (evidenceState) => ({
    title: "Synthetic nearby feature",
    layerTitle: "Synthetic nearby layer",
    distanceMiles: 1,
    evidenceState,
  });
  return [
    {
      label: "context-only restricted visible-layer release",
      context: { ...context, visibleLayers: [{ ...releasedLayer, releaseState: "RESTRICTED" }] },
    },
    {
      label: "context-only restricted visible-layer public status",
      context: { ...context, visibleLayers: [{ ...releasedLayer, publicStatus: "RESTRICTED" }] },
    },
    {
      label: "context-only restricted nearby evidence",
      context: { ...context, nearbyContext: [nearby("RESTRICTED_ACCESS")] },
    },
    {
      label: "context-only policy-denied nearby evidence",
      context: { ...context, nearbyContext: [nearby("DENIED_BY_POLICY")] },
    },
    {
      label: "supported selection plus unrelated restricted visible layer",
      context: {
        ...released,
        visibleLayers: [
          ...released.visibleLayers,
          { ...releasedLayer, id: "unrelated-layer", title: "Unrelated restricted layer", releaseState: "RESTRICTED" },
        ],
      },
    },
    {
      label: "supported selection plus restricted nearby evidence",
      context: { ...released, nearbyContext: [nearby("DENIED_BY_POLICY")] },
    },
  ];
};

const modelContent = (disposition, answer, evidenceRefs = []) => JSON.stringify({
  disposition,
  answer,
  evidenceRefs,
});

const interpretationContent = (overrides = {}) => JSON.stringify({
  summary: "The view shows statewide USGS River Pulse context without a selected KFM record.",
  observations: ["USGS is selected and displayed with 2 features."],
  inferences: ["The gauges may help orient a river question."],
  gaps: ["A released EvidenceBundle for a selected reach."],
  followUps: ["Which watersheds have no active gauge?"],
  ...overrides,
});

const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/;
const withoutReceipt = (payload) => {
  const copy = { ...payload };
  delete copy.receipt;
  return copy;
};

/** Compare an ask reply to its finite envelope; receipts are per request, so check their shape separately. */
async function assertAskEnvelope(response, outcome, reasonCode, message, extras = {}) {
  const payload = await response.json();
  assert.notEqual(parseLocalQwenAskEnvelope(payload), null, message);
  assert.deepEqual(withoutReceipt(payload), withoutReceipt(localQwenAskEnvelope(outcome, reasonCode, extras)), message);
  assert.match(payload.receipt.requestId, UUID, message);
  return payload;
}

const readyOllamaResponse = (url) => {
  if (url.endsWith("/api/version")) return Response.json({ version: QWEN_LOCAL_OLLAMA_MIN_VERSION });
  if (url.endsWith("/api/tags")) {
    return Response.json({ models: [{ name: LOCAL_QWEN_MODEL, digest: LOCAL_QWEN_MODEL_DIGEST }] });
  }
  return null;
};

const withReadyOllama = (chatResponse) => async (url, options) =>
  readyOllamaResponse(url) ?? chatResponse(url, options);

const ollamaNetworkError = (code) => {
  const cause = new Error("private network detail");
  cause.code = code;
  const error = new TypeError("fetch failed");
  error.cause = cause;
  return error;
};

test("the bounded official-source contract accepts the complete registry and rejects overflow", () => {
  const complete = {
    ...context,
    officialSources: Array.from(
      { length: QWEN_LOCAL_MAX_OFFICIAL_SOURCES },
      (_, index) => ({ ...context.officialSources[0], id: `source-${index}` }),
    ),
  };
  assert.equal(QWEN_LOCAL_MAX_OFFICIAL_SOURCES, 48);
  assert.equal(hasSafeQwenContextShape(complete), true);
  assert.equal(hasRequiredLocalQwenContext(complete), true);
  const overflow = {
    ...complete,
    officialSources: [...complete.officialSources, { ...context.officialSources[0], id: "source-overflow" }],
  };
  assert.equal(hasSafeQwenContextShape(overflow), false);
  assert.equal(hasRequiredLocalQwenContext(overflow), false);

  const cameraWithoutRedactionMarker = { ...context.camera };
  delete cameraWithoutRedactionMarker.locationRedacted;
  const missingRedactionMarker = { ...context, camera: cameraWithoutRedactionMarker };
  assert.equal(hasSafeQwenContextShape(missingRedactionMarker), false);
  assert.equal(hasRequiredLocalQwenContext(missingRedactionMarker), false);
});

test("supported evidence requires one matching future-released visible layer and accepted feature review", () => {
  const reference = "kfm:evidence:synthetic:future-release-2026";
  const released = selectionContext("ANSWER", reference);
  assert.equal(inspectLocalQwenEvidence(released).disposition, "supported");
  assert.equal(inspectLocalQwenEvidence(selectionContext("ANSWER", reference, {
    layer: { publicStatus: "GENERALIZED" },
  })).disposition, "supported");

  for (const [label, candidate, disposition] of [
    ["absent visible layer", selectionContext("ANSWER", reference, { visibleLayers: [] }), "unsupported"],
    ["mismatched layer id", selectionContext("ANSWER", reference, {
      layer: { id: "different-layer" },
    }), "unsupported"],
    ["mismatched layer EvidenceRef", selectionContext("ANSWER", reference, {
      layer: { evidenceReference: "kfm:evidence:synthetic:different" },
    }), "unsupported"],
    ["unreleased layer", selectionContext("ANSWER", reference, {
      layer: { releaseState: "DEMONSTRATION" },
    }), "unsupported"],
    ["generalized but not released layer", selectionContext("ANSWER", reference, {
      layer: { releaseState: "GENERALIZED", publicStatus: "GENERALIZED" },
    }), "unsupported"],
    ["restricted layer", selectionContext("ANSWER", reference, {
      layer: { publicStatus: "RESTRICTED" },
    }), "withheld"],
    ["unreleased feature", selectionContext("ANSWER", reference, {
      selection: { releaseState: "DEMONSTRATION" },
    }), "unsupported"],
    ["restricted feature", selectionContext("ANSWER", reference, {
      selection: { releaseState: "RESTRICTED" },
    }), "withheld"],
    ["unreviewed feature", selectionContext("ANSWER", reference, {
      selection: { reviewState: "PENDING" },
    }), "unsupported"],
  ]) {
    assert.equal(inspectLocalQwenEvidence(candidate).disposition, disposition, label);
    assert.deepEqual(inspectLocalQwenEvidence(candidate).allowedEvidenceRefs, [], label);
  }

  for (const field of ["reviewState", "releaseState"]) {
    const candidate = selectionContext("ANSWER", reference);
    delete candidate.selection[field];
    assert.equal(hasSafeQwenContextShape(candidate), true, `missing selection ${field} has no undeclared fields`);
    assert.equal(hasRequiredLocalQwenContext(candidate), false, `missing selection ${field}`);
  }
  const layerWithoutReference = selectionContext("ANSWER", reference);
  delete layerWithoutReference.visibleLayers[0].evidenceReference;
  assert.equal(hasSafeQwenContextShape(layerWithoutReference), true);
  assert.equal(hasRequiredLocalQwenContext(layerWithoutReference), false);
});

test("every restrictive evidence and release combination takes deny precedence", () => {
  const cases = restrictiveSelectionCases();
  assert.equal(cases.length, 65);
  for (const scenario of [...cases, ...restrictivePromptCarrierCases()]) {
    const evidence = inspectLocalQwenEvidence(scenario.context);
    assert.equal(evidence.disposition, "withheld", scenario.label);
    assert.deepEqual(evidence.allowedEvidenceRefs, [], scenario.label);
    assert.equal(hasRequiredLocalQwenContext(scenario.context), true, scenario.label);
  }
});

async function withBridge(fetcher, exercise, options = {}) {
  const server = createLocalQwenBridge({ fetcher, ...options });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  try {
    await exercise(`http://127.0.0.1:${server.address().port}`);
  } finally {
    await new Promise((resolve) => server.close(resolve));
  }
}

const localFetch = (base, path, options = {}) => fetch(`${base}${path}`, {
  ...options,
  headers: { origin: SITE_ORIGIN, ...(options.headers ?? {}) },
});

test("health exposes only finite local-only states for the pinned qwen3:8b model", async () => {
  for (const [upstream, expectedStatus, expectedReason, expectedHttp] of [
    [async (url) => url.endsWith("/api/version")
      ? Response.json({ version: QWEN_LOCAL_OLLAMA_MIN_VERSION })
      : Response.json({ models: [{ name: LOCAL_QWEN_MODEL, digest: LOCAL_QWEN_MODEL_DIGEST.replace("sha256:", "") }] }), "ready", "READY", 200],
    [async (url) => url.endsWith("/api/version")
      ? Response.json({ version: QWEN_LOCAL_OLLAMA_MIN_VERSION })
      : Response.json({ models: [{ name: "other:latest", digest: LOCAL_QWEN_MODEL_DIGEST }] }), "model_missing", "MODEL_MISSING", 503],
    [async () => { throw ollamaNetworkError("ECONNREFUSED"); }, "ollama_unavailable", "OLLAMA_UNAVAILABLE", 503],
    [async () => { throw ollamaNetworkError("EHOSTUNREACH"); }, "ollama_unavailable", "OLLAMA_UNAVAILABLE", 503],
    [async () => { throw new Error("private upstream detail"); }, "error", "OLLAMA_RUNTIME_ERROR", 503],
    [async () => { throw new DOMException("probe timed out", "TimeoutError"); }, "error", "OLLAMA_RUNTIME_ERROR", 503],
    [async () => new Response("private failure", { status: 503 }), "error", "OLLAMA_RUNTIME_ERROR", 503],
    [async (url) => url.endsWith("/api/version")
      ? Response.json({ version: QWEN_LOCAL_OLLAMA_MIN_VERSION })
      : Response.json({ models: [{ name: LOCAL_QWEN_MODEL, digest: "sha256:" + "0".repeat(64) }] }), "error", "MODEL_DIGEST_MISMATCH", 503],
    [async (url) => url.endsWith("/api/version")
      ? Response.json({ version: "0.35.0" })
      : Response.json({ models: [{ name: LOCAL_QWEN_MODEL, digest: LOCAL_QWEN_MODEL_DIGEST }] }), "error", "OLLAMA_VERSION_MISMATCH", 503],
    [async (url) => url.endsWith("/api/version")
      ? new Response("{", { headers: { "content-type": "application/json" } })
      : Response.json({ models: [] }), "error", "OLLAMA_RUNTIME_ERROR", 503],
    [async (url) => url.endsWith("/api/version")
      ? Response.json({})
      : Response.json({ models: [] }), "error", "OLLAMA_RUNTIME_ERROR", 503],
    [async (url) => url.endsWith("/api/version")
      ? Response.json({ version: "not-semver" })
      : Response.json({ models: [] }), "error", "OLLAMA_RUNTIME_ERROR", 503],
    [async (url) => url.endsWith("/api/version")
      ? Response.json({ version: QWEN_LOCAL_OLLAMA_MIN_VERSION })
      : new Response("{", { headers: { "content-type": "application/json" } }), "error", "OLLAMA_RUNTIME_ERROR", 503],
    [async (url) => url.endsWith("/api/version")
      ? Response.json({ version: QWEN_LOCAL_OLLAMA_MIN_VERSION })
      : new Response("private failure", { status: 500 }), "error", "OLLAMA_RUNTIME_ERROR", 503],
    [async (url) => url.endsWith("/api/version")
      ? Response.json({ version: QWEN_LOCAL_OLLAMA_MIN_VERSION })
      : Response.json({ models: {} }), "error", "OLLAMA_RUNTIME_ERROR", 503],
    [async (url) => url.endsWith("/api/version")
      ? Response.json({ version: QWEN_LOCAL_OLLAMA_MIN_VERSION })
      : Response.json({ models: [{}] }), "error", "OLLAMA_RUNTIME_ERROR", 503],
    [async (url) => url.endsWith("/api/version")
      ? Response.json({ version: QWEN_LOCAL_OLLAMA_MIN_VERSION })
      : Response.json({ models: [{ name: "", digest: LOCAL_QWEN_MODEL_DIGEST }] }), "error", "OLLAMA_RUNTIME_ERROR", 503],
    [async (url) => url.endsWith("/api/version")
      ? Response.json({ version: QWEN_LOCAL_OLLAMA_MIN_VERSION })
      : Response.json({ models: [{ name: LOCAL_QWEN_MODEL, digest: "not-a-digest" }] }), "error", "OLLAMA_RUNTIME_ERROR", 503],
  ]) {
    await withBridge(upstream, async (base) => {
      const response = await localFetch(base, "/health");
      assert.equal(response.status, expectedHttp);
      assert.equal(response.headers.get("access-control-allow-origin"), SITE_ORIGIN);
      assert.equal(response.headers.get("cache-control"), "no-store");
      const payload = await response.json();
      assert.deepEqual(
        { ...payload, ollamaVersion: null },
        localQwenHealthEnvelope(expectedStatus, expectedReason, { knowledgeDigest: QWEN_KNOWLEDGE_DIGEST }),
      );
      assert.equal(payload.knowledgeVersion, QWEN_LOCAL_KNOWLEDGE_VERSION);
    });
  }
});

test("ask distinguishes unreachable Ollama from runtime probe faults", async () => {
  const supported = selectionContext("ANSWER", "kfm:evidence:synthetic:runtime-probe");
  for (const [upstream, expectedReason] of [
    [async () => { throw ollamaNetworkError("ENETUNREACH"); }, "OLLAMA_UNAVAILABLE"],
    [async () => { throw new Error("generic local runtime fault"); }, "OLLAMA_RUNTIME_ERROR"],
    [async () => new Response("service failure", { status: 500 }), "OLLAMA_RUNTIME_ERROR"],
    [async () => new Response("{", { headers: { "content-type": "application/json" } }), "OLLAMA_RUNTIME_ERROR"],
  ]) {
    await withBridge(upstream, async (base) => {
      const response = await localFetch(base, "/ask", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ question: "What does the selected feature support?", context: supported }),
      });
      assert.equal(response.status, 503);
      await assertAskEnvelope(response, "ERROR", expectedReason);
    });
  }
});

test("exact origins receive private-network preflight and foreign origins receive no CORS grant", async () => {
  await withBridge(withReadyOllama(async () => Response.json({})), async (base) => {
    for (const origin of [SITE_ORIGIN, LOCAL_PREVIEW_ORIGIN, LOCAL_EXPLORER_ORIGIN]) {
      const response = await fetch(`${base}/ask`, {
        method: "OPTIONS",
        headers: { origin, "access-control-request-private-network": "true" },
      });
      assert.equal(response.status, 204);
      assert.equal(response.headers.get("access-control-allow-origin"), origin);
      assert.equal(response.headers.get("access-control-allow-private-network"), "true");
    }
    for (const origin of ["https://other.test", "http://localhost:4173", "http://127.0.0.1:4174", "null"]) {
      const response = await fetch(`${base}/health`, { headers: { origin } });
      assert.equal(response.status, 403);
      assert.equal(response.headers.get("access-control-allow-origin"), null);
      assert.equal((await response.json()).reasonCode, "ORIGIN_NOT_ALLOWED");
    }
    assert.equal((await localFetch(base, "/health?probe=1")).status, 404);
    assert.equal((await localFetch(base, "/unknown")).status, 404);
  });
});

test("context-only questions reach Ollama with knowledge metadata and stay ABSTAIN interpretations", async () => {
  const calls = [];
  const logged = [];
  await withBridge(async (url, options) => {
    calls.push({ url, options });
    return readyOllamaResponse(url) ?? Response.json({
      message: { content: interpretationContent() },
      prompt_eval_count: 2048,
      eval_count: 96,
    });
  }, async (base) => {
    const response = await localFetch(base, "/ask", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "What do the river gauges in this view tell me?", context }),
    });
    assert.equal(response.status, 200);
    const payload = await assertAskEnvelope(response, "ABSTAIN", "CONTEXT_ONLY_INTERPRETATION", undefined, {
      interpretation: JSON.parse(interpretationContent()),
    });
    assert.equal(payload.answer, null);
    assert.deepEqual(payload.evidenceRefs, []);
    assert.equal(payload.authority, "INTERPRETIVE_ONLY");
    assert.equal(payload.receipt.profile, "context-interpretation-v1");
    assert.equal(payload.receipt.modelInvoked, true);
    assert.equal(payload.receipt.knowledgeDigest, QWEN_KNOWLEDGE_DIGEST);
    assert.equal(payload.receipt.knowledgeVersion, QWEN_LOCAL_KNOWLEDGE_VERSION);
    assert.ok(payload.receipt.knowledgeSourceIds.includes("usgs-streamflow"));
    assert.match(payload.receipt.contextSha256, /^sha256:[a-f0-9]{64}$/);
    assert.equal(payload.receipt.promptTokens, 2048);
    assert.equal(payload.receipt.outputTokens, 96);
  }, { logger: (entry) => logged.push(entry) });
  assert.equal(calls.length, 3);
  assert.equal(calls[2].url, "http://127.0.0.1:11434/api/chat");
  const sent = JSON.parse(calls[2].options.body);
  assert.deepEqual(sent.format, QWEN_LOCAL_INTERPRETATION_SCHEMA);
  assert.equal(sent.options.temperature, 0);
  assert.equal(sent.options.num_ctx, QWEN_LOCAL_CONTEXT_WINDOW_TOKENS);
  assert.equal(sent.options.num_predict, QWEN_LOCAL_MAX_INTERPRETATION_TOKENS);
  assert.equal(typeof sent.keep_alive, "string");
  assert.match(sent.messages[0].content, /not evidence about any place/);
  assert.match(sent.messages[1].content, /Prompt profile: context-interpretation-v1/);
  assert.match(sent.messages[1].content, /METADATA_NOT_EVIDENCE/);
  assert.match(sent.messages[1].content, /Discharge is not comparable across differently sized basins/);
  assert.match(sent.messages[1].content, /No KFM feature is selected/);
  assert.equal(logged.length, 1);
  assert.equal(logged[0].event, "kfm.qwen.request");
  assert.equal(logged[0].route, "/ask");
  assert.equal(logged[0].interpretation, true);
  assert.doesNotMatch(JSON.stringify(logged), /river gauges|statewide USGS River Pulse/);
});

test("sensitive questions abstain before any Ollama call", async () => {
  let calls = 0;
  await withBridge(async () => { calls++; throw new Error("must not call"); }, async (base) => {
    for (const question of ["Is it safe to swim here?", "Where should I dig for artifacts?", "Give me the GPS coordinates."]) {
      const response = await localFetch(base, "/ask", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ question, context }),
      });
      assert.equal(response.status, 200, question);
      const payload = await assertAskEnvelope(response, "ABSTAIN", "SENSITIVE_QUESTION_NOT_INTERPRETED", question);
      assert.equal(payload.receipt.modelInvoked, false);
    }
  });
  assert.equal(calls, 0);
  assert.equal(isSensitiveQwenQuestion("Which PUBLIC_SAFE layers are visible?"), false);
});

test("interpretations cannot carry EvidenceRefs, precise locations, or malformed shapes", async () => {
  for (const [content, status, outcome, reasonCode] of [
    [interpretationContent({ observations: ["Supported by kfm:evidence:invented"] }), 502, "ERROR", "UNDECLARED_EVIDENCE_REFERENCE"],
    [interpretationContent({ inferences: ["The gauge sits at 38.12345, -98.54321."] }), 200, "ABSTAIN", "OVER_PRECISE_OUTPUT"],
    [interpretationContent({ summary: "   " }), 502, "ERROR", "INVALID_MODEL_RESPONSE"],
    [JSON.stringify({ ...JSON.parse(interpretationContent()), extra: "field" }), 502, "ERROR", "INVALID_MODEL_RESPONSE"],
    [modelContent("UNSUPPORTED", "Wrong schema."), 502, "ERROR", "INVALID_MODEL_RESPONSE"],
  ]) {
    await withBridge(withReadyOllama(async () => Response.json({ message: { content } })), async (base) => {
      const response = await localFetch(base, "/ask", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ question: "What is visible?", context }),
      });
      assert.equal(response.status, status, content);
      const payload = await assertAskEnvelope(response, outcome, reasonCode, content);
      assert.equal(payload.interpretation, null);
      assert.doesNotMatch(JSON.stringify(payload), /invented|38\.12345/);
    });
  }
  // Grammar decoding may overrun list caps; the bridge trims instead of failing.
  await withBridge(withReadyOllama(async () => Response.json({ message: { content: interpretationContent({
    followUps: ["One?", "Two?", "Three?", "Four?", "Five?"],
  }) } })), async (base) => {
    const response = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "What is visible?", context }),
    });
    const payload = await response.json();
    assert.deepEqual(payload.interpretation.followUps, ["One?", "Two?", "Three?"]);
  });
});

test("supported answers must cite the exact declared EvidenceRef", async () => {
  const reference = "kfm:evidence:synthetic:atmo-2026";
  const supported = selectionContext("ANSWER", reference);
  const calls = [];
  await withBridge(async (url, options) => {
    calls.push({ url, options });
    return readyOllamaResponse(url) ?? Response.json({ message: { content: modelContent(
      "SUPPORTED",
      `The bounded selection is supported by ${reference}.`,
      [reference],
    ) } });
  }, async (base) => {
    const response = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "What does the selected feature support?", context: supported }),
    });
    assert.equal(response.status, 200);
    const payload = await response.json();
    assert.equal(payload.outcome, "ANSWER");
    assert.equal(payload.reasonCode, "SUPPORTED_SELECTION_INTERPRETATION");
    assert.deepEqual(payload.evidenceRefs, [reference]);
    assert.match(payload.answer, /Synthetic future-released feature: A bounded synthetic future-release contract fixture; not a live record\./);
    assert.match(payload.answer, /Spatial scope: Synthetic test extent\./);
    assert.match(payload.answer, /Source year: 2026\./);
    assert.match(payload.answer, /Release state: RELEASED\./);
    assert.match(payload.answer, /Review state: ACCEPTED\./);
    assert.match(payload.answer, new RegExp(`EvidenceRef: ${reference.replaceAll("/", "\\/")}`));
  });
  assert.equal(calls.length, 3);
  assert.equal(calls[0].url, "http://127.0.0.1:11434/api/version");
  assert.equal(calls[1].url, "http://127.0.0.1:11434/api/tags");
  assert.equal(calls[2].url, "http://127.0.0.1:11434/api/chat");
  const sent = JSON.parse(calls[2].options.body);
  assert.equal(sent.model, LOCAL_QWEN_MODEL);
  assert.equal(sent.stream, false);
  assert.equal(sent.think, false);
  assert.deepEqual(sent.tools, []);
  assert.deepEqual(sent.format, QWEN_LOCAL_MODEL_RESPONSE_SCHEMA);
  assert.equal(sent.options.temperature, 0);
  assert.equal(sent.options.num_predict, QWEN_LOCAL_MAX_OUTPUT_TOKENS);
  assert.equal(sent.options.num_ctx, QWEN_LOCAL_CONTEXT_WINDOW_TOKENS);
  assert.match(sent.messages[0].content, /answer field MUST end with the exact allowed EvidenceRef/);
  assert.match(sent.messages[1].content, /SITE_LOCAL_REDACTED_DIAGNOSTIC/);
  assert.match(sent.messages[1].content, new RegExp(`Allowed EvidenceRefs \\(exact strings only\\): \\["${reference}"\\]`));
  assert.match(sent.messages[1].content, new RegExp(`EvidenceRef: ${reference}`));
  assert.equal(calls[2].options.redirect, "error");
  assert.equal(calls.every((call) => call.options.signal instanceof AbortSignal), true);

  await withBridge(withReadyOllama(async () => Response.json({ message: { content: modelContent(
      "SUPPORTED",
      "The model omitted the required reference.",
    ) } })), async (base) => {
    const response = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "What does the selected feature support?", context: supported }),
    });
    await assertAskEnvelope(response, "ABSTAIN", "CITATION_REQUIRED");
  });
});

test("a model cannot replace the deterministic supported-selection answer with an invented claim", async () => {
  const reference = "kfm:evidence:synthetic:atmo-2026";
  const supported = selectionContext("ANSWER", reference);
  await withBridge(withReadyOllama(async () => Response.json({ message: { content: modelContent(
      "SUPPORTED",
      `The selected feature is a secret depot according to ${reference}.`,
      [reference],
    ) } })), async (base) => {
    const response = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "What does the selected feature support?", context: supported }),
    });
    const payload = await response.json();
    assert.equal(payload.outcome, "ANSWER");
    assert.doesNotMatch(payload.answer, /secret depot/);
    assert.match(payload.answer, /A bounded synthetic future-release contract fixture; not a live record/);
    assert.deepEqual(payload.evidenceRefs, [reference]);
  });
});

test("a positive model response cannot bridge a missing release-linked visible layer", async () => {
  const reference = "kfm:evidence:synthetic:future-release-2026";
  const unlinked = selectionContext("ANSWER", reference, { visibleLayers: [] });
  const formats = [];
  await withBridge(withReadyOllama(async (_url, options) => {
    formats.push(JSON.parse(options.body).format);
    return Response.json({ message: { content: interpretationContent() } });
  }), async (base) => {
    const response = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "What does the selected feature support?", context: unlinked }),
    });
    assert.equal(response.status, 200);
    const payload = await assertAskEnvelope(response, "ABSTAIN", "EVIDENCE_NOT_SUPPORTIVE", undefined, {
      interpretation: JSON.parse(interpretationContent()),
    });
    assert.equal(payload.answer, null);
    assert.deepEqual(payload.evidenceRefs, []);
  });
  // The unsupported selection only ever reaches the interpretation profile, never the citation gate.
  assert.deepEqual(formats, [QWEN_LOCAL_INTERPRETATION_SCHEMA]);
});

test("a cited model echo cannot turn an unrelated question into an ANSWER", async () => {
  const reference = "kfm:evidence:synthetic:atmo-2026";
  const supported = selectionContext("ANSWER", reference);
  const formats = [];
  // Even a model that echoes the allowed reference only produces an interpretation, which may not cite.
  await withBridge(withReadyOllama(async (_url, options) => {
    formats.push(JSON.parse(options.body).format);
    return Response.json({ message: { content: interpretationContent() } });
  }), async (base) => {
    for (const [label, question, candidate, reasonCode] of [
      ["unrelated weather", "What is today's statewide weather forecast?", supported, "QUESTION_OUTSIDE_SELECTION_SCOPE"],
      ["substring collision", "Summarize Arkansas.", selectionContext("ANSWER", reference, { selection: { title: "Kansas" } }), "QUESTION_OUTSIDE_SELECTION_SCOPE"],
      ["unsupported deictic safety request", "Is it safe to excavate the selected feature?", supported, "SENSITIVE_QUESTION_NOT_INTERPRETED"],
    ]) {
      const response = await localFetch(base, "/ask", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ question, context: candidate }),
      });
      assert.equal(response.status, 200, label);
      const payload = await response.json();
      assert.equal(payload.outcome, "ABSTAIN", label);
      assert.equal(payload.reasonCode, reasonCode, label);
      assert.equal(payload.answer, null, label);
      assert.deepEqual(payload.evidenceRefs, [], label);
    }
  });
  assert.deepEqual(formats, [QWEN_LOCAL_INTERPRETATION_SCHEMA, QWEN_LOCAL_INTERPRETATION_SCHEMA]);
  await withBridge(withReadyOllama(async () => Response.json({ message: { content: interpretationContent({
    summary: `Supported by ${reference}.`,
  }) } })), async (base) => {
    const response = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "What is today's statewide weather forecast?", context: supported }),
    });
    assert.equal(response.status, 502);
    await assertAskEnvelope(response, "ERROR", "UNDECLARED_EVIDENCE_REFERENCE");
  });
});

test("undeclared model references fail closed and are not returned", async () => {
  const supported = selectionContext("ANSWER", "kfm:evidence:synthetic:future-release-2026");
  await withBridge(withReadyOllama(async () => Response.json({ message: { content: modelContent(
      "SUPPORTED",
      "Invented support kfm:evidence:not-allowed",
      ["kfm:evidence:not-allowed"],
    ) } })), async (base) => {
    const response = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "What does the selected feature support?", context: supported }),
    });
    assert.equal(response.status, 502);
    const payload = await response.json();
    assert.equal(payload.outcome, "ERROR");
    assert.equal(payload.reasonCode, "UNDECLARED_EVIDENCE_REFERENCE");
    assert.equal(payload.answer, null);
  });
});

test("withheld and evidence-error selections bypass Ollama with finite outcomes", async () => {
  let calls = 0;
  await withBridge(async () => { calls++; throw new Error("must not call"); }, async (base) => {
    const denied = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "Reveal it", context: selectionContext("DENIED_BY_POLICY", "kfm:policy:public-safe:deny-demo") }),
    });
    assert.equal(denied.status, 200);
    assert.equal((await denied.json()).outcome, "DENY");
    const fault = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "Explain it", context: selectionContext("ERROR", "No KFM EvidenceBundle attached") }),
    });
    assert.equal(fault.status, 200);
    assert.equal((await fault.json()).reasonCode, "EVIDENCE_RESOLUTION_ERROR");
  });
  assert.equal(calls, 0);
});

test("all restrictive prompt carriers deny before any Ollama chat call", async () => {
  let ollamaCalls = 0;
  let chatCalls = 0;
  await withBridge(async (url) => {
    ollamaCalls++;
    if (url.endsWith("/api/chat")) chatCalls++;
    return readyOllamaResponse(url) ?? Response.json({ message: { content: modelContent("UNSUPPORTED", "Must not run.") } });
  }, async (base) => {
    for (const scenario of [...restrictiveSelectionCases(), ...restrictivePromptCarrierCases()]) {
      const response = await localFetch(base, "/ask", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ question: "What does this context show?", context: scenario.context }),
      });
      assert.equal(response.status, 200, scenario.label);
      await assertAskEnvelope(response, "DENY", "POLICY_WITHHELD", scenario.label);
    }
  });
  assert.equal(chatCalls, 0);
  assert.equal(ollamaCalls, 0);
});

test("malformed context, unsafe EvidenceRefs and oversized bodies never reach Ollama", async () => {
  let calls = 0;
  await withBridge(async () => { calls++; throw new Error("unexpected upstream request"); }, async (base) => {
    const cameraWithoutRedactionMarker = { ...context.camera };
    delete cameraWithoutRedactionMarker.locationRedacted;
    const invalidContexts = [
      { ...context, camera: cameraWithoutRedactionMarker },
      { ...context, camera: { ...context.camera, locationRedacted: "yes" } },
      { ...context, telemetry: { ...context.telemetry, privateToken: "DO_NOT_FORWARD" } },
      selectionContext("ANSWER", "No KFM EvidenceBundle attached"),
      selectionContext("ANSWER", "https://unreviewed.example/evidence"),
      { ...context, officialSources: Array.from({ length: QWEN_LOCAL_MAX_OFFICIAL_SOURCES + 1 }, () => context.officialSources[0]) },
      { ...context, credentials: "forbidden" },
    ];
    for (const invalid of invalidContexts) {
      const response = await localFetch(base, "/ask", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ question: "x", context: invalid }),
      });
      assert.equal(response.status, 400);
      assert.equal((await response.json()).reasonCode, "INVALID_REQUEST_SHAPE");
    }
    const oversized = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "x", context: { ...context, padding: "x".repeat(34 * 1024) } }),
    });
    assert.equal(oversized.status, 413);
    assert.equal((await oversized.json()).reasonCode, "INVALID_OR_OVERSIZED_REQUEST");
  });
  assert.equal(calls, 0);
});

test("upstream failures, oversized replies and concurrent requests stay finite", async () => {
  const supported = selectionContext("ANSWER", "kfm:evidence:synthetic:runtime-failures");
  const body = JSON.stringify({ question: "What does the selected feature support?", context: supported });
  await withBridge(async (url) => {
    const readiness = readyOllamaResponse(url);
    if (readiness) return readiness;
    throw new Error("PRIVATE_UPSTREAM_DETAIL");
  }, async (base) => {
    const response = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body,
    });
    assert.equal(response.status, 502);
    const text = await response.text();
    assert.match(text, /LOCAL_MODEL_UNAVAILABLE/);
    assert.doesNotMatch(text, /PRIVATE_UPSTREAM_DETAIL/);
  });

  await withBridge(withReadyOllama(async () => Response.json({
    message: { content: modelContent("UNSUPPORTED", "x".repeat(65 * 1024)) },
  })), async (base) => {
    const response = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body,
    });
    assert.equal(response.status, 502);
    assert.equal((await response.json()).outcome, "ERROR");
  });

  let release;
  const pending = new Promise((resolve) => { release = resolve; });
  await withBridge(withReadyOllama(async () => pending), async (base) => {
    const first = localFetch(base, "/ask", { method: "POST", headers: { "content-type": "application/json" }, body });
    await new Promise((resolve) => setTimeout(resolve, 10));
    const second = await localFetch(base, "/ask", { method: "POST", headers: { "content-type": "application/json" }, body });
    assert.equal(second.status, 429);
    assert.equal((await second.json()).reasonCode, "BRIDGE_BUSY");
    release(Response.json({ message: { content: modelContent("UNSUPPORTED", "Context only.") } }));
    assert.equal((await first).status, 200);
  });
});

test("a streaming non-2xx inference response is canceled before the finite error", async () => {
  let canceled = false;
  const supported = selectionContext("ANSWER", "kfm:evidence:synthetic:stream-failure");
  const failedStream = new ReadableStream({
    start(controller) { controller.enqueue(new TextEncoder().encode("private upstream error")); },
    cancel() { canceled = true; },
  });
  await withBridge(withReadyOllama(async () => new Response(failedStream, { status: 503 })), async (base) => {
    const response = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "What does the selected feature support?", context: supported }),
    });
    assert.equal(response.status, 502);
    await assertAskEnvelope(response, "ERROR", "LOCAL_MODEL_UNAVAILABLE");
  });
  assert.equal(canceled, true);
});

test("the one-request lock is acquired before a streamed request body finishes", async () => {
  await withBridge(withReadyOllama(async () => Response.json({
    message: { content: interpretationContent() },
  })), async (base) => {
    const encoded = new TextEncoder().encode(JSON.stringify({ question: "x", context }));
    let requestController;
    const requestStream = new ReadableStream({
      start(controller) {
        requestController = controller;
        controller.enqueue(encoded.slice(0, 8));
      },
    });
    const first = localFetch(base, "/ask", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: requestStream,
      duplex: "half",
    });
    await new Promise((resolve) => setTimeout(resolve, 10));
    const second = await localFetch(base, "/ask", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "x", context }),
    });
    assert.equal(second.status, 429);
    assert.equal((await second.json()).reasonCode, "BRIDGE_BUSY");
    requestController.enqueue(encoded.slice(8));
    requestController.close();
    assert.equal((await first).status, 200);
  });
});

test("request body and request deadline timers are finite", async () => {
  const declaredOversized = new EventEmitter();
  declaredOversized.headers = { "content-length": String(QWEN_LOCAL_MAX_REQUEST_BYTES + 1) };
  let oversizedResumed = false;
  declaredOversized.resume = () => { oversizedResumed = true; };
  await assert.rejects(
    readBoundedLocalQwenBody(declaredOversized),
    (error) => error?.message === "REQUEST_TOO_LARGE",
  );
  assert.equal(oversizedResumed, true);

  const request = new EventEmitter();
  request.headers = {};
  let resumed = false;
  request.resume = () => { resumed = true; };
  await assert.rejects(
    readBoundedLocalQwenBody(request, { timeoutMs: 20 }),
    (error) => error?.code === "REQUEST_TIMEOUT",
  );
  assert.equal(resumed, true);

  const deadline = createLocalQwenDeadlineSignal(20);
  await new Promise((resolve, reject) => {
    const guard = setTimeout(() => reject(new Error("deadline signal did not abort")), 250);
    deadline.addEventListener("abort", () => {
      clearTimeout(guard);
      resolve();
    }, { once: true });
  });
  assert.equal(deadline.aborted, true);
  assert.equal(deadline.reason?.name, "TimeoutError");
});

test("declared oversized bodies are drained before the bridge lock is released", async () => {
  await withBridge(withReadyOllama(async () => Response.json({ message: { content: interpretationContent() } })), async (base) => {
    const oversized = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: "x".repeat(QWEN_LOCAL_MAX_REQUEST_BYTES + 1),
    });
    assert.equal(oversized.status, 413);
    assert.equal((await oversized.json()).reasonCode, "INVALID_OR_OVERSIZED_REQUEST");

    const followup = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "What is visible?", context }),
    });
    assert.equal(followup.status, 200);
    assert.equal((await followup.json()).outcome, "ABSTAIN");
  });
});

test("bounded coordinate detection covers DMS and grid references without classifying street addresses", () => {
  for (const precise of [
    "38.12345, -98.54321",
    "38.12345 -98.54321",
    "38.12345° -98.54321°",
    "38.12345°-98.54321°",
    "-98.54321 38.12345",
    "38° 12′ 34.5″ N, 98° 32′ 45.6″ W",
    "98°32′45.6″W, 38°12′34.5″N",
    "38°12.575′N, 98°32.760′W",
    "98:32:45.6W, 38:12:34.5N",
    "14SQL1234567890",
    "14 S QL 12345 67890",
    "14S QL 12345 67890",
    "UTM zone 14S 450000 mE, 4260000 mN",
    "86F3QX2X+X4",
    "geohash 9yzu4jgz",
  ]) assert.equal(localQwenAnswerHasOverPreciseLocation(precise), true, precise);

  assert.equal(localQwenAnswerHasOverPreciseLocation("123 Main Street, Topeka, Kansas"), false);
  assert.equal(localQwenAnswerHasOverPreciseLocation("The values are 38.12345 and 2026.00000."), false);
});

test("unsupported prose and over-precise model output are never returned fluently", async () => {
  for (const [modelResponse, expectedReason] of [
    [modelContent("UNSUPPORTED", "Invented claim: a secret depot is present."), "MODEL_ABSTAINED"],
    [modelContent("SUPPORTED", "The selection is at 38.12345, -98.54321 and is supported by kfm:evidence:synthetic:atmo-2026.", ["kfm:evidence:synthetic:atmo-2026"]), "OVER_PRECISE_OUTPUT"],
  ]) {
    const safeContext = selectionContext("ANSWER", "kfm:evidence:synthetic:atmo-2026");
    await withBridge(withReadyOllama(async () => Response.json({ message: { content: modelResponse } })), async (base) => {
      const response = await localFetch(base, "/ask", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ question: "What does the selected feature support?", context: safeContext }),
      });
      assert.equal(response.status, 200);
      const payload = await response.json();
      assert.equal(payload.outcome, "ABSTAIN");
      assert.equal(payload.reasonCode, expectedReason);
      assert.equal(payload.answer, null);
      assert.deepEqual(payload.evidenceRefs, []);
      assert.doesNotMatch(JSON.stringify(payload), /secret depot|38\.12345|-98\.54321/);
    });
  }
});

test("deterministic projected answers are postvalidated for precision and undeclared references", async () => {
  const reference = "kfm:evidence:synthetic:atmo-2026";
  for (const [summary, expectedStatus, expectedReason, forbidden] of [
    ["The bounded selection is at 38.12345, -98.54321.", 200, "OVER_PRECISE_OUTPUT", /38\.12345|-98\.54321/],
    ["The bounded selection is at 38.12345 -98.54321.", 200, "OVER_PRECISE_OUTPUT", /38\.12345|-98\.54321/],
    ["The bounded selection is at 38.12345°-98.54321°.", 200, "OVER_PRECISE_OUTPUT", /38\.12345|-98\.54321/],
    ["The bounded selection is at 38° 12′ 34.5″ N, 98° 32′ 45.6″ W.", 200, "OVER_PRECISE_OUTPUT", /38°|98°/],
    ["The bounded selection is at 98°32′45.6″W, 38°12′34.5″N.", 200, "OVER_PRECISE_OUTPUT", /98°|38°/],
    ["The bounded selection is at 38°12.575′N, 98°32.760′W.", 200, "OVER_PRECISE_OUTPUT", /12\.575|32\.760/],
    ["The bounded selection is at 98:32:45.6W, 38:12:34.5N.", 200, "OVER_PRECISE_OUTPUT", /98:32|38:12/],
    ["The bounded selection is at MGRS 14S QL 12345 67890.", 200, "OVER_PRECISE_OUTPUT", /14S QL/],
    ["The bounded selection is at UTM zone 14S 450000 mE, 4260000 mN.", 200, "OVER_PRECISE_OUTPUT", /450000|4260000/],
    ["The bounded selection is at plus code 86F3QX2X+X4.", 200, "OVER_PRECISE_OUTPUT", /86F3QX2X/],
    ["The bounded selection is at geohash 9yzu4jgz.", 200, "OVER_PRECISE_OUTPUT", /9yzu4jgz/],
    ["The bounded selection mentions kfm:evidence:not-allowed.", 502, "UNDECLARED_EVIDENCE_REFERENCE", /not-allowed/],
  ]) {
    const supported = {
      ...selectionContext("ANSWER", reference),
      selection: { ...selectionContext("ANSWER", reference).selection, summary },
    };
    await withBridge(withReadyOllama(async () => Response.json({ message: { content: modelContent(
      "SUPPORTED",
      `The selected feature is supported by ${reference}.`,
      [reference],
    ) } })), async (base) => {
      const response = await localFetch(base, "/ask", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ question: "What does the selected feature support?", context: supported }),
      });
      assert.equal(response.status, expectedStatus);
      const payload = await response.json();
      assert.equal(payload.reasonCode, expectedReason, summary);
      assert.equal(payload.answer, null);
      assert.deepEqual(payload.evidenceRefs, []);
      assert.doesNotMatch(JSON.stringify(payload), forbidden);
    });
  }
});

test("plain text and extended model replies fail the structured response contract", async () => {
  const supported = selectionContext("ANSWER", "kfm:evidence:synthetic:invalid-model-response");
  for (const content of [
    "A plain unstructured answer.",
    JSON.stringify({ disposition: "UNSUPPORTED", answer: "No support.", evidenceRefs: [], extra: true }),
  ]) {
    await withBridge(withReadyOllama(async () => Response.json({ message: { content } })), async (base) => {
      const response = await localFetch(base, "/ask", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ question: "What does the selected feature support?", context: supported }),
      });
      assert.equal(response.status, 502);
      await assertAskEnvelope(response, "ERROR", "INVALID_MODEL_RESPONSE");
    });
  }
});

test("ask re-verifies the installed digest and never invokes a changed model", async () => {
  let chatCalls = 0;
  const supported = selectionContext("ANSWER", "kfm:evidence:synthetic:digest-check");
  await withBridge(async (url) => {
    if (url.endsWith("/api/version")) return Response.json({ version: QWEN_LOCAL_OLLAMA_MIN_VERSION });
    if (url.endsWith("/api/tags")) {
      return Response.json({ models: [{ name: LOCAL_QWEN_MODEL, digest: "sha256:" + "f".repeat(64) }] });
    }
    chatCalls++;
    return Response.json({ message: { content: "must not be returned" } });
  }, async (base) => {
    const response = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "What does the selected feature support?", context: supported }),
    });
    assert.equal(response.status, 503);
    const payload = await response.json();
    assert.equal(payload.outcome, "ERROR");
    assert.equal(payload.reasonCode, "MODEL_DIGEST_MISMATCH");
    assert.equal(payload.modelDigest, LOCAL_QWEN_MODEL_DIGEST);
  });
  assert.equal(chatCalls, 0);
});

test("Ollama releases at or above the tested floor are accepted; older ones are refused", async () => {
  for (const [version, expectedStatus] of [["0.35.1", "ready"], ["0.36.4", "ready"], ["1.2.0", "ready"], ["0.35.0", "error"], ["0.35.1-rc2", "error"]]) {
    await withBridge(async (url) => url.endsWith("/api/version")
      ? Response.json({ version })
      : Response.json({ models: [{ name: LOCAL_QWEN_MODEL, digest: LOCAL_QWEN_MODEL_DIGEST }] }), async (base) => {
      const payload = await (await localFetch(base, "/health")).json();
      assert.equal(payload.status, expectedStatus, version);
      assert.equal(payload.ollamaVersion, version);
    });
  }
});

test("ask re-verifies the Ollama runtime floor before tags or inference", async () => {
  const calls = [];
  const supported = selectionContext("ANSWER", "kfm:evidence:synthetic:version-check");
  await withBridge(async (url) => {
    calls.push(url);
    return Response.json({ version: "0.35.0" });
  }, async (base) => {
    const response = await localFetch(base, "/ask", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question: "What does the selected feature support?", context: supported }),
    });
    assert.equal(response.status, 503);
    await assertAskEnvelope(response, "ERROR", "OLLAMA_VERSION_MISMATCH");
  });
  assert.deepEqual(calls, ["http://127.0.0.1:11434/api/version"]);
});

test("bridge configuration cannot widen model, endpoint or origins", () => {
  assert.throws(() => createLocalQwenBridge({ model: "qwen3:latest" }), /pinned loopback endpoint and model/);
  assert.throws(() => createLocalQwenBridge({ ollamaUrl: "https://model.test" }), /pinned loopback endpoint and model/);
  assert.throws(() => createLocalQwenBridge({ allowedOrigins: [SITE_ORIGIN, "https://other.test"] }), /origin allowlist is fixed/);
});
