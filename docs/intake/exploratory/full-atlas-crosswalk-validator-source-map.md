<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/full-atlas-crosswalk-validator-source-map
title: Full Atlas SQL-First Non-Publisher Crosswalk Validator Source Map
type: source-map
version: v0.1.0
status: proposed; exploratory; non-authoritative
owners: OWNER_TBD — intake steward; join steward; validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: repository-facing; provenance; implementation-intake
owning_root: docs/
responsibility: Record the evidence chain and repository-gap decision for the proposed CrossLaneJoinAssessment helper.
truth_posture: cite-or-abstain
[/KFM_META_BLOCK_V2] -->

# Full Atlas SQL-first non-publisher crosswalk validator source map

## Selected idea

| Item | Evidence reference | Use |
|---|---|---|
| Full Atlas idea card | `gdrive://1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho#Crosswalk Validator Lane (SQL-First Non-Publisher)`; Drive revision `AIroW364lZaCNMZL0IeqV_wlJ6faYfOIOR2mrnnjeZjOizodlP7bmOVL8UDK_45hHBIZLfgkHpq_ik04xfjj4okO6S4U8srdHXuvBMtQqrw` | Requires a narrow SQL-first validator whose rule failure counts feed `ALLOW`, `DENY`, `ABSTAIN`, or `ERROR`, with no `ANSWER`/`HOLD` and no publisher authority. |
| Repository join plan | `tools/joins/README.md` (`sha256:0659f1a0332bac17b4d8db2021e37bd1a4fd987ea95ae5de83c39a1b27811174`) | Names `join_candidates.py`, expected reports, and the six first synthetic fixture classes. |
| Generic validator boundary | `tools/validators/cross-domain-joins/README.md` (`sha256:e08199585f51d92e99ac767a02682a9ad7c2f65e249a452b638537e9288da4d8`) | Requires ownership, source-role, sensitivity, evidence, identity, time, space, and non-publication preservation. |
| Directory authority | `docs/doctrine/directory-rules.md` (`sha256:44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`) | Governs placement and prevents parallel source, policy, receipt, or release authority. |
| Adoption decision | `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` | Establishes the accepted Directory Rules baseline. |

The exact Drive paragraph range is tab `t.0`, indexes `710077–710168`; its normalized statement is at `710431–710754`. These ranges pin the inspected revision but do not turn the synthesis card into implementation authority.

## Repository-gap check

The implementation base is `eed7627f0bac70c4f11303ce6790320f46f7b080`. Current-tree and active-branch searches found the join doctrine and pair-specific README lanes, but no `tools/joins/join_candidates.py`, executable generic join assessment, dedicated `tests/joins/` proof, or path-scoped workflow. The repository README itself labels those surfaces `PROPOSED`.

## Decision and boundaries

Status: `REPO_GAP`. The smallest dependency-closed continuation implements only exact-key and synthetic spatial-temporal candidate assessment, the six requested risk fixtures, stable rule-level counts, and finite validator outcomes. It does not create a crosswalk registry, real spatial join, source descriptor, EvidenceBundle, PolicyDecision, receipt, lifecycle record, canonical relation, graph edge, ReleaseManifest, or public artifact.

## Collision and rollback note

Main through `eed7627f` and branches matching `cross-lane`, `join-assessment`, and related source terms were inspected before implementation. Revert the bounded implementation commit to remove the proposal; no database, lifecycle, release, or public rollback is required.
