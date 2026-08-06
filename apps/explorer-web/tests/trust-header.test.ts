import { describe, expect, it } from "vitest";

import abstainFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/abstain-stale.json";
import answerFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import denyFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import errorFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/error-upstream.json";
import invalidExtraFieldFixture from "../../../fixtures/ui/evidence_drawer_payload/invalid/extra-field.json";
import trustHeaderSource from "../src/features/trust_header/index.tsx?raw";
import { resolveTrustHeader } from "../src/features/trust_header";

describe("Explorer governed Trust Header", () => {
  it("projects released support into six text-first trust badges", () => {
    const result = resolveTrustHeader(answerFixture);
    const labels = Object.fromEntries(
      result.badges.map((item) => [item.label, item.value]),
    );

    expect(result).toMatchObject({
      visibility: "VISIBLE",
      state: "SUPPORTED",
      reason: "SUPPORTED",
      canOpenDrawer: true,
      accessibilityLabel: "Trust status: supported released evidence",
    });
    expect(labels).toEqual({
      Outcome: "ANSWER",
      Policy: "ALLOW",
      Review: "REVIEWED",
      Release: "RELEASED",
      Freshness: "CURRENT",
      Correction: "CORRECTED",
    });
  });

  it.each([
    ["ABSTAIN", abstainFixture, "Released evidence is not sufficient for this view."],
    ["DENY", denyFixture, "Policy does not permit this view to expose governed detail."],
    ["ERROR", errorFixture, "The governed trust projection could not be completed."],
  ] as const)(
    "narrows %s to generic no-leak copy",
    (state, fixture, expectedMessage) => {
      const result = resolveTrustHeader(fixture);
      const serialized = JSON.stringify(result);

      expect(result).toMatchObject({
        visibility: "VISIBLE",
        state,
        message: expectedMessage,
        canOpenDrawer: false,
      });
      expect(result.badges).toEqual([
        { key: "outcome", label: "Outcome", value: state },
      ]);
      expect(serialized).not.toContain("kfm:evidence:");
      expect(serialized).not.toContain("SENSITIVE_DENIAL_CANARY_4d7ec2");
      expect(serialized).not.toContain("INTERNAL_ERROR_CANARY_e6f1af");
    },
  );

  it("renders no header for a malformed governed response", () => {
    const result = resolveTrustHeader(invalidExtraFieldFixture);

    expect(result).toMatchObject({
      visibility: "HIDDEN",
      reason: "INVALID_GOVERNED_RESPONSE",
      canOpenDrawer: false,
    });
    expect(JSON.stringify(result)).not.toContain("PRIVATE_FIELD_CANARY_981cba");
  });

  it("renders no header when no governed response exists", () => {
    expect(resolveTrustHeader()).toMatchObject({
      visibility: "HIDDEN",
      reason: "NO_GOVERNED_RESPONSE",
      canOpenDrawer: false,
    });
  });

  it("contains no browser-side transport, persistence, lifecycle, or model access", () => {
    expect(trustHeaderSource).not.toMatch(/\bfetch\s*\(/);
    expect(trustHeaderSource).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(trustHeaderSource).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(trustHeaderSource).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
  });
});
