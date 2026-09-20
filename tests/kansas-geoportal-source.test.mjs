import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

test("registers Kansas Geoportal as live discovery without collapsing admission", async () => {
  const sources = await readFile(new URL("../app/source-intelligence.ts", import.meta.url), "utf8");
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");

  assert.match(sources, /SRC-CAND-KS-DASC/);
  assert.match(sources, /Kansas Geoportal \(DASC\) live ArcGIS catalog/);
  assert.ok(sources.includes('sourceUrl: "https://hub.kansasgis.org/"'));
  assert.match(sources, /end-to-end ingestion reuse remains unproven/);
  assert.match(sources, /Item-specific descriptor fixtures/);
  assert.match(sources, /REJECTED_SCOPE because its extent is outside Kansas/);
  assert.match(sources, /Parcel-owner and infrastructure-sensitive fields remain deny-by-default/);
  assert.match(sources, /"SRC-CAND-KS-DASC": "candidate"/);
  assert.doesNotMatch(sources, /"SRC-CAND-KS-DASC": "admitted"/);
  assert.match(page, /dateTime=\{source\.checkedAt\}>\{source\.checkedAt\}/);
});
