<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/briefing-classification-release-source-map
title: Briefing ClassificationRelease Source Map
type: exploratory-source-map
version: v0.1.0
status: draft; PROPOSED adaptation; non-authoritative
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; common; classification; no-authority
owning_root: docs/
responsibility: Record the bounded adaptation from the briefing-to-system conditions backlog into an inactive ClassificationRelease profile and an evidence-backed follow-on queue.
truth_posture: "CONFIRMED source/repository inspection; PROPOSED implementation adaptation; NEEDS VERIFICATION human review, hosted CI, and future operational design"
related:
  - ../../../contracts/common/classification_release.md
  - ../../../schemas/contracts/v1/common/classification_release.schema.json
  - ../../../contracts/common/condition_relation.md
  - ../../../contracts/domains/soil/domain_observation.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, exploratory, briefing, classification, observation, conditions]
[/KFM_META_BLOCK_V2] -->

# Briefing ClassificationRelease Source Map

## Goal

Continue the briefing-to-system implementation sequence with the smallest dependency-closed conditions-lane slice while avoiding a second observation authority.

## Source requirements

The briefing architecture's Phase 4 conditions framework names four object families:

1. `ClassificationRelease`;
2. `ObservationSeries` / `ObservationRecord`;
3. `ForecastProduct`;
4. `ConditionRelation`.

Its P2 backlog pairs `ClassificationRelease` and `ObservationRecord` as a USDM/Mesonet source-role reference. The same source defines a station observation model and a distinct broad classification-release model. It requires synthetic, no-network modeling before live adapters, public APIs, MapLibre layers, dashboards, or governed AI.

The source is design authority only. It does not prove repository implementation or current source rights.

## Current repository inspection

Inspection base:

```text
main@1001a87233e0f23695b6b12e60c654f938e6ffb5
```

CONFIRMED from current repository evidence:

- `contracts/common/condition_relation.md`, its schema, fixtures, validator, and tests already preserve classification/observation/forecast roles and deny causality.
- `OfficialSourceSnapshotCandidate` and `OfficialSourceSnapshotLineageAssessment` already provide immutable no-network source-capture and finite correction/supersession/conflict carriers.
- domain-owned `DomainObservation` profiles already exist across multiple lanes.
- the soil profile is closed and executable; its committed valid fixture models a synthetic Kansas Mesonet-style station soil-moisture observation.
- repository search found no current `classification_release` file and no open pull request for this exact object family.
- repository search found no current `ForecastProduct`, `ClaimFieldBinding`, or `ReleaseEvidenceIndex` object family.
- water-planning `ProgramVersion` already exists, so a future funding slice should extend the outcome chain rather than duplicate that model.

## Adaptation decision

The bounded implementation is:

```text
ClassificationRelease source requirement
  -> common semantic contract
  -> closed Draft 2020-12 schema
  -> four positive lineage bases
  -> isolated semantic and identity mutations
  -> deterministic no-network validator
  -> focused tests
  -> existing Mesonet-style observation boundary test
  -> read-only workflow
  -> byte-bound generated authoring receipt
```

This packet intentionally does **not** create a common `ObservationRecord`. The existing domain observation profiles are the current repository implementation evidence. The cross-domain test proves that a broad classification and a soil station observation pass only their own profiles.

## Implemented acceptance boundary

The packet proves locally:

- `CLASSIFICATION` and `DERIVED_CLASSIFICATION` are mandatory;
- point scale is denied for a broad classification release;
- source cutoff, validity, release, retrieval, correction, and supersession are distinct;
- resolved and unresolved geometry states fail closed;
- current, corrected, superseded, and conflicted lineage states are explicit;
- arrays and deterministic identity are canonical;
- release, public use, and all trust-bearing effects remain false;
- the existing Mesonet-style station candidate cannot substitute for a classification candidate.

It does not prove live USDM or Mesonet source state, source rights, currentness, evidence closure, policy, review, release, or publication.

## Sourced next implementation candidates

| Order | Candidate | Source basis | Current repo reconciliation | Proposed review boundary |
|---:|---|---|---|---|
| 1 | `ForecastProduct` fixture profile | Phase 4 conditions framework; forecast/observation anti-collapse examples | No current `ForecastProduct` file found | One common contract/schema/fixtures/validator/test packet; no live NWS adapter |
| 2 | `ClaimFieldBinding` | Evidence-binding table requires object field, native statement, normalized value, EvidenceRef, transform, and confidence | No current object found | Evidence-plane candidate with exact field-pointer and transform-receipt negatives |
| 3 | Conditions role-crosswalk matrix | Phase 4 exit condition requires USDM/Mesonet source-role and scale separation | Classification, soil observation, and ConditionRelation components exist after this packet | Test-only matrix before another shared object family |
| 4 | `GovernanceEvent` fixture profile | Phase 5 and Lane D require meeting, comment, recommendation, decision, and implementation separation | Exact object not found; TemporalAuthorityEnvelope mentions the concept only | Separate governance-event contract packet; no calendar connector |
| 5 | Water-planning outcome-chain integrity | Program-to-outcome backlog | `ProgramVersion` and related water-planning contracts already exist | Validator/negative-fixture extension, not a duplicate ProgramVersion |
| 6 | `ReleaseEvidenceIndex` | Evidence-binding table and Phase 6 release requirements | No current object found | HOLD until evidence, policy, review, release, correction, and rollback reference families are selected |
| 7 | Conditions Explorer public projection | Phase 7 public products | UI/map release depends on completed release-safe projections | HOLD until release-neutral objects graduate through governed release |

## Deliberate holds

This slice does not:

- fetch or activate USDM, Kansas Mesonet, NWS, or another source;
- select current source endpoints, licenses, terms, cadence, or redistribution rights;
- create an EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, or public artifact;
- add a public route, map source, layer, search index, graph edge, alert, dashboard, or AI answer;
- move or replace domain observation contracts;
- treat a fixture, workflow, commit, or pull request as promotion or publication.

## Directory Rules basis

ADR-0029 accepts Directory Governance Standard v2. The packet uses established responsibility roots only: `contracts/`, `schemas/`, `fixtures/`, `tools/`, `tests/`, `.github/`, `docs/intake/exploratory/`, and `data/receipts/generated/`. No new root or parallel authority is introduced.

## Correction and rollback

Before merge, discard the additive patch. After an authorized merge, revert the packet. The source requirement remains visible as proposal pressure, and the existing observation/condition families remain intact. No live or public state requires rollback.
