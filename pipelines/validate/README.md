<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-validate-readme
title: Validate Pipeline README
type: readme
version: v0.1
status: draft
owners: [<pipeline-owner>, <validation-steward>, <domain-stewards>, <evidence-steward>, <docs-steward>]
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/validate/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipelines/README.md
  - pipelines/ingest/README.md
  - pipelines/normalize/README.md
  - pipeline_specs/validate/
  - pipelines/domains/
  - tests/pipelines/validate/
  - fixtures/validate/
  - data/work/
  - data/quarantine/
  - data/processed/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
tags: [kfm, pipelines, validate, validation-report, receipts, evidence-bundle, governance]
notes:
  - "This README replaces the greenfield stub at pipelines/validate/README.md with a governed implementation-lane contract."
  - "pipelines/ is executable logic; pipeline_specs/ is declarative configuration."
  - "This lane is shared validation support, not a schema, contract, policy, data, catalog, proof, or release authority."
  - "Domain-specific validation remains under domain lanes unless an ADR says otherwise."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Validate Pipelines

> Shared executable validation lane for common KFM candidate checks, ValidationReport helpers, receipt checks, review-preflight checks, quarantine routing, and domain-validator support.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-shared%20validation-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20checks%20only-0a7ea4)
![publication](https://img.shields.io/badge/publication-no%20direct%20publish-d62728)

**Status:** Draft  
**Path:** `pipelines/validate/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Sublane:** Shared validation helpers / cross-domain validation support  
**Placement posture:** implementation sublane under `pipelines/`; exact long-term authority remains `NEEDS VERIFICATION / ADR` if this becomes a shared framework.  
**Public posture:** no direct publication; validation outputs are reports, quarantine reasons, readiness handoffs, receipts, and blocker reports only.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Anti-collapse rules](#3-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Lifecycle contract](#6-lifecycle-contract)
- [7. Required gates](#7-required-gates)
- [8. Directory contract](#8-directory-contract)
- [9. Inputs and outputs](#9-inputs-and-outputs)
- [10. Definition of done](#10-definition-of-done)
- [11. Open questions](#11-open-questions)

---

## 1. Purpose

`pipelines/validate/` is the shared executable lane for validation support that is useful across multiple KFM domain pipelines.

It may support common helpers for:

- schema and contract conformance wrappers that reference accepted schema homes;
- source descriptor and source-role checks;
- lifecycle-state and input-ref checks;
- evidence-reference readiness checks;
- review preflight checks;
- receipt and digest checks;
- quarantine reason helpers;
- processed-readiness blockers;
- no-network fixture runners;
- shared adapters used by domain-specific validation sublanes.

This directory implements or will implement the **how** of shared validation support. It does not define object meaning, define schemas, approve review state, create EvidenceBundles, write catalog truth, approve release, or serve public clients.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | Validation helpers are executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why a shared `validate/` lane? | It can hold reusable validation helpers that should not be duplicated across domain lanes. | PROPOSED / NEEDS VERIFICATION |
| Does this replace domain validators? | No. Domain-owned behavior stays under `pipelines/domains/<domain>/validate/` or an accepted domain validation sublane. | CONFIRMED boundary posture |
| Is this a schema or contract home? | No. Schemas and contracts remain in their own responsibility roots. | CONFIRMED authority separation |
| Does this write catalog or release outputs? | No. It may emit reports, quarantine reasons, receipts, and readiness handoffs only. | CONFIRMED governance posture |

> [!IMPORTANT]
> A validation pass is not EvidenceBundle closure, catalog truth, public truth, or release approval. Validation is a governed readiness check bounded by the input scope.

[⬆ Back to top](#top)

---

## 3. Anti-collapse rules

Disallowed collapses:

```text
validation pass -> public release
validation pass -> catalog truth
ValidationReport -> EvidenceBundle
schema-valid object -> approved object
receipt hash -> evidence proof
processed-readiness -> processed promotion
generated validation summary -> evidence
pipeline run -> ReleaseManifest
```

Required distinctions:

- WORK candidate, QUARANTINE record, ValidationReport, processed candidate, TransformReceipt, EvidenceBundle, catalog record, triplet projection, ReleaseManifest, CorrectionNotice, RollbackCard, and public artifact remain separate;
- source roles and domain meanings remain owned by source descriptors, contracts, schemas, and domain lanes;
- evidence readiness checks can require EvidenceBundle refs but cannot replace EvidenceBundles;
- unresolved rights, source roles, evidence, review, or representation questions fail closed.

[⬆ Back to top](#top)

---

## 4. What belongs here

Appropriate contents include:

- shared validation README files;
- fixture-only validation dry-run entrypoints;
- finite outcome helpers;
- schema/contract wrapper helpers that call accepted schema validators;
- source descriptor and source-role preservation helpers;
- EvidenceRef and EvidenceBundle readiness helpers;
- review preflight helpers;
- receipt/digest verification helpers;
- quarantine reason-code helpers;
- processed-readiness blocker builders;
- shared validator adapters used by domain lanes.

A good placement test:

> If the code helps multiple domain validators check candidate readiness without owning domain truth, it may belong here. If it only belongs to one domain, place it in that domain's validation lane. If it owns schemas, source admission, catalog truth, release decisions, or public serving, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Domain-specific validation workflows | `pipelines/domains/<domain>/validate/` |
| Ingest/source admission | `pipelines/ingest/` or domain ingest lanes |
| Normalization mappers | `pipelines/normalize/` or domain normalize lanes |
| Source access clients | `connectors/<source_id>/` or accepted connector home |
| Source descriptors | `data/registry/sources/<domain>/` or accepted registry home |
| Domain doctrine | `docs/domains/<domain>/` |
| Schemas | `schemas/contracts/v1/...` accepted schema home |
| Contracts/object meaning | `contracts/...` accepted contract home |
| Declarative validation specs | `pipeline_specs/validate/` or domain-specific spec homes |
| Fixtures | `fixtures/validate/` or domain fixture homes |
| Tests | `tests/pipelines/validate/` or domain test homes |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions | `release/...` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Lifecycle contract

Every shared validation helper must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** fixture, WORK, or approved QUARANTINE remediation refs only when a domain pipeline authorizes the call.
2. **Check** shape, source role, lifecycle state, evidence readiness, review refs, receipts, and domain-supplied invariants.
3. **Emit** ValidationReports, validation receipts, quarantine reasons, or readiness blockers.
4. **Return** to the owning domain lane for processed promotion, catalog closure, release, and public artifact decisions.
5. **Never create EvidenceBundles, write catalog records, approve release, or publish.**

[⬆ Back to top](#top)

---

## 7. Required gates

Every shared validation component must check or explicitly fail closed on:

1. **Caller ownership gate** — an owning domain pipeline or approved proof harness must provide scope.
2. **Input lifecycle gate** — input is fixture, WORK, approved QUARANTINE remediation, or approved recheck material.
3. **Schema/contract gate** — candidate shape is checked against accepted schema/contract refs.
4. **Finite outcome gate** — result is finite and reviewable.
5. **SourceDescriptor/source-role gate** — source identity, role, rights, and citation refs are carried forward.
6. **Evidence gate** — EvidenceRefs are preserved and EvidenceBundle readiness is explicit.
7. **Review gate** — unresolved required review blocks processed/public readiness.
8. **Receipt gate** — every validation invocation emits deterministic receipt/report metadata.
9. **No-direct-process gate** — validation support does not promote material to PROCESSED by itself.
10. **No-direct-catalog gate** — validation support does not write catalog/triplet records.
11. **No-direct-publish gate** — validation support does not write public UI, public API, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 8. Directory contract

Recommended shape:

```text
pipelines/validate/
├── README.md
├── VALIDATE_SHARED_CONTRACT.md        # PROPOSED
├── run_dry_fixture.py                 # PROPOSED
├── finite_outcomes.py                 # PROPOSED
├── validate_schema_contract.py        # PROPOSED
├── validate_lifecycle_state.py        # PROPOSED
├── validate_source_role.py            # PROPOSED
├── validate_evidence_refs.py          # PROPOSED
├── validate_review_state.py           # PROPOSED
├── build_validation_report.py         # PROPOSED
├── route_quarantine_reason.py         # PROPOSED
├── emit_validation_receipt.py         # PROPOSED only if not shared
└── adapters/                          # PROPOSED domain/proof adapters only
```

Declarative specs should live outside this directory:

```text
pipeline_specs/validate/<profile>.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/`, `data/quarantine/`, `data/processed/`, and `data/receipts/`, with domain-owned pipelines deciding the target domain lane.

[⬆ Back to top](#top)

---

## 9. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Shared fixture | `fixtures/validate/` or domain fixture home | Synthetic/public-safe by default. |
| Declarative spec | `pipeline_specs/validate/` or domain spec home | The what, not executable logic. |
| Candidate input | `data/work/<domain>/` or approved remediation refs | Read by stable refs only. |
| ValidationReport | `data/processed/<domain>/` or accepted validation-report home | Report/handoff only; not public. |
| QUARANTINE reason | `data/quarantine/<domain>/` | Owned by calling domain lane. |
| Receipt | `data/receipts/pipeline/<domain>/validate/` or accepted receipt home | Records inputs, checks, outcomes, hashes, and output refs. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced only; not created here. |

[⬆ Back to top](#top)

---

## 10. Definition of done

This README is done when it:

- replaces the greenfield stub at `pipelines/validate/README.md`;
- identifies this directory as a shared executable validation-support lane under `pipelines/`;
- prevents domain-specific logic, schemas, contracts, source descriptors, lifecycle data, EvidenceBundles, release decisions, public API, UI, catalog, and publication authority from being placed here;
- preserves caller scope, source-role, schema/contract, EvidenceRef, EvidenceBundle-readiness, finite-outcome, review, lifecycle, quarantine, correction, and rollback boundaries;
- blocks validation-success-as-publication, ValidationReport-as-EvidenceBundle, schema-valid-as-approved, processed-readiness-as-promotion, generated-summary-as-evidence, catalog side effects, and direct publication writes;
- gives maintainers a fixture-first, receipt-emitting, fail-closed expansion pattern.

Future executable work in this lane is done only when it has public-safe fixtures, no-network tests, caller-scope checks, input-lifecycle checks, schema/contract tests, finite-outcome tests, source-role/evidence/review tests, deterministic receipts, CI coverage, domain-steward handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 11. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-VALIDATE-001` | Is `pipelines/validate/` the final accepted home for shared validation helpers, or should this move under `packages/`, `tools/validators/`, or domain lanes by ADR? | NEEDS VERIFICATION / ADR |
| `PIPE-VALIDATE-002` | Which schema owns shared ValidationReports, validation receipts, finite outcomes, and reason codes? | NEEDS VERIFICATION |
| `PIPE-VALIDATE-003` | Should every domain validation sublane call shared helpers, or only use them for common schema/source/evidence/review checks? | NEEDS VERIFICATION |
| `PIPE-VALIDATE-004` | Which CI job owns shared validation invariant tests? | UNKNOWN |
| `PIPE-VALIDATE-005` | Which validation profiles belong in `pipeline_specs/validate/` versus domain-specific specs? | NEEDS VERIFICATION |
| `PIPE-VALIDATE-006` | Should shared validation emit complete ValidationReports directly, or only return report fragments to domain validators? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/public-safe fixtures and negative tests. Do not add live source calls, domain truth ownership, schema authority, processed-promotion shortcuts, catalog writes, public API code, UI code, release-manifest writes, published-layer writes, or generated summaries until caller scope, input lifecycle, finite outcomes, source roles, schema refs, EvidenceRef handling, review state, deterministic receipts, and rollback expectations are proven.
