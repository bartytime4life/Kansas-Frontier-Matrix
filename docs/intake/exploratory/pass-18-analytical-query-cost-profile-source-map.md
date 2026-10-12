<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-analytical-query-cost-profile
title: Pass 18 Analytical Query Cost Profile Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Analytics steward · Common contract steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; analytics; query-cost; reproducibility
responsibility: Preserve source and repository lineage for a bounded analytical query-cost profile without turning resource observations into evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED attached-card transcription, visual review, Drive metadata, and inspected-repository comparison; PROPOSED bounded adaptation; UNKNOWN engine portability; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/common/analytical_query_cost_profile.md
  - ../../../contracts/common/rolling_metric_window_disclosure.md
  - ../../../contracts/evidence/analytic_output_disclosure_assessment.md
  - ../../../contracts/governance/query_run_record.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Analytical Query Cost Profile Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical PDF pages 274-275 / printed pages 271-272 | Card `KFM-P18-INV-406` proposes recording performance assumptions, indexes, input-size budgets, plan identity, and cost posture when analytical runtime affects repeatability or operational cost. Both pages were rendered and visually inspected. | `CONFIRMED` |
| Connected Drive `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` (`1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5`) | Drive metadata confirms the named Pass 18 dossier is present. Byte identity with the supplied attachment was not asserted. | `CONFIRMED` metadata only |
| Connected Drive `KFM_Full_Atlas_seed_cards` (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`) | The seed corpus preserves fixture validation, review, release, correction, and rollback boundaries for proposed analytic records. | `CONFIRMED` thematic corroboration |
| `contracts/governance/query_run_record.md` | The existing query-run family records a governed AI/control-loop query iteration and explicitly omits raw prompts and authority effects; it does not record analytical execution budgets. | `CONFIRMED` adjacent, non-duplicate family |
| `contracts/evidence/analytic_output_disclosure_assessment.md` and `contracts/common/rolling_metric_window_disclosure.md` | Existing profiles disclose output support and rolling-window semantics but do not bind plan identity, input size, index assumptions, and observed resource ceilings. | `CONFIRMED` bounded gap |
| Starting `main@fa244eb7bd11d8ff96e91f4925ca8abc5bdaa9fe` plus GitHub PR/code searches | No exact card ID, analytical query-cost contract, schema, fixture family, validator, workflow, branch, or PR was found before implementation. | `CONFIRMED` inspected snapshot |

The source artifacts are design evidence, not repository instruction authority.
Placement and scope follow accepted Directory Rules and current responsibility
roots.

## Selected increment

The implementation is a small, additive `contracts/common/` disclosure value
object. It binds an opaque query reference and digest to safe engine, input,
plan, index, resource-budget, observation, and review declarations. It stores no
SQL, parameter values, connection details, plan text, table paths, or vendor
billing data.

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Record plan assumptions. | Capture class plus SHA-256 plan digest and fixed-false raw-plan/raw-SQL flags. | No plan collection, parsing, or authentication. |
| Record data-size assumptions. | Sorted dataset references and row/byte estimates with an explicit basis. | No dataset inspection or evidence resolution. |
| Record index assumptions. | Logical names, fields, access kinds, and budget dependency flags. | No database catalog lookup or index recommendation. |
| Record time, cost, and infrastructure constraints. | Portable duration, rows-read, bytes-read, and peak-memory ceilings; optional opaque billing-profile reference. | No vendor pricing, production threshold, or automatic gate. |
| Keep measured results reviewable. | Opaque run/telemetry references and a validator-derived within-budget or exceeded result. | No telemetry authentication, policy, review, promotion, or release decision. |

## Directory Rules basis

The artifact has one authority owner: reusable cross-domain disclosure
semantics. It therefore uses the existing common-contract responsibility root,
with shape, fixtures, validator, tests, workflow, source map, and generated
receipt in their established roots. No parallel query, analytics, telemetry,
budget, evidence, policy, release, or publication home is created.

## Deferred questions

- Which query-plan signals are stable enough to compare across engines?
- Whether an adopted analytical run receipt embeds this profile or references it remains undecided.
- Production budgets, billing units, telemetry sources, and public disclosure placement require separate reviewed authority.

## Rollback

Rollback is a focused revert of the additive packet. No query rerun, data
correction, release withdrawal, cache invalidation, or public cleanup is
required because the profile is inactive and has no consumer.
