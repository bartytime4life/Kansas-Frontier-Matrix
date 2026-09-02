<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-flora-hazards-readme
title: Flora Hazards Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <flora-pipeline-owner>
  - <flora-domain-steward>
  - <hazards-domain-steward>
  - <habitat-domain-steward>
  - <agriculture-domain-steward>
  - <evidence-steward>
  - <geoprivacy-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-rare-flora-and-life-safety-gates
path: pipelines/domains/flora/hazards/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/flora/README.md
  - pipelines/domains/hazards/README.md
  - pipelines/biodiversity/vegetation_stress/README.md
  - docs/domains/flora/README.md
  - docs/domains/flora/DATA_LIFECYCLE.md
  - docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - docs/domains/flora/SOURCES.md
  - docs/domains/flora/SOURCE_FAMILIES.md
  - docs/domains/flora/CROSSWALKS.md
  - docs/domains/flora/PRESERVATION_MATRIX.md
  - docs/domains/hazards/ARCHITECTURE.md
  - docs/domains/hazards/DATA_LIFECYCLE.md
  - pipeline_specs/flora/hazards.yaml
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - data/raw/flora/
  - data/work/flora/
  - data/quarantine/flora/
  - data/processed/flora/
  - data/catalog/domain/flora/
  - data/triplets/flora/
  - data/published/layers/flora/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/flora/
  - release/manifests/flora/
tags:
  - kfm
  - pipelines
  - domains
  - flora
  - hazards
  - drought
  - wildfire
  - smoke
  - flood
  - heat
  - freeze
  - vegetation-stress
  - phenology-anomaly
  - invasive-plants
  - life-safety-boundary
  - geoprivacy
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/flora/hazards path as a nested executable Flora hazards-context sublane."
  - "Flora hazards logic is executable Flora-domain support only; it does not own Hazards truth, emergency alerts, official warnings, life-safety instructions, source descriptors, schemas, policy, lifecycle data, catalog truth, geoprivacy decisions, or release decisions."
  - "The lane prepares Flora-centered hazard-context candidates such as drought response, burn recovery, flood impact, freeze injury, heat stress, smoke/ash context, phenology anomaly, invasive pressure, and vegetation-stress handoffs."
  - "Hazard event, warning, declaration, exposure, and risk authority stays in the Hazards domain; Flora may link to it only as governed context."
  - "Rare, protected, culturally sensitive, steward-reviewed, join-sensitive, and unresolved flora records fail closed until geoprivacy, evidence, review, policy, correction, and rollback closure are present."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Hazards Pipeline

> Executable Flora sublane for preparing governed Flora-centered hazard-context candidates, vegetation-stress handoffs, quarantine records, normalized records, catalog/triplet handoffs, receipts, and release-review packages from admitted Flora and hazard-context evidence — without becoming a Hazards-domain source of truth, emergency alert system, life-safety authority, geoprivacy authority, or public release path.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-flora%20hazards%20context-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20context%20logic-0a7ea4)
![life-safety](https://img.shields.io/badge/life--safety-not%20an%20alert%20system-d62728)
![geoprivacy](https://img.shields.io/badge/rare%20flora-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/flora/hazards/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Flora  
**Sublane:** Hazards context / vegetation stress / plant-impact candidates  
**Placement posture:** nested executable sublane under `pipelines/domains/flora/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication and no life-safety alerting; public output requires lifecycle, EvidenceBundle, source-role, geoprivacy/sensitivity transform, Hazards-domain context refs, review, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Flora-hazards anti-collapse rules](#3-flora-hazards-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Flora-hazards scope](#6-flora-hazards-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal flora-hazards candidate record](#11-minimal-flora-hazards-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/flora/hazards/` is the executable sublane for Flora-centered hazards context and plant-impact candidate processing.

It supports candidate processing for:

- drought response and drought-stress context for plant occurrences, vegetation communities, restoration sites, and public-safe botanical surfaces;
- wildfire, prescribed-fire, burn-scar, and burn-recovery context where admitted and evidence-bound;
- flood, inundation, sedimentation, ice, freeze, hail, wind, heat, smoke, ash, pest/disease-pressure, and other hazard-context links that affect Flora objects;
- phenology anomaly, vegetation-stress, invasive-pressure, and post-disturbance recovery candidates;
- links from Flora records to Hazards-domain event, observation, warning-context, declaration, exposure, or modeled derivative records without taking ownership of Hazards truth;
- public-safe generalized summaries for plant-impact context where release policy permits;
- quarantine records for missing EvidenceBundle, unresolved taxon identity, unresolved hazard-context ref, stale warning/expiry context, source-role collapse, unresolved geoprivacy, rights uncertainty, policy failure, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of Flora hazards-context processing. It does not fetch source data, normalize raw hazard events, define Flora or Hazards object meaning, define schemas, encode policy, decide geoprivacy, issue warnings, provide life-safety instructions, own Hazards truth, decide release, or publish public API/map payloads.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/flora/`? | Flora is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `hazards/` here? | This is a Flora-owned sublane for plant-impact and vegetation-stress context, not Hazards-domain truth. | PROPOSED / NEEDS VERIFICATION |
| Does this own Hazards source truth? | No. Hazards event, observation, warning, declaration, exposure, and risk records remain Hazards-owned. | CONFIRMED boundary posture |
| Does this own geoprivacy decisions? | No. It consumes geoprivacy/policy/review outputs and fails closed when unresolved. | CONFIRMED Flora posture |
| Can this sublane publish or alert? | No. It may prepare reviewable handoffs only; it is not a public release or life-safety alert lane. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Flora hazards outputs are context candidates, not official hazard determinations, emergency alerts, drought declarations, crop-loss findings, habitat truth, or public botanical release. They must carry Flora object refs, Hazards context refs, evidence, freshness, geoprivacy, policy, correction, and rollback refs.

[⬆ Back to top](#top)

---

## 3. Flora-hazards anti-collapse rules

Flora hazards processing must preserve Flora ownership, Hazards ownership, source role, freshness/expiry, evidence state, and release state.

Disallowed collapses:

```text
flora hazard-context candidate -> Hazards event truth
vegetation stress signal -> emergency alert
drought response candidate -> drought declaration
burn-recovery candidate -> wildfire incident truth
flood-impact candidate -> flood warning
smoke/heat context -> health/safety instruction
phenology anomaly -> taxon status change
invasive pressure -> regulatory invasive determination
hazard context join -> exact rare-plant geometry exposure
public-safe summary -> raw sensitive occurrence geometry
remote-sensing anomaly -> plant occurrence truth
generated summary -> evidence
pipeline run -> release approval
```

Required distinctions:

- Flora object refs, Hazards context refs, source role, source vintage, observation time, valid time, issue/expiry time, retrieval time, processing time, and release time remain distinct;
- hazard context remains context unless Hazards-owned records support it;
- vegetation-stress, burn-recovery, drought-response, and phenology-anomaly outputs remain candidates until validated and reviewed;
- rare/protected/culturally sensitive Flora geometry remains withheld, generalized, aggregated, staged, or denied unless policy permits a public-safe derivative;
- every public claim resolves evidence or abstains;
- release requires correction path and rollback target.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Flora hazards-context processing.

Appropriate contents include:

- fixture-only dry-run entrypoints;
- Flora hazard-context candidate builders;
- vegetation-stress, drought-response, fire/burn-recovery, flood-impact, freeze/heat, smoke/ash, pest/disease-pressure, invasive-pressure, and phenology-anomaly handoff builders;
- Hazards-context reference validators that preserve Hazards ownership;
- freshness/expiry validators for operational-warning context, when present;
- geoprivacy, redaction, generalization, aggregation, and public-safe transform validators;
- cross-lane ownership validators for Habitat, Agriculture, Hydrology, Hazards, Fauna, Soil, and Infrastructure refs;
- quarantine routing helpers for missing hazard refs, stale context, missing evidence, unresolved geoprivacy, policy failure, or source-role collapse;
- receipt emitters, if not shared;
- handoff helpers for validation, catalog, triplet, and release workflow.

A good placement test:

> If the code transforms processed Flora records and admitted Hazards context refs into reviewable Flora hazard-impact candidates, quarantine records, receipts, or downstream handoff packages, it may belong here. If it issues warnings, owns hazard event truth, fetches hazard sources, defines schemas, decides policy/geoprivacy/release, writes public artifacts, or serves API/map payloads, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Hazard event, warning, declaration, exposure, or risk source processing | `pipelines/domains/hazards/` and Hazards responsibility roots |
| Emergency alerting, watch/warning/advisory instructions, life-safety text | Official sources and Hazards context only; not KFM Flora pipelines |
| Source fetchers / connectors | `connectors/<source>` or accepted connector home |
| Source descriptors / source registry entries | `data/registry/sources/flora/`, `data/registry/sources/hazards/`, or approved registry homes |
| Flora or Hazards doctrine and object meaning | `docs/domains/flora/`, `docs/domains/hazards/`, and `contracts/...` |
| JSON Schemas | `schemas/contracts/v1/domains/flora/`, `schemas/contracts/v1/domains/hazards/`, or accepted schema homes |
| Policy, rights, sensitivity, geoprivacy, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/flora/...` or accepted spec home |
| Fixtures | `fixtures/domains/flora/hazards/` or accepted fixture home |
| Tests | `tests/pipelines/domains/flora/hazards/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Habitat suitability, crop-loss, animal health, soil/hydrology measurements, or infrastructure exposure truth | Owning domain roots |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Flora-hazards scope

| Scope area | Pipeline responsibility | Failure behavior |
|---|---|---|
| Flora input | Confirm input is processed Flora material, fixture, or approved reprocessing material. | Deny or quarantine. |
| Hazards context | Preserve Hazards-owned refs, source role, freshness, and issue/expiry state. | Deny or quarantine on missing/stale refs. |
| Stress signal | Keep vegetation-stress and plant-impact outputs as candidates until validated. | Quarantine if unsupported. |
| Evidence | Resolve EvidenceBundle refs for claim-bearing records. | Abstain or quarantine if unresolved. |
| Geoprivacy | Preserve exact/private geometry protection and public-safe transform refs. | Deny release-facing handoff if unresolved. |
| Cross-lane refs | Preserve owning-domain refs for Habitat/Agriculture/Hydrology/Hazards/Fauna/Soil joins. | Deny if join becomes Flora truth or Hazards truth. |
| Life-safety | Redirect to official sources; never produce instructions or alerts. | Deny publication wording. |
| Release readiness | Check correction path and rollback target expectations. | Deny release handoff if missing. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Flora hazards-context run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, processed Flora records, admitted Hazards context refs, vegetation-stress candidates, validation reports, public-safe transform refs, EvidenceBundle refs, review records, policy decisions, correction refs, and rollback refs.
2. **Validate** Flora identity, source role, Hazards context refs, freshness/expiry, evidence closure, geoprivacy, sensitivity, rights, review state, policy outcome, cross-lane ownership, correction path, and rollback target.
3. **Emit** Flora hazard-context candidates, quarantine records, receipts, catalog/triplet handoff refs, or release-candidate handoff packages into accepted lifecycle homes.
4. **Quarantine** missing EvidenceBundle, missing source role, unresolved taxon identity, unresolved Hazards context ref, stale context, unresolved geoprivacy, rights failure, policy failure, schema drift, or cross-lane ownership collapse.
5. **Support release** only by providing reviewable handoff packages to release workflow.
6. **Never publish directly and never alert.**

[⬆ Back to top](#top)

---

## 8. Required gates

Every Flora hazards-context run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is processed Flora material, fixture-only material, or approved reprocessing material.
2. **Hazards context gate** — Hazards refs exist, remain Hazards-owned, and carry source/freshness/expiry state where applicable.
3. **Validation report gate** — upstream Flora and hazard-context validation refs exist and pass or state a reviewable exception.
4. **EvidenceBundle gate** — claim-bearing records resolve EvidenceBundle support.
5. **Taxon identity gate** — accepted taxon refs, synonym refs, authority refs, and uncertainty are explicit.
6. **Source-role gate** — occurrence/specimen/taxonomic/model/remote-sensing/aggregate/generated/Hazards-context distinctions remain distinct.
7. **Geoprivacy gate** — exact rare/protected/culturally sensitive/steward-reviewed records have withheld/generalized/staged/denied posture.
8. **Policy/review gate** — finite policy outcome and review state exist; no silent allow.
9. **Life-safety gate** — no emergency alert, warning instruction, official source replacement, or safety advice is emitted.
10. **Cross-lane ownership gate** — joins do not become Habitat, Fauna, Soil, Hydrology, Agriculture, Hazards, Archaeology, or People/Land truth.
11. **Schema/contract gate** — candidates match accepted Flora/Hazards context contract shapes.
12. **Correction/rollback gate** — release-facing handoff includes correction path and rollback target expectations.
13. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests as a pipeline side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/flora/hazards/
├── README.md                         # this file
├── HAZARDS_CONTEXT_CONTRACT.md       # PROPOSED: Flora hazards-context execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized/redacted fixture only
├── build_hazard_context_candidate.py # PROPOSED
├── validate_hazards_refs.py          # PROPOSED
├── validate_freshness_expiry.py      # PROPOSED
├── validate_taxon_identity.py        # PROPOSED
├── validate_evidence_refs.py         # PROPOSED
├── validate_geoprivacy.py            # PROPOSED
├── validate_life_safety_boundary.py  # PROPOSED
├── validate_cross_lane_refs.py       # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/flora/hazards.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/flora/`, `data/quarantine/flora/`, `data/processed/flora/`, `data/catalog/domain/flora/`, `data/triplets/flora/`, `data/receipts/`, `data/proofs/`, and `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/flora/hazards/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Processed Flora input | `data/processed/flora/<dataset_id>/<version>/` | Validated normalized objects only. |
| Hazards context ref | `data/processed/hazards/`, `data/catalog/domain/hazards/`, or accepted refs | Referenced only; not owned here. |
| Flora hazard-context candidate | `data/work/flora/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/flora/<reason>/<run_id>/` | Failed, stale, restricted, unresolved, or unsafe material. |
| Catalog/triplet handoff | `data/catalog/domain/flora/`, `data/triplets/flora/` | Projection refs only; not publication. |
| Receipt | `data/receipts/pipeline/flora/hazards/<run_id>.yml` or accepted receipt home | Records inputs, checks, geoprivacy, evidence, outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` | Required for claim-bearing records. |
| Release handoff | `release/candidates/flora/` | Reviewable, release-gated output only. |

[⬆ Back to top](#top)

---

## 11. Minimal flora-hazards candidate record

The final schema is not defined here. This example shows the minimum information a Flora hazards-context candidate should preserve.

```yaml
schema_version: kfm.flora_hazards_context_candidate.v1
candidate_id: flora_hazards_<flora_object_id>_<hazard_context_id>_<hash>
pipeline_id: domains.flora.hazards
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <FloraHazardContext|VegetationStressCandidate|PhenologyAnomalyCandidate|BurnRecoveryCandidate>
flora_object:
  object_ref: data/processed/flora/<dataset_id>/<version>/
  object_family: <PlantTaxon|FloraOccurrence|Specimen|VegetationCommunity|PhenologyObservation|InvasivePlantRecord>
  accepted_taxon_ref: null
hazards_context:
  hazard_ref: null
  hazard_context_type: <drought|fire|flood|heat|freeze|smoke|pest_disease|other>
  hazards_owner: hazards
  issue_time: null
  expiry_time: null
  freshness_state: needs_review
spatial_privacy:
  original_geometry_state: restricted
  public_geometry_state: <withheld|generalized|aggregated|staged|denied|public>
  public_safe_transform_ref: null
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
policy:
  outcome: ABSTAIN
  review_ref: null
anti_collapse:
  flora_hazard_context_is_hazards_truth: false
  vegetation_stress_is_emergency_alert: false
  drought_response_is_drought_declaration: false
  hazard_join_exposes_exact_rare_flora: false
  generated_summary_is_evidence: false
outputs:
  candidate_record_ref: data/work/flora/run_YYYYMMDDThhmmssZ/hazards_context_candidate.yml
  receipt_ref: data/receipts/pipeline/flora/hazards/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until Flora hazards specs, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/flora/hazards/
├── test_no_network_dry_run.py              # PROPOSED
├── test_processed_flora_input_required.py  # PROPOSED
├── test_hazards_context_ref_required.py    # PROPOSED
├── test_hazards_context_remains_hazards_owned.py # PROPOSED
├── test_freshness_expiry_required.py       # PROPOSED
├── test_evidence_bundle_required.py        # PROPOSED
├── test_taxon_identity_required.py         # PROPOSED
├── test_rare_flora_geoprivacy_required.py  # PROPOSED
├── test_no_life_safety_alerting.py         # PROPOSED
├── test_cross_lane_context_not_truth.py    # PROPOSED
├── test_policy_review_required.py          # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, processed Flora inputs and Hazards context refs are required, Hazards ownership is preserved, rare-flora geometry fails closed, stale context quarantines, receipts are deterministic, and no run writes directly to public UI, public API, published layers, release manifests, or life-safety alert surfaces.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Flora hazards-context pipelines may prepare candidates and handoff packages. They do not publish or alert.

Required chain:

```text
processed Flora record + governed Hazards context ref
  -> Flora hazard-context candidate
  -> validation report
  -> EvidenceBundle closure
  -> geoprivacy and policy review
  -> processed Flora context record
  -> catalog / triplet handoff
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, stale, restricted, conflicted, and quarantined hazards-context runs remain auditable;
- receipts preserve Flora refs, Hazards refs, freshness refs, source-role refs, evidence refs, geoprivacy refs, review refs, policy outcomes, and failure reasons;
- hazard-context candidates are superseded by governed state transition, not hidden overwrite;
- downstream artifacts are invalidated if Flora refs, Hazards refs, EvidenceBundle refs, freshness refs, geoprivacy refs, policy refs, review refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/flora/hazards/README.md` file;
- identifies this directory as a nested executable Flora hazards-context sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, Hazards truth, emergency-alert, public API, UI, geoprivacy decision, and release authority from being placed here;
- preserves Flora object, Hazards context, source-role, freshness/expiry, taxon identity, EvidenceBundle, geoprivacy, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks Flora-context-as-Hazards-truth, vegetation-stress-as-alert, drought-response-as-declaration, hazard-join-as-exact-rare-flora-exposure, generated-summary-as-evidence, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has processed-fixture coverage, Hazards-context fixture refs, schema-backed candidates, contract conformance, taxon/evidence/source-role/geoprivacy/freshness/life-safety/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `FLORA-HAZ-001` | Should Flora hazards execution remain one sublane, or split into drought, fire, flood, freeze/heat, pest/disease, and vegetation-stress processors? | NEEDS VERIFICATION / ADR |
| `FLORA-HAZ-002` | Which Hazards-domain reference types are allowed as inputs before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `FLORA-HAZ-003` | Which schema owns FloraHazardContext, VegetationStressCandidate, PhenologyAnomalyCandidate, and quarantine reason codes? | NEEDS VERIFICATION |
| `FLORA-HAZ-004` | Should the existing biodiversity vegetation-stress lane migrate into this Flora domain lane, remain cross-lane, or become a shared adapter? | NEEDS VERIFICATION / ADR |
| `FLORA-HAZ-005` | Which CI job owns Flora hazards-context invariant tests? | UNKNOWN |
| `FLORA-HAZ-006` | Which geoprivacy receipt format is required before rare-flora hazard-context joins can become release candidates? | NEEDS VERIFICATION / ADR |
| `FLORA-HAZ-007` | Which freshness/expiry standard is required for operational Hazards context refs? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized/redacted fixture-only dry runs and negative tests. Do not add live source fetching, Hazards truth authority, schema authority, policy authority, geoprivacy-decision authority, emergency-alert wording, direct public API code, direct UI code, release-manifest writes, public layer writes, or generated botanical hazard summaries until source roles, Hazards ownership, taxon identity, EvidenceBundle closure, geoprivacy transforms, freshness, review state, release review, and rollback are proven.
