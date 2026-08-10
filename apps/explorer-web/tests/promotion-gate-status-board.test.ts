import { describe, expect, it } from "vitest";

import invalidExtra from "../../../fixtures/ui/promotion_gate_status_board_projection/invalid/extra-field.json";
import invalidSummary from "../../../fixtures/ui/promotion_gate_status_board_projection/invalid/summary-mismatch.json";
import deniedFixture from "../../../fixtures/ui/promotion_gate_status_board_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/promotion_gate_status_board_projection/valid/error.json";
import holdFixture from "../../../fixtures/ui/promotion_gate_status_board_projection/valid/hold.json";
import missingFixture from "../../../fixtures/ui/promotion_gate_status_board_projection/valid/missing.json";
import readyFixture from "../../../fixtures/ui/promotion_gate_status_board_projection/valid/ready-for-review.json";
import adapterSource from "../src/adapters/PromotionGateStatusBoardProjection.ts?raw";
import boardSource from "../src/features/promotion_gate_status_board/index.ts?raw";
import { resolvePromotionGateStatusBoard } from "../src/features/promotion_gate_status_board";

describe("Explorer promotion gate status board", () => {
  it("derives HOLD from held and not-run projected components", () => {
    const result = resolvePromotionGateStatusBoard(holdFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "BOARD_AVAILABLE",
      boardState: "HOLD",
      candidateRef: "kfm://release-candidate/synthetic/candidate-001",
      counts: { passCount: 3, holdCount: 1, notRunCount: 2 },
    });
    expect(result.components).toHaveLength(6);
    expect(result.summaryText).toContain("must remain blocked");
  });

  it("labels six passes READY_FOR_REVIEW without granting approval or release", () => {
    const result = resolvePromotionGateStatusBoard(readyFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      boardState: "READY_FOR_REVIEW",
      counts: { passCount: 6 },
    });
    expect(result.summaryText).toContain("not approved or released");
    expect(result.summaryText).toContain("does not execute checks");
  });

  it.each([
    [missingFixture, "ABSTAIN", "BOARD_UNAVAILABLE"],
    [deniedFixture, "DENY", "POLICY_DENIED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR"],
  ] as const)("renders fixed %s state without candidate detail", (fixture, outcome, code) => {
    const result = resolvePromotionGateStatusBoard(fixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome,
      code,
      candidateRef: null,
      components: [],
    });
    expect(JSON.stringify(result)).not.toContain("kfm://release-candidate/");
  });

  it.each([invalidExtra, invalidSummary])(
    "fails closed on unknown fields or summary contradictions",
    (fixture) => {
      const result = resolvePromotionGateStatusBoard(fixture);
      expect(result).toMatchObject({
        visibility: "HIDDEN",
        code: "INVALID_PAYLOAD",
        components: [],
      });
      expect(JSON.stringify(result)).not.toContain(
        "PROMOTION_BOARD_INTERNAL_CANARY_395de0",
      );
    },
  );

  it("renders nothing without a governed response", () => {
    expect(resolvePromotionGateStatusBoard()).toMatchObject({
      visibility: "HIDDEN",
      code: "NO_GOVERNED_RESPONSE",
    });
  });

  it("contains no execution, transport, storage, policy, signing, release, or model access", () => {
    const source = `${adapterSource}\n${boardSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/(?:evaluatePolicy|verifyAttestation|authorizeRelease|promoteCandidate)\s*\(/);
    expect(source).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
  });
});
