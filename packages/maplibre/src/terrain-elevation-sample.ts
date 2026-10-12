import { MapRuntimePortError } from "./map-runtime-port";
import { MAP_RUNTIME_DEFAULT_TERRAIN_EXAGGERATION } from "./map-runtime-terrain-fallback";

export const TERRAIN_ELEVATION_SAMPLE_PROFILE =
  "kfm.terrain-elevation-sample.v1" as const;
export const TERRAIN_ELEVATION_SAMPLE_EXECUTION_MODE = "FIXTURE_ONLY" as const;
export const TERRAIN_ELEVATION_SAMPLE_METHOD = "NEAREST_CELL" as const;
export const TERRAIN_ELEVATION_SAMPLE_ENCODING = "TERRARIUM" as const;
export const TERRAIN_ELEVATION_SAMPLE_UNITS = "metre" as const;
export const TERRAIN_ELEVATION_VALIDITY_MASK_METHOD =
  "SOURCE_NODATA_COMPARISON_BEFORE_ENCODING" as const;
export const TERRAIN_ELEVATION_EXACT_CANDIDATE_ID =
  "kfm:dem-source-asset-candidate:e3ebb5873588926de04806b002c795c343cd441e97a9605697f7ce920525f08c" as const;
export const TERRAIN_ELEVATION_EXACT_ARTIFACT_ID =
  "USGS_1M_14_x56y429_KS_Statewide_2018_A18.tif" as const;
export const TERRAIN_ELEVATION_EXACT_ARTIFACT_DIGEST =
  "sha256:8d923dc122ee99303201acb07c9fc49c190b19545a75768384f49ccb4e975cd7" as const;
export const TERRAIN_ELEVATION_EXACT_VERTICAL_DATUM = "NAVD88" as const;
export const TERRAIN_ELEVATION_EXACT_SOURCE_NODATA = -999999 as const;

export type TerrainRgb = readonly [red: number, green: number, blue: number];

export type TerrainElevationSampleRequest = Readonly<{
  profile: typeof TERRAIN_ELEVATION_SAMPLE_PROFILE;
  executionMode: typeof TERRAIN_ELEVATION_SAMPLE_EXECUTION_MODE;
  samplingMethod: typeof TERRAIN_ELEVATION_SAMPLE_METHOD;
  encoding: typeof TERRAIN_ELEVATION_SAMPLE_ENCODING;
  candidateId: typeof TERRAIN_ELEVATION_EXACT_CANDIDATE_ID;
  artifactId: typeof TERRAIN_ELEVATION_EXACT_ARTIFACT_ID;
  artifactDigest: typeof TERRAIN_ELEVATION_EXACT_ARTIFACT_DIGEST;
  verticalDatum: typeof TERRAIN_ELEVATION_EXACT_VERTICAL_DATUM;
  units: typeof TERRAIN_ELEVATION_SAMPLE_UNITS;
  cellSize: Readonly<{
    value: number;
    units: typeof TERRAIN_ELEVATION_SAMPLE_UNITS;
  }>;
  width: number;
  height: number;
  sourceWindowOrigin: Readonly<{
    column: number;
    row: number;
  }>;
  /** Row-major RGB bytes for the minimized in-memory source window. */
  rgb: Uint8Array | readonly number[];
  /** Row-major 0/1 mask derived from the source nodata comparison. */
  validityMask: Uint8Array | readonly number[];
  validityMaskMethod: typeof TERRAIN_ELEVATION_VALIDITY_MASK_METHOD;
  sourceNodataValue: number;
  sample: Readonly<{
    column: number;
    row: number;
  }>;
  displayExaggeration?: number;
}>;

type TerrainElevationSampleCommon = Readonly<{
  profile: typeof TERRAIN_ELEVATION_SAMPLE_PROFILE;
  executionMode: typeof TERRAIN_ELEVATION_SAMPLE_EXECUTION_MODE;
  candidateId: string;
  artifactId: string;
  artifactDigest: string;
  verticalDatum: string;
  units: typeof TERRAIN_ELEVATION_SAMPLE_UNITS;
  cellSize: Readonly<{
    value: number;
    units: typeof TERRAIN_ELEVATION_SAMPLE_UNITS;
  }>;
  encoding: typeof TERRAIN_ELEVATION_SAMPLE_ENCODING;
  samplingMethod: typeof TERRAIN_ELEVATION_SAMPLE_METHOD;
  sampledCell: Readonly<{
    column: number;
    row: number;
  }>;
  displayExaggeration: number;
  valueExaggerated: false;
  /** This pure decoder reports supplied references; it does not verify lineage. */
  provenanceVerified: false;
  validityMaskMethod: typeof TERRAIN_ELEVATION_VALIDITY_MASK_METHOD;
  sourceNodataValue: number;
}>;

export type TerrainElevationSampleAnswer = TerrainElevationSampleCommon &
  Readonly<{
    status: "ANSWER";
    reason: null;
    sourceElevation: number;
    nodata: false;
  }>;

export type TerrainElevationSampleAbstention = TerrainElevationSampleCommon &
  Readonly<{
    status: "ABSTAIN";
    reason: "NODATA";
    sourceElevation: null;
    nodata: true;
  }>;

export type TerrainElevationSampleResult =
  | TerrainElevationSampleAnswer
  | TerrainElevationSampleAbstention;

const REQUIRED_REQUEST_FIELDS = new Set([
  "profile",
  "executionMode",
  "samplingMethod",
  "encoding",
  "candidateId",
  "artifactId",
  "artifactDigest",
  "verticalDatum",
  "units",
  "cellSize",
  "width",
  "height",
  "sourceWindowOrigin",
  "rgb",
  "validityMask",
  "validityMaskMethod",
  "sourceNodataValue",
  "sample",
]);
const REQUEST_FIELDS = new Set([
  ...REQUIRED_REQUEST_FIELDS,
  "displayExaggeration",
]);
const CELL_SIZE_FIELDS = new Set(["value", "units"]);
const SOURCE_WINDOW_ORIGIN_FIELDS = new Set(["column", "row"]);
const SAMPLE_FIELDS = new Set(["column", "row"]);
const SAFE_ID = /^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$/;
const SHA256 = /^sha256:[a-f0-9]{64}$/;
const SAFE_DATUM = /^[A-Za-z0-9][A-Za-z0-9 ._:/()+-]{0,159}$/;

function invalid(message: string): never {
  throw new MapRuntimePortError("MAP_RUNTIME_STATE_INVALID", message);
}

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

function hasClosedRequestFields(value: Record<string, unknown>): boolean {
  const keys = Object.keys(value);
  return (
    keys.every((key) => REQUEST_FIELDS.has(key)) &&
    [...REQUIRED_REQUEST_FIELDS].every((key) => Object.hasOwn(value, key))
  );
}

function isFiniteNumber(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

function isByte(value: unknown): value is number {
  return (
    typeof value === "number" &&
    Number.isInteger(value) &&
    value >= 0 &&
    value <= 255
  );
}

function isNumericBuffer(value: unknown): value is Uint8Array | readonly number[] {
  return value instanceof Uint8Array || Array.isArray(value);
}

function validateRequest(
  request: unknown,
): asserts request is TerrainElevationSampleRequest {
  if (!isRecord(request) || !hasClosedRequestFields(request)) {
    invalid("Terrain elevation sample request is invalid.");
  }
  if (
    request.profile !== TERRAIN_ELEVATION_SAMPLE_PROFILE ||
    request.executionMode !== TERRAIN_ELEVATION_SAMPLE_EXECUTION_MODE ||
    request.samplingMethod !== TERRAIN_ELEVATION_SAMPLE_METHOD ||
    request.encoding !== TERRAIN_ELEVATION_SAMPLE_ENCODING ||
    request.units !== TERRAIN_ELEVATION_SAMPLE_UNITS ||
    request.candidateId !== TERRAIN_ELEVATION_EXACT_CANDIDATE_ID ||
    !SAFE_ID.test(request.candidateId) ||
    request.artifactId !== TERRAIN_ELEVATION_EXACT_ARTIFACT_ID ||
    !SAFE_ID.test(request.artifactId) ||
    request.artifactDigest !== TERRAIN_ELEVATION_EXACT_ARTIFACT_DIGEST ||
    !SHA256.test(request.artifactDigest) ||
    request.verticalDatum !== TERRAIN_ELEVATION_EXACT_VERTICAL_DATUM ||
    !SAFE_DATUM.test(request.verticalDatum)
  ) {
    invalid("Terrain elevation sample identity or metadata is invalid.");
  }
  if (
    !isRecord(request.cellSize) ||
    !hasExactFields(request.cellSize, CELL_SIZE_FIELDS) ||
    !isFiniteNumber(request.cellSize.value) ||
    request.cellSize.value !== 1 ||
    request.cellSize.units !== TERRAIN_ELEVATION_SAMPLE_UNITS
  ) {
    invalid("Terrain elevation sample cell size is invalid.");
  }
  if (
    typeof request.width !== "number" ||
    !Number.isSafeInteger(request.width) ||
    request.width <= 0 ||
    typeof request.height !== "number" ||
    !Number.isSafeInteger(request.height) ||
    request.height <= 0 ||
    !isNumericBuffer(request.rgb) ||
    !isNumericBuffer(request.validityMask) ||
    request.validityMaskMethod !== TERRAIN_ELEVATION_VALIDITY_MASK_METHOD ||
    request.sourceNodataValue !== TERRAIN_ELEVATION_EXACT_SOURCE_NODATA
  ) {
    invalid("Terrain elevation sample raster is invalid.");
  }

  if (
    !isRecord(request.sourceWindowOrigin) ||
    !hasExactFields(
      request.sourceWindowOrigin,
      SOURCE_WINDOW_ORIGIN_FIELDS,
    ) ||
    typeof request.sourceWindowOrigin.column !== "number" ||
    !Number.isSafeInteger(request.sourceWindowOrigin.column) ||
    request.sourceWindowOrigin.column < 0 ||
    typeof request.sourceWindowOrigin.row !== "number" ||
    !Number.isSafeInteger(request.sourceWindowOrigin.row) ||
    request.sourceWindowOrigin.row < 0
  ) {
    invalid("Terrain elevation source window origin is invalid.");
  }

  const expectedLength = request.width * request.height * 3;
  if (
    !Number.isSafeInteger(expectedLength) ||
    request.rgb.length !== expectedLength ||
    request.validityMask.length !== request.width * request.height
  ) {
    invalid("Terrain elevation sample raster bytes are invalid.");
  }
  for (const channel of request.rgb) {
    if (!isByte(channel)) {
      invalid("Terrain elevation sample raster bytes are invalid.");
    }
  }
  for (const validity of request.validityMask) {
    if (validity !== 0 && validity !== 1) {
      invalid("Terrain elevation validity mask is invalid.");
    }
  }

  if (
    request.width - 1 >
      Number.MAX_SAFE_INTEGER - request.sourceWindowOrigin.column ||
    request.height - 1 >
      Number.MAX_SAFE_INTEGER - request.sourceWindowOrigin.row ||
    !isRecord(request.sample) ||
    !hasExactFields(request.sample, SAMPLE_FIELDS) ||
    !isFiniteNumber(request.sample.column) ||
    !isFiniteNumber(request.sample.row)
  ) {
    invalid("Terrain elevation sample location is invalid.");
  }

  const maximumColumn = request.sourceWindowOrigin.column + request.width - 1;
  const maximumRow = request.sourceWindowOrigin.row + request.height - 1;
  if (
    request.sample.column < request.sourceWindowOrigin.column ||
    request.sample.column > maximumColumn ||
    request.sample.row < request.sourceWindowOrigin.row ||
    request.sample.row > maximumRow
  ) {
    invalid("Terrain elevation sample location is invalid.");
  }
  if (
    request.displayExaggeration !== undefined &&
    (!isFiniteNumber(request.displayExaggeration) ||
      request.displayExaggeration <= 0)
  ) {
    invalid("Terrain elevation display exaggeration is invalid.");
  }
}

function commonResult(
  request: TerrainElevationSampleRequest,
  column: number,
  row: number,
): TerrainElevationSampleCommon {
  return {
    profile: TERRAIN_ELEVATION_SAMPLE_PROFILE,
    executionMode: TERRAIN_ELEVATION_SAMPLE_EXECUTION_MODE,
    candidateId: request.candidateId,
    artifactId: request.artifactId,
    artifactDigest: request.artifactDigest,
    verticalDatum: request.verticalDatum,
    units: TERRAIN_ELEVATION_SAMPLE_UNITS,
    cellSize: Object.freeze({ ...request.cellSize }),
    encoding: TERRAIN_ELEVATION_SAMPLE_ENCODING,
    samplingMethod: TERRAIN_ELEVATION_SAMPLE_METHOD,
    sampledCell: Object.freeze({ column, row }),
    displayExaggeration:
      request.displayExaggeration ?? MAP_RUNTIME_DEFAULT_TERRAIN_EXAGGERATION,
    valueExaggerated: false,
    provenanceVerified: false,
    validityMaskMethod: TERRAIN_ELEVATION_VALIDITY_MASK_METHOD,
    sourceNodataValue: request.sourceNodataValue,
  };
}

/**
 * Internal conformance seam for sampling an in-memory Terrarium fixture.
 *
 * It is intentionally omitted from the package root facade. It performs no
 * acquisition, source admission, renderer mutation, network access, or
 * filesystem access. Display exaggeration is disclosed but is never applied
 * to the decoded source elevation.
 */
export function __testOnlySampleTerrariumElevationNearestCell(
  request: TerrainElevationSampleRequest,
): TerrainElevationSampleResult {
  validateRequest(request);

  const localColumn = Math.floor(
    request.sample.column - request.sourceWindowOrigin.column + 0.5,
  );
  const localRow = Math.floor(
    request.sample.row - request.sourceWindowOrigin.row + 0.5,
  );
  const column = request.sourceWindowOrigin.column + localColumn;
  const row = request.sourceWindowOrigin.row + localRow;
  const offset = (localRow * request.width + localColumn) * 3;
  const validityOffset = localRow * request.width + localColumn;
  const rgb: TerrainRgb = [
    request.rgb[offset] as number,
    request.rgb[offset + 1] as number,
    request.rgb[offset + 2] as number,
  ];
  const common = commonResult(request, column, row);

  if (request.validityMask[validityOffset] === 0) {
    return Object.freeze({
      ...common,
      status: "ABSTAIN",
      reason: "NODATA",
      sourceElevation: null,
      nodata: true,
    });
  }

  const sourceElevation = rgb[0] * 256 + rgb[1] + rgb[2] / 256 - 32768;
  return Object.freeze({
    ...common,
    status: "ANSWER",
    reason: null,
    sourceElevation,
    nodata: false,
  });
}

/**
 * Decodes only the exact, one-cell Ellsworth candidate fixture.
 *
 * The public package surface accepts no caller-controlled source identity,
 * digest, raster bytes, mask, grid geometry, datum, or nodata value. The
 * returned value remains non-authoritative because this offline function does
 * not independently verify lineage or activate runtime sampling.
 */
export function sampleExactDemCandidateFixture(
  displayExaggeration?: number,
): TerrainElevationSampleAnswer {
  const result = __testOnlySampleTerrariumElevationNearestCell({
    profile: TERRAIN_ELEVATION_SAMPLE_PROFILE,
    executionMode: TERRAIN_ELEVATION_SAMPLE_EXECUTION_MODE,
    samplingMethod: TERRAIN_ELEVATION_SAMPLE_METHOD,
    encoding: TERRAIN_ELEVATION_SAMPLE_ENCODING,
    candidateId: TERRAIN_ELEVATION_EXACT_CANDIDATE_ID,
    artifactId: TERRAIN_ELEVATION_EXACT_ARTIFACT_ID,
    artifactDigest: TERRAIN_ELEVATION_EXACT_ARTIFACT_DIGEST,
    verticalDatum: TERRAIN_ELEVATION_EXACT_VERTICAL_DATUM,
    units: TERRAIN_ELEVATION_SAMPLE_UNITS,
    cellSize: { value: 1, units: TERRAIN_ELEVATION_SAMPLE_UNITS },
    width: 1,
    height: 1,
    sourceWindowOrigin: { column: 6934, row: 2909 },
    rgb: [129, 213, 118],
    validityMask: [1],
    validityMaskMethod: TERRAIN_ELEVATION_VALIDITY_MASK_METHOD,
    sourceNodataValue: TERRAIN_ELEVATION_EXACT_SOURCE_NODATA,
    sample: { column: 6934, row: 2909 },
    ...(displayExaggeration === undefined ? {} : { displayExaggeration }),
  });

  if (result.status !== "ANSWER") {
    invalid("Exact terrain elevation fixture unexpectedly abstained.");
  }
  return result;
}
