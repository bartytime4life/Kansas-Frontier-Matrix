import {
  Map as MapLibreMap,
  type MapGeoJSONFeature,
  type MapMouseEvent,
  type StyleSpecification,
} from "maplibre-gl";

import {
  MAP_FEATURE_SELECTION_PROFILE,
  freezeMapFeatureSelection,
  type MapFeatureSelection,
} from "./map-runtime-port";

export const SYNTHETIC_3D_FIXTURE_PROFILE =
  "kfm.maplibre.synthetic-3d-fixture.v1" as const;
export const SYNTHETIC_3D_FIXTURE_SOURCE_ID =
  "kfm-synthetic-3d-fixture" as const;
export const SYNTHETIC_3D_EXTRUSION_LAYER_ID =
  "kfm-synthetic-evidence-towers" as const;
export const SYNTHETIC_3D_POINT_LAYER_ID =
  "kfm-synthetic-evidence-points" as const;
export const SYNTHETIC_3D_CORRIDOR_LAYER_ID =
  "kfm-synthetic-context-corridor" as const;
export const DEFAULT_SYNTHETIC_3D_INITIALIZATION_DEADLINE_MS = 10_000;
const MAX_SYNTHETIC_3D_INITIALIZATION_DEADLINE_MS = 60_000;
const CONTAINER_ID = /^[A-Za-z][A-Za-z0-9._:-]{0,127}$/;

export type Synthetic3dFixtureProjection = "mercator" | "globe";
export type Synthetic3dFixtureSkyPreset = "night" | "dusk" | "clear";
export type Synthetic3dFixtureStatus =
  | "INITIALIZING"
  | "READY"
  | "ERROR"
  | "DISPOSED";

export type Synthetic3dFixtureFeature = Readonly<{
  id: string;
  title: string;
  summary: string;
  category: "landscape" | "water" | "community";
  renderLayerId:
    | typeof SYNTHETIC_3D_EXTRUSION_LAYER_ID
    | typeof SYNTHETIC_3D_POINT_LAYER_ID;
  center: readonly [number, number];
  evidenceRefs: readonly string[];
  historyEvidenceRefs: readonly string[];
}>;

export type Synthetic3dFixtureSnapshot = Readonly<{
  profile: typeof SYNTHETIC_3D_FIXTURE_PROFILE;
  status: Synthetic3dFixtureStatus;
  projection: Synthetic3dFixtureProjection;
  skyPreset: Synthetic3dFixtureSkyPreset;
  verticalScale: number;
  fieldOfView: number;
  lightAzimuth: number;
  selectedFeatureId: string | null;
  camera: Readonly<{
    longitude: number;
    latitude: number;
    zoom: number;
    bearing: number;
    pitch: number;
  }>;
  reason: string | null;
}>;

export type Synthetic3dFixtureSelection = Readonly<{
  selection: MapFeatureSelection;
  feature: Synthetic3dFixtureFeature;
}>;

export type Synthetic3dFixtureLabOptions = Readonly<{
  containerId: string;
  initialProjection?: Synthetic3dFixtureProjection;
  initialSkyPreset?: Synthetic3dFixtureSkyPreset;
  initialVerticalScale?: number;
  initialFieldOfView?: number;
  initialLightAzimuth?: number;
  initializationDeadlineMs?: number;
  onSelection?: (value: Synthetic3dFixtureSelection) => void;
  onStatus?: (snapshot: Synthetic3dFixtureSnapshot) => void;
}>;

export type Synthetic3dFixtureLabController = Readonly<{
  getSnapshot: () => Synthetic3dFixtureSnapshot;
  setProjection: (
    projection: Synthetic3dFixtureProjection,
  ) => Synthetic3dFixtureSnapshot;
  setSkyPreset: (
    preset: Synthetic3dFixtureSkyPreset,
  ) => Synthetic3dFixtureSnapshot;
  setVerticalScale: (scale: number) => Synthetic3dFixtureSnapshot;
  setFieldOfView: (fieldOfView: number) => Synthetic3dFixtureSnapshot;
  setLightAzimuth: (azimuth: number) => Synthetic3dFixtureSnapshot;
  setPitch: (pitch: number) => Synthetic3dFixtureSnapshot;
  setBearing: (bearing: number) => Synthetic3dFixtureSnapshot;
  setZoom: (zoom: number) => Synthetic3dFixtureSnapshot;
  selectFeature: (featureId: string) => Synthetic3dFixtureSnapshot;
  clearSelection: () => Synthetic3dFixtureSnapshot;
  reset: () => Synthetic3dFixtureSnapshot;
  resize: () => Synthetic3dFixtureSnapshot;
  destroy: () => void;
}>;

export class Synthetic3dFixtureLabError extends Error {
  readonly code:
    | "SYNTHETIC_3D_CONTAINER_INVALID"
    | "SYNTHETIC_3D_WEBGL2_UNAVAILABLE"
    | "SYNTHETIC_3D_INITIALIZATION_FAILED"
    | "SYNTHETIC_3D_NOT_READY"
    | "SYNTHETIC_3D_VALUE_INVALID"
    | "SYNTHETIC_3D_FEATURE_INVALID"
    | "SYNTHETIC_3D_DISPOSED";

  constructor(
    code: Synthetic3dFixtureLabError["code"],
    message: string,
  ) {
    super(message);
    this.name = "Synthetic3dFixtureLabError";
    this.code = code;
  }
}

const INITIAL_CAMERA = Object.freeze({
  longitude: -98.45,
  latitude: 38.45,
  zoom: 5.2,
  bearing: -18,
  pitch: 54,
});

export const SYNTHETIC_3D_FIXTURE_FEATURES: readonly Synthetic3dFixtureFeature[] =
  Object.freeze([
    Object.freeze({
      id: "synthetic:western-context",
      title: "Western context tower",
      summary:
        "Generalized synthetic western Kansas context. Height is presentation-only and carries no elevation claim.",
      category: "landscape",
      renderLayerId: SYNTHETIC_3D_EXTRUSION_LAYER_ID,
      center: Object.freeze([-101.15, 38.55] as const),
      evidenceRefs: Object.freeze([
        "kfm:evidence:synthetic:3d:western-context",
      ]),
      historyEvidenceRefs: Object.freeze([
        "kfm:evidence:synthetic:3d:western-context:prior",
      ]),
    }),
    Object.freeze({
      id: "synthetic:central-context",
      title: "Central context tower",
      summary:
        "Generalized synthetic central Kansas context. The extrusion is a visual index, not measured terrain.",
      category: "community",
      renderLayerId: SYNTHETIC_3D_EXTRUSION_LAYER_ID,
      center: Object.freeze([-98.55, 38.55] as const),
      evidenceRefs: Object.freeze([
        "kfm:evidence:synthetic:3d:central-context",
      ]),
      historyEvidenceRefs: Object.freeze([]),
    }),
    Object.freeze({
      id: "synthetic:eastern-context",
      title: "Eastern context tower",
      summary:
        "Generalized synthetic eastern Kansas context. Geometry is deliberately coarse and non-authoritative.",
      category: "water",
      renderLayerId: SYNTHETIC_3D_EXTRUSION_LAYER_ID,
      center: Object.freeze([-95.75, 38.45] as const),
      evidenceRefs: Object.freeze([
        "kfm:evidence:synthetic:3d:eastern-context",
      ]),
      historyEvidenceRefs: Object.freeze([
        "kfm:evidence:synthetic:3d:eastern-context:prior",
      ]),
    }),
    Object.freeze({
      id: "synthetic:northern-context",
      title: "Northern context beacon",
      summary:
        "Synthetic selection beacon for keyboard and feature-state testing.",
      category: "community",
      renderLayerId: SYNTHETIC_3D_POINT_LAYER_ID,
      center: Object.freeze([-98.9, 39.45] as const),
      evidenceRefs: Object.freeze([
        "kfm:evidence:synthetic:3d:northern-context",
      ]),
      historyEvidenceRefs: Object.freeze([]),
    }),
    Object.freeze({
      id: "synthetic:southern-context",
      title: "Southern context beacon",
      summary:
        "Synthetic selection beacon with no protected-location, property, or infrastructure meaning.",
      category: "water",
      renderLayerId: SYNTHETIC_3D_POINT_LAYER_ID,
      center: Object.freeze([-97.8, 37.45] as const),
      evidenceRefs: Object.freeze([
        "kfm:evidence:synthetic:3d:southern-context",
      ]),
      historyEvidenceRefs: Object.freeze([]),
    }),
  ]);

const FEATURES_BY_ID = new Map(
  SYNTHETIC_3D_FIXTURE_FEATURES.map((feature) => [feature.id, feature]),
);

const SKY_PRESETS = Object.freeze({
  night: Object.freeze({
    "sky-color": "#07171a",
    "horizon-color": "#173438",
    "fog-color": "#0d2427",
    "fog-ground-blend": 0.35,
    "horizon-fog-blend": 0.7,
    "sky-horizon-blend": 0.82,
    "atmosphere-blend": 0.68,
  }),
  dusk: Object.freeze({
    "sky-color": "#263744",
    "horizon-color": "#d49c78",
    "fog-color": "#5f6867",
    "fog-ground-blend": 0.28,
    "horizon-fog-blend": 0.62,
    "sky-horizon-blend": 0.9,
    "atmosphere-blend": 0.82,
  }),
  clear: Object.freeze({
    "sky-color": "#6d9dac",
    "horizon-color": "#d4e5df",
    "fog-color": "#afc9c3",
    "fog-ground-blend": 0.22,
    "horizon-fog-blend": 0.48,
    "sky-horizon-blend": 0.78,
    "atmosphere-blend": 0.88,
  }),
} satisfies Readonly<
  Record<Synthetic3dFixtureSkyPreset, Readonly<Record<string, string | number>>>
>);

function polygonFeature(
  id: string,
  category: Synthetic3dFixtureFeature["category"],
  title: string,
  height: number,
  west: number,
  south: number,
  east: number,
  north: number,
) {
  return {
    type: "Feature" as const,
    id,
    properties: {
      id,
      category,
      title,
      height,
      sourceRole: "synthetic_fixture",
      evidenceState: "SYNTHETIC_ONLY",
    },
    geometry: {
      type: "Polygon" as const,
      coordinates: [
        [
          [west, south],
          [east, south],
          [east, north],
          [west, north],
          [west, south],
        ],
      ],
    },
  };
}

function pointFeature(feature: Synthetic3dFixtureFeature) {
  return {
    type: "Feature" as const,
    id: feature.id,
    properties: {
      id: feature.id,
      category: feature.category,
      title: feature.title,
      sourceRole: "synthetic_fixture",
      evidenceState: "SYNTHETIC_ONLY",
    },
    geometry: {
      type: "Point" as const,
      coordinates: [...feature.center],
    },
  };
}

function createSyntheticFixtureStyle(): StyleSpecification {
  const western = SYNTHETIC_3D_FIXTURE_FEATURES[0];
  const central = SYNTHETIC_3D_FIXTURE_FEATURES[1];
  const eastern = SYNTHETIC_3D_FIXTURE_FEATURES[2];
  const northern = SYNTHETIC_3D_FIXTURE_FEATURES[3];
  const southern = SYNTHETIC_3D_FIXTURE_FEATURES[4];

  const data = {
    type: "FeatureCollection" as const,
    features: [
      polygonFeature(
        western.id,
        western.category,
        western.title,
        28_000,
        -102.15,
        37.75,
        -100.15,
        39.25,
      ),
      polygonFeature(
        central.id,
        central.category,
        central.title,
        46_000,
        -99.55,
        37.75,
        -97.55,
        39.25,
      ),
      polygonFeature(
        eastern.id,
        eastern.category,
        eastern.title,
        36_000,
        -96.75,
        37.75,
        -94.75,
        39.25,
      ),
      pointFeature(northern),
      pointFeature(southern),
      {
        type: "Feature" as const,
        id: "synthetic:context-corridor",
        properties: {
          id: "synthetic:context-corridor",
          category: "landscape",
          title: "Synthetic context corridor",
          sourceRole: "synthetic_fixture",
          evidenceState: "SYNTHETIC_ONLY",
        },
        geometry: {
          type: "LineString" as const,
          coordinates: [
            [-102.2, 38.15],
            [-100.7, 38.8],
            [-98.8, 38.15],
            [-96.7, 38.9],
            [-94.8, 38.35],
          ],
        },
      },
    ],
  };

  return {
    version: 8,
    sources: {
      [SYNTHETIC_3D_FIXTURE_SOURCE_ID]: {
        type: "geojson",
        data,
        lineMetrics: true,
        promoteId: "id",
      },
    },
    layers: [
      {
        id: "kfm-synthetic-3d-background",
        type: "background",
        paint: {
          "background-color": "#071517",
        },
      },
      {
        id: SYNTHETIC_3D_CORRIDOR_LAYER_ID,
        type: "line",
        source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
        filter: ["==", ["geometry-type"], "LineString"],
        layout: {
          "line-cap": "round",
          "line-join": "round",
        },
        paint: {
          "line-width": [
            "interpolate",
            ["linear"],
            ["zoom"],
            4,
            2,
            8,
            8,
          ],
          "line-opacity": 0.78,
          "line-gradient": [
            "interpolate",
            ["linear"],
            ["line-progress"],
            0,
            "#5fd5d0",
            0.5,
            "#f4d27a",
            1,
            "#dd7f5b",
          ],
        },
      },
      {
        id: "kfm-synthetic-evidence-footprints",
        type: "fill",
        source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
        filter: ["==", ["geometry-type"], "Polygon"],
        paint: {
          "fill-color": [
            "match",
            ["get", "category"],
            "water",
            "#2f87a8",
            "community",
            "#c59155",
            "#5c8c6a",
          ],
          "fill-opacity": 0.2,
          "fill-outline-color": "#d7f3ea",
        },
      },
      {
        id: SYNTHETIC_3D_EXTRUSION_LAYER_ID,
        type: "fill-extrusion",
        source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
        filter: ["==", ["geometry-type"], "Polygon"],
        minzoom: 3,
        paint: {
          "fill-extrusion-base": 0,
          "fill-extrusion-height": ["get", "height"],
          "fill-extrusion-color": [
            "case",
            ["boolean", ["feature-state", "selected"], false],
            "#ffe08a",
            [
              "match",
              ["get", "category"],
              "water",
              "#2f87a8",
              "community",
              "#c59155",
              "#5c8c6a",
            ],
          ],
          "fill-extrusion-opacity": 0.86,
          "fill-extrusion-vertical-gradient": true,
        },
      },
      {
        id: "kfm-synthetic-evidence-point-halo",
        type: "circle",
        source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
        filter: ["==", ["geometry-type"], "Point"],
        paint: {
          "circle-radius": [
            "case",
            ["boolean", ["feature-state", "selected"], false],
            18,
            13,
          ],
          "circle-color": "rgba(4, 18, 20, 0.45)",
          "circle-stroke-color": "#d7f3ea",
          "circle-stroke-width": 1.5,
          "circle-pitch-alignment": "map",
          "circle-pitch-scale": "map",
        },
      },
      {
        id: SYNTHETIC_3D_POINT_LAYER_ID,
        type: "circle",
        source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
        filter: ["==", ["geometry-type"], "Point"],
        paint: {
          "circle-radius": [
            "case",
            ["boolean", ["feature-state", "selected"], false],
            9,
            6,
          ],
          "circle-color": [
            "case",
            ["boolean", ["feature-state", "selected"], false],
            "#ffe08a",
            [
              "match",
              ["get", "category"],
              "water",
              "#59c3e6",
              "community",
              "#efb86f",
              "#7bc28b",
            ],
          ],
          "circle-stroke-color": "#071517",
          "circle-stroke-width": 2,
          "circle-pitch-alignment": "map",
          "circle-pitch-scale": "map",
        },
      },
    ],
  } as StyleSpecification;
}

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

function finiteWithin(
  value: number,
  minimum: number,
  maximum: number,
  label: string,
): number {
  if (!Number.isFinite(value) || value < minimum || value > maximum) {
    throw new Synthetic3dFixtureLabError(
      "SYNTHETIC_3D_VALUE_INVALID",
      `${label} must be a finite value from ${minimum} through ${maximum}.`,
    );
  }
  return value;
}

function normalizeBearing(value: number): number {
  finiteWithin(value, -10_000, 10_000, "Bearing");
  const normalized = ((value + 180) % 360 + 360) % 360 - 180;
  return Object.is(normalized, -0) ? 0 : normalized;
}

function isProjection(
  value: unknown,
): value is Synthetic3dFixtureProjection {
  return value === "mercator" || value === "globe";
}

function isSkyPreset(
  value: unknown,
): value is Synthetic3dFixtureSkyPreset {
  return value === "night" || value === "dusk" || value === "clear";
}

function featureFromRendered(
  rendered: readonly MapGeoJSONFeature[],
): Synthetic3dFixtureFeature | null {
  for (const candidate of rendered) {
    const id = candidate.id;
    if (typeof id !== "string") continue;
    const feature = FEATURES_BY_ID.get(id);
    if (feature) return feature;
  }
  return null;
}

class Synthetic3dFixtureLab implements Synthetic3dFixtureLabController {
  private status: Synthetic3dFixtureStatus = "INITIALIZING";
  private projection: Synthetic3dFixtureProjection;
  private skyPreset: Synthetic3dFixtureSkyPreset;
  private verticalScale: number;
  private fieldOfView: number;
  private lightAzimuth: number;
  private selectedFeatureId: string | null = null;
  private reason: string | null = null;
  private readonly subscriptions = new Set<() => void>();

  constructor(
    private readonly map: MapLibreMap,
    private readonly onSelection:
      | ((value: Synthetic3dFixtureSelection) => void)
      | undefined,
    private readonly onStatus:
      | ((snapshot: Synthetic3dFixtureSnapshot) => void)
      | undefined,
    initialProjection: Synthetic3dFixtureProjection,
    initialSkyPreset: Synthetic3dFixtureSkyPreset,
    initialVerticalScale: number,
    initialFieldOfView: number,
    initialLightAzimuth: number,
  ) {
    this.projection = initialProjection;
    this.skyPreset = initialSkyPreset;
    this.verticalScale = initialVerticalScale;
    this.fieldOfView = initialFieldOfView;
    this.lightAzimuth = initialLightAzimuth;
  }

  markReady(): Synthetic3dFixtureSnapshot {
    this.assertNotDisposed();
    this.map.setProjection({ type: this.projection });
    this.applySky();
    this.applyLight();
    this.map.setVerticalFieldOfView(this.fieldOfView);
    this.applyVerticalScale();

    const clickSubscription = this.map.on(
      "click",
      (event: MapMouseEvent) => {
        if (this.status !== "READY") return;
        try {
          const rendered = this.map.queryRenderedFeatures(event.point, {
            layers: [
              SYNTHETIC_3D_EXTRUSION_LAYER_ID,
              SYNTHETIC_3D_POINT_LAYER_ID,
            ],
          });
          const feature = featureFromRendered(rendered);
          if (feature) this.selectFeature(feature.id);
        } catch {
          this.markError("SYNTHETIC_3D_SELECTION_FAILED");
        }
      },
    );
    this.subscriptions.add(clickSubscription.unsubscribe);

    const errorSubscription = this.map.on("error", () => {
      if (this.status !== "DISPOSED") {
        this.markError("SYNTHETIC_3D_RENDERER_ERROR");
      }
    });
    this.subscriptions.add(errorSubscription.unsubscribe);

    this.status = "READY";
    this.reason = null;
    return this.notify();
  }

  getSnapshot(): Synthetic3dFixtureSnapshot {
    const center = this.map.getCenter();
    return Object.freeze({
      profile: SYNTHETIC_3D_FIXTURE_PROFILE,
      status: this.status,
      projection: this.projection,
      skyPreset: this.skyPreset,
      verticalScale: this.verticalScale,
      fieldOfView: this.fieldOfView,
      lightAzimuth: this.lightAzimuth,
      selectedFeatureId: this.selectedFeatureId,
      camera: Object.freeze({
        longitude: center.lng,
        latitude: center.lat,
        zoom: this.map.getZoom(),
        bearing: this.map.getBearing(),
        pitch: this.map.getPitch(),
      }),
      reason: this.reason,
    });
  }

  setProjection(
    projection: Synthetic3dFixtureProjection,
  ): Synthetic3dFixtureSnapshot {
    this.assertReady();
    if (!isProjection(projection)) {
      throw new Synthetic3dFixtureLabError(
        "SYNTHETIC_3D_VALUE_INVALID",
        "Projection must be mercator or globe.",
      );
    }
    this.map.setProjection({ type: projection });
    this.projection = projection;
    return this.notify();
  }

  setSkyPreset(
    preset: Synthetic3dFixtureSkyPreset,
  ): Synthetic3dFixtureSnapshot {
    this.assertReady();
    if (!isSkyPreset(preset)) {
      throw new Synthetic3dFixtureLabError(
        "SYNTHETIC_3D_VALUE_INVALID",
        "Sky preset must be night, dusk, or clear.",
      );
    }
    this.skyPreset = preset;
    this.applySky();
    return this.notify();
  }

  setVerticalScale(scale: number): Synthetic3dFixtureSnapshot {
    this.assertReady();
    this.verticalScale = finiteWithin(
      scale,
      0.25,
      3,
      "Vertical scale",
    );
    this.applyVerticalScale();
    return this.notify();
  }

  setFieldOfView(fieldOfView: number): Synthetic3dFixtureSnapshot {
    this.assertReady();
    this.fieldOfView = finiteWithin(
      fieldOfView,
      10,
      75,
      "Field of view",
    );
    this.map.setVerticalFieldOfView(this.fieldOfView);
    return this.notify();
  }

  setLightAzimuth(azimuth: number): Synthetic3dFixtureSnapshot {
    this.assertReady();
    this.lightAzimuth = finiteWithin(
      azimuth,
      0,
      360,
      "Light azimuth",
    );
    this.applyLight();
    return this.notify();
  }

  setPitch(pitch: number): Synthetic3dFixtureSnapshot {
    this.assertReady();
    const nextPitch = finiteWithin(pitch, 0, 80, "Pitch");
    this.map.jumpTo({ pitch: nextPitch });
    return this.notify();
  }

  setBearing(bearing: number): Synthetic3dFixtureSnapshot {
    this.assertReady();
    this.map.jumpTo({ bearing: normalizeBearing(bearing) });
    return this.notify();
  }

  setZoom(zoom: number): Synthetic3dFixtureSnapshot {
    this.assertReady();
    this.map.jumpTo({ zoom: finiteWithin(zoom, 3, 10, "Zoom") });
    return this.notify();
  }

  selectFeature(featureId: string): Synthetic3dFixtureSnapshot {
    this.assertReady();
    const feature = FEATURES_BY_ID.get(featureId);
    if (!feature) {
      throw new Synthetic3dFixtureLabError(
        "SYNTHETIC_3D_FEATURE_INVALID",
        "Synthetic fixture feature is not registered.",
      );
    }

    if (this.selectedFeatureId !== null) {
      this.map.setFeatureState(
        {
          source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
          id: this.selectedFeatureId,
        },
        { selected: false },
      );
    }

    this.selectedFeatureId = feature.id;
    this.map.setFeatureState(
      {
        source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
        id: feature.id,
      },
      { selected: true },
    );
    this.map.jumpTo({
      center: [feature.center[0], feature.center[1]],
      zoom: Math.max(this.map.getZoom(), 5.8),
      pitch: Math.max(this.map.getPitch(), 48),
    });

    this.onSelection?.(
      Object.freeze({
        selection: freezeMapFeatureSelection({
          profile: MAP_FEATURE_SELECTION_PROFILE,
          selectionId: `selection:${feature.id}`,
          layerId: feature.renderLayerId,
          featureId: feature.id,
          evidenceRefs: feature.evidenceRefs,
          historyEvidenceRefs: feature.historyEvidenceRefs,
        }),
        feature,
      }),
    );

    return this.notify();
  }

  clearSelection(): Synthetic3dFixtureSnapshot {
    this.assertReady();
    if (this.selectedFeatureId !== null) {
      this.map.setFeatureState(
        {
          source: SYNTHETIC_3D_FIXTURE_SOURCE_ID,
          id: this.selectedFeatureId,
        },
        { selected: false },
      );
    }
    this.selectedFeatureId = null;
    return this.notify();
  }

  reset(): Synthetic3dFixtureSnapshot {
    this.assertReady();
    this.clearSelection();
    this.projection = "globe";
    this.skyPreset = "night";
    this.verticalScale = 1;
    this.fieldOfView = 36;
    this.lightAzimuth = 210;
    this.map.setProjection({ type: this.projection });
    this.applySky();
    this.applyLight();
    this.map.setVerticalFieldOfView(this.fieldOfView);
    this.applyVerticalScale();
    this.map.jumpTo({
      center: [INITIAL_CAMERA.longitude, INITIAL_CAMERA.latitude],
      zoom: INITIAL_CAMERA.zoom,
      bearing: INITIAL_CAMERA.bearing,
      pitch: INITIAL_CAMERA.pitch,
    });
    return this.notify();
  }

  resize(): Synthetic3dFixtureSnapshot {
    this.assertReady();
    this.map.resize();
    return this.notify();
  }

  destroy(): void {
    if (this.status === "DISPOSED") return;
    for (const unsubscribe of this.subscriptions) unsubscribe();
    this.subscriptions.clear();
    this.map.remove();
    this.status = "DISPOSED";
    this.selectedFeatureId = null;
    this.reason = "SYNTHETIC_3D_DISPOSED";
    this.notify();
  }

  private applySky(): void {
    this.map.setSky(
      { ...SKY_PRESETS[this.skyPreset] } as Parameters<MapLibreMap["setSky"]>[0],
    );
  }

  private applyLight(): void {
    this.map.setLight(
      {
        anchor: "map",
        color: "#fff8df",
        intensity: 0.62,
        position: [1.5, this.lightAzimuth, 42],
      } as Parameters<MapLibreMap["setLight"]>[0],
    );
  }

  private applyVerticalScale(): void {
    this.map.setPaintProperty(
      SYNTHETIC_3D_EXTRUSION_LAYER_ID,
      "fill-extrusion-height",
      ["*", ["get", "height"], this.verticalScale],
    );
  }

  private markError(reason: string): Synthetic3dFixtureSnapshot {
    this.status = "ERROR";
    this.reason = reason;
    return this.notify();
  }

  private notify(): Synthetic3dFixtureSnapshot {
    const snapshot = this.getSnapshot();
    this.onStatus?.(snapshot);
    return snapshot;
  }

  private assertNotDisposed(): void {
    if (this.status === "DISPOSED") {
      throw new Synthetic3dFixtureLabError(
        "SYNTHETIC_3D_DISPOSED",
        "Synthetic 3D fixture lab has been disposed.",
      );
    }
  }

  private assertReady(): void {
    this.assertNotDisposed();
    if (this.status !== "READY") {
      throw new Synthetic3dFixtureLabError(
        "SYNTHETIC_3D_NOT_READY",
        "Synthetic 3D fixture lab is not ready.",
      );
    }
  }
}

export async function createSynthetic3dFixtureLab(
  options: Synthetic3dFixtureLabOptions,
): Promise<Synthetic3dFixtureLabController> {
  if (!CONTAINER_ID.test(options.containerId)) {
    throw new Synthetic3dFixtureLabError(
      "SYNTHETIC_3D_CONTAINER_INVALID",
      "Synthetic 3D fixture container ID is invalid.",
    );
  }
  if (typeof document === "undefined" || !document.getElementById(options.containerId)) {
    throw new Synthetic3dFixtureLabError(
      "SYNTHETIC_3D_CONTAINER_INVALID",
      "Synthetic 3D fixture container does not exist.",
    );
  }
  if (!supportsWebGL2()) {
    throw new Synthetic3dFixtureLabError(
      "SYNTHETIC_3D_WEBGL2_UNAVAILABLE",
      "WebGL2 is unavailable; the synthetic 3D fixture remains disabled.",
    );
  }

  const projection = options.initialProjection ?? "globe";
  const skyPreset = options.initialSkyPreset ?? "night";
  if (!isProjection(projection) || !isSkyPreset(skyPreset)) {
    throw new Synthetic3dFixtureLabError(
      "SYNTHETIC_3D_VALUE_INVALID",
      "Synthetic 3D fixture initial scene is invalid.",
    );
  }

  const verticalScale = finiteWithin(
    options.initialVerticalScale ?? 1,
    0.25,
    3,
    "Vertical scale",
  );
  const fieldOfView = finiteWithin(
    options.initialFieldOfView ?? 36,
    10,
    75,
    "Field of view",
  );
  const lightAzimuth = finiteWithin(
    options.initialLightAzimuth ?? 210,
    0,
    360,
    "Light azimuth",
  );
  const deadline = options.initializationDeadlineMs ??
    DEFAULT_SYNTHETIC_3D_INITIALIZATION_DEADLINE_MS;
  if (
    !Number.isSafeInteger(deadline) ||
    deadline < 1 ||
    deadline > MAX_SYNTHETIC_3D_INITIALIZATION_DEADLINE_MS
  ) {
    throw new Synthetic3dFixtureLabError(
      "SYNTHETIC_3D_VALUE_INVALID",
      "Synthetic 3D fixture initialization deadline is invalid.",
    );
  }

  options.onStatus?.(
    Object.freeze({
      profile: SYNTHETIC_3D_FIXTURE_PROFILE,
      status: "INITIALIZING",
      projection,
      skyPreset,
      verticalScale,
      fieldOfView,
      lightAzimuth,
      selectedFeatureId: null,
      camera: INITIAL_CAMERA,
      reason: null,
    }),
  );

  let map: MapLibreMap;
  try {
    map = new MapLibreMap({
      container: options.containerId,
      style: createSyntheticFixtureStyle(),
      center: [INITIAL_CAMERA.longitude, INITIAL_CAMERA.latitude],
      zoom: INITIAL_CAMERA.zoom,
      bearing: INITIAL_CAMERA.bearing,
      pitch: INITIAL_CAMERA.pitch,
      interactive: true,
      hash: false,
      attributionControl: false,
      maplibreLogo: false,
      cooperativeGestures: true,
      maxPitch: 80,
      minZoom: 3,
      maxZoom: 10,
      renderWorldCopies: false,
    });
  } catch (error) {
    throw new Synthetic3dFixtureLabError(
      "SYNTHETIC_3D_INITIALIZATION_FAILED",
      `Synthetic 3D fixture renderer construction failed: ${
        error instanceof Error ? error.message : "unknown error"
      }`,
    );
  }

  const controller = new Synthetic3dFixtureLab(
    map,
    options.onSelection,
    options.onStatus,
    projection,
    skyPreset,
    verticalScale,
    fieldOfView,
    lightAzimuth,
  );

  return await new Promise<Synthetic3dFixtureLabController>(
    (resolve, reject) => {
      let settled = false;
      const timer = setTimeout(() => {
        if (settled) return;
        settled = true;
        loadSubscription.unsubscribe();
        errorSubscription.unsubscribe();
        map.remove();
        reject(
          new Synthetic3dFixtureLabError(
            "SYNTHETIC_3D_INITIALIZATION_FAILED",
            "Synthetic 3D fixture initialization timed out.",
          ),
        );
      }, deadline);

      const settle = (
        result:
          | { ok: true; controller: Synthetic3dFixtureLabController }
          | { ok: false; error: Synthetic3dFixtureLabError },
      ): void => {
        if (settled) return;
        settled = true;
        clearTimeout(timer);
        loadSubscription.unsubscribe();
        errorSubscription.unsubscribe();
        if (result.ok === true) {
          resolve(result.controller);
        } else {
          map.remove();
          reject(result.error);
        }
      };

      const loadSubscription = map.on("load", () => {
        try {
          controller.markReady();
          settle({ ok: true, controller });
        } catch (error) {
          settle({
            ok: false,
            error:
              error instanceof Synthetic3dFixtureLabError
                ? error
                : new Synthetic3dFixtureLabError(
                    "SYNTHETIC_3D_INITIALIZATION_FAILED",
                    "Synthetic 3D fixture post-load setup failed.",
                  ),
          });
        }
      });

      const errorSubscription = map.on("error", () => {
        settle({
          ok: false,
          error: new Synthetic3dFixtureLabError(
            "SYNTHETIC_3D_INITIALIZATION_FAILED",
            "Synthetic 3D fixture renderer reported an initialization error.",
          ),
        });
      });
    },
  );
}
