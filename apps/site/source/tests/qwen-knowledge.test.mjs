import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { QWEN_KNOWLEDGE_PACK_PATH, renderQwenKnowledgePack } from "../scripts/build-qwen-knowledge-pack.mjs";
import { QWEN_KNOWLEDGE_PACK } from "../scripts/qwen-knowledge-pack.mjs";
import {
  QWEN_KNOWLEDGE_DIGEST,
  QWEN_KNOWLEDGE_MAX_DETAILED_SOURCES,
  rankQwenKnowledgeSources,
  selectQwenKnowledge,
} from "../scripts/qwen-knowledge.mjs";
import { QWEN_LOCAL_INTERPRETATION_PROMPT_BUDGET_BYTES, QWEN_LOCAL_KNOWLEDGE_VERSION } from "../scripts/qwen-local-contract.mjs";

test("the committed knowledge pack matches the Site source registries", async () => {
  assert.equal(
    await readFile(QWEN_KNOWLEDGE_PACK_PATH, "utf8"),
    await renderQwenKnowledgePack(),
    "Run: node scripts/build-qwen-knowledge-pack.mjs",
  );
});

test("every pack source carries the metadata an interpretation must respect", () => {
  assert.equal(QWEN_KNOWLEDGE_PACK.version, QWEN_LOCAL_KNOWLEDGE_VERSION);
  assert.match(QWEN_KNOWLEDGE_DIGEST, /^sha256:[a-f0-9]{64}$/);
  assert.ok(QWEN_KNOWLEDGE_PACK.officialSources.length >= 40);
  for (const source of QWEN_KNOWLEDGE_PACK.officialSources) {
    for (const key of ["id", "title", "organization", "domain", "cadence", "freshness", "boundary", "fallback"]) {
      assert.ok(typeof source[key] === "string" && source[key].trim(), `${source.id}.${key}`);
    }
    assert.equal(source.evidenceRole, "EXTERNAL_CONTEXT_ONLY", source.id);
  }
  const domainSources = QWEN_KNOWLEDGE_PACK.domains.flatMap((domain) => domain.sourceIds);
  assert.deepEqual(new Set(domainSources), new Set(QWEN_KNOWLEDGE_PACK.officialSources.map((source) => source.id)));
  assert.ok(QWEN_KNOWLEDGE_PACK.domains.every((domain) => domain.ideas.length > 0), "every domain has exploration ideas");
  assert.ok(Object.isFrozen(QWEN_KNOWLEDGE_PACK.officialSources[0]));
  assert.doesNotMatch(JSON.stringify(QWEN_KNOWLEDGE_PACK), /kfm:(?:\/\/)?[A-Za-z0-9]/, "the pack never carries EvidenceRefs");
});

test("displayed sources outrank question matches, and question words find the right metadata", () => {
  const ranked = rankQwenKnowledgeSources("Where have earthquakes been recorded?", {
    officialSources: [{ id: "noaa-hms-smoke", displayed: true, selected: true }],
  });
  assert.equal(ranked[0].id, "noaa-hms-smoke");
  assert.ok(ranked.slice(0, 3).some((source) => source.id === "usgs-earthquakes"));
  assert.deepEqual(rankQwenKnowledgeSources("What is visible?", { officialSources: [] }), []);
});

test("knowledge selection is bounded, indexes everything, and trims to the prompt budget", () => {
  const everything = {
    officialSources: QWEN_KNOWLEDGE_PACK.officialSources.map((source) => ({ id: source.id, displayed: true, selected: true })),
  };
  const full = selectQwenKnowledge("basemap terrain aquifer bridges", everything);
  assert.equal(full.payload.relevantSources.length, QWEN_KNOWLEDGE_MAX_DETAILED_SOURCES);
  assert.equal(
    full.payload.relevantSources.length + full.payload.otherSources.length,
    QWEN_KNOWLEDGE_PACK.officialSources.length,
  );
  assert.equal(full.payload.authority, "METADATA_NOT_EVIDENCE");
  assert.ok(full.payload.displaySources.every((source) => typeof source === "object"), "basemap questions get basemap boundaries");
  assert.ok(Buffer.byteLength(JSON.stringify(full.payload)) < QWEN_LOCAL_INTERPRETATION_PROMPT_BUDGET_BYTES / 2);

  const tight = selectQwenKnowledge("basemap terrain aquifer bridges", everything, { maxBytes: 6_000 });
  assert.ok(Buffer.byteLength(JSON.stringify(tight.payload)) <= 6_000);
  assert.deepEqual(tight.payload.principles, QWEN_KNOWLEDGE_PACK.principles, "principles are never trimmed");
  assert.deepEqual(tight.payload.glossary, QWEN_KNOWLEDGE_PACK.glossary, "the glossary is never trimmed");
  assert.deepEqual(tight.sourceIds, tight.payload.relevantSources.map((source) => source.id));
  assert.equal(tight.digest, QWEN_KNOWLEDGE_DIGEST);
});
