# UI projection validators

This lane owns bounded validators for machine-shaped UI projections. It does not
own UI implementation, evidence truth, policy decisions, release records, or
public permission.

`validate_evidence_drawer_payload.py` validates the proposed public-safe
EvidenceDrawerPayload schema, finite outcome consistency, correction history,
and negative-history non-resolution over synthetic fixtures without network
access. A pass is validation evidence only.
