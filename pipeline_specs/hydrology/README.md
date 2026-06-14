<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-hydrology-readme
title: Hydrology Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <hydrology-domain-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/hydrology/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipelines/README.md
  - pipelines/domains/hydrology/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - data/registry/sources/hydrology/
  - data/receipts/pipeline/hydrology/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/hydrology/
  - fixtures/pipeline_specs/hydrology/
tags: [kfm, pipeline-specs, hydrology, watershed, huc, gauge, groundwater, water-quality, nfhl, flood-context, declarative-config, receipts, governance]
notes:
  - "This README replaces the short pipeline_specs/hydrology stub with a governed declarative-spec lane contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Hydrology specs configure pipeline intent, source scope, lifecycle gates, temporal/freshness checks, source-role separation, evidence gates, receipts, and release blockers. They do not execute pipeline logic or store lifecycle outputs."
  - "Hydrology is not an emergency flood-warning or life-safety instruction system. Warning-adjacent context must redirect to official sources."
  - "NFHL and comparable regulatory flood context must not collapse into observed inundation."
  - "Concrete spec filenames, schema validation, CI coverage, and activation state remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Pipeline Specs

> Declarative configuration lane for Hydrology pipeline profiles, source scopes, schedules, lifecycle gates, temporal/freshness checks, source-role boundaries, evidence requirements, fixtures, receipts, and release-readiness intent — separate from executable Hydrology pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fdomains%2Fhydrology%2F-d62728)
![anti-collapse](https://img.shields.io/badge/NFHL%20%E2%89%A0%20observed%20flooding-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/hydrology/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion implementation lane:** `pipelines/domains/hydrology/` — executable pipeline logic, the **how**  
**Placement posture:** Hydrology declarative specs belong here unless an ADR or migration note establishes a different accepted spec home.  
**Public posture:** no public release, data storage, flood-warning behavior, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Emergency-warning boundary](#3-emergency-warning-boundary)
- [4. Spec anti-collapse rules](#4-spec-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Hydrology spec scope](#7-hydrology-spec-scope)
- [8. Lifecycle posture](#8-lifecycle-posture)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Spec profile families](#11-spec-profile-families)
- [12. Inputs and outputs](#12-inputs-and-outputs)
- [13. Minimal spec profile shape](#13-minimal-spec-profile-shape)
- [14. Tests, fixtures, and validation](#14-tests-fixtures-and-validation)
- [15. Definition of done](#15-definition-of-done)
- [16. Open questions](#16-open-questions)

---

## 1. Purpose

`pipeline_specs/hydrology/` owns declarative Hydrology pipeline configuration.

It may describe:

- which Hydrology pipeline profile should run;
- which source descriptor ids are in scope;
- which source-family, cadence, observation-time, valid-time, retrieval-time, processing-time, and freshness checks apply;
- which lifecycle gates are required;
- which source-role, regulatory-context, observation/model, topology, and public-safe representation requirements apply;
- which fixtures support no-network tests;
- which receipts, reports, blockers, and review handoffs are expected;
- which downstream implementation lane is authorized to execute the spec.

It does **not** implement pipeline behavior. Hydrology implementation belongs under `pipelines/domains/hydrology/` and related executable lanes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `hydrology/`? | Hydrology has a domain pipeline lane and needs domain-specific run profiles. | CONFIRMED path pattern / NEEDS VERIFICATION for active specs |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define Hydrology objects? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Does this issue warnings or approve release? | No. Specs cannot issue warnings, provide instructions, publish, or approve release. | CONFIRMED boundary posture |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not catalog truth, not an official forecast, not emergency instruction, and not release approval.

[⬆ Back to top](#top)

---

## 3. Emergency-warning boundary

KFM Hydrology specs must preserve the emergency-warning boundary.

Any near-current, flood-context, forecast-adjacent, or operational-context profile must declare:

- official source identity;
- observation time, valid time, retrieval time, and processing time;
- freshness or stale-state classification;
- source role and knowledge-character label;
- non-life-safety posture where an output could be confused with current warning status;
- official-source redirect where current safety information is needed;
- EvidenceBundle or source reference requirements;
- finite policy outcome.

If those fields cannot be proven, the profile must fail closed or route to review/quarantine. Specs must not provide emergency instructions.

[⬆ Back to top](#top)

---

## 4. Spec anti-collapse rules

Disallowed collapses:

```text
spec file -> executable pipeline
spec profile -> release approval
source list -> source authority
schedule -> source freshness proof
gauge reading -> official warning
NFHL zone -> observed inundation
modeled hydrograph -> observation truth
forecast context -> current flood instruction
regulatory context -> observed event
source summary -> EvidenceBundle
generated summary -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- observed gauge readings, regulatory flood context, modeled hydrographs, forecasts, operational context, source observations, and generated summaries remain separately labeled;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include declarative Hydrology specs for:

- source-intake profiles;
- normalization profiles;
- validation profiles;
- catalog and triplet profiles;
- publish-readiness profiles;
- rollback-readiness profiles;
- watcher profiles;
- proof or dry-run profiles;
- watershed, HUC, stream/reach, gauge, groundwater, water-quality, regulatory-flood-context, topology, terrain, hydrostratigraphy, water-use, drought, irrigation, and public-safe map-product variants.

A good placement test:

> If the file answers “what Hydrology pipeline should run, with what source scope, temporal gates, source-role boundaries, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable Hydrology pipeline code | `pipelines/domains/hydrology/` |
| Shared executable helpers | `pipelines/<lane>/` or accepted package/tool home |
| Source connectors | `connectors/<source>` |
| Source descriptors | `data/registry/sources/hydrology/` or accepted registry home |
| Hydrology object meaning | `contracts/domains/hydrology/`, `contracts/hydrology/`, and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy and review decisions | `policy/domains/hydrology/`, `policy/sensitivity/hydrology/`, review roots |
| Tests | `tests/pipeline_specs/hydrology/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/hydrology/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 7. Hydrology spec scope

Hydrology specs may configure profiles for object families and candidate products such as:

- watersheds and HUC units;
- stream, river, reach, waterbody, and hydrographic identity;
- gauge sites and hydrologic observation sites;
- flow, stage, water-level, water-quality, aquifer, groundwater, and hydrograph observations;
- regulatory flood context such as NFHL zones without treating them as observed inundation;
- upstream/downstream traces and topology candidates;
- hydrostratigraphy links and geology-hydrology bridge records;
- water-use, drought, irrigation, habitat, hazards, agriculture, soil, and infrastructure context joins;
- public-safe generalized map products and release-reviewed derivatives.

Hydrology cites other lanes for context. It does not absorb Soil, Agriculture, Geology, Infrastructure, Hazards, Atmosphere, Habitat, or other canonical domain claims.

[⬆ Back to top](#top)

---

## 8. Lifecycle posture

Specs may target lifecycle stages, but do not create the lifecycle transition themselves:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare input lifecycle state, expected output lifecycle state, source descriptor refs, temporal/freshness checks, source-role labels, regulatory-context separation, EvidenceBundle requirements, receipt requirements, release blockers, rollback support, and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 9. Required gates

Every Hydrology spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Temporal/freshness gate** — observation time, valid time, retrieval time, processing time, cadence, and stale-source behavior.
5. **Lifecycle gate** — allowed input and output lifecycle states.
6. **Source-role gate** — observed, modeled, regulatory, forecast-adjacent, operational-context, and generated-summary distinctions.
7. **Emergency-boundary gate** — current-state or flood-context outputs are contextual only and not instruction.
8. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
9. **Receipt gate** — required run, transform, validation, temporal, source-vintage, topology, or release-readiness receipts.
10. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipeline_specs/hydrology/
├── README.md
├── ingest.yaml                    # PROPOSED
├── normalize.yaml                 # PROPOSED
├── validate.yaml                  # PROPOSED
├── catalog.yaml                   # PROPOSED
├── triplets.yaml                  # PROPOSED
├── publish.yaml                   # PROPOSED
├── rollback.yaml                  # PROPOSED
├── watchers.yaml                  # PROPOSED
├── watersheds_huc.yaml            # PROPOSED
├── streams_reaches.yaml           # PROPOSED
├── gauges_observations.yaml       # PROPOSED
├── groundwater.yaml               # PROPOSED
├── water_quality.yaml             # PROPOSED
├── regulatory_flood_context.yaml  # PROPOSED
├── topology_traces.yaml           # PROPOSED
└── hydrostratigraphy.yaml         # PROPOSED
```

These filenames are proposed placeholders until actual spec files and validators are implemented.

[⬆ Back to top](#top)

---

## 11. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/hydrology/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Hydrology normalize implementation |
| `validate` | Declare temporal, source-role, topology, and anti-collapse checks. | Hydrology validate implementation |
| `catalog` | Declare catalog closure requirements. | Hydrology catalog implementation |
| `triplets` | Declare graph/triplet projection profile. | Hydrology triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Hydrology/domain publish support |
| `rollback` | Declare rollback-readiness check profile. | Hydrology/domain rollback support |
| `watchers` | Declare source-change observation profiles. | Hydrology/domain watcher support |
| `object-family` | Declare watershed, stream/reach, gauge, groundwater, water-quality, regulatory context, topology, or hydrostratigraphy variants. | Domain sublane implementations |

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/hydrology/` | Declarative config only. |
| Executable target | `pipelines/domains/hydrology/` or shared pipeline lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/hydrology/` | Read by stable ref. |
| Fixture | `fixtures/pipeline_specs/hydrology/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/hydrology/` | Verifies shape and root boundaries. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/hydrology/` | Emitted by execution, not by the spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/hydrology/`, `release/manifests/hydrology/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 13. Minimal spec profile shape

```yaml
schema_version: kfm.pipeline_spec.hydrology.v1
spec_id: hydrology.<profile>
version: 0.1.0
status: draft
domain: hydrology
owner: <hydrology-domain-steward>
implementation:
  target_pipeline: pipelines/domains/hydrology/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  temporal_fields_required: true
  source_role_separation_required: true
  nfhl_not_observed_flooding: true
  not_for_life_safety: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  spec_is_emergency_warning: false
  spec_is_regulatory_determination: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 14. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/hydrology/
├── test_spec_shape.py                      # PROPOSED
├── test_no_runtime_outputs.py              # PROPOSED
├── test_implementation_refs.py             # PROPOSED
├── test_source_descriptor_refs.py          # PROPOSED
├── test_lifecycle_states.py                # PROPOSED
├── test_temporal_freshness_requirements.py # PROPOSED
├── test_source_role_separation.py          # PROPOSED
├── test_nfhl_regulatory_context.py         # PROPOSED
├── test_required_receipts.py               # PROPOSED
└── test_root_boundary.py                   # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, temporal/freshness checks, source-role separation, regulatory-context handling, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- replaces the short `pipeline_specs/hydrology/README.md` stub;
- identifies this path as Hydrology declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, data storage, proof storage, policy decisions, emergency warnings, flood instructions, regulatory determinations, release approval, or public API/UI authority;
- defines expected Hydrology profile families, lifecycle gates, temporal/freshness gates, source-role gates, emergency-boundary gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/source-role/emergency-boundary posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-HYD-001` | Which Hydrology spec schema is canonical for these profiles? | NEEDS VERIFICATION |
| `PIPE-SPEC-HYD-002` | Which first-wave Hydrology source descriptors should be activated? | NEEDS VERIFICATION |
| `PIPE-SPEC-HYD-003` | Which profile should be implemented first: watersheds/HUC, stream/reach, gauges/observations, groundwater, water quality, regulatory flood context, topology, or hydrostratigraphy? | NEEDS VERIFICATION |
| `PIPE-SPEC-HYD-004` | Which CI workflow validates Hydrology specs? | UNKNOWN |
| `PIPE-SPEC-HYD-005` | Which temporal, source-vintage, topology, NFHL-context, and promotion-decision receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-HYD-006` | Should specs be split by lifecycle stage, source family, object family, observation type, or regulatory-context family? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative. Do not add executable code, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, warning instructions, public API code, UI code, regulatory determinations, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
