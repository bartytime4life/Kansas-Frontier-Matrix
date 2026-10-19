import { parseTerrainDiscovery } from "./terrain-provenance-data";

/** Site projection only; the original worker snapshot remains its own artifact. */
export function parseAcquisitionTerrain(value: unknown) {
  const parsed = parseTerrainDiscovery(value);
  if (!parsed || parsed.rejectedProjects !== 0 || parsed.declaredProjectCount !== parsed.projects.length) return null;
  return {
    schema_version: "kfm-3dep-discovery-v1", selection: "KS_ provider prefix",
    captured_at: parsed.capturedAt, project_count: parsed.projects.length,
    complete_for_prefix: parsed.completeForPrefix, complete_for_state: false,
    metadata_bytes_captured: parsed.metadataBytes,
    projects: parsed.projects.map(item => ({
      provider_work_unit: item.id, source_url: item.sourceUrl,
      metadata_sha256: item.metadataSha256, metadata_bytes: item.metadataBytes,
      point_count: item.pointCount, bounds: item.nativeBounds,
      srs: { authority: item.horizontalCrs?.split(":")[0] ?? item.verticalCrs?.split(":")[0] ?? null,
        horizontal: item.horizontalCrs?.split(":")[1] ?? null, vertical: item.verticalCrs?.split(":")[1] ?? null },
      temporal_start: item.acquisitionStart, temporal_end: item.acquisitionEnd,
      temporal_reason: item.acquisitionReason,
    })),
  };
}
export type AcquisitionTerrain = NonNullable<ReturnType<typeof parseAcquisitionTerrain>>;
