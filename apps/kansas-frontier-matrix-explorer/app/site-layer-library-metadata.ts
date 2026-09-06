import type { CardInput, Match } from "../../../packages/ui/src/layer-library-model.js";

/** Compatibility projection of eight inspected built-in fixtures. Not source admission,
 * an operational layer registry, or a general adapter for uploaded/remote records.
 * New source-backed catalog delivery must replace this bounded projection, not add
 * production identifiers to this set. Unlisted fixtures retain their legacy controls.
 */
export const INSPECTED_DEMO_IDS: ReadonlySet<string> = new Set([
  "kansas-extent", "water-context", "watershed-context", "prairie-context",
  "geology-context", "elevation-concept", "agriculture-context", "atmosphere-observations",
]);
export type DemoMetadata = Readonly<{
  id: string; title: string; description: string; domain: string; sourceId: string;
  sourceType: string; geometryType: string; bounds: readonly number[];
  validTimeExtent: string; sourceTime: string; releaseTime: string;
  attribution: string; evidenceReference: string; publicStatus: string;
  releaseState: string; defaultOpacity?: number; sensitivityNote: string; correctionNote: string; units: string;
}>;
export type AnalysisBounds = Readonly<{ west: number; south: number; east: number; north: number }>;
export function boundingBoxMatch(bounds: readonly number[], area: AnalysisBounds | null): Match {
  if (!area || !Array.isArray(bounds) || bounds.length !== 4) return null;
  const [west, south, east, north] = bounds;
  const values = [...bounds, area.west, area.south, area.east, area.north];
  if (!values.every(Number.isFinite) || west < -180 || east > 180 || south < -90 || north > 90
    || area.west < -180 || area.east > 180 || area.south < -90 || area.north > 90
    || west > east || south > north || area.west > area.east || area.south > area.north) return null;
  return west <= area.east && east >= area.west && south <= area.north && north >= area.south;
}
export function projectSiteDemoCards<T extends DemoMetadata>(
  layers: readonly T[], area: AnalysisBounds | null, matchesCurrentTime: (layer: T) => Match,
): readonly CardInput[] {
  const cards: CardInput[] = [];
  for (const layer of layers) {
    // Do not read titles, geometry, feature counts, or times of undisclosable entries.
    if (!INSPECTED_DEMO_IDS.has(layer.id) || !["PUBLIC_SAFE", "GENERALIZED"].includes(layer.publicStatus)
      || !["DEMONSTRATION", "GENERALIZED"].includes(layer.releaseState)) continue;
    cards.push({
      id: layer.id, disclosure: "allow", title: layer.title, description: layer.description,
      provider: layer.attribution, domain: layer.domain,
      representation: `${layer.sourceType} · ${layer.geometryType} · fixture`,
      sourceId: layer.sourceId, coverageLabel: area ? "Bounding-box overlap only; not a complete spatial query" : "Analysis area not selected; coverage match unknown",
      areaMatch: boundingBoxMatch(layer.bounds, area), timeLabel: layer.validTimeExtent,
      timeMatch: matchesCurrentTime(layer), sourceTime: layer.sourceTime, releaseTime: layer.releaseTime,
      datasetVersion: "", artifactVersion: "", fixture: true,
      generalized: layer.publicStatus === "GENERALIZED", release: "unreleased",
      // The cleared right is inspection of these built-in synthetic previews only.
      // It says nothing about rights to a real upstream dataset with a similar name.
      access: "allow", rights: "cleared", sensitivity: "public", workspaceAction: "preview",
      runtime: "held", renderGroup: null, defaultOpacity: layer.defaultOpacity, evidenceRef: layer.evidenceReference, units: layer.units,
      limitations: `Built-in demonstration only. Legacy release label: ${layer.releaseState}; not an operational release. ${layer.sensitivityNote} ${layer.correctionNote} Per-feature evidence requires governed resolution.`,
    });
  }
  return cards;
}
