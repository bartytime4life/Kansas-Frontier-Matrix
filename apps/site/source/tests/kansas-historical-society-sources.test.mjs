import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

test("keeps Kansas Memory and State Archives as separate held candidates", async () => {
  const sources = await readFile(new URL("../app/source-intelligence.ts", import.meta.url), "utf8");

  assert.equal((sources.match(/"id":"SRC-CAND-KSMEM"/g) ?? []).length, 1);
  assert.equal((sources.match(/"id":"SRC-CAND-KS-STATE-ARCHIVES"/g) ?? []).length, 1);
  assert.match(sources, /"SRC-CAND-KSMEM": "held"/);
  assert.match(sources, /"SRC-CAND-KS-STATE-ARCHIVES": "held"/);
  assert.match(sources, /Needs a State Archives-specific scraping or data-access agreement/);
  assert.match(sources, /No Kansas Memory analogue is reused/);

  const stateArchives = sources.slice(sources.indexOf('{"id":"SRC-CAND-KS-STATE-ARCHIVES"'));
  const stateArchivesRecord = stateArchives.slice(0, stateArchives.indexOf("}),") + 3);
  assert.doesNotMatch(stateArchivesRecord, /"layerId"/);
  assert.doesNotMatch(stateArchivesRecord, /"featureId"/);
});
