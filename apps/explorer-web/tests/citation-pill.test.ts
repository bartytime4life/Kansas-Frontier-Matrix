import { describe, expect, it } from "vitest";

import abstainFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/abstain-stale.json";
import answerFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import denyFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import errorFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/error-upstream.json";
import invalidExtraFieldFixture from "../../../fixtures/ui/evidence_drawer_payload/invalid/extra-field.json";
import citationPillSource from "../src/features/citation_pill/index.ts?raw";
import { resolveCitationPill } from "../src/features/citation_pill";

const TIMESTAMP = "1850-06-01T00:00:00Z";

describe("Explorer governed inline Citation Pill", () => {
  it("builds one bounded timestamped deep link for released supporting evidence", () => {
    const result = resolveCitationPill(answerFixture, {
      timestamp: TIMESTAMP,
      view: "focus",
    });

    expect(result).toMatchObject({
      visibility: "VISIBLE",
      reason: "SUPPORTED",
      status: "VERIFIED",
      label: "Evidence",
      title: "Synthetic streamflow observation",
      evidenceRef: "kfm:evidence:synthetic:flow-001",
      timestamp: TIMESTAMP,
      view: "focus",
      canCopy: true,
    });
    expect(result.deepLink).toBe(
      "kfm:evidence:synthetic:flow-001?t=1850-06-01T00%3A00%3A00Z&view=focus",
    );
  });

  it("uses the source packet's map view default and bounds caller labels", () => {
    const result = resolveCitationPill(answerFixture, {
      timestamp: TIMESTAMP,
      label: `  Synthetic   dataset ${"x".repeat(100)}  `,
    });

    expect(result.visibility).toBe("VISIBLE");
    expect(result.view).toBe("map");
    expect(result.label.length).toBeLessThanOrEqual(80);
    expect(result.label).toMatch(/^Synthetic dataset /);
  });

  it("requires explicit selection when a governed payload contains multiple evidence refs", () => {
    const multiEvidence = {
      ...answerFixture,
      evidence_refs: [
        "kfm:evidence:synthetic:flow-001",
        "kfm:evidence:synthetic:flow-002",
      ],
    };

    expect(resolveCitationPill(multiEvidence, { timestamp: TIMESTAMP })).toMatchObject({
      visibility: "HIDDEN",
      reason: "AMBIGUOUS_EVIDENCE",
      evidenceRef: null,
      deepLink: null,
    });

    expect(
      resolveCitationPill(multiEvidence, {
        timestamp: TIMESTAMP,
        evidenceRef: "kfm:evidence:synthetic:flow-002",
      }),
    ).toMatchObject({
      visibility: "VISIBLE",
      evidenceRef: "kfm:evidence:synthetic:flow-002",
    });
  });

  it("denies an explicit evidence ref that is not bound to the governed payload", () => {
    expect(
      resolveCitationPill(answerFixture, {
        timestamp: TIMESTAMP,
        evidenceRef: "kfm:evidence:synthetic:not-bound",
      }),
    ).toMatchObject({
      visibility: "HIDDEN",
      reason: "EVIDENCE_REF_NOT_BOUND",
      canCopy: false,
    });
  });

  for (const timestamp of [undefined, "1850-06-01", "1850-06-01T00:00:00.123Z"]) {
    it("fails closed when the exact UTC second is absent or malformed", () => {
      expect(resolveCitationPill(answerFixture, { timestamp })).toMatchObject({
        visibility: "HIDDEN",
        reason: "INVALID_TIMESTAMP",
        deepLink: null,
      });
    });
  }

  it("fails closed for an unsupported view", () => {
    expect(
      resolveCitationPill(answerFixture, {
        timestamp: TIMESTAMP,
        view: "globe" as never,
      }),
    ).toMatchObject({ visibility: "HIDDEN", reason: "INVALID_VIEW" });
  });

  for (const negative of [abstainFixture, denyFixture, errorFixture]) {
    it("withdraws the pill for every governed non-answer state without reflecting payload canaries", () => {
      const result = resolveCitationPill(negative, { timestamp: TIMESTAMP });
      const serialized = JSON.stringify(result);

      expect(result).toMatchObject({
        visibility: "HIDDEN",
        reason: "NON_ANSWER_OUTCOME",
        canCopy: false,
        evidenceRef: null,
        deepLink: null,
      });
      expect(serialized).not.toContain("SENSITIVE_DENIAL_CANARY_4d7ec2");
      expect(serialized).not.toContain("INTERNAL_ERROR_CANARY_e6f1af");
    });
  }

  it("fails closed on an invalid governed response without reflecting unknown fields", () => {
    const result = resolveCitationPill(invalidExtraFieldFixture, { timestamp: TIMESTAMP });

    expect(result).toMatchObject({
      visibility: "HIDDEN",
      reason: "INVALID_GOVERNED_RESPONSE",
      canCopy: false,
    });
    expect(JSON.stringify(result)).not.toContain("PRIVATE_FIELD_CANARY_981cba");
  });

  it("fails closed when no governed response exists", () => {
    expect(resolveCitationPill(undefined, { timestamp: TIMESTAMP })).toMatchObject({
      visibility: "HIDDEN",
      reason: "NO_GOVERNED_RESPONSE",
      canCopy: false,
    });
  });

  it("contains no browser-side transport, persistence, lifecycle-store, or model-runtime access", () => {
    expect(citationPillSource).not.toMatch(/\bfetch\s*\(/);
    expect(citationPillSource).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(citationPillSource).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(citationPillSource).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
    expect(citationPillSource).not.toMatch(/\b(?:window\.)?location\b/);
  });
});
