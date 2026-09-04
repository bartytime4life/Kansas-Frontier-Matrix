import "maplibre-gl/dist/maplibre-gl.css";

import { Map as MapLibreMap, type StyleSpecification } from "maplibre-gl";

import {
  SYNTHETIC_3D_FIXTURE_EXTRUSION_LAYER_ID,
  SYNTHETIC_3D_FIXTURE_FEATURES,
  SYNTHETIC_3D_FIXTURE_LAB_PROFILE,
  SYNTHETIC_3D_FIXTURE_SOURCE_ID,
  Synthetic3DFixtureLabError,
  type Synthetic3DFixtureCamera,
  type Synthetic3DFixtureFeature,
  type Synthetic3DFixtureLabController,
  type Synthetic3DFixtureLabOptions,
  type Synthetic3DFixtureLabReasonCode,
  type Synthetic3DFixtureLabSnapshot,
  type Synthetic3DFixtureLabState,
  type Synthetic3DFixtureProjection,
  type Synthetic3DFixtureSelection,
} from "./synthetic-3d-fixture-contract";

export {
  SYNTHETIC_3D_FIXTURE_EXTRUSION_LAYER_ID,
  SYNTHETIC_3D_FIXTURE_FEATURES,
  SYNTHETIC_3D_FIXTURE_LAB_PROFILE,
  SYNTHETIC_3D_FIXTURE_SOURCE_ID,
  Synthetic3DFixtureLabError,
} from "./synthetic-3d-fixture-contract";
export type {
  Synthetic3DFixtureCamera,
  Synthetic3DFixtureFeature,
  Synthetic3DFixtureLabController,
  Synthetic3DFixtureLabOptions,
  Synthetic3DFixtureLabReasonCode,
  Synthetic3DFixtureLabSnapshot,
  Synthetic3DFixtureLabState,
  Synthetic3DFixtureProjection,
  Synthetic3DFixtureSelection,
} from "./synthetic-3d-fixture-contract";

const CONTAINER_ID = /^[A-Za-z][A-Za-z0-9._:-]{0,127}$/;
const INITIALIZATION_DEADLINE_MS = 10_000;

const DEFAULT_CAMERA: Synthetic3DFixtureCamera = Object.freeze({
  pitch: 52,
  bearing: -18,
  verticalFieldOfView: 36.87,
});

const DEFAULT_CENTER: [number, number] = [-98.5, 38.5];

type FixtureCoordinate = [number, number];
const FEATURE_GEOMETRIES: Readonly<
  Record<string, readonly FixtureCoordinate[]>
> = {
  "fixture-west": [
    [-101.6, 37.5],
    [-100.4, 37.5],
    [-100.4, 38.2],
    [-101.6, 38.2],
    [-101.6, 37.5],
  ],
  "fixture-central": [
    [-99.3, 38.1],
    [-98.0, 38.1],
    [-98.0, 39.0],
    [-99.3, 39.0],
    [-99.3, 38.1],
  ],
  "fixture-east": [
    [-96.9, 37.6],
    [-95.7, 37.6],
    [-95.7, 38.5],
    [-96.9, 38.5],
    [-96.9, 37.6],
  ],
};

function supportsWebGL2(): boolean {
  if (typeof document === "undefined") return false;
  try {
    const context = document.createElement("canvas").getContext("webgl2");
    if (context === null) return false;
    context.getExtension("WEBGL_lose_context")?.loseContext();
    return true;
  } catch {
    return false;
  }
}

function freezeCamera(
  camera: Synthetic3DFixtureCamera,
): Synthetic3DFixtureCamera {
  if (
    !Number.isFinite(camera.pitch) ||
    camera.pitch < 0 ||
    camera.pitch > 60
  ) {
    throw new Synthetic3DFixtureLabError(
      "RUNTIME_ERROR",
      "Synthetic 3D fixture pitch must be between 0 and 60 degrees.",
    );
  }
  if (
    !Number.isFinite(camera.bearing) ||
    camera.bearing < -180 ||
    camera.bearing > 180
  ) {
    throw new Synthetic3DFixtureLabError(
      "RUNTIME_ERROR",
      "Synthetic 3D fixture bearing must be between -180 and 180 degrees.",
    );
  }
  if (
    !Number.isFinite(camera.verticalFieldOfView) ||
    camera.verticalFieldOfView < 20 ||
    camera.verticalFieldOfView > 80
  ) {
    throw new Synthetic3DFixtureLabError(
      "RUNTIME_ERROR",
      "Synthetic 3D fixture field of view must be between 20 and 80 degrees.",
    );
  }
  return Object.freeze({
    pitch: camera.pitch,
    bearing: camera.bearing,
    verticalFieldOfView: camera.verticalFieldOfView,
  });
}

function fixtureFeature(featureId: string): Synthetic3DFixtureFeature {
  const feature = SYNTHETIC_3D_FIXTURE_FEATURES.find(
    (candidate) => candidate.featureId === featureId,
  );
  if (!feature) {
    throw new Synthetic3DFixtureLabError(
      "RUNTIME_ERROR",
      "Synthetic 3D fixture feature is not admitted by this lab.",
    );
  }
  return feature;
}

export function createSynthetic3DFixtureStyle(): StyleSpecification {
  return {
    version: 8,
    name: "KFM synthetic MapLibre 3D fixture lab",
    sources: {
      [SYNTHETIC_3D_FIXTURE_SOURCE_ID]: {
        type: "geojson",
        data: {
          type: "FeatureCollection",
          features: SYNTHETIC_3D_FIXTURE_FEATURES.map((feature) => ({
            type: "Feature",
            id: feature.featureId,
            properties: {
              label: feature.label,
              evidence_ref: feature.evidenceRef,
              visual_height_m: feature.visualHeightMeters,
            },
            geometry: {
              type: "Polygon",
              coordinates: [
                FEATURE_GEOMETRIES[feature.featureId].map(([longitude, latitude]) => [
                  longitude,
                  latitude,
                ]),
              ],
            },
          })),
        },
      },
    },
    layers: [
      {
        id: "kfm-synthetic-3d-fixture-background",
        type: "background",
        paint: {
          "background-color": "#071517",
        },
      },
      {
        id: "kfm-synthetic-3d-fixture-footprints",
        type: "fill",
        source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
        paint: {
          "fill-color": "#55c6b5",
          "fill-opacity": 0.16,
          "fill-outline-color": "#d8fff7",
        },
      },
      {
        id: SYNTHETIC_3D_FIXTURE_EXTRUSION_LAYER_ID,
        type: "fill-extrusion",
        source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
        paint: {
          "fill-extrusion-color": [
            "case",
            ["boolean", ["feature-state", "selected"], false],
            "#ffd166",
            "#2aa198",
          ],
          "fill-extrusion-height": ["get", "visual_height_m"],
          "fill-extrusion-base": 0,
          "fill-extrusion-opacity": 0.82,
          "fill-extrusion-vertical-gradient": true,
        },
      },
    ],
  };
}

class Synthetic3DFixtureLab implements Synthetic3DFixtureLabController {
  private readonly containerId: string;
  private readonly interactive: boolean;
  private readonly onSelection:
    | ((selection: Synthetic3DFixtureSelection) => void)
    | undefined;
  private map: MapLibreMap | null = null;
  private state: Synthetic3DFixtureLabState = "IDLE";
  private reason: Synthetic3DFixtureLabReasonCode | null = null;
  private projection: Synthetic3DFixtureProjection = "mercator";
  private camera: Synthetic3DFixtureCamera = DEFAULT_CAMERA;
  private selection: Synthetic3DFixtureSelection | null = null;
  private initialization: Promise<Synthetic3DFixtureLabSnapshot> | null = null;
  private rejectInitialization:
    | ((error: Synthetic3DFixtureLabError) => void)
    | null = null;
  private initializationDeadline: ReturnType<typeof setTimeout> | null = null;
  private readonly rendererUnsubscribers = new Set<() => void>();

  constructor(options: Synthetic3DFixtureLabOptions) {
    if (!CONTAINER_ID.test(options.containerId)) {
      throw new Synthetic3DFixtureLabError(
        "CONTAINER_INVALID",
        "Synthetic 3D fixture container ID is invalid.",
      );
    }
    this.containerId = options.containerId;
    this.interactive = options.interactive ?? true;
    this.onSelection = options.onSelection;
  }

  initialize(): Promise<Synthetic3DFixtureLabSnapshot> {
    this.assertNotDisposed();
    if (this.state === "READY") return Promise.resolve(this.getSnapshot());
    if (this.initialization !== null) return this.initialization;

    let resolveInitialization!: (
      snapshot: Synthetic3DFixtureLabSnapshot,
    ) => void;
    let rejectInitialization!: (error: Synthetic3DFixtureLabError) => void;
    const initialization = new Promise<Synthetic3DFixtureLabSnapshot>(
      (resolve, reject) => {
        resolveInitialization = resolve;
        rejectInitialization = reject;
      },
    );
    this.initialization = initialization;
    this.rejectInitialization = rejectInitialization;
    this.state = "INITIALIZING";
    this.reason = null;

    if (!supportsWebGL2()) {
      this.fail("WEBGL2_UNAVAILABLE", "WebGL2 is unavailable.");
      return initialization;
    }

    try {
      const map = new MapLibreMap({
        container: this.containerId,
        style: createSynthetic3DFixtureStyle(),
        center: [DEFAULT_CENTER[0], DEFAULT_CENTER[1]],
        zoom: 5.35,
        pitch: this.camera.pitch,
        bearing: this.camera.bearing,
        interactive: this.interactive,
        hash: false,
        attributionControl: false,
        maplibreLogo: false,
        maxPitch: 60,
        renderWorldCopies: false,
        transformRequest: (url: string) => {
          throw new Synthetic3DFixtureLabError(
            "NETWORK_REQUEST_BLOCKED",
            `Synthetic 3D fixture lab blocked an unexpected network request: ${url}`,
          );
        },
      });
      this.map = map;
      this.initializationDeadline = setTimeout(() => {
        if (
          this.state === "INITIALIZING" &&
          this.initialization === initialization &&
          this.map === map
        ) {
          this.fail(
            "INITIALIZATION_FAILED",
            "Synthetic 3D fixture initialization timed out.",
          );
        }
      }, INITIALIZATION_DEADLINE_MS);

      const loadSubscription = map.on("load", () => {
        loadSubscription.unsubscribe();
        this.rendererUnsubscribers.delete(loadSubscription.unsubscribe);
        if (this.state === "DISPOSED") return;

        try {
          map.setVerticalFieldOfView(this.camera.verticalFieldOfView);
          map.getCanvas().setAttribute(
            "aria-label",
            "Interactive synthetic Kansas 3D fixture map. Use the adjacent keyboard controls for an equivalent selection path.",
          );
          const clickSubscription = map.on(
            "click",
            SYNTHETIC_3D_FIXTURE_EXTRUSION_LAYER_ID,
            (event) => {
              const featureId = event.features?.[0]?.id;
              if (typeof featureId !== "string") return;
              this.selectFeature(featureId);
            },
          );
          this.rendererUnsubscribers.add(clickSubscription.unsubscribe);

          this.state = "READY";
          this.reason = null;
          this.clearInitializationDeadline();
          this.initialization = null;
          this.rejectInitialization = null;
          const snapshot = this.readSnapshot(map);
          resolveInitialization(snapshot);
        } catch {
          this.fail(
            "INITIALIZATION_FAILED",
            "Synthetic 3D fixture initialization failed.",
          );
        }
      });
      this.rendererUnsubscribers.add(loadSubscription.unsubscribe);

      const errorSubscription = map.on("error", () => {
        if (this.state === "DISPOSED") return;
        this.fail(
          this.state === "INITIALIZING"
            ? "INITIALIZATION_FAILED"
            : "RUNTIME_ERROR",
          "Synthetic 3D fixture renderer reported an error.",
        );
      });
      this.rendererUnsubscribers.add(errorSubscription.unsubscribe);
    } catch (error) {
      const code =
        error instanceof Synthetic3DFixtureLabError
          ? error.code
          : "INITIALIZATION_FAILED";
      this.fail(code, "Synthetic 3D fixture renderer construction failed.");
    }

    return initialization;
  }

  getSnapshot(): Synthetic3DFixtureLabSnapshot {
    if (this.map !== null && this.state === "READY") {
      return this.readSnapshot(this.map);
    }
    return Object.freeze({
      profile: SYNTHETIC_3D_FIXTURE_LAB_PROFILE,
      state: this.state,
      reason: this.reason,
      projection: this.projection,
      camera: this.camera,
      selection: this.selection,
    });
  }

  setProjection(
    projection: Synthetic3DFixtureProjection,
  ): Synthetic3DFixtureLabSnapshot {
    const map = this.assertReady();
    if (projection !== "mercator" && projection !== "globe") {
      throw new Synthetic3DFixtureLabError(
        "RUNTIME_ERROR",
        "Synthetic 3D fixture projection is invalid.",
      );
    }
    map.setProjection({ type: projection });
    this.projection = projection;
    return this.readSnapshot(map);
  }

  setCamera(camera: Synthetic3DFixtureCamera): Synthetic3DFixtureLabSnapshot {
    const map = this.assertReady();
    const frozen = freezeCamera(camera);
    map.jumpTo({
      pitch: frozen.pitch,
      bearing: frozen.bearing,
    });
    map.setVerticalFieldOfView(frozen.verticalFieldOfView);
    this.camera = frozen;
    return this.readSnapshot(map);
  }

  selectFeature(featureId: string): Synthetic3DFixtureLabSnapshot {
    const map = this.assertReady();
    const feature = fixtureFeature(featureId);

    if (this.selection !== null) {
      map.setFeatureState(
        {
          source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
          id: this.selection.featureId,
        },
        { selected: false },
      );
    }

    map.setFeatureState(
      {
        source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
        id: feature.featureId,
      },
      { selected: true },
    );

    const selection: Synthetic3DFixtureSelection = Object.freeze({
      profile: SYNTHETIC_3D_FIXTURE_LAB_PROFILE,
      sourceId: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
      layerId: SYNTHETIC_3D_FIXTURE_EXTRUSION_LAYER_ID,
      featureId: feature.featureId,
      label: feature.label,
      evidenceRef: feature.evidenceRef,
    });
    this.selection = selection;
    try {
      this.onSelection?.(selection);
    } catch {
      // A presentation callback cannot become renderer or evidence authority.
    }
    return this.readSnapshot(map);
  }

  dispose(): void {
    if (this.state === "DISPOSED") return;
    this.clearInitializationDeadline();
    const rejection = this.rejectInitialization;
    this.rejectInitialization = null;
    this.initialization = null;
    this.clearRendererSubscriptions();
    const map = this.map;
    this.map = null;
    map?.remove();
    this.state = "DISPOSED";
    this.reason = "DISPOSED";
    this.selection = null;
    rejection?.(
      new Synthetic3DFixtureLabError(
        "DISPOSED",
        "Synthetic 3D fixture lab was disposed during initialization.",
      ),
    );
  }

  private readSnapshot(map: MapLibreMap): Synthetic3DFixtureLabSnapshot {
    const projectionType = map.getProjection().type;
    this.projection = projectionType === "globe" ? "globe" : "mercator";
    this.camera = freezeCamera({
      pitch: map.getPitch(),
      bearing: map.getBearing(),
      verticalFieldOfView: map.getVerticalFieldOfView(),
    });
    return Object.freeze({
      profile: SYNTHETIC_3D_FIXTURE_LAB_PROFILE,
      state: this.state,
      reason: this.reason,
      projection: this.projection,
      camera: this.camera,
      selection: this.selection,
    });
  }

  private assertNotDisposed(): void {
    if (this.state === "DISPOSED") {
      throw new Synthetic3DFixtureLabError(
        "DISPOSED",
        "Synthetic 3D fixture lab is disposed.",
      );
    }
  }

  private assertReady(): MapLibreMap {
    this.assertNotDisposed();
    if (this.state !== "READY" || this.map === null) {
      throw new Synthetic3DFixtureLabError(
        "RUNTIME_ERROR",
        "Synthetic 3D fixture lab is not ready.",
      );
    }
    return this.map;
  }

  private fail(
    code: Synthetic3DFixtureLabReasonCode,
    message: string,
  ): void {
    this.clearInitializationDeadline();
    this.clearRendererSubscriptions();
    const map = this.map;
    this.map = null;
    map?.remove();
    this.state = "ERROR";
    this.reason = code;
    this.selection = null;
    const rejection = this.rejectInitialization;
    this.rejectInitialization = null;
    this.initialization = null;
    rejection?.(new Synthetic3DFixtureLabError(code, message));
  }

  private clearRendererSubscriptions(): void {
    for (const unsubscribe of this.rendererUnsubscribers) unsubscribe();
    this.rendererUnsubscribers.clear();
  }

  private clearInitializationDeadline(): void {
    if (this.initializationDeadline !== null) {
      clearTimeout(this.initializationDeadline);
      this.initializationDeadline = null;
    }
  }
}

export function createSynthetic3DFixtureLab(
  options: Synthetic3DFixtureLabOptions,
): Synthetic3DFixtureLabController {
  return new Synthetic3DFixtureLab(options);
}
