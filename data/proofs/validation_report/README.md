# `data/proofs/validation_report/`

Status: draft  
Policy label: public-review  
Owner: `<data steward>` · `<validation steward>` · `<proof steward>` · `<release steward>` — TODO

This directory is the parent KFM lane for **ValidationReport** proof support.

ValidationReport files should record validator outcomes in a stable, inspectable form. They should identify the validator, validator version, schema version, fixture set, run id, candidate reference, input and output digests, relevant evidence references, related receipts, review references, ProofPack references, release references, rollback references, finite outcome, and reasons.

## Authority boundary

A ValidationReport is support material. It is not a receipt, EvidenceBundle, ProofPack, policy decision, ReviewRecord, catalog record, ReleaseManifest, public layer, or published report.

Use stable references instead of duplicating source payloads. Keep release authority under `release/`. Keep published carriers under `data/published/`.

## Authored sublanes

| Lane | Purpose |
|---|---|
| [`atmosphere/`](./atmosphere/) | Atmosphere / Air validation-report support. |
| [`flora/`](./flora/) | Flora validation-report support. |

## Suggested child pattern

```text
data/proofs/validation_report/
├── README.md
├── <domain>/
│   ├── README.md
│   ├── candidates/
│   ├── failures/
│   ├── indexes/
│   ├── release/
│   └── retired/
└── cross_domain/
    └── <scope>/
```

## Minimum fields, proposed

- `validation_report_id`
- `domain`
- `validator_family`
- `validator_name`
- `validator_version`
- `schema_version`
- `fixture_set_ref`
- `run_id`
- `candidate_ref`
- `input_digest`
- `output_digest`
- `evidence_bundle_refs`
- `receipt_refs`
- `review_record_refs`
- `proof_pack_refs`
- `release_refs`
- `rollback_refs`
- `finite_outcome`
- `reasons`
- `created_at`
- `created_by`

## Definition of done

This lane is operationally useful when a semantic contract, JSON schema, fixtures, validator tooling, and CI checks exist and active domain sublanes have README files before live ValidationReport instances land there.
