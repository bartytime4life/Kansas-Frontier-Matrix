# ADR 0004: Meta Block V2

## Status

Accepted

## Context

Standards and governance documents need machine-readable metadata so promotion policy can identify owners, versions, sensitivity, evidence references, and review obligations.

## Decision

All standards documents that participate in promotion must include Meta Block V2 as YAML front matter or an equivalent top-level metadata block:

```yaml
meta:
  schema: meta-block-v2
  standard_id: STD-EXAMPLE-001
  title: Example Standard
  version: 1.0.0
  status: active
  owner: team-or-person
  steward: governance-owner
  effective_date: 2026-05-05
  review_due_date: 2026-11-05
  sensitivity: internal
  rights:
    license_id: internal-use
    allowed_uses: [promotion, audit]
    prohibited_uses: []
  obligations:
    redaction_required: false
  evidence_bundle_ref: artifacts/EvidenceBundle.json
  decision_log_ref: artifacts/decision_log.json
  spec_hash: "<64-char-sha256>"
  supersedes: null
  references: []
  changelog:
    - version: 1.0.0
      date: 2026-05-05
      summary: Initial version
```

Required fields are `schema`, `standard_id`, `title`, `version`, `status`, `owner`, `steward`, `effective_date`, `review_due_date`, `sensitivity`, `rights`, `obligations`, `evidence_bundle_ref`, `decision_log_ref`, and `spec_hash`.

## Consequences

Governance metadata is no longer prose-only. CI and reviewers can enforce document ownership, freshness, sensitivity handling, and evidence linkage.

## Validation / Enforcement

Gate C checks rights and sensitivity. Gate E checks decision ownership. Gate G checks release linkage. Add repository-specific linters for Meta Block V2 when standards documents become first-class inputs.

## Rollback

Documents may temporarily accept Meta Block V1 only through an explicit migration exception recorded in `decision_log.json`. New documents must use V2.
