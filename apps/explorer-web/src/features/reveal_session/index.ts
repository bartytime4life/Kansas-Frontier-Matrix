import {
  type GovernedRevealSessionProjection,
  type RevealScopeCode,
  type RevealSessionOutcome,
  type RevealSessionProjectionReasonCode,
  parseRevealSessionProjection,
} from "../../adapters/RevealSessionProjection";

export type RevealSessionReasonCode =
  | RevealSessionProjectionReasonCode
  | "NO_GOVERNED_RESPONSE"
  | "INVALID_PAYLOAD"
  | "REVEAL_EXPIRED"
  | "REVEAL_REVOKED"
  | "REVEAL_TERMINATED";

export type RevealSessionStatus =
  | "ACTIVE"
  | "EXPIRED"
  | "REVOKED"
  | "TERMINATED"
  | "UNAVAILABLE"
  | "DENIED"
  | "ERROR";

export type RevealTeardownStatus =
  | "NOT_REQUIRED"
  | "COMPLETE"
  | "INCOMPLETE";

export type RevealSessionViewModel = Readonly<{
  outcome: RevealSessionOutcome;
  code: RevealSessionReasonCode;
  status: RevealSessionStatus;
  title: string;
  message: string;
  remainingSeconds: number;
  timerLabel: string;
  scopeLabels: readonly string[];
  canRevoke: boolean;
  teardownStatus: RevealTeardownStatus;
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

export type RevealTerminationCause =
  | "TTL_EXPIRED"
  | "VIEWER_REVOKED"
  | "COMPONENT_DESTROYED";

export type RevealTeardownAction =
  | "DISCARD_KEY_MATERIAL"
  | "REMOVE_OVERLAY"
  | "RESTORE_OBFUSCATED_STATE"
  | "FINALIZE_AUDIT";

export type RevealTerminationEvent = Readonly<{
  kind: "REVEAL_SESSION_TERMINATED";
  cause: RevealTerminationCause;
  sessionId: string;
  layerRef: string;
  auditRef: string;
  policyDecisionRef: string;
  occurredAt: string;
  localKeyReferenceDiscarded: true;
  requiredActions: readonly RevealTeardownAction[];
  completedActionsBeforeAudit: readonly RevealTeardownAction[];
  unresolvedActionsBeforeAudit: readonly RevealTeardownAction[];
  authority: "NONE";
}>;

export type RevealSessionClock = Readonly<{
  now: () => number;
  setTimer: (callback: () => void, delayMs: number) => unknown;
  clearTimer: (handle: unknown) => void;
}>;

export type RevealSessionControllerOptions = Readonly<{
  clock?: RevealSessionClock;
  onStateChange?: (state: RevealSessionViewModel) => void;
  onDiscardKeyMaterial?: (keyHandleRef: string) => void;
  onOverlayVisibilityChange?: (visible: false) => void;
  onRestoreObfuscatedState?: (layerRef: string) => void;
  onFinalizeAudit?: (event: RevealTerminationEvent) => void;
}>;

export type RevealSessionMountOptions = Omit<
  RevealSessionControllerOptions,
  "onStateChange"
>;

export type RevealSessionController = Readonly<{
  readonly state: RevealSessionViewModel;
  revoke: () => boolean;
  destroy: () => void;
}>;

export type RevealSessionResolveOptions = Readonly<{
  now?: string;
}>;

const EMPTY_STRINGS = Object.freeze([]) as readonly string[];
const REQUIRED_ACTIONS = Object.freeze([
  "DISCARD_KEY_MATERIAL",
  "REMOVE_OVERLAY",
  "RESTORE_OBFUSCATED_STATE",
  "FINALIZE_AUDIT",
]) as readonly RevealTeardownAction[];
const UTC_SECOND_PATTERN = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;

const SCOPE_LABELS: Readonly<Record<RevealScopeCode, string>> = Object.freeze({
  GENERALIZED_VIEW: "Generalized display only",
  NO_EXPORT: "Export is disabled",
  NO_REDISTRIBUTION: "Redistribution is prohibited",
  STEWARD_SESSION: "Restricted steward session",
});

const FIXED_NEGATIVE_COPY: Readonly<
  Record<
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD"
    | "REVEAL_UNAVAILABLE"
    | "POLICY_DENIED"
    | "UPSTREAM_ERROR",
    Readonly<{
      outcome: "ABSTAIN" | "DENY" | "ERROR";
      status: "UNAVAILABLE" | "DENIED" | "ERROR";
      title: string;
      message: string;
    }>
  >
> = Object.freeze({
  NO_GOVERNED_RESPONSE: Object.freeze({
    outcome: "ABSTAIN",
    status: "UNAVAILABLE",
    title: "Sensitive reveal unavailable",
    message: "No governed reveal-session response is available. The overlay remains hidden.",
  }),
  INVALID_PAYLOAD: Object.freeze({
    outcome: "ERROR",
    status: "ERROR",
    title: "Sensitive reveal unavailable",
    message: "The governed reveal-session response is invalid. The overlay remains hidden.",
  }),
  REVEAL_UNAVAILABLE: Object.freeze({
    outcome: "ABSTAIN",
    status: "UNAVAILABLE",
    title: "Sensitive reveal unavailable",
    message: "A governed reveal session is not available. The overlay remains hidden.",
  }),
  POLICY_DENIED: Object.freeze({
    outcome: "DENY",
    status: "DENIED",
    title: "Sensitive reveal restricted",
    message: "Policy does not permit this reveal session.",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    status: "ERROR",
    title: "Sensitive reveal unavailable",
    message: "The governed reveal service could not complete the request. The overlay remains hidden.",
  }),
});

const DEFAULT_CLOCK: RevealSessionClock = Object.freeze({
  now: () => Date.now(),
  setTimer: (callback, delayMs) => globalThis.setTimeout(callback, delayMs),
  clearTimer: (handle) => globalThis.clearTimeout(handle as number),
});

function isCanonicalUtcSecond(value: unknown): value is string {
  if (typeof value !== "string" || !UTC_SECOND_PATTERN.test(value)) return false;
  const parsed = Date.parse(value);
  return (
    Number.isFinite(parsed) &&
    new Date(parsed).toISOString().replace(".000Z", "Z") === value
  );
}

function utcSecondFromEpoch(value: number): string | null {
  if (!Number.isFinite(value)) return null;
  try {
    return new Date(Math.floor(value / 1000) * 1000)
      .toISOString()
      .replace(".000Z", "Z");
  } catch {
    return null;
  }
}

function fixedNegativeView(
  code:
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD"
    | "REVEAL_UNAVAILABLE"
    | "POLICY_DENIED"
    | "UPSTREAM_ERROR",
): RevealSessionViewModel {
  const copy = FIXED_NEGATIVE_COPY[code];
  return Object.freeze({
    outcome: copy.outcome,
    code,
    status: copy.status,
    title: copy.title,
    message: copy.message,
    remainingSeconds: 0,
    timerLabel: "Time remaining: unavailable",
    scopeLabels: EMPTY_STRINGS,
    canRevoke: false,
    teardownStatus: "NOT_REQUIRED",
    accessibilityLabel: `Reveal session: ${copy.status.toLowerCase()}`,
    ariaLive: copy.outcome === "ERROR" ? "assertive" : "polite",
  });
}

function formatRemaining(seconds: number): string {
  const bounded = Math.max(0, Math.min(24 * 60 * 60, Math.ceil(seconds)));
  const hours = Math.floor(bounded / 3600);
  const minutes = Math.floor((bounded % 3600) / 60);
  const remainder = bounded % 60;
  const clock =
    hours > 0
      ? `${String(hours).padStart(2, "0")}:${String(minutes).padStart(2, "0")}:${String(remainder).padStart(2, "0")}`
      : `${String(minutes).padStart(2, "0")}:${String(remainder).padStart(2, "0")}`;
  return `Time remaining: ${clock}`;
}

function activeView(
  payload: GovernedRevealSessionProjection,
  now: string,
): RevealSessionViewModel {
  const expiresAt = payload.expiresAt as string;
  const remainingSeconds = Math.max(
    0,
    Math.ceil((Date.parse(expiresAt) - Date.parse(now)) / 1000),
  );
  return Object.freeze({
    outcome: "ANSWER",
    code: "REVEAL_ACTIVE",
    status: "ACTIVE",
    title: "Sensitive reveal active",
    message: "This timeboxed reveal ends automatically. Revoke it immediately when it is no longer needed.",
    remainingSeconds,
    timerLabel: formatRemaining(remainingSeconds),
    scopeLabels: Object.freeze(
      payload.scopeCodes.map((code) => SCOPE_LABELS[code]),
    ),
    canRevoke: true,
    teardownStatus: "NOT_REQUIRED",
    accessibilityLabel: "Reveal session: active",
    ariaLive: "polite",
  });
}

function terminatedView(
  cause: RevealTerminationCause,
  teardownStatus: Exclude<RevealTeardownStatus, "NOT_REQUIRED">,
): RevealSessionViewModel {
  const copy =
    cause === "TTL_EXPIRED"
      ? {
          code: "REVEAL_EXPIRED" as const,
          status: "EXPIRED" as const,
          title: "Sensitive reveal expired",
          message: "The reveal timer ended. Sensitive overlay content is hidden.",
        }
      : cause === "VIEWER_REVOKED"
        ? {
            code: "REVEAL_REVOKED" as const,
            status: "REVOKED" as const,
            title: "Sensitive reveal revoked",
            message: "The reveal was revoked. Sensitive overlay content is hidden.",
          }
        : {
            code: "REVEAL_TERMINATED" as const,
            status: "TERMINATED" as const,
            title: "Sensitive reveal ended",
            message: "The reveal component ended. Sensitive overlay content is hidden.",
          };
  return Object.freeze({
    outcome: "ABSTAIN",
    code: copy.code,
    status: copy.status,
    title: copy.title,
    message: copy.message,
    remainingSeconds: 0,
    timerLabel: "Time remaining: 00:00",
    scopeLabels: EMPTY_STRINGS,
    canRevoke: false,
    teardownStatus,
    accessibilityLabel: `Reveal session: ${copy.status.toLowerCase()}`,
    ariaLive: "assertive",
  });
}

/** Resolve a governed projection into a finite, non-revealing UI state. */
export function resolveRevealSession(
  input?: unknown,
  options: RevealSessionResolveOptions = {},
): RevealSessionViewModel {
  if (input === undefined) return fixedNegativeView("NO_GOVERNED_RESPONSE");
  const parsed = parseRevealSessionProjection(input);
  if (!parsed.ok) return fixedNegativeView("INVALID_PAYLOAD");
  if (parsed.payload.outcome !== "ANSWER") {
    return fixedNegativeView(
      parsed.payload.reasonCode as
        | "REVEAL_UNAVAILABLE"
        | "POLICY_DENIED"
        | "UPSTREAM_ERROR",
    );
  }

  const now = options.now ?? utcSecondFromEpoch(Date.now());
  if (!isCanonicalUtcSecond(now)) return fixedNegativeView("INVALID_PAYLOAD");
  if (Date.parse(now) >= Date.parse(parsed.payload.expiresAt as string)) {
    return terminatedView("TTL_EXPIRED", "INCOMPLETE");
  }
  return activeView(parsed.payload, now);
}

function attempt(
  action: RevealTeardownAction,
  effect: (() => void) | undefined,
  completed: RevealTeardownAction[],
  unresolved: RevealTeardownAction[],
): void {
  if (effect === undefined) {
    unresolved.push(action);
    return;
  }
  try {
    effect();
    completed.push(action);
  } catch {
    unresolved.push(action);
  }
}

/**
 * Create the timer and teardown lifecycle without mounting DOM.
 *
 * Every termination drops the controller-local key reference before invoking
 * caller effects. All effects are attempted in order; one failure never skips
 * overlay removal, obfuscated-state restoration, or audit finalization.
 */
export function createRevealSessionController(
  input?: unknown,
  options: RevealSessionControllerOptions = {},
): RevealSessionController {
  const clock = options.clock ?? DEFAULT_CLOCK;
  const parsed = input === undefined ? null : parseRevealSessionProjection(input);
  const now = utcSecondFromEpoch(clock.now());
  let state = resolveRevealSession(input, { now: now ?? "" });
  let timerHandle: unknown = null;
  let active =
    parsed?.ok === true &&
    parsed.payload.outcome === "ANSWER";
  const payload = active
    ? (parsed as Readonly<{ ok: true; payload: GovernedRevealSessionProjection }>).payload
    : null;
  let keyHandleRef = payload?.keyHandleRef ?? null;

  const notify = (): void => {
    try {
      options.onStateChange?.(state);
    } catch {
      // A view observer cannot reopen or prolong a reveal session.
    }
  };

  const clearScheduledTimer = (): void => {
    if (timerHandle === null) return;
    try {
      clock.clearTimer(timerHandle);
    } finally {
      timerHandle = null;
    }
  };

  const terminate = (cause: RevealTerminationCause): boolean => {
    if (!active || payload === null) return false;
    active = false;
    clearScheduledTimer();

    const discardedRef = keyHandleRef;
    keyHandleRef = null;
    const completed: RevealTeardownAction[] = [];
    const unresolved: RevealTeardownAction[] = [];
    attempt(
      "DISCARD_KEY_MATERIAL",
      discardedRef === null || options.onDiscardKeyMaterial === undefined
        ? undefined
        : () => options.onDiscardKeyMaterial?.(discardedRef),
      completed,
      unresolved,
    );
    attempt(
      "REMOVE_OVERLAY",
      options.onOverlayVisibilityChange === undefined
        ? undefined
        : () => options.onOverlayVisibilityChange?.(false),
      completed,
      unresolved,
    );
    attempt(
      "RESTORE_OBFUSCATED_STATE",
      options.onRestoreObfuscatedState === undefined
        ? undefined
        : () => options.onRestoreObfuscatedState?.(payload.layerRef as string),
      completed,
      unresolved,
    );

    const occurredAt = utcSecondFromEpoch(clock.now()) ?? "1970-01-01T00:00:00Z";
    const event: RevealTerminationEvent = Object.freeze({
      kind: "REVEAL_SESSION_TERMINATED",
      cause,
      sessionId: payload.sessionId,
      layerRef: payload.layerRef as string,
      auditRef: payload.auditRef as string,
      policyDecisionRef: payload.policyDecisionRef as string,
      occurredAt,
      localKeyReferenceDiscarded: true,
      requiredActions: REQUIRED_ACTIONS,
      completedActionsBeforeAudit: Object.freeze([...completed]),
      unresolvedActionsBeforeAudit: Object.freeze([...unresolved]),
      authority: "NONE",
    });
    attempt(
      "FINALIZE_AUDIT",
      options.onFinalizeAudit === undefined
        ? undefined
        : () => options.onFinalizeAudit?.(event),
      completed,
      unresolved,
    );

    state = terminatedView(
      cause,
      unresolved.length === 0 ? "COMPLETE" : "INCOMPLETE",
    );
    notify();
    return true;
  };

  const synchronize = (): void => {
    if (!active || payload === null) return;
    const observedNow = utcSecondFromEpoch(clock.now());
    if (observedNow === null) {
      terminate("TTL_EXPIRED");
      return;
    }
    const remainingMs = Date.parse(payload.expiresAt as string) - Date.parse(observedNow);
    if (remainingMs <= 0) {
      terminate("TTL_EXPIRED");
      return;
    }
    state = activeView(payload, observedNow);
    notify();
    timerHandle = clock.setTimer(synchronize, Math.min(1000, remainingMs));
  };

  if (active && payload !== null) {
    const expiresMs = Date.parse(payload.expiresAt as string);
    if (now === null || clock.now() >= expiresMs) {
      terminate("TTL_EXPIRED");
    } else {
      notify();
      timerHandle = clock.setTimer(
        synchronize,
        Math.min(1000, Math.max(1, expiresMs - clock.now())),
      );
    }
  } else {
    try {
      options.onOverlayVisibilityChange?.(false);
    } catch {
      // Negative states remain non-revealing even if caller cleanup reports failure.
    }
    notify();
  }

  return Object.freeze({
    get state(): RevealSessionViewModel {
      return state;
    },
    revoke(): boolean {
      return terminate("VIEWER_REVOKED");
    },
    destroy(): void {
      if (!terminate("COMPONENT_DESTROYED")) clearScheduledTimer();
    },
  });
}

/** Mount the accessible reveal timer HUD for one governed projection. */
export function mountRevealSessionHud(
  host: HTMLElement,
  input?: unknown,
  options: RevealSessionMountOptions = {},
): RevealSessionController {
  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const outcome = document.createElement("p");
  const message = document.createElement("p");
  const timer = document.createElement("p");
  const scopeHeading = document.createElement("h3");
  const scopeList = document.createElement("ul");
  const revokeButton = document.createElement("button");

  section.dataset.component = "reveal-session-hud";
  section.setAttribute("role", "region");
  outcome.dataset.revealOutcome = "";
  timer.dataset.revealTimer = "";
  timer.setAttribute("role", "timer");
  timer.setAttribute("aria-live", "polite");
  scopeHeading.textContent = "Consent scope";
  revokeButton.type = "button";
  revokeButton.textContent = "Revoke reveal now";
  section.replaceChildren(
    heading,
    outcome,
    message,
    timer,
    scopeHeading,
    scopeList,
    revokeButton,
  );
  host.replaceChildren(section);

  const render = (next: RevealSessionViewModel): void => {
    heading.textContent = next.title;
    outcome.textContent = `${next.outcome} / ${next.code}`;
    outcome.setAttribute("aria-live", next.ariaLive);
    message.textContent = next.message;
    timer.textContent = next.timerLabel;
    scopeList.replaceChildren(
      ...next.scopeLabels.map((label) => {
        const item = document.createElement("li");
        item.textContent = label;
        return item;
      }),
    );
    scopeHeading.hidden = next.scopeLabels.length === 0;
    scopeList.hidden = next.scopeLabels.length === 0;
    revokeButton.hidden = !next.canRevoke;
    revokeButton.disabled = !next.canRevoke;
    section.setAttribute("aria-label", next.accessibilityLabel);
    section.dataset.revealStatus = next.status;
    section.dataset.teardownStatus = next.teardownStatus;
  };

  let lifecycle: RevealSessionController | null = null;
  const handleRevoke = (): void => {
    lifecycle?.revoke();
  };
  revokeButton.addEventListener("click", handleRevoke);
  lifecycle = createRevealSessionController(input, {
    ...options,
    onStateChange: render,
  });

  return Object.freeze({
    get state(): RevealSessionViewModel {
      return (lifecycle as RevealSessionController).state;
    },
    revoke(): boolean {
      return (lifecycle as RevealSessionController).revoke();
    },
    destroy(): void {
      revokeButton.removeEventListener("click", handleRevoke);
      (lifecycle as RevealSessionController).destroy();
      host.replaceChildren();
    },
  });
}
