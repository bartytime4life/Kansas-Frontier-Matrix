<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-evidence-frontier-classification
title: contracts/evidence/frontier_classification.md — FrontierClassification Contract
type: contract
version: v1.0.0
status: draft; PROPOSED; schema-paired; synthetic-only; fixture-first
owners: OWNER_TBD — Evidence steward · Contracts steward · Schema steward · Policy steward · Review steward
created: 2026-08-16
updated: 2026-08-16
policy_label: public; contracts; evidence; frontier-classification; synthetic-only; no-network; finite-classification; correction-lineage
tags: [kfm, contracts, evidence, frontier-classification, county-year-panel, frontier-definition, geography-version, uncertainty, evidence-ref, evidence-bundle, threshold-policy-ref, deterministic-identity, correction, no-network]
related:
  - ./frontier_definition.md
  - ../data/county_year_panel.md
  - ../common/geography_version.md
  - ./access_observation.md
  - ./population_observation.md
  - ./evidence_ref.md
  - ./evidence_bundle.md
  - ../runtime/decision_envelope.md
  - ../../schemas/contracts/v1/evidence/frontier_classification.schema.json
  - ../../fixtures/contracts/v1/evidence/frontier_classification/cases.json
  - ../../tools/validators/evidence/validate_frontier_classification.py
  - ../../tests/validators/evidence/test_validate_frontier_classification.py
notes:
  - "FrontierClassification is an evidence assessment, not a threshold policy, runtime DecisionEnvelope, review decision, release object, public API response, or map layer."
  - "This initial profile is dependency-closed, deterministic, synthetic-only, fixture-bound, and no-network."
  - "Threshold values remain inside sealed synthetic fixture threshold-policy resources; they are not copied into the assessment packet."
  - "Reusable EvidenceRef-to-EvidenceBundle resolution is outside this contract and remains separately owned."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FrontierClassification Contract

> `FrontierClassification` records a deterministic, synthetic-only assessment of one validated `CountyYearPanel` against one validated `FrontierDefinition`. It preserves criterion-level support and produces exactly one classification value: `FRONTIER`, `NOT_FRONTIER`, or `UNCLASSIFIED`.

**Status:** draft / PROPOSED

**Path:** `contracts/evidence/frontier_classification.md`

**Paired schema:** `schemas/contracts/v1/evidence/frontier_classification.schema.json`

**Fixture profile:** `kfm.frontier-classification.fixture.v1`

**Implementation posture:** synthetic-only · deterministic · no-network · no lifecycle writes · no authority effects

## Purpose

The contract closes the smallest governed seam between the existing declaration and composition objects:

```text
FrontierDefinition
  + CountyYearPanel
  + version-bound AccessObservation / PopulationObservation fixtures
  + exact local GeographyVersion / crosswalk support
  + exact local uncertainty resources
  + exact local EvidenceRef / EvidenceBundle support
  + exact local threshold-policy fixture resources
  -> FrontierClassification
```

The assessment may determine a synthetic fixture classification. It does not classify a real county and does not create source, truth, threshold, policy, review, promotion, release, publication, deployment, public API, or map authority.

## Authority boundaries

`FrontierClassification` consumes existing authority without replacing it:

| Concern | Existing authority retained | This packet may do |
|---|---|---|
| Definition meaning and combination rule | `FrontierDefinition` | Bind to its exact id/digest and evaluate its declared rule. |
| County/year composition | `CountyYearPanel` | Bind to its exact id/digest and inspect its four governed slots. |
| Geography identity and cross-version joins | `GeographyVersion` and admitted crosswalk evidence | Accept same-version support or one exact admitted synthetic crosswalk. |
| Observation meaning and source roles | Existing observation contracts | Validate exact synthetic observation fixtures and mirror their identity/source role into traces. |
| Uncertainty | Observation and definition uncertainty posture | Require exact local interval support; abstain when absent, unresolved, excessive, or threshold-crossing. |
| Evidence pointers and closure | `EvidenceRef` / `EvidenceBundle` | Verify exact fixture membership and bundle content identity without exposing or generalizing a store resolver. |
| Thresholds and policy | Existing referenced threshold-policy authority | Read only an exact synthetic fixture resource; never change a value or declare policy. |
| Runtime finite decisions | `DecisionEnvelope` | Remain separate. Classification values are not `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. |
| Correction | Existing correction and supersession doctrine | Create a new assessment identity that retains a digest-bound predecessor and correction record. |

The validator's sealed fixture registry is not a reusable EvidenceRef resolver. It has no network or store adapter and creates no parallel authority to the separately governed resolver seam.

## Classification values

| Value | Required meaning |
|---|---|
| `FRONTIER` | The declared combination rule is satisfied by all support required to reach that result. |
| `NOT_FRONTIER` | The declared combination rule is determinately unsatisfied. Missing, suppressed, stale, superseded, unresolved, mismatched, or excessive-uncertainty support must not produce this value. |
| `UNCLASSIFIED` | Required support is insufficient or unsafe for a valid determination. This is the fail-closed value for missingness, suppression, stale or superseded inputs, unresolved correction lineage, geography/time mismatch, evidence mismatch, uncertainty failure, or threshold-policy mismatch. |

Combination behavior is finite and deterministic:

- `ALL_CRITERIA`: all satisfied yields `FRONTIER`; any determinate unsatisfied criterion yields `NOT_FRONTIER`; any indeterminate criterion yields `UNCLASSIFIED`.
- `ANY_CRITERION`: any satisfied criterion yields `FRONTIER`; all determinate unsatisfied criteria yield `NOT_FRONTIER`; otherwise an indeterminate criterion yields `UNCLASSIFIED`.

## Separate execution and review posture

Classification is not a runtime or governance decision. The packet therefore records separate posture fields:

| Classification | Execution posture | Review posture |
|---|---|---|
| `FRONTIER` / `NOT_FRONTIER` | `CALCULATED` | `REVIEW_CANDIDATE` |
| `UNCLASSIFIED` | `ABSTAIN` | `HOLD` |

`REVIEW_CANDIDATE` is not approval. Every calculated result retains a human-review obligation and an explicit no-publication obligation.

## Criterion trace

Every declared criterion has exactly one trace. A trace preserves:

- the criterion key, indicator reference, comparison operator, and threshold-policy reference from `FrontierDefinition`;
- the panel observation reference, observation identity/digest, observation kind, source-role reference, and source-role value;
- observation lifecycle posture;
- uncertainty reference and admitted posture;
- exact EvidenceRef and EvidenceBundle identity posture;
- same-version or crosswalk-backed geography alignment;
- county-year and definition-interval alignment;
- a finite comparison state: `SATISFIED`, `UNSATISFIED`, or `INDETERMINATE`;
- canonical reason codes.

Threshold values, observation values, uncertainty interval values, raw source rows, evidence-store internals, and sensitive details are not copied into the classification packet.

## Fail-closed rules

A criterion must be `INDETERMINATE` when any required support is not exact and admitted, including:

- panel observation missing or suppressed;
- observation stale, superseded, withdrawn, or corrected without accepted current lineage;
- source-role reference/value mismatch;
- unresolved geography alignment, missing or mismatched crosswalk, or time mismatch;
- missing EvidenceRef, unresolved bundle, bundle membership mismatch, or bundle identity mismatch;
- missing, unresolved, excessive-width, mismatched, or threshold-crossing uncertainty;
- missing, mismatched, time-invalid, or not-admitted threshold-policy fixture support.

A malformed assessment, dependency binding, derived trace, classification output, correction lineage, or deterministic identity is denied by the validator rather than reinterpreted as a classification.

## Identity

`spec_hash` is the SHA-256 digest of RFC 8785 canonical JSON over the assessment identity projection.

The projection excludes:

- `assessment_id`;
- `spec_hash`;
- `metadata.generated_at`.

All semantic inputs, criterion traces, classification, posture, lineage, and governance fields remain identity-bearing. The identifier is:

```text
kfm:frontier-classification:<64 lowercase hex characters>
```

Changing only `metadata.generated_at` does not change identity. Changing semantic content does.

## Correction lineage

An original assessment has no predecessor, correction record, or corrected-input references.

A corrected assessment:

- is a new immutable assessment with a new identity;
- retains a digest-bound `supersedes_assessment_ref`;
- retains a digest-bound `correction_record_ref`;
- identifies corrected input references;
- must not supersede itself;
- does not overwrite or delete its predecessor.

## Synthetic fixture registry

The initial validator materializes one closed synthetic domain fixture. Its local registry contains only the exact resources needed for replay:

- one inactive synthetic frontier definition;
- one synthetic county/year panel with the existing four observation slots;
- validated synthetic access and population observations;
- exact geography and optional crosswalk support;
- exact uncertainty resources;
- exact EvidenceRefs and EvidenceBundles;
- exact threshold-policy fixture resources.

The registry is in-memory, deterministic, finite, and unreachable through any public API. It performs no discovery, network access, model invocation, source activation, or lifecycle write.

## Validation outcomes

Validator outcomes remain distinct from classification values:

| Validator outcome | Meaning |
|---|---|
| `PASS` | The synthetic packet is schema-valid, dependency-valid, identity-valid, and exactly derived. A `PASS` packet may still be `UNCLASSIFIED`. |
| `DENY` | The packet, dependency binding, trace, result, identity, or lineage is invalid or tampered. |
| `ERROR` | The bounded fixture registry or validator dependency could not be evaluated safely. |

## Explicit non-effects

This contract and its validator do not:

- classify any real county;
- activate or fetch a source;
- use network or model calls;
- change a threshold or policy;
- expose internal evidence stores;
- write lifecycle state;
- approve review, promotion, or release;
- publish or deploy;
- produce public API or map output.

## Validation surface

```bash
python -m unittest -v tests.validators.evidence.test_validate_frontier_classification
python tools/validators/evidence/validate_frontier_classification.py --fixtures
python tools/validators/evidence/validate_frontier_classification.py --case all_criteria_frontier
```

The bounded workflow also runs the adjacent `FrontierDefinition`, `CountyYearPanel`, `GeographyVersion`, `AccessObservation`, and `PopulationObservation` suites.
