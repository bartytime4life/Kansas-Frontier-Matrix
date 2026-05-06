import type { EcologyEvidenceDrawerEvidence } from "./evidenceBundle";
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
  evidence?: EcologyEvidenceDrawerEvidence;
  evidenceStatus?: string;
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

function EmptyNote({ children }: { children: string }) {
  return <p style={{ color: "#666", fontStyle: "italic" }}>{children}</p>;
}

export default function EvidenceDrawer({
  payload,
  open = true,
  onClose,
  featureProperties,
  layerMetadata,
  evidence,
  evidenceStatus
}: EvidenceDrawerProps) {
  if (!open) return null;

  return (
    <aside
      style={{
        borderLeft: "1px solid #ddd",
        padding: 12,
        width: 380,
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

      <h4>Resolved EvidenceBundle</h4>

      {evidenceStatus ? (
        <p style={{ color: "#8a5a00" }}>{evidenceStatus}</p>
      ) : null}

      {evidence ? (
        <>
          <ul>
            <li>
              <strong>Bundle:</strong> {evidence.bundle_id}
            </li>
            <li>
              <strong>Resolved:</strong> {String(evidence.resolved)}
            </li>
            <li>
              <strong>Resolution:</strong> {evidence.resolution_state}
            </li>
            <li>
              <strong>Visibility:</strong> {evidence.visibility}
            </li>
            <li>
              <strong>Policy:</strong> {evidence.policy_label}
            </li>
            <li>
              <strong>Rights:</strong> {evidence.rights_status}
            </li>
            <li>
              <strong>Sensitivity:</strong> {evidence.sensitivity}
            </li>
            <li>
              <strong>Spec hash:</strong> {evidence.spec_hash}
            </li>
          </ul>

          <h4>Source refs</h4>
          {evidence.source_refs.length ? (
            <FieldList value={evidence.source_refs} />
          ) : (
            <EmptyNote>No source refs in bundle.</EmptyNote>
          )}

          <h4>Dataset refs</h4>
          {evidence.dataset_refs.length ? (
            <FieldList value={evidence.dataset_refs} />
          ) : (
            <EmptyNote>No dataset refs in bundle.</EmptyNote>
          )}

          <h4>Evidence refs</h4>
          {evidence.evidence_refs.length ? (
            <FieldList value={evidence.evidence_refs} />
          ) : (
            <EmptyNote>No evidence refs in bundle.</EmptyNote>
          )}

          <h4>Object refs</h4>
          {evidence.object_refs.length ? (
            <FieldList value={evidence.object_refs} />
          ) : (
            <EmptyNote>No object refs in bundle.</EmptyNote>
          )}

          {evidence.catalog_refs.length ? (
            <>
              <h4>Catalog refs</h4>
              <FieldList value={evidence.catalog_refs} />
            </>
          ) : null}

          {evidence.release_refs.length ? (
            <>
              <h4>Release refs</h4>
              <FieldList value={evidence.release_refs} />
            </>
          ) : null}

          {evidence.limitations.length ? (
            <>
              <h4>Evidence limitations</h4>
              <ul>
                {evidence.limitations.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </>
          ) : null}

          {evidence.warnings.length ? (
            <>
              <h4>Evidence warnings</h4>
              <ul>
                {evidence.warnings.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </>
          ) : null}

          {evidence.notes.length ? (
            <>
              <h4>Evidence notes</h4>
              <ul>
                {evidence.notes.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </>
          ) : null}

          {evidence.artifacts.length ? (
            <>
              <h4>Artifacts</h4>
              <ul>
                {evidence.artifacts.map((artifact, index) => (
                  <li key={`${artifact.role ?? "artifact"}-${index}`}>
                    <strong>{artifact.role ?? "artifact"}:</strong>{" "}
                    {artifact.uri ?? "UNKNOWN"}
                    {artifact.digest ? (
                      <>
                        <br />
                        <code>{artifact.digest}</code>
                      </>
                    ) : null}
                  </li>
                ))}
              </ul>
            </>
          ) : null}
        </>
      ) : !evidenceStatus ? (
        <EmptyNote>Click a governed ecology feature to resolve evidence.</EmptyNote>
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
