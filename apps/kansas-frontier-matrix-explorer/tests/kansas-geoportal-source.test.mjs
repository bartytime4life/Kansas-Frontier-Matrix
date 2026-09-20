import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

const sources = readFileSync(new URL("../app/source-intelligence.ts", import.meta.url), "utf8");

test("registers Kansas Geoportal as a bounded live source candidate", () => {
  assert.match(sources, /SRC-CAND-KS-DASC/);
  assert.match(sources, /Kansas Geoportal \(DASC\) live ArcGIS catalog/);
  assert.ok(sources.includes('sourceUrl: "https://hub.kansasgis.org/"'));
  assert.match(sources, /one SourceDescriptor per selected ArcGIS item/);
  assert.match(sources, /Parcel-owner and infrastructure-sensitive fields remain deny-by-default/);
  assert.match(sources, /sourceCount: 12/);
});
