import { createHash, randomUUID } from "node:crypto";
import { createServer } from "node:http";
import { realpathSync } from "node:fs";
import { performance } from "node:perf_hooks";
import { fileURLToPath } from "node:url";
import { hasSafeQwenContextShape } from "../app/qwen-context-safety.mjs";
import {
  QWEN_LOCAL_ALLOWED_ORIGINS,
  QWEN_LOCAL_BODY_TIMEOUT_MS,
  QWEN_LOCAL_BRIDGE_PORT,
  QWEN_LOCAL_BRIDGE_VERSION,
  QWEN_LOCAL_CONTEXT_WINDOW_TOKENS,
  QWEN_LOCAL_CONTRACT_VERSION,
  QWEN_LOCAL_EXPLORER_ORIGIN,
  QWEN_LOCAL_HEALTH_TIMEOUT_MS,
  QWEN_LOCAL_INFERENCE_TIMEOUT_MS,
  QWEN_LOCAL_INTERPRETATION_PROMPT_BUDGET_BYTES,
  QWEN_LOCAL_INTERPRETATION_SCHEMA,
  QWEN_LOCAL_KEEP_ALIVE,
  QWEN_LOCAL_MAX_INTERPRETATION_TOKENS,
  QWEN_LOCAL_MAX_OUTPUT_TOKENS,
  QWEN_LOCAL_MAX_REPLY_BYTES,
  QWEN_LOCAL_MAX_REQUEST_BYTES,
  QWEN_LOCAL_MODEL,
  QWEN_LOCAL_MODEL_DIGEST,
  QWEN_LOCAL_MODEL_RESPONSE_SCHEMA,
  QWEN_LOCAL_OLLAMA_ORIGIN,
  QWEN_LOCAL_PREVIEW_ORIGIN,
  QWEN_LOCAL_REQUEST_DEADLINE_MS,
  QWEN_LOCAL_SITE_ORIGIN,
  hasRequiredLocalQwenContext,
  inspectLocalQwenEvidence,
  isSupportedOllamaVersion,
  localQwenAnswerHasOverPreciseLocation,
  localQwenAskEnvelope,
  localQwenHealthEnvelope,
  parseLocalQwenModelInterpretation,
  parseLocalQwenModelResponse,
  referencesInLocalQwenAnswer,
} from "./qwen-local-contract.mjs";
import { QWEN_KNOWLEDGE_DIGEST, QWEN_KNOWLEDGE_VERSION, selectQwenKnowledge } from "./qwen-knowledge.mjs";

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
  const ollamaVersion = versionResult.value.version;
  if (!isSupportedOllamaVersion(ollamaVersion)) {
    return { status: "error", reasonCode: "OLLAMA_VERSION_MISMATCH", ollamaVersion };
  }
  const tagsResult = await fetchOllamaJson(fetcher, `${ollamaUrl}/api/tags`, deadlineSignal);
  if (tagsResult.state === "unreachable") {
    return { status: "ollama_unavailable", reasonCode: "OLLAMA_UNAVAILABLE" };
  }
  if (tagsResult.state !== "ok" || !isRecord(tagsResult.value) || !Array.isArray(tagsResult.value.models)) {
    return { status: "error", reasonCode: "OLLAMA_RUNTIME_ERROR", ollamaVersion };
  }
  if (!tagsResult.value.models.every((item) => isRecord(item)
    && ((typeof item.name === "string" && item.name.trim().length > 0)
      || (typeof item.model === "string" && item.model.trim().length > 0))
    && typeof item.digest === "string")) {
    return { status: "error", reasonCode: "OLLAMA_RUNTIME_ERROR", ollamaVersion };
  }
  const installed = tagsResult.value.models.find((item) => item?.name === model || item?.model === model);
  if (!installed) return { status: "model_missing", reasonCode: "MODEL_MISSING", ollamaVersion };
  const installedDigest = normalizeDigest(installed.digest);
  if (!installedDigest) return { status: "error", reasonCode: "OLLAMA_RUNTIME_ERROR", ollamaVersion };
  return installedDigest === LOCAL_QWEN_MODEL_DIGEST
    ? { status: "ready", reasonCode: "READY", ollamaVersion }
    : { status: "error", reasonCode: "MODEL_DIGEST_MISMATCH", ollamaVersion };
}

const INTERPRETATION_SYSTEM_PROMPT = [
  "You are the local Qwen companion for Kansas Frontier Matrix (KFM), an evidence-first map of Kansas land, water, weather, hazards, infrastructure, and history.",
  "Explain the current map view using only the supplied map context and the KFM knowledge metadata.",
  "The knowledge metadata describes sources, vocabulary, and exploration ideas; it is not evidence about any place, time, or condition. Use its glossary and domain terms for exact meanings.",
  "Your reply is shown as interpretation under an ABSTAIN outcome. It can never become evidence, a citation, a review decision, or a release.",
  "Respect each source's boundary text: say what a source cannot show when that limits the answer. Treat missing data as a gap, never as zero or an all-clear.",
  "Never write a kfm: identifier, coordinates, grid references, or street-level locations. Never give safety, emergency, legal, medical, or excavation guidance.",
  "Never claim current conditions beyond the frame and retrieval times present in the context.",
].join(" ");

const INTERPRETATION_REASONS = Object.freeze({
  CONTEXT_ONLY_INTERPRETATION: "No KFM feature is selected, so no EvidenceBundle is in scope for this view.",
  EVIDENCE_NOT_SUPPORTIVE: "The selected feature is not released, reviewed, and linked to a public visible layer, so its evidence cannot support an answer.",
  QUESTION_OUTSIDE_SELECTION_SCOPE: "The question reaches beyond the selected feature's released record, so the record alone cannot answer it.",
});

function interpretationPromptFor(question, context, knowledge, reasonCode) {
  return [
    "Context contract: kfm-qwen-map-context-v1",
    "Prompt profile: context-interpretation-v1",
    `Why there is no evidence-backed answer: ${INTERPRETATION_REASONS[reasonCode]}`,
    `User question: ${question}`,
    "KFM knowledge metadata (METADATA_NOT_EVIDENCE, JSON):",
    JSON.stringify(knowledge),
    "Map context and redacted connection health (JSON):",
    JSON.stringify(context),
    [
      "Return only the requested JSON object:",
      "- summary: 2 to 4 plain sentences that answer as far as the context and metadata allow, naming the source limits that matter.",
      "- observations: up to 5 facts that appear in the map context JSON (layer or source titles, states, counts, frame or retrieval times).",
      "- inferences: up to 4 cautious readings, each phrased as possible rather than certain.",
      "- gaps: up to 4 items KFM would need (a released EvidenceBundle, a source, a review, a fresher frame) before this could become an evidence-backed answer.",
      "- followUps: up to 3 short questions the user could ask next in this map, preferring the domain and cross-domain ideas when they fit.",
      "Use empty lists rather than inventing content.",
    ].join("\n"),
  ].join("\n\n");
}

/**
 * Questions that would turn interpretation into guidance or precision are
 * not sent to the model at all. The deterministic ABSTAIN explains why.
 */
// "Safe to show / publish / at its declared precision" asks about release status (PUBLIC_SAFE), not personal safety.
const NOT_RELEASE_STATUS = "(?! (?:to|for) (?:(?:public|external|general|wider|open|outside|online) )?(?:show\\w*|display\\w*|publish\\w*|releas\\w+|shar\\w+|map\\w*|render\\w*|expos\\w+)\\b| at (?:(?:its|their|the|this|that) )?(?:declared |stated |published )?(?:precision|resolution|scale|zoom)\\b)";
// Address metadata (fields, formats, address-point layers) is not a request for an address.
const NOT_ADDRESS_METADATA = "(?! (?:fields?|columns?|attributes?|metadata|formats?|schemas?|layers?|data|points?|ranges?|standards?)\\b)";
// "Marked safe", "considered safe": a status label on a layer or record, not a safety question.
const NOT_STATUS_LABEL = "(?<!(?:public|marked|considered|labeled|labelled|flagged|rated|classed|classified|tagged|deemed) )";
const NOT_AGGREGATE_TAIL = "(?!(?: \\w+){0,2} (?:by|per) (?:county|counties|state|region|year|decade)\\b)";
const SENSITIVE_SITE = "(?:burials?|graves?|gravesites?|(?<!blue )mounds?(?! (?:city|valley|ridge|township|creek)\\b)|archaeological sites?|nests?|nesting sites?|leks?|dens?|den sites?|roosts?|roosting sites?|hibernacul\\w*)";
const SENSITIVE_QUESTION = new RegExp([
  `\\b(?:is it|is this|is that|are they|how) (?:\\w+ ){0,3}${NOT_STATUS_LABEL}(?:safe|dangerous)\\b${NOT_RELEASE_STATUS}`,
  // PUBLIC_SAFE and "marked safe" are release labels, not safety questions.
  `\\b(?:is|are|how) (?:\\w+ ){0,5}${NOT_STATUS_LABEL}(?:safe|unsafe|dangerous|hazardous)\\b${NOT_RELEASE_STATUS}`,
  // "Okay to drink", "would drinking this water be safe", "is swimming here fine".
  `\\b(?:okay|ok|fine|alright|good) (?:to|for) (?:drink\\w*|swim\\w*|wad\\w+|eat\\w*)\\b|\\b(?:drinking|swimming|wading|eating) (?:\\w+ ){0,4}(?:be |is |are )?(?:safe|okay|ok|fine|alright|dangerous|harmful)\\b${NOT_RELEASE_STATUS}`,
  "\\bsafe (?:to|for) (?:drink\\w*|swim\\w*|wad\\w+|fish\\w*|eat\\w*|cross\\w*|walk\\w*|hik\\w+|camp\\w*|hunt\\w*|boat\\w*|kayak\\w*|canoe\\w*|live|kids|children|people|pets|dogs|humans|consumption)\\b",
  "\\b(?:can|could|should|may) (?:i|we|you|people|kids|children|cattle|cows|horses|livestock|dogs|pets|animals|(?:my|our|your|the|a|an) (?:\\w+ )?(?:child|children|kids?|dogs?|pets?|cattle|cows?|horses?|livestock|family|son|daughter|baby|babies|toddlers?|students?|scouts?|campers?|swimmers?)) (?:\\w+ ){0,2}(?:drink|swim|wade|eat|camp)\\b",
  "\\b(?:safety|evacuat\\w*|emergency|shelter|rescue)\\b",
  "\\b(?:excavat\\w*|dig|digging|loot\\w*|metal detect\\w*|artifact hunting|trespass\\w*)\\b",
  "\\b(?:drinkable|potable|medical|diagnos\\w*|legal advice|lawsuit)\\b",
  "\\bexact (?:location|spot|address|site)\\b",
  // Street addresses. (Coordinate and ZIP terms are checked below; PLSS section-scale references are
  // allowed, as the knowledge pack describes, while sensitive sites and personal places stay gated.)
  `\\b(?:street|mailing|home|physical|exact|what|which|whose|its|their|his|her|the|an?|\\w+ s) address(?:es)?\\b${NOT_ADDRESS_METADATA}`,
  "\\baddress (?:of|for)\\b",
  // A house number, a street name (not "4 or more lane", "30 minute drive") and a street suffix.
  "\\b\\d{1,6}(?: [nsew]{1,2})? (?:(?!(?:or|and|to|more|less|than|of|the|a|an|in|on|at|for|with|by|per|from|minutes?|hours?|miles?|mi|km|feet|foot|ft|yards?|lanes?)\\b)\\w+ ){1,3}(?:st|street|ave|avenue|blvd|boulevard|dr|drive|ln|lane|ct|court|rd|road|pl|place|ter|terrace|pkwy|parkway|cir|circle|trl|trail)\\b",
  "\\b(?:ks|kansas) \\d{5}\\b",
  // Exact or personal locations in other words: where exactly, precisely, near me, my house, where I live.
  "\\b(?:where exactly|exactly where|where precisely|precisely where|pinpoint\\w*)\\b",
  "\\bwhere\\b(?: \\w+){1,6} (?:exactly|precisely)\\b",
  "\\bprecise (?:locations?|spots?|sites?|positions?|places?|address(?:es)?)\\b",
  "\\b(?:nearest|closest)\\b(?: \\w+){0,4} (?:(?:to|from) )?(?:my|our|me|us)\\b",
  "\\b(?:near|nearby|close to|around|next to) (?:me|us)\\b",
  // "My parents' house", "our neighbor's farm": a possessor between "my" and the place.
  "\\b(?:my|our) (?:current )?(?:(?:\\w+ s|\\w+s) ){0,2}(?:house|home|address|property|yard|farm|land|lot|parcel|location|position|whereabouts|basement|neighborhood|neighbourhood|street|block|place|apartment|well|field|pasture|ranch|acreage|driveway)\\b",
  "\\bwhere (?:i|we) (?:am|are|m|re|live|stay|work)\\b",
  "\\bwhere (?:my|our) (?:\\w+ ){1,2}(?:live|lives|stay|stays|work|works)\\b",
  "\\bwho (?:owns|lives|rents)\\b(?: \\w+){0,5} (?:parcels?|land|property|house|home|farm|lot|field|well|tract|ranch|acreage|building)\\b",
  // Culturally or ecologically sensitive sites are never located more precisely than the map shows.
  `\\b(?:where|locate|located|locations?|nearest|closest|near|nearby|close to|next to|adjacent to|around)\\b(?: \\w+){0,6} ${SENSITIVE_SITE}\\b${NOT_AGGREGATE_TAIL}`,
  `\\b${SENSITIVE_SITE}\\b(?: \\w+){0,6} (?:located|locations?|nearest|closest|near|nearby|close to|next to|adjacent to|around)\\b`,
  "\\bwhere\\b(?: \\w+){0,4} (?:lek|nest|den|roost)s?\\b",
].join("|"));

// Any other mention of a sensitive site abstains, whatever the verb (show, list, plot, point out …),
// unless the whole request has one of a few recognised shapes: a count or county-level summary, a
// "why" or "how is it generalized" policy question, a definition, a question about map symbols, or a
// question about the layer, dataset or source itself. A matching word elsewhere is not enough.
const SENSITIVE_SITE_MENTION = new RegExp(`\\b${SENSITIVE_SITE}\\b`);
const SITE_COMMAND = /^(?:please )?(?:(?:can|could|would|will) you (?:please )?|i (?:want|d like|would like) (?:to (?:see|view|know) )?|let me (?:see|view|know) )?(?:show|plot|map|list|display|highlight|mark|point|identify|find|give|tell|guide|take|draw|label|zoom|navigate|direct|locate|pin|pinpoint|reveal|get|fetch|return|output|print)\b/;
const SITE_COMMAND_SOURCE = SITE_COMMAND.source.slice(1);
// A policy question asks why something is withheld, generalized or protected, not "why is the mound at
// Smith Ranch" or "why not list …".
const WHY_POLICY = /^why (?:are|is|were|was|do|does|did|must|should|would) (?:\w+ ){0,5}(?:withh[eo]ld|redact\w*|generali[sz]\w*|protect\w*|hidden|restricted|sensitive|coarsened|rounded|removed|excluded|omitted|blurred|aggregated|private|confidential|kept|stale|missing|unavailable|delayed|limited|labell?ed|marked|treated|handled)\b/;
const AGGREGATE_NOUN = "(?:numbers?|counts?|totals?|summary|summaries|share|percent\\w*|density|trends?)";
// A count that also asks for the sites themselves ("how many … can you list", "… please list them")
// is an enumeration, not a summary.
const ENUMERATION_TAIL = /\b(?:can|could|would|will) you (?:\w+ )?(?:list|show|name|map|plot|identify|tell|give)\b|\b(?:please|then|now) (?:list|show|name|map|plot|identify|tell|give)\b|\b(?:list|name|enumerate|identify) (?:them|those|these|each|all|every)\b|\bwhich ones\b|\bwhere\b|\b(?:names?|named|identit\w*|locations?|each one|one by one|individually|itemi[sz]\w*)\b|\bbroken down by (?:name|site|location)\b/;
const SITE_AGGREGATE_SHAPES = [
  /^how many\b/,
  new RegExp(`^(?:what|which) (?:is|are|was|were) the ${AGGREGATE_NOUN} of\\b`),
  new RegExp(`^${SITE_COMMAND_SOURCE} (?:me )?(?:the )?${AGGREGATE_NOUN} (?:of|by|per)\\b`),
  new RegExp(`\\b${SENSITIVE_SITE}\\b(?: \\w+){0,2} (?:by|per) (?:county|counties|state|region|year|decade)$`),
];
// Definitions may carry ordinary modifiers ("what is a prairie-chicken lek", "what are burial mounds"),
// but not inventory words ("the known nests", "all archaeological sites") or proper nouns.
const DEFINITION_MODIFIERS = "(?:(?!(?:the|all|any|these|those|known|mapped|recorded|documented|surveyed|monitored|protected|withheld|local|nearby|our|your|their|its)\\b)\\w+ ){0,3}";
const SITE_DEFINITION = new RegExp(`^what (?:is|are) (?:an? )?${DEFINITION_MODIFIERS}${SENSITIVE_SITE}$|^what (?:does|do) (?:the )?(?:word |term )?${DEFINITION_MODIFIERS}${SENSITIVE_SITE} mean$|^define (?:an? )?${DEFINITION_MODIFIERS}${SENSITIVE_SITE}$`);
const SITE_ALLOWED_SHAPES = [
  // Policy and map presentation.
  // "Why not list …" and "why don't you show …" are commands, not policy questions.
  WHY_POLICY,
  new RegExp(`^(?:how|why) (?:are|is|were|was|do|does) (?:\\w+ ){0,4}${SENSITIVE_SITE}\\b(?: \\w+){0,3} (?:generali[sz]\\w*|withh[eo]ld|redact\\w*|protect\\w*|symboli[sz]\\w*|shown|displayed|represented|handled|treated|coarsened)\\b`),
  /^what (?:symbols?|colou?rs?|icons?|styles?|legend)\b/,
];
// A question about the layer, dataset or source itself, unless it asks which sites it contains.
const SITE_METADATA_QUESTION = /^(?:is|are|was|were|when|how (?:fresh|current|old|recent|often)|what|which|who|compare)\b.*\b(?:layers?|datasets?|data|sources?|surveys?|records?|licen[cs]\w*|provenance|metadata|agenc\w+)\b/;
const SITE_ENUMERATION = new RegExp(`^(?:what|which) (?:(?:are|is|were|was) )?(?:the |all |any )?(?:\\w+ )?${SENSITIVE_SITE}\\b`);

const SENSITIVE_SITE_LOCATING = SITE_ENUMERATION;

// "Which records contain the burial sites?", "which source lists the nests?": enumeration behind a
// metadata noun.
const SITE_CONTAINMENT = new RegExp(`\\b(?:contain\\w*|list\\w*|includ\\w*|has|have|show\\w*|maps?|marks?|locat\\w*|names?)\\b(?: \\w+){0,3} ${SENSITIVE_SITE}\\b`);

function sensitiveSiteMentionAllowed(text, { properNoun = false } = {}) {
  if (SITE_AGGREGATE_SHAPES.some((shape) => shape.test(text))) return !ENUMERATION_TAIL.test(text);
  if (!properNoun && SITE_DEFINITION.test(text)) return true;
  if (SITE_ALLOWED_SHAPES.some((shape) => shape.test(text))) return true;
  return SITE_METADATA_QUESTION.test(text) && !SITE_ENUMERATION.test(text) && !SITE_CONTAINMENT.test(text);
}

// Coordinate and ZIP terms ask for a precise value unless the clause is about the term itself
// ("what does UTM mean", "which UTM zone", "why are coordinates withheld").
const PRECISE_TERM_WORDS = "(?:coordinates?|gps(?: coordinates?)?|lat long|latitude|longitude|lat lon\\w*|lat lng|latlon\\w*|latlng|utm(?: coordinates?)?|eastings?|northings?|zip(?: ?codes?)?|postal codes?)";
const PRECISE_TERM = /\b(?:coordinates?|gps|lat long|latitude|longitude|lat lon\w*|lat lng|latlon\w*|latlng|utm|eastings?|northings?|zip(?: ?codes?)?|postal codes?)\b(?! (?:files?|archives?|downloads?)\b)/;
const PRECISE_TERM_ABOUT_SHAPES = [
  // A direct definition ("what are coordinates", "what is a ZIP code"), not "what are the coordinates".
  new RegExp(`^what (?:is|are) (?:an? )?${PRECISE_TERM_WORDS}$`),
  // A definition, not a value request that merely ends in "… what it means".
  /^what (?:does|do) (?:the )?(?:\w+ ){0,3}(?:mean|stand for)$|^what is the meaning of\b/,
  /^(?:which|what) (?:\w+ ){0,2}(?:zones?|projections?|datums?|systems?|formats?|precision|accuracy)\b/,
  /^how (?:precise|accurate|rounded|generali[sz]ed|coarse)\b/,
  new RegExp(`^define (?:an? )?${PRECISE_TERM_WORDS}$|^explain what (?:an? )?${PRECISE_TERM_WORDS} (?:is|are|means?)$`),
  WHY_POLICY,
];

// Each clause is checked on its own, so a harmless trailing clause ("… and why is the map
// generalized?") cannot excuse a precise or locating request in another. A clause that only
// continues the first ("what do latitude | and longitude mean") is judged with the whole question,
// but only when no later clause starts a question of its own ("… and which ranch has them").
const CLAUSE_BREAK = /[?;:!.,()\u2013\u2014]+|\b(?:and|but|then|also|plus)\b/i;
const NEW_QUESTION = new RegExp(`^(?:what|which|where|how|when|who|whose|why|is|are|was|were|can|could|would|will|do|does|did)\\b|${SITE_COMMAND.source}`);
const LOCATING_CLAUSE = new RegExp(`^where\\b|${SITE_COMMAND.source}|\\b(?:near|nearby|nearest|closest|located|locations?)\\b`);
const POLICY_CLAUSE = /^(?:how|why) (?:are|is|were|was|do|does) (?:\w+ ){0,4}(?:generali[sz]\w*|withh[eo]ld|redact\w*|protect\w*|symboli[sz]\w*|shown|displayed|represented|handled|treated|coarsened)\b/;
const preciseAbout = (text) => PRECISE_TERM_ABOUT_SHAPES.some((shape) => shape.test(text));

function siteClauseBlocked(clause, index, wholeAllowed, options) {
  const newQuestion = index > 0 && NEW_QUESTION.test(clause);
  if (SENSITIVE_SITE_MENTION.test(clause)) {
    if (sensitiveSiteMentionAllowed(clause, options)) return false;
    return !wholeAllowed || newQuestion || LOCATING_CLAUSE.test(clause) || SENSITIVE_SITE_LOCATING.test(clause);
  }
  if (LOCATING_CLAUSE.test(clause) || ENUMERATION_TAIL.test(clause)) return true;
  // A later question about sites already named must itself be a summary, policy or metadata question.
  return newQuestion && !sensitiveSiteMentionAllowed(clause, options) && !POLICY_CLAUSE.test(clause)
    && !SITE_METADATA_QUESTION.test(clause);
}

function preciseClauseBlocked(clause, index, wholeAbout) {
  if (!PRECISE_TERM.test(clause)) return false;
  if (SITE_COMMAND.test(clause)) return true;
  if (preciseAbout(clause)) return false;
  return !wholeAbout || (index > 0 && NEW_QUESTION.test(clause));
}

// A capitalised word after the first names a place ("Ellis County nests", "Cheyenne Bottoms roost")
// unless it is a question word, a site noun or an ordinary modifier, so title case ("What Is A
// Prairie-Chicken Lek?") is not mistaken for a place name.
const COMMON_CAPITALISED = new Set(("what which is are a an the of does do define mean means meaning "
  + "burial burials grave graves mound mounds archaeological site sites nest nests nesting lek leks den dens roost "
  + "roosts roosting hibernaculum hibernacula prairie chicken chickens lesser greater sage grouse bird birds eagle "
  + "bald golden heron herons bat bats raptor raptors hawk owl crane cranes native ancient historic indian").split(" "));

function hasProperNoun(question) {
  if (typeof question !== "string") return false;
  const words = question.match(/[A-Za-z]+/g) ?? [];
  return words.slice(1).some((word) => /^[A-Z]/.test(word) && !COMMON_CAPITALISED.has(word.toLowerCase()));
}

export function isSensitiveQwenQuestion(question) {
  const text = normalizeScopeText(question);
  if (SENSITIVE_QUESTION.test(text)) return true;
  const clauses = typeof question === "string"
    ? question.split(CLAUSE_BREAK).map(normalizeScopeText).filter(Boolean)
    : [];
  const judgedTogether = clauses.slice(1).every((clause) => !NEW_QUESTION.test(clause));
  if (SENSITIVE_SITE_MENTION.test(text)) {
    // A capitalised word after the first ("What are Ellis County nests?") names a place, not a kind.
    const options = { properNoun: hasProperNoun(question) };
    const wholeAllowed = judgedTogether && sensitiveSiteMentionAllowed(text, options);
    if (clauses.some((clause, index) => siteClauseBlocked(clause, index, wholeAllowed, options))) return true;
  }
  const wholeAbout = judgedTogether && !SITE_COMMAND.test(text) && preciseAbout(text);
  return clauses.some((clause, index) => preciseClauseBlocked(clause, index, wholeAbout));
}

const sha256 = (value) => `sha256:${createHash("sha256").update(value).digest("hex")}`;
const tokenCount = (value) => Number.isSafeInteger(value) && value >= 0 ? value : null;

async function chatWithOllama(fetcher, ollamaUrl, model, signal, { messages, format, numPredict }) {
  const upstream = await fetcher(`${ollamaUrl}/api/chat`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      model,
      stream: false,
      think: false,
      tools: [],
      format,
      keep_alive: QWEN_LOCAL_KEEP_ALIVE,
      messages,
      options: { temperature: 0, num_predict: numPredict, num_ctx: QWEN_LOCAL_CONTEXT_WINDOW_TOKENS },
    }),
    redirect: "error",
    signal,
  });
  if (!upstream.ok) {
    await upstream.body?.cancel().catch(() => undefined);
    throw new Error("OLLAMA_ERROR");
  }
  const payload = await boundedJson(upstream, QWEN_LOCAL_MAX_REPLY_BYTES, signal);
  const raw = payload?.message?.content;
  let decoded = null;
  try { decoded = typeof raw === "string" ? JSON.parse(raw) : null; } catch { decoded = null; }
  return {
    decoded,
    promptTokens: tokenCount(payload?.prompt_eval_count),
    outputTokens: tokenCount(payload?.eval_count),
  };
}

export function createLocalQwenBridge({
  fetcher = fetch,
  ollamaUrl = OLLAMA_URL,
  model = LOCAL_QWEN_MODEL,
  allowedOrigins = QWEN_LOCAL_ALLOWED_ORIGINS,
  logger = null,
} = {}) {
  if (ollamaUrl !== OLLAMA_URL || model !== LOCAL_QWEN_MODEL) {
    throw new TypeError("The governed local Qwen bridge uses its pinned loopback endpoint and model.");
  }
  const originAllowlist = new Set(allowedOrigins);
  if (originAllowlist.size !== QWEN_LOCAL_ALLOWED_ORIGINS.length
    || QWEN_LOCAL_ALLOWED_ORIGINS.some((origin) => !originAllowlist.has(origin))) {
    throw new TypeError("The governed local Qwen origin allowlist is fixed.");
  }
  if (logger !== null && typeof logger !== "function") throw new TypeError("The bridge logger must be a function.");
  let busy = false;
  return createServer(async (req, res) => {
    const startedAt = performance.now();
    const path = req.url?.split("?", 1)[0];
    const trace = {
      requestId: randomUUID(),
      profile: "none",
      modelInvoked: false,
      contextSha256: null,
      knowledgeVersion: null,
      knowledgeDigest: null,
      knowledgeSourceIds: [],
      promptTokens: null,
      outputTokens: null,
    };
    /** Every ask reply carries its receipt; the log line carries no question or answer text. */
    const reply = (origin, status, outcome, reasonCode, extras = {}) => {
      const receipt = { ...trace, latencyMs: Math.max(0, Math.round(performance.now() - startedAt)) };
      const envelope = localQwenAskEnvelope(outcome, reasonCode, { ...extras, receipt });
      send(res, origin, status, envelope);
      logger?.({
        event: "kfm.qwen.request",
        route: ["/health", "/ask"].includes(path) ? path : "other",
        requestId: receipt.requestId,
        httpStatus: status,
        outcome,
        reasonCode,
        profile: receipt.profile,
        modelInvoked: receipt.modelInvoked,
        latencyMs: receipt.latencyMs,
        promptTokens: receipt.promptTokens,
        outputTokens: receipt.outputTokens,
        knowledgeSourceIds: receipt.knowledgeSourceIds,
        interpretation: envelope.interpretation !== null,
      });
    };
    const origin = req.headers.origin;
    const allowedOrigin = typeof origin === "string" && originAllowlist.has(origin) ? origin : null;
    const localRequest = isLoopbackPeer(req.socket.remoteAddress) && isLoopbackHost(req.headers.host);
    if (!localRequest || !allowedOrigin) {
      discardRequestBody(req);
      reply(null, 403, "DENY", "ORIGIN_NOT_ALLOWED");
      return;
    }
    if (!["/health", "/ask"].includes(path) || req.url !== path) {
      discardRequestBody(req);
      reply(allowedOrigin, 404, "ERROR", "ROUTE_NOT_FOUND");
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
        localQwenHealthEnvelope(state.status, state.reasonCode, {
          knowledgeDigest: QWEN_KNOWLEDGE_DIGEST,
          ollamaVersion: state.ollamaVersion ?? null,
        }),
      );
      return;
    }
    if (req.method !== "POST" || path !== "/ask"
      || req.headers["content-type"]?.split(";", 1)[0].trim().toLowerCase() !== "application/json") {
      discardRequestBody(req);
      reply(allowedOrigin, 415, "ERROR", "JSON_REQUEST_REQUIRED");
      return;
    }
    if (busy) {
      discardRequestBody(req);
      reply(allowedOrigin, 429, "ERROR", "BRIDGE_BUSY");
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
          reply(allowedOrigin, 408, "ERROR", "REQUEST_TIMEOUT");
          return;
        }
        reply(allowedOrigin, 413, "ERROR", "INVALID_OR_OVERSIZED_REQUEST");
        return;
      }
      const question = typeof body?.question === "string" ? body.question.trim() : "";
      if (!isRecord(body) || Object.keys(body).some((key) => key !== "question" && key !== "context")
        || !question || question.length > 1200 || QUESTION_CONTROL_CHARACTERS.test(question)
        || !validContext(body.context)) {
        reply(allowedOrigin, 400, "ERROR", "INVALID_REQUEST_SHAPE");
        return;
      }
      trace.contextSha256 = sha256(JSON.stringify(body.context));
      const evidence = inspectLocalQwenEvidence(body.context);
      if (evidence.disposition === "withheld") {
        reply(allowedOrigin, 200, "DENY", "POLICY_WITHHELD");
        return;
      }
      if (evidence.disposition === "error") {
        reply(allowedOrigin, 200, "ERROR", "EVIDENCE_RESOLUTION_ERROR");
        return;
      }
      const selectionScoped = evidence.disposition === "supported"
        && questionTargetsSelection(question, body.context.selection);
      if (!selectionScoped) {
        const abstainReason = evidence.disposition === "supported"
          ? "QUESTION_OUTSIDE_SELECTION_SCOPE"
          : evidence.disposition === "context-only" ? "CONTEXT_ONLY_INTERPRETATION" : "EVIDENCE_NOT_SUPPORTIVE";
        if (isSensitiveQwenQuestion(question)) {
          reply(allowedOrigin, 200, "ABSTAIN", "SENSITIVE_QUESTION_NOT_INTERPRETED");
          return;
        }
        const modelState = await installedModelState(fetcher, ollamaUrl, model, requestDeadline);
        if (modelState.status !== "ready") {
          reply(allowedOrigin, 503, "ERROR", modelState.reasonCode);
          return;
        }
        const knowledge = selectQwenKnowledge(question, body.context, {
          maxBytes: QWEN_LOCAL_INTERPRETATION_PROMPT_BUDGET_BYTES - Buffer.byteLength(JSON.stringify(body.context)),
        });
        Object.assign(trace, {
          profile: "context-interpretation-v1",
          modelInvoked: true,
          knowledgeVersion: QWEN_KNOWLEDGE_VERSION,
          knowledgeDigest: knowledge.digest,
          knowledgeSourceIds: [...knowledge.sourceIds],
        });
        const chat = await chatWithOllama(fetcher, ollamaUrl, model, withDeadline(requestDeadline, QWEN_LOCAL_INFERENCE_TIMEOUT_MS), {
          format: QWEN_LOCAL_INTERPRETATION_SCHEMA,
          numPredict: QWEN_LOCAL_MAX_INTERPRETATION_TOKENS,
          messages: [
            { role: "system", content: INTERPRETATION_SYSTEM_PROMPT },
            { role: "user", content: interpretationPromptFor(question, body.context, knowledge.payload, abstainReason) },
          ],
        });
        trace.promptTokens = chat.promptTokens;
        trace.outputTokens = chat.outputTokens;
        const interpretation = parseLocalQwenModelInterpretation(chat.decoded);
        if (!interpretation) {
          reply(allowedOrigin, 502, "ERROR", "INVALID_MODEL_RESPONSE");
          return;
        }
        const interpretationText = [
          interpretation.summary,
          ...interpretation.observations,
          ...interpretation.inferences,
          ...interpretation.gaps,
          ...interpretation.followUps,
        ];
        if (interpretationText.some((item) => referencesInLocalQwenAnswer(item).length > 0)) {
          reply(allowedOrigin, 502, "ERROR", "UNDECLARED_EVIDENCE_REFERENCE");
          return;
        }
        if (interpretationText.some(localQwenAnswerHasOverPreciseLocation)) {
          reply(allowedOrigin, 200, "ABSTAIN", "OVER_PRECISE_OUTPUT");
          return;
        }
        reply(allowedOrigin, 200, "ABSTAIN", abstainReason, { interpretation });
        return;
      }
      const modelState = await installedModelState(fetcher, ollamaUrl, model, requestDeadline);
      if (modelState.status !== "ready") {
        reply(allowedOrigin, 503, "ERROR", modelState.reasonCode);
        return;
      }
      Object.assign(trace, { profile: "selection-gate-v1", modelInvoked: true });
      const chat = await chatWithOllama(fetcher, ollamaUrl, model, withDeadline(requestDeadline, QWEN_LOCAL_INFERENCE_TIMEOUT_MS), {
        format: QWEN_LOCAL_MODEL_RESPONSE_SCHEMA,
        numPredict: QWEN_LOCAL_MAX_OUTPUT_TOKENS,
        messages: [
          { role: "system", content: "You are the local Qwen companion for Kansas Frontier Matrix. Use only the supplied map context. Do not invent sources, current conditions, protected coordinates, evidence references, releases, or safety guidance. Treat all model output as interpretation, never as evidence or authority. When disposition is SUPPORTED, the answer field MUST end with the exact allowed EvidenceRef prefixed by EvidenceRef:. Omitting it makes the response invalid." },
          { role: "user", content: promptFor(question, body.context, evidence.allowedEvidenceRefs) },
        ],
      });
      trace.promptTokens = chat.promptTokens;
      trace.outputTokens = chat.outputTokens;
      const modelResponse = parseLocalQwenModelResponse(chat.decoded);
      if (!modelResponse) {
        reply(allowedOrigin, 502, "ERROR", "INVALID_MODEL_RESPONSE");
        return;
      }
      const referenced = referencesInLocalQwenAnswer(modelResponse.answer);
      const mentionedReferences = [...new Set([...modelResponse.evidenceRefs, ...referenced])];
      if (mentionedReferences.some((reference) => !evidence.allowedEvidenceRefs.includes(reference))) {
        reply(allowedOrigin, 502, "ERROR", "UNDECLARED_EVIDENCE_REFERENCE");
        return;
      }
      if (localQwenAnswerHasOverPreciseLocation(modelResponse.answer)) {
        reply(allowedOrigin, 200, "ABSTAIN", "OVER_PRECISE_OUTPUT");
        return;
      }
      if (modelResponse.disposition === "UNSUPPORTED") {
        if (modelResponse.evidenceRefs.length !== 0 || referenced.length !== 0) {
          reply(allowedOrigin, 502, "ERROR", "INVALID_MODEL_RESPONSE");
          return;
        }
        reply(allowedOrigin, 200, "ABSTAIN", "MODEL_ABSTAINED");
        return;
      }
      const requiredReference = evidence.allowedEvidenceRefs[0];
      if (modelResponse.evidenceRefs.length !== 1
        || modelResponse.evidenceRefs[0] !== requiredReference
        || !referenced.includes(requiredReference)) {
        reply(allowedOrigin, 200, "ABSTAIN", "CITATION_REQUIRED");
        return;
      }
      const groundedAnswer = supportedSelectionAnswer(body.context.selection, requiredReference);
      if (localQwenAnswerHasOverPreciseLocation(groundedAnswer)) {
        reply(allowedOrigin, 200, "ABSTAIN", "OVER_PRECISE_OUTPUT");
        return;
      }
      const groundedReferences = referencesInLocalQwenAnswer(groundedAnswer);
      if (groundedReferences.some((reference) => !evidence.allowedEvidenceRefs.includes(reference))) {
        reply(allowedOrigin, 502, "ERROR", "UNDECLARED_EVIDENCE_REFERENCE");
        return;
      }
      if (groundedReferences.length !== 1 || groundedReferences[0] !== requiredReference) {
        reply(allowedOrigin, 200, "ABSTAIN", "CITATION_REQUIRED");
        return;
      }
      reply(allowedOrigin, 200, "ANSWER", "SUPPORTED_SELECTION_INTERPRETATION", {
        answer: groundedAnswer,
        evidenceRefs: [requiredReference],
      });
    } catch (error) {
      if (requestDeadline.aborted
        || (error instanceof LocalQwenRequestError && error.code === "REQUEST_TIMEOUT")
        || error?.name === "TimeoutError" || error?.name === "AbortError") {
        reply(allowedOrigin, 504, "ERROR", "REQUEST_TIMEOUT");
      } else {
        reply(allowedOrigin, 502, "ERROR", "LOCAL_MODEL_UNAVAILABLE");
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
  const logger = (entry) => process.stdout.write(`${JSON.stringify({ at: new Date().toISOString(), ...entry })}\n`);
  createLocalQwenBridge({ logger }).listen(LOCAL_BRIDGE_PORT, "127.0.0.1", () => {
    process.stdout.write(`KFM local Qwen bridge ${LOCAL_QWEN_BRIDGE_VERSION} ready on 127.0.0.1:${LOCAL_BRIDGE_PORT} · ${LOCAL_QWEN_MODEL} · knowledge ${QWEN_KNOWLEDGE_DIGEST.slice(0, 19)}\n`);
  });
}
