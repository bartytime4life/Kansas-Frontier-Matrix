<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-habitat-land-cover-readme
title: Habitat Land Cover Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <habitat-domain-steward>
  - <land-cover-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/habitat/land_cover/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipeline_specs/habitat/README.md
  - pipelines/README.md
  - pipelines/domains/habitat/README.md
  - pipelines/domains/habitat/land_cover/README.md
  - docs/domains/habitat/ARCHITECTURE.md
  - data/registry/sources/habitat/
  - data/receipts/pipeline/habitat/land_cover/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/habitat/land_cover/
  - fixtures/pipeline_specs/habitat/land_cover/
tags: [kfm, pipeline-specs, habitat, land-cover, land-cover-observation, declarative-config, native-classification, crosswalk, source-epoch, receipts, governance]
notes:
  - "This README replaces the one-character pipeline_specs/habitat/land_cover stub with a governed declarative land-cover-spec contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Land-cover specs configure source scope, native class preservation, class-map versioning, source epoch, advisory crosswalk posture, evidence gates, receipts, and release blockers. They do not execute pipeline logic or store lifecycle outputs."
  - "Land cover is Habitat context. It must not collapse into species occurrence truth, plant occurrence truth, crop truth, wetland designation truth, hydrology truth, soil truth, hazard truth, or release approval."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Land Cover Pipeline Specs

> Declarative configuration lane for Habitat land-cover profiles: source families, class maps, native classification preservation, source epochs, advisory crosswalks, geometry posture, evidence requirements, fixtures, receipts, and release-readiness intent — separate from executable land-cover pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fdomains%2Fhabitat%2Fland__cover%2F-d62728)
![crosswalk](https://img.shields.io/badge/crosswalk-advisory%20only-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/habitat/land_cover/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Parent spec lane:** `pipeline_specs/habitat/`  
**Companion implementation lane:** `pipelines/domains/habitat/land_cover/` — executable pipeline logic, the **how**  
**Placement posture:** Habitat land-cover specs belong here as declarative profiles unless an ADR or migration note establishes a different accepted spec home.  
**Public posture:** no public release, data storage, source admission, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Land-cover spec anti-collapse rules](#3-land-cover-spec-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Land-cover spec scope](#6-land-cover-spec-scope)
- [7. Lifecycle posture](#7-lifecycle-posture)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Spec profile families](#10-spec-profile-families)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal land-cover spec profile shape](#12-minimal-land-cover-spec-profile-shape)
- [13. Tests, fixtures, and validation](#13-tests-fixtures-and-validation)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipeline_specs/habitat/land_cover/` owns declarative land-cover configuration for the Habitat lane.

It may describe:

- which land-cover profile should run;
- which source descriptor ids are in scope;
- which source family, native class map, source epoch, and source-vintage checks apply;
- which raster/vector, CRS, geometry, tile-index, and summary metadata checks are required;
- which EvidenceBundle, receipt, validation, and review outputs are expected;
- which downstream executable land-cover lane is authorized to execute the spec.

It does **not** implement pipeline behavior. Land-cover execution belongs under `pipelines/domains/habitat/land_cover/` or an accepted shared implementation lane.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `habitat/land_cover/`? | Habitat specs include land-cover profiles, and this path narrows that profile family. | CONFIRMED path pattern / NEEDS VERIFICATION for active specs |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define Habitat or land-cover object meaning? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Does this approve release? | No. Release decisions, manifests, correction notices, and rollback cards belong under release authority. | CONFIRMED authority separation |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not catalog truth, not a source class authority, and not release approval.

[⬆ Back to top](#top)

---

## 3. Land-cover spec anti-collapse rules

Disallowed collapses:

```text
spec file -> executable pipeline
spec profile -> release approval
source list -> source authority
schedule -> source freshness proof
native class -> common class without native class preservation
crosswalk class -> authoritative source class
modeled pixel -> direct field measurement
crop context -> Agriculture crop truth
wetland class -> hydrology or wetland designation truth
land-cover context -> occurrence truth
spec summary -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- native source classification, advisory crosswalk, source epoch, source version, geometry lineage, and public-safe release state remain explicit;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include declarative land-cover specs for:

- source-intake profile constraints;
- land-cover source-family constraints;
- native class-map and class-label preservation constraints;
- source-vintage, source-epoch, and class-map version checks;
- raster, vector, CRS, geometry, tile-index, and summary metadata checks;
- normalization and validation profiles;
- catalog and triplet profiles;
- publish-readiness and rollback-readiness profiles;
- watcher profiles for land-cover source updates;
- dry-run profiles that only declare intent and gates.

A good placement test:

> If the file answers “what land-cover pipeline should run, with what source family, class map, epoch, geometry checks, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable land-cover pipeline code | `pipelines/domains/habitat/land_cover/` |
| Shared executable helpers | `pipelines/<lane>/` or accepted package/tool home |
| Source connectors | `connectors/<source>/` |
| Source descriptors | `data/registry/sources/habitat/` or accepted registry home |
| Habitat object meaning | `contracts/domains/habitat/` and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/habitat/` or accepted schema home |
| Policy and review decisions | `policy/domains/habitat/`, `policy/sensitivity/habitat/`, review roots |
| Tests | `tests/pipeline_specs/habitat/land_cover/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/habitat/land_cover/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Land-cover spec scope

Land-cover specs may configure profiles for candidate products such as:

- `LandCoverObservation` profile families;
- NLCD, CDL, LANDFIRE, GAP, NWI, and other admitted land-cover sources;
- native class code, class label, class-map version, and source epoch;
- advisory crosswalks that do not replace native classifications;
- raster, vector, tile-index, and summary metadata candidates;
- handoffs to HabitatPatch, habitat quality, suitability, condition, connectivity, restoration, and stewardship-context workflows;
- public-safe generalized map products and release-reviewed derivatives.

Land cover is context. It does not become species occurrence truth, plant occurrence truth, Agriculture crop truth, wetland designation truth, hydrology truth, soil truth, hazard truth, or release approval.

[⬆ Back to top](#top)

---

## 7. Lifecycle posture

Specs may target lifecycle stages, but do not create the lifecycle transition themselves:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare input lifecycle state, expected output lifecycle state, source descriptor refs, source-family/class-map requirements, native classification posture, advisory crosswalk posture, source-epoch/source-vintage checks, geometry checks, EvidenceBundle requirements, receipt requirements, release blockers, rollback support, and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 8. Required gates

Every land-cover spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Class-map gate** — native class code, label, class-map version, source family, and source epoch.
5. **Lifecycle gate** — allowed input and output lifecycle states.
6. **Geometry gate** — CRS, raster/vector footprint, tile-index, extent, and public-safe representation posture.
7. **Crosswalk gate** — crosswalks remain advisory and cannot overwrite native classification.
8. **Anti-collapse gate** — land-cover context remains distinct from occurrence, crop, wetland, hydrology, soil, hazard, and release truth.
9. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
10. **Receipt gate** — required run, transform, validation, class-map, source-vintage, geometry, or release-readiness receipts.
11. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipeline_specs/habitat/land_cover/
├── README.md
├── ingest.yaml                  # PROPOSED
├── normalize.yaml               # PROPOSED
├── validate.yaml                # PROPOSED
├── catalog.yaml                 # PROPOSED
├── triplets.yaml                # PROPOSED
├── publish.yaml                 # PROPOSED
├── rollback.yaml                # PROPOSED
├── watchers.yaml                # PROPOSED
├── nlcd.yaml                    # PROPOSED
├── cdl_context.yaml             # PROPOSED
├── landfire.yaml                # PROPOSED
├── gap.yaml                     # PROPOSED
├── nwi_context.yaml             # PROPOSED
├── class_map_checks.yaml        # PROPOSED
└── geometry_release.yaml        # PROPOSED
```

These filenames are proposed placeholders until actual spec files and validators are implemented.

[⬆ Back to top](#top)

---

## 10. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/habitat/land_cover/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Habitat land-cover normalize implementation |
| `validate` | Declare native-class, class-map, geometry, and anti-collapse checks. | Habitat land-cover validate implementation |
| `catalog` | Declare catalog closure requirements. | Habitat land-cover catalog implementation |
| `triplets` | Declare graph/triplet projection profile. | Habitat land-cover triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Habitat/domain publish support |
| `rollback` | Declare rollback-readiness check profile. | Habitat/domain rollback support |
| `watchers` | Declare source-change observation profiles. | Habitat/domain watcher support |
| `source-family` | Declare NLCD, CDL context, LANDFIRE, GAP, NWI context, or other admitted land-cover source variants. | Domain sublane implementations |
| `geometry` | Declare CRS, topology, simplification, tile-index, and public-safe geometry profiles. | Domain sublane implementations |

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/habitat/land_cover/` | Declarative config only. |
| Executable target | `pipelines/domains/habitat/land_cover/` or shared pipeline lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/habitat/` | Read by stable ref. |
| Fixture | `fixtures/pipeline_specs/habitat/land_cover/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/habitat/land_cover/` | Verifies shape and root boundaries. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/habitat/land_cover/` | Emitted by execution, not by the spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/habitat/`, `release/manifests/habitat/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 12. Minimal land-cover spec profile shape

```yaml
schema_version: kfm.pipeline_spec.habitat.land_cover.v1
spec_id: habitat.land_cover.<profile>
version: 0.1.0
status: draft
domain: habitat
lane: land_cover
owner: <habitat-domain-steward>
implementation:
  target_pipeline: pipelines/domains/habitat/land_cover/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
land_cover:
  source_family: <source-family>
  class_map_ref: <class-map-ref>
  source_epoch: <epoch>
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  native_class_preservation_required: true
  advisory_crosswalk_only: true
  class_map_receipt_required: true
  source_vintage_receipt_required: true
  geometry_validation_required: true
  public_safe_geometry_required: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  land_cover_is_occurrence_truth: false
  crosswalk_is_authoritative_class: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/habitat/land_cover/
├── test_spec_shape.py                      # PROPOSED
├── test_no_runtime_outputs.py              # PROPOSED
├── test_implementation_refs.py             # PROPOSED
├── test_source_descriptor_refs.py          # PROPOSED
├── test_class_map_refs.py                  # PROPOSED
├── test_source_epoch_refs.py               # PROPOSED
├── test_lifecycle_states.py                # PROPOSED
├── test_geometry_requirements.py           # PROPOSED
├── test_anti_collapse_requirements.py      # PROPOSED
├── test_required_receipts.py               # PROPOSED
└── test_root_boundary.py                   # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, source-family/class-map assertions, source-epoch assertions, lifecycle-state assertions, geometry checks, anti-collapse gates, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- replaces the one-character `pipeline_specs/habitat/land_cover/README.md` stub;
- identifies this path as Habitat land-cover declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, source authority, data storage, proof storage, regulatory designation, occurrence truth, crop truth, wetland/hydrology truth, release approval, or public API/UI authority;
- defines expected land-cover profile families, source-family/class-map gates, source-epoch gates, geometry gates, advisory-crosswalk gates, receipts, tests, and open questions.

Future land-cover spec files are done only when they validate, point to executable lanes, use stable source descriptors, preserve native classification, declare source family/class-map/source-epoch fields, require geometry and vintage receipts, preserve evidence/anti-collapse posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-HAB-LC-001` | Which land-cover spec schema is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-002` | Which first-wave land-cover source descriptor should be activated: NLCD, LANDFIRE, GAP, CDL context, NWI context, or another admitted source? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-003` | Which source-family profile should be implemented first? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-004` | Which CI workflow validates Habitat land-cover specs? | UNKNOWN |
| `PIPE-SPEC-HAB-LC-005` | Which class-map, source-vintage, geometry, and public-safe map receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAB-LC-006` | Should specs be split by lifecycle stage, source family, class-map family, or geometry-release family? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative. Do not add executable code, source clients, source descriptors, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, regulatory designations, occurrence truth records, crop truth records, wetland/hydrology truth records, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
