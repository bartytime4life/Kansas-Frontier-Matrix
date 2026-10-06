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

export function acquisitionTerrainRead(body: unknown): AcquisitionTerrain | null {
  if (!body || typeof body !== "object" || Array.isArray(body) || !("discovery" in body)) throw new Error("Saved terrain response is invalid.");
  if (body.discovery === null) return null;
  const discovery = parseAcquisitionTerrain(body.discovery);
  if (!discovery) throw new Error("Saved terrain metadata failed validation. It has not been loaded.");
  return discovery;
}

export async function verifyAcquisitionTerrainSave(body: unknown, submitted: AcquisitionTerrain): Promise<void> {
  if (!body || typeof body !== "object" || !("saved" in body) || body.saved !== true || !("sha256" in body)
    || typeof body.sha256 !== "string" || !/^[a-f0-9]{64}$/.test(body.sha256)) throw new Error("Terrain save was not confirmed. Check saved status before retrying.");
  const saved = acquisitionTerrainRead(body), expected = parseAcquisitionTerrain(submitted);
  if (!saved || !expected || JSON.stringify(saved) !== JSON.stringify(expected)) throw new Error("Saved terrain identity differs from the submitted preview.");
  const digest = Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(JSON.stringify(expected)))), byte => byte.toString(16).padStart(2, "0")).join("");
  if (digest !== body.sha256) throw new Error("Saved terrain digest differs from the submitted preview.");
}
