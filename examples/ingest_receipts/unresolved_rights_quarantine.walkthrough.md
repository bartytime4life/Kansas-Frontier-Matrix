# Synthetic source head with unresolved rights

This static walkthrough shows a source-intake handoff that stops in `QUARANTINE` when rights and sensitivity review have not closed. All IDs and source-head values are invented. It is not an emitted IngestReceipt, admitted SourceDescriptor, source payload, proof, catalog entry, or release record.

```yaml
example: true
authority: non_authoritative_example
do_not_publish: true
maturity: STATIC_WALKTHROUGH
real_vs_synthetic: synthetic_only
expected_outcome: QUARANTINE
operational_home: data/receipts/ingest/ (emitted receipts only)
validation_boundary: JSON snippet parsing and relative-link checks; no intake or receipt execution
correction_trigger: source-admission, rights, sensitivity, or ingest-receipt contract change
```

## Toy intake observation

```json
{
  "example": true,
  "authority": "non_authoritative_example",
  "do_not_publish": true,
  "scenario_id": "kfm://example/ingest-receipts/unresolved-rights-001",
  "source_ref": "fixture://source/synthetic/head-001",
  "source_role": "synthetic",
  "source_head": {
    "etag": "synthetic-etag-001",
    "last_modified": "synthetic-time-001",
    "digest_ref": "fixture://digest/synthetic/head-001"
  },
  "admission_state": "UNVERIFIED",
  "rights_state": "UNRESOLVED",
  "sensitivity_state": "UNREVIEWED",
  "expected_outcome": "QUARANTINE"
}
```

This is a teaching scenario, not an instance of the [IngestReceipt schema](../../schemas/contracts/v1/source/ingest_receipt.schema.json). The [valid contract fixture](../../fixtures/contracts/v1/source/ingest_receipt/valid/valid_1.json) shows the receipt fields used by that schema; this walkthrough adds review states outside that object.

## Expected handoff

| Step | Toy result | Consequence |
|---|---|---|
| Observe source head | Synthetic values captured | Observation alone does not admit a source. |
| Check rights and sensitivity | `UNRESOLVED` and `UNREVIEWED` | Stop before RAW admission or public use. |
| Route candidate | `QUARANTINE` | Preserve a bounded review state; no claim of an emitted receipt. |
| Proof, catalog, release | `NOT_RUN` | None can be inferred from source-head capture. |

`QUARANTINE` is the illustrated intake disposition, not a public DecisionEnvelope outcome. The [ingest receipt contract](../../contracts/source/ingest_receipt.md) and [receipt home](../../data/receipts/ingest/README.md) own operational meaning. If their rules change, revise or retire this example and its inbound links; promotion into a fixture, test, or live intake flow needs separate review.
