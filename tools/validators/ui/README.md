# UI projection validators

This lane owns bounded validators for machine-shaped UI projections. It does not
own UI implementation, evidence truth, policy decisions, review authority,
release records, correction records, publication, or public permission.

- `validate_evidence_drawer_payload.py` validates the proposed public-safe
  EvidenceDrawerPayload schema, finite outcome consistency, correction history,
  and negative-history non-resolution over synthetic fixtures without network
  access.
- `validate_story_node.py` validates the proposed public-safe StoryNode schema
  and finite evidence/citation/rights/sensitivity/policy/review/release/
  correction/supersession inheritance rules over synthetic fixtures without
  network access.

A passing validator is bounded conformance evidence only.
