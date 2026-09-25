import { describe, expect, it } from "vitest";
import { projectLayerCatalogRow } from "../src/features/layer_catalog";
import { LAYER_RECORDS } from "../src/features/living_atlas";

describe("site-local layer catalog row", () => {
  const available = LAYER_RECORDS.find((entry) => entry.availability === "AVAILABLE")!;
  const held = LAYER_RECORDS.find((entry) => entry.availability === "HELD")!;

  it("allows a compatible, available fixture layer", () => {
    expect(projectLayerCatalogRow(available, true, true)).toEqual({
      checked: true, disabled: false, status: "AVAILABLE",
    });
  });

  it("clears visibility and disables held, missing, and time-incompatible layers", () => {
    expect(projectLayerCatalogRow(held, true, true)).toEqual({
      checked: false, disabled: true, status: "HELD",
    });
    expect(projectLayerCatalogRow(null, true, true)).toEqual({
      checked: false, disabled: true, status: "UNAVAILABLE",
    });
    expect(projectLayerCatalogRow(available, true, false)).toEqual({
      checked: false, disabled: true, status: "TIME_HOLD",
    });
  });
});
