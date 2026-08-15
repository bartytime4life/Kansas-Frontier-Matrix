import { describe, expect, it } from "vitest";

import fixtureSuite from "../../../fixtures/ui/story_manifest/cases.json";
import featureSource from "../src/features/story_player/index.tsx?raw";
import { resolveStoryPlayer } from "../src/features/story_player";

function cloneBase(): Record<string, any> {
  return JSON.parse(JSON.stringify(fixtureSuite.base));
}

describe("Explorer Story Player governed projection", () => {
  it("allows 2D playback only for a fully public-safe READY manifest", () => {
    const result = resolveStoryPlayer(fixtureSuite.base);

    expect(result).toMatchObject({
      outcome: "ANSWER",
      code: "STORY_READY",
      title: "Synthetic frontier overview",
      storyRef: "kfm://story/synthetic-frontier-overview",
      state: "READY",
      canPlay: true,
      mode: "2D",
      authoritative: false,
    });
    expect(result.nodes).toEqual([
      { nodeRef: "kfm://story-node/context", orderIndex: 0 },
      { nodeRef: "kfm://story-node/overview", orderIndex: 1 },
    ]);
    expect(result.evidenceBundleRefs).toEqual([
      "evidence:synthetic-story-bundle",
    ]);
  });

  it("abstains and withholds node playback for stale or unreleased support", () => {
    for (const mutation of [
      { freshness: "STALE", reason: "STALE_EVIDENCE" },
      { release: "UNRELEASED", reason: "RELEASE_UNAVAILABLE" },
    ]) {
      const candidate = cloneBase();
      if (mutation.freshness) {
        candidate.trust_state.freshness = mutation.freshness;
      }
      if (mutation.release) {
        candidate.trust_state.release = mutation.release;
      }
      candidate.state = "PARTIAL";
      candidate.outcome = "ABSTAIN";
      candidate.reason_codes = [mutation.reason];
      candidate.limiting_node_refs = ["kfm://story-node/overview"];

      const result = resolveStoryPlayer(candidate);
      expect(result).toMatchObject({
        outcome: "ABSTAIN",
        code: "STORY_ABSTAINED",
        canPlay: false,
        nodes: [],
      });
    }
  });

  it("denies playback for blocked rights or restricted sensitivity", () => {
    for (const [field, value, reason] of [
      ["rights", "UNRESOLVED", "RIGHTS_UNRESOLVED"],
      ["sensitivity", "RESTRICTED", "SENSITIVE_DETAIL_RESTRICTED"],
    ] as const) {
      const candidate = cloneBase();
      candidate.trust_state[field] = value;
      candidate.state = "BLOCKED";
      candidate.outcome = "DENY";
      candidate.reason_codes = [reason];
      candidate.limiting_node_refs = ["kfm://story-node/context"];

      expect(resolveStoryPlayer(candidate)).toMatchObject({
        outcome: "DENY",
        code: "STORY_DENIED",
        nodes: [],
        canPlay: false,
      });
    }
  });

  it("surfaces upstream error without exposing node playback", () => {
    const candidate = cloneBase();
    candidate.trust_state.policy = "ERROR";
    candidate.state = "ERROR";
    candidate.outcome = "ERROR";
    candidate.reason_codes = ["UPSTREAM_ERROR"];
    candidate.limiting_node_refs = ["kfm://story-node/overview"];

    expect(resolveStoryPlayer(candidate)).toMatchObject({
      outcome: "ERROR",
      code: "STORY_ERROR",
      nodes: [],
      canPlay: false,
    });
  });

  it("abstains on a superseded manifest and exposes only its public replacement ref", () => {
    const candidate = cloneBase();
    candidate.state = "SUPERSEDED";
    candidate.outcome = "ABSTAIN";
    candidate.reason_codes = ["SUPERSEDED"];
    candidate.limiting_node_refs = ["kfm://story-node/context"];
    candidate.trust_state.release = "WITHDRAWN";
    candidate.trust_state.correction = "SUPERSEDED";
    candidate.support.correction_refs = [
      "correction:synthetic-story-supersession",
    ];
    candidate.supersession = {
      replacement_manifest_ref:
        "kfm:story-manifest:111111111111111111111111",
      public_note: "Synthetic replacement.",
    };

    expect(resolveStoryPlayer(candidate)).toMatchObject({
      outcome: "ABSTAIN",
      code: "STORY_ABSTAINED",
      replacementManifestRef:
        "kfm:story-manifest:111111111111111111111111",
      nodes: [],
      canPlay: false,
    });
  });

  it("fails closed on optimistic READY trust and malformed projection flags", () => {
    const staleReady = cloneBase();
    staleReady.trust_state.freshness = "STALE";

    expect(resolveStoryPlayer(staleReady)).toMatchObject({
      outcome: "ABSTAIN",
      code: "STORY_ABSTAINED",
      nodes: [],
      canPlay: false,
    });

    for (const candidate of [
      { ...cloneBase(), authoritative: true },
      { ...cloneBase(), projection_only: false },
      { ...cloneBase(), profile: "untrusted.profile" },
    ]) {
      expect(resolveStoryPlayer(candidate)).toEqual({
        outcome: "ERROR",
        code: "INVALID_PAYLOAD",
        title: null,
        accessibilitySummary: "Story playback is unavailable.",
        storyRef: null,
        state: null,
        nodes: [],
        reasonCodes: [],
        limitingNodeRefs: [],
        evidenceBundleRefs: [],
        citationValidationRefs: [],
        caveats: [],
        replacementManifestRef: null,
        canPlay: false,
        mode: "2D",
        authoritative: false,
      });
    }
  });

  it("rejects closed-profile drift without reflecting untrusted content", () => {
    const candidate = cloneBase();
    candidate.body = "UNTRUSTED_STORY_BODY_CANARY_8d31";

    const result = resolveStoryPlayer(candidate);
    expect(result).toMatchObject({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
      nodes: [],
      canPlay: false,
    });
    expect(JSON.stringify(result)).not.toContain(
      "UNTRUSTED_STORY_BODY_CANARY_8d31",
    );
  });

  it("rejects duplicate or unsorted constituents", () => {
    const duplicate = cloneBase();
    duplicate.constituents[1].node_ref = duplicate.constituents[0].node_ref;

    const unsorted = cloneBase();
    unsorted.constituents[0].order_index = 1;
    unsorted.constituents[1].order_index = 0;

    for (const candidate of [duplicate, unsorted]) {
      expect(resolveStoryPlayer(candidate)).toMatchObject({
        outcome: "ERROR",
        code: "INVALID_PAYLOAD",
        nodes: [],
        canPlay: false,
      });
    }
  });

  it("uses explicit abstention when no governed projection exists", () => {
    expect(resolveStoryPlayer()).toMatchObject({
      outcome: "ABSTAIN",
      code: "NO_GOVERNED_RESPONSE",
      nodes: [],
      canPlay: false,
    });
  });

  it("keeps Story Player free of transport, internal-store, mutation, and renderer seams", () => {
    expect(featureSource).not.toMatch(/\bfetch\s*\(|XMLHttpRequest|WebSocket/);
    expect(featureSource).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(featureSource).not.toMatch(
      /\b(?:approve|override|publish|release|deploy)\s*\(/i,
    );
    expect(featureSource).not.toMatch(/maplibre|cesium|ollama/i);
  });
});
