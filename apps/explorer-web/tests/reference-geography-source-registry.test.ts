import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import {
  KANSAS_COUNTY_REFERENCE_CANDIDATE,
  validateKansasCountyReferenceCandidate,
} from "../src/site/reference-geography-source-registry";

const SOURCE_DESCRIPTOR_PATH = new URL(
  "../../../data/registry/sources/settlements-infrastructure/census_cartographic_boundary_counties_2025_500k.source.json",
  import.meta.url,
);

const readSourceDescriptor = (): unknown =>
  JSON.parse(readFileSync(SOURCE_DESCRIPTOR_PATH, "utf8")) as unknown;

const clone = <T>(value: T): T =>
  JSON.parse(JSON.stringify(value)) as T;

describe("Kansas county reference-geography source registry", () => {
  it("exposes the verified archive facts on an explicit HOLD", () => {
    const candidate = KANSAS_COUNTY_REFERENCE_CANDIDATE;

    expect(validateKansasCountyReferenceCandidate()).toEqual([]);
    expect(candidate.state).toBe("VERIFIED_CANDIDATE_HOLD");
    expect(candidate.source).toEqual(
      expect.objectContaining({
        archiveUrl:
          "https://www2.census.gov/geo/tiger/GENZ2025/shp/cb_2025_us_county_500k.zip",
        archiveSha256:
          "aa976c00b181939755d0da757f4c7c2dc0103c3b3b4530fb2a91c2bb62fc777c",
        archiveBytes: 11_758_981,
        vintage: "2025-01-01",
        scale: "1:500,000",
        crs: "EPSG:4269",
      }),
    );
    expect(candidate.coverage.bbox).toEqual([
      -102.051744, 36.993016, -94.588413, 40.003162,
    ]);
    expect(candidate.integrity).toEqual({
      identitySha256:
        "ef0e2721bc98ee5542072e1f10e83c279551d73cd2db3e841f0a39da703d0e15",
      shapeRecordsSha256:
        "bb466162a735f1c386a10b7d06b4538f16ffd2fc340ba369540a17d4a1b91197",
    });
  });

  it("pins the complete ordered set of 105 Kansas county GEOIDs", () => {
    const expectedGeoids = Array.from(
      { length: 105 },
      (_, index) => `20${String(index * 2 + 1).padStart(3, "0")}`,
    );

    expect(KANSAS_COUNTY_REFERENCE_CANDIDATE.coverage).toEqual(
      expect.objectContaining({
        filter: "STATEFP=20",
        featureCount: 105,
        geoids: expectedGeoids,
      }),
    );
    expect(new Set(expectedGeoids).size).toBe(105);
  });

  it("keeps every admission, evidence, release, and runtime effect false", () => {
    const candidate = KANSAS_COUNTY_REFERENCE_CANDIDATE;

    expect(Object.values(candidate.governance)).toHaveLength(14);
    expect(Object.values(candidate.governance).every((value) => !value)).toBe(
      true,
    );
    expect(candidate.summary).toMatch(/unadmitted, unreleased, non-evidentiary/i);
    expect(candidate.nextGate).toMatch(/before any runtime binding/i);
    expect(candidate.limitations.join(" ")).toMatch(/not cadastral/i);
    expect(candidate.limitations.join(" ")).toMatch(/does not establish admission/i);
  });

  it("binds the display record to the repository SourceDescriptor", () => {
    const sourceDescriptor = readSourceDescriptor();

    expect(
      validateKansasCountyReferenceCandidate(
        KANSAS_COUNTY_REFERENCE_CANDIDATE,
        sourceDescriptor,
      ),
    ).toEqual([]);
    expect(KANSAS_COUNTY_REFERENCE_CANDIDATE.artifactPaths).toEqual({
      sourceDescriptor:
        "data/registry/sources/settlements-infrastructure/census_cartographic_boundary_counties_2025_500k.source.json",
      productDocumentation:
        "docs/sources/catalog/census/cartographic-boundary-files.md",
      archiveValidator:
        "tools/validators/source/census_cartographic_boundary_counties.py",
      archiveValidatorTests:
        "tests/source/test_census_cartographic_boundary_counties.py",
      validationReceipt:
        "data/receipts/generated/genrec-census-county-reference-candidate-20260910.json",
    });
  });

  it("returns deterministic failures for candidate drift", () => {
    const drifted = clone(KANSAS_COUNTY_REFERENCE_CANDIDATE) as unknown as {
      state: string;
      source: { archiveSha256: string };
      coverage: { geoids: string[] };
      artifactPaths: { validationReceipt: string };
      limitations: string[];
      governance: { runtimeBindingAllowed: boolean };
    };
    drifted.state = "ADMITTED";
    drifted.source.archiveSha256 = "0".repeat(64);
    drifted.coverage.geoids[0] = "20000";
    drifted.artifactPaths.validationReceipt = "data/receipts/generated/latest.json";
    drifted.limitations.pop();
    drifted.governance.runtimeBindingAllowed = true;

    expect(
      validateKansasCountyReferenceCandidate(
        drifted as unknown as Parameters<
          typeof validateKansasCountyReferenceCandidate
        >[0],
      ),
    ).toEqual([
      "STATE_NOT_HOLD",
      "ARCHIVE_IDENTITY_MISMATCH",
      "KANSAS_GEOID_SET_MISMATCH",
      "ARTIFACT_PATH_MISMATCH:validationReceipt",
      "LIMITATIONS_MISMATCH",
      "GOVERNANCE_EFFECT_NOT_FALSE",
    ]);
  });

  it("fails closed when SourceDescriptor identity or HOLD posture drifts", () => {
    const sourceDescriptor = clone(readSourceDescriptor()) as {
      source_head: { content_identity: { content_sha256: string } };
      public_release: { allowed: boolean };
    };
    sourceDescriptor.source_head.content_identity.content_sha256 = "f".repeat(64);
    sourceDescriptor.public_release.allowed = true;

    expect(
      validateKansasCountyReferenceCandidate(
        KANSAS_COUNTY_REFERENCE_CANDIDATE,
        sourceDescriptor,
      ),
    ).toEqual([
      "SOURCE_DESCRIPTOR_ARCHIVE_MISMATCH",
      "SOURCE_DESCRIPTOR_HOLD_MISMATCH",
    ]);
  });

  it("freezes the exported record and all directly consumable collections", () => {
    const candidate = KANSAS_COUNTY_REFERENCE_CANDIDATE;

    expect(Object.isFrozen(candidate)).toBe(true);
    expect(Object.isFrozen(candidate.source)).toBe(true);
    expect(Object.isFrozen(candidate.coverage)).toBe(true);
    expect(Object.isFrozen(candidate.coverage.geoids)).toBe(true);
    expect(Object.isFrozen(candidate.coverage.bbox)).toBe(true);
    expect(Object.isFrozen(candidate.integrity)).toBe(true);
    expect(Object.isFrozen(candidate.artifactPaths)).toBe(true);
    expect(Object.isFrozen(candidate.limitations)).toBe(true);
    expect(Object.isFrozen(candidate.governance)).toBe(true);
  });
});
