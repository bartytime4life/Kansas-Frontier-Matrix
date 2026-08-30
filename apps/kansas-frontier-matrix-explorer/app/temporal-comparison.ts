import type { EvidenceState, LayerRecord } from "./explorer-data";
import { isFeatureAvailableAtTime } from "./map-interface";

export type TemporalComparisonLayer = Readonly<{
  layerId: string;
  title: string;
  domain: string;
  temporalMode: "exact" | "through" | "untimed";
  timeARecordCount: number;
  timeBRecordCount: number;
  stableRecordIds: readonly string[];
  enteredRecordIds: readonly string[];
  exitedRecordIds: readonly string[];
  timeAEvidenceStates: Readonly<Record<string, number>>;
  timeBEvidenceStates: Readonly<Record<string, number>>;
}>;

export type TemporalComparison = Readonly<{
  format: "kfm-temporal-catalog-comparison-v1";
  authority: "SITE_LOCAL_CONTEXT_ONLY";
  interpretation: "CATALOG_AVAILABILITY_NOT_OBSERVED_CHANGE";
  timeA: number;
  timeB: number;
  timeARecordCount: number;
  timeBRecordCount: number;
  recordDelta: number;
  timeALayerCount: number;
  timeBLayerCount: number;
  changedLayerCount: number;
  layers: readonly TemporalComparisonLayer[];
  limitations: readonly string[];
}>;

const countEvidenceStates = (states: readonly EvidenceState[]) => states.reduce<Record<string, number>>((counts, state) => {
  counts[state] = (counts[state] ?? 0) + 1;
  return counts;
}, {});

export const buildTemporalComparison = (
  layers: readonly LayerRecord[],
  timeA: number,
  timeB: number,
): TemporalComparison => {
  const rows = layers.map<TemporalComparisonLayer>((layer) => {
    const atA = layer.data.features.filter((feature) => isFeatureAvailableAtTime(layer, feature.properties.year, timeA));
    const atB = layer.data.features.filter((feature) => isFeatureAvailableAtTime(layer, feature.properties.year, timeB));
    const idsA = new Set(atA.map((feature) => feature.properties.fid));
    const idsB = new Set(atB.map((feature) => feature.properties.fid));

    return Object.freeze({
      layerId: layer.id,
      title: layer.title,
      domain: layer.domain,
      temporalMode: layer.temporal?.mode ?? "untimed",
      timeARecordCount: atA.length,
      timeBRecordCount: atB.length,
      stableRecordIds: Object.freeze([...idsA].filter((id) => idsB.has(id)).sort()),
      enteredRecordIds: Object.freeze([...idsB].filter((id) => !idsA.has(id)).sort()),
      exitedRecordIds: Object.freeze([...idsA].filter((id) => !idsB.has(id)).sort()),
      timeAEvidenceStates: Object.freeze(countEvidenceStates(atA.map((feature) => feature.properties.evidenceState))),
      timeBEvidenceStates: Object.freeze(countEvidenceStates(atB.map((feature) => feature.properties.evidenceState))),
    });
  });

  const timeARecordCount = rows.reduce((count, row) => count + row.timeARecordCount, 0);
  const timeBRecordCount = rows.reduce((count, row) => count + row.timeBRecordCount, 0);

  return Object.freeze({
    format: "kfm-temporal-catalog-comparison-v1",
    authority: "SITE_LOCAL_CONTEXT_ONLY",
    interpretation: "CATALOG_AVAILABILITY_NOT_OBSERVED_CHANGE",
    timeA,
    timeB,
    timeARecordCount,
    timeBRecordCount,
    recordDelta: timeBRecordCount - timeARecordCount,
    timeALayerCount: rows.filter((row) => row.timeARecordCount > 0).length,
    timeBLayerCount: rows.filter((row) => row.timeBRecordCount > 0).length,
    changedLayerCount: rows.filter((row) => row.enteredRecordIds.length > 0 || row.exitedRecordIds.length > 0).length,
    layers: Object.freeze(rows),
    limitations: Object.freeze([
      "This comparison reports which site-local records are time-compatible at Time A and Time B; it does not detect real-world change.",
      "Untimed context can appear at both times and must not be interpreted as historical persistence.",
      "Entered and exited identifiers describe fixture availability under declared temporal rules, not imagery, causation, or evidence of an event.",
    ]),
  });
};
