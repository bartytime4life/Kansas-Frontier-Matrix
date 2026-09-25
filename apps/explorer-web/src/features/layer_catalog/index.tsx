import type { LayerRecord } from "../living_atlas/types";

/** Site-local catalog state. This projection cannot authorize a release or load a tile. */
export type LayerCatalogRow = Readonly<{
  checked: boolean;
  disabled: boolean;
  status: "AVAILABLE" | "HELD" | "DENIED" | "UNAVAILABLE" | "TIME_HOLD";
}>;

export function projectLayerCatalogRow(
  record: LayerRecord | null,
  visible: boolean,
  temporallyCompatible: boolean,
): LayerCatalogRow {
  if (record === null || record.availability !== "AVAILABLE") {
    return Object.freeze({
      checked: false,
      disabled: true,
      status: record?.availability ?? "UNAVAILABLE",
    });
  }
  if (!temporallyCompatible) {
    return Object.freeze({ checked: false, disabled: true, status: "TIME_HOLD" });
  }
  return Object.freeze({ checked: visible, disabled: false, status: "AVAILABLE" });
}
