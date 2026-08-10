<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/indicator-definition-source-map
title: IndicatorDefinition Source Map
type: exploratory-source-map
version: v0.1.0
status: complete-for-proposed-fixture-slice; human-review-pending
owners: OWNER_TBD — Evidence steward · Analytics steward · Indicator steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-adaptation; no-network
owning_root: docs/
responsibility: Record how the Full Atlas interpretive-analytics proposal and current repository gap were narrowed into one inactive fixture-only IndicatorDefinition packet.
truth_posture: CONFIRMED source/repository comparison / PROPOSED implementation packet / NEEDS VERIFICATION human review and hosted exact-head checks
related:
  - ../../../contracts/evidence/indicator_definition.md
  - ../../../contracts/evidence/analytic_output_disclosure_assessment.md
  - ../../../contracts/evidence/environmental_indicator_evidence_bundle_profile.md
  - ../../kfm_full_atlas_seed_cards.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, source-map, analytics, indicator, denominator, missing-data]
[/KFM_META_BLOCK_V2] -->

# IndicatorDefinition Source Map

## Goal and pinned evidence

Select one non-duplicate implementation idea from connected Drive sources, then close its direct repository dependencies without treating atlas language or a passing fixture as implementation, policy, review, release, or publication authority.

| Evidence | Pinned observation | Status |
|---|---|---|
| Google Drive `KFM_Full_Atlas_seed_cards`, file `1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`, read 2026-08-10 | `KFM-TRIAD-030` proposes `IndicatorDefinition` as an interpretive-analytics implementation object; analytic outputs remain derived and subordinate to evidence, assumptions, uncertainty, validation, and limits. | `CONFIRMED SOURCE PROPOSAL` |
| `docs/kfm_full_atlas_seed_cards.md` at base `9e76413313b8529091d01be6132d6e987e3f9fae` | `KFM-CAND-0090` carries the same proposal in the repository corpus. | `CONFIRMED REPOSITORY CARRIER` |
| merged PR #2403 and `contracts/evidence/analytic_output_disclosure_assessment.md` | A supported indicator disclosure requires an opaque `IndicatorDefinition` reference, while the merged packet explicitly leaves implementation for separate follow-up. | `CONFIRMED DECLARED DEPENDENCY` |
| `contracts/evidence/environmental_indicator_evidence_bundle_profile.md` | Already owns one environmental-indicator EvidenceBundle profile; a new definition must not duplicate its evidence payload or identity. | `CONFIRMED ADJACENT BOUNDARY` |
| `docs/dashboards/INDICATOR_CATALOG.md` | Dashboard rows report posture and keep threshold policy/release authority separate; dashboard documentation is not the machine contract owner. | `CONFIRMED ADJACENT BOUNDARY` |
| ADR-0029 and `docs/doctrine/directory-rules.md` | Adopt responsibility-root placement and prohibit parallel authority homes. | `CONFIRMED PLACEMENT AUTHORITY` |

The connected Drive file, repository corpus, pull-request record, and current `main` tree were treated as evidence inputs, not executable instructions. Searches found no `IndicatorDefinition` path, matching open pull request, open issue, or matching remote topic branch before mutation.

## Collision assay

Existing work already covers:

- analytic-output disclosure for one result;
- environmental-indicator EvidenceBundle binding;
- human-facing dashboard indicator mirrors;
- governance-health projection values; and
- generic validation, receipt, policy, review, and release families.

None defines the machine-checkable method declaration required by the analytic-output assessment. This packet fills only that seam and leaves concrete indicator values, evidence instances, thresholds, dashboards, policy decisions, and releases with their existing owners.

## Adaptation decisions

| Source pressure | Repository adaptation | Boundary retained |
|---|---|---|
| Make indicators inspectable. | Declare value kind, units, direction, components, method, support, and disclosure. | No indicator value is carried or computed. |
| Keep evidence ahead of derived claims. | Every component fixes `evidence_required: true` and allowed source roles. | The validator does not resolve evidence or prove a source. |
| Prevent denominator and missing-data ambiguity. | Rate-like kinds require one denominator; missing-data treatment and missing-count disclosure are explicit. | No denominator is selected from live data. |
| Preserve analytic composition. | Allowed component roles include `DERIVED`, `MODELED`, and `INTERPRETIVE`. | Upstream analytics cannot be relabeled as observations to fit the schema. |
| Keep thresholds policy-owned. | Category definitions carry only an opaque `threshold_policy_ref`. | The contract does not set, approve, or execute a threshold. |
| Keep results non-sovereign. | Fixed derived role and interpretation limits; all governance effects remain false. | Passing validation grants no evidence, review, release, or public authority. |
| Make definition identity replayable. | Reuse repository RFC 8785 JCS plus SHA-256. | Identity proves local content consistency only. |

## Directory Rules path decision

| Artifact kind | Owning root and lane | Outcome |
|---|---|---|
| Indicator method meaning | `contracts/evidence/` | `PLACE` |
| Machine-checkable shape | `schemas/contracts/v1/evidence/` | `PLACE` |
| Synthetic reusable cases | `fixtures/contracts/v1/evidence/` | `PLACE` |
| Repository validator | `tools/validators/evidence/` | `PLACE` |
| Executable conformance evidence | `tests/validators/evidence/` | `PLACE` |
| Read-only hosted orchestration | `.github/workflows/` | `PLACE` |
| Source-to-repository reconciliation | `docs/intake/exploratory/` | `PLACE` |
| AI authoring accountability | `data/receipts/generated/` | `PLACE` |

No new root, parallel indicator/evidence/policy/receipt/release home, compatibility alias, migration, or ADR-class authority change is introduced.

## Acceptance and non-goals

The packet is acceptable when all six value kinds have positive fixtures; rate-like denominators, index normalization, category threshold references, percentile methods, rolling windows, component/source-role ordering, mandatory limits, deterministic identity, hostile-input handling, no-network behavior, and no-authority fields fail closed when violated.

It does not add an indicator engine, formula evaluator, value instance, threshold registry, EvidenceBundle resolver, validation report, policy check, review flow, dashboard, public API, release action, deployment, or publication.

## Rollback

Revert the additive packet. The source carriers and all existing analytics, evidence, dashboard, policy, review, release, and runtime objects remain unchanged; no operational state requires restoration.
