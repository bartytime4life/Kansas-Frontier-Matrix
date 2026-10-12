# Soil EvidenceDrawerPayload projection

Status: PROPOSED  
Authority: domain projection only; not independent evidence, policy, review, release, correction, or publication authority.

The Soil lane reuses the shared Explorer public-safe `EvidenceDrawerPayload` semantics defined by `contracts/ui/evidence_drawer_payload.md` and shaped by `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json`.

This Soil contract exists only to make the domain relationship explicit. Soil does not define a second payload shape, parser, renderer, EvidenceBundle format, or release decision.

## Invariants

- Finite outcomes remain `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`.
- `ANSWER` must remain downstream of governed evidence, policy, review, release, freshness, and correction state supplied by the shared projection.
- `DENY` and `ERROR` must not expose evidence refs, citations, correction history, protected source text, or sensitive detail through the Soil surface.
- Evidence refs are pointers; this projection does not resolve or authenticate an `EvidenceBundle`.
- The Soil domain component must delegate to the shared Explorer Evidence Drawer implementation rather than create a parallel renderer.

## Trust boundary

Schema validity or successful rendering does not establish evidence truth, rights clearance, sensitivity clearance, source admission, review completion, lifecycle promotion, release, deployment, publication, or public-use authority.
