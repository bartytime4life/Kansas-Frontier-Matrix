import { describe, expect, it } from "vitest";

import packet from "../../../fixtures/contracts/v1/domains/hydrology/living_waters_fixture_packet/valid/first_proof.json";
import {
  LIVING_WATERS_FRAME_STATES,
  LIVING_WATERS_SCENARIO_IDS,
  LIVING_WATERS_FIXTURE_PACKET_ID,
  type LivingWatersFixturePacket,
  projectLivingWatersFixture,
} from "../src/features/living_atlas";

const canonicalPacket: LivingWatersFixturePacket = packet;

describe("Living Waters fixture frame projection", () => {
  it("projects the canonical packet without creating source authority", () => {
    const frame = projectLivingWatersFixture(canonicalPacket, "current");

    expect(frame).toMatchObject({
      profile: "kfm.explorer.living-waters-fixture-projection.v1",
      packetId: LIVING_WATERS_FIXTURE_PACKET_ID,
      scenarioId: "current",
      state: "AVAILABLE",
      joinOutcome: "EXACT",
      spatial: {
        huc12: "102600150101",
        reachIds: ["fixture-reach-01", "fixture-reach-02"],
        spatialSupport: "generalized_county",
      },
      measurement: {
        parameterCode: "00060",
        parameterName: "discharge",
        statisticCode: "00000",
        statisticName: "instantaneous",
        unitCode: "ft3/s",
        qualifierCode: "P",
        qualifierName: "provisional",
        points: [
          { observedAt: "2026-09-10T12:00:00Z", value: 118 },
          { observedAt: "2026-09-10T12:15:00Z", value: 121 },
          { observedAt: "2026-09-10T12:30:00Z", value: 125 },
        ],
      },
      temporal: {
        observedAtStart: "2026-09-10T12:00:00Z",
        observedAtEnd: "2026-09-10T12:30:00Z",
        pointCount: 3,
      },
      trust: {
        state: "SITE_LOCAL_DEMO",
        fixtureRef: LIVING_WATERS_FIXTURE_PACKET_ID,
        evidenceRefs: [],
        sourceAdmitted: false,
        sourceActivated: false,
        released: false,
        deployed: false,
        published: false,
        fixtureOnly: true,
      },
      render: {
        layerId: "layer:watershed-storage",
        representation: "CATALOG_ONLY",
        visible: false,
        rendererBound: false,
      },
    });
    expect(frame.reasonCodes).toEqual(["FIXTURE_EVIDENCE_RESOLVED"]);
    expect(frame.displayMessage).toBe("Synthetic hydrograph available.");
  });

  it("keeps all five canonical scenarios finite and preserves stale history only", () => {
    expect(LIVING_WATERS_FRAME_STATES).toEqual([
      "AVAILABLE",
      "STALE",
      "NO_RESULTS",
      "UNAVAILABLE",
      "ABSTAIN",
    ]);
    expect(LIVING_WATERS_SCENARIO_IDS).toEqual([
      "current",
      "stale",
      "no-results",
      "unavailable",
      "ambiguous-reach",
    ]);

    expect(projectLivingWatersFixture(canonicalPacket, "stale")).toMatchObject({
      state: "STALE",
      joinOutcome: "EXACT",
      temporal: { pointCount: 3 },
      render: { visible: false, rendererBound: false },
    });

    for (const scenarioId of ["no-results", "unavailable"] as const) {
      const frame = projectLivingWatersFixture(canonicalPacket, scenarioId);
      expect(frame.state).not.toBe("AVAILABLE");
      expect(frame.measurement.points).toEqual([]);
      expect(frame.temporal).toMatchObject({
        observedAtStart: null,
        observedAtEnd: null,
        pointCount: 0,
      });
    }

    const ambiguous = projectLivingWatersFixture(canonicalPacket, "ambiguous-reach");
    expect(ambiguous).toMatchObject({
      state: "ABSTAIN",
      joinOutcome: "AMBIGUOUS",
      reasonCodes: ["MULTIPLE_REACH_CANDIDATES"],
      measurement: { points: [] },
      trust: { evidenceRefs: [], fixtureOnly: true },
    });
  });

  it("rejects a packet that crosses the fixture-only governance boundary", () => {
    expect(() =>
      projectLivingWatersFixture(
        {
          ...canonicalPacket,
          governance: { ...canonicalPacket.governance, source_activated: true },
        },
        "current",
      ),
    ).toThrow("LIVING_WATERS_FIXTURE_GOVERNANCE_BOUNDARY_VIOLATION");

    expect(() =>
      projectLivingWatersFixture(
        { ...canonicalPacket, profile: "live-source-v1" },
        "current",
      ),
    ).toThrow("LIVING_WATERS_FIXTURE_IDENTITY_MISMATCH");
  });
});

