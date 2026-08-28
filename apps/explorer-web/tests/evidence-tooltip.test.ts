import { describe, expect, it } from "vitest";

import abstainFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/abstain-stale.json";
import answerFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import denyFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import errorFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/error-upstream.json";
import invalidExtraFieldFixture from "../../../fixtures/ui/evidence_drawer_payload/invalid/extra-field.json";
import evidenceTooltipSource from "../src/features/evidence_tooltip/index.ts?raw";
import { resolveEvidenceTooltip } from "../src/features/evidence_tooltip";

describe("Explorer governed Evidence Tooltip", () => {
  it("shows a bounded trust snapshot for released supporting evidence", () => {
    const result = resolveEvidenceTooltip(answerFixture);

    expect(result).toMatchObject({
      visibility: "VISIBLE",
      reason: "SUPPORTED",
      title: "Synthetic streamflow observation",
      canOpenDrawer: true,
      accessibilityLabel: "Evidence tooltip: released supporting evidence",
    });
    expect(result.evidenceRefs).toEqual(["kfm:evidence:synthetic:flow-001"]);
    expect(result.citationLabels).toEqual(["Synthetic fixture evidence"]);
    expect(result.trustLabels).toContain("Policy: ALLOW");
    expect(result.trustLabels).toContain("Release: RELEASED");
    expect(result.trustLabels).toContain("Correction: CORRECTED");
  });

  it("limits tooltip evidence and citation summaries", () => {
    const expanded = {
      ...answerFixture,
      evidence_refs: [
        "kfm:evidence:synthetic:flow-001",
        "kfm:evidence:synthetic:flow-002",
        "kfm:evidence:synthetic:flow-003",
        "kfm:evidence:synthetic:flow-004",
      ],
      citations: [
        ...answerFixture.citations,
        { label: "Second citation", href: "https://example.invalid/kfm/evidence/2" },
        { label: "Third citation", href: "https://example.invalid/kfm/evidence/3" },
        { label: "Fourth citation", href: "https://example.invalid/kfm/evidence/4" },
      ],
    };

    const result = resolveEvidenceTooltip(expanded, {
      maxEvidenceRefs: 2,
      maxCitations: 2,
    });

    expect(result.visibility).toBe("VISIBLE");
    expect(result.evidenceRefs).toHaveLength(2);
    expect(result.citationLabels).toHaveLength(2);
  });

  for (const negative of [abstainFixture, denyFixture, errorFixture]) {
    it("withdraws the tooltip for every finite non-answer state", () => {
      const serialized = JSON.stringify(resolveEvidenceTooltip(negative));

      expect(resolveEvidenceTooltip(negative)).toMatchObject({
        visibility: "HIDDEN",
        reason: "NON_ANSWER_OUTCOME",
        canOpenDrawer: false,
        evidenceRefs: [],
        citationLabels: [],
      });
      expect(serialized).not.toContain("SENSITIVE_DENIAL_CANARY_4d7ec2");
      expect(serialized).not.toContain("INTERNAL_ERROR_CANARY_e6f1af");
    });
  }

  it("fails closed on an invalid governed response without reflecting unknown fields", () => {
    const result = resolveEvidenceTooltip(invalidExtraFieldFixture);

    expect(result).toMatchObject({
      visibility: "HIDDEN",
      reason: "INVALID_GOVERNED_RESPONSE",
      canOpenDrawer: false,
    });
    expect(JSON.stringify(result)).not.toContain("PRIVATE_FIELD_CANARY_981cba");
  });

  it("fails closed when no governed response exists", () => {
    expect(resolveEvidenceTooltip()).toMatchObject({
      visibility: "HIDDEN",
      reason: "NO_GOVERNED_RESPONSE",
      canOpenDrawer: false,
    });
  });

  it("contains no browser-side transport or lifecycle-store access", () => {
    expect(evidenceTooltipSource).not.toMatch(/\bfetch\s*\(/);
    expect(evidenceTooltipSource).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(evidenceTooltipSource).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(evidenceTooltipSource).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
  });
});
