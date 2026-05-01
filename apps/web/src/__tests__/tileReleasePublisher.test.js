import fs from "node:fs";
import path from "node:path";
import { describe, expect, test } from "vitest";
import { publishTileLayer } from "../map/pmtiles/tileReleasePublisher.js";

const root = path.resolve(process.cwd(), "..", "..");
const validCandidate = JSON.parse(fs.readFileSync(path.join(root, "tests/fixtures/tile_release/valid/veg.layer.json"), "utf8"));
const validMetadata = JSON.parse(fs.readFileSync(path.join(root, "tests/fixtures/tile_release/valid/veg.pmtiles-metadata.json"), "utf8"));

const clone = (v) => JSON.parse(JSON.stringify(v));

describe("tile release publisher", () => {
  test("1 valid public released layer publishes deterministically", () => {
    const a = publishTileLayer(clone(validCandidate), clone(validMetadata), "2026-05-01T12:00:00Z");
    const b = publishTileLayer(clone(validCandidate), clone(validMetadata), "2026-05-01T12:00:00Z");
    expect(a.outcome).toBe("PUBLISHABLE");
    expect(JSON.stringify(a.generated.release_manifest)).toBe(JSON.stringify(b.generated.release_manifest));
  });

  test("2 mismatched TileJSON spec hash blocked", () => {
    const c = clone(validCandidate); c.tilejson_fixture = { "kfm:spec_hash": "sha256:2222222222222222222222222222222222222222222222222222222222222222" };
    expect(publishTileLayer(c, clone(validMetadata)).outcome).toBe("BLOCKED");
  });
  test("3 mismatched PMTiles spec hash blocked", () => {
    expect(publishTileLayer(clone(validCandidate), { ...validMetadata, "kfm:spec_hash": "sha256:2222222222222222222222222222222222222222222222222222222222222222" }).outcome).toBe("BLOCKED");
  });
  test("4 missing spec hash blocked", () => { const c = clone(validCandidate); delete c.spec_hash; expect(publishTileLayer(c, clone(validMetadata)).outcome).toBe("BLOCKED"); });
  test("5 restricted/private layer blocked", () => { const c = clone(validCandidate); c.policy_label = "restricted"; expect(publishTileLayer(c, clone(validMetadata)).outcome).toBe("BLOCKED"); });
  test("6 blocked lifecycle marker path", () => { const c = clone(validCandidate); c.source_pmtiles = "data/work/private.pmtiles"; expect(publishTileLayer(c, clone(validMetadata)).outcome).toBe("BLOCKED"); });
  test("7 draft review blocked", () => { const c = clone(validCandidate); c.review_state = "draft"; expect(publishTileLayer(c, clone(validMetadata)).outcome).toBe("BLOCKED"); });
  test("8 missing receipt returns NEEDS_RECEIPT", () => { const c = clone(validCandidate); c.receipts.items = c.receipts.items.filter((x) => x.type !== "generalization_receipt"); expect(publishTileLayer(c, clone(validMetadata)).outcome).toBe("NEEDS_RECEIPT"); });
  test("9 wrong receipt identity blocked", () => { const c = clone(validCandidate); c.receipts.items[0].layer_id = "wrong"; expect(publishTileLayer(c, clone(validMetadata)).outcome).toBe("BLOCKED"); });
  test("10 fallback not public safe blocked", () => { const c = clone(validCandidate); c.fallback.public_safe = false; expect(publishTileLayer(c, clone(validMetadata)).outcome).toBe("BLOCKED"); });
  test("11 release manifest stable across runs", () => {
    const a = publishTileLayer(clone(validCandidate), clone(validMetadata), "2026-05-01T00:00:00Z");
    const b = publishTileLayer(clone(validCandidate), clone(validMetadata), "2026-05-01T06:00:00Z");
    expect(a.generated.release_manifest.artifact_hashes.manifest).toBe(b.generated.release_manifest.artifact_hashes.manifest);
  });
  test("12 catalog no sensitive geometry", () => {
    const out = publishTileLayer(clone(validCandidate), clone(validMetadata));
    expect(out.generated.catalog_record.geometry).toBeUndefined();
  });
});
