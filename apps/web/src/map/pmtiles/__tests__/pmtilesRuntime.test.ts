import { describe, expect, it } from "vitest";
import { evaluatePMTilesArchive } from "../runtimePolicy";
import { selectRenderablePMTilesArchives } from "../manifestLoader";
import { toPMTilesEvidenceRows } from "../pmtilesEvidenceAdapter";
import { installPMTilesSources } from "../installPMTilesSources";

const base = {
  archive_id: "base",
  href: "https://example.test/base.pmtiles",
  stage: "RELEASED",
  public_safe: true,
  digest: "sha256:" + "a".repeat(64),
  proof_ref: "proof://1",
  rights_status: "public",
  completeness_pct: 0.99,
  masked_pct: 0.1,
  verification_status: "verified"
} as const;

describe("pmtiles runtime policy", () => {
  it("allows valid archive", () => {
    expect(evaluatePMTilesArchive({ ...base }).decision).toBe("ALLOW_RENDER");
  });
  it("review band requires attestation", () => {
    expect(evaluatePMTilesArchive({ ...base, masked_pct: 0.2 }).decision).toBe("DENY_RENDER");
    expect(
      evaluatePMTilesArchive({ ...base, masked_pct: 0.2, steward_attestation_ref: "att://1" }).decision
    ).toBe("ALLOW_RENDER_WITH_REVIEW_BADGE");
  });
  it("denies thresholds and missing proofs", () => {
    expect(evaluatePMTilesArchive({ ...base, masked_pct: 0.31 }).decision).toBe("DENY_RENDER");
    expect(evaluatePMTilesArchive({ ...base, completeness_pct: 0.9 }).decision).toBe("DENY_RENDER");
    expect(evaluatePMTilesArchive({ ...base, digest: undefined }).decision).toBe("DENY_RENDER");
    expect(evaluatePMTilesArchive({ ...base, proof_ref: undefined, signature_ref: undefined }).decision).toBe("DENY_RENDER");
    expect(evaluatePMTilesArchive({ ...base, stage: "RAW" }).decision).toBe("DENY_RENDER");
  });
});

describe("loader and install", () => {
  it("selects renderable and avoids duplicates/denied", () => {
    const index: any = { object_type: "PMTilesTimeIndex", base_archive: { ...base }, delta_archives: [{ ...base, archive_id: "d1", generated_at: "2026-01-01T00:00:00Z" }] };
    expect(selectRenderablePMTilesArchives(index).length).toBe(2);

    const sources = new Map<string, unknown>();
    const map: any = {
      addProtocol: () => {},
      getSource: (id: string) => sources.get(id),
      addSource: (id: string, src: unknown) => sources.set(id, src)
    };
    const report = installPMTilesSources(map, [{ ...base }, { ...base, archive_id: "bad", digest: undefined } as any, { ...base }]);
    expect(report.added.length).toBe(1);
    expect(report.denied.length).toBe(1);
  });

  it("evidence adapter keeps non-sensitive fields", () => {
    const row = toPMTilesEvidenceRows([evaluatePMTilesArchive({ ...base, sensitivity: "exact", geoprivacy_receipt_ref: "geo://1" })])[0];
    expect((row as any).exact_geometry).toBeUndefined();
    expect(row.geoprivacy_receipt_ref).toBe("geo://1");
  });
});
