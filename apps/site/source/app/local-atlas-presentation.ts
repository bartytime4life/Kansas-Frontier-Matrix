import type { AtlasGroup } from "./local-atlas-client";
export function atlasCollectionLabel(group: AtlasGroup): string {
  const names: Record<string, string> = { ppt: "Precipitation", tmean: "Mean temperature", tmin: "Minimum temperature", tmax: "Maximum temperature", tdmean: "Mean dew point", vpdmin: "Minimum vapor pressure deficit", vpdmax: "Maximum vapor pressure deficit", solclear: "Clear-sky solar radiation", soltotal: "Total solar radiation", solslope: "Slope-adjusted solar radiation", soltrans: "Solar transmittance" };
  return `${names[group.variable.toLowerCase()] ?? group.variable.toUpperCase()} · ${group.period} · ${group.resolution.replace(/(\d)(km|m)$/, "$1 $2")}`;
}
export function atlasInspectorLabel(key: string, climate: boolean, difference: boolean): string {
  if (!climate) return key;
  const labels: Record<string, string> = { geoid: "County identifier", name: "County", value: difference ? "Difference (B − A)" : "County mean", mean: difference ? "Period B mean" : "County mean", minimum: difference ? "Period B minimum" : "Minimum grid value", maximum: difference ? "Period B maximum" : "Maximum grid value", valid_pixels: difference ? "Period B valid grid cells" : "Valid grid cells", valid_pixels_A: "Period A valid grid cells", valueA: "Period A value", valueB: "Period B value" };
  return labels[key] ?? key;
}
/** Fit into the exposed map rectangle, not behind a mobile control sheet. */
export function atlasMobilePadding(mapTop: number, mapBottom: number, sheetTop: number) {
  const height = Math.max(1, mapBottom - mapTop);
  return { top: 32, left: 24, right: 24, bottom: Math.max(24, Math.min(height - 100, mapBottom - sheetTop + 16)) };
}
