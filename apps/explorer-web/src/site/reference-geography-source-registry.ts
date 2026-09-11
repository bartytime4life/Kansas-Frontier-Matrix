export type ReferenceGeographyCandidateState = "VERIFIED_CANDIDATE_HOLD";

export interface ReferenceGeographySourceCandidate {
  readonly id: string;
  readonly title: string;
  readonly organization: string;
  readonly state: ReferenceGeographyCandidateState;
  readonly summary: string;
  readonly nextGate: string;
  readonly source: {
    readonly sourceId: string;
    readonly role: string;
    readonly archiveUrl: string;
    readonly archiveSha256: string;
    readonly archiveBytes: number;
    readonly vintage: string;
    readonly scale: string;
    readonly crs: string;
  };
  readonly coverage: {
    readonly filter: string;
    readonly featureCount: number;
    readonly geoids: readonly string[];
    readonly bbox: readonly [number, number, number, number];
  };
  readonly integrity: {
    readonly identitySha256: string;
    readonly shapeRecordsSha256: string;
  };
  readonly artifactPaths: {
    readonly sourceDescriptor: string;
    readonly productDocumentation: string;
    readonly archiveValidator: string;
    readonly archiveValidatorTests: string;
    readonly validationReceipt: string;
  };
  readonly limitations: readonly string[];
  readonly governance: {
    readonly connectorActivated: false;
    readonly sourcePayloadCommitted: false;
    readonly sourceAdmitted: false;
    readonly admissionReceiptIssued: false;
    readonly rightsReviewed: false;
    readonly domainReviewed: false;
    readonly evidenceBundleEmitted: false;
    readonly evidenceClaimAuthorized: false;
    readonly policyApproved: false;
    readonly releaseManifestIssued: false;
    readonly publicReleaseAllowed: false;
    readonly runtimeBindingAllowed: false;
    readonly mapLibreSourceCreated: false;
    readonly published: false;
  };
}

const EXPECTED_ARCHIVE_URL =
  "https://www2.census.gov/geo/tiger/GENZ2025/shp/cb_2025_us_county_500k.zip";
const EXPECTED_ARCHIVE_SHA256 =
  "aa976c00b181939755d0da757f4c7c2dc0103c3b3b4530fb2a91c2bb62fc777c";
const EXPECTED_ARCHIVE_BYTES = 11_758_981;
const EXPECTED_IDENTITY_SHA256 =
  "ef0e2721bc98ee5542072e1f10e83c279551d73cd2db3e841f0a39da703d0e15";
const EXPECTED_SHAPE_RECORDS_SHA256 =
  "bb466162a735f1c386a10b7d06b4538f16ffd2fc340ba369540a17d4a1b91197";
const EXPECTED_SUMMARY =
  "Offline archive identity and structure are verified for all 105 Kansas county GEOIDs. The candidate remains unadmitted, unreleased, non-evidentiary, and unbound from the map runtime.";
const EXPECTED_NEXT_GATE =
  "Independent rights, source, domain, evidence, policy, transform, release, correction, and rollback review is required before any runtime binding.";

const EXPECTED_KANSAS_GEOIDS = Object.freeze([
  "20001",
  "20003",
  "20005",
  "20007",
  "20009",
  "20011",
  "20013",
  "20015",
  "20017",
  "20019",
  "20021",
  "20023",
  "20025",
  "20027",
  "20029",
  "20031",
  "20033",
  "20035",
  "20037",
  "20039",
  "20041",
  "20043",
  "20045",
  "20047",
  "20049",
  "20051",
  "20053",
  "20055",
  "20057",
  "20059",
  "20061",
  "20063",
  "20065",
  "20067",
  "20069",
  "20071",
  "20073",
  "20075",
  "20077",
  "20079",
  "20081",
  "20083",
  "20085",
  "20087",
  "20089",
  "20091",
  "20093",
  "20095",
  "20097",
  "20099",
  "20101",
  "20103",
  "20105",
  "20107",
  "20109",
  "20111",
  "20113",
  "20115",
  "20117",
  "20119",
  "20121",
  "20123",
  "20125",
  "20127",
  "20129",
  "20131",
  "20133",
  "20135",
  "20137",
  "20139",
  "20141",
  "20143",
  "20145",
  "20147",
  "20149",
  "20151",
  "20153",
  "20155",
  "20157",
  "20159",
  "20161",
  "20163",
  "20165",
  "20167",
  "20169",
  "20171",
  "20173",
  "20175",
  "20177",
  "20179",
  "20181",
  "20183",
  "20185",
  "20187",
  "20189",
  "20191",
  "20193",
  "20195",
  "20197",
  "20199",
  "20201",
  "20203",
  "20205",
  "20207",
  "20209",
] as const);

const EXPECTED_KANSAS_BBOX = Object.freeze([
  -102.051744,
  36.993016,
  -94.588413,
  40.003162,
] as const);

const EXPECTED_ARTIFACT_PATHS = Object.freeze({
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
} as const);

const EXPECTED_LIMITATIONS = Object.freeze([
  "Generalized 1:500,000 federal-statistical county geometry for small-scale thematic mapping. It is not cadastral, survey, title, municipal-status, navigation, geocoding, area/perimeter, or legal-boundary authority. Preserve source-reported ALAND and AWATER rather than recomputing them from generalized geometry.",
  "The offline archive inspection verifies source identity and structure only; it does not establish admission, evidence, policy, review, release, publication, or runtime authority.",
] as const);

const FALSE_GOVERNANCE_KEYS = Object.freeze([
  "connectorActivated",
  "sourcePayloadCommitted",
  "sourceAdmitted",
  "admissionReceiptIssued",
  "rightsReviewed",
  "domainReviewed",
  "evidenceBundleEmitted",
  "evidenceClaimAuthorized",
  "policyApproved",
  "releaseManifestIssued",
  "publicReleaseAllowed",
  "runtimeBindingAllowed",
  "mapLibreSourceCreated",
  "published",
] as const);

export const KANSAS_COUNTY_REFERENCE_CANDIDATE = Object.freeze({
  id: "reference-census-kansas-counties-2025-500k",
  title:
    "U.S. Census Bureau 2025 Cartographic Boundary Counties — 1:500,000",
  organization: "U.S. Census Bureau, Geography Division",
  state: "VERIFIED_CANDIDATE_HOLD",
  summary: EXPECTED_SUMMARY,
  nextGate: EXPECTED_NEXT_GATE,
  source: Object.freeze({
    sourceId:
      "kfm://source/us/census/cartographic-boundary/counties-2025-500k",
    role: "authoritative_for_claim",
    archiveUrl: EXPECTED_ARCHIVE_URL,
    archiveSha256: EXPECTED_ARCHIVE_SHA256,
    archiveBytes: EXPECTED_ARCHIVE_BYTES,
    vintage: "2025-01-01",
    scale: "1:500,000",
    crs: "EPSG:4269",
  }),
  coverage: Object.freeze({
    filter: "STATEFP=20",
    featureCount: 105,
    geoids: EXPECTED_KANSAS_GEOIDS,
    bbox: EXPECTED_KANSAS_BBOX,
  }),
  integrity: Object.freeze({
    identitySha256: EXPECTED_IDENTITY_SHA256,
    shapeRecordsSha256: EXPECTED_SHAPE_RECORDS_SHA256,
  }),
  artifactPaths: EXPECTED_ARTIFACT_PATHS,
  limitations: EXPECTED_LIMITATIONS,
  governance: Object.freeze({
    connectorActivated: false,
    sourcePayloadCommitted: false,
    sourceAdmitted: false,
    admissionReceiptIssued: false,
    rightsReviewed: false,
    domainReviewed: false,
    evidenceBundleEmitted: false,
    evidenceClaimAuthorized: false,
    policyApproved: false,
    releaseManifestIssued: false,
    publicReleaseAllowed: false,
    runtimeBindingAllowed: false,
    mapLibreSourceCreated: false,
    published: false,
  }),
} as const satisfies ReferenceGeographySourceCandidate);

const isRecord = (value: unknown): value is Record<string, unknown> =>
  typeof value === "object" && value !== null && !Array.isArray(value);

const valuesEqual = (
  actual: readonly unknown[],
  expected: readonly unknown[],
): boolean =>
  actual.length === expected.length &&
  actual.every((value, index) => value === expected[index]);

const getNested = (root: Record<string, unknown>, path: readonly string[]) => {
  let value: unknown = root;
  for (const key of path) {
    if (!isRecord(value)) return undefined;
    value = value[key];
  }
  return value;
};

/**
 * Validates the complete display record against independently pinned constants.
 * Passing a parsed SourceDescriptor additionally proves that the display record
 * has not drifted from the repository-owned candidate identity. A clean result
 * confirms only deterministic record consistency; it grants no governance effect.
 */
export const validateKansasCountyReferenceCandidate = (
  candidate: ReferenceGeographySourceCandidate =
    KANSAS_COUNTY_REFERENCE_CANDIDATE,
  sourceDescriptor?: unknown,
): readonly string[] => {
  const issues: string[] = [];

  if (candidate.id !== "reference-census-kansas-counties-2025-500k") {
    issues.push("CANDIDATE_ID_MISMATCH");
  }
  if (
    candidate.title !==
      "U.S. Census Bureau 2025 Cartographic Boundary Counties — 1:500,000" ||
    candidate.organization !== "U.S. Census Bureau, Geography Division"
  ) {
    issues.push("SOURCE_PRESENTATION_MISMATCH");
  }
  if (candidate.state !== "VERIFIED_CANDIDATE_HOLD") {
    issues.push("STATE_NOT_HOLD");
  }
  if (candidate.summary !== EXPECTED_SUMMARY) {
    issues.push("SUMMARY_SCOPE_MISMATCH");
  }
  if (candidate.nextGate !== EXPECTED_NEXT_GATE) issues.push("NEXT_GATE_MISSING");

  if (
    candidate.source.sourceId !==
      "kfm://source/us/census/cartographic-boundary/counties-2025-500k" ||
    candidate.source.role !== "authoritative_for_claim"
  ) {
    issues.push("SOURCE_IDENTITY_MISMATCH");
  }
  if (
    candidate.source.archiveUrl !== EXPECTED_ARCHIVE_URL ||
    candidate.source.archiveSha256 !== EXPECTED_ARCHIVE_SHA256 ||
    candidate.source.archiveBytes !== EXPECTED_ARCHIVE_BYTES
  ) {
    issues.push("ARCHIVE_IDENTITY_MISMATCH");
  }
  if (
    candidate.source.vintage !== "2025-01-01" ||
    candidate.source.scale !== "1:500,000" ||
    candidate.source.crs !== "EPSG:4269"
  ) {
    issues.push("PRODUCT_PROFILE_MISMATCH");
  }

  if (
    candidate.coverage.filter !== "STATEFP=20" ||
    candidate.coverage.featureCount !== EXPECTED_KANSAS_GEOIDS.length ||
    !valuesEqual(candidate.coverage.geoids, EXPECTED_KANSAS_GEOIDS)
  ) {
    issues.push("KANSAS_GEOID_SET_MISMATCH");
  }
  if (!valuesEqual(candidate.coverage.bbox, EXPECTED_KANSAS_BBOX)) {
    issues.push("KANSAS_BBOX_MISMATCH");
  }
  if (
    candidate.integrity.identitySha256 !== EXPECTED_IDENTITY_SHA256 ||
    candidate.integrity.shapeRecordsSha256 !==
      EXPECTED_SHAPE_RECORDS_SHA256
  ) {
    issues.push("KANSAS_INTEGRITY_MISMATCH");
  }

  for (const [key, expected] of Object.entries(EXPECTED_ARTIFACT_PATHS)) {
    if (
      candidate.artifactPaths[
        key as keyof ReferenceGeographySourceCandidate["artifactPaths"]
      ] !== expected
    ) {
      issues.push(`ARTIFACT_PATH_MISMATCH:${key}`);
    }
  }
  if (!valuesEqual(candidate.limitations, EXPECTED_LIMITATIONS)) {
    issues.push("LIMITATIONS_MISMATCH");
  }

  const actualGovernanceKeys = Object.keys(candidate.governance).sort();
  const expectedGovernanceKeys = [...FALSE_GOVERNANCE_KEYS].sort();
  if (!valuesEqual(actualGovernanceKeys, expectedGovernanceKeys)) {
    issues.push("GOVERNANCE_FLAG_SET_MISMATCH");
  }
  if (
    FALSE_GOVERNANCE_KEYS.some(
      (key) => candidate.governance[key] !== false,
    )
  ) {
    issues.push("GOVERNANCE_EFFECT_NOT_FALSE");
  }

  if (sourceDescriptor !== undefined) {
    if (!isRecord(sourceDescriptor)) {
      issues.push("SOURCE_DESCRIPTOR_INVALID");
    } else {
      const endpoint = getNested(sourceDescriptor, ["access", "endpoints"]);
      const downloadEndpoint =
        Array.isArray(endpoint) && endpoint.length > 0 && isRecord(endpoint[0])
          ? endpoint[0]
          : undefined;
      const descriptorVersion = `${candidate.source.vintage}/${candidate.source.scale.replace(",", "")}`;

      if (
        sourceDescriptor.object_type !== "SourceDescriptor" ||
        sourceDescriptor.source_id !== candidate.source.sourceId ||
        sourceDescriptor.source_role !== candidate.source.role ||
        sourceDescriptor.title !== candidate.title ||
        getNested(sourceDescriptor, ["owner_or_steward", "name"]) !==
          candidate.organization
      ) {
        issues.push("SOURCE_DESCRIPTOR_IDENTITY_MISMATCH");
      }
      if (
        downloadEndpoint?.uri !== candidate.source.archiveUrl ||
        downloadEndpoint?.version !== descriptorVersion ||
        getNested(sourceDescriptor, [
          "source_head",
          "content_identity",
          "source_head_uri",
        ]) !== candidate.source.archiveUrl ||
        getNested(sourceDescriptor, [
          "source_head",
          "content_identity",
          "content_sha256",
        ]) !== candidate.source.archiveSha256 ||
        getNested(sourceDescriptor, [
          "source_head",
          "content_identity",
          "content_length",
        ]) !== candidate.source.archiveBytes ||
        getNested(sourceDescriptor, [
          "source_head",
          "content_identity",
          "upstream_version",
        ]) !== descriptorVersion
      ) {
        issues.push("SOURCE_DESCRIPTOR_ARCHIVE_MISMATCH");
      }
      if (
        getNested(sourceDescriptor, ["governance_refs", "source_registry_ref"]) !==
        candidate.artifactPaths.sourceDescriptor
      ) {
        issues.push("SOURCE_DESCRIPTOR_PATH_MISMATCH");
      }
      if (
        getNested(sourceDescriptor, ["admissibility_limits", "limitations"]) !==
        candidate.limitations[0]
      ) {
        issues.push("SOURCE_DESCRIPTOR_LIMITATIONS_MISMATCH");
      }
      if (
        getNested(sourceDescriptor, ["connectors", "activation_state"]) !==
          "disabled" ||
        getNested(sourceDescriptor, ["public_release", "allowed"]) !== false ||
        sourceDescriptor.release_state !== "not_released" ||
        sourceDescriptor.review_state !== "needs_review" ||
        getNested(sourceDescriptor, ["rights", "rights_status"]) !==
          "noassertion"
      ) {
        issues.push("SOURCE_DESCRIPTOR_HOLD_MISMATCH");
      }
    }
  }

  return Object.freeze(issues);
};
