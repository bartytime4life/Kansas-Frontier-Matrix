export type TimeScrubSource = "drag" | "key" | "touch";

export type ScrubEvent = Readonly<{
  t: string;
  source: TimeScrubSource;
}>;

export type TimeScrubberVisibility = "VISIBLE" | "HIDDEN";

export type TimeScrubberReason =
  | "SUPPORTED"
  | "NO_GOVERNED_TIME_STATE"
  | "INVALID_GOVERNED_TIME_STATE"
  | "NON_ANSWER_OUTCOME"
  | "UNSUPPORTED_REASON"
  | "POLICY_NOT_ALLOWED"
  | "RELEASE_NOT_PUBLIC"
  | "STALE_OR_UNKNOWN_TIME"
  | "TEMPORAL_CONFLICT"
  | "SELECTED_TIME_OUT_OF_RANGE";

export type TimeScrubberViewModel = Readonly<{
  visibility: TimeScrubberVisibility;
  reason: TimeScrubberReason;
  minimumIso: string | null;
  maximumIso: string | null;
  selectedIso: string | null;
  minimumEpochSeconds: number | null;
  maximumEpochSeconds: number | null;
  selectedEpochSeconds: number | null;
  timeKind: "SELECTED_TIME" | null;
  precision: "SECOND" | null;
  timezone: "UTC" | null;
  ariaValueText: string;
  accessibilityLabel: string;
  canInteract: boolean;
}>;

export type TimeScrubberOptions = Readonly<{
  onScrub?: (event: ScrubEvent) => void;
  copyText?: (text: string) => Promise<void> | void;
  longPressMs?: number;
}>;

export type TimeScrubberController = Readonly<{
  state: TimeScrubberViewModel;
  getValue: () => string | null;
  setValue: (timestamp: string) => boolean;
  showDetails: () => void;
  hideDetails: () => void;
  destroy: () => void;
}>;

type FiniteOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR" | "HOLD";

type GovernedTimeScrubberProjection = Readonly<{
  outcome: "ANSWER";
  reasonCode: "SUPPORTED";
  time: Readonly<{
    minimum: string;
    maximum: string;
    selected: string;
    kind: "SELECTED_TIME";
    precision: "SECOND";
    timezone: "UTC";
  }>;
  trustState: Readonly<{
    policy: "ALLOW";
    release: "RELEASED";
    freshness: "CURRENT";
    temporalConflict: false;
  }>;
}>;

type ProjectionResolution = Readonly<{
  state: TimeScrubberViewModel;
  payload: GovernedTimeScrubberProjection | null;
}>;

const UTC_SECOND_PATTERN = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const FINITE_OUTCOMES = new Set<FiniteOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
  "HOLD",
]);
const TOP_LEVEL_KEYS = Object.freeze(["outcome", "reason_code", "time", "trust_state"]);
const TIME_KEYS = Object.freeze([
  "minimum",
  "maximum",
  "selected",
  "kind",
  "precision",
  "timezone",
]);
const TRUST_KEYS = Object.freeze([
  "policy",
  "release",
  "freshness",
  "temporal_conflict",
]);
const DEFAULT_LONG_PRESS_MS = 600;
const MIN_LONG_PRESS_MS = 300;
const MAX_LONG_PRESS_MS = 1500;
let scrubberSequence = 0;

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactKeys(value: Record<string, unknown>, expected: readonly string[]): boolean {
  const actual = Object.keys(value).sort();
  const wanted = [...expected].sort();
  return actual.length === wanted.length && actual.every((key, index) => key === wanted[index]);
}

function parseUtcSecond(value: unknown): Readonly<{ iso: string; epochSeconds: number }> | null {
  if (typeof value !== "string" || !UTC_SECOND_PATTERN.test(value)) return null;
  const milliseconds = Date.parse(value);
  if (!Number.isFinite(milliseconds) || milliseconds % 1000 !== 0) return null;
  const roundTrip = new Date(milliseconds).toISOString().replace(".000Z", "Z");
  if (roundTrip !== value) return null;
  return Object.freeze({ iso: value, epochSeconds: milliseconds / 1000 });
}

function ariaTimestamp(iso: string): string {
  return iso.replace("T", " ");
}

function hidden(reason: TimeScrubberReason): TimeScrubberViewModel {
  return Object.freeze({
    visibility: "HIDDEN",
    reason,
    minimumIso: null,
    maximumIso: null,
    selectedIso: null,
    minimumEpochSeconds: null,
    maximumEpochSeconds: null,
    selectedEpochSeconds: null,
    timeKind: null,
    precision: null,
    timezone: null,
    ariaValueText: "",
    accessibilityLabel: "Time scrubber unavailable",
    canInteract: false,
  });
}

function nonAnswerOutcome(input: Record<string, unknown>): boolean {
  return (
    typeof input.outcome === "string" &&
    FINITE_OUTCOMES.has(input.outcome as FiniteOutcome) &&
    input.outcome !== "ANSWER"
  );
}

function resolveProjection(input: unknown | undefined): ProjectionResolution {
  if (input === undefined) {
    return Object.freeze({ state: hidden("NO_GOVERNED_TIME_STATE"), payload: null });
  }
  if (!isRecord(input)) {
    return Object.freeze({ state: hidden("INVALID_GOVERNED_TIME_STATE"), payload: null });
  }
  if (nonAnswerOutcome(input)) {
    return Object.freeze({ state: hidden("NON_ANSWER_OUTCOME"), payload: null });
  }
  if (!hasExactKeys(input, TOP_LEVEL_KEYS) || input.outcome !== "ANSWER") {
    return Object.freeze({ state: hidden("INVALID_GOVERNED_TIME_STATE"), payload: null });
  }
  if (input.reason_code !== "SUPPORTED") {
    return Object.freeze({ state: hidden("UNSUPPORTED_REASON"), payload: null });
  }
  if (!isRecord(input.time) || !hasExactKeys(input.time, TIME_KEYS)) {
    return Object.freeze({ state: hidden("INVALID_GOVERNED_TIME_STATE"), payload: null });
  }
  if (!isRecord(input.trust_state) || !hasExactKeys(input.trust_state, TRUST_KEYS)) {
    return Object.freeze({ state: hidden("INVALID_GOVERNED_TIME_STATE"), payload: null });
  }

  const minimum = parseUtcSecond(input.time.minimum);
  const maximum = parseUtcSecond(input.time.maximum);
  const selected = parseUtcSecond(input.time.selected);
  if (
    minimum === null ||
    maximum === null ||
    selected === null ||
    input.time.kind !== "SELECTED_TIME" ||
    input.time.precision !== "SECOND" ||
    input.time.timezone !== "UTC"
  ) {
    return Object.freeze({ state: hidden("INVALID_GOVERNED_TIME_STATE"), payload: null });
  }
  if (minimum.epochSeconds > maximum.epochSeconds) {
    return Object.freeze({ state: hidden("INVALID_GOVERNED_TIME_STATE"), payload: null });
  }
  if (
    selected.epochSeconds < minimum.epochSeconds ||
    selected.epochSeconds > maximum.epochSeconds
  ) {
    return Object.freeze({ state: hidden("SELECTED_TIME_OUT_OF_RANGE"), payload: null });
  }
  if (input.trust_state.policy !== "ALLOW") {
    return Object.freeze({ state: hidden("POLICY_NOT_ALLOWED"), payload: null });
  }
  if (input.trust_state.release !== "RELEASED") {
    return Object.freeze({ state: hidden("RELEASE_NOT_PUBLIC"), payload: null });
  }
  if (input.trust_state.freshness !== "CURRENT") {
    return Object.freeze({ state: hidden("STALE_OR_UNKNOWN_TIME"), payload: null });
  }
  if (input.trust_state.temporal_conflict !== false) {
    return Object.freeze({ state: hidden("TEMPORAL_CONFLICT"), payload: null });
  }

  const payload: GovernedTimeScrubberProjection = Object.freeze({
    outcome: "ANSWER",
    reasonCode: "SUPPORTED",
    time: Object.freeze({
      minimum: minimum.iso,
      maximum: maximum.iso,
      selected: selected.iso,
      kind: "SELECTED_TIME",
      precision: "SECOND",
      timezone: "UTC",
    }),
    trustState: Object.freeze({
      policy: "ALLOW",
      release: "RELEASED",
      freshness: "CURRENT",
      temporalConflict: false,
    }),
  });
  const state: TimeScrubberViewModel = Object.freeze({
    visibility: "VISIBLE",
    reason: "SUPPORTED",
    minimumIso: minimum.iso,
    maximumIso: maximum.iso,
    selectedIso: selected.iso,
    minimumEpochSeconds: minimum.epochSeconds,
    maximumEpochSeconds: maximum.epochSeconds,
    selectedEpochSeconds: selected.epochSeconds,
    timeKind: "SELECTED_TIME",
    precision: "SECOND",
    timezone: "UTC",
    ariaValueText: ariaTimestamp(selected.iso),
    accessibilityLabel: "Selected time in UTC with second precision",
    canInteract: true,
  });

  return Object.freeze({ state, payload });
}

function clampLongPress(value: number | undefined): number {
  if (value === undefined || !Number.isFinite(value)) return DEFAULT_LONG_PRESS_MS;
  return Math.min(Math.max(Math.round(value), MIN_LONG_PRESS_MS), MAX_LONG_PRESS_MS);
}

function epochToIso(epochSeconds: number): string {
  return new Date(epochSeconds * 1000).toISOString().replace(".000Z", "Z");
}

async function copyWithFallback(text: string, document: Document): Promise<void> {
  const clipboard = document.defaultView?.navigator.clipboard;
  if (clipboard?.writeText !== undefined) {
    await clipboard.writeText(text);
    return;
  }

  const textarea = document.createElement("textarea");
  textarea.value = text;
  textarea.setAttribute("readonly", "");
  textarea.style.position = "fixed";
  textarea.style.opacity = "0";
  document.body.append(textarea);
  textarea.select();
  const copied = document.execCommand("copy");
  textarea.remove();
  if (!copied) throw new Error("Clipboard copy was not available.");
}

/**
 * Resolve an app-local governed time projection into a finite, fail-closed scrubber state.
 *
 * This function does not resolve evidence, decide policy, infer freshness, or authorize
 * release. It accepts only a deliberately small projection that is already ANSWER /
 * SUPPORTED, ALLOW, RELEASED, CURRENT, conflict-free, UTC, and second-precise.
 */
export function resolveTimeScrubber(input?: unknown): TimeScrubberViewModel {
  return resolveProjection(input).state;
}

/**
 * Mount an accessible, single-handle time scrubber for already-governed temporal state.
 *
 * The controller performs no network access and reads no lifecycle, canonical, graph,
 * vector, AI-provider, or browser-persistence store. Selected time scopes interaction;
 * it is not evidence or claim proof.
 */
export function mountTimeScrubber(
  host: HTMLElement,
  input?: unknown,
  options: TimeScrubberOptions = {},
): TimeScrubberController {
  const resolved = resolveProjection(input);
  const { state, payload } = resolved;
  host.replaceChildren();

  if (state.visibility === "HIDDEN" || payload === null) {
    return Object.freeze({
      state,
      getValue: () => null,
      setValue: () => false,
      showDetails: () => undefined,
      hideDetails: () => undefined,
      destroy: () => host.replaceChildren(),
    });
  }

  const document = host.ownerDocument;
  const root = document.createElement("section");
  const label = document.createElement("label");
  const inputElement = document.createElement("input");
  const output = document.createElement("output");
  const selectedTime = document.createElement("time");
  const detailToggle = document.createElement("button");
  const detailRegion = document.createElement("div");
  const exactTimestamp = document.createElement("code");
  const copyButton = document.createElement("button");
  const copyStatus = document.createElement("p");
  const announcement = document.createElement("p");
  const scrubberId = `kfm-time-scrubber-${++scrubberSequence}`;
  const detailId = `${scrubberId}-details`;
  const announcementId = `${scrubberId}-announcement`;
  const minimum = state.minimumEpochSeconds as number;
  const maximum = state.maximumEpochSeconds as number;
  let current = state.selectedEpochSeconds as number;
  let lastPointerType: string | null = null;
  let longPressTimer: number | null = null;
  let destroyed = false;

  root.dataset.component = "accessible-time-scrubber";
  root.setAttribute("aria-label", state.accessibilityLabel);

  label.htmlFor = scrubberId;
  label.textContent = "Selected time";

  inputElement.id = scrubberId;
  inputElement.type = "range";
  inputElement.min = String(minimum);
  inputElement.max = String(maximum);
  inputElement.step = "1";
  inputElement.value = String(current);
  inputElement.dataset.component = "time-scrubber-slider";
  inputElement.setAttribute("role", "slider");
  inputElement.setAttribute("aria-valuemin", String(minimum));
  inputElement.setAttribute("aria-valuemax", String(maximum));
  inputElement.setAttribute("aria-valuenow", String(current));
  inputElement.setAttribute("aria-valuetext", ariaTimestamp(epochToIso(current)));
  inputElement.setAttribute("aria-describedby", announcementId);

  output.htmlFor = scrubberId;
  output.dataset.component = "time-scrubber-output";
  selectedTime.dateTime = epochToIso(current);
  selectedTime.textContent = ariaTimestamp(selectedTime.dateTime);
  output.append(selectedTime);

  detailToggle.type = "button";
  detailToggle.textContent = "Show exact timestamp";
  detailToggle.setAttribute("aria-controls", detailId);
  detailToggle.setAttribute("aria-expanded", "false");
  detailToggle.dataset.component = "time-scrubber-details-toggle";

  detailRegion.id = detailId;
  detailRegion.hidden = true;
  detailRegion.setAttribute("role", "region");
  detailRegion.setAttribute("aria-label", "Exact selected timestamp");
  detailRegion.dataset.component = "time-scrubber-details";

  exactTimestamp.textContent = epochToIso(current);
  copyButton.type = "button";
  copyButton.textContent = "Copy timestamp";
  copyButton.setAttribute("aria-label", `Copy selected timestamp ${epochToIso(current)}`);
  copyStatus.setAttribute("aria-live", "polite");
  copyStatus.dataset.component = "time-scrubber-copy-status";
  detailRegion.append(exactTimestamp, copyButton, copyStatus);

  announcement.id = announcementId;
  announcement.setAttribute("aria-live", "polite");
  announcement.dataset.component = "time-scrubber-announcement";
  announcement.textContent = `Selected time ${ariaTimestamp(epochToIso(current))}`;

  root.append(label, inputElement, output, detailToggle, detailRegion, announcement);
  host.append(root);

  const cancelLongPress = (): void => {
    if (longPressTimer !== null) {
      document.defaultView?.clearTimeout(longPressTimer);
      longPressTimer = null;
    }
  };

  const hideDetails = (): void => {
    cancelLongPress();
    detailRegion.hidden = true;
    detailToggle.setAttribute("aria-expanded", "false");
    copyStatus.textContent = "";
  };

  const showDetails = (): void => {
    detailRegion.hidden = false;
    detailToggle.setAttribute("aria-expanded", "true");
  };

  const updateValue = (next: number, source: TimeScrubSource | null): boolean => {
    if (!Number.isSafeInteger(next) || next < minimum || next > maximum) return false;
    current = next;
    const iso = epochToIso(current);
    inputElement.value = String(current);
    inputElement.setAttribute("aria-valuenow", String(current));
    inputElement.setAttribute("aria-valuetext", ariaTimestamp(iso));
    selectedTime.dateTime = iso;
    selectedTime.textContent = ariaTimestamp(iso);
    exactTimestamp.textContent = iso;
    copyButton.setAttribute("aria-label", `Copy selected timestamp ${iso}`);
    announcement.textContent = `Selected time ${ariaTimestamp(iso)}`;
    copyStatus.textContent = "";
    if (source !== null) options.onScrub?.(Object.freeze({ t: iso, source }));
    return true;
  };

  const setValue = (timestamp: string): boolean => {
    const parsed = parseUtcSecond(timestamp);
    if (parsed === null) return false;
    return updateValue(parsed.epochSeconds, null);
  };

  const onKeyDown = (event: KeyboardEvent): void => {
    let next: number | null = null;
    const delta = event.shiftKey ? 60 : 1;
    switch (event.key) {
      case "ArrowLeft":
      case "ArrowDown":
        next = Math.max(minimum, current - delta);
        break;
      case "ArrowRight":
      case "ArrowUp":
        next = Math.min(maximum, current + delta);
        break;
      case "Home":
        next = minimum;
        break;
      case "End":
        next = maximum;
        break;
      case "Escape":
        hideDetails();
        return;
      default:
        return;
    }
    event.preventDefault();
    updateValue(next, "key");
  };

  const onPointerDown = (event: PointerEvent): void => {
    lastPointerType = event.pointerType || "mouse";
    cancelLongPress();
    if (lastPointerType === "touch") {
      const delay = clampLongPress(options.longPressMs);
      longPressTimer = document.defaultView?.setTimeout(() => {
        longPressTimer = null;
        showDetails();
      }, delay) ?? null;
    }
  };

  const onPointerEnd = (): void => {
    cancelLongPress();
    document.defaultView?.setTimeout(() => {
      lastPointerType = null;
    }, 0);
  };

  const onInput = (): void => {
    const parsed = Number(inputElement.value);
    const source: TimeScrubSource = lastPointerType === "touch" ? "touch" : "drag";
    if (!updateValue(parsed, source)) inputElement.value = String(current);
  };

  const onToggle = (): void => {
    if (detailRegion.hidden) showDetails();
    else hideDetails();
  };

  const onCopy = async (): Promise<void> => {
    const text = epochToIso(current);
    try {
      if (options.copyText !== undefined) await options.copyText(text);
      else await copyWithFallback(text, document);
      copyStatus.textContent = "Timestamp copied.";
    } catch {
      copyStatus.textContent = "Timestamp could not be copied.";
    }
  };

  const onDocumentKeyDown = (event: KeyboardEvent): void => {
    if (event.key === "Escape" && !detailRegion.hidden) hideDetails();
  };

  inputElement.addEventListener("keydown", onKeyDown);
  inputElement.addEventListener("pointerdown", onPointerDown);
  inputElement.addEventListener("pointerup", onPointerEnd);
  inputElement.addEventListener("pointercancel", onPointerEnd);
  inputElement.addEventListener("input", onInput);
  detailToggle.addEventListener("click", onToggle);
  copyButton.addEventListener("click", onCopy);
  document.addEventListener("keydown", onDocumentKeyDown);

  const destroy = (): void => {
    if (destroyed) return;
    destroyed = true;
    cancelLongPress();
    inputElement.removeEventListener("keydown", onKeyDown);
    inputElement.removeEventListener("pointerdown", onPointerDown);
    inputElement.removeEventListener("pointerup", onPointerEnd);
    inputElement.removeEventListener("pointercancel", onPointerEnd);
    inputElement.removeEventListener("input", onInput);
    detailToggle.removeEventListener("click", onToggle);
    copyButton.removeEventListener("click", onCopy);
    document.removeEventListener("keydown", onDocumentKeyDown);
    host.replaceChildren();
  };

  return Object.freeze({
    state,
    getValue: () => (destroyed ? null : epochToIso(current)),
    setValue: (timestamp: string) => (!destroyed ? setValue(timestamp) : false),
    showDetails: () => {
      if (!destroyed) showDetails();
    },
    hideDetails: () => {
      if (!destroyed) hideDetails();
    },
    destroy,
  });
}
