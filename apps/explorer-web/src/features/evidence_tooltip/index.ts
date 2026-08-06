import {
  type EvidenceDrawerCitation,
  type EvidenceDrawerTrustState,
  type GovernedEvidenceDrawerProjection,
  parseEvidenceDrawerProjection,
} from "../../adapters/GovernedClient";

export type EvidenceTooltipVisibility = "VISIBLE" | "HIDDEN";

export type EvidenceTooltipReason =
  | "SUPPORTED"
  | "NO_GOVERNED_RESPONSE"
  | "INVALID_GOVERNED_RESPONSE"
  | "NON_ANSWER_OUTCOME"
  | "UNSUPPORTED_REASON"
  | "MISSING_EVIDENCE"
  | "POLICY_NOT_ALLOWED"
  | "REVIEW_NOT_COMPLETE"
  | "RELEASE_NOT_PUBLIC"
  | "STALE_EVIDENCE"
  | "SUPERSEDED_EVIDENCE";

export type EvidenceTooltipOptions = Readonly<{
  maxEvidenceRefs?: number;
  maxCitations?: number;
}>;

export type EvidenceTooltipViewModel = Readonly<{
  visibility: EvidenceTooltipVisibility;
  reason: EvidenceTooltipReason;
  title: string;
  summary: string;
  evidenceRefs: readonly string[];
  citationLabels: readonly string[];
  trustLabels: readonly string[];
  canOpenDrawer: boolean;
  accessibilityLabel: string;
}>;

export type EvidenceTooltipMountOptions = EvidenceTooltipOptions &
  Readonly<{
    onOpenDrawer?: (payload: GovernedEvidenceDrawerProjection) => void;
  }>;

export type EvidenceTooltipController = Readonly<{
  state: EvidenceTooltipViewModel;
  show: () => void;
  hide: () => void;
  destroy: () => void;
}>;

const DEFAULT_MAX_REFS = 3;
const MAX_ALLOWED_REFS = 8;
const EMPTY_STRINGS = Object.freeze([]) as readonly string[];
const HIDDEN_TITLE = "Evidence details unavailable";
const HIDDEN_SUMMARY = "No tooltip is shown unless released evidence passes every trust check.";
let tooltipSequence = 0;

function boundedCount(value: number | undefined, fallback: number): number {
  if (value === undefined || !Number.isInteger(value)) return fallback;
  return Math.min(Math.max(value, 1), MAX_ALLOWED_REFS);
}

function trustLabels(trustState: EvidenceDrawerTrustState): readonly string[] {
  return Object.freeze([
    `Source role: ${trustState.sourceRole}`,
    `Policy: ${trustState.policy}`,
    `Review: ${trustState.review}`,
    `Release: ${trustState.release}`,
    `Freshness: ${trustState.freshness}`,
    `Correction: ${trustState.correction}`,
  ]);
}

function hidden(reason: EvidenceTooltipReason): EvidenceTooltipViewModel {
  return Object.freeze({
    visibility: "HIDDEN",
    reason,
    title: HIDDEN_TITLE,
    summary: HIDDEN_SUMMARY,
    evidenceRefs: EMPTY_STRINGS,
    citationLabels: EMPTY_STRINGS,
    trustLabels: EMPTY_STRINGS,
    canOpenDrawer: false,
    accessibilityLabel: "Evidence tooltip unavailable",
  });
}

function resolveProjection(
  input: unknown | undefined,
  options: EvidenceTooltipOptions,
): Readonly<{
  state: EvidenceTooltipViewModel;
  payload: GovernedEvidenceDrawerProjection | null;
}> {
  if (input === undefined) {
    return Object.freeze({ state: hidden("NO_GOVERNED_RESPONSE"), payload: null });
  }

  const parsed = parseEvidenceDrawerProjection(input);
  if (!parsed.ok) {
    return Object.freeze({
      state: hidden("INVALID_GOVERNED_RESPONSE"),
      payload: null,
    });
  }

  const { payload } = parsed;
  if (payload.outcome !== "ANSWER") {
    return Object.freeze({ state: hidden("NON_ANSWER_OUTCOME"), payload: null });
  }
  if (payload.reasonCode !== "SUPPORTED") {
    return Object.freeze({ state: hidden("UNSUPPORTED_REASON"), payload: null });
  }
  if (payload.evidenceRefs.length === 0 || payload.citations.length === 0) {
    return Object.freeze({ state: hidden("MISSING_EVIDENCE"), payload: null });
  }
  if (payload.trustState.policy !== "ALLOW") {
    return Object.freeze({ state: hidden("POLICY_NOT_ALLOWED"), payload: null });
  }
  if (payload.trustState.review !== "REVIEWED") {
    return Object.freeze({ state: hidden("REVIEW_NOT_COMPLETE"), payload: null });
  }
  if (payload.trustState.release !== "RELEASED") {
    return Object.freeze({ state: hidden("RELEASE_NOT_PUBLIC"), payload: null });
  }
  if (payload.trustState.freshness !== "CURRENT") {
    return Object.freeze({ state: hidden("STALE_EVIDENCE"), payload: null });
  }
  if (payload.trustState.correction === "SUPERSEDED") {
    return Object.freeze({ state: hidden("SUPERSEDED_EVIDENCE"), payload: null });
  }

  const maximumEvidenceRefs = boundedCount(
    options.maxEvidenceRefs,
    DEFAULT_MAX_REFS,
  );
  const maximumCitations = boundedCount(options.maxCitations, DEFAULT_MAX_REFS);
  const state: EvidenceTooltipViewModel = Object.freeze({
    visibility: "VISIBLE",
    reason: "SUPPORTED",
    title: payload.title,
    summary: payload.summary,
    evidenceRefs: Object.freeze(payload.evidenceRefs.slice(0, maximumEvidenceRefs)),
    citationLabels: Object.freeze(
      payload.citations
        .slice(0, maximumCitations)
        .map((citation: EvidenceDrawerCitation) => citation.label),
    ),
    trustLabels: trustLabels(payload.trustState),
    canOpenDrawer: true,
    accessibilityLabel: "Evidence tooltip: released supporting evidence",
  });

  return Object.freeze({ state, payload });
}

/**
 * Resolve a strict governed Evidence Drawer projection into a small tooltip state.
 *
 * The tooltip intentionally accepts the existing governed browser projection rather
 * than arbitrary map-feature properties. Any missing, malformed, abstained, denied,
 * errored, unreleased, stale, unreviewed, or superseded state is represented by no
 * tooltip at all.
 */
export function resolveEvidenceTooltip(
  input?: unknown,
  options: EvidenceTooltipOptions = {},
): EvidenceTooltipViewModel {
  return resolveProjection(input, options).state;
}

/**
 * Mount a keyboard- and pointer-operable tooltip trigger for released evidence.
 *
 * The tooltip contains only text copied from the already-validated governed
 * projection. It performs no network requests, reads no lifecycle storage, and
 * delegates detailed evidence display to the existing Evidence Drawer callback.
 */
export function mountEvidenceTooltip(
  host: HTMLElement,
  input?: unknown,
  options: EvidenceTooltipMountOptions = {},
): EvidenceTooltipController {
  const resolved = resolveProjection(input, options);
  const { state, payload } = resolved;
  host.replaceChildren();

  if (state.visibility === "HIDDEN" || payload === null) {
    return Object.freeze({
      state,
      show: () => undefined,
      hide: () => undefined,
      destroy: () => host.replaceChildren(),
    });
  }

  const supportedPayload = payload;
  const document = host.ownerDocument;
  const trigger = document.createElement("button");
  const tooltip = document.createElement("div");
  const heading = document.createElement("strong");
  const summary = document.createElement("p");
  const trustList = document.createElement("ul");
  const evidenceList = document.createElement("ul");
  const citationList = document.createElement("ul");
  const tooltipId = `kfm-evidence-tooltip-${++tooltipSequence}`;
  let pointerInside = false;
  let focusInside = false;

  trigger.type = "button";
  trigger.textContent = "Evidence details";
  trigger.dataset.component = "evidence-tooltip-trigger";
  trigger.setAttribute("aria-describedby", tooltipId);
  trigger.setAttribute("aria-expanded", "false");

  tooltip.id = tooltipId;
  tooltip.hidden = true;
  tooltip.dataset.component = "evidence-tooltip";
  tooltip.setAttribute("role", "tooltip");
  tooltip.setAttribute("aria-label", state.accessibilityLabel);

  heading.textContent = state.title;
  summary.textContent = state.summary;

  trustList.setAttribute("aria-label", "Evidence trust snapshot");
  for (const label of state.trustLabels) {
    const item = document.createElement("li");
    item.textContent = label;
    trustList.append(item);
  }

  evidenceList.setAttribute("aria-label", "Evidence references");
  for (const evidenceRef of state.evidenceRefs) {
    const item = document.createElement("li");
    item.textContent = evidenceRef;
    evidenceList.append(item);
  }

  citationList.setAttribute("aria-label", "Evidence citations");
  for (const label of state.citationLabels) {
    const item = document.createElement("li");
    item.textContent = label;
    citationList.append(item);
  }

  tooltip.replaceChildren(
    heading,
    summary,
    trustList,
    evidenceList,
    citationList,
  );

  function show(): void {
    tooltip.hidden = false;
    trigger.setAttribute("aria-expanded", "true");
  }

  function hide(): void {
    tooltip.hidden = true;
    trigger.setAttribute("aria-expanded", "false");
  }

  function syncVisibility(): void {
    if (pointerInside || focusInside) show();
    else hide();
  }

  function onPointerEnter(): void {
    pointerInside = true;
    syncVisibility();
  }

  function onPointerLeave(): void {
    pointerInside = false;
    syncVisibility();
  }

  function onFocus(): void {
    focusInside = true;
    syncVisibility();
  }

  function onBlur(): void {
    focusInside = false;
    syncVisibility();
  }

  function onKeydown(event: KeyboardEvent): void {
    if (event.key !== "Escape") return;
    event.preventDefault();
    pointerInside = false;
    focusInside = false;
    hide();
  }

  function onClick(): void {
    options.onOpenDrawer?.(supportedPayload);
  }

  function destroy(): void {
    trigger.removeEventListener("mouseenter", onPointerEnter);
    trigger.removeEventListener("mouseleave", onPointerLeave);
    trigger.removeEventListener("focus", onFocus);
    trigger.removeEventListener("blur", onBlur);
    trigger.removeEventListener("keydown", onKeydown);
    trigger.removeEventListener("click", onClick);
    host.replaceChildren();
  }

  trigger.addEventListener("mouseenter", onPointerEnter);
  trigger.addEventListener("mouseleave", onPointerLeave);
  trigger.addEventListener("focus", onFocus);
  trigger.addEventListener("blur", onBlur);
  trigger.addEventListener("keydown", onKeydown);
  trigger.addEventListener("click", onClick);
  host.replaceChildren(trigger, tooltip);

  return Object.freeze({ state, show, hide, destroy });
}
