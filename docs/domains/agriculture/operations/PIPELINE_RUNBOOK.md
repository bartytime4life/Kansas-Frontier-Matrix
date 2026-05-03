# Agriculture Pipeline Runbook

This runbook covers a fixture-first pipeline flow for the agriculture lane.

## Lifecycle sequence

1. Register or update source descriptor.
2. Ingest RAW fixture/live payload with immutable receipt.
3. Normalize into WORK with source IDs, units, CRS, and time semantics preserved.
4. Validate with schema, role, rights, and policy checks.
5. Promote valid candidates to PROCESSED and emit catalog/provenance objects.
6. Evaluate publication gate and produce DecisionEnvelope.
7. Publish release manifest + rollback card for approved artifacts.

## Standard incident responses

- **Malformed source payload**: quarantine with reason code and do not publish.
- **Rights/sensitivity ambiguity**: force deny/abstain until steward review.
- **Catalog closure failure**: block publication and record obligation to repair references.
- **Regression in negative fixture**: rollback candidate release and reopen validation.
