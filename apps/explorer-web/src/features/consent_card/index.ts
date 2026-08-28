import {
  type ConsentCardOutcome,
  type ConsentCardProjectionReasonCode,
  type GovernedConsentCardProjection,
  type SubjectConsentState,
  parseConsentCardProjection,
} from "../../adapters/ConsentCardProjection";

export type ConsentCardViewerDecision = "OPTED_IN" | "WITHDRAWN";

export type ConsentCardReasonCode =
  | ConsentCardProjectionReasonCode
  | "NO_GOVERNED_RESPONSE"
  | "INVALID_PAYLOAD"
  | "CONSENT_EXPIRED";

export type ConsentCardViewModel = Readonly<{
  outcome: ConsentCardOutcome;
  code: ConsentCardReasonCode;
  title: string;
  message: string;
  layerRef: string | null;
  basis: string | null;
  scope: readonly string[];
  expirationLabel: string;
  subjectConsentLabel: string;
  viewerDecision: ConsentCardViewerDecision | null;
  canOptIn: boolean;
  canWithdraw: boolean;
  canViewObligations: boolean;
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

export type ConsentCardPreferenceStore = Readonly<{
  read: (key: string) => ConsentCardViewerDecision | null;
  write: (key: string, value: ConsentCardViewerDecision) => void;
}>;

export type ConsentCardDecisionEvent = Readonly<{
  kind: "VIEWER_LAYER_OPT_IN" | "VIEWER_LAYER_WITHDRAWAL";
  cardId: string;
  layerRef: string;
  obligationSetRef: string;
  policyDecisionRef: string;
  viewerDecision: ConsentCardViewerDecision;
  affectsSubjectConsent: false;
  upstreamNoticeRequired: boolean;
}>;

export type ConsentCardObligationsEvent = Readonly<{
  cardId: string;
  layerRef: string;
  obligationSetRef: string;
  policyDecisionRef: string;
}>;

export type ConsentCardResolveOptions = Readonly<{
  now?: string;
  viewerDecision?: ConsentCardViewerDecision | null;
}>;

export type ConsentCardMountOptions = Readonly<{
  now?: string;
  preferenceStore?: ConsentCardPreferenceStore;
  onLayerVisibilityChange?: (visible: boolean) => void;
  onViewerDecision?: (event: ConsentCardDecisionEvent) => void;
  onViewObligations?: (event: ConsentCardObligationsEvent) => void;
}>;

export type ConsentCardController = Readonly<{
  state: ConsentCardViewModel;
  optIn: () => boolean;
  withdraw: () => boolean;
  viewObligations: () => boolean;
  destroy: () => void;
}>;

type ResolvedConsentCard = Readonly<{
  state: ConsentCardViewModel;
  payload: GovernedConsentCardProjection | null;
}>;

const UTC_SECOND_PATTERN = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const EMPTY_SCOPE = Object.freeze([]) as readonly string[];
let consentCardSequence = 0;

const SUBJECT_CONSENT_LABELS: Readonly<Record<SubjectConsentState, string>> =
  Object.freeze({
    RECORDED: "Subject inclusion consent: recorded upstream.",
    NOT_APPLICABLE: "Subject inclusion consent: not applicable to this projection.",
    WITHHELD: "Subject inclusion consent: status recorded upstream; details withheld.",
    UNRESOLVED: "Subject inclusion consent: unresolved.",
  });

const FIXED_NEGATIVE_COPY: Readonly<
  Record<
    Exclude<ConsentCardReasonCode, "CONSENT_CARD_READY">,
    Readonly<{ title: string; message: string; outcome: "ABSTAIN" | "DENY" | "ERROR" }>
  >
> = Object.freeze({
  NO_GOVERNED_RESPONSE: Object.freeze({
    outcome: "ABSTAIN",
    title: "Consent details unavailable",
    message: "No governed consent-card response is available. The layer remains hidden.",
  }),
  INVALID_PAYLOAD: Object.freeze({
    outcome: "ERROR",
    title: "Consent details unavailable",
    message: "The governed consent-card response is invalid. The layer remains hidden.",
  }),
  CONSENT_UNRESOLVED: Object.freeze({
    outcome: "ABSTAIN",
    title: "Consent details unresolved",
    message: "Consent details are unresolved. The layer remains hidden.",
  }),
  POLICY_DENIED: Object.freeze({
    outcome: "DENY",
    title: "Layer access restricted",
    message: "Policy does not permit this layer to be shown.",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    title: "Consent details unavailable",
    message: "The governed consent service could not complete the request. The layer remains hidden.",
  }),
  CONSENT_EXPIRED: Object.freeze({
    outcome: "ABSTAIN",
    title: "Consent details expired",
    message: "The projected consent period has expired. The layer remains hidden.",
  }),
});

function isCanonicalUtcSecond(value: unknown): value is string {
  if (typeof value !== "string" || !UTC_SECOND_PATTERN.test(value)) return false;
  const parsed = Date.parse(value);
  return (
    Number.isFinite(parsed) &&
    new Date(parsed).toISOString().replace(".000Z", "Z") === value
  );
}

function currentUtcSecond(): string {
  return new Date(Math.floor(Date.now() / 1000) * 1000)
    .toISOString()
    .replace(".000Z", "Z");
}

function fixedNegativeView(
  code: Exclude<ConsentCardReasonCode, "CONSENT_CARD_READY">,
): ConsentCardViewModel {
  const copy = FIXED_NEGATIVE_COPY[code];
  return Object.freeze({
    outcome: copy.outcome,
    code,
    title: copy.title,
    message: copy.message,
    layerRef: null,
    basis: null,
    scope: EMPTY_SCOPE,
    expirationLabel: "Expiration: not available.",
    subjectConsentLabel: "Subject inclusion consent: not displayed.",
    viewerDecision: null,
    canOptIn: false,
    canWithdraw: false,
    canViewObligations: false,
    accessibilityLabel: `Consent card: ${copy.outcome.toLowerCase()}`,
    ariaLive: copy.outcome === "ERROR" ? "assertive" : "polite",
  });
}

function expirationLabel(expiresAt: string | null): string {
  return expiresAt === null
    ? "Expiration: no expiry supplied by the governed projection."
    : `Expiration: ${expiresAt}`;
}

function resolveProjection(
  input: unknown | undefined,
  options: ConsentCardResolveOptions,
): ResolvedConsentCard {
  if (input === undefined) {
    return Object.freeze({
      state: fixedNegativeView("NO_GOVERNED_RESPONSE"),
      payload: null,
    });
  }

  const parsed = parseConsentCardProjection(input);
  if (!parsed.ok) {
    return Object.freeze({
      state: fixedNegativeView("INVALID_PAYLOAD"),
      payload: null,
    });
  }

  const { payload } = parsed;
  if (payload.outcome !== "ANSWER") {
    return Object.freeze({
      state: fixedNegativeView(
        payload.reasonCode as Exclude<ConsentCardReasonCode, "CONSENT_CARD_READY">,
      ),
      payload: null,
    });
  }

  const now = options.now ?? currentUtcSecond();
  if (!isCanonicalUtcSecond(now)) {
    return Object.freeze({
      state: fixedNegativeView("INVALID_PAYLOAD"),
      payload: null,
    });
  }
  if (
    payload.expiresAt !== null &&
    Date.parse(payload.expiresAt) <= Date.parse(now)
  ) {
    return Object.freeze({
      state: fixedNegativeView("CONSENT_EXPIRED"),
      payload: null,
    });
  }

  const viewerDecision =
    options.viewerDecision === "OPTED_IN" ||
    options.viewerDecision === "WITHDRAWN"
      ? options.viewerDecision
      : null;
  const state: ConsentCardViewModel = Object.freeze({
    outcome: "ANSWER",
    code: "CONSENT_CARD_READY",
    title: payload.layerLabel as string,
    message:
      "Your choice controls whether this layer is shown in this browser session. It does not grant or revoke a subject's consent to inclusion.",
    layerRef: payload.layerRef,
    basis: payload.basis,
    scope: payload.scope,
    expirationLabel: expirationLabel(payload.expiresAt),
    subjectConsentLabel:
      SUBJECT_CONSENT_LABELS[payload.subjectConsentState],
    viewerDecision,
    canOptIn: viewerDecision !== "OPTED_IN",
    canWithdraw: viewerDecision === "OPTED_IN",
    canViewObligations: true,
    accessibilityLabel: `Consent card for ${payload.layerLabel}`,
    ariaLive: "polite",
  });

  return Object.freeze({ state, payload });
}

/** Resolve a strict governed projection into a finite, no-leak card state. */
export function resolveConsentCard(
  input?: unknown,
  options: ConsentCardResolveOptions = {},
): ConsentCardViewModel {
  return resolveProjection(input, options).state;
}

function preferenceKey(payload: GovernedConsentCardProjection): string {
  return `${payload.profile}:${payload.id}:${payload.layerRef ?? "unresolved"}`;
}

function createSessionPreferenceStore(
  window: Window | null,
): ConsentCardPreferenceStore {
  const memory = new Map<string, ConsentCardViewerDecision>();

  return Object.freeze({
    read(key: string): ConsentCardViewerDecision | null {
      try {
        const stored = window?.sessionStorage.getItem(key);
        if (stored === "OPTED_IN" || stored === "WITHDRAWN") return stored;
      } catch {
        // A denied storage surface falls back to the controller-local memory map.
      }
      return memory.get(key) ?? null;
    },
    write(key: string, value: ConsentCardViewerDecision): void {
      memory.set(key, value);
      try {
        window?.sessionStorage.setItem(key, value);
      } catch {
        // Local memory still preserves the choice for this mounted controller.
      }
    },
  });
}

function decisionEvent(
  payload: GovernedConsentCardProjection,
  viewerDecision: ConsentCardViewerDecision,
): ConsentCardDecisionEvent {
  return Object.freeze({
    kind:
      viewerDecision === "OPTED_IN"
        ? "VIEWER_LAYER_OPT_IN"
        : "VIEWER_LAYER_WITHDRAWAL",
    cardId: payload.id,
    layerRef: payload.layerRef as string,
    obligationSetRef: payload.obligationSetRef as string,
    policyDecisionRef: payload.policyDecisionRef as string,
    viewerDecision,
    affectsSubjectConsent: false,
    upstreamNoticeRequired: viewerDecision === "WITHDRAWN",
  });
}

function obligationsEvent(
  payload: GovernedConsentCardProjection,
): ConsentCardObligationsEvent {
  return Object.freeze({
    cardId: payload.id,
    layerRef: payload.layerRef as string,
    obligationSetRef: payload.obligationSetRef as string,
    policyDecisionRef: payload.policyDecisionRef as string,
  });
}

/**
 * Mount a lightweight, non-modal consent card for one governed layer projection.
 *
 * The component records only the viewer's local display preference. It does not
 * issue, revoke, or evaluate a subject's consent; it performs no transport; and
 * it never exposes a view-anyway override for ABSTAIN, DENY, or ERROR states.
 */
export function mountConsentCard(
  host: HTMLElement,
  input?: unknown,
  options: ConsentCardMountOptions = {},
): ConsentCardController {
  const initial = resolveProjection(input, { now: options.now });
  const document = host.ownerDocument;
  const preferenceStore =
    options.preferenceStore ??
    createSessionPreferenceStore(document.defaultView);
  const payload = initial.payload;
  const key = payload === null ? null : preferenceKey(payload);
  let viewerDecision =
    payload === null || key === null ? null : preferenceStore.read(key);
  let state =
    payload === null
      ? initial.state
      : resolveConsentCard(input, {
          now: options.now,
          viewerDecision,
        });

  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const outcome = document.createElement("p");
  const message = document.createElement("p");
  const distinction = document.createElement("p");
  const details = document.createElement("dl");
  const basisTerm = document.createElement("dt");
  const basisValue = document.createElement("dd");
  const scopeTerm = document.createElement("dt");
  const scopeValue = document.createElement("dd");
  const scopeList = document.createElement("ul");
  const expirationTerm = document.createElement("dt");
  const expirationValue = document.createElement("dd");
  const subjectTerm = document.createElement("dt");
  const subjectValue = document.createElement("dd");
  const actions = document.createElement("div");
  const optInButton = document.createElement("button");
  const withdrawButton = document.createElement("button");
  const obligationsButton = document.createElement("button");
  const liveStatus = document.createElement("p");
  const componentId = `kfm-consent-card-${++consentCardSequence}`;
  let destroyed = false;

  section.dataset.component = "consent-card";
  section.id = componentId;
  section.setAttribute("aria-labelledby", `${componentId}-title`);
  section.setAttribute("aria-describedby", `${componentId}-message`);
  section.setAttribute("aria-live", state.ariaLive);

  heading.id = `${componentId}-title`;
  message.id = `${componentId}-message`;
  distinction.textContent =
    "Viewer display choice and subject inclusion consent are separate. This card changes only the viewer's local layer preference.";

  basisTerm.textContent = "Basis";
  scopeTerm.textContent = "Scope";
  expirationTerm.textContent = "Expiration";
  subjectTerm.textContent = "Subject inclusion consent";

  scopeValue.append(scopeList);
  details.append(
    basisTerm,
    basisValue,
    scopeTerm,
    scopeValue,
    expirationTerm,
    expirationValue,
    subjectTerm,
    subjectValue,
  );

  optInButton.type = "button";
  optInButton.textContent = "Show this layer";
  optInButton.dataset.action = "opt-in";

  withdrawButton.type = "button";
  withdrawButton.textContent = "Hide this layer";
  withdrawButton.dataset.action = "withdraw";

  obligationsButton.type = "button";
  obligationsButton.textContent = "View obligations";
  obligationsButton.dataset.action = "view-obligations";

  liveStatus.setAttribute("role", "status");
  liveStatus.setAttribute("aria-live", "polite");
  liveStatus.dataset.component = "consent-card-status";

  actions.dataset.component = "consent-card-actions";
  actions.append(optInButton, withdrawButton, obligationsButton);
  section.append(
    heading,
    outcome,
    message,
    distinction,
    details,
    actions,
    liveStatus,
  );
  host.replaceChildren(section);

  function render(): void {
    heading.textContent = state.title;
    outcome.textContent = `${state.outcome} / ${state.code}`;
    outcome.dataset.outcome = state.outcome;
    message.textContent = state.message;

    section.setAttribute("aria-label", state.accessibilityLabel);
    section.setAttribute("aria-live", state.ariaLive);
    section.dataset.outcome = state.outcome;
    section.dataset.viewerDecision = state.viewerDecision ?? "UNDECIDED";

    basisValue.textContent = state.basis ?? "Not available.";
    scopeList.replaceChildren();
    for (const scope of state.scope) {
      const item = document.createElement("li");
      item.textContent = scope;
      scopeList.append(item);
    }
    if (state.scope.length === 0) {
      const item = document.createElement("li");
      item.textContent = "Not available.";
      scopeList.append(item);
    }
    expirationValue.textContent = state.expirationLabel.replace(/^Expiration:\s*/, "");
    subjectValue.textContent = state.subjectConsentLabel.replace(
      /^Subject inclusion consent:\s*/,
      "",
    );

    optInButton.hidden = !state.canOptIn;
    optInButton.disabled = !state.canOptIn;
    withdrawButton.hidden = !state.canWithdraw;
    withdrawButton.disabled = !state.canWithdraw;
    obligationsButton.hidden = !state.canViewObligations;
    obligationsButton.disabled = !state.canViewObligations;

    details.hidden = state.outcome !== "ANSWER";
    distinction.hidden = state.outcome !== "ANSWER";
    actions.hidden =
      !state.canOptIn && !state.canWithdraw && !state.canViewObligations;
  }

  function setViewerDecision(next: ConsentCardViewerDecision): void {
    if (payload === null || key === null) return;
    viewerDecision = next;
    preferenceStore.write(key, next);
    state = resolveConsentCard(input, {
      now: options.now,
      viewerDecision,
    });
    render();
  }

  function emitDecision(next: ConsentCardViewerDecision): void {
    if (payload === null) return;
    options.onViewerDecision?.(decisionEvent(payload, next));
  }

  function optIn(): boolean {
    if (destroyed || payload === null || !state.canOptIn) return false;
    try {
      emitDecision("OPTED_IN");
      setViewerDecision("OPTED_IN");
      options.onLayerVisibilityChange?.(true);
      liveStatus.textContent = "Layer display preference saved for this browser session.";
      return true;
    } catch {
      options.onLayerVisibilityChange?.(false);
      liveStatus.textContent = "The layer remains hidden because the viewer choice could not be recorded.";
      return false;
    }
  }

  function withdraw(): boolean {
    if (destroyed || payload === null || !state.canWithdraw) return false;

    setViewerDecision("WITHDRAWN");
    options.onLayerVisibilityChange?.(false);
    try {
      emitDecision("WITHDRAWN");
      liveStatus.textContent = "Layer hidden for this browser session. Viewer withdrawal notice emitted to the caller.";
    } catch {
      liveStatus.textContent = "Layer hidden for this browser session; upstream viewer-withdrawal notice was not confirmed.";
    }
    return true;
  }

  function viewObligations(): boolean {
    if (
      destroyed ||
      payload === null ||
      !state.canViewObligations ||
      options.onViewObligations === undefined
    ) {
      if (!destroyed && state.canViewObligations) {
        liveStatus.textContent = "Obligation details are not connected to a governed caller.";
      }
      return false;
    }
    try {
      options.onViewObligations(obligationsEvent(payload));
      liveStatus.textContent = "Obligation detail request emitted to the caller.";
      return true;
    } catch {
      liveStatus.textContent = "Obligation details are unavailable.";
      return false;
    }
  }

  function handleOptIn(): void {
    optIn();
  }

  function handleWithdraw(): void {
    withdraw();
  }

  function handleViewObligations(): void {
    viewObligations();
  }

  function destroy(): void {
    if (destroyed) return;
    destroyed = true;
    optInButton.removeEventListener("click", handleOptIn);
    withdrawButton.removeEventListener("click", handleWithdraw);
    obligationsButton.removeEventListener("click", handleViewObligations);
    host.replaceChildren();
  }

  optInButton.addEventListener("click", handleOptIn);
  withdrawButton.addEventListener("click", handleWithdraw);
  obligationsButton.addEventListener("click", handleViewObligations);

  render();
  options.onLayerVisibilityChange?.(
    state.outcome === "ANSWER" && state.viewerDecision === "OPTED_IN",
  );

  return Object.freeze({
    get state(): ConsentCardViewModel {
      return state;
    },
    optIn,
    withdraw,
    viewObligations,
    destroy,
  });
}
