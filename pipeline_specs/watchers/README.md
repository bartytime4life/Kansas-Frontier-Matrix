<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-watchers-readme
title: Watcher Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <watcher-steward>
  - <source-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-watcher-review-gates
path: pipeline_specs/watchers/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipelines/README.md
  - pipelines/watchers/README.md
  - pipeline_specs/fauna/watchers/README.md
  - pipeline_specs/flora/watchers/README.md
  - pipelines/domains/
  - connectors/
  - data/registry/sources/
  - data/work/
  - data/quarantine/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/
  - tests/pipeline_specs/watchers/
  - fixtures/pipeline_specs/watchers/
tags: [kfm, pipeline-specs, watchers, declarative-config, source-change, material-change, cadence, freshness, source-head, etag, checksum, manifest, receipts, governance]
notes:
  - "This README replaces the one-character pipeline_specs/watchers stub with a governed declarative watcher-spec lane contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Watcher specs configure source-change observation intent, source scope, cadence, freshness checks, material-change thresholds, review handoffs, and receipt requirements. They do not execute watchers or admit source material."
  - "Watcher events are not source admission, RAW capture, EvidenceBundle closure, catalog truth, public truth, or release approval."
  - "Concrete watcher profiles, schema validation, CI coverage, fixtures, source activation, and release wiring remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Watcher Pipeline Specs

> Declarative configuration lane for shared watcher profiles: source scopes, source-descriptor refs, cadence, freshness checks, source-head checks, manifest/checksum/ETag/header/date comparisons, material-change thresholds, candidate report expectations, receipt requirements, and review handoffs — separate from executable watcher logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fwatchers%2F-d62728)
![admission](https://img.shields.io/badge/source%20admission-separate-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/watchers/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion implementation lane:** `pipelines/watchers/` — executable watcher orchestration, the **how**  
**Domain-specific spec posture:** domain watcher specs may live under `pipeline_specs/<domain>/watchers/` when they narrow source families or domain review rules.  
**Public posture:** no public release, data storage, source admission, RAW capture, or executable side effect; specs only configure governed watcher runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Watcher spec anti-collapse rules](#3-watcher-spec-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Watcher spec scope](#6-watcher-spec-scope)
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

`pipeline_specs/watchers/` owns shared declarative watcher configuration for KFM source-change observation.

It may describe:

- which source-change profile should be observed;
- which source descriptor ids are in scope;
- which source-head, version, manifest, checksum, ETag, header, date, or metadata checks apply;
- which cadence and stale-source behavior apply;
- which material-change classes should create candidate reports;
- which unresolved changes should route to review or quarantine;
- which receipts and review handoffs are expected;
- which downstream executable watcher lane is authorized to execute the spec.

It does **not** implement watcher behavior. Executable watcher logic belongs under `pipelines/watchers/` or accepted domain watcher implementation lanes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why shared `watchers/`? | Shared watcher profiles can configure source-change checks used across multiple domains without becoming domain truth. | PROPOSED / NEEDS VERIFICATION |
| Does this execute watchers? | No. Execution belongs under `pipelines/watchers/` or accepted domain implementation lanes. | CONFIRMED separation |
| Does this admit source material? | No. Watchers observe change signals and create candidate reports or handoffs only. | CONFIRMED watcher posture |
| Does this define source authority? | No. Source authority belongs to governed source descriptors and registry controls. | CONFIRMED authority separation |
| Does this publish? | No. Watcher specs cannot publish or approve release. | CONFIRMED release separation |

> [!IMPORTANT]
> A watcher spec describes what should be observed and what checks should run. It is not a watcher event, not source admission, not RAW capture, not evidence, not catalog truth, not public truth, and not release approval.

[⬆ Back to top](#top)

---

## 3. Watcher spec anti-collapse rules

Disallowed collapses:

```text
watcher spec -> watcher execution
watcher spec -> source admission
watcher spec -> RAW capture
source list -> source authority
cadence -> source freshness proof
source-head match -> rights approval
checksum match -> validation pass
material-change threshold -> ValidationReport
watcher report -> EvidenceBundle
watcher profile -> PUBLISHED
spec summary -> evidence
```

Required separations:

- watcher specs stay in `pipeline_specs/`;
- executable watcher logic stays in `pipelines/watchers/` or accepted domain implementation lanes;
- source descriptors stay in accepted source registry homes;
- connectors own upstream access and staging authority;
- candidate work records and quarantine records stay in lifecycle homes;
- receipts stay in receipt homes;
- EvidenceBundles stay in proof homes;
- release decisions stay under `release/`;
- unclear source, review, representation, rights, policy, or sensitivity state fails closed.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include declarative watcher specs for:

- source descriptor watch profiles;
- source-head and source-vintage checks;
- cadence and stale-source profiles;
- manifest/checksum/ETag/header/date comparison profiles;
- source descriptor drift profiles;
- material-change classification profiles;
- candidate report and proposed work-record expectations;
- quarantine/review handoff rules;
- watcher run receipt and material-change receipt requirements;
- no-network dry-run watcher profiles;
- shared source-family profiles that are not specific enough to belong under `pipeline_specs/<domain>/watchers/`.

A good placement test:

> If the file answers “what source should be watched, at what cadence, with what change checks and handoff rules?”, it may belong here. If it answers “how does the watcher execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable watcher code | `pipelines/watchers/` or accepted domain watcher lane |
| Domain pipeline implementation | `pipelines/domains/<domain>/` |
| Source connectors | `connectors/<source>/` |
| Source descriptors | `data/registry/sources/<domain>/` or accepted registry home |
| Candidate work records | `data/work/<domain>/` or accepted work-record home |
| QUARANTINE records | `data/quarantine/<domain>/` |
| Runtime receipts | `data/receipts/pipeline/<domain>/watchers/` or accepted receipt home |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Schemas | `schemas/contracts/v1/...` accepted schema home |
| Contracts/object meaning | `contracts/...` accepted contract home |
| Policy decisions | `policy/...` responsibility roots |
| Tests | `tests/pipeline_specs/watchers/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/watchers/` or accepted fixture home |
| Release decisions | `release/...` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Watcher spec scope

Shared watcher specs may configure profiles for candidate products such as:

- source availability checks;
- source-head and source-version checks;
- source-vintage and cadence checks;
- manifest, checksum, ETag, Last-Modified, header, date, and metadata checks;
- source descriptor drift checks;
- material-change classification;
- candidate `MaterialChangeReport` expectations;
- candidate work-record handoff expectations;
- QUARANTINE routing for unsupported or unresolved changes;
- review handoff expectations;
- watcher receipt requirements.

Domain-sensitive watcher profiles should move into domain-specific spec sublanes when they need domain-specific source roles, review rules, sensitivity posture, or public-safe representation posture.

[⬆ Back to top](#top)

---

## 7. Lifecycle posture

Watcher specs may target watcher handoff stages, but do not create lifecycle transitions:

```text
source signal -> watcher candidate report -> review / ingest decision
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare source descriptor refs, expected cadence, freshness posture, checks to run, material-change classes, watcher report requirements, receipt requirements, review handoff requirements, downstream ingest posture, quarantine posture, and no-op posture.

Only governed executable pipelines and release authority can perform lifecycle transitions.

[⬆ Back to top](#top)

---

## 8. Required gates

Every watcher spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, lane, domain applicability, and version.
2. **Implementation gate** — target executable watcher lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Cadence gate** — expected run cadence, stale-source behavior, and retry posture.
5. **Change-check gate** — source-head, version, manifest, checksum, ETag, header, date, or metadata checks.
6. **Material-change gate** — classes that produce candidate reports or review handoffs.
7. **Review gate** — required steward, source, policy, or domain review handoff when material changes are detected.
8. **Receipt gate** — required watcher run and material-change receipts.
9. **Handoff gate** — downstream ingest, quarantine, or no-op posture.
10. **No-admission gate** — watcher output cannot admit source material by itself.
11. **No-release gate** — watcher output cannot publish or approve release.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipeline_specs/watchers/
├── README.md
├── source_head.yaml             # PROPOSED
├── source_vintage.yaml          # PROPOSED
├── cadence_freshness.yaml       # PROPOSED
├── checksum_manifest.yaml       # PROPOSED
├── etag_header_date.yaml        # PROPOSED
├── source_descriptor_drift.yaml # PROPOSED
├── material_change.yaml         # PROPOSED
├── review_handoff.yaml          # PROPOSED
├── quarantine_handoff.yaml      # PROPOSED
└── no_network_dry_run.yaml      # PROPOSED
```

These filenames are proposed placeholders until actual spec files and validators are implemented.

[⬆ Back to top](#top)

---

## 10. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `source_head` | Watch source-head or source-version signatures. | `pipelines/watchers/` |
| `source_vintage` | Watch source vintage, issue dates, update dates, or release-cycle metadata. | `pipelines/watchers/` |
| `cadence_freshness` | Declare cadence, stale-source, retry, and no-op posture. | `pipelines/watchers/` |
| `checksum_manifest` | Compare checksums, manifests, package digests, and payload signatures. | `pipelines/watchers/` |
| `etag_header_date` | Compare ETag, Last-Modified, headers, and metadata fields. | `pipelines/watchers/` |
| `source_descriptor_drift` | Detect mismatch between source descriptor expectations and observed source metadata. | `pipelines/watchers/` |
| `material_change` | Classify detected changes into bounded candidate categories. | `pipelines/watchers/` |
| `review_handoff` | Declare steward/domain/source/policy review handoff requirements. | `pipelines/watchers/` |
| `quarantine_handoff` | Declare fail-closed routing for unsupported or unresolved changes. | `pipelines/watchers/` |
| `domain_watchers` | Narrow shared watcher profiles for domain-specific lanes. | `pipeline_specs/<domain>/watchers/` and accepted domain implementation lanes |

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Watcher spec | `pipeline_specs/watchers/` or `pipeline_specs/<domain>/watchers/` | Declarative config only. |
| Executable target | `pipelines/watchers/` or accepted domain watcher lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/<domain>/` | Required stable input. |
| Fixture | `fixtures/pipeline_specs/watchers/` or accepted domain fixture home | Supports no-network validation. |
| Spec validation test | `tests/pipeline_specs/watchers/` | Verifies shape and root boundaries. |
| Candidate report | `data/work/<domain>/` or accepted work-record home | Emitted by executable watcher, not by spec alone. |
| QUARANTINE handoff | `data/quarantine/<domain>/` | For unresolved or unsupported material changes. |
| Receipts | `data/receipts/pipeline/<domain>/watchers/` | Emitted by execution, not by spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced later; watcher report is not a proof by itself. |
| Release material | `release/candidates/<domain>/`, `release/manifests/<domain>/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 12. Minimal watcher spec profile shape

```yaml
schema_version: kfm.pipeline_spec.watcher.v1
spec_id: watchers.<profile>
version: 0.1.0
status: draft
lane: watchers
owner: <watcher-steward>
implementation:
  target_pipeline: pipelines/watchers/<adapter-or-profile>
  execution_mode: dry_run_first
applicability:
  domains: []
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
tests/pipeline_specs/watchers/
├── test_spec_shape.py                    # PROPOSED
├── test_no_runtime_outputs.py            # PROPOSED
├── test_implementation_refs.py           # PROPOSED
├── test_source_descriptor_refs.py        # PROPOSED
├── test_cadence_and_checks.py            # PROPOSED
├── test_material_change_rules.py         # PROPOSED
├── test_no_source_admission.py           # PROPOSED
├── test_no_evidencebundle_closure.py     # PROPOSED
├── test_required_receipts.py             # PROPOSED
└── test_root_boundary.py                 # PROPOSED
```

A watcher spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, cadence assertions, change-check assertions, material-change handling, receipt requirements, and explicit no-admission/no-release posture.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- replaces the one-character `pipeline_specs/watchers/README.md` stub;
- identifies this path as shared watcher declarative configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks watcher specs from becoming executable logic, source admission, lifecycle storage, proof storage, catalog truth, release approval, or public API/UI authority;
- defines expected watcher profile families, source-change gates, cadence gates, review gates, receipts, fixtures, tests, and open questions.

Future watcher spec files are done only when they validate, point to executable watcher lanes, use stable source descriptors, declare cadence/change checks, require receipts, preserve review posture, and document downstream ingest/quarantine/no-op behavior.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-WATCH-001` | Which shared watcher spec schema is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-WATCH-002` | Which shared watcher profiles should live here versus under `pipeline_specs/<domain>/watchers/`? | NEEDS VERIFICATION |
| `PIPE-SPEC-WATCH-003` | Which source descriptor refs and source families should be activated first? | NEEDS VERIFICATION |
| `PIPE-SPEC-WATCH-004` | Which CI workflow validates shared watcher specs? | UNKNOWN |
| `PIPE-SPEC-WATCH-005` | Which MaterialChangeReport, watcher run receipt, and quarantine handoff schemas are canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-WATCH-006` | Should watcher specs be split by check type, source family, domain applicability, cadence class, or sensitivity tier? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative. Do not add executable watcher code, source clients, source descriptors, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, policy decisions, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
