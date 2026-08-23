export const TRUST_STATE_PRIMITIVE_PROFILE =
  "kfm.explorer.trust-state-primitives.v1" as const;

export const TRUST_STATE_OUTCOMES = [
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
  "LOADING",
] as const;
export const TRUST_STATE_EVIDENCE = [
  "RESOLVED",
  "UNRESOLVED",
  "STALE",
  "RESTRICTED",
  "ERROR",
  "PENDING",
] as const;
export const TRUST_STATE_FRESHNESS = [
  "CURRENT",
  "STALE",
  "UNKNOWN",
  "PENDING",
] as const;
export const TRUST_STATE_SENSITIVITY = [
  "PUBLIC_SAFE",
  "GENERALIZED",
  "RESTRICTED",
  "UNKNOWN",
] as const;
export const TRUST_STATE_RELEASE = [
  "RELEASED",
  "UNRELEASED",
  "WITHDRAWN",
  "UNKNOWN",
  "PENDING",
] as const;
export const TRUST_STATE_CORRECTION = [
  "NONE",
  "CORRECTED",
  "SUPERSEDED",
  "UNKNOWN",
  "PENDING",
] as const;

export type TrustStateOutcome = (typeof TRUST_STATE_OUTCOMES)[number];
export type TrustStateEvidence = (typeof TRUST_STATE_EVIDENCE)[number];
export type TrustStateFreshness = (typeof TRUST_STATE_FRESHNESS)[number];
export type TrustStateSensitivity = (typeof TRUST_STATE_SENSITIVITY)[number];
export type TrustStateRelease = (typeof TRUST_STATE_RELEASE)[number];
export type TrustStateCorrection = (typeof TRUST_STATE_CORRECTION)[number];
export type TrustStateTone = "positive" | "caution" | "critical" | "neutral";

export type TrustStateSummaryInput = Readonly<{
  profile: typeof TRUST_STATE_PRIMITIVE_PROFILE;
  caseId: string;
  outcome: TrustStateOutcome;
  evidence: TrustStateEvidence;
  freshness: TrustStateFreshness;
  sensitivity: TrustStateSensitivity;
  release: TrustStateRelease;
  correction: TrustStateCorrection;
  title: string;
  message: string;
}>;

export type TrustStateBadge = Readonly<{
  key: "outcome" | "evidence" | "freshness" | "sensitivity" | "release" | "correction";
  label: string;
  value: string;
}>;

export type TrustStateSummary = Readonly<{
  profile: typeof TRUST_STATE_PRIMITIVE_PROFILE;
  valid: boolean;
  code: TrustStateOutcome | "INVALID_TRUST_STATE";
  caseId: string;
  outcome: TrustStateOutcome;
  title: string;
  message: string;
  badges: readonly TrustStateBadge[];
  tone: TrustStateTone;
  role: "status" | "alert";
  ariaLive: "polite" | "assertive";
  ariaBusy: boolean;
  accessibilityLabel: string;
}>;

export type TrustStateSummaryController = Readonly<{
  state: TrustStateSummary;
  destroy: () => void;
}>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "caseId",
  "outcome",
  "evidence",
  "freshness",
  "sensitivity",
  "release",
  "correction",
  "title",
  "message",
]);
const OUTCOMES = new Set<string>(TRUST_STATE_OUTCOMES);
const EVIDENCE = new Set<string>(TRUST_STATE_EVIDENCE);
const FRESHNESS = new Set<string>(TRUST_STATE_FRESHNESS);
const SENSITIVITY = new Set<string>(TRUST_STATE_SENSITIVITY);
const RELEASE = new Set<string>(TRUST_STATE_RELEASE);
const CORRECTION = new Set<string>(TRUST_STATE_CORRECTION);
const SAFE_CASE_ID = /^[a-z][a-z0-9-]{0,63}$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
const MAX_TITLE_LENGTH = 120;
const MAX_MESSAGE_LENGTH = 280;

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  expected: ReadonlySet<string>,
): boolean {
  const keys = Object.keys(value);
  return keys.length === expected.size && keys.every((key) => expected.has(key));
}

function isBoundedText(value: unknown, maximum: number): value is string {
  return (
    typeof value === "string" &&
    value.length > 0 &&
    value.length <= maximum &&
    value.trim() === value &&
    !CONTROL_CHARACTER.test(value)
  );
}

function badge(
  key: TrustStateBadge["key"],
  label: string,
  value: string,
): TrustStateBadge {
  return Object.freeze({ key, label, value });
}

function combinationIsValid(input: TrustStateSummaryInput): boolean {
  if (input.outcome === "ANSWER") {
    return (
      input.evidence === "RESOLVED" &&
      input.freshness === "CURRENT" &&
      (input.sensitivity === "PUBLIC_SAFE" ||
        input.sensitivity === "GENERALIZED") &&
      input.release === "RELEASED" &&
      (input.correction === "NONE" || input.correction === "CORRECTED")
    );
  }

  if (input.outcome === "ABSTAIN") {
    const evidenceMatches =
      input.evidence === "UNRESOLVED" || input.evidence === "STALE";
    const freshnessMatches =
      input.evidence === "STALE"
        ? input.freshness === "STALE"
        : input.freshness === "UNKNOWN";
    return (
      evidenceMatches &&
      freshnessMatches &&
      input.sensitivity !== "RESTRICTED" &&
      input.release !== "PENDING" &&
      input.correction !== "PENDING"
    );
  }

  if (input.outcome === "DENY") {
    return (
      input.evidence === "RESTRICTED" &&
      input.sensitivity === "RESTRICTED" &&
      (input.freshness === "UNKNOWN" || input.freshness === "STALE") &&
      input.release !== "RELEASED" &&
      input.release !== "PENDING" &&
      input.correction !== "PENDING"
    );
  }

  if (input.outcome === "ERROR") {
    return (
      input.evidence === "ERROR" &&
      input.freshness === "UNKNOWN" &&
      input.sensitivity === "UNKNOWN" &&
      input.release === "UNKNOWN" &&
      input.correction === "UNKNOWN"
    );
  }

  return (
    input.evidence === "PENDING" &&
    input.freshness === "PENDING" &&
    input.sensitivity === "UNKNOWN" &&
    input.release === "PENDING" &&
    input.correction === "PENDING"
  );
}

function invalidSummary(): TrustStateSummary {
  return Object.freeze({
    profile: TRUST_STATE_PRIMITIVE_PROFILE,
    valid: false,
    code: "INVALID_TRUST_STATE",
    caseId: "invalid",
    outcome: "ERROR",
    title: "Trust state unavailable",
    message: "The public trust-state projection is invalid. No claim-bearing detail is shown.",
    badges: Object.freeze([
      badge("outcome", "Outcome", "ERROR"),
      badge("evidence", "Evidence", "ERROR"),
    ]),
    tone: "critical",
    role: "alert",
    ariaLive: "assertive",
    ariaBusy: false,
    accessibilityLabel: "Trust state: invalid public projection",
  });
}

/**
 * Validate one closed, text-first public trust-state summary.
 *
 * This app-local primitive is presentation metadata only. It does not evaluate
 * policy, resolve evidence, admit sources, change release state, or infer
 * sensitivity. Unknown or inconsistent input fails closed to a fixed error.
 */
export function resolveTrustStateSummary(input?: unknown): TrustStateSummary {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return invalidSummary();
  }
  if (
    input.profile !== TRUST_STATE_PRIMITIVE_PROFILE ||
    typeof input.caseId !== "string" ||
    !SAFE_CASE_ID.test(input.caseId) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome) ||
    typeof input.evidence !== "string" ||
    !EVIDENCE.has(input.evidence) ||
    typeof input.freshness !== "string" ||
    !FRESHNESS.has(input.freshness) ||
    typeof input.sensitivity !== "string" ||
    !SENSITIVITY.has(input.sensitivity) ||
    typeof input.release !== "string" ||
    !RELEASE.has(input.release) ||
    typeof input.correction !== "string" ||
    !CORRECTION.has(input.correction) ||
    !isBoundedText(input.title, MAX_TITLE_LENGTH) ||
    !isBoundedText(input.message, MAX_MESSAGE_LENGTH)
  ) {
    return invalidSummary();
  }

  const normalized: TrustStateSummaryInput = Object.freeze({
    profile: TRUST_STATE_PRIMITIVE_PROFILE,
    caseId: input.caseId,
    outcome: input.outcome as TrustStateOutcome,
    evidence: input.evidence as TrustStateEvidence,
    freshness: input.freshness as TrustStateFreshness,
    sensitivity: input.sensitivity as TrustStateSensitivity,
    release: input.release as TrustStateRelease,
    correction: input.correction as TrustStateCorrection,
    title: input.title,
    message: input.message,
  });
  if (!combinationIsValid(normalized)) return invalidSummary();

  const isError = normalized.outcome === "ERROR";
  const isLoading = normalized.outcome === "LOADING";
  const tone: TrustStateTone =
    normalized.outcome === "ANSWER"
      ? "positive"
      : normalized.outcome === "DENY" || isError
        ? "critical"
        : normalized.outcome === "ABSTAIN"
          ? "caution"
          : "neutral";

  return Object.freeze({
    profile: TRUST_STATE_PRIMITIVE_PROFILE,
    valid: true,
    code: normalized.outcome,
    caseId: normalized.caseId,
    outcome: normalized.outcome,
    title: normalized.title,
    message: normalized.message,
    badges: Object.freeze([
      badge("outcome", "Outcome", normalized.outcome),
      badge("evidence", "Evidence", normalized.evidence),
      badge("freshness", "Freshness", normalized.freshness),
      badge("sensitivity", "Sensitivity", normalized.sensitivity),
      badge("release", "Release", normalized.release),
      badge("correction", "Correction", normalized.correction),
    ]),
    tone,
    role: isError ? "alert" : "status",
    ariaLive: isError ? "assertive" : "polite",
    ariaBusy: isLoading,
    accessibilityLabel: `Trust state: ${normalized.outcome.toLocaleLowerCase()} — ${normalized.evidence.toLocaleLowerCase()}`,
  });
}

/** Mount one reusable, non-color-only trust-state summary. */
export function mountTrustStateSummary(
  host: HTMLElement,
  input?: unknown,
): TrustStateSummaryController {
  const state = resolveTrustStateSummary(input);
  const document = host.ownerDocument;
  const region = document.createElement("section");
  const heading = document.createElement("h3");
  const message = document.createElement("p");
  const badgeList = document.createElement("dl");

  region.dataset.component = "trust-state-summary";
  region.dataset.outcome = state.outcome;
  region.dataset.tone = state.tone;
  region.setAttribute("role", state.role);
  region.setAttribute("aria-label", state.accessibilityLabel);
  region.setAttribute("aria-live", state.ariaLive);
  region.setAttribute("aria-busy", state.ariaBusy ? "true" : "false");
  heading.textContent = state.title;
  message.textContent = state.message;
  badgeList.setAttribute("aria-label", "Public trust-state labels");

  for (const item of state.badges) {
    const row = document.createElement("div");
    const term = document.createElement("dt");
    const value = document.createElement("dd");
    row.dataset.trustStateField = item.key;
    term.textContent = item.label;
    value.textContent = item.value;
    row.append(term, value);
    badgeList.append(row);
  }

  region.append(heading, message, badgeList);
  host.replaceChildren(region);

  return Object.freeze({
    state,
    destroy(): void {
      host.replaceChildren();
    },
  });
}
