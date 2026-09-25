import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
const source = await readFile(new URL("../app/import-preview.ts", import.meta.url), "utf8");
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { buildLocalImportPreview } = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);
const preview = (text, fileSizeBytes = Buffer.byteLength(text)) => buildLocalImportPreview({
  fileName: "local.kml", text, fileSizeBytes, inspectedAt: "2026-09-24T00:00:00Z",
  supportedBounds: { west: -104.8, south: 34.8, east: -92, north: 42.2 },
});
test("malformed and deeply nested KML returns a bounded error", () => {
  for (const tag of ["Placemark", "Data", "SimpleData", "k:Placemark"]) {
    assert.throws(() => preview(`<kml>${`<${tag}>`.repeat(3000)}</kml>`), /complexity|balanced/);
  }
  assert.throws(() => preview('<kml><Placemark></kml>'), /balanced/);
  assert.throws(() => preview('<kml><Placemark attr="<Point>"'), /incomplete|well formed/);
  assert.throws(() => preview(' '.repeat(2 * 1024 * 1024 + 1), 1), /2 MB/);
});
test("namespaced elements, quoted attributes, and extended fields remain supported", () => {
  const result = preview(`<k:kml><k:Placemark title="a > b"><k:ExtendedData><k:Data name="attribution"><k:value>Synthetic &amp; fixture</k:value></k:Data><k:SimpleData name="year">2026</k:SimpleData></k:ExtendedData><k:Point><k:coordinates>-98,38</k:coordinates></k:Point></k:Placemark></k:kml>`);
  assert.equal(result.featureCount, 1);
  assert.equal(result.attribution, "Synthetic & fixture");
  assert.equal(result.featureCollection.features[0].properties.year, "2026");
});
