<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-archaeology-normalize-readme
title: Archaeology Normalize Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <archaeology-pipeline-owner>
  - <archaeology-domain-steward>
  - <normalization-steward>
  - <review-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-archaeology-normalization-review-and-evidence-gates
path: pipelines/domains/archaeology/normalize/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/archaeology/README.md
  - pipelines/domains/archaeology/validate/README.md
  - pipelines/domains/archaeology/publish/README.md
  - docs/domains/archaeology/DATA_LIFECYCLE.md
  - docs/domains/archaeology/VALIDATORS.md
  - docs/domains/archaeology/OBJECT_FAMILIES.md
  - docs/domains/archaeology/CULTURAL_REVIEW.md
  - pipeline_specs/archaeology/normalize.yaml
  - contracts/domains/archaeology/
  - schemas/contracts/v1/domains/archaeology/
  - policy/domains/archaeology/
  - policy/sensitivity/archaeology/
  - data/raw/archaeology/
  - data/work/archaeology/
  - data/quarantine/archaeology/
  - data/processed/archaeology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/archaeology/
  - release/manifests/archaeology/
tags: [kfm, pipelines, domains, archaeology, normalize, transform-receipt, review, evidence-bundle, policy, governance]
notes:
  - "This README fills the blank pipelines/domains/archaeology/normalize path as a nested executable Archaeology normalization sublane."
  - "Normalization logic is executable implementation support only; it does not own source descriptors, connectors, schemas, contracts, policy, review decisions, lifecycle data, catalog truth, release decisions, or public API authority."
  - "Normalization converts admitted RAW/WORK/fixture inputs into structured WORK candidates and validation-ready records; it does not make public Archaeology truth by itself."
  - "Original fields, source roles, candidate boundaries, temporal facets, review state, TransformReceipts, EvidenceRef candidates, and public-representation state must remain auditable."
  - "Concrete executable behavior, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Normalize Pipeline

> Executable Archaeology sublane for transforming admitted RAW/WORK/fixture material into normalized, validation-ready WORK candidates while preserving source identity, source role, original fields, candidate boundaries, temporal facets, representation state, review needs, evidence refs, policy posture, quarantine reasons, correction paths, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-archaeology%20normalize-8a6d3b)
![authority](https://img.shields.io/badge/authority-normalization%20logic%20only-0a7ea4)
![posture](https://img.shields.io/badge/posture-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/domains/archaeology/normalize/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Archaeology  
**Sublane:** Normalize / WORK candidate shaping  
**Placement posture:** nested executable sublane under `pipelines/domains/archaeology/`; concrete behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; normalized outputs remain WORK candidates, quarantine records, validation inputs, and receipts until validation, EvidenceBundle, catalog/triplet, release, correction, and rollback closure.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Normalize anti-collapse rules](#3-normalize-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Normalization scope](#6-normalization-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal normalized candidate record](#11-minimal-normalized-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/archaeology/normalize/` is the executable sublane for Archaeology normalization.

It supports candidate processing for:

- admitted source captures, public-safe fixtures, normalized remediation inputs, and steward-reviewed work packets;
- object-family shaping for survey, record, candidate, model, aggregate, documentation, chronology, repository, and interpretation records;
- source-role preservation and source-vintage retention;
- original-field retention and normalized-field mapping;
- temporal normalization of observed, recorded, valid, survey, collection, accession, processing, review, release, and correction times;
- coordinate/geometry handling into internal geometry plus public-representation candidates without treating a representation as release approval;
- evidence-ref candidate preparation and digest inputs;
- transform-receipt candidate preparation for public-safe representation, aggregation, generalized surfaces, documentation carriers, and reality-boundary notes;
- quarantine records for rights uncertainty, source-role collapse, unsupported object family, missing review state, ambiguous time, schema drift, unsupported geometry, evidence gaps, or policy gaps.

This directory implements or will implement the **how** of Archaeology normalization. It does not fetch source data, admit sources, define source descriptors, define schemas, decide policy, decide review outcomes, own EvidenceBundle truth, own catalog truth, decide release, or publish public API/map payloads.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/archaeology/`? | Archaeology is a domain lane under the domain-pipeline umbrella. | CONFIRMED path pattern; behavior NEEDS VERIFICATION |
| Why `normalize/`? | This sublane transforms admitted Archaeology inputs into normalized WORK candidates. | PROPOSED / NEEDS VERIFICATION |
| Is this ingest? | No. Ingest admits captures; normalization reshapes admitted material for validation. | CONFIRMED local separation |
| Does this own schemas or policy? | No. It consumes accepted contracts, schemas, policy outcomes, and source descriptors. | CONFIRMED authority separation |
| Can this sublane publish? | No. It prepares validation-ready candidates only. | CONFIRMED governance posture |

> [!IMPORTANT]
> A normalized Archaeology record is not validated truth, catalog truth, public truth, or release approval. Normalization makes records comparable, validatable, evidence-linkable, and receipt-backed while preserving original source fields and review needs.

[⬆ Back to top](#top)

---

## 3. Normalize anti-collapse rules

Archaeology normalization must preserve source roles, candidate boundaries, representation state, evidence state, review state, and lifecycle state.

Disallowed collapses:

```text
normalized record -> accepted public truth
normalized candidate -> confirmed record
candidate signal -> confirmed site
source label -> accepted object family without evidence
coordinate transform candidate -> public-safe release
unit or date normalization -> silent edit
schema-shaped object -> validation pass
review-needed -> reviewer-approved
EvidenceRef candidate -> EvidenceBundle
generated normalization summary -> evidence
pipeline run -> release approval
```

Required distinctions:

- source capture, normalized WORK candidate, quarantine record, ValidationReport, processed object, EvidenceBundle, catalog record, release candidate, ReleaseManifest, CorrectionNotice, and RollbackCard remain separate;
- original source fields, normalized fields, mappings, method refs, and TransformReceipt candidates remain auditable;
- source role, object family, temporal facets, representation state, review state, and evidence readiness are not silently flattened;
- unresolved review, rights, source-role, evidence, policy, and representation questions fail closed;
- every downstream claim resolves evidence or abstains.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Archaeology normalization.

Appropriate contents include:

- fixture-only normalization dry-run entrypoints;
- source-to-normalized-field mappers;
- source-role and object-family preservation helpers;
- candidate-boundary shapers;
- temporal facet normalization helpers;
- geometry/public-representation candidate builders;
- transform-receipt candidate builders;
- evidence-ref and digest-input preparation helpers;
- review-state and policy-preflight preservation helpers;
- quarantine routing helpers for unresolved roles, rights, review state, geometry, evidence, time, schema drift, or unsupported object family;
- receipt emitters, if not shared;
- handoff helpers for validation and catalog workflows.

A good placement test:

> If the code transforms admitted Archaeology RAW/WORK/fixture inputs into normalized WORK candidates, quarantine records, validation-ready handoffs, or receipts, it may belong here. If it fetches from an upstream, admits source captures, defines a SourceDescriptor, decides policy, approves review, writes catalog truth, approves release, or serves public API/map output, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Upstream fetchers and API clients | `connectors/<source>` or accepted connector home |
| Ingest/source admission | `pipelines/domains/archaeology/ingest/` or accepted ingest lane |
| Validation logic | `pipelines/domains/archaeology/validate/` |
| Protective transform execution for release artifacts | redaction / publish / policy roots as applicable |
| Catalog and triplet builders | catalog sublanes and lifecycle catalog/triplet homes |
| Domain doctrine and object meaning | `docs/domains/archaeology/`, `contracts/domains/archaeology/` |
| Source descriptors / source registry entries | `data/registry/sources/archaeology/` or approved registry home |
| JSON Schemas | `schemas/contracts/v1/domains/archaeology/` or accepted schema home |
| Policy, rights, review, release rules | `policy/...` and review responsibility roots |
| Declarative run specs | `pipeline_specs/archaeology/...` |
| Fixtures | `fixtures/domains/archaeology/normalize/` or accepted fixture home |
| Tests | `tests/pipelines/domains/archaeology/normalize/` or accepted test home |
| Lifecycle outputs | `data/...` lifecycle homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Normalization scope

| Scope area | Normalize responsibility | Failure behavior |
|---|---|---|
| Source identity | Preserve source id, source role, source family, source vintage, citation refs, rights, and input hashes. | Quarantine if missing or conflicting. |
| Object family | Normalize object-family hints without upgrading candidates to confirmed truth. | Hold on ambiguity. |
| Original fields | Preserve original labels, values, dates, notes, geometry refs, repository refs, and source payload hashes. | Fail if lossy. |
| Time | Preserve observed, recorded, valid, survey, collection, processing, review, release, and correction times. | Quarantine on material collapse. |
| Representation | Prepare internal geometry and public-representation candidates without release approval. | Hold if unsafe or unsupported. |
| Review/policy | Carry review requirements and policy preflight state forward. | Hold or quarantine if missing. |
| Evidence | Carry source refs and candidate EvidenceRef inputs forward. | Abstain if unresolved. |
| Validation handoff | Emit validation-ready candidates with receipts. | No direct processed/catalog output. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Archaeology normalization run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, admitted RAW captures, WORK candidates, or QUARANTINE remediation inputs with source identity and receipts.
2. **Normalize** fields into validation-ready Archaeology candidates while preserving original source fields, source refs, source roles, object-family hints, temporal facets, representation state, rights, review requirements, and evidence refs.
3. **Prepare** deterministic identity and digest inputs without claiming validation, catalog, or release truth.
4. **Quarantine** unresolved source roles, rights, review gaps, unsupported object families, ambiguous time, representation risk, evidence gaps, policy gaps, schema drift, and malformed inputs.
5. **Emit receipts** for every normalized, rejected, quarantined, or abstained normalization action.
6. **Never publish or catalog directly.**

Normalization is a WORK-stage shaping operation. It is not source admission, validation pass, catalog closure, review approval, or release.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Archaeology normalization run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is admitted RAW, WORK, approved QUARANTINE remediation, or fixture-only material.
2. **SourceDescriptor gate** — source identity, source family, source role, rights, citation, cadence, and source vintage are present.
3. **Original-field preservation gate** — original field values, labels, temporal values, spatial refs, repository refs, and payload hashes remain recoverable.
4. **Object-family gate** — object-family mapping is explicit and does not convert candidate signals into confirmed records.
5. **Source-role gate** — record, candidate, model, aggregate, synthetic, and interpretation records remain distinct.
6. **Temporal gate** — observed, recorded, valid, survey, collection, processing, review, release, and correction times remain distinct.
7. **Representation gate** — public-representation candidates are receipt-ready and do not imply release approval.
8. **Review/policy gate** — required review and policy preflight state are carried forward or the record holds.
9. **Evidence gate** — candidate evidence refs are preserved and unresolved support abstains.
10. **Quarantine reason gate** — every denied/held record has a structured reason code and receipt.
11. **No-direct-validation gate** — normalization does not mark candidates as validation-passed.
12. **No-direct-catalog gate** — normalization does not write catalog/triplet records as a side effect.
13. **No-direct-publish gate** — normalization does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/archaeology/normalize/
├── README.md                         # this file
├── NORMALIZE_CONTRACT.md             # PROPOSED: Archaeology normalization execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/public-safe fixture only
├── normalize_source_fields.py        # PROPOSED
├── normalize_object_family.py        # PROPOSED
├── normalize_temporal_facets.py      # PROPOSED
├── normalize_representation_state.py # PROPOSED
├── prepare_evidence_refs.py          # PROPOSED
├── prepare_transform_receipts.py     # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_normalize_receipt.py         # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/archaeology/normalize.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/archaeology/`, `data/quarantine/archaeology/`, and `data/receipts/` before downstream validation, processed, catalog, release, and published-layer roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/archaeology/normalize/` or accepted fixture home | Synthetic/public-safe fixture. |
| RAW capture | `data/raw/archaeology/<source_id>/<run_id>/` | Immutable input; read only. |
| WORK input | `data/work/archaeology/<run_id>/` | Candidate from ingest or remediation. |
| Normalized WORK candidate | `data/work/archaeology/<run_id>/` | Validation-ready candidate; not processed truth. |
| QUARANTINE record | `data/quarantine/archaeology/<reason>/<run_id>/` | Failed, restricted, malformed, unresolved, or unsafe material. |
| Receipt | `data/receipts/pipeline/archaeology/normalize/<run_id>.yml` or accepted receipt home | Records inputs, normalization choices, checks, hashes, and output refs. |
| Downstream handoff | validate/catalog sublanes | Handoff only; no promotion by file move. |

[⬆ Back to top](#top)

---

## 11. Minimal normalized candidate record

The final schema is not defined here. This example shows the minimum information an Archaeology normalized candidate should preserve.

```yaml
schema_version: kfm.archaeology_normalized_candidate.v1
normalized_candidate_id: archaeology_normalized_<source_id>_<object_family>_<hash>
pipeline_id: domains.archaeology.normalize
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
source:
  source_id: <source_id>
  source_family: <source_family>
  source_role: <record|survey|candidate|model|aggregate|interpretation|synthetic>
  source_descriptor_ref: data/registry/sources/archaeology/<source_id>.yml
  source_vintage: null
  rights_state: needs_review
candidate:
  object_family: <ArchaeologyObjectFamily>
  original_labels_ref: null
  normalized_fields_ref: null
  candidate_boundary_state: needs_review
time:
  observed_time: null
  recorded_time: null
  valid_time: null
  processing_time: null
representation:
  internal_representation_ref: null
  public_representation_candidate_ref: null
  transform_receipt_candidate_ref: null
review_policy:
  review_required: true
  review_record_ref: null
  policy_preflight: ABSTAIN
evidence:
  evidence_ref_candidates: []
anti_collapse:
  normalized_is_validated_truth: false
  candidate_signal_is_confirmed_record: false
  transform_candidate_is_release_approval: false
outputs:
  work_ref: data/work/archaeology/run_YYYYMMDDThhmmssZ/normalized_candidate.yml
  quarantine_ref: null
  receipt_ref: data/receipts/pipeline/archaeology/normalize/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/public-safe, and no-network** until normalization specs, source descriptors, evidence, policy, review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/archaeology/normalize/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_original_fields_preserved.py       # PROPOSED
├── test_object_family_not_silently_upgraded.py # PROPOSED
├── test_candidate_signal_not_confirmed_record.py # PROPOSED
├── test_temporal_facets_preserved.py       # PROPOSED
├── test_representation_state_receipt_ready.py # PROPOSED
├── test_review_policy_state_preserved.py   # PROPOSED
├── test_evidence_refs_preserved.py         # PROPOSED
├── test_malformed_payload_quarantines.py   # PROPOSED
├── test_no_validation_pass_side_effect.py  # PROPOSED
├── test_no_catalog_side_effect.py          # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors and source roles are required, original fields are preserved, candidate boundaries hold, representation state is receipt-ready, review/policy state is preserved, evidence refs are carried forward, receipts are deterministic, and no run writes directly to validation pass state, catalog, triplet, public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Archaeology normalization pipelines may prepare normalized WORK candidates, quarantine records, validation handoffs, and receipts. They do not publish.

Required chain:

```text
admitted RAW / WORK / fixture input
  -> normalization checks
  -> normalized WORK candidate or QUARANTINE hold
  -> validation report
  -> EvidenceBundle closure
  -> processed Archaeology object
  -> catalog / triplet handoff
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public artifact
```

Correction and rollback posture:

- denied, abstained, malformed, restricted, stale, conflicted, and quarantined normalization runs remain auditable;
- receipts preserve source refs, source-role refs, original fields, normalized fields, object-family refs, temporal facets, representation refs, review refs, evidence refs, payload hashes, normalizer refs, and failure reasons;
- normalized candidates are superseded through governed state transitions, not hidden overwrite;
- downstream artifacts are invalidated if source refs, source-role refs, object-family refs, temporal refs, representation refs, EvidenceBundle refs, policy refs, review refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/archaeology/normalize/README.md` file;
- identifies this directory as a nested executable Archaeology normalization sublane;
- prevents connector, ingest/source-admission, source-profile, schema, contract, policy, fixture, test, data, proof, public API, UI, validation, catalog, and release authority from being placed here;
- preserves source descriptor, source role, object family, original fields, normalized fields, temporal facets, representation state, review state, EvidenceRef readiness, lifecycle, quarantine, correction, and rollback boundaries;
- blocks normalized-record-as-truth, candidate-signal-as-confirmed-record, transform-candidate-as-release-approval, generated-summary-as-evidence, validation-pass side effects, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor fixtures, no-network tests, schema-backed normalized candidates, contract conformance, source-role/original-field/object-family/time/representation/review/evidence/no-validation-pass/no-catalog/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `ARCH-NORM-001` | Should Archaeology normalization remain one sublane, or split into source-field, object-family, temporal, representation, review, and evidence-prep normalizers? | NEEDS VERIFICATION / ADR |
| `ARCH-NORM-002` | Which schema owns normalized candidates, transform receipt candidates, and quarantine reason codes? | NEEDS VERIFICATION |
| `ARCH-NORM-003` | Which fixture set should be first-wave for no-network dry runs? | NEEDS VERIFICATION |
| `ARCH-NORM-004` | Which CI job owns Archaeology normalization invariant tests? | UNKNOWN |
| `ARCH-NORM-005` | Which receipt name is canonical for public-representation candidate preparation? | NEEDS VERIFICATION |
| `ARCH-NORM-006` | Should review preflight happen during normalization, validation, or catalog closure? | NEEDS VERIFICATION |
| `ARCH-NORM-007` | How should normalization report release blockers to validation and catalog sublanes? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe fixture-only dry runs and negative tests. Do not add live source fetching, ingest authority, source-profile editing, schema authority, policy authority, review-decision authority, direct validation pass shortcuts, direct catalog writes, public API code, public UI code, release-manifest writes, public layer writes, or generated archaeology summaries until source roles, source descriptors, original-field preservation, object-family boundaries, representation state, review state, deterministic receipts, and rollback expectations are proven.
