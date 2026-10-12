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
import {
  QWEN_LOCAL_INTERPRETATION_PROMPT_BUDGET_BYTES,
  QWEN_LOCAL_KNOWLEDGE_VERSION,
  localQwenAnswerHasOverPreciseLocation,
} from "../scripts/qwen-local-contract.mjs";

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
  // Even this adversarial view leaves 20 KiB for map context, about twice the real
  // 48-source browser envelope; larger contexts are handled by the trimming below.
  assert.ok(Buffer.byteLength(JSON.stringify(full.payload)) <= QWEN_LOCAL_INTERPRETATION_PROMPT_BUDGET_BYTES - 20 * 1024);

  // The smallest budget the bridge can pass is 44 KiB minus a 32 KiB maximum request.
  const tight = selectQwenKnowledge("basemap terrain aquifer bridges", everything, { maxBytes: 8_000 });
  assert.ok(Buffer.byteLength(JSON.stringify(tight.payload)) <= 8_000);
  assert.deepEqual(tight.payload.domainTerms, [], "domain terms are trimmed before detailed sources");
  assert.deepEqual(tight.payload.principles, QWEN_KNOWLEDGE_PACK.principles, "principles are never trimmed");
  assert.deepEqual(tight.payload.glossary, QWEN_KNOWLEDGE_PACK.glossary, "the glossary is never trimmed");
  assert.deepEqual(tight.sourceIds, tight.payload.relevantSources.map((source) => source.id));
  assert.equal(tight.digest, QWEN_KNOWLEDGE_DIGEST);
});

test("every domain has a full set of exploration ideas that stay questions, not findings", () => {
  const domainNames = QWEN_KNOWLEDGE_PACK.domains.map((domain) => domain.name);
  for (const domain of QWEN_KNOWLEDGE_PACK.domains) {
    assert.ok(domain.ideas.length >= 6, `${domain.name} has ${domain.ideas.length} ideas`);
    assert.equal(new Set(domain.ideas).size, domain.ideas.length, `${domain.name} repeats an idea`);
  }
  assert.ok(QWEN_KNOWLEDGE_PACK.crossDomainIdeas.length > 0);
  for (const entry of QWEN_KNOWLEDGE_PACK.crossDomainIdeas) {
    assert.equal(entry.domains.length, 2, entry.idea);
    assert.ok(entry.domains.every((domain) => domainNames.includes(domain)), entry.idea);
  }
  const allIdeas = [
    ...QWEN_KNOWLEDGE_PACK.domains.flatMap((domain) => domain.ideas),
    ...QWEN_KNOWLEDGE_PACK.crossDomainIdeas.map((entry) => entry.idea),
    ...QWEN_KNOWLEDGE_PACK.projectIdeas,
  ];
  for (const idea of allIdeas) {
    assert.ok(idea.length <= 400, idea);
    assert.equal(localQwenAnswerHasOverPreciseLocation(idea), false, idea);
  }
});

test("cross-domain ideas appear only when both of their domains are in view", () => {
  const view = (ids) => ({ officialSources: ids.map((id) => ({ id, displayed: true, selected: true })) });
  const riverOnly = selectQwenKnowledge("What is visible?", view(["usgs-streamflow"]));
  assert.ok(riverOnly.payload.crossDomainIdeas.every((idea) => !/aquifer/i.test(idea)));
  // Asking about aquifers pulls aquifer metadata into the prompt but does not put an aquifer layer in view.
  const askedOnly = selectQwenKnowledge("How does this river interact with the alluvial aquifer?", view(["usgs-streamflow"]));
  assert.ok(askedOnly.payload.relevantSources.some((source) => source.domain === "Aquifers & groundwater"));
  assert.deepEqual(askedOnly.payload.crossDomainIdeas, []);
  const selectedNotDisplayed = selectQwenKnowledge("What is visible?", {
    officialSources: [
      { id: "usgs-streamflow", displayed: true, selected: true },
      { id: "kgs-aquifer-alluvial", displayed: false, selected: true },
    ],
  });
  assert.deepEqual(selectedNotDisplayed.payload.crossDomainIdeas, []);
  const riverAndAquifer = selectQwenKnowledge("What is visible?", view(["usgs-streamflow", "kgs-aquifer-alluvial"]));
  const expected = QWEN_KNOWLEDGE_PACK.crossDomainIdeas.find((entry) =>
    entry.domains.includes("Living waters") && entry.domains.includes("Aquifers & groundwater")).idea;
  assert.ok(riverAndAquifer.payload.crossDomainIdeas.includes(expected));
  const trimmed = selectQwenKnowledge("What is visible?", view(["usgs-streamflow", "kgs-aquifer-alluvial"]), { maxBytes: 9_000 });
  assert.deepEqual(trimmed.payload.crossDomainIdeas, [], "cross-domain ideas are trimmed before domain ideas");
});

test("the glossary defines the context fields, states and kinds the model reads, plus terms for every domain", () => {
  const { glossary } = QWEN_KNOWLEDGE_PACK;
  const officialKinds = new Set(QWEN_KNOWLEDGE_PACK.officialSources.map((source) => source.kind));
  const displayKinds = new Set(QWEN_KNOWLEDGE_PACK.displaySources.map((source) => source.kind));
  for (const kind of [...officialKinds, ...displayKinds]) assert.ok(glossary.sourceKinds[kind], `source kind ${kind}`);
  for (const state of ["idle", "loading", "ready", "empty", "partial", "error"]) assert.ok(glossary.connectionStates[state], state);
  for (const field of ["officialSources.selected", "officialSources.displayed", "officialSources.retrievedAt", "camera.locationRedacted"]) {
    assert.ok(glossary.contextFields[field], field);
  }
  for (const domain of QWEN_KNOWLEDGE_PACK.domains) {
    assert.ok(Object.keys(domain.terms).length >= 3, `${domain.name} has domain terms`);
  }
  const definitions = [
    ...Object.values(glossary).flatMap((section) => Object.values(section)),
    ...QWEN_KNOWLEDGE_PACK.domains.flatMap((domain) => Object.values(domain.terms)),
  ];
  for (const definition of definitions) {
    assert.ok(typeof definition === "string" && definition.length > 0 && definition.length <= 300, definition);
    assert.equal(localQwenAnswerHasOverPreciseLocation(definition), false, definition);
  }
});

test("domain terms follow the relevant domains and are trimmed before detailed sources", () => {
  const view = (ids) => ({ officialSources: ids.map((id) => ({ id, displayed: true, selected: true })) });
  const river = selectQwenKnowledge("What is the discharge at these gauges?", view(["usgs-streamflow"]));
  assert.deepEqual(river.payload.domainTerms.map((entry) => entry.domain), ["Living waters"]);
  assert.ok(river.payload.domainTerms[0].terms.Discharge);
  assert.deepEqual(selectQwenKnowledge("What is visible?", view([])).payload.domainTerms, []);
});
