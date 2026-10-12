<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/catalog-matrix-claim-closure-profile
title: CatalogMatrix ClaimEnvelope Closure Profile
class: semantic-contract-profile
version: 0.1.0
status: proposed
truth_posture: cite-or-abstain
responsibility_root: contracts/
related:
  - contracts/evidence/claim_envelope.md
  - contracts/data/catalog_matrix.md
  - contracts/data/catalog_matrix_closure_profile.md
  - schemas/contracts/v1/data/catalog_matrix_claim_closure_profile.schema.json
  - fixtures/data/catalog_matrix/claim_closure/
  - tools/validators/validate_catalog_matrix_claim_closure.py
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "Additive proposed integration profile; ClaimEnvelope and CatalogMatrix retain their existing owners and authority boundaries."
  - "Catalog projection may mirror or narrow claim posture, but it must never strengthen evidence, policy, review, release, or publication status."
  - "A PASS proves deterministic local consistency only; it does not resolve evidence, decide policy, authenticate review, release, publish, or authorize public use."
[/KFM_META_BLOCK_V2] -->

# CatalogMatrix ClaimEnvelope Closure Profile

> **PROPOSED:** `CLAIM_ENVELOPE_CATALOG_MATRIX_CLOSURE_V1` composes one already-valid `ClaimEnvelope` with one already-valid additive CatalogMatrix STAC/DCAT/PROV closure record and rejects a catalog projection that claims more authority than the claim carries.

## Compatibility and authority boundary

This profile is additive. It applies only to objects declaring:

```json
{"profile": "CLAIM_ENVELOPE_CATALOG_MATRIX_CLOSURE_V1"}
```

It does not modify the broader CatalogMatrix contract, the STAC/DCAT/PROV closure profile, or the proposed ClaimEnvelope contract. The embedded objects remain governed by their own semantic contracts, machine schemas, validators, policy/review systems, and release families.

| Responsibility | Owning surface |
|---|---|
| Claim meaning and posture | `contracts/evidence/claim_envelope.md` |
| STAC/DCAT/PROV tuple closure | `contracts/data/catalog_matrix_closure_profile.md` |
| Additive non-overstatement relation | this profile |
| Machine shape | `schemas/contracts/v1/data/catalog_matrix_claim_closure_profile.schema.json` |
| Deterministic local validation | `tools/validators/validate_catalog_matrix_claim_closure.py` |
| Evidence resolution | `EvidenceBundle` and governed resolvers |
| Policy, review, release, publication | their distinct authority-bearing object families |

Neither embedding nor validator success upgrades either object. A catalog record remains a derived discovery carrier; a ClaimEnvelope remains a bounded claim carrier. Neither is evidence, a PolicyDecision, review approval, a ReleaseManifest, a PromotionDecision, or publication authority.

## Non-overstatement rules

The catalog side may narrow or mirror the claim side, never expand it:

1. Catalog `evidence_refs` and `source_refs` must be subsets of the ClaimEnvelope arrays.
2. Catalog `artifact.release_ref`, `correction_path_ref`, and `rollback_ref` must exactly match the ClaimEnvelope references.
3. Catalog `decision: READY` is locally consistent only when the claim is `SUPPORTED`, policy is `ALLOW`, review is `APPROVED`, and release state is `CANDIDATE` or `PUBLISHED`.
4. A claim denied, rejected, withdrawn, or superseded must project as catalog `DENY`; `HOLD` cannot soften a terminal negative posture.
5. `catalog_publication_state: PUBLISHED` is locally consistent only when the ClaimEnvelope says `PUBLISHED` and the catalog closure decision is `READY`.
6. `NOT_PUBLISHED` is always allowed because a catalog may be more conservative than an otherwise eligible claim.

These are consistency checks over already-shaped objects. They do not dereference identifiers or prove that any referenced evidence, policy decision, review, release, correction, or rollback object exists or is current.

## Validation order

```text
wrapper schema
  -> ClaimEnvelope validator
  -> CatalogMatrix closure validator
  -> additive non-overstatement checks
  -> PASS / FAIL / ERROR
```

Lower-level failures are preserved with prefixed reason codes. The integration validator never silently coerces a claim or catalog decision into a stronger state.

## Synthetic fixture contract

The no-network fixture corpus proves:

- a published, approved, supported claim may align with a locally READY catalog and a `PUBLISHED` projection;
- a restricted candidate may align with `HOLD` and `NOT_PUBLISHED`;
- a denied claim may align only with catalog `DENY`;
- extra evidence/source references, READY posture inflation, publication inflation, and release/correction/rollback drift fail closed;
- schema-negative and semantic-negative cases remain distinguishable and replay deterministically.

All examples are synthetic. A positive fixture is validation evidence only, not proof of a real Kansas claim, source, review, release, or publication.

## Lifecycle posture

```text
EvidenceRef -> EvidenceBundle -> policy/review -> ClaimEnvelope
PROCESSED artifact -> STAC/DCAT/PROV candidate closure
                                                   -> proposed non-overstatement validation
                          -> separate proof/promotion/release gates
                          -> PUBLISHED only through governed release
```

## Rollback

Revert the additive feature commit or close its draft pull request. Rollback removes only this profile contract, schema, synthetic fixtures, validator, focused tests, workflow, and generated authoring receipt. It does not modify the two base contracts, canonical data, catalog records, release objects, repository settings, or public products.
