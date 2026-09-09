import type { MapRuntimePort } from "@kfm/maplibre";
import { createViteMapLibreAdapter } from "@kfm/maplibre/vite-adapter";
import {
  ATLAS_VIEWS,
  EVIDENCE_RECORDS,
  LAYER_RECORDS,
  SOURCE_DESCRIPTORS,
  TEMPORAL_EXTENTS,
  createInitialSnapshot,
  createLivingAtlasStyle,
  evaluateFocusSelection,
  findAtlasView,
  findEvidenceForLayer,
  findLayerRecord,
  findSourceDescriptor,
  findTemporalExtent,
  type MapRepresentation,
  type MapSnapshot,
  type ReportDraft,
  type StoryScene,
} from "../features/living_atlas";

export type LivingAtlasController = Readonly<{ destroy: () => void }>;

const DISPLAY_TIMES = TEMPORAL_EXTENTS.filter(
  (entry) => entry.kind === "INTERVAL",
);

function el<K extends keyof HTMLElementTagNameMap>(
  document: Document,
  tag: K,
  className?: string,
): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className) node.className = className;
  return node;
}

function text<K extends keyof HTMLElementTagNameMap>(
  document: Document,
  tag: K,
  value: string,
  className?: string,
): HTMLElementTagNameMap[K] {
  const node = el(document, tag, className);
  node.textContent = value;
  return node;
}

function button(
  document: Document,
  label: string,
  action: string,
  className?: string,
): HTMLButtonElement {
  const node = el(document, "button", className);
  node.type = "button";
  node.textContent = label;
  node.dataset.atlasAction = action;
  return node;
}

function cloneSnapshot(
  snapshot: MapSnapshot,
  changes: Partial<MapSnapshot>,
): MapSnapshot {
  return Object.freeze({
    ...snapshot,
    ...changes,
    capturedAt: new Date().toISOString(),
  });
}

function createId(prefix: string): string {
  return `${prefix}:${Date.now().toString(36)}`;
}

function readDrafts<T>(key: string): readonly T[] {
  try {
    const value = window.localStorage.getItem(key);
    return value === null ? [] : (JSON.parse(value) as readonly T[]);
  } catch {
    return [];
  }
}

function writeDrafts<T>(key: string, drafts: readonly T[]): void {
  try {
    window.localStorage.setItem(key, JSON.stringify(drafts));
  } catch {
    // Draft persistence is optional; the in-memory draft remains available.
  }
}

export function mountLivingAtlasWorkspace(
  host: HTMLElement,
): LivingAtlasController {
  const document = host.ownerDocument;
  const cleanup: Array<() => void> = [];
  let snapshot = createInitialSnapshot();
  let previewTimeId = snapshot.committedTimeId;
  let runtime: MapRuntimePort | null = null;
  let reports = [...readDrafts<ReportDraft>("kfm.explorer.report-drafts.v1")];
  let stories = [...readDrafts<StoryScene>("kfm.explorer.story-scenes.v1")];

  const workspace = el(document, "div", "living-atlas");
  workspace.dataset.component = "living-atlas-workspace";
  const topbar = el(document, "div", "atlas-topbar");
  const identity = el(document, "div", "atlas-identity");
  identity.append(
    text(document, "p", "Kansas-first · evidence-first", "eyebrow"),
    text(document, "h1", "Kansas Living Atlas"),
  );
  const modeNav = el(document, "nav", "atlas-mode-nav");
  modeNav.setAttribute("aria-label", "Living Atlas work modes");
  ["Map", "Reports", "Stories"].forEach((label) => {
    const node = button(document, label, `mode:${label.toLowerCase()}`);
    node.setAttribute("aria-pressed", String(label === "Map"));
    modeNav.append(node);
  });
  const search = el(document, "input", "atlas-search");
  search.type = "search";
  search.placeholder = "Search views or layers";
  search.setAttribute("aria-label", "Search Living Atlas views and layers");
  topbar.append(identity, modeNav, search, button(document, "New from map", "composer:open", "atlas-primary-action"));

  const mapMode = el(document, "div", "atlas-mode-panel atlas-mode-panel--map");
  mapMode.dataset.atlasMode = "map";
  const leftRail = el(document, "aside", "atlas-left-rail");
  leftRail.setAttribute("aria-label", "Atlas catalog");
  const railTabs = el(document, "div", "atlas-rail-tabs");
  ["Views", "Layers", "Places", "Sources"].forEach((label) => {
    const node = button(document, label, `rail:${label.toLowerCase()}`);
    node.setAttribute("aria-pressed", String(label === "Views"));
    railTabs.append(node);
  });
  const railPanels = el(document, "div", "atlas-rail-panels");

  const viewsPanel = el(document, "div", "atlas-rail-panel");
  viewsPanel.dataset.railPanel = "views";
  viewsPanel.append(text(document, "h2", "18 default views"));
  const viewList = el(document, "div", "atlas-view-list");
  ATLAS_VIEWS.forEach((view) => {
    const node = button(document, view.name, `view:${view.id}`, "atlas-view-button");
    node.dataset.searchText = `${view.name} ${view.question}`.toLowerCase();
    node.dataset.status = view.status;
    node.setAttribute("aria-pressed", String(view.id === snapshot.activeViewId));
    node.append(text(document, "small", view.status === "SITE_LOCAL_DEMO" ? "Bounded demo" : "Data hold"));
    viewList.append(node);
  });
  viewsPanel.append(viewList);

  const layersPanel = el(document, "div", "atlas-rail-panel");
  layersPanel.dataset.railPanel = "layers";
  layersPanel.hidden = true;
  layersPanel.append(text(document, "h2", "Layer catalog"));
  const layerList = el(document, "div", "atlas-layer-list");
  LAYER_RECORDS.forEach((record) => {
    const state = snapshot.layers.find((entry) => entry.id === record.id)!;
    const row = el(document, "article", "atlas-layer-row");
    row.dataset.searchText = `${record.name} ${record.domain}`.toLowerCase();
    const toggle = el(document, "input");
    toggle.type = "checkbox";
    toggle.checked = state.visible;
    toggle.disabled = record.availability !== "AVAILABLE";
    toggle.dataset.layerToggle = record.id;
    toggle.setAttribute("aria-label", `Show ${record.name}`);
    const copy = el(document, "div");
    copy.append(text(document, "strong", record.name), text(document, "small", `${record.domain} · ${record.trustState}`));
    const inspect = button(document, "Inspect", `inspect:${record.id}`);
    row.append(toggle, copy, inspect);
    layerList.append(row);
  });
  layersPanel.append(layerList);

  const placesPanel = el(document, "div", "atlas-rail-panel");
  placesPanel.dataset.railPanel = "places";
  placesPanel.hidden = true;
  placesPanel.append(
    text(document, "h2", "Places"),
    text(document, "p", "Statewide generalized fixture extent"),
    text(document, "p", "County locator samples are synthetic and intentionally unnamed.", "atlas-muted"),
  );

  const sourcesPanel = el(document, "div", "atlas-rail-panel");
  sourcesPanel.dataset.railPanel = "sources";
  sourcesPanel.hidden = true;
  sourcesPanel.append(
    text(document, "h2", "Source Observatory"),
    text(document, "p", "Candidates are visible without being silently admitted.", "atlas-muted"),
  );
  SOURCE_DESCRIPTORS.forEach((source) => {
    const card = el(document, "article", "atlas-source-card");
    card.dataset.searchText = `${source.title} ${source.organization} ${source.domain}`.toLowerCase();
    card.append(
      text(document, "strong", source.title),
      text(document, "small", `${source.admissionState} · ${source.organization}`),
      text(document, "p", source.nextGate),
    );
    if (source.officialUrl !== null) {
      const link = el(document, "a");
      link.href = source.officialUrl;
      link.target = "_blank";
      link.rel = "noreferrer";
      link.textContent = "Official source context";
      card.append(link);
    }
    sourcesPanel.append(card);
  });
  railPanels.append(viewsPanel, layersPanel, placesPanel, sourcesPanel);
  leftRail.append(railTabs, railPanels);

  const mapStage = el(document, "section", "atlas-map-stage");
  mapStage.setAttribute("aria-label", "Interactive Living Atlas map");
  const representationBar = el(document, "div", "atlas-representation-bar");
  const representationLabels: Readonly<Record<MapRepresentation, string>> = {
    "2D": "2D",
    TERRAIN_3D: "Terrain 3D",
    GLOBE: "Globe",
    COMPARE: "Compare",
  };
  (Object.keys(representationLabels) as MapRepresentation[]).forEach((value) => {
    const node = button(document, representationLabels[value], `representation:${value}`);
    node.setAttribute("aria-pressed", String(value === snapshot.representation));
    representationBar.append(node);
  });
  const mapCanvas = el(document, "div", "atlas-map-canvas");
  mapCanvas.id = "kfm-living-atlas-map";
  const mapNotice = el(document, "div", "atlas-map-notice");
  const runtimeState = text(document, "p", "Map runtime initializing…", "atlas-runtime-state");
  runtimeState.setAttribute("role", "status");
  runtimeState.setAttribute("aria-live", "polite");
  mapNotice.append(
    text(document, "strong", "Generalized synthetic geometry"),
    text(document, "span", "No external tiles, live observations, legal boundaries, or precise sensitive locations."),
    runtimeState,
  );
  mapStage.append(representationBar, mapCanvas, mapNotice);

  const evidence = el(document, "aside", "atlas-evidence-drawer");
  evidence.setAttribute("aria-label", "Evidence Drawer");
  const renderEvidence = (layerId: string | null): void => {
    if (layerId === null) {
      evidence.replaceChildren(
        text(document, "p", "Evidence Drawer", "eyebrow"),
        text(document, "h2", "Inspect before interpretation"),
        text(document, "p", "Choose Inspect on a layer. Rendered pixels and properties never become evidence authority."),
      );
      return;
    }
    const record = findLayerRecord(layerId);
    const claim = findEvidenceForLayer(layerId);
    const source = record ? findSourceDescriptor(record.sourceId) : null;
    if (!record || !claim || !source) {
      renderEvidence(null);
      return;
    }
    const policy = evaluateFocusSelection(layerId);
    evidence.replaceChildren(
      text(document, "p", "Evidence Drawer", "eyebrow"),
      text(document, "h2", record.name),
      text(document, "p", `${policy.outcome} · ${policy.reasonCode}`, `atlas-outcome atlas-outcome--${policy.outcome.toLowerCase()}`),
      text(document, "p", claim.supports),
      text(document, "h3", "Cannot prove"),
      text(document, "p", claim.cannotProve),
      text(document, "h3", "Source and time"),
      text(document, "p", `${source.title} · ${source.admissionState} · ${claim.temporalScope}`),
      text(document, "h3", "Evidence references"),
      text(document, "p", claim.evidenceRefs.length > 0 ? claim.evidenceRefs.join(", ") : "None eligible"),
      button(document, "Ask Focus for bounded next steps", "focus:run", "atlas-primary-action"),
      button(document, "Exercise deterministic error", "focus:error"),
    );
  };
  renderEvidence(null);

  const timeline = el(document, "div", "atlas-timeline");
  const timelineCopy = el(document, "div");
  const timeLabel = text(document, "strong", findTemporalExtent(previewTimeId)?.label ?? "Unknown time");
  const timeDetail = text(document, "small", "Preview only — select Apply time to commit");
  timelineCopy.append(text(document, "span", "Deep-time navigator", "eyebrow"), timeLabel, timeDetail);
  const timeInput = el(document, "input");
  timeInput.type = "range";
  timeInput.min = "0";
  timeInput.max = String(DISPLAY_TIMES.length - 1);
  timeInput.value = String(DISPLAY_TIMES.findIndex((entry) => entry.id === previewTimeId));
  timeInput.setAttribute("aria-label", "Preview atlas time");
  const applyTime = button(document, "Apply time", "time:commit", "atlas-primary-action");
  timeline.append(timelineCopy, timeInput, applyTime);

  mapMode.append(leftRail, mapStage, evidence, timeline);

  const reportsMode = el(document, "section", "atlas-mode-panel atlas-draft-workspace");
  reportsMode.dataset.atlasMode = "reports";
  reportsMode.hidden = true;
  const storiesMode = el(document, "section", "atlas-mode-panel atlas-draft-workspace");
  storiesMode.dataset.atlasMode = "stories";
  storiesMode.hidden = true;

  const renderReports = (): void => {
    reportsMode.replaceChildren(
      text(document, "p", "Draft workspace", "eyebrow"),
      text(document, "h2", "Reports from map state"),
      text(document, "p", "Drafts preserve camera, committed time, layer state, and eligible evidence references. No publish action exists."),
      button(document, "New report from map", "create:report", "atlas-primary-action"),
    );
    const list = el(document, "div", "atlas-draft-list");
    reports.forEach((draft) => {
      const card = el(document, "article", "atlas-draft-card");
      card.append(
        text(document, "strong", draft.title),
        text(document, "small", `DRAFT · ${draft.snapshot.activeViewId} · ${draft.snapshot.committedTimeId}`),
        text(document, "p", draft.sections.limitations),
        button(document, "Export JSON", `export:report:${draft.id}`),
      );
      list.append(card);
    });
    reportsMode.append(list);
  };

  const seedTrustStory = (): readonly StoryScene[] => {
    const scenes = [
      ["A bounded claim", "Available site-local evidence supports interaction only."],
      ["Correction stays attached", "A correction chain must travel with any later released evidence."],
      ["Historical stays historical", "Changing time never silently turns a dated source into present truth."],
      ["Protected detail fails closed", "Restricted cultural and ecological locations remain undisclosed."],
    ] as const;
    return scenes.map(([title, narrative], index) => Object.freeze({
      profile: "kfm.explorer.story-scene.v1" as const,
      id: createId(`story-${index + 1}`),
      title,
      narrative,
      order: index + 1,
      snapshot,
      evidenceRefs: snapshot.evidenceRefs,
      caveats: Object.freeze(["Synthetic draft scene; not released or published."]),
      motion: "NONE" as const,
      lifecycle: "DRAFT" as const,
    }));
  };

  const renderStories = (): void => {
    storiesMode.replaceChildren(
      text(document, "p", "Draft workspace", "eyebrow"),
      text(document, "h2", "Story Atlas"),
      text(document, "p", "Scenes are replayable map snapshots with evidence references and caveats. Motion is off by default."),
      button(document, "Create “Trust in the map”", "create:trust-story", "atlas-primary-action"),
    );
    const list = el(document, "div", "atlas-draft-list");
    stories.forEach((scene) => {
      const card = el(document, "article", "atlas-draft-card");
      card.append(
        text(document, "strong", `${scene.order}. ${scene.title}`),
        text(document, "small", `DRAFT · ${scene.motion}`),
        text(document, "p", scene.narrative),
      );
      list.append(card);
    });
    storiesMode.append(list);
  };
  renderReports();
  renderStories();

  const composer = el(document, "aside", "atlas-composer");
  composer.hidden = true;
  composer.setAttribute("aria-label", "Create from current map state");
  composer.append(
    text(document, "p", "New from map", "eyebrow"),
    text(document, "h2", "Capture an inspectable draft"),
    text(document, "p", "The draft records only the committed timeline state; preview changes are excluded."),
    button(document, "Create report draft", "create:report", "atlas-primary-action"),
    button(document, "Create story scene", "create:story"),
    button(document, "Close", "composer:close"),
  );

  workspace.append(topbar, mapMode, reportsMode, storiesMode, composer);
  host.replaceChildren(workspace);

  const refreshLayerControls = (): void => {
    layerList.querySelectorAll<HTMLInputElement>("[data-layer-toggle]").forEach((control) => {
      control.checked = snapshot.layers.find((entry) => entry.id === control.dataset.layerToggle)?.visible ?? false;
    });
  };

  const initializeRuntime = (): void => {
    runtime?.dispose();
    mapCanvas.replaceChildren();
    runtimeState.textContent = "Map runtime initializing…";
    runtime = createViteMapLibreAdapter({
      containerId: mapCanvas.id,
      interactive: true,
      style: createLivingAtlasStyle(snapshot.representation, snapshot.layers),
      initializationDeadlineMs: 8_000,
    });
    cleanup.push(runtime.subscribeSnapshot((state) => {
      runtimeState.textContent = `Renderer ${state.state}${state.reason === null ? "" : ` · ${state.reason}`}`;
      if (state.state === "READY") {
        snapshot = cloneSnapshot(snapshot, { camera: state.camera });
      }
    }));
    void runtime.initialize(snapshot.camera).catch(() => {
      runtimeState.textContent = "Renderer ERROR · no factual fallback";
    });
  };

  const activateView = (viewId: string): void => {
    const view = findAtlasView(viewId);
    if (view === null) return;
    if (view.status === "DESIGN_DATA_HOLD") {
      runtimeState.textContent = `HELD · ${view.statusReason}`;
      renderEvidence(view.layerIds[0] ?? null);
      return;
    }
    const requestedRepresentation = view.representation;
    const usableRepresentation: MapRepresentation =
      requestedRepresentation === "GLOBE" ? "GLOBE" : "2D";
    snapshot = cloneSnapshot(snapshot, {
      activeViewId: view.id,
      representation: usableRepresentation,
      camera: view.camera,
      committedTimeId: view.temporalExtentId,
      layers: Object.freeze(snapshot.layers.map((state) => Object.freeze({
        ...state,
        visible: view.layerIds.includes(state.id) && findLayerRecord(state.id)?.availability === "AVAILABLE",
      }))),
      selectedLayerId: null,
      evidenceRefs: Object.freeze([]),
    });
    previewTimeId = view.temporalExtentId;
    timeInput.value = String(Math.max(0, DISPLAY_TIMES.findIndex((entry) => entry.id === previewTimeId)));
    timeLabel.textContent = findTemporalExtent(previewTimeId)?.label ?? "Unknown time";
    viewList.querySelectorAll<HTMLButtonElement>("button").forEach((node) => node.setAttribute("aria-pressed", String(node.dataset.atlasAction === `view:${view.id}`)));
    representationBar.querySelectorAll<HTMLButtonElement>("button").forEach((node) => node.setAttribute("aria-pressed", String(node.dataset.atlasAction === `representation:${usableRepresentation}`)));
    refreshLayerControls();
    renderEvidence(null);
    initializeRuntime();
    if (requestedRepresentation !== usableRepresentation) {
      runtimeState.textContent = `${requestedRepresentation} composition held · inspectable layers loaded in 2D`;
    }
  };

  const createReport = (): void => {
    const activeView = findAtlasView(snapshot.activeViewId);
    const draft: ReportDraft = Object.freeze({
      profile: "kfm.explorer.report-draft.v1",
      id: createId("report"),
      title: `${activeView?.name ?? "Kansas Atlas"} evidence note`,
      researchQuestion: activeView?.question ?? "What does the current map state support?",
      createdAt: new Date().toISOString(),
      snapshot,
      includedEvidenceRefs: snapshot.evidenceRefs,
      sections: Object.freeze({
        summary: "Draft generated from an inspectable map state.",
        observations: "Only visible, committed, public-safe demonstration state is included.",
        findings: "No Kansas factual finding is asserted by this fixture.",
        limitations: "Synthetic/generalized geometry; external data and publication remain held.",
        openQuestions: "Which exact source artifact, policy, review, and release should be admitted next?",
      }),
      lifecycle: "DRAFT",
      publishable: false,
    });
    reports = [draft, ...reports];
    writeDrafts("kfm.explorer.report-drafts.v1", reports);
    renderReports();
    composer.hidden = true;
    activateMode("reports");
  };

  const createStory = (): void => {
    const scene: StoryScene = Object.freeze({
      profile: "kfm.explorer.story-scene.v1",
      id: createId("story"),
      title: `Scene from ${findAtlasView(snapshot.activeViewId)?.name ?? "map"}`,
      narrative: "A draft scene captured from the current committed map state.",
      order: stories.length + 1,
      snapshot,
      evidenceRefs: snapshot.evidenceRefs,
      caveats: Object.freeze(["Draft only; synthetic/generalized context is not a factual claim."]),
      motion: "NONE",
      lifecycle: "DRAFT",
    });
    stories = [...stories, scene];
    writeDrafts("kfm.explorer.story-scenes.v1", stories);
    renderStories();
    composer.hidden = true;
    activateMode("stories");
  };

  const activateMode = (mode: string): void => {
    workspace.querySelectorAll<HTMLElement>("[data-atlas-mode]").forEach((panel) => {
      panel.hidden = panel.dataset.atlasMode !== mode;
    });
    modeNav.querySelectorAll<HTMLButtonElement>("button").forEach((node) => node.setAttribute("aria-pressed", String(node.dataset.atlasAction === `mode:${mode}`)));
  };

  const exportReport = (id: string): void => {
    const draft = reports.find((entry) => entry.id === id);
    if (!draft) return;
    const url = URL.createObjectURL(new Blob([JSON.stringify(draft, null, 2)], { type: "application/json" }));
    const link = el(document, "a");
    link.href = url;
    link.download = `${id.replaceAll(":", "-")}.json`;
    link.click();
    URL.revokeObjectURL(url);
  };

  const handleClick = (event: Event): void => {
    const target = (event.target as Element | null)?.closest<HTMLButtonElement>("[data-atlas-action]");
    if (!target) return;
    const action = target.dataset.atlasAction ?? "";
    if (action.startsWith("mode:")) activateMode(action.slice(5));
    else if (action.startsWith("rail:")) {
      const panel = action.slice(5);
      railPanels.querySelectorAll<HTMLElement>("[data-rail-panel]").forEach((node) => { node.hidden = node.dataset.railPanel !== panel; });
      railTabs.querySelectorAll<HTMLButtonElement>("button").forEach((node) => node.setAttribute("aria-pressed", String(node === target)));
    } else if (action.startsWith("view:")) activateView(action.slice(5));
    else if (action.startsWith("inspect:")) {
      const layerId = action.slice(8);
      const claim = findEvidenceForLayer(layerId);
      snapshot = cloneSnapshot(snapshot, { selectedLayerId: layerId, evidenceRefs: claim?.evidenceRefs ?? Object.freeze([]) });
      renderEvidence(layerId);
    } else if (action.startsWith("representation:")) {
      const requested = action.slice(15) as MapRepresentation;
      if (requested === "TERRAIN_3D" || requested === "COMPARE") {
        runtimeState.textContent = `${representationLabels[requested]} HELD · required admitted data/composition is unavailable`;
      } else {
        snapshot = cloneSnapshot(snapshot, { representation: requested });
        representationBar.querySelectorAll<HTMLButtonElement>("button").forEach((node) => node.setAttribute("aria-pressed", String(node === target)));
        initializeRuntime();
      }
    } else if (action === "time:commit") {
      snapshot = cloneSnapshot(snapshot, { committedTimeId: previewTimeId });
      timeDetail.textContent = `Committed to map snapshot · ${new Date().toLocaleTimeString()}`;
    } else if (action === "composer:open") composer.hidden = false;
    else if (action === "composer:close") composer.hidden = true;
    else if (action === "create:report") createReport();
    else if (action === "create:story") createStory();
    else if (action === "create:trust-story") {
      stories = [...stories, ...seedTrustStory()];
      writeDrafts("kfm.explorer.story-scenes.v1", stories);
      renderStories();
    } else if (action === "focus:run" || action === "focus:error") {
      const decision = evaluateFocusSelection(snapshot.selectedLayerId, action === "focus:error");
      const result = text(document, "p", `${decision.outcome} · ${decision.summary}`, `atlas-focus-result atlas-outcome--${decision.outcome.toLowerCase()}`);
      result.setAttribute("role", "status");
      evidence.append(result);
    } else if (action.startsWith("export:report:")) exportReport(action.slice("export:report:".length));
  };

  const handleChange = (event: Event): void => {
    const control = event.target as HTMLInputElement;
    const layerId = control.dataset.layerToggle;
    if (!layerId) return;
    snapshot = cloneSnapshot(snapshot, { layers: Object.freeze(snapshot.layers.map((state) => state.id === layerId ? Object.freeze({ ...state, visible: control.checked }) : state)) });
    initializeRuntime();
  };

  const handleTimePreview = (): void => {
    const time = DISPLAY_TIMES[Number(timeInput.value)];
    if (!time) return;
    previewTimeId = time.id;
    timeLabel.textContent = time.label;
    timeDetail.textContent = `${time.startLabel} → ${time.endLabel} · preview only`;
  };

  const handleSearch = (): void => {
    const query = search.value.trim().toLowerCase();
    workspace.querySelectorAll<HTMLElement>("[data-search-text]").forEach((node) => {
      node.hidden = query.length > 0 && !(node.dataset.searchText ?? "").includes(query);
    });
  };

  const handleKeydown = (event: KeyboardEvent): void => {
    if (event.key === "Escape" && !composer.hidden) composer.hidden = true;
  };

  workspace.addEventListener("click", handleClick);
  workspace.addEventListener("change", handleChange);
  timeInput.addEventListener("input", handleTimePreview);
  search.addEventListener("input", handleSearch);
  document.addEventListener("keydown", handleKeydown);
  cleanup.push(
    () => workspace.removeEventListener("click", handleClick),
    () => workspace.removeEventListener("change", handleChange),
    () => timeInput.removeEventListener("input", handleTimePreview),
    () => search.removeEventListener("input", handleSearch),
    () => document.removeEventListener("keydown", handleKeydown),
  );

  initializeRuntime();

  return Object.freeze({
    destroy: () => {
      cleanup.forEach((fn) => fn());
      runtime?.dispose();
      runtime = null;
      host.replaceChildren();
    },
  });
}
