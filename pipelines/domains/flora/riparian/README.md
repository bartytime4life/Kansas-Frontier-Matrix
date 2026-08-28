<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-flora-riparian-readme
title: Flora Riparian Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <flora-pipeline-owner>
  - <flora-domain-steward>
  - <riparian-steward>
  - <hydrology-domain-steward>
  - <habitat-domain-steward>
  - <soil-domain-steward>
  - <hazards-domain-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-riparian-flora-and-geoprivacy-gates
path: pipelines/domains/flora/riparian/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/flora/README.md
  - pipelines/domains/flora/ingest/README.md
  - pipelines/domains/flora/normalize/README.md
  - pipelines/domains/flora/catalog/README.md
  - pipelines/domains/flora/redact/README.md
  - pipelines/cross_lane/riparian_vegetation/README.md
  - docs/domains/flora/README.md
  - docs/domains/flora/DATA_LIFECYCLE.md
  - docs/domains/flora/CROSSWALKS.md
  - docs/domains/flora/SENSITIVITY_POSTURE.md
  - docs/domains/habitat/cross-domain.md
  - docs/domains/hydrology/README.md
  - pipeline_specs/flora/riparian.yaml
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
  - riparian
  - riparian-vegetation
  - wetland-plants
  - stream-corridor
  - floodplain
  - vegetation-community
  - hydrology-context
  - habitat-context
  - cross-lane
  - source-role
  - evidence-bundle
  - geoprivacy
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/flora/riparian path as a nested executable Flora riparian sublane."
  - "Flora riparian logic is executable Flora-domain support only; it does not own Hydrology truth, Habitat truth, Soil truth, Hazards truth, cross-lane truth, source descriptors, schemas, policy, catalog truth, release decisions, or public API authority."
  - "The existing cross-lane riparian vegetation pipeline remains the cross-lane composition lane; this path is Flora-owned and prepares plant-centered riparian candidates and handoffs."
  - "Riparian plant candidates compose Flora records with Hydrology/Habitat/Soil/Hazards context without turning context joins into botanical truth or public release."
  - "Controlled Flora records, steward-reviewed material, rights-unclear material, and join-sensitive context fail closed until evidence, policy, review, transform receipt, correction path, and rollback target are present."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Riparian Pipeline

> Executable Flora sublane for preparing plant-centered riparian vegetation candidates, wetland/stream-corridor plant context, quarantine records, normalized records, catalog/triplet handoffs, receipts, and release-review packages from admitted Flora records and governed cross-lane context — while preserving Flora ownership, Hydrology/Habitat/Soil/Hazards ownership, source roles, EvidenceBundle refs, geoprivacy posture, correction paths, and rollback targets.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-flora%20riparian-2e7d32)
![authority](https://img.shields.io/badge/authority-flora%20sublane%20only-0a7ea4)
![cross--lane](https://img.shields.io/badge/cross--lane-context%20only-455a64)
![geoprivacy](https://img.shields.io/badge/geoprivacy-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/flora/riparian/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Flora  
**Sublane:** Riparian / stream-corridor plant context  
**Placement posture:** nested executable sublane under `pipelines/domains/flora/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; riparian outputs require lifecycle, EvidenceBundle, source-role, geoprivacy/sensitivity transform, cross-lane ownership refs, review, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Riparian anti-collapse rules](#3-riparian-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Riparian scope](#6-riparian-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal riparian flora candidate record](#11-minimal-riparian-flora-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/flora/riparian/` is the executable sublane for Flora-owned riparian vegetation and stream-corridor plant-context processing.

It supports candidate processing for:

- riparian `FloraOccurrence`, `VegetationCommunity`, `PlantTaxon`, `Specimen`, `InvasivePlantRecord`, restoration, phenology, and range/distribution context;
- stream-adjacent, wetland-adjacent, floodplain-adjacent, spring/seep, oxbow, gallery forest, cottonwood/willow corridor, prairie stream, and other riparian plant-context candidates;
- Hydrology refs such as streams, reaches, watersheds, wetlands, floodplain context, water-level context, or flow-context refs without becoming Hydrology truth;
- Habitat refs such as land cover, ecological systems, habitat patches, corridors, restoration areas, or suitability outputs without becoming Habitat truth;
- Soil, Hazards, Agriculture, Fauna, and Infrastructure context refs where source roles, evidence, policy, and ownership are preserved;
- vegetation-stress, burn/flood/drought/freeze recovery, invasive pressure, and restoration-readiness candidates where reviewed and evidence-bound;
- quarantine records for missing taxon identity, unresolved Hydrology/Habitat refs, source-role collapse, unsupported riparian classification, rights uncertainty, geoprivacy risk, stale context, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of Flora riparian candidate preparation. It does not fetch source data, define source descriptors, decide taxonomy, define schemas, encode policy, decide geoprivacy, own Hydrology/Habitat/Soil/Hazards truth, replace the cross-lane riparian vegetation pipeline, decide release, or publish public API/map payloads.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/flora/`? | Flora is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `riparian/`? | This is a narrow executable sublane for Flora-owned riparian plant candidates and handoffs. | PROPOSED / NEEDS VERIFICATION |
| How is this different from `pipelines/cross_lane/riparian_vegetation/`? | The cross-lane path composes multiple domains. This path is Flora-owned and must preserve cross-lane refs instead of owning them. | CONFIRMED adjacent boundary / PROPOSED implementation |
| Does this own Hydrology or Habitat truth? | No. It may reference governed Hydrology/Habitat records only by stable refs and source-role-preserving context. | CONFIRMED boundary posture |
| Can this sublane publish? | No. It may prepare reviewable handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Riparian Flora output is not a stream boundary, wetland determination, floodplain determination, habitat-patch truth, restoration approval, hazards risk, or public botanical release. It is Flora-centered context that must carry source roles, owning-domain refs, evidence, policy, correction, and rollback refs.

[⬆ Back to top](#top)

---

## 3. Riparian anti-collapse rules

Riparian processing must preserve Flora ownership, cross-lane ownership, source role, evidence state, geoprivacy state, and release state.

Disallowed collapses:

```text
riparian flora candidate -> Hydrology truth
riparian flora candidate -> HabitatPatch
riparian vegetation signal -> wetland determination
stream proximity -> Flora occurrence truth
floodplain context -> hazards risk
soil moisture context -> plant condition truth
remote-sensing vegetation signal -> taxon occurrence
restoration context -> restoration approval
cross-lane candidate -> public layer
catalog record -> public artifact
generated summary -> evidence
pipeline run -> release approval
```

Required distinctions:

- Flora object refs, Hydrology refs, Habitat refs, Soil refs, Hazards refs, Agriculture refs, Fauna refs, source role, evidence refs, review refs, and policy refs remain explicit;
- riparian class, stream-adjacent context, wetland-adjacent context, vegetation community, and habitat condition remain distinct object claims;
- cross-lane joins preserve each owning domain's authority and never import another domain's truth into Flora;
- controlled Flora geometry uses public-safe transform state before release-facing artifacts are prepared;
- every public claim resolves evidence or abstains;
- release requires correction path and rollback target.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Flora riparian candidate processing.

Appropriate contents include:

- fixture-only riparian dry-run entrypoints;
- riparian Flora candidate builders;
- plant taxon, occurrence, specimen, vegetation-community, invasive-plant, and phenology context mappers;
- Hydrology/Habitat/Soil/Hazards context reference validators that preserve owning-domain authority;
- stream corridor, wetland-adjacent, floodplain-adjacent, spring/seep, oxbow, and restoration-context candidate builders;
- vegetation-stress and recovery handoff builders that preserve source role and uncertainty;
- geoprivacy/redaction/generalization/aggregation state validators;
- cross-lane ownership validators;
- quarantine routing helpers for missing evidence, stale context, unresolved taxon identity, unsupported riparian classification, or source-role collapse;
- receipt emitters, if not shared;
- handoff helpers for validation, catalog, triplet, and release workflow.

A good placement test:

> If the code transforms admitted Flora records and governed cross-lane refs into reviewable Flora riparian candidates, quarantine records, receipts, or downstream handoff packages, it may belong here. If it defines stream truth, wetland truth, habitat truth, source descriptors, schemas, policy, release decisions, public API output, or public map state, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Cross-lane riparian composition authority | `pipelines/cross_lane/riparian_vegetation/` or approved cross-lane root |
| Hydrology source truth, streams, gauges, floodplain/wetland determinations | Hydrology responsibility roots |
| Habitat patches, suitability, corridors, or ecological-system truth | Habitat responsibility roots |
| Soil measurements, soil map units, and moisture observations | Soil responsibility roots |
| Hazards events, exposure, warnings, or risk truth | Hazards responsibility roots |
| Source fetchers and API clients | `connectors/<source>` or accepted connector home |
| Source descriptors / source registry entries | `data/registry/sources/flora/` or approved registry home |
| Flora doctrine and object meaning | `docs/domains/flora/`, `contracts/domains/flora/` |
| JSON Schemas | `schemas/contracts/v1/domains/flora/` or accepted schema home |
| Policy, rights, sensitivity, geoprivacy, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/flora/...` |
| Fixtures | `fixtures/domains/flora/riparian/` or accepted fixture home |
| Tests | `tests/pipelines/domains/flora/riparian/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Riparian scope

| Scope area | Pipeline responsibility | Failure behavior |
|---|---|---|
| Flora input | Confirm input is processed/work Flora material, fixture, or approved reprocessing material. | Deny or quarantine. |
| Taxon identity | Preserve accepted taxon refs, synonyms, authority refs, and uncertainty. | Abstain or quarantine on unresolved identity. |
| Cross-lane refs | Preserve Hydrology/Habitat/Soil/Hazards/Fauna/Agriculture refs as context. | Deny if join becomes truth transfer. |
| Riparian classification | Preserve method, confidence, time, and source-role state. | Quarantine if unsupported. |
| Evidence | Resolve EvidenceBundle refs for claim-bearing records. | Abstain or quarantine if unresolved. |
| Geoprivacy | Preserve source geometry protection and public transform refs. | Deny release-facing handoff if unresolved. |
| Freshness | Preserve source-vintage, hydrology/hazards context freshness, and review age. | Mark stale or quarantine. |
| Release readiness | Check correction path and rollback target expectations. | Deny release handoff if missing. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Flora riparian run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, admitted Flora work/processed records, cross-lane context refs, public-safe transform refs, EvidenceBundle refs, review records, policy decisions, correction refs, and rollback refs.
2. **Validate** taxon identity, source role, riparian method, cross-lane ownership, evidence closure, geoprivacy, sensitivity, rights, review state, policy outcome, source freshness, correction path, and rollback target.
3. **Emit** Flora riparian candidates, quarantine records, receipts, catalog/triplet handoff refs, or release-candidate handoff packages into accepted lifecycle homes.
4. **Quarantine** missing EvidenceBundle, missing source role, unresolved taxon identity, unsupported riparian class, unresolved cross-lane ref, stale context, unresolved geoprivacy, rights failure, policy failure, schema drift, or cross-lane ownership collapse.
5. **Support release** only by providing reviewable handoff packages to release workflow.
6. **Never publish directly.**

Riparian Flora processing is a governed lifecycle transformation. It is not hydrology mapping, habitat modeling, catalog closure, or publication.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Flora riparian run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is approved fixture, admitted Flora WORK, PROCESSED, or reviewable remediation material.
2. **Taxon identity gate** — accepted taxon refs, synonym refs, authority refs, and uncertainty are explicit.
3. **Source-role gate** — occurrence, specimen, community, model, aggregate, remote-sensing, and generated-context records remain distinct.
4. **Cross-lane ownership gate** — Hydrology, Habitat, Soil, Hazards, Fauna, Agriculture, and Infrastructure refs remain owning-domain context.
5. **Riparian method gate** — stream/wetland/floodplain proximity and vegetation classification method refs are explicit.
6. **EvidenceBundle gate** — claim-bearing records resolve EvidenceBundle support or abstain.
7. **Geoprivacy gate** — controlled Flora records have withheld/generalized/aggregated/staged/denied posture where needed.
8. **Freshness/stale gate** — stale Hydrology/Habitat/Hazards/remote-sensing context is surfaced and handled.
9. **Policy/review gate** — finite policy outcome and review state exist; no silent allow.
10. **Schema/contract gate** — candidates match accepted Flora and cross-lane context contract shapes.
11. **Correction/rollback gate** — release-facing handoff includes correction path and rollback target expectations.
12. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests as a pipeline side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/flora/riparian/
├── README.md                         # this file
├── RIPARIAN_CONTRACT.md              # PROPOSED: Flora riparian execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized/redacted fixture only
├── build_riparian_candidate.py       # PROPOSED
├── validate_taxon_identity.py        # PROPOSED
├── validate_hydrology_refs.py        # PROPOSED
├── validate_habitat_refs.py          # PROPOSED
├── validate_cross_lane_ownership.py  # PROPOSED
├── validate_riparian_method.py       # PROPOSED
├── validate_geoprivacy.py            # PROPOSED
├── validate_freshness.py             # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/flora/riparian.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/flora/`, `data/quarantine/flora/`, `data/processed/flora/`, `data/catalog/domain/flora/`, `data/triplets/flora/`, `data/receipts/`, `data/proofs/`, and `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/flora/riparian/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Flora input | `data/work/flora/`, `data/processed/flora/` | Validated or reviewable Flora objects only. |
| Cross-lane context refs | Hydrology/Habitat/Soil/Hazards catalog or processed refs | Referenced only; not owned here. |
| Riparian candidate | `data/work/flora/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/flora/<reason>/<run_id>/` | Failed, stale, restricted, unresolved, or unsafe material. |
| Catalog/triplet handoff | `data/catalog/domain/flora/`, `data/triplets/flora/` | Projection refs only; not publication. |
| Receipt | `data/receipts/pipeline/flora/riparian/<run_id>.yml` or accepted receipt home | Records inputs, cross-lane refs, checks, evidence, outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` | Required for claim-bearing records. |
| Release handoff | `release/candidates/flora/` | Reviewable, release-gated output only. |

[⬆ Back to top](#top)

---

## 11. Minimal riparian flora candidate record

The final schema is not defined here. This example shows the minimum information a Flora riparian candidate should preserve.

```yaml
schema_version: kfm.flora_riparian_candidate.v1
candidate_id: flora_riparian_<flora_object_id>_<context_hash>
pipeline_id: domains.flora.riparian
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <RiparianFloraContext|RiparianVegetationCommunity|RiparianOccurrenceContext|RiparianRestorationContext>
flora_object:
  object_ref: data/processed/flora/<dataset_id>/<version>/
  object_family: <PlantTaxon|FloraOccurrence|Specimen|VegetationCommunity|InvasivePlantRecord|PhenologyObservation>
  accepted_taxon_ref: null
cross_lane_context:
  hydrology_refs: []
  habitat_refs: []
  soil_refs: []
  hazards_refs: []
  agriculture_refs: []
  owning_domain_refs_preserved: true
riparian_method:
  method_id: null
  confidence: needs_review
  source_vintage: null
  freshness_state: needs_review
spatial_privacy:
  original_geometry_state: restricted
  public_geometry_state: <withheld|generalized|aggregated|staged|denied|public|not_applicable>
  public_safe_transform_ref: null
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
policy:
  outcome: ABSTAIN
  review_ref: null
anti_collapse:
  riparian_context_is_hydrology_truth: false
  riparian_context_is_habitat_truth: false
  remote_sensing_signal_is_occurrence_truth: false
  cross_lane_context_is_public_release: false
  generated_summary_is_evidence: false
outputs:
  candidate_record_ref: data/work/flora/run_YYYYMMDDThhmmssZ/riparian_candidate.yml
  receipt_ref: data/receipts/pipeline/flora/riparian/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until Flora riparian specs, cross-lane fixtures, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/flora/riparian/
├── test_no_network_dry_run.py              # PROPOSED
├── test_flora_input_required.py            # PROPOSED
├── test_hydrology_refs_remain_context.py   # PROPOSED
├── test_habitat_refs_remain_context.py     # PROPOSED
├── test_cross_lane_ownership_preserved.py  # PROPOSED
├── test_riparian_method_required.py        # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_controlled_flora_geoprivacy_required.py # PROPOSED
├── test_remote_sensing_not_occurrence_truth.py # PROPOSED
├── test_freshness_state_required.py        # PROPOSED
├── test_policy_review_required.py          # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, Flora inputs and cross-lane refs are required, Hydrology/Habitat ownership is preserved, riparian method refs are explicit, controlled Flora geometry fails closed, stale context is surfaced, receipts are deterministic, and no run writes directly to public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Flora riparian pipelines may prepare candidates and handoff packages. They do not publish.

Required chain:

```text
Flora object + governed cross-lane context refs
  -> Flora riparian candidate
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

- denied, abstained, errored, stale, restricted, conflicted, and quarantined riparian runs remain auditable;
- receipts preserve Flora refs, Hydrology/Habitat/Soil/Hazards refs, freshness refs, source-role refs, evidence refs, geoprivacy refs, review refs, policy outcomes, and failure reasons;
- riparian candidates are superseded by governed state transition, not hidden overwrite;
- downstream artifacts are invalidated if Flora refs, cross-lane refs, EvidenceBundle refs, freshness refs, geoprivacy refs, policy refs, review refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/flora/riparian/README.md` file;
- identifies this directory as a nested executable Flora riparian sublane;
- preserves the boundary between Flora-owned riparian candidates and cross-lane riparian vegetation composition;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, Hydrology truth, Habitat truth, Soil truth, Hazards truth, public API, UI, geoprivacy decision, and release authority from being placed here;
- preserves Flora object, cross-lane context refs, source-role, freshness, taxon identity, EvidenceBundle, geoprivacy, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks Flora-context-as-Hydrology-truth, Flora-context-as-Habitat-truth, remote-sensing-as-occurrence-truth, cross-lane-candidate-as-public-release, generated-summary-as-evidence, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has processed-fixture coverage, cross-lane fixture refs, schema-backed candidates, contract conformance, taxon/evidence/source-role/geoprivacy/freshness/cross-lane/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `FLORA-RIP-001` | Should Flora riparian execution remain a Flora sublane, move fully to `pipelines/cross_lane/riparian_vegetation/`, or stay split as Flora-owned candidate prep plus cross-lane composition? | NEEDS VERIFICATION / ADR |
| `FLORA-RIP-002` | Which Hydrology/Habitat/Soil/Hazards reference types are allowed as inputs before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `FLORA-RIP-003` | Which schema owns RiparianFloraContext, RiparianVegetationCommunity, and quarantine reason codes? | NEEDS VERIFICATION |
| `FLORA-RIP-004` | Which first-wave fixture should be used: synthetic riparian corridor, KGS/KBS plant record, NWI-adjacent plant community, or land-cover-derived riparian surface? | NEEDS VERIFICATION |
| `FLORA-RIP-005` | Which CI job owns Flora riparian invariant tests? | UNKNOWN |
| `FLORA-RIP-006` | Which geoprivacy receipt format is required before controlled riparian Flora joins can become release candidates? | NEEDS VERIFICATION / ADR |
| `FLORA-RIP-007` | Should shared riparian methods live here, in the cross-lane riparian pipeline, or in a package under a governed cross-lane method root? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Start with synthetic/generalized/redacted fixture-only dry runs and negative tests. Do not add live source fetching, Hydrology/Habitat truth authority, schema authority, policy authority, geoprivacy-decision authority, direct public API code, direct UI code, release-manifest writes, public layer writes, or generated riparian summaries until source roles, cross-lane ownership, taxon identity, EvidenceBundle closure, public-safe transforms, freshness, review state, release review, and rollback are proven.
