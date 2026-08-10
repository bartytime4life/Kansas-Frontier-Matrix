import { describe, expect, it } from "vitest";

import invalidCrypto from "../../../fixtures/ui/pmtiles_range_diagnostics_projection/invalid/crypto-overclaim.json";
import invalidExtra from "../../../fixtures/ui/pmtiles_range_diagnostics_projection/invalid/extra-field.json";
import availableFixture from "../../../fixtures/ui/pmtiles_range_diagnostics_projection/valid/available.json";
import deniedFixture from "../../../fixtures/ui/pmtiles_range_diagnostics_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/pmtiles_range_diagnostics_projection/valid/error.json";
import missingFixture from "../../../fixtures/ui/pmtiles_range_diagnostics_projection/valid/missing.json";
import adapterSource from "../src/adapters/PmtilesRangeDiagnosticsProjection.ts?raw";
import panelSource from "../src/features/pmtiles_range_diagnostics/index.ts?raw";
import { resolvePmtilesRangeDiagnostics } from "../src/features/pmtiles_range_diagnostics";

describe("Explorer PMTiles range diagnostics", () => {
  it("shows structural range checks while retaining every unresolved hold", () => {
    const result = resolvePmtilesRangeDiagnostics(availableFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "DIAGNOSTICS_AVAILABLE",
      verificationState: "STRUCTURAL_HOLD",
      artifactRef: "kfm://artifact/pmtiles/synthetic/kansas-001",
      verifiedRange: { offset: 4096, length: 512, leaf: 1 },
      http: {
        acceptRanges: "SUPPORTED",
        contentRange: "VALID",
        etag: "MATCH",
        cache: "HIT",
      },
    });
    expect(result.checks).toHaveLength(4);
    expect(result.holds).toContain("CRYPTOGRAPHIC_VERIFICATION_UNWIRED");
    expect(result.summary).toContain("does not prove cryptographic trust");
  });

  it.each([
    [missingFixture, "ABSTAIN", "DIAGNOSTICS_UNAVAILABLE"],
    [deniedFixture, "DENY", "VERIFICATION_DENIED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR"],
  ] as const)("renders fixed %s state without artifact detail", (fixture, outcome, code) => {
    const result = resolvePmtilesRangeDiagnostics(fixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome,
      code,
      artifactRef: null,
      checks: [],
      holds: [],
    });
    expect(JSON.stringify(result)).not.toContain("kfm://artifact/");
  });

  it.each([invalidExtra, invalidCrypto])(
    "fails closed on unknown fields or cryptographic overclaim",
    (fixture) => {
      const result = resolvePmtilesRangeDiagnostics(fixture);
      expect(result).toMatchObject({
        visibility: "HIDDEN",
        code: "INVALID_PAYLOAD",
        checks: [],
        holds: [],
      });
      expect(JSON.stringify(result)).not.toContain("PMTILES_INTERNAL_CANARY_782ca1");
    },
  );

  it("renders nothing without a governed response", () => {
    expect(resolvePmtilesRangeDiagnostics()).toMatchObject({
      visibility: "HIDDEN",
      code: "NO_GOVERNED_RESPONSE",
    });
  });

  it("contains no transport, archive IO, persistence, lifecycle, policy, signing, or model access", () => {
    const source = `${adapterSource}\n${panelSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(/(?:readFile|createReadStream|Range\s*:)/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/(?:cosign|verifySignature|authorizeRelease)\s*\(/i);
    expect(source).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
  });
});
