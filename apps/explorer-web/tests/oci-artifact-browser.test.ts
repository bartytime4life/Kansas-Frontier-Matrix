import { describe, expect, it } from "vitest";

import invalidExtra from "../../../fixtures/ui/oci_artifact_browser_projection/invalid/extra-field.json";
import invalidSubject from "../../../fixtures/ui/oci_artifact_browser_projection/invalid/referrer-subject-mismatch.json";
import invalidTag from "../../../fixtures/ui/oci_artifact_browser_projection/invalid/tag-binding-drift.json";
import availableFixture from "../../../fixtures/ui/oci_artifact_browser_projection/valid/available.json";
import deniedFixture from "../../../fixtures/ui/oci_artifact_browser_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/oci_artifact_browser_projection/valid/error.json";
import missingFixture from "../../../fixtures/ui/oci_artifact_browser_projection/valid/missing.json";
import adapterSource from "../src/adapters/OciArtifactBrowserProjection.ts?raw";
import browserSource from "../src/features/oci_artifact_browser/index.ts?raw";
import { resolveOciArtifactBrowser } from "../src/features/oci_artifact_browser";

describe("Explorer OCI artifact review browser", () => {
  it("shows digest identity separately from mutable tags and recorded referrers", () => {
    const result = resolveOciArtifactBrowser(availableFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "ARTIFACTS_AVAILABLE",
      registryScope: "oci://registry.example/kfm/geospatial",
      reviewedAt: "2026-08-10T20:00:00Z",
      rollbackCandidateRef:
        "oci://registry.example/kfm/geospatial@sha256:" + "a".repeat(64),
    });
    expect(result.artifacts).toHaveLength(2);
    expect(result.artifacts[0]).toMatchObject({
      tag: "county-basemap-2026-08-10",
      digest: `sha256:${"a".repeat(64)}`,
      mediaType: "application/vnd.pmtiles",
    });
    expect(result.artifacts[0]?.referrers.map((item) => item.kind)).toEqual([
      "SIGNATURE",
      "PROVENANCE",
      "SBOM",
    ]);
    expect(result.message).toContain("not verified here");
    expect(result.message).toContain("rollback remains unauthorized");
  });

  it.each([
    [missingFixture, "ABSTAIN", "ARTIFACTS_MISSING"],
    [deniedFixture, "DENY", "POLICY_DENIED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR"],
  ] as const)("renders %s without registry or artifact detail", (fixture, outcome, code) => {
    const result = resolveOciArtifactBrowser(fixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome,
      code,
      registryScope: null,
      reviewedAt: null,
      artifacts: [],
      rollbackCandidateRef: null,
    });
    expect(JSON.stringify(result)).not.toContain("oci://");
  });

  it.each([invalidExtra, invalidSubject, invalidTag])(
    "fails closed on extra fields and digest/referrer binding drift",
    (fixture) => {
      const result = resolveOciArtifactBrowser(fixture);
      expect(result).toMatchObject({
        visibility: "HIDDEN",
        code: "INVALID_PAYLOAD",
        registryScope: null,
        artifacts: [],
      });
      expect(JSON.stringify(result)).not.toContain(
        "OCI_BROWSER_INTERNAL_CANARY_6b48d2",
      );
    },
  );

  it("renders nothing without a governed projection", () => {
    expect(resolveOciArtifactBrowser()).toMatchObject({
      visibility: "HIDDEN",
      code: "NO_GOVERNED_RESPONSE",
    });
  });

  it("contains no registry transport, persistence, cryptography, lifecycle mutation, or release action", () => {
    const source = `${adapterSource}\n${browserSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage|indexedDB)\b/);
    expect(source).not.toMatch(/\b(?:crypto|subtle|verify)\s*\(/);
    expect(source).not.toMatch(/\b(?:oras|docker|registryClient)\s*[.(]/i);
    expect(source).not.toMatch(
      /(?:pushArtifact|pullArtifact|verifySignature|executeRollback|promoteArtifact|authorizeRelease|publishArtifact)\s*\(/,
    );
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
  });
});
