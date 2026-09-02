<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-temporal-retention-disposition-assessment
title: Pass 18 Temporal Retention Disposition Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Governance steward · Temporal steward · Privacy steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; governance; temporal; retention; erasure
responsibility: Preserve source and repository lineage for a bounded retention-disposition assessment without deciding policy, authorizing erasure, executing maintenance, or deleting history or evidence.
truth_posture: "CONFIRMED attached-card transcription, visual review, and inspected-repository comparison; PROPOSED bounded KFM adaptation; UNKNOWN policy ownership and family adoption; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/governance/temporal_retention_disposition_assessment.md
  - ../../../contracts/evidence/after_image_reconstruction_record.md
  - ../../../contracts/correction/correction_propagation_plan.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Temporal Retention Disposition Assessment Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical PDF page 122 / printed page 119 | Card `KFM-P18-INV-439` proposes an explicit temporal-vacuuming policy that separates archival retention from deletion of evidence, depends on retention policy, proof archive, rollback target, and audit ledger, and surfaces the tension between privacy erasure and audit retention. The page was rendered and visually inspected. | `CONFIRMED` |
| `contracts/evidence/after_image_reconstruction_record.md` | The adjacent reconstruction-support contract explicitly leaves retention policy unresolved and grants no deletion, evidence-mutation, or lifecycle authority. | `CONFIRMED` adjacent responsibility |
| `contracts/correction/correction_propagation_plan.md` | Correction and rollback dependencies already have a separate planning surface; this increment references dependency state without replacing propagation planning. | `CONFIRMED` adjacent responsibility |
| Starting `main@bd59127604f3ab7578fe43f30caaeef089c0fffc` plus repository, code, branch, and PR searches | No exact card ID, retention-disposition contract, schema, fixture family, validator, workflow, matching branch, or open matching PR was found before implementation. | `CONFIRMED` inspected snapshot |

The attached and Drive sources are design evidence, not repository instruction,
legal interpretation, privacy authority, or permission to run a destructive
database operation.

## Selected increment

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Prevent temporal vacuuming from silently deleting evidence. | Distinguish `RETAIN`, `ARCHIVE`, `COMPACT`, and `ERASE`; require declared proof preservation and dependency state. | No database inspection, `VACUUM`, archive write, compaction, mutation, or deletion. |
| Preserve reconstructability and rollback. | Archive and compaction proposals require explicit archive, disposition receipt, reversibility, and rollback declarations. | References are opaque and unresolved; no proof or rollback is executed. |
| Reconcile retention with privacy erasure. | Erasure always holds for separate authority, even when a synthetic obligation is declared verified. | No legal determination, identity resolution, consent change, or erasure authorization. |
| Keep released dependents visible. | Active release state blocks erasure and holds compaction for a separate handoff. | No release withdrawal, correction, propagation, or lifecycle write. |

## Directory Rules basis

| Artifact | Owning root and scope | Outcome |
|---|---|---|
| Semantic assessment meaning | `contracts/governance/` owns the cross-family governance contract. | `PLACE` |
| Closed machine shape | `schemas/contracts/v1/governance/` owns the Draft 2020-12 schema. | `PLACE` |
| Public-safe replay and validation | `fixtures/contracts/v1/governance/`, `tools/validators/governance/`, and `tests/validators/governance/` own deterministic conformance. | `PLACE` |
| Source lineage and read-only CI | `docs/intake/exploratory/` and `.github/workflows/` keep their existing non-authoritative roles. | `PLACE` |

No new root, retention-policy register, privacy/legal rule, archive store,
maintenance job, deletion service, evidence authority, correction service,
release lane, or public path is created.

## Deferred questions

- Which steward roles may approve retention schedules and separately authorize erasure?
- Which temporal record families, if any, should adopt this inactive profile?
- What archive and receipt objects would prove a reversible disposition in runtime use?
- How should legal hold, data minimization, released dependents, and evidence-preservation obligations be reconciled in policy?

## Rollback

Rollback is a focused revert of the additive packet. No database record, archive,
evidence object, correction, policy, legal decision, release, deployment, or
public artifact requires restoration.
