<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-geology-readme
title: Geology Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <geology-domain-steward>
  - <natural-resources-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/geology/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipelines/README.md
  - pipelines/domains/geology/README.md
  - docs/domains/geology/ARCHITECTURE.md
  - docs/domains/geology/POLICY.md
  - docs/domains/geology/PRESERVATION_MATRIX.md
  - docs/domains/geology/OPEN_QUESTIONS.md
  - data/registry/sources/geology/
  - data/receipts/pipeline/geology/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/geology/
  - fixtures/pipeline_specs/geology/
tags: [kfm, pipeline-specs, geology, natural-resources, declarative-config, stratigraphy, lithology, boreholes, well-logs, geophysics, geochemistry, mineral-occurrences, receipts, governance]
notes:
  - "This README replaces the short pipeline_specs/geology stub with a governed declarative-spec lane contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Geology specs configure pipeline intent, source scope, lifecycle gates, anti-collapse gates, evidence gates, receipts, public-safe geometry posture, and release blockers. They do not execute pipeline logic or store lifecycle outputs."
  - "Occurrence, deposit, estimate, permit, production, reserve, title, and extraction claims must remain distinct."
  - "Exact subsurface, private-well, sensitive resource, infrastructure-adjacent, and unresolved-rights material fail closed by default."
  - "Concrete spec filenames, schema validation, CI coverage, and activation state remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Pipeline Specs

> Declarative configuration lane for Geology and Natural Resources pipeline profiles, source scopes, schedules, lifecycle gates, anti-collapse checks, public-safe geometry requirements, evidence requirements, fixtures, receipts, and release-readiness intent — separate from executable Geology pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fdomains%2Fgeology%2F-d62728)
![anti-collapse](https://img.shields.io/badge/anti--collapse-required-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/geology/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion implementation lane:** `pipelines/domains/geology/` — executable pipeline logic, the **how**  
**Placement posture:** Geology declarative specs belong here unless an ADR or migration note establishes a different accepted spec home.  
**Public posture:** no public release, data storage, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Spec anti-collapse rules](#3-spec-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Geology spec scope](#6-geology-spec-scope)
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

`pipeline_specs/geology/` owns declarative Geology and Natural Resources pipeline configuration.

It may describe:

- which Geology pipeline profile should run;
- which source descriptor ids are in scope;
- which source-family, cadence, and source-vintage checks apply;
- which lifecycle gates are required;
- which interpretation, uncertainty, anti-collapse, and public-safe geometry requirements apply;
- which fixtures support no-network tests;
- which receipts, reports, blockers, and review handoffs are expected;
- which downstream implementation lane is authorized to execute the spec.

It does **not** implement pipeline behavior. Geology implementation belongs under `pipelines/domains/geology/` and related executable lanes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `geology/`? | Geology has a domain pipeline lane and needs domain-specific run profiles. | CONFIRMED path pattern / NEEDS VERIFICATION for active specs |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define Geology objects? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Does this approve release or resource decisions? | No. Release, permit, title, ownership, extraction, reserve, and resource decisions belong elsewhere. | CONFIRMED authority separation |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not catalog truth, not a resource/permit/title decision, and not release approval.

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
occurrence profile -> deposit truth
estimate profile -> per-place measurement
permit profile -> resource proof
production profile -> reserve estimate
spec summary -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- occurrence, deposit, estimate, permit, production, reserve, title, and extraction claims remain separately labeled;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include declarative Geology specs for:

- source-intake profiles;
- normalization profiles;
- validation profiles;
- catalog and triplet profiles;
- publish-readiness profiles;
- rollback-readiness profiles;
- watcher profiles;
- proof or dry-run profiles;
- bedrock, surficial, stratigraphy, lithology, structures, boreholes, well logs, cores, geophysics, geochemistry, hydrostratigraphy, mineral occurrence, extraction/reclamation, and public-safe map-product variants.

A good placement test:

> If the file answers “what Geology pipeline should run, with what scope, anti-collapse gates, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable Geology pipeline code | `pipelines/domains/geology/` |
| Shared executable helpers | `pipelines/<lane>/` or accepted package/tool home |
| Source connectors | `connectors/<source>/` |
| Source descriptors | `data/registry/sources/geology/` or accepted registry home |
| Geology object meaning | `contracts/domains/geology/` and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/geology/` or accepted schema home |
| Policy and review decisions | `policy/domains/geology/`, `policy/sensitivity/geology/`, review roots |
| Tests | `tests/pipeline_specs/geology/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/geology/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Geology spec scope

Geology specs may configure profiles for object families and candidate products such as:

- geologic units and surficial units;
- lithology, stratigraphy, stratigraphic intervals, and correlations;
- structure features, faults, folds, lineaments, and boundary versions;
- borehole references, well log references, core samples, and samples;
- geophysical observations and geochemistry sample references;
- mineral occurrences, resource deposits, and resource estimates;
- extraction sites, reclamation records, and administrative context without collapsing into deposit or resource truth;
- cross sections and hydrostratigraphic units on the geology side;
- public-safe generalized geometry and release-reviewed derivatives.

Exact subsurface, private-well, sensitive resource, infrastructure-adjacent, and unresolved-rights material must default to hold, denial, aggregation, generalization, or release-reviewed representation posture.

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
- source-role and interpretation-role requirements;
- anti-collapse requirements;
- public-safe geometry requirements;
- EvidenceBundle requirements;
- review and policy requirements;
- release blockers;
- rollback and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Geology spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Cadence/freshness gate** — expected run cadence and stale-source behavior.
5. **Lifecycle gate** — allowed input and output lifecycle states.
6. **Anti-collapse gate** — occurrence, deposit, estimate, permit, production, reserve, title, and extraction distinctions.
7. **Geometry/sensitivity gate** — exact subsurface, private-well, sensitive resource, infrastructure-adjacent, and public-safe geometry posture.
8. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
9. **Validation gate** — validators, finite outcomes, and blocker handling.
10. **Receipt gate** — required run, transform, validation, representation, aggregation, or release-readiness receipts.
11. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipeline_specs/geology/
├── README.md
├── ingest.yaml                    # PROPOSED
├── normalize.yaml                 # PROPOSED
├── validate.yaml                  # PROPOSED
├── catalog.yaml                   # PROPOSED
├── triplets.yaml                  # PROPOSED
├── publish.yaml                   # PROPOSED
├── rollback.yaml                  # PROPOSED
├── watchers.yaml                  # PROPOSED
├── bedrock_units.yaml             # PROPOSED
├── surficial_units.yaml           # PROPOSED
├── stratigraphy.yaml              # PROPOSED
├── structures.yaml                # PROPOSED
├── boreholes_well_logs.yaml       # PROPOSED
├── geophysics_geochemistry.yaml   # PROPOSED
├── hydrostratigraphy.yaml         # PROPOSED
└── mineral_resources.yaml         # PROPOSED
```

These filenames are proposed placeholders until actual spec files and validators are implemented.

[⬆ Back to top](#top)

---

## 10. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/geology/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Geology normalize implementation |
| `validate` | Declare validators, anti-collapse outcomes, and required reports. | Geology validate implementation |
| `catalog` | Declare catalog closure requirements. | Geology catalog implementation |
| `triplets` | Declare graph/triplet projection profile. | Geology triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Geology/domain publish support |
| `rollback` | Declare rollback-readiness check profile. | Geology/domain rollback support |
| `watchers` | Declare source-change observation profiles. | Geology/domain watcher support |
| `object-family` | Declare bedrock, surficial, stratigraphy, structures, boreholes, well logs, geophysics, geochemistry, hydrostratigraphy, or resource profile variants. | Domain sublane implementations |

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/geology/` | Declarative config only. |
| Executable target | `pipelines/domains/geology/` or shared pipeline lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/geology/` | Read by stable ref. |
| Fixture | `fixtures/pipeline_specs/geology/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/geology/` | Verifies shape and root boundaries. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/geology/` | Emitted by execution, not by the spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/geology/`, `release/manifests/geology/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 12. Minimal spec profile shape

```yaml
schema_version: kfm.pipeline_spec.geology.v1
spec_id: geology.<profile>
version: 0.1.0
status: draft
domain: geology
owner: <geology-domain-steward>
implementation:
  target_pipeline: pipelines/domains/geology/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  review_required: true
  anti_collapse_required: true
  public_safe_geometry_required: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  spec_is_resource_decision: false
  spec_is_permit_or_title_decision: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/geology/
├── test_spec_shape.py                      # PROPOSED
├── test_no_runtime_outputs.py              # PROPOSED
├── test_implementation_refs.py             # PROPOSED
├── test_source_descriptor_refs.py          # PROPOSED
├── test_lifecycle_states.py                # PROPOSED
├── test_anti_collapse_requirements.py      # PROPOSED
├── test_public_safe_geometry_requirements.py # PROPOSED
├── test_required_receipts.py               # PROPOSED
├── test_release_requirements.py            # PROPOSED
└── test_root_boundary.py                   # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, anti-collapse gates, public-safe geometry posture, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- replaces the short `pipeline_specs/geology/README.md` stub;
- identifies this path as Geology declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, data storage, proof storage, policy decisions, resource/permit/title decisions, release approval, or public API/UI authority;
- defines expected Geology profile families, lifecycle gates, anti-collapse gates, geometry/sensitivity gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/review/anti-collapse posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-GEOL-001` | Which Geology spec schema is canonical for these profiles? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-002` | Which first-wave Geology source descriptors should be activated? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-003` | Which profile should be implemented first: bedrock units, surficial units, boreholes/well logs, cross sections, or mineral resources? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-004` | Which CI workflow validates Geology specs? | UNKNOWN |
| `PIPE-SPEC-GEOL-005` | Which public-safe geometry and aggregation receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-GEOL-006` | Should spec files be split by lifecycle stage, source family, object family, or sensitivity tier? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative. Do not add executable code, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, private subsurface artifacts, resource decisions, permit/title decisions, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
