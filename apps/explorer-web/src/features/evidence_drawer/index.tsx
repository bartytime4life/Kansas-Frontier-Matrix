import {
  type EvidenceDrawerCitation,
  type EvidenceDrawerHistory,
  type EvidenceDrawerOutcome,
  type EvidenceDrawerReasonCode,
  type EvidenceDrawerTrustState,
  parseEvidenceDrawerProjection,
} from "../../adapters/GovernedClient";

export type EvidenceDrawerRepresentationDisclosure = Readonly<{
  kind: "DERIVED";
  label: "Derived representation";
  message: "Computed from upstream evidence; not a source-observed relationship or event.";
}>;

export type EvidenceDrawerViewModel = Readonly<{
  outcome: EvidenceDrawerOutcome;
  code: EvidenceDrawerReasonCode | "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD";
  title: string;
  message: string;
  representationDisclosure: EvidenceDrawerRepresentationDisclosure | null;
  evidenceRefs: readonly string[];
  evidenceRefsLabel:
    | "Current evidence references"
    | "Non-current evidence references";
  citations: readonly EvidenceDrawerCitation[];
  limitations: readonly string[];
  trustLabels: readonly string[];
  historyLabels: readonly string[];
  landmarkRole: "complementary";
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

export type EvidenceDrawerController = Readonly<{
  state: EvidenceDrawerViewModel;
  open: () => void;
  close: () => void;
  destroy: () => void;
}>;

type EvidenceDrawerDomIds = Readonly<{
  panelId: string;
  labelId: string;
  titleId: string;
}>;

const EMPTY_STRINGS = Object.freeze([]) as readonly string[];
const EMPTY_CITATIONS = Object.freeze([]) as readonly EvidenceDrawerCitation[];

export const DERIVED_REPRESENTATION_DISCLOSURE: EvidenceDrawerRepresentationDisclosure =
  Object.freeze({
    kind: "DERIVED",
    label: "Derived representation",
    message:
      "Computed from upstream evidence; not a source-observed relationship or event.",
  });

const SAFE_NEGATIVE_MESSAGES: Readonly<Record<EvidenceDrawerReasonCode, string>> =
  Object.freeze({
    SUPPORTED: "The governed evidence projection is available.",
    MISSING_EVIDENCE: "Required evidence is not available.",
    STALE_EVIDENCE: "Available evidence is stale for this request.",
    CITATION_UNRESOLVED: "One or more required citations could not be resolved.",
    POLICY_DENIED: "Policy does not permit this evidence detail to be shown.",
    RIGHTS_UNRESOLVED: "Source rights are not resolved for this evidence detail.",
    SENSITIVE_DETAIL_RESTRICTED: "Sensitive detail is restricted.",
    UPSTREAM_ERROR: "The governed evidence service could not complete the request.",
    HELD_EVIDENCE: "Evidence is held for review and is not current claim support.",
    SUPERSEDED_EVIDENCE: "The available evidence is superseded and is shown only as history.",
    WITHDRAWN_EVIDENCE: "The available evidence was withdrawn and is not current claim support.",
    REVOKED_EVIDENCE: "The available evidence was revoked and is not current claim support.",
  });

const HISTORY_STATE_LABELS = Object.freeze({
  HELD: "Held evidence",
  DENIED: "Denied evidence",
  SUPERSEDED: "Superseded evidence",
  REVOKED: "Revoked evidence",
  WITHDRAWN: "Withdrawn evidence",
});

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

function historyLabels(history: EvidenceDrawerHistory): readonly string[] {
  return Object.freeze([
    ...history.negativeOutcomes.map(
      (item) =>
        `${HISTORY_STATE_LABELS[item.state]}: ${item.evidenceRef} — ${SAFE_NEGATIVE_MESSAGES[item.reasonCode]}`,
    ),
    ...history.corrections.map(
      (item) =>
        `Correction lineage: ${item.priorEvidenceRef} → ${item.activeEvidenceRef} (${item.recordedAt})`,
    ),
  ]);
}

function negativeTrustLabels(
  outcome: "ABSTAIN" | "DENY" | "ERROR",
  labels: readonly string[],
): readonly string[] {
  if (outcome !== "ERROR") return labels;

  // An upstream or adapter error cannot establish a reliable release or
  // correction interpretation for the user. Keep stable policy/freshness cues,
  // but suppress those two fields rather than presenting conflicting detail.
  return Object.freeze(
    labels.filter(
      (label) =>
        !label.startsWith("Release: ") && !label.startsWith("Correction: "),
    ),
  );
}

function fixedNegativeView(
  outcome: "ABSTAIN" | "DENY" | "ERROR",
  code: EvidenceDrawerReasonCode,
  evidenceRefs: readonly string[],
  labels: readonly string[],
  history: readonly string[],
): EvidenceDrawerViewModel {
  const title =
    outcome === "ABSTAIN"
      ? "Evidence not sufficient"
      : outcome === "DENY"
        ? "Evidence restricted"
        : "Evidence unavailable";

  return Object.freeze({
    outcome,
    code,
    title,
    message: SAFE_NEGATIVE_MESSAGES[code],
    representationDisclosure: null,
    evidenceRefs: outcome === "ABSTAIN" ? evidenceRefs : EMPTY_STRINGS,
    evidenceRefsLabel: "Non-current evidence references",
    citations: EMPTY_CITATIONS,
    limitations: Object.freeze(["No unsupported claim is shown."]),
    trustLabels: negativeTrustLabels(outcome, labels),
    historyLabels: history,
    landmarkRole: "complementary",
    accessibilityLabel: `Evidence Drawer: ${outcome.toLowerCase()}`,
    ariaLive: outcome === "ERROR" ? "assertive" : "polite",
  });
}

/** Resolve a strict governed projection into a finite, no-leak UI state. */
export function resolveEvidenceDrawer(
  input?: unknown,
): EvidenceDrawerViewModel {
  if (input === undefined) {
    return Object.freeze({
      outcome: "ABSTAIN",
      code: "NO_GOVERNED_RESPONSE",
      title: "Evidence not available",
      message: "No governed evidence response is available.",
      representationDisclosure: null,
      evidenceRefs: EMPTY_STRINGS,
      evidenceRefsLabel: "Non-current evidence references",
      citations: EMPTY_CITATIONS,
      limitations: Object.freeze(["No unsupported claim is shown."]),
      trustLabels: Object.freeze(["Evidence state: unavailable"]),
      historyLabels: EMPTY_STRINGS,
      landmarkRole: "complementary",
      accessibilityLabel: "Evidence Drawer: no governed response",
      ariaLive: "polite",
    });
  }

  const parsed = parseEvidenceDrawerProjection(input);
  if (!parsed.ok) {
    return Object.freeze({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
      title: "Evidence unavailable",
      message: "The governed evidence response is invalid.",
      representationDisclosure: null,
      evidenceRefs: EMPTY_STRINGS,
      evidenceRefsLabel: "Non-current evidence references",
      citations: EMPTY_CITATIONS,
      limitations: Object.freeze(["No partial or unsupported claim is shown."]),
      trustLabels: Object.freeze(["Evidence state: invalid payload"]),
      historyLabels: EMPTY_STRINGS,
      landmarkRole: "complementary",
      accessibilityLabel: "Evidence Drawer: invalid governed response",
      ariaLive: "assertive",
    });
  }

  const { payload } = parsed;
  const labels = trustLabels(payload.trustState);
  const history = historyLabels(payload.history);
  if (payload.outcome !== "ANSWER") {
    return fixedNegativeView(
      payload.outcome,
      payload.reasonCode,
      payload.evidenceRefs,
      labels,
      history,
    );
  }

  return Object.freeze({
    outcome: "ANSWER",
    code: payload.reasonCode,
    title: payload.title,
    message: payload.summary,
    representationDisclosure:
      payload.trustState.sourceRole === "derived"
        ? DERIVED_REPRESENTATION_DISCLOSURE
        : null,
    evidenceRefs: payload.evidenceRefs,
    evidenceRefsLabel: "Current evidence references",
    citations: payload.citations,
    limitations: payload.limitations,
    trustLabels: labels,
    historyLabels: history,
    landmarkRole: "complementary",
    accessibilityLabel: "Evidence Drawer: supported evidence",
    ariaLive: "polite",
  });
}

function allocateEvidenceDrawerDomIds(document: Document): EvidenceDrawerDomIds {
  let ordinal = 1;

  while (true) {
    const prefix = ordinal === 1 ? "evidence-drawer" : `evidence-drawer-${ordinal}`;
    const ids = Object.freeze({
      panelId: `${prefix}-panel`,
      labelId: `${prefix}-label`,
      titleId: `${prefix}-title`,
    });

    if (
      document.getElementById(ids.panelId) === null &&
      document.getElementById(ids.labelId) === null &&
      document.getElementById(ids.titleId) === null
    ) {
      return ids;
    }

    ordinal += 1;
  }
}

/**
 * Mount one keyboard-operable browser projection of the resolved drawer state.
 *
 * The renderer consumes only the finite app-local view model above. It does
 * not parse policy, access sources, perform transport, or inspect lifecycle
 * storage. Denied and error projections therefore cannot bypass the resolver's
 * fixed no-leak copy.
 */
export function mountEvidenceDrawer(
  host: HTMLElement,
  input?: unknown,
): EvidenceDrawerController {
  const state = resolveEvidenceDrawer(input);
  const document = host.ownerDocument;
  const ids = allocateEvidenceDrawerDomIds(document);
  const trigger = document.createElement("button");
  const drawer = document.createElement("aside");
  const accessibleLabel = document.createElement("span");
  const heading = document.createElement("h2");
  const outcome = document.createElement("p");
  const message = document.createElement("p");
  const closeButton = document.createElement("button");
  const trustList = document.createElement("ul");
  const evidenceList = document.createElement("ul");
  const citationList = document.createElement("ul");
  const historyList = document.createElement("ul");
  const limitationList = document.createElement("ul");
  let returnFocus: HTMLElement | null = null;

  trigger.type = "button";
  trigger.textContent = "Open Evidence Drawer";
  trigger.setAttribute("aria-controls", ids.panelId);
  trigger.setAttribute("aria-expanded", "false");

  accessibleLabel.id = ids.labelId;
  accessibleLabel.textContent = state.accessibilityLabel;

  heading.id = ids.titleId;
  heading.textContent = state.title;

  outcome.textContent = `${state.outcome} / ${state.code}`;
  outcome.dataset.evidenceOutcome = state.outcome;
  message.textContent = state.message;

  closeButton.type = "button";
  closeButton.textContent = "Close Evidence Drawer";

  trustList.setAttribute("aria-label", "Evidence trust state");
  for (const label of state.trustLabels) {
    const item = document.createElement("li");
    item.textContent = label;
    trustList.append(item);
  }

  evidenceList.setAttribute("aria-label", state.evidenceRefsLabel);
  for (const evidenceRef of state.evidenceRefs) {
    const item = document.createElement("li");
    item.textContent = evidenceRef;
    evidenceList.append(item);
  }

  citationList.setAttribute("aria-label", "Evidence citations");
  for (const citation of state.citations) {
    const item = document.createElement("li");
    const link = document.createElement("a");
    link.href = citation.href;
    link.textContent = citation.label;
    item.append(link);
    citationList.append(item);
  }

  historyList.setAttribute("aria-label", "Evidence history");
  for (const label of state.historyLabels) {
    const item = document.createElement("li");
    item.textContent = label;
    historyList.append(item);
  }

  limitationList.setAttribute("aria-label", "Evidence limitations");
  for (const limitation of state.limitations) {
    const item = document.createElement("li");
    item.textContent = limitation;
    limitationList.append(item);
  }

  const drawerChildren: Node[] = [accessibleLabel, heading, outcome];
  if (state.representationDisclosure !== null) {
    const disclosure = document.createElement("section");
    const disclosureHeading = document.createElement("strong");
    const disclosureMessage = document.createElement("p");
    disclosure.className = "guardrail evidence-drawer__representation-disclosure";
    disclosure.dataset.component = "derived-representation-disclosure";
    disclosure.dataset.representationKind = state.representationDisclosure.kind;
    disclosure.setAttribute("role", "note");
    disclosure.setAttribute("aria-label", "Representation disclosure");
    disclosureHeading.textContent = state.representationDisclosure.label;
    disclosureMessage.textContent = state.representationDisclosure.message;
    disclosure.replaceChildren(disclosureHeading, disclosureMessage);
    drawerChildren.push(disclosure);
  }
  drawerChildren.push(
    message,
    trustList,
    evidenceList,
    citationList,
    historyList,
    limitationList,
    closeButton,
  );

  drawer.id = ids.panelId;
  drawer.hidden = true;
  drawer.dataset.component = "evidence-drawer";
  drawer.dataset.outcome = state.outcome;
  if (state.representationDisclosure !== null) {
    drawer.dataset.representationKind = state.representationDisclosure.kind;
  }
  drawer.setAttribute("role", state.landmarkRole);
  drawer.setAttribute(
    "aria-labelledby",
    `${accessibleLabel.id} ${heading.id}`,
  );
  drawer.setAttribute("aria-live", state.ariaLive);
  drawer.replaceChildren(...drawerChildren);

  function open(): void {
    if (!drawer.hidden) return;
    returnFocus =
      document.activeElement instanceof HTMLElement
        ? document.activeElement
        : trigger;
    drawer.hidden = false;
    trigger.setAttribute("aria-expanded", "true");
    closeButton.focus();
  }

  function close(): void {
    if (drawer.hidden) return;
    drawer.hidden = true;
    trigger.setAttribute("aria-expanded", "false");
    const focusTarget = returnFocus?.isConnected ? returnFocus : trigger;
    focusTarget.focus();
    returnFocus = null;
  }

  function handleDrawerKeydown(event: KeyboardEvent): void {
    if (event.key !== "Escape" || drawer.hidden) return;
    event.preventDefault();
    close();
  }

  function destroy(): void {
    trigger.removeEventListener("click", open);
    closeButton.removeEventListener("click", close);
    drawer.removeEventListener("keydown", handleDrawerKeydown);
    host.replaceChildren();
  }

  trigger.addEventListener("click", open);
  closeButton.addEventListener("click", close);
  drawer.addEventListener("keydown", handleDrawerKeydown);
  host.replaceChildren(trigger, drawer);

  return Object.freeze({ state, open, close, destroy });
}
