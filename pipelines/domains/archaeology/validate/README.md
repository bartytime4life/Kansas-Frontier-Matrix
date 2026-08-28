<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-archaeology-validate-readme
title: Archaeology Validate Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <archaeology-pipeline-owner>
  - <archaeology-domain-steward>
  - <validation-steward>
  - <review-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-archaeology-validation-gates
path: pipelines/domains/archaeology/validate/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/archaeology/README.md
  - docs/domains/archaeology/DATA_LIFECYCLE.md
  - docs/domains/archaeology/VALIDATORS.md
  - pipeline_specs/archaeology/validate.yaml
  - contracts/domains/archaeology/
  - schemas/contracts/v1/domains/archaeology/
  - policy/domains/archaeology/
  - data/work/archaeology/
  - data/quarantine/archaeology/
  - data/processed/archaeology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/archaeology/
  - release/manifests/archaeology/
tags: [kfm, pipelines, domains, archaeology, validate, validation-report, evidence-bundle, policy, governance]
notes:
  - "This README fills the blank pipelines/domains/archaeology/validate path as a nested executable Archaeology validation sublane."
  - "Validation logic is executable implementation support only; it does not own source descriptors, connectors, schemas, contracts, policy, review decisions, lifecycle data, catalog truth, release decisions, or public API authority."
  - "Validators are finite-outcome, receipt-emitting, and fail closed."
  - "Concrete executable behavior, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Validate Pipeline

> Executable Archaeology sublane for validating normalized WORK candidates into `ValidationReport` outcomes, processed-candidate handoffs, quarantine records, receipts, and downstream catalog/release readiness checks while preserving source role, review state, EvidenceBundle readiness, policy outcomes, correction paths, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-archaeology%20validate-8a6d3b)
![authority](https://img.shields.io/badge/authority-validation%20logic%20only-0a7ea4)
![posture](https://img.shields.io/badge/posture-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/domains/archaeology/validate/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Archaeology  
**Sublane:** Validate / WORK-to-PROCESSED readiness  
**Placement posture:** nested executable sublane under `pipelines/domains/archaeology/`; concrete behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; validation outputs remain reports, quarantine records, processed-candidate handoffs, and receipts until EvidenceBundle, review, policy, catalog/triplet, release, correction, and rollback closure.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Validation anti-collapse rules](#3-validation-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Required gates](#6-required-gates)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Directory contract](#8-directory-contract)
- [9. Tests and receipts](#9-tests-and-receipts)
- [10. Definition of done](#10-definition-of-done)
- [11. Open questions](#11-open-questions)

---

## 1. Purpose

`pipelines/domains/archaeology/validate/` is the executable sublane for checking normalized Archaeology WORK candidates before processed/catalog handoff.

It supports:

- schema and contract conformance checks;
- source descriptor, source-role, rights, citation, source-vintage, and payload-hash checks;
- candidate-role and object-family boundary checks;
- review, policy, evidence, receipt, correction, and rollback precondition checks;
- `ValidationReport` outputs with finite outcomes;
- quarantine routing for incomplete, unsupported, stale, conflicted, or policy-blocked material;
- handoffs to processed, catalog, triplet, and release workflows without owning those decisions.

This directory implements or will implement the **how** of validation. It does not fetch source data, admit sources, normalize records, define schemas, decide policy, decide review outcomes, own EvidenceBundle truth, own catalog truth, decide release, or publish public API/map payloads.

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/archaeology/`? | Archaeology is a domain lane under the domain-pipeline umbrella. | CONFIRMED path pattern; behavior NEEDS VERIFICATION |
| Why `validate/`? | This sublane checks normalized WORK candidates before processed/catalog handoff. | PROPOSED / NEEDS VERIFICATION |
| Does this own policy or review decisions? | No. It consumes policy and review outcomes and fails closed when unresolved. | CONFIRMED authority separation |
| Can this sublane publish? | No. It prepares validation reports and handoffs only. | CONFIRMED governance posture |

> [!IMPORTANT]
> Validation pass is not publication. A passing `ValidationReport` still requires evidence closure, catalog closure, release review, correction path, and rollback target before any public surface changes.

---

## 3. Validation anti-collapse rules

Disallowed collapses:

```text
validation pass -> public release
validation pass -> confirmed truth
ValidationReport -> EvidenceBundle
EvidenceRef -> EvidenceBundle
schema-valid object -> policy-approved object
candidate signal -> confirmed record
review-needed -> reviewer-approved
catalog readiness -> catalog closure
processed handoff -> published artifact
generated validation summary -> evidence
pipeline run -> ReleaseManifest
```

Required distinctions:

- WORK candidate, ValidationReport, processed candidate, quarantine record, EvidenceBundle, ReviewRecord, PolicyDecision, catalog record, release candidate, ReleaseManifest, CorrectionNotice, and RollbackCard remain separate;
- source roles are preserved and cannot be silently upgraded;
- reviewer gaps, rights gaps, evidence gaps, and policy gaps fail closed;
- every public claim resolves evidence or abstains.

---

## 4. What belongs here

Appropriate contents include:

- fixture-only validation dry-run entrypoints;
- schema/contract checks that reference accepted schema homes;
- source descriptor, source-role, rights, citation, and source-vintage validators;
- candidate-boundary validators;
- review and policy-presence validators;
- EvidenceRef and EvidenceBundle readiness checks;
- catalog-closure readiness checks;
- quarantine reason-code routing helpers;
- `ValidationReport` builders and receipt emitters;
- handoff helpers for processed, catalog, triplet, and release workflows without owning those decisions.

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers and API clients | `connectors/<source>` or accepted connector home |
| Ingest/source admission | `pipelines/domains/archaeology/ingest/` or accepted ingest lane |
| Normalization mappers | `pipelines/domains/archaeology/normalize/` or accepted normalize lane |
| Catalog and triplet builders | catalog sublanes and lifecycle catalog/triplet homes |
| Domain doctrine and object meaning | `docs/domains/archaeology/`, `contracts/domains/archaeology/` |
| JSON Schemas | `schemas/contracts/v1/domains/archaeology/` or accepted schema home |
| Policy, rights, review, and release rules | `policy/...` and review responsibility roots |
| Fixtures | `fixtures/domains/archaeology/validate/` or accepted fixture home |
| Tests | `tests/pipelines/domains/archaeology/validate/` or accepted test home |
| Lifecycle outputs | `data/...` lifecycle homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

---

## 6. Required gates

Every validation run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is normalized WORK, approved QUARANTINE remediation, or fixture-only material.
2. **SourceDescriptor gate** — source identity, source family, source role, rights, citation, cadence, and source vintage are present.
3. **Schema/contract gate** — candidate validates against the accepted Archaeology contract shape.
4. **Finite outcome gate** — validator outcome is one of `PASS`, `DENY`, `ABSTAIN`, `ERROR`, or `NEEDS_REVIEW`.
5. **Source-role gate** — record, candidate, model, aggregate, synthetic, and interpretation records remain distinct.
6. **Evidence gate** — claim-bearing candidates resolve EvidenceRef/EvidenceBundle preconditions or abstain.
7. **Policy/review gate** — finite policy outcome and required review state exist; no silent allow.
8. **Receipt gate** — every validation invocation emits a deterministic `ValidationReport`.
9. **No-direct-catalog gate** — validation does not write catalog/triplet records as a side effect.
10. **No-direct-publish gate** — validation does not write public UI, public API, published layers, or release manifests.

---

## 7. Lifecycle contract

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Validation is the WORK-to-PROCESSED readiness gate. It reads normalized WORK candidates, emits `ValidationReport` outcomes and receipts, routes unresolved material to QUARANTINE, and prepares processed-candidate handoffs only when validation closes. It is not catalog closure, release approval, or public serving.

---

## 8. Directory contract

Recommended shape:

```text
pipelines/domains/archaeology/validate/
├── README.md
├── VALIDATE_CONTRACT.md              # PROPOSED
├── run_dry_fixture.py                # PROPOSED
├── validate_all.py                   # PROPOSED wrapper/adapter
├── validate_schema_contract.py       # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_review_policy.py         # PROPOSED
├── validate_evidence_bundle.py       # PROPOSED
├── validate_catalog_readiness.py     # PROPOSED
├── build_validation_report.py        # PROPOSED
├── route_quarantine.py               # PROPOSED
└── emit_validation_receipt.py        # PROPOSED
```

Declarative specs should live outside this directory:

```text
pipeline_specs/archaeology/validate.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/archaeology/`, `data/quarantine/archaeology/`, `data/processed/archaeology/`, and `data/receipts/` before downstream catalog, release, and published-layer roots.

---

## 9. Tests and receipts

Default execution is **fixture-only, synthetic/public-safe, and no-network** until validation specs, source descriptors, evidence, policy, reviewer, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/archaeology/validate/
├── test_no_network_dry_run.py
├── test_source_descriptor_required.py
├── test_schema_contract_required.py
├── test_source_role_preserved.py
├── test_review_policy_required.py
├── test_evidence_bundle_required.py
├── test_catalog_closure_readiness.py
├── test_receipt_hashes.py
├── test_policy_parity.py
└── test_no_direct_publish.py
```

A dry run should prove fixtures load without network access, all validators emit receipts, finite outcomes are used, policy parity is preserved, EvidenceBundle readiness is explicit, and no run writes directly to catalog, triplet, public UI, public API, published layers, or release manifests.

---

## 10. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/archaeology/validate/README.md` file;
- identifies this directory as a nested executable Archaeology validation sublane;
- prevents connector, source-admission, normalization, source-profile, schema, contract, policy, review-decision, fixture, test, data, proof, public API, UI, catalog, and release authority from being placed here;
- preserves source descriptor, source role, object family, candidate boundary, review, EvidenceRef/EvidenceBundle readiness, policy state, lifecycle, quarantine, correction, and rollback boundaries;
- blocks validation-pass-as-publication, ValidationReport-as-EvidenceBundle, schema-valid-as-policy-approved, candidate-signal-as-confirmed-record, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

---

## 11. Open questions

| ID | Question | Status |
|---|---|---|
| `ARCH-VAL-001` | Should Archaeology validation remain one sublane, or split into source-role, evidence, review, catalog-closure, and AI-surface validators? | NEEDS VERIFICATION / ADR |
| `ARCH-VAL-002` | Which schema owns `ValidationReport`, finite outcomes, validator reason codes, and validation receipts? | NEEDS VERIFICATION |
| `ARCH-VAL-003` | Should this sublane wrap the canonical `validate_all.py` entrypoint or host domain-specific adapters only? | NEEDS VERIFICATION |
| `ARCH-VAL-004` | Which CI job owns Archaeology validation invariant tests and policy parity tests? | UNKNOWN |
| `ARCH-VAL-005` | How should validation report release blockers be shared with catalog and release sublanes? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe fixture-only dry runs and negative tests. Do not add live source fetching, ingest authority, normalization authority, source-profile editing, schema authority, policy authority, review-decision authority, direct catalog writes, direct public API code, direct UI code, release-manifest writes, public layer writes, or generated archaeology summaries until source roles, source descriptors, schema/contract checks, finite outcomes, EvidenceBundle handling, policy review, deterministic receipts, and rollback expectations are proven.
