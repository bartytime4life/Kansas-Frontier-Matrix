<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-open-ended-temporal-semantics-disclosure
title: Pass 18 Open-Ended Temporal Semantics Disclosure Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Common contract steward · Temporal steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; temporal; open-ended; as-of
responsibility: Preserve exact and thematic source lineage for the bounded open-ended temporal-semantics adaptation without promoting proposal material into temporal truth, policy, review, release, or publication authority.
truth_posture: "CONFIRMED attached-card transcription and inspected-repository comparison; PROPOSED bounded adaptation; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/common/open_ended_temporal_semantics_disclosure.md
  - ../../../contracts/common/temporal_window.md
  - ../../../contracts/common/period_boundary_predicate_disclosure.md
  - ../../../schemas/contracts/v1/common/open_ended_temporal_semantics_disclosure.schema.json
  - ../../../fixtures/contracts/v1/common/open_ended_temporal_semantics_disclosure/cases.json
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Open-Ended Temporal Semantics Disclosure Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical pages 87–88 | Card `KFM-P18-INV-093` proposes explicit `temporal_open_end_policy` and `now_resolution_time` semantics and distinguishes observation, source, transaction, release, and related time roles. | `CONFIRMED` |
| Same supplied PDF, physical pages 100 and 108 | Cards `KFM-P18-INV-194` and `KFM-P18-INV-287` warn that now-relative validity and forever sentinels create ambiguity and require explicit handling. | `CONFIRMED` supporting lineage |
| Connected Drive `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) | The `Time-Aware Spatial Semantics Pattern` distinguishes valid, observed, source, retrieval, release, and correction time and calls for explicit query mode and time windows. Its stable IDs remain placeholders, so it is thematic corroboration rather than exact-card identity. | `CONFIRMED` thematic corroboration |
| `main@c4cb046829f72afd07e39d167c781fb7435a9ac4` | Exact searches found the common `TemporalWindow`, the finite period-boundary profile, and an as-of snapshot profile. The period-boundary source map explicitly deferred open-ended periods; no reusable open-ended/current/now-relative disclosure contract, closed schema, fixture corpus, validator, or matching branch was present. | `CONFIRMED` for the inspected snapshot |

The supplied and Drive artifacts are proposal evidence, not repository instruction authority. Connected-source identifiers are included only for traceability; no private Drive content is copied into fixtures or validator output.

## Reconciliation and selected increment

The repository already separates time roles and owns finite windows, interval-boundary predicates, and snapshot as-of semantics. Expanding those accepted objects, picking one universal “current” clock, or rewriting stored sentinel values would create compatibility and authority risk.

The selected increment is therefore one additive common disclosure profile. It makes end absence, as-of resolution, now-basis role, supersession caveat, and sentinel use explicit without modifying an existing temporal object or consumer.

## Source-to-profile mapping

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Open-ended “now” needs explicit semantics. | Four-value end-semantics vocabulary plus nullable end and pinned as-of instant. | No universal clock or domain rule. |
| Time roles must not collapse. | Closed now-basis vocabulary for observed, source, transaction, and release time. | No equivalence or inference between roles. |
| Current state differs from unknown end. | Separate `CURRENT_KNOWN_STATE` and `END_NOT_KNOWN` interpretations. | No temporal-truth determination. |
| Forever sentinels are risky. | Explicit sentinel declaration and fail-closed prohibition. | No migration or source rewrite. |
| Public explanation needs governance. | Public-use obligation plus at least one review-record reference. | No review, release, publication, or public-use authority. |
| Missing context must remain visible. | `ABSTAIN` for unresolved scope or incomplete/unknown disclosure. | No guessed defaults. |

## Directory Rules basis

Shared temporal semantics live in `contracts/common/`; their closed shape, synthetic examples, validation, tests, workflow, source mapping, and generated receipt remain in established responsibility roots. The accepted Directory Rules at `docs/doctrine/directory-rules.md` and accepted ADR-0029 were consulted before placement. No new root or parallel authority is introduced.

## Deferred questions

- Which accepted domain objects should adopt this profile and which clock role should each use?
- How should uncertain, recurring, fuzzy, and anticipated intervals compose with open-ended semantics?
- Which migration can replace legacy far-future sentinels while preserving source provenance and rollback?
- Which accepted reader surface, if any, may render a reviewed public explanation?

These questions require separate decisions. This profile fixes none of them.

## Validation and rollback

Focused validation covers closed schema shape, deterministic identity, all four end semantics, UTC/order, required as-of and now-basis roles, interpretation/obligation alignment, sentinel prohibition, unresolved/incomplete abstention, public-review prerequisites, canonical references, hash tampering, and unknown-field rejection.

Rollback is a focused revert of this additive packet. No data reprocessing, correction notice, release withdrawal, cache invalidation, UI cleanup, or public cleanup is required because the profile has no consumer and changes no existing temporal object.
