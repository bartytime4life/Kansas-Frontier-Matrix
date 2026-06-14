<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-habitat-readme
title: Habitat Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <habitat-domain-steward>
  - <ecology-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/habitat/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipelines/README.md
  - pipelines/domains/habitat/README.md
  - docs/domains/habitat/ARCHITECTURE.md
  - docs/domains/habitat/DATA_LIFECYCLE.md
  - docs/domains/habitat/IDENTITY_MODEL.md
  - docs/domains/habitat/PRESERVATION_MATRIX.md
  - docs/domains/habitat/CANONICAL_PATHS.md
  - docs/domains/habitat/API_CONTRACTS.md
  - data/registry/sources/habitat/
  - data/receipts/pipeline/habitat/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/habitat/
  - fixtures/pipeline_specs/habitat/
tags: [kfm, pipeline-specs, habitat, ecology, declarative-config, land-cover, suitability, connectivity, corridors, restoration, stewardship-zones, receipts, governance]
notes:
  - "This README replaces the short pipeline_specs/habitat stub with a governed declarative-spec lane contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Habitat specs configure pipeline intent, source scope, lifecycle gates, model/observation distinction, evidence gates, receipts, public-safe joins, and release blockers. They do not execute pipeline logic or store lifecycle outputs."
  - "Habitat is a context lane and must not collapse into Fauna/Flora species occurrence truth, regulatory critical-habitat authority, Hydrology truth, Soil truth, or land-management instruction."
  - "Sensitive ecological context, species/plant joins, exact vulnerable habitat, stewardship-controlled data, and unresolved rights fail closed by default."
  - "Concrete spec filenames, schema validation, CI coverage, and activation state remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Pipeline Specs

> Declarative configuration lane for Habitat pipeline profiles, source scopes, schedules, lifecycle gates, model/observation distinctions, evidence requirements, public-safe join rules, fixtures, receipts, and release-readiness intent — separate from executable Habitat pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fdomains%2Fhabitat%2F-d62728)
![context](https://img.shields.io/badge/context%20lane-not%20species%20truth-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/habitat/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion implementation lane:** `pipelines/domains/habitat/` — executable pipeline logic, the **how**  
**Placement posture:** Habitat declarative specs belong here unless an ADR or migration note establishes a different accepted spec home.  
**Public posture:** no public release, data storage, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Spec anti-collapse rules](#3-spec-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Habitat spec scope](#6-habitat-spec-scope)
- [7. Lifecycle posture](#7-lifecycle-posture)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Spec profile families](#10-spec-profile-families)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal spec profile shape](#12-minimal-spec-profile-shape)
- [13. Tests, fixtures, and validation](#13-tests-fixtures-and-validation)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipeline_specs/habitat/` owns declarative Habitat pipeline configuration.

It may describe:

- which Habitat pipeline profile should run;
- which source descriptor ids are in scope;
- which source-family, cadence, and source-vintage checks apply;
- which lifecycle gates are required;
- which model/observation, suitability, connectivity, public-safe geometry, and sensitive-join requirements apply;
- which fixtures support no-network tests;
- which receipts, reports, blockers, and review handoffs are expected;
- which downstream implementation lane is authorized to execute the spec.

It does **not** implement pipeline behavior. Habitat implementation belongs under `pipelines/domains/habitat/` and related executable lanes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `habitat/`? | Habitat has a domain pipeline lane and needs domain-specific run profiles. | CONFIRMED path pattern / NEEDS VERIFICATION for active specs |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define Habitat objects? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Does this approve release or habitat designations? | No. Release decisions, regulatory authority, and stewardship decisions belong elsewhere. | CONFIRMED authority separation |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not catalog truth, not a suitability model result, not regulatory critical-habitat authority, and not release approval.

[⬆ Back to top](#top)

---

## 3. Spec anti-collapse rules

Disallowed collapses:

```text
spec file -> executable pipeline
spec profile -> release approval
source list -> source authority
schedule -> source freshness proof
validation profile -> ValidationReport
catalog profile -> catalog truth
publish profile -> PUBLISHED
habitat suitability profile -> occurrence truth
critical-habitat join profile -> regulatory authority
connectivity profile -> conservation instruction
spec summary -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- habitat patch, land cover, suitability model, critical-habitat designation, species occurrence, plant occurrence, and public-safe derivative states remain separately labeled;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include declarative Habitat specs for:

- source-intake profiles;
- normalization profiles;
- validation profiles;
- catalog and triplet profiles;
- publish-readiness profiles;
- rollback-readiness profiles;
- watcher profiles;
- proof or dry-run profiles;
- land-cover, ecological-system, habitat-patch, suitability, condition, connectivity, corridor, restoration, stewardship-zone, wetland/riparian, and public-safe map-product variants.

A good placement test:

> If the file answers “what Habitat pipeline should run, with what scope, sensitivity gates, model labels, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable Habitat pipeline code | `pipelines/domains/habitat/` |
| Shared executable helpers | `pipelines/<lane>/` or accepted package/tool home |
| Source connectors | `connectors/<source>/` |
| Source descriptors | `data/registry/sources/habitat/` or accepted registry home |
| Habitat object meaning | `contracts/domains/habitat/` and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/habitat/` or accepted schema home |
| Policy and review decisions | `policy/domains/habitat/`, `policy/sensitivity/habitat/`, review roots |
| Tests | `tests/pipeline_specs/habitat/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/habitat/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Habitat spec scope

Habitat specs may configure profiles for object families and candidate products such as:

- habitat patches and habitat classes;
- land-cover observations;
- ecological-system classifications;
- habitat-quality and habitat-condition scores;
- suitability models and model-run receipts;
- connectivity edges, corridors, buffers, and patch graph context;
- restoration opportunity candidates;
- stewardship-zone context;
- uncertainty surfaces;
- wetland, riparian, soil, hydrology, hazards, flora, and fauna context joins;
- public-safe generalized geometry and release-reviewed derivatives.

Habitat is a context lane. Species occurrence truth, plant occurrence truth, taxonomic identity, hydrology truth, soil truth, and regulatory critical-habitat authority remain with their owning lanes or external authorities.

[⬆ Back to top](#top)

---

## 7. Lifecycle posture

Specs may target lifecycle stages, but do not create the lifecycle transition themselves:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare:

- input lifecycle state;
- expected output lifecycle state;
- source descriptor refs;
- model/observation labels;
- sensitive join and public-safe geometry requirements;
- EvidenceBundle requirements;
- review and policy requirements;
- release blockers;
- rollback and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Habitat spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Cadence/freshness gate** — expected run cadence and stale-source behavior.
5. **Lifecycle gate** — allowed input and output lifecycle states.
6. **Model/observation gate** — habitat observations, model outputs, suitability scores, and uncertainty surfaces remain labeled.
7. **Sensitive-join gate** — species/plant joins and exact vulnerable habitat default to public-safe handling.
8. **Anti-collapse gate** — habitat patch, land cover, suitability model, critical-habitat designation, occurrence evidence, and public derivative distinctions.
9. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
10. **Receipt gate** — required run, model, transform, validation, representation, aggregation, or release-readiness receipts.
11. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipeline_specs/habitat/
├── README.md
├── ingest.yaml                    # PROPOSED
├── normalize.yaml                 # PROPOSED
├── validate.yaml                  # PROPOSED
├── catalog.yaml                   # PROPOSED
├── triplets.yaml                  # PROPOSED
├── publish.yaml                   # PROPOSED
├── rollback.yaml                  # PROPOSED
├── watchers.yaml                  # PROPOSED
├── land_cover.yaml                # PROPOSED
├── ecological_systems.yaml        # PROPOSED
├── habitat_patches.yaml           # PROPOSED
├── suitability_models.yaml        # PROPOSED
├── connectivity_corridors.yaml    # PROPOSED
├── restoration.yaml               # PROPOSED
├── stewardship_zones.yaml         # PROPOSED
└── wetland_riparian_context.yaml  # PROPOSED
```

These filenames are proposed placeholders until actual spec files and validators are implemented.

[⬆ Back to top](#top)

---

## 10. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/habitat/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Habitat normalize implementation |
| `validate` | Declare validators, anti-collapse outcomes, and required reports. | Habitat validate implementation |
| `catalog` | Declare catalog closure requirements. | Habitat catalog implementation |
| `triplets` | Declare graph/triplet projection profile. | Habitat triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Habitat/domain publish support |
| `rollback` | Declare rollback-readiness check profile. | Habitat/domain rollback support |
| `watchers` | Declare source-change observation profiles. | Habitat/domain watcher support |
| `object-family` | Declare land-cover, ecological-system, patch, suitability, connectivity, corridor, restoration, stewardship-zone, or wetland/riparian profile variants. | Domain sublane implementations |

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/habitat/` | Declarative config only. |
| Executable target | `pipelines/domains/habitat/` or shared pipeline lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/habitat/` | Read by stable ref. |
| Fixture | `fixtures/pipeline_specs/habitat/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/habitat/` | Verifies shape and root boundaries. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/habitat/` | Emitted by execution, not by the spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/habitat/`, `release/manifests/habitat/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 12. Minimal spec profile shape

```yaml
schema_version: kfm.pipeline_spec.habitat.v1
spec_id: habitat.<profile>
version: 0.1.0
status: draft
domain: habitat
owner: <habitat-domain-steward>
implementation:
  target_pipeline: pipelines/domains/habitat/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  review_required: true
  model_observation_labels_required: true
  sensitive_join_review_required: true
  public_safe_geometry_required: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  spec_is_policy_decision: false
  spec_is_critical_habitat_authority: false
  spec_is_species_occurrence_truth: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/habitat/
├── test_spec_shape.py                         # PROPOSED
├── test_no_runtime_outputs.py                 # PROPOSED
├── test_implementation_refs.py                # PROPOSED
├── test_source_descriptor_refs.py             # PROPOSED
├── test_lifecycle_states.py                   # PROPOSED
├── test_model_observation_labels.py           # PROPOSED
├── test_sensitive_join_requirements.py        # PROPOSED
├── test_public_safe_geometry_requirements.py  # PROPOSED
├── test_required_receipts.py                  # PROPOSED
├── test_release_requirements.py               # PROPOSED
└── test_root_boundary.py                      # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, model/observation label checks, sensitive-join gates, public-safe geometry posture, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- replaces the short `pipeline_specs/habitat/README.md` stub;
- identifies this path as Habitat declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, data storage, proof storage, policy decisions, species occurrence truth, critical-habitat authority, release approval, or public API/UI authority;
- defines expected Habitat profile families, lifecycle gates, model/observation gates, sensitive-join gates, anti-collapse gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/review/anti-collapse posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-HAB-001` | Which Habitat spec schema is canonical for these profiles? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-002` | Which first-wave Habitat source descriptors should be activated? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-003` | Which profile should be implemented first: land cover, habitat patches, suitability models, connectivity/corridors, restoration, or stewardship zones? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-004` | Which CI workflow validates Habitat specs? | UNKNOWN |
| `PIPE-SPEC-HAB-005` | Which public-safe geometry, model-run, uncertainty, and sensitive-join receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-006` | Should spec files be split by lifecycle stage, source family, object family, model family, or sensitivity tier? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative. Do not add executable code, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, species occurrence records, regulatory authority decisions, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
