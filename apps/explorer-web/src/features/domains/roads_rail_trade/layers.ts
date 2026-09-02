/**
 * Governed Roads/Rail/Trade trust-overlay helpers.
 *
 * This module consumes an already-governed trust projection. It does not fetch
 * data, calculate policy, resolve evidence, authorize release, or publish a
 * feature. Unknown status and audience mismatches fail closed.
 */

export type TrustDecision = "publish" | "quarantine" | "deny";
export type TrustAudience = "public" | "steward";
export type TrustMode = TrustAudience;
export type CollectionDecision = "publish" | "quarantine-partial" | "deny-partial" | "deny";

export type FrontierRouteTrustFeature = {
  kfm_id: string;
  name: string;
  decision: TrustDecision;
  code: string;
  detail: string;
  source_uri: string;
  policy_decision_ref: string;
  evidence_refs: string[];
  release_id: string | null;
  visible_in_public_catalog: boolean;
};

export type FrontierRouteTrustStatus = {
  profile: "kfm.roads-rail-trade.frontier-route-trust-status.v1";
  collection_id: string;
  generated_at: string;
  audience: TrustAudience;
  collection_decision: CollectionDecision;
  features: FrontierRouteTrustFeature[];
};

export type TrustOverlay = Pick<FrontierRouteTrustFeature, "decision" | "code" | "visible_in_public_catalog">;

export type RouteFeatureLike = {
  properties?: { kfm_id?: string; [key: string]: unknown } | null;
  [key: string]: unknown;
};

export class TrustBoundaryError extends Error {
  readonly code: "PUBLIC_PAYLOAD_REQUIRED" | "DUPLICATE_FEATURE_ID";
  constructor(code: "PUBLIC_PAYLOAD_REQUIRED" | "DUPLICATE_FEATURE_ID", message: string) {
    super(message);
    this.name = "TrustBoundaryError";
    this.code = code;
  }
}

export function buildTrustIndex(status: FrontierRouteTrustStatus): ReadonlyMap<string, FrontierRouteTrustFeature> {
  const index = new Map<string, FrontierRouteTrustFeature>();
  for (const feature of status.features) {
    if (index.has(feature.kfm_id)) {
      throw new TrustBoundaryError("DUPLICATE_FEATURE_ID", `duplicate trust status for ${feature.kfm_id}`);
    }
    index.set(feature.kfm_id, feature);
  }
  return index;
}

function assertAudience(status: FrontierRouteTrustStatus, mode: TrustMode): void {
  if (mode === "public" && status.audience !== "public") {
    throw new TrustBoundaryError("PUBLIC_PAYLOAD_REQUIRED", "public mode requires a public-safe projection; steward payloads must not be client-filtered");
  }
}

export function buildTrustOverlay(status: FrontierRouteTrustStatus, kfmId: string, mode: TrustMode): TrustOverlay | null {
  assertAudience(status, mode);
  const row = buildTrustIndex(status).get(kfmId);
  if (!row) return null;
  if (mode === "public" && (row.decision !== "publish" || !row.visible_in_public_catalog || !row.release_id)) return null;
  return { decision: row.decision, code: row.code, visible_in_public_catalog: row.visible_in_public_catalog };
}

export function filterFeaturesByTrust<T extends RouteFeatureLike>(features: readonly T[], status: FrontierRouteTrustStatus, mode: TrustMode): T[] {
  assertAudience(status, mode);
  const index = buildTrustIndex(status);
  return features.filter((feature) => {
    const kfmId = feature.properties?.kfm_id;
    if (!kfmId) return false;
    const trust = index.get(kfmId);
    if (!trust) return false;
    if (mode === "public") return trust.decision === "publish" && trust.visible_in_public_catalog && Boolean(trust.release_id);
    return true;
  });
}

const COLOR_BY_DECISION: Readonly<Record<TrustDecision, string>> = { publish: "#2563eb", quarantine: "#d97706", deny: "#dc2626" };
const WIDTH_BY_DECISION: Readonly<Record<TrustDecision, number>> = { publish: 4, quarantine: 5, deny: 5 };

function expressionEntries(status: FrontierRouteTrustStatus, mode: TrustMode, values: Readonly<Record<TrustDecision, string | number>>): unknown[] {
  assertAudience(status, mode);
  const entries: unknown[] = [];
  for (const row of [...status.features].sort((a, b) => a.kfm_id.localeCompare(b.kfm_id))) {
    if (mode === "public" && (row.decision !== "publish" || !row.visible_in_public_catalog || !row.release_id)) continue;
    entries.push(row.kfm_id, values[row.decision]);
  }
  return entries;
}

export function buildLineColorExpression(status: FrontierRouteTrustStatus, mode: TrustMode): readonly unknown[] {
  return ["match", ["get", "kfm_id"], ...expressionEntries(status, mode, COLOR_BY_DECISION), "#6b7280"] as const;
}

export function buildLineWidthExpression(status: FrontierRouteTrustStatus, mode: TrustMode): readonly unknown[] {
  return ["match", ["get", "kfm_id"], ...expressionEntries(status, mode, WIDTH_BY_DECISION), 3] as const;
}
