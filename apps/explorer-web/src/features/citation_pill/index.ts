import {
  type GovernedEvidenceDrawerProjection,
  parseEvidenceDrawerProjection,
} from "../../adapters/GovernedClient";

export type CitationPillView = "map" | "story" | "focus";

export type CitationPillVisibility = "VISIBLE" | "HIDDEN";

export type CitationPillReason =
  | "SUPPORTED"
  | "NO_GOVERNED_RESPONSE"
  | "INVALID_GOVERNED_RESPONSE"
  | "NON_ANSWER_OUTCOME"
  | "UNSUPPORTED_REASON"
  | "MISSING_EVIDENCE"
  | "AMBIGUOUS_EVIDENCE"
  | "INVALID_EVIDENCE_REF"
  | "EVIDENCE_REF_NOT_BOUND"
  | "POLICY_NOT_ALLOWED"
  | "REVIEW_NOT_COMPLETE"
  | "RELEASE_NOT_PUBLIC"
  | "STALE_EVIDENCE"
  | "SUPERSEDED_EVIDENCE"
  | "INVALID_TIMESTAMP"
  | "INVALID_VIEW";

export type CitationPillOptions = Readonly<{
  timestamp?: string;
  view?: CitationPillView;
  evidenceRef?: string;
  label?: string;
}>;

export type CitationPillMountOptions = CitationPillOptions &
  Readonly<{
    copyText?: (text: string) => Promise<void> | void;
  }>;

export type CitationPillViewModel = Readonly<{
  visibility: CitationPillVisibility;
  reason: CitationPillReason;
  status: "VERIFIED" | null;
  label: string;
  title: string;
  evidenceRef: string | null;
  timestamp: string | null;
  view: CitationPillView | null;
  deepLink: string | null;
  canCopy: boolean;
  accessibilityLabel: string;
}>;

export type CitationPillController = Readonly<{
  state: CitationPillViewModel;
  show: () => void;
  hide: () => void;
  copy: () => Promise<boolean>;
  destroy: () => void;
}>;

type ResolvedCitationPill = Readonly<{
  state: CitationPillViewModel;
  payload: GovernedEvidenceDrawerProjection | null;
}>;

const DEFAULT_LABEL = "Evidence";
const DEFAULT_VIEW: CitationPillView = "map";
const UTC_SECOND_PATTERN = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const KFM_EVIDENCE_URI_PATTERN = /^kfm:\/\/evidence\/[A-Za-z0-9][A-Za-z0-9._~:-]{2,255}$/;
const KFM_EVIDENCE_ID_PATTERN = /^kfm:evidence:[A-Za-z0-9][A-Za-z0-9._:-]{2,255}$/;
const EMPTY_TITLE = "Evidence link unavailable";
let citationPillSequence = 0;

function hidden(reason: CitationPillReason): CitationPillViewModel {
  return Object.freeze({
    visibility: "HIDDEN",
    reason,
    status: null,
    label: DEFAULT_LABEL,
    title: EMPTY_TITLE,
    evidenceRef: null,
    timestamp: null,
    view: null,
    deepLink: null,
    canCopy: false,
    accessibilityLabel: "Evidence citation unavailable",
  });
}

function isUtcSecond(value: unknown): value is string {
  if (typeof value !== "string" || !UTC_SECOND_PATTERN.test(value)) return false;
  const milliseconds = Date.parse(value);
  if (!Number.isFinite(milliseconds) || milliseconds % 1000 !== 0) return false;
  return new Date(milliseconds).toISOString().replace(".000Z", "Z") === value;
}

function isEvidenceRef(value: unknown): value is string {
  if (typeof value !== "string") return false;
  if (/[\u0000-\u0020\u007f?#]/.test(value)) return false;
  return KFM_EVIDENCE_URI_PATTERN.test(value) || KFM_EVIDENCE_ID_PATTERN.test(value);
}

function isCitationPillView(value: unknown): value is CitationPillView {
  return value === "map" || value === "story" || value === "focus";
}

function displayLabel(value: unknown): string {
  if (typeof value !== "string") return DEFAULT_LABEL;
  const normalized = value.trim().replace(/\s+/g, " ");
  if (normalized.length === 0) return DEFAULT_LABEL;
  return normalized.slice(0, 80);
}

function selectEvidenceRef(
  evidenceRefs: readonly string[],
  requested: string | undefined,
): Readonly<{ ref: string | null; reason: CitationPillReason | null }> {
  if (requested !== undefined) {
    if (!isEvidenceRef(requested)) {
      return Object.freeze({ ref: null, reason: "INVALID_EVIDENCE_REF" });
    }
    if (!evidenceRefs.includes(requested)) {
      return Object.freeze({ ref: null, reason: "EVIDENCE_REF_NOT_BOUND" });
    }
    return Object.freeze({ ref: requested, reason: null });
  }

  if (evidenceRefs.length === 0) {
    return Object.freeze({ ref: null, reason: "MISSING_EVIDENCE" });
  }
  if (evidenceRefs.length !== 1) {
    return Object.freeze({ ref: null, reason: "AMBIGUOUS_EVIDENCE" });
  }
  const only = evidenceRefs[0];
  if (!isEvidenceRef(only)) {
    return Object.freeze({ ref: null, reason: "INVALID_EVIDENCE_REF" });
  }
  return Object.freeze({ ref: only, reason: null });
}

function buildDeepLink(
  evidenceRef: string,
  timestamp: string,
  view: CitationPillView,
): string {
  return `${evidenceRef}?t=${encodeURIComponent(timestamp)}&view=${view}`;
}

function resolveProjection(
  input: unknown | undefined,
  options: CitationPillOptions,
): ResolvedCitationPill {
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
  if (!isUtcSecond(options.timestamp)) {
    return Object.freeze({ state: hidden("INVALID_TIMESTAMP"), payload: null });
  }

  const view = options.view ?? DEFAULT_VIEW;
  if (!isCitationPillView(view)) {
    return Object.freeze({ state: hidden("INVALID_VIEW"), payload: null });
  }

  const selected = selectEvidenceRef(payload.evidenceRefs, options.evidenceRef);
  if (selected.ref === null || selected.reason !== null) {
    return Object.freeze({
      state: hidden(selected.reason ?? "INVALID_EVIDENCE_REF"),
      payload: null,
    });
  }

  const label = displayLabel(options.label);
  const state: CitationPillViewModel = Object.freeze({
    visibility: "VISIBLE",
    reason: "SUPPORTED",
    status: "VERIFIED",
    label,
    title: payload.title,
    evidenceRef: selected.ref,
    timestamp: options.timestamp,
    view,
    deepLink: buildDeepLink(selected.ref, options.timestamp, view),
    canCopy: true,
    accessibilityLabel: `${label}: verified evidence for ${payload.title}`,
  });

  return Object.freeze({ state, payload });
}

/**
 * Resolve an existing governed Evidence Drawer projection into an inline citation pill.
 *
 * This app-local projection is intentionally narrower than the source packet: it emits only
 * VERIFIED because the current governed payload has authoritative fields for reviewed,
 * released, current support but no canonical PROPOSED or UNKNOWN citation status. Every
 * non-supported state fails closed to no pill.
 */
export function resolveCitationPill(
  input?: unknown,
  options: CitationPillOptions = {},
): CitationPillViewModel {
  return resolveProjection(input, options).state;
}

async function fallbackCopy(document: Document, text: string): Promise<void> {
  const textarea = document.createElement("textarea");
  textarea.value = text;
  textarea.setAttribute("readonly", "");
  textarea.setAttribute("aria-hidden", "true");
  textarea.style.position = "fixed";
  textarea.style.opacity = "0";
  document.body.append(textarea);
  textarea.select();
  const copied = document.execCommand("copy");
  textarea.remove();
  if (!copied) throw new Error("copy command was rejected");
}

async function copyDeepLink(
  document: Document,
  text: string,
  injected?: (text: string) => Promise<void> | void,
): Promise<void> {
  if (injected !== undefined) {
    await injected(text);
    return;
  }

  const clipboard = document.defaultView?.navigator.clipboard;
  if (clipboard !== undefined && typeof clipboard.writeText === "function") {
    await clipboard.writeText(text);
    return;
  }
  await fallbackCopy(document, text);
}

/**
 * Mount an accessible, copy-only citation pill for one released EvidenceRef.
 *
 * The controller performs no navigation and does not define a canonical KFM deep-link
 * contract. It only formats the source packet's proposed link grammar for a later governed
 * route adapter. Rendering uses text nodes and contains no transport or lifecycle-store access.
 */
export function mountCitationPill(
  host: HTMLElement,
  input?: unknown,
  options: CitationPillMountOptions = {},
): CitationPillController {
  const resolved = resolveProjection(input, options);
  const { state, payload } = resolved;
  host.replaceChildren();

  if (
    state.visibility === "HIDDEN" ||
    payload === null ||
    state.evidenceRef === null ||
    state.timestamp === null ||
    state.deepLink === null
  ) {
    return Object.freeze({
      state,
      show: () => undefined,
      hide: () => undefined,
      copy: async () => false,
      destroy: () => host.replaceChildren(),
    });
  }

  const document = host.ownerDocument;
  const wrapper = document.createElement("span");
  const toggle = document.createElement("button");
  const status = document.createElement("span");
  const region = document.createElement("span");
  const title = document.createElement("strong");
  const evidenceLabel = document.createElement("span");
  const evidenceCode = document.createElement("code");
  const linkLabel = document.createElement("span");
  const linkCode = document.createElement("code");
  const copyButton = document.createElement("button");
  const liveStatus = document.createElement("span");
  const regionId = `kfm-citation-pill-${++citationPillSequence}`;
  let destroyed = false;

  wrapper.dataset.component = "citation-pill";

  toggle.type = "button";
  toggle.dataset.component = "citation-pill-toggle";
  toggle.setAttribute("aria-controls", regionId);
  toggle.setAttribute("aria-expanded", "false");
  toggle.setAttribute("aria-label", state.accessibilityLabel);
  toggle.append(document.createTextNode(state.label), document.createTextNode(" "));

  status.dataset.component = "citation-pill-status";
  status.setAttribute("aria-label", "Status: VERIFIED");
  status.textContent = "■ VERIFIED";
  toggle.append(status);

  region.id = regionId;
  region.hidden = true;
  region.dataset.component = "citation-pill-region";
  region.setAttribute("role", "region");
  region.setAttribute("aria-label", `Evidence citation for ${state.title}`);

  title.textContent = state.title;
  evidenceLabel.textContent = "EvidenceRef: ";
  evidenceCode.textContent = state.evidenceRef;
  linkLabel.textContent = " Evidence link: ";
  linkCode.textContent = state.deepLink;

  copyButton.type = "button";
  copyButton.dataset.component = "citation-pill-copy";
  copyButton.textContent = "Copy evidence link";
  copyButton.setAttribute(
    "aria-label",
    `Copy evidence link for ${state.title} at ${state.timestamp}`,
  );

  liveStatus.dataset.component = "citation-pill-copy-status";
  liveStatus.setAttribute("role", "status");
  liveStatus.setAttribute("aria-live", "polite");

  region.append(
    title,
    document.createTextNode(" "),
    evidenceLabel,
    evidenceCode,
    linkLabel,
    linkCode,
    document.createTextNode(" "),
    copyButton,
    liveStatus,
  );
  wrapper.append(toggle, region);
  host.append(wrapper);

  const show = (): void => {
    if (destroyed) return;
    region.hidden = false;
    toggle.setAttribute("aria-expanded", "true");
  };

  const hide = (): void => {
    if (destroyed) return;
    region.hidden = true;
    toggle.setAttribute("aria-expanded", "false");
  };

  const copy = async (): Promise<boolean> => {
    if (destroyed) return false;
    try {
      await copyDeepLink(document, state.deepLink as string, options.copyText);
      liveStatus.textContent = "Link copied.";
      return true;
    } catch {
      liveStatus.textContent = "Copy unavailable.";
      return false;
    }
  };

  const onToggle = (): void => {
    if (region.hidden) show();
    else hide();
  };
  const onCopy = (): void => {
    void copy();
  };
  const onKeyDown = (event: KeyboardEvent): void => {
    if (event.key !== "Escape" || region.hidden) return;
    event.preventDefault();
    hide();
    toggle.focus();
  };

  toggle.addEventListener("click", onToggle);
  copyButton.addEventListener("click", onCopy);
  wrapper.addEventListener("keydown", onKeyDown);

  const destroy = (): void => {
    if (destroyed) return;
    destroyed = true;
    toggle.removeEventListener("click", onToggle);
    copyButton.removeEventListener("click", onCopy);
    wrapper.removeEventListener("keydown", onKeyDown);
    host.replaceChildren();
  };

  return Object.freeze({ state, show, hide, copy, destroy });
}
