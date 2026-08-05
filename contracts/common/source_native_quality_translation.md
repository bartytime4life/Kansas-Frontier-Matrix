<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-common-source-native-quality-translation
title: SourceNativeQualityTranslation Contract
type: semantic-contract; shared-kernel; source-quality; assessment-separation
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-source-or-release-authority
owners: OWNER_TBD — Contracts steward · Source steward · Domain data-quality stewards · Schema steward · Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; contracts; common; quality-translation; health-separation; non-authoritative
tags: [kfm, source-quality, native-vocabulary, quality-mapping, operational-health, observation-validity, semantic-loss, unmapped]
related:
  - ./README.md
  - ../../schemas/contracts/v1/common/source_native_quality_translation.schema.json
  - ../../fixtures/contracts/v1/common/source_native_quality_translation/
  - ../../tools/validators/validate_source_native_quality_translation.py
  - ../../tests/validators/test_validate_source_native_quality_translation.py
  - ../../docs/intake/exploratory/new-ideas-4-15-source-map.md
notes:
  - "Implements the bounded Source-Native Quality Translation and Health Separation gap identified as KFM-TRIAD-068."
  - "Operational health, source-native quality, and observation validity are separate claim families and must not be collapsed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SourceNativeQualityTranslation

> `SourceNativeQualityTranslation` preserves a source's native quality vocabulary and a versioned mapping decision while recording operational health and observation validity as independent assessments.

## Purpose

Source systems frequently expose compact quality codes, status flags, or provider-specific labels. Those values are useful only when KFM preserves:

- the exact native code and label;
- the source vocabulary identity, version, and digest;
- the mapping profile and decision used to interpret the code;
- whether the mapping was exact, ambiguous, unmapped, or not applicable;
- any semantic loss introduced by normalization;
- the operational state of the source, station, sensor, or adapter; and
- the validity of a particular observation.

These concepts must remain separate. A station becoming offline does not retroactively invalidate a previously supported reading. A missing reading does not prove an environmental condition. A native quality code is not source admission, evidence closure, policy approval, release authority, or scientific truth.

## Why this belongs in `common/`

No single KFM domain owns source-native quality translation or the distinction between operational health and observation validity. Soil moisture, atmosphere, hydrology, habitat, agriculture, and other observation-bearing lanes can all reuse the same narrow vocabulary and invariants while retaining domain-owned quality mappings and thresholds.

The shared contract does not define domain thresholds, provider-specific code tables, calibration rules, or scientific acceptance decisions. Those remain in their owning source, domain, policy, or profile lanes.

## Directory Rules basis

| Responsibility | Home | Role in this slice |
|---|---|---|
| Shared human-readable meaning | `contracts/common/` | This semantic contract. |
| Machine-checkable shape | `schemas/contracts/v1/common/` | Closed Draft 2020-12 profile. |
| Synthetic examples | `fixtures/contracts/v1/common/` | Valid and exact-negative records. |
| Executable validation | `tools/validators/` | Deterministic no-network validation. |
| Enforceability | `tests/validators/` | Schema, semantic, parser, CLI, determinism, and non-echoing tests. |
| CI orchestration | `.github/workflows/` | Read-only focused workflow. |
| AI authoring provenance | `data/receipts/generated/` | Pending-review generation receipt only. |

No new root, source registry, policy authority, evidence store, lifecycle store, release family, or public path is introduced.

## Object boundary

The record owns:

- a translation identity and deterministic fixture `spec_hash`;
- source descriptor and declared source-role references;
- source-native vocabulary identity, version, digest, code, label, and detail;
- the mapping profile, digest, decision reference, finite mapping outcome, normalized quality, semantic-loss class, unmapped-state marker, reason codes, and review requirement;
- one operational-health assessment;
- one observation-validity assessment;
- fixed separation declarations;
- run provenance and input references; and
- explicit non-authority governance fields.

The record does not own:

- source admission or activation;
- a provider's complete quality-code table;
- domain thresholds, calibration, or scientific interpretation;
- an `EvidenceBundle`, `PolicyDecision`, review approval, or source-rights determination;
- lifecycle promotion, proof closure, release, deployment, publication, or public-use permission.

## Native vocabulary identity

Every record preserves:

| Field | Meaning |
|---|---|
| `vocabulary_id` | Stable identifier for the source-native quality vocabulary. |
| `vocabulary_version` | Source-declared or steward-declared vocabulary version. |
| `vocabulary_digest` | Non-placeholder SHA-256 binding for the reviewed vocabulary artifact or fixture profile. |
| `native_code` | Exact source-native code; never replaced by the normalized value. |
| `native_label` / `native_detail` | Optional source wording retained without granting authority. |
| `native_value_preserved` | Fixed `true`; normalization never erases the original code. |

A mapping cannot be treated as portable across source versions unless the vocabulary identity remains bound.

## Mapping outcomes

| Outcome | Required interpretation |
|---|---|
| `MAPPED` | The profile maps the native code to `ACCEPTED`, `SUSPECT`, `REJECTED`, or `MISSING`. Semantic loss is explicit. |
| `UNMAPPED` | The native code is retained, normalized quality is `UNKNOWN`, semantic loss is `MATERIAL` or `UNKNOWN`, and review is required. |
| `AMBIGUOUS` | More than one meaning remains possible. Normalized quality is `UNKNOWN` or `SUSPECT`; semantic loss cannot be `NONE`; review is required. |
| `NOT_APPLICABLE` | No quality mapping applies to this record. Normalized quality is `NOT_APPLICABLE`, semantic loss is `NONE`, and review is not required. |

`normalized_quality` is a portable review vocabulary, not an assertion that the source, observation, or environmental condition is authoritative.

## Operational health

Operational health describes the current ability of a station, sensor, source, or adapter to produce or deliver observations:

- `ONLINE`
- `DEGRADED`
- `OFFLINE`
- `UNKNOWN`
- `NOT_APPLICABLE`

An `OFFLINE` assessment must state that current observation availability is affected. `ONLINE` and `NOT_APPLICABLE` do not. Every health assessment keeps reason codes and any local evidence references.

Operational health is forbidden from deciding observation validity or claiming an environmental condition.

## Observation validity

Observation validity is scoped to one observation or expected observation:

- `VALID`
- `SUSPECT`
- `INVALID`
- `MISSING`
- `NOT_ASSESSED`

A `VALID`, `SUSPECT`, or `INVALID` assessment requires an observation reference and assessment time. `MISSING` records the absence of an expected observation without claiming an environmental state. `NOT_ASSESSED` preserves an explicit unresolved state.

Observation validity is never derived solely from operational health.

## Required separation

The schema fixes these declarations to `true`:

- `health_and_validity_independent`;
- `offline_does_not_invalidate_prior_observations`;
- `no_data_is_not_environmental_condition`; and
- `source_quality_is_not_source_authority`.

The health and validity assessments also have different ID grammars, vocabularies, timestamps, reason codes, and evidence references.

### Valid example: offline now, historical reading still valid

A record may legitimately contain:

```text
operational_health.state = OFFLINE
operational_health.affects_current_observation_availability = true
observation_validity.state = VALID
observation_validity.observation_ref = historical reading
```

This is not a contradiction. It proves the two claim families were not collapsed.

### Denied example: offline used as observation validity

```text
operational_health.state = OFFLINE
observation_validity.state = OFFLINE
```

`OFFLINE` is not an observation-validity state. The validator emits `HEALTH_VALIDITY_VOCABULARY_COLLAPSE`.

## Deterministic identity

`spec_hash` uses the local fixture profile `kfm-fixture-json-v1`:

1. remove the top-level `spec_hash`;
2. serialize the remaining JSON with UTF-8, sorted object keys, no insignificant whitespace, and JSON-native array order;
3. compute SHA-256;
4. prefix with `sha256:`.

This bounded profile supports fixture replay only. It does not claim RFC 8785/JCS conformance or settle a repository-wide hash policy.

## Validator behavior

The no-network validator:

- rejects symbolic links, missing/non-regular/oversized files, malformed JSON, duplicate keys, non-finite numbers, and non-object roots;
- validates the Draft 2020-12 schema with bounded findings;
- checks non-placeholder digests and deterministic `spec_hash`;
- requires sorted unique reason/reference arrays;
- enforces mapping outcome, unmapped-state, semantic-loss, and review consistency;
- denies health-to-validity vocabulary or causal collapse;
- enforces health/availability and observation-support rules;
- enforces temporal ordering and distinct assessment identities;
- fixes all governance authority fields to false and `release_ref` to null;
- emits stable codes and JSON pointers without echoing candidate values.

## Fixture profile

The valid corpus proves:

- exact native mapping with online health and a valid observation;
- an unmapped code retained under degraded health without fabricating validity;
- a current outage that does not invalidate a historical reading;
- an ambiguous mapping producing a suspect observation and required review; and
- a health-only record where quality and observation assessment are not applicable.

The exact-negative corpus covers:

- unmapped code collapsed to accepted quality;
- operational-health vocabulary used as observation validity;
- health state directly deciding validity;
- ambiguous mapping without review;
- semantic loss hidden as `NONE`;
- offline state not affecting current availability;
- assessed validity without an observation reference;
- noncanonical reference order;
- `spec_hash` mismatch;
- governance overclaim;
- temporal inversion; and
- incomplete native-vocabulary identity.

Every semantic-negative fixture also contains an undeclared schema canary so repository-wide valid/invalid fixture polarity and dedicated semantic validation remain independently non-vacuous.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_source_native_quality_translation.py' \
  --verbose

python tools/validators/validate_source_native_quality_translation.py --fixtures
```

A green result proves only the proposed shape, fixture hash, local mapping consistency, exact synthetic fixture polarity, and separation invariants.

It does not prove a source vocabulary is current, a mapping is scientifically correct, a source is admitted, an observation is true, evidence resolves, rights or policy allow use, review is complete, or release/publication is authorized.

## Rollback

Before merge, close the draft pull request and abandon its feature branch. After an authorized merge, revert the dependency-closed contract/schema/fixture/validator/test/workflow/receipt commit. If downstream records later reference stable translation IDs, preserve historical process memory and use correction or supersession rather than deleting relied-on records.

<p align="right"><a href="#top">Back to top</a></p>
