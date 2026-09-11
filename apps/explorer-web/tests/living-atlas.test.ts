import { describe, expect, it } from "vitest";
import {
  ATLAS_WORKBENCH_TOOLS,
  ATLAS_VIEWS,
  EVIDENCE_RECORDS,
  LAYER_RECORDS,
  MAP_INTERACTION_TOOLS,
  REPOSITORY_LAYER_CONNECTIONS,
  SOURCE_DESCRIPTORS,
  TEMPORAL_EXTENTS,
  createInitialSnapshot,
  createLivingAtlasStyle,
  commitSnapshotTime,
  evaluateFocusSelection,
} from "../src/features/living_atlas";
import {
  createInitialPlayback,
  isPlaybackPlaying,
  playbackFrameId,
  playbackHasNext,
  reducePlayback,
} from "../src/features/temporal";

describe("Living Atlas governed foundation", () => {
  it("publishes the complete bounded registry with unique bindings", () => {
    expect(ATLAS_VIEWS).toHaveLength(18);
    expect(LAYER_RECORDS).toHaveLength(24);
    expect(EVIDENCE_RECORDS).toHaveLength(LAYER_RECORDS.length);
    expect(new Set(ATLAS_VIEWS.map((entry) => entry.id)).size).toBe(18);
    expect(new Set(LAYER_RECORDS.map((entry) => entry.id)).size).toBe(24);
    expect(
      ATLAS_VIEWS.every((view) =>
        view.layerIds.every((id) => LAYER_RECORDS.some((layer) => layer.id === id)),
      ),
    ).toBe(true);
    expect(
      LAYER_RECORDS.every((layer) =>
        SOURCE_DESCRIPTORS.some((source) => source.id === layer.sourceId),
      ),
    ).toBe(true);
  });

  it("keeps source portals unadmitted and precise sensitive detail denied", () => {
    expect(SOURCE_DESCRIPTORS.some((source) => source.admissionState === "ADMITTED")).toBe(false);
    expect(
      LAYER_RECORDS.find((layer) => layer.id === "layer:protected-context"),
    ).toMatchObject({
      availability: "DENIED",
      representation: "CATALOG_ONLY",
      trustState: "DENIED",
    });
  });

  it("maps repository layer candidates without treating them as runtime admission", () => {
    expect(REPOSITORY_LAYER_CONNECTIONS).toHaveLength(15);
    expect(
      REPOSITORY_LAYER_CONNECTIONS.filter(
        (entry) => entry.state === "FIXTURE_ONLY",
      ).map((entry) => entry.id),
    ).toEqual(["connection:wbd-huc12", "connection:three-dep-terrain"]);
    expect(
      REPOSITORY_LAYER_CONNECTIONS.find(
        (entry) => entry.id === "connection:three-dep-terrain",
      ),
    ).toMatchObject({
      state: "FIXTURE_ONLY",
      statusReason: expect.stringContaining("no source descriptor"),
      cannotProve: expect.stringContaining("admission"),
    });
    expect(
      REPOSITORY_LAYER_CONNECTIONS.find(
        (entry) => entry.id === "connection:usgs-earthquakes",
      ),
    ).toMatchObject({
      state: "DOCUMENTED_ONLY",
      geometryType: "POINT",
      statusReason: expect.stringContaining("Accepted connector and lifecycle responsibility roots"),
      nextGate: expect.stringContaining("canonical earthquake source identity"),
      cannotProve: expect.stringContaining("prediction"),
    });
    expect(
      REPOSITORY_LAYER_CONNECTIONS.every(
        (entry) => entry.artifacts.length >= 3,
      ),
    ).toBe(true);
    expect(
      REPOSITORY_LAYER_CONNECTIONS.flatMap((entry) => entry.artifacts).every(
        (entry) => !entry.path.match(/^(https?:|data:|blob:|file:)/i),
      ),
    ).toBe(true);
    expect(
      REPOSITORY_LAYER_CONNECTIONS.flatMap((entry) => entry.artifacts)
        .filter((entry) => entry.path.startsWith("pipeline_specs/"))
        .every((entry) => entry.kind === "PIPELINE_SPEC"),
    ).toBe(true);
    expect(
      REPOSITORY_LAYER_CONNECTIONS.every((entry) =>
        entry.relatedToolIds.every((id) =>
          ATLAS_WORKBENCH_TOOLS.some((tool) => tool.id === id),
        ),
      ),
    ).toBe(true);
    expect(
      REPOSITORY_LAYER_CONNECTIONS.every((connection) =>
        connection.relatedToolIds.every((toolId) =>
          ATLAS_WORKBENCH_TOOLS.some(
            (tool) =>
              tool.id === toolId &&
              tool.relatedLayerConnectionIds.includes(connection.id),
          ),
        ),
      ),
    ).toBe(true);
    expect(
      ATLAS_WORKBENCH_TOOLS.every((tool) =>
        tool.relatedLayerConnectionIds.every((connectionId) =>
          REPOSITORY_LAYER_CONNECTIONS.some(
            (connection) =>
              connection.id === connectionId &&
              connection.relatedToolIds.includes(tool.id),
          ),
        ),
      ),
    ).toBe(true);
  });

  it("keeps map tools finite and binds workbenches to feature paths", () => {
    expect(MAP_INTERACTION_TOOLS.map((tool) => tool.id)).toEqual([
      "select",
      "draw",
      "measure",
      "profile",
    ]);
    expect(
      MAP_INTERACTION_TOOLS.filter(
        (tool) => tool.state === "AVAILABLE_IN_SITE",
      ).map((tool) => tool.id),
    ).toEqual(["select"]);
    expect(ATLAS_WORKBENCH_TOOLS).toHaveLength(10);
    expect(
      ATLAS_WORKBENCH_TOOLS.every((tool) =>
        tool.featurePath.startsWith("apps/explorer-web/src/features/"),
      ),
    ).toBe(true);
  });

  it("separates a multiscale time preview vocabulary from the committed snapshot", () => {
    expect(TEMPORAL_EXTENTS[0]?.label).toBe("Hadean");
    expect(TEMPORAL_EXTENTS.some((entry) => entry.id === "time:present")).toBe(true);
    const snapshot = createInitialSnapshot(new Date("2026-09-09T00:00:00Z"));
    expect(snapshot.committedTimeId).toBe("time:modern");
    expect(snapshot.capturedAt).toBe("2026-09-09T00:00:00.000Z");
    expect(snapshot.draftOnly).toBe(true);
  });

  it("returns only the four finite Focus outcomes", () => {
    expect(evaluateFocusSelection("layer:kansas-frame").outcome).toBe("ANSWER");
    expect(evaluateFocusSelection("layer:watershed-storage").outcome).toBe("ABSTAIN");
    expect(
      evaluateFocusSelection(
        "layer:weather-window",
        false,
        "view:weather-window",
      ),
    ).toMatchObject({
      outcome: "ABSTAIN",
      reasonCode: "VIEW_DATA_HELD",
      evidenceRefs: [],
    });
    expect(evaluateFocusSelection("layer:protected-context").outcome).toBe("DENY");
    expect(
      evaluateFocusSelection(
        "layer:protected-context",
        false,
        "view:archaeology",
      ).outcome,
    ).toBe("DENY");
    expect(evaluateFocusSelection("layer:does-not-exist").outcome).toBe("ERROR");
    expect(evaluateFocusSelection("layer:kansas-frame", true).outcome).toBe("ERROR");
  });

  it("creates a network-free inline MapLibre style", () => {
    const snapshot = createInitialSnapshot();
    const style = createLivingAtlasStyle(
      "GLOBE",
      snapshot.layers,
      snapshot.committedTimeId,
    );
    expect(style.projection).toMatchObject({ type: "globe" });
    expect(JSON.stringify(style)).not.toMatch(/https?:|pmtiles:|data:|blob:|file:/i);
    expect(Object.values(style.sources ?? {}).every((source) => source.type === "geojson")).toBe(true);
  });

  it("applies committed time to map visibility while preserving timeless context", () => {
    const snapshot = createInitialSnapshot();
    const layerStates = snapshot.layers.map((entry) => Object.freeze({
      ...entry,
      visible: [
        "layer:kansas-frame",
        "layer:county-locators",
        "layer:rail-study",
      ].includes(entry.id),
    }));
    const modern = createLivingAtlasStyle("2D", layerStates, "time:modern");
    const twentiethCentury = createLivingAtlasStyle(
      "2D",
      layerStates,
      "time:1900s",
    );
    const visibility = (style: ReturnType<typeof createLivingAtlasStyle>, id: string) =>
      style.layers?.find((entry) => entry.id === id)?.layout?.visibility;

    expect(visibility(modern, "layer:kansas-frame")).toBe("visible");
    expect(visibility(modern, "layer:county-locators")).toBe("visible");
    expect(visibility(modern, "layer:rail-study")).toBe("none");
    expect(visibility(twentiethCentury, "layer:kansas-frame")).toBe("visible");
    expect(visibility(twentiethCentury, "layer:county-locators")).toBe("none");
    expect(visibility(twentiethCentury, "layer:rail-study")).toBe("visible");
  });

  it("clears stale selection and evidence when committing a different time bucket", () => {
    const snapshot = createInitialSnapshot(new Date("2026-09-10T00:00:00.000Z"));
    const selected = Object.freeze({
      ...snapshot,
      selectedLayerId: "layer:county-locators",
      evidenceRefs: Object.freeze(["evidence:site-local-county-locators"]),
    });
    const committed = commitSnapshotTime(
      selected,
      "time:1900s",
      new Date("2026-09-10T01:00:00.000Z"),
    );

    expect(committed).toMatchObject({
      committedTimeId: "time:1900s",
      selectedLayerId: null,
      evidenceRefs: [],
      capturedAt: "2026-09-10T01:00:00.000Z",
    });
    expect(committed.layers.find((entry) => entry.id === "layer:county-locators")?.visible)
      .toBe(false);
    expect(committed.layers.find((entry) => entry.id === "layer:kansas-frame")?.visible)
      .toBe(true);
  });

  it("keeps same-time commits idempotent", () => {
    const snapshot = createInitialSnapshot(new Date("2026-09-10T00:00:00.000Z"));
    const selected = Object.freeze({
      ...snapshot,
      selectedLayerId: "layer:county-locators",
      evidenceRefs: evaluateFocusSelection("layer:county-locators").evidenceRefs,
    });
    const committed = commitSnapshotTime(
      selected,
      selected.committedTimeId,
      new Date("2026-09-10T01:00:00.000Z"),
    );

    expect(committed).toBe(selected);
    expect(committed.selectedLayerId).toBe("layer:county-locators");
    expect(committed.evidenceRefs).toEqual(selected.evidenceRefs);
    expect(committed.capturedAt).toBe("2026-09-10T00:00:00.000Z");
  });

  it("preserves compatible timeless evidence and protected DENY across time", () => {
    const snapshot = createInitialSnapshot(new Date("2026-09-10T00:00:00.000Z"));
    const timeless = Object.freeze({
      ...snapshot,
      selectedLayerId: "layer:kansas-frame",
      evidenceRefs: evaluateFocusSelection("layer:kansas-frame").evidenceRefs,
    });
    const committedTimeless = commitSnapshotTime(
      timeless,
      "time:1900s",
      new Date("2026-09-10T01:00:00.000Z"),
    );
    expect(committedTimeless.selectedLayerId).toBe("layer:kansas-frame");
    expect(committedTimeless.evidenceRefs).toEqual(timeless.evidenceRefs);

    const denied = Object.freeze({
      ...snapshot,
      selectedLayerId: "layer:protected-context",
      evidenceRefs: Object.freeze([]),
    });
    const committedDenied = commitSnapshotTime(
      denied,
      "time:1900s",
      new Date("2026-09-10T01:00:00.000Z"),
    );
    expect(committedDenied.selectedLayerId).toBe("layer:protected-context");
    expect(committedDenied.evidenceRefs).toEqual([]);
  });
  it("replays finite frames deterministically and stops at the terminal frame", () => {
    const frames = ["time:1900s", "time:modern", "time:present"];
    let playback = createInitialPlayback(frames);

    expect(playback).toMatchObject({
      status: "PAUSED",
      index: 0,
      pauseReason: "INITIAL",
    });
    expect(isPlaybackPlaying(playback)).toBe(false);
    expect(playbackFrameId(playback, frames)).toBe("time:1900s");

    playback = reducePlayback(playback, frames, { type: "PLAY" });
    expect(isPlaybackPlaying(playback)).toBe(true);
    expect(playbackHasNext(playback, frames)).toBe(true);

    playback = reducePlayback(playback, frames, { type: "TICK" });
    expect(playback).toMatchObject({ status: "PLAYING", index: 1 });
    playback = reducePlayback(playback, frames, { type: "TICK" });
    expect(playback).toMatchObject({ status: "PLAYING", index: 2 });
    expect(playbackHasNext(playback, frames)).toBe(false);

    playback = reducePlayback(playback, frames, { type: "TICK" });
    expect(playback).toMatchObject({
      status: "PAUSED",
      index: 2,
      pauseReason: "END_OF_TIMELINE",
    });
    expect(reducePlayback(playback, frames, { type: "PLAY" }).pauseReason)
      .toBe("END_OF_TIMELINE");

    playback = reducePlayback(playback, frames, { type: "STEP", delta: -1 });
    expect(playback).toMatchObject({
      status: "PAUSED",
      index: 1,
      pauseReason: "USER_STEP",
    });
  });

  it("keeps step and scrub controls available while reduced motion pauses replay", () => {
    const frames = ["frame:a", "frame:b", "frame:c"];
    let playback = createInitialPlayback(frames, 0, true);

    expect(playback.pauseReason).toBe("REDUCED_MOTION");
    playback = reducePlayback(playback, frames, { type: "PLAY" });
    expect(playback).toMatchObject({
      status: "PAUSED",
      index: 0,
      pauseReason: "REDUCED_MOTION",
    });

    playback = reducePlayback(playback, frames, { type: "STEP", delta: 1 });
    expect(playback).toMatchObject({
      status: "PAUSED",
      index: 1,
      pauseReason: "USER_STEP",
      reducedMotion: true,
    });
    playback = reducePlayback(playback, frames, { type: "SCRUB", index: 99 });
    expect(playback).toMatchObject({
      status: "PAUSED",
      index: 2,
      pauseReason: "SCRUB",
    });

    playback = reducePlayback(playback, frames, {
      type: "SET_REDUCED_MOTION",
      enabled: false,
    });
    expect(playback.reducedMotion).toBe(false);
    playback = reducePlayback(playback, frames, { type: "PLAY" });
    expect(isPlaybackPlaying(playback)).toBe(false);
    playback = reducePlayback(playback, frames, { type: "STEP", delta: -1 });
    playback = reducePlayback(playback, frames, { type: "PLAY" });
    expect(isPlaybackPlaying(playback)).toBe(true);
    playback = reducePlayback(playback, frames, { type: "VISIBILITY_HIDDEN" });
    expect(playback.pauseReason).toBe("HIDDEN_DOCUMENT");
    playback = reducePlayback(playback, frames, {
      type: "PAUSE",
      reason: "EVIDENCE_FAILURE",
    });
    expect(playback.pauseReason).toBe("EVIDENCE_FAILURE");
  });


});
