<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/observation-fitness-assessment
title: ObservationFitnessAssessment Contract
type: contract
version: v0.1.0
status: proposed; fixture-first; local-only; non-authoritative
owners: OWNER_TBD — evidence steward; analysis steward; domain quality steward; validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: repository-facing; fitness-for-use; confounder-exclusion; fail-closed
owning_root: contracts/
responsibility: Determine whether one retained observation is fit for one declared analysis use while preserving exclusion reasons, context, and correction lineage.
truth_posture: cite-or-abstain
related:
  - ../../schemas/contracts/v1/evidence/observation_fitness_assessment.schema.json
  - ../../tools/validators/evidence/validate_observation_fitness_assessment.py
  - ../../fixtures/contracts/v1/evidence/observation_fitness_assessment/cases.json
  - ../../tests/evidence/test_observation_fitness_assessment.py
  - ../../docs/intake/exploratory/full-atlas-observation-fitness-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "EXCLUDED means unfit for the declared use, not nonexistent, false, deleted, or globally unusable."
  - "The profile uses synthetic observations and candidate reason codes; domain adoption requires separate scientific and policy review."
[/KFM_META_BLOCK_V2] -->

# ObservationFitnessAssessment

> **Purpose.** Bind one observation, one declared analysis use, one versioned method, quality-mask state, confounder context, persistence support, and correction lineage to a finite fitness decision without discarding the underlying evidence.

## Source basis

Full Atlas `KFM-TRIAD-053` and programming card `KFM-CAND-0159` call for reusable observation-fitness decisions, context snapshots, exclusion receipts, deterministic profiles, and synthetic cloud, smoke, shadow, snow, missing-QA, single-observation, contradictory-context, stale-mask, and corrected-mask cases. This composite is the smallest dependency-closed implementation of that proposal. It does not adopt the source packet's candidate vegetation thresholds or activate a domain source.

## Finite states

| State | Handling | Required meaning |
|---|---|---|
| `FIT` | `INCLUDE` | Quality is current and passing, declared confounders are absent, and persistence support is present for this use. |
| `CONDITIONALLY_FIT` | `INCLUDE_WITH_QUALIFICATION` | Quality and confounder checks pass, but persistence is unsupported; single-observation limitations remain visible. |
| `EXCLUDED` | `RETAIN_AND_EXCLUDE` | A current confounder, failed quality check, or stale quality mask makes the observation unfit for this use. The evidence remains retained. |
| `UNKNOWN` | `ABSTAIN` | Quality, confounder, or persistence support cannot be resolved strongly enough to decide fitness. |

The validator derives the state, handling, reason codes, and obligations. A candidate cannot self-promote by editing stored decision fields.

## Preservation and correction rules

- `retained_evidence_refs` must exactly cover observation evidence plus quality, confounder, and persistence evidence used by the assessment.
- Confounder codes are unique within a context snapshot; contradictory duplicate states are denied instead of averaged.
- An `EXCLUDED` observation must carry `RETAIN_EXCLUDED_EVIDENCE`, `DISPLAY_EXCLUSION_REASON`, and `REASSESS_AFTER_CONTEXT_CORRECTION` obligations.
- A corrected assessment must identify the superseded assessment and at least one corrected mask. Correction creates a new assessment; it never rewrites the prior record.
- `spec_hash` is RFC 8785 JCS plus SHA-256 over the assessment with `assessment_id` and `spec_hash` omitted. `assessment_id` is `kfm:observation-fitness:<digest>`.

## Directory Rules basis

Meaning belongs in `contracts/evidence/`; shape in `schemas/contracts/v1/evidence/`; deterministic validation in `tools/validators/evidence/`; synthetic cases in `fixtures/contracts/v1/evidence/`; tests in `tests/evidence/`; provenance in `data/receipts/generated/`. These are accepted responsibility roots under ADR-0029; no parallel authority is introduced.

## Non-effects and rollback

This fixture-only profile performs no network access, changes no lifecycle data, deletes no observation, establishes no scientific threshold, and grants no truth, analysis, policy, review, release, publication, or public-use authority. Revert the bounded commit to remove it.
