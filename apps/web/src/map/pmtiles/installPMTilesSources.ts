import type { PMTiles } from "pmtiles";
import { Protocol } from "pmtiles";
import type { PMTilesArchiveRef } from "./types";
import { evaluatePMTilesArchive } from "./runtimePolicy";

let installedProtocol = false;

export function installPMTilesSources(map: any, archives: PMTilesArchiveRef[]) {
  const protocol = new Protocol();
  if (!installedProtocol) {
    map.addProtocol?.("pmtiles", protocol.tile);
    installedProtocol = true;
  }

  const report = { added: [] as string[], denied: [] as string[], reasons: {} as Record<string, string[]>, qc_badges: {} as Record<string, string | undefined>, evidence_refs: {} as Record<string, string[]> };

  for (const archive of archives) {
    const evalResult = evaluatePMTilesArchive(archive);
    const sourceId = `pmtiles-${archive.archive_id}`;
    if (map.getSource?.(sourceId)) continue;
    if (evalResult.decision === "DENY_RENDER") {
      report.denied.push(sourceId);
      report.reasons[sourceId] = evalResult.reasons;
      continue;
    }

    protocol.add(new (Object as unknown as { new (href: string): PMTiles })(archive.href));
    map.addSource(sourceId, { type: "vector", url: `pmtiles://${archive.href}` });
    report.added.push(sourceId);
    report.qc_badges[sourceId] = evalResult.review_badge_reason;
    report.evidence_refs[sourceId] = [archive.proof_ref, archive.signature_ref, archive.release_ref, archive.promotion_decision_ref].filter(Boolean) as string[];
  }

  return report;
}
