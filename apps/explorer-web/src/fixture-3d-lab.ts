import "./site/fixture-3d-lab.css";

import {
  SYNTHETIC_3D_FIXTURE_FEATURES,
  createViteSynthetic3dFixtureLab,
  type Synthetic3dFixtureLabController,
  type Synthetic3dFixtureProjection,
  type Synthetic3dFixtureSelection,
  type Synthetic3dFixtureSkyPreset,
  type Synthetic3dFixtureSnapshot,
} from "@kfm/maplibre/vite-adapter";

const LAB_ID = "kfm-synthetic-maplibre-3d-lab";
const MAP_CONTAINER_ID = "kfm-synthetic-maplibre-3d-root";
const SELECTION_EVENT = "kfm:synthetic-3d-selection";

type NumericControl = Readonly<{
  id: "pitch" | "bearing" | "zoom" | "verticalScale" | "fieldOfView" | "lightAzimuth";
  label: string;
  minimum: number;
  maximum: number;
  step: number;
  suffix: string;
  initial: number;
  apply: (controller: Synthetic3dFixtureLabController, value: number) => Synthetic3dFixtureSnapshot;
  read: (snapshot: Synthetic3dFixtureSnapshot) => number;
}>;

const NUMERIC_CONTROLS: readonly NumericControl[] = Object.freeze([
  Object.freeze({
    id: "pitch",
    label: "Camera pitch",
    minimum: 0,
    maximum: 80,
    step: 1,
    suffix: "°",
    initial: 54,
    apply: (controller: Synthetic3dFixtureLabController, value: number) => controller.setPitch(value),
    read: (snapshot: Synthetic3dFixtureSnapshot) => snapshot.camera.pitch,
  }),
  Object.freeze({
    id: "bearing",
    label: "Camera bearing",
    minimum: -180,
    maximum: 180,
    step: 1,
    suffix: "°",
    initial: -18,
    apply: (controller: Synthetic3dFixtureLabController, value: number) => controller.setBearing(value),
    read: (snapshot: Synthetic3dFixtureSnapshot) => snapshot.camera.bearing,
  }),
  Object.freeze({
    id: "zoom",
    label: "Zoom",
    minimum: 3,
    maximum: 10,
    step: 0.1,
    suffix: "",
    initial: 5.2,
    apply: (controller: Synthetic3dFixtureLabController, value: number) => controller.setZoom(value),
    read: (snapshot: Synthetic3dFixtureSnapshot) => snapshot.camera.zoom,
  }),
  Object.freeze({
    id: "verticalScale",
    label: "Synthetic vertical scale",
    minimum: 0.25,
    maximum: 3,
    step: 0.05,
    suffix: "×",
    initial: 1,
    apply: (controller: Synthetic3dFixtureLabController, value: number) => controller.setVerticalScale(value),
    read: (snapshot: Synthetic3dFixtureSnapshot) => snapshot.verticalScale,
  }),
  Object.freeze({
    id: "fieldOfView",
    label: "Vertical field of view",
    minimum: 10,
    maximum: 75,
    step: 1,
    suffix: "°",
    initial: 36,
    apply: (controller: Synthetic3dFixtureLabController, value: number) => controller.setFieldOfView(value),
    read: (snapshot: Synthetic3dFixtureSnapshot) => snapshot.fieldOfView,
  }),
  Object.freeze({
    id: "lightAzimuth",
    label: "Light azimuth",
    minimum: 0,
    maximum: 360,
    step: 1,
    suffix: "°",
    initial: 210,
    apply: (controller: Synthetic3dFixtureLabController, value: number) => controller.setLightAzimuth(value),
    read: (snapshot: Synthetic3dFixtureSnapshot) => snapshot.lightAzimuth,
  }),
]);

function element<K extends keyof HTMLElementTagNameMap>(
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
  const node = element(document, tag, className);
  node.textContent = value;
  return node;
}

function button(
  document: Document,
  label: string,
  className?: string,
): HTMLButtonElement {
  const node = element(document, "button", className);
  node.type = "button";
  node.textContent = label;
  return node;
}

function formatNumber(value: number, step: number): string {
  if (Number.isInteger(step)) return Math.round(value).toString();
  return value.toFixed(step < 0.1 ? 2 : 1).replace(/\.0+$/, "");
}

function installSynthetic3dFixtureLab(root: HTMLElement): void {
  const document = root.ownerDocument;
  if (document.getElementById(LAB_ID)) return;

  const mapSection = root.querySelector<HTMLElement>("#map");
  if (mapSection === null) return;

  const details = element(document, "details", "synthetic-3d-lab card");
  details.id = LAB_ID;
  details.dataset.activation = "disabled";
  const summary = element(document, "summary", "synthetic-3d-lab__summary");
  summary.append(
    text(document, "span", "Optional MapLibre 3D fixture lab"),
    text(document, "span", "Disabled by default", "synthetic-3d-lab__summary-state"),
  );
  details.append(summary);

  const introduction = element(document, "div", "synthetic-3d-lab__intro");
  introduction.append(
    text(
      document,
      "p",
      "Branch-only 3D preparation",
      "eyebrow",
    ),
    text(
      document,
      "h3",
      "Globe, evidence towers, atmosphere, light, camera, and feature-state — without external data",
    ),
    text(
      document,
      "p",
      "This opt-in lab uses only inline generalized synthetic fixtures. Extrusion height is a visual index, not terrain or elevation evidence. It requests no style, tile, glyph, sprite, API, DEM, PMTiles, LiDAR, model, protected location, private-property detail, or live source.",
      "section-summary",
    ),
  );

  const activationRow = element(document, "div", "synthetic-3d-lab__activation");
  const activationButton = button(
    document,
    "Activate synthetic 3D lab",
    "button button--primary",
  );
  const status = text(
    document,
    "p",
    "Renderer is inactive. Opening this panel does not initialize MapLibre.",
    "synthetic-3d-lab__status",
  );
  status.setAttribute("role", "status");
  status.setAttribute("aria-live", "polite");
  activationRow.append(activationButton, status);

  const workspace = element(document, "div", "synthetic-3d-lab__workspace");
  const mapColumn = element(document, "div", "synthetic-3d-lab__map-column");
  const mapFrame = element(document, "div", "synthetic-3d-lab__map-frame");
  const mapContainer = element(document, "div", "synthetic-3d-lab__map");
  mapContainer.id = MAP_CONTAINER_ID;
  mapContainer.tabIndex = 0;
  mapContainer.setAttribute(
    "aria-label",
    "Synthetic MapLibre 3D map. Use Arrow Left and Right for bearing, Arrow Up and Down for pitch, Plus and Minus for zoom, G for projection, number keys for synthetic features, Home to reset, and Escape to clear selection.",
  );
  const placeholder = element(
    document,
    "div",
    "synthetic-3d-lab__placeholder",
  );
  placeholder.append(
    text(document, "strong", "3D renderer not started"),
    text(
      document,
      "span",
      "Activate explicitly to construct the inline-only MapLibre scene.",
    ),
  );
  mapFrame.append(mapContainer, placeholder);

  const keyboardHelp = text(
    document,
    "p",
    "Keyboard: ←/→ bearing · ↑/↓ pitch · +/− zoom · G globe/mercator · 1–5 select · Home reset · Esc clear",
    "synthetic-3d-lab__keyboard",
  );
  const snapshotOutput = text(
    document,
    "output",
    "INACTIVE · no renderer · no source request",
    "synthetic-3d-lab__snapshot",
  );
  snapshotOutput.setAttribute("for", MAP_CONTAINER_ID);
  mapColumn.append(mapFrame, keyboardHelp, snapshotOutput);

  const controls = element(document, "aside", "synthetic-3d-lab__controls");
  controls.setAttribute("aria-label", "Synthetic MapLibre 3D controls");
  const controlNodes: Array<
    HTMLButtonElement | HTMLInputElement | HTMLSelectElement
  > = [];
  const numericInputs = new Map<
    NumericControl["id"],
    Readonly<{ input: HTMLInputElement; output: HTMLOutputElement }>
  >();

  const projectionFieldset = element(
    document,
    "fieldset",
    "synthetic-3d-lab__control-group",
  );
  projectionFieldset.append(
    text(document, "legend", "Projection"),
  );
  const projectionButtons = new Map<
    Synthetic3dFixtureProjection,
    HTMLButtonElement
  >();
  (["globe", "mercator"] as const).forEach((projection) => {
    const node = button(
      document,
      projection === "globe" ? "Globe" : "Mercator",
      "synthetic-3d-lab__choice",
    );
    node.setAttribute("aria-pressed", String(projection === "globe"));
    projectionButtons.set(projection, node);
    controlNodes.push(node);
    projectionFieldset.append(node);
  });

  const sceneFieldset = element(
    document,
    "fieldset",
    "synthetic-3d-lab__control-group",
  );
  sceneFieldset.append(text(document, "legend", "Instant scene presets"));
  const scenePresets = [
    {
      id: "globe",
      label: "Globe evidence towers",
      apply: (controller: Synthetic3dFixtureLabController) => {
        controller.setProjection("globe");
        controller.setPitch(54);
        controller.setBearing(-18);
        controller.setZoom(5.2);
        controller.setSkyPreset("night");
        controller.setVerticalScale(1);
      },
    },
    {
      id: "mercator",
      label: "Mercator 3D",
      apply: (controller: Synthetic3dFixtureLabController) => {
        controller.setProjection("mercator");
        controller.setPitch(62);
        controller.setBearing(24);
        controller.setZoom(5.5);
        controller.setSkyPreset("dusk");
        controller.setVerticalScale(1.25);
      },
    },
    {
      id: "flat",
      label: "Flat comparison",
      apply: (controller: Synthetic3dFixtureLabController) => {
        controller.setProjection("mercator");
        controller.setPitch(0);
        controller.setBearing(0);
        controller.setZoom(5.2);
        controller.setSkyPreset("clear");
        controller.setVerticalScale(0.25);
      },
    },
  ] as const;
  scenePresets.forEach((preset) => {
    const node = button(
      document,
      preset.label,
      "synthetic-3d-lab__preset",
    );
    node.dataset.scenePreset = preset.id;
    controlNodes.push(node);
    sceneFieldset.append(node);
  });

  const numericFieldset = element(
    document,
    "fieldset",
    "synthetic-3d-lab__control-group synthetic-3d-lab__sliders",
  );
  numericFieldset.append(text(document, "legend", "Camera and scene"));
  NUMERIC_CONTROLS.forEach((definition) => {
    const row = element(document, "div", "synthetic-3d-lab__slider");
    const label = element(document, "label");
    const input = element(document, "input");
    const output = element(document, "output");
    input.type = "range";
    input.id = `kfm-synthetic-3d-${definition.id}`;
    input.min = String(definition.minimum);
    input.max = String(definition.maximum);
    input.step = String(definition.step);
    input.value = String(definition.initial);
    output.setAttribute("for", input.id);
    output.textContent = `${formatNumber(definition.initial, definition.step)}${definition.suffix}`;
    label.htmlFor = input.id;
    label.textContent = definition.label;
    row.append(label, input, output);
    numericFieldset.append(row);
    controlNodes.push(input);
    numericInputs.set(definition.id, Object.freeze({ input, output }));
  });

  const skyFieldset = element(
    document,
    "fieldset",
    "synthetic-3d-lab__control-group",
  );
  skyFieldset.append(text(document, "legend", "Atmosphere presentation"));
  const skyLabel = element(document, "label");
  skyLabel.htmlFor = "kfm-synthetic-3d-sky";
  skyLabel.textContent = "Sky preset";
  const skySelect = element(document, "select");
  skySelect.id = "kfm-synthetic-3d-sky";
  (["night", "dusk", "clear"] as const).forEach((preset) => {
    const option = element(document, "option");
    option.value = preset;
    option.textContent =
      preset === "night" ? "Night" : preset === "dusk" ? "Dusk" : "Clear";
    skySelect.append(option);
  });
  skyFieldset.append(skyLabel, skySelect);
  controlNodes.push(skySelect);

  const featureFieldset = element(
    document,
    "fieldset",
    "synthetic-3d-lab__control-group",
  );
  featureFieldset.append(text(document, "legend", "Synthetic feature-state"));
  const featureButtons = new Map<string, HTMLButtonElement>();
  SYNTHETIC_3D_FIXTURE_FEATURES.forEach((feature, index) => {
    const node = button(
      document,
      `${index + 1}. ${feature.title}`,
      "synthetic-3d-lab__feature",
    );
    node.dataset.synthetic3dFeature = feature.id;
    node.setAttribute("aria-pressed", "false");
    featureButtons.set(feature.id, node);
    controlNodes.push(node);
    featureFieldset.append(node);
  });

  const actionFieldset = element(
    document,
    "fieldset",
    "synthetic-3d-lab__control-group",
  );
  actionFieldset.append(text(document, "legend", "Scene actions"));
  const clearButton = button(
    document,
    "Clear feature-state selection",
    "synthetic-3d-lab__choice",
  );
  const resetButton = button(
    document,
    "Reset synthetic scene",
    "synthetic-3d-lab__choice",
  );
  controlNodes.push(clearButton, resetButton);
  actionFieldset.append(clearButton, resetButton);

  const evidencePanel = element(
    document,
    "section",
    "synthetic-3d-lab__evidence",
  );
  evidencePanel.setAttribute("aria-label", "Synthetic evidence-reference handoff");
  const evidenceTitle = text(
    document,
    "h4",
    "No synthetic feature selected",
  );
  evidenceTitle.tabIndex = -1;
  const evidenceSummary = text(
    document,
    "p",
    "A selection will emit one renderer-neutral KFM selection event with bounded evidence references.",
  );
  const evidenceRefs = element(document, "ul");
  evidencePanel.append(
    text(document, "p", "Evidence-reference handoff", "eyebrow"),
    evidenceTitle,
    evidenceSummary,
    evidenceRefs,
  );

  controls.append(
    projectionFieldset,
    sceneFieldset,
    numericFieldset,
    skyFieldset,
    featureFieldset,
    actionFieldset,
    evidencePanel,
  );
  workspace.append(mapColumn, controls);
  details.append(introduction, activationRow, workspace);
  mapSection.append(details);

  let controller: Synthetic3dFixtureLabController | null = null;
  let activationGeneration = 0;
  let activating = false;
  let latestSnapshot: Synthetic3dFixtureSnapshot | null = null;

  const setControlsEnabled = (enabled: boolean): void => {
    controlNodes.forEach((node) => {
      node.disabled = !enabled;
    });
    mapContainer.tabIndex = enabled ? 0 : -1;
  };
  setControlsEnabled(false);

  const renderSnapshot = (snapshot: Synthetic3dFixtureSnapshot): void => {
    latestSnapshot = snapshot;
    projectionButtons.forEach((node, projection) => {
      node.setAttribute(
        "aria-pressed",
        String(snapshot.projection === projection),
      );
    });
    NUMERIC_CONTROLS.forEach((definition) => {
      const nodes = numericInputs.get(definition.id);
      if (!nodes) return;
      const value = definition.read(snapshot);
      nodes.input.value = String(value);
      nodes.output.textContent = `${formatNumber(value, definition.step)}${definition.suffix}`;
    });
    skySelect.value = snapshot.skyPreset;
    featureButtons.forEach((node, featureId) => {
      node.setAttribute(
        "aria-pressed",
        String(snapshot.selectedFeatureId === featureId),
      );
    });
    snapshotOutput.textContent =
      `${snapshot.status} · ${snapshot.projection} · ` +
      `zoom ${snapshot.camera.zoom.toFixed(1)} · pitch ${Math.round(snapshot.camera.pitch)}° · ` +
      `bearing ${Math.round(snapshot.camera.bearing)}° · vertical ${snapshot.verticalScale.toFixed(2)}× · ` +
      `FOV ${Math.round(snapshot.fieldOfView)}° · ` +
      `${snapshot.selectedFeatureId ?? "no selection"}`;
  };

  const renderSelection = (
    value: Synthetic3dFixtureSelection,
  ): void => {
    evidenceTitle.textContent = value.feature.title;
    evidenceSummary.textContent = value.feature.summary;
    evidenceRefs.replaceChildren(
      ...[
        ...value.selection.evidenceRefs.map((reference) => ({
          label: "Current synthetic evidence",
          reference,
        })),
        ...(value.selection.historyEvidenceRefs ?? []).map((reference) => ({
          label: "History-only synthetic evidence",
          reference,
        })),
      ].map(({ label, reference }) => {
        const item = element(document, "li");
        item.append(
          text(document, "span", `${label}: `),
          text(document, "code", reference),
        );
        return item;
      }),
    );
    document.dispatchEvent(
      new CustomEvent<Synthetic3dFixtureSelection>(SELECTION_EVENT, {
        detail: value,
      }),
    );
  };

  const showInactive = (message: string): void => {
    details.dataset.activation = "disabled";
    placeholder.hidden = false;
    mapContainer.replaceChildren();
    activationButton.textContent = "Activate synthetic 3D lab";
    activationButton.disabled = false;
    status.textContent = message;
    snapshotOutput.textContent = "INACTIVE · no renderer · no source request";
    latestSnapshot = null;
    setControlsEnabled(false);
    featureButtons.forEach((node) => node.setAttribute("aria-pressed", "false"));
  };

  const deactivate = (): void => {
    activationGeneration += 1;
    activating = false;
    controller?.destroy();
    controller = null;
    showInactive(
      "Renderer deactivated and deterministically torn down. Inline fixture data remains local to the bundle.",
    );
  };

  const activate = async (): Promise<void> => {
    if (controller !== null || activating) {
      deactivate();
      return;
    }

    activating = true;
    const generation = ++activationGeneration;
    details.dataset.activation = "initializing";
    activationButton.disabled = true;
    activationButton.textContent = "Initializing…";
    status.textContent =
      "Checking WebGL2 and constructing the inline-only MapLibre scene.";
    placeholder.hidden = false;
    placeholder.querySelector("strong")!.textContent = "Initializing MapLibre";
    placeholder.querySelector("span")!.textContent =
      "No external style, tile, glyph, sprite, API, DEM, or archive request is permitted.";

    try {
      const next = await createViteSynthetic3dFixtureLab({
        containerId: MAP_CONTAINER_ID,
        initialProjection: "globe",
        initialSkyPreset: "night",
        initialVerticalScale: 1,
        initialFieldOfView: 36,
        initialLightAzimuth: 210,
        onSelection: renderSelection,
        onStatus: renderSnapshot,
      });
      if (generation !== activationGeneration) {
        next.destroy();
        return;
      }
      controller = next;
      activating = false;
      details.dataset.activation = "active";
      placeholder.hidden = true;
      activationButton.disabled = false;
      activationButton.textContent = "Deactivate and tear down";
      status.textContent =
        "Synthetic MapLibre 3D is active. All geometry and evidence references are inline fixture data.";
      setControlsEnabled(true);
      renderSnapshot(controller.getSnapshot());
      requestAnimationFrame(() => controller?.resize());
      mapContainer.focus();
    } catch (error) {
      if (generation !== activationGeneration) return;
      activating = false;
      controller = null;
      const message =
        error instanceof Error
          ? error.message
          : "Synthetic MapLibre 3D initialization failed.";
      showInactive(
        `Fail-closed fallback: ${message} The existing renderer-neutral Explorer remains available.`,
      );
    }
  };

  activationButton.addEventListener("click", () => {
    void activate();
  });

  projectionButtons.forEach((node, projection) => {
    node.addEventListener("click", () => {
      if (!controller) return;
      renderSnapshot(controller.setProjection(projection));
    });
  });

  scenePresets.forEach((preset) => {
    const node = sceneFieldset.querySelector<HTMLButtonElement>(
      `[data-scene-preset="${preset.id}"]`,
    );
    node?.addEventListener("click", () => {
      if (!controller) return;
      preset.apply(controller);
      renderSnapshot(controller.getSnapshot());
    });
  });

  NUMERIC_CONTROLS.forEach((definition) => {
    const nodes = numericInputs.get(definition.id);
    if (!nodes) return;
    nodes.input.addEventListener("input", () => {
      if (!controller) return;
      const value = Number(nodes.input.value);
      renderSnapshot(definition.apply(controller, value));
    });
  });

  skySelect.addEventListener("change", () => {
    if (!controller) return;
    renderSnapshot(
      controller.setSkyPreset(skySelect.value as Synthetic3dFixtureSkyPreset),
    );
  });

  featureButtons.forEach((node, featureId) => {
    node.addEventListener("click", () => {
      if (!controller) return;
      renderSnapshot(controller.selectFeature(featureId));
      evidenceTitle.focus();
    });
  });

  clearButton.addEventListener("click", () => {
    if (!controller) return;
    renderSnapshot(controller.clearSelection());
    evidenceTitle.textContent = "No synthetic feature selected";
    evidenceSummary.textContent =
      "A selection will emit one renderer-neutral KFM selection event with bounded evidence references.";
    evidenceRefs.replaceChildren();
  });

  resetButton.addEventListener("click", () => {
    if (!controller) return;
    renderSnapshot(controller.reset());
    evidenceTitle.textContent = "No synthetic feature selected";
    evidenceSummary.textContent =
      "The scene is reset. No selection or evidence reference was promoted.";
    evidenceRefs.replaceChildren();
  });

  mapContainer.addEventListener("keydown", (event) => {
    if (!controller || !latestSnapshot) return;
    const snapshot = latestSnapshot;
    let handled = true;
    switch (event.key) {
      case "ArrowLeft":
        renderSnapshot(controller.setBearing(snapshot.camera.bearing - 10));
        break;
      case "ArrowRight":
        renderSnapshot(controller.setBearing(snapshot.camera.bearing + 10));
        break;
      case "ArrowUp":
        renderSnapshot(controller.setPitch(Math.min(80, snapshot.camera.pitch + 5)));
        break;
      case "ArrowDown":
        renderSnapshot(controller.setPitch(Math.max(0, snapshot.camera.pitch - 5)));
        break;
      case "+":
      case "=":
        renderSnapshot(controller.setZoom(Math.min(10, snapshot.camera.zoom + 0.5)));
        break;
      case "-":
      case "_":
        renderSnapshot(controller.setZoom(Math.max(3, snapshot.camera.zoom - 0.5)));
        break;
      case "g":
      case "G":
        renderSnapshot(
          controller.setProjection(
            snapshot.projection === "globe" ? "mercator" : "globe",
          ),
        );
        break;
      case "Home":
        renderSnapshot(controller.reset());
        break;
      case "Escape":
        renderSnapshot(controller.clearSelection());
        evidenceTitle.textContent = "No synthetic feature selected";
        evidenceRefs.replaceChildren();
        break;
      default: {
        const index = Number(event.key) - 1;
        const feature = SYNTHETIC_3D_FIXTURE_FEATURES[index];
        if (Number.isInteger(index) && feature) {
          renderSnapshot(controller.selectFeature(feature.id));
        } else {
          handled = false;
        }
      }
    }
    if (handled) event.preventDefault();
  });

  details.addEventListener("toggle", () => {
    if (details.open && controller) {
      requestAnimationFrame(() => controller?.resize());
    }
  });

  const pageHide = (): void => deactivate();
  window.addEventListener("pagehide", pageHide, { once: true });



  document.documentElement.dataset.kfmSynthetic3dLab = "available";
}

function boot(): void {
  const root = document.querySelector<HTMLElement>("#root");
  if (root === null) return;
  installSynthetic3dFixtureLab(root);
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", boot, { once: true });
} else {
  boot();
}
