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
  evaluateFocusSelection,
} from "../src/features/living_atlas";

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
    expect(REPOSITORY_LAYER_CONNECTIONS).toHaveLength(14);
    expect(
      REPOSITORY_LAYER_CONNECTIONS.filter(
        (entry) => entry.state === "FIXTURE_ONLY",
      ).map((entry) => entry.id),
    ).toEqual(["connection:wbd-huc12"]);
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
    ).toMatchObject({ outcome: "ABSTAIN", reasonCode: "VIEW_DATA_HELD" });
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
    const style = createLivingAtlasStyle("GLOBE", snapshot.layers);
    expect(style.projection).toMatchObject({ type: "globe" });
    expect(JSON.stringify(style)).not.toMatch(/https?:|pmtiles:|data:|blob:|file:/i);
    expect(Object.values(style.sources ?? {}).every((source) => source.type === "geojson")).toBe(true);
  });
});
