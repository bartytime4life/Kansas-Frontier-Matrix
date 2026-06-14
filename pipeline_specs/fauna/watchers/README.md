<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-fauna-watchers-readme
title: Fauna Watcher Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <fauna-domain-steward>
  - <watcher-steward>
  - <source-steward>
  - <evidence-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipeline_specs/fauna/watchers/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipeline_specs/fauna/README.md
  - pipelines/README.md
  - pipelines/watchers/README.md
  - pipelines/domains/fauna/README.md
  - docs/domains/fauna/ARCHITECTURE.md
  - data/registry/sources/fauna/
  - data/receipts/pipeline/fauna/watchers/
  - tests/pipeline_specs/fauna/watchers/
  - fixtures/pipeline_specs/fauna/watchers/
tags: [kfm, pipeline-specs, fauna, watchers, declarative-config, source-change, cadence, freshness, receipts, governance]
notes:
  - "This README replaces the one-character pipeline_specs/fauna/watchers stub with a governed declarative watcher-spec contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Fauna watcher specs configure source-change observation intent, source scope, cadence, material-change thresholds, review handoffs, and receipts. They do not execute watchers or admit source material."
  - "Watcher events are not source admission, RAW capture, EvidenceBundle closure, catalog truth, public truth, or release approval."
  - "Concrete watcher profiles, schema validation, CI coverage, fixtures, and activation state remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Watcher Pipeline Specs

> Declarative configuration lane for Fauna watcher profiles: source scopes, cadence, freshness checks, material-change thresholds, source-descriptor refs, candidate report expectations, receipt requirements, and review handoffs — separate from executable watcher logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fwatchers%2F-d62728)
![admission](https://img.shields.io/badge/source%20admission-separate-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/fauna/watchers/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Parent spec lane:** `pipeline_specs/fauna/`  
**Companion implementation lanes:** `pipelines/watchers/` and `pipelines/domains/fauna/` — executable pipeline logic, the **how**  
**Placement posture:** Fauna watcher specs belong here as declarative profiles unless an ADR or migration note establishes a different accepted spec home.  
**Public posture:** no public release, data storage, source admission, or executable side effect; specs only configure governed watcher runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Watcher spec anti-collapse rules](#3-watcher-spec-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Fauna watcher spec scope](#6-fauna-watcher-spec-scope)
- [7. Lifecycle posture](#7-lifecycle-posture)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Spec profile families](#10-spec-profile-families)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal watcher spec profile shape](#12-minimal-watcher-spec-profile-shape)
- [13. Tests, fixtures, and validation](#13-tests-fixtures-and-validation)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipeline_specs/fauna/watchers/` owns declarative Fauna watcher configuration.

It may describe:

- which Fauna source-change profile should be observed;
- which source descriptor ids are in scope;
- which source-head, version, manifest, checksum, ETag, header, date, or metadata checks apply;
- which cadence and stale-source behavior apply;
- which material-change classes should create candidate reports;
- which review handoffs and receipt outputs are expected;
- which downstream executable watcher lane is authorized to execute the spec.

It does **not** implement watcher behavior. Executable watcher logic belongs under `pipelines/watchers/` or an accepted Fauna domain watcher lane.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `fauna/watchers/`? | Fauna specs explicitly include watcher profiles, and this path narrows the watcher profile family. | CONFIRMED path pattern / NEEDS VERIFICATION for active specs |
| Does this execute watchers? | No. Execution belongs under `pipelines/watchers/` or accepted domain watcher lanes. | CONFIRMED separation |
| Does this admit source material? | No. Watchers observe change signals and create candidate reports or handoffs only. | CONFIRMED watcher posture |
| Does this define source authority? | No. Source authority belongs to governed source descriptors and registry controls. | CONFIRMED authority separation |
| Does this publish? | No. Watcher specs cannot publish or approve release. | CONFIRMED release separation |

> [!IMPORTANT]
> A watcher spec describes what should be observed and what checks should run. It is not a watcher event, not source admission, not RAW capture, not evidence, not catalog truth, and not release approval.

[⬆ Back to top](#top)

---

## 3. Watcher spec anti-collapse rules

Disallowed collapses:

```text
watcher spec -> watcher execution
watcher spec -> source admission
source list -> source authority
cadence -> source freshness proof
source-head match -> rights approval
material-change threshold -> ValidationReport
watcher report -> EvidenceBundle
watcher profile -> PUBLISHED
spec summary -> evidence
```

Required separations:

- watcher specs stay in `pipeline_specs/`;
- executable watcher logic stays in `pipelines/watchers/` or accepted domain implementation lanes;
- source descriptors stay in accepted source registry homes;
- candidate work records and receipts stay in lifecycle/receipt homes;
- EvidenceBundles stay in proof homes;
- release decisions stay under `release/`;
- unclear source, review, or representation state fails closed.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include declarative Fauna watcher specs for:

- source descriptor watch profiles;
- checklist-style source-head checks;
- source vintage and cadence profiles;
- manifest/checksum/ETag/header/date comparison profiles;
- material-change classification profiles;
- review-handoff profiles;
- candidate report and watcher receipt expectations;
- no-network dry-run profiles;
- source-family watcher variants for taxonomy, status, occurrence, monitoring, range, health, and invasive-species feeds.

A good placement test:

> If the file answers “what Fauna source should be watched, at what cadence, with what change checks and handoff rules?”, it may belong here. If it answers “how does the watcher execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable watcher code | `pipelines/watchers/` or accepted domain watcher lane |
| Fauna pipeline implementation | `pipelines/domains/fauna/` |
| Source connectors | `connectors/<source>/` |
| Source descriptors | `data/registry/sources/fauna/` or accepted registry home |
| Candidate work records | `data/work/fauna/` or accepted work-record home |
| QUARANTINE records | `data/quarantine/fauna/` |
| Receipts | `data/receipts/pipeline/fauna/watchers/` or accepted receipt home |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Fauna object meaning | `contracts/domains/fauna/` and domain doctrine |
| Schemas | `schemas/contracts/v1/domains/fauna/` or accepted schema home |
| Policy/review decisions | `policy/domains/fauna/`, `policy/sensitivity/fauna/`, review roots |
| Tests | `tests/pipeline_specs/fauna/watchers/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/fauna/watchers/` or accepted fixture home |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Fauna watcher spec scope

Fauna watcher specs may configure observation profiles for:

- taxonomic source drift;
- conservation or legal status source drift;
- occurrence-source update notices;
- monitoring feed update notices;
- range or seasonal range source updates;
- mortality, disease, or invasive-species source updates;
- public-indicator source updates;
- source descriptor drift and source-vintage warnings.

The spec should classify material change without deciding that changed source material is admitted, valid, processed, cataloged, or publishable.

[⬆ Back to top](#top)

---

## 7. Lifecycle posture

Watcher specs may target watcher handoff stages, but do not create lifecycle transitions:

```text
source signal -> watcher candidate report -> review / ingest decision
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare:

- source descriptor refs;
- expected cadence and freshness posture;
- checks to run;
- material-change classes;
- watcher report requirements;
- receipt requirements;
- review handoff requirements;
- downstream ingest or quarantine handoff posture.

Only governed executable pipelines and release authority can perform lifecycle transitions.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Fauna watcher spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, domain, lane, and version.
2. **Implementation gate** — target executable watcher lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Cadence gate** — expected run cadence, stale-source behavior, and retry posture.
5. **Change-check gate** — source-head, version, manifest, checksum, ETag, header, date, or metadata checks.
6. **Material-change gate** — classes that produce candidate reports or review handoffs.
7. **Review gate** — required steward or domain review handoff when material changes are detected.
8. **Receipt gate** — required watcher run and material-change receipts.
9. **Handoff gate** — downstream ingest, quarantine, or no-op posture.
10. **No-admission gate** — watcher output cannot admit source material by itself.
11. **No-release gate** — watcher output cannot publish or approve release.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipeline_specs/fauna/watchers/
├── README.md
├── taxonomy_sources.yaml          # PROPOSED
├── status_sources.yaml            # PROPOSED
├── occurrence_sources.yaml        # PROPOSED
├── monitoring_sources.yaml        # PROPOSED
├── range_sources.yaml             # PROPOSED
├── health_mortality_sources.yaml  # PROPOSED
├── invasive_species_sources.yaml  # PROPOSED
└── indicators_sources.yaml        # PROPOSED
```

These filenames are proposed placeholders until actual spec files and validators are implemented.

[⬆ Back to top](#top)

---

## 10. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `taxonomy_sources` | Watch taxonomy and crosswalk source-change signals. | shared watcher or Fauna watcher implementation |
| `status_sources` | Watch status source-change signals. | shared watcher or Fauna watcher implementation |
| `occurrence_sources` | Watch occurrence-source change notices. | shared watcher or Fauna watcher implementation |
| `monitoring_sources` | Watch monitoring-feed update notices. | shared watcher or Fauna watcher implementation |
| `range_sources` | Watch range or seasonal range source updates. | shared watcher or Fauna watcher implementation |
| `health_mortality_sources` | Watch mortality/disease source update notices. | shared watcher or Fauna watcher implementation |
| `invasive_species_sources` | Watch invasive-species source updates. | shared watcher or Fauna watcher implementation |
| `indicators_sources` | Watch source updates for public indicators. | shared watcher or Fauna watcher implementation |

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Watcher spec | `pipeline_specs/fauna/watchers/` | Declarative config only. |
| Executable target | `pipelines/watchers/` or accepted Fauna watcher lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/fauna/` | Required stable input. |
| Fixture | `fixtures/pipeline_specs/fauna/watchers/` or accepted fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/fauna/watchers/` | Verifies shape and root boundaries. |
| Candidate report | `data/work/fauna/` or accepted work-record home | Emitted by executable watcher, not by spec alone. |
| QUARANTINE handoff | `data/quarantine/fauna/` | For unresolved or unsupported material changes. |
| Receipts | `data/receipts/pipeline/fauna/watchers/` | Emitted by execution, not by spec file alone. |

[⬆ Back to top](#top)

---

## 12. Minimal watcher spec profile shape

```yaml
schema_version: kfm.pipeline_spec.fauna.watcher.v1
spec_id: fauna.watchers.<profile>
version: 0.1.0
status: draft
domain: fauna
lane: watchers
owner: <fauna-domain-steward>
implementation:
  target_pipeline: pipelines/watchers/<adapter-or-profile>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
watch:
  cadence: manual
  checks:
    - source_head
    - manifest_digest
    - source_vintage
material_change:
  report_required: true
  review_required: true
  admit_to_raw: false
receipts:
  watcher_run_receipt_required: true
  material_change_receipt_required: true
anti_collapse:
  spec_is_executable: false
  watcher_event_is_source_admission: false
  watcher_report_is_evidence_bundle: false
  watcher_result_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 13. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/fauna/watchers/
├── test_spec_shape.py                    # PROPOSED
├── test_no_runtime_outputs.py            # PROPOSED
├── test_implementation_refs.py           # PROPOSED
├── test_source_descriptor_refs.py        # PROPOSED
├── test_cadence_and_checks.py            # PROPOSED
├── test_material_change_rules.py         # PROPOSED
├── test_no_source_admission.py           # PROPOSED
├── test_required_receipts.py             # PROPOSED
└── test_root_boundary.py                 # PROPOSED
```

A watcher spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, cadence assertions, change-check assertions, material-change handling, receipt requirements, and explicit no-admission/no-release posture.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- replaces the one-character `pipeline_specs/fauna/watchers/README.md` stub;
- identifies this path as Fauna watcher declarative configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks watcher specs from becoming executable logic, source admission, lifecycle storage, proof storage, catalog truth, release approval, or public API/UI authority;
- defines expected watcher profile families, source-change gates, cadence gates, review gates, receipts, fixtures, tests, and open questions.

Future watcher spec files are done only when they validate, point to executable watcher lanes, use stable source descriptors, declare cadence/change checks, require receipts, preserve review posture, and document downstream ingest/quarantine behavior.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-FAUNA-WATCH-001` | Which Fauna watcher spec schema is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-FAUNA-WATCH-002` | Which first-wave Fauna source descriptors should be watched? | NEEDS VERIFICATION |
| `PIPE-SPEC-FAUNA-WATCH-003` | Which executable lane should own domain-specific watcher adapters: shared `pipelines/watchers/` or `pipelines/domains/fauna/watchers/`? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-FAUNA-WATCH-004` | Which CI workflow validates Fauna watcher specs? | UNKNOWN |
| `PIPE-SPEC-FAUNA-WATCH-005` | Which MaterialChangeReport and watcher receipt schemas are canonical? | NEEDS VERIFICATION |

---

## Maintainer note

Keep this directory declarative. Do not add executable watcher code, source clients, source descriptors, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
