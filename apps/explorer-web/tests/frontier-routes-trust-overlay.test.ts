import { describe, expect, it } from "vitest";
import { TrustBoundaryError, buildLineColorExpression, buildTrustIndex, buildTrustOverlay, filterFeaturesByTrust, type FrontierRouteTrustStatus, type RouteFeatureLike } from "../src/features/domains/roads_rail_trade/layers";

const stewardStatus: FrontierRouteTrustStatus = {
  profile: "kfm.roads-rail-trade.frontier-route-trust-status.v1",
  collection_id: "synthetic-steward-routes",
  generated_at: "2026-03-31T12:00:00Z",
  audience: "steward",
  collection_decision: "deny-partial",
  features: [
    { kfm_id: "kfm://feature/route/published", name: "Published", decision: "publish", code: "ALLOWED", detail: "Synthetic fixture", source_uri: "https://example.invalid/published", policy_decision_ref: "kfm://policy-decision/published", evidence_refs: ["kfm://evidence/published"], release_id: "kfm://release/published/v1", visible_in_public_catalog: true },
    { kfm_id: "kfm://feature/route/quarantined", name: "Quarantined", decision: "quarantine", code: "RIGHTS_REVIEW_REQUIRED", detail: "Synthetic fixture", source_uri: "https://example.invalid/quarantined", policy_decision_ref: "kfm://policy-decision/quarantined", evidence_refs: ["kfm://evidence/quarantined"], release_id: null, visible_in_public_catalog: false },
    { kfm_id: "kfm://feature/route/denied", name: "Denied", decision: "deny", code: "POLICY_DENIED", detail: "Synthetic fixture", source_uri: "https://example.invalid/denied", policy_decision_ref: "kfm://policy-decision/denied", evidence_refs: ["kfm://evidence/denied"], release_id: null, visible_in_public_catalog: false }
  ]
};

const publicStatus: FrontierRouteTrustStatus = { ...stewardStatus, collection_id: "synthetic-public-routes", audience: "public", collection_decision: "publish", features: [stewardStatus.features[0]] };
const routeFeatures: RouteFeatureLike[] = [
  { properties: { kfm_id: "kfm://feature/route/published" } },
  { properties: { kfm_id: "kfm://feature/route/quarantined" } },
  { properties: { kfm_id: "kfm://feature/route/denied" } },
  { properties: { kfm_id: "kfm://feature/route/unknown" } },
  { properties: {} }
];

describe("frontier route trust overlay", () => {
  it("requires a public-safe payload instead of client-filtering steward rows", () => {
    expect(() => filterFeaturesByTrust(routeFeatures, stewardStatus, "public")).toThrowError(TrustBoundaryError);
  });
  it("shows only released publish entries in public mode", () => {
    const visible = filterFeaturesByTrust(routeFeatures, publicStatus, "public");
    expect(visible).toHaveLength(1);
    expect(visible[0].properties?.kfm_id).toBe("kfm://feature/route/published");
  });
  it("shows all known entries to an admitted steward and hides unknown status", () => {
    const visible = filterFeaturesByTrust(routeFeatures, stewardStatus, "steward");
    expect(visible.map((item) => item.properties?.kfm_id)).toEqual(["kfm://feature/route/published", "kfm://feature/route/quarantined", "kfm://feature/route/denied"]);
  });
  it("returns the minimal map-hover payload", () => {
    expect(buildTrustOverlay(publicStatus, "kfm://feature/route/published", "public")).toEqual({ decision: "publish", code: "ALLOWED", visible_in_public_catalog: true });
    expect(buildTrustOverlay(publicStatus, "kfm://feature/route/unknown", "public")).toBeNull();
  });
  it("rejects duplicate feature identities", () => {
    const duplicate: FrontierRouteTrustStatus = { ...stewardStatus, features: [...stewardStatus.features, stewardStatus.features[0]] };
    expect(() => buildTrustIndex(duplicate)).toThrowError(/duplicate trust status/);
  });
  it("builds deterministic trust styling expressions", () => {
    expect(buildLineColorExpression(stewardStatus, "steward")).toEqual(["match", ["get", "kfm_id"], "kfm://feature/route/denied", "#dc2626", "kfm://feature/route/published", "#2563eb", "kfm://feature/route/quarantined", "#d97706", "#6b7280"]);
  });
});
