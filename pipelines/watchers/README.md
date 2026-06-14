<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-watchers-readme
title: Pipeline Watchers README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-owner>
  - <watcher-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-watcher-review-gates
path: pipelines/watchers/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/ingest/README.md
  - pipeline_specs/watchers/
  - pipelines/watchers/plants/README.md
  - pipelines/domains/
  - connectors/
  - data/registry/sources/
  - data/work/
  - data/quarantine/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/
tags: [kfm, pipelines, watchers, source-change, material-change, receipts, evidence-bundle, policy, governance]
notes:
  - "This README fills the blank pipelines/watchers path as a shared executable watcher orchestration lane."
  - "Watchers observe upstream change signals and create bounded candidate records. They do not admit, normalize, validate, catalog, publish, or decide release."
  - "The pipelines root is executable pipeline logic — the how — while pipeline_specs is declarative configuration — the what."
  - "Watcher outputs are candidate evidence-development artifacts only and must flow through normal KFM gates."
  - "Concrete executable behavior, schedules, source activation, CI coverage, fixture coverage, and release wiring remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pipeline Watchers

> Shared executable watcher lane for upstream-change observation, source metadata drift checks, material-change reports, candidate work records, quarantine routing, and review handoffs — without owning connectors, source descriptors, schemas, contracts, policy decisions, lifecycle truth, EvidenceBundle truth, catalog truth, release decisions, or public API/UI behavior.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-watchers-2e7d32)
![authority](https://img.shields.io/badge/authority-change%20observation%20only-0a7ea4)
![lifecycle](https://img.shields.io/badge/lifecycle-WORK%20or%20QUARANTINE-455a64)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/watchers/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Sublane:** Shared watcher orchestration / upstream-change observation support  
**Placement posture:** implementation sublane under `pipelines/`; exact long-term authority remains `NEEDS VERIFICATION / ADR` if this becomes a shared watcher framework rather than a small orchestration lane  
**Public posture:** no direct publication; watcher outputs are material-change candidates, work records, quarantine records, receipts, and review handoffs only.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Watcher anti-collapse rules](#3-watcher-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Watcher scope](#6-watcher-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal material-change record](#11-minimal-material-change-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/watchers/` is the shared executable lane for watcher support that is useful across multiple KFM domains and source families.

It may support:

- source-head checks;
- version, date, manifest, checksum, ETag, header, and source-profile drift checks;
- source descriptor mismatch checks;
- cadence and freshness checks;
- material-change classification;
- candidate work-record creation;
- quarantine routing for unresolved or unsupported changes;
- review-handoff preparation;
- no-network watcher fixture runs;
- run receipt and material-change receipt builders;
- shared adapters used by domain-specific watcher sublanes.

This directory implements or will implement the **how** of watcher orchestration. It does not own upstream access authority, admit source material into RAW, normalize records, validate records, define SourceDescriptors, decide policy, create EvidenceBundles, write catalog truth, approve release, or publish public artifacts.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | Watcher orchestration is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why a shared `watchers/` lane? | It can hold reusable change-observation helpers and watcher sublanes that are not domain truth owners. | PROPOSED / NEEDS VERIFICATION |
| Does this replace domain pipelines? | No. Domain-owned behavior remains under `pipelines/domains/<domain>/...` or accepted domain sublanes. | CONFIRMED boundary posture |
| Is this a connector home? | No. Connectors own upstream access/staging; watchers observe change signals and prepare candidate review records. | CONFIRMED authority separation |
| Is this a registry home? | No. Source descriptors remain in accepted source registry homes. | CONFIRMED authority separation |
| Can public clients read this lane? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust-membrane posture |

> [!IMPORTANT]
> A watcher noticing change is not source admission, validation, EvidenceBundle closure, catalog truth, public truth, or release approval. Watchers create bounded, auditable candidates for later governed pipeline stages.

[⬆ Back to top](#top)

---

## 3. Watcher anti-collapse rules

Disallowed collapses:

```text
watcher event -> source admission
watcher event -> RAW capture
source changed -> published layer
material-change report -> EvidenceBundle
source-head match -> rights approval
freshness check -> validation pass
checksum change -> catalog update
watcher run -> ReleaseManifest
generated watcher summary -> evidence
```

Required distinctions:

- watcher event, connector output, source descriptor, source-intake record, RAW capture, WORK candidate, QUARANTINE record, RunReceipt, ValidationReport, EvidenceBundle, catalog record, ReleaseManifest, CorrectionNotice, RollbackCard, and public artifact remain separate;
- watcher code can observe change signals but cannot decide source authority or public fitness;
- source roles are read from governed descriptors and cannot be invented by watcher code;
- rights, citation, cadence, source-vintage, payload hash, review state, and policy state remain auditable;
- unclear source role, rights, evidence, policy, or sensitivity state fails closed.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is reusable executable watcher/change-observation support.

Appropriate contents include:

- shared watcher README files;
- fixture-only watcher dry-run entrypoints;
- source-head and freshness check helpers;
- checksum/hash/manifest/ETag/header metadata comparison helpers;
- source descriptor drift check helpers;
- material-change classifiers;
- candidate `MaterialChangeReport` builders;
- candidate `ProposedWorkRecord` builders;
- QUARANTINE reason-code helpers;
- review-handoff helpers;
- watcher receipt builders;
- shared watcher adapters used by domain lanes.

A good placement test:

> If the code helps multiple watcher lanes observe whether a source has changed and emits a candidate report or review handoff, it may belong here. If it owns upstream access authority, admits source material into RAW, owns source descriptors, owns schemas, decides policy, writes catalog truth, approves release, or serves public clients, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Domain-specific ingest/normalize/validate/catalog/publish workflows | `pipelines/domains/<domain>/...` |
| Upstream access clients | `connectors/<source_id>/` or accepted connector home |
| Source descriptors | `data/registry/sources/<domain>/` or accepted registry home |
| Domain doctrine | `docs/domains/<domain>/` |
| Schemas | `schemas/contracts/v1/...` accepted schema home |
| Contracts/object meaning | `contracts/...` accepted contract home |
| Policy | `policy/...` responsibility roots |
| Declarative watcher specs | `pipeline_specs/watchers/` or domain-specific spec homes |
| Fixtures | `fixtures/watchers/` or domain fixture homes |
| Tests | `tests/pipelines/watchers/` or domain test homes |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Lifecycle records outside governed writer scope | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| Release decisions | `release/...` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Watcher scope

| Scope area | Watcher responsibility | Failure behavior |
|---|---|---|
| Source descriptor | Read source identity, role, cadence, rights, citation, and expected freshness metadata. | Hold if missing. |
| Source signal | Compare source head, manifest, version, checksum, header, metadata, or fixture snapshot. | Record candidate or abstain. |
| Materiality | Classify whether drift appears material enough for steward review. | Emit `NEEDS_REVIEW` or `ABSTAIN`. |
| Candidate record | Emit bounded material-change report and proposed work refs. | No RAW admission. |
| Quarantine | Route unsupported or unresolved watcher signals to QUARANTINE candidates. | Fail closed. |
| Receipts | Emit deterministic watcher receipts. | Fail on missing refs/hashes. |
| Handoff | Notify or hand off to ingest/domain steward workflow. | No normalize/validate/catalog/publish side effects. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every watcher helper must preserve the KFM lifecycle:

```text
WATCHER SIGNAL -> WORK / QUARANTINE CANDIDATE -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** fixture, source descriptor, prior receipt, prior source-head, manifest, or metadata refs.
2. **Compare** recorded change signals without treating them as admitted source material.
3. **Classify** materiality and produce a candidate report or abstention.
4. **Route** unresolved or unsupported signals to QUARANTINE candidates with structured reasons.
5. **Emit** watcher receipts and review handoffs.
6. **Return** to source steward, connector, ingest, or domain lane for any later admission/normalization/validation/catalog/release action.
7. **Never admit, normalize, validate, catalog, publish, or decide release directly.**

[⬆ Back to top](#top)

---

## 8. Required gates

Every watcher component must check or explicitly fail closed on:

1. **Scope gate** — watcher id, source id, source descriptor ref, and owner are explicit.
2. **No-network fixture gate** — default tests use fixture snapshots and do not call upstream systems.
3. **SourceDescriptor gate** — source identity, source role, cadence, rights, citation, and expected freshness metadata are present.
4. **Prior-state gate** — prior hash, version, source-head, manifest, or receipt exists where comparison requires it.
5. **Materiality gate** — every detected change is classified as material, non-material, unknown, or needs review.
6. **Policy/review gate** — unresolved source-role, rights, policy, or review state becomes a hold or blocker.
7. **Receipt gate** — every watcher invocation emits deterministic inputs, checks, hashes, outcome, and handoff refs.
8. **No-direct-ingest gate** — watcher output does not admit source material into RAW.
9. **No-direct-normalize gate** — watcher output does not rewrite fields into normalized records.
10. **No-direct-validate/catalog gate** — watcher output does not emit validation pass, catalog records, or graph/triplets.
11. **No-direct-publish gate** — watcher output does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/watchers/
├── README.md
├── WATCHERS_SHARED_CONTRACT.md        # PROPOSED
├── run_dry_fixture.py                 # PROPOSED
├── check_source_head.py               # PROPOSED
├── compare_manifest.py                # PROPOSED
├── compare_checksum.py                # PROPOSED
├── classify_material_change.py        # PROPOSED
├── build_material_change_report.py    # PROPOSED
├── route_quarantine_reason.py         # PROPOSED
├── emit_watcher_receipt.py            # PROPOSED only if not shared
├── plants/                            # existing watcher sublane
└── adapters/                          # PROPOSED domain/proof adapters only
```

Declarative specs should live outside this directory:

```text
pipeline_specs/watchers/<watcher_id>.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/`, `data/quarantine/`, and `data/receipts/`, with domain-owned pipelines deciding any later lifecycle transition.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Watcher fixture | `fixtures/watchers/` or domain fixture home | Synthetic/public-safe by default. |
| Declarative spec | `pipeline_specs/watchers/` or domain spec home | The what, not executable logic. |
| Source descriptor | `data/registry/sources/<domain>/` or accepted registry home | Read-only source authority. |
| Prior state | prior receipt/source-head/manifest/checksum refs | Used for comparison only. |
| MaterialChangeReport | `data/work/<domain>/` or accepted watcher work home | Candidate record only. |
| QUARANTINE candidate | `data/quarantine/<domain>/<reason>/<run_id>/` | For unresolved or unsupported signals. |
| Receipt | `data/receipts/pipeline/watchers/<watcher_id>/` or domain receipt home | Records inputs, checks, outcomes, hashes, and handoff refs. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced only; not created here. |

[⬆ Back to top](#top)

---

## 11. Minimal material-change record

The final schema is not defined here. This example shows the minimum information a watcher output should preserve.

```yaml
schema_version: kfm.watcher.material_change.v1
watcher_run_id: watcher_run_YYYYMMDDThhmmssZ
watcher_id: <watcher_id>
status: NEEDS_REVIEW
source:
  source_id: <source_id>
  source_descriptor_ref: data/registry/sources/<domain>/<source_id>.yml
  source_role: <source_role>
comparison:
  previous_ref: null
  previous_hash: null
  current_ref: null
  current_hash: null
  changed: null
materiality:
  outcome: NEEDS_REVIEW
  reason_codes: []
checks:
  source_descriptor_resolved: false
  prior_state_resolved: false
  rights_policy_review_state_preserved: false
  no_direct_ingest: true
  no_direct_publish: true
anti_collapse:
  watcher_event_is_source_admission: false
  material_change_report_is_evidence_bundle: false
  source_changed_is_publication: false
outputs:
  material_change_report_ref: data/work/<domain>/watchers/<watcher_id>/run_YYYYMMDDThhmmssZ.yml
  quarantine_ref: null
  receipt_ref: data/receipts/pipeline/watchers/<watcher_id>/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Recommended tests:

```text
tests/pipelines/watchers/
├── test_no_network_dry_run.py              # PROPOSED
├── test_scope_required.py                  # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_prior_state_required_when_compare.py # PROPOSED
├── test_materiality_classified.py          # PROPOSED
├── test_policy_review_state_preserved.py   # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
├── test_no_direct_ingest.py                # PROPOSED
├── test_no_normalize_side_effect.py        # PROPOSED
├── test_no_validation_pass_side_effect.py  # PROPOSED
├── test_no_catalog_side_effect.py          # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors are required, prior state is required for comparison profiles, materiality is classified, review/policy state is preserved, receipts are deterministic, and no watcher run writes directly to RAW admission, normalization, validation pass state, catalog, triplet, public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Watchers may prepare material-change records, proposed work records, QUARANTINE candidates, review handoffs, and receipts. They do not publish.

Required chain:

```text
source descriptor + prior source state
  -> watcher signal comparison
  -> material-change report / abstention / quarantine candidate
  -> steward review
  -> connector or ingest action, if approved
  -> normal lifecycle pipeline
  -> ReleaseManifest
  -> RollbackCard
  -> public artifact
```

Correction and rollback posture:

- watcher runs remain auditable;
- receipts preserve source refs, prior state refs, current state refs, comparison hashes, policy refs, review refs, and failure reasons;
- watcher outputs are superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated only through governed correction/release workflows;
- rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/watchers/README.md` file;
- identifies this directory as a shared executable watcher/source-change detection support lane under `pipelines/`;
- prevents connector, ingest/source-admission, domain-specific workflow, source-profile, schema, contract, policy, fixture, test, data, proof, normalization, validation, catalog, public API, UI, and release authority from being placed here;
- preserves watcher event, source descriptor, source role, prior source state, current source state, material-change report, WORK/QUARANTINE lifecycle, receipts, correction, and rollback boundaries;
- blocks watcher-event-as-source-admission, source-change-as-publication, material-change-report-as-EvidenceBundle, generated-summary-as-evidence, RAW admission side effects, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

Future executable work in this lane is done only when it has public-safe fixtures, no-network tests, scope checks, source-descriptor/prior-state/materiality/review-policy/no-ingest/no-normalize/no-validate/no-catalog/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-WATCH-001` | Is `pipelines/watchers/` the final accepted home for shared watcher helpers, or should this move under `packages/`, `tools/`, or domain lanes by ADR? | NEEDS VERIFICATION / ADR |
| `PIPE-WATCH-002` | Which schema owns MaterialChangeReport, ProposedWorkRecord, watcher receipts, and watcher reason codes? | NEEDS VERIFICATION |
| `PIPE-WATCH-003` | Should every domain watcher sublane call shared helpers, or only use them for common source-head and materiality checks? | NEEDS VERIFICATION |
| `PIPE-WATCH-004` | Which CI job owns shared watcher invariant tests? | UNKNOWN |
| `PIPE-WATCH-005` | Which watcher profiles belong in `pipeline_specs/watchers/` versus domain-specific specs? | NEEDS VERIFICATION |
| `PIPE-WATCH-006` | Should watcher receipts live under `data/receipts/pipeline/watchers/` or under domain-specific receipt paths? | NEEDS VERIFICATION |
| `PIPE-WATCH-007` | Should watcher outputs create PRs automatically, or only emit review packets for maintainers to act on? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe fixtures and negative tests. Do not add live upstream calls, connector authority, source-profile editing, schema authority, policy authority, source admission, normalization shortcuts, validation shortcuts, catalog writes, public API code, UI code, release-manifest writes, published-layer writes, or generated summaries until source descriptors, prior-state comparisons, materiality classification, review handoff, deterministic receipts, quarantine routing, and rollback expectations are proven.
