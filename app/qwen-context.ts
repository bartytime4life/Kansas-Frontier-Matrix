export type QwenLayerContext = Readonly<{
  id: string;
  title: string;
  domain: string;
  sourceType: string;
  releaseState: string;
  publicStatus: string;
  freshnessState: string;
}>;

export type QwenSelectionContext = Readonly<{
  featureId: string;
  title: string;
  layerId: string;
  layerTitle: string;
  domain: string;
  evidenceState: string;
  evidenceReference: string;
  sourceYear: number;
  spatialScope: string;
  summary: string;
}>;

export type QwenMapContext = Readonly<{
  camera: Readonly<{
    center: readonly [number, number];
    zoom: number;
    bearing: number;
    pitch: number;
    projection: string;
    representation: string;
  }>;
  basemap: Readonly<{ key: string; title: string; note: string }>;
  time: Readonly<{ value: number; label: string; era: string }>;
  visibleLayers: readonly QwenLayerContext[];
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
  "Keep observations separate from inferences. If the supplied context cannot support an answer, say so plainly and identify the missing gate.",
  "Never upgrade synthetic or generalized fixtures into operational data. Never reveal protected precision.",
  "Answer briefly, with the active place, time, visible layers, and evidence boundary in view.",
].join(" ");

export const normalizeQwenQuestion = (value: unknown) => {
  const question = typeof value === "string" ? value.trim() : "";
  return question.slice(0, 1200);
};

export const buildQwenPrompt = (question: string, context: QwenMapContext) => {
  const normalizedQuestion = normalizeQwenQuestion(question) || "What should I notice in this map view?";
  return [
    `Context contract: ${QWEN_CONTEXT_VERSION}`,
    `User question: ${normalizedQuestion}`,
    "Map context (JSON):",
    JSON.stringify(context, null, 2),
    "Response rules: distinguish visible map context from evidence-backed support; cite the supplied evidenceReference when discussing a selection; state when a conclusion is unsupported; do not suggest that this response changes policy, review, release, or publication state.",
  ].join("\n\n");
};
