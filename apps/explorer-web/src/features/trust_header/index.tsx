import {
  type EvidenceDrawerTrustState,
  type GovernedEvidenceDrawerProjection,
  parseEvidenceDrawerProjection,
} from "../../adapters/GovernedClient";

export type TrustHeaderVisibility = "VISIBLE" | "HIDDEN";

export type TrustHeaderState = "SUPPORTED" | "ABSTAIN" | "DENY" | "ERROR";

export type TrustHeaderReason =
  | "SUPPORTED"
  | "ABSTAIN_OUTCOME"
  | "DENY_OUTCOME"
  | "ERROR_OUTCOME"
  | "NO_GOVERNED_RESPONSE"
  | "INVALID_GOVERNED_RESPONSE";

export type TrustHeaderBadgeKey =
  | "outcome"
  | "policy"
  | "review"
  | "release"
  | "freshness"
  | "correction";

export type TrustHeaderBadge = Readonly<{
  key: TrustHeaderBadgeKey;
  label: string;
  value: string;
}>;

export type TrustHeaderViewModel = Readonly<{
  visibility: TrustHeaderVisibility;
  state: TrustHeaderState;
  reason: TrustHeaderReason;
  title: string;
  message: string;
  badges: readonly TrustHeaderBadge[];
  canOpenDrawer: boolean;
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

export type TrustHeaderMountOptions = Readonly<{
  compact?: boolean;
  onOpenDrawer?: (payload: GovernedEvidenceDrawerProjection) => void;
}>;

export type TrustHeaderController = Readonly<{
  state: TrustHeaderViewModel;
  destroy: () => void;
}>;

const EMPTY_BADGES = Object.freeze([]) as readonly TrustHeaderBadge[];

const NEGATIVE_COPY: Readonly<
  Record<
    Exclude<TrustHeaderState, "SUPPORTED">,
    Readonly<{ title: string; message: string; accessibilityLabel: string }>
  >
> = Object.freeze({
  ABSTAIN: Object.freeze({
    title: "Support not sufficient",
    message: "Released evidence is not sufficient for this view.",
    accessibilityLabel: "Trust status: insufficient support",
  }),
  DENY: Object.freeze({
    title: "View restricted",
    message: "Policy does not permit this view to expose governed detail.",
    accessibilityLabel: "Trust status: restricted",
  }),
  ERROR: Object.freeze({
    title: "Trust status unavailable",
    message: "The governed trust projection could not be completed.",
    accessibilityLabel: "Trust status: unavailable",
  }),
});

function badge(
  key: TrustHeaderBadgeKey,
  label: string,
  value: string,
): TrustHeaderBadge {
  return Object.freeze({ key, label, value });
}

function supportedBadges(
  trustState: EvidenceDrawerTrustState,
): readonly TrustHeaderBadge[] {
  return Object.freeze([
    badge("outcome", "Outcome", "ANSWER"),
    badge("policy", "Policy", trustState.policy),
    badge("review", "Review", trustState.review),
    badge("release", "Release", trustState.release),
    badge("freshness", "Freshness", trustState.freshness),
    badge("correction", "Correction", trustState.correction),
  ]);
}

function hidden(reason: TrustHeaderReason): TrustHeaderViewModel {
  return Object.freeze({
    visibility: "HIDDEN",
    state: "ERROR",
    reason,
    title: "Trust status unavailable",
    message: "No Trust Header is rendered without a valid governed projection.",
    badges: EMPTY_BADGES,
    canOpenDrawer: false,
    accessibilityLabel: "Trust status unavailable",
    ariaLive: "polite",
  });
}

function negative(
  state: Exclude<TrustHeaderState, "SUPPORTED">,
  reason: Exclude<
    TrustHeaderReason,
    "SUPPORTED" | "NO_GOVERNED_RESPONSE" | "INVALID_GOVERNED_RESPONSE"
  >,
): TrustHeaderViewModel {
  const copy = NEGATIVE_COPY[state];
  return Object.freeze({
    visibility: "VISIBLE",
    state,
    reason,
    title: copy.title,
    message: copy.message,
    badges: Object.freeze([badge("outcome", "Outcome", state)]),
    canOpenDrawer: false,
    accessibilityLabel: copy.accessibilityLabel,
    ariaLive: state === "ERROR" ? "assertive" : "polite",
  });
}

function resolveProjection(input: unknown | undefined): Readonly<{
  state: TrustHeaderViewModel;
  payload: GovernedEvidenceDrawerProjection | null;
}> {
  if (input === undefined) {
    return Object.freeze({
      state: hidden("NO_GOVERNED_RESPONSE"),
      payload: null,
    });
  }

  const parsed = parseEvidenceDrawerProjection(input);
  if (!parsed.ok) {
    return Object.freeze({
      state: hidden("INVALID_GOVERNED_RESPONSE"),
      payload: null,
    });
  }

  const { payload } = parsed;
  if (payload.outcome === "ABSTAIN") {
    return Object.freeze({
      state: negative("ABSTAIN", "ABSTAIN_OUTCOME"),
      payload: null,
    });
  }
  if (payload.outcome === "DENY") {
    return Object.freeze({
      state: negative("DENY", "DENY_OUTCOME"),
      payload: null,
    });
  }
  if (payload.outcome === "ERROR") {
    return Object.freeze({
      state: negative("ERROR", "ERROR_OUTCOME"),
      payload: null,
    });
  }

  const state: TrustHeaderViewModel = Object.freeze({
    visibility: "VISIBLE",
    state: "SUPPORTED",
    reason: "SUPPORTED",
    title: "Governed trust status",
    message: "Released evidence passed the bounded browser trust projection.",
    badges: supportedBadges(payload.trustState),
    canOpenDrawer: true,
    accessibilityLabel: "Trust status: supported released evidence",
    ariaLive: "polite",
  });

  return Object.freeze({ state, payload });
}

/**
 * Resolve the existing governed Evidence Drawer projection into Trust Header
 * chrome. Missing and malformed input produces no renderable header. Finite
 * negative outcomes use fixed copy and never reflect protected payload detail.
 */
export function resolveTrustHeader(input?: unknown): TrustHeaderViewModel {
  return resolveProjection(input).state;
}

/**
 * Mount a text-first, non-color-only Trust Header projection.
 *
 * This renderer performs no transport, persistence, policy evaluation, evidence
 * resolution, release mutation, or model invocation. Supported detail is handed
 * to the existing Evidence Drawer callback rather than rendered as authority in
 * the header itself.
 */
export function mountTrustHeader(
  host: HTMLElement,
  input?: unknown,
  options: TrustHeaderMountOptions = {},
): TrustHeaderController {
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
  const heading = document.createElement("h2");
  const message = document.createElement("p");
  const badgeList = document.createElement("dl");
  let drawerButton: HTMLButtonElement | null = null;

  region.dataset.component = "trust-header";
  region.dataset.state = state.state;
  region.dataset.layout = options.compact === true ? "compact" : "wide";
  region.setAttribute("role", state.state === "ERROR" ? "alert" : "status");
  region.setAttribute("aria-label", state.accessibilityLabel);
  region.setAttribute("aria-live", state.ariaLive);

  heading.textContent = state.title;
  message.textContent = state.message;
  badgeList.setAttribute("aria-label", "Governed trust status labels");

  for (const item of state.badges) {
    const row = document.createElement("div");
    const term = document.createElement("dt");
    const value = document.createElement("dd");
    row.dataset.trustBadge = item.key;
    term.textContent = item.label;
    value.textContent = item.value;
    row.append(term, value);
    badgeList.append(row);
  }

  region.append(heading, message, badgeList);

  if (
    state.canOpenDrawer &&
    payload !== null &&
    options.onOpenDrawer !== undefined
  ) {
    const supportedPayload = payload;
    drawerButton = document.createElement("button");
    drawerButton.type = "button";
    drawerButton.textContent = "Open Evidence Drawer";
    drawerButton.addEventListener("click", () => {
      options.onOpenDrawer?.(supportedPayload);
    });
    region.append(drawerButton);
  }

  host.replaceChildren(region);

  function destroy(): void {
    drawerButton?.replaceWith();
    host.replaceChildren();
  }

  return Object.freeze({ state, destroy });
}
