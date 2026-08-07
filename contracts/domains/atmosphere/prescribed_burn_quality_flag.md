<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/atmosphere/prescribed-burn-quality-flag
title: Prescribed-Burn Air-Quality Context Flag
type: semantic-contract
version: v1
status: proposed
owners: [atmosphere-domain-steward]
created: 2026-08-07
policy_label: internal
related:
  - schemas/contracts/v1/domains/atmosphere/prescribed_burn_quality_flag.schema.json
  - tools/validators/domains/atmosphere/validate_prescribed_burn_quality_flag.py
  - fixtures/contracts/v1/domains/atmosphere/prescribed_burn_quality_flag/
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
source_ideas:
  - KFM-P25-PROG-0003
truth_posture: cite-or-abstain
[/KFM_META_BLOCK_V2] -->

# Prescribed-Burn Air-Quality Context Flag

## Purpose

`PrescribedBurnQualityFlag` is a **fixture-first contextual quality assessment** for an
observed PM2.5 or AQI record and a separately evidenced smoke context. It records whether
downstream detector or model-training use should remain flagged, be suppressed, be held, or
proceed without a smoke flag.

The contract implements the source idea `KFM-P25-PROG-0003`: mark air-quality
observations affected or potentially affected by prescribed-burn smoke before they feed
detectors or model training.

It does **not** claim that a burn caused a measured concentration. An air-quality observation
remains direct measurement evidence; smoke or burn information remains contextual evidence.

## Authority boundary

- `OBSERVATION` must map to `DIRECT_MEASUREMENT`.
- `CONTEXT` must map to `CONTEXT_ONLY`.
- A contextual assessment may return `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.
- A causal request must return `DENY`.
- `ANSWER` can support a contextual smoke flag, but cannot create an emergency advisory,
  policy decision, release decision, or publication authority.
- The validator performs no network, dispersion, plume, meteorological, or spatial computation.
  Spatial and temporal relations are supplied as reviewed inputs and checked for coherent use.

## Required fields

| Field | Meaning |
|---|---|
| `flag_id` | Deterministic ID derived from the canonical packet excluding `flag_id` and `spec_hash`. |
| `schema_version` | `v1`. |
| `requested_claim_type` | `CONTEXTUAL` or `CAUSAL`. |
| `observation` | PM2.5/AQI observation reference, time, place, role, support type, and evidence. |
| `smoke_context` | Smoke-context reference, event type, time window, place, role, support type, and evidence. |
| `assessment` | Finite outcome, declared relations, influence status, downstream dispositions, reasons, and evidence closure. |
| `governance` | Explicit anti-collapse and non-authority boundary. |
| `spec_hash` | Canonical packet digest. |

## Finite outcomes

| Outcome | Required semantics |
|---|---|
| `ANSWER` | Contextual request only; space/time are resolved; evidence closure is complete. |
| `ABSTAIN` | Spatial, temporal, or influence status remains unresolved. Downstream uses are held. |
| `DENY` | Causal assertion requested or a protected scope is blocked. |
| `ERROR` | Operational failure; all relation and use fields remain `UNKNOWN`. |

## Influence and downstream controls

| Influence status | Detector disposition | Model-training disposition |
|---|---|---|
| `SUPPORTED_CONTEXT` | `SUPPRESS_EVENT_CALLING` | `EXCLUDE` |
| `POSSIBLE_CONTEXT` | `ALLOW_WITH_FLAG` | `INCLUDE_WITH_FLAG` |
| `NOT_SUPPORTED` | `ALLOW_UNFLAGGED` | `INCLUDE_UNFLAGGED` |
| `UNRESOLVED` | `HOLD` | `HOLD` |
| `UNKNOWN` | `UNKNOWN` | `UNKNOWN` |

These are **review recommendations**, not direct mutations of detector or training
configuration.

## Deterministic validation

```bash
python tools/validators/domains/atmosphere/validate_prescribed_burn_quality_flag.py \
  fixtures/contracts/v1/domains/atmosphere/prescribed_burn_quality_flag/valid/supported_context_answer.json

pytest -q tests/domains/atmosphere/test_prescribed_burn_quality_flag.py
```

## Non-goals

This contract does not:

- fetch KDHE, AirNow, AQS, HMS, VIIRS, HRRR-Smoke, or burn-permit data;
- infer plume transport or causality;
- issue public-health guidance;
- suppress a production detector or alter a model-training corpus;
- evaluate rights, sensitivity, policy, promotion, release, deployment, or publication.
