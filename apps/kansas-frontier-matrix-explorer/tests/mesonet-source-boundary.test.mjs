import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

const candidateSource = readFileSync(new URL("../app/source-intelligence.ts", import.meta.url), "utf8");
const observatory = readFileSync(new URL("../app/page.tsx", import.meta.url), "utf8");
const atlas = readFileSync(new URL("../../explorer-web/src/features/living_atlas/registry.ts", import.meta.url), "utf8");

test("Mesonet discovery links stay on the official site and never target data endpoints", () => {
  const pageList = candidateSource.match(/export const MESONET_OFFICIAL_PAGES = Object\.freeze\(\[([\s\S]*?)\] as const\);/);
  assert.ok(pageList, "official page list must remain explicit and reviewable");
  const urls = [...pageList[1].matchAll(/url: "([^"]+)"/g)].map((match) => match[1]);
  assert.ok(urls.length >= 7, "the principal page families must be represented");
  assert.equal(new Set(urls).size, urls.length, "each page needs one stable link");
  for (const rawUrl of urls) {
    const url = new URL(rawUrl);
    assert.equal(url.protocol, "https:");
    assert.equal(url.hostname, "mesonet.k-state.edu");
    assert.doesNotMatch(url.pathname, /^\/rest\/(?:stationdata|stationnames|mostrecent|fw13)/);
  }
  for (const family of ["Maps and stations", "Weather", "Agriculture", "Climate", "Derived context", "Methods and access"]) {
    assert.match(pageList[1], new RegExp(`family: "${family}"`));
  }
});

test("Mesonet remains a consent-gated source candidate with outbound links only", () => {
  assert.match(candidateSource, /id: "SRC-CAND-MESONET"[\s\S]*?written Kansas Mesonet consent before automated scraping or ingestion/);
  assert.match(candidateSource, /officialPages: MESONET_OFFICIAL_PAGES/);
  assert.match(observatory, /source\.officialPages\.map\(\(page\) => <li/);
  assert.match(observatory, /href=\{page\.url\} target="_blank" rel="noreferrer"/);
  assert.match(atlas, /layer\("layer:air-quality"[^\n]*sourceId: "source:site-local-atlas"/);
});
