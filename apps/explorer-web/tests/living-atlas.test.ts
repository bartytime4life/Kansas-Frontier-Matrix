import { describe, expect, it } from "vitest";
import {
  ATLAS_VIEWS,
  EVIDENCE_RECORDS,
  LAYER_RECORDS,
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
    expect(evaluateFocusSelection("layer:protected-context").outcome).toBe("DENY");
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
