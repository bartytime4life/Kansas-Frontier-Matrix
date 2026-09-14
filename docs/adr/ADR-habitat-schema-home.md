<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/habitat-schema-home
title: "ADR Candidate — Habitat Schema Home"
adr_id: ADR-habitat-schema-home
type: architecture-decision-record; unassigned-scaffold
version: v1.1
status: proposed
effective_decision_status: not-assigned
owners:
  - <habitat-domain-steward>
  - <schema-steward>
  - <contract-steward>
reviewers_required:
  - <architecture-steward>
  - <validation-steward>
  - <docs-steward>
created: 2026-07-24
updated: 2026-09-14
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
current_path: docs/adr/ADR-habitat-schema-home.md
responsibility: "Preserve the unresolved Habitat schema-home question and its evidence crosswalk without selecting a path, assigning an ADR number, accepting a decision, creating a schema or migration authority, or changing runtime, data, release, or publication state."
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3b3940b52ecf1f7c71e32b298fd76499af116e75
  target_prior_blob: b08c28162b86601244683312657d6e85ded0bf01
  adr_index_blob: 0c143676dfd3c1bda16cb44398c5ad5d4a49cf67
  adr_0001_blob: 5a9fe1d142582589d4b6db8e02064508157731d0
  habitat_alias_guardrail_blob: 0d011f06cdb9d1bffb2df57c9f7300d683222302
  habitat_domain_model_blob: d94aab2a7238953fea9a2e8e18ea98157c5cc063
  habitat_architecture_blob: 82263ea8f5862401e5aef57ec43f49711d12c998
  habitat_ecoregions_readme_blob: 4b796579b73598b0a9343848e1cf68b7613c1153
  habitat_catalog_readme_blob: 0d907f9e81de64cdd67a9e4594007873f0baf978
  habitat_rollback_readme_blob: df4dcd37fda290b297435eb7254196e32fe1da68
  scope_limit: >
    Documentation currentness reconciliation only. No ADR number assignment,
    acceptance, schema creation, move, deletion, alias promotion, migration,
    validation or CI execution, source admission, lifecycle-data operation,
    policy evaluation, runtime operation, release, deployment, promotion, or
    publication was performed.
related:
  - docs/adr/INDEX.md
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/domains/habitat/HABITAT_DOMAIN_MODEL.md
  - docs/domains/habitat/ARCHITECTURE.md
  - schemas/contracts/v1/habitat/README.md
tags: [kfm, adr, habitat, schema-home, contracts, schemas, governance, unassigned]
notes:
  - "The canonical ADR index classifies this exact file as a slug-only scaffold with decision status not-assigned."
  - "The repository contains conflicting Habitat schema-home guidance; this candidate records rather than resolves it."
  - "The v1.0 path-selection text is retained only as historical lineage and has no independent decision effect."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR Candidate — Habitat Schema Home

> **Unassigned scaffold — not a decision.** This file records the unresolved Habitat schema-home question and a source-level crosswalk. It does **not** select **schemas/contracts/v1/domains/habitat/**, **schemas/contracts/v1/habitat/**, or any other path as the canonical Habitat home.

![status](https://img.shields.io/badge/status-PROPOSED-yellow?style=flat-square)
![assignment](https://img.shields.io/badge/ADR%20assignment-NOT--ASSIGNED-6e7781?style=flat-square)
![schema-home](https://img.shields.io/badge/schema%20home-UNRESOLVED-important?style=flat-square)
![effect](https://img.shields.io/badge/effect-docs--only-lightgrey?style=flat-square)

## Status and authority boundary

| Field | Current posture |
| --- | --- |
| ADR-index classification | slug-only scaffold |
| Effective decision status | **not-assigned** |
| Repository-wide ADR number | None; this file does not reserve one |
| Scope | Habitat schema-home question and evidence crosswalk |
| Decision, migration, or implementation effect | None |
| This revision | Same-path documentation currentness reconciliation at main@3b3940b52ecf1f7c71e32b298fd76499af116e75 |

The canonical ADR index is controlling for this record’s inventory and assignment posture. It lists this exact filename under **Unassigned scaffolds** and says that such records do not carry a repository-wide number or reserve one.

The document is not an exception to ADR-0001, ADR-0002, ADR-0029, Directory Rules, contract/schema ownership, validation, release, or publication authority. It cannot independently accept, reject, supersede, or amend any of those records.

## Question preserved

What path, if any, should become the canonical Habitat machine-schema home, and what compatibility, migration, validation, consumer, and rollback evidence would be required before that status could be adopted?

This candidate intentionally leaves open:

- the relationship between flat **schemas/contracts/v1/habitat/** and segmented **schemas/contracts/v1/domains/habitat/** paths;
- the canonical source, profile, mirror, alias, transitional, and deprecated classifications for Habitat schema files;
- the ownership of Habitat-specific versus shared spatial, evidence, source, receipt, policy-envelope, and release-support shapes;
- any required identity, contract pairing, fixture, validator, CI, consumer, compatibility, migration, or rollback commitments.

A source path’s presence, a README statement, a JSON file, or successful parsing would not by itself settle any of these questions.

## Evidence crosswalk

The following targeted source reads establish a documentation conflict and boundary; they do not establish an accepted route or an active schema family.

| Source | Current source-level signal | Consequence for this candidate |
| --- | --- | --- |
| **docs/adr/INDEX.md** | This exact path is a slug-only scaffold with decision status not-assigned. | No ADR number or decision status is asserted here. |
| **ADR-0001** | The repository-wide schema-home record remains proposed. | This candidate cannot treat a root or a domain lane as accepted authority. |
| **docs/domains/habitat/HABITAT_DOMAIN_MODEL.md** | Explicitly labels Habitat schema-home as **CONFLICTED**, describing segmented and flat alternatives. | The conflict remains open. |
| **docs/domains/habitat/ARCHITECTURE.md** | Also labels the Habitat schema-home conflict unresolved and treats its ADR-S-01 reference as confirm-or-amend work. | ADR-S-01 is navigation/planning context, not an assigned ADR number or approval. |
| **schemas/contracts/v1/habitat/README.md** | Self-describes as an alias/guardrail index and says it must not become a parallel canonical home without ADR or migration work. | That guardrail is recorded; it does not decide the target home. |
| Habitat ecoregion, catalog, and rollback READMEs | Preserve or defer the schema-home question and avoid independent authority. | No downstream README can resolve this candidate’s question. |

Some repository documents still describe a configured or active Habitat lane. Those are source claims that conflict with the unassigned-index posture and the documented flat-versus-segmented conflict. This revision does not reconcile them by choosing one; any such choice requires a separately assigned and reviewed decision with a governed implementation plan.

## Non-effects

This update changes only the documentation posture of this one file. It does not:

- assign an ADR number, alter the ADR index, or change the status of ADR-0001, ADR-0002, or ADR-0029;
- create, move, delete, edit, validate, register, promote, deprecate, or alias a schema or contract;
- choose a Habitat schema directory, identity grammar, schema dialect, shared-shape boundary, or consumer compatibility posture;
- authorize a migration, correction, rollback, source admission, policy decision, runtime behavior, release, deployment, promotion, or publication;
- claim a test, CI run, validator result, inventory, or producer/consumer analysis that was not performed.

## Conditions for a future assigned decision

Before a later record can select a Habitat schema home, it should at minimum:

1. follow the normal ADR assignment workflow and update the canonical index in the same change;
2. inspect the competing path trees and identify every schema, README, identity, contract, fixture, validator, test, registry entry, producer, and consumer;
3. classify each overlapping surface as canonical, profile, mirror, alias, transitional, deprecated, stub, or unresolved;
4. determine which shapes belong to Habitat and which must remain shared;
5. specify compatibility, migration sequencing, validation, CI evidence, release constraints, rollback target, owners, and retirement conditions;
6. obtain the required architecture, Habitat, schema, contract, validation, and affected-consumer review.

Until those conditions are met, the safe posture is **HOLD / NEEDS VERIFICATION**.

## Historical lineage and rollback

The prior v1.0 text at this same path presented a proposed segmented-path selection. At the base commit recorded above, that presentation was incompatible with the canonical index’s unassigned status and the Habitat documentation’s explicit conflict. It has therefore been replaced with this bounded candidate; it is not retained as an operative decision.

This documentation-only revision is reversible by reverting its single commit. Any future schema migration requires its own reviewed migration and rollback record; reverting this document must not be interpreted as moving, activating, or restoring schema authority.

## Evidence boundary

This v1.1 reconciliation is grounded only in the pinned repository files named in the metadata block at main@3b3940b52ecf1f7c71e32b298fd76499af116e75. It is a targeted documentation read, not a filesystem inventory, schema validation, test/CI result, runtime observation, or release determination.

[Back to top](#top)
