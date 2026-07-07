<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-agriculture-readme
title: tools/validators/agriculture README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-agriculture-domain-steward-plus-policy-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; agriculture-validator-lane; sensitive-aggregation-aware
owning_root: tools/
responsibility: proposed agriculture-domain validator lane for schema, source-rights, aggregation, sensitivity, evidence, lifecycle, and release-reference checks
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../../../docs/domains/agriculture/README.md
  - ../../../contracts/domains/agriculture/
  - ../../../schemas/contracts/v1/domains/agriculture/
  - ../../../policy/domains/agriculture/
  - ../../../tests/domains/agriculture/
  - ../../../fixtures/domains/agriculture/
  - ../../../data/registry/sources/agriculture/
  - ../../../data/raw/agriculture/
  - ../../../data/processed/agriculture/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../release/candidates/agriculture/
notes:
  - "This README documents a proposed agriculture-domain validator lane. It does not confirm executable files."
  - "Agriculture validation must preserve source rights, sensitivity tier, aggregation/redaction evidence, source-role separation, evidence closure, lifecycle boundaries, and release references."
  - "Validators enforce declared contracts, schemas, and policy. They do not define agriculture semantics, source rights, policy rules, proof records, release decisions, or public products."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/agriculture

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-agriculture--validators-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-aggregation--aware-yellow)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/agriculture/` is the proposed validator lane for agriculture-domain checks: schema shape, source-rights posture, aggregation/redaction evidence, sensitivity tier, evidence closure, lifecycle boundary, and release-reference checks.

---

## Purpose

`tools/validators/agriculture/` exists to hold agriculture-specific validator entrypoints and helpers that are too domain-specific for `_common/` but still belong under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does an agriculture-domain candidate satisfy the declared agriculture contracts, schemas, source-rights posture, sensitivity controls, evidence requirements, lifecycle boundaries, and release-reference expectations?

The answer should be a deterministic validation result. It should not become agriculture truth, source-rights authority, policy authority, proof closure, or release approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/agriculture/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Agriculture validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Agriculture domain doctrine | **CONFIRMED in repo evidence / draft** | Domain README defines agriculture scope, source families, sensitivity posture, and validation needs. |
| Agriculture schema home | **PROPOSED / NEEDS VERIFICATION** | Domain README points to `schemas/contracts/v1/domains/agriculture/`. |
| Agriculture policy home | **PROPOSED / NEEDS VERIFICATION** | Domain README points to `policy/domains/agriculture/`. |
| Source descriptors | **NEEDS VERIFICATION** | Domain README requires SourceDescriptors for NASS CDL, QuickStats, SSURGO cited from Soil, and Mesonet. |
| Public release validation | **PROPOSED / NEEDS VERIFICATION** | Requires evidence closure, aggregation/redaction posture, release references, and rollback support. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Agriculture validator entrypoints | `tools/validators/agriculture/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Agriculture domain meaning | `docs/domains/agriculture/` and `contracts/domains/agriculture/` |
| Agriculture schemas | `schemas/contracts/v1/domains/agriculture/` or accepted schema home |
| Agriculture policy rules | `policy/domains/agriculture/` |
| Agriculture source descriptors | `data/registry/sources/agriculture/` |
| Agriculture lifecycle data | `data/raw/agriculture/`, `data/work/agriculture/`, `data/quarantine/agriculture/`, `data/processed/agriculture/` |
| Receipts and proofs | `data/receipts/`, `data/proofs/` |
| Release candidates and release records | `release/candidates/agriculture/` and accepted `release/` lanes |
| Tests and fixtures | `tests/domains/agriculture/`, `fixtures/domains/agriculture/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** agriculture validator code may live here when it enforces declared contracts/schemas/policy and is fixture-tested.
- **NEEDS VERIFICATION:** exact executable names, current schemas, fixtures, policy bundles, source descriptors, and CI wiring.
- **DENY:** using this folder as source registry, schema home, policy home, lifecycle data store, proof store, release record store, or public product surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/agriculture/` include validators that check:

- `CropObservation` schema shape;
- `YieldObservation` schema shape;
- `FieldCandidate` sensitivity and geometry posture;
- `CropRotation` temporal consistency;
- `SoilCropSuitability` references to Soil-owned MUKEY semantics;
- `DroughtStressIndicator` and `PestStressIndicator` indicator-vs-advisory boundaries;
- `AggregationReceipt` or `RedactionReceipt` presence for field-to-aggregate public products;
- SourceDescriptor presence for NASS, Mesonet, HLS/SMAP, and other agriculture source families;
- evidence closure for public claims;
- lifecycle path discipline, including no RAW-to-published shortcut;
- release-reference readiness for agriculture release candidates.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/agriculture/` | Correct home |
|---|---|
| Shared schema registry helpers | `tools/validators/_common/` |
| Agriculture contracts | `contracts/domains/agriculture/` |
| Agriculture schemas | `schemas/contracts/v1/domains/agriculture/` |
| Agriculture policy rules | `policy/domains/agriculture/` |
| Source descriptors | `data/registry/sources/agriculture/` |
| Raw, work, quarantine, processed, catalog, or published data | dedicated `data/` lifecycle roots |
| Receipts and proofs | `data/receipts/`, `data/proofs/` |
| Release records | `release/` |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Connectors or pipelines | `connectors/`, `pipelines/` |

[Back to top](#top)

---

## Agriculture validation posture

Agriculture validation is privacy- and rights-aware. Validators should fail closed or return review-required outcomes when:

- field-level detail lacks aggregation/redaction support;
- operator-level or private parcel joins appear in a public-bound candidate;
- source rights or terms are unresolved;
- soil semantics are redefined instead of cited from Soil;
- hydrology or atmosphere inputs are treated as agriculture-owned truth;
- public claims lack EvidenceBundle resolution;
- LayerManifest or ReleaseManifest references are missing where release is in scope.

Validators should preserve KFM's lifecycle boundary:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `AG_VALIDATION_PASS` | Configured agriculture checks passed. |
| `AG_VALIDATION_FAIL` | Configured agriculture checks failed. |
| `SOURCE_DESCRIPTOR_MISSING` | Required agriculture source descriptor is absent. |
| `RIGHTS_REVIEW_REQUIRED` | Source rights or terms require review. |
| `SENSITIVITY_REVIEW_REQUIRED` | Sensitivity posture blocks automatic downstream use. |
| `AGGREGATION_RECEIPT_MISSING` | Required aggregation/redaction support is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `CROSS_LANE_AUTHORITY_CONFLICT` | Candidate redefines Soil, Hydrology, Atmosphere, or People/Land authority. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `RELEASE_REFERENCE_MISSING` | Required release support pointer is absent. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/domains/agriculture/
├── README.md
├── test_agriculture_validators.py
└── fixtures/
    ├── valid_crop_observation/
    ├── missing_source_descriptor/
    ├── field_without_aggregation/
    ├── operator_join_public_candidate/
    ├── soil_semantics_redefined/
    └── evidence_missing/
```

Suggested future command pattern:

```bash
pytest -q tests/domains/agriculture
```

```bash
python tools/validators/agriculture/validate_agriculture_candidate.py --fixtures --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_agriculture_candidate.py` or `tests/domains/agriculture/` exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared contracts and schemas rather than inlining new shape rules.
- [ ] Validator reads declared policy posture rather than defining policy locally.
- [ ] SourceDescriptor references are checked where required.
- [ ] Field/operator/private joins fail closed unless proper support records exist.
- [ ] Soil, Hydrology, Atmosphere, Hazards, and People/Land authority boundaries are preserved.
- [ ] EvidenceBundle or EvidenceRef support is required for public claims.
- [ ] Aggregation/redaction support is checked for public-safe products.
- [ ] Lifecycle and release-reference checks are explicit.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify actual agriculture schemas, source descriptors, policy bundles, fixtures, and validator entrypoints before wiring CI. |
