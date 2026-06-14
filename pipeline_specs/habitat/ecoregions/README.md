<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-habitat-ecoregions-readme
title: Habitat Ecoregions Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <habitat-domain-steward>
  - <ecoregions-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/habitat/ecoregions/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipeline_specs/habitat/README.md
  - pipelines/README.md
  - pipelines/domains/habitat/README.md
  - pipelines/domains/habitat/ecoregions/README.md
  - docs/domains/habitat/ARCHITECTURE.md
  - docs/domains/habitat/sublanes/ecoregions.md
  - data/registry/sources/habitat/
  - data/receipts/pipeline/habitat/ecoregions/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/habitat/ecoregions/
  - fixtures/pipeline_specs/habitat/ecoregions/
tags: [kfm, pipeline-specs, habitat, ecoregions, regionalization, biophysical-context, declarative-config, hierarchy, source-version, receipts, governance]
notes:
  - "This README replaces the one-character pipeline_specs/habitat/ecoregions stub with a governed declarative ecoregions-spec contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Ecoregion specs configure source scope, framework identity, hierarchy level, source-vintage checks, geometry posture, evidence gates, receipts, and release blockers. They do not execute pipeline logic or store lifecycle outputs."
  - "Ecoregions are regionalization context. They must not collapse into species occurrence truth, plant occurrence truth, HabitatPatch truth, critical-habitat designation, or regulatory authority."
  - "Concrete spec filenames, schema validation, CI coverage, and activation state remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Ecoregions Pipeline Specs

> Declarative configuration lane for Habitat ecoregion and biophysical-regionalization profiles: source frameworks, hierarchy levels, versioning, geometry posture, evidence requirements, fixtures, receipts, and release-readiness intent — separate from executable ecoregion pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fdomains%2Fhabitat%2Fecoregions%2F-d62728)
![anti-collapse](https://img.shields.io/badge/ecoregion%20%E2%89%A0%20occurrence%20truth-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/habitat/ecoregions/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Parent spec lane:** `pipeline_specs/habitat/`  
**Companion implementation lane:** `pipelines/domains/habitat/ecoregions/` — executable pipeline logic, the **how**  
**Placement posture:** Habitat ecoregions specs belong here as declarative profiles unless an ADR or migration note establishes a different accepted spec home.  
**Public posture:** no public release, data storage, source admission, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Ecoregion spec anti-collapse rules](#3-ecoregion-spec-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Ecoregion spec scope](#6-ecoregion-spec-scope)
- [7. Lifecycle posture](#7-lifecycle-posture)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Spec profile families](#10-spec-profile-families)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal ecoregion spec profile shape](#12-minimal-ecoregion-spec-profile-shape)
- [13. Tests, fixtures, and validation](#13-tests-fixtures-and-validation)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipeline_specs/habitat/ecoregions/` owns declarative ecoregion and biophysical-regionalization configuration for the Habitat lane.

It may describe:

- which ecoregion or regionalization profile should run;
- which source descriptor ids are in scope;
- which framework, hierarchy level, source version, and source-vintage checks apply;
- which geometry, CRS, topology, boundary, and public-safe representation checks are required;
- which EvidenceBundle, receipt, validation, and review outputs are expected;
- which downstream executable ecoregion lane is authorized to execute the spec.

It does **not** implement pipeline behavior. Ecoregion execution belongs under `pipelines/domains/habitat/ecoregions/` or an accepted shared implementation lane.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `habitat/ecoregions/`? | Habitat specs include ecoregion/regionalization profiles, and this path narrows that profile family. | CONFIRMED path pattern / NEEDS VERIFICATION for active specs |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define Habitat or ecoregion object meaning? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Does this approve release? | No. Release decisions, manifests, correction notices, and rollback cards belong under release authority. | CONFIRMED authority separation |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not catalog truth, not an ecoregion source authority, and not release approval.

[⬆ Back to top](#top)

---

## 3. Ecoregion spec anti-collapse rules

Disallowed collapses:

```text
spec file -> executable pipeline
spec profile -> release approval
source list -> source authority
schedule -> source freshness proof
ecoregion polygon -> species occurrence truth
ecoregion polygon -> plant occurrence truth
ecoregion polygon -> HabitatPatch truth
ecoregion context -> critical-habitat designation
ecoregion framework A -> framework B without framework ref
hierarchy level -> different hierarchy level without receipt
spec summary -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- ecoregion framework, source version, hierarchy level, geometry lineage, and public-safe release state remain explicit;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include declarative ecoregion specs for:

- source-intake profile constraints;
- ecoregion framework and hierarchy profile constraints;
- source-vintage and source-version checks;
- geometry, CRS, topology, and boundary checks;
- normalization and validation profiles;
- catalog and triplet profiles;
- publish-readiness and rollback-readiness profiles;
- watcher profiles for ecoregion source updates;
- dry-run profiles that only declare intent and gates.

A good placement test:

> If the file answers “what ecoregion/regionalization pipeline should run, with what framework, hierarchy, source version, geometry checks, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable ecoregion pipeline code | `pipelines/domains/habitat/ecoregions/` |
| Shared executable helpers | `pipelines/<lane>/` or accepted package/tool home |
| Source connectors | `connectors/<source>/` |
| Source descriptors | `data/registry/sources/habitat/` or accepted registry home |
| Habitat object meaning | `contracts/domains/habitat/` and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/habitat/` or accepted schema home |
| Policy and review decisions | `policy/domains/habitat/`, `policy/sensitivity/habitat/`, review roots |
| Tests | `tests/pipeline_specs/habitat/ecoregions/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/habitat/ecoregions/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Ecoregion spec scope

Ecoregion specs may configure profiles for candidate products such as:

- ecoregion framework identity and source family;
- hierarchy level, code, name, parent/child relation, and source version;
- boundary geometry, CRS, topology, and extent checks;
- source-vintage and version-change detection;
- joins to habitat patches, ecological systems, land-cover observations, suitability models, corridors, restoration opportunities, and stewardship zones;
- cross-lane context joins to Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, and Spatial Foundation without adopting their truth;
- public-safe generalized map products and release-reviewed derivatives.

Ecoregions are context. They do not prove species presence, plant presence, habitat patch quality, regulatory designation, or cross-domain truth.

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
- framework and hierarchy requirements;
- source-version and source-vintage checks;
- geometry and topology validation requirements;
- EvidenceBundle requirements;
- receipt requirements;
- release blockers;
- rollback and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 8. Required gates

Every ecoregion spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Framework gate** — source framework, hierarchy system, level, version, and parent/child posture.
5. **Lifecycle gate** — allowed input and output lifecycle states.
6. **Geometry gate** — CRS, topology, extent, boundary lineage, simplification, and public-safe representation posture.
7. **Anti-collapse gate** — ecoregion context stays distinct from species, plant, habitat patch, critical-habitat, hydrology, soil, hazards, and agriculture truth.
8. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
9. **Receipt gate** — required run, transform, validation, hierarchy, source-vintage, geometry, or release-readiness receipts.
10. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipeline_specs/habitat/ecoregions/
├── README.md
├── ingest.yaml                 # PROPOSED
├── normalize.yaml              # PROPOSED
├── validate.yaml               # PROPOSED
├── catalog.yaml                # PROPOSED
├── triplets.yaml               # PROPOSED
├── publish.yaml                # PROPOSED
├── rollback.yaml               # PROPOSED
├── watchers.yaml               # PROPOSED
├── framework_epa_omernik.yaml  # PROPOSED
├── framework_usfs_bailey.yaml  # PROPOSED
├── hierarchy_checks.yaml       # PROPOSED
└── geometry_release.yaml       # PROPOSED
```

These filenames are proposed placeholders until actual spec files and validators are implemented.

[⬆ Back to top](#top)

---

## 10. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/habitat/ecoregions/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Habitat ecoregion normalize implementation |
| `validate` | Declare framework, hierarchy, geometry, and anti-collapse checks. | Habitat ecoregion validate implementation |
| `catalog` | Declare catalog closure requirements. | Habitat ecoregion catalog implementation |
| `triplets` | Declare graph/triplet projection profile. | Habitat ecoregion triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Habitat/domain publish support |
| `rollback` | Declare rollback-readiness check profile. | Habitat/domain rollback support |
| `watchers` | Declare source-change observation profiles. | Habitat/domain watcher support |
| `framework` | Declare EPA/Omernik, USFS/Bailey, or other admitted framework variants. | Domain sublane implementations |
| `geometry` | Declare CRS, topology, simplification, and public-safe geometry profiles. | Domain sublane implementations |

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/habitat/ecoregions/` | Declarative config only. |
| Executable target | `pipelines/domains/habitat/ecoregions/` or shared pipeline lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/habitat/` | Read by stable ref. |
| Fixture | `fixtures/pipeline_specs/habitat/ecoregions/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/habitat/ecoregions/` | Verifies shape and root boundaries. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/habitat/ecoregions/` | Emitted by execution, not by the spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/habitat/`, `release/manifests/habitat/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 12. Minimal ecoregion spec profile shape

```yaml
schema_version: kfm.pipeline_spec.habitat.ecoregions.v1
spec_id: habitat.ecoregions.<profile>
version: 0.1.0
status: draft
domain: habitat
lane: ecoregions
owner: <habitat-domain-steward>
implementation:
  target_pipeline: pipelines/domains/habitat/ecoregions/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
regionalization:
  framework: <framework-id>
  hierarchy_level: <level>
  source_version: <version>
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  framework_ref_required: true
  hierarchy_receipt_required: true
  source_vintage_receipt_required: true
  geometry_validation_required: true
  public_safe_geometry_required: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  ecoregion_is_species_occurrence_truth: false
  ecoregion_is_habitat_patch_truth: false
  ecoregion_is_regulatory_designation: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/habitat/ecoregions/
├── test_spec_shape.py                      # PROPOSED
├── test_no_runtime_outputs.py              # PROPOSED
├── test_implementation_refs.py             # PROPOSED
├── test_source_descriptor_refs.py          # PROPOSED
├── test_framework_and_hierarchy_refs.py    # PROPOSED
├── test_lifecycle_states.py                # PROPOSED
├── test_geometry_requirements.py           # PROPOSED
├── test_anti_collapse_requirements.py      # PROPOSED
├── test_required_receipts.py               # PROPOSED
├── test_release_requirements.py            # PROPOSED
└── test_root_boundary.py                   # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, framework/hierarchy assertions, lifecycle-state assertions, geometry checks, anti-collapse gates, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- replaces the one-character `pipeline_specs/habitat/ecoregions/README.md` stub;
- identifies this path as Habitat ecoregion declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, source authority, data storage, proof storage, regulatory designation, species/plant occurrence truth, habitat patch truth, release approval, or public API/UI authority;
- defines expected ecoregion profile families, framework/hierarchy gates, geometry gates, anti-collapse gates, receipts, tests, and open questions.

Future ecoregion spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare framework/hierarchy/source-version fields, require geometry and vintage receipts, preserve evidence/anti-collapse posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-HAB-ECO-001` | Which ecoregion spec schema is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-ECO-002` | Which first-wave ecoregion source descriptors should be activated? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-ECO-003` | Which framework profile should be implemented first: EPA/Omernik, USFS/Bailey, or another admitted framework? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-ECO-004` | Which CI workflow validates Habitat ecoregion specs? | UNKNOWN |
| `PIPE-SPEC-HAB-ECO-005` | Which hierarchy, source-vintage, geometry, and public-safe map receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-ECO-006` | Should specs be split by lifecycle stage, ecoregion framework, hierarchy level, or geometry-release family? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative. Do not add executable code, source clients, source descriptors, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, regulatory designations, occurrence truth records, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
