import { evaluatePMTilesArchive } from "./runtimePolicy";
import type {
  PMTilesArchiveRef,
  PMTilesRuntimeDecision,
  PMTilesTimeIndex
} from "./types";

function normalizeArchive(ref: PMTilesArchiveRef): PMTilesArchiveRef {
  const normalized = { ...ref };
  if (
    typeof normalized.completeness_pct !== "number" &&
    typeof normalized.tile_count === "number" &&
    typeof normalized.expected_tile_count === "number" &&
    normalized.expected_tile_count > 0
  ) {
    normalized.completeness_pct = normalized.tile_count / normalized.expected_tile_count;
  }
  return normalized;
}

function validArchiveLike(value: unknown): value is PMTilesArchiveRef {
  if (!value || typeof value !== "object") return false;
  const rec = value as Record<string, unknown>;
  return typeof rec.archive_id === "string" && typeof rec.href === "string";
}

export async function loadPMTilesTimeIndex(url: string): Promise<PMTilesTimeIndex> {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`Failed to load PMTiles time index: ${response.status}`);
  const payload = await response.json();
  if (!payload || typeof payload !== "object") throw new Error("Malformed PMTiles time index");

  const base_archive = (payload as Record<string, unknown>).base_archive;
  const delta_archives = (payload as Record<string, unknown>).delta_archives ?? [];
  if (!validArchiveLike(base_archive) || !Array.isArray(delta_archives)) {
    throw new Error("Malformed PMTiles time index: missing required fields");
  }

  return {
    object_type: "PMTilesTimeIndex",
    generated_at: (payload as Record<string, unknown>).generated_at as string | undefined,
    base_archive: normalizeArchive(base_archive),
    delta_archives: delta_archives.filter(validArchiveLike).map(normalizeArchive)
  };
}

function sortDeltas(deltas: PMTilesArchiveRef[]): PMTilesArchiveRef[] {
  return [...deltas].sort((a, b) =>
    String(a.generated_at ?? a.archive_id).localeCompare(String(b.generated_at ?? b.archive_id))
  );
}

export function getPMTilesRuntimeDecision(index: PMTilesTimeIndex): PMTilesRuntimeDecision {
  return {
    base: evaluatePMTilesArchive(index.base_archive),
    deltas: sortDeltas(index.delta_archives ?? []).map(evaluatePMTilesArchive)
  };
}

export function selectRenderablePMTilesArchives(index: PMTilesTimeIndex): PMTilesArchiveRef[] {
  const decision = getPMTilesRuntimeDecision(index);
  const eligible = [decision.base, ...decision.deltas].filter((entry) =>
    entry.decision.startsWith("ALLOW_RENDER")
  );
  const base = eligible.find((entry) => entry.archive.archive_id === index.base_archive.archive_id);
  const deltas = eligible
    .filter((entry) => entry.archive.archive_id !== index.base_archive.archive_id)
    .sort((a, b) => String(a.archive.generated_at ?? "").localeCompare(String(b.archive.generated_at ?? "")));
  return [base?.archive, deltas.at(-1)?.archive].filter(Boolean) as PMTilesArchiveRef[];
}
