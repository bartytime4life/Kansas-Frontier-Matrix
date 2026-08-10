import { describe, expect, it } from "vitest";

import invalidDoi from "../../../fixtures/ui/provenance_citations_projection/invalid/doi-link-mismatch.json";
import invalidExtra from "../../../fixtures/ui/provenance_citations_projection/invalid/extra-field.json";
import availableFixture from "../../../fixtures/ui/provenance_citations_projection/valid/available.json";
import deniedFixture from "../../../fixtures/ui/provenance_citations_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/provenance_citations_projection/valid/error.json";
import missingFixture from "../../../fixtures/ui/provenance_citations_projection/valid/missing.json";
import adapterSource from "../src/adapters/ProvenanceCitationsProjection.ts?raw";
import panelSource from "../src/features/provenance_citations/index.ts?raw";
import { resolveProvenanceCitations } from "../src/features/provenance_citations";

describe("Explorer provenance citations panel", () => {
  it("exposes bounded citations only for complete positive closure", () => {
    const result = resolveProvenanceCitations(availableFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "CITATIONS_AVAILABLE",
      heading: "Provenance citations",
      activityRef: "kfm://prov/activity/synthetic/citations-001",
      releaseManifestRef: "kfm://release/synthetic/manifest-001",
    });
    expect(result.citations).toHaveLength(2);
    expect(result.citations[0]).toMatchObject({
      doi: "10.1234/kfm.synthetic.001",
      href: "https://doi.org/10.1234/kfm.synthetic.001",
    });
    expect(result.summary).toContain("does not establish evidence sufficiency");
  });

  it.each([
    [missingFixture, "ABSTAIN", "CITATIONS_MISSING"],
    [deniedFixture, "DENY", "POLICY_DENIED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR"],
  ] as const)("renders fixed %s state without citation detail", (fixture, outcome, code) => {
    const result = resolveProvenanceCitations(fixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome,
      code,
      citations: [],
      activityRef: null,
      releaseManifestRef: null,
    });
    expect(JSON.stringify(result)).not.toContain("https://");
    expect(JSON.stringify(result)).not.toContain("kfm://");
  });

  it.each([invalidExtra, invalidDoi])(
    "fails closed on extra fields or contradictory DOI closure",
    (fixture) => {
      const result = resolveProvenanceCitations(fixture);
      expect(result).toMatchObject({
        visibility: "HIDDEN",
        code: "INVALID_PAYLOAD",
        citations: [],
      });
      expect(JSON.stringify(result)).not.toContain(
        "PROVENANCE_INTERNAL_CANARY_9f17c2",
      );
    },
  );

  it("renders nothing without a governed response", () => {
    expect(resolveProvenanceCitations()).toMatchObject({
      visibility: "HIDDEN",
      code: "NO_GOVERNED_RESPONSE",
    });
  });

  it("contains no transport, persistence, lifecycle-store, policy, or model access", () => {
    const source = `${adapterSource}\n${panelSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
    expect(source).not.toMatch(/(?:policyDecision|authorizeRelease)\s*\(/);
  });
});
