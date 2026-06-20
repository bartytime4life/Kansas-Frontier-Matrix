<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-manual-curation-src-package-readme
title: connectors/manual_curation/src/manual_curation/ — Manual Curation Package Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Source steward · Docs steward · Validation steward · Rights reviewer · Sensitivity reviewer
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; package-boundary; manual-curation; steward-assisted; no-publication; quarantine-aware; implementation-depth-needs-verification
proposed_path: connectors/manual_curation/src/manual_curation/README.md
truth_posture: CONFIRMED path exists / PROPOSED package boundary / MODULE INVENTORY NEEDS VERIFICATION
related:
  - ../../README.md
  - ../../tests/README.md
  - ../../../../docs/sources/catalog/manual_curation/README.md
  - ../../../../docs/sources/catalog/manual_curation/steward-curation-workflow.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../docs/sources/source-roles.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/trust-membrane.md
  - ../../../../docs/doctrine/lifecycle-law.md
  - ../../../../docs/doctrine/truth-posture.md
  - ../../../../docs/governance/separation-of-duties.md
  - ../../../../data/registry/sources/
  - ../../../../data/raw/
  - ../../../../data/quarantine/
  - ../../../../fixtures/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/sources/
  - ../../../../policy/sensitivity/
  - ../../../../policy/rights/
  - ../../../../release/
tags: [kfm, connectors, manual-curation, package, python, steward-review, source-admission, source-descriptor, source-role, quarantine, validation, evidencebundle, rollback, governance]
notes:
  - "This README fills a blank package-boundary README under the proposed manual-curation helper lane."
  - "The manual-curation catalog README states it is methodology and steward reference, not implementation proof."
  - "This package may support steward-gate helper code only; it must not approve activation, source-role upgrade, catalog closure, or release."
  - "Package output may support RAW or QUARANTINE handoff only; policy and release decisions remain outside this package."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Manual Curation Package Boundary

> Implementation-boundary README for the `manual_curation` package namespace under `connectors/manual_curation/`. This package may support steward-assisted source-admission helpers only; it is **not** a truth store, release engine, public API, policy authority, source registry, catalog-closure authority, proof root, or publication path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Truth: module inventory needs verification" src="https://img.shields.io/badge/truth-module__inventory__needs__verification-orange">
  <img alt="Policy: cite or abstain" src="https://img.shields.io/badge/posture-cite__or__abstain-success">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` package README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/manual_curation/src/manual_curation/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` package boundary · `NEEDS VERIFICATION` actual modules, fixtures, and CI wiring  
> **Boundary:** helper package only; no source activation, no source-role upgrade, no catalog closure, no release artifact.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed responsibilities](#allowed-responsibilities) · [Forbidden responsibilities](#forbidden-responsibilities) · [Expected module map](#expected-module-map) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation contract](#validation-contract) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/manual_curation/src/manual_curation/` is the package namespace for manual-curation helper code.

It may contain helpers for candidate intake packets, descriptor-draft references, source-role review routing, rights and sensitivity routing, evidence-reference preservation, validation-defect summaries, quarantine disposition notes, correction handoff notes, rollback handoff notes, and RAW/QUARANTINE handoff-envelope preparation.

It must not decide final source authority, source activation, source-role upgrade, rights, sensitivity, catalog closure, release class, publication status, or public visibility.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/manual_curation/src/manual_curation/` | Manual-curation helper package namespace. | **CONFIRMED path / NEEDS VERIFICATION modules** |
| `connectors/manual_curation/README.md` | Parent manual-curation connector-boundary README. | **CONFIRMED** |
| `connectors/manual_curation/tests/README.md` | Manual-curation test-boundary README. | **CONFIRMED** |
| `docs/sources/catalog/manual_curation/README.md` | Manual-curation methodology and steward reference. | **CONFIRMED** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside package / NEEDS VERIFICATION for entries** |
| `data/raw/` and `data/quarantine/` | Candidate handoff targets. | **Outside package** |
| `release/` | Release and publication controls. | **Out of scope for this package** |

---

## Allowed responsibilities

Package code may support:

- candidate intake packet helpers;
- SourceDescriptor drafting support;
- SourceActivationDecision preparation support, without approval;
- source-role review routing;
- rights-state and sensitivity-state routing;
- evidence-reference preservation helpers;
- validation-defect summaries;
- quarantine-reason helpers;
- correction and rollback handoff helpers;
- RAW or QUARANTINE handoff-envelope helpers;
- deterministic fail-closed errors;
- fixture-only parser and validation helpers.

---

## Forbidden responsibilities

Package code must not:

- approve source activation;
- upgrade source role;
- decide rights, sensitivity, release class, or public visibility;
- close catalog records;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- treat AI or watcher output as approval;
- emit public claims;
- bypass SourceDescriptor, validation, EvidenceBundle, policy, release, correction, or rollback gates.

---

## Expected module map

The following module map is **PROPOSED**, not confirmed implementation:

```text
connectors/manual_curation/src/manual_curation/
├── README.md              # CONFIRMED — this package-boundary README
├── __init__.py            # NEEDS VERIFICATION
├── packets.py             # PROPOSED — candidate intake packet helpers
├── descriptors.py         # PROPOSED — descriptor-draft helpers
├── roles.py               # PROPOSED — source-role review helpers
├── review.py              # PROPOSED — steward review routing helpers
├── evidence.py            # PROPOSED — evidence-reference helpers
├── defects.py             # PROPOSED — validation-defect summaries
├── disposition.py         # PROPOSED — quarantine/review disposition helpers
├── handoff.py             # PROPOSED — RAW/QUARANTINE envelope helpers
└── errors.py              # PROPOSED — deterministic fail-closed errors
```

Do not create these modules from this README alone; verify repo conventions, tests, and policy contracts first.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/manual_curation/src/manual_curation/README.md` | **CONFIRMED** | Target package README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/manual_curation/README.md` | **CONFIRMED** | Parent README defines the helper boundary and forbids activation, source-role upgrade, catalog closure, and publication. | Does not prove implementation maturity. |
| `connectors/manual_curation/tests/README.md` | **CONFIRMED** | Test README defines gate-preserving test posture. | Does not prove tests exist or pass. |
| `docs/sources/catalog/manual_curation/README.md` | **CONFIRMED** | Manual curation is steward-led methodology, not implementation proof. | Exact workflow implementation and tooling remain unverified. |
| Package modules below this path | **NEEDS VERIFICATION** | This README defines expected implementation boundaries. | Actual files, behavior, and CI status remain unverified. |

---

## Runtime posture

Default runtime posture for this package:

- no source activation decision;
- no source-role upgrade;
- no public output;
- no catalog closure;
- no release artifact creation;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- deterministic failure when descriptor, rights, sensitivity, source role, evidence, validation, review, correction, or rollback state is unresolved.

---

## Validation contract

The package should provide or support validation for:

- descriptor or descriptor-draft reference presence;
- explicit source-role preservation;
- rights-state and sensitivity-state routing;
- evidence-reference preservation;
- validation-defect visibility;
- quarantine reason preservation;
- correction and rollback handoff preservation;
- RAW/QUARANTINE-only handoff envelopes;
- refusal to emit release, catalog-closure, or public artifacts.

Validation must be paired with tests before any implementation maturity is claimed.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify source activation, source-role upgrade, catalog closure, public release, rights/sensitivity bypass, or implementation maturity without tests.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter package-boundary note until implementation files and tests are verified.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual package module inventory. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm descriptor and source-role support. | **NEEDS VERIFICATION** | Registry entries, code, and tests. |
| Confirm rights/sensitivity/review-state routing. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this package small and gate-preserving. It should help stewards prepare reviewable curation artifacts, not approve them.

[Back to top ↑](#top)
