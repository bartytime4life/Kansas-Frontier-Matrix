# Settlements & Infrastructure Pipeline

Fixture-first lifecycle for governed promotion.

## Lifecycle

1. Register source descriptor.
2. Ingest RAW fixture/live payload with immutable receipt.
3. Normalize to WORK while preserving source IDs, time semantics, and CRS.
4. Validate schema, source-role, policy, and precision gates.
5. Route failed candidates to QUARANTINE with reason codes.
6. Promote valid artifacts to PROCESSED and emit catalog/provenance objects.
7. Evaluate promotion gate and emit DecisionEnvelope.
8. Publish approved release artifacts with ReleaseManifest + rollback reference.

## Incident responses

- **Malformed legal/status event**: quarantine and require source correction.
- **Sensitive exact geometry**: deny publication or force generalized derivative.
- **Missing EvidenceBundle links**: fail publication gate.
- **Regression in negative fixtures**: rollback candidate release and reopen validation.
