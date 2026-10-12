<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/pm25-trigger-candidate-assessment
title: PM2.5 Trigger Candidate Assessment
type: semantic-contract
version: v0.1.0
status: proposed; fixture-first; no-network; non-regulatory
created: 2026-08-09
policy_label: internal; atmosphere; analytical-candidate; no-health-authority
source_ideas: [KFM-P32-IDEA-0012, KFM-P32-PROG-0009]
related:
  - ./PM25Observation.md
  - ./AtmosphereAirDecisionEnvelope.md
  - ../../../schemas/contracts/v1/domains/atmosphere/pm25_trigger_candidate_assessment.schema.json
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# PM2.5 Trigger Candidate Assessment

> **PROPOSED:** `PM25_TRIGGER_CANDIDATE_ASSESSMENT_V1` evaluates declared categorical PM2.5 threshold, trailing-median, freshness, quality, and evidence posture for one synthetic analytical candidate. It does not calculate a threshold, issue AQI or health advice, declare an event, evaluate regulatory compliance, or authorize release.

## Source adaptation

Pass 32 cards `KFM-P32-IDEA-0012` and `KFM-P32-PROG-0009` propose positive and negative PM2.5 trigger fixtures that fail closed when monitored thresholds, trailing medians, or evidence are incomplete. This profile implements only that local fixture boundary. It accepts no raw concentration, numeric threshold, coordinates, station identity, patient data, or live source response.

## Finite outcomes

| Assessment | Local meaning |
|---|---|
| `PROPOSED_TRIGGER_CANDIDATE` | Both declared comparisons are above their separately governed references, the observation is fresh and quality-acceptable, and two or more distinct EvidenceRefs are present. |
| `NO_TRIGGER_CANDIDATE` | At least one declared comparison is at or below its reference while integrity remains clear. |
| `HOLD` | A comparison, freshness, quality, or source state is unknown or unsuitable. |
| `ERROR` | The supplied upstream state explicitly failed. |

Validator `PASS` means only that a proposed/no-trigger packet is internally coherent. `ABSTAIN` preserves `HOLD`; `ERROR` preserves upstream failure; and `DENY` rejects malformed, inconsistent, unsupported, identity-drifted, or authority-overreaching packets.

## Anti-collapse rules

- `OBSERVED_SENSOR` is the only admitted knowledge character. AQI reports, model fields, AOD, smoke masks, and advisories cannot be treated as PM2.5 concentration observations.
- The observation and trailing-median references are distinct.
- A proposed trigger requires at least two distinct EvidenceRefs.
- No numeric concentration, threshold, median, or health category is admitted.
- All authority-bearing flags are fixed false.
- The profile cannot mutate detector configuration or write any lifecycle lane.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the packet excluding `assessment_id` and `spec_hash`.

```text
spec_hash     = SHA-256(JCS(identity subject))
assessment_id = "kfm:pm25-trigger-candidate:" + first 24 digest hex characters
```

## Directory Rules basis

Atmosphere meaning remains in `contracts/domains/atmosphere/`; machine shape in `schemas/contracts/v1/domains/atmosphere/`; synthetic cases in `fixtures/contracts/v1/domains/atmosphere/`; validation in `tools/validators/domains/atmosphere/`; tests in `tests/domains/atmosphere/`; CI in `.github/workflows/`; source mapping in `docs/intake/exploratory/`; and authoring accountability in `data/receipts/generated/`. These are existing responsibility roots under accepted ADR-0029.

## Rollback

Close the draft or revert the additive packet. No live source, detector, evidence object, policy decision, release, deployment, or public artifact requires restoration.
