import { afterEach, describe, expect, it, vi } from "vitest";
import carrierText from "../../../fixtures/release/promotion_verification_execution/artifacts/synthetic_atlas_carrier.geojson?raw";
import referenceText from "../../../fixtures/release/promotion_verification_execution/references/evidence.json?raw";
import bundleText from "../../../fixtures/contracts/v1/evidence/evidence_bundle/valid/valid_3.json?raw";
import { parseEvidenceDrawerProjection } from "../src/adapters/GovernedClient";
import { resolveMapRuntimeSelectionEvidence } from "../src/features/map_runtime/runtime-evidence-binding";
import {
  fixtureProjectionForScenario,
  loadSyntheticAtlasFixture,
  type SyntheticAtlasScenario,
} from "./browser/synthetic-atlas-evidence.fixture";

afterEach(() => vi.unstubAllGlobals());

describe("digest-bound synthetic Atlas browser inputs", () => {
  it("binds the original carrier through a full fixture bundle and the existing admission/evidence seam without transport", async () => {
    const fetch = vi.fn(() => { throw new Error("Network must not be used."); });
    vi.stubGlobal("fetch", fetch);
    const packet = await loadSyntheticAtlasFixture();
    const carrier = JSON.parse(carrierText);
    const bundle = JSON.parse(bundleText);
    const source = packet.style.sources["source:synthetic-kansas-promotion-proof"];
    expect(source.type).toBe("geojson");
    if (source.type !== "geojson" || typeof source.data !== "object") throw new Error("Missing fixture GeoJSON.");
    expect(source.data).toEqual({
      type: "FeatureCollection",
      features: [{
        ...carrier.features[0],
        properties: { ...carrier.features[0].properties, fixture: true },
      }],
    });
    expect(carrier.features[0].properties).not.toHaveProperty("fixture");
    expect(packet.selection).toMatchObject({
      layerId: carrier.kfm.candidate_id,
      featureId: carrier.features[0].id,
      evidenceRefs: [bundle.bundle_id],
    });
    expect(packet).toMatchObject({
      lifecycleState: "FIXTURE",
      simulation: "SYNTHETIC_RELEASED_STATE_ONLY",
      timeStart: carrier.kfm.temporal.start,
      timeEnd: carrier.kfm.temporal.end,
    });
    expect(Object.values(packet.admission.authority)).toEqual([false, false, false, false]);
    const resolver = vi.fn(async () => packet.projection);
    const result = await resolveMapRuntimeSelectionEvidence(packet.selection, packet.admission, resolver);
    expect(result).toMatchObject({
      layerAdmission: { outcome: "PASS", authority: "NONE", registryMutated: false },
      evidence: { code: "SUPPORTED", drawer: { outcome: "ANSWER", evidenceRefs: [packet.evidenceRef] } },
    });
    expect(result.evidence.drawer.limitations.join(" ")).toContain("not actual review");
    expect(resolver).toHaveBeenCalledTimes(1);
    expect(fetch).not.toHaveBeenCalled();
  });

  it.each([
    ["carrierText", carrierText],
    ["referenceText", referenceText],
    ["bundleText", bundleText],
  ] as const)("rejects byte drift in %s even when the JSON meaning is unchanged", async (key, bytes) => {
    await expect(loadSyntheticAtlasFixture({ [key]: `${bytes}\n` })).rejects.toThrow("Synthetic fixture integrity mismatch.");
  });

  it("rejects an oversized fixture before interpreting it", async () => {
    await expect(loadSyntheticAtlasFixture({ carrierText: " ".repeat(32_769) })).rejects.toThrow("Synthetic fixture input exceeds its byte limit.");
  });

  it("does not permit a drawer bundle outside the selected candidate evidence scope", async () => {
    const packet = await loadSyntheticAtlasFixture();
    const result = await resolveMapRuntimeSelectionEvidence(
      { ...packet.selection, evidenceRefs: ["evidence:synthetic:unrelated:v1"] },
      packet.admission,
      async () => packet.projection,
    );
    expect(result.evidence.code).toBe("DRAWER_EVIDENCE_OUTSIDE_SELECTION");
    expect(result.evidence.drawer.outcome).not.toBe("ANSWER");
    expect(result.evidence.drawer.evidenceRefs).toEqual([]);
  });

  it.each([
    ["available", "ANSWER", "SUPPORTED"],
    ["no-results", "ABSTAIN", "MISSING_EVIDENCE"],
    ["stale", "ABSTAIN", "STALE_EVIDENCE"],
    ["deny", "DENY", "POLICY_DENIED"],
    ["error", "ERROR", "UPSTREAM_ERROR"],
  ] satisfies [SyntheticAtlasScenario, string, string][])("preserves the finite %s fixture scenario", async (scenario, outcome, reason) => {
    const packet = await loadSyntheticAtlasFixture();
    const projection = fixtureProjectionForScenario(packet, scenario);
    expect(parseEvidenceDrawerProjection(projection).ok).toBe(true);
    const result = await resolveMapRuntimeSelectionEvidence(packet.selection, packet.admission, async () => projection);
    expect(result.evidence.drawer).toMatchObject({ outcome, code: reason });
    if (scenario !== "available") {
      expect(result.evidence.drawer.evidenceRefs).toEqual([]);
      expect(result.evidence.drawer.citations).toEqual([]);
    }
  });
});
