import {
  EXPLORATION_MODES,
  type ExplorationMode,
} from "./exploration-mode";

/**
 * App-local, public-safe composition for a compact "what you are seeing" strip.
 * It projects already-governed values and never infers truth from pixels,
 * renderer properties, camera motion, or hidden lifecycle stores.
 */
export const VIEW_CONTEXT_PROFILE = "kfm.explorer.view-context.v1" as const;

export const VIEW_CONTEXT_REPRESENTATION_ROLES = [
  "authoritative",
  "official",
  "derived",
  "context",
] as const;

export type ViewContextRepresentationRole =
  (typeof VIEW_CONTEXT_REPRESENTATION_ROLES)[number];

export type ViewContextInput = Readonly<{
  profile: typeof VIEW_CONTEXT_PROFILE;
  placeLabel: string;
  timeLabel: string;
  mode: ExplorationMode;
  visibleLayerCount: number;
  representationRole: ViewContextRepresentationRole;
  release: "RELEASED" | "UNRELEASED" | "WITHDRAWN";
  freshness: "CURRENT" | "STALE" | "UNKNOWN";
  correction: "NONE" | "CURRENT" | "CORRECTED" | "SUPERSEDED";
  publicSafe: true;
}>;

export type ViewContextReason =
  | "SUPPORTED"
  | "INVALID_CONTEXT"
  | "NOT_PUBLIC_SAFE";

export type ViewContextViewModel = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  reason: ViewContextReason;
  heading: "What you are seeing";
  summary: string;
  labels: readonly string[];
  derivedDisclosure: string | null;
  accessibilityLabel: string;
}>;

export type ViewContextStripController = Readonly<{
  state: ViewContextViewModel;
  destroy: () => void;
}>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "placeLabel",
  "timeLabel",
  "mode",
  "visibleLayerCount",
  "representationRole",
  "release",
  "freshness",
  "correction",
  "publicSafe",
]);
const MODES = new Set<string>(EXPLORATION_MODES);
const ROLES = new Set<string>(VIEW_CONTEXT_REPRESENTATION_ROLES);
const RELEASES = new Set(["RELEASED", "UNRELEASED", "WITHDRAWN"]);
const FRESHNESS = new Set(["CURRENT", "STALE", "UNKNOWN"]);
const CORRECTIONS = new Set([
  "NONE",
  "CURRENT",
  "CORRECTED",
  "SUPERSEDED",
]);
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
const DERIVED_DISCLOSURE =
  "Derived representation — computed from upstream evidence; not a source-observed relationship or event.";

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

function isBoundedLabel(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length > 0 &&
    value.length <= 120 &&
    value.trim() === value &&
    !CONTROL_CHARACTER.test(value)
  );
}

function hidden(reason: ViewContextReason): ViewContextViewModel {
  return Object.freeze({
    visibility: "HIDDEN",
    reason,
    heading: "What you are seeing",
    summary: "View context is unavailable.",
    labels: Object.freeze([]),
    derivedDisclosure: null,
    accessibilityLabel: "View context unavailable",
  });
}

/** Strictly parse the UI-owned public context projection. */
export function parseViewContext(value: unknown): ViewContextInput | null {
  if (!isRecord(value) || !hasExactFields(value, TOP_LEVEL_FIELDS)) return null;
  if (value.profile !== VIEW_CONTEXT_PROFILE) return null;
  if (value.publicSafe !== true) return null;
  if (!isBoundedLabel(value.placeLabel) || !isBoundedLabel(value.timeLabel)) {
    return null;
  }
  if (typeof value.mode !== "string" || !MODES.has(value.mode)) return null;
  if (
    typeof value.visibleLayerCount !== "number" ||
    !Number.isInteger(value.visibleLayerCount) ||
    value.visibleLayerCount < 0 ||
    value.visibleLayerCount > 256
  ) {
    return null;
  }
  if (
    typeof value.representationRole !== "string" ||
    !ROLES.has(value.representationRole)
  ) {
    return null;
  }
  if (typeof value.release !== "string" || !RELEASES.has(value.release)) {
    return null;
  }
  if (
    typeof value.freshness !== "string" ||
    !FRESHNESS.has(value.freshness)
  ) {
    return null;
  }
  if (
    typeof value.correction !== "string" ||
    !CORRECTIONS.has(value.correction)
  ) {
    return null;
  }

  return Object.freeze({
    profile: VIEW_CONTEXT_PROFILE,
    placeLabel: value.placeLabel,
    timeLabel: value.timeLabel,
    mode: value.mode as ExplorationMode,
    visibleLayerCount: value.visibleLayerCount,
    representationRole:
      value.representationRole as ViewContextRepresentationRole,
    release: value.release as ViewContextInput["release"],
    freshness: value.freshness as ViewContextInput["freshness"],
    correction: value.correction as ViewContextInput["correction"],
    publicSafe: true,
  });
}

/** Resolve a strict input into a finite no-leak view model. */
export function resolveViewContext(value: unknown): ViewContextViewModel {
  if (isRecord(value) && value.publicSafe !== true) {
    return hidden("NOT_PUBLIC_SAFE");
  }
  const context = parseViewContext(value);
  if (context === null) return hidden("INVALID_CONTEXT");

  const labels = Object.freeze([
    `Place: ${context.placeLabel}`,
    `Time: ${context.timeLabel}`,
    `Mode: ${context.mode}`,
    `Visible layers: ${context.visibleLayerCount}`,
    `Representation: ${context.representationRole}`,
    `Release: ${context.release}`,
    `Freshness: ${context.freshness}`,
    `Correction: ${context.correction}`,
  ]);
  const summary = `${context.placeLabel}; ${context.timeLabel}; ${context.mode}; ${context.visibleLayerCount} visible layer${context.visibleLayerCount === 1 ? "" : "s"}; ${context.representationRole} representation.`;

  return Object.freeze({
    visibility: "VISIBLE",
    reason: "SUPPORTED",
    heading: "What you are seeing",
    summary,
    labels,
    derivedDisclosure:
      context.representationRole === "derived" ? DERIVED_DISCLOSURE : null,
    accessibilityLabel: `View context: ${summary}`,
  });
}

/** Mount the compact context strip with an optional evidence handoff. */
export function mountViewContextStrip(
  host: HTMLElement,
  input: unknown,
  onInspectEvidence?: () => void,
): ViewContextStripController {
  const state = resolveViewContext(input);
  const document = host.ownerDocument;
  const region = document.createElement("section");
  const heading = document.createElement("h3");
  const summary = document.createElement("p");
  const list = document.createElement("ul");

  region.dataset.component = "view-context-strip";
  region.dataset.visibility = state.visibility;
  region.setAttribute("aria-label", state.accessibilityLabel);
  heading.textContent = state.heading;
  summary.textContent = state.summary;
  list.setAttribute("aria-label", "Current view context");
  for (const label of state.labels) {
    const item = document.createElement("li");
    item.textContent = label;
    list.append(item);
  }

  const children: Node[] = [heading, summary, list];
  if (state.derivedDisclosure !== null) {
    const disclosure = document.createElement("p");
    disclosure.className = "guardrail";
    disclosure.dataset.component = "view-context-derived-disclosure";
    disclosure.setAttribute("role", "note");
    disclosure.textContent = state.derivedDisclosure;
    children.push(disclosure);
  }
  if (onInspectEvidence !== undefined && state.visibility === "VISIBLE") {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = "Inspect evidence";
    button.addEventListener("click", onInspectEvidence);
    children.push(button);
    region.replaceChildren(...children);
    host.replaceChildren(region);
    return Object.freeze({
      state,
      destroy: () => {
        button.removeEventListener("click", onInspectEvidence);
        host.replaceChildren();
      },
    });
  }

  region.replaceChildren(...children);
  host.replaceChildren(region);
  return Object.freeze({
    state,
    destroy: () => host.replaceChildren(),
  });
}
