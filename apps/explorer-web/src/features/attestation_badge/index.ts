import {
  type AttestationBadgeOutcome,
  type AttestationBadgeReasonCode,
  type GovernedAttestationBadgeProjection,
  parseAttestationBadgeProjection,
} from "../../adapters/AttestationBadgeProjection";

export type AttestationBadgeVisibility = "VISIBLE" | "HIDDEN";
export type AttestationBadgeStatus =
  | "VERIFIED"
  | "INCOMPLETE"
  | "FAILED"
  | "ERROR";

export type AttestationBadgeViewModel = Readonly<{
  visibility: AttestationBadgeVisibility;
  outcome: AttestationBadgeOutcome;
  code:
    | AttestationBadgeReasonCode
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD";
  status: AttestationBadgeStatus;
  label: string;
  message: string;
  canInspect: boolean;
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

export type AttestationBadgeMountOptions = Readonly<{
  onInspect?: (payload: GovernedAttestationBadgeProjection) => void;
}>;

export type AttestationBadgeController = Readonly<{
  state: AttestationBadgeViewModel;
  destroy: () => void;
}>;

type ResolvedAttestationBadge = Readonly<{
  state: AttestationBadgeViewModel;
  payload: GovernedAttestationBadgeProjection | null;
}>;

const NEGATIVE_COPY: Readonly<
  Record<
    Exclude<AttestationBadgeReasonCode, "CHECKS_VERIFIED">,
    Readonly<{
      outcome: Exclude<AttestationBadgeOutcome, "ANSWER">;
      status: Exclude<AttestationBadgeStatus, "VERIFIED">;
      label: string;
      message: string;
      ariaLive: "polite" | "assertive";
    }>
  >
> = Object.freeze({
  CHECKS_INCOMPLETE: Object.freeze({
    outcome: "ABSTAIN",
    status: "INCOMPLETE",
    label: "Verification incomplete",
    message: "Required verification evidence is incomplete. This badge grants no trust or release authority.",
    ariaLive: "polite",
  }),
  CHECKS_FAILED: Object.freeze({
    outcome: "DENY",
    status: "FAILED",
    label: "Verification failed",
    message: "Required verification checks failed. The layer must remain unavailable.",
    ariaLive: "assertive",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    status: "ERROR",
    label: "Verification unavailable",
    message: "The governed verification projection could not be completed.",
    ariaLive: "assertive",
  }),
});

function hidden(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): AttestationBadgeViewModel {
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: "ERROR",
    code,
    status: "ERROR",
    label: "Verification unavailable",
    message: "No attestation badge is rendered without a valid governed projection.",
    canInspect: false,
    accessibilityLabel: "Attestation status unavailable",
    ariaLive: "polite",
  });
}

function resolveProjection(input: unknown | undefined): ResolvedAttestationBadge {
  if (input === undefined) {
    return Object.freeze({
      state: hidden("NO_GOVERNED_RESPONSE"),
      payload: null,
    });
  }
  const parsed = parseAttestationBadgeProjection(input);
  if (!parsed.ok) {
    return Object.freeze({ state: hidden("INVALID_PAYLOAD"), payload: null });
  }

  const { payload } = parsed;
  if (payload.outcome !== "ANSWER") {
    const copy = NEGATIVE_COPY[
      payload.reasonCode as Exclude<AttestationBadgeReasonCode, "CHECKS_VERIFIED">
    ];
    return Object.freeze({
      payload: null,
      state: Object.freeze({
        visibility: "VISIBLE",
        outcome: copy.outcome,
        code: payload.reasonCode,
        status: copy.status,
        label: copy.label,
        message: copy.message,
        canInspect: false,
        accessibilityLabel: `Attestation status: ${copy.status.toLowerCase()}`,
        ariaLive: copy.ariaLive,
      }),
    });
  }

  return Object.freeze({
    payload,
    state: Object.freeze({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "CHECKS_VERIFIED",
      status: "VERIFIED",
      label: "Verification evidence available",
      message: "Attestation, run-receipt, EvidenceBundle, and release references are available for inspection. The badge is not proof or release authority.",
      canInspect: true,
      accessibilityLabel: "Attestation status: checks reported verified",
      ariaLive: "polite",
    }),
  });
}

/** Resolve a governed projection into a compact, non-authoritative badge state. */
export function resolveAttestationBadge(input?: unknown): AttestationBadgeViewModel {
  return resolveProjection(input).state;
}

/** Mount a text-first badge whose positive action opens supporting references. */
export function mountAttestationBadge(
  host: HTMLElement,
  input?: unknown,
  options: AttestationBadgeMountOptions = {},
): AttestationBadgeController {
  const resolved = resolveProjection(input);
  const { state, payload } = resolved;
  host.replaceChildren();

  if (state.visibility === "HIDDEN") {
    return Object.freeze({
      state,
      destroy: () => host.replaceChildren(),
    });
  }

  const document = host.ownerDocument;
  const region = document.createElement("section");
  const label = document.createElement("strong");
  const status = document.createElement("span");
  const message = document.createElement("p");
  let inspectButton: HTMLButtonElement | null = null;

  region.dataset.component = "attestation-badge";
  region.dataset.status = state.status;
  region.setAttribute("role", state.outcome === "ERROR" ? "alert" : "status");
  region.setAttribute("aria-label", state.accessibilityLabel);
  region.setAttribute("aria-live", state.ariaLive);
  label.textContent = state.label;
  status.dataset.attestationStatus = state.status;
  status.textContent = state.status;
  message.textContent = state.message;
  region.append(label, status, message);

  if (state.canInspect && payload !== null && options.onInspect !== undefined) {
    const inspectablePayload = payload;
    inspectButton = document.createElement("button");
    inspectButton.type = "button";
    inspectButton.textContent = "Inspect supporting references";
    inspectButton.addEventListener("click", () => {
      options.onInspect?.(inspectablePayload);
    });
    region.append(inspectButton);
  }

  host.replaceChildren(region);

  function destroy(): void {
    inspectButton?.replaceWith();
    host.replaceChildren();
  }

  return Object.freeze({ state, destroy });
}
