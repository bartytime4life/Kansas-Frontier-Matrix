<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-local-upload-src-package-readme
title: connectors/local_upload/src/local_upload/ — Local Upload Package Boundary
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Package maintainer · Source-intake steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; package-boundary; connector-family; directory-rules-7-3; local-upload; no-network-default; fixture-safe; deny-by-default; quarantine-first; no-publication
proposed_path: connectors/local_upload/src/local_upload/README.md
truth_posture: CONFIRMED path exists / CONFIRMED doctrine-level §7.3 connector-family package path / MODULE INVENTORY NEEDS VERIFICATION
related:
  - ../../README.md
  - ../../tests/README.md
  - ../../../../docs/sources/catalog/local_upload/README.md
  - ../../../../docs/sources/catalog/local_upload.md
  - ../../../../docs/sources/catalog/local_upload/user-file-upload.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/trust-membrane.md
  - ../../../../docs/doctrine/lifecycle-law.md
  - ../../../../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../../../../data/registry/sources/
  - ../../../../data/raw/
  - ../../../../data/quarantine/
  - ../../../../fixtures/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/sources/local_upload/
  - ../../../../policy/sensitivity/
  - ../../../../policy/rights/
  - ../../../../release/
tags: [kfm, connectors, local-upload, local_upload, package, python, intake, source-admission, descriptor, validation, raw, quarantine, rights, sensitivity, provenance, governance]
notes:
  - "This README fills a blank package-boundary README under the canonical local-upload connector family."
  - "The local-upload source catalog states that `connectors/local_upload/` is named in Directory Rules §7.3 and is a highest-uncertainty trust-edge intake lane."
  - "This README describes allowed implementation responsibilities only; it does not prove parser modules, fixtures, tests, endpoint access, or CI wiring exist."
  - "Package code may only support governed source-admission helpers and RAW/QUARANTINE handoff; policy and release decisions remain outside this package."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Local Upload Package Boundary

> Implementation-boundary README for the `local_upload` package namespace under `connectors/local_upload/`. This package may support source-admission helpers only; it is **not** a truth store, release engine, public API, policy authority, source registry, or publication path.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Directory Rules: §7.3 connector" src="https://img.shields.io/badge/directory__rules-%C2%A77.3__connector-success">
  <img alt="Policy: deny by default" src="https://img.shields.io/badge/policy-deny__by__default-red">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` package README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/local_upload/src/local_upload/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `CONFIRMED` doctrine-level §7.3 connector-family package path · `NEEDS VERIFICATION` actual modules, fixtures, and CI wiring  
> **Boundary:** helper package only; no source-role upgrade, no release artifact, no public claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Allowed responsibilities](#allowed-responsibilities) · [Forbidden responsibilities](#forbidden-responsibilities) · [Expected module map](#expected-module-map) · [Evidence ledger](#evidence-ledger) · [Runtime posture](#runtime-posture) · [Validation contract](#validation-contract) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/local_upload/src/local_upload/` is the package namespace for local-upload source-admission helpers.

It may contain code for upload-event metadata, candidate descriptor preparation, content fingerprint preservation, file-shape inspection, validation helpers, quarantine disposition helpers, and RAW/QUARANTINE handoff-envelope construction.

It must not decide final source authority, rights, sensitivity, release class, publication status, catalog admission, triplet projection, or public visibility.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/local_upload/src/local_upload/` | Local-upload package namespace. | **CONFIRMED path / NEEDS VERIFICATION modules** |
| `connectors/local_upload/README.md` | Parent local-upload connector README. | **CONFIRMED** |
| `connectors/local_upload/tests/README.md` | Local-upload test-boundary README. | **CONFIRMED** |
| `docs/sources/catalog/local_upload/README.md` | Human-facing source catalog entry for local uploads. | **CONFIRMED** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside package / NEEDS VERIFICATION for entries** |
| `data/raw/` and `data/quarantine/` | Allowed handoff targets. | **Outside package** |
| `release/` | Release and publication controls. | **Out of scope for this package** |

---

## Allowed responsibilities

Package code may support:

- upload-event metadata helpers;
- candidate SourceDescriptor preparation helpers;
- content fingerprint helpers;
- content and metadata inspection helpers;
- candidate source-role preservation;
- rights-state preservation;
- sensitivity-state preservation;
- provenance and review-state preservation;
- quarantine disposition helpers;
- RAW or QUARANTINE handoff-envelope helpers;
- deterministic fail-closed errors;
- fixture-only parser and validation helpers.

---

## Forbidden responsibilities

Package code must not:

- decide source activation;
- upgrade source role without steward review;
- decide rights, sensitivity, release class, or public visibility;
- write directly to processed, catalog, triplet, published, proof, receipt, or release roots;
- emit public map, API, release, or truth claims;
- treat filename, extension, uploader claim, or model output as authoritative by itself;
- bypass SourceDescriptor, validation, EvidenceBundle, policy, release, correction, or rollback gates.

---

## Expected module map

The following module map is **PROPOSED**, not confirmed implementation:

```text
connectors/local_upload/src/local_upload/
├── README.md              # CONFIRMED — this package-boundary README
├── __init__.py            # NEEDS VERIFICATION
├── descriptors.py         # PROPOSED — SourceDescriptor preparation helpers
├── inspect.py             # PROPOSED — file-shape and metadata inspection helpers
├── fingerprints.py        # PROPOSED — content digest helpers
├── roles.py               # PROPOSED — candidate source-role helpers
├── disposition.py         # PROPOSED — RAW/QUARANTINE decision helpers
├── handoff.py             # PROPOSED — RAW/QUARANTINE envelope helpers
└── errors.py              # PROPOSED — deterministic fail-closed errors
```

Do not create these modules from this README alone; verify repo conventions, tests, and policy contracts first.

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/local_upload/src/local_upload/README.md` | **CONFIRMED** | Target package README exists and was blank before this update. | Does not prove modules, tests, or CI. |
| `connectors/local_upload/README.md` | **CONFIRMED** | Parent path is documented as a §7.3 local-upload connector family. | Does not prove implementation maturity. |
| `connectors/local_upload/tests/README.md` | **CONFIRMED** | Test posture is no-network by default, fixture-safe, and source-admission only. | Does not prove tests exist or pass. |
| `docs/sources/catalog/local_upload/README.md` | **CONFIRMED** | Catalog defines local upload as a high-uncertainty trust-edge intake lane with RAW/QUARANTINE handling. | Does not prove endpoint, fixture, or code coverage. |
| Package modules below this path | **NEEDS VERIFICATION** | This README defines expected implementation boundaries. | Actual files, behavior, and CI status remain unverified. |

---

## Runtime posture

Default runtime posture for this package:

- no publication;
- no source activation decision;
- no source-role upgrade;
- no public output;
- no direct writes beyond RAW or QUARANTINE handoff envelopes;
- deterministic failure when descriptor, rights state, sensitivity state, source role, provenance, or disposition is unresolved.

---

## Validation contract

The package should provide or support validation for:

- upload event metadata presence;
- source fingerprint presence;
- candidate SourceDescriptor preparation;
- candidate source-role preservation;
- rights-state preservation;
- sensitivity-state preservation;
- provenance and review-state preservation;
- quarantine reason preservation;
- RAW/QUARANTINE-only handoff envelopes;
- refusal to emit release/public artifacts.

Validation must be paired with tests before any implementation maturity is claimed.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify source activation, source-role upgrade, public release, rights/sensitivity bypass, direct publication, or implementation maturity without tests.

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
| Confirm SourceDescriptor and candidate-role handling. | **NEEDS VERIFICATION** | Source registry entry, code, and tests. |
| Confirm rights/sensitivity/review-state handling. | **NEEDS VERIFICATION** | Policy references, code, and tests. |
| Confirm RAW/QUARANTINE handoff envelope shape. | **NEEDS VERIFICATION** | Schemas/contracts and tests. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep this package small, deterministic, and conservative. It should preserve candidate upload evidence for governed review, not decide truth or publication.

[Back to top ↑](#top)
