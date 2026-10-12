import { describe, expect, it } from "vitest";

import {
  TERRAIN_ELEVATION_EXACT_ARTIFACT_DIGEST,
  TERRAIN_ELEVATION_EXACT_ARTIFACT_ID,
  TERRAIN_ELEVATION_EXACT_CANDIDATE_ID,
  TERRAIN_ELEVATION_EXACT_SOURCE_NODATA,
  TERRAIN_ELEVATION_EXACT_VERTICAL_DATUM,
  TERRAIN_ELEVATION_SAMPLE_ENCODING,
  TERRAIN_ELEVATION_SAMPLE_EXECUTION_MODE,
  TERRAIN_ELEVATION_SAMPLE_METHOD,
  TERRAIN_ELEVATION_SAMPLE_PROFILE,
  TERRAIN_ELEVATION_SAMPLE_UNITS,
  TERRAIN_ELEVATION_VALIDITY_MASK_METHOD,
  sampleExactDemCandidateFixture,
} from "../src/index";
import * as publicMapLibre from "../src/index";
import {
  __testOnlySampleTerrariumElevationNearestCell as sampleTerrariumElevationNearestCell,
  type TerrainElevationSampleRequest,
} from "../src/terrain-elevation-sample";
import candidateSuite from "../../../fixtures/contracts/v1/spatial-foundation/dem_source_asset_candidate/cases.json";

const candidateFixture = candidateSuite.base_candidate;
const inspectionSample = candidateFixture.inspection_sample;
const sourcePixel = Object.freeze({
  row: inspectionSample.row,
  column: inspectionSample.column,
  longitude: inspectionSample.longitude,
  latitude: inspectionSample.latitude,
  rawElevation: inspectionSample.source_elevation.value,
  terrariumRgb: inspectionSample.fixture_encoding.rgb as readonly number[],
});
const artifactDigest = TERRAIN_ELEVATION_EXACT_ARTIFACT_DIGEST;
const candidateId = TERRAIN_ELEVATION_EXACT_CANDIDATE_ID;
const baseRequest: TerrainElevationSampleRequest = {
  profile: TERRAIN_ELEVATION_SAMPLE_PROFILE,
  executionMode: TERRAIN_ELEVATION_SAMPLE_EXECUTION_MODE,
  samplingMethod: TERRAIN_ELEVATION_SAMPLE_METHOD,
  encoding: TERRAIN_ELEVATION_SAMPLE_ENCODING,
  candidateId,
  artifactId: TERRAIN_ELEVATION_EXACT_ARTIFACT_ID,
  artifactDigest,
  verticalDatum: TERRAIN_ELEVATION_EXACT_VERTICAL_DATUM,
  units: TERRAIN_ELEVATION_SAMPLE_UNITS,
  cellSize: {
    value: candidateFixture.raster_grid.cell_size_x,
    units: TERRAIN_ELEVATION_SAMPLE_UNITS,
  },
  width: 1,
  height: 1,
  sourceWindowOrigin: {
    column: sourcePixel.column,
    row: sourcePixel.row,
  },
  rgb: new Uint8Array(sourcePixel.terrariumRgb),
  validityMask: new Uint8Array([
    inspectionSample.fixture_encoding.validity_mask_value,
  ]),
  validityMaskMethod: TERRAIN_ELEVATION_VALIDITY_MASK_METHOD,
  sourceNodataValue: TERRAIN_ELEVATION_EXACT_SOURCE_NODATA,
  sample: { column: sourcePixel.column, row: sourcePixel.row },
};

describe("fixture-only Terrarium elevation sampling", () => {
  it("exposes only the exact candidate fixture through the package facade", () => {
    expect("sampleTerrariumElevationNearestCell" in publicMapLibre).toBe(false);
    expect("__testOnlySampleTerrariumElevationNearestCell" in publicMapLibre).toBe(
      false,
    );

    const result = sampleExactDemCandidateFixture();

    expect(candidateFixture.candidate_id).toBe(TERRAIN_ELEVATION_EXACT_CANDIDATE_ID);
    expect(candidateFixture.assets.raster_tiff.filename).toBe(
      TERRAIN_ELEVATION_EXACT_ARTIFACT_ID,
    );
    expect(candidateFixture.assets.raster_tiff.content_sha256).toBe(
      TERRAIN_ELEVATION_EXACT_ARTIFACT_DIGEST,
    );

    expect(result).toEqual({
      profile: TERRAIN_ELEVATION_SAMPLE_PROFILE,
      executionMode: "FIXTURE_ONLY",
      status: "ANSWER",
      reason: null,
      candidateId: TERRAIN_ELEVATION_EXACT_CANDIDATE_ID,
      artifactId: TERRAIN_ELEVATION_EXACT_ARTIFACT_ID,
      artifactDigest: TERRAIN_ELEVATION_EXACT_ARTIFACT_DIGEST,
      verticalDatum: TERRAIN_ELEVATION_EXACT_VERTICAL_DATUM,
      units: "metre",
      cellSize: { value: 1, units: "metre" },
      encoding: "TERRARIUM",
      samplingMethod: "NEAREST_CELL",
      sampledCell: { column: sourcePixel.column, row: sourcePixel.row },
      displayExaggeration: 1,
      valueExaggerated: false,
      provenanceVerified: false,
      validityMaskMethod: "SOURCE_NODATA_COMPARISON_BEFORE_ENCODING",
      sourceNodataValue: TERRAIN_ELEVATION_EXACT_SOURCE_NODATA,
      sourceElevation: 469.4609375,
      nodata: false,
    });
    expect(sourcePixel).toMatchObject({
      row: 2909,
      column: 6934,
      longitude: -98.23,
      latitude: 38.73,
      rawElevation: 469.4603271484375,
    });
    expect(
      Math.abs((result.sourceElevation ?? 0) - sourcePixel.rawElevation),
    ).toBeLessThanOrEqual(1 / 256);
    expect(Object.isFrozen(result)).toBe(true);
    expect(Object.isFrozen(result.cellSize)).toBe(true);
    expect(Object.isFrozen(result.sampledCell)).toBe(true);
  });

  it.each([0.25, 1, 2, 5, 100])(
    "keeps source elevation unexaggerated at %sx display exaggeration",
    (displayExaggeration) => {
      const result = sampleExactDemCandidateFixture(displayExaggeration);

      expect(result.status).toBe("ANSWER");
      expect(result.sourceElevation).toBe(469.4609375);
      expect(result.valueExaggerated).toBe(false);
      expect(result.provenanceVerified).toBe(false);
      expect(result.displayExaggeration).toBe(displayExaggeration);
    },
  );

  it("selects the nearest cell before decoding", () => {
    const result = sampleTerrariumElevationNearestCell({
      ...baseRequest,
      width: 2,
      rgb: [128, 0, 0, ...sourcePixel.terrariumRgb],
      validityMask: [1, 1],
      sample: {
        column: sourcePixel.column + 0.75,
        row: sourcePixel.row,
      },
    });

    expect(result.status).toBe("ANSWER");
    expect(result.sourceElevation).toBe(469.4609375);
    expect(result.sampledCell).toEqual({
      column: sourcePixel.column + 1,
      row: sourcePixel.row,
    });
  });

  it("abstains through the source-derived validity mask without reserving an RGB value", () => {
    const result = sampleTerrariumElevationNearestCell({
      ...baseRequest,
      validityMask: [0],
    });

    expect(result).toMatchObject({
      status: "ABSTAIN",
      reason: "NODATA",
      sourceElevation: null,
      nodata: true,
      valueExaggerated: false,
      sourceNodataValue: -999999,
    });
  });

  it("preserves zero as valid source elevation when it is not nodata", () => {
    const result = sampleTerrariumElevationNearestCell({
      ...baseRequest,
      rgb: [128, 0, 0],
      validityMask: [1],
    });

    expect(result).toMatchObject({
      status: "ANSWER",
      reason: null,
      sourceElevation: 0,
      nodata: false,
    });
  });

  it("locks row-major indexing and rounds exact half-cell ties upward", () => {
    const result = sampleTerrariumElevationNearestCell({
      ...baseRequest,
      width: 2,
      height: 2,
      rgb: [128, 0, 0, 128, 1, 0, 128, 2, 0, 128, 3, 0],
      validityMask: [1, 1, 1, 1],
      sample: {
        column: sourcePixel.column + 0.5,
        row: sourcePixel.row + 0.5,
      },
    });

    expect(result).toMatchObject({
      status: "ANSWER",
      sourceElevation: 3,
      sampledCell: {
        column: sourcePixel.column + 1,
        row: sourcePixel.row + 1,
      },
    });
  });

  it("samples safely at a maximum-safe-integer source origin", () => {
    const result = sampleTerrariumElevationNearestCell({
      ...baseRequest,
      sourceWindowOrigin: {
        column: Number.MAX_SAFE_INTEGER,
        row: Number.MAX_SAFE_INTEGER,
      },
      sample: {
        column: Number.MAX_SAFE_INTEGER,
        row: Number.MAX_SAFE_INTEGER,
      },
    });

    expect(result).toMatchObject({
      status: "ANSWER",
      sourceElevation: 469.4609375,
      sampledCell: {
        column: Number.MAX_SAFE_INTEGER,
        row: Number.MAX_SAFE_INTEGER,
      },
    });
  });

  it.each([
    {
      axis: "column",
      request: {
        ...baseRequest,
        width: 2,
        rgb: [128, 0, 0, 128, 0, 0],
        validityMask: [1, 1],
        sourceWindowOrigin: {
          column: Number.MAX_SAFE_INTEGER,
          row: sourcePixel.row,
        },
        sample: {
          column: Number.MAX_SAFE_INTEGER,
          row: sourcePixel.row,
        },
      },
    },
    {
      axis: "row",
      request: {
        ...baseRequest,
        height: 2,
        rgb: [128, 0, 0, 128, 0, 0],
        validityMask: [1, 1],
        sourceWindowOrigin: {
          column: sourcePixel.column,
          row: Number.MAX_SAFE_INTEGER,
        },
        sample: {
          column: sourcePixel.column,
          row: Number.MAX_SAFE_INTEGER,
        },
      },
    },
  ])("rejects a source window whose $axis extent exceeds safe integers", ({ request }) => {
    expect(() => sampleTerrariumElevationNearestCell(request)).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }),
    );
  });

  it.each([
    { field: "live execution", request: { ...baseRequest, executionMode: "LIVE" } },
    { field: "sampling method", request: { ...baseRequest, samplingMethod: "BILINEAR" } },
    { field: "encoding", request: { ...baseRequest, encoding: "MAPBOX" } },
    { field: "digest", request: { ...baseRequest, artifactDigest: "sha256:bad" } },
    {
      field: "candidate identity mismatch",
      request: {
        ...baseRequest,
        candidateId:
          "kfm:dem-source-asset-candidate:ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
      },
    },
    {
      field: "artifact identity mismatch",
      request: { ...baseRequest, artifactId: "other-dem.tif" },
    },
    {
      field: "valid but wrong digest",
      request: {
        ...baseRequest,
        artifactDigest:
          "sha256:0000000000000000000000000000000000000000000000000000000000000000",
      },
    },
    {
      field: "vertical datum mismatch",
      request: { ...baseRequest, verticalDatum: "NAVD88_OTHER" },
    },
    {
      field: "source nodata mismatch",
      request: { ...baseRequest, sourceNodataValue: -32768 },
    },
    { field: "datum", request: { ...baseRequest, verticalDatum: "" } },
    {
      field: "cell size",
      request: { ...baseRequest, cellSize: { value: 0, units: "metre" } },
    },
    { field: "byte range", request: { ...baseRequest, rgb: [128, 256, 0] } },
    { field: "byte length", request: { ...baseRequest, rgb: [128, 100] } },
    { field: "mask length", request: { ...baseRequest, validityMask: [] } },
    { field: "mask value", request: { ...baseRequest, validityMask: [2] } },
    { field: "mask method", request: { ...baseRequest, validityMaskMethod: "RGB_SENTINEL" } },
    { field: "sample location", request: { ...baseRequest, sample: { column: 0, row: 0 } } },
    { field: "exaggeration", request: { ...baseRequest, displayExaggeration: 0 } },
    { field: "extra field", request: { ...baseRequest, extra: true } },
  ])("rejects invalid $field input", ({ request }) => {
    expect(() => sampleTerrariumElevationNearestCell(request as never)).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }),
    );
  });
});
