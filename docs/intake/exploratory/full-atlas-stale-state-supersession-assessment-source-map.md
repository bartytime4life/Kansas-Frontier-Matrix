<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/full-atlas-stale-state-supersession-assessment
title: Full Atlas Stale-State and Supersession Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD - Intake steward · Data steward · Evidence steward · Correction steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; stale-state; supersession; correction; release
responsibility: Preserve source and repository lineage for a bounded stale-state and supersession assessment without deciding cross-lane propagation, changing object state, rewriting history, issuing correction, or granting lifecycle authority.
truth_posture: "CONFIRMED connected Full Atlas topic, current repository stale-state reference, accepted Directory Rules, adjacent object families, and inspected-repository gap; PROPOSED bounded assessment; UNKNOWN cross-lane propagation and steward ownership; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/common/stale_state_supersession_assessment.md
  - ../../atlases/stale-state-reference.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Full Atlas stale-state and supersession assessment source map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Connected Google Drive `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) | The "Stale-State and Supersession Lineage" topic proposes visible stale-state markers, explicit lineage, correction links, and tests that forbid silent replacement. The cards retain unresolved pass/ordinal placeholders, so the topic is cited rather than assigned a fabricated stable ID. | `CONFIRMED` proposal lineage |
| `docs/atlases/stale-state-reference.md` | The current repository already distinguishes stale from wrong, lists marker and lineage families, preserves AIReceipt non-retroactivity, and explicitly leaves cross-lane propagation open. | `CONFIRMED` current repository guidance; not machine authority |
| Existing SourceDescriptor, EvidenceBundle, correction, withdrawal, release, rollback, review, and temporal contracts | These families already own their meanings. | `REUSE BY OPAQUE REF`; do not create parallel authority |
| `docs/doctrine/directory-rules.md` and accepted ADR-0029 | Contract meaning, schema shape, fixtures, validation, tests, source mapping, and CI each remain in their owning responsibility roots; path placement cannot create lifecycle authority. | `CONFIRMED` accepted placement authority |
| Starting `main@01b3f70bb0514c0557e777294b36992317e992c8` plus repository, history, branch, and pull-request searches | No exact stale-state/supersession assessment contract, schema, fixture family, validator, workflow, branch, or open pull request was found. Existing stale-doc scanning and withdrawal/correction objects solve different problems. | `CONFIRMED` bounded implementation gap |

The Drive source is evidence input, not repository authority. Current repository
objects and accepted Directory Rules control the adaptation.

## Collision decision

| Source pressure | Existing owner | Decision |
|---|---|---|
| Define stale-state markers and supersession rules. | The repository atlas reference already preserves the navigational doctrine. | `REUSE`; do not duplicate or canonize the atlas table. |
| Record corrections, withdrawals, releases, rollbacks, evidence, policy, and review. | Existing object-family contracts own those meanings. | `REFERENCE`; never embed replacement objects here. |
| Decide cross-lane propagation. | The repository reference marks the decision open. | `HOLD`; the assessment exposes affected surfaces but cannot propagate state. |
| Prove one declaration is coherent. | No bounded executable assessment was found. | `PLACE` one inactive contract/schema/fixture/validator packet. |

## Selected increment

| Concern | Bounded adaptation | Held boundary |
|---|---|---|
| Stale vs incorrect | One explicit marker and substance posture. | The validator neither measures freshness nor determines truth. |
| Supersession lineage | Explicit predecessor/successor, retention, effective time, and lineage refs. | No object is modified, deleted, replaced, or made current. |
| Immutable AI history | `AI_RECEIPT` permits only a new-receipt cross-reference. | No prior receipt is rewritten or replayed. |
| Correction/release closure | Incorrect or public cases require declared correction/withdrawal/rollback support. | Refs remain opaque and unresolved. |
| Human review | A coherent declaration returns `REVIEW_REQUIRED`. | A passing fixture cannot approve review or state transition. |

## Directory Rules path decision

| Artifact | Responsibility signature | Outcome |
|---|---|---|
| Assessment meaning | Cross-family semantic contract, no lifecycle instance, internal, versioned; `contracts/common/`. | `PLACE` |
| Machine shape | Closed Draft 2020-12 schema; `schemas/contracts/v1/common/`. | `PLACE` |
| Synthetic cases | Public-safe test inputs; `fixtures/contracts/v1/common/`. | `PLACE` |
| Validator and tests | Repository validator and executable conformance; `tools/validators/governance/` and `tests/validators/governance/`. | `PLACE` |
| Source lineage and orchestration | Human exploratory mapping and platform read-only CI; `docs/intake/exploratory/` and `.github/workflows/`. | `PLACE` |

No new root, stale-state register, correction store, supersession store, policy
package, receipt family, release lane, runtime service, or public path is
created.

## Deferred questions

- Which cross-lane propagation rules are accepted, and which surfaces are merely reported?
- Which object families require mandatory freshness evaluation, and at what cadence?
- Which reviewer classes may complete a real assessment?
- How correction, withdrawal, cache invalidation, and public notice compose remains outside this candidate.

## Rollback

Rollback is a focused revert of the additive packet. No object, lineage,
correction, policy, cache, release, deployment, publication, or public state
requires restoration.
