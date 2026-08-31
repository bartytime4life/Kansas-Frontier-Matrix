import {
  createNullMapRuntime,
  type InlineGeoJsonMapRuntimePort,
  type MapRuntimeSnapshot,
} from "@kfm/maplibre";
import {
  parseGovernedLayerSlice,
  type GovernedLayerProjection,
  type GovernedTransport,
} from "../adapters/GovernedClient";
import {
  mountEvidenceDrawer,
  type EvidenceDrawerController,
} from "../features/evidence_drawer";
import {
  bindGovernedMapRuntimeEvidence,
  type MapRuntimeEvidenceBinding,
  type MapRuntimeEvidenceUpdate,
} from "../features/map_runtime/runtime-evidence-binding";
import {
  mountMapRuntimeTrustStatus,
  type MapRuntimeTrustStatusController,
} from "../features/map_runtime/runtime-trust-status";

export type ExplorerMapRuntimeFactory = (
  options: Readonly<{ containerId: string; interactive: boolean }>,
) => InlineGeoJsonMapRuntimePort;

export type GovernedMapWorkspaceDependencies = Readonly<{
  transport: GovernedTransport;
  createMapRuntime: ExplorerMapRuntimeFactory;
  runtimeInitializationDeadlineMs?: number;
}>;

export type GovernedMapWorkspaceController = Readonly<{
  start: () => Promise<void>;
  destroy: () => void;
}>;

let mapContainerOrdinal = 0;
export const DEFAULT_EXPLORER_RUNTIME_INITIALIZATION_DEADLINE_MS = 15_000;
const MAX_EXPLORER_RUNTIME_INITIALIZATION_DEADLINE_MS = 60_000;

type RuntimeInitializationAttempt = Readonly<{
  promise: Promise<MapRuntimeSnapshot>;
  cancel: () => void;
}>;

function beginRuntimeInitialization(
  candidate: InlineGeoJsonMapRuntimePort,
  deadlineMs: number,
): RuntimeInitializationAttempt {
  let settled = false;
  let deadline: ReturnType<typeof setTimeout> | null = null;
  let resolveAttempt!: (snapshot: MapRuntimeSnapshot) => void;
  let rejectAttempt!: (error: Error) => void;
  const promise = new Promise<MapRuntimeSnapshot>((resolve, reject) => {
    resolveAttempt = resolve;
    rejectAttempt = reject;
  });
  const clearDeadline = (): void => {
    if (deadline === null) return;
    clearTimeout(deadline);
    deadline = null;
  };
  const fail = (): void => {
    if (settled) return;
    settled = true;
    clearDeadline();
    rejectAttempt(new Error("Map runtime initialization did not settle."));
  };
  const succeed = (snapshot: MapRuntimeSnapshot): void => {
    if (settled) return;
    settled = true;
    clearDeadline();
    resolveAttempt(snapshot);
  };

  deadline = setTimeout(fail, deadlineMs);
  try {
    candidate.initialize().then(succeed, fail);
  } catch {
    fail();
  }
  return Object.freeze({ promise, cancel: fail });
}

function createElement<K extends keyof HTMLElementTagNameMap>(
  document: Document,
  tag: K,
  className?: string,
): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className) node.className = className;
  return node;
}

function createText<K extends keyof HTMLElementTagNameMap>(
  document: Document,
  tag: K,
  value: string,
  className?: string,
): HTMLElementTagNameMap[K] {
  const node = createElement(document, tag, className);
  node.textContent = value;
  return node;
}

function createChip(document: Document, value: string, tone = "neutral"): HTMLElement {
  return createText(document, "span", value, `chip chip--${tone}`);
}

/**
 * Mount the canonical exact-one governed map slice.
 *
 * Renderer construction, governed transport, and evidence resolution remain
 * injected and separately bounded. A renderer failure swaps once to the Null
 * port so the accessible feature list keeps the same governed selection path.
 */
export function mountGovernedMapWorkspace(
  host: HTMLElement,
  dependencies: GovernedMapWorkspaceDependencies,
): GovernedMapWorkspaceController {
  if (
    typeof dependencies.createMapRuntime !== "function" ||
    typeof dependencies.transport?.loadLayers !== "function" ||
    typeof dependencies.transport?.loadEvidence !== "function" ||
    typeof dependencies.transport?.close !== "function"
  ) {
    throw new TypeError("Governed map workspace dependencies are invalid.");
  }
  const runtimeInitializationDeadlineMs =
    dependencies.runtimeInitializationDeadlineMs ??
    DEFAULT_EXPLORER_RUNTIME_INITIALIZATION_DEADLINE_MS;
  if (
    !Number.isSafeInteger(runtimeInitializationDeadlineMs) ||
    runtimeInitializationDeadlineMs < 1 ||
    runtimeInitializationDeadlineMs >
      MAX_EXPLORER_RUNTIME_INITIALIZATION_DEADLINE_MS
  ) {
    throw new TypeError("Governed map runtime initialization deadline is invalid.");
  }

  const document = host.ownerDocument;
  const region = createElement(document, "div", "governed-map-workspace");
  const mapColumn = createElement(document, "div", "governed-map-column card");
  const toolbar = createElement(document, "div", "map-toolbar");
  const mapContainer = createElement(document, "div", "governed-map-canvas");
  const rendererNotice = createText(document, "p", "", "renderer-notice");
  const side = createElement(document, "aside", "runtime-card card");
  const runtimeStatusHost = createElement(document, "div", "runtime-status-host");
  const layerStatus = createText(document, "p", "Loading governed map layer…", "governed-layer-status");
  const evidenceStatus = createText(document, "p", "ABSTAIN / SELECTION_REQUIRED", "governed-evidence-status");
  const featureList = createElement(document, "ul", "accessible-feature-list");
  const drawerHost = createElement(document, "div", "governed-evidence-drawer-host");
  const mapContainerId = `explorer-governed-map-${++mapContainerOrdinal}`;

  mapContainer.id = mapContainerId;
  mapContainer.setAttribute("role", "region");
  mapContainer.setAttribute("aria-label", "Governed synthetic streamflow map");
  rendererNotice.setAttribute("role", "status");
  rendererNotice.setAttribute("aria-live", "polite");
  rendererNotice.dataset.component = "governed-map-renderer-status";
  rendererNotice.dataset.renderer = "STARTING";
  rendererNotice.textContent = "Starting the package-owned map renderer…";
  layerStatus.setAttribute("role", "status");
  layerStatus.setAttribute("aria-live", "polite");
  layerStatus.dataset.component = "governed-layer-status";
  layerStatus.dataset.outcome = "PENDING";
  evidenceStatus.setAttribute("role", "status");
  evidenceStatus.setAttribute("aria-live", "polite");
  evidenceStatus.tabIndex = -1;
  evidenceStatus.dataset.component = "governed-evidence-status";
  evidenceStatus.dataset.outcome = "ABSTAIN";
  runtimeStatusHost.dataset.component = "explorer-map-runtime-status-host";
  featureList.setAttribute("aria-label", "Governed map features");

  toolbar.append(
    createChip(document, "Governed API", "positive"),
    createChip(document, "MapLibre adapter", "positive"),
    createChip(document, "Broader readiness: HOLD", "critical"),
  );
  mapColumn.append(toolbar, mapContainer, rendererNotice);
  side.append(
    createText(document, "p", "Evidence-preserving map", "eyebrow"),
    createText(document, "h3", "One governed layer, two equivalent selection paths"),
    createText(
      document,
      "p",
      "Select the rendered point or use the keyboard-operable feature list. Both paths reuse the same governed layer, feature, selection, and evidence identities.",
    ),
    layerStatus,
    createText(document, "h4", "Accessible map features"),
    featureList,
    evidenceStatus,
    drawerHost,
    runtimeStatusHost,
    createText(
      document,
      "p",
      "This bounded synthetic slice does not establish broader MapLibre readiness, source admission, release, deployment, or publication authority.",
      "guardrail",
    ),
  );
  region.replaceChildren(mapColumn, side);
  host.replaceChildren(region);

  let destroyed = false;
  let started = false;
  let generation = 0;
  let fallbackActivated = false;
  let runtime: InlineGeoJsonMapRuntimePort | null = null;
  let boundRuntime: InlineGeoJsonMapRuntimePort | null = null;
  let layer: GovernedLayerProjection | null = null;
  let featureButton: HTMLButtonElement | null = null;
  let runtimeStatus: MapRuntimeTrustStatusController | null = null;
  let evidenceBinding: MapRuntimeEvidenceBinding | null = null;
  let drawer: EvidenceDrawerController | null = null;
  let removeFeatureButtonListener = (): void => undefined;
  let unsubscribeRuntimeFailure = (): void => undefined;
  let unsubscribePendingSelection = (): void => undefined;
  let cancelRuntimeInitialization = (): void => undefined;

  function setLayerStatus(outcome: "ANSWER" | "ERROR", status: string): void {
    layerStatus.textContent = status;
    layerStatus.dataset.outcome = outcome;
    layerStatus.setAttribute("role", outcome === "ERROR" ? "alert" : "status");
    layerStatus.setAttribute(
      "aria-live",
      outcome === "ERROR" ? "assertive" : "polite",
    );
  }

  function setEvidenceStatus(
    outcome: "PENDING" | "ANSWER" | "ABSTAIN" | "DENY" | "ERROR",
    status: string,
    code?: string,
  ): void {
    evidenceStatus.textContent = status;
    evidenceStatus.dataset.outcome = outcome;
    if (code === undefined) delete evidenceStatus.dataset.code;
    else evidenceStatus.dataset.code = code;
    const assertive = outcome === "DENY" || outcome === "ERROR";
    evidenceStatus.setAttribute("role", assertive ? "alert" : "status");
    evidenceStatus.setAttribute(
      "aria-live",
      assertive ? "assertive" : "polite",
    );
  }

  function clearDrawer(
    outcome: "ABSTAIN" | "ERROR",
    status: string,
    focusStatus: boolean,
  ): void {
    drawer?.close();
    drawer?.destroy();
    drawer = null;
    drawerHost.replaceChildren();
    setEvidenceStatus(outcome, status);
    if (focusStatus && evidenceStatus.isConnected) evidenceStatus.focus();
  }

  function consumeEvidence(update: MapRuntimeEvidenceUpdate): void {
    if (destroyed) return;
    if (update.kind === "RUNTIME_INVALIDATED") {
      clearDrawer(
        "ABSTAIN",
        `ABSTAIN / SELECTION_INVALIDATED (${update.runtimeReason ?? update.runtimeState})`,
        true,
      );
      return;
    }

    drawer?.close();
    drawer?.destroy();
    drawer = mountEvidenceDrawer(
      drawerHost,
      update.resolution.evidence.drawerInput,
    );
    const resolved = update.resolution.evidence;
    setEvidenceStatus(
      resolved.drawer.outcome,
      `${resolved.drawer.outcome} / ${resolved.code}`,
      resolved.code,
    );
    drawer.open();
  }

  function detachRuntime(dispose: boolean): void {
    cancelRuntimeInitialization();
    cancelRuntimeInitialization = (): void => undefined;
    if (featureButton !== null) featureButton.disabled = true;
    evidenceBinding?.destroy();
    evidenceBinding = null;
    unsubscribePendingSelection();
    unsubscribePendingSelection = (): void => undefined;
    unsubscribeRuntimeFailure();
    unsubscribeRuntimeFailure = (): void => undefined;
    runtimeStatus?.destroy();
    runtimeStatus = null;
    boundRuntime = null;

    const previous = runtime;
    runtime = null;
    if (previous !== null && dispose) {
      if (layer !== null && previous.getSnapshot().state === "READY") {
        try {
          previous.removeSource(layer.runtimeLayer.sourceId);
        } catch {
          // Teardown remains finite even if the renderer already dropped it.
        }
      }
      previous.dispose();
    }
  }

  function bindLayerIfReady(current: InlineGeoJsonMapRuntimePort): void {
    if (
      destroyed ||
      runtime !== current ||
      layer === null ||
      boundRuntime === current ||
      current.getSnapshot().state !== "READY"
    ) {
      return;
    }

    try {
      current.bindInlineGeoJsonLayer(layer.runtimeLayer);
    } catch {
      if (runtime !== current) return;
      if (!fallbackActivated) {
        void activateFallback("The map renderer could not bind the governed layer.");
      } else {
        rendererNotice.dataset.renderer = "ERROR";
        rendererNotice.setAttribute("role", "alert");
        rendererNotice.setAttribute("aria-live", "assertive");
        rendererNotice.textContent =
          "The map renderer and its dependency-free fallback could not bind the governed layer.";
        setLayerStatus("ERROR", "ERROR / LAYER_BIND_FAILED");
      }
      return;
    }

    boundRuntime = current;
    unsubscribePendingSelection = current.subscribeSelection(() => {
      if (destroyed || runtime !== current) return;
      drawer?.close();
      drawer?.destroy();
      drawer = null;
      drawerHost.replaceChildren();
      setEvidenceStatus("PENDING", "Resolving governed evidence…");
    });
    evidenceBinding = bindGovernedMapRuntimeEvidence(
      current,
      (selection) => dependencies.transport.loadEvidence(selection),
      consumeEvidence,
    );
    if (featureButton !== null) featureButton.disabled = false;
  }

  async function activateRuntime(
    candidate: InlineGeoJsonMapRuntimePort,
    mode: "MAPLIBRE" | "NULL_FALLBACK",
  ): Promise<void> {
    const currentGeneration = ++generation;
    detachRuntime(true);
    if (destroyed) {
      candidate.dispose();
      return;
    }
    runtime = candidate;
    runtimeStatus = mountMapRuntimeTrustStatus(runtimeStatusHost, candidate);
    unsubscribeRuntimeFailure = candidate.subscribeSnapshot(
      (snapshot: MapRuntimeSnapshot) => {
        if (
          destroyed ||
          runtime !== candidate ||
          mode !== "MAPLIBRE" ||
          snapshot.state !== "ERROR"
        ) {
          return;
        }
        clearDrawer("ERROR", "ERROR / RENDERER_FAILED", true);
        void activateFallback("The map renderer failed after initialization.");
      },
    );

    const initialization = beginRuntimeInitialization(
      candidate,
      runtimeInitializationDeadlineMs,
    );
    if (
      !destroyed &&
      generation === currentGeneration &&
      runtime === candidate
    ) {
      cancelRuntimeInitialization = initialization.cancel;
    } else {
      initialization.cancel();
    }

    try {
      await initialization.promise;
    } catch {
      if (
        !destroyed &&
        generation === currentGeneration &&
        runtime === candidate &&
        mode === "MAPLIBRE"
      ) {
        await activateFallback("The map renderer could not initialize.");
      }
      return;
    } finally {
      if (cancelRuntimeInitialization === initialization.cancel) {
        cancelRuntimeInitialization = (): void => undefined;
      }
    }
    if (
      destroyed ||
      generation !== currentGeneration ||
      runtime !== candidate
    ) {
      return;
    }

    rendererNotice.dataset.renderer = mode;
    rendererNotice.setAttribute("role", "status");
    rendererNotice.setAttribute("aria-live", "polite");
    rendererNotice.textContent =
      mode === "MAPLIBRE"
        ? "The package-owned MapLibre renderer is ready for the governed synthetic layer."
        : "Renderer failure contained: the dependency-free fallback keeps the accessible evidence path available.";
    bindLayerIfReady(candidate);
  }

  async function activateFallback(reason: string): Promise<void> {
    if (destroyed || fallbackActivated) return;
    fallbackActivated = true;
    rendererNotice.dataset.renderer = "NULL_FALLBACK";
    rendererNotice.textContent = `${reason} Activating the dependency-free fallback.`;
    await activateRuntime(createNullMapRuntime(), "NULL_FALLBACK");
  }

  function renderLayerProjection(projection: GovernedLayerProjection): void {
    layer = projection;
    setLayerStatus("ANSWER", `ANSWER / SUPPORTED — ${projection.title}`);
    const item = createElement(document, "li");
    const button = createElement(document, "button");
    const description = createText(document, "p", projection.description);
    button.type = "button";
    button.disabled = true;
    button.textContent = `Select ${projection.title}`;
    button.dataset.layerId = projection.runtimeLayer.layerId;
    button.dataset.featureId = projection.runtimeLayer.selection.featureId;
    const select = (): void => {
      if (destroyed || runtime === null) return;
      try {
        runtime.selectFeature(
          projection.runtimeLayer.layerId,
          projection.runtimeLayer.selection.featureId,
        );
      } catch {
        clearDrawer("ERROR", "ERROR / SELECTION_UNAVAILABLE", true);
      }
    };
    button.addEventListener("click", select);
    removeFeatureButtonListener();
    removeFeatureButtonListener = () => button.removeEventListener("click", select);
    featureButton = button;
    item.append(button, description);
    featureList.replaceChildren(item);
    if (runtime !== null) bindLayerIfReady(runtime);
  }

  async function loadLayer(): Promise<void> {
    try {
      const result = parseGovernedLayerSlice(
        await dependencies.transport.loadLayers(),
      );
      if (destroyed) return;
      if (!result.ok) {
        setLayerStatus("ERROR", "ERROR / INVALID_GOVERNED_LAYER_PAYLOAD");
        featureList.replaceChildren(
          createText(document, "li", "No governed map feature is available."),
        );
        return;
      }
      if (result.payload.outcome === "ERROR") {
        setLayerStatus("ERROR", `ERROR / ${result.payload.reasonCode}`);
        featureList.replaceChildren(
          createText(document, "li", "No governed map feature is available."),
        );
        return;
      }
      renderLayerProjection(result.payload.layers[0]);
    } catch {
      if (destroyed) return;
      setLayerStatus("ERROR", "ERROR / GOVERNED_LAYER_TRANSPORT_FAILED");
      featureList.replaceChildren(
        createText(document, "li", "No governed map feature is available."),
      );
    }
  }

  async function start(): Promise<void> {
    if (started || destroyed) return;
    started = true;
    const layerRequest = loadLayer();
    try {
      const candidate = dependencies.createMapRuntime({
        containerId: mapContainerId,
        interactive: true,
      });
      await Promise.all([layerRequest, activateRuntime(candidate, "MAPLIBRE")]);
    } catch {
      await Promise.all([
        layerRequest,
        activateFallback("The map renderer could not be constructed."),
      ]);
    }
  }

  function destroy(): void {
    if (destroyed) return;
    destroyed = true;
    generation += 1;
    drawer?.close();
    drawer?.destroy();
    drawer = null;
    try {
      dependencies.transport.close();
    } catch {
      // An injected transport cannot interrupt local listener/runtime/DOM cleanup.
    }
    detachRuntime(true);
    removeFeatureButtonListener();
    removeFeatureButtonListener = (): void => undefined;
    featureButton = null;
    host.replaceChildren();
  }

  return Object.freeze({ start, destroy });
}
