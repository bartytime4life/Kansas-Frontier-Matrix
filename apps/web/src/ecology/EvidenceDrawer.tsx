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

  policy_flags?: Array<
    | "sensitivity"
    | "rights"
    | "review_required"
    | "generalized"
    | "derived_context"
    | "redacted"
  >;

  redaction_receipt_refs?: string[];
  limitations?: string[];

  freshness: {
    generated_at: string;
    stale_after: string;
  };

  spec_hash: string;
};

export type EvidenceDrawerLayerMetadata = {
  layerId: string;
  evidenceBundleRef: string;
  promotionDecisionRef: string;
  runReceiptRef: string;
  allowedFields: string[];
  publicSafe: boolean;
};

export type EvidenceDrawerProps = {
  payload?: EvidenceDrawerPayload;
  open?: boolean;
  onClose?: () => void;
  featureProperties?: Record<string, unknown>;
  layerMetadata?: EvidenceDrawerLayerMetadata;
};

function FieldList({ value }: { value?: string[] }) {
  if (!value?.length) return null;

  return (
    <ul>
      {value.map((item) => (
        <li key={item}>
          <code>{item}</code>
        </li>
      ))}
    </ul>
  );
}

export default function EvidenceDrawer({
  payload,
  open = true,
  onClose,
  featureProperties,
  layerMetadata
}: EvidenceDrawerProps) {
  if (!open) return null;

  return (
    <aside
      style={{
        borderLeft: "1px solid #ddd",
        padding: 12,
        width: 360,
        maxHeight: "100%",
        overflow: "auto",
        background: "white"
      }}
    >
      <div style={{ display: "flex", justifyContent: "space-between", gap: 12 }}>
        <h2 style={{ marginTop: 0 }}>Evidence Drawer</h2>
        {onClose ? (
          <button type="button" onClick={onClose}>
            Close
          </button>
        ) : null}
      </div>

      <p style={{ marginTop: 0, color: "#555" }}>
        Inspect why this claim or layer is visible and how it was constrained.
      </p>

      {payload ? (
        <>
          <p>
            <strong>{payload.summary.headline}</strong>
          </p>
          <p style={{ color: "#444" }}>{payload.summary.trust_note}</p>

          <TrustBadges badges={payload.trust_badges} />

          <h4>Outcome</h4>
          <ul>
            <li>
              <strong>Decision:</strong> {payload.decision}
            </li>
            <li>
              <strong>Visible outcome:</strong> {payload.visible_outcome}
            </li>
            {payload.summary.knowledge_character ? (
              <li>
                <strong>Knowledge character:</strong>{" "}
                {payload.summary.knowledge_character}
              </li>
            ) : null}
            {payload.summary.taxon ? (
              <li>
                <strong>Taxon:</strong> {payload.summary.taxon}
              </li>
            ) : null}
            {payload.summary.habitat_class ? (
              <li>
                <strong>Habitat:</strong> {payload.summary.habitat_class}
              </li>
            ) : null}
          </ul>

          <h4>References</h4>
          <ul>
            <li>
              <strong>Payload:</strong> {payload.payload_id}
            </li>
            <li>
              <strong>Claim:</strong> {payload.claim_ref}
            </li>
            <li>
              <strong>EvidenceBundle:</strong> {payload.evidence_bundle_ref}
            </li>
            <li>
              <strong>DecisionEnvelope:</strong> {payload.decision_ref}
            </li>
            <li>
              <strong>ReleaseManifest:</strong> {payload.release_ref}
            </li>
            <li>
              <strong>Spec hash:</strong> {payload.spec_hash}
            </li>
          </ul>

          <h4>Evidence refs</h4>
          <FieldList value={payload.evidence_refs} />

          <h4>Sources</h4>
          <ul>
            {payload.sources.map((source) => (
              <li key={source.source_ref}>
                <strong>{source.source_role}:</strong> {source.citation}
                <br />
                <code>{source.source_ref}</code>
              </li>
            ))}
          </ul>

          {payload.policy_flags?.length ? (
            <>
              <h4>Policy flags</h4>
              <FieldList value={payload.policy_flags} />
            </>
          ) : null}

          {payload.limitations?.length ? (
            <>
              <h4>Limitations</h4>
              <ul>
                {payload.limitations.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </>
          ) : null}

          {payload.redaction_receipt_refs?.length ? (
            <>
              <h4>Redaction receipts</h4>
              <FieldList value={payload.redaction_receipt_refs} />
            </>
          ) : null}

          <h4>Freshness</h4>
          <ul>
            <li>
              <strong>Generated:</strong> {payload.freshness.generated_at}
            </li>
            <li>
              <strong>Stale after:</strong> {payload.freshness.stale_after}
            </li>
          </ul>
        </>
      ) : null}

      {layerMetadata ? (
        <>
          <h4>Layer trust</h4>
          <ul>
            <li>
              <strong>Layer:</strong> {layerMetadata.layerId}
            </li>
            <li>
              <strong>Public safe:</strong> {String(layerMetadata.publicSafe)}
            </li>
            <li>
              <strong>EvidenceBundle:</strong>{" "}
              {layerMetadata.evidenceBundleRef}
            </li>
            <li>
              <strong>PromotionDecision:</strong>{" "}
              {layerMetadata.promotionDecisionRef}
            </li>
            <li>
              <strong>RunReceipt:</strong> {layerMetadata.runReceiptRef}
            </li>
          </ul>

          <h4>Allowed fields</h4>
          <FieldList value={layerMetadata.allowedFields} />
        </>
      ) : null}

      {featureProperties ? (
        <>
          <h4>Feature properties</h4>
          <pre
            style={{
              whiteSpace: "pre-wrap",
              background: "#f6f8fa",
              padding: 12,
              borderRadius: 8
            }}
          >
            {JSON.stringify(featureProperties, null, 2)}
          </pre>
        </>
      ) : null}
    </aside>
  );
}
