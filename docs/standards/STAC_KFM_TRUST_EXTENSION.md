<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standards/stac-kfm-trust-extension
title: KFM STAC Trust Extension v1
type: standard; catalog-profile; trust-projection
version: v0.1.0
status: proposed; fixture-first; namespace-decision-pending; non-release
owners: OWNER_TBD — Catalog steward · Standards steward · Evidence steward · Release steward · Schema steward
created: 2026-08-08
updated: 2026-08-08
policy_label: public; stac; catalog; trust; evidence-linked; non-authoritative
owning_root: docs/
responsibility: Define the proposed KFM-specific trust fields carried by STAC catalog projections without turning catalog records into evidence, proof, release approval, or publication authority.
truth_posture: CONFIRMED repository placement and existing profile scaffold; PROPOSED field realization and namespace; NEEDS VERIFICATION external STAC conformance and human review
related:
  - ./stac.md
  - ./STAC_KFM_PROFILE.md
  - ../../schemas/contracts/v1/stac/kfm-profile-v1.schema.json
  - ../../tools/validators/stac/validate_kfm_profile_v1.py
  - ../../fixtures/contracts/v1/stac/kfm-profile-v1/
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, stac, catalog, evidence, receipt, proof, source-role, release, publication]
[/KFM_META_BLOCK_V2] -->

# KFM STAC Trust Extension v1

> A STAC record is a discovery projection. It may point to receipts, proofs, evidence, and release records, but it is not any of those objects and cannot authorize publication.

## Status

| Field | Value |
|---|---|
| Profile identifier | `kfm-stac-profile-v1` |
| Namespace used by this draft | `kfm:` |
| Namespace authority | **PROPOSED / NEEDS VERIFICATION** |
| Machine shape | `schemas/contracts/v1/stac/kfm-profile-v1.schema.json` |
| Validation posture | deterministic, fixture-first, no-network |
| Release effect | none |

The existing standards corpus identifies `kfm:` versus `ks-kfm:` as an unresolved ADR-class choice. This draft uses `kfm:` consistently so fixtures and validators can be reviewed, but it does not settle that decision or create a stable external namespace commitment.

## Responsibility split

| Responsibility | Owning surface |
|---|---|
| Human-facing profile meaning | this standard and the existing STAC standards documents |
| Machine shape | `schemas/contracts/v1/stac/kfm-profile-v1.schema.json` |
| Deterministic checking | `tools/validators/stac/validate_kfm_profile_v1.py` |
| Synthetic examples | `fixtures/contracts/v1/stac/kfm-profile-v1/` |
| Evidence and proof | their own evidence/proof contracts and stores |
| Release and publication decisions | release and policy roots |

Directory Rules place standards under `docs/`, machine shape under `schemas/`, executable checks under `tools/validators/`, fixtures under `fixtures/`, tests under `tests/`, and provenance receipts under `data/receipts/`. No new root or parallel catalog authority is created.

## Required KFM trust fields

The draft profile adds the following namespaced properties to a bounded STAC Item projection:

| Property | Meaning |
|---|---|
| `kfm:profile_version` | Profile version carried by the projection. |
| `kfm:spec_hash` | RFC 8785 JCS plus SHA-256 digest of the Item with this field omitted. |
| `kfm:source_role` | Canonical seven-class source role. |
| `kfm:trust_class` | Finite summary of which upstream references are present. |
| `kfm:run_receipt_ref` | Receipt reference or `null`; never proof by itself. |
| `kfm:proof_ref` | Proof reference or `null`; never release approval by itself. |
| `kfm:release_ref` | Release record reference or `null`; the reference does not execute release. |
| `kfm:catalog_state` | `CANDIDATE` or `CATALOGED`. |
| `kfm:release_state` | `NOT_RELEASED` or `RELEASE_LINKED`. |
| `kfm:publication_state` | `NOT_PUBLISHED` or `PUBLICATION_LINKED`. |
| `kfm:reason_codes` | Canonical public-safe reason codes. |
| `kfm:authority` | Required all-false authority flags for this profile object. |

## Finite trust classes

| Trust class | Required linkage | Prohibited inference |
|---|---|---|
| `UNRESOLVED` | no upstream reference is required | unresolved does not mean failed or false |
| `CATALOG_ONLY` | catalog identity only | cataloged does not mean receipted, proved, released, or published |
| `RECEIPT_BOUND` | `kfm:run_receipt_ref` | a receipt does not prove the claim or approve release |
| `PROOF_BOUND` | receipt and proof references | proof does not approve release or publication |
| `RELEASE_LINKED` | receipt, proof, and release references | a catalog projection does not execute the linked release |

## Invariants

1. `receipt != proof != catalog != release != publication`.
2. Source role uses the repository's canonical values: `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`.
3. `PROOF_BOUND` requires both receipt and proof references.
4. `RELEASE_LINKED` requires receipt, proof, and release references plus `kfm:release_state: RELEASE_LINKED`.
5. `PUBLICATION_LINKED` requires a release reference and release-linked state; the projection still carries no publication authority.
6. Every authority flag is `false`.
7. Arrays are unique and canonical where ordering is significant.
8. `kfm:spec_hash` excludes only itself from the hash subject.
9. Validator output contains stable reason codes and JSON pointers, never protected values.

## Validation boundary

The fixture-first validator checks the closed draft schema, deterministic identity, finite trust-class dependencies, source-role vocabulary, reference separation, state consistency, canonical arrays, and all-false authority flags.

A validator `PASS` does not establish complete STAC core conformance, source admission, EvidenceBundle resolution, proof authenticity, policy approval, review approval, release validity, publication, deployment, or public safety. External STAC conformance and namespace ratification remain **NEEDS VERIFICATION**.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive documentation, schema, validator, fixtures, tests, workflow, and receipt packet and restore the prior permissive schema blob. No catalog service, live source, release, deployment, or public artifact requires rollback.
