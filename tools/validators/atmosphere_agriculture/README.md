<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-atmosphere-agriculture-readme
title: tools/validators/atmosphere_agriculture README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-atmosphere-steward-plus-agriculture-steward-plus-policy-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; cross-domain-validator; atmosphere-agriculture; stress-indicator-aware
owning_root: tools/
responsibility: proposed cross-domain validator lane for Atmosphere/Air evidence cited by Agriculture stress products, including source-role, evidence, sensitivity, aggregation, freshness, correction, lifecycle, and release-boundary checks
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../../../docs/domains/agriculture/atmosphere-stress.md
  - ../../../docs/domains/agriculture/README.md
  - ../../../docs/domains/agriculture/OBJECTS.md
  - ../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../docs/domains/agriculture/CROSS_LANE.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../contracts/domains/agriculture/
  - ../../../contracts/domains/atmosphere/
  - ../../../schemas/contracts/v1/domains/agriculture/
  - ../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../policy/domains/agriculture/
  - ../../../policy/domains/atmosphere/
  - ../../../data/proofs/evidence_bundle/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README documents a proposed cross-domain validator lane. It does not confirm executable files."
  - "Atmosphere/Air owns the atmospheric record. Agriculture owns stress interpretation that cites atmospheric evidence. Validators must not collapse those responsibilities."
  - "Validators enforce declared contracts, schemas, and policy. They do not define source roles, create EvidenceBundles, approve release, or publish stress products."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/atmosphere_agriculture

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-atmosphere--agriculture--validators-informational)
![edge](https://img.shields.io/badge/edge-stress--indicators-yellow)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/atmosphere_agriculture/` is the proposed cross-domain validator lane for Agriculture stress products that cite Atmosphere/Air evidence: drought stress, pest stress, vegetation stress, smoke, AOD, weather, heat, precipitation, soil-moisture-adjacent context, freshness, aggregation, and source-role anti-collapse checks.

---

## Purpose

`tools/validators/atmosphere_agriculture/` exists for validator logic that is genuinely cross-domain between Atmosphere/Air and Agriculture.

The durable KFM question for this lane is:

> Does an Agriculture stress-product candidate cite Atmosphere/Air evidence without re-owning atmospheric truth, collapsing source roles, leaking field/operator-sensitive context, or skipping evidence, lifecycle, correction, and release gates?

The answer should be a deterministic validation result. It should not create atmospheric observations, crop/yield records, stress indicators, EvidenceBundles, policy decisions, release decisions, or map/API products.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/atmosphere_agriculture/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Agriculture × Atmosphere reference | **CONFIRMED in repo evidence / draft** | Cross-lane reference documents how Agriculture cites Atmosphere/Air evidence for `DroughtStressIndicator`, `PestStressIndicator`, and vegetation-stress surfaces. |
| Source-role anti-collapse posture | **CONFIRMED in repo evidence / draft** | The reference flags Atmosphere/Air source-role anti-collapse as acute and names observed, regulatory, modeled, aggregate, candidate, and synthetic collapse risks. |
| Contract/schema paths | **PROPOSED / NEEDS VERIFICATION** | Agriculture and Atmosphere schema-home questions remain subject to ADR/path verification. |
| Policy and release wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove policy bundles, source descriptors, release gates, or CI are wired. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Cross-domain Atmosphere/Agriculture validator entrypoints | `tools/validators/atmosphere_agriculture/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-lane reference doctrine | `docs/domains/agriculture/atmosphere-stress.md` |
| Agriculture domain meaning | `docs/domains/agriculture/`, `contracts/domains/agriculture/` |
| Atmosphere/Air domain meaning | `docs/domains/atmosphere/`, `contracts/domains/atmosphere/` |
| Agriculture schemas | `schemas/contracts/v1/domains/agriculture/` or accepted schema home |
| Atmosphere/Air schemas | `schemas/contracts/v1/domains/atmosphere/` or accepted schema home |
| Policy rules | `policy/domains/agriculture/`, `policy/domains/atmosphere/`, or accepted policy homes |
| EvidenceBundles and receipts | `data/proofs/evidence_bundle/`, `data/receipts/` |
| Release records | `release/` |
| Tests and fixtures | `tests/validators/atmosphere_agriculture/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it validates a cross-lane invariant and reads declared contracts, schemas, policy, and source descriptors.
- **NEEDS VERIFICATION:** exact executable names, schema homes, fixtures, policy bundles, source descriptors, and CI wiring.
- **DENY:** using this folder as a domain contract home, schema home, policy home, source registry, evidence store, lifecycle data store, release record store, or public runtime surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/atmosphere_agriculture/` include checks that:

- preserve Atmosphere/Air ownership of `WeatherObservation`, `PrecipitationObservation`, `TemperatureObservation`, `WindField`, `SmokeContext`, `AODRaster`, `AirObservation`, and `ClimateNormal` evidence;
- preserve Agriculture ownership of `DroughtStressIndicator`, `PestStressIndicator`, vegetation-stress surfaces, `CropObservation`, `YieldObservation`, `FieldCandidate`, and `AggregationReceipt` records;
- prevent modeled smoke, radar QPE, AOD, or climate-normal context from being presented as observed field truth;
- prevent aggregate climate normals from being joined to field-candidate scope without required aggregation support;
- require SourceDescriptor role, authority, rights, sensitivity, cadence, and freshness posture for cited Atmosphere/Air evidence;
- require EvidenceRef or EvidenceBundle support for public-bound stress-product claims;
- require `AggregationReceipt`, `RedactionReceipt`, `ReviewRecord`, or policy decision where field/operator scope is approached;
- propagate Atmosphere/Air correction or stale-state signals into dependent Agriculture stress products;
- enforce `ABSTAIN`, `DENY`, `NARROWED`, or `BOUNDED` behavior for governed-AI surfaces when evidence or policy is insufficient.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/atmosphere_agriculture/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Agriculture contracts | `contracts/domains/agriculture/` |
| Atmosphere/Air contracts | `contracts/domains/atmosphere/` |
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

This validator lane is for source-role, scope, evidence, and sensitivity anti-collapse checks.

It should fail closed, narrow, or route to review when a candidate collapses:

- modeled atmospheric output into observed field truth;
- aggregate climate baseline into per-field truth;
- regulatory air-quality context into observed event evidence;
- candidate or unvalidated sensor records into published stress indicators;
- synthetic or AI bridging text into observed reality;
- public-safe stress products into farm/operator-level inference;
- Atmosphere-owned observations into Agriculture-owned data;
- Agriculture-owned stress interpretation into Atmosphere-owned measurements.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `ATM_AG_VALIDATION_PASS` | Configured Atmosphere/Agriculture cross-domain checks passed. |
| `ATM_AG_VALIDATION_FAIL` | Configured checks failed. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses modeled, observed, aggregate, regulatory, candidate, or synthetic roles. |
| `ATMOSPHERE_OWNERSHIP_CONFLICT` | Agriculture candidate appears to redefine or re-own Atmosphere/Air evidence. |
| `AGRICULTURE_SCOPE_CONFLICT` | Atmospheric evidence is being used to claim unsupported agriculture field/operator truth. |
| `SOURCE_DESCRIPTOR_MISSING` | Required source descriptor is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `AGGREGATION_RECEIPT_MISSING` | Required aggregation/redaction support is absent. |
| `FRESHNESS_OR_CORRECTION_REQUIRED` | Stale, superseded, corrected, or unversioned atmospheric evidence requires action. |
| `SENSITIVITY_REVIEW_REQUIRED` | Public-bound output requires sensitivity review, generalization, or denial. |
| `PUBLIC_BOUNDARY_VIOLATION` | Candidate is not safe for public/governed output as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/atmosphere_agriculture/
├── README.md
├── test_atmosphere_agriculture_validators.py
└── fixtures/
    ├── valid_county_drought_stress/
    ├── modeled_smoke_as_observed_denied/
    ├── climate_normal_as_field_truth_denied/
    ├── missing_source_descriptor/
    ├── missing_evidence_ref/
    ├── missing_aggregation_receipt/
    ├── farm_operator_join_denied/
    └── stale_atmosphere_source_abstain/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/atmosphere_agriculture
```

```bash
python tools/validators/atmosphere_agriculture/validate_atmosphere_agriculture_candidate.py --fixtures --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_atmosphere_agriculture_candidate.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared contracts and schemas rather than defining shape locally.
- [ ] Validator reads declared policy posture rather than defining policy locally.
- [ ] Atmosphere/Air and Agriculture ownership boundaries are preserved.
- [ ] Source-role and knowledge-character fields are explicit.
- [ ] Modeled, observed, aggregate, regulatory, candidate, and synthetic records remain distinct.
- [ ] Public-bound stress products require EvidenceRef or EvidenceBundle support.
- [ ] Field/operator-sensitive outputs require aggregation, redaction, review, or denial.
- [ ] Corrections and stale-state signals propagate to dependent stress products.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify contracts, schemas, policy bundles, source descriptors, fixtures, validator entrypoints, and CI wiring before promoting this lane beyond draft. |
