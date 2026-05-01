# GBIF Catalog + Triplet + Read Model

## KFM Meta Block v2
- Domain: fauna
- Layer: PROCESSED/PUBLISHED_CANDIDATE -> CATALOG -> TRIPLET -> RUNTIME_READ_MODEL
- Status: Draft
- NEEDS_VERIFICATION: schema-home and naming finalized against broader KFM canon.

## Purpose
Register public-safe GBIF aggregates and geoprivacy receipts into catalog/triplet artifacts and answer only cited aggregate questions or abstain.

## Contracts
- Catalog contract: `schemas/catalog/fauna/gbif_catalog_entry.schema.json`
- Triplet contract: `schemas/triplets/fauna/gbif_occurrence_aggregate_claim.schema.json`
- Read model contract: `schemas/readmodels/fauna/gbif_occurrence_answer.schema.json`

## Rules
- Preserve source_evidence_bundle_id, download_key, query_predicate_hash, geoprivacy_receipt_ref, kfm:spec_hash, rights/sensitivity posture, limitations.
- Forbidden language: confirmed present, verified present, known population, exact location, site-level record.
- Required posture phrase in claim text: GBIF-reported public occurrence aggregate.
- Abstain on exact coordinate request or confirmed-presence request.

## CLI
See tool headers:
- `tools/catalog/fauna/kfm_gbif_catalog_register.py`
- `tools/triplets/fauna/kfm_gbif_triplet_emit.py`
- `tools/readmodels/fauna/kfm_gbif_occurrence_readmodel.py`

## Validation and Policy
- Validator: `tools/validators/fauna/gbif_catalog_triplet_validator.py`
- Rego gate: `policy/fauna/gbif_catalog_triplet.rego`

## Limitations
- Aggregate-only posture; not conservation-status confirmation.
- Generalized geography only; no exact coordinates.

## Promotion checklist
- Fixtures pass
- Validator pass
- Policy pass

## Rollback/correction
- Re-emit catalog/triplet/readmodel with corrected evidence refs and spec hashes.
