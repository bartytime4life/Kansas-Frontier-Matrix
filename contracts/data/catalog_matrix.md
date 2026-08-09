<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/catalog-matrix
title: CatalogMatrix Contract
class: semantic-contract
version: 0.3.0
status: proposed-validation-profile
truth_posture: cite-or-abstain
responsibility_root: contracts/
related:
  - contracts/data/README.md
  - contracts/common/spec_hash.md
  - schemas/contracts/v1/data/catalog_matrix.schema.json
  - fixtures/data/catalog_matrix/
  - tools/validators/validate_catalog_matrix.py
  - docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "v0.3 replaces the greenfield placeholder profile with a closed, fixture-backed STAC/DCAT/PROV alignment contract."
  - "The validator proves bounded local closure only; it does not emit catalogs, resolve evidence, decide policy, approve review, release, publish, or authorize public use."
[/KFM_META_BLOCK_V2] -->

# CatalogMatrix Contract

> **PROPOSED validation profile:** `CatalogMatrix` records whether the STAC, DCAT, and PROV catalog representations for one release candidate agree on artifact identity, digest, and release reference while preserving evidence, source, policy, review, correction, and rollback links.

## Why this object exists

Catalog standards have different native models. KFM still needs one deterministic closure check before a release candidate can rely on them. `CatalogMatrix` is that cross-standard alignment record. It is an inspectability aid, not a catalog standard, source of truth, proof pack, policy decision, release manifest, or published product.

## Authority boundary

| Responsibility | Owning surface |
|---|---|
| Object meaning | `contracts/data/catalog_matrix.md` |
| Machine shape | `schemas/contracts/v1/data/catalog_matrix.schema.json` |
| Local closure validation | `tools/validators/validate_catalog_matrix.py` |
| Synthetic polarity evidence | `fixtures/data/catalog_matrix/` and `tests/validators/` |
| Actual STAC/DCAT/PROV records | governed catalog lifecycle surfaces |
| Evidence closure | `EvidenceBundle` and proof surfaces |
| Policy and review | their own decision/record families |
| Release, correction, rollback | `release/` and governed lifecycle objects |

## Required alignment

Each matrix binds one canonical `artifact` tuple:

```text
artifact_id + digest + release_ref
```

The `stac`, `dcat`, and `prov` records must repeat that tuple exactly. A mismatch is a validation failure, not a warning. Each standard record retains its own `record_ref`; KFM does not collapse the standards into one format.

## Required trust links

The profile also requires sorted, unique:

- `evidence_refs`;
- `source_refs`;
- a `policy_decision_ref`;
- a `review_ref`;
- a `correction_path_ref`;
- a `rollback_ref`;
- a deterministic `spec_hash`.

These are references only. A local PASS does not prove that the referenced objects exist, are current, are authorized, or support public release.

## Finite decision grammar

| Decision | Local rule |
|---|---|
| `READY` | Alignment passes and `reason_codes` is empty. |
| `HOLD` | Alignment still passes, and at least one reason code explains the hold. |
| `DENY` | Alignment still passes, and at least one reason code explains the denial. |

The matrix records a candidate disposition; it does not replace the governing policy, review, promotion, or release decision.

## Validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Closed schema and bounded local alignment rules pass. |
| `FAIL` | The record is readable but violates schema or semantic closure. |
| `ERROR` | The record cannot be safely evaluated. |

The no-network validator denies duplicate JSON keys, non-finite numbers, symlink inputs, oversized inputs, lifecycle-private references, non-canonical reference arrays, cross-standard tuple drift, and invalid decision/reason combinations.

## Lifecycle posture

```text
PROCESSED artifact
  -> STAC + DCAT + PROV candidates
  -> CatalogMatrix local alignment
  -> evidence / policy / review / proof / promotion gates
  -> ReleaseManifest
  -> PUBLISHED governed products
```

CatalogMatrix validation is only one gate. It must never become a shortcut from catalog metadata to publication.

## Rollback

Revert the feature-branch commit to restore the prior placeholder schema and validator stub together with removal of the new fixtures, tests, workflow, and authoring receipt. No canonical data, catalog record, release, or public product is mutated by this slice.
