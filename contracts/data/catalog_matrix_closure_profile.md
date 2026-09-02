<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/catalog-matrix-closure-profile
title: CatalogMatrix STAC/DCAT/PROV Closure Profile
class: semantic-contract-profile
version: 0.1.0
status: proposed
truth_posture: cite-or-abstain
responsibility_root: contracts/
related:
  - contracts/data/catalog_matrix.md
  - contracts/common/spec_hash.md
  - schemas/contracts/v1/data/catalog_matrix_closure_profile.schema.json
  - fixtures/data/catalog_matrix/closure/
  - tools/validators/validate_catalog_matrix_closure.py
  - docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "Additive proposed profile; it does not replace or narrow the broader CatalogMatrix semantic contract."
  - "ADR-0022 remains proposed. This profile supplies reviewable implementation evidence without accepting the ADR or creating a promotion requirement."
  - "A validator PASS proves bounded local alignment only; it does not emit catalogs, resolve evidence, decide policy, approve review, release, publish, or authorize public use."
[/KFM_META_BLOCK_V2] -->

# CatalogMatrix STAC/DCAT/PROV Closure Profile

> **PROPOSED:** This additive profile makes one bounded Pass 18 requirement executable: STAC, DCAT, and PROV records for a release candidate must agree on artifact identity, byte digest, and release reference.

## Compatibility and authority boundary

The existing `contracts/data/catalog_matrix.md` remains the broader semantic contract. This profile applies only to objects declaring:

```json
{"profile": "STAC_DCAT_PROV_CLOSURE_V1"}
```

Objects without that discriminator are outside this profile and must not be denied by this validator. The profile does not accept ADR-0022, redefine all CatalogMatrix uses, establish a required promotion gate, or create release/publication authority.

| Responsibility | Owning surface |
|---|---|
| Broad CatalogMatrix meaning | `contracts/data/catalog_matrix.md` |
| Closure-profile meaning | `contracts/data/catalog_matrix_closure_profile.md` |
| Closure-profile machine shape | `schemas/contracts/v1/data/catalog_matrix_closure_profile.schema.json` |
| Local closure validation | `tools/validators/validate_catalog_matrix_closure.py` |
| Synthetic polarity evidence | `fixtures/data/catalog_matrix/closure/` and `tests/validators/` |
| Actual catalog records | governed STAC/DCAT/PROV lifecycle surfaces |
| Evidence, policy, review, proof, release | their distinct governing object families |

## Required alignment

Each profiled matrix binds one canonical tuple:

```text
artifact_id + digest + release_ref
```

The `stac`, `dcat`, and `prov` bindings must repeat that tuple exactly. Each binding keeps a distinct `record_ref`; the profile cross-checks standards-facing records without collapsing their native models.

## Required trust links

The record also carries sorted, unique `evidence_refs` and `source_refs`, plus references for policy decision, review, correction path, rollback, and deterministic `spec_hash`. These are references only. Local validation does not prove that they resolve, are current, or authorize exposure.

## Finite profile decision grammar

| Decision | Local rule |
|---|---|
| `READY` | Alignment passes and `reason_codes` is empty. |
| `HOLD` | Alignment passes and one or more reason codes explain the hold. |
| `DENY` | Alignment passes and one or more reason codes explain the denial. |

The decision is a profile-local candidate disposition. It is not a `PolicyDecision`, `PromotionDecision`, review approval, or release authorization.

## Validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Closed schema and bounded profile semantics pass. |
| `FAIL` | Readable input violates schema or closure semantics. |
| `ERROR` | Input cannot be safely evaluated. |

The no-network validator denies duplicate JSON keys, non-finite numbers, symlink and oversized inputs, lifecycle-private references, non-canonical reference arrays, cross-standard tuple drift, duplicate standard-record references, and invalid decision/reason combinations.

## Lifecycle posture

```text
PROCESSED artifact
  -> STAC + DCAT + PROV candidates
  -> proposed closure-profile validation
  -> evidence / policy / review / proof / promotion gates
  -> ReleaseManifest
  -> PUBLISHED governed products
```

Profile validation is only one candidate gate. It never creates a shortcut from catalog metadata to publication.

## Acceptance evidence

This proposed profile is reviewable when:

- the closed Draft 2020-12 schema meta-validates;
- exact positive, schema-negative, and semantic-negative fixtures replay deterministically;
- checksum, artifact-ID, and release-reference mismatches fail closed;
- socket creation is denied during focused tests;
- the generated authoring receipt binds every introduced byte;
- hosted exact-head validation reports its result on the draft pull request.

Human review and any ADR acceptance remain separate.

## Rollback

Revert the additive profile commit. Rollback removes the profile contract, schema, fixtures, validator, tests, workflow, and authoring receipt while leaving the existing broad CatalogMatrix contract, placeholder schema, generic validator stub, canonical data, catalog records, releases, and public products unchanged.
