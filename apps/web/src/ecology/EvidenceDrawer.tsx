import { TrustBadges, type TrustBadge } from "./trustBadges";

export type EvidenceDrawerPayload = {
  schema_version: "v1";
  object_type: "EcologyEvidenceDrawerPayload";
  payload_id: string;
  claim_ref: string;
  evidence_bundle_ref: string;
  decision_ref: string;
  release_ref: string;
  decision: "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";
  visible_outcome: "shown" | "generalized" | "withheld" | "unavailable";
  summary: {
    headline: string;
    trust_note: string;
    taxon?: string;
    habitat_class?: string;
    knowledge_character?: "derived" | "observed" | "interpreted" | "modeled";
  };
  sources: Array<{
    source_ref: string;
    source_role:
      | "TAXONOMIC_AUTHORITY"
      | "OBSERVATION_SYSTEM"
      | "AGGREGATOR"
      | "DERIVED_MODEL_LAYER"
      | "SENSITIVE_OCCURRENCE"
      | "BASELINE"
      | "REGULATORY_CONTEXT"
      | "RENDER_DESCRIPTOR";
    citation: string;
  }>;
  evidence_refs: string[];
  trust_badges: TrustBadge[];
  policy_flags?: Array<"sensitivity" | "rights" | "review_required" | "generalized" | "derived_context" | "redacted">;
  redaction_receipt_refs?: string[];
  limitations?: string[];
  freshness: {
    generated_at: string;
    stale_after: string;
  };
  spec_hash: string;
};

export default function EvidenceDrawer({ payload }: { payload: EvidenceDrawerPayload }) {
  return (
    <aside style={{ borderLeft: "1px solid #ddd", padding: 12, width: 340 }}>
      <h2>Evidence Drawer</h2>
      <p style={{ marginTop: 0, color: "#555" }}>Inspect why this claim is visible and how it was constrained.</p>
      <p><strong>{payload.summary.headline}</strong></p>
      <p style={{ color: "#444" }}>{payload.summary.trust_note}</p>

      <TrustBadges badges={payload.trust_badges} />

      <h4>References</h4>
      <ul>
        <li><strong>Payload:</strong> {payload.payload_id}</li>
        <li><strong>Claim:</strong> {payload.claim_ref}</li>
        <li><strong>EvidenceBundle:</strong> {payload.evidence_bundle_ref}</li>
        <li><strong>DecisionEnvelope:</strong> {payload.decision_ref}</li>
        <li><strong>ReleaseManifest:</strong> {payload.release_ref}</li>
      </ul>

      <h4>Sources</h4>
      <ul>{payload.sources.map((source) => <li key={source.source_ref}>{source.source_role}: {source.citation}</li>)}</ul>

      {payload.limitations?.length ? <><h4>Limitations</h4><ul>{payload.limitations.map((item) => <li key={item}>{item}</li>)}</ul></> : null}

      {payload.redaction_receipt_refs?.length ? <><h4>Redaction receipts</h4><ul>{payload.redaction_receipt_refs.map((ref) => <li key={ref}>{ref}</li>)}</ul></> : null}
    </aside>
  );
}
