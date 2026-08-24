import {
  MAP_RUNTIME_PORT_PROFILE,
  MAP_RUNTIME_STATES,
  MAP_RUNTIME_TRUST_STATE_REASONS,
  isMapFeatureSelection,
  isMapRuntimeCamera,
  type MapRuntimePort,
  type MapRuntimeReasonCode,
  type MapRuntimeSnapshot,
  type MapRuntimeState,
} from "@kfm/maplibre";

export const MAP_RUNTIME_TRUST_STATUS_PROFILE =
  "kfm.explorer.map-runtime-trust-status.v1" as const;

export type MapRuntimeTrustStatusTone =
  | "positive"
  | "caution"
  | "critical"
  | "neutral";

export type MapRuntimeTrustStatus = Readonly<{
  profile: typeof MAP_RUNTIME_TRUST_STATUS_PROFILE;
  valid: boolean;
  state: MapRuntimeState;
  reason: MapRuntimeReasonCode | null;
  title: string;
  message: string;
  tone: MapRuntimeTrustStatusTone;
  role: "status" | "alert";
  ariaLive: "polite" | "assertive";
  ariaBusy: boolean;
  canResolveSelection: boolean;
  accessibilityLabel: string;
}>;

export type MapRuntimeTrustStatusController = Readonly<{
  getState: () => MapRuntimeTrustStatus;
  destroy: () => void;
}>;

type StatusCopy = Readonly<{
  title: string;
  message: string;
  tone: MapRuntimeTrustStatusTone;
}>;

const SNAPSHOT_FIELDS = new Set([
  "profile",
  "state",
  "camera",
  "selection",
  "reason",
]);
const STATES = new Set<string>(MAP_RUNTIME_STATES);
const CRITICAL_STATES = new Set<MapRuntimeState>([
  "DENIED",
  "WITHDRAWN",
  "ERROR",
]);

const STATUS_COPY: Readonly<Record<MapRuntimeState, StatusCopy>> = Object.freeze({
  IDLE: Object.freeze({
    title: "Map runtime idle",
    message: "The map runtime has not started. Candidate selection is unavailable.",
    tone: "neutral",
  }),
  INITIALIZING: Object.freeze({
    title: "Map runtime initializing",
    message: "The renderer-neutral runtime is starting. Candidate selection remains blocked.",
    tone: "neutral",
  }),
  READY: Object.freeze({
    title: "Map runtime ready",
    message: "Candidate selections may enter the governed evidence bridge.",
    tone: "positive",
  }),
  STALE: Object.freeze({
    title: "Map runtime stale",
    message: "The runtime is stale. Candidate selection remains blocked until recovery.",
    tone: "caution",
  }),
  ABSTAINED: Object.freeze({
    title: "Map runtime abstained",
    message: "The runtime cannot support a selection in its current state.",
    tone: "caution",
  }),
  DENIED: Object.freeze({
    title: "Map runtime denied",
    message: "The runtime is denied. No candidate selection is exposed.",
    tone: "critical",
  }),
  CONFLICT: Object.freeze({
    title: "Map runtime conflict",
    message: "The runtime reports conflicting support. Candidate selection remains blocked.",
    tone: "caution",
  }),
  DEGRADED: Object.freeze({
    title: "Map runtime degraded",
    message: "The runtime is degraded. Candidate selection remains blocked until recovery.",
    tone: "caution",
  }),
  WITHDRAWN: Object.freeze({
    title: "Map runtime withdrawn",
    message: "The runtime reports withdrawal. No candidate selection is current.",
    tone: "critical",
  }),
  ROLLED_BACK: Object.freeze({
    title: "Map runtime rolled back",
    message: "The runtime reports rollback. Candidate selection remains blocked until recovery.",
    tone: "caution",
  }),
  ERROR: Object.freeze({
    title: "Map runtime error",
    message: "The runtime failed. No partial selection or internal diagnostic is shown.",
    tone: "critical",
  }),
  DISPOSED: Object.freeze({
    title: "Map runtime disposed",
    message: "The runtime has been disposed. Candidate selection is unavailable.",
    tone: "neutral",
  }),
});

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

function expectedReason(state: MapRuntimeState): MapRuntimeReasonCode | null {
  if (state === "DISPOSED") return "MAP_RUNTIME_DISPOSED";
  if (Object.prototype.hasOwnProperty.call(MAP_RUNTIME_TRUST_STATE_REASONS, state)) {
    return MAP_RUNTIME_TRUST_STATE_REASONS[
      state as keyof typeof MAP_RUNTIME_TRUST_STATE_REASONS
    ];
  }
  return null;
}

function isSnapshot(value: unknown): value is MapRuntimeSnapshot {
  if (!isRecord(value) || !hasExactFields(value, SNAPSHOT_FIELDS)) return false;
  if (value.profile !== MAP_RUNTIME_PORT_PROFILE) return false;
  if (typeof value.state !== "string" || !STATES.has(value.state)) return false;
  if (!isMapRuntimeCamera(value.camera)) return false;
  if (value.selection !== null && !isMapFeatureSelection(value.selection)) return false;

  const state = value.state as MapRuntimeState;
  if (value.reason !== expectedReason(state)) return false;
  return state === "READY" || value.selection === null;
}

function invalidStatus(): MapRuntimeTrustStatus {
  return Object.freeze({
    profile: MAP_RUNTIME_TRUST_STATUS_PROFILE,
    valid: false,
    state: "ERROR",
    reason: "MAP_RUNTIME_STATE_INVALID",
    title: "Map runtime status unavailable",
    message: "The runtime status is invalid. No selection or internal diagnostic is shown.",
    tone: "critical",
    role: "alert",
    ariaLive: "assertive",
    ariaBusy: false,
    canResolveSelection: false,
    accessibilityLabel: "Map runtime status: invalid",
  });
}

/**
 * Resolve one KFM-owned runtime snapshot into fixed, text-first UI status.
 *
 * The presenter reports runtime state only. It does not infer evidence,
 * sensitivity, policy, review, correction, release, rollback authority, or
 * publication state from renderer behavior.
 */
export function resolveMapRuntimeTrustStatus(
  input?: unknown,
): MapRuntimeTrustStatus {
  if (!isSnapshot(input)) return invalidStatus();

  const copy = STATUS_COPY[input.state];
  const critical = CRITICAL_STATES.has(input.state);
  return Object.freeze({
    profile: MAP_RUNTIME_TRUST_STATUS_PROFILE,
    valid: true,
    state: input.state,
    reason: input.reason,
    title: copy.title,
    message: copy.message,
    tone: copy.tone,
    role: critical ? "alert" : "status",
    ariaLive: critical ? "assertive" : "polite",
    ariaBusy: input.state === "INITIALIZING",
    canResolveSelection: input.state === "READY",
    accessibilityLabel: `Map runtime status: ${input.state.toLocaleLowerCase()}`,
  });
}

/** Mount an observable, non-color-only projection of MapRuntimePort state. */
export function mountMapRuntimeTrustStatus(
  host: HTMLElement,
  runtime: MapRuntimePort,
): MapRuntimeTrustStatusController {
  const document = host.ownerDocument;
  const region = document.createElement("section");
  let active = true;
  let state = invalidStatus();

  region.dataset.component = "map-runtime-trust-status";
  host.replaceChildren(region);

  function render(snapshot?: unknown): void {
    if (!active) return;
    state = resolveMapRuntimeTrustStatus(snapshot);

    const heading = document.createElement("h3");
    const message = document.createElement("p");
    const details = document.createElement("dl");
    const stateRow = document.createElement("div");
    const stateTerm = document.createElement("dt");
    const stateValue = document.createElement("dd");
    const reasonRow = document.createElement("div");
    const reasonTerm = document.createElement("dt");
    const reasonValue = document.createElement("dd");
    const selectionRow = document.createElement("div");
    const selectionTerm = document.createElement("dt");
    const selectionValue = document.createElement("dd");

    heading.textContent = state.title;
    message.textContent = state.message;
    details.setAttribute("aria-label", "Map runtime status fields");
    stateTerm.textContent = "State";
    stateValue.textContent = state.state;
    reasonTerm.textContent = "Reason";
    reasonValue.textContent = state.reason ?? "NONE";
    selectionTerm.textContent = "Candidate selection";
    selectionValue.textContent = state.canResolveSelection ? "ELIGIBLE" : "BLOCKED";
    stateRow.append(stateTerm, stateValue);
    reasonRow.append(reasonTerm, reasonValue);
    selectionRow.append(selectionTerm, selectionValue);
    details.append(stateRow, reasonRow, selectionRow);

    region.dataset.state = state.state;
    region.dataset.tone = state.tone;
    region.setAttribute("role", state.role);
    region.setAttribute("aria-label", state.accessibilityLabel);
    region.setAttribute("aria-live", state.ariaLive);
    region.setAttribute("aria-busy", state.ariaBusy ? "true" : "false");
    region.replaceChildren(heading, message, details);
  }

  let unsubscribe = (): void => undefined;
  try {
    unsubscribe = runtime.subscribeSnapshot(render);
    render(runtime.getSnapshot());
  } catch {
    render(undefined);
  }

  return Object.freeze({
    getState: () => state,
    destroy(): void {
      if (!active) return;
      active = false;
      unsubscribe();
      host.replaceChildren();
    },
  });
}
