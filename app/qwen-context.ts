import type { SoilMoistureEngineContext } from "./soil-moisture-control";
import {
  hasRequiredLocalQwenContext,
  inspectLocalQwenEvidence,
} from "../scripts/qwen-local-contract.mjs";
import { hasSafeQwenContextShape } from "./qwen-context-safety.mjs";

export type QwenLayerContext = Readonly<{
  id: string;
  title: string;
  domain: string;
  sourceType: string;
  releaseState: string;
  publicStatus: string;
  freshnessState: string;
  evidenceReference: string;
}>;

export type QwenSelectionContext = Readonly<{
  featureId: string;
  title: string;
  layerId: string;
  layerTitle: string;
  domain: string;
  evidenceState: string;
  evidenceReference: string;
  reviewState: string;
  releaseState: string;
  sourceYear: number;
  spatialScope: string;
  summary: string;
}>;

export type QwenMapContext = Readonly<{
  camera: Readonly<{
    center: readonly [number, number];
    locationRedacted: boolean;
    zoom: number;
    bearing: number;
    pitch: number;
    projection: string;
    representation: string;
  }>;
  basemap: Readonly<{ key: string; title: string; note: string }>;
  time: Readonly<{ value: number; label: string; era: string }>;
  visibleLayers: readonly QwenLayerContext[];
  officialSources: readonly Readonly<{
    id: string;
    title: string;
    selected: boolean;
    displayed: boolean;
    state: string;
    featureCount: number | null;
    retrievedAt: string | null;
    evidenceRole: "EXTERNAL_CONTEXT_ONLY";
  }>[];
  soilMoisture?: SoilMoistureEngineContext | null;
  telemetry: Readonly<{
    authority: "SITE_LOCAL_REDACTED_DIAGNOSTIC";
    renderer: Readonly<{ state: string; styleLoaded: boolean; canvasReady: boolean; tilesLoaded: boolean; failedChecks: readonly string[] }>;
    registry: Readonly<{ total: number; ready: number; loading: number; error: number }>;
    radar: Readonly<{ state: string; frameTime: string | null; manifestFresh: boolean }>;
    streamflow: Readonly<{ state: string; frameTime: string | null }>;
  }>;
  selection: QwenSelectionContext | null;
  nearbyContext: readonly Readonly<{
    title: string;
    layerTitle: string;
    distanceMiles: number;
    evidenceState: string;
  }>[];
}>;

export const QWEN_CONTEXT_VERSION = "kfm-qwen-map-context-v1";

export const QWEN_SYSTEM_PROMPT = [
  "You are the Qwen contextual companion for the Kansas Frontier Matrix Explorer.",
  "Use only the supplied map context and evidence labels; do not invent sources, current conditions, people, DNA, sensitive coordinates, releases, or safety guidance.",
  "Treat imagery, tiles, labels, overlays, measurements, and model language as context carriers rather than authority.",
  "For soil moisture, distinguish a selected frame from a confirmed rendered frame. A visualTransition is only a color-image blend between exact NASA daily frames, or a fade through the basemap across a missing-day/loop reset; it is not a numeric temporal or spatial estimate. Colorized GIBS tiles contain no numeric pixel samples in this context; do not infer point values, local wetness, or water travel from their colors.",
  "Keep observations separate from inferences. If the supplied context cannot support an answer, say so plainly and identify the missing gate.",
  "Never upgrade synthetic or generalized fixtures into operational data. Never reveal protected precision.",
  "Answer briefly, with the active place, time, visible layers, and evidence boundary in view.",
].join(" ");

export const normalizeQwenQuestion = (value: unknown) => {
  const question = typeof value === "string" ? value.trim() : "";
  return question.slice(0, 1200);
};

/**
 * Keep a bounded context while making a deny-significant record impossible to
 * hide just past the cap. The original order is preserved unless one
 * restrictive record would otherwise be omitted, in which case it replaces
 * the final sampled item.
 */
export const policyPreservingQwenSample = <T,>(
  values: readonly T[],
  maximum: number,
  isRestrictive: (value: T) => boolean,
) => {
  if (!Number.isInteger(maximum) || maximum <= 0) return [] as readonly T[];
  const bounded = values.slice(0, maximum);
  if (bounded.some(isRestrictive)) return bounded;
  const restrictive = values.find(isRestrictive);
  if (!restrictive) return bounded;
  return [...bounded.slice(0, maximum - 1), restrictive];
};

export const buildQwenPrompt = (question: string, context: QwenMapContext) => {
  const normalizedQuestion = normalizeQwenQuestion(question) || "What should I notice in this map view?";
  return [
    `Context contract: ${QWEN_CONTEXT_VERSION}`,
    `System rules: ${QWEN_SYSTEM_PROMPT}`,
    `User question: ${normalizedQuestion}`,
    "Map context (JSON):",
    JSON.stringify(context, null, 2),
    "Response rules: distinguish visible map context from evidence-backed support; cite the supplied evidenceReference when discussing a selection; treat release and review fields as gates rather than claims the model may change; state when a conclusion is unsupported; do not suggest that this response changes policy, review, release, or publication state.",
  ].join("\n\n");
};

/**
 * Clipboard export is a separate trust boundary. Only evidence-supported
 * selections, or a context-only view with no selection, may carry the full
 * bounded prompt. Denied, unsupported, malformed, and resolution-error
 * selections produce a policy receipt with sensitive carriers removed.
 */
export const buildCopyableQwenPrompt = (question: string, context: QwenMapContext) => {
  const evidence = inspectLocalQwenEvidence(context);
  const validContext = hasSafeQwenContextShape(context) && hasRequiredLocalQwenContext(context);
  if (validContext && evidence.ok && (evidence.disposition === "supported"
    || (evidence.disposition === "context-only" && context.selection === null))) {
    return buildQwenPrompt(question, context);
  }
  const outcome = evidence.disposition === "withheld"
    ? "DENY"
    : evidence.disposition === "unsupported"
      ? "ABSTAIN"
      : "ERROR";
  const reasonCode = evidence.disposition === "withheld"
    ? "POLICY_WITHHELD"
    : evidence.disposition === "unsupported"
      ? "EVIDENCE_NOT_SUPPORTIVE"
      : "EVIDENCE_RESOLUTION_ERROR";
  const safeFrame = {
    representation: context.camera?.representation ?? "UNKNOWN",
    basemap: context.basemap?.title ?? "UNKNOWN",
    time: context.time?.label ?? "UNKNOWN",
    visibleLayerCount: Array.isArray(context.visibleLayers) ? context.visibleLayers.length : 0,
    officialSourceCount: Array.isArray(context.officialSources) ? context.officialSources.length : 0,
    nearbyRecordCount: Array.isArray(context.nearbyContext) ? context.nearbyContext.length : 0,
  };
  return [
    `Context contract: ${QWEN_CONTEXT_VERSION}`,
    `System rules: ${QWEN_SYSTEM_PROMPT}`,
    `Copy outcome: ${outcome}`,
    `Reason: ${reasonCode}`,
    "Selection, question, coordinates, evidence identifiers, and policy-sensitive carriers were not copied.",
    "Safe frame (JSON):",
    JSON.stringify(safeFrame, null, 2),
  ].join("\n\n");
};
