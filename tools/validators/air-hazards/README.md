<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-air-hazards-readme
title: tools/validators/air-hazards README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-atmosphere-steward-plus-hazards-steward-plus-policy-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; cross-domain-validator; air-hazards; operational-context-aware
owning_root: tools/
responsibility: proposed cross-domain validator lane for Atmosphere/Air and Hazards knowledge-character, source-role, temporal, freshness, sensitivity, evidence, and release-boundary checks
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../docs/domains/hazards/ARCHITECTURE.md
  - ../../../contracts/domains/atmosphere/
  - ../../../contracts/hazards/
  - ../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../schemas/contracts/v1/hazards/
  - ../../../policy/domains/atmosphere/
  - ../../../policy/domains/hazards/
  - ../../../data/proofs/evidence_bundle/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README documents a proposed cross-domain validator lane. It does not confirm executable files."
  - "Air/Hazards validation must preserve Atmosphere/Air knowledge-character rules, Hazards source-role separation, freshness/expiry handling, evidence support, and public-boundary constraints."
  - "Validators enforce declared contracts, schemas, and policy. They do not define source roles, issue alerts, create EvidenceBundles, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/air-hazards

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-air--hazards--validators-informational)
![boundary](https://img.shields.io/badge/boundary-operational--context-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/air-hazards/` is the proposed cross-domain validator lane for checks that span Atmosphere/Air and Hazards: smoke, AOD, AQI, weather context, advisory context, fire-weather context, freshness/expiry, source-role separation, evidence support, and public-release boundaries.

---

## Purpose

`tools/validators/air-hazards/` exists for validator logic that is genuinely cross-domain between Atmosphere/Air and Hazards.

The durable KFM question for this lane is:

> Does an air/hazards candidate preserve the owning lane, source role, knowledge character, time/freshness state, sensitivity posture, evidence support, and release boundary before it reaches any governed output?

The answer should be a deterministic validation result. It should not create an observation, hazard event, alert, EvidenceBundle, policy decision, release decision, or map/API product.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/air-hazards/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Atmosphere/Air object roster | **CONFIRMED in repo evidence / draft** | Object-family map names air observations, AOD, smoke, model, advisory, and related object families. |
| Hazards architecture boundary | **CONFIRMED in repo evidence / draft** | Hazards cites Atmosphere/Air for smoke, heat/cold, AQI/advisory, wind, and fire-weather context while preserving ownership and source role. |
| Contract/schema paths | **PROPOSED / NEEDS VERIFICATION** | Atmosphere paths use `domains/atmosphere`; Hazards docs note schema-home tensions requiring verification. |
| Policy and release wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove CI or release gates are wired. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Cross-domain air/hazards validator entrypoints | `tools/validators/air-hazards/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Atmosphere/Air domain meaning | `docs/domains/atmosphere/`, `contracts/domains/atmosphere/` |
| Hazards domain meaning | `docs/domains/hazards/`, `contracts/hazards/` or accepted contracts home |
| Atmosphere/Air schemas | `schemas/contracts/v1/domains/atmosphere/` or accepted schema home |
| Hazards schemas | `schemas/contracts/v1/hazards/` or accepted schema home |
| Policy rules | `policy/domains/atmosphere/`, `policy/domains/hazards/`, or accepted policy homes |
| EvidenceBundles and receipts | `data/proofs/evidence_bundle/`, `data/receipts/` |
| Release records | `release/` |
| Tests and fixtures | `tests/validators/air-hazards/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it validates a cross-lane invariant and reads declared contracts, schemas, and policy.
- **NEEDS VERIFICATION:** exact executable names, schema homes, fixtures, policy bundles, source descriptors, and CI wiring.
- **DENY:** using this folder as a domain contract home, schema home, policy home, evidence store, source registry, release record store, or public runtime surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/air-hazards/` include checks that:

- preserve Atmosphere/Air ownership for smoke, AQI, AOD, weather, wind, temperature, and advisory context;
- preserve Hazards ownership for hazard event, warning/advisory context, exposure, resilience, and timeline objects;
- prevent AQI reports from being treated as raw concentration observations;
- prevent AOD or satellite masks from being treated as ground PM2.5 measurements;
- prevent modeled atmospheric fields from being treated as observed sensor readings;
- prevent remote-sensing fire/smoke detections from being treated as confirmed ground events without review;
- require issue/expiry/freshness state for operational-context objects;
- require EvidenceRef or EvidenceBundle support for public-bound claims;
- preserve sensitivity and generalization requirements for station, infrastructure, and impact-area context;
- enforce finite outcomes for governed-AI summaries over released evidence.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/air-hazards/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Atmosphere/Air contracts | `contracts/domains/atmosphere/` |
| Hazards contracts | `contracts/hazards/` or accepted contracts home |
| Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| Lifecycle data | dedicated `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, and `data/published` roots |
| EvidenceBundles or receipts | `data/proofs/`, `data/receipts/` |
| Release records | `release/` |
| Connectors or pipelines | `connectors/`, `pipelines/` |
| Tests and fixtures | `tests/` and `fixtures/` conventions |

[Back to top](#top)

---

## Cross-domain validation posture

This validator lane is for anti-collapse checks.

It should fail closed or return review-required outcomes when a candidate collapses:

- AQI into raw concentration;
- AOD into PM2.5;
- model field into observation;
- remote-sensing detection into confirmed event;
- operational context into official instruction;
- regulatory context into observed condition;
- stale or expired context into current state;
- Atmosphere-owned observations into Hazards-owned truth;
- Hazards-owned timelines into Atmosphere-owned sensor truth.

The validator must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `AIR_HAZARDS_VALIDATION_PASS` | Configured cross-domain checks passed. |
| `AIR_HAZARDS_VALIDATION_FAIL` | Configured checks failed. |
| `KNOWLEDGE_CHARACTER_COLLAPSE` | Candidate collapses AQI/AOD/model/observation/advisory meaning. |
| `SOURCE_ROLE_CONFLICT` | Candidate treats one source role as another. |
| `FRESHNESS_OR_EXPIRY_MISSING` | Required issue, expiry, retrieval, or freshness state is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SENSITIVITY_REVIEW_REQUIRED` | Public-bound output requires sensitivity review or generalization. |
| `PUBLIC_BOUNDARY_VIOLATION` | Candidate is not safe for public/governed output as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/air-hazards/
├── README.md
├── test_air_hazards_validators.py
└── fixtures/
    ├── valid_smoke_context/
    ├── aod_as_pm25_denied/
    ├── aqi_as_concentration_denied/
    ├── model_as_observation_denied/
    ├── missing_expiry/
    ├── remote_sensing_as_confirmed_event_denied/
    └── missing_evidence_ref/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/air-hazards
```

```bash
python tools/validators/air-hazards/validate_air_hazards_candidate.py --fixtures --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_air_hazards_candidate.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared contracts and schemas rather than defining shape locally.
- [ ] Validator reads declared policy posture rather than defining policy locally.
- [ ] Atmosphere/Air and Hazards ownership boundaries are preserved.
- [ ] Knowledge-character and source-role fields are explicit.
- [ ] Issue, expiry, retrieval, valid, release, and correction times are not collapsed where material.
- [ ] Public-bound claims require EvidenceRef or EvidenceBundle support.
- [ ] Sensitive geometry or infrastructure context is generalized or routed for review.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify contracts, schemas, policy bundles, source descriptors, fixtures, and validator entrypoints before wiring CI. |
