import { describe, expect, it } from "vitest";

import invalidExtra from "../../../fixtures/ui/attestation_badge_projection/invalid/extra-field.json";
import invalidMissing from "../../../fixtures/ui/attestation_badge_projection/invalid/verified-missing-reference.json";
import errorFixture from "../../../fixtures/ui/attestation_badge_projection/valid/error.json";
import failedFixture from "../../../fixtures/ui/attestation_badge_projection/valid/failed.json";
import incompleteFixture from "../../../fixtures/ui/attestation_badge_projection/valid/incomplete.json";
import verifiedFixture from "../../../fixtures/ui/attestation_badge_projection/valid/verified.json";
import adapterSource from "../src/adapters/AttestationBadgeProjection.ts?raw";
import badgeSource from "../src/features/attestation_badge/index.ts?raw";
import { resolveAttestationBadge } from "../src/features/attestation_badge";

describe("Explorer receipt-linked attestation badge", () => {
  it("exposes a compact inspectable signal only for complete verified references", () => {
    expect(resolveAttestationBadge(verifiedFixture)).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "CHECKS_VERIFIED",
      status: "VERIFIED",
      label: "Verification evidence available",
      canInspect: true,
      accessibilityLabel: "Attestation status: checks reported verified",
    });
  });

  it.each([
    [incompleteFixture, "ABSTAIN", "CHECKS_INCOMPLETE", "INCOMPLETE"],
    [failedFixture, "DENY", "CHECKS_FAILED", "FAILED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR", "ERROR"],
  ] as const)(
    "projects %s without exposing proof references",
    (fixture, outcome, code, status) => {
      const result = resolveAttestationBadge(fixture);
      expect(result).toMatchObject({
        visibility: "VISIBLE",
        outcome,
        code,
        status,
        canInspect: false,
      });
      expect(JSON.stringify(result)).not.toContain("kfm://");
    },
  );

  it.each([invalidExtra, invalidMissing])(
    "fails closed on malformed or contradictory positive closure",
    (fixture) => {
      const result = resolveAttestationBadge(fixture);
      expect(result).toMatchObject({
        visibility: "HIDDEN",
        code: "INVALID_PAYLOAD",
        canInspect: false,
      });
      expect(JSON.stringify(result)).not.toContain(
        "ATTESTATION_INTERNAL_CANARY_845ad2",
      );
    },
  );

  it("renders no badge without a governed projection", () => {
    expect(resolveAttestationBadge()).toMatchObject({
      visibility: "HIDDEN",
      code: "NO_GOVERNED_RESPONSE",
    });
  });

  it("contains no browser transport, persistence, cryptography, lifecycle, or model access", () => {
    const source = `${adapterSource}\n${badgeSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(/\b(?:crypto|subtle|verify)\s*\(/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
  });
});
