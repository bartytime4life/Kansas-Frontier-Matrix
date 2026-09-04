import {
  SYNTHETIC_3D_FIXTURE_FEATURES,
  createViteSynthetic3DFixtureLab,
  type Synthetic3DFixtureCamera,
  type Synthetic3DFixtureLabController,
  type Synthetic3DFixtureLabSnapshot,
  type Synthetic3DFixtureSelection,
} from "@kfm/maplibre/vite-adapter";

import "./styles.css";

const MAP_CONTAINER_ID = "kfm-maplibre-3d-fixture-map";

export type MountedMapLibre3DFixtureLab = Readonly<{
  destroy: () => void;
}>;

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

function badge(document: Document, value: string): HTMLElement {
  return text(document, "span", value, "maplibre-3d-fixture__badge");
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

function setControlsDisabled(
  controls: readonly (HTMLButtonElement | HTMLInputElement)[],
  disabled: boolean,
): void {
  for (const control of controls) control.disabled = disabled;
}

function cameraFromControls(
  pitch: HTMLInputElement,
  bearing: HTMLInputElement,
  fieldOfView: HTMLInputElement,
): Synthetic3DFixtureCamera {
  return Object.freeze({
    pitch: Number(pitch.value),
    bearing: Number(bearing.value),
    verticalFieldOfView: Number(fieldOfView.value),
  });
}

function updateCameraReadout(
  output: HTMLElement,
  camera: Synthetic3DFixtureCamera,
): void {
  output.textContent = `Pitch ${camera.pitch.toFixed(0)}° · bearing ${camera.bearing.toFixed(0)}° · vertical field of view ${camera.verticalFieldOfView.toFixed(0)}°`;
}

function describeSelection(
  selectionHost: HTMLElement,
  selection: Synthetic3DFixtureSelection,
): void {
  const document = selectionHost.ownerDocument;
  selectionHost.replaceChildren(
    text(document, "p", selection.label, "maplibre-3d-fixture__selection-title"),
    text(
      document,
      "p",
      `EvidenceRef handoff: ${selection.evidenceRef}`,
      "maplibre-3d-fixture__evidence-ref",
    ),
    text(
      document,
      "p",
      "Synthetic fixture only. The EvidenceRef is a test handoff and does not identify released evidence or establish a public claim.",
      "maplibre-3d-fixture__limitation",
    ),
  );
}

function reasonMessage(snapshot: Synthetic3DFixtureLabSnapshot): string {
  if (snapshot.state === "READY") {
    return "READY — inline synthetic MapLibre rendering is active. No source, release, or publication state changed.";
  }
  if (snapshot.state === "ERROR") {
    return `ERROR / ${snapshot.reason ?? "RUNTIME_ERROR"} — the lab failed closed and exposed no substitute claim.`;
  }
  if (snapshot.state === "DISPOSED") {
    return "DISPOSED — renderer listeners and WebGL resources were released.";
  }
  return `${snapshot.state} — waiting for the finite renderer outcome.`;
}

export async function mountMapLibre3DFixtureLab(
  host: HTMLElement,
): Promise<MountedMapLibre3DFixtureLab> {
  const document = host.ownerDocument;
  const cleanup: Array<() => void> = [];
  let destroyed = false;
  let renderer: Synthetic3DFixtureLabController | null = null;

  host.className = "maplibre-3d-fixture";
  host.dataset.component = "maplibre-3d-fixture-lab";

  const heading = text(
    document,
    "h3",
    "Synthetic MapLibre 3D fixture lab",
    "maplibre-3d-fixture__title",
  );
  heading.id = "maplibre-3d-fixture-title";

  const status = text(
    document,
    "p",
    "INITIALIZING — acquiring the package-owned renderer through the Vite adapter seam.",
    "maplibre-3d-fixture__status",
  );
  status.setAttribute("role", "status");
  status.setAttribute("aria-live", "polite");
  status.dataset.state = "INITIALIZING";

  const mapContainer = element(
    document,
    "div",
    "maplibre-3d-fixture__map",
  );
  mapContainer.id = MAP_CONTAINER_ID;

  const projectionGroup = element(
    document,
    "div",
    "maplibre-3d-fixture__button-group",
  );
  projectionGroup.setAttribute("role", "group");
  projectionGroup.setAttribute("aria-label", "Projection");
  const mercatorButton = button(document, "Mercator");
  const globeButton = button(document, "Globe");
  mercatorButton.setAttribute("aria-pressed", "true");
  globeButton.setAttribute("aria-pressed", "false");
  projectionGroup.append(mercatorButton, globeButton);

  const cameraFieldset = element(
    document,
    "fieldset",
    "maplibre-3d-fixture__camera",
  );
  cameraFieldset.append(
    text(document, "legend", "Camera controls"),
  );

  const pitch = element(document, "input");
  pitch.type = "range";
  pitch.min = "0";
  pitch.max = "60";
  pitch.step = "1";
  pitch.value = "52";
  pitch.id = "maplibre-3d-fixture-pitch";
  const pitchLabel = element(document, "label");
  pitchLabel.htmlFor = pitch.id;
  pitchLabel.append(
    text(document, "span", "Pitch"),
    pitch,
  );

  const bearing = element(document, "input");
  bearing.type = "range";
  bearing.min = "-180";
  bearing.max = "180";
  bearing.step = "1";
  bearing.value = "-18";
  bearing.id = "maplibre-3d-fixture-bearing";
  const bearingLabel = element(document, "label");
  bearingLabel.htmlFor = bearing.id;
  bearingLabel.append(
    text(document, "span", "Bearing"),
    bearing,
  );

  const fieldOfView = element(document, "input");
  fieldOfView.type = "range";
  fieldOfView.min = "20";
  fieldOfView.max = "80";
  fieldOfView.step = "1";
  fieldOfView.value = "37";
  fieldOfView.id = "maplibre-3d-fixture-field-of-view";
  const fieldOfViewLabel = element(document, "label");
  fieldOfViewLabel.htmlFor = fieldOfView.id;
  fieldOfViewLabel.append(
    text(document, "span", "Vertical field of view"),
    fieldOfView,
  );

  const cameraReadout = text(
    document,
    "p",
    "",
    "maplibre-3d-fixture__camera-readout",
  );
  cameraReadout.setAttribute("aria-live", "polite");
  updateCameraReadout(
    cameraReadout,
    cameraFromControls(pitch, bearing, fieldOfView),
  );
  cameraFieldset.append(
    pitchLabel,
    bearingLabel,
    fieldOfViewLabel,
    cameraReadout,
  );

  const selectionGroup = element(
    document,
    "div",
    "maplibre-3d-fixture__selection-controls",
  );
  selectionGroup.setAttribute("role", "group");
  selectionGroup.setAttribute(
    "aria-label",
    "Keyboard-accessible synthetic feature selection",
  );
  selectionGroup.append(
    text(
      document,
      "p",
      "Select a synthetic prism without using the map canvas:",
      "maplibre-3d-fixture__control-label",
    ),
  );

  const selectionHost = element(
    document,
    "aside",
    "maplibre-3d-fixture__selection",
  );
  selectionHost.setAttribute("aria-label", "Synthetic evidence handoff");
  selectionHost.setAttribute("aria-live", "polite");
  selectionHost.append(
    text(
      document,
      "p",
      "No synthetic feature selected.",
      "maplibre-3d-fixture__limitation",
    ),
  );

  const featureButtons = SYNTHETIC_3D_FIXTURE_FEATURES.map((feature) => {
    const control = button(document, feature.label);
    control.dataset.featureId = feature.featureId;
    control.setAttribute("aria-pressed", "false");
    selectionGroup.append(control);
    return control;
  });

  const controls = [
    mercatorButton,
    globeButton,
    pitch,
    bearing,
    fieldOfView,
    ...featureButtons,
  ] as const;
  setControlsDisabled(controls, true);

  const badges = element(document, "div", "maplibre-3d-fixture__badges");
  badges.append(
    badge(document, "BRANCH-ONLY"),
    badge(document, "DISABLED BY DEFAULT"),
    badge(document, "INLINE SYNTHETIC GEOMETRY"),
    badge(document, "NO EXTERNAL MAP REQUESTS"),
  );

  const controlsPanel = element(
    document,
    "div",
    "maplibre-3d-fixture__controls",
  );
  controlsPanel.append(
    projectionGroup,
    cameraFieldset,
    selectionGroup,
    selectionHost,
  );

  const layout = element(document, "div", "maplibre-3d-fixture__layout");
  layout.append(mapContainer, controlsPanel);

  host.append(
    text(document, "p", "Opt-in implementation proof", "eyebrow"),
    heading,
    text(
      document,
      "p",
      "A disabled-by-default, synthetic-only branch lab for globe projection, fill extrusion, camera controls, feature-state selection, and EvidenceRef handoff. It is not released data and is not a production-readiness claim.",
      "maplibre-3d-fixture__summary",
    ),
    badges,
    status,
    layout,
  );

  const updateStatus = (snapshot: Synthetic3DFixtureLabSnapshot): void => {
    status.textContent = reasonMessage(snapshot);
    status.dataset.state = snapshot.state;
    status.setAttribute(
      "role",
      snapshot.state === "ERROR" ? "alert" : "status",
    );
  };

  const handleSelection = (selection: Synthetic3DFixtureSelection): void => {
    describeSelection(selectionHost, selection);
    for (const control of featureButtons) {
      control.setAttribute(
        "aria-pressed",
        String(control.dataset.featureId === selection.featureId),
      );
    }
  };

  try {
    renderer = await createViteSynthetic3DFixtureLab({
      containerId: MAP_CONTAINER_ID,
      interactive: true,
      onSelection: handleSelection,
    });

    const snapshot = await renderer.initialize();
    if (destroyed) {
      renderer.dispose();
      renderer = null;
      return Object.freeze({ destroy: () => undefined });
    }

    updateStatus(snapshot);
    updateCameraReadout(cameraReadout, snapshot.camera);
    setControlsDisabled(controls, false);

    const selectProjection = (projection: "mercator" | "globe"): void => {
      if (renderer === null) return;
      const next = renderer.setProjection(projection);
      mercatorButton.setAttribute(
        "aria-pressed",
        String(next.projection === "mercator"),
      );
      globeButton.setAttribute(
        "aria-pressed",
        String(next.projection === "globe"),
      );
      updateStatus(next);
    };
    const handleMercator = (): void => selectProjection("mercator");
    const handleGlobe = (): void => selectProjection("globe");
    mercatorButton.addEventListener("click", handleMercator);
    globeButton.addEventListener("click", handleGlobe);
    cleanup.push(
      () => mercatorButton.removeEventListener("click", handleMercator),
      () => globeButton.removeEventListener("click", handleGlobe),
    );

    const handleCameraInput = (): void => {
      if (renderer === null) return;
      const next = renderer.setCamera(
        cameraFromControls(pitch, bearing, fieldOfView),
      );
      updateCameraReadout(cameraReadout, next.camera);
      updateStatus(next);
    };
    for (const control of [pitch, bearing, fieldOfView]) {
      control.addEventListener("input", handleCameraInput);
      cleanup.push(() =>
        control.removeEventListener("input", handleCameraInput),
      );
    }

    for (const control of featureButtons) {
      const handleFeatureSelection = (): void => {
        const featureId = control.dataset.featureId;
        if (renderer === null || featureId === undefined) return;
        updateStatus(renderer.selectFeature(featureId));
      };
      control.addEventListener("click", handleFeatureSelection);
      cleanup.push(() =>
        control.removeEventListener("click", handleFeatureSelection),
      );
    }
  } catch (error) {
    const snapshot = renderer?.getSnapshot();
    status.textContent =
      snapshot === undefined
        ? "ERROR / INITIALIZATION_FAILED — the lab failed closed before renderer control was established."
        : reasonMessage(snapshot);
    status.dataset.state = "ERROR";
    status.setAttribute("role", "alert");
    setControlsDisabled(controls, true);
    mapContainer.replaceChildren(
      text(
        document,
        "p",
        "MapLibre is unavailable in this browser context. The synthetic evidence controls remain disabled.",
        "maplibre-3d-fixture__fallback",
      ),
    );
    if (error instanceof Error) {
      status.dataset.errorName = error.name;
    }
  }

  return Object.freeze({
    destroy: () => {
      if (destroyed) return;
      destroyed = true;
      for (const dispose of cleanup) dispose();
      cleanup.length = 0;
      renderer?.dispose();
      renderer = null;
      host.replaceChildren();
      host.className = "";
      delete host.dataset.component;
    },
  });
}
