/**
 * Browser-only composition input, owned by the Explorer test lane. Directory
 * Rules v2 (adopted by ADR-0029) keeps test instances in fixtures/ and this
 * application composition in apps/; ADR-0006 keeps renderer acquisition in the
 * package adapter. No source, schema, registry, or release authority is added.
 */
import carrierBytes from "../../../../fixtures/release/promotion_verification_execution/artifacts/synthetic_atlas_carrier.geojson?raw";
import referenceBytes from "../../../../fixtures/release/promotion_verification_execution/references/evidence.json?raw";
import bundleBytes from "../../../../fixtures/contracts/v1/evidence/evidence_bundle/valid/valid_3.json?raw";
import admissionCases from "../../../../fixtures/runtime/layer_manifest_admission/cases.json";
import {
  MAP_FEATURE_SELECTION_PROFILE,
  freezeMapFeatureSelection,
  type MapFeatureSelection,
} from "@kfm/maplibre";
import type { MapLibreSafeStyle } from "@kfm/maplibre/vite-adapter";
import {
  EVIDENCE_DRAWER_PROJECTION_PROFILE,
  parseEvidenceDrawerProjection,
} from "../../src/adapters/GovernedClient";
import { evaluateLayerManifestAdmission } from "../../src/features/map_runtime/layer_manifest_admission";

const CARRIER_DIGEST = "sha256:8ad3948994680b0e6a85a3eb4c82f69466d0c5c2baf4c15fb4e14e43c1acb26d";
const REFERENCE_DIGEST = "sha256:79aa8c518fe95922cc3c29567a5edf067a866a5b0036eb0133a930b73a2748f6";
const BUNDLE_DIGEST = "sha256:b84c2869e16f6c4050f1a5736fad57fd6fa3a9fb65bde5f4c709b0a8487c530f";
const CANDIDATE_ID = "overlay:synthetic-kansas-promotion-proof";
const EVIDENCE_REF = "evidence:synthetic:promotion-proof:v1";
const FEATURE_ID = "synthetic-kansas-test-extent";
const MAX_FIXTURE_BYTES = 32_768;

type FixtureCarrier = {
  type: "FeatureCollection";
  kfm: {
    candidate_id: string;
    fixture_only: boolean;
    truth_posture: string;
    lifecycle_state: string;
    temporal: { start: string; end: string };
    quality: { limitations: string[] };
  };
  features: {
    type: "Feature";
    id: string;
    properties: { classification: string; value: number };
    geometry: { type: "Polygon"; coordinates: number[][][] };
  }[];
};

type FixtureBundle = {
  bundle_id: string;
  claim_scope: string;
  evidence_refs: { ref: string; kind: string; bundle_ref: string }[];
  source_records: string[];
  citations: string[];
  transforms: string[];
  checksums: { carrier: string; promotion_evidence_reference: string };
  spec_hash: { value: string };
};

export type SyntheticAtlasScenario = "available" | "no-results" | "stale" | "deny" | "error";

export type SyntheticAtlasPacket = Readonly<{
  style: MapLibreSafeStyle;
  selection: MapFeatureSelection;
  admission: typeof admissionCases.base;
  projection: Readonly<Record<string, unknown>>;
  candidateId: string;
  featureId: string;
  evidenceRef: string;
  bundleId: string;
  carrierDigest: string;
  referenceDigest: string;
  bundleDigest: string;
  provenance: readonly string[];
  units: string;
  timeStart: string;
  timeEnd: string;
  source: string;
  lifecycleState: "FIXTURE";
  simulation: "SYNTHETIC_RELEASED_STATE_ONLY";
}>;

/** Overrides exist only for integrity-denial tests; none can change the pins. */
type FixtureInputBytes = Readonly<{
  carrierText?: string;
  referenceText?: string;
  bundleText?: string;
}>;

async function verifyBytes(text: string, expected: string): Promise<void> {
  const bytes = new TextEncoder().encode(text);
  if (bytes.byteLength > MAX_FIXTURE_BYTES) {
    throw new Error("Synthetic fixture input exceeds its byte limit.");
  }
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  const actual = `sha256:${Array.from(new Uint8Array(digest), (byte) => byte.toString(16).padStart(2, "0")).join("")}`;
  if (actual !== expected) throw new Error("Synthetic fixture integrity mismatch.");
}

/**
 * Verify local Vite-imported UTF-8 source bytes before interpreting any input.
 * All three documents have literal digest pins; no fetch or other transport is
 * performed. Schema validation of the bundle uses the existing repository
 * validator; these checks additionally bind its identity and source digests.
 */
export async function loadSyntheticAtlasFixture(
  input: FixtureInputBytes = {},
): Promise<SyntheticAtlasPacket> {
  const carrierText = input.carrierText ?? carrierBytes;
  const referenceText = input.referenceText ?? referenceBytes;
  const bundleText = input.bundleText ?? bundleBytes;
  await Promise.all([
    verifyBytes(carrierText, CARRIER_DIGEST),
    verifyBytes(referenceText, REFERENCE_DIGEST),
    verifyBytes(bundleText, BUNDLE_DIGEST),
  ]);
  const carrier = JSON.parse(carrierText) as FixtureCarrier;
  const reference = JSON.parse(referenceText) as {
    object_type: string; kind: string; ref_id: string;
    subject_spec_hash: string; artifact_digest: string;
  };
  const bundle = JSON.parse(bundleText) as FixtureBundle;
  if (
    carrier.type !== "FeatureCollection" ||
    carrier.kfm.candidate_id !== CANDIDATE_ID ||
    carrier.kfm.fixture_only !== true ||
    carrier.kfm.truth_posture !== "SYNTHETIC" ||
    carrier.kfm.lifecycle_state !== "FIXTURE" ||
    carrier.features.length !== 1 || carrier.features[0].id !== FEATURE_ID ||
    reference.object_type !== "ResolvedPromotionReference" ||
    reference.kind !== "EVIDENCE_BUNDLE" ||
    reference.ref_id !== EVIDENCE_REF ||
    reference.artifact_digest !== CARRIER_DIGEST ||
    bundle.bundle_id !== reference.ref_id ||
    bundle.spec_hash.value !== reference.subject_spec_hash ||
    bundle.checksums.carrier !== CARRIER_DIGEST ||
    bundle.checksums.promotion_evidence_reference !== REFERENCE_DIGEST ||
    bundle.evidence_refs.length !== 1 ||
    bundle.evidence_refs[0].ref !== CANDIDATE_ID ||
    bundle.evidence_refs[0].kind !== "artifact" ||
    bundle.evidence_refs[0].bundle_ref !== EVIDENCE_REF
  ) throw new Error("Synthetic fixture identity binding failed.");

  const sourceId = "source:synthetic-kansas-promotion-proof";
  // A display projection, not an edit or promotion of the pinned carrier.
  // The original feature identity and polygon are copied without remapping.
  const feature = structuredClone(carrier.features[0]);
  const style: MapLibreSafeStyle = {
    version: 8,
    sources: {
      [sourceId]: {
        type: "geojson",
        data: {
          type: "FeatureCollection",
          features: [{ ...feature, properties: { ...feature.properties, fixture: carrier.kfm.fixture_only } }],
        },
      },
    },
    layers: [
      { id: "synthetic-fixture-background", type: "background", paint: { "background-color": "#eaf0ed" } },
      {
        id: CANDIDATE_ID,
        type: "fill",
        source: sourceId,
        paint: { "fill-color": "#2f6f8e", "fill-opacity": 0.52, "fill-outline-color": "#082d49" },
      },
    ],
  };
  const selection = freezeMapFeatureSelection({
    profile: MAP_FEATURE_SELECTION_PROFILE,
    selectionId: "selection:synthetic-kansas-promotion-proof",
    layerId: CANDIDATE_ID,
    featureId: FEATURE_ID,
    evidenceRefs: [EVIDENCE_REF],
  });

  // Reuse the closed admission fixture. Its approved/released/signature fields
  // simulate a successful gate; they assert no actual approval or signature.
  const admission = structuredClone(admissionCases.base);
  admission.layer_id = CANDIDATE_ID;
  admission.manifest_id = `layer-manifest:${reference.subject_spec_hash.slice(7, 31)}`;
  admission.manifest_spec_hash = reference.subject_spec_hash;
  admission.release_binding.subject_manifest_id = admission.manifest_id;
  admission.release_binding.subject_spec_hash = admission.manifest_spec_hash;
  admission.release_binding.release_manifest_ref = "kfm://release/fixture/synthetic-kansas-promotion-proof";
  admission.runtime_request.layer_id = CANDIDATE_ID;
  if (evaluateLayerManifestAdmission(admission).outcome !== "PASS") {
    throw new Error("Synthetic fixture admission projection is invalid.");
  }

  const projection = Object.freeze({
    profile: EVIDENCE_DRAWER_PROJECTION_PROFILE,
    id: "kfm:drawer:synthetic-kansas-promotion-proof",
    outcome: "ANSWER",
    reason_code: "SUPPORTED",
    title: "Synthetic Kansas Atlas test extent",
    summary: "The selected polygon is the digest-verified synthetic Atlas carrier. Its fixture EvidenceBundle binds the original geometry and candidate identity; it makes no observed environmental claim.",
    evidence_refs: [bundle.bundle_id],
    citations: bundle.citations.map((href) => ({ label: "Pinned synthetic carrier source", href })),
    limitations: [
      ...carrier.kfm.quality.limitations,
      "Fixture-only released-state simulation: REVIEWED, RELEASED, admission PASS and signature flags are test inputs, not actual review, source admission, release or publication decisions.",
      "Coordinates: longitude/latitude in degrees. The value 1 is a dimensionless test marker, not a measurement. Times are a synthetic fixture interval in UTC.",
    ],
    trust_state: {
      source_role: "context",
      policy: "ALLOW", review: "REVIEWED", release: "RELEASED",
      freshness: "CURRENT", correction: "NONE",
    },
    history: { negative_outcomes: [], corrections: [] },
  });
  if (!parseEvidenceDrawerProjection(projection).ok) {
    throw new Error("Synthetic fixture evidence projection is invalid.");
  }

  return Object.freeze({
    style, selection, admission, projection,
    candidateId: CANDIDATE_ID, featureId: FEATURE_ID,
    evidenceRef: EVIDENCE_REF, bundleId: bundle.bundle_id,
    carrierDigest: CARRIER_DIGEST, referenceDigest: REFERENCE_DIGEST,
    bundleDigest: BUNDLE_DIGEST,
    provenance: Object.freeze([
      ...bundle.source_records,
      "fixtures/contracts/v1/evidence/evidence_bundle/valid/valid_3.json",
      ...bundle.transforms,
    ]),
    units: "longitude/latitude degrees; dimensionless fixture value",
    timeStart: carrier.kfm.temporal.start,
    timeEnd: carrier.kfm.temporal.end,
    source: bundle.source_records[0],
    lifecycleState: "FIXTURE",
    simulation: "SYNTHETIC_RELEASED_STATE_ONLY",
  });
}

/** Negative scenarios expose no current or unauthorized history references. */
export function fixtureProjectionForScenario(
  packet: SyntheticAtlasPacket,
  scenario: SyntheticAtlasScenario,
): Readonly<Record<string, unknown>> {
  if (scenario === "available") return packet.projection;
  const outcome = scenario === "deny" ? "DENY" : scenario === "error" ? "ERROR" : "ABSTAIN";
  const reason = scenario === "deny" ? "POLICY_DENIED" : scenario === "error" ? "UPSTREAM_ERROR" : scenario === "stale" ? "STALE_EVIDENCE" : "MISSING_EVIDENCE";
  const projection = Object.freeze({
    profile: EVIDENCE_DRAWER_PROJECTION_PROFILE,
    id: `kfm:drawer:synthetic-kansas-promotion-proof:${scenario}`,
    outcome, reason_code: reason,
    title: "Synthetic fixture negative state",
    summary: "No supported fixture claim is available for this scenario.",
    evidence_refs: [], citations: [],
    limitations: ["Fixture-only negative scenario; no unsupported claim is shown."],
    trust_state: {
      source_role: "context", policy: outcome, review: "PENDING",
      release: "UNRELEASED", freshness: scenario === "stale" ? "STALE" : "UNKNOWN",
      correction: "NONE",
    },
    history: { negative_outcomes: [], corrections: [] },
  });
  if (!parseEvidenceDrawerProjection(projection).ok) {
    throw new Error("Synthetic fixture negative projection is invalid.");
  }
  return projection;
}
