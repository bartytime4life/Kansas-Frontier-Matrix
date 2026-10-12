<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/correctable-environmental-event-lifecycle-source-map
title: Correctable Environmental Event Lifecycle - Source Map and Implementation Boundary
type: exploratory-intake-source-map
version: v0.1.0
status: promoted-to-fixture-candidate; non-authoritative; repository-grounded
owners: OWNER_TBD — Intake steward · Atmosphere steward · Evidence steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; intake; atmosphere; event-lifecycle; correction; cite-or-abstain
owning_root: docs/
responsibility: Preserve traceability from the Drive idea corpus and governed Atlas triad to one synthetic correctable-event lifecycle fixture family without creating live-event, alert, policy, review, release, or publication authority.
truth_posture: CONFIRMED source lineage and current-main collision review / PROPOSED bounded adaptation / NEEDS VERIFICATION steward approval and later-main collisions
related:
  - ./new-ideas-4-16-source-map.md
  - ../../kfm_full_atlas_seed_cards.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/domains/atmosphere/correctable_environmental_event_assessment.md
tags: [kfm, intake, atmosphere, observation, candidate, event, correction]
[/KFM_META_BLOCK_V2] -->

# Correctable environmental-event lifecycle - source map

## Outcome

The Google Drive document *New Ideas 4-16-26* contributes air-quality baselining, anomaly, corroboration, and correction pressure. The governed repository synthesis narrows that material into `KFM-TRIAD-035`: observations, candidates, review dispositions, events, and corrections must remain distinct time-aware states. This packet implements only synthetic no-network lifecycle conformance.

## Source lineage

| Source | Relevant pressure | Posture used here |
|---|---|---|
| Google Drive `New Ideas 4-16-26` (`1IqoqVHWERGK8VtLSUX69VBBmFNXqS62xBC2HE380Jrc`) | Historical observations, baselines, anomaly candidates, corroborating sources, and correction-ready process memory. | Design pressure only; source and health claims are not carried forward. |
| `docs/intake/exploratory/new-ideas-4-16-source-map.md` | Classifies the correctable environmental-event lifecycle as a repository gap and recommends synthetic `Observation -> Candidate -> Event -> Correction` semantics first. | Repository routing authority for the bounded next step. |
| `docs/kfm_full_atlas_seed_cards.md` | `KFM-TRIAD-035` and `KFM-CAND-0105` require distinct lifecycle objects, transition guards, baseline and evidence refs, corrections, and withdrawal lineage. | Governed candidate lineage; this first slice implements correction, not withdrawal. |
| Existing Atmosphere contracts | PM2.5 candidate, observation, knowledge-character, and source-role profiles already constrain upstream meaning. | Reused ownership and anti-collapse boundaries; no duplicate observation or trigger authority. |
| Directory Rules and accepted ADR-0029 | Responsibility-root placement and no-parallel-authority rules. | Placement authority. |

## Current-main collision review

The inspected tree at `main@52675a800825c071ddc9df9476b543c49d73efd8` contains Atmosphere observations, source reconciliation, PM2.5 trigger candidates, anomaly and knowledge-character profiles, correction and rollback infrastructure in other lanes, and event-adjacent documents. No contract, schema, fixture family, validator, test, or workflow was found that proves one synthetic observation/candidate/review/event/correction chain with distinct references, baseline identity, source-role composition, freshness outcomes, correction target, replacement identity, and monotonic time guards. This finding is **CONFIRMED for that inspected tree**, not timeless.

## Bounded adaptation

The packet accepts reference-only synthetic lifecycle packets. Candidate-only and stale packets hold; coherent event and corrected-event packets pass; source-role collapse, missing corroboration, reference collapse, correction-target drift, time reversal, scope mismatch, report drift, identity drift, and authority overreach deny.

It contains no raw concentration, threshold, AQI, coordinates, live source call, candidate promotion, review approval, real-world event declaration, applied correction, withdrawal, alert, health advice, regulatory decision, policy, release, deployment, publication, or public-use authority.

## Directory placement

| Responsibility | Path |
|---|---|
| Atmosphere semantic meaning | `contracts/domains/atmosphere/correctable_environmental_event_assessment.md` |
| Canonical machine shape | `schemas/contracts/v1/domains/atmosphere/correctable_environmental_event_assessment.schema.json` |
| Reusable synthetic inputs | `fixtures/contracts/v1/domains/atmosphere/correctable_environmental_event_assessment/cases.json` |
| Atmosphere validator | `tools/validators/domains/atmosphere/validate_correctable_environmental_event_assessment.py` |
| Executable evidence | `tests/domains/atmosphere/test_correctable_environmental_event_assessment.py` |
| Hosted orchestration | `.github/workflows/correctable-environmental-event-assessment.yml` |
| Human source adaptation | This file under `docs/intake/exploratory/` |
| AI-authoring process memory | `data/receipts/generated/` |

## Verification and rollback

Atmosphere, evidence, policy, review, and release stewards must still decide how real source records, thresholds, spatial scope, persistence, confidence, review dispositions, withdrawal, correction application, public alerts, and release controls bind to these identities. Rollback is an ordinary revert of this additive packet; it changes no live environmental or publication state.
