import { describe, expect, it } from "vitest";

import invalidExtraFieldFixture from "../../../fixtures/ui/time_scrubber_projection/invalid/extra-field.json";
import answerConflictFixture from "../../../fixtures/ui/time_scrubber_projection/valid/answer-conflict.json";
import answerCurrentFixture from "../../../fixtures/ui/time_scrubber_projection/valid/answer-current.json";
import answerStaleFixture from "../../../fixtures/ui/time_scrubber_projection/valid/answer-stale.json";
import denyPolicyFixture from "../../../fixtures/ui/time_scrubber_projection/valid/deny-policy.json";
import timeBannerSource from "../src/features/time_banner/index.tsx?raw";
import { resolveTimeScrubber } from "../src/features/time_banner";

describe("Explorer governed accessible Time Scrubber", () => {
  it("resolves a current released UTC projection into exact slider state", () => {
    const result = resolveTimeScrubber(answerCurrentFixture);

    expect(result).toMatchObject({
      visibility: "VISIBLE",
      reason: "SUPPORTED",
      minimumIso: "1850-06-01T00:00:00Z",
      maximumIso: "1850-06-01T00:10:00Z",
      selectedIso: "1850-06-01T00:05:00Z",
      timeKind: "SELECTED_TIME",
      precision: "SECOND",
      timezone: "UTC",
      ariaValueText: "1850-06-01 00:05:00Z",
      canInteract: true,
    });
    expect(result.minimumEpochSeconds).toBeLessThan(result.selectedEpochSeconds as number);
    expect(result.selectedEpochSeconds).toBeLessThan(result.maximumEpochSeconds as number);
  });

  it("fails closed for policy denial without reflecting internal detail", () => {
    const result = resolveTimeScrubber(denyPolicyFixture);

    expect(result).toMatchObject({
      visibility: "HIDDEN",
      reason: "NON_ANSWER_OUTCOME",
      canInteract: false,
      selectedIso: null,
    });
    expect(JSON.stringify(result)).not.toContain("SENSITIVE_TIME_DENIAL_CANARY_64ad31");
  });

  it("withdraws stale and temporally conflicted ANSWER projections", () => {
    expect(resolveTimeScrubber(answerStaleFixture)).toMatchObject({
      visibility: "HIDDEN",
      reason: "STALE_OR_UNKNOWN_TIME",
    });
    expect(resolveTimeScrubber(answerConflictFixture)).toMatchObject({
      visibility: "HIDDEN",
      reason: "TEMPORAL_CONFLICT",
    });
  });

  it("rejects extra fields without reflecting private values", () => {
    const result = resolveTimeScrubber(invalidExtraFieldFixture);

    expect(result).toMatchObject({
      visibility: "HIDDEN",
      reason: "INVALID_GOVERNED_TIME_STATE",
      canInteract: false,
    });
    expect(JSON.stringify(result)).not.toContain("PRIVATE_TIME_CANARY_9ff2ce");
  });

  it("rejects malformed, inverted, and out-of-range time state", () => {
    expect(
      resolveTimeScrubber({
        ...answerCurrentFixture,
        time: { ...answerCurrentFixture.time, selected: "1850-06-01" },
      }),
    ).toMatchObject({ reason: "INVALID_GOVERNED_TIME_STATE" });

    expect(
      resolveTimeScrubber({
        ...answerCurrentFixture,
        time: {
          ...answerCurrentFixture.time,
          minimum: "1850-06-01T00:10:00Z",
          maximum: "1850-06-01T00:00:00Z",
        },
      }),
    ).toMatchObject({ reason: "INVALID_GOVERNED_TIME_STATE" });

    expect(
      resolveTimeScrubber({
        ...answerCurrentFixture,
        time: { ...answerCurrentFixture.time, selected: "1850-06-01T00:10:01Z" },
      }),
    ).toMatchObject({ reason: "SELECTED_TIME_OUT_OF_RANGE" });
  });

  it("fails closed when governed time state is absent", () => {
    expect(resolveTimeScrubber()).toMatchObject({
      visibility: "HIDDEN",
      reason: "NO_GOVERNED_TIME_STATE",
      canInteract: false,
    });
  });

  it("contains no browser transport, persistence, lifecycle-store, or model access", () => {
    expect(timeBannerSource).not.toMatch(/\bfetch\s*\(/);
    expect(timeBannerSource).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(timeBannerSource).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(timeBannerSource).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
  });
});
