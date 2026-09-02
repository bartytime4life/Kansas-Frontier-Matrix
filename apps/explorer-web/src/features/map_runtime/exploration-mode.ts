/**
 * App-local exploration-mode proof inspired by spatial-navigation products.
 *
 * This module does not change MapRuntimePort, acquire a renderer, request
 * pointer lock, resolve evidence, or grant release/publication authority. It
 * makes interaction state explicit and interruptible before any concrete
 * renderer integration is attempted.
 */
export const EXPLORATION_MODE_PROFILE =
  "kfm.explorer.interaction-mode.v1" as const;

export const EXPLORATION_MODES = [
  "ORIENT",
  "INSPECT",
  "TRAVERSE",
  "STORY",
] as const;

export type ExplorationMode = (typeof EXPLORATION_MODES)[number];

export const EXPLORATION_MODE_REASONS = [
  "INITIALIZED",
  "USER_SELECTED",
  "SHORTCUT_SELECTED",
  "SPEED_CHANGED",
  "INVALID_MODE",
  "INVALID_SPEED",
  "REDUCED_MOTION",
  "ESCAPE",
  "DRAWER_OPENED",
  "ROUTE_CHANGED",
  "VISIBILITY_LOST",
  "RUNTIME_ERROR",
  "DISPOSED",
] as const;

export type ExplorationModeReason =
  (typeof EXPLORATION_MODE_REASONS)[number];

export type ExplorationModeState = "ACTIVE" | "DISPOSED";

export type ExplorationModeSnapshot = Readonly<{
  profile: typeof EXPLORATION_MODE_PROFILE;
  state: ExplorationModeState;
  mode: ExplorationMode;
  traversalSpeed: number;
  prefersReducedMotion: boolean;
  reason: ExplorationModeReason;
  escapeHintVisible: boolean;
}>;

export type ExplorationModeInterrupt =
  | "ESCAPE"
  | "DRAWER_OPENED"
  | "ROUTE_CHANGED"
  | "VISIBILITY_LOST"
  | "RUNTIME_ERROR";

export type ExplorationModeListener = (
  snapshot: ExplorationModeSnapshot,
) => void;

export type ExplorationModeController = Readonly<{
  getSnapshot: () => ExplorationModeSnapshot;
  selectMode: (
    mode: unknown,
    reason?: "USER_SELECTED" | "SHORTCUT_SELECTED",
  ) => ExplorationModeSnapshot;
  setTraversalSpeed: (speed: unknown) => ExplorationModeSnapshot;
  setReducedMotion: (value: boolean) => ExplorationModeSnapshot;
  interrupt: (reason: ExplorationModeInterrupt) => ExplorationModeSnapshot;
  subscribe: (listener: ExplorationModeListener) => () => void;
  dispose: () => ExplorationModeSnapshot;
}>;

export type ExplorationShortcutInput = Readonly<{
  key: string;
  targetKind: "TEXT_ENTRY" | "OTHER";
  ctrlKey?: boolean;
  altKey?: boolean;
  metaKey?: boolean;
  shiftKey?: boolean;
}>;

export type ExplorationModeControlOptions = Readonly<{
  prefersReducedMotion?: boolean;
  initialMode?: ExplorationMode;
  initialTraversalSpeed?: number;
  onChange?: ExplorationModeListener;
}>;

export type ExplorationModeControl = Readonly<{
  controller: ExplorationModeController;
  destroy: () => void;
}>;

const MODE_SET = new Set<string>(EXPLORATION_MODES);
const MIN_TRAVERSAL_SPEED = 0.25;
const MAX_TRAVERSAL_SPEED = 2;
const TRAVERSAL_SPEED_STEP = 0.25;
const DEFAULT_TRAVERSAL_SPEED = 1;

function isExplorationMode(value: unknown): value is ExplorationMode {
  return typeof value === "string" && MODE_SET.has(value);
}

function isTraversalSpeed(value: unknown): value is number {
  if (typeof value !== "number" || !Number.isFinite(value)) return false;
  if (value < MIN_TRAVERSAL_SPEED || value > MAX_TRAVERSAL_SPEED) {
    return false;
  }
  const steps = (value - MIN_TRAVERSAL_SPEED) / TRAVERSAL_SPEED_STEP;
  return Math.abs(steps - Math.round(steps)) < Number.EPSILON * 16;
}

function freezeSnapshot(
  state: ExplorationModeState,
  mode: ExplorationMode,
  traversalSpeed: number,
  prefersReducedMotion: boolean,
  reason: ExplorationModeReason,
): ExplorationModeSnapshot {
  return Object.freeze({
    profile: EXPLORATION_MODE_PROFILE,
    state,
    mode,
    traversalSpeed,
    prefersReducedMotion,
    reason,
    escapeHintVisible: state === "ACTIVE" && mode === "TRAVERSE",
  });
}

/**
 * Resolve discoverable single-key shortcuts without activating inside text
 * entry or while a browser/system modifier is held.
 */
export function resolveExplorationShortcut(
  input: ExplorationShortcutInput,
): ExplorationMode | null {
  if (
    input.targetKind === "TEXT_ENTRY" ||
    input.ctrlKey === true ||
    input.altKey === true ||
    input.metaKey === true ||
    input.shiftKey === true
  ) {
    return null;
  }

  switch (input.key.toLowerCase()) {
    case "o":
      return "ORIENT";
    case "i":
      return "INSPECT";
    case "t":
      return "TRAVERSE";
    case "s":
      return "STORY";
    default:
      return null;
  }
}

export function createExplorationModeController(
  options: ExplorationModeControlOptions = {},
): ExplorationModeController {
  const listeners = new Set<ExplorationModeListener>();
  let disposed = false;
  let prefersReducedMotion = options.prefersReducedMotion ?? false;
  let traversalSpeed = isTraversalSpeed(options.initialTraversalSpeed)
    ? options.initialTraversalSpeed
    : DEFAULT_TRAVERSAL_SPEED;
  const requestedInitialMode = options.initialMode ?? "ORIENT";
  let mode: ExplorationMode =
    prefersReducedMotion && requestedInitialMode === "TRAVERSE"
      ? "ORIENT"
      : requestedInitialMode;
  let snapshot = freezeSnapshot(
    "ACTIVE",
    mode,
    traversalSpeed,
    prefersReducedMotion,
    prefersReducedMotion && requestedInitialMode === "TRAVERSE"
      ? "REDUCED_MOTION"
      : "INITIALIZED",
  );

  const publish = (reason: ExplorationModeReason): ExplorationModeSnapshot => {
    snapshot = freezeSnapshot(
      disposed ? "DISPOSED" : "ACTIVE",
      mode,
      traversalSpeed,
      prefersReducedMotion,
      reason,
    );
    if (!disposed) {
      for (const listener of listeners) listener(snapshot);
    }
    return snapshot;
  };

  const selectMode = (
    value: unknown,
    reason: "USER_SELECTED" | "SHORTCUT_SELECTED" = "USER_SELECTED",
  ): ExplorationModeSnapshot => {
    if (disposed) return snapshot;
    if (!isExplorationMode(value)) return publish("INVALID_MODE");
    if (value === "TRAVERSE" && prefersReducedMotion) {
      mode = "ORIENT";
      return publish("REDUCED_MOTION");
    }
    mode = value;
    return publish(reason);
  };

  const setTraversalSpeed = (value: unknown): ExplorationModeSnapshot => {
    if (disposed) return snapshot;
    if (!isTraversalSpeed(value)) return publish("INVALID_SPEED");
    traversalSpeed = value;
    return publish("SPEED_CHANGED");
  };

  const setReducedMotion = (value: boolean): ExplorationModeSnapshot => {
    if (disposed) return snapshot;
    prefersReducedMotion = value;
    if (prefersReducedMotion && mode === "TRAVERSE") {
      mode = "ORIENT";
      return publish("REDUCED_MOTION");
    }
    return publish("USER_SELECTED");
  };

  const interrupt = (
    reason: ExplorationModeInterrupt,
  ): ExplorationModeSnapshot => {
    if (disposed) return snapshot;
    mode = "ORIENT";
    return publish(reason);
  };

  const subscribe = (listener: ExplorationModeListener): (() => void) => {
    if (disposed) return () => undefined;
    listeners.add(listener);
    listener(snapshot);
    return () => listeners.delete(listener);
  };

  const dispose = (): ExplorationModeSnapshot => {
    if (disposed) return snapshot;
    disposed = true;
    mode = "ORIENT";
    listeners.clear();
    snapshot = freezeSnapshot(
      "DISPOSED",
      mode,
      traversalSpeed,
      prefersReducedMotion,
      "DISPOSED",
    );
    return snapshot;
  };

  return Object.freeze({
    getSnapshot: () => snapshot,
    selectMode,
    setTraversalSpeed,
    setReducedMotion,
    interrupt,
    subscribe,
    dispose,
  });
}

function targetKind(target: EventTarget | null): "TEXT_ENTRY" | "OTHER" {
  if (!(target instanceof Element)) return "OTHER";
  const editable = target.closest(
    "input, textarea, select, [contenteditable='true'], [contenteditable='']",
  );
  return editable === null ? "OTHER" : "TEXT_ENTRY";
}

/** Mount an app-local, renderer-neutral exploration mode controller. */
export function mountExplorationModeControl(
  host: HTMLElement,
  options: ExplorationModeControlOptions = {},
): ExplorationModeControl {
  const document = host.ownerDocument;
  const controller = createExplorationModeController(options);
  const region = document.createElement("section");
  const heading = document.createElement("h3");
  const modeControls = document.createElement("div");
  const status = document.createElement("p");
  const speedLabel = document.createElement("label");
  const speed = document.createElement("input");
  const escapeHint = document.createElement("p");
  const buttons = new Map<ExplorationMode, HTMLButtonElement>();

  region.dataset.component = "exploration-mode-control";
  region.setAttribute("aria-labelledby", "exploration-mode-control-title");
  heading.id = "exploration-mode-control-title";
  heading.textContent = "Exploration mode";
  modeControls.setAttribute("aria-label", "Explorer interaction modes");
  status.setAttribute("role", "status");
  status.setAttribute("aria-live", "polite");
  speed.type = "range";
  speed.min = String(MIN_TRAVERSAL_SPEED);
  speed.max = String(MAX_TRAVERSAL_SPEED);
  speed.step = String(TRAVERSAL_SPEED_STEP);
  speedLabel.textContent = "Traverse speed";
  speedLabel.append(speed);
  escapeHint.textContent = "Esc — leave Traverse mode";
  escapeHint.dataset.component = "traverse-escape-hint";

  for (const modeName of EXPLORATION_MODES) {
    const button = document.createElement("button");
    button.type = "button";
    buttton.textContent = modeName[0] + modeName.slice(1).toLowerCase();
    button.dataset.explorationMode = modeName;
    button.addEventListener("click", () => {
      controller.selectMode(modeName);
    });
    buttons.set(modeName, button);
    modeControls.append(button);
  }

  const render = (next: ExplorationModeSnapshot): void => {
    region.dataset.mode = next.mode;
    region.dataset.state = next.state;
    for (const [modeName, button] of buttons) {
      button.setAttribute("aria-pressed", String(modeName === next.mode));
      button.disabled = next.state === "DISPOSED";
    }
    speed.value = String(next.traversalSpeed);
    speed.disabled = next.state === "DISPOSED";
    escapeHint.hidden = !next.escapeHintVisible;
    status.textContent = `${next.mode} / ${next.reason}`;
    options.onChange?.(next);
  };

  const unsubscribe = controller.subscribe(render);
  const onSpeed = (): void => {
    controller.setTraversalSpeed(Number(speed.value));
  };
  const onKeyDown = (event: KeyboardEvent): void => {
    if (event.key === "Escape") {
      if (controller.getSnapshot().mode !== "ORIENT") {
        event.preventDefault();
        controller.interrupt("ESCAPE");
      }
      return;
    }
    const shortcut = resolveExplorationShortcut({
      key: event.key,
      targetKind: targetKind(event.target),
      ctrlKey: event.ctrlKey,
      altKey: event.altKey,
      metaKey: event.metaKey,
      shiftKey: event.shiftKey,
    });
    if (shortcut === null) return;
    event.preventDefault();
    controller.selectMode(shortcut, "SHORTCUT_SELECTED");
  };

  speed.addEventListener("input", onSpeed);
  document.addEventListener("keydown", onKeyDown);
  region.replaceChildren(
    heading,
    modeControls,
    status,
    speedLabel,
    escapeHint,
  );
  host.replaceChildren(region);

  const destroy = (): void => {
    unsubscribe();
    speed.removeEventListener("input", onSpeed);
    document.removeEventListener("keydown", onKeyDown);
    controller.dispose();
    host.replaceChildren();
  };

  return Object.freeze({ controller, destroy });
}
