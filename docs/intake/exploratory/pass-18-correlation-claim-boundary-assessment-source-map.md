<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-correlation-claim-boundary-assessment
title: Pass 18 Correlation Claim-Boundary Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Evidence steward · Analytics steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; analytics; correlation; causality-boundary
responsibility: Preserve exact and thematic source lineage for the bounded correlation claim-language adaptation without promoting proposal material into statistical, causal, evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED attached-card transcription and inspected-repository comparison; PROPOSED bounded adaptation; NEEDS VERIFICATION causal-design sufficiency, human review, and hosted exact-head CI"
related:
  - ../../../contracts/evidence/correlation_claim_boundary_assessment.md
  - ../../../contracts/evidence/analytic_output_disclosure_assessment.md
  - ../../../contracts/common/condition_relation.md
  - ../../../schemas/contracts/v1/evidence/correlation_claim_boundary_assessment.schema.json
  - ../../../fixtures/contracts/v1/evidence/correlation_claim_boundary_assessment/cases.json
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Correlation Claim-Boundary Assessment Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical pages 237–238 / printed pages 234–235 | Card `KFM-P18-INV-158` proposes labeling correlation aggregates as relationship evidence, denying or abstaining on causal wording without stronger design, and checking “correlation,” “association,” “contribution,” “exposure,” and “cause.” It marks sufficient causal-design evidence as an open question. | `CONFIRMED` |
| Same card’s source attribution to `SRC-P18-003`, `Advanced-SQL-Concepts.pdf`, page 22 | The cited source supports the availability of a `CORR()` aggregate. It does not, by itself, establish the KFM governance matrix or causal-design sufficiency. | `CONFIRMED` bounded source role |
| Connected Drive `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) | The `Interpretive Analytics Governance Pattern` keeps analytic outputs subordinate to evidence, assumptions, uncertainty, validation, confidence, citations, and interpretation limits. Stable IDs remain proposal placeholders, so this is thematic corroboration rather than exact-card identity. | `CONFIRMED` thematic corroboration |
| `main@c4cb046829f72afd07e39d167c781fb7435a9ac4` | `AnalyticOutputDisclosureAssessment` already requires `NO_CAUSAL_CLAIM`; `ConditionRelation` denies causal requests; domain contracts and validator guidance repeat correlation/causality cautions. Exact searches found no reusable correlation-method plus claim-role assessment for association, contribution, exposure, cause, and causal-design handoff. | `CONFIRMED` for the inspected snapshot |

The supplied and Drive artifacts are proposal evidence, not repository instruction authority. The source material supports a candidate boundary, not a conclusion about a real-world relationship or cause.

## Reconciliation and selected increment

The repository does not need another general analytic disclosure or contextual-relation authority. The selected increment is a thin evidence-lane composition profile that pins those two established objects and assesses only correlation-specific language.

It records method family, requested role, wording class, causal-design posture, caveats, and review prerequisites. It contains no observations or coefficient and cannot approve a causal claim.

## Source-to-profile mapping

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Correlation is relationship evidence. | Schema-fixed `RELATIONSHIP_EVIDENCE` role and association-only `PASS`. | No relationship-truth authority. |
| Causal wording needs stronger design. | Cause without design or with observational design is denied; unresolved or stronger design abstains for review. | No definition of sufficient causal evidence. |
| Contribution and exposure need language checks. | Both roles are explicit and always abstain to a stronger-claim review in v1. | No lexical model or domain-specific causal interpretation. |
| Analytic support must remain visible. | Pinned analytic-output, condition-relation, method-registry, uncertainty, and evidence references. | No reference resolution or recomputation. |
| Public use remains downstream. | Public/release-review use requires caveats and review-record references. | No review, release, publication, or public-use authority. |
| Ambiguity must not silently clear. | Ambiguous wording yields `ABSTAIN`. | No guessed claim classification. |

## Directory Rules basis

Because the object assesses evidence support and interpretation limits for a statistic, it belongs in the evidence contract family. Shape, fixtures, validator, tests, workflow, source mapping, and generated receipt remain in established responsibility roots under the accepted Directory Rules at `docs/doctrine/directory-rules.md` and ADR-0029. No new root or parallel analytic, causal, evidence, policy, review, release, or publication authority is introduced.

## Deferred questions

- Which accepted authority may define sufficient causal-design evidence by domain?
- Which claim lexicon and review workflow should classify real text without exposing sensitive content?
- Which analytical-method registry, if any, may resolve method identity and version?
- Which accepted reader surface may present a reviewed association explanation?
- How should multiple-testing, spatial autocorrelation, uncertainty, confounding, and effect size be composed without duplicating existing assessments?

These questions require separate decisions. This profile fixes none of them.

## Validation and rollback

Focused validation covers closed schema shape, deterministic identity, four correlation-method kinds, composition-reference abstention, role/wording alignment, causal-design declaration consistency, association caveats, public/release-review prerequisites, stronger-role abstention, unsupported causal denial, canonical references, hash tampering, and unknown-field rejection.

Rollback is a focused revert of this additive packet. No analysis rerun, evidence correction, release withdrawal, cache invalidation, UI cleanup, or public cleanup is required because the profile has no consumer and changes no existing analytic or relation object.
