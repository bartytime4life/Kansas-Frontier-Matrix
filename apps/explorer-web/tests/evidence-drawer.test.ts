import { describe, expect, it } from "vitest";

import answerFixture from "../../../tests/fixtures/ui/evidence_drawer/answer.json";
import abstainFixture from "../../../tests/fixtures/ui/evidence_drawer/abstain-stale.json";
import denyFixture from "../../../tests/fixtures/ui/evidence_drawer/deny-sensitive.json";
import errorFixture from "../../../tests/fixtures/ui/evidence_drawer/error-upstream.json";
import invalidExtraFieldFixture from "../../../tests/fixtures/ui/evidence_drawer/invalid-extra-field.json";
import invalidMissingEvidenceFixture from "../../../tests/fixtures/ui/evidence_drawer/invalid-answer-missing-evidence.json";
import governedClientSource from "../src/adapters/GovernedClient.ts?raw";
import evidenceDrawerSource from "../src/features/evidence_drawer/index.tsx?raw";
import { resolveEvidenceDrawer } from "../src/features/evidence_drawer";

describe("Explorer Evidence Drawer governed projection", () => {
  it("renders a supported answer with citations and text trust labels", () => {
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

  it("rejects an ANSWER that lacks evidence and citations", () => {
    expect(resolveEvidenceDrawer(invalidMissingEvidenceFixture)).toMatchObject({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
    });
  });

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
