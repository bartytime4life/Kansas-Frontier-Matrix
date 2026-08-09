<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/stac-attestation-hook
title: STAC Attestation Hook Projection Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
updated: 2026-08-08
owning_root: contracts/
policy_label: public; catalog; stac; evidence; no-network; no-publication-authority
related:
  - ../../schemas/contracts/v1/data/stac_attestation_hook.schema.json
  - ../../fixtures/data/stac_attestation_hook/cases.json
  - ../../tools/validators/data/validate_stac_attestation_hook.py
  - ../../tests/validators/test_validate_stac_attestation_hook.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# STAC Attestation Hook Projection

This closed, no-network profile implements the smallest testable form of Pass 7 card `KFM-P7-PROG-0001`: a STAC projection carries one explicit `rel: attestation` link to the `EvidenceBundle` whose declared certification hash matches the STAC Item `spec_hash`.

## Boundary

The profile is `PROPOSED_INACTIVE` and `FIXTURE_ONLY`. It does not validate complete STAC Items, dereference evidence, verify signatures, execute policy, authenticate review, mutate catalog state, register a layer, promote, release, deploy, publish, or authorize public use.

## Rules

- `CANDIDATE`, `RELEASED`, `WITHDRAWN`, `CORRECTED`, and `SUPERSEDED` require exactly one `attestation` link.
- `UNRELEASED` may omit it.
- `prov` is not an attestation alias.
- The hook target equals `evidence_bundle_ref`.
- The hook certification hash equals `item_spec_hash`.
- The media type is `application/vnd.kfm.evidence-bundle+json`.
- The bundle digest is non-placeholder.
- Authority-bearing `latest` references are denied.
- Links are canonical and unique.
- `spec_hash` and `projection_id` reproduce deterministically.
- Every authority flag remains false.

## Directory Rules basis

Meaning stays under `contracts/data/`; shape under `schemas/contracts/v1/data/`; synthetic cases under `fixtures/data/`; executable validation under `tools/validators/data/`; tests under `tests/validators/`; CI under `.github/workflows/`; authoring accountability under `data/receipts/generated/`. No new root or parallel catalog/evidence authority is created.

## Validation

```bash
python -m unittest tests.validators.test_validate_stac_attestation_hook --verbose
python tools/validators/data/validate_stac_attestation_hook.py --fixtures
```

## Rollback

Revert this additive packet. It performs no lifecycle, catalog, release, or runtime write, so no data migration, cache invalidation, source deactivation, withdrawal, or public correction is required.
