import type { AssistantContext } from "./assistant-context";

export type InvestigationResult = {
  outcome: string; reasonCode: string; answer: string | null; interpretation: string | null;
  sourceSummary?: string; contextLimited?: boolean; outputLimited?: boolean; truncated?: boolean;
  citations?: { evidenceRef: string; title: string; url: string }[];
};
export type InvestigationJob = {
  id: string; state: string; deadline: number; result: InvestigationResult | null;
  checkedAt?: string; sourceRevision?: string | null; releaseId?: string | null;
  contextReleaseId?: string | null; evidenceReleaseId?: string | null;
  context?: { label: string; boundary: string; references?: { label: string; url: string; role: string }[] } | null;
};

const digest = (value: unknown) => typeof value === "string" && /^sha256:[a-f0-9]{64}$/.test(value) ? value : null;
const bounded = (value: unknown, limit: number) => typeof value === "string"
  ? value.replace(/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/g, "").slice(0, limit) : "";
const object = (value: unknown): value is Record<string, unknown> => value !== null && typeof value === "object" && !Array.isArray(value);

// Project only submitted display scope, never current focus, camera, browser
// location, free-form attributes, credentials, private notes or account state.
function scope(value: unknown) {
  if (!object(value) || value.version !== 1 || !Number.isInteger(value.frame) ||
      Number(value.frame) < -5e9 || Number(value.frame) > 2200) return null;
  const context = value as unknown as AssistantContext;
  const selection = object(context.selection) ? context.selection : null;
  let record: Record<string, unknown> | null = null;
  if (selection?.kind === "subsurface") record = { kind: selection.kind, tileId: bounded(selection.tileId, 80),
    recordId: bounded(selection.recordId, 160), intervalIndex: Number.isInteger(selection.intervalIndex) ? selection.intervalIndex : null };
  if (selection?.kind === "registry") record = { kind: selection.kind, layerId: bounded(selection.layerId, 160), featureId: bounded(selection.featureId, 160) };
  if (selection?.kind === "knowledge") record = { kind: selection.kind, recordId: bounded(selection.recordId, 128) };
  if (selection?.kind === "display") record = { kind: "display", note: "Browser attributes omitted; unverified display context only." };
  const comparison = object(context.comparison) && Number.isInteger(context.comparison.frameA) && Number.isInteger(context.comparison.frameB)
    ? { frameA: context.comparison.frameA, frameB: context.comparison.frameB } : null;
  return { mapDisplayYear: context.frame, timeMeaning: "Display frame, not a collection, drilling or observation date",
    view: ["2D", "Terrain 3D", "Globe", "Compare", "Page"].includes(context.view) ? context.view : "Unspecified",
    layers: Array.isArray(context.layers) ? context.layers.slice(0, 14).map(id => bounded(id, 160)) : [],
    filters: context.filters ? { evidence: bounded(context.filters.evidence, 40), temporalMode: bounded(context.filters.temporalMode, 40) } : null,
    comparison, selection: record };
}

function sourceUrl(value: string) {
  try {
    const url = new URL(value, "https://kansasfrontiermatrix.com");
    if (url.protocol !== "https:" || url.username || url.password) return null;
    if (url.pathname === "/knowledge/record" && (value.startsWith("/knowledge/record?") ||
        ["https://kansasfrontiermatrix.com", "https://www.kansasfrontiermatrix.com"].includes(url.origin))) return url.pathname + url.search;
    if (url.hostname === "kgs.ku.edu" || url.hostname.endsWith(".kgs.ku.edu")) return url.href;
  } catch { /* No unverified or invented source links in the draft. */ }
  return null;
}

/** Application export projection, not an evidence, release or approval contract. */
export function buildInvestigationDraft(question: string, submittedContext: unknown, job: InvestigationJob) {
  const result = job.result;
  if (job.state !== "completed" || !result || !["ABSTAIN", "DENY", "ERROR"].includes(result.outcome) ||
      !/^[A-Z][A-Z0-9_]{1,100}$/.test(result.reasonCode) || !job.checkedAt || !Number.isFinite(Date.parse(job.checkedAt))) {
    throw new Error("INVESTIGATION_NOT_CHECKED");
  }
  const withheld = result.outcome !== "ABSTAIN" || ["RELEASE_CHANGED", "CONTEXT_UNAVAILABLE", "CONTEXT_TIME_MISMATCH", "EVIDENCE_WITHHELD"].includes(result.reasonCode);
  if (!withheld && result.reasonCode === "SOURCE_CONTEXT_ONLY" &&
      (!digest(job.sourceRevision) || !job.context || !bounded(result.sourceSummary, 4096))) throw new Error("INVESTIGATION_NOT_CHECKED");
  const released = digest(job.releaseId);
  const contextRelease = digest(job.contextReleaseId === undefined ? job.releaseId : job.contextReleaseId);
  const evidenceRelease = digest(job.evidenceReleaseId === undefined ? job.releaseId : job.evidenceReleaseId);
  const references = !withheld ? (job.context?.references ?? []).flatMap(ref => {
    const url = sourceUrl(ref.url);
    if (!url || !["SOURCE_CONTEXT", "RELEASED_RECORD"].includes(ref.role) || ref.role === "RELEASED_RECORD" && !contextRelease) return [];
    return [{ label: bounded(ref.label, 240), url, role: ref.role, releaseId: ref.role === "RELEASED_RECORD" ? contextRelease : null }];
  }).slice(0, 4) : [];
  const citations = !withheld && evidenceRelease ? (result.citations ?? []).flatMap(ref => {
    const url = sourceUrl(ref.url);
    return url?.startsWith("/knowledge/record?") ? [{ title: bounded(ref.title, 200), url, evidenceRef: bounded(ref.evidenceRef, 240), releaseId: evidenceRelease }] : [];
  }).slice(0, 4) : [];
  return {
    format: "kfm-investigation-draft-v1", status: "DRAFT", publication: "NOT_PUBLISHED", checkedAt: job.checkedAt,
    question: withheld ? "Withheld from export" : bounded(question, 4096),
    scope: withheld ? null : scope(submittedContext),
    context: !withheld && job.context ? { label: bounded(job.context.label, 240), boundary: bounded(job.context.boundary, 240) } : null,
    sourceCheck: { fingerprint: withheld ? null : digest(job.sourceRevision), releaseId: withheld ? null : released,
      contextReleaseId: withheld ? null : contextRelease, evidenceReleaseId: withheld ? null : evidenceRelease,
      meaning: "Response rechecked at export time; fingerprint is not source admission, factual proof or release approval." },
    result: { outcome: result.outcome, reasonCode: result.reasonCode, answer: null,
      sourceSummary: !withheld && result.reasonCode === "SOURCE_CONTEXT_ONLY" ? bounded(result.sourceSummary, 4096) : null,
      generatedDiscussion: !withheld && result.reasonCode === "UNVERIFIED_AI_DISCUSSION" ? bounded(result.interpretation, 16384) : null },
    references, citations,
    limitations: [
      "Source summaries are external context, not admitted KFM evidence. Generated discussion is unverified. No supported factual answer is asserted.",
      "This draft records a past check. Sources can change or be withdrawn; reopen the original sources before reuse.",
      "The display frame is separate from each source date. Missing values and intervals remain unknown.",
      ...(result.contextLimited ? ["Earlier conversation was omitted to fit the model context."] : []),
      ...(result.outputLimited ? ["The generated reply reached a resource limit and may be incomplete."] : []),
      ...(result.truncated ? ["The bounded search may omit additional records."] : []),
    ],
  };
}

// Escape authored/model text so a rendered Markdown draft cannot acquire
// executable HTML or fabricated link markup from the conversation.
const md = (text: string) => text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/[\\`*_{}\[\]()#+!|~]/g, "\\$&");
export function investigationMarkdown(draft: ReturnType<typeof buildInvestigationDraft>) {
  return ["# KFM investigation", "", "> DRAFT · NOT PUBLISHED · No supported factual answer asserted", "",
    "Checked: " + draft.checkedAt, "", "## Research question", "", md(draft.question), "",
    "## Scope", "", draft.context ? md(draft.context.label + " · " + draft.context.boundary) : "No reusable source context established.",
    ...(draft.scope ? ["Map display year: " + draft.scope.mapDisplayYear + " · " + draft.scope.timeMeaning,
      "View: " + draft.scope.view, "Layer IDs: " + md(draft.scope.layers.join(", ") || "none"),
      "Selection: " + md(JSON.stringify(draft.scope.selection)), "Filters: " + md(JSON.stringify(draft.scope.filters)),
      "Comparison: " + md(JSON.stringify(draft.scope.comparison))] : []), "",
    "## Outcome", "", draft.result.outcome + " · " + draft.result.reasonCode,
    ...(draft.result.sourceSummary ? ["", "### Source summary · not admitted evidence", "", md(draft.result.sourceSummary)] : []),
    ...(draft.result.generatedDiscussion ? ["", "### Generated discussion · unverified", "", md(draft.result.generatedDiscussion)] : []),
    "", "## Sources to inspect", "", ...draft.references.map(ref => "- " + md(ref.label) + " — " + ref.url + " · " + ref.role),
    ...draft.citations.map(ref => "- " + md(ref.title) + " — " + ref.url + " · " + md(ref.evidenceRef)),
    ...(!draft.references.length && !draft.citations.length ? ["No reusable source references returned."] : []),
    "", "Response fingerprint: " + (draft.sourceCheck.fingerprint ?? "not available"),
    "Context release ID: " + (draft.sourceCheck.contextReleaseId ?? "none established"),
    "Evidence-search release ID: " + (draft.sourceCheck.evidenceReleaseId ?? "none established"), md(draft.sourceCheck.meaning),
    "", "## Limitations", "", ...draft.limitations.map(item => "- " + md(item)), ""].join("\n");
}
