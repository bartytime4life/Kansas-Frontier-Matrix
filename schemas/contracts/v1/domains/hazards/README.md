<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-hazards-readme
title: schemas/contracts/v1/domains/hazards/ — Hazards Domain Schema Index
type: readme
version: v1.1
status: draft; repository-grounded; mixed-maturity; non-semantic; non-policy; non-release; non-publication
owner: NEEDS VERIFICATION — explicit CODEOWNERS routing for schemas/ is @bartytime4life; no independently verified Hazards schema steward or required-review control was established
created: 2026-08-28
updated: 2026-08-28
policy_label: repository-facing; schemas; hazards; machine-shape; cite-or-abstain; release-gated; no-life-safety-authority
current_path: schemas/contracts/v1/domains/hazards/README.md
owning_root: schemas/
responsibility: index the current Hazards machine-schema lane without replacing semantic contracts, evidence, policy, lifecycle, release, or publication authority
truth_posture: cite-or-abstain; file presence and schema validity prove only current machine shape, never source admission, semantic truth, evidence closure, rights, sensitivity, policy approval, release state, publication safety, or life-safety authority
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_ref: main
evidence_base_commit: bacb77cfbc04014a2c05da541f9cba8025629068
codeowners_route: /schemas/ @bartytime4life
directory_rules_adoption_adr: docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
related:
  - ../../../../README.md
  - ./receipts/README.md
  - ../../hazards/README.md
  - ../../../../../contracts/domains/hazards/README.md
  - ../../../../../docs/domains/hazards/README.md
  - ../../../../../fixtures/domains/hazards/README.md
  - ../../../../../tests/domains/hazards/README.md
  - ../../../../../tools/validators/domains/hazards/README.md
  - ../../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../../docs/doctrine/directory-rules.md
notes:
  - "v1.1 corrects the prior claim that this lane contained no concrete schema files; the pinned tree contains 23 root-level .schema.json files and one receipts child index."
  - "The inventory is maturity-specific: permissive scaffolds, bounded proposed profiles, and tested convergence profiles are not described as one implementation state."
  - "Accepted ADR-0029 adopts Directory Rules placement; ADR-0001 and the Hazards architecture schema-home question remain proposed or NEEDS VERIFICATION and are not accepted here."
  - "This documentation-only change modifies no schema bytes, contract semantics, source state, evidence, policy, lifecycle object, release, deployment, or public surface."
[/KFM_META_BLOCK_V2] -->

# `schemas/contracts/v1/domains/hazards/` — Hazards Domain Schema Index

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Inventory: 23 schemas](https://img.shields.io/badge/inventory-23%20schemas-2da44e?style=flat-square)](#current-schema-inventory)
[![Authority: machine shape](https://img.shields.io/badge/authority-machine%20shape-1f6feb?style=flat-square)](#authority-boundary)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#exposure-mutation-and-retention)

> [!IMPORTANT]
> **Schema presence is not operational authority.** These files constrain proposed or fixture-backed machine shapes. They do not admit a source, prove a hazard claim, authorize an emergency alert, promote lifecycle state, approve a release, or permit publication.

## Purpose

This directory is the populated Hazards domain lane under the `schemas/` machine-shape responsibility root. It owns JSON Schema files and local schema-family navigation. It inherits the contract/schema/policy/evidence/release separation from the [schema-root contract](../../../../README.md) and accepted [Directory Rules](../../../../../docs/doctrine/directory-rules.md).

The index reports what is present at pinned `main@bacb77cfbc04014a2c05da541f9cba8025629068`. It does not upgrade a scaffold or proposed profile to active status.

## Status

| Field | Repository-grounded value |
|---|---|
| Owning responsibility root | `schemas/` — machine-checkable shape |
| Local scope | Hazards domain schema index |
| Current root inventory | 23 `.schema.json` files |
| Current child lane | [`receipts/`](./receipts/README.md), index-only; no child schema file is present |
| Maturity | Mixed: 16 permissive or empty proposed scaffolds; 7 bounded proposed profiles with executable evidence |
| CODEOWNERS route | `/schemas/ @bartytime4life` |
| Steward assignment | **NEEDS VERIFICATION** beyond the repository route |
| Source admission, policy, release, deployment, publication | Not granted by this lane |

## Authority boundary

[Accepted ADR-0029](../../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the Directory Rules bytes that place domain machine shape under `schemas/contracts/v1/domains/<domain>/`. The narrower [ADR-0001](../../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) remains proposed. The alternate [`schemas/contracts/v1/hazards/`](../../hazards/README.md) lane is a README-only guardrail, not a second writable schema home.

The Hazards architecture contains a conflicting, proposed schema-home statement. This index records the current populated tree and accepted responsibility-root placement; it does not silently resolve the remaining documentation/ADR question.

The authority split remains:

```text
contracts/  semantic meaning and claim limits
schemas/    machine-checkable shape
fixtures/   valid, invalid, edge, and golden examples
tests/      executable proof for the tested surface
tools/      validator implementation
policy/     allow, deny, restrict, hold, and abstain decisions
data/       lifecycle objects, receipts, proofs, catalogs, and published carriers
release/    promotion, release, correction, withdrawal, and rollback decisions
```

## Current schema inventory

### Bounded proposed profiles with executable evidence

| Schema | Declared posture | Confirmed executable evidence |
|---|---|---|
| `drinking_water_advisory.schema.json` | `PROPOSED_INACTIVE`; closed advisory profile | Domain test, validator, fixtures, and dedicated workflow |
| `drought_observation.schema.json` | `PROPOSED`; closed physical-observation family | Valid/invalid fixtures plus drought separation and family-validator tests |
| `drought_declaration.schema.json` | `PROPOSED`; closed legal/administrative family | Valid/invalid fixtures plus drought separation and family-validator tests |
| `drought_obs_decl_relationship.schema.json` | `PROPOSED`; closed relationship family | Valid/invalid fixtures plus drought separation and family-validator tests |
| `evidence_bundle.schema.json` | `PROPOSED`; Hazards projection of the shared EvidenceBundle | Convergence validator, test, and dedicated workflow |
| `kdhe_hab_advisory_snapshot.schema.json` | `PROPOSED`; closed no-network snapshot candidate | Valid/invalid fixtures and schema tests |
| `nfhl_nld_nid_source_role_profile.schema.json` | `PROPOSED_INACTIVE`; closed source-role profile | Fixture cases, validator test, and dedicated workflow |

Executable evidence proves only the asserted fixture and validator behavior. It does not prove live retrieval, source admission, rights, freshness, complete EvidenceRef resolution, policy activation, release, or publication.

### Permissive or empty proposed scaffolds

The following 16 files are present, but their current descriptions or open shapes identify them as scaffolds rather than field-complete contracts:

```text
catalog_matrix.schema.json
correction_notice.schema.json
decision_envelope.schema.json
domain_feature_identity.schema.json
domain_layer_descriptor.schema.json
domain_observation.schema.json
domain_validation_report.schema.json
evidence_drawer_payload.schema.json
hazards_decision_envelope.schema.json
layer_manifest.schema.json
promotion_decision.schema.json
release_manifest.schema.json
rollback_card.schema.json
run_receipt.schema.json
source_descriptor.schema.json
source_state_hash.schema.json
```

Their presence is **CONFIRMED**. Their field completeness, fixture polarity, validator coverage, consumer adoption, and activation are **NEEDS VERIFICATION**.

## Current child map

```text
schemas/contracts/v1/domains/hazards/
├── README.md
├── 23 root-level *.schema.json files
└── receipts/
    ├── .gitkeep
    └── README.md
```

No receipt schema file is present under the child lane at the pinned snapshot.

## What belongs here

- Hazards JSON Schema documents at the currently governed domain-machine-shape path.
- This index and bounded schema-family indexes.
- Links to paired contracts, fixtures, validators, tests, registry records, policy, evidence, correction, rollback, and release families.
- Migration or compatibility notes that preserve one writer and identify an accepted target.

## What is prohibited

- Semantic contract prose, policy rules, validator implementation, runtime code, connector logic, or pipeline logic.
- Source payloads, source-registry instances, emitted receipts, proofs, EvidenceBundles as instance data, catalogs, or release records.
- RAW, WORK, QUARANTINE, PROCESSED, PUBLISHED, or other lifecycle payloads.
- Emergency directions, public alert authority, or claims that a schema-valid object is safe for operational use.
- Duplicate writable schemas under the alternate Hazards guardrail lane without an accepted migration decision.

## Inputs and outputs

Inputs are reviewed semantic contracts, accepted placement decisions, object-family identity, and explicit shape requirements. Outputs are versioned JSON Schema documents and this navigation index.

Permitted writers are repository contributors routed through CODEOWNERS and normal review. A schema edit must not mutate semantic meaning, evidence state, policy state, lifecycle state, or release state by implication.

## Exposure, mutation, and retention

This lane is repository-facing and contains no sensitive hazard instance payloads. Schema files are mutable only through reviewed Git history. Published payloads and release decisions are outside this directory. Rollback is a reviewed revert of the index or schema commit; it is not a lifecycle rollback by itself.

## Validation

For this index, the minimum documentation checks are metadata, local links, changed-document graph, whitespace, and repository topology. For a schema change, add the narrowest paired schema/fixture tests and the relevant domain or convergence workflow.

Confirmed executable relationships include:

- [Drought schema separation tests](../../../../../tests/schemas/test_drought_separation_contracts.py)
- [KDHE HAB snapshot schema tests](../../../../../tests/schemas/test_kdhe_hab_advisory_snapshot_contracts.py)
- [Hazards EvidenceBundle convergence test](../../../../../tests/validators/domains/hazards/test_evidence_bundle_schema_convergence.py)
- [NFHL/NLD/NID source-role validator test](../../../../../tests/validators/domains/hazards/test_validate_nfhl_nld_nid_source_role_profile.py)
- [Drinking-water advisory fixtures](../../../../../fixtures/domains/hazards/drinking_water_advisory/README.md)
- [Hazards validator index](../../../../../tools/validators/domains/hazards/README.md)

## Related families

| Family | Responsibility |
|---|---|
| [Hazards semantic contracts](../../../../../contracts/domains/hazards/README.md) | Meaning and claim limits; not machine shape |
| [Hazards domain documentation](../../../../../docs/domains/hazards/README.md) | Human navigation and doctrine; not schema authority |
| [Hazards fixtures](../../../../../fixtures/domains/hazards/README.md) | Representative test material; not source or published data |
| [Hazards tests](../../../../../tests/domains/hazards/README.md) | Executable assertions for covered behavior |
| [Hazards receipts schema child](./receipts/README.md) | Candidate receipt-shape index; no emitted receipts |
| [Alternate Hazards schema guardrail](../../hazards/README.md) | README-only conflict/migration boundary; no current schema files |

## Review burden

Changes require the repository's `schemas/` owner route. Object-family changes also require the relevant semantic-contract, validation, evidence, policy, and release reviewers where those responsibilities are affected. Named steward assignments and enforced separation of duties remain **NEEDS VERIFICATION**.

## Open verification

- Map every scaffold to its exact semantic contract and classify whether it should be completed, replaced by a shared reference, or retired.
- Record complete valid/invalid fixture and validator coverage per schema.
- Reconcile the proposed Hazards architecture schema-home statement with accepted Directory Rules and the populated domain lane without creating parallel authority.
- Verify schema-registry records, `$id` uniqueness, and downstream consumers.
- Verify source admission, rights, sensitivity, freshness, EvidenceRef closure, policy, release, correction, withdrawal, and rollback dependencies before any operational use.

## Last reviewed

| Field | Value |
|---|---|
| Evidence date | 2026-08-28 |
| Pinned repository commit | `bacb77cfbc04014a2c05da541f9cba8025629068` |
| Review result | 23 root schema files and one index-only child lane confirmed; maturity reported file-family by file-family |
| Next trigger | Schema add/remove/rename, schema-home authority change, fixture/validator/workflow change, registry change, or consumer adoption |
