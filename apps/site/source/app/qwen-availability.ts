import {
  QWEN_LOCAL_ASK_TIMEOUT_MS,
  QWEN_LOCAL_BRIDGE_ORIGIN,
  QWEN_LOCAL_BROWSER_HEALTH_TIMEOUT_MS,
  QWEN_LOCAL_MAX_REPLY_BYTES,
  QWEN_LOCAL_MODEL,
  QWEN_LOCAL_OLLAMA_MIN_VERSION,
  localQwenHealthStatus,
  parseLocalQwenAskEnvelope,
} from "../scripts/qwen-local-contract.mjs";

export { QWEN_LOCAL_MODEL, QWEN_LOCAL_OLLAMA_MIN_VERSION };

export const QWEN_LOCAL_BROWSER_CONFIG = Object.freeze({
  bridgeOrigin: QWEN_LOCAL_BRIDGE_ORIGIN,
  healthTimeoutMs: QWEN_LOCAL_BROWSER_HEALTH_TIMEOUT_MS,
  askTimeoutMs: QWEN_LOCAL_ASK_TIMEOUT_MS,
  maxReplyBytes: QWEN_LOCAL_MAX_REPLY_BYTES,
});

/** Local bridge readiness and observed answers are separate finite states. */
export type QwenBridgeState =
  | "checking"
  | "ready"
  | "answered"
  | "abstained"
  | "busy"
  | "timeout"
  | "bridge-unavailable"
  | "ollama-unavailable"
  | "model-missing"
  | "denied"
  | "error";

export const isQwenHealthEnvelope = (value: unknown) => localQwenHealthStatus(value) !== null;
export const isQwenAskEnvelope = (value: unknown) => parseLocalQwenAskEnvelope(value) !== null;

/** Model language attached to an ABSTAIN; never evidence, never citable. */
export type QwenInterpretation = Readonly<{
  summary: string;
  observations: readonly string[];
  inferences: readonly string[];
  gaps: readonly string[];
  followUps: readonly string[];
}>;

export type QwenAskEnvelope = Readonly<{
  outcome: "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";
  reasonCode: string;
  answer: string | null;
  evidenceRefs: readonly string[];
  interpretation: QwenInterpretation | null;
  requestId: string | null;
}>;

export const parseQwenAskEnvelope = (value: unknown): QwenAskEnvelope | null => {
  const envelope = parseLocalQwenAskEnvelope(value);
  if (!envelope) return null;
  return {
    outcome: envelope.outcome as QwenAskEnvelope["outcome"],
    reasonCode: envelope.reasonCode,
    answer: envelope.answer,
    evidenceRefs: envelope.evidenceRefs,
    interpretation: envelope.interpretation,
    requestId: envelope.receipt?.requestId ?? null,
  };
};

export const qwenStateFromHealth = (value: unknown): QwenBridgeState => {
  const status = localQwenHealthStatus(value);
  if (status === "model_missing") return "model-missing";
  if (status === "ollama_unavailable") return "ollama-unavailable";
  if (status === "ready") return "ready";
  return "error";
};

export const shouldUseLocalQwen = (state: QwenBridgeState) =>
  state === "ready" || state === "answered" || state === "abstained";

export const qwenStateFromTransportFailure = (
  timedOut: boolean,
  responseReceived: boolean,
): QwenBridgeState => timedOut ? "timeout" : responseReceived ? "error" : "bridge-unavailable";

export const qwenStateFromAsk = (value: unknown): QwenBridgeState => {
  const envelope = parseLocalQwenAskEnvelope(value);
  if (!envelope) return "error";
  if (envelope.outcome === "ANSWER") return "answered";
  if (envelope.outcome === "ABSTAIN") return "abstained";
  if (envelope.outcome === "DENY") return "denied";
  if (envelope.reasonCode === "BRIDGE_BUSY") return "busy";
  if (envelope.reasonCode === "REQUEST_TIMEOUT") return "timeout";
  if (envelope.reasonCode === "OLLAMA_UNAVAILABLE") return "ollama-unavailable";
  if (envelope.reasonCode === "MODEL_MISSING") return "model-missing";
  return "error";
};

export const qwenStatusLabel = (state: QwenBridgeState): string => {
  switch (state) {
    case "checking": return "CHECKING LOCAL QWEN";
    case "ready": return "LOCAL QWEN READY";
    case "answered": return "LOCAL QWEN ANSWERED";
    case "abstained": return "LOCAL QWEN ABSTAINED";
    case "busy": return "LOCAL QWEN BUSY";
    case "timeout": return "LOCAL QWEN TIMED OUT";
    case "bridge-unavailable": return "LOCAL BRIDGE UNREACHABLE";
    case "ollama-unavailable": return "OLLAMA NOT RUNNING";
    case "model-missing": return `${QWEN_LOCAL_MODEL.toUpperCase()} NOT INSTALLED`;
    case "denied": return "LOCAL REQUEST DENIED";
    case "error": return "LOCAL QWEN REQUEST FAILED";
  }
};
