<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-air-readme
title: Air Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <atmosphere-domain-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/air/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipelines/README.md
  - pipelines/domains/air/README.md
  - pipelines/domains/atmosphere/README.md
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/SOURCE_REGISTRY.md
  - docs/domains/atmosphere/DATA_LIFECYCLE.md
  - docs/domains/atmosphere/CANONICAL_PATHS.md
  - docs/domains/atmosphere/API_CONTRACTS.md
  - data/registry/sources/atmosphere/
  - data/receipts/pipeline/atmosphere/
  - tests/pipeline_specs/air/
  - fixtures/pipeline_specs/air/
tags: [kfm, pipeline-specs, air, atmosphere, declarative-config, weather, air-quality, smoke, aod, climate, lifecycle, receipts, governance]
notes:
  - "This README replaces the one-character pipeline_specs/air stub with a governed declarative-spec lane contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Visible domain doctrine treats Air / Atmosphere as a slug-conflicted lane; this README keeps air as a NEEDS VERIFICATION alias-candidate for declarative specs."
  - "Concrete spec filenames, schema validation, CI coverage, and activation state remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Air Pipeline Specs

> Declarative configuration lane for Air / Atmosphere pipeline profiles, source scopes, schedules, stage gates, caveat requirements, evidence requirements, fixtures, and release-readiness intent — separate from executable pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2F-d62728)
![slug](https://img.shields.io/badge/slug-air%20vs%20atmosphere%20NEEDS%20VERIFICATION-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/air/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion implementation lane:** `pipelines/domains/air/` or accepted Atmosphere implementation lane — executable pipeline logic, the **how**  
**Placement posture:** `NEEDS VERIFICATION`; existing domain docs use `atmosphere` while this requested spec path uses `air`. Do not create parallel spec authority without ADR or migration note.  
**Public posture:** no public release, data storage, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Slug posture: air vs atmosphere](#3-slug-posture-air-vs-atmosphere)
- [4. Spec anti-collapse rules](#4-spec-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Air / Atmosphere spec scope](#7-air--atmosphere-spec-scope)
- [8. Lifecycle posture](#8-lifecycle-posture)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Profile families](#11-profile-families)
- [12. Inputs and outputs](#12-inputs-and-outputs)
- [13. Minimal spec profile shape](#13-minimal-spec-profile-shape)
- [14. Tests, fixtures, and validation](#14-tests-fixtures-and-validation)
- [15. Definition of done](#15-definition-of-done)
- [16. Open questions](#16-open-questions)

---

## 1. Purpose

`pipeline_specs/air/` is a declarative configuration lane for requested Air / Atmosphere pipeline profiles.

It may describe:

- which Air / Atmosphere pipeline profile should run;
- which source descriptor ids are in scope;
- which stage gates are required;
- which cadence, freshness, and source-vintage checks apply;
- which caveats apply to low-cost sensors, model fields, AOD, AQI context, and advisory context;
- which fixtures support no-network tests;
- which receipts, reports, and blockers are expected;
- which downstream executable lane is authorized to run the profile.

It does **not** implement pipeline behavior. Executable logic belongs under `pipelines/` lanes such as `pipelines/domains/air/` or an accepted Atmosphere lane.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `air/`? | User requested this path; visible domain docs treat Air / Atmosphere slug placement as unresolved. | NEEDS VERIFICATION |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define Air / Atmosphere objects? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Does this approve release? | No. Release decisions and manifests belong under `release/`. | CONFIRMED authority separation |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not catalog truth, and not release approval.

[⬆ Back to top](#top)

---

## 3. Slug posture: air vs atmosphere

This requested path uses `air`, while visible domain documentation uses `atmosphere` as the main domain lane and records `air` versus `atmosphere` slug drift.

Until an ADR or lane register resolves the canonical slug:

- treat `pipeline_specs/air/` as an alias-candidate or transitional spec lane;
- do not create duplicate authoritative specs under both `air` and `atmosphere` for the same profile;
- prefer existing `atmosphere` source, schema, policy, and release names where they are already established;
- document any migration with path mapping, tests, compatibility notes, and rollback notes.

[⬆ Back to top](#top)

---

## 4. Spec anti-collapse rules

Disallowed collapses:

```text
spec file -> executable pipeline
spec profile -> release approval
source list -> source authority
schedule -> source freshness proof
validation profile -> ValidationReport
catalog profile -> catalog truth
publish profile -> PUBLISHED
model-field profile -> observation truth
AOD profile -> PM2.5 truth
spec summary -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- release decisions stay under `release/`;
- emergency/life-safety advisories redirect to official issuing authorities.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include declarative Air / Atmosphere specs for:

- source-intake profiles;
- normalization profiles;
- validation profiles;
- catalog and triplet profiles;
- publish-readiness profiles;
- rollback-readiness profiles;
- watcher profiles;
- air-quality observation profiles;
- weather and mesonet profiles;
- smoke, aerosol, model, climate, and advisory-context profiles;
- dry-run profiles that only declare intent and gates.

A good placement test:

> If the file answers “what Air / Atmosphere pipeline should run, with what scope and gates?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable Air / Atmosphere pipeline code | `pipelines/domains/air/` or accepted Atmosphere lane |
| Shared executable helpers | `pipelines/<lane>/` or accepted package/tool home |
| Source connectors | `connectors/<source>/` |
| Source descriptors | `data/registry/sources/atmosphere/` or accepted registry home |
| Domain object meaning | `contracts/domains/atmosphere/` and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/atmosphere/` or accepted schema home |
| Policy and review decisions | `policy/domains/atmosphere/`, `policy/release/`, review roots |
| Tests | `tests/pipeline_specs/air/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/air/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 7. Air / Atmosphere spec scope

Air / Atmosphere specs may configure profiles for candidate products such as:

- air stations and air observations;
- PM2.5 and ozone observations;
- smoke context;
- aerosol optical depth rasters;
- weather stations and weather observations;
- wind, precipitation, and temperature observations;
- climate normals and anomalies;
- forecast/model context;
- advisory context with official-source redirection;
- public-safe, caveat-aware, evidence-backed derived products.

This domain is not an emergency alert system. Life-safety instructions must point to the official issuing authority and remain outside the spec’s release claims.

[⬆ Back to top](#top)

---

## 8. Lifecycle posture

Specs may target lifecycle stages, but do not create the lifecycle transition themselves:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare:

- input lifecycle state;
- expected output lifecycle state;
- source descriptor refs;
- validators and caveat checks;
- EvidenceBundle requirements;
- ReviewRecord requirements;
- receipt requirements;
- release blockers;
- rollback and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 9. Required gates

Every Air / Atmosphere spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Cadence/freshness gate** — expected run cadence and stale-source behavior.
5. **Lifecycle gate** — allowed input and output lifecycle states.
6. **Caveat gate** — low-cost sensor, model field, AOD, AQI, and advisory-context caveats where relevant.
7. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
8. **Validation gate** — validators, finite outcomes, and blocker handling.
9. **Receipt gate** — required run, transform, validation, caveat, or release-readiness receipts.
10. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipeline_specs/air/
├── README.md
├── ingest.yaml                 # PROPOSED
├── normalize.yaml              # PROPOSED
├── validate.yaml               # PROPOSED
├── catalog.yaml                # PROPOSED
├── triplets.yaml               # PROPOSED
├── publish.yaml                # PROPOSED
├── rollback.yaml               # PROPOSED
├── watchers.yaml               # PROPOSED
├── air_quality.yaml            # PROPOSED
├── weather.yaml                # PROPOSED
├── smoke_aod.yaml              # PROPOSED
├── climate.yaml                # PROPOSED
└── advisory_context.yaml       # PROPOSED
```

These filenames are proposed placeholders until actual spec files and validators are implemented.

[⬆ Back to top](#top)

---

## 11. Profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/air/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Air / Atmosphere normalize implementation |
| `validate` | Declare validators, caveats, outcomes, and reports. | Air / Atmosphere validate implementation |
| `catalog` | Declare catalog closure requirements. | Air / Atmosphere catalog implementation |
| `triplets` | Declare graph/triplet projection profile. | Air / Atmosphere triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Air / Atmosphere publish support |
| `rollback` | Declare rollback-readiness check profile. | Air / Atmosphere rollback support |
| `watchers` | Declare source-change observation profiles. | Air / Atmosphere watcher support |
| `source-family` | Declare air-quality, weather, smoke/AOD, climate, or advisory-context variants. | Domain source-family implementations |

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/air/` | Declarative config only. |
| Executable target | `pipelines/domains/air/` or accepted Atmosphere lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/atmosphere/` | Read by stable ref. |
| Fixture | `fixtures/pipeline_specs/air/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/air/` | Verifies shape and root boundaries. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/atmosphere/` | Emitted by execution, not by the spec file alone. |
| Release material | `release/candidates/atmosphere/`, `release/manifests/atmosphere/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 13. Minimal spec profile shape

The final schema is not defined here. This example shows the minimum intent a spec should preserve.

```yaml
schema_version: kfm.pipeline_spec.air.v1
spec_id: air.<profile>
version: 0.1.0
status: draft
domain: air-atmosphere
canonical_slug: NEEDS_VERIFICATION
owner: <atmosphere-domain-steward>
implementation:
  target_pipeline: pipelines/domains/air/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  review_required: true
  caveats_required: []
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  spec_is_evidence: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 14. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/air/
├── test_spec_shape.py                 # PROPOSED
├── test_no_runtime_outputs.py          # PROPOSED
├── test_implementation_refs.py         # PROPOSED
├── test_source_descriptor_refs.py      # PROPOSED
├── test_lifecycle_states.py            # PROPOSED
├── test_caveat_requirements.py         # PROPOSED
├── test_required_receipts.py           # PROPOSED
├── test_release_requirements.py        # PROPOSED
└── test_root_boundary.py               # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, caveat requirements, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- replaces the one-character `pipeline_specs/air/README.md` stub;
- identifies this path as Air / Atmosphere declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- marks the air/atmosphere slug decision as unresolved;
- blocks specs from becoming executable logic, data storage, proof storage, policy decisions, release approval, or public API/UI authority;
- defines expected profile families, lifecycle gates, caveat gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/review posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-AIR-001` | Is `air` or `atmosphere` the canonical spec slug? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-AIR-002` | Which spec schema is canonical for Air / Atmosphere profiles? | NEEDS VERIFICATION |
| `PIPE-SPEC-AIR-003` | Which first-wave source descriptors should be activated? | NEEDS VERIFICATION |
| `PIPE-SPEC-AIR-004` | Which source-family profile should be implemented first: air quality, weather, smoke/AOD, climate, or advisory context? | NEEDS VERIFICATION |
| `PIPE-SPEC-AIR-005` | Which CI workflow validates Air / Atmosphere specs? | UNKNOWN |
| `PIPE-SPEC-AIR-006` | Should specs be split by lifecycle stage, source family, or canonical object family? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative. Do not add executable code, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
