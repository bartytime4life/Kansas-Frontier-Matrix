<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-fauna-readme
title: Fauna Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <fauna-domain-steward>
  - <sensitivity-review-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/fauna/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipelines/README.md
  - pipelines/domains/fauna/README.md
  - docs/domains/fauna/ARCHITECTURE.md
  - policy/domains/fauna/
  - policy/sensitivity/fauna/
  - data/registry/sources/fauna/
  - data/receipts/pipeline/fauna/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/fauna/
  - fixtures/pipeline_specs/fauna/
tags: [kfm, pipeline-specs, fauna, biodiversity, declarative-config, species, occurrence, monitoring, representation, receipts, governance]
notes:
  - "This README replaces the short pipeline_specs/fauna stub with a governed declarative-spec lane contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Fauna specs configure pipeline intent, source scope, lifecycle gates, representation requirements, evidence gates, receipts, and release blockers. They do not execute pipeline logic or store lifecycle outputs."
  - "Restricted observations and unresolved review state fail closed by default."
  - "Concrete spec filenames, schema validation, CI coverage, and activation state remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Pipeline Specs

> Declarative configuration lane for Fauna pipeline profiles, source scopes, schedules, lifecycle gates, representation requirements, evidence requirements, fixtures, receipts, and release-readiness intent — separate from executable Fauna pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fdomains%2Ffauna%2F-d62728)
![review](https://img.shields.io/badge/review-fail%20closed-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/fauna/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion implementation lane:** `pipelines/domains/fauna/` — executable pipeline logic, the **how**  
**Placement posture:** Fauna declarative specs belong here unless an ADR or migration note establishes a different accepted spec home.  
**Public posture:** no public release, data storage, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Spec anti-collapse rules](#3-spec-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Fauna spec scope](#6-fauna-spec-scope)
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

`pipeline_specs/fauna/` owns declarative Fauna pipeline configuration.

It may describe:

- which Fauna pipeline profile should run;
- which source descriptor ids are in scope;
- which stage gates are required;
- which cadence, freshness, and source-vintage checks apply;
- which representation requirements apply before release handoff;
- which fixtures support no-network tests;
- which receipts, reports, blockers, and review handoffs are expected;
- which downstream implementation lane is authorized to execute the spec.

It does **not** implement pipeline behavior. Fauna implementation belongs under `pipelines/domains/fauna/` and related executable lanes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `fauna/`? | Fauna has a domain pipeline lane and needs domain-specific run profiles. | CONFIRMED path pattern / NEEDS VERIFICATION for active specs |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define Fauna objects? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Does this approve release? | No. Release decisions, manifests, correction notices, and rollback cards belong under release authority. | CONFIRMED authority separation |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not catalog truth, not a representation approval, and not release approval.

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
occurrence profile -> confirmed observation truth
representation profile -> review approval
spec summary -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- review records remain review artifacts, not spec assertions;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include declarative Fauna specs for:

- source-intake profiles;
- normalization profiles;
- validation profiles;
- representation-transform profiles;
- catalog and triplet profiles;
- publish-readiness profiles;
- rollback-readiness profiles;
- watcher profiles;
- proof or dry-run profiles;
- taxonomy, occurrence, monitoring, range, seasonal range, movement, mortality, disease, invasive-species, and public-indicator profile variants.

A good placement test:

> If the file answers “what Fauna pipeline should run, with what scope, review gates, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable Fauna pipeline code | `pipelines/domains/fauna/` |
| Shared executable helpers | `pipelines/<lane>/` or accepted package/tool home |
| Source connectors | `connectors/<source>/` |
| Source descriptors | `data/registry/sources/fauna/` or accepted registry home |
| Fauna object meaning | `contracts/domains/fauna/` and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/fauna/` or accepted schema home |
| Policy and review decisions | `policy/domains/fauna/`, `policy/sensitivity/fauna/`, review roots |
| Tests | `tests/pipeline_specs/fauna/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/fauna/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Fauna spec scope

Fauna specs may configure profiles for object families and candidate products such as:

- taxon and taxon crosswalk candidates;
- conservation/legal status candidates;
- occurrence evidence;
- restricted and public representation variants;
- range, seasonal range, and movement context;
- monitoring events;
- mortality and disease observations;
- invasive-species records;
- abundance and richness indicators;
- representation transforms, receipts, and release-readiness blockers.

Restricted observations, steward-controlled records, and unresolved rights or review state must default to hold, denial, aggregation, or release-reviewed representation posture.

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
- restricted/public representation requirements;
- representation transform and receipt requirements;
- EvidenceBundle requirements;
- review requirements;
- release blockers;
- rollback and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Fauna spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Cadence/freshness gate** — expected run cadence and stale-source behavior.
5. **Lifecycle gate** — allowed input and output lifecycle states.
6. **Review gate** — restricted, steward-controlled, and public representation posture.
7. **Representation gate** — public-safe transform, aggregation, generalization, or redaction requirements.
8. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
9. **Validation gate** — validators, finite outcomes, and blocker handling.
10. **Receipt gate** — required run, transform, validation, representation, redaction, or release-readiness receipts.
11. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipeline_specs/fauna/
├── README.md
├── ingest.yaml                    # PROPOSED
├── normalize.yaml                 # PROPOSED
├── validate.yaml                  # PROPOSED
├── representation_transform.yaml  # PROPOSED
├── catalog.yaml                   # PROPOSED
├── triplets.yaml                  # PROPOSED
├── publish.yaml                   # PROPOSED
├── rollback.yaml                  # PROPOSED
├── watchers.yaml                  # PROPOSED
├── taxonomy.yaml                  # PROPOSED
├── occurrence.yaml                # PROPOSED
├── monitoring.yaml                # PROPOSED
├── range.yaml                     # PROPOSED
├── health_mortality.yaml          # PROPOSED
└── invasive_species.yaml          # PROPOSED
```

These filenames are proposed placeholders until actual spec files and validators are implemented.

[⬆ Back to top](#top)

---

## 10. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/fauna/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Fauna normalize implementation |
| `validate` | Declare validators, finite outcomes, and required reports. | Fauna validate implementation |
| `representation_transform` | Declare public-safe transform, aggregation, redaction, and review requirements. | Fauna representation implementation |
| `catalog` | Declare catalog closure requirements. | Fauna catalog implementation |
| `triplets` | Declare graph/triplet projection profile. | Fauna triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Fauna/domain publish support |
| `rollback` | Declare rollback-readiness check profile. | Fauna/domain rollback support |
| `watchers` | Declare source-change observation profiles. | Fauna/domain watcher support |
| `object-family` | Declare taxonomy, occurrence, monitoring, range, health, invasive-species, or indicator profile variants. | Domain sublane implementations |

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/fauna/` | Declarative config only. |
| Executable target | `pipelines/domains/fauna/` or shared pipeline lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/fauna/` | Read by stable ref. |
| Fixture | `fixtures/pipeline_specs/fauna/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/fauna/` | Verifies shape and root boundaries. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/fauna/` | Emitted by execution, not by the spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/fauna/`, `release/manifests/fauna/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 12. Minimal spec profile shape

```yaml
schema_version: kfm.pipeline_spec.fauna.v1
spec_id: fauna.<profile>
version: 0.1.0
status: draft
domain: fauna
owner: <fauna-domain-steward>
implementation:
  target_pipeline: pipelines/domains/fauna/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  review_required: true
  representation_transform_required: true
  restricted_public_split_required: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  spec_is_policy_decision: false
  spec_is_review_approval: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/fauna/
├── test_spec_shape.py                      # PROPOSED
├── test_no_runtime_outputs.py              # PROPOSED
├── test_implementation_refs.py             # PROPOSED
├── test_source_descriptor_refs.py          # PROPOSED
├── test_lifecycle_states.py                # PROPOSED
├── test_review_gates.py                    # PROPOSED
├── test_representation_requirements.py     # PROPOSED
├── test_required_receipts.py               # PROPOSED
├── test_release_requirements.py            # PROPOSED
└── test_root_boundary.py                   # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, review gates, representation gates, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- replaces the short `pipeline_specs/fauna/README.md` stub;
- identifies this path as Fauna declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, data storage, proof storage, policy decisions, review approval, release approval, or public API/UI authority;
- defines expected Fauna profile families, lifecycle gates, review gates, representation gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/review posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-FAUNA-001` | Which Fauna spec schema is canonical for these profiles? | NEEDS VERIFICATION |
| `PIPE-SPEC-FAUNA-002` | Which first-wave Fauna source descriptors should be activated? | NEEDS VERIFICATION |
| `PIPE-SPEC-FAUNA-003` | Which profile should be implemented first: taxonomy, occurrence, monitoring, representation transform, catalog, or publish readiness? | NEEDS VERIFICATION |
| `PIPE-SPEC-FAUNA-004` | Which CI workflow validates Fauna specs? | UNKNOWN |
| `PIPE-SPEC-FAUNA-005` | Which representation and public-safe transform receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-FAUNA-006` | Should spec files be split by lifecycle stage, source family, object family, or review tier? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative. Do not add executable code, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, restricted public artifacts, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
