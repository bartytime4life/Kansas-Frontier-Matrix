import { describe, expect, it } from "vitest";

import driftReviewFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/abstain-source-drift-review.json";
import quarantinedRightsFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/deny-source-quarantined-rights.json";
import missingSidecarFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/abstain-missing-sidecar.json";
import invalidProvenanceFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/abstain-invalid-provenance-reference.json";
import hashMismatchFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/error-artifact-hash-mismatch.json";
import internalDiagnosticsLeakFixture from "../../../fixtures/ui/evidence_drawer_payload/invalid/drift-integrity-internal-diagnostics-leak.json";
import { resolveEvidenceDrawer } from "../src/features/evidence_drawer";

describe("Pass 4 Evidence Drawer drift and integrity profile", () => {
  it("renders source drift as a held, non-current abstention", () => {
    const result = resolveEvidenceDrawer(driftReviewFixture);
    expect(result).toMatchObject({
      outcome: "ABSTAIN",
      code: "HELD_EVIDENCE",
      message: "Evidence is held for review and is not current claim support.",
    });
    expect(result.evidenceRefs).toEqual([]);
    expect(result.historyLabels.join(" ")).toContain(
      "kfm:evidence:synthetic:source-drift-held-001",
    );
    expect(result.trustLabels).toContain("Review: PENDING");
    expect(result.trustLabels).toContain("Release: UNRELEASED");
  });

  it("renders a missing sidecar as missing evidence", () => {
    expect(resolveEvidenceDrawer(missingSidecarFixture)).toMatchObject({
      outcome: "ABSTAIN",
      code: "MISSING_EVIDENCE",
      message: "Required evidence is not available.",
    });
  });

  it("renders an invalid provenance reference as unresolved citation support", () => {
    expect(resolveEvidenceDrawer(invalidProvenanceFixture)).toMatchObject({
      outcome: "ABSTAIN",
      code: "CITATION_UNRESOLVED",
      message: "One or more required citations could not be resolved.",
    });
  });

  it("does not reflect steward-only quarantine detail into the public denial", () => {
    const result = resolveEvidenceDrawer(quarantinedRightsFixture);
    expect(result).toMatchObject({
      outcome: "DENY",
      code: "RIGHTS_UNRESOLVED",
      message: "Source rights are not resolved for this evidence detail.",
    });
    expect(JSON.stringify(result)).not.toContain("STEWARD_ONLY_QUARANTINE");
    expect(result.evidenceRefs).toEqual([]);
    expect(result.citations).toEqual([]);
    expect(result.historyLabels).toEqual([]);
  });

  it("does not reflect private hash diagnostics into the public error", () => {
    const result = resolveEvidenceDrawer(hashMismatchFixture);
    expect(result).toMatchObject({
      outcome: "ERROR",
      code: "UPSTREAM_ERROR",
      message: "The governed evidence service could not complete the request.",
    });
    expect(JSON.stringify(result)).not.toContain("INTERNAL_HASH");
    expect(result.evidenceRefs).toEqual([]);
    expect(result.citations).toEqual([]);
  });

  it("fails closed when an internal diagnostics field enters the public profile", () => {
    const result = resolveEvidenceDrawer(internalDiagnosticsLeakFixture);
    expect(result).toMatchObject({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
      message: "The governed evidence response is invalid.",
    });
    expect(JSON.stringify(result)).not.toContain("PRIVATE_CANARY");
    expect(JSON.stringify(result)).not.toContain("PRIVATE_STACK");
    expect(JSON.stringify(result)).not.toContain("data/quarantine");
  });
});
