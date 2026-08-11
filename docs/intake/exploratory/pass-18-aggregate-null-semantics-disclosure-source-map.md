<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-aggregate-null-semantics-disclosure
title: Pass 18 Aggregate NULL-Semantics Disclosure Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Analytics steward · Data-quality steward · Common contract steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; analytics; aggregate; null-semantics; data-quality
responsibility: Preserve source and repository lineage for a bounded aggregate NULL-semantics disclosure without turning a declaration into a metric value, data-quality finding, evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED attached-card transcription, visual review, Drive metadata, and inspected-repository comparison; PROPOSED bounded adaptation; UNKNOWN cross-engine parity and consumer adoption; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/common/aggregate_null_semantics_disclosure.md
  - ../../../contracts/common/aggregate_statistic.md
  - ../../../contracts/common/aggregate_grouping_disclosure.md
  - ../../../contracts/evidence/count_population_disclosure.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Aggregate NULL-Semantics Disclosure Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical PDF pages 280-281 / printed pages 277-278 | Card `KFM-P18-INV-430` proposes disclosing NULL treatment for counts, distinct counts, averages, and grouped summaries; it identifies data-quality report, SQL receipt, missingness profile, and validator dependencies. Both pages were rendered and visually inspected. | `CONFIRMED` |
| Connected Drive `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` (`1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5`) | Drive metadata confirms the named Pass 18 dossier is present. Byte identity with the supplied attachment was not asserted. | `CONFIRMED` metadata only |
| Connected Drive `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) | The seed corpus preserves fixture validation, review, release, correction, and rollback boundaries for proposed analytic records. | `CONFIRMED` thematic corroboration |
| `contracts/evidence/count_population_disclosure.md` | The existing family owns whether counts describe rows, non-null values, distinct tuples, grouped rows, or filtered populations. | `CONFIRMED` composed responsibility |
| `contracts/common/aggregate_grouping_disclosure.md` | The existing family owns detail, subtotal, grand-total, grouping-mask, and source-null-versus-rollup row roles. | `CONFIRMED` adjacent, non-duplicate responsibility |
| `contracts/common/aggregate_statistic.md` and `contracts/common/missing_value_filter_receipt.md` | Existing objects identify aggregate and missing-data behavior but do not provide the proposed report-side cross-aggregate NULL and empty-input disclosure. | `CONFIRMED` bounded gap |
| Starting `main@fa244eb7bd11d8ff96e91f4925ca8abc5bdaa9fe` plus GitHub PR, code, and branch searches | No exact card ID, aggregate NULL-semantics contract, schema, fixture family, validator, workflow, branch, or open PR was found before implementation. | `CONFIRMED` inspected snapshot |

The source artifacts are design evidence, not repository instruction authority.
Placement and scope follow accepted Directory Rules and current responsibility
roots.

## Selected increment

The implementation is a small, additive `contracts/common/` disclosure value
object. It records one aggregate kind, value and grouping fields, input-value
NULL treatment, group-key NULL treatment, empty-input result, and adjacent
opaque references. It stores no SQL, rows, imputed values, or metric values.

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Distinguish row counts, value counts, and distinct counts. | Closed aggregate-kind vocabulary plus a required reference to the existing count-population disclosure. | No duplicated population schema or count computation. |
| Make aggregate input NULL behavior visible. | Declare included-row, excluded, imputed, error, or unresolved posture. | No row inspection, imputation, or statistical endorsement. |
| Make grouped NULL behavior visible. | Declare own-group, row-excluded, error, unresolved, or not-grouped posture. | No replacement of subtotal and rollup semantics. |
| Expose empty-input behavior. | Declare zero, null, no-result, error, or unresolved, with kind-specific coherence checks. | No query execution or numeric-result claim. |
| Preserve data-quality review context. | Opaque query-receipt, missingness-profile, aggregate-statistic, report, disclosure, and review references. | No reference authentication, evidence resolution, review approval, or public authority. |

## Directory Rules basis

The artifact has one authority owner: reusable cross-domain aggregate NULL
semantics. It therefore uses the existing common-contract responsibility root,
with shape, fixtures, validator, tests, workflow, source map, and generated
receipt in their established roots. No parallel analytics, data-quality,
missingness, evidence, policy, release, or publication home is created.

## Deferred questions

- Which additional aggregate functions require mandatory NULL-semantics disclosure?
- Whether adopted report schemas embed this object or reference it remains undecided.
- Cross-engine equivalence, production report placement, and public wording require separate reviewed authority.

## Rollback

Rollback is a focused revert of the additive packet. No query rerun, metric
correction, data restoration, release withdrawal, cache invalidation, or public
cleanup is required because the profile is inactive and has no consumer.
