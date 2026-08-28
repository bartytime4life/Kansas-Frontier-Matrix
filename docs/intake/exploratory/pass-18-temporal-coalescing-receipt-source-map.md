<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-temporal-coalescing-receipt
title: Pass 18 Temporal Coalescing Receipt Source Map
type: exploratory-intake; implementation-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; source-lineage; temporal; evidence
related:
  - ../../../contracts/evidence/temporal_coalescing_receipt.md
  - ../../../schemas/contracts/v1/evidence/temporal_coalescing_receipt.schema.json
  - ../../../fixtures/contracts/v1/evidence/temporal_coalescing_receipt/cases.json
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Temporal Coalescing Receipt Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical page 153 / printed page 150 | Card `KFM-P18-INV-414` proposes recording whether adjacent or overlapping periods were coalesced, split, or retained separately and identifies event-count, duration, and continuity interpretation risk. | `CONFIRMED` |
| Connected Drive `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` (`1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5`, modified `2026-05-17T16:04:12Z`) | Its downstream carrier card `KFM-P9-PROG-0015` independently calls for coalescing receipts that list merged interval identifiers and evidence references. | `CONFIRMED` |
| `main@149af17075f7f12d716aa14de439ea22ee6a343e` | Exact searches found temporal-window, temporal-slice, temporal-support, RunReceipt, and spatial-transform surfaces, but no temporal coalescing receipt/profile, validator, fixture family, workflow, or matching PR history. | `CONFIRMED` for the inspected snapshot |

The supplied and Drive artifacts are proposal evidence, not repository instruction authority. External source-rights, package, database, and runtime claims were not needed for this no-network adaptation.

## Reconciliation and selected increment

The repository already owns:

- temporal interval meaning in `contracts/common/temporal_window.md` and `contracts/data/temporal_slice.md`;
- temporal evidence fitness in `contracts/evidence/temporal_support_assessment.md`;
- execution provenance in `contracts/runtime/run_receipt.md`; and
- a sibling transform-receipt pattern in `contracts/evidence/spatial_transform_receipt.md`.

The selected increment is therefore one additive evidence-receipt profile that composes those authorities by reference. It does not create a temporal store, transform engine, duration policy, evidence resolver, or release decision.

## Source-to-profile mapping

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Record coalesced, split, or separate temporal facts. | Closed `operation` vocabulary with operation-specific interval invariants. | No transform execution or semantic-equivalence inference. |
| List merged interval identifiers. | Output-to-input lineage closure over exact interval IDs. | No database identifier migration or source mutation. |
| Preserve evidence references. | Sorted bounded `evidence_refs` retained for a later resolver. | No evidence resolution or claim authorization. |
| Make continuity-changing behavior reviewable. | Half-open UTC coverage equality, fact-key preservation, canonical order, and digest replay. | No public display, review approval, or policy decision. |
| Remain downstream of release controls. | All authority effects are fixed false. | No promotion, release manifest creation, release, deployment, or publication. |

## Directory Rules basis

`contracts/evidence/` owns this receipt profile's meaning; the versioned schema, fixtures, validator, tests, workflow, and generated receipt remain in their established responsibility roots. No new root or parallel temporal, evidence, receipt, policy, release, or publication authority is introduced.

## Deferred questions

- Which domain steward may declare two source-split intervals semantically continuous?
- Which accepted duration-policy object should be referenced by a later runtime consumer?
- Which released reader surface, if any, should expose source interval lineage?
- How should corrections supersede a receipt after source interval boundaries change?

These questions require separate decisions. This profile fixes none of them.

## Validation and rollback

Focused validation covers closed schema shape, deterministic profile and interval-set digests, all three source dispositions, unresolved-method abstention, coverage loss, fact-key collapse, incomplete lineage, invalid duration, digest tampering, and unknown-field rejection.

Rollback is a focused revert of this additive packet. No data reprocessing, correction notice, release withdrawal, cache invalidation, or public cleanup is required because the profile executes no transform and emits no release.
