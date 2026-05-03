# KFM Meta Block v2
- doc_id: kfm://doc/fauna/gbif-public-aggregates
- status: PROPOSED
- owners: fauna-platform
- tags: [kfm, fauna, gbif, public, aggregate, geoprivacy]

## Purpose
Define fixture-backed GBIF public-safe aggregate publication outputs from validated EvidenceBundles.

## Lifecycle placement
PROCESSED -> PUBLISHED candidate.

## Public-safe aggregate contract
See `schemas/fauna/gbif_public_aggregate.schema.json`.

## Geoprivacy transform rules
- Remove `decimalLatitude`/`decimalLongitude` from public outputs.
- Generalize geometry to `geometry_role=generalized_public_area`.
- Emit geoprivacy receipt per run.

## Suppression rules
- Suppress aggregates where `observation_count < 10`.

## CLI examples
```bash
python tools/publishers/fauna/kfm_gbif_public_aggregate.py \
  --input tests/fixtures/fauna/gbif/valid/evidencebundle.json \
  --aggregation-unit county \
  --suppression-threshold 10 \
  --output /tmp/gbif_public_aggregates.json \
  --receipt-output /tmp/gbif_geoprivacy_receipt.json
```

## Validation and policy gates
- Schema validation for aggregate + receipt.
- Validator fail-closed rules for rights/sensitivity/receipt/source refs.
- OPA policy denies exact coordinates and under-threshold aggregates.

## Limitations
Occurrence aggregates are observational signals and must not be treated as confirmed species presence without review posture.

## Promotion checklist
- EvidenceBundle exists and validates.
- Geoprivacy receipt emitted and referenced.
- Policy denies count is zero.

## Rollback/correction notes
Recompute and republish aggregate + receipt from source EvidenceBundle.

## NEEDS_VERIFICATION
- Shared schema home for receipt contracts may be centralized elsewhere.
- Whether aggregate artifacts require additional shared catalog linkage fields.
