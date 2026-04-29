import { TrustBadges, type TrustBadge } from "./trustBadges";

export type EvidenceDrawerPayload = {
  schema_version: "v1";
  object_type: "EvidenceDrawerPayload";
  claim_ref: string;
  evidence_bundle_ref: string;
  decision_ref: string;
  release_ref: string;
  trust_badges: TrustBadge[];
  limitations: string[];
  redaction_receipt_refs: string[];
};

export default function EvidenceDrawer({ payload }: { payload: EvidenceDrawerPayload }) {
  return (
    <aside style={{ borderLeft: "1px solid #ddd", padding: 12, width: 340 }}>
      <h2>Evidence Drawer</h2>
      <p style={{ marginTop: 0, color: "#555" }}>Inspect why this claim is visible and how it was constrained.</p>

      <TrustBadges badges={payload.trust_badges} />

      <h4>References</h4>
      <ul>
        <li><strong>Claim:</strong> {payload.claim_ref}</li>
        <li><strong>EvidenceBundle:</strong> {payload.evidence_bundle_ref}</li>
        <li><strong>DecisionEnvelope:</strong> {payload.decision_ref}</li>
        <li><strong>ReleaseManifest:</strong> {payload.release_ref}</li>
      </ul>

      <h4>Limitations</h4>
      <ul>{payload.limitations.map((item) => <li key={item}>{item}</li>)}</ul>

      <h4>Redaction receipts</h4>
      <ul>{payload.redaction_receipt_refs.map((ref) => <li key={ref}>{ref}</li>)}</ul>
    </aside>
  );
}
