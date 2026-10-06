import { createServer } from "node:http";
import { realpathSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { hasSafeQwenContextShape } from "../app/qwen-context-safety.mjs";
import {
  QWEN_LOCAL_ALLOWED_ORIGINS,
  QWEN_LOCAL_BODY_TIMEOUT_MS,
  QWEN_LOCAL_BRIDGE_PORT,
  QWEN_LOCAL_BRIDGE_VERSION,
  QWEN_LOCAL_CONTRACT_VERSION,
  QWEN_LOCAL_EXPLORER_ORIGIN,
  QWEN_LOCAL_HEALTH_TIMEOUT_MS,
  QWEN_LOCAL_INFERENCE_TIMEOUT_MS,
  QWEN_LOCAL_MAX_OUTPUT_TOKENS,
  QWEN_LOCAL_MAX_REPLY_BYTES,
  QWEN_LOCAL_MAX_REQUEST_BYTES,
  QWEN_LOCAL_MODEL,
  QWEN_LOCAL_MODEL_DIGEST,
  QWEN_LOCAL_MODEL_RESPONSE_SCHEMA,
  QWEN_LOCAL_OLLAMA_ORIGIN,
  QWEN_LOCAL_OLLAMA_VERSION,
  QWEN_LOCAL_PREVIEW_ORIGIN,
  QWEN_LOCAL_REQUEST_DEADLINE_MS,
  QWEN_LOCAL_SITE_ORIGIN,
  hasRequiredLocalQwenContext,
  inspectLocalQwenEvidence,
  localQwenAnswerHasOverPreciseLocation,
  localQwenAskEnvelope,
  localQwenHealthEnvelope,
  parseLocalQwenModelResponse,
  referencesInLocalQwenAnswer,
} from "./qwen-local-contract.mjs";

export const SITE_ORIGIN = QWEN_LOCAL_SITE_ORIGIN;
export const LOCAL_PREVIEW_ORIGIN = QWEN_LOCAL_PREVIEW_ORIGIN;
export const LOCAL_EXPLORER_ORIGIN = QWEN_LOCAL_EXPLORER_ORIGIN;
export const LOCAL_BRIDGE_PORT = QWEN_LOCAL_BRIDGE_PORT;
export const LOCAL_QWEN_MODEL = QWEN_LOCAL_MODEL;
export const LOCAL_QWEN_MODEL_DIGEST = QWEN_LOCAL_MODEL_DIGEST;
export const LOCAL_QWEN_BRIDGE_VERSION = QWEN_LOCAL_BRIDGE_VERSION;
export const LOCAL_QWEN_CONTRACT = QWEN_LOCAL_CONTRACT_VERSION;
const OLLAMA_URL = QWEN_LOCAL_OLLAMA_ORIGIN;
const QUESTION_CONTROL_CHARACTERS = /[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/;
const OLLAMA_PROBE_TIMEOUT_MS = 3_000;
const OLLAMA_UNREACHABLE_CODES = new Set(["ECONNREFUSED", "EHOSTUNREACH", "ENETUNREACH"]);
const OLLAMA_VERSION_PATTERN = /^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$/;

class LocalQwenRequestError extends Error {
  constructor(code) {
    super(code);
    this.name = "LocalQwenRequestError";
    this.code = code;
  }
}

const isRecord = (value) => value !== null && typeof value === "object" && !Array.isArray(value);
const responseHeaders = (origin = null) => ({
  ...(origin ? { "access-control-allow-origin": origin } : {}),
  "access-control-allow-methods": "GET, POST, OPTIONS",
  "access-control-allow-headers": "content-type",
  "access-control-allow-private-network": "true",
  "cache-control": "no-store",
  "content-type": "application/json; charset=utf-8",
  "vary": "Origin, Access-Control-Request-Private-Network",
  "x-content-type-options": "nosniff",
});
const send = (res, origin, status, body) => {
  res.writeHead(status, responseHeaders(origin));
  res.end(JSON.stringify(body));
};

const requestEnvelope = (outcome, reasonCode) => localQwenAskEnvelope(outcome, reasonCode);
const isLoopbackPeer = (address) => address === "127.0.0.1" || address === "::1" || address === "::ffff:127.0.0.1";
const isLoopbackHost = (host) => typeof host === "string" && /^127\.0\.0\.1:\d{1,5}$/.test(host);
const discardRequestBody = (req) => {
  if (req.readableEnded || req.destroyed) return;
  if (typeof req.resume === "function") req.resume();
  else if (typeof req.destroy === "function") req.destroy();
};
const normalizeDigest = (value) => {
  if (typeof value !== "string") return null;
  const normalized = value.startsWith("sha256:") ? value.toLowerCase() : `sha256:${value.toLowerCase()}`;
  return /^sha256:[a-f0-9]{64}$/.test(normalized) ? normalized : null;
};
const ollamaFailureState = (error) => {
  let candidate = error;
  for (let depth = 0; candidate && depth < 6; depth++) {
    if (typeof candidate.code === "string" && OLLAMA_UNREACHABLE_CODES.has(candidate.code)) {
      return "unreachable";
    }
    candidate = candidate.cause;
  }
  return "runtime_error";
};

const requestTimeoutError = () => new LocalQwenRequestError("REQUEST_TIMEOUT");
const withDeadline = (signal, timeoutMs) => signal
  ? AbortSignal.any([signal, AbortSignal.timeout(timeoutMs)])
  : AbortSignal.timeout(timeoutMs);

export function createLocalQwenDeadlineSignal(timeoutMs = QWEN_LOCAL_REQUEST_DEADLINE_MS) {
  if (!Number.isSafeInteger(timeoutMs) || timeoutMs <= 0) throw new TypeError("Invalid Qwen deadline");
  return AbortSignal.timeout(timeoutMs);
}

async function abortableRead(reader, signal) {
  if (!signal) return reader.read();
  if (signal.aborted) throw requestTimeoutError();
  let rejectOnAbort;
  const aborted = new Promise((_, reject) => { rejectOnAbort = () => reject(requestTimeoutError()); });
  signal.addEventListener("abort", rejectOnAbort, { once: true });
  try { return await Promise.race([reader.read(), aborted]); }
  finally { signal.removeEventListener("abort", rejectOnAbort); }
}

async function boundedJson(response, limit, signal) {
  const reader = response.body?.getReader();
  if (!reader) throw new Error("EMPTY_RESPONSE");
  const chunks = [];
  let size = 0;
  try {
    for (;;) {
      const { done, value } = await abortableRead(reader, signal);
      if (done) break;
      size += value.byteLength;
      if (size > limit) throw new Error("RESPONSE_TOO_LARGE");
      chunks.push(value);
    }
  } finally {
    await reader.cancel().catch(() => undefined);
  }
  return JSON.parse(new TextDecoder().decode(Buffer.concat(chunks)));
}

export async function readBoundedLocalQwenBody(
  req,
  { limit = QWEN_LOCAL_MAX_REQUEST_BYTES, timeoutMs = QWEN_LOCAL_BODY_TIMEOUT_MS, deadlineSignal = null } = {},
) {
  const declaredLength = Number(req.headers["content-length"] ?? 0);
  if (!Number.isSafeInteger(declaredLength) || declaredLength < 0 || declaredLength > limit) {
    discardRequestBody(req);
    throw new Error("REQUEST_TOO_LARGE");
  }
  if (!Number.isSafeInteger(timeoutMs) || timeoutMs <= 0) throw new TypeError("Invalid body timeout");
  return new Promise((resolve, reject) => {
    const chunks = [];
    let size = 0;
    let settled = false;
    const cleanup = () => {
      clearTimeout(timer);
      req.removeListener("data", onData);
      req.removeListener("end", onEnd);
      req.removeListener("aborted", onAborted);
      req.removeListener("error", onError);
      deadlineSignal?.removeEventListener("abort", onDeadline);
    };
    const finish = (action, value, drain = false) => {
      if (settled) return;
      settled = true;
      cleanup();
      if (drain && typeof req.resume === "function") req.resume();
      action(value);
    };
    const onDeadline = () => finish(reject, requestTimeoutError(), true);
    const onAborted = () => finish(reject, new Error("REQUEST_ABORTED"));
    const onError = () => finish(reject, new Error("REQUEST_ERROR"));
    const onData = (chunk) => {
      size += chunk.byteLength;
      if (size > limit) {
        finish(reject, new Error("REQUEST_TOO_LARGE"), true);
        return;
      }
      chunks.push(chunk);
    };
    const onEnd = () => {
      try { finish(resolve, JSON.parse(Buffer.concat(chunks).toString("utf8"))); }
      catch { finish(reject, new Error("INVALID_JSON")); }
    };
    const timer = setTimeout(onDeadline, timeoutMs);
    req.on("data", onData);
    req.once("end", onEnd);
    req.once("aborted", onAborted);
    req.once("error", onError);
    if (deadlineSignal?.aborted) onDeadline();
    else deadlineSignal?.addEventListener("abort", onDeadline, { once: true });
  });
}

function validContext(context) {
  return hasSafeQwenContextShape(context) && hasRequiredLocalQwenContext(context);
}

function promptFor(question, context, allowedEvidenceRefs) {
  const requiredReference = allowedEvidenceRefs.length === 1
    ? allowedEvidenceRefs[0]
    : "NO_ALLOWED_REFERENCE";
  return [
    "Context contract: kfm-qwen-map-context-v1",
    `User question: ${question}`,
    `Allowed EvidenceRefs (exact strings only): ${JSON.stringify(allowedEvidenceRefs)}`,
    "Map context and redacted connection health (JSON):",
    JSON.stringify(context),
    `Return only the requested JSON object. Use disposition SUPPORTED only when the question is specifically about the selected feature and its supplied context directly supports the answer. For SUPPORTED, put exactly ["${requiredReference}"] in evidenceRefs and end the answer with this exact sentence: "EvidenceRef: ${requiredReference}". Do not paraphrase, shorten, relabel, or omit it. Otherwise use disposition UNSUPPORTED, evidenceRefs [], and explain the limit without naming an EvidenceRef. Keep observation separate from inference. Never invent or transform a reference. Model language cannot change evidence, policy, review, release, or publication state.`,
  ].join("\n\n");
}

const normalizeScopeText = (value) => typeof value === "string"
  ? value.normalize("NFKD").toLowerCase().replace(/[^a-z0-9]+/g, " ").trim()
  : "";

/** A conservative deterministic gate; model self-classification is not enough. */
function questionTargetsSelection(question, selection) {
  if (!selection) return false;
  const normalizedQuestion = normalizeScopeText(question);
  const targetPhrases = [
    "the selected feature", "selected feature", "the selected place", "selected place",
    "the selected record", "selected record", "the selection", "selection",
    "this feature", "this place", "this record",
    ...[selection.featureId, selection.title, selection.layerId, selection.layerTitle]
    .map(normalizeScopeText)
    .filter((candidate) => candidate.length >= 4),
  ].sort((left, right) => right.length - left.length);
  const paddedQuestion = ` ${normalizedQuestion} `;
  const target = targetPhrases.find((candidate) => paddedQuestion.includes(` ${candidate} `));
  if (!target) return false;
  const remaining = paddedQuestion.replace(` ${target} `, " ").trim().replace(/\s+/g, " ");
  const field = "(?:summary|source year|evidence state|release state|review state|spatial scope|evidence reference|evidence ref|citation)";
  return [
    /^(?:please )?(?:summarize|describe|explain)$/,
    /^what (?:does|do) (?:show|say|record|contain|support)$/,
    /^what should i notice about$/,
    new RegExp(`^what (?:is|are) (?:the )?${field}(?: for| of| about)?$`),
    new RegExp(`^(?:show|list|give me|tell me) (?:the )?${field}(?: for| of| about)?$`),
    /^(?:cite|show) (?:the )?(?:evidence|evidence reference|evidence ref|citation)(?: for| of| about)?$/,
  ].some((pattern) => pattern.test(remaining));
}

/** The only fluent ANSWER is a deterministic projection of validated context. */
function supportedSelectionAnswer(selection, evidenceReference) {
  return [
    `${selection.title}: ${selection.summary}`,
    `Spatial scope: ${selection.spatialScope}.`,
    `Source year: ${selection.sourceYear}.`,
    `Evidence state: ${selection.evidenceState}.`,
    `Release state: ${selection.releaseState}.`,
    `Review state: ${selection.reviewState}.`,
    `EvidenceRef: ${evidenceReference}`,
  ].join(" ");
}

async function fetchOllamaJson(fetcher, url, deadlineSignal) {
  const operationSignal = withDeadline(deadlineSignal, OLLAMA_PROBE_TIMEOUT_MS);
  let upstream;
  try {
    upstream = await fetcher(url, {
      cache: "no-store",
      signal: operationSignal,
      redirect: "error",
    });
  } catch (error) {
    return { state: ollamaFailureState(error), value: null };
  }
  if (!upstream.ok) {
    await upstream.body?.cancel().catch(() => undefined);
    return { state: "runtime_error", value: null };
  }
  try {
    return { state: "ok", value: await boundedJson(upstream, QWEN_LOCAL_MAX_REPLY_BYTES, operationSignal) };
  } catch {
    return { state: "runtime_error", value: null };
  }
}

async function installedModelState(fetcher, ollamaUrl, model, deadlineSignal) {
  const versionResult = await fetchOllamaJson(fetcher, `${ollamaUrl}/api/version`, deadlineSignal);
  if (versionResult.state === "unreachable") {
    return { status: "ollama_unavailable", reasonCode: "OLLAMA_UNAVAILABLE" };
  }
  if (versionResult.state !== "ok"
    || !isRecord(versionResult.value)
    || typeof versionResult.value.version !== "string"
    || !OLLAMA_VERSION_PATTERN.test(versionResult.value.version)) {
    return { status: "error", reasonCode: "OLLAMA_RUNTIME_ERROR" };
  }
  if (versionResult.value.version !== QWEN_LOCAL_OLLAMA_VERSION) {
    return { status: "error", reasonCode: "OLLAMA_VERSION_MISMATCH" };
  }
  const tagsResult = await fetchOllamaJson(fetcher, `${ollamaUrl}/api/tags`, deadlineSignal);
  if (tagsResult.state === "unreachable") {
    return { status: "ollama_unavailable", reasonCode: "OLLAMA_UNAVAILABLE" };
  }
  if (tagsResult.state !== "ok" || !isRecord(tagsResult.value) || !Array.isArray(tagsResult.value.models)) {
    return { status: "error", reasonCode: "OLLAMA_RUNTIME_ERROR" };
  }
  if (!tagsResult.value.models.every((item) => isRecord(item)
    && ((typeof item.name === "string" && item.name.trim().length > 0)
      || (typeof item.model === "string" && item.model.trim().length > 0))
    && typeof item.digest === "string")) {
    return { status: "error", reasonCode: "OLLAMA_RUNTIME_ERROR" };
  }
  const installed = tagsResult.value.models.find((item) => item?.name === model || item?.model === model);
  if (!installed) return { status: "model_missing", reasonCode: "MODEL_MISSING" };
  const installedDigest = normalizeDigest(installed.digest);
  if (!installedDigest) return { status: "error", reasonCode: "OLLAMA_RUNTIME_ERROR" };
  return installedDigest === LOCAL_QWEN_MODEL_DIGEST
    ? { status: "ready", reasonCode: "READY" }
    : { status: "error", reasonCode: "MODEL_DIGEST_MISMATCH" };
}

export function createLocalQwenBridge({
  fetcher = fetch,
  ollamaUrl = OLLAMA_URL,
  model = LOCAL_QWEN_MODEL,
  allowedOrigins = QWEN_LOCAL_ALLOWED_ORIGINS,
} = {}) {
  if (ollamaUrl !== OLLAMA_URL || model !== LOCAL_QWEN_MODEL) {
    throw new TypeError("The governed local Qwen bridge uses its pinned loopback endpoint and model.");
  }
  const originAllowlist = new Set(allowedOrigins);
  if (originAllowlist.size !== QWEN_LOCAL_ALLOWED_ORIGINS.length
    || QWEN_LOCAL_ALLOWED_ORIGINS.some((origin) => !originAllowlist.has(origin))) {
    throw new TypeError("The governed local Qwen origin allowlist is fixed.");
  }
  let busy = false;
  return createServer(async (req, res) => {
    const origin = req.headers.origin;
    const path = req.url?.split("?", 1)[0];
    const allowedOrigin = typeof origin === "string" && originAllowlist.has(origin) ? origin : null;
    const localRequest = isLoopbackPeer(req.socket.remoteAddress) && isLoopbackHost(req.headers.host);
    if (!localRequest || !allowedOrigin) {
      discardRequestBody(req);
      send(res, null, 403, requestEnvelope("DENY", "ORIGIN_NOT_ALLOWED"));
      return;
    }
    if (!["/health", "/ask"].includes(path) || req.url !== path) {
      discardRequestBody(req);
      send(res, allowedOrigin, 404, requestEnvelope("ERROR", "ROUTE_NOT_FOUND"));
      return;
    }
    if (req.method === "OPTIONS") {
      res.writeHead(204, responseHeaders(allowedOrigin));
      res.end();
      return;
    }
    if (req.method === "GET" && path === "/health") {
      let state;
      try {
        state = await installedModelState(
          fetcher,
          ollamaUrl,
          model,
          createLocalQwenDeadlineSignal(QWEN_LOCAL_HEALTH_TIMEOUT_MS),
        );
      } catch {
        state = { status: "error", reasonCode: "OLLAMA_RUNTIME_ERROR" };
      }
      send(
        res,
        allowedOrigin,
        state.status === "ready" ? 200 : 503,
        localQwenHealthEnvelope(state.status, state.reasonCode),
      );
      return;
    }
    if (req.method !== "POST" || path !== "/ask"
      || req.headers["content-type"]?.split(";", 1)[0].trim().toLowerCase() !== "application/json") {
      discardRequestBody(req);
      send(res, allowedOrigin, 415, requestEnvelope("ERROR", "JSON_REQUEST_REQUIRED"));
      return;
    }
    if (busy) {
      discardRequestBody(req);
      send(res, allowedOrigin, 429, requestEnvelope("ERROR", "BRIDGE_BUSY"));
      return;
    }
    busy = true;
    const requestDeadline = createLocalQwenDeadlineSignal();
    try {
      let body;
      try {
        body = await readBoundedLocalQwenBody(req, { deadlineSignal: requestDeadline });
      } catch (error) {
        if (error instanceof LocalQwenRequestError && error.code === "REQUEST_TIMEOUT") {
          send(res, allowedOrigin, 408, requestEnvelope("ERROR", "REQUEST_TIMEOUT"));
          return;
        }
        send(res, allowedOrigin, 413, requestEnvelope("ERROR", "INVALID_OR_OVERSIZED_REQUEST"));
        return;
      }
      const question = typeof body?.question === "string" ? body.question.trim() : "";
      if (!isRecord(body) || Object.keys(body).some((key) => key !== "question" && key !== "context")
        || !question || question.length > 1200 || QUESTION_CONTROL_CHARACTERS.test(question)
        || !validContext(body.context)) {
        send(res, allowedOrigin, 400, requestEnvelope("ERROR", "INVALID_REQUEST_SHAPE"));
        return;
      }
      const evidence = inspectLocalQwenEvidence(body.context);
      if (evidence.disposition === "withheld") {
        send(res, allowedOrigin, 200, localQwenAskEnvelope("DENY", "POLICY_WITHHELD"));
        return;
      }
      if (evidence.disposition === "error") {
        send(res, allowedOrigin, 200, localQwenAskEnvelope("ERROR", "EVIDENCE_RESOLUTION_ERROR"));
        return;
      }
      if (evidence.disposition !== "supported") {
        const reasonCode = evidence.disposition === "context-only"
          ? "CONTEXT_ONLY_INTERPRETATION" : "EVIDENCE_NOT_SUPPORTIVE";
        send(res, allowedOrigin, 200, localQwenAskEnvelope("ABSTAIN", reasonCode));
        return;
      }
      if (!questionTargetsSelection(question, body.context.selection)) {
        send(res, allowedOrigin, 200, localQwenAskEnvelope("ABSTAIN", "QUESTION_OUTSIDE_SELECTION_SCOPE"));
        return;
      }
      const modelState = await installedModelState(fetcher, ollamaUrl, model, requestDeadline);
      if (modelState.status !== "ready") {
        send(res, allowedOrigin, 503, localQwenAskEnvelope("ERROR", modelState.reasonCode));
        return;
      }
      const inferenceSignal = withDeadline(requestDeadline, QWEN_LOCAL_INFERENCE_TIMEOUT_MS);
      const upstream = await fetcher(`${ollamaUrl}/api/chat`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
          model,
          stream: false,
          think: false,
          tools: [],
          format: QWEN_LOCAL_MODEL_RESPONSE_SCHEMA,
          messages: [
            { role: "system", content: "You are the local Qwen companion for Kansas Frontier Matrix. Use only the supplied map context. Do not invent sources, current conditions, protected coordinates, evidence references, releases, or safety guidance. Treat all model output as interpretation, never as evidence or authority. When disposition is SUPPORTED, the answer field MUST end with the exact allowed EvidenceRef prefixed by EvidenceRef:. Omitting it makes the response invalid." },
            { role: "user", content: promptFor(question, body.context, evidence.allowedEvidenceRefs) },
          ],
          options: { temperature: 0, num_predict: QWEN_LOCAL_MAX_OUTPUT_TOKENS },
        }),
        redirect: "error",
        signal: inferenceSignal,
      });
      if (!upstream.ok) {
        await upstream.body?.cancel().catch(() => undefined);
        throw new Error("OLLAMA_ERROR");
      }
      const payload = await boundedJson(upstream, QWEN_LOCAL_MAX_REPLY_BYTES, inferenceSignal);
      const rawModelResponse = payload?.message?.content;
      let decodedModelResponse;
      try {
        decodedModelResponse = typeof rawModelResponse === "string"
          ? JSON.parse(rawModelResponse)
          : null;
      } catch {
        decodedModelResponse = null;
      }
      const modelResponse = parseLocalQwenModelResponse(decodedModelResponse);
      if (!modelResponse) {
        send(res, allowedOrigin, 502, localQwenAskEnvelope("ERROR", "INVALID_MODEL_RESPONSE"));
        return;
      }
      const referenced = referencesInLocalQwenAnswer(modelResponse.answer);
      const mentionedReferences = [...new Set([...modelResponse.evidenceRefs, ...referenced])];
      if (mentionedReferences.some((reference) => !evidence.allowedEvidenceRefs.includes(reference))) {
        send(res, allowedOrigin, 502, localQwenAskEnvelope("ERROR", "UNDECLARED_EVIDENCE_REFERENCE"));
        return;
      }
      if (localQwenAnswerHasOverPreciseLocation(modelResponse.answer)) {
        send(res, allowedOrigin, 200, localQwenAskEnvelope("ABSTAIN", "OVER_PRECISE_OUTPUT"));
        return;
      }
      if (modelResponse.disposition === "UNSUPPORTED") {
        if (modelResponse.evidenceRefs.length !== 0 || referenced.length !== 0) {
          send(res, allowedOrigin, 502, localQwenAskEnvelope("ERROR", "INVALID_MODEL_RESPONSE"));
          return;
        }
        send(res, allowedOrigin, 200, localQwenAskEnvelope("ABSTAIN", "MODEL_ABSTAINED"));
        return;
      }
      const requiredReference = evidence.allowedEvidenceRefs[0];
      if (modelResponse.evidenceRefs.length !== 1
        || modelResponse.evidenceRefs[0] !== requiredReference
        || !referenced.includes(requiredReference)) {
        send(res, allowedOrigin, 200, localQwenAskEnvelope("ABSTAIN", "CITATION_REQUIRED"));
        return;
      }
      const groundedAnswer = supportedSelectionAnswer(body.context.selection, requiredReference);
      if (localQwenAnswerHasOverPreciseLocation(groundedAnswer)) {
        send(res, allowedOrigin, 200, localQwenAskEnvelope("ABSTAIN", "OVER_PRECISE_OUTPUT"));
        return;
      }
      const groundedReferences = referencesInLocalQwenAnswer(groundedAnswer);
      if (groundedReferences.some((reference) => !evidence.allowedEvidenceRefs.includes(reference))) {
        send(res, allowedOrigin, 502, localQwenAskEnvelope("ERROR", "UNDECLARED_EVIDENCE_REFERENCE"));
        return;
      }
      if (groundedReferences.length !== 1 || groundedReferences[0] !== requiredReference) {
        send(res, allowedOrigin, 200, localQwenAskEnvelope("ABSTAIN", "CITATION_REQUIRED"));
        return;
      }
      send(res, allowedOrigin, 200, localQwenAskEnvelope("ANSWER", "SUPPORTED_SELECTION_INTERPRETATION", {
        answer: groundedAnswer,
        evidenceRefs: [requiredReference],
      }));
    } catch (error) {
      if (requestDeadline.aborted
        || (error instanceof LocalQwenRequestError && error.code === "REQUEST_TIMEOUT")
        || error?.name === "TimeoutError" || error?.name === "AbortError") {
        send(res, allowedOrigin, 504, localQwenAskEnvelope("ERROR", "REQUEST_TIMEOUT"));
      } else {
        send(res, allowedOrigin, 502, localQwenAskEnvelope("ERROR", "LOCAL_MODEL_UNAVAILABLE"));
      }
    } finally {
      busy = false;
    }
  });
}

export function isDirectEntryPoint(moduleUrl, entryPath = process.argv[1]) {
  if (!entryPath) return false;
  try { return realpathSync(fileURLToPath(moduleUrl)) === realpathSync(entryPath); }
  catch { return false; }
}

if (isDirectEntryPoint(import.meta.url)) {
  createLocalQwenBridge().listen(LOCAL_BRIDGE_PORT, "127.0.0.1", () => {
    process.stdout.write(`KFM local Qwen bridge ready on 127.0.0.1:${LOCAL_BRIDGE_PORT} · ${LOCAL_QWEN_MODEL}\n`);
  });
}
