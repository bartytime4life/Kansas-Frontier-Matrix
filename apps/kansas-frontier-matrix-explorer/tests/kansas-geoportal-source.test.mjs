import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

const sources = readFileSync(new URL("../app/source-intelligence.ts", import.meta.url), "utf8");
const page = readFileSync(new URL("../app/page.tsx", import.meta.url), "utf8");

test("registers Kansas Geoportal as a bounded live source candidate", () => {
  assert.match(sources, /SRC-CAND-KS-DASC/);
  assert.match(sources, /Kansas Geoportal \(DASC\) live ArcGIS catalog/);
  assert.ok(sources.includes('sourceUrl: "https://hub.kansasgis.org/"'));
  assert.match(sources, /Item-specific descriptor fixtures/);
  assert.match(sources, /REJECTED_SCOPE because its extent is outside Kansas/);
  assert.match(sources, /Parcel-owner and infrastructure-sensitive fields remain deny-by-default/);
  assert.match(sources, /sourceCount: 12/);
});


test("preserves candidate locator and freshness evidence in the Observatory handoff", () => {
  assert.match(page, /officialPortal: source\.sourceUrl \?\? null/);
  assert.match(page, /portalCheckedAt: source\.checkedAt \?\? null/);
  assert.match(page, /dateTime=\{source\.checkedAt\}>\{source\.checkedAt\}/);
  assert.match(page, /href=\{source\.sourceUrl\} target="_blank" rel="noreferrer">Open official source/);
});
