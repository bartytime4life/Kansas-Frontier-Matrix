/** Non-secret, local-only contract shared by the Qwen bridge and its tests. */
export const QWEN_LOCAL_CONTRACT_VERSION = "kfm-qwen-local-v2";
export const QWEN_LOCAL_BRIDGE_VERSION = "2.0.0";
export const QWEN_LOCAL_MODE = "local-only";
export const QWEN_LOCAL_MODEL = "qwen3:8b";
export const QWEN_LOCAL_MODEL_DIGEST = "sha256:500a1f067a9f782620b40bee6f7b0c89e17ae61f686b92c24933e4ca4b2b8b41";
export const QWEN_LOCAL_MODEL_FORMAT = "GGUF";
export const QWEN_LOCAL_MODEL_QUANTIZATION = "Q4_K_M";
export const QWEN_LOCAL_MODEL_PARAMETERS = "8.2B";
// Ollama.app updates itself, so an exact runtime pin breaks the companion on
// the next update. The tested release is a floor; the model digest stays exact.
export const QWEN_LOCAL_OLLAMA_MIN_VERSION = "0.35.1";
export const QWEN_LOCAL_OLLAMA_ORIGIN = "http://127.0.0.1:11434";
export const QWEN_LOCAL_BRIDGE_PORT = 8768;
export const QWEN_LOCAL_BRIDGE_ORIGIN = `http://127.0.0.1:${QWEN_LOCAL_BRIDGE_PORT}`;
export const QWEN_LOCAL_MAX_REQUEST_BYTES = 32 * 1024;
export const QWEN_LOCAL_MAX_REPLY_BYTES = 64 * 1024;
export const QWEN_LOCAL_MAX_OUTPUT_TOKENS = 512;
export const QWEN_LOCAL_MAX_INTERPRETATION_TOKENS = 900;
// Ollama silently drops the start of a prompt (the system rules) when it
// exceeds the runtime's default window, so the window is always explicit.
export const QWEN_LOCAL_CONTEXT_WINDOW_TOKENS = 16_384;
export const QWEN_LOCAL_KEEP_ALIVE = "15m";
// Bytes of map context plus knowledge metadata sent with an interpretation.
// JSON averages roughly 3.5 bytes per token, so 44 KiB leaves room inside the
// window for the system rules, instructions and the interpretation itself.
export const QWEN_LOCAL_INTERPRETATION_PROMPT_BUDGET_BYTES = 44 * 1024;
export const QWEN_LOCAL_KNOWLEDGE_VERSION = "kfm-qwen-knowledge-v1";
export const QWEN_LOCAL_BODY_TIMEOUT_MS = 5_000;
export const QWEN_LOCAL_HEALTH_TIMEOUT_MS = 5_000;
// The browser allows the companion's bounded Ollama probe to finish and return
// a classified health envelope before applying its own transport deadline.
export const QWEN_LOCAL_BROWSER_HEALTH_TIMEOUT_MS = 7_500;
export const QWEN_LOCAL_INFERENCE_TIMEOUT_MS = 90_000;
export const QWEN_LOCAL_REQUEST_DEADLINE_MS = 92_000;
export const QWEN_LOCAL_ASK_TIMEOUT_MS = 95_000;
export const QWEN_LOCAL_SITE_ORIGIN = "https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site";
export const QWEN_LOCAL_PREVIEW_ORIGIN = "http://127.0.0.1:5173";
export const QWEN_LOCAL_EXPLORER_ORIGIN = "http://127.0.0.1:4173";
export const QWEN_LOCAL_MAX_OFFICIAL_SOURCES = 48;
export const QWEN_LOCAL_ACCEPTED_REVIEW_STATE = "ACCEPTED";
export const QWEN_LOCAL_ALLOWED_ORIGINS = Object.freeze([
  QWEN_LOCAL_SITE_ORIGIN,
  QWEN_LOCAL_PREVIEW_ORIGIN,
  QWEN_LOCAL_EXPLORER_ORIGIN,
]);

export const QWEN_HEALTH_STATUSES = Object.freeze([
  "ready",
  "model_missing",
  "ollama_unavailable",
  "error",
]);
export const QWEN_ASK_OUTCOMES = Object.freeze(["ANSWER", "ABSTAIN", "DENY", "ERROR"]);
export const QWEN_ASK_REASON_CODES = Object.freeze({
  ANSWER: Object.freeze(["SUPPORTED_SELECTION_INTERPRETATION"]),
  ABSTAIN: Object.freeze([
    "CITATION_REQUIRED",
    "CONTEXT_ONLY_INTERPRETATION",
    "EVIDENCE_NOT_SUPPORTIVE",
    "MODEL_ABSTAINED",
    "OVER_PRECISE_OUTPUT",
    "QUESTION_OUTSIDE_SELECTION_SCOPE",
    "SENSITIVE_QUESTION_NOT_INTERPRETED",
  ]),
  DENY: Object.freeze(["ORIGIN_NOT_ALLOWED", "POLICY_WITHHELD"]),
  ERROR: Object.freeze([
    "BRIDGE_BUSY",
    "EVIDENCE_RESOLUTION_ERROR",
    "INVALID_MODEL_RESPONSE",
    "INVALID_OR_OVERSIZED_REQUEST",
    "INVALID_REQUEST_SHAPE",
    "JSON_REQUEST_REQUIRED",
    "LOCAL_MODEL_UNAVAILABLE",
    "MODEL_DIGEST_MISMATCH",
    "MODEL_MISSING",
    "OLLAMA_VERSION_MISMATCH",
    "OLLAMA_RUNTIME_ERROR",
    "OLLAMA_UNAVAILABLE",
    "REQUEST_TIMEOUT",
    "ROUTE_NOT_FOUND",
    "UNDECLARED_EVIDENCE_REFERENCE",
  ]),
});
/** ABSTAIN reasons that may carry a model interpretation; nothing else may. */
export const QWEN_INTERPRETABLE_ABSTAIN_REASONS = Object.freeze([
  "CONTEXT_ONLY_INTERPRETATION",
  "EVIDENCE_NOT_SUPPORTIVE",
  "QUESTION_OUTSIDE_SELECTION_SCOPE",
]);
export const QWEN_PROMPT_PROFILES = Object.freeze([
  "none",
  "selection-gate-v1",
  "context-interpretation-v1",
]);
export const NO_EVIDENCE_REFERENCE = "No KFM EvidenceBundle attached";

const SEMVER = /^(\d+)\.(\d+)\.(\d+)(?:-([0-9A-Za-z.-]+))?(?:\+[0-9A-Za-z.-]+)?$/;
/** True when a reported Ollama release is at or above the tested floor. */
export function isSupportedOllamaVersion(version, minimum = QWEN_LOCAL_OLLAMA_MIN_VERSION) {
  const found = typeof version === "string" ? SEMVER.exec(version) : null;
  const floor = SEMVER.exec(minimum);
  if (!found || !floor) return false;
  for (let part = 1; part <= 3; part++) {
    const difference = Number(found[part]) - Number(floor[part]);
    if (difference !== 0) return difference > 0;
  }
  // A pre-release of the floor itself (0.35.1-rc0) predates the tested release.
  return found[4] === undefined || floor[4] !== undefined;
}

const EVIDENCE_STATES = new Set([
  "ANSWER", "MISSING_EVIDENCE", "SOURCE_STALE", "GENERALIZED_GEOMETRY",
  "RESTRICTED_ACCESS", "DENIED_BY_POLICY", "CORRECTED", "SUPERSEDED", "ERROR",
]);
const SUPPORTED_EVIDENCE_STATES = new Set(["ANSWER", "CORRECTED"]);
const WITHHELD_EVIDENCE_STATES = new Set(["RESTRICTED_ACCESS", "DENIED_BY_POLICY"]);
const KFM_EVIDENCE_REFERENCE = /^kfm:(?:\/\/)?[A-Za-z0-9][A-Za-z0-9._~:/-]{0,511}$/;

const record = (value) => value !== null && typeof value === "object" && !Array.isArray(value);
const own = (value, key) => Object.hasOwn(value, key);
const required = (value, keys) => record(value) && keys.every((key) => own(value, key));
const text = (value) => typeof value === "string" && value.trim().length > 0 && value.length <= 2048;
const number = (value) => typeof value === "number" && Number.isFinite(value);
const count = (value) => Number.isInteger(value) && value >= 0;
const nullableText = (value) => value === null || text(value);
const tuple = (value, size) => Array.isArray(value) && value.length === size && value.every(number);

export const isKfmEvidenceReference = (value) =>
  typeof value === "string" && KFM_EVIDENCE_REFERENCE.test(value);

/**
 * Resolve the evidence posture without trusting the model. Unsupported and
 * withheld selections never become evidence-bearing answers.
 */
export function inspectLocalQwenEvidence(context) {
  if (!record(context) || !own(context, "selection")) {
    return Object.freeze({ ok: false, disposition: "invalid", allowedEvidenceRefs: Object.freeze([]) });
  }
  const visibleLayers = Array.isArray(context.visibleLayers) ? context.visibleLayers : [];
  const restrictiveVisibleLayer = visibleLayers.some((layer) =>
    layer?.releaseState === "RESTRICTED" || layer?.publicStatus === "RESTRICTED");
  const restrictiveNearbyContext = Array.isArray(context.nearbyContext)
    && context.nearbyContext.some((item) => WITHHELD_EVIDENCE_STATES.has(item?.evidenceState));
  if (context.selection === null) {
    return Object.freeze({
      ok: true,
      disposition: restrictiveVisibleLayer || restrictiveNearbyContext ? "withheld" : "context-only",
      allowedEvidenceRefs: Object.freeze([]),
    });
  }
  const selection = context.selection;
  if (!record(selection) || !EVIDENCE_STATES.has(selection.evidenceState)) {
    return Object.freeze({ ok: false, disposition: "invalid", allowedEvidenceRefs: Object.freeze([]) });
  }
  const linkedLayers = visibleLayers.filter((layer) => layer?.id === selection.layerId);
  const restrictiveSelection = WITHHELD_EVIDENCE_STATES.has(selection.evidenceState)
    || selection.releaseState === "RESTRICTED";
  // A restrictive posture always takes precedence over support, absence, or an
  // evidence-resolution fault. No model may reinterpret a deny as an answer.
  if (restrictiveSelection || restrictiveVisibleLayer || restrictiveNearbyContext) {
    return Object.freeze({ ok: true, disposition: "withheld", allowedEvidenceRefs: Object.freeze([]) });
  }
  const reference = selection.evidenceReference;
  const declaredReference = isKfmEvidenceReference(reference);
  const explicitAbsence = reference === NO_EVIDENCE_REFERENCE;
  if (!declaredReference && !explicitAbsence) {
    return Object.freeze({ ok: false, disposition: "invalid", allowedEvidenceRefs: Object.freeze([]) });
  }
  if (SUPPORTED_EVIDENCE_STATES.has(selection.evidenceState)) {
    if (!declaredReference) {
      return Object.freeze({ ok: false, disposition: "invalid", allowedEvidenceRefs: Object.freeze([]) });
    }
    const linkedLayer = linkedLayers.length === 1 ? linkedLayers[0] : null;
    if (!linkedLayer
      || linkedLayer.title !== selection.layerTitle
      || linkedLayer.domain !== selection.domain
      || linkedLayer.releaseState !== "RELEASED"
      || !["PUBLIC_SAFE", "GENERALIZED"].includes(linkedLayer.publicStatus)
      || linkedLayer.evidenceReference !== reference
      || selection.releaseState !== "RELEASED"
      || selection.reviewState !== QWEN_LOCAL_ACCEPTED_REVIEW_STATE) {
      return Object.freeze({ ok: true, disposition: "unsupported", allowedEvidenceRefs: Object.freeze([]) });
    }
    return Object.freeze({
      ok: true,
      disposition: "supported",
      allowedEvidenceRefs: Object.freeze([reference]),
    });
  }
  if (selection.evidenceState === "ERROR") {
    return Object.freeze({ ok: true, disposition: "error", allowedEvidenceRefs: Object.freeze([]) });
  }
  return Object.freeze({ ok: true, disposition: "unsupported", allowedEvidenceRefs: Object.freeze([]) });
}

const validCamera = (value) => required(value, ["center", "locationRedacted", "zoom", "bearing", "pitch", "projection", "representation"])
  && tuple(value.center, 2)
  && value.center[0] >= -180 && value.center[0] <= 180
  && value.center[1] >= -90 && value.center[1] <= 90
  && number(value.zoom) && value.zoom >= 0 && value.zoom <= 24
  && number(value.bearing)
  && number(value.pitch) && value.pitch >= 0 && value.pitch <= 85
  && text(value.projection) && text(value.representation)
  && typeof value.locationRedacted === "boolean";

const validLayer = (value) => required(value, [
  "id", "title", "domain", "sourceType", "releaseState", "publicStatus", "freshnessState", "evidenceReference",
]) && [value.id, value.title, value.domain, value.sourceType, value.releaseState,
  value.publicStatus, value.freshnessState, value.evidenceReference].every(text)
  && ["RELEASED", "DEMONSTRATION", "GENERALIZED", "RESTRICTED"].includes(value.releaseState)
  && ["PUBLIC_SAFE", "GENERALIZED", "RESTRICTED"].includes(value.publicStatus)
  && (isKfmEvidenceReference(value.evidenceReference) || value.evidenceReference === NO_EVIDENCE_REFERENCE);

const validOfficialSource = (value) => required(value, [
  "id", "title", "selected", "displayed", "state", "featureCount", "retrievedAt", "evidenceRole",
]) && text(value.id) && text(value.title) && typeof value.selected === "boolean"
  && typeof value.displayed === "boolean" && text(value.state)
  && (value.featureCount === null || count(value.featureCount))
  && nullableText(value.retrievedAt) && value.evidenceRole === "EXTERNAL_CONTEXT_ONLY";

const validTelemetry = (value) => required(value, ["authority", "renderer", "registry", "radar", "streamflow"])
  && value.authority === "SITE_LOCAL_REDACTED_DIAGNOSTIC"
  && required(value.renderer, ["state", "styleLoaded", "canvasReady", "tilesLoaded", "failedChecks"])
  && text(value.renderer.state)
  && [value.renderer.styleLoaded, value.renderer.canvasReady, value.renderer.tilesLoaded].every((item) => typeof item === "boolean")
  && Array.isArray(value.renderer.failedChecks) && value.renderer.failedChecks.length <= 32 && value.renderer.failedChecks.every(text)
  && required(value.registry, ["total", "ready", "loading", "error"])
  && [value.registry.total, value.registry.ready, value.registry.loading, value.registry.error].every(count)
  && required(value.radar, ["state", "frameTime", "manifestFresh"])
  && text(value.radar.state) && nullableText(value.radar.frameTime) && typeof value.radar.manifestFresh === "boolean"
  && required(value.streamflow, ["state", "frameTime"])
  && text(value.streamflow.state) && nullableText(value.streamflow.frameTime);

const validSelection = (value) => value === null || (required(value, [
  "featureId", "title", "layerId", "layerTitle", "domain", "evidenceState",
  "evidenceReference", "reviewState", "releaseState", "sourceYear", "spatialScope", "summary",
]) && [value.featureId, value.title, value.layerId, value.layerTitle, value.domain,
  value.evidenceState, value.evidenceReference, value.reviewState, value.releaseState,
  value.spatialScope, value.summary].every(text)
  && ["RELEASED", "DEMONSTRATION", "GENERALIZED", "RESTRICTED"].includes(value.releaseState)
  && number(value.sourceYear));

const validNearby = (value) => required(value, ["title", "layerTitle", "distanceMiles", "evidenceState"])
  && text(value.title) && text(value.layerTitle) && number(value.distanceMiles)
  && value.distanceMiles >= 0 && EVIDENCE_STATES.has(value.evidenceState);

const SOIL_KEYS = [
  "enabled", "availabilityState", "mapState", "selectedView", "selectedDepthCm",
  "selectedUtcDay", "selectedFrameTimeUtc", "renderedFrameTimeUtc", "renderedAtUtc",
  "retainedFrameTimeUtc", "visualTransition", "displaySmoothing", "playing",
  "rangeStartUtcDay", "rangeEndUtcDay", "rangeFrameCount", "availableFrameCount",
  "latestAvailableUtcDay", "sourceCheckedAtUtc", "product", "version", "displayCadence",
  "nativeCadence", "nativeFormat", "approximateResolutionKm", "coverageBoundsWgs84",
  "evidenceRole", "dataKind", "numericPixelsAvailable", "qualityNotice", "sourceUrl", "productGuideUrl",
];
const SOIL_VISUAL_TRANSITION_KEYS = [
  "fromFrameTimeUtc", "toFrameTimeUtc", "fraction", "kind", "numericInterpolation",
];

/** Required-field complement to the undeclared-field validator. */
export function hasRequiredLocalQwenContext(context) {
  if (!required(context, ["camera", "basemap", "time", "visibleLayers", "officialSources", "telemetry", "selection", "nearbyContext"])) return false;
  if (!validCamera(context.camera)) return false;
  if (!required(context.basemap, ["key", "title", "note"]) || ![context.basemap.key, context.basemap.title, context.basemap.note].every(text)) return false;
  if (!required(context.time, ["value", "label", "era"]) || !number(context.time.value) || !text(context.time.label) || !text(context.time.era)) return false;
  if (!Array.isArray(context.visibleLayers) || context.visibleLayers.length > 14 || !context.visibleLayers.every(validLayer)) return false;
  if (!Array.isArray(context.officialSources) || context.officialSources.length > QWEN_LOCAL_MAX_OFFICIAL_SOURCES || !context.officialSources.every(validOfficialSource)) return false;
  if (!validTelemetry(context.telemetry) || !validSelection(context.selection)) return false;
  if (!Array.isArray(context.nearbyContext) || context.nearbyContext.length > 8 || !context.nearbyContext.every(validNearby)) return false;
  if (own(context, "soilMoisture") && context.soilMoisture !== null) {
    if (!required(context.soilMoisture, SOIL_KEYS)) return false;
    if (context.soilMoisture.visualTransition !== null
      && !required(context.soilMoisture.visualTransition, SOIL_VISUAL_TRANSITION_KEYS)) return false;
  }
  return inspectLocalQwenEvidence(context).ok;
}

const HEALTH_REASON_CODES = Object.freeze({
  ready: Object.freeze(["READY"]),
  model_missing: Object.freeze(["MODEL_MISSING"]),
  ollama_unavailable: Object.freeze(["OLLAMA_UNAVAILABLE"]),
  error: Object.freeze(["MODEL_DIGEST_MISMATCH", "OLLAMA_RUNTIME_ERROR", "OLLAMA_VERSION_MISMATCH"]),
});
const DEFAULT_HEALTH_REASON_CODE = Object.freeze({
  ready: "READY",
  model_missing: "MODEL_MISSING",
  ollama_unavailable: "OLLAMA_UNAVAILABLE",
  error: "OLLAMA_RUNTIME_ERROR",
});

const SHA256_DIGEST = /^sha256:[a-f0-9]{64}$/;
const validObservedOllamaVersion = (value) => value === null
  || (typeof value === "string" && value.length <= 64 && SEMVER.test(value));

export const localQwenHealthStatus = (value) => {
  if (!record(value)
    || Object.keys(value).sort().join(",") !== "bridgeVersion,contract,kind,knowledgeDigest,knowledgeVersion,mode,model,modelDigest,ollamaVersion,reasonCode,status"
    || value.knowledgeVersion !== QWEN_LOCAL_KNOWLEDGE_VERSION
    || typeof value.knowledgeDigest !== "string" || !SHA256_DIGEST.test(value.knowledgeDigest)
    || !validObservedOllamaVersion(value.ollamaVersion)
    || value.contract !== QWEN_LOCAL_CONTRACT_VERSION
    || value.kind !== "health"
    || value.mode !== QWEN_LOCAL_MODE
    || value.bridgeVersion !== QWEN_LOCAL_BRIDGE_VERSION
    || value.model !== QWEN_LOCAL_MODEL
    || value.modelDigest !== QWEN_LOCAL_MODEL_DIGEST
    || !QWEN_HEALTH_STATUSES.includes(value.status)
    || !HEALTH_REASON_CODES[value.status].includes(value.reasonCode)) return null;
  return value.status;
};

export const localQwenHealthEnvelope = (
  status,
  reasonCode = DEFAULT_HEALTH_REASON_CODE[status],
  { knowledgeDigest = `sha256:${"0".repeat(64)}`, ollamaVersion = null } = {},
) => {
  if (!QWEN_HEALTH_STATUSES.includes(status)) throw new TypeError("Unknown Qwen health status");
  if (!HEALTH_REASON_CODES[status].includes(reasonCode)) throw new TypeError("Invalid Qwen health reason code");
  const envelope = Object.freeze({
    contract: QWEN_LOCAL_CONTRACT_VERSION,
    kind: "health",
    mode: QWEN_LOCAL_MODE,
    status,
    reasonCode,
    bridgeVersion: QWEN_LOCAL_BRIDGE_VERSION,
    model: QWEN_LOCAL_MODEL,
    modelDigest: QWEN_LOCAL_MODEL_DIGEST,
    ollamaVersion,
    knowledgeVersion: QWEN_LOCAL_KNOWLEDGE_VERSION,
    knowledgeDigest,
  });
  if (localQwenHealthStatus(envelope) === null) throw new TypeError("Invalid Qwen health envelope");
  return envelope;
};

const validAnswerText = (value) => typeof value === "string"
  && value.trim().length > 0
  && value.length <= 12_000
  && !/[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/.test(value);

const INTERPRETATION_LIMITS = Object.freeze({
  summaryChars: 2_000,
  itemChars: 400,
  observations: 5,
  inferences: 4,
  gaps: 4,
  followUps: 3,
});
const INTERPRETATION_LISTS = Object.freeze(["observations", "inferences", "gaps", "followUps"]);
const validInterpretationText = (value, maximum) => typeof value === "string"
  && value.trim().length > 0 && value.length <= maximum
  && !/[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/.test(value);

/** Strict shape of the interpretation carried on an ABSTAIN envelope. */
export function parseLocalQwenInterpretation(value) {
  if (value === null) return null;
  if (!record(value)
    || Object.keys(value).sort().join(",") !== "followUps,gaps,inferences,observations,summary"
    || !validInterpretationText(value.summary, INTERPRETATION_LIMITS.summaryChars)
    || INTERPRETATION_LISTS.some((key) => !Array.isArray(value[key])
      || value[key].length > INTERPRETATION_LIMITS[key]
      || value[key].some((item) => !validInterpretationText(item, INTERPRETATION_LIMITS.itemChars)))) return undefined;
  return Object.freeze({
    summary: value.summary,
    observations: Object.freeze([...value.observations]),
    inferences: Object.freeze([...value.inferences]),
    gaps: Object.freeze([...value.gaps]),
    followUps: Object.freeze([...value.followUps]),
  });
}

const RECEIPT_KEYS = "contextSha256,knowledgeDigest,knowledgeSourceIds,knowledgeVersion,latencyMs,modelInvoked,outputTokens,profile,promptTokens,requestId";
const REQUEST_ID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/;
const nullableCount = (value) => value === null || count(value);

/** Observability metadata: identifiers, digests, timing and token counts; never question or answer text. */
export function parseLocalQwenReceipt(value) {
  if (value === null) return null;
  if (!record(value)
    || Object.keys(value).sort().join(",") !== RECEIPT_KEYS
    || typeof value.requestId !== "string" || !REQUEST_ID.test(value.requestId)
    || !QWEN_PROMPT_PROFILES.includes(value.profile)
    || typeof value.modelInvoked !== "boolean"
    || (value.modelInvoked && value.profile === "none")
    || !(value.contextSha256 === null || (typeof value.contextSha256 === "string" && SHA256_DIGEST.test(value.contextSha256)))
    || !(value.knowledgeVersion === null || value.knowledgeVersion === QWEN_LOCAL_KNOWLEDGE_VERSION)
    || !(value.knowledgeDigest === null || (typeof value.knowledgeDigest === "string" && SHA256_DIGEST.test(value.knowledgeDigest)))
    || (value.knowledgeVersion === null) !== (value.knowledgeDigest === null)
    || !Array.isArray(value.knowledgeSourceIds) || value.knowledgeSourceIds.length > 8
    || value.knowledgeSourceIds.some((item) => typeof item !== "string" || !/^[a-z0-9][a-z0-9-]{0,63}$/.test(item))
    || !count(value.latencyMs)
    || !nullableCount(value.promptTokens) || !nullableCount(value.outputTokens)) return undefined;
  return Object.freeze({ ...value, knowledgeSourceIds: Object.freeze([...value.knowledgeSourceIds]) });
}

export function parseLocalQwenAskEnvelope(value) {
  if (!record(value)
    || Object.keys(value).sort().join(",") !== "answer,authority,bridgeVersion,contract,evidenceRefs,interpretation,kind,mode,model,modelDigest,outcome,reasonCode,receipt"
    || value.contract !== QWEN_LOCAL_CONTRACT_VERSION
    || value.kind !== "ask"
    || value.mode !== QWEN_LOCAL_MODE
    || value.bridgeVersion !== QWEN_LOCAL_BRIDGE_VERSION
    || value.model !== QWEN_LOCAL_MODEL
    || value.modelDigest !== QWEN_LOCAL_MODEL_DIGEST
    || value.authority !== "INTERPRETIVE_ONLY"
    || !QWEN_ASK_OUTCOMES.includes(value.outcome)
    || !QWEN_ASK_REASON_CODES[value.outcome].includes(value.reasonCode)
    || (value.answer !== null && !validAnswerText(value.answer))
    || !Array.isArray(value.evidenceRefs) || value.evidenceRefs.length > 1
    || value.evidenceRefs.some((item) => !isKfmEvidenceReference(item))
    || new Set(value.evidenceRefs).size !== value.evidenceRefs.length
    || (value.outcome === "ANSWER" && (value.answer === null || value.evidenceRefs.length !== 1))
    || (["ABSTAIN", "DENY", "ERROR"].includes(value.outcome) && (value.answer !== null || value.evidenceRefs.length !== 0))) return null;
  const interpretation = parseLocalQwenInterpretation(value.interpretation);
  const receipt = parseLocalQwenReceipt(value.receipt);
  if (interpretation === undefined || receipt === undefined) return null;
  // Model language rides only on an ABSTAIN that explains missing support. It
  // never accompanies an evidence-bearing ANSWER, a DENY or an ERROR, and it
  // may not carry an EvidenceRef or protected precision.
  if (interpretation !== null) {
    const text = [interpretation.summary, ...INTERPRETATION_LISTS.flatMap((key) => interpretation[key])];
    if (value.outcome !== "ABSTAIN"
      || !QWEN_INTERPRETABLE_ABSTAIN_REASONS.includes(value.reasonCode)
      || text.some((item) => referencesInLocalQwenAnswer(item).length > 0
        || localQwenAnswerHasOverPreciseLocation(item))) return null;
  }
  return Object.freeze({ ...value, evidenceRefs: Object.freeze([...value.evidenceRefs]), interpretation, receipt });
}

export const localQwenAskEnvelope = (
  outcome,
  reasonCode,
  { answer = null, evidenceRefs = [], interpretation = null, receipt = null } = {},
) => {
  if (!QWEN_ASK_OUTCOMES.includes(outcome)) throw new TypeError("Unknown Qwen ask outcome");
  if (!QWEN_ASK_REASON_CODES[outcome].includes(reasonCode)) throw new TypeError("Invalid Qwen reason code");
  const envelope = {
    contract: QWEN_LOCAL_CONTRACT_VERSION,
    kind: "ask",
    mode: QWEN_LOCAL_MODE,
    outcome,
    reasonCode,
    bridgeVersion: QWEN_LOCAL_BRIDGE_VERSION,
    model: QWEN_LOCAL_MODEL,
    modelDigest: QWEN_LOCAL_MODEL_DIGEST,
    authority: "INTERPRETIVE_ONLY",
    answer: typeof answer === "string" ? answer.trim() : answer,
    evidenceRefs,
    interpretation,
    receipt,
  };
  const parsed = parseLocalQwenAskEnvelope(envelope);
  if (!parsed) throw new TypeError("Invalid Qwen ask envelope");
  return parsed;
};

export function referencesInLocalQwenAnswer(answer) {
  if (typeof answer !== "string") return Object.freeze([]);
  const matches = answer.match(/kfm:(?:\/\/)?[A-Za-z0-9][A-Za-z0-9._~:/-]{0,511}/g) ?? [];
  return Object.freeze([...new Set(matches.map((item) => item.replace(/[.,;!?)}\]]+$/g, "")))].filter(Boolean));
}

const hasDirectionalCoordinatePair = (answer) => {
  const directions = new Set();
  const accept = (degreesText, minutesText, secondsText, directionText) => {
    const direction = directionText.toUpperCase();
    const degrees = Number(degreesText);
    const minutes = minutesText === undefined ? 0 : Number(minutesText);
    const seconds = secondsText === undefined ? 0 : Number(secondsText);
    const maximumDegrees = direction === "N" || direction === "S" ? 90 : 180;
    if (Number.isFinite(degrees) && degrees >= 0 && degrees <= maximumDegrees
      && Number.isFinite(minutes) && minutes >= 0 && minutes < 60
      && Number.isFinite(seconds) && seconds >= 0 && seconds < 60) directions.add(direction);
  };
  for (const match of answer.matchAll(/\b(\d{1,3})\s*°\s*(\d{1,2}(?:\.\d+)?)\s*[′'’](?:\s*(\d{1,2}(?:\.\d+)?)\s*(?:["″”]|''|′′))?\s*([NSEW])\b/gi)) {
    accept(match[1], match[2], match[3], match[4]);
  }
  for (const match of answer.matchAll(/\b(\d{1,3})\s*:\s*(\d{1,2}(?:\.\d+)?)(?:\s*:\s*(\d{1,2}(?:\.\d+)?))?\s*([NSEW])\b/gi)) {
    accept(match[1], match[2], match[3], match[4]);
  }
  for (const match of answer.matchAll(/\b(\d{1,3}(?:\.\d+)?)\s*°\s*([NSEW])\b/gi)) {
    accept(match[1], undefined, undefined, match[2]);
  }
  return [...directions].some((direction) => direction === "N" || direction === "S")
    && [...directions].some((direction) => direction === "E" || direction === "W");
};

const hasDecimalCoordinatePair = (answer) => {
  const patterns = [
    /(?:^|[^\d.])(-?\d{1,3}\.\d{3,})\s*°?\s*(?:[,;/]|\s)\s*(-?\d{1,3}\.\d{3,})\s*°?(?:[^\d]|$)/g,
    /(?:^|[^\d.])(-?\d{1,3}\.\d{3,})\s*°\s*(-?\d{1,3}\.\d{3,})\s*°(?:[^\d]|$)/g,
  ];
  for (const pattern of patterns) {
    for (const match of answer.matchAll(pattern)) {
      const first = Math.abs(Number(match[1]));
      const second = Math.abs(Number(match[2]));
      const latitudeLongitude = first <= 90 && second <= 180;
      const longitudeLatitude = first <= 180 && second <= 90;
      if (Number.isFinite(first) && Number.isFinite(second)
        && (latitudeLongitude || longitudeLatitude)) return true;
    }
  }
  return false;
};

/** Reject bounded precise-coordinate forms that are not in the safe selection contract. */
export function localQwenAnswerHasOverPreciseLocation(answer) {
  if (typeof answer !== "string") return false;
  return /\b(?:lat(?:itude)?|lon(?:gitude)?)\s*[:=]?\s*-?\d{1,3}(?:\.\d+)?\b/i.test(answer)
    || hasDecimalCoordinatePair(answer)
    || hasDirectionalCoordinatePair(answer)
    || /\b(?:[1-9]|[1-5]\d|60)\s*[C-HJ-NP-X]\s*[A-HJ-NP-Z]{2}\s*(?:\d{2}|\d{4}|\d{6}|\d{8}|\d{10})\b/i.test(answer)
    || /\b(?:[1-9]|[1-5]\d|60)\s*[C-HJ-NP-X]\s+[A-HJ-NP-Z]{2}\s+\d{1,5}\s+\d{1,5}\b/i.test(answer)
    || /\b(?:UTM\s*(?:zone\s*)?)?(?:[1-9]|[1-5]\d|60)\s*[C-HJ-NP-XNS]\s+\d{5,7}(?:\s*m?E)?[\s,;/]+\d{6,8}(?:\s*m?N)?\b/i.test(answer)
    || /\b[23456789CFGHJMPQRVWX]{4,8}\+[23456789CFGHJMPQRVWX]{2,3}\b/i.test(answer)
    || /\bgeohash\s*[:=]?\s*[0123456789BCDEFGHJKMNPQRSTUVWXYZ]{7,12}\b/i.test(answer);
}

export const QWEN_LOCAL_MODEL_RESPONSE_SCHEMA = Object.freeze({
  type: "object",
  properties: Object.freeze({
    disposition: Object.freeze({ type: "string", enum: Object.freeze(["SUPPORTED", "UNSUPPORTED"]) }),
    answer: Object.freeze({ type: "string" }),
    evidenceRefs: Object.freeze({
      type: "array",
      items: Object.freeze({ type: "string" }),
      maxItems: 1,
    }),
  }),
  required: Object.freeze(["disposition", "answer", "evidenceRefs"]),
  additionalProperties: false,
});

export function parseLocalQwenModelResponse(value) {
  if (!record(value)
    || Object.keys(value).sort().join(",") !== "answer,disposition,evidenceRefs"
    || !["SUPPORTED", "UNSUPPORTED"].includes(value.disposition)
    || !validAnswerText(value.answer)
    || !Array.isArray(value.evidenceRefs) || value.evidenceRefs.length > 1
    || value.evidenceRefs.some((reference) => !isKfmEvidenceReference(reference))) return null;
  return Object.freeze({
    disposition: value.disposition,
    answer: value.answer.trim(),
    evidenceRefs: Object.freeze([...value.evidenceRefs]),
  });
}

const stringList = (maxItems) => Object.freeze({
  type: "array",
  items: Object.freeze({ type: "string" }),
  maxItems,
});

/** Structured output for view-level interpretation: observation, inference and gaps stay separate. */
export const QWEN_LOCAL_INTERPRETATION_SCHEMA = Object.freeze({
  type: "object",
  properties: Object.freeze({
    summary: Object.freeze({ type: "string" }),
    observations: stringList(INTERPRETATION_LIMITS.observations),
    inferences: stringList(INTERPRETATION_LIMITS.inferences),
    gaps: stringList(INTERPRETATION_LIMITS.gaps),
    followUps: stringList(INTERPRETATION_LIMITS.followUps),
  }),
  required: Object.freeze(["summary", "observations", "inferences", "gaps", "followUps"]),
  additionalProperties: false,
});

/**
 * Normalize a raw model interpretation. Grammar-constrained decoding does not
 * always honor maxItems, so lists are trimmed to their caps; any other shape
 * deviation (missing or extra keys, non-strings, empty summary) is rejected.
 */
export function parseLocalQwenModelInterpretation(value) {
  if (!record(value)
    || Object.keys(value).sort().join(",") !== "followUps,gaps,inferences,observations,summary"
    || typeof value.summary !== "string"
    || INTERPRETATION_LISTS.some((key) => !Array.isArray(value[key]) || value[key].some((item) => typeof item !== "string"))) return null;
  const clean = (item) => item.replace(/\s+/g, " ").trim();
  const normalized = {
    summary: value.summary.trim(),
    ...Object.fromEntries(INTERPRETATION_LISTS.map((key) => [key, value[key]
      .map(clean)
      .filter(Boolean)
      .slice(0, INTERPRETATION_LIMITS[key])])),
  };
  return parseLocalQwenInterpretation(normalized) ?? null;
}
