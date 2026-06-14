<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-hazards-readme
title: Hazards Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <hazards-domain-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/hazards/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipelines/README.md
  - pipelines/domains/hazards/README.md
  - docs/domains/hazards/ARCHITECTURE.md
  - docs/domains/hazards/DATA_LIFECYCLE.md
  - docs/domains/hazards/EXPANSION_BACKLOG.md
  - data/registry/sources/hazards/
  - data/receipts/pipeline/hazards/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/hazards/
  - fixtures/pipeline_specs/hazards/
tags: [kfm, pipeline-specs, hazards, declarative-config, severe-weather, flood, wildfire, smoke, drought, heat, earthquake, exposure, resilience, receipts, governance]
notes:
  - "This README replaces the short pipeline_specs/hazards stub with a governed declarative-spec lane contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Hazards specs configure pipeline intent, source scope, lifecycle gates, freshness and expiry gates, knowledge-character labels, evidence gates, receipts, and release blockers. They do not execute pipeline logic or store lifecycle outputs."
  - "Hazards is not an emergency alerting or life-safety instruction system. Operational context must redirect to official sources."
  - "Concrete spec filenames, schema validation, CI coverage, and activation state remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Pipeline Specs

> Declarative configuration lane for Hazards pipeline profiles, source scopes, schedules, lifecycle gates, freshness/expiry checks, knowledge-character labels, evidence requirements, fixtures, receipts, and release-readiness intent — separate from executable Hazards pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fdomains%2Fhazards%2F-d62728)
![life-safety](https://img.shields.io/badge/life--safety-boundary-required-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/hazards/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion implementation lane:** `pipelines/domains/hazards/` — executable pipeline logic, the **how**  
**Placement posture:** Hazards declarative specs belong here unless an ADR or migration note establishes a different accepted spec home.  
**Public posture:** no public release, data storage, alerting, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Life-safety boundary](#3-life-safety-boundary)
- [4. Spec anti-collapse rules](#4-spec-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Hazards spec scope](#7-hazards-spec-scope)
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

`pipeline_specs/hazards/` owns declarative Hazards pipeline configuration.

It may describe:

- which Hazards pipeline profile should run;
- which source descriptor ids are in scope;
- which source-family, cadence, source-vintage, issue-time, expiry-time, and freshness checks apply;
- which lifecycle gates are required;
- which knowledge-character, operational-context, regulatory-context, model/observation, and public-safe representation requirements apply;
- which fixtures support no-network tests;
- which receipts, reports, blockers, and review handoffs are expected;
- which downstream implementation lane is authorized to execute the spec.

It does **not** implement pipeline behavior. Hazards implementation belongs under `pipelines/domains/hazards/` and related executable lanes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `hazards/`? | Hazards has a domain pipeline lane and needs domain-specific run profiles. | CONFIRMED path pattern / NEEDS VERIFICATION for active specs |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define Hazards objects? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Does this issue alerts or approve release? | No. Specs cannot issue alerts, provide instructions, publish, or approve release. | CONFIRMED boundary posture |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not catalog truth, not an official warning, not life-safety instruction, and not release approval.

[⬆ Back to top](#top)

---

## 3. Life-safety boundary

KFM Hazards specs must preserve the life-safety boundary.

Any operational warning, watch, advisory, or comparable operational-context profile must declare:

- official source identity;
- issue time;
- expiry time or valid-through state;
- retrieval and processing time;
- freshness state;
- official-source redirect;
- non-life-safety posture;
- EvidenceBundle or source reference requirements;
- finite policy outcome.

If the required operational-context fields cannot be proven, the profile must fail closed or route to review/quarantine. Specs must not provide emergency instructions.

[⬆ Back to top](#top)

---

## 4. Spec anti-collapse rules

Disallowed collapses:

```text
spec file -> executable pipeline
spec profile -> release approval
source list -> source authority
schedule -> source freshness proof
watch/warning/advisory context -> emergency instruction
historical event -> current operational hazard
regulatory context -> observed event
model derivative -> observation truth
exposure summary -> impact truth
generated summary -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- historical event, regulatory context, scientific observation, remote-sensing detection, modeled derivative, operational context, administrative declaration, exposure summary, and generated summary states remain separately labeled;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include declarative Hazards specs for:

- source-intake profiles;
- normalization profiles;
- validation profiles;
- catalog and triplet profiles;
- publish-readiness profiles;
- rollback-readiness profiles;
- watcher profiles;
- proof or dry-run profiles;
- historical-event, regulatory-context, observation, remote-sensing, model, operational-context, administrative-declaration, exposure, and resilience-timeline variants.

A good placement test:

> If the file answers “what Hazards pipeline should run, with what source scope, freshness/expiry gates, knowledge-character labels, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable Hazards pipeline code | `pipelines/domains/hazards/` |
| Shared executable helpers | `pipelines/<lane>/` or accepted package/tool home |
| Source connectors | `connectors/<source>/` |
| Source descriptors | `data/registry/sources/hazards/` or accepted registry home |
| Hazards object meaning | `contracts/hazards/`, `contracts/domains/hazards/`, and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/hazards/` or accepted schema home |
| Policy and review decisions | `policy/domains/hazards/`, `policy/sensitivity/hazards/`, review roots |
| Tests | `tests/pipeline_specs/hazards/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/hazards/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 7. Hazards spec scope

Hazards specs may configure profiles for object families and candidate products such as:

- historical events for severe weather, flood, wildfire, smoke, drought, earthquake, heat, cold, hail, wind, and tornado records;
- regulatory hazard context such as flood zones and comparable archives;
- scientific observations and remote-sensing detections;
- modeled derivatives, exposure summaries, and resilience timelines;
- operational warning/watch/advisory context with issue time, expiry time, freshness state, and official-source redirect;
- administrative declarations and emergency-management context as administrative records;
- public-safe generalized map products and release-reviewed derivatives.

Hazards cites other lanes for context. It does not duplicate or override Hydrology, Atmosphere, Infrastructure, Roads/Rail, Geology, Soil, Agriculture, Archaeology, People, or other canonical domain claims.

[⬆ Back to top](#top)

---

## 8. Lifecycle posture

Specs may target lifecycle stages, but do not create the lifecycle transition themselves:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare input lifecycle state, expected output lifecycle state, source descriptor refs, knowledge-character labels, operational-context freshness/expiry checks, EvidenceBundle requirements, receipt requirements, release blockers, rollback support, and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 9. Required gates

Every Hazards spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Cadence/freshness gate** — expected run cadence, issue/expiry handling, stale-source behavior, and official-source redirect where relevant.
5. **Lifecycle gate** — allowed input and output lifecycle states.
6. **Knowledge-character gate** — historical, regulatory, observational, remote-sensing, modeled, operational-context, administrative, exposure, and generated-summary distinctions.
7. **Life-safety gate** — operational context is contextual only and not instruction.
8. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
9. **Receipt gate** — required run, transform, validation, freshness, expiry, source-vintage, or release-readiness receipts.
10. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipeline_specs/hazards/
├── README.md
├── ingest.yaml                     # PROPOSED
├── normalize.yaml                  # PROPOSED
├── validate.yaml                   # PROPOSED
├── catalog.yaml                    # PROPOSED
├── triplets.yaml                   # PROPOSED
├── publish.yaml                    # PROPOSED
├── rollback.yaml                   # PROPOSED
├── watchers.yaml                   # PROPOSED
├── historical_events.yaml          # PROPOSED
├── regulatory_context.yaml         # PROPOSED
├── observations_remote_sensing.yaml # PROPOSED
├── modeled_derivatives.yaml        # PROPOSED
├── operational_context.yaml        # PROPOSED
├── administrative_declarations.yaml # PROPOSED
└── exposure_resilience.yaml         # PROPOSED
```

These filenames are proposed placeholders until actual spec files and validators are implemented.

[⬆ Back to top](#top)

---

## 11. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/hazards/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Hazards normalize implementation |
| `validate` | Declare freshness, expiry, knowledge-character, and boundary checks. | Hazards validate implementation |
| `catalog` | Declare catalog closure requirements. | Hazards catalog implementation |
| `triplets` | Declare graph/triplet projection profile. | Hazards triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Hazards/domain publish support |
| `rollback` | Declare rollback-readiness check profile. | Hazards/domain rollback support |
| `watchers` | Declare source-change observation profiles. | Hazards/domain watcher support |
| `source-family` | Declare historical, regulatory, observation, remote-sensing, model, operational-context, administrative, exposure, or resilience variants. | Domain sublane implementations |

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/hazards/` | Declarative config only. |
| Executable target | `pipelines/domains/hazards/` or shared pipeline lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/hazards/` | Read by stable ref. |
| Fixture | `fixtures/pipeline_specs/hazards/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/hazards/` | Verifies shape and root boundaries. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/hazards/` | Emitted by execution, not by the spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/hazards/`, `release/manifests/hazards/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 13. Minimal spec profile shape

```yaml
schema_version: kfm.pipeline_spec.hazards.v1
spec_id: hazards.<profile>
version: 0.1.0
status: draft
domain: hazards
owner: <hazards-domain-steward>
implementation:
  target_pipeline: pipelines/domains/hazards/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  knowledge_character_labels_required: true
  official_source_redirect_required: true
  freshness_or_expiry_check_required: true
  not_for_life_safety: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  spec_is_alerting_system: false
  spec_is_life_safety_instruction: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 14. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/hazards/
├── test_spec_shape.py                      # PROPOSED
├── test_no_runtime_outputs.py              # PROPOSED
├── test_implementation_refs.py             # PROPOSED
├── test_source_descriptor_refs.py          # PROPOSED
├── test_lifecycle_states.py                # PROPOSED
├── test_freshness_and_expiry_requirements.py # PROPOSED
├── test_knowledge_character_labels.py      # PROPOSED
├── test_life_safety_boundary.py            # PROPOSED
├── test_required_receipts.py               # PROPOSED
└── test_root_boundary.py                   # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, freshness/expiry checks, knowledge-character labels, life-safety boundary checks, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- replaces the short `pipeline_specs/hazards/README.md` stub;
- identifies this path as Hazards declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, data storage, proof storage, policy decisions, official warnings, life-safety instructions, release approval, or public API/UI authority;
- defines expected Hazards profile families, lifecycle gates, freshness/expiry gates, knowledge-character gates, life-safety gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/review/life-safety-boundary posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-HAZ-001` | Which Hazards spec schema is canonical for these profiles? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAZ-002` | Which first-wave Hazards source descriptors should be activated? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAZ-003` | Which profile should be implemented first: historical events, regulatory context, observations, remote sensing, modeled derivatives, operational context, or exposure/resilience? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAZ-004` | Which CI workflow validates Hazards specs? | UNKNOWN |
| `PIPE-SPEC-HAZ-005` | Which freshness, expiry, knowledge-character, and operational-context receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-HAZ-006` | Should specs be split by lifecycle stage, source family, hazard family, or knowledge-character family? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative. Do not add executable code, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, warning instructions, public API code, UI code, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
