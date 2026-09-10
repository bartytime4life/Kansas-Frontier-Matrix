import { describe, expect, it } from "vitest";

import {
  createInitialSnapshot,
  isPersistedMapSnapshot,
  isPersistedReportDraft,
  isPersistedStoryScene,
  parsePersistedDraftCollection,
} from "../src/features/living_atlas";

type Mutable<T> = T extends readonly (infer Item)[]
  ? Mutable<Item>[]
  : T extends object
    ? { -readonly [Key in keyof T]: Mutable<T[Key]> }
    : T;

const clone = <T>(value: T): Mutable<T> =>
  JSON.parse(JSON.stringify(value)) as Mutable<T>;

function validReport() {
  const snapshot = createInitialSnapshot(new Date("2026-09-10T00:00:00.000Z"));
  return {
    profile: "kfm.explorer.report-draft.v1",
    id: "report:persistence-test",
    title: "Persistence test",
    researchQuestion: "What does this bounded snapshot support?",
    createdAt: "2026-09-10T00:00:01.000Z",
    snapshot,
    includedEvidenceRefs: snapshot.evidenceRefs,
    sections: {
      summary: "Draft summary.",
      observations: "Draft observations.",
      findings: "No factual finding.",
      limitations: "Fixture only.",
      openQuestions: "What should be reviewed next?",
    },
    lifecycle: "DRAFT",
    publishable: false,
  };
}

function validStory() {
  const snapshot = createInitialSnapshot(new Date("2026-09-10T00:00:00.000Z"));
  return {
    profile: "kfm.explorer.story-scene.v1",
    id: "story:persistence-test",
    title: "Persistence test",
    narrative: "A bounded fixture scene.",
    order: 1,
    snapshot,
    evidenceRefs: snapshot.evidenceRefs,
    caveats: ["Draft only."],
    motion: "NONE",
    lifecycle: "DRAFT",
  };
}

describe("Living Atlas persisted draft boundary", () => {
  it("accepts complete current report and story drafts", () => {
    expect(isPersistedReportDraft(validReport())).toBe(true);
    expect(isPersistedStoryScene(validStory())).toBe(true);
  });

  it("rejects shallow, privileged, and unknown report fields", () => {
    expect(isPersistedReportDraft({
      profile: "kfm.explorer.report-draft.v1",
      id: "report:shallow",
      snapshot: { profile: "kfm.explorer.map-snapshot.v1" },
    })).toBe(false);

    const publishable = clone(validReport());
    publishable.publishable = true;
    expect(isPersistedReportDraft(publishable)).toBe(false);

    const extended = { ...validReport(), releaseAuthorized: true };
    expect(isPersistedReportDraft(extended)).toBe(false);
  });

  it("rejects unknown time, layers, duplicate layers, and stale visibility", () => {
    const unknownTime = clone(validReport());
    unknownTime.snapshot.committedTimeId = "time:not-registered";
    expect(isPersistedReportDraft(unknownTime)).toBe(false);

    const unknownLayer = clone(validReport());
    unknownLayer.snapshot.layers[0]!.id = "layer:not-registered";
    expect(isPersistedReportDraft(unknownLayer)).toBe(false);

    const duplicateLayer = clone(validReport());
    duplicateLayer.snapshot.layers[1]!.id = duplicateLayer.snapshot.layers[0]!.id;
    expect(isPersistedReportDraft(duplicateLayer)).toBe(false);

    const staleVisibility = clone(validReport());
    const historical = staleVisibility.snapshot.layers.find(
      (entry) => entry.id === "layer:rail-study",
    )!;
    historical.visible = true;
    expect(isPersistedReportDraft(staleVisibility)).toBe(false);
  });

  it("rejects incompatible selection and stale or mismatched evidence", () => {
    const incompatible = clone(validReport());
    incompatible.snapshot.selectedLayerId = "layer:rail-study";
    expect(isPersistedReportDraft(incompatible)).toBe(false);

    const staleEvidence = clone(validReport());
    staleEvidence.snapshot.evidenceRefs = ["evidence:injected"];
    staleEvidence.includedEvidenceRefs = ["evidence:injected"];
    expect(isPersistedReportDraft(staleEvidence)).toBe(false);

    const mismatched = clone(validReport());
    mismatched.includedEvidenceRefs = ["evidence:injected"];
    expect(isPersistedReportDraft(mismatched)).toBe(false);

    const story = clone(validStory());
    story.evidenceRefs = ["evidence:injected"];
    expect(isPersistedStoryScene(story)).toBe(false);
  });

  it("keeps protected DENY selectable without admitting evidence", () => {
    const snapshot = clone(validReport().snapshot);
    snapshot.selectedLayerId = "layer:protected-context";
    snapshot.evidenceRefs = [];
    expect(isPersistedMapSnapshot(snapshot)).toBe(true);
  });

  it("distinguishes an absent key from malformed or filtered collections", () => {
    expect(parsePersistedDraftCollection(null, isPersistedReportDraft)).toBeNull();
    expect(parsePersistedDraftCollection("not json", isPersistedReportDraft)).toEqual([]);
    expect(parsePersistedDraftCollection("{}", isPersistedReportDraft)).toEqual([]);
    expect(parsePersistedDraftCollection(
      JSON.stringify([validReport(), { profile: "wrong" }]),
      isPersistedReportDraft,
    )).toHaveLength(1);
  });
});
