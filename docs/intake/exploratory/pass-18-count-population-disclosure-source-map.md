<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-count-population-disclosure
title: Pass 18 Count Population Disclosure Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Evidence steward · Analytics steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; analytics; count; population
responsibility: Preserve source and repository lineage for a bounded count-population disclosure adaptation without promoting proposal material into metric, evidence, policy, release, or publication authority.
truth_posture: "CONFIRMED attached-card transcription, visual review, Drive discovery, and inspected-repository comparison; PROPOSED bounded adaptation; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/evidence/count_population_disclosure.md
  - ../../../contracts/evidence/indicator_definition.md
  - ../../../contracts/evidence/analytic_output_disclosure_assessment.md
  - ../../../contracts/common/aggregate_statistic.md
  - ../../../schemas/contracts/v1/evidence/count_population_disclosure.schema.json
  - ../../../fixtures/contracts/v1/evidence/count_population_disclosure/cases.json
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Count Population Disclosure Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical page 236 / printed page 233 | Card `KFM-P18-INV-157` proposes that public counts disclose whether they include all rows, non-null values, distinct values, grouped rows, or filtered subsets. The page was rendered and visually checked. | `CONFIRMED` |
| Connected Drive `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` (`1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5`) | Drive metadata confirms the named Pass 18 dossier is present. Byte identity with the supplied attachment was not asserted. | `CONFIRMED` metadata only |
| Connected Drive `Kansas Frontier Matrix — Connected-Dots Architecture Brief` (`1sdiLNDLFr2cVD3Q8h3ZvHO4D96WLJ6V7vf5neNzEyTM`) | The brief keeps indicators and analytical products derivative, with inputs, uncertainty, methods, and release posture visible. | `CONFIRMED` thematic corroboration |
| `main@b67b98cff3a8dbc7d0cc5548a26ae97d00c92847` | Current repository and GitHub searches found `IndicatorDefinition`, `AggregateStatistic`, rolling-window, and analytic-output disclosure profiles, but no count-population disclosure contract, schema, fixture family, validator, workflow, branch, or PR. | `CONFIRMED` for the inspected snapshot |

The source artifacts are proposal evidence, not repository instruction authority. Repository placement and scope follow accepted Directory Rules and current responsibility-root evidence.

## Reconciliation and selected increment

The current repository already defines indicator methods, aggregate-statistic posture, and analytic-output disclosure. None records whether a count is row-based, non-null, distinct, grouped, or filtered. Modifying those existing objects would enlarge compatibility and migration risk.

The selected increment is one additive disclosure candidate that composes existing metric, query-receipt, and evidence families by pinned reference. It records the eligible count population without carrying a computed value or changing any existing contract.

## Source-to-profile mapping

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Distinguish `COUNT(*)` from non-null value counts. | Closed `ROWS` and `NON_NULL_VALUES` kinds with coherent field and null posture. | No SQL execution or row inspection. |
| Disclose distinct and multi-column uniqueness. | Sorted `distinct_fields` and `DISTINCT_VALUE_TUPLES` population basis. | No identity reconciliation or deduplication. |
| Disclose grouping. | Sorted `group_by_fields` and `GROUPED_OUTPUT_ROWS` population basis. | No group calculation or metric registry mutation. |
| Disclose filtered subsets. | Separate filter state plus opaque predicate reference. | No predicate evaluation or query-receipt authentication. |
| Keep public interpretation reviewable. | Population note, details surface, and review references for public candidates. | No evidence, review, release, or publication authority. |

## Directory Rules basis

Semantic meaning is placed beside the evidence/analytics contracts it qualifies. Shape, fixtures, validator, tests, workflow, source map, and generated receipt stay in their established responsibility roots. No new root or parallel metric, query, evidence, policy, release, or publication authority is introduced.

## Deferred questions

- Which public surfaces should show the population note inline rather than through the Evidence Drawer?
- Whether a later compatible `IndicatorDefinition` or analytic receipt version embeds this disclosure or references it remains undecided.
- SQL-engine-specific behavior remains a separate dialect-verification responsibility.

## Validation and rollback

Focused validation covers closed shape, deterministic identity, UTC timestamps, canonical arrays, count-kind/field/null/population coherence, filter-reference coherence, public notes and review references, unresolved abstention, malformed Unicode, and unknown-field rejection.

Rollback is a focused revert of the additive packet. No recomputation, correction notice, release withdrawal, cache invalidation, UI cleanup, or public-artifact cleanup is required because the profile has no consumer and carries no metric value.
