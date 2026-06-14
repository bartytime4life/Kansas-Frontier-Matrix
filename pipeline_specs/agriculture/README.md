<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-agriculture-readme
title: Agriculture Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <agriculture-domain-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/agriculture/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipelines/README.md
  - pipelines/domains/agriculture/README.md
  - docs/domains/agriculture/ARCHITECTURE.md
  - docs/domains/agriculture/PIPELINE.md
  - docs/domains/agriculture/SOURCES.md
  - docs/domains/agriculture/SOURCE_REGISTRY.md
  - docs/domains/agriculture/sublanes/cropland.md
  - connectors/usda/nass/
  - connectors/nrcs/ssurgo/
  - connectors/kansas/mesonet/
  - connectors/noaa/uscrn/
  - connectors/nasa/smap/
  - connectors/nasa/hls/
  - data/registry/sources/agriculture/
  - data/receipts/pipeline/agriculture/
  - tests/pipeline_specs/agriculture/
  - fixtures/pipeline_specs/agriculture/
tags: [kfm, pipeline-specs, agriculture, declarative-config, schedules, profiles, sources, lifecycle, receipts, governance]
notes:
  - "This README replaces the short pipeline_specs/agriculture stub with a governed declarative-spec lane contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Agriculture specs configure pipeline intent, source scope, cadence, stage profiles, and gates. They do not execute pipeline logic or store lifecycle outputs."
  - "Concrete spec filenames, schema validation, CI coverage, and activation state remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Pipeline Specs

> Declarative configuration lane for Agriculture pipeline profiles, source scopes, schedules, stage gates, receipts, fixtures, and release-readiness intent — separate from executable Agriculture pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2F-d62728)
![lifecycle](https://img.shields.io/badge/lifecycle-no%20data%20storage-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/agriculture/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion implementation lane:** `pipelines/domains/agriculture/` — executable pipeline logic, the **how**  
**Placement posture:** Agriculture declarative specs belong here unless an ADR or migration note establishes a different accepted spec home.  
**Public posture:** no public release, data storage, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Spec anti-collapse rules](#3-spec-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Agriculture spec scope](#6-agriculture-spec-scope)
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

`pipeline_specs/agriculture/` owns declarative Agriculture pipeline configuration.

It may describe:

- which Agriculture pipeline profile should run;
- which source descriptor ids are in scope;
- which stage gates are required;
- which cadence, freshness, and source-vintage checks apply;
- which fixtures support no-network tests;
- which receipts, reports, and blocker records are expected;
- which public-safe aggregation or representation requirements apply before release handoff;
- which downstream implementation lane is authorized to execute the spec.

It does **not** implement pipeline behavior. Agriculture implementation belongs under `pipelines/domains/agriculture/` and related executable lanes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `agriculture/`? | Agriculture has a domain pipeline lane and needs domain-specific run profiles. | CONFIRMED path pattern / NEEDS VERIFICATION for active specs |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define Agriculture objects? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Does this approve release? | No. Release decisions and manifests belong under `release/`. | CONFIRMED authority separation |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not catalog truth, and not release approval.

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
spec summary -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include declarative Agriculture specs for:

- source-intake profiles;
- normalization profiles;
- validation profiles;
- catalog and triplet profiles;
- publish-readiness profiles;
- rollback-readiness profiles;
- watcher profiles;
- proof or dry-run profiles;
- cross-lane Agriculture profiles that only declare intent and constraints.

A good placement test:

> If the file answers “what Agriculture pipeline should run, with what scope and gates?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable Agriculture pipeline code | `pipelines/domains/agriculture/` |
| Shared executable helpers | `pipelines/<lane>/` or accepted package/tool home |
| Source connectors | `connectors/<source>/` |
| Source descriptors | `data/registry/sources/agriculture/` or accepted registry home |
| Agriculture object meaning | `contracts/domains/agriculture/` and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/agriculture/` or accepted schema home |
| Policy and review decisions | `policy/domains/agriculture/`, `policy/sensitivity/agriculture/`, `policy/release/` |
| Tests | `tests/pipeline_specs/agriculture/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/agriculture/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Agriculture spec scope

Agriculture specs may configure profiles for objects and candidate products such as:

- crop observations;
- crop progress and condition candidates;
- cropland and field candidates;
- crop rotation and land-use context;
- aggregate yield observations;
- irrigation links;
- conservation-practice context;
- soil-crop suitability candidates;
- vegetation, drought, pest, and stress indicators;
- agricultural-economy observations;
- public-safe aggregate or release-reviewed products.

Sensitive or high-impact Agriculture outputs should default to aggregation, review, and release gating before public use.

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
- required source descriptors;
- required validators;
- required receipts;
- required review/policy gates;
- required release blockers;
- expected rollback or correction support.

Only the governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Agriculture spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Cadence/freshness gate** — expected run cadence and stale-source behavior.
5. **Lifecycle gate** — allowed input and output lifecycle states.
6. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
7. **Validation gate** — validators, expected finite outcomes, and blocker handling.
8. **Sensitivity/aggregation gate** — public-safe representation requirements where applicable.
9. **Receipt gate** — required run, transform, validation, aggregation, redaction, or release-readiness receipts.
10. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipeline_specs/agriculture/
├── README.md
├── ingest.yaml                 # PROPOSED
├── normalize.yaml              # PROPOSED
├── validate.yaml               # PROPOSED
├── catalog.yaml                # PROPOSED
├── triplets.yaml               # PROPOSED
├── publish.yaml                # PROPOSED
├── rollback.yaml               # PROPOSED
├── watchers.yaml               # PROPOSED
├── cropland.yaml               # PROPOSED
├── crop_progress.yaml          # PROPOSED
├── irrigation.yaml             # PROPOSED
├── conservation.yaml           # PROPOSED
└── stress_indicators.yaml      # PROPOSED
```

These filenames are proposed placeholders until actual spec files and validators are implemented.

[⬆ Back to top](#top)

---

## 10. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare Agriculture source intake scope and prerequisites. | `pipelines/domains/agriculture/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Agriculture normalize implementation |
| `validate` | Declare validators, finite outcomes, and required reports. | Agriculture validate implementation |
| `catalog` | Declare catalog closure requirements. | Agriculture catalog implementation |
| `triplets` | Declare graph/triplet projection profile. | Agriculture triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Agriculture/domain publish support |
| `rollback` | Declare rollback-readiness check profile. | Agriculture/domain rollback support |
| `watchers` | Declare source-change observation profiles. | Agriculture/domain watcher support |
| `sublanes` | Declare crop/cropland/irrigation/conservation/stress profile variants. | Domain sublane implementations |

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/agriculture/` | Declarative config only. |
| Executable target | `pipelines/domains/agriculture/` or shared pipeline lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/agriculture/` | Read by stable ref. |
| Fixture | `fixtures/pipeline_specs/agriculture/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/agriculture/` | Verifies shape and root boundaries. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/agriculture/` | Emitted by execution, not by the spec file alone. |
| Release material | `release/candidates/agriculture/`, `release/manifests/agriculture/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 12. Minimal spec profile shape

The final schema is not defined here. This example shows the minimum intent a spec should preserve.

```yaml
schema_version: kfm.pipeline_spec.agriculture.v1
spec_id: agriculture.<profile>
version: 0.1.0
status: draft
domain: agriculture
owner: <agriculture-domain-steward>
implementation:
  target_pipeline: pipelines/domains/agriculture/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  review_required: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  spec_is_policy_decision: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/agriculture/
├── test_spec_shape.py                 # PROPOSED
├── test_no_runtime_outputs.py          # PROPOSED
├── test_implementation_refs.py         # PROPOSED
├── test_source_descriptor_refs.py      # PROPOSED
├── test_lifecycle_states.py            # PROPOSED
├── test_required_receipts.py           # PROPOSED
├── test_release_requirements.py        # PROPOSED
└── test_root_boundary.py               # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- replaces the short `pipeline_specs/agriculture/README.md` stub;
- identifies this path as Agriculture declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, data storage, proof storage, policy decisions, release approval, or public API/UI authority;
- defines expected Agriculture profile families, lifecycle gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/review posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-AG-001` | Which Agriculture spec schema is canonical for these profiles? | NEEDS VERIFICATION |
| `PIPE-SPEC-AG-002` | Which first-wave Agriculture source descriptors should be activated? | NEEDS VERIFICATION |
| `PIPE-SPEC-AG-003` | Which Agriculture sublane profile should be implemented first: cropland, crop progress, irrigation, conservation, or stress indicators? | NEEDS VERIFICATION |
| `PIPE-SPEC-AG-004` | Which CI workflow validates Agriculture specs? | UNKNOWN |
| `PIPE-SPEC-AG-005` | Which aggregation/public-representation receipt vocabulary is canonical for Agriculture release handoff? | NEEDS VERIFICATION |
| `PIPE-SPEC-AG-006` | Should spec files be split by lifecycle stage, sublane, or source family? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative. Do not add executable code, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
