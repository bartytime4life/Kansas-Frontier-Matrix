import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/historical-topo-overlay.ts", import.meta.url), "utf8");
const output = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const overlay = await import(`data:text/javascript;base64,${Buffer.from(output).toString("base64")}`);
const sha = "a".repeat(64);
const manifest = () => ({
  version: 1, packageId: sha.slice(0, 24), sheet: { id: 4628, scanId: 122705, name: "Topeka", year: 1889, scale: 125000, state: "KS" },
  geotiff: { url: "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/KS/KS_Topeka_122705_1889_125000_geo.tif", sha256: sha, bytes: 5372903, crs: "NAD27 Polyconic", transform: [0, 10.58, 0, 0, 0, -10.58], width: 4796, height: 5892 },
  bounds: [-96.04, 38.96, -95.45, 39.53], minZoom: 9, maxZoom: 14, sourceRetrievedAt: "2026-09-30T21:00:00Z",
  tiles: { "14/3834/6243": { sha256: "b".repeat(64), bytes: 65421 } }, evidenceRole: "EXTERNAL_CONTEXT_ONLY",
});

test("only an exact Kansas GeoTIFF package and bounded tiles can be served", () => {
  assert.ok(overlay.parseTopoOverlayManifest(manifest()));
  for (const altered of [
    { sheet: { ...manifest().sheet, state: "OK" } },
    { geotiff: { ...manifest().geotiff, url: "https://elsewhere.example/map.tif" } },
    { packageId: "b".repeat(24) },
    { bounds: [-90, 30, -89, 31] },
    { tiles: { "14/20000/6243": { sha256: "b".repeat(64), bytes: 65421 } } },
  ]) assert.equal(overlay.parseTopoOverlayManifest({ ...manifest(), ...altered }), null);
  assert.equal(overlay.topoTileKey(122705, sha.slice(0, 24), "14/3834/6243"), `historical-topo/v1/packages/122705/${sha.slice(0, 24)}/tiles/14/3834/6243.png`);
});

test("release pointers retain a validated rollback target", () => {
  const pointer = { scanId: 122705, packageId: sha.slice(0, 24), manifestSha256: sha, reviewedAt: "2026-09-30T21:00:00Z", reviewedBy: "b".repeat(64), note: "Checked Topeka alignment", previousPackageId: null, previousManifestSha256: null };
  assert.ok(overlay.parseTopoActivePointer(pointer));
  assert.equal(overlay.parseTopoActivePointer({ ...pointer, previousPackageId: "c".repeat(24) }), null);
  assert.ok(overlay.parseTopoActivePointer({ ...pointer, previousPackageId: "c".repeat(24), previousManifestSha256: "d".repeat(64) }));
});
