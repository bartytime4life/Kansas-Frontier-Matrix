import { describe, expect, it } from "vitest";

import invalidExtra from "../../../fixtures/ui/redaction_preview_projection/invalid/extra-restricted-geometry.json";
import invalidMissingReceipt from "../../../fixtures/ui/redaction_preview_projection/invalid/ready-missing-receipt.json";
import deniedFixture from "../../../fixtures/ui/redaction_preview_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/redaction_preview_projection/valid/error.json";
import incompleteFixture from "../../../fixtures/ui/redaction_preview_projection/valid/incomplete.json";
import readyFixture from "../../../fixtures/ui/redaction_preview_projection/valid/ready.json";
import adapterSource from "../src/adapters/RedactionPreviewProjection.ts?raw";
import previewSource from "../src/features/redaction_preview/index.ts?raw";
import { parseRedactionPreviewProjection } from "../src/adapters/RedactionPreviewProjection";
import { resolveRedactionPreview } from "../src/features/redaction_preview";

describe("Explorer public-safe redaction preview", () => {
  it("projects the four source-required reviewer summaries", () => {
    const result = resolveRedactionPreview(readyFixture);

    expect(result).toMatchObject({
      outcome: "ANSWER",
      code: "PREVIEW_READY",
      title: "Public-safe redaction preview",
      evaluatedAtLabel: "Evaluation time: 2026-08-10T18:00:00Z",
      canInspectReceipt: true,
      canApprove: false,
      canRelease: false,
      accessibilityLabel: "Redaction preview: public-safe transforms ready",
    });
    expect(result.items).toEqual([
      expect.objectContaining({
        kind: "GEOMETRY",
        value: "Generalized",
      }),
      expect.objectContaining({
        kind: "SUPPRESSION",
        value: "Low-count cells suppressed",
      }),
      expect.objectContaining({
        kind: "ZOOM_LIMIT",
        value: "z10",
      }),
      expect.objectContaining({
        kind: "ABSTRACTION",
        value: "County aggregate",
      }),
    ]);
    expect(JSON.stringify(result)).not.toContain("kfm://");
  });

  it.each([
    [incompleteFixture, "ABSTAIN", "PREVIEW_INCOMPLETE"],
    [deniedFixture, "DENY", "POLICY_DENIED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR"],
  ] as const)(
    "uses fixed no-detail copy for %s",
    (fixture, outcome, code) => {
      const result = resolveRedactionPreview(fixture);
      expect(result).toMatchObject({
        outcome,
        code,
        items: [],
        canInspectReceipt: false,
        canApprove: false,
        canRelease: false,
      });
      expect(JSON.stringify(result)).not.toContain("kfm://");
    },
  );

  it.each([invalidExtra, invalidMissingReceipt])(
    "fails closed on restricted detail or incomplete positive closure",
    (fixture) => {
      expect(parseRedactionPreviewProjection(fixture)).toEqual({
        ok: false,
        code: "MALFORMED_REDACTION_PREVIEW_PROJECTION",
      });
      const result = resolveRedactionPreview(fixture);
      expect(result).toMatchObject({
        outcome: "ERROR",
        code: "INVALID_PAYLOAD",
        items: [],
        canInspectReceipt: false,
      });
      expect(JSON.stringify(result)).not.toContain(
        "RESTRICTED_GEOMETRY_CANARY_52b6",
      );
    },
  );

  it("rejects noncanonical timestamps, out-of-range zoom, and wrong reference families", () => {
    const candidates = [
      { ...readyFixture, evaluated_at: "2026-08-10T18:00:00.000Z" },
      { ...readyFixture, maximum_public_zoom: 23 },
      {
        ...readyFixture,
        redaction_receipt_ref:
          "kfm://release-candidate/synthetic/wrong-family@sha256:" + "c".repeat(64),
      },
    ];

    for (const candidate of candidates) {
      expect(parseRedactionPreviewProjection(candidate)).toEqual({
        ok: false,
        code: "MALFORMED_REDACTION_PREVIEW_PROJECTION",
      });
    }
  });

  it("abstains when no governed projection is available", () => {
    expect(resolveRedactionPreview()).toMatchObject({
      outcome: "ABSTAIN",
      code: "NO_GOVERNED_RESPONSE",
      items: [],
      canInspectReceipt: false,
    });
  });

  it("contains no browser transport, persistence, lifecycle-store, renderer, or authority seam", () => {
    const source = `${adapterSource}\n${previewSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(|XMLHttpRequest|WebSocket/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage|indexedDB)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(
      /from\s+["'](?:maplibre-gl|three|@deck\.gl|3d-tiles-renderer)/,
    );
    expect(source).not.toMatch(/\b(?:approve|publish|release)\s*\(/i);
  });
});
