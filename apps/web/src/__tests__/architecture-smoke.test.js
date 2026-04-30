import { describe, expect, it } from "vitest";

import { createGovernedApiClient } from "../api/governedClient.js";
import { EVIDENCE_DRAWER_FIXTURE } from "../fixtures/publicSafeFixtures.js";
import { releasedLayerDescriptors } from "../map/layers/fromGovernedManifest.js";
import { createViewSessionState } from "../state/viewSessionState.js";

describe("web architecture scaffolding", () => {
  it("exposes a governed API client surface", () => {
    const client = createGovernedApiClient();
    expect(typeof client.getLayerManifest).toBe("function");
    expect(typeof client.getEvidenceDrawerPayload).toBe("function");
    expect(typeof client.getFocusOutcome).toBe("function");
  });

  it("filters map layers to released-only descriptors", () => {
    const descriptors = releasedLayerDescriptors({
      layers: [
        { id: "one", type: "fill", source: { kind: "released" } },
        { id: "two", type: "line", source: { kind: "work" } }
      ]
    });
    expect(descriptors).toHaveLength(1);
    expect(descriptors[0].id).toBe("one");
  });

  it("keeps fixture payload public-safe", () => {
    expect(EVIDENCE_DRAWER_FIXTURE.claimId).toContain("claim.");
    expect(EVIDENCE_DRAWER_FIXTURE.sources).toHaveLength(1);
  });

  it("initializes ephemeral view state", () => {
    const state = createViewSessionState();
    expect(state.evidenceDrawerOpen).toBe(false);
  });
});
