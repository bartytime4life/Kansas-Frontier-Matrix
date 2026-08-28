<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/correctable-environmental-event-assessment
title: Correctable Environmental Event Lifecycle Assessment
type: semantic-contract
version: v0.1.0
status: proposed; fixture-only; no-network; non-regulatory
owners: OWNER_TBD — Atmosphere steward · Evidence steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; atmosphere; event-lifecycle; correction; no-public-authority
owning_root: contracts/
responsibility: Prove that synthetic observation, candidate, review disposition, event, and correction identities and transitions remain distinct without declaring or publishing a real-world event.
truth_posture: PROPOSED contract / CONFIRMED deterministic synthetic implementation / NEEDS VERIFICATION steward approval and operational integration
related:
  - ../../../schemas/contracts/v1/domains/atmosphere/correctable_environmental_event_assessment.schema.json
  - ../../../fixtures/contracts/v1/domains/atmosphere/correctable_environmental_event_assessment/cases.json
  - ../../../tools/validators/domains/atmosphere/validate_correctable_environmental_event_assessment.py
  - ../../../docs/intake/exploratory/correctable-environmental-event-lifecycle-source-map.md
  - ./pm25_trigger_candidate_assessment.md
tags: [kfm, atmosphere, observation, candidate, event, correction, anti-collapse]
notes:
  - "PASS proves only supplied synthetic lifecycle coherence; it is not an event, review, policy, alert, release, or publication decision."
[/KFM_META_BLOCK_V2] -->

# Correctable environmental-event lifecycle assessment

## Status and purpose

`CORRECTABLE_ENVIRONMENTAL_EVENT_ASSESSMENT_V1` is a **PROPOSED**, fixture-only profile for proving `Observation -> Candidate -> Review disposition -> Event -> Correction` anti-collapse behavior. It consumes declared references and source roles; it does not read a live feed, calculate a threshold, promote a candidate, approve a review, declare a real-world event, apply a correction, issue an alert, or publish anything.

## Lifecycle distinctions

- An observation is source-bound and time-bound evidence, not an event.
- A candidate cites one or more observations and a separately identified baseline snapshot.
- An event transition cites the candidate, a distinct review-disposition record, and distinct observation, baseline, and corroboration source roles.
- A correction cites the event it corrects and a distinct replacement event identity.
- Source identities cannot occupy multiple roles, and lifecycle identities cannot collapse into one another.
- Transition times are monotonic and explicitly timezone-aware.

## Finite outcomes

| Validator outcome | Assessment outcome | Meaning |
|---|---|---|
| `PASS` | `EVENT_CHAIN_CONFIRMED` | The supplied synthetic observation-to-event chain is coherent. |
| `PASS` | `CORRECTION_CHAIN_CONFIRMED` | The supplied synthetic chain carries coherent correction and replacement lineage. |
| `ABSTAIN` | `HOLD` | The packet remains candidate-only, stale, unknown, or otherwise unsuitable for a chain claim. |
| `DENY` | validation finding | Shape, role composition, scope, reference, time, report, or deterministic identity is inconsistent. |
| `ERROR` | `ERROR` | The supplied upstream state explicitly failed or input cannot be safely read. |

## Anti-collapse and authority boundary

The profile admits no concentration, threshold, AQI, health category, coordinates, person identity, or live service response. A declared review-disposition reference is an input identity, not approval by this validator. A synthetic event or correction reference is not a real-world assertion. Every authority-bearing governance flag is fixed false.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the packet excluding `assessment_id` and `spec_hash`.

```text
spec_hash     = SHA-256(JCS(identity subject))
assessment_id = "kfm:correctable-event:" + first 24 digest hex characters
```

## Directory Rules basis and rollback

Atmosphere meaning remains in `contracts/domains/atmosphere/`; machine shape in `schemas/contracts/v1/domains/atmosphere/`; synthetic cases in `fixtures/contracts/v1/domains/atmosphere/`; validation in `tools/validators/domains/atmosphere/`; tests in `tests/domains/atmosphere/`; CI in `.github/workflows/`; source mapping in `docs/intake/exploratory/`; and process memory in `data/receipts/generated/`. These are existing responsibility roots under accepted ADR-0029.

Rollback is an ordinary revert of this additive packet. No source, observation, candidate, event, correction, policy decision, release, deployment, alert, or publication state requires restoration.
