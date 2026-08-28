import { describe, expect, it } from "vitest";

import answerFixture from "../../../fixtures/ui/consent_card_projection/valid/answer-viewer-choice.json";
import abstainFixture from "../../../fixtures/ui/consent_card_projection/valid/abstain-unresolved.json";
import denyFixture from "../../../fixtures/ui/consent_card_projection/valid/deny-policy.json";
import errorFixture from "../../../fixtures/ui/consent_card_projection/valid/error-upstream.json";
import invalidExtraFieldFixture from "../../../fixtures/ui/consent_card_projection/invalid/extra-field.json";
import invalidMissingScopeFixture from "../../../fixtures/ui/consent_card_projection/invalid/answer-missing-scope.json";
import invalidSubjectFixture from "../../../fixtures/ui/consent_card_projection/invalid/answer-unresolved-subject.json";
import invalidReasonFixture from "../../../fixtures/ui/consent_card_projection/invalid/reason-mismatch.json";
import adapterSource from "../src/adapters/ConsentCardProjection.ts?raw";
import featureSource from "../src/features/consent_card/index.ts?raw";
import { parseConsentCardProjection } from "../src/adapters/ConsentCardProjection";
import { resolveConsentCard } from "../src/features/consent_card";

const FIXED_NOW = "2026-08-08T00:00:00Z";

describe("Explorer tiny consent card", () => {
  it("projects basis, scope, expiration, and a separate subject-consent label", () => {
    const result = resolveConsentCard(answerFixture, { now: FIXED_NOW });

    expect(result).toMatchObject({
      outcome: "ANSWER",
      code: "CONSENT_CARD_READY",
      title: "Synthetic generalized soil-moisture layer",
      layerRef: "kfm://layer/synthetic/soil-moisture-generalized",
      subjectConsentLabel:
        "Subject inclusion consent: not applicable to this projection.",
      viewerDecision: null,
      canOptIn: true,
      canWithdraw: false,
      canViewObligations: true,
      ariaLive: "polite",
    });
    expect(result.message).toContain(
      "does not grant or revoke a subject's consent to inclusion",
    );
    expect(result.scope).toEqual([
      "View aggregate values only",
      "No exact private locations",
      "No redistribution from this viewer surface",
    ]);
    expect(result.expirationLabel).toBe(
      "Expiration: 2099-08-08T00:00:00Z",
    );
  });

  it("reflects only the viewer's stored display decision", () => {
    const optedIn = resolveConsentCard(answerFixture, {
      now: FIXED_NOW,
      viewerDecision: "OPTED_IN",
    });
    const withdrawn = resolveConsentCard(answerFixture, {
      now: FIXED_NOW,
      viewerDecision: "WITHDRAWN",
    });

    expect(optedIn).toMatchObject({
      viewerDecision: "OPTED_IN",
      canOptIn: false,
      canWithdraw: true,
    });
    expect(withdrawn).toMatchObject({
      viewerDecision: "WITHDRAWN",
      canOptIn: true,
      canWithdraw: false,
    });
    expect(optedIn.subjectConsentLabel).toBe(withdrawn.subjectConsentLabel);
  });

  it("fails closed when an otherwise valid answer is expired", () => {
    const expired = {
      ...answerFixture,
      expires_at: "2026-08-07T23:59:59Z",
    };

    expect(
      resolveConsentCard(expired, { now: FIXED_NOW }),
    ).toMatchObject({
      outcome: "ABSTAIN",
      code: "CONSENT_EXPIRED",
      title: "Consent details expired",
      canOptIn: false,
      canWithdraw: false,
      canViewObligations: false,
    });
  });

  for (const negative of [
    {
      fixture: abstainFixture,
      outcome: "ABSTAIN",
      code: "CONSENT_UNRESOLVED",
      message: "Consent details are unresolved. The layer remains hidden.",
      canary: "CONSENT_UNRESOLVED_CANARY_71c9",
    },
    {
      fixture: denyFixture,
      outcome: "DENY",
      code: "POLICY_DENIED",
      message: "Policy does not permit this layer to be shown.",
      canary: "SENSITIVE_DENIAL_CANARY_4aa9",
    },
    {
      fixture: errorFixture,
      outcome: "ERROR",
      code: "UPSTREAM_ERROR",
      message:
        "The governed consent service could not complete the request. The layer remains hidden.",
      canary: "INTERNAL_ERROR_CANARY_2f61",
    },
  ] as const) {
    it(`uses fixed no-leak copy for ${negative.outcome}`, () => {
      const result = resolveConsentCard(negative.fixture, { now: FIXED_NOW });

      expect(result).toMatchObject({
        outcome: negative.outcome,
        code: negative.code,
        message: negative.message,
        layerRef: null,
        basis: null,
        scope: [],
        canOptIn: false,
        canWithdraw: false,
        canViewObligations: false,
      });
      expect(JSON.stringify(result)).not.toContain(negative.canary);
    });
  }

  for (const invalid of [
    invalidExtraFieldFixture,
    invalidMissingScopeFixture,
    invalidSubjectFixture,
    invalidReasonFixture,
  ]) {
    it("rejects malformed or contradictory projections", () => {
      expect(parseConsentCardProjection(invalid)).toEqual({
        ok: false,
        code: "MALFORMED_CONSENT_CARD_PROJECTION",
      });
      expect(resolveConsentCard(invalid, { now: FIXED_NOW })).toMatchObject({
        outcome: "ERROR",
        code: "INVALID_PAYLOAD",
      });
    });
  }

  it("does not reflect unknown-field values from an invalid payload", () => {
    const result = resolveConsentCard(invalidExtraFieldFixture, {
      now: FIXED_NOW,
    });
    expect(JSON.stringify(result)).not.toContain("PRIVATE_CONSENT_CANARY_11f0");
  });

  it("keeps the adapter and feature free of network and lifecycle-store reads", () => {
    const combined = `${adapterSource}\n${featureSource}`;

    expect(combined).not.toMatch(/\bfetch\s*\(/);
    expect(combined).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(combined).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
    expect(combined).not.toMatch(/POST\s+\/consent\//i);
  });
});
