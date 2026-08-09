import { describe, expect, it } from "vitest";
import fixtureSuite from "../../../fixtures/runtime/layer_manifest_admission/cases.json";
import moduleSource from "../src/features/map_runtime/layer_manifest_admission.ts?raw";
import { evaluateLayerManifestAdmission } from "../src/features/map_runtime/layer_manifest_admission";

type Candidate = typeof fixtureSuite.base;
function clone<T>(value: T): T {
  return JSON.parse(JSON.stringify(value)) as T;
}
function mutate(base: Candidate, name: string): unknown {
  const value = clone(base);
  if (name === "NONE") return value;
  if (name === "LEGACY") value.manifest_profile = "LEGACY";
  else if (name === "INACTIVE") value.profile_status = "PROPOSED_INACTIVE";
  else if (name === "CANDIDATE") value.lifecycle_state = "CANDIDATE";
  else if (name === "STALE") value.trust_state = "STALE";
  else if (name === "WITHDRAWN") value.release_binding.release_state = "WITHDRAWN";
  else if (name === "SUPERSEDED") value.release_binding.correction_state = "SUPERSEDED";
  else if (name === "EVIDENCE_UNRESOLVED") value.release_binding.evidence_resolved = false;
  else if (name === "POLICY_DENIED") value.release_binding.policy_allowed = false;
  else if (name === "SUBJECT_MISMATCH") value.release_binding.subject_spec_hash = `sha256:${"2b".repeat(32)}`;
  else if (name === "DIRECT_INTERNAL_SOURCE") value.runtime_request.source_url_class = "CANONICAL_INTERNAL";
  else if (name === "AUTHORITY_OVERCLAIM") value.authority.public_use_authorized = true;
  else if (name === "INVALID_SHAPE") return { ...value, unexpected: true };
  else throw new Error(`unknown mutation: ${name}`);
  return value;
}

describe("LayerManifest runtime admission fixture", () => {
  it("replays exact finite outcomes", () => {
    expect(fixtureSuite.profile).toBe("kfm.layer-manifest-admission-fixtures.v1");
    for (const declared of fixtureSuite.cases) {
      expect(evaluateLayerManifestAdmission(mutate(fixtureSuite.base, declared.mutation)), declared.case_id)
        .toMatchObject({ outcome: declared.expected_outcome, code: declared.expected_code });
    }
  });
  it("does not mutate a runtime registry or create a MapLibre source", () => {
    expect(evaluateLayerManifestAdmission(clone(fixtureSuite.base))).toEqual({
      outcome: "PASS",
      code: "LAYER_MANIFEST_REGISTER_ELIGIBLE",
      authority: "NONE",
      registryMutated: false,
      maplibreSourceCreated: false,
      registrationEligible: true,
      holds: ["RUNTIME_REGISTRATION_NOT_EXECUTED"],
    });
  });
  it("contains no transport, MapLibre import, or registry mutation shortcut", () => {
    for (const forbidden of ["fetch(", "XMLHttpRequest", "WebSocket", 'from "maplibre', "addSource(", "registry.set(", "registry.push("]) {
      expect(moduleSource).not.toContain(forbidden);
    }
    expect(moduleSource).toContain('source_url_class !== "GOVERNED_API"');
    expect(moduleSource).toContain('authority: "NONE"');
  });
});
