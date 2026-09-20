import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";

const sources = readFileSync(new URL("../app/source-intelligence.ts", import.meta.url), "utf8");
const kansasMemory = readFileSync(new URL("../../../docs/sources/catalog/kansas/kansas-memory.md", import.meta.url), "utf8");
const stateArchives = readFileSync(new URL("../../../docs/sources/catalog/kansas/kansas-state-archives.md", import.meta.url), "utf8");

const candidateBlock = (id) => {
  const start = sources.indexOf(`id: "${id}"`);
  assert.notEqual(start, -1, `missing source candidate ${id}`);
  const end = sources.indexOf("  }),", start);
  assert.notEqual(end, -1, `unterminated source candidate ${id}`);
  return sources.slice(start, end);
};

test("keeps Kansas Memory and State Archives as separate manual-only candidates", () => {
  const kansasMemoryCandidate = candidateBlock("SRC-CAND-KSMEM");
  const stateArchivesCandidate = candidateBlock("SRC-CAND-KS-STATE-ARCHIVES");

  assert.match(sources, /candidateCount: 13/);
  assert.equal((sources.match(/id: "SRC-CAND-KSMEM"/g) ?? []).length, 1);
  assert.equal((sources.match(/id: "SRC-CAND-KS-STATE-ARCHIVES"/g) ?? []).length, 1);
  assert.match(kansasMemoryCandidate, /Kansas Memory digital archive · manual-only/);
  assert.match(kansasMemoryCandidate, /layerId: "historical-context"/);
  assert.match(kansasMemoryCandidate, /featureId: "history-route-1885"/);
  assert.match(stateArchivesCandidate, /Kansas State Archives · manual-only/);
  assert.match(stateArchivesCandidate, /State Archives-specific descriptor/);
  assert.doesNotMatch(stateArchivesCandidate, /layerId:/);
  assert.doesNotMatch(stateArchivesCandidate, /featureId:/);
});

test("records the scraping-agreement hold in both source profiles", () => {
  for (const profile of [kansasMemory, stateArchives]) {
    assert.match(profile, /MANUAL_ONLY/);
    assert.match(profile, /NEEDS_SCRAPING_AGREEMENT/);
    assert.match(profile, /AUTOMATED_INTAKE_HELD/);
    assert.match(profile, /scraping or data-access agreement|scraping\/data-access agreement/);
  }
  assert.match(stateArchives, /distinct candidate IDs, descriptors, access mechanics, rights decisions, and provenance chains/);
});
