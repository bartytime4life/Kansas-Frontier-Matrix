import { describe, expect, it } from "vitest";

import invalidExtra from "../../../fixtures/ui/county_environmental_cadence_projection/invalid/extra-field.json";
import invalidSummary from "../../../fixtures/ui/county_environmental_cadence_projection/invalid/summary-mismatch.json";
import completeFixture from "../../../fixtures/ui/county_environmental_cadence_projection/valid/complete.json";
import deniedFixture from "../../../fixtures/ui/county_environmental_cadence_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/county_environmental_cadence_projection/valid/error.json";
import holdFixture from "../../../fixtures/ui/county_environmental_cadence_projection/valid/hold.json";
import missingFixture from "../../../fixtures/ui/county_environmental_cadence_projection/valid/missing.json";
import adapterSource from "../src/adapters/CountyEnvironmentalCadenceProjection.ts?raw";
import calendarSource from "../src/features/county_environmental_cadence_calendar/index.ts?raw";
import { resolveCountyEnvironmentalCadenceCalendar } from "../src/features/county_environmental_cadence_calendar";

describe("Explorer county environmental cadence calendar", () => {
  it("shows a coherent six-lane complete week", () => {
    const result = resolveCountyEnvironmentalCadenceCalendar(completeFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "CALENDAR_AVAILABLE",
      county: { stateCode: "KS" },
      week: { cadenceHours: 168 },
      summary: {
        laneCount: 6,
        recordedCount: 6,
        holdCount: 0,
        overallOutcome: "COMPLETE",
      },
    });
    expect(result.lanes.map((lane) => lane.lane)).toEqual([
      "AIR",
      "BIODIVERSITY",
      "HYDROLOGY",
      "IMAGERY",
      "SOILS",
      "VEGETATION",
    ]);
  });

  it("makes stale and missed lanes visible without interpreting conditions", () => {
    const result = resolveCountyEnvironmentalCadenceCalendar(holdFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      summary: {
        recordedCount: 5,
        holdCount: 2,
        overallOutcome: "HOLD",
      },
    });
    expect(result.lanes[0]).toMatchObject({
      lane: "AIR",
      healthOutcome: "STALE",
      reasonCode: "SOURCE_STALE",
    });
    expect(result.lanes[1]).toMatchObject({
      lane: "BIODIVERSITY",
      checkedAt: null,
      checkResult: "MISSED",
      reasonCode: "CHECK_MISSING",
    });
    expect(result.message).toContain("does not probe sources");
  });

  it.each([
    [missingFixture, "ABSTAIN", "CALENDAR_MISSING"],
    [deniedFixture, "DENY", "POLICY_DENIED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR"],
  ] as const)("renders %s without county or source detail", (fixture, outcome, code) => {
    const result = resolveCountyEnvironmentalCadenceCalendar(fixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome,
      code,
      county: null,
      week: null,
      lanes: [],
      summary: null,
      sourceAvailabilityWatchlistRef: null,
    });
    expect(JSON.stringify(result)).not.toContain("kfm://");
  });

  it.each([invalidExtra, invalidSummary])(
    "fails closed on extra fields or incoherent rollup",
    (fixture) => {
      const result = resolveCountyEnvironmentalCadenceCalendar(fixture);
      expect(result).toMatchObject({
        visibility: "HIDDEN",
        code: "INVALID_PAYLOAD",
        county: null,
        lanes: [],
        summary: null,
      });
      expect(JSON.stringify(result)).not.toContain(
        "CADENCE_INTERNAL_CANARY_36ad0e",
      );
    },
  );

  it("renders nothing without a governed projection", () => {
    expect(resolveCountyEnvironmentalCadenceCalendar()).toMatchObject({
      visibility: "HIDDEN",
      code: "NO_GOVERNED_RESPONSE",
    });
  });

  it("contains no transport, persistence, lifecycle mutation, or model access", () => {
    const source = `${adapterSource}\n${calendarSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
    expect(source).not.toMatch(
      /(?:probeSource|authorSourceHealth|interpretConditions|promoteArtifact|authorizeRelease|publishArtifact)\s*\(/,
    );
  });
});
