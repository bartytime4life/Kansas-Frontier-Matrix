<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-period-boundary-predicate-disclosure
title: Pass 18 Period-Boundary Predicate Disclosure Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Common contract steward · Temporal steward
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; source-lineage; temporal; interval-boundary
responsibility: Preserve exact and thematic source lineage for the bounded period-boundary predicate disclosure adaptation without promoting proposal material into temporal truth, policy, release, or publication authority.
truth_posture: "CONFIRMED attached-card transcription and inspected-repository comparison; PROPOSED bounded adaptation; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/common/period_boundary_predicate_disclosure.md
  - ../../../contracts/common/temporal_window.md
  - ../../../schemas/contracts/v1/common/period_boundary_predicate_disclosure.schema.json
  - ../../../fixtures/contracts/v1/common/period_boundary_predicate_disclosure/cases.json
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Period-Boundary Predicate Disclosure Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical page 52 / printed page 49 | Card `KFM-P18-INV-462` proposes disclosing closed versus half-open interval semantics and whether periods overlap, meet, occur during, start, or finish together. | `CONFIRMED` |
| Connected Drive `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) | The `Time-Aware Spatial Semantics Pattern`, capability, and implementation carriers require distinct time meanings plus explicit temporal query mode, time window, geography version, uncertainty, and fitness. Their stable IDs remain placeholders, so they are thematic corroboration rather than exact-card or repository identity. | `CONFIRMED` thematic corroboration |
| `main@7d3b894deeb82d3ecb0ddf3daeec9158f266edb1` | Exact searches found `TemporalWindow`, temporal-slice, temporal-support, temporal-coalescing, playback-bucket, and query-receipt surfaces, but no period-boundary predicate disclosure contract, schema, fixture family, validator, workflow, or matching PR history. | `CONFIRMED` for the inspected snapshot |

The supplied and Drive artifacts are proposal evidence, not repository instruction authority. The connected Drive Pass 18 PDF has a different byte size and its text extraction did not expose `KFM-P18-INV-462`; this source map therefore does not claim byte identity or exact-card corroboration from that Drive PDF.

## Reconciliation and selected increment

The repository already owns generic interval meaning in `contracts/common/temporal_window.md`, domain temporal slices, evidence fitness, playback buckets, and transform receipts. Expanding those established objects or selecting a universal boundary convention would create compatibility and authority risk.

The selected increment is therefore one additive common disclosure profile. It pins existing window candidates by reference, makes boundary inclusion explicit, and checks a finite relation plus intersection shape without changing any existing temporal schema or consumer.

## Source-to-profile mapping

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Disclose closed versus half-open periods. | Four conventional inclusion patterns plus `MIXED_EXPLICIT`, checked against both intervals. | No repository-wide convention decision. |
| Distinguish overlap, meeting, during, starting, and finishing. | Closed 13-relation endpoint vocabulary with exhaustive positive fixtures. | No external-standard conformance claim or uncertain-time inference. |
| Make boundary consequences understandable. | Separate `EMPTY`, `POINT`, and `INTERVAL` intersection shape computed with inclusivity. | No claim-truth or fitness determination. |
| Bind the disclosure to its claim and windows. | Pinned refs and digests with explicit unresolved abstention. | No resolver or authentication. |
| Retain evidence lineage. | Sorted bounded evidence refs. | No evidence resolution, review, or release authority. |

## Directory Rules basis

The profile meaning is adjacent to the current `contracts/common/temporal_window.md` shared value object. Shape, fixtures, validator, tests, workflow, source mapping, and generated receipt remain in their established responsibility roots. No new root or parallel temporal, evidence, policy, release, or publication authority is introduced.

## Deferred questions

- Which domains should adopt closed, open, or either half-open convention?
- How should uncertain, fuzzy, recurring, or open-ended periods disclose predicates?
- Which accepted object should bind geography version and clock/precision metadata to this profile?
- Which released reader surface, if any, may present these explanations?

These questions require separate decisions. This profile fixes none of them.

## Validation and rollback

Focused validation covers closed schema shape, deterministic identity, proper UTC intervals, all 13 endpoint relations, conventional and mixed inclusivity, empty/point/interval intersection shape, unresolved-reference abstention, canonical evidence references, hash tampering, and unknown-field rejection.

Rollback is a focused revert of this additive packet. No data reprocessing, correction notice, release withdrawal, cache invalidation, UI cleanup, or public cleanup is required because the profile has no consumer and changes no existing temporal object.
