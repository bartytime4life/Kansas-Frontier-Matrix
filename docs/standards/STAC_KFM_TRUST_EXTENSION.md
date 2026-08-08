<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standards/stac-kfm-trust-extension
title: KFM STAC Trust Extension v1
type: standard-profile
version: v0.2.0
status: draft; fixture-first; namespace-decision-pending; non-release
owners:
  - OWNER_TBD - Catalog steward
  - OWNER_TBD - Standards steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Release steward
  - OWNER_TBD - Schema steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public; stac; catalog; trust; evidence-linked; non-authoritative
owning_root: docs/
responsibility: Define the proposed KFM-specific trust fields carried by STAC catalog projections without turning catalog records into evidence, proof, release approval, or publication authority.
truth_posture: CONFIRMED repository placement, prior permissive scaffold, and corrective implementation packet; PROPOSED field realization and namespace; NEEDS VERIFICATION external STAC conformance and human review
related:
  - ./stac.md
  - ./STAC_KFM_PROFILE.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../schemas/contracts/v1/stac/kfm-profile-v1.schema.json
  - ../../tools/validators/stac/validate_kfm_profile_v1.py
  - ../../fixtures/contracts/v1/stac/kfm-profile-v1/
  - ../../tests/validators/test_validate_kfm_stac_profile.py
  - ../../.github/workflows/stac-kfm-trust-profile.yml
tags: [kfm, stac, catalog, evidence, receipt, proof, source-role, release, publication]
notes:
  - "v0.2.0 replaces the v0.1 documentation-only state with the dependency-closed schema, validator, fixtures, tests, workflow, and byte-bound authoring receipt."
  - "The initial merged v0.1 packet carried this document and a placeholder generated receipt but not the claimed executable companions; the corrective packet records that gap rather than rewriting history."
  - "No external namespace, live source, catalog service, release, deployment, or publication authority is created."
[/KFM_META_BLOCK_V2] -->

# KFM STAC Trust Extension v1

> A STAC record is a discovery projection. It may point to receipts, proofs, evidence, and release records, but it is not any of those objects and cannot authorize publication.

## Status and correction record

| Field | Value |
|---|---|
| Profile identifier | `kfm-stac-profile-v1` |
| Profile URI used by fixtures | `kfm://profile/stac/kfm-profile-v1` |
| Namespace used by this draft | `kfm:` |
| Namespace authority | **PROPOSED / NEEDS VERIFICATION** |
| Machine shape | `schemas/contracts/v1/stac/kfm-profile-v1.schema.json` |
| Validator | `tools/validators/stac/validate_kfm_profile_v1.py` |
| Fixture profile | `fixtures/contracts/v1/stac/kfm-profile-v1/fixture_manifest.json` |
| Test module | `tests/validators/test_validate_kfm_stac_profile.py` |
| Workflow | `.github/workflows/stac-kfm-trust-profile.yml` |
| Validation posture | deterministic, fixture-first, no-network |
| Release effect | none |

The first merged edition of this document described a complete executable packet, but that merge contained only this document and a placeholder generated receipt. The corrective packet makes the dependency set real: it replaces the permissive schema scaffold, adds the validator and exact fixtures, runs focused tests, adds the workflow, and replaces the placeholder receipt with final artifact hashes. This is an append-only correction; the earlier merge remains visible in Git history.

The existing standards corpus identifies `kfm:` versus `ks-kfm:` as an unresolved ADR-class choice. This draft uses `kfm:` consistently so fixtures and validators can be reviewed, but it does not settle that decision or create a stable external namespace commitment.

## Responsibility split

| Responsibility | Owning surface |
|---|---|
| Human-facing profile meaning | this standard and the existing STAC standards documents |
| Machine shape | `schemas/contracts/v1/stac/kfm-profile-v1.schema.json` |
| Deterministic checking | `tools/validators/stac/validate_kfm_profile_v1.py` |
| Synthetic examples | `fixtures/contracts/v1/stac/kfm-profile-v1/` |
| Enforceability | `tests/validators/test_validate_kfm_stac_profile.py` and the dedicated workflow |
| Evidence and proof | their own evidence/proof contracts and stores |
| Release and publication decisions | release and policy roots |
| Authoring provenance | `data/receipts/generated/` |

Accepted Directory Rules place standards under `docs/`, machine shape under `schemas/`, executable checks under `tools/validators/`, fixtures under `fixtures/`, tests under `tests/`, workflow integration under `.github/workflows/`, and authoring provenance under `data/receipts/`. No new root or parallel catalog authority is created.

## Required KFM trust fields

The draft profile adds the following namespaced properties to a bounded STAC Item projection:

| Property | Meaning |
|---|---|
| `kfm:profile_version` | Exact draft-profile version carried by the projection. |
| `kfm:spec_hash` | RFC 8785 JCS plus SHA-256 digest of the full Item with only this field omitted. |
| `kfm:source_role` | Canonical seven-class source role. |
| `kfm:trust_class` | Finite summary of which upstream references are present. |
| `kfm:run_receipt_ref` | Receipt reference or `null`; never proof by itself. |
| `kfm:proof_ref` | Proof reference or `null`; never release approval by itself. |
| `kfm:release_ref` | Release record reference or `null`; the reference does not execute release. |
| `kfm:catalog_state` | `CANDIDATE` or `CATALOGED`. |
| `kfm:release_state` | `NOT_RELEASED` or `RELEASE_LINKED`. |
| `kfm:publication_state` | `NOT_PUBLISHED` or `PUBLICATION_LINKED`. |
| `kfm:reason_codes` | Unique, lexicographically sorted, public-safe reason codes. |
| `kfm:authority` | Required all-false source, evidence, policy, review, release, and publication authority flags. |

Ordinary STAC properties and third-party extension properties remain extensible. Undeclared `kfm:` properties are rejected so the draft namespace cannot silently acquire new authority-bearing fields.

## Finite trust classes

| Trust class | Required linkage | Prohibited inference |
|---|---|---|
| `UNRESOLVED` | no upstream reference | unresolved does not mean failed or false |
| `CATALOG_ONLY` | catalog identity only | cataloged does not mean receipted, proved, released, or published |
| `RECEIPT_BOUND` | `kfm:run_receipt_ref` | a receipt does not prove the claim or approve release |
| `PROOF_BOUND` | receipt and proof references | proof does not approve release or publication |
| `RELEASE_LINKED` | receipt, proof, and release references | a catalog projection does not execute the linked release |

## Invariants

1. `receipt != proof != catalog != release != publication`.
2. Source role uses `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`.
3. `PROOF_BOUND` requires distinct receipt and proof references.
4. `RELEASE_LINKED` requires distinct receipt, proof, and release references plus `kfm:release_state: RELEASE_LINKED`.
5. `PUBLICATION_LINKED` requires a release reference and release-linked state; the projection still carries no publication authority.
6. Every authority flag is `false`.
7. `stac_extensions`, `kfm:reason_codes`, and KFM trust links are unique and canonical.
8. Every non-null KFM reference has exactly one matching `kfm:receipt`, `kfm:proof`, or `kfm:release` link.
9. `kfm:spec_hash` excludes only itself from the identity subject.
10. Validator output contains stable reason codes and JSON pointers, never untrusted field values.

## Fixture profile

The fixture manifest binds three valid synthetic projections and six semantic-negative projections.

| Fixture family | Coverage |
|---|---|
| Valid receipt-bound candidate | Receipt reference remains separate from proof and release. |
| Valid proof-bound catalog item | Receipt and proof are distinct; no release is inferred. |
| Valid release-linked item | Receipt, proof, and release are distinct; publication remains `NOT_PUBLISHED`. |
| Receipt used as proof | Rejected with `REFERENCE_ROLE_COLLAPSE`. |
| Proof without receipt | Rejected with `TRUST_CLASS_DEPENDENCY_MISMATCH`. |
| Release without proof | Rejected with `TRUST_CLASS_DEPENDENCY_MISMATCH`. |
| Publication without release | Rejected with `PUBLICATION_STATE_INCONSISTENT`. |
| Unsorted reason codes | Rejected with `REASON_CODES_NOT_CANONICAL`. |
| Identity drift | Rejected with `SPEC_HASH_MISMATCH`. |

All fixtures are synthetic and contain no live-source record, protected location, secret, or public release.

## Validation boundary

The fixture-first validator checks:

- Draft 2020-12 schema shape;
- the declared profile URI and version;
- deterministic RFC 8785 JCS plus SHA-256 identity;
- canonical source-role and trust-class vocabularies;
- distinct receipt/proof/release roles;
- trust-class dependency closure;
- catalog, release, and publication state consistency;
- canonical reason-code and KFM-link arrays;
- matching KFM reference links; and
- all-false authority flags.

A validator `PASS` does not establish complete STAC core or extension conformance, source admission, EvidenceBundle resolution, proof authenticity, policy approval, review approval, release validity, publication, deployment, or public safety. External STAC conformance and namespace ratification remain **NEEDS VERIFICATION**.

## Commands

```bash
python -m unittest tests/validators/test_validate_kfm_stac_profile.py -v
python tools/validators/stac/validate_kfm_profile_v1.py --fixtures
python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-pass3-catalog-trust-extension-20260808.json \
  --repo-root .
```

These commands are no-network and fixture-only. The dedicated workflow installs the repository-declared test dependencies and runs the same bounded checks.

## Rollback

Before merge, close the draft corrective pull request and delete its feature branch.

After an authorized merge:

1. revert the corrective packet;
2. restore the prior permissive schema blob `f46e676952af40775506088727ccc68f0bfe5b3e`;
3. restore this document to its prior v0.1.0 bytes only if the executable companions are also removed; and
4. retain the correction history and generated-receipt lineage.

No catalog service, live source, lifecycle record, release, deployment, cache, route, or public artifact requires rollback.
