<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-flora-temporal-readme
title: Tests — Flora Temporal
class: test-readme
status: draft
truth_posture: CONFIRMED path / PROPOSED test matrix / UNKNOWN enforcement completeness
owner: <flora-domain-steward> + <data-lifecycle-steward> + <test-steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/domains/flora/DATA_LIFECYCLE.md
  - docs/domains/flora/SOURCE_REGISTRY.md
  - docs/domains/flora/SOURCE_INTAKE.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - tests/domains/flora/source_descriptor/
  - fixtures/domains/flora/
tags:
  - kfm
  - tests
  - flora
  - temporal
  - lifecycle
  - source-time
  - observed-time
  - valid-time
  - retrieval-time
  - release-time
  - correction-time
  - fail-closed
notes:
  - "This README governs the temporal test lane under tests/domains/flora/temporal/."
  - "It documents intended temporal test coverage; it does not claim that all tests already exist."
  - "Temporal distinctions are trust-bearing: source, observed, valid, retrieval, release, and correction times must remain separate where material."
[/KFM_META_BLOCK_V2] -->

# Tests — Flora Temporal

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![root](https://img.shields.io/badge/root-tests%2Fdomains%2Fflora%2Ftemporal-blue?style=flat-square)
![posture](https://img.shields.io/badge/posture-time--aware-success?style=flat-square)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-orange?style=flat-square)
![network](https://img.shields.io/badge/network-no--network-success?style=flat-square)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20path%20%2F%20PROPOSED%20matrix-lightgrey?style=flat-square)

> **Purpose.** This folder is the Flora-domain test lane for temporal integrity: source time, observed time, valid time, retrieval time, release time, correction time, cadence, staleness, and lifecycle-stage ordering.

---

## 1. Placement and authority

`tests/domains/flora/temporal/` is a domain-specific test lane. It belongs under `tests/` because its primary responsibility is to prove Flora temporal rules are enforceable.

| Question | Answer |
|---|---|
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Test lane | `temporal/` |
| Primary lifecycle doc | `docs/domains/flora/DATA_LIFECYCLE.md` |
| Source descriptor standard | `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` |
| Fixture home | `fixtures/domains/flora/` |
| Adjacent lanes | `tests/domains/flora/source_descriptor/`, `tests/domains/flora/evidence_closure/`, `tests/domains/flora/release_manifest/` |

**Directory basis.** Directory Rules place enforceability proofs under `tests/` and domain-specific tests under `tests/domains/<domain>/`. The Flora file-system plan names `tests/domains/flora/temporal/` as the lane for keeping observed, valid, retrieval, release, and correction time distinct.

---

## 2. What this lane must prove

These tests should prove that Flora records do not collapse time fields or promote temporally unsupported material into public claims.

| Test area | Required behavior | Expected failure posture |
|---|---|---|
| Source time | The source publication/version timestamp is recorded separately from KFM retrieval and release. | Temporal validation failure. |
| Observed time | Botanical observation/specimen/event time is preserved when material. | `MISSING_OBSERVED_TIME` or equivalent. |
| Valid time | Range, status, vegetation-community, model, or restoration claims carry validity scope when different from observation time. | `MISSING_VALID_TIME` or equivalent. |
| Retrieval time | Connector/watcher fetch time is recorded and does not overwrite source or observed time. | `MISSING_RETRIEVAL_TIME` or equivalent. |
| Release time | Public release time is emitted only after catalog/release gates. | Release-order failure. |
| Correction time | Corrections/supersessions carry their own time and do not silently edit prior releases. | `MISSING_CORRECTION_TIME` or stale-state failure. |
| Cadence and staleness | Expected update interval and staleness threshold are enforced for refreshed Flora sources. | `SOURCE_STALE`, `TERMS_STALE`, or equivalent. |
| Lifecycle ordering | `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED` ordering is preserved. | Stage-order failure; no public edge. |
| Join temporal support | Cross-source joins do not imply a single shared time unless the temporal scopes truly align. | `TEMPORAL_SCOPE_MISMATCH` or equivalent. |
| Modeled vs. observed time | Modeled distribution/range surfaces carry model run/release time and input temporal scope distinctly. | Source-role / temporal collapse failure. |

---

## 3. Expected test families

This folder should eventually contain narrowly scoped tests, not one large temporal harness.

```text
tests/domains/flora/temporal/
├── README.md
├── test_time_field_distinction.py           # PROPOSED
├── test_observed_time_required.py           # PROPOSED
├── test_valid_time_scope.py                 # PROPOSED
├── test_retrieval_time_required.py          # PROPOSED
├── test_release_time_after_catalog.py       # PROPOSED
├── test_correction_time_supersession.py     # PROPOSED
├── test_cadence_and_staleness.py            # PROPOSED
├── test_lifecycle_stage_order.py            # PROPOSED
├── test_join_temporal_scope.py              # PROPOSED
├── test_modeled_temporal_provenance.py      # PROPOSED
└── conftest.py                              # PROPOSED, only if shared fixtures are needed
```

If the repository uses another test runner or filename convention, preserve that convention and keep this README as the lane contract.

---

## 4. Fixture expectations

Tests in this lane should be no-network by default. They should use small synthetic or golden Flora records that isolate temporal behavior.

Recommended fixture groups:

```text
fixtures/domains/flora/temporal/
├── valid/
│   ├── occurrence_with_observed_and_retrieval_time.json
│   ├── specimen_with_source_observed_retrieval_time.json
│   ├── modeled_distribution_with_input_scope_and_model_run_time.json
│   ├── range_polygon_with_valid_time.json
│   └── corrected_record_with_release_and_correction_time.json
├── invalid/
│   ├── observed_time_missing.json
│   ├── retrieval_time_overwrites_observed_time.json
│   ├── source_time_collapsed_to_release_time.json
│   ├── valid_time_required_but_missing.json
│   ├── published_before_catalog_closure.json
│   ├── correction_without_correction_time.json
│   ├── stale_source_without_stale_state.json
│   └── join_temporal_scope_mismatch.json
└── golden/
    ├── flora_temporal_minimal_occurrence.json
    └── flora_temporal_release_lineage.json
```

Fixture data must not contain real precise rare-plant locations, unpublished steward records, credentials, or live-source payloads. Use synthetic plant names, synthetic coordinates, placeholder source IDs, and stable timestamps.

---

## 5. Time vocabulary under test

The temporal lane should preserve the six time meanings below where material.

| Time kind | Meaning in Flora | Example |
|---|---|---|
| `source_time` | When the source itself was produced, updated, published, or versioned. | USDA PLANTS release date; herbarium export date. |
| `observed_time` / `observed_scope` | When the plant observation, specimen collection, survey, phenology event, or field record occurred. | iNaturalist observation date; specimen collection date. |
| `valid_time` | When a claim is valid for the real-world condition being represented. | Range polygon effective period; listing status period; restoration planting active interval. |
| `retrieval_time` | When KFM fetched or received the source material. | Connector run timestamp; manual upload timestamp. |
| `release_time` | When KFM released a public-safe artifact. | ReleaseManifest timestamp. |
| `correction_time` | When a correction, supersession, rollback, or stale-state change was recorded. | CorrectionNotice timestamp. |

**Rule:** absence and `null` are not equivalent unless the schema explicitly says they are. A missing key can mean a validator never checked the temporal claim; `null` can mean the time kind was considered and found not material.

---

## 6. Flora-specific temporal checks

The Flora temporal lane should add domain assertions only where Flora objects create time-aware risk.

| ID | Flora-specific assertion | Why it matters |
|---|---|---|
| `FLORA-TEMP-001` | A Flora occurrence or specimen with a place claim must preserve observation/collection time separately from retrieval time. | Prevents treating a recent fetch as a recent observation. |
| `FLORA-TEMP-002` | Phenology observations require event time or event interval. | Phenology is meaningless without time. |
| `FLORA-TEMP-003` | Range polygons and distribution surfaces must carry validity or model/input temporal scope. | Prevents stale range/model products from appearing current. |
| `FLORA-TEMP-004` | Public release time cannot exist before catalog closure and release decision artifacts. | Preserves publication as governed state transition. |
| `FLORA-TEMP-005` | Source cadence and staleness thresholds are enforced for periodically refreshed botanical sources. | Supports stale-state badges and recheck gates. |
| `FLORA-TEMP-006` | Corrections and supersessions create new temporal lineage rather than mutating prior records silently. | Preserves auditability and rollback. |
| `FLORA-TEMP-007` | Cross-source joins must compare temporal scopes before producing a public derivative. | Prevents mismatched checklist/occurrence/range timelines. |
| `FLORA-TEMP-008` | Rare-plant delayed-publication transforms must record embargo/release timing and review. | Connects temporal rules to sensitivity controls. |

---

## 7. Minimal acceptance matrix

A first useful implementation of this lane should include at least these no-network checks:

| ID | Scenario | Given | Then |
|---|---|---|---|
| `FLORA-TEMP-001` | Valid occurrence time passes. | A Flora occurrence with observed time, source time, retrieval time, and source descriptor. | Temporal validation passes. |
| `FLORA-TEMP-002` | Missing observation time fails where material. | A specimen/occurrence that asserts a place but omits collection/observation time. | Validation fails closed. |
| `FLORA-TEMP-003` | Retrieval time cannot replace observed time. | A descriptor or object where retrieval timestamp is copied into observed time without support. | Temporal collapse is rejected. |
| `FLORA-TEMP-004` | Range/model validity must be explicit. | A distribution surface or range polygon without input scope or valid time. | Validation fails or routes to review. |
| `FLORA-TEMP-005` | Stale source is visibly stale. | A source whose staleness threshold is exceeded. | Output carries stale state or blocks promotion. |
| `FLORA-TEMP-006` | Release time follows catalog closure. | A published artifact candidate without catalog closure time or release manifest. | Public edge is denied. |
| `FLORA-TEMP-007` | Correction time is required. | A corrected Flora record without correction timestamp or CorrectionNotice link. | Correction validation fails. |
| `FLORA-TEMP-008` | Join temporal mismatch fails. | A checklist from one period joined to occurrence data from another without declared interpretation. | Join product is denied, held, or marked review-required. |

---

## 8. Non-goals

This folder must not:

- call live external source APIs;
- decide botanical taxonomy or source authority by timestamp alone;
- treat retrieval time as observation time;
- treat source publication time as release time;
- silently mutate prior releases during correction;
- bypass catalog closure or release manifest checks;
- publish stale records without visible stale state; or
- create a second temporal schema or policy home.

---

## 9. Review checklist

Before adding or changing tests in this lane, confirm:

- [ ] The test is deterministic and no-network.
- [ ] The fixture is synthetic, public-safe, or intentionally invalid.
- [ ] The test proves a temporal rule, not a downstream botanical fact.
- [ ] The expected result is fail-closed where temporal support is missing or collapsed.
- [ ] Source, observed, valid, retrieval, release, and correction time remain separate where material.
- [ ] Stale-state behavior is explicit, not silently ignored.
- [ ] The test preserves lifecycle ordering from RAW to PUBLISHED.
- [ ] Any path conflict is recorded as drift or verification backlog, not silently normalized.

---

## 10. Current implementation note

This lane is documentation-first. The Flora lifecycle doctrine is well described, but this README does not prove that executable temporal tests, fixtures, validators, or CI wiring already exist. Treat the test matrix as `PROPOSED` until actual test files and validation runs confirm enforcement.

---

## 11. Definition of done

This README becomes implementation-backed when:

- at least the `FLORA-TEMP-001` through `FLORA-TEMP-008` scenarios exist as executable tests;
- temporal fixtures exist under the repository's approved Flora fixture home;
- schema and policy validators preserve source, observed, valid, retrieval, release, and correction time distinctly;
- stale-state and correction-time failures emit finite reason codes;
- lifecycle-order tests block premature public release; and
- CI runs the temporal lane without network access.
