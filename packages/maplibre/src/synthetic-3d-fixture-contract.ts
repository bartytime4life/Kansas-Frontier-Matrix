export const SYNTHETIC_3D_FIXTURE_LAB_PROFILE =
  "kfm.maplibre.synthetic-3d-fixture-lab.v1";
export const SYNTHETIC_3D_FIXTURE_SOURCE_ID =
  "kfm-synthetic-3d-fixture-source";
export const SYNTHETIC_3D_FIXTURE_EXTRUSION_LAYER_ID =
  "kfm-synthetic-3d-fixture-extrusions";

export type Synthetic3DFixtureProjection = "mercator" | "globe";
export type Synthetic3DFixtureLabState =
  | "IDLE"
  | "INITIALIZING"
  | "READY"
  | "ERROR"
  | "DISPOSED";
export type Synthetic3DFixtureLabReasonCode =
  | "WEBGL2_UNAVAILABLE"
  | "CONTAINER_INVALID"
  | "INITIALIZATION_FAILED"
  | "NETWORK_REQUEST_BLOCKED"
  | "RUNTIME_ERROR"
  | "DISPOSED";

export type Synthetic3DFixtureFeature = Readonly<{
  featureId: string;
  label: string;
  evidenceRef: string;
  visualHeightMeters: number;
}>;

export const SYNTHETIC_3D_FIXTURE_FEATURES: readonly Synthetic3DFixtureFeature[] =
  Object.freeze([
    Object.freeze({
      featureId: "fixture-west",
      label: "Synthetic western Kansas prism",
      evidenceRef: "kfm:evidence:synthetic:maplibre-3d:west",
      visualHeightMeters: 18_000,
    }),
    Object.freeze({
      featureId: "fixture-central",
      label: "Synthetic central Kansas prism",
      evidenceRef: "kfm:evidence:synthetic:maplibre-3d:central",
      visualHeightMeters: 30_000,
    }),
    Object.freeze({
      featureId: "fixture-east",
      label: "Synthetic eastern Kansas prism",
      evidenceRef: "kfm:evidence:synthetic:maplibre-3d:east",
      visualHeightMeters: 42_000,
    }),
  ]);

export type Synthetic3DFixtureSelection = Readonly<{
  profile: typeof SYNTHETIC_3D_FIXTURE_LAB_PROFILE;
  sourceId: typeof SYNTHETIC_3D_FIXTURE_SOURCE_ID;
  layerId: typeof SYNTHETIC_3D_FIXTURE_EXTRUSION_LAYER_ID;
  featureId: string;
  label: string;
  evidenceRef: string;
}>;

export type Synthetic3DFixtureCamera = Readonly<{
  pitch: number;
  bearing: number;
  verticalFieldOfView: number;
}>;

export type Synthetic3DFixtureLabSnapshot = Readonly<{
  profile: typeof SYNTHETIC_3D_FIXTURE_LAB_PROFILE;
  state: Synthetic3DFixtureLabState;
  reason: Synthetic3DFixtureLabReasonCode | null;
  projection: Synthetic3DFixtureProjection;
  camera: Synthetic3DFixtureCamera;
  selection: Synthetic3DFixtureSelection | null;
}>;

export type Synthetic3DFixtureLabOptions = Readonly<{
  containerId: string;
  interactive?: boolean;
  onSelection?: (selection: Synthetic3DFixtureSelection) => void;
}>;

export interface Synthetic3DFixtureLabController {
  initialize(): Promise<Synthetic3DFixtureLabSnapshot>;
  getSnapshot(): Synthetic3DFixtureLabSnapshot;
  setProjection(
    projection: Synthetic3DFixtureProjection,
  ): Synthetic3DFixtureLabSnapshot;
  setCamera(camera: Synthetic3DFixtureCamera): Synthetic3DFixtureLabSnapshot;
  selectFeature(featureId: string): Synthetic3DFixtureLabSnapshot;
  dispose(): void;
}

export class Synthetic3DFixtureLabError extends Error {
  readonly code: Synthetic3DFixtureLabReasonCode;

  constructor(code: Synthetic3DFixtureLabReasonCode, message: string) {
    super(message);
    this.name = "Synthetic3DFixtureLabError";
    this.code = code;
  }
}
