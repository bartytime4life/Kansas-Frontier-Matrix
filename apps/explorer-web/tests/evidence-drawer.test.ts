import { describe, expect, it } from "vitest";

import answerFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import abstainFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/abstain-stale.json";
import supersededFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/abstain-superseded.json";
import denyFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import errorFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/error-upstream.json";
import invalidExtraFieldFixture from "../../../fixtures/ui/evidence_drawer_payload/invalid/extra-field.json";
import invalidMissingEvidenceFixture from "../../../fixtures/ui/evidence_drawer_payload/invalid/answer-missing-evidence.json";
import invalidCorrectionFixture from "../../../fixtures/ui/evidence_drawer_payload/invalid/corrected-answer-without-history.json";
import invalidDenyHistoryFixture from "../../../fixtures/ui/evidence_drawer_payload/invalid/deny-history-leak.json";
import invalidCycleFixture from "../../../fixtures/ui/evidence_drawer_payload/invalid/correction-cycle.json";
import governedClientSource from "../src/adapters/GovernedClient.ts?raw";
import evidenceDrawerSource from "../src/features/evidence_drawer/index.tsx?raw";
import { resolveEvidenceDrawer } from "../src/features/evidence_drawer";

describe("Explorer Evidence Drawer governed projection", () => {
  it("renders a corrected answer with citations and auditable prior history", () => {
    const result = resolveEvidenceDrawer(answerFixture);

    expect(result).toMatchObject({
      outcome: "ANSWER",
      code: "SUPPORTED",
      title: "Synthetic streamflow observation",
      landmarkRole: "complementary",
      accessibilityLabel: "Evidence Drawer: supported evidence",
      ariaLive: "polite",
    });
    expect(result.evidenceRefs).toEqual(["kfm:evidence:synthetic:flow-001"]);
    expect(result.citations).toHaveLength(1);
    expect(result.trustLabels).toContain("Policy: ALLOW");
    expect(result.trustLabels).toContain("Correction: CORRECTED");
    expect(result.historyLabels).toContain(
      "Correction lineage: kfm:evidence:synthetic:flow-000 → kfm:evidence:synthetic:flow-001 (2026-08-01T00:00:00Z)",
    );
    expect(result.historyLabels.join(" ")).toContain("Superseded evidence");
  });

  it("keeps stale support visible while abstaining", () => {
    const result = resolveEvidenceDrawer(abstainFixture);

    expect(result).toMatchObject({
      outcome: "ABSTAIN",
      code: "STALE_EVIDENCE",
      title: "Evidence not sufficient",
      message: "Available evidence is stale for this request.",
    });
    expect(result.evidenceRefs).toEqual(["kfm:evidence:synthetic:stale-001"]);
    expect(result.citations).toEqual([]);
    expect(result.trustLabels).toContain("Freshness: STALE");
  });

  it("shows superseded evidence as history without current claim support", () => {
    const result = resolveEvidenceDrawer(supersededFixture);
    expect(result).toMatchObject({
      outcome: "ABSTAIN",
      code: "SUPERSEDED_EVIDENCE",
      message: "The available evidence is superseded and is shown only as history.",
    });
    expect(result.evidenceRefs).toEqual([]);
    expect(result.historyLabels.join(" ")).toContain(
      "kfm:evidence:synthetic:superseded-001",
    );
    expect(result.historyLabels.join(" ")).not.toContain(
      "SUPERSEDED_SUMMARY_MUST_NOT_RENDER_AS_CURRENT",
    );
  });

  it("does not reflect governed-payload text from a denied state", () => {
    const forbiddenCanary = "SENSITIVE_DENIAL_CANARY_4d7ec2";
    const result = resolveEvidenceDrawer(denyFixture);

    expect(result).toMatchObject({
      outcome: "DENY",
      code: "SENSITIVE_DETAIL_RESTRICTED",
      message: "Sensitive detail is restricted.",
    });
    expect(JSON.stringify(result)).not.toContain(forbiddenCanary);
    expect(result.evidenceRefs).toEqual([]);
    expect(result.citations).toEqual([]);
    expect(result.historyLabels).toEqual([]);
  });

  it("uses a fixed upstream error without exposing diagnostic text", () => {
    const forbiddenCanary = "INTERNAL_ERROR_CANARY_e6f1af";
    const result = resolveEvidenceDrawer(errorFixture);

    expect(result).toMatchObject({
      outcome: "ERROR",
      code: "UPSTREAM_ERROR",
      ariaLive: "assertive",
    });
    expect(JSON.stringify(result)).not.toContain(forbiddenCanary);
  });

  it("fails closed on unknown fields without reflecting their values", () => {
    const forbiddenCanary = "PRIVATE_FIELD_CANARY_981cba";
    const result = resolveEvidenceDrawer(invalidExtraFieldFixture);

    expect(result).toMatchObject({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
      message: "The governed evidence response is invalid.",
    });
    expect(JSON.stringify(result)).not.toContain(forbiddenCanary);
  });

  for (const invalid of [
    invalidMissingEvidenceFixture,
    invalidCorrectionFixture,
    invalidDenyHistoryFixture,
    invalidCycleFixture,
  ]) {
    it("rejects an internally contradictory projection", () => {
      expect(resolveEvidenceDrawer(invalid)).toMatchObject({
        outcome: "ERROR",
        code: "INVALID_PAYLOAD",
      });
    });
  }

  it("rejects oversized arrays at the adapter boundary", () => {
    const oversized = {
      ...answerFixture,
      evidence_refs: Array.from(
        { length: 17 },
        (_, index) => `kfm:evidence:synthetic:${index}`,
      ),
    };

    expect(resolveEvidenceDrawer(oversized)).toMatchObject({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
    });
  });

  it("keeps browser feature code free of network and lifecycle-store reads", () => {
    const combinedSource = `${governedClientSource}\n${evidenceDrawerSource}`;

    expect(combinedSource).not.toMatch(/\bfetch\s*\(/);
    expect(combinedSource).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(combinedSource).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
  });
});
